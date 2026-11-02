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
import logging as std_logging
import re
from collections import OrderedDict
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
)

import google.protobuf
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry_async as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.devtools.cloudbuild_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.api_core.operation as operation  # type: ignore
import google.api_core.operation_async as operation_async  # type: ignore
import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore

from google.cloud.devtools.cloudbuild_v1.services.cloud_build import pagers
from google.cloud.devtools.cloudbuild_v1.types import cloudbuild

from .client import CloudBuildClient
from .transports.base import DEFAULT_CLIENT_INFO, CloudBuildTransport
from .transports.grpc_asyncio import CloudBuildGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class CloudBuildAsyncClient:
    """Creates and manages builds on Google Cloud Platform.

    The main concept used by this API is a ``Build``, which describes
    the location of the source to build, how to build the source, and
    where to store the built artifacts, if any.

    A user can list previously-requested builds or get builds by their
    ID to determine the status of the build.
    """

    _client: CloudBuildClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = CloudBuildClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = CloudBuildClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = CloudBuildClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = CloudBuildClient._DEFAULT_UNIVERSE

    build_path = staticmethod(CloudBuildClient.build_path)
    parse_build_path = staticmethod(CloudBuildClient.parse_build_path)
    build_trigger_path = staticmethod(CloudBuildClient.build_trigger_path)
    parse_build_trigger_path = staticmethod(CloudBuildClient.parse_build_trigger_path)
    crypto_key_path = staticmethod(CloudBuildClient.crypto_key_path)
    parse_crypto_key_path = staticmethod(CloudBuildClient.parse_crypto_key_path)
    default_service_account_path = staticmethod(
        CloudBuildClient.default_service_account_path
    )
    parse_default_service_account_path = staticmethod(
        CloudBuildClient.parse_default_service_account_path
    )
    github_enterprise_config_path = staticmethod(
        CloudBuildClient.github_enterprise_config_path
    )
    parse_github_enterprise_config_path = staticmethod(
        CloudBuildClient.parse_github_enterprise_config_path
    )
    git_repository_link_path = staticmethod(CloudBuildClient.git_repository_link_path)
    parse_git_repository_link_path = staticmethod(
        CloudBuildClient.parse_git_repository_link_path
    )
    network_path = staticmethod(CloudBuildClient.network_path)
    parse_network_path = staticmethod(CloudBuildClient.parse_network_path)
    network_attachment_path = staticmethod(CloudBuildClient.network_attachment_path)
    parse_network_attachment_path = staticmethod(
        CloudBuildClient.parse_network_attachment_path
    )
    repository_path = staticmethod(CloudBuildClient.repository_path)
    parse_repository_path = staticmethod(CloudBuildClient.parse_repository_path)
    secret_version_path = staticmethod(CloudBuildClient.secret_version_path)
    parse_secret_version_path = staticmethod(CloudBuildClient.parse_secret_version_path)
    service_account_path = staticmethod(CloudBuildClient.service_account_path)
    parse_service_account_path = staticmethod(
        CloudBuildClient.parse_service_account_path
    )
    subscription_path = staticmethod(CloudBuildClient.subscription_path)
    parse_subscription_path = staticmethod(CloudBuildClient.parse_subscription_path)
    topic_path = staticmethod(CloudBuildClient.topic_path)
    parse_topic_path = staticmethod(CloudBuildClient.parse_topic_path)
    worker_pool_path = staticmethod(CloudBuildClient.worker_pool_path)
    parse_worker_pool_path = staticmethod(CloudBuildClient.parse_worker_pool_path)
    common_billing_account_path = staticmethod(
        CloudBuildClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        CloudBuildClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(CloudBuildClient.common_folder_path)
    parse_common_folder_path = staticmethod(CloudBuildClient.parse_common_folder_path)
    common_organization_path = staticmethod(CloudBuildClient.common_organization_path)
    parse_common_organization_path = staticmethod(
        CloudBuildClient.parse_common_organization_path
    )
    common_project_path = staticmethod(CloudBuildClient.common_project_path)
    parse_common_project_path = staticmethod(CloudBuildClient.parse_common_project_path)
    common_location_path = staticmethod(CloudBuildClient.common_location_path)
    parse_common_location_path = staticmethod(
        CloudBuildClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            CloudBuildAsyncClient: The constructed client.
        """
        sa_info_func = (
            CloudBuildClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(CloudBuildAsyncClient, info, *args, **kwargs)

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
            CloudBuildAsyncClient: The constructed client.
        """
        sa_file_func = (
            CloudBuildClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(CloudBuildAsyncClient, filename, *args, **kwargs)

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

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
        return CloudBuildClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> CloudBuildTransport:
        """Returns the transport used by the client instance.

        Returns:
            CloudBuildTransport: The transport used by the client instance.
        """
        return self._client.transport

    @property
    def api_endpoint(self) -> str:
        """Return the API endpoint used by the client instance.

        Returns:
            str: The API endpoint used by the client instance.
        """
        return self._client._api_endpoint

    @property
    def universe_domain(self) -> str:
        """Return the universe domain used by the client instance.

        Returns:
            str: The universe domain used
                by the client instance.
        """
        return self._client._universe_domain

    get_transport_class = CloudBuildClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[str, CloudBuildTransport, Callable[..., CloudBuildTransport]]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the cloud build async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,CloudBuildTransport,Callable[..., CloudBuildTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the CloudBuildTransport constructor.
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
                default "googleapis.com" universe. Note that ``api_endpoint``
                property still takes precedence; and ``universe_domain`` is
                currently not supported for mTLS.

            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = CloudBuildClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.devtools.cloudbuild_v1.CloudBuildAsyncClient`.",
                extra={
                    "serviceName": "google.devtools.cloudbuild.v1.CloudBuild",
                    "universeDomain": getattr(
                        self._client._transport._credentials, "universe_domain", ""
                    ),
                    "credentialsType": f"{type(self._client._transport._credentials).__module__}.{type(self._client._transport._credentials).__qualname__}",
                    "credentialsInfo": getattr(
                        self.transport._credentials, "get_cred_info", lambda: None
                    )(),
                }
                if hasattr(self._client._transport, "_credentials")
                else {
                    "serviceName": "google.devtools.cloudbuild.v1.CloudBuild",
                    "credentialsType": None,
                },
            )

    async def create_build(
        self,
        request: Optional[Union[cloudbuild.CreateBuildRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        build: Optional[cloudbuild.Build] = None,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Starts a build with the specified configuration.

        This method returns a long-running ``Operation``, which includes
        the build ID. Pass the build ID to ``GetBuild`` to determine the
        build status (such as ``SUCCESS`` or ``FAILURE``).

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.devtools import cloudbuild_v1

            async def sample_create_build():
                # Create a client
                client = cloudbuild_v1.CloudBuildAsyncClient()

                # Initialize request argument(s)
                request = cloudbuild_v1.CreateBuildRequest(
                    project_id="project_id_value",
                )

                # Make the request
                operation = await client.create_build(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.devtools.cloudbuild_v1.types.CreateBuildRequest, dict]]):
                The request object. Request to create a new build.
            project_id (:class:`str`):
                Required. ID of the project.
                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            build (:class:`google.cloud.devtools.cloudbuild_v1.types.Build`):
                Required. Build resource to create.
                This corresponds to the ``build`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            parent (:class:`str`):
                The parent resource where this build will be created.
                Format: ``projects/{project}/locations/{location}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.devtools.cloudbuild_v1.types.Build`
                A build resource in the Cloud Build API.

                   At a high level, a Build describes where to find
                   source code, how to build it (for example, the
                   builder image to run on the source), and where to
                   store the built artifacts.

                   Fields can include the following variables, which
                   will be expanded when the build is created:

                   - $PROJECT_ID: the project ID of the build.
                   - $PROJECT_NUMBER: the project number of the build.
                   - $LOCATION: the location/region of the build.
                   - $BUILD_ID: the autogenerated ID of the build.
                   - $REPO_NAME: the source repository name specified by
                     RepoSource.
                   - $BRANCH_NAME: the branch name specified by
                     RepoSource.
                   - $TAG_NAME: the tag name specified by RepoSource.
                   - $REVISION_ID or $COMMIT_SHA: the commit SHA
                     specified by RepoSource or resolved from the
                     specified branch or tag.
                   - $SHORT_SHA: first 7 characters of $REVISION_ID or
                     $COMMIT_SHA.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [project_id, build, parent]
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
        if not isinstance(request, cloudbuild.CreateBuildRequest):
            request = cloudbuild.CreateBuildRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id
        if build is not None:
            request.build = build
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_build
        ]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^projects/[^/]+/locations/(?P<location>[^/]+)$"
        )
        regex_match = routing_param_regex.match(request.parent)
        if regex_match and regex_match.group("location"):
            header_params["location"] = regex_match.group("location")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            cloudbuild.Build,
            metadata_type=cloudbuild.BuildOperationMetadata,
        )

        # Done; return the response.
        return response

    async def get_build(
        self,
        request: Optional[Union[cloudbuild.GetBuildRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloudbuild.Build:
        r"""Returns information about a previously requested build.

        The ``Build`` that is returned includes its status (such as
        ``SUCCESS``, ``FAILURE``, or ``WORKING``), and timing
        information.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.devtools import cloudbuild_v1

            async def sample_get_build():
                # Create a client
                client = cloudbuild_v1.CloudBuildAsyncClient()

                # Initialize request argument(s)
                request = cloudbuild_v1.GetBuildRequest(
                    project_id="project_id_value",
                    id="id_value",
                )

                # Make the request
                response = await client.get_build(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.devtools.cloudbuild_v1.types.GetBuildRequest, dict]]):
                The request object. Request to get a build.
            project_id (:class:`str`):
                Required. ID of the project.
                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            id (:class:`str`):
                Required. ID of the build.
                This corresponds to the ``id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            name (:class:`str`):
                The name of the ``Build`` to retrieve. Format:
                ``projects/{project}/locations/{location}/builds/{build}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.devtools.cloudbuild_v1.types.Build:
                A build resource in the Cloud Build API.

                   At a high level, a Build describes where to find
                   source code, how to build it (for example, the
                   builder image to run on the source), and where to
                   store the built artifacts.

                   Fields can include the following variables, which
                   will be expanded when the build is created:

                   - $PROJECT_ID: the project ID of the build.
                   - $PROJECT_NUMBER: the project number of the build.
                   - $LOCATION: the location/region of the build.
                   - $BUILD_ID: the autogenerated ID of the build.
                   - $REPO_NAME: the source repository name specified by
                     RepoSource.
                   - $BRANCH_NAME: the branch name specified by
                     RepoSource.
                   - $TAG_NAME: the tag name specified by RepoSource.
                   - $REVISION_ID or $COMMIT_SHA: the commit SHA
                     specified by RepoSource or resolved from the
                     specified branch or tag.
                   - $SHORT_SHA: first 7 characters of $REVISION_ID or
                     $COMMIT_SHA.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [project_id, id, name]
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
        if not isinstance(request, cloudbuild.GetBuildRequest):
            request = cloudbuild.GetBuildRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id
        if id is not None:
            request.id = id
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_build
        ]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^projects/[^/]+/locations/(?P<location>[^/]+)/builds/[^/]+$"
        )
        regex_match = routing_param_regex.match(request.name)
        if regex_match and regex_match.group("location"):
            header_params["location"] = regex_match.group("location")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_builds(
        self,
        request: Optional[Union[cloudbuild.ListBuildsRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        filter: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListBuildsAsyncPager:
        r"""Lists previously requested builds.

        Previously requested builds may still be in-progress, or
        may have finished successfully or unsuccessfully.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.devtools import cloudbuild_v1

            async def sample_list_builds():
                # Create a client
                client = cloudbuild_v1.CloudBuildAsyncClient()

                # Initialize request argument(s)
                request = cloudbuild_v1.ListBuildsRequest(
                    project_id="project_id_value",
                )

                # Make the request
                page_result = client.list_builds(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.devtools.cloudbuild_v1.types.ListBuildsRequest, dict]]):
                The request object. Request to list builds.
            project_id (:class:`str`):
                Required. ID of the project.
                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            filter (:class:`str`):
                The raw filter text to constrain the
                results.

                This corresponds to the ``filter`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.devtools.cloudbuild_v1.services.cloud_build.pagers.ListBuildsAsyncPager:
                Response including listed builds.

                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [project_id, filter]
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
        if not isinstance(request, cloudbuild.ListBuildsRequest):
            request = cloudbuild.ListBuildsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id
        if filter is not None:
            request.filter = filter

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_builds
        ]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^projects/[^/]+/locations/(?P<location>[^/]+)$"
        )
        regex_match = routing_param_regex.match(request.parent)
        if regex_match and regex_match.group("location"):
            header_params["location"] = regex_match.group("location")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListBuildsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def cancel_build(
        self,
        request: Optional[Union[cloudbuild.CancelBuildRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloudbuild.Build:
        r"""Cancels a build in progress.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.devtools import cloudbuild_v1

            async def sample_cancel_build():
                # Create a client
                client = cloudbuild_v1.CloudBuildAsyncClient()

                # Initialize request argument(s)
                request = cloudbuild_v1.CancelBuildRequest(
                    project_id="project_id_value",
                    id="id_value",
                )

                # Make the request
                response = await client.cancel_build(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.devtools.cloudbuild_v1.types.CancelBuildRequest, dict]]):
                The request object. Request to cancel an ongoing build.
            project_id (:class:`str`):
                Required. ID of the project.
                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            id (:class:`str`):
                Required. ID of the build.
                This corresponds to the ``id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            name (:class:`str`):
                The name of the ``Build`` to cancel. Format:
                ``projects/{project}/locations/{location}/builds/{build}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.devtools.cloudbuild_v1.types.Build:
                A build resource in the Cloud Build API.

                   At a high level, a Build describes where to find
                   source code, how to build it (for example, the
                   builder image to run on the source), and where to
                   store the built artifacts.

                   Fields can include the following variables, which
                   will be expanded when the build is created:

                   - $PROJECT_ID: the project ID of the build.
                   - $PROJECT_NUMBER: the project number of the build.
                   - $LOCATION: the location/region of the build.
                   - $BUILD_ID: the autogenerated ID of the build.
                   - $REPO_NAME: the source repository name specified by
                     RepoSource.
                   - $BRANCH_NAME: the branch name specified by
                     RepoSource.
                   - $TAG_NAME: the tag name specified by RepoSource.
                   - $REVISION_ID or $COMMIT_SHA: the commit SHA
                     specified by RepoSource or resolved from the
                     specified branch or tag.
                   - $SHORT_SHA: first 7 characters of $REVISION_ID or
                     $COMMIT_SHA.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [project_id, id, name]
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
        if not isinstance(request, cloudbuild.CancelBuildRequest):
            request = cloudbuild.CancelBuildRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id
        if id is not None:
            request.id = id
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.cancel_build
        ]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^projects/[^/]+/locations/(?P<location>[^/]+)/builds/[^/]+$"
        )
        regex_match = routing_param_regex.match(request.name)
        if regex_match and regex_match.group("location"):
            header_params["location"] = regex_match.group("location")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def retry_build(
        self,
        request: Optional[Union[cloudbuild.RetryBuildRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Creates a new build based on the specified build.

        This method creates a new build using the original build
        request, which may or may not result in an identical build.

        For triggered builds:

        - Triggered builds resolve to a precise revision; therefore a
          retry of a triggered build will result in a build that uses
          the same revision.

        For non-triggered builds that specify ``RepoSource``:

        - If the original build built from the tip of a branch, the
          retried build will build from the tip of that branch, which
          may not be the same revision as the original build.
        - If the original build specified a commit sha or revision ID,
          the retried build will use the identical source.

        For builds that specify ``StorageSource``:

        - If the original build pulled source from Cloud Storage without
          specifying the generation of the object, the new build will
          use the current object, which may be different from the
          original build source.
        - If the original build pulled source from Cloud Storage and
          specified the generation of the object, the new build will
          attempt to use the same object, which may or may not be
          available depending on the bucket's lifecycle management
          settings.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.devtools import cloudbuild_v1

            async def sample_retry_build():
                # Create a client
                client = cloudbuild_v1.CloudBuildAsyncClient()

                # Initialize request argument(s)
                request = cloudbuild_v1.RetryBuildRequest(
                    project_id="project_id_value",
                    id="id_value",
                )

                # Make the request
                operation = await client.retry_build(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.devtools.cloudbuild_v1.types.RetryBuildRequest, dict]]):
                The request object. Specifies a build to retry.
            project_id (:class:`str`):
                Required. ID of the project.
                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            id (:class:`str`):
                Required. Build ID of the original
                build.

                This corresponds to the ``id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            name (:class:`str`):
                The name of the ``Build`` to retry. Format:
                ``projects/{project}/locations/{location}/builds/{build}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.devtools.cloudbuild_v1.types.Build`
                A build resource in the Cloud Build API.

                   At a high level, a Build describes where to find
                   source code, how to build it (for example, the
                   builder image to run on the source), and where to
                   store the built artifacts.

                   Fields can include the following variables, which
                   will be expanded when the build is created:

                   - $PROJECT_ID: the project ID of the build.
                   - $PROJECT_NUMBER: the project number of the build.
                   - $LOCATION: the location/region of the build.
                   - $BUILD_ID: the autogenerated ID of the build.
                   - $REPO_NAME: the source repository name specified by
                     RepoSource.
                   - $BRANCH_NAME: the branch name specified by
                     RepoSource.
                   - $TAG_NAME: the tag name specified by RepoSource.
                   - $REVISION_ID or $COMMIT_SHA: the commit SHA
                     specified by RepoSource or resolved from the
                     specified branch or tag.
                   - $SHORT_SHA: first 7 characters of $REVISION_ID or
                     $COMMIT_SHA.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [project_id, id, name]
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
        if not isinstance(request, cloudbuild.RetryBuildRequest):
            request = cloudbuild.RetryBuildRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id
        if id is not None:
            request.id = id
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.retry_build
        ]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^projects/[^/]+/locations/(?P<location>[^/]+)/builds/[^/]+$"
        )
        regex_match = routing_param_regex.match(request.name)
        if regex_match and regex_match.group("location"):
            header_params["location"] = regex_match.group("location")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            cloudbuild.Build,
            metadata_type=cloudbuild.BuildOperationMetadata,
        )

        # Done; return the response.
        return response

    async def approve_build(
        self,
        request: Optional[Union[cloudbuild.ApproveBuildRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        approval_result: Optional[cloudbuild.ApprovalResult] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Approves or rejects a pending build.

        If approved, the returned long-running operation (LRO)
        will be analogous to the LRO returned from a CreateBuild
        call.

        If rejected, the returned LRO will be immediately done.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.devtools import cloudbuild_v1

            async def sample_approve_build():
                # Create a client
                client = cloudbuild_v1.CloudBuildAsyncClient()

                # Initialize request argument(s)
                request = cloudbuild_v1.ApproveBuildRequest(
                    name="name_value",
                )

                # Make the request
                operation = await client.approve_build(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.devtools.cloudbuild_v1.types.ApproveBuildRequest, dict]]):
                The request object. Request to approve or reject a
                pending build.
            name (:class:`str`):
                Required. Name of the target build. For example:
                "projects/{$project_id}/builds/{$build_id}"

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            approval_result (:class:`google.cloud.devtools.cloudbuild_v1.types.ApprovalResult`):
                Approval decision and metadata.
                This corresponds to the ``approval_result`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.devtools.cloudbuild_v1.types.Build`
                A build resource in the Cloud Build API.

                   At a high level, a Build describes where to find
                   source code, how to build it (for example, the
                   builder image to run on the source), and where to
                   store the built artifacts.

                   Fields can include the following variables, which
                   will be expanded when the build is created:

                   - $PROJECT_ID: the project ID of the build.
                   - $PROJECT_NUMBER: the project number of the build.
                   - $LOCATION: the location/region of the build.
                   - $BUILD_ID: the autogenerated ID of the build.
                   - $REPO_NAME: the source repository name specified by
                     RepoSource.
                   - $BRANCH_NAME: the branch name specified by
                     RepoSource.
                   - $TAG_NAME: the tag name specified by RepoSource.
                   - $REVISION_ID or $COMMIT_SHA: the commit SHA
                     specified by RepoSource or resolved from the
                     specified branch or tag.
                   - $SHORT_SHA: first 7 characters of $REVISION_ID or
                     $COMMIT_SHA.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, approval_result]
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
        if not isinstance(request, cloudbuild.ApproveBuildRequest):
            request = cloudbuild.ApproveBuildRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if approval_result is not None:
            request.approval_result = approval_result

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.approve_build
        ]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^projects/[^/]+/locations/(?P<location>[^/]+)/builds/[^/]+$"
        )
        regex_match = routing_param_regex.match(request.name)
        if regex_match and regex_match.group("location"):
            header_params["location"] = regex_match.group("location")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            cloudbuild.Build,
            metadata_type=cloudbuild.BuildOperationMetadata,
        )

        # Done; return the response.
        return response

    async def create_build_trigger(
        self,
        request: Optional[Union[cloudbuild.CreateBuildTriggerRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        trigger: Optional[cloudbuild.BuildTrigger] = None,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloudbuild.BuildTrigger:
        r"""Creates a new ``BuildTrigger``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.devtools import cloudbuild_v1

            async def sample_create_build_trigger():
                # Create a client
                client = cloudbuild_v1.CloudBuildAsyncClient()

                # Initialize request argument(s)
                trigger = cloudbuild_v1.BuildTrigger()
                trigger.autodetect = True

                request = cloudbuild_v1.CreateBuildTriggerRequest(
                    project_id="project_id_value",
                    trigger=trigger,
                )

                # Make the request
                response = await client.create_build_trigger(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.devtools.cloudbuild_v1.types.CreateBuildTriggerRequest, dict]]):
                The request object. Request to create a new ``BuildTrigger``.
            project_id (:class:`str`):
                Required. ID of the project for which
                to configure automatic builds.

                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            trigger (:class:`google.cloud.devtools.cloudbuild_v1.types.BuildTrigger`):
                Required. ``BuildTrigger`` to create.
                This corresponds to the ``trigger`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            parent (:class:`str`):
                The parent resource where this trigger will be created.
                Format: ``projects/{project}/locations/{location}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.devtools.cloudbuild_v1.types.BuildTrigger:
                Configuration for an automated build
                in response to source repository
                changes.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [project_id, trigger, parent]
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
        if not isinstance(request, cloudbuild.CreateBuildTriggerRequest):
            request = cloudbuild.CreateBuildTriggerRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id
        if trigger is not None:
            request.trigger = trigger
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_build_trigger
        ]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^projects/[^/]+/locations/(?P<location>[^/]+)$"
        )
        regex_match = routing_param_regex.match(request.parent)
        if regex_match and regex_match.group("location"):
            header_params["location"] = regex_match.group("location")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_build_trigger(
        self,
        request: Optional[Union[cloudbuild.GetBuildTriggerRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        trigger_id: Optional[str] = None,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloudbuild.BuildTrigger:
        r"""Returns information about a ``BuildTrigger``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.devtools import cloudbuild_v1

            async def sample_get_build_trigger():
                # Create a client
                client = cloudbuild_v1.CloudBuildAsyncClient()

                # Initialize request argument(s)
                request = cloudbuild_v1.GetBuildTriggerRequest(
                    project_id="project_id_value",
                    trigger_id="trigger_id_value",
                )

                # Make the request
                response = await client.get_build_trigger(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.devtools.cloudbuild_v1.types.GetBuildTriggerRequest, dict]]):
                The request object. Returns the ``BuildTrigger`` with the specified ID.
            project_id (:class:`str`):
                Required. ID of the project that owns
                the trigger.

                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            trigger_id (:class:`str`):
                Required. Identifier (``id`` or ``name``) of the
                ``BuildTrigger`` to get.

                This corresponds to the ``trigger_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            name (:class:`str`):
                The name of the ``Trigger`` to retrieve. Format:
                ``projects/{project}/locations/{location}/triggers/{trigger}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.devtools.cloudbuild_v1.types.BuildTrigger:
                Configuration for an automated build
                in response to source repository
                changes.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [project_id, trigger_id, name]
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
        if not isinstance(request, cloudbuild.GetBuildTriggerRequest):
            request = cloudbuild.GetBuildTriggerRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id
        if trigger_id is not None:
            request.trigger_id = trigger_id
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_build_trigger
        ]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^projects/[^/]+/locations/(?P<location>[^/]+)/triggers/[^/]+$"
        )
        regex_match = routing_param_regex.match(request.name)
        if regex_match and regex_match.group("location"):
            header_params["location"] = regex_match.group("location")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_build_triggers(
        self,
        request: Optional[Union[cloudbuild.ListBuildTriggersRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListBuildTriggersAsyncPager:
        r"""Lists existing ``BuildTrigger``\ s.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.devtools import cloudbuild_v1

            async def sample_list_build_triggers():
                # Create a client
                client = cloudbuild_v1.CloudBuildAsyncClient()

                # Initialize request argument(s)
                request = cloudbuild_v1.ListBuildTriggersRequest(
                    project_id="project_id_value",
                )

                # Make the request
                page_result = client.list_build_triggers(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.devtools.cloudbuild_v1.types.ListBuildTriggersRequest, dict]]):
                The request object. Request to list existing ``BuildTriggers``.
            project_id (:class:`str`):
                Required. ID of the project for which
                to list BuildTriggers.

                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.devtools.cloudbuild_v1.services.cloud_build.pagers.ListBuildTriggersAsyncPager:
                Response containing existing BuildTriggers.

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [project_id]
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
        if not isinstance(request, cloudbuild.ListBuildTriggersRequest):
            request = cloudbuild.ListBuildTriggersRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_build_triggers
        ]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^projects/[^/]+/locations/(?P<location>[^/]+)$"
        )
        regex_match = routing_param_regex.match(request.parent)
        if regex_match and regex_match.group("location"):
            header_params["location"] = regex_match.group("location")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListBuildTriggersAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_build_trigger(
        self,
        request: Optional[Union[cloudbuild.DeleteBuildTriggerRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        trigger_id: Optional[str] = None,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a ``BuildTrigger`` by its project ID and trigger ID.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.devtools import cloudbuild_v1

            async def sample_delete_build_trigger():
                # Create a client
                client = cloudbuild_v1.CloudBuildAsyncClient()

                # Initialize request argument(s)
                request = cloudbuild_v1.DeleteBuildTriggerRequest(
                    project_id="project_id_value",
                    trigger_id="trigger_id_value",
                )

                # Make the request
                await client.delete_build_trigger(request=request)

        Args:
            request (Optional[Union[google.cloud.devtools.cloudbuild_v1.types.DeleteBuildTriggerRequest, dict]]):
                The request object. Request to delete a ``BuildTrigger``.
            project_id (:class:`str`):
                Required. ID of the project that owns
                the trigger.

                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            trigger_id (:class:`str`):
                Required. ID of the ``BuildTrigger`` to delete.
                This corresponds to the ``trigger_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            name (:class:`str`):
                The name of the ``Trigger`` to delete. Format:
                ``projects/{project}/locations/{location}/triggers/{trigger}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
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
        flattened_params = [project_id, trigger_id, name]
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
        if not isinstance(request, cloudbuild.DeleteBuildTriggerRequest):
            request = cloudbuild.DeleteBuildTriggerRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id
        if trigger_id is not None:
            request.trigger_id = trigger_id
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_build_trigger
        ]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^projects/[^/]+/locations/(?P<location>[^/]+)/triggers/[^/]+$"
        )
        regex_match = routing_param_regex.match(request.name)
        if regex_match and regex_match.group("location"):
            header_params["location"] = regex_match.group("location")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def update_build_trigger(
        self,
        request: Optional[Union[cloudbuild.UpdateBuildTriggerRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        trigger_id: Optional[str] = None,
        trigger: Optional[cloudbuild.BuildTrigger] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloudbuild.BuildTrigger:
        r"""Updates a ``BuildTrigger`` by its project ID and trigger ID.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.devtools import cloudbuild_v1

            async def sample_update_build_trigger():
                # Create a client
                client = cloudbuild_v1.CloudBuildAsyncClient()

                # Initialize request argument(s)
                trigger = cloudbuild_v1.BuildTrigger()
                trigger.autodetect = True

                request = cloudbuild_v1.UpdateBuildTriggerRequest(
                    project_id="project_id_value",
                    trigger_id="trigger_id_value",
                    trigger=trigger,
                )

                # Make the request
                response = await client.update_build_trigger(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.devtools.cloudbuild_v1.types.UpdateBuildTriggerRequest, dict]]):
                The request object. Request to update an existing ``BuildTrigger``.
            project_id (:class:`str`):
                Required. ID of the project that owns
                the trigger.

                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            trigger_id (:class:`str`):
                Required. ID of the ``BuildTrigger`` to update.
                This corresponds to the ``trigger_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            trigger (:class:`google.cloud.devtools.cloudbuild_v1.types.BuildTrigger`):
                Required. ``BuildTrigger`` to update.
                This corresponds to the ``trigger`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.devtools.cloudbuild_v1.types.BuildTrigger:
                Configuration for an automated build
                in response to source repository
                changes.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [project_id, trigger_id, trigger]
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
        if not isinstance(request, cloudbuild.UpdateBuildTriggerRequest):
            request = cloudbuild.UpdateBuildTriggerRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id
        if trigger_id is not None:
            request.trigger_id = trigger_id
        if trigger is not None:
            request.trigger = trigger

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_build_trigger
        ]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^projects/[^/]+/locations/(?P<location>[^/]+)/triggers/[^/]+$"
        )
        regex_match = routing_param_regex.match(request.trigger.resource_name)
        if regex_match and regex_match.group("location"):
            header_params["location"] = regex_match.group("location")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def run_build_trigger(
        self,
        request: Optional[Union[cloudbuild.RunBuildTriggerRequest, dict]] = None,
        *,
        project_id: Optional[str] = None,
        trigger_id: Optional[str] = None,
        source: Optional[cloudbuild.RepoSource] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Runs a ``BuildTrigger`` at a particular source revision.

        To run a regional or global trigger, use the POST request that
        includes the location endpoint in the path (ex.
        v1/projects/{projectId}/locations/{region}/triggers/{triggerId}:run).
        The POST request that does not include the location endpoint in
        the path can only be used when running global triggers.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.devtools import cloudbuild_v1

            async def sample_run_build_trigger():
                # Create a client
                client = cloudbuild_v1.CloudBuildAsyncClient()

                # Initialize request argument(s)
                request = cloudbuild_v1.RunBuildTriggerRequest(
                    project_id="project_id_value",
                    trigger_id="trigger_id_value",
                )

                # Make the request
                operation = await client.run_build_trigger(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.devtools.cloudbuild_v1.types.RunBuildTriggerRequest, dict]]):
                The request object. Specifies a build trigger to run and
                the source to use.
            project_id (:class:`str`):
                Required. ID of the project.
                This corresponds to the ``project_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            trigger_id (:class:`str`):
                Required. ID of the trigger.
                This corresponds to the ``trigger_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            source (:class:`google.cloud.devtools.cloudbuild_v1.types.RepoSource`):
                Source to build against this trigger.
                Branch and tag names cannot consist of
                regular expressions.

                This corresponds to the ``source`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.devtools.cloudbuild_v1.types.Build`
                A build resource in the Cloud Build API.

                   At a high level, a Build describes where to find
                   source code, how to build it (for example, the
                   builder image to run on the source), and where to
                   store the built artifacts.

                   Fields can include the following variables, which
                   will be expanded when the build is created:

                   - $PROJECT_ID: the project ID of the build.
                   - $PROJECT_NUMBER: the project number of the build.
                   - $LOCATION: the location/region of the build.
                   - $BUILD_ID: the autogenerated ID of the build.
                   - $REPO_NAME: the source repository name specified by
                     RepoSource.
                   - $BRANCH_NAME: the branch name specified by
                     RepoSource.
                   - $TAG_NAME: the tag name specified by RepoSource.
                   - $REVISION_ID or $COMMIT_SHA: the commit SHA
                     specified by RepoSource or resolved from the
                     specified branch or tag.
                   - $SHORT_SHA: first 7 characters of $REVISION_ID or
                     $COMMIT_SHA.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [project_id, trigger_id, source]
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
        if not isinstance(request, cloudbuild.RunBuildTriggerRequest):
            request = cloudbuild.RunBuildTriggerRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_id is not None:
            request.project_id = project_id
        if trigger_id is not None:
            request.trigger_id = trigger_id
        if source is not None:
            request.source = source

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.run_build_trigger
        ]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^projects/[^/]+/locations/(?P<location>[^/]+)/triggers/[^/]+$"
        )
        regex_match = routing_param_regex.match(request.name)
        if regex_match and regex_match.group("location"):
            header_params["location"] = regex_match.group("location")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            cloudbuild.Build,
            metadata_type=cloudbuild.BuildOperationMetadata,
        )

        # Done; return the response.
        return response

    async def receive_trigger_webhook(
        self,
        request: Optional[Union[cloudbuild.ReceiveTriggerWebhookRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloudbuild.ReceiveTriggerWebhookResponse:
        r"""ReceiveTriggerWebhook [Experimental] is called when the API
        receives a webhook request targeted at a specific trigger.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.devtools import cloudbuild_v1

            async def sample_receive_trigger_webhook():
                # Create a client
                client = cloudbuild_v1.CloudBuildAsyncClient()

                # Initialize request argument(s)
                request = cloudbuild_v1.ReceiveTriggerWebhookRequest(
                )

                # Make the request
                response = await client.receive_trigger_webhook(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.devtools.cloudbuild_v1.types.ReceiveTriggerWebhookRequest, dict]]):
                The request object. ReceiveTriggerWebhookRequest [Experimental] is the
                request object accepted by the ReceiveTriggerWebhook
                method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.devtools.cloudbuild_v1.types.ReceiveTriggerWebhookResponse:
                ReceiveTriggerWebhookResponse [Experimental] is the response object for the
                   ReceiveTriggerWebhook method.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, cloudbuild.ReceiveTriggerWebhookRequest):
            request = cloudbuild.ReceiveTriggerWebhookRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.receive_trigger_webhook
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    ("project_id", request.project_id),
                    ("trigger", request.trigger),
                )
            ),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_worker_pool(
        self,
        request: Optional[Union[cloudbuild.CreateWorkerPoolRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        worker_pool: Optional[cloudbuild.WorkerPool] = None,
        worker_pool_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Creates a ``WorkerPool``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.devtools import cloudbuild_v1

            async def sample_create_worker_pool():
                # Create a client
                client = cloudbuild_v1.CloudBuildAsyncClient()

                # Initialize request argument(s)
                request = cloudbuild_v1.CreateWorkerPoolRequest(
                    parent="parent_value",
                    worker_pool_id="worker_pool_id_value",
                )

                # Make the request
                operation = await client.create_worker_pool(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.devtools.cloudbuild_v1.types.CreateWorkerPoolRequest, dict]]):
                The request object. Request to create a new ``WorkerPool``.
            parent (:class:`str`):
                Required. The parent resource where this worker pool
                will be created. Format:
                ``projects/{project}/locations/{location}``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            worker_pool (:class:`google.cloud.devtools.cloudbuild_v1.types.WorkerPool`):
                Required. ``WorkerPool`` resource to create.
                This corresponds to the ``worker_pool`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            worker_pool_id (:class:`str`):
                Required. Immutable. The ID to use for the
                ``WorkerPool``, which will become the final component of
                the resource name.

                This value should be 1-63 characters, and valid
                characters are /[a-z][0-9]-/.

                This corresponds to the ``worker_pool_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.devtools.cloudbuild_v1.types.WorkerPool`
                Configuration for a WorkerPool.

                   Cloud Build owns and maintains a pool of workers for
                   general use and have no access to a project's private
                   network. By default, builds submitted to Cloud Build
                   will use a worker from this pool.

                   If your build needs access to resources on a private
                   network, create and use a WorkerPool to run your
                   builds. Private \`WorkerPool`s give your builds
                   access to any single VPC network that you administer,
                   including any on-prem resources connected to that VPC
                   network. For an overview of private pools, see
                   [Private pools
                   overview](https://cloud.google.com/build/docs/private-pools/private-pools-overview).

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, worker_pool, worker_pool_id]
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
        if not isinstance(request, cloudbuild.CreateWorkerPoolRequest):
            request = cloudbuild.CreateWorkerPoolRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if worker_pool is not None:
            request.worker_pool = worker_pool
        if worker_pool_id is not None:
            request.worker_pool_id = worker_pool_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_worker_pool
        ]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^projects/[^/]+/locations/(?P<location>[^/]+)$"
        )
        regex_match = routing_param_regex.match(request.parent)
        if regex_match and regex_match.group("location"):
            header_params["location"] = regex_match.group("location")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            cloudbuild.WorkerPool,
            metadata_type=cloudbuild.CreateWorkerPoolOperationMetadata,
        )

        # Done; return the response.
        return response

    async def get_worker_pool(
        self,
        request: Optional[Union[cloudbuild.GetWorkerPoolRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloudbuild.WorkerPool:
        r"""Returns details of a ``WorkerPool``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.devtools import cloudbuild_v1

            async def sample_get_worker_pool():
                # Create a client
                client = cloudbuild_v1.CloudBuildAsyncClient()

                # Initialize request argument(s)
                request = cloudbuild_v1.GetWorkerPoolRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_worker_pool(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.devtools.cloudbuild_v1.types.GetWorkerPoolRequest, dict]]):
                The request object. Request to get a ``WorkerPool`` with the specified name.
            name (:class:`str`):
                Required. The name of the ``WorkerPool`` to retrieve.
                Format:
                ``projects/{project}/locations/{location}/workerPools/{workerPool}``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.devtools.cloudbuild_v1.types.WorkerPool:
                Configuration for a WorkerPool.

                   Cloud Build owns and maintains a pool of workers for
                   general use and have no access to a project's private
                   network. By default, builds submitted to Cloud Build
                   will use a worker from this pool.

                   If your build needs access to resources on a private
                   network, create and use a WorkerPool to run your
                   builds. Private \`WorkerPool`s give your builds
                   access to any single VPC network that you administer,
                   including any on-prem resources connected to that VPC
                   network. For an overview of private pools, see
                   [Private pools
                   overview](https://cloud.google.com/build/docs/private-pools/private-pools-overview).

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
        if not isinstance(request, cloudbuild.GetWorkerPoolRequest):
            request = cloudbuild.GetWorkerPoolRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_worker_pool
        ]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^projects/[^/]+/locations/(?P<location>[^/]+)/workerPools/[^/]+$"
        )
        regex_match = routing_param_regex.match(request.name)
        if regex_match and regex_match.group("location"):
            header_params["location"] = regex_match.group("location")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_worker_pool(
        self,
        request: Optional[Union[cloudbuild.DeleteWorkerPoolRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Deletes a ``WorkerPool``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.devtools import cloudbuild_v1

            async def sample_delete_worker_pool():
                # Create a client
                client = cloudbuild_v1.CloudBuildAsyncClient()

                # Initialize request argument(s)
                request = cloudbuild_v1.DeleteWorkerPoolRequest(
                    name="name_value",
                )

                # Make the request
                operation = await client.delete_worker_pool(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.devtools.cloudbuild_v1.types.DeleteWorkerPoolRequest, dict]]):
                The request object. Request to delete a ``WorkerPool``.
            name (:class:`str`):
                Required. The name of the ``WorkerPool`` to delete.
                Format:
                ``projects/{project}/locations/{location}/workerPools/{workerPool}``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation_async.AsyncOperation:
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
        if not isinstance(request, cloudbuild.DeleteWorkerPoolRequest):
            request = cloudbuild.DeleteWorkerPoolRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_worker_pool
        ]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^projects/[^/]+/locations/(?P<location>[^/]+)/workerPools/[^/]+$"
        )
        regex_match = routing_param_regex.match(request.name)
        if regex_match and regex_match.group("location"):
            header_params["location"] = regex_match.group("location")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=cloudbuild.DeleteWorkerPoolOperationMetadata,
        )

        # Done; return the response.
        return response

    async def update_worker_pool(
        self,
        request: Optional[Union[cloudbuild.UpdateWorkerPoolRequest, dict]] = None,
        *,
        worker_pool: Optional[cloudbuild.WorkerPool] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Updates a ``WorkerPool``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.devtools import cloudbuild_v1

            async def sample_update_worker_pool():
                # Create a client
                client = cloudbuild_v1.CloudBuildAsyncClient()

                # Initialize request argument(s)
                request = cloudbuild_v1.UpdateWorkerPoolRequest(
                )

                # Make the request
                operation = await client.update_worker_pool(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.devtools.cloudbuild_v1.types.UpdateWorkerPoolRequest, dict]]):
                The request object. Request to update a ``WorkerPool``.
            worker_pool (:class:`google.cloud.devtools.cloudbuild_v1.types.WorkerPool`):
                Required. The ``WorkerPool`` to update.

                The ``name`` field is used to identify the
                ``WorkerPool`` to update. Format:
                ``projects/{project}/locations/{location}/workerPools/{workerPool}``.

                This corresponds to the ``worker_pool`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Optional. A mask specifying which fields in
                ``worker_pool`` to update.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.devtools.cloudbuild_v1.types.WorkerPool`
                Configuration for a WorkerPool.

                   Cloud Build owns and maintains a pool of workers for
                   general use and have no access to a project's private
                   network. By default, builds submitted to Cloud Build
                   will use a worker from this pool.

                   If your build needs access to resources on a private
                   network, create and use a WorkerPool to run your
                   builds. Private \`WorkerPool`s give your builds
                   access to any single VPC network that you administer,
                   including any on-prem resources connected to that VPC
                   network. For an overview of private pools, see
                   [Private pools
                   overview](https://cloud.google.com/build/docs/private-pools/private-pools-overview).

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [worker_pool, update_mask]
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
        if not isinstance(request, cloudbuild.UpdateWorkerPoolRequest):
            request = cloudbuild.UpdateWorkerPoolRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if worker_pool is not None:
            request.worker_pool = worker_pool
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_worker_pool
        ]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^projects/[^/]+/locations/(?P<location>[^/]+)/workerPools/[^/]+$"
        )
        regex_match = routing_param_regex.match(request.worker_pool.name)
        if regex_match and regex_match.group("location"):
            header_params["location"] = regex_match.group("location")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            cloudbuild.WorkerPool,
            metadata_type=cloudbuild.UpdateWorkerPoolOperationMetadata,
        )

        # Done; return the response.
        return response

    async def list_worker_pools(
        self,
        request: Optional[Union[cloudbuild.ListWorkerPoolsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListWorkerPoolsAsyncPager:
        r"""Lists ``WorkerPool``\ s.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.devtools import cloudbuild_v1

            async def sample_list_worker_pools():
                # Create a client
                client = cloudbuild_v1.CloudBuildAsyncClient()

                # Initialize request argument(s)
                request = cloudbuild_v1.ListWorkerPoolsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_worker_pools(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.devtools.cloudbuild_v1.types.ListWorkerPoolsRequest, dict]]):
                The request object. Request to list ``WorkerPool``\ s.
            parent (:class:`str`):
                Required. The parent of the collection of
                ``WorkerPools``. Format:
                ``projects/{project}/locations/{location}``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.devtools.cloudbuild_v1.services.cloud_build.pagers.ListWorkerPoolsAsyncPager:
                Response containing existing WorkerPools.

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
        if not isinstance(request, cloudbuild.ListWorkerPoolsRequest):
            request = cloudbuild.ListWorkerPoolsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_worker_pools
        ]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^projects/[^/]+/locations/(?P<location>[^/]+)$"
        )
        regex_match = routing_param_regex.match(request.parent)
        if regex_match and regex_match.group("location"):
            header_params["location"] = regex_match.group("location")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListWorkerPoolsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_default_service_account(
        self,
        request: Optional[
            Union[cloudbuild.GetDefaultServiceAccountRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> cloudbuild.DefaultServiceAccount:
        r"""Returns the ``DefaultServiceAccount`` used by the project.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud.devtools import cloudbuild_v1

            async def sample_get_default_service_account():
                # Create a client
                client = cloudbuild_v1.CloudBuildAsyncClient()

                # Initialize request argument(s)
                request = cloudbuild_v1.GetDefaultServiceAccountRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_default_service_account(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.devtools.cloudbuild_v1.types.GetDefaultServiceAccountRequest, dict]]):
                The request object. Returns the default service account that will be used
                for ``Builds``.
            name (:class:`str`):
                Required. The name of the ``DefaultServiceAccount`` to
                retrieve. Format:
                ``projects/{project}/locations/{location}/defaultServiceAccount``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.devtools.cloudbuild_v1.types.DefaultServiceAccount:
                The default service account used for Builds.
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
        if not isinstance(request, cloudbuild.GetDefaultServiceAccountRequest):
            request = cloudbuild.GetDefaultServiceAccountRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_default_service_account
        ]

        header_params: dict[str, str] = {}

        routing_param_regex = re.compile(
            "^projects/[^/]+/locations/(?P<location>[^/]+)/defaultServiceAccount$"
        )
        regex_match = routing_param_regex.match(request.name)
        if regex_match and regex_match.group("location"):
            header_params["location"] = regex_match.group("location")

        if header_params:
            metadata = tuple(metadata) + (
                gapic_v1.routing_header.to_grpc_metadata(header_params),
            )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self) -> "CloudBuildAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("CloudBuildAsyncClient",)
