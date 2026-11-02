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

import google.api.httpbody_pb2 as httpbody_pb2  # type: ignore
import google.api_core
import google.auth  # type: ignore
import google.protobuf
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.managedkafka_schemaregistry_v1 import gapic_version as package_version
from google.cloud.managedkafka_schemaregistry_v1.types import (
    schema_registry,
    schema_registry_resources,
)
from google.cloud.managedkafka_schemaregistry_v1.types import (
    schema_registry as gcms_schema_registry,
)

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class ManagedSchemaRegistryTransport(abc.ABC):
    """Abstract transport class for ManagedSchemaRegistry."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "managedkafka.googleapis.com"

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
                 The hostname to connect to (default: 'managedkafka.googleapis.com').
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
            self.get_schema_registry: gapic_v1.method.wrap_method(
                self.get_schema_registry,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_schema_registries: gapic_v1.method.wrap_method(
                self.list_schema_registries,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_schema_registry: gapic_v1.method.wrap_method(
                self.create_schema_registry,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_schema_registry: gapic_v1.method.wrap_method(
                self.delete_schema_registry,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_context: gapic_v1.method.wrap_method(
                self.get_context,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_contexts: gapic_v1.method.wrap_method(
                self.list_contexts,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_schema: gapic_v1.method.wrap_method(
                self.get_schema,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_raw_schema: gapic_v1.method.wrap_method(
                self.get_raw_schema,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_schema_versions: gapic_v1.method.wrap_method(
                self.list_schema_versions,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_schema_types: gapic_v1.method.wrap_method(
                self.list_schema_types,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_subjects: gapic_v1.method.wrap_method(
                self.list_subjects,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_subjects_by_schema_id: gapic_v1.method.wrap_method(
                self.list_subjects_by_schema_id,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_subject: gapic_v1.method.wrap_method(
                self.delete_subject,
                default_timeout=None,
                client_info=client_info,
            ),
            self.lookup_version: gapic_v1.method.wrap_method(
                self.lookup_version,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_version: gapic_v1.method.wrap_method(
                self.get_version,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_raw_schema_version: gapic_v1.method.wrap_method(
                self.get_raw_schema_version,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_versions: gapic_v1.method.wrap_method(
                self.list_versions,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_version: gapic_v1.method.wrap_method(
                self.create_version,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_version: gapic_v1.method.wrap_method(
                self.delete_version,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_referenced_schemas: gapic_v1.method.wrap_method(
                self.list_referenced_schemas,
                default_timeout=None,
                client_info=client_info,
            ),
            self.check_compatibility: gapic_v1.method.wrap_method(
                self.check_compatibility,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_schema_config: gapic_v1.method.wrap_method(
                self.get_schema_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_schema_config: gapic_v1.method.wrap_method(
                self.update_schema_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_schema_config: gapic_v1.method.wrap_method(
                self.delete_schema_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_schema_mode: gapic_v1.method.wrap_method(
                self.get_schema_mode,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_schema_mode: gapic_v1.method.wrap_method(
                self.update_schema_mode,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_schema_mode: gapic_v1.method.wrap_method(
                self.delete_schema_mode,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_location: gapic_v1.method.wrap_method(
                self.get_location,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_locations: gapic_v1.method.wrap_method(
                self.list_locations,
                default_timeout=None,
                client_info=client_info,
            ),
            self.cancel_operation: gapic_v1.method.wrap_method(
                self.cancel_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_operation: gapic_v1.method.wrap_method(
                self.delete_operation,
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
    def get_schema_registry(
        self,
    ) -> Callable[
        [schema_registry.GetSchemaRegistryRequest],
        Union[
            schema_registry_resources.SchemaRegistry,
            Awaitable[schema_registry_resources.SchemaRegistry],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_schema_registries(
        self,
    ) -> Callable[
        [schema_registry.ListSchemaRegistriesRequest],
        Union[
            schema_registry.ListSchemaRegistriesResponse,
            Awaitable[schema_registry.ListSchemaRegistriesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_schema_registry(
        self,
    ) -> Callable[
        [gcms_schema_registry.CreateSchemaRegistryRequest],
        Union[
            schema_registry_resources.SchemaRegistry,
            Awaitable[schema_registry_resources.SchemaRegistry],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_schema_registry(
        self,
    ) -> Callable[
        [schema_registry.DeleteSchemaRegistryRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def get_context(
        self,
    ) -> Callable[
        [schema_registry.GetContextRequest],
        Union[
            schema_registry_resources.Context,
            Awaitable[schema_registry_resources.Context],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_contexts(
        self,
    ) -> Callable[
        [schema_registry.ListContextsRequest],
        Union[httpbody_pb2.HttpBody, Awaitable[httpbody_pb2.HttpBody]],
    ]:
        raise NotImplementedError()

    @property
    def get_schema(
        self,
    ) -> Callable[
        [schema_registry.GetSchemaRequest],
        Union[
            schema_registry_resources.Schema,
            Awaitable[schema_registry_resources.Schema],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_raw_schema(
        self,
    ) -> Callable[
        [schema_registry.GetSchemaRequest],
        Union[httpbody_pb2.HttpBody, Awaitable[httpbody_pb2.HttpBody]],
    ]:
        raise NotImplementedError()

    @property
    def list_schema_versions(
        self,
    ) -> Callable[
        [schema_registry.ListSchemaVersionsRequest],
        Union[httpbody_pb2.HttpBody, Awaitable[httpbody_pb2.HttpBody]],
    ]:
        raise NotImplementedError()

    @property
    def list_schema_types(
        self,
    ) -> Callable[
        [schema_registry.ListSchemaTypesRequest],
        Union[httpbody_pb2.HttpBody, Awaitable[httpbody_pb2.HttpBody]],
    ]:
        raise NotImplementedError()

    @property
    def list_subjects(
        self,
    ) -> Callable[
        [schema_registry.ListSubjectsRequest],
        Union[httpbody_pb2.HttpBody, Awaitable[httpbody_pb2.HttpBody]],
    ]:
        raise NotImplementedError()

    @property
    def list_subjects_by_schema_id(
        self,
    ) -> Callable[
        [schema_registry.ListSubjectsBySchemaIdRequest],
        Union[httpbody_pb2.HttpBody, Awaitable[httpbody_pb2.HttpBody]],
    ]:
        raise NotImplementedError()

    @property
    def delete_subject(
        self,
    ) -> Callable[
        [schema_registry.DeleteSubjectRequest],
        Union[httpbody_pb2.HttpBody, Awaitable[httpbody_pb2.HttpBody]],
    ]:
        raise NotImplementedError()

    @property
    def lookup_version(
        self,
    ) -> Callable[
        [schema_registry.LookupVersionRequest],
        Union[
            schema_registry_resources.SchemaVersion,
            Awaitable[schema_registry_resources.SchemaVersion],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_version(
        self,
    ) -> Callable[
        [schema_registry.GetVersionRequest],
        Union[
            schema_registry_resources.SchemaVersion,
            Awaitable[schema_registry_resources.SchemaVersion],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_raw_schema_version(
        self,
    ) -> Callable[
        [schema_registry.GetVersionRequest],
        Union[httpbody_pb2.HttpBody, Awaitable[httpbody_pb2.HttpBody]],
    ]:
        raise NotImplementedError()

    @property
    def list_versions(
        self,
    ) -> Callable[
        [schema_registry.ListVersionsRequest],
        Union[httpbody_pb2.HttpBody, Awaitable[httpbody_pb2.HttpBody]],
    ]:
        raise NotImplementedError()

    @property
    def create_version(
        self,
    ) -> Callable[
        [schema_registry.CreateVersionRequest],
        Union[
            schema_registry.CreateVersionResponse,
            Awaitable[schema_registry.CreateVersionResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_version(
        self,
    ) -> Callable[
        [schema_registry.DeleteVersionRequest],
        Union[httpbody_pb2.HttpBody, Awaitable[httpbody_pb2.HttpBody]],
    ]:
        raise NotImplementedError()

    @property
    def list_referenced_schemas(
        self,
    ) -> Callable[
        [schema_registry.ListReferencedSchemasRequest],
        Union[httpbody_pb2.HttpBody, Awaitable[httpbody_pb2.HttpBody]],
    ]:
        raise NotImplementedError()

    @property
    def check_compatibility(
        self,
    ) -> Callable[
        [schema_registry.CheckCompatibilityRequest],
        Union[
            schema_registry.CheckCompatibilityResponse,
            Awaitable[schema_registry.CheckCompatibilityResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_schema_config(
        self,
    ) -> Callable[
        [schema_registry.GetSchemaConfigRequest],
        Union[
            schema_registry_resources.SchemaConfig,
            Awaitable[schema_registry_resources.SchemaConfig],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_schema_config(
        self,
    ) -> Callable[
        [schema_registry.UpdateSchemaConfigRequest],
        Union[
            schema_registry_resources.SchemaConfig,
            Awaitable[schema_registry_resources.SchemaConfig],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_schema_config(
        self,
    ) -> Callable[
        [schema_registry.DeleteSchemaConfigRequest],
        Union[
            schema_registry_resources.SchemaConfig,
            Awaitable[schema_registry_resources.SchemaConfig],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_schema_mode(
        self,
    ) -> Callable[
        [schema_registry.GetSchemaModeRequest],
        Union[
            schema_registry_resources.SchemaMode,
            Awaitable[schema_registry_resources.SchemaMode],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_schema_mode(
        self,
    ) -> Callable[
        [schema_registry.UpdateSchemaModeRequest],
        Union[
            schema_registry_resources.SchemaMode,
            Awaitable[schema_registry_resources.SchemaMode],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_schema_mode(
        self,
    ) -> Callable[
        [schema_registry.DeleteSchemaModeRequest],
        Union[
            schema_registry_resources.SchemaMode,
            Awaitable[schema_registry_resources.SchemaMode],
        ],
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


__all__ = ("ManagedSchemaRegistryTransport",)
