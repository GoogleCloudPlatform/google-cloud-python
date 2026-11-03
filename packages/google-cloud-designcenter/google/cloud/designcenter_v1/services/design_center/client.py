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

from google.cloud.designcenter_v1 import gapic_version as package_version
from google.cloud.designcenter_v1._compat import (
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
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
from google.cloud.apphub_v1.types import application, attributes
from google.cloud.apphub_v1.types import application as gca_application
from google.cloud.location import locations_pb2  # type: ignore
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore

from google.cloud.designcenter_v1.services.design_center import pagers
from google.cloud.designcenter_v1.types import (
    apphub_integration_messages,
    assessment,
    authoring,
    authoring_messages,
    best_practices,
    best_practices_messages,
    catalog_management,
    catalog_management_messages,
    deployment,
    deployment_messages,
    deployment_resources,
    designcenter,
    enums,
    export,
    iac,
    ingestion,
    metadata_,
    parameters,
    sharing,
    sharing_messages,
)

from .transports.base import DEFAULT_CLIENT_INFO, DesignCenterTransport
from .transports.grpc import DesignCenterGrpcTransport
from .transports.grpc_asyncio import DesignCenterGrpcAsyncIOTransport
from .transports.rest import DesignCenterRestTransport


class DesignCenterClientMeta(type):
    """Metaclass for the DesignCenter client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = OrderedDict()  # type: Dict[str, Type[DesignCenterTransport]]
    _transport_registry["grpc"] = DesignCenterGrpcTransport
    _transport_registry["grpc_asyncio"] = DesignCenterGrpcAsyncIOTransport
    _transport_registry["rest"] = DesignCenterRestTransport

    def get_transport_class(
        cls,
        label: Optional[str] = None,
    ) -> Type[DesignCenterTransport]:
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


class DesignCenterClient(metaclass=DesignCenterClientMeta):
    """Service describing handlers for resources"""

    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = "designcenter.googleapis.com"
    DEFAULT_MTLS_ENDPOINT = get_default_mtls_endpoint(DEFAULT_ENDPOINT)

    _DEFAULT_ENDPOINT_TEMPLATE = "designcenter.{UNIVERSE_DOMAIN}"
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
            DesignCenterClient: The constructed client.
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
            DesignCenterClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> DesignCenterTransport:
        """Returns the transport used by the client instance.

        Returns:
            DesignCenterTransport: The transport used by the client
                instance.
        """
        return self._transport

    @staticmethod
    def application_path(
        project: str,
        location: str,
        space: str,
        application: str,
    ) -> str:
        """Returns a fully-qualified application string."""
        return "projects/{project}/locations/{location}/spaces/{space}/applications/{application}".format(
            project=project,
            location=location,
            space=space,
            application=application,
        )

    @staticmethod
    def parse_application_path(path: str) -> Dict[str, str]:
        """Parses a application path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/spaces/(?P<space>.+?)/applications/(?P<application>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def application_template_path(
        project: str,
        location: str,
        space: str,
        application_template: str,
    ) -> str:
        """Returns a fully-qualified application_template string."""
        return "projects/{project}/locations/{location}/spaces/{space}/applicationTemplates/{application_template}".format(
            project=project,
            location=location,
            space=space,
            application_template=application_template,
        )

    @staticmethod
    def parse_application_template_path(path: str) -> Dict[str, str]:
        """Parses a application_template path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/spaces/(?P<space>.+?)/applicationTemplates/(?P<application_template>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def application_template_revision_path(
        project: str,
        location: str,
        space: str,
        application_template: str,
        revision: str,
    ) -> str:
        """Returns a fully-qualified application_template_revision string."""
        return "projects/{project}/locations/{location}/spaces/{space}/applicationTemplates/{application_template}/revisions/{revision}".format(
            project=project,
            location=location,
            space=space,
            application_template=application_template,
            revision=revision,
        )

    @staticmethod
    def parse_application_template_revision_path(path: str) -> Dict[str, str]:
        """Parses a application_template_revision path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/spaces/(?P<space>.+?)/applicationTemplates/(?P<application_template>.+?)/revisions/(?P<revision>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def application_template_system_revision_path(
        project: str,
        location: str,
        space: str,
        application_template: str,
        system_revision: str,
    ) -> str:
        """Returns a fully-qualified application_template_system_revision string."""
        return "projects/{project}/locations/{location}/spaces/{space}/applicationTemplates/{application_template}/systemRevisions/{system_revision}".format(
            project=project,
            location=location,
            space=space,
            application_template=application_template,
            system_revision=system_revision,
        )

    @staticmethod
    def parse_application_template_system_revision_path(path: str) -> Dict[str, str]:
        """Parses a application_template_system_revision path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/spaces/(?P<space>.+?)/applicationTemplates/(?P<application_template>.+?)/systemRevisions/(?P<system_revision>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def catalog_path(
        project: str,
        location: str,
        space: str,
        catalog: str,
    ) -> str:
        """Returns a fully-qualified catalog string."""
        return "projects/{project}/locations/{location}/spaces/{space}/catalogs/{catalog}".format(
            project=project,
            location=location,
            space=space,
            catalog=catalog,
        )

    @staticmethod
    def parse_catalog_path(path: str) -> Dict[str, str]:
        """Parses a catalog path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/spaces/(?P<space>.+?)/catalogs/(?P<catalog>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def catalog_template_path(
        project: str,
        location: str,
        space: str,
        catalog: str,
        catalog_template: str,
    ) -> str:
        """Returns a fully-qualified catalog_template string."""
        return "projects/{project}/locations/{location}/spaces/{space}/catalogs/{catalog}/templates/{catalog_template}".format(
            project=project,
            location=location,
            space=space,
            catalog=catalog,
            catalog_template=catalog_template,
        )

    @staticmethod
    def parse_catalog_template_path(path: str) -> Dict[str, str]:
        """Parses a catalog_template path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/spaces/(?P<space>.+?)/catalogs/(?P<catalog>.+?)/templates/(?P<catalog_template>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def catalog_template_revision_path(
        project: str,
        location: str,
        space: str,
        catalog: str,
        catalog_template: str,
        revision: str,
    ) -> str:
        """Returns a fully-qualified catalog_template_revision string."""
        return "projects/{project}/locations/{location}/spaces/{space}/catalogs/{catalog}/templates/{catalog_template}/revisions/{revision}".format(
            project=project,
            location=location,
            space=space,
            catalog=catalog,
            catalog_template=catalog_template,
            revision=revision,
        )

    @staticmethod
    def parse_catalog_template_revision_path(path: str) -> Dict[str, str]:
        """Parses a catalog_template_revision path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/spaces/(?P<space>.+?)/catalogs/(?P<catalog>.+?)/templates/(?P<catalog_template>.+?)/revisions/(?P<revision>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def cloud_control_path(
        organization: str,
        location: str,
        cloud_control: str,
    ) -> str:
        """Returns a fully-qualified cloud_control string."""
        return "organizations/{organization}/locations/{location}/cloudControls/{cloud_control}".format(
            organization=organization,
            location=location,
            cloud_control=cloud_control,
        )

    @staticmethod
    def parse_cloud_control_path(path: str) -> Dict[str, str]:
        """Parses a cloud_control path into its component segments."""
        m = re.match(
            r"^organizations/(?P<organization>.+?)/locations/(?P<location>.+?)/cloudControls/(?P<cloud_control>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def component_path(
        project: str,
        location: str,
        space: str,
        application_template: str,
        component: str,
    ) -> str:
        """Returns a fully-qualified component string."""
        return "projects/{project}/locations/{location}/spaces/{space}/applicationTemplates/{application_template}/components/{component}".format(
            project=project,
            location=location,
            space=space,
            application_template=application_template,
            component=component,
        )

    @staticmethod
    def parse_component_path(path: str) -> Dict[str, str]:
        """Parses a component path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/spaces/(?P<space>.+?)/applicationTemplates/(?P<application_template>.+?)/components/(?P<component>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def connection_path(
        project: str,
        location: str,
        space: str,
        application_template: str,
        component: str,
        connection: str,
    ) -> str:
        """Returns a fully-qualified connection string."""
        return "projects/{project}/locations/{location}/spaces/{space}/applicationTemplates/{application_template}/components/{component}/connections/{connection}".format(
            project=project,
            location=location,
            space=space,
            application_template=application_template,
            component=component,
            connection=connection,
        )

    @staticmethod
    def parse_connection_path(path: str) -> Dict[str, str]:
        """Parses a connection path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/spaces/(?P<space>.+?)/applicationTemplates/(?P<application_template>.+?)/components/(?P<component>.+?)/connections/(?P<connection>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def deployment_path(
        project: str,
        location: str,
        deployment: str,
    ) -> str:
        """Returns a fully-qualified deployment string."""
        return (
            "projects/{project}/locations/{location}/deployments/{deployment}".format(
                project=project,
                location=location,
                deployment=deployment,
            )
        )

    @staticmethod
    def parse_deployment_path(path: str) -> Dict[str, str]:
        """Parses a deployment path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/deployments/(?P<deployment>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def deployment_group_path(
        project: str,
        location: str,
        deployment_group: str,
    ) -> str:
        """Returns a fully-qualified deployment_group string."""
        return "projects/{project}/locations/{location}/deploymentGroups/{deployment_group}".format(
            project=project,
            location=location,
            deployment_group=deployment_group,
        )

    @staticmethod
    def parse_deployment_group_path(path: str) -> Dict[str, str]:
        """Parses a deployment_group path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/deploymentGroups/(?P<deployment_group>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def git_repository_link_path(
        project: str,
        location: str,
        connection: str,
        git_repository_link: str,
    ) -> str:
        """Returns a fully-qualified git_repository_link string."""
        return "projects/{project}/locations/{location}/connections/{connection}/gitRepositoryLinks/{git_repository_link}".format(
            project=project,
            location=location,
            connection=connection,
            git_repository_link=git_repository_link,
        )

    @staticmethod
    def parse_git_repository_link_path(path: str) -> Dict[str, str]:
        """Parses a git_repository_link path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/connections/(?P<connection>.+?)/gitRepositoryLinks/(?P<git_repository_link>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def policy_path(
        project: str,
        location: str,
        space: str,
        application_template: str,
        policy: str,
    ) -> str:
        """Returns a fully-qualified policy string."""
        return "projects/{project}/locations/{location}/spaces/{space}/applicationTemplates/{application_template}/policies/{policy}".format(
            project=project,
            location=location,
            space=space,
            application_template=application_template,
            policy=policy,
        )

    @staticmethod
    def parse_policy_path(path: str) -> Dict[str, str]:
        """Parses a policy path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/spaces/(?P<space>.+?)/applicationTemplates/(?P<application_template>.+?)/policies/(?P<policy>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def preview_path(
        project: str,
        location: str,
        preview: str,
    ) -> str:
        """Returns a fully-qualified preview string."""
        return "projects/{project}/locations/{location}/previews/{preview}".format(
            project=project,
            location=location,
            preview=preview,
        )

    @staticmethod
    def parse_preview_path(path: str) -> Dict[str, str]:
        """Parses a preview path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/previews/(?P<preview>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def role_path(
        organization: str,
        role: str,
    ) -> str:
        """Returns a fully-qualified role string."""
        return "organizations/{organization}/roles/{role}".format(
            organization=organization,
            role=role,
        )

    @staticmethod
    def parse_role_path(path: str) -> Dict[str, str]:
        """Parses a role path into its component segments."""
        m = re.match(r"^organizations/(?P<organization>.+?)/roles/(?P<role>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def service_account_path(
        project: str,
        service_account: str,
    ) -> str:
        """Returns a fully-qualified service_account string."""
        return "projects/{project}/serviceAccounts/{service_account}".format(
            project=project,
            service_account=service_account,
        )

    @staticmethod
    def parse_service_account_path(path: str) -> Dict[str, str]:
        """Parses a service_account path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/serviceAccounts/(?P<service_account>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def share_path(
        project: str,
        location: str,
        space: str,
        catalog: str,
        share: str,
    ) -> str:
        """Returns a fully-qualified share string."""
        return "projects/{project}/locations/{location}/spaces/{space}/catalogs/{catalog}/shares/{share}".format(
            project=project,
            location=location,
            space=space,
            catalog=catalog,
            share=share,
        )

    @staticmethod
    def parse_share_path(path: str) -> Dict[str, str]:
        """Parses a share path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/spaces/(?P<space>.+?)/catalogs/(?P<catalog>.+?)/shares/(?P<share>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def shared_template_path(
        project: str,
        location: str,
        space: str,
        shared_template: str,
    ) -> str:
        """Returns a fully-qualified shared_template string."""
        return "projects/{project}/locations/{location}/spaces/{space}/sharedTemplates/{shared_template}".format(
            project=project,
            location=location,
            space=space,
            shared_template=shared_template,
        )

    @staticmethod
    def parse_shared_template_path(path: str) -> Dict[str, str]:
        """Parses a shared_template path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/spaces/(?P<space>.+?)/sharedTemplates/(?P<shared_template>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def shared_template_revision_path(
        project: str,
        location: str,
        space: str,
        shared_template: str,
        revision: str,
    ) -> str:
        """Returns a fully-qualified shared_template_revision string."""
        return "projects/{project}/locations/{location}/spaces/{space}/sharedTemplates/{shared_template}/revisions/{revision}".format(
            project=project,
            location=location,
            space=space,
            shared_template=shared_template,
            revision=revision,
        )

    @staticmethod
    def parse_shared_template_revision_path(path: str) -> Dict[str, str]:
        """Parses a shared_template_revision path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/spaces/(?P<space>.+?)/sharedTemplates/(?P<shared_template>.+?)/revisions/(?P<revision>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def space_path(
        project: str,
        location: str,
        space: str,
    ) -> str:
        """Returns a fully-qualified space string."""
        return "projects/{project}/locations/{location}/spaces/{space}".format(
            project=project,
            location=location,
            space=space,
        )

    @staticmethod
    def parse_space_path(path: str) -> Dict[str, str]:
        """Parses a space path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/spaces/(?P<space>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def worker_pool_path(
        project: str,
        location: str,
        worker_pool: str,
    ) -> str:
        """Returns a fully-qualified worker_pool string."""
        return (
            "projects/{project}/locations/{location}/workerPools/{worker_pool}".format(
                project=project,
                location=location,
                worker_pool=worker_pool,
            )
        )

    @staticmethod
    def parse_worker_pool_path(path: str) -> Dict[str, str]:
        """Parses a worker_pool path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/workerPools/(?P<worker_pool>.+?)$",
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
            Union[str, DesignCenterTransport, Callable[..., DesignCenterTransport]]
        ] = None,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the design center client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,DesignCenterTransport,Callable[..., DesignCenterTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the DesignCenterTransport constructor.
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
        self._client_cert_source = DesignCenterClient._get_client_cert_source(
            self._client_options.client_cert_source, self._use_client_cert
        )
        self._universe_domain = get_universe_domain(
            universe_domain_opt,
            self._universe_domain_env,
            default_universe=DesignCenterClient._DEFAULT_UNIVERSE,
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
        transport_provided = isinstance(transport, DesignCenterTransport)
        if transport_provided:
            # transport is a DesignCenterTransport instance.
            if credentials or self._client_options.credentials_file or api_key_value:
                raise ValueError(
                    "When providing a transport instance, "
                    "provide its credentials directly."
                )
            if self._client_options.scopes:
                raise ValueError(
                    "When providing a transport instance, provide its scopes directly."
                )
            self._transport = cast(DesignCenterTransport, transport)
            self._api_endpoint = self._transport.host

        self._api_endpoint = self._api_endpoint or get_api_endpoint(
            api_override=self._client_options.api_endpoint,
            universe_domain=self._universe_domain,
            default_universe=DesignCenterClient._DEFAULT_UNIVERSE,
            default_mtls_endpoint=DesignCenterClient.DEFAULT_MTLS_ENDPOINT,
            default_endpoint_template=DesignCenterClient._DEFAULT_ENDPOINT_TEMPLATE,
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
                Type[DesignCenterTransport], Callable[..., DesignCenterTransport]
            ] = (
                DesignCenterClient.get_transport_class(transport)
                if isinstance(transport, str) or transport is None
                else cast(Callable[..., DesignCenterTransport], transport)
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
                    "Created client `google.cloud.designcenter_v1.DesignCenterClient`.",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
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
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "credentialsType": None,
                    },
                )

    def get_space(
        self,
        request: Optional[
            Union[catalog_management_messages.GetSpaceRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> catalog_management.Space:
        r"""Gets details about a space.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_get_space():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.GetSpaceRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_space(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.GetSpaceRequest, dict]):
                The request object. Results returned from
                projects.locations.spaces.get.
            name (str):
                Required. The space name.
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
            google.cloud.designcenter_v1.types.Space:
                Space is a top level resource for
                managing teams building applications
                through Application Design Center.

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
        if not isinstance(request, catalog_management_messages.GetSpaceRequest):
            request = catalog_management_messages.GetSpaceRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_space]

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

    def list_spaces(
        self,
        request: Optional[
            Union[catalog_management_messages.ListSpacesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListSpacesPager:
        r"""Lists spaces in a given project and location.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_list_spaces():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.ListSpacesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_spaces(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.ListSpacesRequest, dict]):
                The request object. Message for requesting a list of
                spaces.
            parent (str):
                Required. The name of the parent
                resource, for which spaces are listed.

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
            google.cloud.designcenter_v1.services.design_center.pagers.ListSpacesPager:
                Results returned from
                projects.locations.spaces.list.
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
        if not isinstance(request, catalog_management_messages.ListSpacesRequest):
            request = catalog_management_messages.ListSpacesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_spaces]

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
        response = pagers.ListSpacesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_space(
        self,
        request: Optional[
            Union[catalog_management_messages.CreateSpaceRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        space: Optional[catalog_management.Space] = None,
        space_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> catalog_management.Space:
        r"""Creates a space.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_create_space():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.CreateSpaceRequest(
                    parent="parent_value",
                    space_id="space_id_value",
                )

                # Make the request
                response = client.create_space(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.CreateSpaceRequest, dict]):
                The request object. Message for creating a space.
            parent (str):
                Required. The parent in which to
                create a space.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            space (google.cloud.designcenter_v1.types.Space):
                Required. The space to create.
                This corresponds to the ``space`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            space_id (str):
                Required. The ID of the space to
                create.

                This corresponds to the ``space_id`` field
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
            google.cloud.designcenter_v1.types.Space:
                Space is a top level resource for
                managing teams building applications
                through Application Design Center.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, space, space_id]
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
        if not isinstance(request, catalog_management_messages.CreateSpaceRequest):
            request = catalog_management_messages.CreateSpaceRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if space is not None:
                request.space = space
            if space_id is not None:
                request.space_id = space_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_space]

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

    def update_space(
        self,
        request: Optional[
            Union[catalog_management_messages.UpdateSpaceRequest, dict]
        ] = None,
        *,
        space: Optional[catalog_management.Space] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> catalog_management.Space:
        r"""Updates a space.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_update_space():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.UpdateSpaceRequest(
                )

                # Make the request
                response = client.update_space(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.UpdateSpaceRequest, dict]):
                The request object. Message for updating a space.
            space (google.cloud.designcenter_v1.types.Space):
                Required. The space to update.
                This corresponds to the ``space`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Optional. The fields to overwrite in
                the space update. If you don't provide a
                mask, all fields are overwritten.

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
            google.cloud.designcenter_v1.types.Space:
                Space is a top level resource for
                managing teams building applications
                through Application Design Center.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [space, update_mask]
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
        if not isinstance(request, catalog_management_messages.UpdateSpaceRequest):
            request = catalog_management_messages.UpdateSpaceRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if space is not None:
                request.space = space
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_space]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("space.name", request.space.name),)
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

    def delete_space(
        self,
        request: Optional[
            Union[catalog_management_messages.DeleteSpaceRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a space.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_delete_space():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.DeleteSpaceRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_space(request=request)

        Args:
            request (Union[google.cloud.designcenter_v1.types.DeleteSpaceRequest, dict]):
                The request object. Message for deleting a space.
            name (str):
                Required. The space name.
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
        if not isinstance(request, catalog_management_messages.DeleteSpaceRequest):
            request = catalog_management_messages.DeleteSpaceRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_space]

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

    def get_application_template(
        self,
        request: Optional[
            Union[authoring_messages.GetApplicationTemplateRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> authoring.ApplicationTemplate:
        r"""Gets details about an application template.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_get_application_template():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.GetApplicationTemplateRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_application_template(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.GetApplicationTemplateRequest, dict]):
                The request object. Message for getting an application
                template.
            name (str):
                Required. The application template
                name.

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
            google.cloud.designcenter_v1.types.ApplicationTemplate:
                Application template resource.
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
        if not isinstance(request, authoring_messages.GetApplicationTemplateRequest):
            request = authoring_messages.GetApplicationTemplateRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_application_template]

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

    def list_application_templates(
        self,
        request: Optional[
            Union[authoring_messages.ListApplicationTemplatesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListApplicationTemplatesPager:
        r"""Lists application templates in a given space.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_list_application_templates():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.ListApplicationTemplatesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_application_templates(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.ListApplicationTemplatesRequest, dict]):
                The request object. Message for requesting a list of
                application templates.
            parent (str):
                Required. The parent resource from
                which to list application templates.

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
            google.cloud.designcenter_v1.services.design_center.pagers.ListApplicationTemplatesPager:
                Message for response to listing
                application templates.
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
        if not isinstance(request, authoring_messages.ListApplicationTemplatesRequest):
            request = authoring_messages.ListApplicationTemplatesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_application_templates
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
        response = pagers.ListApplicationTemplatesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_application_template(
        self,
        request: Optional[
            Union[authoring_messages.CreateApplicationTemplateRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        application_template: Optional[authoring.ApplicationTemplate] = None,
        application_template_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> authoring.ApplicationTemplate:
        r"""Creates an application template.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_create_application_template():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.CreateApplicationTemplateRequest(
                    parent="parent_value",
                    application_template_id="application_template_id_value",
                )

                # Make the request
                response = client.create_application_template(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.CreateApplicationTemplateRequest, dict]):
                The request object. Message for creating an application
                template.
            parent (str):
                Required. The parent resource in
                which to create the application
                template.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            application_template (google.cloud.designcenter_v1.types.ApplicationTemplate):
                Required. The application template to
                create.

                This corresponds to the ``application_template`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            application_template_id (str):
                Required. The ID of the application
                template to create.

                This corresponds to the ``application_template_id`` field
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
            google.cloud.designcenter_v1.types.ApplicationTemplate:
                Application template resource.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, application_template, application_template_id]
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
        if not isinstance(request, authoring_messages.CreateApplicationTemplateRequest):
            request = authoring_messages.CreateApplicationTemplateRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if application_template is not None:
                request.application_template = application_template
            if application_template_id is not None:
                request.application_template_id = application_template_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.create_application_template
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

    def update_application_template(
        self,
        request: Optional[
            Union[authoring_messages.UpdateApplicationTemplateRequest, dict]
        ] = None,
        *,
        application_template: Optional[authoring.ApplicationTemplate] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> authoring.ApplicationTemplate:
        r"""Updates an application template.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_update_application_template():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.UpdateApplicationTemplateRequest(
                )

                # Make the request
                response = client.update_application_template(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.UpdateApplicationTemplateRequest, dict]):
                The request object. Message for updating an application
                template.
            application_template (google.cloud.designcenter_v1.types.ApplicationTemplate):
                Required. The application template to
                update.

                This corresponds to the ``application_template`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Optional. The fields to overwrite in the application
                template update. The fields specified in the update_mask
                are relative to the resource, not the full request. A
                field will be overwritten if it is in the mask. If you
                don't provide a mask, all fields are overwritten.

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
            google.cloud.designcenter_v1.types.ApplicationTemplate:
                Application template resource.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [application_template, update_mask]
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
        if not isinstance(request, authoring_messages.UpdateApplicationTemplateRequest):
            request = authoring_messages.UpdateApplicationTemplateRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if application_template is not None:
                request.application_template = application_template
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.update_application_template
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("application_template.name", request.application_template.name),)
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

    def import_application_template(
        self,
        request: Optional[
            Union[authoring_messages.ImportApplicationTemplateRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        application_template_revision_uri: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> authoring.ApplicationTemplate:
        r"""Imports to an existing application template from a
        given shared template.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_import_application_template():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.ImportApplicationTemplateRequest(
                    application_template_revision_uri="application_template_revision_uri_value",
                    name="name_value",
                )

                # Make the request
                response = client.import_application_template(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.ImportApplicationTemplateRequest, dict]):
                The request object. Request message for
                ImportApplicationTemplate method.
            name (str):
                Required. The name of the application
                template.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            application_template_revision_uri (str):
                Optional. The source URI for
                application template revision.

                This corresponds to the ``application_template_revision_uri`` field
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
            google.cloud.designcenter_v1.types.ApplicationTemplate:
                Application template resource.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, application_template_revision_uri]
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
        if not isinstance(request, authoring_messages.ImportApplicationTemplateRequest):
            request = authoring_messages.ImportApplicationTemplateRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name
            if application_template_revision_uri is not None:
                request.application_template_revision_uri = (
                    application_template_revision_uri
                )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.import_application_template
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

    def delete_application_template(
        self,
        request: Optional[
            Union[authoring_messages.DeleteApplicationTemplateRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes an application template.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_delete_application_template():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.DeleteApplicationTemplateRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_application_template(request=request)

        Args:
            request (Union[google.cloud.designcenter_v1.types.DeleteApplicationTemplateRequest, dict]):
                The request object. Message for deleting an application
                template.
            name (str):
                Required. The application template
                name.

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
        if not isinstance(request, authoring_messages.DeleteApplicationTemplateRequest):
            request = authoring_messages.DeleteApplicationTemplateRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.delete_application_template
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

    def commit_application_template(
        self,
        request: Optional[
            Union[authoring_messages.CommitApplicationTemplateRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> authoring.ApplicationTemplateRevision:
        r"""Commits an application template to create a new
        revision.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_commit_application_template():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.CommitApplicationTemplateRequest(
                    name="name_value",
                )

                # Make the request
                response = client.commit_application_template(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.CommitApplicationTemplateRequest, dict]):
                The request object. Request message for
                CommitApplicationTemplate method.
            name (str):
                Required. The name of the application
                template.

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
            google.cloud.designcenter_v1.types.ApplicationTemplateRevision:
                Application template revision
                resource.

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
        if not isinstance(request, authoring_messages.CommitApplicationTemplateRequest):
            request = authoring_messages.CommitApplicationTemplateRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.commit_application_template
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

    def snapshot_application_template(
        self,
        request: Optional[
            Union[authoring_messages.SnapshotApplicationTemplateRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Snapshots an application template to create a new
        revision asynchronously.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_snapshot_application_template():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.SnapshotApplicationTemplateRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.snapshot_application_template(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.SnapshotApplicationTemplateRequest, dict]):
                The request object. Message for snapshotting an
                application template asynchronously.
            name (str):
                Required. The name of the application
                template.

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
                :class:`google.cloud.designcenter_v1.types.SnapshotApplicationTemplateResponse`
                Response message for snapshotting an application
                template asynchronously.

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
            request, authoring_messages.SnapshotApplicationTemplateRequest
        ):
            request = authoring_messages.SnapshotApplicationTemplateRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.snapshot_application_template
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

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            authoring_messages.SnapshotApplicationTemplateResponse,
            metadata_type=designcenter.OperationMetadata,
        )

        # Done; return the response.
        return response

    def generate_application_template_ia_c(
        self,
        request: Optional[
            Union[authoring_messages.GenerateApplicationTemplateIaCRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> authoring_messages.GenerateApplicationTemplateIaCResponse:
        r"""Generates Terraform files for an application
        template. This is a SYNCHRONOUS operation and returns
        the generated IaC directly in the response. It
        does NOT download external module sources; it only uses
        remote sources.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_generate_application_template_ia_c():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.GenerateApplicationTemplateIaCRequest(
                    name="name_value",
                )

                # Make the request
                response = client.generate_application_template_ia_c(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.GenerateApplicationTemplateIaCRequest, dict]):
                The request object. Request message for
                GenerateApplicationTemplateIaC method.
            name (str):
                Required. The name of the application
                template.

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
            google.cloud.designcenter_v1.types.GenerateApplicationTemplateIaCResponse:
                Response message for
                GenerateApplicationTemplateIaC method.

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
            request, authoring_messages.GenerateApplicationTemplateIaCRequest
        ):
            request = authoring_messages.GenerateApplicationTemplateIaCRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.generate_application_template_ia_c
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

    def export_application_template_ia_c(
        self,
        request: Optional[
            Union[authoring_messages.ExportApplicationTemplateIaCRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Exports Terraform files for an application template.
        The generated modules can have remote sources or local
        sources downloaded from remote. This is an ASYNCHRONOUS
        operation that returns a Long Running Operation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_export_application_template_ia_c():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.ExportApplicationTemplateIaCRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.export_application_template_ia_c(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.ExportApplicationTemplateIaCRequest, dict]):
                The request object. Request message for
                ExportApplicationTemplateIaC method.
            name (str):
                Required. The name of the application
                template.

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
                :class:`google.cloud.designcenter_v1.types.ExportApplicationTemplateIaCResponse`
                Response message for ExportApplicationTemplateIaC
                method.

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
            request, authoring_messages.ExportApplicationTemplateIaCRequest
        ):
            request = authoring_messages.ExportApplicationTemplateIaCRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.export_application_template_ia_c
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

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            authoring_messages.ExportApplicationTemplateIaCResponse,
            metadata_type=designcenter.OperationMetadata,
        )

        # Done; return the response.
        return response

    def generate_application_template_revision_ia_c(
        self,
        request: Optional[
            Union[
                authoring_messages.GenerateApplicationTemplateRevisionIaCRequest, dict
            ]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> authoring_messages.GenerateApplicationTemplateRevisionIaCResponse:
        r"""Generates Terraform files for an application template
        revision. This is a SYNCHRONOUS operation and returns
        the generated IaC directly in the response. It
        does NOT download external module sources; it only uses
        remote sources.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_generate_application_template_revision_ia_c():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.GenerateApplicationTemplateRevisionIaCRequest(
                    name="name_value",
                )

                # Make the request
                response = client.generate_application_template_revision_ia_c(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.GenerateApplicationTemplateRevisionIaCRequest, dict]):
                The request object. Request message for
                GenerateApplicationTemplateRevisionIaC
                method.
            name (str):
                Required. The name of the application
                template revision.

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
            google.cloud.designcenter_v1.types.GenerateApplicationTemplateRevisionIaCResponse:
                Response message for
                GenerateApplicationTemplateRevisionIaC
                method.

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
            request, authoring_messages.GenerateApplicationTemplateRevisionIaCRequest
        ):
            request = authoring_messages.GenerateApplicationTemplateRevisionIaCRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.generate_application_template_revision_ia_c
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

    def export_application_template_revision_ia_c(
        self,
        request: Optional[
            Union[authoring_messages.ExportApplicationTemplateRevisionIaCRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Exports Terraform files for an application template
        revision. The generated modules can have remote sources
        or local sources downloaded from remote. This is an
        ASYNCHRONOUS operation that returns a Long Running
        Operation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_export_application_template_revision_ia_c():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.ExportApplicationTemplateRevisionIaCRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.export_application_template_revision_ia_c(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.ExportApplicationTemplateRevisionIaCRequest, dict]):
                The request object. Request message for
                ExportApplicationTemplateRevisionIaC
                method.
            name (str):
                Required. The name of the application
                template revision.

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
                :class:`google.cloud.designcenter_v1.types.ExportApplicationTemplateRevisionIaCResponse`
                Response message for
                ExportApplicationTemplateRevisionIaC method.

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
            request, authoring_messages.ExportApplicationTemplateRevisionIaCRequest
        ):
            request = authoring_messages.ExportApplicationTemplateRevisionIaCRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.export_application_template_revision_ia_c
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

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            authoring_messages.ExportApplicationTemplateRevisionIaCResponse,
            metadata_type=designcenter.OperationMetadata,
        )

        # Done; return the response.
        return response

    def get_component(
        self,
        request: Optional[Union[authoring_messages.GetComponentRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> authoring.Component:
        r"""Gets details about a Component.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_get_component():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.GetComponentRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_component(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.GetComponentRequest, dict]):
                The request object. Message for getting a component.
            name (str):
                Required. The component name.
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
            google.cloud.designcenter_v1.types.Component:
                Component resource.
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
        if not isinstance(request, authoring_messages.GetComponentRequest):
            request = authoring_messages.GetComponentRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_component]

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

    def list_components(
        self,
        request: Optional[Union[authoring_messages.ListComponentsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListComponentsPager:
        r"""Lists components in an application template.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_list_components():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.ListComponentsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_components(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.ListComponentsRequest, dict]):
                The request object. Message for requesting a list of
                components.
            parent (str):
                Required. The parent resource from
                which the list of components is
                requested.

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
            google.cloud.designcenter_v1.services.design_center.pagers.ListComponentsPager:
                Message for response to listing
                components.
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
        if not isinstance(request, authoring_messages.ListComponentsRequest):
            request = authoring_messages.ListComponentsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_components]

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
        response = pagers.ListComponentsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_component(
        self,
        request: Optional[
            Union[authoring_messages.CreateComponentRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        component: Optional[authoring.Component] = None,
        component_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> authoring.Component:
        r"""Creates a component.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_create_component():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                component = designcenter_v1.Component()
                component.shared_template_revision_uri = "shared_template_revision_uri_value"

                request = designcenter_v1.CreateComponentRequest(
                    parent="parent_value",
                    component_id="component_id_value",
                    component=component,
                )

                # Make the request
                response = client.create_component(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.CreateComponentRequest, dict]):
                The request object. Message for creating a component.
            parent (str):
                Required. The parent resource in
                which to create the component.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            component (google.cloud.designcenter_v1.types.Component):
                Required. The component to create.
                This corresponds to the ``component`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            component_id (str):
                Required. The ID of the component to
                create.

                This corresponds to the ``component_id`` field
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
            google.cloud.designcenter_v1.types.Component:
                Component resource.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, component, component_id]
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
        if not isinstance(request, authoring_messages.CreateComponentRequest):
            request = authoring_messages.CreateComponentRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if component is not None:
                request.component = component
            if component_id is not None:
                request.component_id = component_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_component]

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

    def update_component(
        self,
        request: Optional[
            Union[authoring_messages.UpdateComponentRequest, dict]
        ] = None,
        *,
        component: Optional[authoring.Component] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> authoring.Component:
        r"""Updates a component.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_update_component():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                component = designcenter_v1.Component()
                component.shared_template_revision_uri = "shared_template_revision_uri_value"

                request = designcenter_v1.UpdateComponentRequest(
                    component=component,
                )

                # Make the request
                response = client.update_component(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.UpdateComponentRequest, dict]):
                The request object. Message for updating a component.
            component (google.cloud.designcenter_v1.types.Component):
                Required. The component to update.
                This corresponds to the ``component`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Optional. The fields to overwrite in
                the component update. If you don't
                provide a mask, all fields are
                overwritten.

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
            google.cloud.designcenter_v1.types.Component:
                Component resource.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [component, update_mask]
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
        if not isinstance(request, authoring_messages.UpdateComponentRequest):
            request = authoring_messages.UpdateComponentRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if component is not None:
                request.component = component
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_component]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("component.name", request.component.name),)
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

    def delete_component(
        self,
        request: Optional[
            Union[authoring_messages.DeleteComponentRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a component.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_delete_component():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.DeleteComponentRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_component(request=request)

        Args:
            request (Union[google.cloud.designcenter_v1.types.DeleteComponentRequest, dict]):
                The request object. Message for deleting a component.
            name (str):
                Required. The component name.
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
        if not isinstance(request, authoring_messages.DeleteComponentRequest):
            request = authoring_messages.DeleteComponentRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_component]

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

    def get_connection(
        self,
        request: Optional[Union[authoring_messages.GetConnectionRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> authoring.Connection:
        r"""Gets details about a connection.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_get_connection():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.GetConnectionRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_connection(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.GetConnectionRequest, dict]):
                The request object. Message for getting a connection.
            name (str):
                Required. Name of the resource
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
            google.cloud.designcenter_v1.types.Connection:
                Connection resource.
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
        if not isinstance(request, authoring_messages.GetConnectionRequest):
            request = authoring_messages.GetConnectionRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_connection]

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

    def list_connections(
        self,
        request: Optional[
            Union[authoring_messages.ListConnectionsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListConnectionsPager:
        r"""Lists connections in an application template.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_list_connections():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.ListConnectionsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_connections(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.ListConnectionsRequest, dict]):
                The request object. Message for requesting a list of
                connections.
            parent (str):
                Required. The parent resource from
                which to request a list of connections.

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
            google.cloud.designcenter_v1.services.design_center.pagers.ListConnectionsPager:
                Message for response to listing
                connections.
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
        if not isinstance(request, authoring_messages.ListConnectionsRequest):
            request = authoring_messages.ListConnectionsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_connections]

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
        response = pagers.ListConnectionsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_connection(
        self,
        request: Optional[
            Union[authoring_messages.CreateConnectionRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        connection: Optional[authoring.Connection] = None,
        connection_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> authoring.Connection:
        r"""Creates a connection.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_create_connection():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                connection = designcenter_v1.Connection()
                connection.destination_component_uri = "destination_component_uri_value"

                request = designcenter_v1.CreateConnectionRequest(
                    parent="parent_value",
                    connection_id="connection_id_value",
                    connection=connection,
                )

                # Make the request
                response = client.create_connection(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.CreateConnectionRequest, dict]):
                The request object. Message for creating a connection.
            parent (str):
                Required. The parent resource in
                which to create a connection.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            connection (google.cloud.designcenter_v1.types.Connection):
                Required. The connection to create.
                This corresponds to the ``connection`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            connection_id (str):
                Required. The ID of the connection to
                create.

                This corresponds to the ``connection_id`` field
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
            google.cloud.designcenter_v1.types.Connection:
                Connection resource.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, connection, connection_id]
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
        if not isinstance(request, authoring_messages.CreateConnectionRequest):
            request = authoring_messages.CreateConnectionRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if connection is not None:
                request.connection = connection
            if connection_id is not None:
                request.connection_id = connection_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_connection]

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

    def update_connection(
        self,
        request: Optional[
            Union[authoring_messages.UpdateConnectionRequest, dict]
        ] = None,
        *,
        connection: Optional[authoring.Connection] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> authoring.Connection:
        r"""Updates a connection.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_update_connection():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                connection = designcenter_v1.Connection()
                connection.destination_component_uri = "destination_component_uri_value"

                request = designcenter_v1.UpdateConnectionRequest(
                    connection=connection,
                )

                # Make the request
                response = client.update_connection(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.UpdateConnectionRequest, dict]):
                The request object. Message for updating a connection.
            connection (google.cloud.designcenter_v1.types.Connection):
                Required. The connection to update.
                This corresponds to the ``connection`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Optional. Fields to overwrite in the connection update.
                The fields specified in the update_mask are relative to
                the resource, not the full request. A field will be
                overwritten if it is in the mask. If you don't provide a
                mask, all fields are overwritten.

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
            google.cloud.designcenter_v1.types.Connection:
                Connection resource.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [connection, update_mask]
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
        if not isinstance(request, authoring_messages.UpdateConnectionRequest):
            request = authoring_messages.UpdateConnectionRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if connection is not None:
                request.connection = connection
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_connection]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("connection.name", request.connection.name),)
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

    def delete_connection(
        self,
        request: Optional[
            Union[authoring_messages.DeleteConnectionRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a connection.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_delete_connection():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.DeleteConnectionRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_connection(request=request)

        Args:
            request (Union[google.cloud.designcenter_v1.types.DeleteConnectionRequest, dict]):
                The request object. Message for deleting a connection.
            name (str):
                Required. The connection name.
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
        if not isinstance(request, authoring_messages.DeleteConnectionRequest):
            request = authoring_messages.DeleteConnectionRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_connection]

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

    def get_application_template_revision(
        self,
        request: Optional[
            Union[authoring_messages.GetApplicationTemplateRevisionRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> authoring.ApplicationTemplateRevision:
        r"""Gets details about an application template revision.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_get_application_template_revision():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.GetApplicationTemplateRevisionRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_application_template_revision(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.GetApplicationTemplateRevisionRequest, dict]):
                The request object. Message for getting an application
                template revision.
            name (str):
                Required. The application template
                revision name.

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
            google.cloud.designcenter_v1.types.ApplicationTemplateRevision:
                Application template revision
                resource.

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
            request, authoring_messages.GetApplicationTemplateRevisionRequest
        ):
            request = authoring_messages.GetApplicationTemplateRevisionRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.get_application_template_revision
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

    def list_application_template_revisions(
        self,
        request: Optional[
            Union[authoring_messages.ListApplicationTemplateRevisionsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListApplicationTemplateRevisionsPager:
        r"""Lists application template revisions in a given
        application template.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_list_application_template_revisions():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.ListApplicationTemplateRevisionsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_application_template_revisions(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.ListApplicationTemplateRevisionsRequest, dict]):
                The request object. Message for requesting a list of
                application template revisions.
            parent (str):
                Required. The parent from which to
                list application template revisions.

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
            google.cloud.designcenter_v1.services.design_center.pagers.ListApplicationTemplateRevisionsPager:
                Message for response to listing
                application template revisions.
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
            request, authoring_messages.ListApplicationTemplateRevisionsRequest
        ):
            request = authoring_messages.ListApplicationTemplateRevisionsRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_application_template_revisions
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
        response = pagers.ListApplicationTemplateRevisionsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def delete_application_template_revision(
        self,
        request: Optional[
            Union[authoring_messages.DeleteApplicationTemplateRevisionRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes an application template revision.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_delete_application_template_revision():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.DeleteApplicationTemplateRevisionRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_application_template_revision(request=request)

        Args:
            request (Union[google.cloud.designcenter_v1.types.DeleteApplicationTemplateRevisionRequest, dict]):
                The request object. Message for deleting an application
                template revision.
            name (str):
                Required. The application template
                revision name.

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
            request, authoring_messages.DeleteApplicationTemplateRevisionRequest
        ):
            request = authoring_messages.DeleteApplicationTemplateRevisionRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.delete_application_template_revision
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

    def get_catalog(
        self,
        request: Optional[
            Union[catalog_management_messages.GetCatalogRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> catalog_management.Catalog:
        r"""Gets details about a catalog.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_get_catalog():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.GetCatalogRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_catalog(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.GetCatalogRequest, dict]):
                The request object. Message for getting a catalog.
            name (str):
                Required. The catalog name in the following format:
                ``projects/$project/locations/$location/spaces/$space/catalogs/$catalog``

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
            google.cloud.designcenter_v1.types.Catalog:
                A catalog is a collection of
                templates.

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
        if not isinstance(request, catalog_management_messages.GetCatalogRequest):
            request = catalog_management_messages.GetCatalogRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_catalog]

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

    def list_catalogs(
        self,
        request: Optional[
            Union[catalog_management_messages.ListCatalogsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListCatalogsPager:
        r"""Lists catalogs in a given space.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_list_catalogs():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.ListCatalogsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_catalogs(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.ListCatalogsRequest, dict]):
                The request object. Message for requesting a list of
                catalogs.
            parent (str):
                Required. The parent space from which catalogs are
                listed. Format:
                ``projects/$project/locations/$location/spaces/$space``

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
            google.cloud.designcenter_v1.services.design_center.pagers.ListCatalogsPager:
                Results returned from catalogs.list.

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
        if not isinstance(request, catalog_management_messages.ListCatalogsRequest):
            request = catalog_management_messages.ListCatalogsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_catalogs]

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
        response = pagers.ListCatalogsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_catalog(
        self,
        request: Optional[
            Union[catalog_management_messages.CreateCatalogRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        catalog: Optional[catalog_management.Catalog] = None,
        catalog_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> catalog_management.Catalog:
        r"""Creates a catalog.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_create_catalog():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.CreateCatalogRequest(
                    parent="parent_value",
                    catalog_id="catalog_id_value",
                )

                # Make the request
                response = client.create_catalog(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.CreateCatalogRequest, dict]):
                The request object. Message for creating a catalog.
            parent (str):
                Required. The parent space in which a catalog is created
                in the following format:
                ``projects/$project/locations/$location/spaces/$space``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            catalog (google.cloud.designcenter_v1.types.Catalog):
                Required. The catalog to create.
                This corresponds to the ``catalog`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            catalog_id (str):
                Required. The ID of the catalog to
                create.

                This corresponds to the ``catalog_id`` field
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
            google.cloud.designcenter_v1.types.Catalog:
                A catalog is a collection of
                templates.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, catalog, catalog_id]
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
        if not isinstance(request, catalog_management_messages.CreateCatalogRequest):
            request = catalog_management_messages.CreateCatalogRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if catalog is not None:
                request.catalog = catalog
            if catalog_id is not None:
                request.catalog_id = catalog_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_catalog]

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

    def update_catalog(
        self,
        request: Optional[
            Union[catalog_management_messages.UpdateCatalogRequest, dict]
        ] = None,
        *,
        catalog: Optional[catalog_management.Catalog] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> catalog_management.Catalog:
        r"""Updates a catalog.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_update_catalog():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.UpdateCatalogRequest(
                )

                # Make the request
                response = client.update_catalog(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.UpdateCatalogRequest, dict]):
                The request object. Message for updating a catalog.
            catalog (google.cloud.designcenter_v1.types.Catalog):
                Required. The catalog to update.
                This corresponds to the ``catalog`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Optional. The fields to overwrite in
                the catalog update. If you don't provide
                a mask, all fields are overwritten.

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
            google.cloud.designcenter_v1.types.Catalog:
                A catalog is a collection of
                templates.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [catalog, update_mask]
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
        if not isinstance(request, catalog_management_messages.UpdateCatalogRequest):
            request = catalog_management_messages.UpdateCatalogRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if catalog is not None:
                request.catalog = catalog
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_catalog]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("catalog.name", request.catalog.name),)
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

    def delete_catalog(
        self,
        request: Optional[
            Union[catalog_management_messages.DeleteCatalogRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes a catalog.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_delete_catalog():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.DeleteCatalogRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_catalog(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.DeleteCatalogRequest, dict]):
                The request object. Message for deleting a catalog.
            name (str):
                Required. The catalog name in the following format:
                ``projects/$project/locations/$location/spaces/$space/catalogs/$catalog``

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
        if not isinstance(request, catalog_management_messages.DeleteCatalogRequest):
            request = catalog_management_messages.DeleteCatalogRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_catalog]

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
            metadata_type=designcenter.OperationMetadata,
        )

        # Done; return the response.
        return response

    def create_catalog_template(
        self,
        request: Optional[
            Union[catalog_management_messages.CreateCatalogTemplateRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        catalog_template: Optional[catalog_management.CatalogTemplate] = None,
        catalog_template_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> catalog_management.CatalogTemplate:
        r"""Adds a template to a catalog.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_create_catalog_template():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                catalog_template = designcenter_v1.CatalogTemplate()
                catalog_template.template_category = "INSTANCE_TEMPLATE"

                request = designcenter_v1.CreateCatalogTemplateRequest(
                    parent="parent_value",
                    catalog_template_id="catalog_template_id_value",
                    catalog_template=catalog_template,
                )

                # Make the request
                response = client.create_catalog_template(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.CreateCatalogTemplateRequest, dict]):
                The request object. Message for creating a catalog
                template.
            parent (str):
                Required. The parent resource in
                which the catalog template is created.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            catalog_template (google.cloud.designcenter_v1.types.CatalogTemplate):
                Required. The catalog template to
                create.

                This corresponds to the ``catalog_template`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            catalog_template_id (str):
                Required. The ID of the catalog
                template to create. The ID is appended
                to the catalog template's name.

                This corresponds to the ``catalog_template_id`` field
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
            google.cloud.designcenter_v1.types.CatalogTemplate:
                A template inside a catalog.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, catalog_template, catalog_template_id]
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
            request, catalog_management_messages.CreateCatalogTemplateRequest
        ):
            request = catalog_management_messages.CreateCatalogTemplateRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if catalog_template is not None:
                request.catalog_template = catalog_template
            if catalog_template_id is not None:
                request.catalog_template_id = catalog_template_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_catalog_template]

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

    def get_catalog_template(
        self,
        request: Optional[
            Union[catalog_management_messages.GetCatalogTemplateRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> catalog_management.CatalogTemplate:
        r"""Gets a catalog template.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_get_catalog_template():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.GetCatalogTemplateRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_catalog_template(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.GetCatalogTemplateRequest, dict]):
                The request object. Message for getting a catalog
                template resource.
            name (str):
                Required. The catalog template name in the following
                format:
                ``projects/$project/locations/$location/spaces/$space/catalogs/$catalog/templates/$template``

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
            google.cloud.designcenter_v1.types.CatalogTemplate:
                A template inside a catalog.
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
            request, catalog_management_messages.GetCatalogTemplateRequest
        ):
            request = catalog_management_messages.GetCatalogTemplateRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_catalog_template]

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

    def list_catalog_templates(
        self,
        request: Optional[
            Union[catalog_management_messages.ListCatalogTemplatesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListCatalogTemplatesPager:
        r"""Lists catalog templates.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_list_catalog_templates():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.ListCatalogTemplatesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_catalog_templates(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.ListCatalogTemplatesRequest, dict]):
                The request object. Message for requesting a list of
                catalog templates.
            parent (str):
                Required. The parent from which the catalog templates
                are listed in the following format:
                ``projects/$project/locations/$location/spaces/$space/catalogs/$catalog``

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
            google.cloud.designcenter_v1.services.design_center.pagers.ListCatalogTemplatesPager:
                Message for response to listing
                catalog templates.
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
            request, catalog_management_messages.ListCatalogTemplatesRequest
        ):
            request = catalog_management_messages.ListCatalogTemplatesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_catalog_templates]

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
        response = pagers.ListCatalogTemplatesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def update_catalog_template(
        self,
        request: Optional[
            Union[catalog_management_messages.UpdateCatalogTemplateRequest, dict]
        ] = None,
        *,
        catalog_template: Optional[catalog_management.CatalogTemplate] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> catalog_management.CatalogTemplate:
        r"""Updates a catalog template resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_update_catalog_template():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                catalog_template = designcenter_v1.CatalogTemplate()
                catalog_template.template_category = "INSTANCE_TEMPLATE"

                request = designcenter_v1.UpdateCatalogTemplateRequest(
                    catalog_template=catalog_template,
                )

                # Make the request
                response = client.update_catalog_template(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.UpdateCatalogTemplateRequest, dict]):
                The request object. Message for updating a catalog
                template.
            catalog_template (google.cloud.designcenter_v1.types.CatalogTemplate):
                Required. The catalog template to update. Format:
                ``projects/$project/locations/$location/spaces/$space/catalogs/$catalog/templates/$template``

                This corresponds to the ``catalog_template`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Optional. The fields to overwrite in the catalog
                template update. The fields specified in the update_mask
                are relative to the resource, not the full request. A
                field will be overwritten if it is in the mask. If you
                don't provide a mask, all fields are overwritten.

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
            google.cloud.designcenter_v1.types.CatalogTemplate:
                A template inside a catalog.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [catalog_template, update_mask]
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
            request, catalog_management_messages.UpdateCatalogTemplateRequest
        ):
            request = catalog_management_messages.UpdateCatalogTemplateRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if catalog_template is not None:
                request.catalog_template = catalog_template
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_catalog_template]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("catalog_template.name", request.catalog_template.name),)
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

    def delete_catalog_template(
        self,
        request: Optional[
            Union[catalog_management_messages.DeleteCatalogTemplateRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes a catalog template.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_delete_catalog_template():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.DeleteCatalogTemplateRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_catalog_template(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.DeleteCatalogTemplateRequest, dict]):
                The request object. Message for deleting a catalog
                template.
            name (str):
                Required. The catalog template name. Format:
                ``projects/$project/locations/$location/spaces/$space/catalogs/$catalog/templates/$template``

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
        if not isinstance(
            request, catalog_management_messages.DeleteCatalogTemplateRequest
        ):
            request = catalog_management_messages.DeleteCatalogTemplateRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_catalog_template]

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
            metadata_type=designcenter.OperationMetadata,
        )

        # Done; return the response.
        return response

    def create_share(
        self,
        request: Optional[Union[sharing_messages.CreateShareRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        share: Optional[sharing.Share] = None,
        share_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Shares a catalog from one space to another space.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_create_share():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                share = designcenter_v1.Share()
                share.destination_space = "destination_space_value"

                request = designcenter_v1.CreateShareRequest(
                    parent="parent_value",
                    share_id="share_id_value",
                    share=share,
                )

                # Make the request
                operation = client.create_share(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.CreateShareRequest, dict]):
                The request object. Message for creating a share of a
                catalog.
            parent (str):
                Required. The parent resource in
                which shares are created.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            share (google.cloud.designcenter_v1.types.Share):
                Required. The share to create.
                This corresponds to the ``share`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            share_id (str):
                Required. The ID of the share to
                create.

                This corresponds to the ``share_id`` field
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
                :class:`google.cloud.designcenter_v1.types.Share` A
                catalog share between spaces.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, share, share_id]
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
        if not isinstance(request, sharing_messages.CreateShareRequest):
            request = sharing_messages.CreateShareRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if share is not None:
                request.share = share
            if share_id is not None:
                request.share_id = share_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_share]

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
            sharing.Share,
            metadata_type=designcenter.OperationMetadata,
        )

        # Done; return the response.
        return response

    def list_shares(
        self,
        request: Optional[Union[sharing_messages.ListSharesRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListSharesPager:
        r"""Lists catalog share objects for the space.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_list_shares():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.ListSharesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_shares(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.ListSharesRequest, dict]):
                The request object. Message for listing shares of a
                catalog.
            parent (str):
                Required. The parent resource from
                which a list of shares is requested.

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
            google.cloud.designcenter_v1.services.design_center.pagers.ListSharesPager:
                Message for response to listing
                shares of a catalog.
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
        if not isinstance(request, sharing_messages.ListSharesRequest):
            request = sharing_messages.ListSharesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_shares]

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
        response = pagers.ListSharesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_share(
        self,
        request: Optional[Union[sharing_messages.GetShareRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> sharing.Share:
        r"""Get catalog share object for the space.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_get_share():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.GetShareRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_share(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.GetShareRequest, dict]):
                The request object. Message for getting a share of a
                catalog.
            name (str):
                Required. The share name in the following format:
                ``projects/$project/locations/$location/spaces/$space/catalogs/$catalog/shares/$share``

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
            google.cloud.designcenter_v1.types.Share:
                A catalog share between spaces.
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
        if not isinstance(request, sharing_messages.GetShareRequest):
            request = sharing_messages.GetShareRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_share]

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

    def delete_share(
        self,
        request: Optional[Union[sharing_messages.DeleteShareRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes a catalog share.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_delete_share():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.DeleteShareRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_share(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.DeleteShareRequest, dict]):
                The request object. Message for deleting a share of a
                catalog.
            name (str):
                Required. The share name in the following format:
                ``projects/$project/locations/$location/spaces/$space/catalogs/$catalog/shares/$share``

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
        if not isinstance(request, sharing_messages.DeleteShareRequest):
            request = sharing_messages.DeleteShareRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_share]

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
            metadata_type=designcenter.OperationMetadata,
        )

        # Done; return the response.
        return response

    def sync_share(
        self,
        request: Optional[Union[sharing_messages.SyncShareRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Synchronizes a share and updates the destination
        workspace to reflect. reflect the most recent changes to
        the catalog.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_sync_share():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.SyncShareRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.sync_share(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.SyncShareRequest, dict]):
                The request object. Message for syncing a share of a
                catalog.
            name (str):
                Required. The share name in the following format:
                ``projects/$project/locations/$location/spaces/$space/catalogs/$catalog/shares/$share``

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
                :class:`google.cloud.designcenter_v1.types.Share` A
                catalog share between spaces.

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
        if not isinstance(request, sharing_messages.SyncShareRequest):
            request = sharing_messages.SyncShareRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.sync_share]

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
            sharing.Share,
            metadata_type=designcenter.OperationMetadata,
        )

        # Done; return the response.
        return response

    def get_shared_template(
        self,
        request: Optional[
            Union[sharing_messages.GetSharedTemplateRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> sharing.SharedTemplate:
        r"""Gets details about a shared template.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_get_shared_template():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.GetSharedTemplateRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_shared_template(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.GetSharedTemplateRequest, dict]):
                The request object. Message for getting a shared
                template.
            name (str):
                Required. The shared template name. Format:
                ``projects/$project/locations/$location/spaces/$space/sharedTemplates/$sharedTemplate``

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
            google.cloud.designcenter_v1.types.SharedTemplate:
                A read-only template that is shared
                with a space.

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
        if not isinstance(request, sharing_messages.GetSharedTemplateRequest):
            request = sharing_messages.GetSharedTemplateRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_shared_template]

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

    def list_shared_templates(
        self,
        request: Optional[
            Union[sharing_messages.ListSharedTemplatesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListSharedTemplatesPager:
        r"""Lists shared templates in a given space.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_list_shared_templates():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.ListSharedTemplatesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_shared_templates(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.ListSharedTemplatesRequest, dict]):
                The request object. Message for requesting list of shared
                templates.
            parent (str):
                Required. The parent space for which shared templates
                are listed in the following format:
                ``projects/$project/locations/$location/spaces/$space``

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
            google.cloud.designcenter_v1.services.design_center.pagers.ListSharedTemplatesPager:
                Message for response to listing
                shared templates.
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
        if not isinstance(request, sharing_messages.ListSharedTemplatesRequest):
            request = sharing_messages.ListSharedTemplatesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_shared_templates]

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
        response = pagers.ListSharedTemplatesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_shared_template_revision(
        self,
        request: Optional[
            Union[sharing_messages.GetSharedTemplateRevisionRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> sharing.SharedTemplateRevision:
        r"""Gets details about a shared template revision.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_get_shared_template_revision():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.GetSharedTemplateRevisionRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_shared_template_revision(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.GetSharedTemplateRevisionRequest, dict]):
                The request object. Message for getting a shared template
                revisions.
            name (str):
                Required. The shared template revision name, in the
                following format:
                ``projects/$project/locations/$location/spaces/$space/sharedTemplates/$sharedTemplate/revisions/$revision``

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
            google.cloud.designcenter_v1.types.SharedTemplateRevision:
                A read-only template revision that is
                shared with a space.

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
        if not isinstance(request, sharing_messages.GetSharedTemplateRevisionRequest):
            request = sharing_messages.GetSharedTemplateRevisionRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.get_shared_template_revision
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

    def list_shared_template_revisions(
        self,
        request: Optional[
            Union[sharing_messages.ListSharedTemplateRevisionsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListSharedTemplateRevisionsPager:
        r"""Lists shared template revisions in a given space.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_list_shared_template_revisions():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.ListSharedTemplateRevisionsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_shared_template_revisions(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.ListSharedTemplateRevisionsRequest, dict]):
                The request object. Message for requesting a list of
                shared template revisions.
            parent (str):
                Required. The parent resource from which to list shared
                template revisions, in the following format:
                ``projects/$project/locations/$location/spaces/$space/sharedTemplates/$sharedTemplate``

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
            google.cloud.designcenter_v1.services.design_center.pagers.ListSharedTemplateRevisionsPager:
                Message for response to listing
                shared templates.
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
        if not isinstance(request, sharing_messages.ListSharedTemplateRevisionsRequest):
            request = sharing_messages.ListSharedTemplateRevisionsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_shared_template_revisions
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
        response = pagers.ListSharedTemplateRevisionsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_catalog_template_revision(
        self,
        request: Optional[
            Union[
                catalog_management_messages.CreateCatalogTemplateRevisionRequest, dict
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        catalog_template_revision: Optional[
            catalog_management.CatalogTemplateRevision
        ] = None,
        catalog_template_revision_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Creates a template revision.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_create_catalog_template_revision():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                catalog_template_revision = designcenter_v1.CatalogTemplateRevision()
                catalog_template_revision.git_source.repo = "repo_value"
                catalog_template_revision.git_source.ref_tag = "ref_tag_value"

                request = designcenter_v1.CreateCatalogTemplateRevisionRequest(
                    parent="parent_value",
                    catalog_template_revision_id="catalog_template_revision_id_value",
                    catalog_template_revision=catalog_template_revision,
                )

                # Make the request
                operation = client.create_catalog_template_revision(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.CreateCatalogTemplateRevisionRequest, dict]):
                The request object. Message for creating a template
                revisions request.
            parent (str):
                Required. The parent in which the catalog template
                revisions request is created in following format:
                ``projects/$project/locations/$location/spaces/$space/templates/$template``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            catalog_template_revision (google.cloud.designcenter_v1.types.CatalogTemplateRevision):
                Required. The template revision to
                create.

                This corresponds to the ``catalog_template_revision`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            catalog_template_revision_id (str):
                Required. The ID of the template
                revision to create.

                This corresponds to the ``catalog_template_revision_id`` field
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
                :class:`google.cloud.designcenter_v1.types.CatalogTemplateRevision`
                Template revisions inside a catalog.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [
            parent,
            catalog_template_revision,
            catalog_template_revision_id,
        ]
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
            request, catalog_management_messages.CreateCatalogTemplateRevisionRequest
        ):
            request = catalog_management_messages.CreateCatalogTemplateRevisionRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if catalog_template_revision is not None:
                request.catalog_template_revision = catalog_template_revision
            if catalog_template_revision_id is not None:
                request.catalog_template_revision_id = catalog_template_revision_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.create_catalog_template_revision
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
            catalog_management.CatalogTemplateRevision,
            metadata_type=designcenter.OperationMetadata,
        )

        # Done; return the response.
        return response

    def get_catalog_template_revision(
        self,
        request: Optional[
            Union[catalog_management_messages.GetCatalogTemplateRevisionRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> catalog_management.CatalogTemplateRevision:
        r"""Gets details about a template revision.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_get_catalog_template_revision():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.GetCatalogTemplateRevisionRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_catalog_template_revision(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.GetCatalogTemplateRevisionRequest, dict]):
                The request object. Message for GetTemplateRevision
                Request
            name (str):
                Required. The catalog template
                revisions name.

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
            google.cloud.designcenter_v1.types.CatalogTemplateRevision:
                Template revisions inside a catalog.
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
            request, catalog_management_messages.GetCatalogTemplateRevisionRequest
        ):
            request = catalog_management_messages.GetCatalogTemplateRevisionRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.get_catalog_template_revision
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

    def list_catalog_template_revisions(
        self,
        request: Optional[
            Union[catalog_management_messages.ListCatalogTemplateRevisionsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListCatalogTemplateRevisionsPager:
        r"""Lists template revisions.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_list_catalog_template_revisions():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.ListCatalogTemplateRevisionsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_catalog_template_revisions(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.ListCatalogTemplateRevisionsRequest, dict]):
                The request object. Message for requesting list of
                template revisions.
            parent (str):
                Required. The parent resource from
                which a list of catalog template
                revisions is requested.

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
            google.cloud.designcenter_v1.services.design_center.pagers.ListCatalogTemplateRevisionsPager:
                Message for response to listing
                template revisions.
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
            request, catalog_management_messages.ListCatalogTemplateRevisionsRequest
        ):
            request = catalog_management_messages.ListCatalogTemplateRevisionsRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_catalog_template_revisions
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
        response = pagers.ListCatalogTemplateRevisionsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def delete_catalog_template_revision(
        self,
        request: Optional[
            Union[
                catalog_management_messages.DeleteCatalogTemplateRevisionRequest, dict
            ]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes a template revision.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_delete_catalog_template_revision():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.DeleteCatalogTemplateRevisionRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_catalog_template_revision(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.DeleteCatalogTemplateRevisionRequest, dict]):
                The request object. Message for deleting a template
                revision.
            name (str):
                Required. The template revision name.
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
        if not isinstance(
            request, catalog_management_messages.DeleteCatalogTemplateRevisionRequest
        ):
            request = catalog_management_messages.DeleteCatalogTemplateRevisionRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.delete_catalog_template_revision
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

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=designcenter.OperationMetadata,
        )

        # Done; return the response.
        return response

    def create_application(
        self,
        request: Optional[
            Union[deployment_messages.CreateApplicationRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        application: Optional[deployment_resources.Application] = None,
        application_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> deployment_resources.Application:
        r"""Creates an application.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_create_application():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                application = designcenter_v1.Application()
                application.source.application_template_revision = "application_template_revision_value"
                application.scope.type_ = "GLOBAL"

                request = designcenter_v1.CreateApplicationRequest(
                    parent="parent_value",
                    application_id="application_id_value",
                    application=application,
                )

                # Make the request
                response = client.create_application(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.CreateApplicationRequest, dict]):
                The request object. Message for creating an application.
            parent (str):
                Required. The parent resource in which to create the
                application. Format:
                ``projects/$project/locations/$location/spaces/$space``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            application (google.cloud.designcenter_v1.types.Application):
                Required. The application to create.
                This corresponds to the ``application`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            application_id (str):
                Required. The ID of the application
                to create.

                This corresponds to the ``application_id`` field
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
            google.cloud.designcenter_v1.types.Application:
                Represents the application resource.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, application, application_id]
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
        if not isinstance(request, deployment_messages.CreateApplicationRequest):
            request = deployment_messages.CreateApplicationRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if application is not None:
                request.application = application
            if application_id is not None:
                request.application_id = application_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_application]

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

    def get_application(
        self,
        request: Optional[
            Union[deployment_messages.GetApplicationRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> deployment_resources.Application:
        r"""Gets details about an application.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_get_application():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.GetApplicationRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_application(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.GetApplicationRequest, dict]):
                The request object. Message for getting an application.
            name (str):
                Required. The application name. Format:
                ``projects/$project/locations/$location/spaces/$space/applications/$application``

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
            google.cloud.designcenter_v1.types.Application:
                Represents the application resource.
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
        if not isinstance(request, deployment_messages.GetApplicationRequest):
            request = deployment_messages.GetApplicationRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_application]

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

    def list_applications(
        self,
        request: Optional[
            Union[deployment_messages.ListApplicationsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListApplicationsPager:
        r"""Lists applications in a given space.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_list_applications():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.ListApplicationsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_applications(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.ListApplicationsRequest, dict]):
                The request object. Message for requesting a list of
                applications.
            parent (str):
                Required. The parent resource from
                which to request a list of applications.

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
            google.cloud.designcenter_v1.services.design_center.pagers.ListApplicationsPager:
                Message for response to listing
                applications.
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
        if not isinstance(request, deployment_messages.ListApplicationsRequest):
            request = deployment_messages.ListApplicationsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_applications]

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
        response = pagers.ListApplicationsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def update_application(
        self,
        request: Optional[
            Union[deployment_messages.UpdateApplicationRequest, dict]
        ] = None,
        *,
        application: Optional[deployment_resources.Application] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> deployment_resources.Application:
        r"""Updates an application.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_update_application():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                application = designcenter_v1.Application()
                application.source.application_template_revision = "application_template_revision_value"
                application.scope.type_ = "GLOBAL"

                request = designcenter_v1.UpdateApplicationRequest(
                    application=application,
                )

                # Make the request
                response = client.update_application(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.UpdateApplicationRequest, dict]):
                The request object. Message for updating an application.
            application (google.cloud.designcenter_v1.types.Application):
                Required. The application to update.
                This corresponds to the ``application`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Optional. The fields to overwrite in
                the application update. If you don't
                provide a mask, all fields are
                overwritten.

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
            google.cloud.designcenter_v1.types.Application:
                Represents the application resource.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [application, update_mask]
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
        if not isinstance(request, deployment_messages.UpdateApplicationRequest):
            request = deployment_messages.UpdateApplicationRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if application is not None:
                request.application = application
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_application]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("application.name", request.application.name),)
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

    def delete_application(
        self,
        request: Optional[
            Union[deployment_messages.DeleteApplicationRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes an application.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_delete_application():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.DeleteApplicationRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_application(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.DeleteApplicationRequest, dict]):
                The request object. Message for deleting an application.
            name (str):
                Required. The application name. Format:
                ``projects/$project/locations/$location/spaces/$space/applications/$application``

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
        if not isinstance(request, deployment_messages.DeleteApplicationRequest):
            request = deployment_messages.DeleteApplicationRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_application]

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
            metadata_type=designcenter.OperationMetadata,
        )

        # Done; return the response.
        return response

    def deploy_application(
        self,
        request: Optional[
            Union[deployment_messages.DeployApplicationRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deploys an application.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_deploy_application():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.DeployApplicationRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.deploy_application(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.DeployApplicationRequest, dict]):
                The request object. Message for deploying an application.
            name (str):
                Required. The application name. Format:
                ``projects/$project/locations/$location/spaces/$space/applications/$application``

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
                :class:`google.cloud.designcenter_v1.types.DeployApplicationResponse`
                Response for DeployApplication.

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
        if not isinstance(request, deployment_messages.DeployApplicationRequest):
            request = deployment_messages.DeployApplicationRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.deploy_application]

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
            deployment_messages.DeployApplicationResponse,
            metadata_type=designcenter.OperationMetadata,
        )

        # Done; return the response.
        return response

    def preview_application(
        self,
        request: Optional[
            Union[deployment_messages.PreviewApplicationRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Previews deployment of an application.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_preview_application():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.PreviewApplicationRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.preview_application(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.PreviewApplicationRequest, dict]):
                The request object. Message for previewing an
                application.
            name (str):
                Required. The application name in the following format:
                ``projects/$project/locations/$location/spaces/$space/applications/$application``

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
                :class:`google.cloud.designcenter_v1.types.PreviewApplicationResponse`
                Response for PreviewApplication.

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
        if not isinstance(request, deployment_messages.PreviewApplicationRequest):
            request = deployment_messages.PreviewApplicationRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.preview_application]

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
            deployment_messages.PreviewApplicationResponse,
            metadata_type=designcenter.OperationMetadata,
        )

        # Done; return the response.
        return response

    def fetch_application_assessment_report(
        self,
        request: Optional[
            Union[best_practices_messages.FetchApplicationAssessmentReportRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> best_practices_messages.FetchApplicationAssessmentReportResponse:
        r"""Fetches the assessment report of a deployed
        application if present.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_fetch_application_assessment_report():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.FetchApplicationAssessmentReportRequest(
                    name="name_value",
                )

                # Make the request
                response = client.fetch_application_assessment_report(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.FetchApplicationAssessmentReportRequest, dict]):
                The request object. Message for fetching an application
                assessment report.
            name (str):
                Required. The application name in the following format:
                ``projects/$project/locations/$location/spaces/$space/applications/$application``

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
            google.cloud.designcenter_v1.types.FetchApplicationAssessmentReportResponse:
                Message for response of fetching an
                application assessment report.

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
            request, best_practices_messages.FetchApplicationAssessmentReportRequest
        ):
            request = best_practices_messages.FetchApplicationAssessmentReportRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.fetch_application_assessment_report
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

    def generate_application_assessment_report(
        self,
        request: Optional[
            Union[
                best_practices_messages.GenerateApplicationAssessmentReportRequest, dict
            ]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Generate Assessment Reports of an application.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_generate_application_assessment_report():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.GenerateApplicationAssessmentReportRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.generate_application_assessment_report(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.GenerateApplicationAssessmentReportRequest, dict]):
                The request object. Message for generating an application
                assessment report.
            name (str):
                Required. The application name in the following format:
                ``projects/$project/locations/$location/spaces/$space/applications/$application``

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
                :class:`google.cloud.designcenter_v1.types.GenerateApplicationAssessmentReportResponse`
                Response for GenerateApplicationAssessmentReport.

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
            request, best_practices_messages.GenerateApplicationAssessmentReportRequest
        ):
            request = (
                best_practices_messages.GenerateApplicationAssessmentReportRequest(
                    request
                )
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.generate_application_assessment_report
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

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            best_practices_messages.GenerateApplicationAssessmentReportResponse,
            metadata_type=designcenter.OperationMetadata,
        )

        # Done; return the response.
        return response

    def generate_application_template_assessment_report(
        self,
        request: Optional[
            Union[
                best_practices_messages.GenerateApplicationTemplateAssessmentReportRequest,
                dict,
            ]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Generate Assessment Reports of an application
        template.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_generate_application_template_assessment_report():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.GenerateApplicationTemplateAssessmentReportRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.generate_application_template_assessment_report(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.GenerateApplicationTemplateAssessmentReportRequest, dict]):
                The request object. Message for generate assessment
                report application template.
            name (str):
                Required. The application template name in the following
                format:
                ``projects/$project/locations/$location/spaces/$space/applicationTemplates/$applicationTemplate``

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
                :class:`google.cloud.designcenter_v1.types.GenerateApplicationTemplateAssessmentReportResponse`
                Response for GenerateAssessmentReport for application
                template.

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
            request,
            best_practices_messages.GenerateApplicationTemplateAssessmentReportRequest,
        ):
            request = best_practices_messages.GenerateApplicationTemplateAssessmentReportRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.generate_application_template_assessment_report
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

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            best_practices_messages.GenerateApplicationTemplateAssessmentReportResponse,
            metadata_type=designcenter.OperationMetadata,
        )

        # Done; return the response.
        return response

    def generate_assessment_report(
        self,
        request: Optional[
            Union[best_practices_messages.GenerateAssessmentReportRequest, dict]
        ] = None,
        *,
        space_name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deprecated: Use GenerateTerraformPlanAssessmentReport
        instead.
        Generate a best practice report for a given Terraform
        plan.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_generate_assessment_report():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.GenerateAssessmentReportRequest(
                    terraform_plan=b'terraform_plan_blob',
                    space_name="space_name_value",
                )

                # Make the request
                operation = client.generate_assessment_report(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.GenerateAssessmentReportRequest, dict]):
                The request object. Deprecated: Use
                GenerateTerraformPlanAssessmentReportRequest
                instead.  Message for the request to
                generate a best practice report for a
                given Terraform plan.
            space_name (str):
                Required. The name of the space at which Generate
                Assessment Report is called. Format:
                ``projects/$project/locations/$location/spaces/$space``

                This corresponds to the ``space_name`` field
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
                :class:`google.cloud.designcenter_v1.types.GenerateAssessmentReportResponse`
                Deprecated: Use
                GenerateTerraformPlanAssessmentReportResponse instead.

                   Response for GenerateAssessmentReport.

        """
        warnings.warn(
            "DesignCenterClient.generate_assessment_report is deprecated",
            DeprecationWarning,
        )

        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [space_name]
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
            request, best_practices_messages.GenerateAssessmentReportRequest
        ):
            request = best_practices_messages.GenerateAssessmentReportRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if space_name is not None:
                request.space_name = space_name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.generate_assessment_report
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("space_name", request.space_name),)
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
            best_practices_messages.GenerateAssessmentReportResponse,
            metadata_type=designcenter.OperationMetadata,
        )

        # Done; return the response.
        return response

    def generate_terraform_plan_assessment_report(
        self,
        request: Optional[
            Union[
                best_practices_messages.GenerateTerraformPlanAssessmentReportRequest,
                dict,
            ]
        ] = None,
        *,
        name: Optional[str] = None,
        terraform_plan: Optional[bytes] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Generate a Terraform plan assessment report for a
        given Terraform plan.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_generate_terraform_plan_assessment_report():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.GenerateTerraformPlanAssessmentReportRequest(
                    name="name_value",
                    terraform_plan=b'terraform_plan_blob',
                )

                # Make the request
                operation = client.generate_terraform_plan_assessment_report(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.GenerateTerraformPlanAssessmentReportRequest, dict]):
                The request object. Message for the request to generate a
                best practice report for a given
                Terraform plan at the collection level.
            name (str):
                Required. The parent resource in
                which to generate the assessment report.
                Format:
                projects/$project/locations/$location/spaces/$space

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            terraform_plan (bytes):
                Required. The raw JSON representation
                of the generated Terraform plan,
                provided as bytes.

                This corresponds to the ``terraform_plan`` field
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
                :class:`google.cloud.designcenter_v1.types.GenerateTerraformPlanAssessmentReportResponse`
                Response for GenerateTerraformPlanAssessmentReport.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, terraform_plan]
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
            request,
            best_practices_messages.GenerateTerraformPlanAssessmentReportRequest,
        ):
            request = (
                best_practices_messages.GenerateTerraformPlanAssessmentReportRequest(
                    request
                )
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name
            if terraform_plan is not None:
                request.terraform_plan = terraform_plan

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.generate_terraform_plan_assessment_report
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

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            best_practices_messages.GenerateTerraformPlanAssessmentReportResponse,
            metadata_type=designcenter.OperationMetadata,
        )

        # Done; return the response.
        return response

    def get_policy(
        self,
        request: Optional[Union[best_practices_messages.GetPolicyRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> best_practices.Policy:
        r"""Policy related APIs.
        Get a policy for an application template.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_get_policy():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.GetPolicyRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.GetPolicyRequest, dict]):
                The request object. Message for getting a policy.
            name (str):
                Required. The policy name in the following format:
                ``projects/$project/locations/$location/spaces/$space/applicationTemplates/$applicationTemplate/policies/$policy``

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
            google.cloud.designcenter_v1.types.Policy:
                A Policy is a resource within an
                Application Template that refers to a
                Policy that you author outside of
                Application Design Center and attach to
                an application template.

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
        if not isinstance(request, best_practices_messages.GetPolicyRequest):
            request = best_practices_messages.GetPolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_policy]

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

    def list_policies(
        self,
        request: Optional[
            Union[best_practices_messages.ListPoliciesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListPoliciesPager:
        r"""Lists policies for an application template.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_list_policies():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.ListPoliciesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_policies(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.ListPoliciesRequest, dict]):
                The request object. Message for requesting a list of
                policies.
            parent (str):
                Required. The parent application template from which
                policies are listed in the following format:
                ``projects/$project/locations/$location/spaces/$space/applicationTemplates/$applicationTemplate``

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
            google.cloud.designcenter_v1.services.design_center.pagers.ListPoliciesPager:
                Message for response to listing
                policies.
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
        if not isinstance(request, best_practices_messages.ListPoliciesRequest):
            request = best_practices_messages.ListPoliciesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_policies]

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
        response = pagers.ListPoliciesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_policy(
        self,
        request: Optional[
            Union[best_practices_messages.CreatePolicyRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        policy: Optional[best_practices.Policy] = None,
        policy_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> best_practices.Policy:
        r"""Creates a policy for an application template.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_create_policy():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                policy = designcenter_v1.Policy()
                policy.policy_uri = "policy_uri_value"
                policy.policy_type = "COMPLIANCE_FRAMEWORK"

                request = designcenter_v1.CreatePolicyRequest(
                    parent="parent_value",
                    policy_id="policy_id_value",
                    policy=policy,
                )

                # Make the request
                response = client.create_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.CreatePolicyRequest, dict]):
                The request object. Message for creating a policy.
            parent (str):
                Required. The parent resource in which to create the
                policy in the following format:
                ``projects/$project/locations/$location/spaces/$space/applicationTemplates/$applicationTemplate``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            policy (google.cloud.designcenter_v1.types.Policy):
                Required. The policy to create.
                This corresponds to the ``policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            policy_id (str):
                Required. The ID of the policy to
                create.

                This corresponds to the ``policy_id`` field
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
            google.cloud.designcenter_v1.types.Policy:
                A Policy is a resource within an
                Application Template that refers to a
                Policy that you author outside of
                Application Design Center and attach to
                an application template.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, policy, policy_id]
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
        if not isinstance(request, best_practices_messages.CreatePolicyRequest):
            request = best_practices_messages.CreatePolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if policy is not None:
                request.policy = policy
            if policy_id is not None:
                request.policy_id = policy_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_policy]

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

    def update_policy(
        self,
        request: Optional[
            Union[best_practices_messages.UpdatePolicyRequest, dict]
        ] = None,
        *,
        policy: Optional[best_practices.Policy] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> best_practices.Policy:
        r"""Updates a policy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_update_policy():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                policy = designcenter_v1.Policy()
                policy.policy_uri = "policy_uri_value"
                policy.policy_type = "COMPLIANCE_FRAMEWORK"

                request = designcenter_v1.UpdatePolicyRequest(
                    policy=policy,
                )

                # Make the request
                response = client.update_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.UpdatePolicyRequest, dict]):
                The request object. Message for updating a policy.
            policy (google.cloud.designcenter_v1.types.Policy):
                Required. The policy to update.
                This corresponds to the ``policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Optional. The fields to overwrite in the policy update.
                The fields specified in the update_mask are relative to
                the resource, not the full request. A field will be
                overwritten if it is in the mask. If you don't provide a
                mask, all fields are overwritten.

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
            google.cloud.designcenter_v1.types.Policy:
                A Policy is a resource within an
                Application Template that refers to a
                Policy that you author outside of
                Application Design Center and attach to
                an application template.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [policy, update_mask]
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
        if not isinstance(request, best_practices_messages.UpdatePolicyRequest):
            request = best_practices_messages.UpdatePolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if policy is not None:
                request.policy = policy
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_policy]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("policy.name", request.policy.name),)
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

    def delete_policy(
        self,
        request: Optional[
            Union[best_practices_messages.DeletePolicyRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a policy.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_delete_policy():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.DeletePolicyRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_policy(request=request)

        Args:
            request (Union[google.cloud.designcenter_v1.types.DeletePolicyRequest, dict]):
                The request object. Message for deleting a policy.
            name (str):
                Required. The policy name in the following format:
                ``projects/$project/locations/$location/spaces/$space/applicationTemplates/$applicationTemplate/policies/$policy``

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
        if not isinstance(request, best_practices_messages.DeletePolicyRequest):
            request = best_practices_messages.DeletePolicyRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_policy]

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

    def fetch_frameworks(
        self,
        request: Optional[
            Union[best_practices_messages.FetchFrameworksRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.FetchFrameworksPager:
        r"""Fetches all frameworks for assessment report.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_fetch_frameworks():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.FetchFrameworksRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.fetch_frameworks(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.FetchFrameworksRequest, dict]):
                The request object. Request for FetchFrameworks rpc
            parent (str):
                Required. The parent resource name.
                Format:
                projects/{project}/locations/{location}

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
            google.cloud.designcenter_v1.services.design_center.pagers.FetchFrameworksPager:
                Response for FetchFrameworks rpc

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
        if not isinstance(request, best_practices_messages.FetchFrameworksRequest):
            request = best_practices_messages.FetchFrameworksRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.fetch_frameworks]

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
        response = pagers.FetchFrameworksPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def generate_application_ia_c(
        self,
        request: Optional[
            Union[deployment_messages.GenerateApplicationIaCRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> deployment_messages.GenerateApplicationIaCResponse:
        r"""Generates Terraform files for an application.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_generate_application_ia_c():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.GenerateApplicationIaCRequest(
                    name="name_value",
                )

                # Make the request
                response = client.generate_application_ia_c(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.GenerateApplicationIaCRequest, dict]):
                The request object. Request message for
                GenerateApplicationIaC method.
            name (str):
                Required. The name of the
                application.

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
            google.cloud.designcenter_v1.types.GenerateApplicationIaCResponse:
                Response message for
                GenerateApplicationIaC method.

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
        if not isinstance(request, deployment_messages.GenerateApplicationIaCRequest):
            request = deployment_messages.GenerateApplicationIaCRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.generate_application_ia_c
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

    def export_application_ia_c(
        self,
        request: Optional[
            Union[deployment_messages.ExportApplicationIaCRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Exports Terraform files for an application
        asynchronously.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_export_application_ia_c():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.ExportApplicationIaCRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.export_application_ia_c(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.ExportApplicationIaCRequest, dict]):
                The request object. Request message for
                ExportApplicationIaC method.
            name (str):
                Required. The name of the
                application.

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
                :class:`google.cloud.designcenter_v1.types.ExportApplicationIaCResponse`
                Response message for ExportApplicationIaC method.

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
        if not isinstance(request, deployment_messages.ExportApplicationIaCRequest):
            request = deployment_messages.ExportApplicationIaCRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.export_application_ia_c]

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
            deployment_messages.ExportApplicationIaCResponse,
            metadata_type=designcenter.OperationMetadata,
        )

        # Done; return the response.
        return response

    def import_application_template_ia_c(
        self,
        request: Optional[
            Union[authoring_messages.ImportApplicationTemplateIaCRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> authoring_messages.ImportApplicationTemplateIaCResponse:
        r"""Imports IaC for an application template.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_import_application_template_ia_c():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.ImportApplicationTemplateIaCRequest(
                    gcs_uri="gcs_uri_value",
                    name="name_value",
                )

                # Make the request
                response = client.import_application_template_ia_c(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.ImportApplicationTemplateIaCRequest, dict]):
                The request object. Request message for
                ImportApplicationTemplateIaC method.
            name (str):
                Required. The name of the application
                template.

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
            google.cloud.designcenter_v1.types.ImportApplicationTemplateIaCResponse:
                Response message for
                ImportApplicationTemplateIaC method.

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
            request, authoring_messages.ImportApplicationTemplateIaCRequest
        ):
            request = authoring_messages.ImportApplicationTemplateIaCRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.import_application_template_ia_c
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

    def ingest_application_template_ia_c(
        self,
        request: Optional[
            Union[authoring_messages.IngestApplicationTemplateIaCRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Ingests IaC for an application template
        asynchronously.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_ingest_application_template_ia_c():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.IngestApplicationTemplateIaCRequest(
                    gcs_uri="gcs_uri_value",
                    name="name_value",
                )

                # Make the request
                operation = client.ingest_application_template_ia_c(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.IngestApplicationTemplateIaCRequest, dict]):
                The request object. Request message for
                IngestApplicationTemplateIaC method.
            name (str):
                Required. The name of the application
                template.

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
                :class:`google.cloud.designcenter_v1.types.IngestApplicationTemplateIaCResponse`
                Response message for IngestApplicationTemplateIaC
                method.

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
            request, authoring_messages.IngestApplicationTemplateIaCRequest
        ):
            request = authoring_messages.IngestApplicationTemplateIaCRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.ingest_application_template_ia_c
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

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            authoring_messages.IngestApplicationTemplateIaCResponse,
            metadata_type=designcenter.OperationMetadata,
        )

        # Done; return the response.
        return response

    def import_application_ia_c(
        self,
        request: Optional[
            Union[deployment_messages.ImportApplicationIaCRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> deployment_messages.ImportApplicationIaCResponse:
        r"""Imports IaC for an application resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_import_application_ia_c():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.ImportApplicationIaCRequest(
                    gcs_uri="gcs_uri_value",
                    name="name_value",
                )

                # Make the request
                response = client.import_application_ia_c(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.ImportApplicationIaCRequest, dict]):
                The request object. Request message for
                ImportApplicationIaC method.
            name (str):
                Required. The name of the
                application.

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
            google.cloud.designcenter_v1.types.ImportApplicationIaCResponse:
                Response message for
                ImportApplicationIaC method.

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
        if not isinstance(request, deployment_messages.ImportApplicationIaCRequest):
            request = deployment_messages.ImportApplicationIaCRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.import_application_ia_c]

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

    def register_app_hub_application_resources(
        self,
        request: Optional[
            Union[
                apphub_integration_messages.RegisterAppHubApplicationResourcesRequest,
                dict,
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        apphub_application: Optional[str] = None,
        tfstate_content: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Register deployed resources from terraform state file
        with App Hub without needing a space.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_register_app_hub_application_resources():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.RegisterAppHubApplicationResourcesRequest(
                    tfstate_content="tfstate_content_value",
                    parent="parent_value",
                    apphub_application="apphub_application_value",
                )

                # Make the request
                operation = client.register_app_hub_application_resources(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.RegisterAppHubApplicationResourcesRequest, dict]):
                The request object. Request message for
                RegisterAppHubApplicationResources
                method.
            parent (str):
                Required. The parent location.
                Format:
                projects/{project}/locations/{location}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            apphub_application (str):
                Required. The name of the AppHub
                Application. Format:

                projects/{project}/locations/{location}/applications/{application}

                This corresponds to the ``apphub_application`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            tfstate_content (str):
                Optional. The Terraform state (tfstate) content as a raw
                string. For large state files exceeding 10MB, use the
                'tfstate_signed_gcs_uri' field instead.

                This corresponds to the ``tfstate_content`` field
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
                :class:`google.cloud.designcenter_v1.types.RegisterAppHubApplicationResourcesResponse`
                Response message for RegisterAppHubApplicationResources
                method.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, apphub_application, tfstate_content]
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
            request,
            apphub_integration_messages.RegisterAppHubApplicationResourcesRequest,
        ):
            request = (
                apphub_integration_messages.RegisterAppHubApplicationResourcesRequest(
                    request
                )
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if apphub_application is not None:
                request.apphub_application = apphub_application
            if tfstate_content is not None:
                request.tfstate_content = tfstate_content

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.register_app_hub_application_resources
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
            apphub_integration_messages.RegisterAppHubApplicationResourcesResponse,
            metadata_type=designcenter.OperationMetadata,
        )

        # Done; return the response.
        return response

    def list_application_template_system_revisions(
        self,
        request: Optional[
            Union[
                authoring_messages.ListApplicationTemplateSystemRevisionsRequest, dict
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListApplicationTemplateSystemRevisionsPager:
        r"""Lists application template system revisions in a
        given application template.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_list_application_template_system_revisions():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.ListApplicationTemplateSystemRevisionsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_application_template_system_revisions(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.ListApplicationTemplateSystemRevisionsRequest, dict]):
                The request object. Message for requesting a list of
                application template system revisions.
            parent (str):
                Required. The parent Application Template from which to
                list the system revisions. Format:
                projects/{project}/locations/{location}/spaces/{space}/applicationTemplates/{application_template}

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
            google.cloud.designcenter_v1.services.design_center.pagers.ListApplicationTemplateSystemRevisionsPager:
                Message for response to listing
                application template system revisions.
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
            request, authoring_messages.ListApplicationTemplateSystemRevisionsRequest
        ):
            request = authoring_messages.ListApplicationTemplateSystemRevisionsRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_application_template_system_revisions
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
        response = pagers.ListApplicationTemplateSystemRevisionsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_application_template_system_revision(
        self,
        request: Optional[
            Union[authoring_messages.GetApplicationTemplateSystemRevisionRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> authoring.ApplicationTemplateSystemRevision:
        r"""Gets the given application template system revision.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_get_application_template_system_revision():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.GetApplicationTemplateSystemRevisionRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_application_template_system_revision(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.GetApplicationTemplateSystemRevisionRequest, dict]):
                The request object. Message for getting an
                ApplicationTemplateSystemRevision.
            name (str):
                Required. The name of the
                ApplicationTemplateSystemRevision to retrieve. Format:
                projects/{project}/locations/{location}/spaces/{space}/applicationTemplates/{application_template}/systemRevisions/{system_revision}

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
            google.cloud.designcenter_v1.types.ApplicationTemplateSystemRevision:
                Application template system revision
                resource.

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
            request, authoring_messages.GetApplicationTemplateSystemRevisionRequest
        ):
            request = authoring_messages.GetApplicationTemplateSystemRevisionRequest(
                request
            )
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.get_application_template_system_revision
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

    def recommend_iam_roles(
        self,
        request: Optional[
            Union[deployment_messages.RecommendIAMRolesRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Gets recommended IAM roles for an application.

        Evaluates the infrastructure resources defined by an application
        (including its template configuration and parameters) to
        determine the set of IAM roles and Google Cloud APIs that you
        must configure before you deploy across target projects.

        The operation is asynchronous and returns a
        ``google.longrunning.Operation``. Upon completion, the operation
        result contains a ``RecommendIAMRolesResponse`` with
        project-level IAM role and API recommendations.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import designcenter_v1

            def sample_recommend_iam_roles():
                # Create a client
                client = designcenter_v1.DesignCenterClient()

                # Initialize request argument(s)
                request = designcenter_v1.RecommendIAMRolesRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.recommend_iam_roles(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.designcenter_v1.types.RecommendIAMRolesRequest, dict]):
                The request object. Request message for ``RecommendIAMRoles``.
            name (str):
                Required. The name of the application
                resource for which to recommend IAM
                roles. Format:

                projects/$project/locations/$location/spaces/$space/applications/$application

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
                :class:`google.cloud.designcenter_v1.types.RecommendIAMRolesResponse`
                Response message for RecommendIAMRoles.

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
        if not isinstance(request, deployment_messages.RecommendIAMRolesRequest):
            request = deployment_messages.RecommendIAMRolesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.recommend_iam_roles]

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
            deployment_messages.RecommendIAMRolesResponse,
            metadata_type=designcenter.OperationMetadata,
        )

        # Done; return the response.
        return response

    def __enter__(self) -> "DesignCenterClient":
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

    def delete_operation(
        self,
        request: Optional[Union[operations_pb2.DeleteOperationRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a long-running operation.

        This method indicates that the client is no longer interested
        in the operation result. It does not cancel the operation.
        If the server doesn't support this method, it returns
        `google.rpc.Code.UNIMPLEMENTED`.

        Args:
            request (:class:`~.operations_pb2.DeleteOperationRequest`):
                The request object. Request message for
                `DeleteOperation` method.
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
            request_pb = operations_pb2.DeleteOperationRequest()
        elif isinstance(request, dict):
            request_pb = operations_pb2.DeleteOperationRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_operation]

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

    def set_iam_policy(
        self,
        request: Optional[Union[iam_policy_pb2.SetIamPolicyRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> policy_pb2.Policy:
        r"""Sets the IAM access control policy on the specified function.

        Replaces any existing policy.

        Args:
            request (:class:`~.iam_policy_pb2.SetIamPolicyRequest`):
                The request object. Request message for `SetIamPolicy`
                method.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            ~.policy_pb2.Policy:
                Defines an Identity and Access Management (IAM) policy.
                It is used to specify access control policies for Cloud
                Platform resources.
                A ``Policy`` is a collection of ``bindings``. A
                ``binding`` binds one or more ``members`` to a single
                ``role``. Members can be user accounts, service
                accounts, Google groups, and domains (such as G Suite).
                A ``role`` is a named list of permissions (defined by
                IAM or configured by users). A ``binding`` can
                optionally specify a ``condition``, which is a logic
                expression that further constrains the role binding
                based on attributes about the request and/or target
                resource.

                **JSON Example**

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
                          "members": ["user:eve@example.com"],
                          "condition": {
                            "title": "expirable access",
                            "description": "Does not grant access after Sep 2020",
                            "expression": "request.time <
                            timestamp('2020-10-01T00:00:00.000Z')",
                          }
                        }
                      ]
                    }

                **YAML Example**

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

                For a description of IAM and its features, see the `IAM
                developer's
                guide <https://cloud.google.com/iam/docs>`__.
        """
        # Create or coerce a protobuf request object.

        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = iam_policy_pb2.SetIamPolicyRequest()
        elif isinstance(request, dict):
            request_pb = iam_policy_pb2.SetIamPolicyRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.set_iam_policy]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("resource", request_pb.resource),)
            ),
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

    def get_iam_policy(
        self,
        request: Optional[Union[iam_policy_pb2.GetIamPolicyRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> policy_pb2.Policy:
        r"""Gets the IAM access control policy for a function.

        Returns an empty policy if the function exists and does not have a
        policy set.

        Args:
            request (:class:`~.iam_policy_pb2.GetIamPolicyRequest`):
                The request object. Request message for `GetIamPolicy`
                method.
            retry (google.api_core.retry.Retry): Designation of what errors, if
                any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            ~.policy_pb2.Policy:
                Defines an Identity and Access Management (IAM) policy.
                It is used to specify access control policies for Cloud
                Platform resources.
                A ``Policy`` is a collection of ``bindings``. A
                ``binding`` binds one or more ``members`` to a single
                ``role``. Members can be user accounts, service
                accounts, Google groups, and domains (such as G Suite).
                A ``role`` is a named list of permissions (defined by
                IAM or configured by users). A ``binding`` can
                optionally specify a ``condition``, which is a logic
                expression that further constrains the role binding
                based on attributes about the request and/or target
                resource.

                **JSON Example**

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
                          "members": ["user:eve@example.com"],
                          "condition": {
                            "title": "expirable access",
                            "description": "Does not grant access after Sep 2020",
                            "expression": "request.time <
                            timestamp('2020-10-01T00:00:00.000Z')",
                          }
                        }
                      ]
                    }

                **YAML Example**

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

                For a description of IAM and its features, see the `IAM
                developer's
                guide <https://cloud.google.com/iam/docs>`__.
        """
        # Create or coerce a protobuf request object.

        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = iam_policy_pb2.GetIamPolicyRequest()
        elif isinstance(request, dict):
            request_pb = iam_policy_pb2.GetIamPolicyRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_iam_policy]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("resource", request_pb.resource),)
            ),
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

    def test_iam_permissions(
        self,
        request: Optional[Union[iam_policy_pb2.TestIamPermissionsRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        r"""Tests the specified IAM permissions against the IAM access control
            policy for a function.

        If the function does not exist, this will return an empty set
        of permissions, not a NOT_FOUND error.

        Args:
            request (:class:`~.iam_policy_pb2.TestIamPermissionsRequest`):
                The request object. Request message for
                `TestIamPermissions` method.
            retry (google.api_core.retry.Retry): Designation of what errors,
                 if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            ~.iam_policy_pb2.TestIamPermissionsResponse:
                Response message for ``TestIamPermissions`` method.
        """
        # Create or coerce a protobuf request object.

        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = iam_policy_pb2.TestIamPermissionsRequest()
        elif isinstance(request, dict):
            request_pb = iam_policy_pb2.TestIamPermissionsRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.test_iam_permissions]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("resource", request_pb.resource),)
            ),
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

__all__ = ("DesignCenterClient",)
