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
import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
import google.iam.v1.policy_pb2 as policy_pb2  # type: ignore
import google.protobuf
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.bigquery_reservation_v1 import gapic_version as package_version
from google.cloud.bigquery_reservation_v1.types import reservation
from google.cloud.bigquery_reservation_v1.types import reservation as gcbr_reservation

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class ReservationServiceTransport(abc.ABC):
    """Abstract transport class for ReservationService."""

    AUTH_SCOPES = (
        "https://www.googleapis.com/auth/bigquery",
        "https://www.googleapis.com/auth/cloud-platform",
    )

    DEFAULT_HOST: str = "bigqueryreservation.googleapis.com"

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
                 The hostname to connect to (default: 'bigqueryreservation.googleapis.com').
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
            self.create_reservation: gapic_v1.method.wrap_method(
                self.create_reservation,
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.list_reservations: gapic_v1.method.wrap_method(
                self.list_reservations,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.get_reservation: gapic_v1.method.wrap_method(
                self.get_reservation,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.delete_reservation: gapic_v1.method.wrap_method(
                self.delete_reservation,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.update_reservation: gapic_v1.method.wrap_method(
                self.update_reservation,
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.failover_reservation: gapic_v1.method.wrap_method(
                self.failover_reservation,
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.create_capacity_commitment: gapic_v1.method.wrap_method(
                self.create_capacity_commitment,
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.list_capacity_commitments: gapic_v1.method.wrap_method(
                self.list_capacity_commitments,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.get_capacity_commitment: gapic_v1.method.wrap_method(
                self.get_capacity_commitment,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.delete_capacity_commitment: gapic_v1.method.wrap_method(
                self.delete_capacity_commitment,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.update_capacity_commitment: gapic_v1.method.wrap_method(
                self.update_capacity_commitment,
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.split_capacity_commitment: gapic_v1.method.wrap_method(
                self.split_capacity_commitment,
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.merge_capacity_commitments: gapic_v1.method.wrap_method(
                self.merge_capacity_commitments,
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.create_assignment: gapic_v1.method.wrap_method(
                self.create_assignment,
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.list_assignments: gapic_v1.method.wrap_method(
                self.list_assignments,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.delete_assignment: gapic_v1.method.wrap_method(
                self.delete_assignment,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.search_assignments: gapic_v1.method.wrap_method(
                self.search_assignments,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.search_all_assignments: gapic_v1.method.wrap_method(
                self.search_all_assignments,
                default_timeout=None,
                client_info=client_info,
            ),
            self.move_assignment: gapic_v1.method.wrap_method(
                self.move_assignment,
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.update_assignment: gapic_v1.method.wrap_method(
                self.update_assignment,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_bi_reservation: gapic_v1.method.wrap_method(
                self.get_bi_reservation,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.update_bi_reservation: gapic_v1.method.wrap_method(
                self.update_bi_reservation,
                default_timeout=300.0,
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
            self.create_reservation_group: gapic_v1.method.wrap_method(
                self.create_reservation_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_reservation_group: gapic_v1.method.wrap_method(
                self.get_reservation_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_reservation_group: gapic_v1.method.wrap_method(
                self.delete_reservation_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_reservation_groups: gapic_v1.method.wrap_method(
                self.list_reservation_groups,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_reservation_group: gapic_v1.method.wrap_method(
                self.update_reservation_group,
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
    def create_reservation(
        self,
    ) -> Callable[
        [gcbr_reservation.CreateReservationRequest],
        Union[gcbr_reservation.Reservation, Awaitable[gcbr_reservation.Reservation]],
    ]:
        raise NotImplementedError()

    @property
    def list_reservations(
        self,
    ) -> Callable[
        [reservation.ListReservationsRequest],
        Union[
            reservation.ListReservationsResponse,
            Awaitable[reservation.ListReservationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_reservation(
        self,
    ) -> Callable[
        [reservation.GetReservationRequest],
        Union[reservation.Reservation, Awaitable[reservation.Reservation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_reservation(
        self,
    ) -> Callable[
        [reservation.DeleteReservationRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def update_reservation(
        self,
    ) -> Callable[
        [gcbr_reservation.UpdateReservationRequest],
        Union[gcbr_reservation.Reservation, Awaitable[gcbr_reservation.Reservation]],
    ]:
        raise NotImplementedError()

    @property
    def failover_reservation(
        self,
    ) -> Callable[
        [reservation.FailoverReservationRequest],
        Union[reservation.Reservation, Awaitable[reservation.Reservation]],
    ]:
        raise NotImplementedError()

    @property
    def create_capacity_commitment(
        self,
    ) -> Callable[
        [reservation.CreateCapacityCommitmentRequest],
        Union[
            reservation.CapacityCommitment, Awaitable[reservation.CapacityCommitment]
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_capacity_commitments(
        self,
    ) -> Callable[
        [reservation.ListCapacityCommitmentsRequest],
        Union[
            reservation.ListCapacityCommitmentsResponse,
            Awaitable[reservation.ListCapacityCommitmentsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_capacity_commitment(
        self,
    ) -> Callable[
        [reservation.GetCapacityCommitmentRequest],
        Union[
            reservation.CapacityCommitment, Awaitable[reservation.CapacityCommitment]
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_capacity_commitment(
        self,
    ) -> Callable[
        [reservation.DeleteCapacityCommitmentRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def update_capacity_commitment(
        self,
    ) -> Callable[
        [reservation.UpdateCapacityCommitmentRequest],
        Union[
            reservation.CapacityCommitment, Awaitable[reservation.CapacityCommitment]
        ],
    ]:
        raise NotImplementedError()

    @property
    def split_capacity_commitment(
        self,
    ) -> Callable[
        [reservation.SplitCapacityCommitmentRequest],
        Union[
            reservation.SplitCapacityCommitmentResponse,
            Awaitable[reservation.SplitCapacityCommitmentResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def merge_capacity_commitments(
        self,
    ) -> Callable[
        [reservation.MergeCapacityCommitmentsRequest],
        Union[
            reservation.CapacityCommitment, Awaitable[reservation.CapacityCommitment]
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_assignment(
        self,
    ) -> Callable[
        [reservation.CreateAssignmentRequest],
        Union[reservation.Assignment, Awaitable[reservation.Assignment]],
    ]:
        raise NotImplementedError()

    @property
    def list_assignments(
        self,
    ) -> Callable[
        [reservation.ListAssignmentsRequest],
        Union[
            reservation.ListAssignmentsResponse,
            Awaitable[reservation.ListAssignmentsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_assignment(
        self,
    ) -> Callable[
        [reservation.DeleteAssignmentRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def search_assignments(
        self,
    ) -> Callable[
        [reservation.SearchAssignmentsRequest],
        Union[
            reservation.SearchAssignmentsResponse,
            Awaitable[reservation.SearchAssignmentsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def search_all_assignments(
        self,
    ) -> Callable[
        [reservation.SearchAllAssignmentsRequest],
        Union[
            reservation.SearchAllAssignmentsResponse,
            Awaitable[reservation.SearchAllAssignmentsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def move_assignment(
        self,
    ) -> Callable[
        [reservation.MoveAssignmentRequest],
        Union[reservation.Assignment, Awaitable[reservation.Assignment]],
    ]:
        raise NotImplementedError()

    @property
    def update_assignment(
        self,
    ) -> Callable[
        [reservation.UpdateAssignmentRequest],
        Union[reservation.Assignment, Awaitable[reservation.Assignment]],
    ]:
        raise NotImplementedError()

    @property
    def get_bi_reservation(
        self,
    ) -> Callable[
        [reservation.GetBiReservationRequest],
        Union[reservation.BiReservation, Awaitable[reservation.BiReservation]],
    ]:
        raise NotImplementedError()

    @property
    def update_bi_reservation(
        self,
    ) -> Callable[
        [reservation.UpdateBiReservationRequest],
        Union[reservation.BiReservation, Awaitable[reservation.BiReservation]],
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
    def set_iam_policy(
        self,
    ) -> Callable[
        [iam_policy_pb2.SetIamPolicyRequest],
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
    def create_reservation_group(
        self,
    ) -> Callable[
        [reservation.CreateReservationGroupRequest],
        Union[reservation.ReservationGroup, Awaitable[reservation.ReservationGroup]],
    ]:
        raise NotImplementedError()

    @property
    def get_reservation_group(
        self,
    ) -> Callable[
        [reservation.GetReservationGroupRequest],
        Union[reservation.ReservationGroup, Awaitable[reservation.ReservationGroup]],
    ]:
        raise NotImplementedError()

    @property
    def delete_reservation_group(
        self,
    ) -> Callable[
        [reservation.DeleteReservationGroupRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def list_reservation_groups(
        self,
    ) -> Callable[
        [reservation.ListReservationGroupsRequest],
        Union[
            reservation.ListReservationGroupsResponse,
            Awaitable[reservation.ListReservationGroupsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_reservation_group(
        self,
    ) -> Callable[
        [reservation.UpdateReservationGroupRequest],
        Union[reservation.ReservationGroup, Awaitable[reservation.ReservationGroup]],
    ]:
        raise NotImplementedError()

    @property
    def kind(self) -> str:
        raise NotImplementedError()


__all__ = ("ReservationServiceTransport",)
