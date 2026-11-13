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

from google.cloud.apphub_v1 import gapic_version as package_version
from google.cloud.apphub_v1.types import (
    apphub_service,
    application,
    boundary,
    extended_metadata_schema,
    service,
    service_project_attachment,
    workload,
)

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class AppHubTransport(abc.ABC):
    """Abstract transport class for AppHub."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "apphub.googleapis.com"

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
                 The hostname to connect to (default: 'apphub.googleapis.com').
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
            self.lookup_service_project_attachment: gapic_v1.method.wrap_method(
                self.lookup_service_project_attachment,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_service_project_attachments: gapic_v1.method.wrap_method(
                self.list_service_project_attachments,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_service_project_attachment: gapic_v1.method.wrap_method(
                self.create_service_project_attachment,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_service_project_attachment: gapic_v1.method.wrap_method(
                self.get_service_project_attachment,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_service_project_attachment: gapic_v1.method.wrap_method(
                self.delete_service_project_attachment,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.detach_service_project_attachment: gapic_v1.method.wrap_method(
                self.detach_service_project_attachment,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_discovered_services: gapic_v1.method.wrap_method(
                self.list_discovered_services,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_discovered_service: gapic_v1.method.wrap_method(
                self.get_discovered_service,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.lookup_discovered_service: gapic_v1.method.wrap_method(
                self.lookup_discovered_service,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_services: gapic_v1.method.wrap_method(
                self.list_services,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_service: gapic_v1.method.wrap_method(
                self.create_service,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_service: gapic_v1.method.wrap_method(
                self.get_service,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_service: gapic_v1.method.wrap_method(
                self.update_service,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_service: gapic_v1.method.wrap_method(
                self.delete_service,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_discovered_workloads: gapic_v1.method.wrap_method(
                self.list_discovered_workloads,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_discovered_workload: gapic_v1.method.wrap_method(
                self.get_discovered_workload,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.lookup_discovered_workload: gapic_v1.method.wrap_method(
                self.lookup_discovered_workload,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_workloads: gapic_v1.method.wrap_method(
                self.list_workloads,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_workload: gapic_v1.method.wrap_method(
                self.create_workload,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_workload: gapic_v1.method.wrap_method(
                self.get_workload,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_workload: gapic_v1.method.wrap_method(
                self.update_workload,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_workload: gapic_v1.method.wrap_method(
                self.delete_workload,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_applications: gapic_v1.method.wrap_method(
                self.list_applications,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_application: gapic_v1.method.wrap_method(
                self.create_application,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_application: gapic_v1.method.wrap_method(
                self.get_application,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_application: gapic_v1.method.wrap_method(
                self.update_application,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_application: gapic_v1.method.wrap_method(
                self.delete_application,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_boundary: gapic_v1.method.wrap_method(
                self.get_boundary,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_boundary: gapic_v1.method.wrap_method(
                self.update_boundary,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_extended_metadata_schema: gapic_v1.method.wrap_method(
                self.get_extended_metadata_schema,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_extended_metadata_schemas: gapic_v1.method.wrap_method(
                self.list_extended_metadata_schemas,
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
            self.get_iam_policy: gapic_v1.method.wrap_method(
                self.get_iam_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.set_iam_policy: gapic_v1.method.wrap_method(
                self.set_iam_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.test_iam_permissions: gapic_v1.method.wrap_method(
                self.test_iam_permissions,
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
    def operations_client(self):
        """Return the client designed to process long-running operations."""
        raise NotImplementedError()

    @property
    def lookup_service_project_attachment(
        self,
    ) -> Callable[
        [apphub_service.LookupServiceProjectAttachmentRequest],
        Union[
            apphub_service.LookupServiceProjectAttachmentResponse,
            Awaitable[apphub_service.LookupServiceProjectAttachmentResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_service_project_attachments(
        self,
    ) -> Callable[
        [apphub_service.ListServiceProjectAttachmentsRequest],
        Union[
            apphub_service.ListServiceProjectAttachmentsResponse,
            Awaitable[apphub_service.ListServiceProjectAttachmentsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_service_project_attachment(
        self,
    ) -> Callable[
        [apphub_service.CreateServiceProjectAttachmentRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_service_project_attachment(
        self,
    ) -> Callable[
        [apphub_service.GetServiceProjectAttachmentRequest],
        Union[
            service_project_attachment.ServiceProjectAttachment,
            Awaitable[service_project_attachment.ServiceProjectAttachment],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_service_project_attachment(
        self,
    ) -> Callable[
        [apphub_service.DeleteServiceProjectAttachmentRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def detach_service_project_attachment(
        self,
    ) -> Callable[
        [apphub_service.DetachServiceProjectAttachmentRequest],
        Union[
            apphub_service.DetachServiceProjectAttachmentResponse,
            Awaitable[apphub_service.DetachServiceProjectAttachmentResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_discovered_services(
        self,
    ) -> Callable[
        [apphub_service.ListDiscoveredServicesRequest],
        Union[
            apphub_service.ListDiscoveredServicesResponse,
            Awaitable[apphub_service.ListDiscoveredServicesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_discovered_service(
        self,
    ) -> Callable[
        [apphub_service.GetDiscoveredServiceRequest],
        Union[service.DiscoveredService, Awaitable[service.DiscoveredService]],
    ]:
        raise NotImplementedError()

    @property
    def lookup_discovered_service(
        self,
    ) -> Callable[
        [apphub_service.LookupDiscoveredServiceRequest],
        Union[
            apphub_service.LookupDiscoveredServiceResponse,
            Awaitable[apphub_service.LookupDiscoveredServiceResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_services(
        self,
    ) -> Callable[
        [apphub_service.ListServicesRequest],
        Union[
            apphub_service.ListServicesResponse,
            Awaitable[apphub_service.ListServicesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_service(
        self,
    ) -> Callable[
        [apphub_service.CreateServiceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_service(
        self,
    ) -> Callable[
        [apphub_service.GetServiceRequest],
        Union[service.Service, Awaitable[service.Service]],
    ]:
        raise NotImplementedError()

    @property
    def update_service(
        self,
    ) -> Callable[
        [apphub_service.UpdateServiceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_service(
        self,
    ) -> Callable[
        [apphub_service.DeleteServiceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_discovered_workloads(
        self,
    ) -> Callable[
        [apphub_service.ListDiscoveredWorkloadsRequest],
        Union[
            apphub_service.ListDiscoveredWorkloadsResponse,
            Awaitable[apphub_service.ListDiscoveredWorkloadsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_discovered_workload(
        self,
    ) -> Callable[
        [apphub_service.GetDiscoveredWorkloadRequest],
        Union[workload.DiscoveredWorkload, Awaitable[workload.DiscoveredWorkload]],
    ]:
        raise NotImplementedError()

    @property
    def lookup_discovered_workload(
        self,
    ) -> Callable[
        [apphub_service.LookupDiscoveredWorkloadRequest],
        Union[
            apphub_service.LookupDiscoveredWorkloadResponse,
            Awaitable[apphub_service.LookupDiscoveredWorkloadResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_workloads(
        self,
    ) -> Callable[
        [apphub_service.ListWorkloadsRequest],
        Union[
            apphub_service.ListWorkloadsResponse,
            Awaitable[apphub_service.ListWorkloadsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_workload(
        self,
    ) -> Callable[
        [apphub_service.CreateWorkloadRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_workload(
        self,
    ) -> Callable[
        [apphub_service.GetWorkloadRequest],
        Union[workload.Workload, Awaitable[workload.Workload]],
    ]:
        raise NotImplementedError()

    @property
    def update_workload(
        self,
    ) -> Callable[
        [apphub_service.UpdateWorkloadRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_workload(
        self,
    ) -> Callable[
        [apphub_service.DeleteWorkloadRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_applications(
        self,
    ) -> Callable[
        [apphub_service.ListApplicationsRequest],
        Union[
            apphub_service.ListApplicationsResponse,
            Awaitable[apphub_service.ListApplicationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_application(
        self,
    ) -> Callable[
        [apphub_service.CreateApplicationRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_application(
        self,
    ) -> Callable[
        [apphub_service.GetApplicationRequest],
        Union[application.Application, Awaitable[application.Application]],
    ]:
        raise NotImplementedError()

    @property
    def update_application(
        self,
    ) -> Callable[
        [apphub_service.UpdateApplicationRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_application(
        self,
    ) -> Callable[
        [apphub_service.DeleteApplicationRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_boundary(
        self,
    ) -> Callable[
        [apphub_service.GetBoundaryRequest],
        Union[boundary.Boundary, Awaitable[boundary.Boundary]],
    ]:
        raise NotImplementedError()

    @property
    def update_boundary(
        self,
    ) -> Callable[
        [apphub_service.UpdateBoundaryRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_extended_metadata_schema(
        self,
    ) -> Callable[
        [apphub_service.GetExtendedMetadataSchemaRequest],
        Union[
            extended_metadata_schema.ExtendedMetadataSchema,
            Awaitable[extended_metadata_schema.ExtendedMetadataSchema],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_extended_metadata_schemas(
        self,
    ) -> Callable[
        [apphub_service.ListExtendedMetadataSchemasRequest],
        Union[
            apphub_service.ListExtendedMetadataSchemasResponse,
            Awaitable[apphub_service.ListExtendedMetadataSchemasResponse],
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


__all__ = ("AppHubTransport",)
