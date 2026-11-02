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

import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
import google.iam.v1.policy_pb2 as policy_pb2  # type: ignore
import google.protobuf
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, operations_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.artifactregistry_v1beta2._compat import transcode_request
from google.cloud.artifactregistry_v1beta2.types import (
    apt_artifact,
    file,
    package,
    repository,
    settings,
    tag,
    version,
    yum_artifact,
)
from google.cloud.artifactregistry_v1beta2.types import repository as gda_repository
from google.cloud.artifactregistry_v1beta2.types import tag as gda_tag

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseArtifactRegistryRestTransport

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


class ArtifactRegistryRestInterceptor:
    """Interceptor for ArtifactRegistry.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the ArtifactRegistryRestTransport.

    .. code-block:: python
        class MyCustomArtifactRegistryInterceptor(ArtifactRegistryRestInterceptor):
            def pre_create_repository(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_repository(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_tag(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_tag(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_package(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_package(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_repository(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_repository(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_tag(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_version(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_file(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_file(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_iam_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_iam_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_package(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_package(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_project_settings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_project_settings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_repository(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_repository(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_tag(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_tag(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_version(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_import_apt_artifacts(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_import_apt_artifacts(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_import_yum_artifacts(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_import_yum_artifacts(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_files(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_files(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_packages(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_packages(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_repositories(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_repositories(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_tags(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_tags(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_versions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_versions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_iam_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_iam_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_test_iam_permissions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_test_iam_permissions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_project_settings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_project_settings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_repository(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_repository(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_tag(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_tag(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = ArtifactRegistryRestTransport(interceptor=MyCustomArtifactRegistryInterceptor())
        client = ArtifactRegistryClient(transport=transport)


    """

    def pre_create_repository(
        self,
        request: gda_repository.CreateRepositoryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gda_repository.CreateRepositoryRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_repository

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ArtifactRegistry server.
        """
        return request, metadata

    def post_create_repository(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_repository

        DEPRECATED. Please use the `post_create_repository_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ArtifactRegistry server but before
        it is returned to user code. This `post_create_repository` interceptor runs
        before the `post_create_repository_with_metadata` interceptor.
        """
        return response

    def post_create_repository_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_repository

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ArtifactRegistry server but before it is returned to user code.

        We recommend only using this `post_create_repository_with_metadata`
        interceptor in new development instead of the `post_create_repository` interceptor.
        When both interceptors are used, this `post_create_repository_with_metadata` interceptor runs after the
        `post_create_repository` interceptor. The (possibly modified) response returned by
        `post_create_repository` will be passed to
        `post_create_repository_with_metadata`.
        """
        return response, metadata

    def pre_create_tag(
        self,
        request: gda_tag.CreateTagRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gda_tag.CreateTagRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_tag

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ArtifactRegistry server.
        """
        return request, metadata

    def post_create_tag(self, response: gda_tag.Tag) -> gda_tag.Tag:
        """Post-rpc interceptor for create_tag

        DEPRECATED. Please use the `post_create_tag_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ArtifactRegistry server but before
        it is returned to user code. This `post_create_tag` interceptor runs
        before the `post_create_tag_with_metadata` interceptor.
        """
        return response

    def post_create_tag_with_metadata(
        self, response: gda_tag.Tag, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[gda_tag.Tag, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_tag

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ArtifactRegistry server but before it is returned to user code.

        We recommend only using this `post_create_tag_with_metadata`
        interceptor in new development instead of the `post_create_tag` interceptor.
        When both interceptors are used, this `post_create_tag_with_metadata` interceptor runs after the
        `post_create_tag` interceptor. The (possibly modified) response returned by
        `post_create_tag` will be passed to
        `post_create_tag_with_metadata`.
        """
        return response, metadata

    def pre_delete_package(
        self,
        request: package.DeletePackageRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[package.DeletePackageRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_package

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ArtifactRegistry server.
        """
        return request, metadata

    def post_delete_package(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_package

        DEPRECATED. Please use the `post_delete_package_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ArtifactRegistry server but before
        it is returned to user code. This `post_delete_package` interceptor runs
        before the `post_delete_package_with_metadata` interceptor.
        """
        return response

    def post_delete_package_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_package

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ArtifactRegistry server but before it is returned to user code.

        We recommend only using this `post_delete_package_with_metadata`
        interceptor in new development instead of the `post_delete_package` interceptor.
        When both interceptors are used, this `post_delete_package_with_metadata` interceptor runs after the
        `post_delete_package` interceptor. The (possibly modified) response returned by
        `post_delete_package` will be passed to
        `post_delete_package_with_metadata`.
        """
        return response, metadata

    def pre_delete_repository(
        self,
        request: repository.DeleteRepositoryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        repository.DeleteRepositoryRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_repository

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ArtifactRegistry server.
        """
        return request, metadata

    def post_delete_repository(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_repository

        DEPRECATED. Please use the `post_delete_repository_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ArtifactRegistry server but before
        it is returned to user code. This `post_delete_repository` interceptor runs
        before the `post_delete_repository_with_metadata` interceptor.
        """
        return response

    def post_delete_repository_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_repository

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ArtifactRegistry server but before it is returned to user code.

        We recommend only using this `post_delete_repository_with_metadata`
        interceptor in new development instead of the `post_delete_repository` interceptor.
        When both interceptors are used, this `post_delete_repository_with_metadata` interceptor runs after the
        `post_delete_repository` interceptor. The (possibly modified) response returned by
        `post_delete_repository` will be passed to
        `post_delete_repository_with_metadata`.
        """
        return response, metadata

    def pre_delete_tag(
        self,
        request: tag.DeleteTagRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[tag.DeleteTagRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_tag

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ArtifactRegistry server.
        """
        return request, metadata

    def pre_delete_version(
        self,
        request: version.DeleteVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[version.DeleteVersionRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ArtifactRegistry server.
        """
        return request, metadata

    def post_delete_version(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_version

        DEPRECATED. Please use the `post_delete_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ArtifactRegistry server but before
        it is returned to user code. This `post_delete_version` interceptor runs
        before the `post_delete_version_with_metadata` interceptor.
        """
        return response

    def post_delete_version_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ArtifactRegistry server but before it is returned to user code.

        We recommend only using this `post_delete_version_with_metadata`
        interceptor in new development instead of the `post_delete_version` interceptor.
        When both interceptors are used, this `post_delete_version_with_metadata` interceptor runs after the
        `post_delete_version` interceptor. The (possibly modified) response returned by
        `post_delete_version` will be passed to
        `post_delete_version_with_metadata`.
        """
        return response, metadata

    def pre_get_file(
        self,
        request: file.GetFileRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[file.GetFileRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_file

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ArtifactRegistry server.
        """
        return request, metadata

    def post_get_file(self, response: file.File) -> file.File:
        """Post-rpc interceptor for get_file

        DEPRECATED. Please use the `post_get_file_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ArtifactRegistry server but before
        it is returned to user code. This `post_get_file` interceptor runs
        before the `post_get_file_with_metadata` interceptor.
        """
        return response

    def post_get_file_with_metadata(
        self, response: file.File, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[file.File, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_file

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ArtifactRegistry server but before it is returned to user code.

        We recommend only using this `post_get_file_with_metadata`
        interceptor in new development instead of the `post_get_file` interceptor.
        When both interceptors are used, this `post_get_file_with_metadata` interceptor runs after the
        `post_get_file` interceptor. The (possibly modified) response returned by
        `post_get_file` will be passed to
        `post_get_file_with_metadata`.
        """
        return response, metadata

    def pre_get_iam_policy(
        self,
        request: iam_policy_pb2.GetIamPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.GetIamPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ArtifactRegistry server.
        """
        return request, metadata

    def post_get_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        DEPRECATED. Please use the `post_get_iam_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ArtifactRegistry server but before
        it is returned to user code. This `post_get_iam_policy` interceptor runs
        before the `post_get_iam_policy_with_metadata` interceptor.
        """
        return response

    def post_get_iam_policy_with_metadata(
        self,
        response: policy_pb2.Policy,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[policy_pb2.Policy, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ArtifactRegistry server but before it is returned to user code.

        We recommend only using this `post_get_iam_policy_with_metadata`
        interceptor in new development instead of the `post_get_iam_policy` interceptor.
        When both interceptors are used, this `post_get_iam_policy_with_metadata` interceptor runs after the
        `post_get_iam_policy` interceptor. The (possibly modified) response returned by
        `post_get_iam_policy` will be passed to
        `post_get_iam_policy_with_metadata`.
        """
        return response, metadata

    def pre_get_package(
        self,
        request: package.GetPackageRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[package.GetPackageRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_package

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ArtifactRegistry server.
        """
        return request, metadata

    def post_get_package(self, response: package.Package) -> package.Package:
        """Post-rpc interceptor for get_package

        DEPRECATED. Please use the `post_get_package_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ArtifactRegistry server but before
        it is returned to user code. This `post_get_package` interceptor runs
        before the `post_get_package_with_metadata` interceptor.
        """
        return response

    def post_get_package_with_metadata(
        self,
        response: package.Package,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[package.Package, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_package

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ArtifactRegistry server but before it is returned to user code.

        We recommend only using this `post_get_package_with_metadata`
        interceptor in new development instead of the `post_get_package` interceptor.
        When both interceptors are used, this `post_get_package_with_metadata` interceptor runs after the
        `post_get_package` interceptor. The (possibly modified) response returned by
        `post_get_package` will be passed to
        `post_get_package_with_metadata`.
        """
        return response, metadata

    def pre_get_project_settings(
        self,
        request: settings.GetProjectSettingsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        settings.GetProjectSettingsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_project_settings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ArtifactRegistry server.
        """
        return request, metadata

    def post_get_project_settings(
        self, response: settings.ProjectSettings
    ) -> settings.ProjectSettings:
        """Post-rpc interceptor for get_project_settings

        DEPRECATED. Please use the `post_get_project_settings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ArtifactRegistry server but before
        it is returned to user code. This `post_get_project_settings` interceptor runs
        before the `post_get_project_settings_with_metadata` interceptor.
        """
        return response

    def post_get_project_settings_with_metadata(
        self,
        response: settings.ProjectSettings,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[settings.ProjectSettings, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_project_settings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ArtifactRegistry server but before it is returned to user code.

        We recommend only using this `post_get_project_settings_with_metadata`
        interceptor in new development instead of the `post_get_project_settings` interceptor.
        When both interceptors are used, this `post_get_project_settings_with_metadata` interceptor runs after the
        `post_get_project_settings` interceptor. The (possibly modified) response returned by
        `post_get_project_settings` will be passed to
        `post_get_project_settings_with_metadata`.
        """
        return response, metadata

    def pre_get_repository(
        self,
        request: repository.GetRepositoryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        repository.GetRepositoryRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_repository

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ArtifactRegistry server.
        """
        return request, metadata

    def post_get_repository(
        self, response: repository.Repository
    ) -> repository.Repository:
        """Post-rpc interceptor for get_repository

        DEPRECATED. Please use the `post_get_repository_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ArtifactRegistry server but before
        it is returned to user code. This `post_get_repository` interceptor runs
        before the `post_get_repository_with_metadata` interceptor.
        """
        return response

    def post_get_repository_with_metadata(
        self,
        response: repository.Repository,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[repository.Repository, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_repository

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ArtifactRegistry server but before it is returned to user code.

        We recommend only using this `post_get_repository_with_metadata`
        interceptor in new development instead of the `post_get_repository` interceptor.
        When both interceptors are used, this `post_get_repository_with_metadata` interceptor runs after the
        `post_get_repository` interceptor. The (possibly modified) response returned by
        `post_get_repository` will be passed to
        `post_get_repository_with_metadata`.
        """
        return response, metadata

    def pre_get_tag(
        self,
        request: tag.GetTagRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[tag.GetTagRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_tag

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ArtifactRegistry server.
        """
        return request, metadata

    def post_get_tag(self, response: tag.Tag) -> tag.Tag:
        """Post-rpc interceptor for get_tag

        DEPRECATED. Please use the `post_get_tag_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ArtifactRegistry server but before
        it is returned to user code. This `post_get_tag` interceptor runs
        before the `post_get_tag_with_metadata` interceptor.
        """
        return response

    def post_get_tag_with_metadata(
        self, response: tag.Tag, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[tag.Tag, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_tag

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ArtifactRegistry server but before it is returned to user code.

        We recommend only using this `post_get_tag_with_metadata`
        interceptor in new development instead of the `post_get_tag` interceptor.
        When both interceptors are used, this `post_get_tag_with_metadata` interceptor runs after the
        `post_get_tag` interceptor. The (possibly modified) response returned by
        `post_get_tag` will be passed to
        `post_get_tag_with_metadata`.
        """
        return response, metadata

    def pre_get_version(
        self,
        request: version.GetVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[version.GetVersionRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ArtifactRegistry server.
        """
        return request, metadata

    def post_get_version(self, response: version.Version) -> version.Version:
        """Post-rpc interceptor for get_version

        DEPRECATED. Please use the `post_get_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ArtifactRegistry server but before
        it is returned to user code. This `post_get_version` interceptor runs
        before the `post_get_version_with_metadata` interceptor.
        """
        return response

    def post_get_version_with_metadata(
        self,
        response: version.Version,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[version.Version, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ArtifactRegistry server but before it is returned to user code.

        We recommend only using this `post_get_version_with_metadata`
        interceptor in new development instead of the `post_get_version` interceptor.
        When both interceptors are used, this `post_get_version_with_metadata` interceptor runs after the
        `post_get_version` interceptor. The (possibly modified) response returned by
        `post_get_version` will be passed to
        `post_get_version_with_metadata`.
        """
        return response, metadata

    def pre_import_apt_artifacts(
        self,
        request: apt_artifact.ImportAptArtifactsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apt_artifact.ImportAptArtifactsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for import_apt_artifacts

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ArtifactRegistry server.
        """
        return request, metadata

    def post_import_apt_artifacts(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for import_apt_artifacts

        DEPRECATED. Please use the `post_import_apt_artifacts_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ArtifactRegistry server but before
        it is returned to user code. This `post_import_apt_artifacts` interceptor runs
        before the `post_import_apt_artifacts_with_metadata` interceptor.
        """
        return response

    def post_import_apt_artifacts_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for import_apt_artifacts

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ArtifactRegistry server but before it is returned to user code.

        We recommend only using this `post_import_apt_artifacts_with_metadata`
        interceptor in new development instead of the `post_import_apt_artifacts` interceptor.
        When both interceptors are used, this `post_import_apt_artifacts_with_metadata` interceptor runs after the
        `post_import_apt_artifacts` interceptor. The (possibly modified) response returned by
        `post_import_apt_artifacts` will be passed to
        `post_import_apt_artifacts_with_metadata`.
        """
        return response, metadata

    def pre_import_yum_artifacts(
        self,
        request: yum_artifact.ImportYumArtifactsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        yum_artifact.ImportYumArtifactsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for import_yum_artifacts

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ArtifactRegistry server.
        """
        return request, metadata

    def post_import_yum_artifacts(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for import_yum_artifacts

        DEPRECATED. Please use the `post_import_yum_artifacts_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ArtifactRegistry server but before
        it is returned to user code. This `post_import_yum_artifacts` interceptor runs
        before the `post_import_yum_artifacts_with_metadata` interceptor.
        """
        return response

    def post_import_yum_artifacts_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for import_yum_artifacts

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ArtifactRegistry server but before it is returned to user code.

        We recommend only using this `post_import_yum_artifacts_with_metadata`
        interceptor in new development instead of the `post_import_yum_artifacts` interceptor.
        When both interceptors are used, this `post_import_yum_artifacts_with_metadata` interceptor runs after the
        `post_import_yum_artifacts` interceptor. The (possibly modified) response returned by
        `post_import_yum_artifacts` will be passed to
        `post_import_yum_artifacts_with_metadata`.
        """
        return response, metadata

    def pre_list_files(
        self,
        request: file.ListFilesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[file.ListFilesRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_files

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ArtifactRegistry server.
        """
        return request, metadata

    def post_list_files(
        self, response: file.ListFilesResponse
    ) -> file.ListFilesResponse:
        """Post-rpc interceptor for list_files

        DEPRECATED. Please use the `post_list_files_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ArtifactRegistry server but before
        it is returned to user code. This `post_list_files` interceptor runs
        before the `post_list_files_with_metadata` interceptor.
        """
        return response

    def post_list_files_with_metadata(
        self,
        response: file.ListFilesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[file.ListFilesResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_files

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ArtifactRegistry server but before it is returned to user code.

        We recommend only using this `post_list_files_with_metadata`
        interceptor in new development instead of the `post_list_files` interceptor.
        When both interceptors are used, this `post_list_files_with_metadata` interceptor runs after the
        `post_list_files` interceptor. The (possibly modified) response returned by
        `post_list_files` will be passed to
        `post_list_files_with_metadata`.
        """
        return response, metadata

    def pre_list_packages(
        self,
        request: package.ListPackagesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[package.ListPackagesRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_packages

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ArtifactRegistry server.
        """
        return request, metadata

    def post_list_packages(
        self, response: package.ListPackagesResponse
    ) -> package.ListPackagesResponse:
        """Post-rpc interceptor for list_packages

        DEPRECATED. Please use the `post_list_packages_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ArtifactRegistry server but before
        it is returned to user code. This `post_list_packages` interceptor runs
        before the `post_list_packages_with_metadata` interceptor.
        """
        return response

    def post_list_packages_with_metadata(
        self,
        response: package.ListPackagesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[package.ListPackagesResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_packages

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ArtifactRegistry server but before it is returned to user code.

        We recommend only using this `post_list_packages_with_metadata`
        interceptor in new development instead of the `post_list_packages` interceptor.
        When both interceptors are used, this `post_list_packages_with_metadata` interceptor runs after the
        `post_list_packages` interceptor. The (possibly modified) response returned by
        `post_list_packages` will be passed to
        `post_list_packages_with_metadata`.
        """
        return response, metadata

    def pre_list_repositories(
        self,
        request: repository.ListRepositoriesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        repository.ListRepositoriesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_repositories

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ArtifactRegistry server.
        """
        return request, metadata

    def post_list_repositories(
        self, response: repository.ListRepositoriesResponse
    ) -> repository.ListRepositoriesResponse:
        """Post-rpc interceptor for list_repositories

        DEPRECATED. Please use the `post_list_repositories_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ArtifactRegistry server but before
        it is returned to user code. This `post_list_repositories` interceptor runs
        before the `post_list_repositories_with_metadata` interceptor.
        """
        return response

    def post_list_repositories_with_metadata(
        self,
        response: repository.ListRepositoriesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        repository.ListRepositoriesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_repositories

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ArtifactRegistry server but before it is returned to user code.

        We recommend only using this `post_list_repositories_with_metadata`
        interceptor in new development instead of the `post_list_repositories` interceptor.
        When both interceptors are used, this `post_list_repositories_with_metadata` interceptor runs after the
        `post_list_repositories` interceptor. The (possibly modified) response returned by
        `post_list_repositories` will be passed to
        `post_list_repositories_with_metadata`.
        """
        return response, metadata

    def pre_list_tags(
        self,
        request: tag.ListTagsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[tag.ListTagsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_tags

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ArtifactRegistry server.
        """
        return request, metadata

    def post_list_tags(self, response: tag.ListTagsResponse) -> tag.ListTagsResponse:
        """Post-rpc interceptor for list_tags

        DEPRECATED. Please use the `post_list_tags_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ArtifactRegistry server but before
        it is returned to user code. This `post_list_tags` interceptor runs
        before the `post_list_tags_with_metadata` interceptor.
        """
        return response

    def post_list_tags_with_metadata(
        self,
        response: tag.ListTagsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[tag.ListTagsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_tags

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ArtifactRegistry server but before it is returned to user code.

        We recommend only using this `post_list_tags_with_metadata`
        interceptor in new development instead of the `post_list_tags` interceptor.
        When both interceptors are used, this `post_list_tags_with_metadata` interceptor runs after the
        `post_list_tags` interceptor. The (possibly modified) response returned by
        `post_list_tags` will be passed to
        `post_list_tags_with_metadata`.
        """
        return response, metadata

    def pre_list_versions(
        self,
        request: version.ListVersionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[version.ListVersionsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_versions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ArtifactRegistry server.
        """
        return request, metadata

    def post_list_versions(
        self, response: version.ListVersionsResponse
    ) -> version.ListVersionsResponse:
        """Post-rpc interceptor for list_versions

        DEPRECATED. Please use the `post_list_versions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ArtifactRegistry server but before
        it is returned to user code. This `post_list_versions` interceptor runs
        before the `post_list_versions_with_metadata` interceptor.
        """
        return response

    def post_list_versions_with_metadata(
        self,
        response: version.ListVersionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[version.ListVersionsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_versions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ArtifactRegistry server but before it is returned to user code.

        We recommend only using this `post_list_versions_with_metadata`
        interceptor in new development instead of the `post_list_versions` interceptor.
        When both interceptors are used, this `post_list_versions_with_metadata` interceptor runs after the
        `post_list_versions` interceptor. The (possibly modified) response returned by
        `post_list_versions` will be passed to
        `post_list_versions_with_metadata`.
        """
        return response, metadata

    def pre_set_iam_policy(
        self,
        request: iam_policy_pb2.SetIamPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.SetIamPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ArtifactRegistry server.
        """
        return request, metadata

    def post_set_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        DEPRECATED. Please use the `post_set_iam_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ArtifactRegistry server but before
        it is returned to user code. This `post_set_iam_policy` interceptor runs
        before the `post_set_iam_policy_with_metadata` interceptor.
        """
        return response

    def post_set_iam_policy_with_metadata(
        self,
        response: policy_pb2.Policy,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[policy_pb2.Policy, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ArtifactRegistry server but before it is returned to user code.

        We recommend only using this `post_set_iam_policy_with_metadata`
        interceptor in new development instead of the `post_set_iam_policy` interceptor.
        When both interceptors are used, this `post_set_iam_policy_with_metadata` interceptor runs after the
        `post_set_iam_policy` interceptor. The (possibly modified) response returned by
        `post_set_iam_policy` will be passed to
        `post_set_iam_policy_with_metadata`.
        """
        return response, metadata

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
        before they are sent to the ArtifactRegistry server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        DEPRECATED. Please use the `post_test_iam_permissions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ArtifactRegistry server but before
        it is returned to user code. This `post_test_iam_permissions` interceptor runs
        before the `post_test_iam_permissions_with_metadata` interceptor.
        """
        return response

    def post_test_iam_permissions_with_metadata(
        self,
        response: iam_policy_pb2.TestIamPermissionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.TestIamPermissionsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ArtifactRegistry server but before it is returned to user code.

        We recommend only using this `post_test_iam_permissions_with_metadata`
        interceptor in new development instead of the `post_test_iam_permissions` interceptor.
        When both interceptors are used, this `post_test_iam_permissions_with_metadata` interceptor runs after the
        `post_test_iam_permissions` interceptor. The (possibly modified) response returned by
        `post_test_iam_permissions` will be passed to
        `post_test_iam_permissions_with_metadata`.
        """
        return response, metadata

    def pre_update_project_settings(
        self,
        request: settings.UpdateProjectSettingsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        settings.UpdateProjectSettingsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_project_settings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ArtifactRegistry server.
        """
        return request, metadata

    def post_update_project_settings(
        self, response: settings.ProjectSettings
    ) -> settings.ProjectSettings:
        """Post-rpc interceptor for update_project_settings

        DEPRECATED. Please use the `post_update_project_settings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ArtifactRegistry server but before
        it is returned to user code. This `post_update_project_settings` interceptor runs
        before the `post_update_project_settings_with_metadata` interceptor.
        """
        return response

    def post_update_project_settings_with_metadata(
        self,
        response: settings.ProjectSettings,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[settings.ProjectSettings, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_project_settings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ArtifactRegistry server but before it is returned to user code.

        We recommend only using this `post_update_project_settings_with_metadata`
        interceptor in new development instead of the `post_update_project_settings` interceptor.
        When both interceptors are used, this `post_update_project_settings_with_metadata` interceptor runs after the
        `post_update_project_settings` interceptor. The (possibly modified) response returned by
        `post_update_project_settings` will be passed to
        `post_update_project_settings_with_metadata`.
        """
        return response, metadata

    def pre_update_repository(
        self,
        request: gda_repository.UpdateRepositoryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gda_repository.UpdateRepositoryRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_repository

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ArtifactRegistry server.
        """
        return request, metadata

    def post_update_repository(
        self, response: gda_repository.Repository
    ) -> gda_repository.Repository:
        """Post-rpc interceptor for update_repository

        DEPRECATED. Please use the `post_update_repository_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ArtifactRegistry server but before
        it is returned to user code. This `post_update_repository` interceptor runs
        before the `post_update_repository_with_metadata` interceptor.
        """
        return response

    def post_update_repository_with_metadata(
        self,
        response: gda_repository.Repository,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gda_repository.Repository, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_repository

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ArtifactRegistry server but before it is returned to user code.

        We recommend only using this `post_update_repository_with_metadata`
        interceptor in new development instead of the `post_update_repository` interceptor.
        When both interceptors are used, this `post_update_repository_with_metadata` interceptor runs after the
        `post_update_repository` interceptor. The (possibly modified) response returned by
        `post_update_repository` will be passed to
        `post_update_repository_with_metadata`.
        """
        return response, metadata

    def pre_update_tag(
        self,
        request: gda_tag.UpdateTagRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gda_tag.UpdateTagRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_tag

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ArtifactRegistry server.
        """
        return request, metadata

    def post_update_tag(self, response: gda_tag.Tag) -> gda_tag.Tag:
        """Post-rpc interceptor for update_tag

        DEPRECATED. Please use the `post_update_tag_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ArtifactRegistry server but before
        it is returned to user code. This `post_update_tag` interceptor runs
        before the `post_update_tag_with_metadata` interceptor.
        """
        return response

    def post_update_tag_with_metadata(
        self, response: gda_tag.Tag, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[gda_tag.Tag, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_tag

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ArtifactRegistry server but before it is returned to user code.

        We recommend only using this `post_update_tag_with_metadata`
        interceptor in new development instead of the `post_update_tag` interceptor.
        When both interceptors are used, this `post_update_tag_with_metadata` interceptor runs after the
        `post_update_tag` interceptor. The (possibly modified) response returned by
        `post_update_tag` will be passed to
        `post_update_tag_with_metadata`.
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
        before they are sent to the ArtifactRegistry server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the ArtifactRegistry server but before
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
        before they are sent to the ArtifactRegistry server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the ArtifactRegistry server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class ArtifactRegistryRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: ArtifactRegistryRestInterceptor


class ArtifactRegistryRestTransport(_BaseArtifactRegistryRestTransport):
    """REST backend synchronous transport for ArtifactRegistry.

    The Artifact Registry API service.

    Artifact Registry is an artifact management system for storing
    artifacts from different package management systems.

    The resources managed by this API are:

    - Repositories, which group packages and their data.
    - Packages, which group versions and their tags.
    - Versions, which are specific forms of a package.
    - Tags, which represent alternative names for versions.
    - Files, which contain content and are optionally associated with a
      Package or Version.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "artifactregistry.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[ArtifactRegistryRestInterceptor] = None,
        api_audience: Optional[str] = None,
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
            interceptor (Optional[ArtifactRegistryRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or ArtifactRegistryRestInterceptor()
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
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v1beta2/{name=projects/*/locations/*/operations/*}",
                    },
                ],
            }

            rest_transport = operations_v1.OperationsRestTransport(
                host=self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                scopes=self._scopes,
                http_options=http_options,
                path_prefix="v1beta2",
            )

            self._operations_client = operations_v1.AbstractOperationsClient(
                transport=rest_transport
            )

        # Return the client from cache.
        return self._operations_client

    class _CreateRepository(
        _BaseArtifactRegistryRestTransport._BaseCreateRepository,
        ArtifactRegistryRestStub,
    ):
        def __hash__(self):
            return hash("ArtifactRegistryRestTransport.CreateRepository")

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
            request: gda_repository.CreateRepositoryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create repository method over HTTP.

            Args:
                request (~.gda_repository.CreateRepositoryRequest):
                    The request object. The request to create a new
                repository.
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

            http_options = _BaseArtifactRegistryRestTransport._BaseCreateRepository._get_http_options()
            request, metadata = self._interceptor.pre_create_repository(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseArtifactRegistryRestTransport._BaseCreateRepository,
                    "_BaseCreateRepository__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.CreateRepository",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "CreateRepository",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ArtifactRegistryRestTransport._CreateRepository._get_response(
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

            resp = self._interceptor.post_create_repository(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_repository_with_metadata(
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
                    "Received response for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.create_repository",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "CreateRepository",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateTag(
        _BaseArtifactRegistryRestTransport._BaseCreateTag, ArtifactRegistryRestStub
    ):
        def __hash__(self):
            return hash("ArtifactRegistryRestTransport.CreateTag")

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
            request: gda_tag.CreateTagRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gda_tag.Tag:
            r"""Call the create tag method over HTTP.

            Args:
                request (~.gda_tag.CreateTagRequest):
                    The request object. The request to create a new tag.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gda_tag.Tag:
                    Tags point to a version and represent
                an alternative name that can be used to
                access the version.

            """

            http_options = (
                _BaseArtifactRegistryRestTransport._BaseCreateTag._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_tag(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseArtifactRegistryRestTransport._BaseCreateTag,
                    "_BaseCreateTag__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.CreateTag",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "CreateTag",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ArtifactRegistryRestTransport._CreateTag._get_response(
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
            resp = gda_tag.Tag()
            pb_resp = gda_tag.Tag.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_tag(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_tag_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gda_tag.Tag.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.create_tag",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "CreateTag",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeletePackage(
        _BaseArtifactRegistryRestTransport._BaseDeletePackage, ArtifactRegistryRestStub
    ):
        def __hash__(self):
            return hash("ArtifactRegistryRestTransport.DeletePackage")

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
            request: package.DeletePackageRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete package method over HTTP.

            Args:
                request (~.package.DeletePackageRequest):
                    The request object. The request to delete a package.
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

            http_options = _BaseArtifactRegistryRestTransport._BaseDeletePackage._get_http_options()
            request, metadata = self._interceptor.pre_delete_package(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseArtifactRegistryRestTransport._BaseDeletePackage,
                    "_BaseDeletePackage__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.DeletePackage",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "DeletePackage",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ArtifactRegistryRestTransport._DeletePackage._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_package(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_package_with_metadata(
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
                    "Received response for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.delete_package",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "DeletePackage",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteRepository(
        _BaseArtifactRegistryRestTransport._BaseDeleteRepository,
        ArtifactRegistryRestStub,
    ):
        def __hash__(self):
            return hash("ArtifactRegistryRestTransport.DeleteRepository")

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
            request: repository.DeleteRepositoryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete repository method over HTTP.

            Args:
                request (~.repository.DeleteRepositoryRequest):
                    The request object. The request to delete a repository.
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

            http_options = _BaseArtifactRegistryRestTransport._BaseDeleteRepository._get_http_options()
            request, metadata = self._interceptor.pre_delete_repository(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseArtifactRegistryRestTransport._BaseDeleteRepository,
                    "_BaseDeleteRepository__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.DeleteRepository",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "DeleteRepository",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ArtifactRegistryRestTransport._DeleteRepository._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_repository(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_repository_with_metadata(
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
                    "Received response for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.delete_repository",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "DeleteRepository",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteTag(
        _BaseArtifactRegistryRestTransport._BaseDeleteTag, ArtifactRegistryRestStub
    ):
        def __hash__(self):
            return hash("ArtifactRegistryRestTransport.DeleteTag")

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
            request: tag.DeleteTagRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete tag method over HTTP.

            Args:
                request (~.tag.DeleteTagRequest):
                    The request object. The request to delete a tag.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseArtifactRegistryRestTransport._BaseDeleteTag._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_tag(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseArtifactRegistryRestTransport._BaseDeleteTag,
                    "_BaseDeleteTag__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.DeleteTag",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "DeleteTag",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ArtifactRegistryRestTransport._DeleteTag._get_response(
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

    class _DeleteVersion(
        _BaseArtifactRegistryRestTransport._BaseDeleteVersion, ArtifactRegistryRestStub
    ):
        def __hash__(self):
            return hash("ArtifactRegistryRestTransport.DeleteVersion")

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
            request: version.DeleteVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete version method over HTTP.

            Args:
                request (~.version.DeleteVersionRequest):
                    The request object. The request to delete a version.
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

            http_options = _BaseArtifactRegistryRestTransport._BaseDeleteVersion._get_http_options()
            request, metadata = self._interceptor.pre_delete_version(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseArtifactRegistryRestTransport._BaseDeleteVersion,
                    "_BaseDeleteVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.DeleteVersion",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "DeleteVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ArtifactRegistryRestTransport._DeleteVersion._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_version_with_metadata(
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
                    "Received response for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.delete_version",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "DeleteVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetFile(
        _BaseArtifactRegistryRestTransport._BaseGetFile, ArtifactRegistryRestStub
    ):
        def __hash__(self):
            return hash("ArtifactRegistryRestTransport.GetFile")

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
            request: file.GetFileRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> file.File:
            r"""Call the get file method over HTTP.

            Args:
                request (~.file.GetFileRequest):
                    The request object. The request to retrieve a file.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.file.File:
                    Files store content that is
                potentially associated with Packages or
                Versions.

            """

            http_options = (
                _BaseArtifactRegistryRestTransport._BaseGetFile._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_file(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseArtifactRegistryRestTransport._BaseGetFile,
                    "_BaseGetFile__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.GetFile",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "GetFile",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ArtifactRegistryRestTransport._GetFile._get_response(
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
            resp = file.File()
            pb_resp = file.File.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_file(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_file_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = file.File.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.get_file",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "GetFile",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetIamPolicy(
        _BaseArtifactRegistryRestTransport._BaseGetIamPolicy, ArtifactRegistryRestStub
    ):
        def __hash__(self):
            return hash("ArtifactRegistryRestTransport.GetIamPolicy")

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
            request: iam_policy_pb2.GetIamPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> policy_pb2.Policy:
            r"""Call the get iam policy method over HTTP.

            Args:
                request (~.iam_policy_pb2.GetIamPolicyRequest):
                    The request object. Request message for ``GetIamPolicy`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.policy_pb2.Policy:
                    An Identity and Access Management (IAM) policy, which
                specifies access controls for Google Cloud resources.

                A ``Policy`` is a collection of ``bindings``. A
                ``binding`` binds one or more ``members``, or
                principals, to a single ``role``. Principals can be user
                accounts, service accounts, Google groups, and domains
                (such as G Suite). A ``role`` is a named list of
                permissions; each ``role`` can be an IAM predefined role
                or a user-created custom role.

                For some types of Google Cloud resources, a ``binding``
                can also specify a ``condition``, which is a logical
                expression that allows access to a resource only if the
                expression evaluates to ``true``. A condition can add
                constraints based on attributes of the request, the
                resource, or both. To learn which resources support
                conditions in their IAM policies, see the `IAM
                documentation <https://cloud.google.com/iam/help/conditions/resource-policies>`__.

                **JSON example:**

                ::

                       {
                         "bindings": [
                           {
                             "role": "roles/resourcemanager.organizationAdmin",
                             "members": [
                               "user:mike@example.com",
                               "group:admins@example.com",
                               "domain:google.com",
                               "serviceAccount:my-project-id@appspot.gserviceaccount.com"
                             ]
                           },
                           {
                             "role": "roles/resourcemanager.organizationViewer",
                             "members": [
                               "user:eve@example.com"
                             ],
                             "condition": {
                               "title": "expirable access",
                               "description": "Does not grant access after Sep 2020",
                               "expression": "request.time <
                               timestamp('2020-10-01T00:00:00.000Z')",
                             }
                           }
                         ],
                         "etag": "BwWWja0YfJA=",
                         "version": 3
                       }

                **YAML example:**

                ::

                       bindings:
                       - members:
                         - user:mike@example.com
                         - group:admins@example.com
                         - domain:google.com
                         - serviceAccount:my-project-id@appspot.gserviceaccount.com
                         role: roles/resourcemanager.organizationAdmin
                       - members:
                         - user:eve@example.com
                         role: roles/resourcemanager.organizationViewer
                         condition:
                           title: expirable access
                           description: Does not grant access after Sep 2020
                           expression: request.time < timestamp('2020-10-01T00:00:00.000Z')
                       etag: BwWWja0YfJA=
                       version: 3

                For a description of IAM and its features, see the `IAM
                documentation <https://cloud.google.com/iam/docs/>`__.

            """

            http_options = (
                _BaseArtifactRegistryRestTransport._BaseGetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseArtifactRegistryRestTransport._BaseGetIamPolicy,
                    "_BaseGetIamPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "GetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ArtifactRegistryRestTransport._GetIamPolicy._get_response(
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
            resp = policy_pb2.Policy()
            pb_resp = resp

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_iam_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_iam_policy_with_metadata(
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
                    "Received response for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.get_iam_policy",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "GetIamPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetPackage(
        _BaseArtifactRegistryRestTransport._BaseGetPackage, ArtifactRegistryRestStub
    ):
        def __hash__(self):
            return hash("ArtifactRegistryRestTransport.GetPackage")

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
            request: package.GetPackageRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> package.Package:
            r"""Call the get package method over HTTP.

            Args:
                request (~.package.GetPackageRequest):
                    The request object. The request to retrieve a package.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.package.Package:
                    Packages are named collections of
                versions.

            """

            http_options = (
                _BaseArtifactRegistryRestTransport._BaseGetPackage._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_package(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseArtifactRegistryRestTransport._BaseGetPackage,
                    "_BaseGetPackage__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.GetPackage",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "GetPackage",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ArtifactRegistryRestTransport._GetPackage._get_response(
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
            resp = package.Package()
            pb_resp = package.Package.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_package(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_package_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = package.Package.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.get_package",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "GetPackage",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetProjectSettings(
        _BaseArtifactRegistryRestTransport._BaseGetProjectSettings,
        ArtifactRegistryRestStub,
    ):
        def __hash__(self):
            return hash("ArtifactRegistryRestTransport.GetProjectSettings")

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
            request: settings.GetProjectSettingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> settings.ProjectSettings:
            r"""Call the get project settings method over HTTP.

            Args:
                request (~.settings.GetProjectSettingsRequest):
                    The request object. Gets the redirection status for a
                project.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.settings.ProjectSettings:
                    The Artifact Registry settings that
                apply to a Project.

            """

            http_options = _BaseArtifactRegistryRestTransport._BaseGetProjectSettings._get_http_options()
            request, metadata = self._interceptor.pre_get_project_settings(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseArtifactRegistryRestTransport._BaseGetProjectSettings,
                    "_BaseGetProjectSettings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.GetProjectSettings",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "GetProjectSettings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ArtifactRegistryRestTransport._GetProjectSettings._get_response(
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
            resp = settings.ProjectSettings()
            pb_resp = settings.ProjectSettings.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_project_settings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_project_settings_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = settings.ProjectSettings.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.get_project_settings",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "GetProjectSettings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetRepository(
        _BaseArtifactRegistryRestTransport._BaseGetRepository, ArtifactRegistryRestStub
    ):
        def __hash__(self):
            return hash("ArtifactRegistryRestTransport.GetRepository")

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
            request: repository.GetRepositoryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> repository.Repository:
            r"""Call the get repository method over HTTP.

            Args:
                request (~.repository.GetRepositoryRequest):
                    The request object. The request to retrieve a repository.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.repository.Repository:
                    A Repository for storing artifacts
                with a specific format.

            """

            http_options = _BaseArtifactRegistryRestTransport._BaseGetRepository._get_http_options()
            request, metadata = self._interceptor.pre_get_repository(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseArtifactRegistryRestTransport._BaseGetRepository,
                    "_BaseGetRepository__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.GetRepository",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "GetRepository",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ArtifactRegistryRestTransport._GetRepository._get_response(
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
            resp = repository.Repository()
            pb_resp = repository.Repository.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_repository(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_repository_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = repository.Repository.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.get_repository",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "GetRepository",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetTag(
        _BaseArtifactRegistryRestTransport._BaseGetTag, ArtifactRegistryRestStub
    ):
        def __hash__(self):
            return hash("ArtifactRegistryRestTransport.GetTag")

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
            request: tag.GetTagRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> tag.Tag:
            r"""Call the get tag method over HTTP.

            Args:
                request (~.tag.GetTagRequest):
                    The request object. The request to retrieve a tag.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.tag.Tag:
                    Tags point to a version and represent
                an alternative name that can be used to
                access the version.

            """

            http_options = (
                _BaseArtifactRegistryRestTransport._BaseGetTag._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_tag(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseArtifactRegistryRestTransport._BaseGetTag,
                    "_BaseGetTag__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.GetTag",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "GetTag",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ArtifactRegistryRestTransport._GetTag._get_response(
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
            resp = tag.Tag()
            pb_resp = tag.Tag.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_tag(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_tag_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = tag.Tag.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.get_tag",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "GetTag",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetVersion(
        _BaseArtifactRegistryRestTransport._BaseGetVersion, ArtifactRegistryRestStub
    ):
        def __hash__(self):
            return hash("ArtifactRegistryRestTransport.GetVersion")

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
            request: version.GetVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> version.Version:
            r"""Call the get version method over HTTP.

            Args:
                request (~.version.GetVersionRequest):
                    The request object. The request to retrieve a version.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.version.Version:
                    The body of a version resource. A
                version resource represents a collection
                of components, such as files and other
                data. This may correspond to a version
                in many package management schemes.

            """

            http_options = (
                _BaseArtifactRegistryRestTransport._BaseGetVersion._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_version(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseArtifactRegistryRestTransport._BaseGetVersion,
                    "_BaseGetVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.GetVersion",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "GetVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ArtifactRegistryRestTransport._GetVersion._get_response(
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
            resp = version.Version()
            pb_resp = version.Version.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_version_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = version.Version.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.get_version",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "GetVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ImportAptArtifacts(
        _BaseArtifactRegistryRestTransport._BaseImportAptArtifacts,
        ArtifactRegistryRestStub,
    ):
        def __hash__(self):
            return hash("ArtifactRegistryRestTransport.ImportAptArtifacts")

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
            request: apt_artifact.ImportAptArtifactsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the import apt artifacts method over HTTP.

            Args:
                request (~.apt_artifact.ImportAptArtifactsRequest):
                    The request object. The request to import new apt
                artifacts.
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

            http_options = _BaseArtifactRegistryRestTransport._BaseImportAptArtifacts._get_http_options()
            request, metadata = self._interceptor.pre_import_apt_artifacts(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseArtifactRegistryRestTransport._BaseImportAptArtifacts,
                    "_BaseImportAptArtifacts__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.ImportAptArtifacts",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "ImportAptArtifacts",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ArtifactRegistryRestTransport._ImportAptArtifacts._get_response(
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

            resp = self._interceptor.post_import_apt_artifacts(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_import_apt_artifacts_with_metadata(
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
                    "Received response for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.import_apt_artifacts",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "ImportAptArtifacts",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ImportYumArtifacts(
        _BaseArtifactRegistryRestTransport._BaseImportYumArtifacts,
        ArtifactRegistryRestStub,
    ):
        def __hash__(self):
            return hash("ArtifactRegistryRestTransport.ImportYumArtifacts")

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
            request: yum_artifact.ImportYumArtifactsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the import yum artifacts method over HTTP.

            Args:
                request (~.yum_artifact.ImportYumArtifactsRequest):
                    The request object. The request to import new yum
                artifacts.
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

            http_options = _BaseArtifactRegistryRestTransport._BaseImportYumArtifacts._get_http_options()
            request, metadata = self._interceptor.pre_import_yum_artifacts(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseArtifactRegistryRestTransport._BaseImportYumArtifacts,
                    "_BaseImportYumArtifacts__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.ImportYumArtifacts",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "ImportYumArtifacts",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ArtifactRegistryRestTransport._ImportYumArtifacts._get_response(
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

            resp = self._interceptor.post_import_yum_artifacts(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_import_yum_artifacts_with_metadata(
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
                    "Received response for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.import_yum_artifacts",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "ImportYumArtifacts",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListFiles(
        _BaseArtifactRegistryRestTransport._BaseListFiles, ArtifactRegistryRestStub
    ):
        def __hash__(self):
            return hash("ArtifactRegistryRestTransport.ListFiles")

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
            request: file.ListFilesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> file.ListFilesResponse:
            r"""Call the list files method over HTTP.

            Args:
                request (~.file.ListFilesRequest):
                    The request object. The request to list files.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.file.ListFilesResponse:
                    The response from listing files.
            """

            http_options = (
                _BaseArtifactRegistryRestTransport._BaseListFiles._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_files(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseArtifactRegistryRestTransport._BaseListFiles,
                    "_BaseListFiles__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.ListFiles",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "ListFiles",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ArtifactRegistryRestTransport._ListFiles._get_response(
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
            resp = file.ListFilesResponse()
            pb_resp = file.ListFilesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_files(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_files_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = file.ListFilesResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.list_files",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "ListFiles",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListPackages(
        _BaseArtifactRegistryRestTransport._BaseListPackages, ArtifactRegistryRestStub
    ):
        def __hash__(self):
            return hash("ArtifactRegistryRestTransport.ListPackages")

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
            request: package.ListPackagesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> package.ListPackagesResponse:
            r"""Call the list packages method over HTTP.

            Args:
                request (~.package.ListPackagesRequest):
                    The request object. The request to list packages.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.package.ListPackagesResponse:
                    The response from listing packages.
            """

            http_options = (
                _BaseArtifactRegistryRestTransport._BaseListPackages._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_packages(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseArtifactRegistryRestTransport._BaseListPackages,
                    "_BaseListPackages__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.ListPackages",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "ListPackages",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ArtifactRegistryRestTransport._ListPackages._get_response(
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
            resp = package.ListPackagesResponse()
            pb_resp = package.ListPackagesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_packages(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_packages_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = package.ListPackagesResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.list_packages",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "ListPackages",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListRepositories(
        _BaseArtifactRegistryRestTransport._BaseListRepositories,
        ArtifactRegistryRestStub,
    ):
        def __hash__(self):
            return hash("ArtifactRegistryRestTransport.ListRepositories")

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
            request: repository.ListRepositoriesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> repository.ListRepositoriesResponse:
            r"""Call the list repositories method over HTTP.

            Args:
                request (~.repository.ListRepositoriesRequest):
                    The request object. The request to list repositories.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.repository.ListRepositoriesResponse:
                    The response from listing
                repositories.

            """

            http_options = _BaseArtifactRegistryRestTransport._BaseListRepositories._get_http_options()
            request, metadata = self._interceptor.pre_list_repositories(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseArtifactRegistryRestTransport._BaseListRepositories,
                    "_BaseListRepositories__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.ListRepositories",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "ListRepositories",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ArtifactRegistryRestTransport._ListRepositories._get_response(
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
            resp = repository.ListRepositoriesResponse()
            pb_resp = repository.ListRepositoriesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_repositories(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_repositories_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = repository.ListRepositoriesResponse.to_json(
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
                    "Received response for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.list_repositories",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "ListRepositories",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListTags(
        _BaseArtifactRegistryRestTransport._BaseListTags, ArtifactRegistryRestStub
    ):
        def __hash__(self):
            return hash("ArtifactRegistryRestTransport.ListTags")

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
            request: tag.ListTagsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> tag.ListTagsResponse:
            r"""Call the list tags method over HTTP.

            Args:
                request (~.tag.ListTagsRequest):
                    The request object. The request to list tags.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.tag.ListTagsResponse:
                    The response from listing tags.
            """

            http_options = (
                _BaseArtifactRegistryRestTransport._BaseListTags._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_tags(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseArtifactRegistryRestTransport._BaseListTags,
                    "_BaseListTags__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.ListTags",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "ListTags",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ArtifactRegistryRestTransport._ListTags._get_response(
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
            resp = tag.ListTagsResponse()
            pb_resp = tag.ListTagsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_tags(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_tags_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = tag.ListTagsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.list_tags",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "ListTags",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListVersions(
        _BaseArtifactRegistryRestTransport._BaseListVersions, ArtifactRegistryRestStub
    ):
        def __hash__(self):
            return hash("ArtifactRegistryRestTransport.ListVersions")

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
            request: version.ListVersionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> version.ListVersionsResponse:
            r"""Call the list versions method over HTTP.

            Args:
                request (~.version.ListVersionsRequest):
                    The request object. The request to list versions.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.version.ListVersionsResponse:
                    The response from listing versions.
            """

            http_options = (
                _BaseArtifactRegistryRestTransport._BaseListVersions._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_versions(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseArtifactRegistryRestTransport._BaseListVersions,
                    "_BaseListVersions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.ListVersions",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "ListVersions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ArtifactRegistryRestTransport._ListVersions._get_response(
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
            resp = version.ListVersionsResponse()
            pb_resp = version.ListVersionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_versions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_versions_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = version.ListVersionsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.list_versions",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "ListVersions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetIamPolicy(
        _BaseArtifactRegistryRestTransport._BaseSetIamPolicy, ArtifactRegistryRestStub
    ):
        def __hash__(self):
            return hash("ArtifactRegistryRestTransport.SetIamPolicy")

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
            request: iam_policy_pb2.SetIamPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> policy_pb2.Policy:
            r"""Call the set iam policy method over HTTP.

            Args:
                request (~.iam_policy_pb2.SetIamPolicyRequest):
                    The request object. Request message for ``SetIamPolicy`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.policy_pb2.Policy:
                    An Identity and Access Management (IAM) policy, which
                specifies access controls for Google Cloud resources.

                A ``Policy`` is a collection of ``bindings``. A
                ``binding`` binds one or more ``members``, or
                principals, to a single ``role``. Principals can be user
                accounts, service accounts, Google groups, and domains
                (such as G Suite). A ``role`` is a named list of
                permissions; each ``role`` can be an IAM predefined role
                or a user-created custom role.

                For some types of Google Cloud resources, a ``binding``
                can also specify a ``condition``, which is a logical
                expression that allows access to a resource only if the
                expression evaluates to ``true``. A condition can add
                constraints based on attributes of the request, the
                resource, or both. To learn which resources support
                conditions in their IAM policies, see the `IAM
                documentation <https://cloud.google.com/iam/help/conditions/resource-policies>`__.

                **JSON example:**

                ::

                       {
                         "bindings": [
                           {
                             "role": "roles/resourcemanager.organizationAdmin",
                             "members": [
                               "user:mike@example.com",
                               "group:admins@example.com",
                               "domain:google.com",
                               "serviceAccount:my-project-id@appspot.gserviceaccount.com"
                             ]
                           },
                           {
                             "role": "roles/resourcemanager.organizationViewer",
                             "members": [
                               "user:eve@example.com"
                             ],
                             "condition": {
                               "title": "expirable access",
                               "description": "Does not grant access after Sep 2020",
                               "expression": "request.time <
                               timestamp('2020-10-01T00:00:00.000Z')",
                             }
                           }
                         ],
                         "etag": "BwWWja0YfJA=",
                         "version": 3
                       }

                **YAML example:**

                ::

                       bindings:
                       - members:
                         - user:mike@example.com
                         - group:admins@example.com
                         - domain:google.com
                         - serviceAccount:my-project-id@appspot.gserviceaccount.com
                         role: roles/resourcemanager.organizationAdmin
                       - members:
                         - user:eve@example.com
                         role: roles/resourcemanager.organizationViewer
                         condition:
                           title: expirable access
                           description: Does not grant access after Sep 2020
                           expression: request.time < timestamp('2020-10-01T00:00:00.000Z')
                       etag: BwWWja0YfJA=
                       version: 3

                For a description of IAM and its features, see the `IAM
                documentation <https://cloud.google.com/iam/docs/>`__.

            """

            http_options = (
                _BaseArtifactRegistryRestTransport._BaseSetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseArtifactRegistryRestTransport._BaseSetIamPolicy,
                    "_BaseSetIamPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "SetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ArtifactRegistryRestTransport._SetIamPolicy._get_response(
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
            resp = policy_pb2.Policy()
            pb_resp = resp

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_set_iam_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_iam_policy_with_metadata(
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
                    "Received response for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.set_iam_policy",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "SetIamPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _TestIamPermissions(
        _BaseArtifactRegistryRestTransport._BaseTestIamPermissions,
        ArtifactRegistryRestStub,
    ):
        def __hash__(self):
            return hash("ArtifactRegistryRestTransport.TestIamPermissions")

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
            request: iam_policy_pb2.TestIamPermissionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> iam_policy_pb2.TestIamPermissionsResponse:
            r"""Call the test iam permissions method over HTTP.

            Args:
                request (~.iam_policy_pb2.TestIamPermissionsRequest):
                    The request object. Request message for ``TestIamPermissions`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.iam_policy_pb2.TestIamPermissionsResponse:
                    Response message for ``TestIamPermissions`` method.
            """

            http_options = _BaseArtifactRegistryRestTransport._BaseTestIamPermissions._get_http_options()
            request, metadata = self._interceptor.pre_test_iam_permissions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseArtifactRegistryRestTransport._BaseTestIamPermissions,
                    "_BaseTestIamPermissions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "TestIamPermissions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ArtifactRegistryRestTransport._TestIamPermissions._get_response(
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
            resp = iam_policy_pb2.TestIamPermissionsResponse()
            pb_resp = resp

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_test_iam_permissions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_test_iam_permissions_with_metadata(
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
                    "Received response for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.test_iam_permissions",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "TestIamPermissions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateProjectSettings(
        _BaseArtifactRegistryRestTransport._BaseUpdateProjectSettings,
        ArtifactRegistryRestStub,
    ):
        def __hash__(self):
            return hash("ArtifactRegistryRestTransport.UpdateProjectSettings")

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
            request: settings.UpdateProjectSettingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> settings.ProjectSettings:
            r"""Call the update project settings method over HTTP.

            Args:
                request (~.settings.UpdateProjectSettingsRequest):
                    The request object. Sets the settings of the project.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.settings.ProjectSettings:
                    The Artifact Registry settings that
                apply to a Project.

            """

            http_options = _BaseArtifactRegistryRestTransport._BaseUpdateProjectSettings._get_http_options()
            request, metadata = self._interceptor.pre_update_project_settings(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseArtifactRegistryRestTransport._BaseUpdateProjectSettings,
                    "_BaseUpdateProjectSettings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.UpdateProjectSettings",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "UpdateProjectSettings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ArtifactRegistryRestTransport._UpdateProjectSettings._get_response(
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
            resp = settings.ProjectSettings()
            pb_resp = settings.ProjectSettings.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_project_settings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_project_settings_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = settings.ProjectSettings.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.update_project_settings",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "UpdateProjectSettings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateRepository(
        _BaseArtifactRegistryRestTransport._BaseUpdateRepository,
        ArtifactRegistryRestStub,
    ):
        def __hash__(self):
            return hash("ArtifactRegistryRestTransport.UpdateRepository")

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
            request: gda_repository.UpdateRepositoryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gda_repository.Repository:
            r"""Call the update repository method over HTTP.

            Args:
                request (~.gda_repository.UpdateRepositoryRequest):
                    The request object. The request to update a repository.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gda_repository.Repository:
                    A Repository for storing artifacts
                with a specific format.

            """

            http_options = _BaseArtifactRegistryRestTransport._BaseUpdateRepository._get_http_options()
            request, metadata = self._interceptor.pre_update_repository(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseArtifactRegistryRestTransport._BaseUpdateRepository,
                    "_BaseUpdateRepository__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.UpdateRepository",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "UpdateRepository",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ArtifactRegistryRestTransport._UpdateRepository._get_response(
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
            resp = gda_repository.Repository()
            pb_resp = gda_repository.Repository.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_repository(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_repository_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gda_repository.Repository.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.update_repository",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "UpdateRepository",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateTag(
        _BaseArtifactRegistryRestTransport._BaseUpdateTag, ArtifactRegistryRestStub
    ):
        def __hash__(self):
            return hash("ArtifactRegistryRestTransport.UpdateTag")

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
            request: gda_tag.UpdateTagRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gda_tag.Tag:
            r"""Call the update tag method over HTTP.

            Args:
                request (~.gda_tag.UpdateTagRequest):
                    The request object. The request to create or update a
                tag.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gda_tag.Tag:
                    Tags point to a version and represent
                an alternative name that can be used to
                access the version.

            """

            http_options = (
                _BaseArtifactRegistryRestTransport._BaseUpdateTag._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_tag(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseArtifactRegistryRestTransport._BaseUpdateTag,
                    "_BaseUpdateTag__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.UpdateTag",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "UpdateTag",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ArtifactRegistryRestTransport._UpdateTag._get_response(
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
            resp = gda_tag.Tag()
            pb_resp = gda_tag.Tag.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_tag(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_tag_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gda_tag.Tag.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.update_tag",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "UpdateTag",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_repository(
        self,
    ) -> Callable[[gda_repository.CreateRepositoryRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateRepository(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_tag(self) -> Callable[[gda_tag.CreateTagRequest], gda_tag.Tag]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateTag(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_package(
        self,
    ) -> Callable[[package.DeletePackageRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeletePackage(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_repository(
        self,
    ) -> Callable[[repository.DeleteRepositoryRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteRepository(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_tag(self) -> Callable[[tag.DeleteTagRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteTag(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_version(
        self,
    ) -> Callable[[version.DeleteVersionRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteVersion(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_file(self) -> Callable[[file.GetFileRequest], file.File]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetFile(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_iam_policy(
        self,
    ) -> Callable[[iam_policy_pb2.GetIamPolicyRequest], policy_pb2.Policy]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_package(self) -> Callable[[package.GetPackageRequest], package.Package]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetPackage(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_project_settings(
        self,
    ) -> Callable[[settings.GetProjectSettingsRequest], settings.ProjectSettings]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetProjectSettings(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_repository(
        self,
    ) -> Callable[[repository.GetRepositoryRequest], repository.Repository]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetRepository(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_tag(self) -> Callable[[tag.GetTagRequest], tag.Tag]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetTag(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_version(self) -> Callable[[version.GetVersionRequest], version.Version]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetVersion(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def import_apt_artifacts(
        self,
    ) -> Callable[[apt_artifact.ImportAptArtifactsRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ImportAptArtifacts(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def import_yum_artifacts(
        self,
    ) -> Callable[[yum_artifact.ImportYumArtifactsRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ImportYumArtifacts(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_files(self) -> Callable[[file.ListFilesRequest], file.ListFilesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListFiles(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_packages(
        self,
    ) -> Callable[[package.ListPackagesRequest], package.ListPackagesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListPackages(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_repositories(
        self,
    ) -> Callable[
        [repository.ListRepositoriesRequest], repository.ListRepositoriesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListRepositories(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_tags(self) -> Callable[[tag.ListTagsRequest], tag.ListTagsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListTags(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_versions(
        self,
    ) -> Callable[[version.ListVersionsRequest], version.ListVersionsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListVersions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def set_iam_policy(
        self,
    ) -> Callable[[iam_policy_pb2.SetIamPolicyRequest], policy_pb2.Policy]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def test_iam_permissions(
        self,
    ) -> Callable[
        [iam_policy_pb2.TestIamPermissionsRequest],
        iam_policy_pb2.TestIamPermissionsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._TestIamPermissions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_project_settings(
        self,
    ) -> Callable[[settings.UpdateProjectSettingsRequest], settings.ProjectSettings]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateProjectSettings(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_repository(
        self,
    ) -> Callable[[gda_repository.UpdateRepositoryRequest], gda_repository.Repository]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateRepository(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_tag(self) -> Callable[[gda_tag.UpdateTagRequest], gda_tag.Tag]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateTag(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseArtifactRegistryRestTransport._BaseGetLocation, ArtifactRegistryRestStub
    ):
        def __hash__(self):
            return hash("ArtifactRegistryRestTransport.GetLocation")

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
                _BaseArtifactRegistryRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseArtifactRegistryRestTransport._BaseGetLocation,
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
                    f"Sending request for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.GetLocation",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ArtifactRegistryRestTransport._GetLocation._get_response(
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
                    "Received response for google.devtools.artifactregistry_v1beta2.ArtifactRegistryAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "GetLocation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_locations(self):
        return self._ListLocations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListLocations(
        _BaseArtifactRegistryRestTransport._BaseListLocations, ArtifactRegistryRestStub
    ):
        def __hash__(self):
            return hash("ArtifactRegistryRestTransport.ListLocations")

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

            http_options = _BaseArtifactRegistryRestTransport._BaseListLocations._get_http_options()
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseArtifactRegistryRestTransport._BaseListLocations,
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
                    f"Sending request for google.devtools.artifactregistry_v1beta2.ArtifactRegistryClient.ListLocations",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ArtifactRegistryRestTransport._ListLocations._get_response(
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
                    "Received response for google.devtools.artifactregistry_v1beta2.ArtifactRegistryAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.devtools.artifactregistry.v1beta2.ArtifactRegistry",
                        "rpcName": "ListLocations",
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


__all__ = ("ArtifactRegistryRestTransport",)
