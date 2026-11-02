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

from google.cloud.artifactregistry_v1 import gapic_version as package_version
from google.cloud.artifactregistry_v1._compat import (
    ASYNC_WRAP_METHOD_SUPPORTS_KIND as _ASYNC_WRAP_METHOD_SUPPORTS_KIND,
)
from google.cloud.artifactregistry_v1._compat import (
    WRAP_METHOD_SUPPORTS_TRACING as _WRAP_METHOD_SUPPORTS_TRACING,
)

_ASYNC_WRAP_METHOD_SUPPORTS_TRACING = _WRAP_METHOD_SUPPORTS_TRACING
_WRAP_METHOD_SUPPORTS_KIND = _WRAP_METHOD_SUPPORTS_TRACING

import google.api_core
import google.auth  # type: ignore
import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
import google.iam.v1.policy_pb2 as policy_pb2  # type: ignore
import google.protobuf
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
from google.api_core import client_options as client_options_lib
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, operations_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.artifactregistry_v1.types import (
    apt_artifact,
    artifact,
    attachment,
    export,
    file,
    package,
    repository,
    rule,
    settings,
    tag,
    version,
    vpcsc_config,
    yum_artifact,
)
from google.cloud.artifactregistry_v1.types import attachment as gda_attachment
from google.cloud.artifactregistry_v1.types import file as gda_file
from google.cloud.artifactregistry_v1.types import package as gda_package
from google.cloud.artifactregistry_v1.types import repository as gda_repository
from google.cloud.artifactregistry_v1.types import rule as gda_rule
from google.cloud.artifactregistry_v1.types import tag as gda_tag
from google.cloud.artifactregistry_v1.types import version as gda_version
from google.cloud.artifactregistry_v1.types import vpcsc_config as gda_vpcsc_config

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class ArtifactRegistryTransport(abc.ABC):
    """Abstract transport class for ArtifactRegistry."""

    AUTH_SCOPES = (
        "https://www.googleapis.com/auth/cloud-platform",
        "https://www.googleapis.com/auth/cloud-platform.read-only",
    )

    DEFAULT_HOST: str = "artifactregistry.googleapis.com"

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
                 The hostname to connect to (default: 'artifactregistry.googleapis.com').
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
            self.list_docker_images: self._wrap_method(
                self.list_docker_images,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/ListDockerImages",
            ),
            self.get_docker_image: self._wrap_method(
                self.get_docker_image,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/GetDockerImage",
            ),
            self.list_maven_artifacts: self._wrap_method(
                self.list_maven_artifacts,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/ListMavenArtifacts",
            ),
            self.get_maven_artifact: self._wrap_method(
                self.get_maven_artifact,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/GetMavenArtifact",
            ),
            self.list_npm_packages: self._wrap_method(
                self.list_npm_packages,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/ListNpmPackages",
            ),
            self.get_npm_package: self._wrap_method(
                self.get_npm_package,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/GetNpmPackage",
            ),
            self.list_python_packages: self._wrap_method(
                self.list_python_packages,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/ListPythonPackages",
            ),
            self.get_python_package: self._wrap_method(
                self.get_python_package,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/GetPythonPackage",
            ),
            self.import_apt_artifacts: self._wrap_method(
                self.import_apt_artifacts,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/ImportAptArtifacts",
            ),
            self.import_yum_artifacts: self._wrap_method(
                self.import_yum_artifacts,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/ImportYumArtifacts",
            ),
            self.list_repositories: self._wrap_method(
                self.list_repositories,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/ListRepositories",
            ),
            self.get_repository: self._wrap_method(
                self.get_repository,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/GetRepository",
            ),
            self.create_repository: self._wrap_method(
                self.create_repository,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/CreateRepository",
            ),
            self.update_repository: self._wrap_method(
                self.update_repository,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/UpdateRepository",
            ),
            self.delete_repository: self._wrap_method(
                self.delete_repository,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/DeleteRepository",
            ),
            self.list_packages: self._wrap_method(
                self.list_packages,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/ListPackages",
            ),
            self.get_package: self._wrap_method(
                self.get_package,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/GetPackage",
            ),
            self.delete_package: self._wrap_method(
                self.delete_package,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/DeletePackage",
            ),
            self.list_versions: self._wrap_method(
                self.list_versions,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/ListVersions",
            ),
            self.get_version: self._wrap_method(
                self.get_version,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/GetVersion",
            ),
            self.delete_version: self._wrap_method(
                self.delete_version,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/DeleteVersion",
            ),
            self.batch_delete_versions: self._wrap_method(
                self.batch_delete_versions,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/BatchDeleteVersions",
            ),
            self.update_version: self._wrap_method(
                self.update_version,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/UpdateVersion",
            ),
            self.list_files: self._wrap_method(
                self.list_files,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/ListFiles",
            ),
            self.get_file: self._wrap_method(
                self.get_file,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/GetFile",
            ),
            self.delete_file: self._wrap_method(
                self.delete_file,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/DeleteFile",
            ),
            self.update_file: self._wrap_method(
                self.update_file,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/UpdateFile",
            ),
            self.list_tags: self._wrap_method(
                self.list_tags,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/ListTags",
            ),
            self.get_tag: self._wrap_method(
                self.get_tag,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/GetTag",
            ),
            self.create_tag: self._wrap_method(
                self.create_tag,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/CreateTag",
            ),
            self.update_tag: self._wrap_method(
                self.update_tag,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/UpdateTag",
            ),
            self.delete_tag: self._wrap_method(
                self.delete_tag,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/DeleteTag",
            ),
            self.create_rule: self._wrap_method(
                self.create_rule,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/CreateRule",
            ),
            self.list_rules: self._wrap_method(
                self.list_rules,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/ListRules",
            ),
            self.get_rule: self._wrap_method(
                self.get_rule,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/GetRule",
            ),
            self.update_rule: self._wrap_method(
                self.update_rule,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/UpdateRule",
            ),
            self.delete_rule: self._wrap_method(
                self.delete_rule,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/DeleteRule",
            ),
            self.set_iam_policy: self._wrap_method(
                self.set_iam_policy,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/SetIamPolicy",
            ),
            self.get_iam_policy: self._wrap_method(
                self.get_iam_policy,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/GetIamPolicy",
            ),
            self.test_iam_permissions: self._wrap_method(
                self.test_iam_permissions,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/TestIamPermissions",
            ),
            self.get_project_settings: self._wrap_method(
                self.get_project_settings,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/GetProjectSettings",
            ),
            self.update_project_settings: self._wrap_method(
                self.update_project_settings,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/UpdateProjectSettings",
            ),
            self.get_vpcsc_config: self._wrap_method(
                self.get_vpcsc_config,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/GetVPCSCConfig",
            ),
            self.update_vpcsc_config: self._wrap_method(
                self.update_vpcsc_config,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/UpdateVPCSCConfig",
            ),
            self.update_package: self._wrap_method(
                self.update_package,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/UpdatePackage",
            ),
            self.list_attachments: self._wrap_method(
                self.list_attachments,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/ListAttachments",
            ),
            self.get_attachment: self._wrap_method(
                self.get_attachment,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/GetAttachment",
            ),
            self.create_attachment: self._wrap_method(
                self.create_attachment,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/CreateAttachment",
            ),
            self.delete_attachment: self._wrap_method(
                self.delete_attachment,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/DeleteAttachment",
            ),
            self.export_artifact: self._wrap_method(
                self.export_artifact,
                default_timeout=None,
                client_info=client_info,
                method_name="google.devtools.artifactregistry.v1.ArtifactRegistry/ExportArtifact",
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
            self.get_operation: self._wrap_method(
                self.get_operation,
                default_timeout=None,
                client_info=client_info,
                method_name="google.longrunning.Operations/GetOperation",
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
    def list_docker_images(
        self,
    ) -> Callable[
        [artifact.ListDockerImagesRequest],
        Union[
            artifact.ListDockerImagesResponse,
            Awaitable[artifact.ListDockerImagesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_docker_image(
        self,
    ) -> Callable[
        [artifact.GetDockerImageRequest],
        Union[artifact.DockerImage, Awaitable[artifact.DockerImage]],
    ]:
        raise NotImplementedError()

    @property
    def list_maven_artifacts(
        self,
    ) -> Callable[
        [artifact.ListMavenArtifactsRequest],
        Union[
            artifact.ListMavenArtifactsResponse,
            Awaitable[artifact.ListMavenArtifactsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_maven_artifact(
        self,
    ) -> Callable[
        [artifact.GetMavenArtifactRequest],
        Union[artifact.MavenArtifact, Awaitable[artifact.MavenArtifact]],
    ]:
        raise NotImplementedError()

    @property
    def list_npm_packages(
        self,
    ) -> Callable[
        [artifact.ListNpmPackagesRequest],
        Union[
            artifact.ListNpmPackagesResponse,
            Awaitable[artifact.ListNpmPackagesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_npm_package(
        self,
    ) -> Callable[
        [artifact.GetNpmPackageRequest],
        Union[artifact.NpmPackage, Awaitable[artifact.NpmPackage]],
    ]:
        raise NotImplementedError()

    @property
    def list_python_packages(
        self,
    ) -> Callable[
        [artifact.ListPythonPackagesRequest],
        Union[
            artifact.ListPythonPackagesResponse,
            Awaitable[artifact.ListPythonPackagesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_python_package(
        self,
    ) -> Callable[
        [artifact.GetPythonPackageRequest],
        Union[artifact.PythonPackage, Awaitable[artifact.PythonPackage]],
    ]:
        raise NotImplementedError()

    @property
    def import_apt_artifacts(
        self,
    ) -> Callable[
        [apt_artifact.ImportAptArtifactsRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def import_yum_artifacts(
        self,
    ) -> Callable[
        [yum_artifact.ImportYumArtifactsRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_repositories(
        self,
    ) -> Callable[
        [repository.ListRepositoriesRequest],
        Union[
            repository.ListRepositoriesResponse,
            Awaitable[repository.ListRepositoriesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_repository(
        self,
    ) -> Callable[
        [repository.GetRepositoryRequest],
        Union[repository.Repository, Awaitable[repository.Repository]],
    ]:
        raise NotImplementedError()

    @property
    def create_repository(
        self,
    ) -> Callable[
        [gda_repository.CreateRepositoryRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_repository(
        self,
    ) -> Callable[
        [gda_repository.UpdateRepositoryRequest],
        Union[gda_repository.Repository, Awaitable[gda_repository.Repository]],
    ]:
        raise NotImplementedError()

    @property
    def delete_repository(
        self,
    ) -> Callable[
        [repository.DeleteRepositoryRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_packages(
        self,
    ) -> Callable[
        [package.ListPackagesRequest],
        Union[package.ListPackagesResponse, Awaitable[package.ListPackagesResponse]],
    ]:
        raise NotImplementedError()

    @property
    def get_package(
        self,
    ) -> Callable[
        [package.GetPackageRequest], Union[package.Package, Awaitable[package.Package]]
    ]:
        raise NotImplementedError()

    @property
    def delete_package(
        self,
    ) -> Callable[
        [package.DeletePackageRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_versions(
        self,
    ) -> Callable[
        [version.ListVersionsRequest],
        Union[version.ListVersionsResponse, Awaitable[version.ListVersionsResponse]],
    ]:
        raise NotImplementedError()

    @property
    def get_version(
        self,
    ) -> Callable[
        [version.GetVersionRequest], Union[version.Version, Awaitable[version.Version]]
    ]:
        raise NotImplementedError()

    @property
    def delete_version(
        self,
    ) -> Callable[
        [version.DeleteVersionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def batch_delete_versions(
        self,
    ) -> Callable[
        [version.BatchDeleteVersionsRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_version(
        self,
    ) -> Callable[
        [gda_version.UpdateVersionRequest],
        Union[gda_version.Version, Awaitable[gda_version.Version]],
    ]:
        raise NotImplementedError()

    @property
    def list_files(
        self,
    ) -> Callable[
        [file.ListFilesRequest],
        Union[file.ListFilesResponse, Awaitable[file.ListFilesResponse]],
    ]:
        raise NotImplementedError()

    @property
    def get_file(
        self,
    ) -> Callable[[file.GetFileRequest], Union[file.File, Awaitable[file.File]]]:
        raise NotImplementedError()

    @property
    def delete_file(
        self,
    ) -> Callable[
        [file.DeleteFileRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_file(
        self,
    ) -> Callable[
        [gda_file.UpdateFileRequest], Union[gda_file.File, Awaitable[gda_file.File]]
    ]:
        raise NotImplementedError()

    @property
    def list_tags(
        self,
    ) -> Callable[
        [tag.ListTagsRequest],
        Union[tag.ListTagsResponse, Awaitable[tag.ListTagsResponse]],
    ]:
        raise NotImplementedError()

    @property
    def get_tag(
        self,
    ) -> Callable[[tag.GetTagRequest], Union[tag.Tag, Awaitable[tag.Tag]]]:
        raise NotImplementedError()

    @property
    def create_tag(
        self,
    ) -> Callable[
        [gda_tag.CreateTagRequest], Union[gda_tag.Tag, Awaitable[gda_tag.Tag]]
    ]:
        raise NotImplementedError()

    @property
    def update_tag(
        self,
    ) -> Callable[
        [gda_tag.UpdateTagRequest], Union[gda_tag.Tag, Awaitable[gda_tag.Tag]]
    ]:
        raise NotImplementedError()

    @property
    def delete_tag(
        self,
    ) -> Callable[
        [tag.DeleteTagRequest], Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]]
    ]:
        raise NotImplementedError()

    @property
    def create_rule(
        self,
    ) -> Callable[
        [gda_rule.CreateRuleRequest], Union[gda_rule.Rule, Awaitable[gda_rule.Rule]]
    ]:
        raise NotImplementedError()

    @property
    def list_rules(
        self,
    ) -> Callable[
        [rule.ListRulesRequest],
        Union[rule.ListRulesResponse, Awaitable[rule.ListRulesResponse]],
    ]:
        raise NotImplementedError()

    @property
    def get_rule(
        self,
    ) -> Callable[[rule.GetRuleRequest], Union[rule.Rule, Awaitable[rule.Rule]]]:
        raise NotImplementedError()

    @property
    def update_rule(
        self,
    ) -> Callable[
        [gda_rule.UpdateRuleRequest], Union[gda_rule.Rule, Awaitable[gda_rule.Rule]]
    ]:
        raise NotImplementedError()

    @property
    def delete_rule(
        self,
    ) -> Callable[
        [rule.DeleteRuleRequest], Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]]
    ]:
        raise NotImplementedError()

    @property
    def set_iam_policy(
        self,
    ) -> Callable[
        [iam_policy_pb2.SetIamPolicyRequest],
        Union[policy_pb2.Policy, Awaitable[policy_pb2.Policy]],
    ]:
        raise NotImplementedError()

    @property
    def get_iam_policy(
        self,
    ) -> Callable[
        [iam_policy_pb2.GetIamPolicyRequest],
        Union[policy_pb2.Policy, Awaitable[policy_pb2.Policy]],
    ]:
        raise NotImplementedError()

    @property
    def test_iam_permissions(
        self,
    ) -> Callable[
        [iam_policy_pb2.TestIamPermissionsRequest],
        Union[
            iam_policy_pb2.TestIamPermissionsResponse,
            Awaitable[iam_policy_pb2.TestIamPermissionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_project_settings(
        self,
    ) -> Callable[
        [settings.GetProjectSettingsRequest],
        Union[settings.ProjectSettings, Awaitable[settings.ProjectSettings]],
    ]:
        raise NotImplementedError()

    @property
    def update_project_settings(
        self,
    ) -> Callable[
        [settings.UpdateProjectSettingsRequest],
        Union[settings.ProjectSettings, Awaitable[settings.ProjectSettings]],
    ]:
        raise NotImplementedError()

    @property
    def get_vpcsc_config(
        self,
    ) -> Callable[
        [vpcsc_config.GetVPCSCConfigRequest],
        Union[vpcsc_config.VPCSCConfig, Awaitable[vpcsc_config.VPCSCConfig]],
    ]:
        raise NotImplementedError()

    @property
    def update_vpcsc_config(
        self,
    ) -> Callable[
        [gda_vpcsc_config.UpdateVPCSCConfigRequest],
        Union[gda_vpcsc_config.VPCSCConfig, Awaitable[gda_vpcsc_config.VPCSCConfig]],
    ]:
        raise NotImplementedError()

    @property
    def update_package(
        self,
    ) -> Callable[
        [gda_package.UpdatePackageRequest],
        Union[gda_package.Package, Awaitable[gda_package.Package]],
    ]:
        raise NotImplementedError()

    @property
    def list_attachments(
        self,
    ) -> Callable[
        [attachment.ListAttachmentsRequest],
        Union[
            attachment.ListAttachmentsResponse,
            Awaitable[attachment.ListAttachmentsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_attachment(
        self,
    ) -> Callable[
        [attachment.GetAttachmentRequest],
        Union[attachment.Attachment, Awaitable[attachment.Attachment]],
    ]:
        raise NotImplementedError()

    @property
    def create_attachment(
        self,
    ) -> Callable[
        [gda_attachment.CreateAttachmentRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_attachment(
        self,
    ) -> Callable[
        [attachment.DeleteAttachmentRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def export_artifact(
        self,
    ) -> Callable[
        [export.ExportArtifactRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
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


__all__ = ("ArtifactRegistryTransport",)
