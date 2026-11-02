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
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, operations_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.telcoautomation_v1alpha1 import gapic_version as package_version
from google.cloud.telcoautomation_v1alpha1.types import telcoautomation

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class TelcoAutomationTransport(abc.ABC):
    """Abstract transport class for TelcoAutomation."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "telcoautomation.googleapis.com"

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
                 The hostname to connect to (default: 'telcoautomation.googleapis.com').
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
            self.list_orchestration_clusters: gapic_v1.method.wrap_method(
                self.list_orchestration_clusters,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_orchestration_cluster: gapic_v1.method.wrap_method(
                self.get_orchestration_cluster,
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
            self.create_orchestration_cluster: gapic_v1.method.wrap_method(
                self.create_orchestration_cluster,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_orchestration_cluster: gapic_v1.method.wrap_method(
                self.delete_orchestration_cluster,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_edge_slms: gapic_v1.method.wrap_method(
                self.list_edge_slms,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_edge_slm: gapic_v1.method.wrap_method(
                self.get_edge_slm,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_edge_slm: gapic_v1.method.wrap_method(
                self.create_edge_slm,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_edge_slm: gapic_v1.method.wrap_method(
                self.delete_edge_slm,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_blueprint: gapic_v1.method.wrap_method(
                self.create_blueprint,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_blueprint: gapic_v1.method.wrap_method(
                self.update_blueprint,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_blueprint: gapic_v1.method.wrap_method(
                self.get_blueprint,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_blueprint: gapic_v1.method.wrap_method(
                self.delete_blueprint,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_blueprints: gapic_v1.method.wrap_method(
                self.list_blueprints,
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
            self.approve_blueprint: gapic_v1.method.wrap_method(
                self.approve_blueprint,
                default_timeout=None,
                client_info=client_info,
            ),
            self.propose_blueprint: gapic_v1.method.wrap_method(
                self.propose_blueprint,
                default_timeout=None,
                client_info=client_info,
            ),
            self.reject_blueprint: gapic_v1.method.wrap_method(
                self.reject_blueprint,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_blueprint_revisions: gapic_v1.method.wrap_method(
                self.list_blueprint_revisions,
                default_timeout=None,
                client_info=client_info,
            ),
            self.search_blueprint_revisions: gapic_v1.method.wrap_method(
                self.search_blueprint_revisions,
                default_timeout=None,
                client_info=client_info,
            ),
            self.search_deployment_revisions: gapic_v1.method.wrap_method(
                self.search_deployment_revisions,
                default_timeout=None,
                client_info=client_info,
            ),
            self.discard_blueprint_changes: gapic_v1.method.wrap_method(
                self.discard_blueprint_changes,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_public_blueprints: gapic_v1.method.wrap_method(
                self.list_public_blueprints,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_public_blueprint: gapic_v1.method.wrap_method(
                self.get_public_blueprint,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_deployment: gapic_v1.method.wrap_method(
                self.create_deployment,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_deployment: gapic_v1.method.wrap_method(
                self.update_deployment,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_deployment: gapic_v1.method.wrap_method(
                self.get_deployment,
                default_timeout=None,
                client_info=client_info,
            ),
            self.remove_deployment: gapic_v1.method.wrap_method(
                self.remove_deployment,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_deployments: gapic_v1.method.wrap_method(
                self.list_deployments,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_deployment_revisions: gapic_v1.method.wrap_method(
                self.list_deployment_revisions,
                default_timeout=None,
                client_info=client_info,
            ),
            self.discard_deployment_changes: gapic_v1.method.wrap_method(
                self.discard_deployment_changes,
                default_timeout=None,
                client_info=client_info,
            ),
            self.apply_deployment: gapic_v1.method.wrap_method(
                self.apply_deployment,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.compute_deployment_status: gapic_v1.method.wrap_method(
                self.compute_deployment_status,
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
            self.rollback_deployment: gapic_v1.method.wrap_method(
                self.rollback_deployment,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_hydrated_deployment: gapic_v1.method.wrap_method(
                self.get_hydrated_deployment,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_hydrated_deployments: gapic_v1.method.wrap_method(
                self.list_hydrated_deployments,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_hydrated_deployment: gapic_v1.method.wrap_method(
                self.update_hydrated_deployment,
                default_timeout=None,
                client_info=client_info,
            ),
            self.apply_hydrated_deployment: gapic_v1.method.wrap_method(
                self.apply_hydrated_deployment,
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
    def operations_client(self):
        """Return the client designed to process long-running operations."""
        raise NotImplementedError()

    @property
    def list_orchestration_clusters(
        self,
    ) -> Callable[
        [telcoautomation.ListOrchestrationClustersRequest],
        Union[
            telcoautomation.ListOrchestrationClustersResponse,
            Awaitable[telcoautomation.ListOrchestrationClustersResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_orchestration_cluster(
        self,
    ) -> Callable[
        [telcoautomation.GetOrchestrationClusterRequest],
        Union[
            telcoautomation.OrchestrationCluster,
            Awaitable[telcoautomation.OrchestrationCluster],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_orchestration_cluster(
        self,
    ) -> Callable[
        [telcoautomation.CreateOrchestrationClusterRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_orchestration_cluster(
        self,
    ) -> Callable[
        [telcoautomation.DeleteOrchestrationClusterRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_edge_slms(
        self,
    ) -> Callable[
        [telcoautomation.ListEdgeSlmsRequest],
        Union[
            telcoautomation.ListEdgeSlmsResponse,
            Awaitable[telcoautomation.ListEdgeSlmsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_edge_slm(
        self,
    ) -> Callable[
        [telcoautomation.GetEdgeSlmRequest],
        Union[telcoautomation.EdgeSlm, Awaitable[telcoautomation.EdgeSlm]],
    ]:
        raise NotImplementedError()

    @property
    def create_edge_slm(
        self,
    ) -> Callable[
        [telcoautomation.CreateEdgeSlmRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_edge_slm(
        self,
    ) -> Callable[
        [telcoautomation.DeleteEdgeSlmRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_blueprint(
        self,
    ) -> Callable[
        [telcoautomation.CreateBlueprintRequest],
        Union[telcoautomation.Blueprint, Awaitable[telcoautomation.Blueprint]],
    ]:
        raise NotImplementedError()

    @property
    def update_blueprint(
        self,
    ) -> Callable[
        [telcoautomation.UpdateBlueprintRequest],
        Union[telcoautomation.Blueprint, Awaitable[telcoautomation.Blueprint]],
    ]:
        raise NotImplementedError()

    @property
    def get_blueprint(
        self,
    ) -> Callable[
        [telcoautomation.GetBlueprintRequest],
        Union[telcoautomation.Blueprint, Awaitable[telcoautomation.Blueprint]],
    ]:
        raise NotImplementedError()

    @property
    def delete_blueprint(
        self,
    ) -> Callable[
        [telcoautomation.DeleteBlueprintRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def list_blueprints(
        self,
    ) -> Callable[
        [telcoautomation.ListBlueprintsRequest],
        Union[
            telcoautomation.ListBlueprintsResponse,
            Awaitable[telcoautomation.ListBlueprintsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def approve_blueprint(
        self,
    ) -> Callable[
        [telcoautomation.ApproveBlueprintRequest],
        Union[telcoautomation.Blueprint, Awaitable[telcoautomation.Blueprint]],
    ]:
        raise NotImplementedError()

    @property
    def propose_blueprint(
        self,
    ) -> Callable[
        [telcoautomation.ProposeBlueprintRequest],
        Union[telcoautomation.Blueprint, Awaitable[telcoautomation.Blueprint]],
    ]:
        raise NotImplementedError()

    @property
    def reject_blueprint(
        self,
    ) -> Callable[
        [telcoautomation.RejectBlueprintRequest],
        Union[telcoautomation.Blueprint, Awaitable[telcoautomation.Blueprint]],
    ]:
        raise NotImplementedError()

    @property
    def list_blueprint_revisions(
        self,
    ) -> Callable[
        [telcoautomation.ListBlueprintRevisionsRequest],
        Union[
            telcoautomation.ListBlueprintRevisionsResponse,
            Awaitable[telcoautomation.ListBlueprintRevisionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def search_blueprint_revisions(
        self,
    ) -> Callable[
        [telcoautomation.SearchBlueprintRevisionsRequest],
        Union[
            telcoautomation.SearchBlueprintRevisionsResponse,
            Awaitable[telcoautomation.SearchBlueprintRevisionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def search_deployment_revisions(
        self,
    ) -> Callable[
        [telcoautomation.SearchDeploymentRevisionsRequest],
        Union[
            telcoautomation.SearchDeploymentRevisionsResponse,
            Awaitable[telcoautomation.SearchDeploymentRevisionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def discard_blueprint_changes(
        self,
    ) -> Callable[
        [telcoautomation.DiscardBlueprintChangesRequest],
        Union[
            telcoautomation.DiscardBlueprintChangesResponse,
            Awaitable[telcoautomation.DiscardBlueprintChangesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_public_blueprints(
        self,
    ) -> Callable[
        [telcoautomation.ListPublicBlueprintsRequest],
        Union[
            telcoautomation.ListPublicBlueprintsResponse,
            Awaitable[telcoautomation.ListPublicBlueprintsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_public_blueprint(
        self,
    ) -> Callable[
        [telcoautomation.GetPublicBlueprintRequest],
        Union[
            telcoautomation.PublicBlueprint, Awaitable[telcoautomation.PublicBlueprint]
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_deployment(
        self,
    ) -> Callable[
        [telcoautomation.CreateDeploymentRequest],
        Union[telcoautomation.Deployment, Awaitable[telcoautomation.Deployment]],
    ]:
        raise NotImplementedError()

    @property
    def update_deployment(
        self,
    ) -> Callable[
        [telcoautomation.UpdateDeploymentRequest],
        Union[telcoautomation.Deployment, Awaitable[telcoautomation.Deployment]],
    ]:
        raise NotImplementedError()

    @property
    def get_deployment(
        self,
    ) -> Callable[
        [telcoautomation.GetDeploymentRequest],
        Union[telcoautomation.Deployment, Awaitable[telcoautomation.Deployment]],
    ]:
        raise NotImplementedError()

    @property
    def remove_deployment(
        self,
    ) -> Callable[
        [telcoautomation.RemoveDeploymentRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def list_deployments(
        self,
    ) -> Callable[
        [telcoautomation.ListDeploymentsRequest],
        Union[
            telcoautomation.ListDeploymentsResponse,
            Awaitable[telcoautomation.ListDeploymentsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_deployment_revisions(
        self,
    ) -> Callable[
        [telcoautomation.ListDeploymentRevisionsRequest],
        Union[
            telcoautomation.ListDeploymentRevisionsResponse,
            Awaitable[telcoautomation.ListDeploymentRevisionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def discard_deployment_changes(
        self,
    ) -> Callable[
        [telcoautomation.DiscardDeploymentChangesRequest],
        Union[
            telcoautomation.DiscardDeploymentChangesResponse,
            Awaitable[telcoautomation.DiscardDeploymentChangesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def apply_deployment(
        self,
    ) -> Callable[
        [telcoautomation.ApplyDeploymentRequest],
        Union[telcoautomation.Deployment, Awaitable[telcoautomation.Deployment]],
    ]:
        raise NotImplementedError()

    @property
    def compute_deployment_status(
        self,
    ) -> Callable[
        [telcoautomation.ComputeDeploymentStatusRequest],
        Union[
            telcoautomation.ComputeDeploymentStatusResponse,
            Awaitable[telcoautomation.ComputeDeploymentStatusResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def rollback_deployment(
        self,
    ) -> Callable[
        [telcoautomation.RollbackDeploymentRequest],
        Union[telcoautomation.Deployment, Awaitable[telcoautomation.Deployment]],
    ]:
        raise NotImplementedError()

    @property
    def get_hydrated_deployment(
        self,
    ) -> Callable[
        [telcoautomation.GetHydratedDeploymentRequest],
        Union[
            telcoautomation.HydratedDeployment,
            Awaitable[telcoautomation.HydratedDeployment],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_hydrated_deployments(
        self,
    ) -> Callable[
        [telcoautomation.ListHydratedDeploymentsRequest],
        Union[
            telcoautomation.ListHydratedDeploymentsResponse,
            Awaitable[telcoautomation.ListHydratedDeploymentsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_hydrated_deployment(
        self,
    ) -> Callable[
        [telcoautomation.UpdateHydratedDeploymentRequest],
        Union[
            telcoautomation.HydratedDeployment,
            Awaitable[telcoautomation.HydratedDeployment],
        ],
    ]:
        raise NotImplementedError()

    @property
    def apply_hydrated_deployment(
        self,
    ) -> Callable[
        [telcoautomation.ApplyHydratedDeploymentRequest],
        Union[
            telcoautomation.HydratedDeployment,
            Awaitable[telcoautomation.HydratedDeployment],
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


__all__ = ("TelcoAutomationTransport",)
