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
from google.api_core import gapic_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.bigquery_reservation_v1._compat import transcode_request
from google.cloud.bigquery_reservation_v1.types import reservation
from google.cloud.bigquery_reservation_v1.types import reservation as gcbr_reservation

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseReservationServiceRestTransport

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


class ReservationServiceRestInterceptor:
    """Interceptor for ReservationService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the ReservationServiceRestTransport.

    .. code-block:: python
        class MyCustomReservationServiceInterceptor(ReservationServiceRestInterceptor):
            def pre_create_assignment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_assignment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_capacity_commitment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_capacity_commitment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_reservation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_reservation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_reservation_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_reservation_group(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_assignment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_capacity_commitment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_reservation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_reservation_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_failover_reservation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_failover_reservation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_bi_reservation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_bi_reservation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_capacity_commitment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_capacity_commitment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_iam_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_iam_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_reservation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_reservation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_reservation_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_reservation_group(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_assignments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_assignments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_capacity_commitments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_capacity_commitments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_reservation_groups(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_reservation_groups(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_reservations(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_reservations(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_merge_capacity_commitments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_merge_capacity_commitments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_move_assignment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_move_assignment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_search_all_assignments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_search_all_assignments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_search_assignments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_search_assignments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_iam_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_iam_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_split_capacity_commitment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_split_capacity_commitment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_test_iam_permissions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_test_iam_permissions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_assignment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_assignment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_bi_reservation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_bi_reservation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_capacity_commitment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_capacity_commitment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_reservation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_reservation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_reservation_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_reservation_group(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = ReservationServiceRestTransport(interceptor=MyCustomReservationServiceInterceptor())
        client = ReservationServiceClient(transport=transport)


    """

    def pre_create_assignment(
        self,
        request: reservation.CreateAssignmentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        reservation.CreateAssignmentRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_assignment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ReservationService server.
        """
        return request, metadata

    def post_create_assignment(
        self, response: reservation.Assignment
    ) -> reservation.Assignment:
        """Post-rpc interceptor for create_assignment

        DEPRECATED. Please use the `post_create_assignment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ReservationService server but before
        it is returned to user code. This `post_create_assignment` interceptor runs
        before the `post_create_assignment_with_metadata` interceptor.
        """
        return response

    def post_create_assignment_with_metadata(
        self,
        response: reservation.Assignment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[reservation.Assignment, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_assignment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ReservationService server but before it is returned to user code.

        We recommend only using this `post_create_assignment_with_metadata`
        interceptor in new development instead of the `post_create_assignment` interceptor.
        When both interceptors are used, this `post_create_assignment_with_metadata` interceptor runs after the
        `post_create_assignment` interceptor. The (possibly modified) response returned by
        `post_create_assignment` will be passed to
        `post_create_assignment_with_metadata`.
        """
        return response, metadata

    def pre_create_capacity_commitment(
        self,
        request: reservation.CreateCapacityCommitmentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        reservation.CreateCapacityCommitmentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_capacity_commitment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ReservationService server.
        """
        return request, metadata

    def post_create_capacity_commitment(
        self, response: reservation.CapacityCommitment
    ) -> reservation.CapacityCommitment:
        """Post-rpc interceptor for create_capacity_commitment

        DEPRECATED. Please use the `post_create_capacity_commitment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ReservationService server but before
        it is returned to user code. This `post_create_capacity_commitment` interceptor runs
        before the `post_create_capacity_commitment_with_metadata` interceptor.
        """
        return response

    def post_create_capacity_commitment_with_metadata(
        self,
        response: reservation.CapacityCommitment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[reservation.CapacityCommitment, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_capacity_commitment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ReservationService server but before it is returned to user code.

        We recommend only using this `post_create_capacity_commitment_with_metadata`
        interceptor in new development instead of the `post_create_capacity_commitment` interceptor.
        When both interceptors are used, this `post_create_capacity_commitment_with_metadata` interceptor runs after the
        `post_create_capacity_commitment` interceptor. The (possibly modified) response returned by
        `post_create_capacity_commitment` will be passed to
        `post_create_capacity_commitment_with_metadata`.
        """
        return response, metadata

    def pre_create_reservation(
        self,
        request: gcbr_reservation.CreateReservationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcbr_reservation.CreateReservationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_reservation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ReservationService server.
        """
        return request, metadata

    def post_create_reservation(
        self, response: gcbr_reservation.Reservation
    ) -> gcbr_reservation.Reservation:
        """Post-rpc interceptor for create_reservation

        DEPRECATED. Please use the `post_create_reservation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ReservationService server but before
        it is returned to user code. This `post_create_reservation` interceptor runs
        before the `post_create_reservation_with_metadata` interceptor.
        """
        return response

    def post_create_reservation_with_metadata(
        self,
        response: gcbr_reservation.Reservation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcbr_reservation.Reservation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_reservation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ReservationService server but before it is returned to user code.

        We recommend only using this `post_create_reservation_with_metadata`
        interceptor in new development instead of the `post_create_reservation` interceptor.
        When both interceptors are used, this `post_create_reservation_with_metadata` interceptor runs after the
        `post_create_reservation` interceptor. The (possibly modified) response returned by
        `post_create_reservation` will be passed to
        `post_create_reservation_with_metadata`.
        """
        return response, metadata

    def pre_create_reservation_group(
        self,
        request: reservation.CreateReservationGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        reservation.CreateReservationGroupRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_reservation_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ReservationService server.
        """
        return request, metadata

    def post_create_reservation_group(
        self, response: reservation.ReservationGroup
    ) -> reservation.ReservationGroup:
        """Post-rpc interceptor for create_reservation_group

        DEPRECATED. Please use the `post_create_reservation_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ReservationService server but before
        it is returned to user code. This `post_create_reservation_group` interceptor runs
        before the `post_create_reservation_group_with_metadata` interceptor.
        """
        return response

    def post_create_reservation_group_with_metadata(
        self,
        response: reservation.ReservationGroup,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[reservation.ReservationGroup, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_reservation_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ReservationService server but before it is returned to user code.

        We recommend only using this `post_create_reservation_group_with_metadata`
        interceptor in new development instead of the `post_create_reservation_group` interceptor.
        When both interceptors are used, this `post_create_reservation_group_with_metadata` interceptor runs after the
        `post_create_reservation_group` interceptor. The (possibly modified) response returned by
        `post_create_reservation_group` will be passed to
        `post_create_reservation_group_with_metadata`.
        """
        return response, metadata

    def pre_delete_assignment(
        self,
        request: reservation.DeleteAssignmentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        reservation.DeleteAssignmentRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_assignment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ReservationService server.
        """
        return request, metadata

    def pre_delete_capacity_commitment(
        self,
        request: reservation.DeleteCapacityCommitmentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        reservation.DeleteCapacityCommitmentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_capacity_commitment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ReservationService server.
        """
        return request, metadata

    def pre_delete_reservation(
        self,
        request: reservation.DeleteReservationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        reservation.DeleteReservationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_reservation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ReservationService server.
        """
        return request, metadata

    def pre_delete_reservation_group(
        self,
        request: reservation.DeleteReservationGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        reservation.DeleteReservationGroupRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_reservation_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ReservationService server.
        """
        return request, metadata

    def pre_failover_reservation(
        self,
        request: reservation.FailoverReservationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        reservation.FailoverReservationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for failover_reservation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ReservationService server.
        """
        return request, metadata

    def post_failover_reservation(
        self, response: reservation.Reservation
    ) -> reservation.Reservation:
        """Post-rpc interceptor for failover_reservation

        DEPRECATED. Please use the `post_failover_reservation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ReservationService server but before
        it is returned to user code. This `post_failover_reservation` interceptor runs
        before the `post_failover_reservation_with_metadata` interceptor.
        """
        return response

    def post_failover_reservation_with_metadata(
        self,
        response: reservation.Reservation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[reservation.Reservation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for failover_reservation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ReservationService server but before it is returned to user code.

        We recommend only using this `post_failover_reservation_with_metadata`
        interceptor in new development instead of the `post_failover_reservation` interceptor.
        When both interceptors are used, this `post_failover_reservation_with_metadata` interceptor runs after the
        `post_failover_reservation` interceptor. The (possibly modified) response returned by
        `post_failover_reservation` will be passed to
        `post_failover_reservation_with_metadata`.
        """
        return response, metadata

    def pre_get_bi_reservation(
        self,
        request: reservation.GetBiReservationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        reservation.GetBiReservationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_bi_reservation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ReservationService server.
        """
        return request, metadata

    def post_get_bi_reservation(
        self, response: reservation.BiReservation
    ) -> reservation.BiReservation:
        """Post-rpc interceptor for get_bi_reservation

        DEPRECATED. Please use the `post_get_bi_reservation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ReservationService server but before
        it is returned to user code. This `post_get_bi_reservation` interceptor runs
        before the `post_get_bi_reservation_with_metadata` interceptor.
        """
        return response

    def post_get_bi_reservation_with_metadata(
        self,
        response: reservation.BiReservation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[reservation.BiReservation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_bi_reservation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ReservationService server but before it is returned to user code.

        We recommend only using this `post_get_bi_reservation_with_metadata`
        interceptor in new development instead of the `post_get_bi_reservation` interceptor.
        When both interceptors are used, this `post_get_bi_reservation_with_metadata` interceptor runs after the
        `post_get_bi_reservation` interceptor. The (possibly modified) response returned by
        `post_get_bi_reservation` will be passed to
        `post_get_bi_reservation_with_metadata`.
        """
        return response, metadata

    def pre_get_capacity_commitment(
        self,
        request: reservation.GetCapacityCommitmentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        reservation.GetCapacityCommitmentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_capacity_commitment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ReservationService server.
        """
        return request, metadata

    def post_get_capacity_commitment(
        self, response: reservation.CapacityCommitment
    ) -> reservation.CapacityCommitment:
        """Post-rpc interceptor for get_capacity_commitment

        DEPRECATED. Please use the `post_get_capacity_commitment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ReservationService server but before
        it is returned to user code. This `post_get_capacity_commitment` interceptor runs
        before the `post_get_capacity_commitment_with_metadata` interceptor.
        """
        return response

    def post_get_capacity_commitment_with_metadata(
        self,
        response: reservation.CapacityCommitment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[reservation.CapacityCommitment, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_capacity_commitment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ReservationService server but before it is returned to user code.

        We recommend only using this `post_get_capacity_commitment_with_metadata`
        interceptor in new development instead of the `post_get_capacity_commitment` interceptor.
        When both interceptors are used, this `post_get_capacity_commitment_with_metadata` interceptor runs after the
        `post_get_capacity_commitment` interceptor. The (possibly modified) response returned by
        `post_get_capacity_commitment` will be passed to
        `post_get_capacity_commitment_with_metadata`.
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
        before they are sent to the ReservationService server.
        """
        return request, metadata

    def post_get_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        DEPRECATED. Please use the `post_get_iam_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ReservationService server but before
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
        is returned by the ReservationService server but before it is returned to user code.

        We recommend only using this `post_get_iam_policy_with_metadata`
        interceptor in new development instead of the `post_get_iam_policy` interceptor.
        When both interceptors are used, this `post_get_iam_policy_with_metadata` interceptor runs after the
        `post_get_iam_policy` interceptor. The (possibly modified) response returned by
        `post_get_iam_policy` will be passed to
        `post_get_iam_policy_with_metadata`.
        """
        return response, metadata

    def pre_get_reservation(
        self,
        request: reservation.GetReservationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        reservation.GetReservationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_reservation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ReservationService server.
        """
        return request, metadata

    def post_get_reservation(
        self, response: reservation.Reservation
    ) -> reservation.Reservation:
        """Post-rpc interceptor for get_reservation

        DEPRECATED. Please use the `post_get_reservation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ReservationService server but before
        it is returned to user code. This `post_get_reservation` interceptor runs
        before the `post_get_reservation_with_metadata` interceptor.
        """
        return response

    def post_get_reservation_with_metadata(
        self,
        response: reservation.Reservation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[reservation.Reservation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_reservation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ReservationService server but before it is returned to user code.

        We recommend only using this `post_get_reservation_with_metadata`
        interceptor in new development instead of the `post_get_reservation` interceptor.
        When both interceptors are used, this `post_get_reservation_with_metadata` interceptor runs after the
        `post_get_reservation` interceptor. The (possibly modified) response returned by
        `post_get_reservation` will be passed to
        `post_get_reservation_with_metadata`.
        """
        return response, metadata

    def pre_get_reservation_group(
        self,
        request: reservation.GetReservationGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        reservation.GetReservationGroupRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_reservation_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ReservationService server.
        """
        return request, metadata

    def post_get_reservation_group(
        self, response: reservation.ReservationGroup
    ) -> reservation.ReservationGroup:
        """Post-rpc interceptor for get_reservation_group

        DEPRECATED. Please use the `post_get_reservation_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ReservationService server but before
        it is returned to user code. This `post_get_reservation_group` interceptor runs
        before the `post_get_reservation_group_with_metadata` interceptor.
        """
        return response

    def post_get_reservation_group_with_metadata(
        self,
        response: reservation.ReservationGroup,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[reservation.ReservationGroup, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_reservation_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ReservationService server but before it is returned to user code.

        We recommend only using this `post_get_reservation_group_with_metadata`
        interceptor in new development instead of the `post_get_reservation_group` interceptor.
        When both interceptors are used, this `post_get_reservation_group_with_metadata` interceptor runs after the
        `post_get_reservation_group` interceptor. The (possibly modified) response returned by
        `post_get_reservation_group` will be passed to
        `post_get_reservation_group_with_metadata`.
        """
        return response, metadata

    def pre_list_assignments(
        self,
        request: reservation.ListAssignmentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        reservation.ListAssignmentsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_assignments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ReservationService server.
        """
        return request, metadata

    def post_list_assignments(
        self, response: reservation.ListAssignmentsResponse
    ) -> reservation.ListAssignmentsResponse:
        """Post-rpc interceptor for list_assignments

        DEPRECATED. Please use the `post_list_assignments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ReservationService server but before
        it is returned to user code. This `post_list_assignments` interceptor runs
        before the `post_list_assignments_with_metadata` interceptor.
        """
        return response

    def post_list_assignments_with_metadata(
        self,
        response: reservation.ListAssignmentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        reservation.ListAssignmentsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_assignments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ReservationService server but before it is returned to user code.

        We recommend only using this `post_list_assignments_with_metadata`
        interceptor in new development instead of the `post_list_assignments` interceptor.
        When both interceptors are used, this `post_list_assignments_with_metadata` interceptor runs after the
        `post_list_assignments` interceptor. The (possibly modified) response returned by
        `post_list_assignments` will be passed to
        `post_list_assignments_with_metadata`.
        """
        return response, metadata

    def pre_list_capacity_commitments(
        self,
        request: reservation.ListCapacityCommitmentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        reservation.ListCapacityCommitmentsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_capacity_commitments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ReservationService server.
        """
        return request, metadata

    def post_list_capacity_commitments(
        self, response: reservation.ListCapacityCommitmentsResponse
    ) -> reservation.ListCapacityCommitmentsResponse:
        """Post-rpc interceptor for list_capacity_commitments

        DEPRECATED. Please use the `post_list_capacity_commitments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ReservationService server but before
        it is returned to user code. This `post_list_capacity_commitments` interceptor runs
        before the `post_list_capacity_commitments_with_metadata` interceptor.
        """
        return response

    def post_list_capacity_commitments_with_metadata(
        self,
        response: reservation.ListCapacityCommitmentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        reservation.ListCapacityCommitmentsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_capacity_commitments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ReservationService server but before it is returned to user code.

        We recommend only using this `post_list_capacity_commitments_with_metadata`
        interceptor in new development instead of the `post_list_capacity_commitments` interceptor.
        When both interceptors are used, this `post_list_capacity_commitments_with_metadata` interceptor runs after the
        `post_list_capacity_commitments` interceptor. The (possibly modified) response returned by
        `post_list_capacity_commitments` will be passed to
        `post_list_capacity_commitments_with_metadata`.
        """
        return response, metadata

    def pre_list_reservation_groups(
        self,
        request: reservation.ListReservationGroupsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        reservation.ListReservationGroupsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_reservation_groups

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ReservationService server.
        """
        return request, metadata

    def post_list_reservation_groups(
        self, response: reservation.ListReservationGroupsResponse
    ) -> reservation.ListReservationGroupsResponse:
        """Post-rpc interceptor for list_reservation_groups

        DEPRECATED. Please use the `post_list_reservation_groups_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ReservationService server but before
        it is returned to user code. This `post_list_reservation_groups` interceptor runs
        before the `post_list_reservation_groups_with_metadata` interceptor.
        """
        return response

    def post_list_reservation_groups_with_metadata(
        self,
        response: reservation.ListReservationGroupsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        reservation.ListReservationGroupsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_reservation_groups

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ReservationService server but before it is returned to user code.

        We recommend only using this `post_list_reservation_groups_with_metadata`
        interceptor in new development instead of the `post_list_reservation_groups` interceptor.
        When both interceptors are used, this `post_list_reservation_groups_with_metadata` interceptor runs after the
        `post_list_reservation_groups` interceptor. The (possibly modified) response returned by
        `post_list_reservation_groups` will be passed to
        `post_list_reservation_groups_with_metadata`.
        """
        return response, metadata

    def pre_list_reservations(
        self,
        request: reservation.ListReservationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        reservation.ListReservationsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_reservations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ReservationService server.
        """
        return request, metadata

    def post_list_reservations(
        self, response: reservation.ListReservationsResponse
    ) -> reservation.ListReservationsResponse:
        """Post-rpc interceptor for list_reservations

        DEPRECATED. Please use the `post_list_reservations_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ReservationService server but before
        it is returned to user code. This `post_list_reservations` interceptor runs
        before the `post_list_reservations_with_metadata` interceptor.
        """
        return response

    def post_list_reservations_with_metadata(
        self,
        response: reservation.ListReservationsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        reservation.ListReservationsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_reservations

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ReservationService server but before it is returned to user code.

        We recommend only using this `post_list_reservations_with_metadata`
        interceptor in new development instead of the `post_list_reservations` interceptor.
        When both interceptors are used, this `post_list_reservations_with_metadata` interceptor runs after the
        `post_list_reservations` interceptor. The (possibly modified) response returned by
        `post_list_reservations` will be passed to
        `post_list_reservations_with_metadata`.
        """
        return response, metadata

    def pre_merge_capacity_commitments(
        self,
        request: reservation.MergeCapacityCommitmentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        reservation.MergeCapacityCommitmentsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for merge_capacity_commitments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ReservationService server.
        """
        return request, metadata

    def post_merge_capacity_commitments(
        self, response: reservation.CapacityCommitment
    ) -> reservation.CapacityCommitment:
        """Post-rpc interceptor for merge_capacity_commitments

        DEPRECATED. Please use the `post_merge_capacity_commitments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ReservationService server but before
        it is returned to user code. This `post_merge_capacity_commitments` interceptor runs
        before the `post_merge_capacity_commitments_with_metadata` interceptor.
        """
        return response

    def post_merge_capacity_commitments_with_metadata(
        self,
        response: reservation.CapacityCommitment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[reservation.CapacityCommitment, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for merge_capacity_commitments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ReservationService server but before it is returned to user code.

        We recommend only using this `post_merge_capacity_commitments_with_metadata`
        interceptor in new development instead of the `post_merge_capacity_commitments` interceptor.
        When both interceptors are used, this `post_merge_capacity_commitments_with_metadata` interceptor runs after the
        `post_merge_capacity_commitments` interceptor. The (possibly modified) response returned by
        `post_merge_capacity_commitments` will be passed to
        `post_merge_capacity_commitments_with_metadata`.
        """
        return response, metadata

    def pre_move_assignment(
        self,
        request: reservation.MoveAssignmentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        reservation.MoveAssignmentRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for move_assignment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ReservationService server.
        """
        return request, metadata

    def post_move_assignment(
        self, response: reservation.Assignment
    ) -> reservation.Assignment:
        """Post-rpc interceptor for move_assignment

        DEPRECATED. Please use the `post_move_assignment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ReservationService server but before
        it is returned to user code. This `post_move_assignment` interceptor runs
        before the `post_move_assignment_with_metadata` interceptor.
        """
        return response

    def post_move_assignment_with_metadata(
        self,
        response: reservation.Assignment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[reservation.Assignment, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for move_assignment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ReservationService server but before it is returned to user code.

        We recommend only using this `post_move_assignment_with_metadata`
        interceptor in new development instead of the `post_move_assignment` interceptor.
        When both interceptors are used, this `post_move_assignment_with_metadata` interceptor runs after the
        `post_move_assignment` interceptor. The (possibly modified) response returned by
        `post_move_assignment` will be passed to
        `post_move_assignment_with_metadata`.
        """
        return response, metadata

    def pre_search_all_assignments(
        self,
        request: reservation.SearchAllAssignmentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        reservation.SearchAllAssignmentsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for search_all_assignments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ReservationService server.
        """
        return request, metadata

    def post_search_all_assignments(
        self, response: reservation.SearchAllAssignmentsResponse
    ) -> reservation.SearchAllAssignmentsResponse:
        """Post-rpc interceptor for search_all_assignments

        DEPRECATED. Please use the `post_search_all_assignments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ReservationService server but before
        it is returned to user code. This `post_search_all_assignments` interceptor runs
        before the `post_search_all_assignments_with_metadata` interceptor.
        """
        return response

    def post_search_all_assignments_with_metadata(
        self,
        response: reservation.SearchAllAssignmentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        reservation.SearchAllAssignmentsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for search_all_assignments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ReservationService server but before it is returned to user code.

        We recommend only using this `post_search_all_assignments_with_metadata`
        interceptor in new development instead of the `post_search_all_assignments` interceptor.
        When both interceptors are used, this `post_search_all_assignments_with_metadata` interceptor runs after the
        `post_search_all_assignments` interceptor. The (possibly modified) response returned by
        `post_search_all_assignments` will be passed to
        `post_search_all_assignments_with_metadata`.
        """
        return response, metadata

    def pre_search_assignments(
        self,
        request: reservation.SearchAssignmentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        reservation.SearchAssignmentsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for search_assignments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ReservationService server.
        """
        return request, metadata

    def post_search_assignments(
        self, response: reservation.SearchAssignmentsResponse
    ) -> reservation.SearchAssignmentsResponse:
        """Post-rpc interceptor for search_assignments

        DEPRECATED. Please use the `post_search_assignments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ReservationService server but before
        it is returned to user code. This `post_search_assignments` interceptor runs
        before the `post_search_assignments_with_metadata` interceptor.
        """
        return response

    def post_search_assignments_with_metadata(
        self,
        response: reservation.SearchAssignmentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        reservation.SearchAssignmentsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for search_assignments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ReservationService server but before it is returned to user code.

        We recommend only using this `post_search_assignments_with_metadata`
        interceptor in new development instead of the `post_search_assignments` interceptor.
        When both interceptors are used, this `post_search_assignments_with_metadata` interceptor runs after the
        `post_search_assignments` interceptor. The (possibly modified) response returned by
        `post_search_assignments` will be passed to
        `post_search_assignments_with_metadata`.
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
        before they are sent to the ReservationService server.
        """
        return request, metadata

    def post_set_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        DEPRECATED. Please use the `post_set_iam_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ReservationService server but before
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
        is returned by the ReservationService server but before it is returned to user code.

        We recommend only using this `post_set_iam_policy_with_metadata`
        interceptor in new development instead of the `post_set_iam_policy` interceptor.
        When both interceptors are used, this `post_set_iam_policy_with_metadata` interceptor runs after the
        `post_set_iam_policy` interceptor. The (possibly modified) response returned by
        `post_set_iam_policy` will be passed to
        `post_set_iam_policy_with_metadata`.
        """
        return response, metadata

    def pre_split_capacity_commitment(
        self,
        request: reservation.SplitCapacityCommitmentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        reservation.SplitCapacityCommitmentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for split_capacity_commitment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ReservationService server.
        """
        return request, metadata

    def post_split_capacity_commitment(
        self, response: reservation.SplitCapacityCommitmentResponse
    ) -> reservation.SplitCapacityCommitmentResponse:
        """Post-rpc interceptor for split_capacity_commitment

        DEPRECATED. Please use the `post_split_capacity_commitment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ReservationService server but before
        it is returned to user code. This `post_split_capacity_commitment` interceptor runs
        before the `post_split_capacity_commitment_with_metadata` interceptor.
        """
        return response

    def post_split_capacity_commitment_with_metadata(
        self,
        response: reservation.SplitCapacityCommitmentResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        reservation.SplitCapacityCommitmentResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for split_capacity_commitment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ReservationService server but before it is returned to user code.

        We recommend only using this `post_split_capacity_commitment_with_metadata`
        interceptor in new development instead of the `post_split_capacity_commitment` interceptor.
        When both interceptors are used, this `post_split_capacity_commitment_with_metadata` interceptor runs after the
        `post_split_capacity_commitment` interceptor. The (possibly modified) response returned by
        `post_split_capacity_commitment` will be passed to
        `post_split_capacity_commitment_with_metadata`.
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
        before they are sent to the ReservationService server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        DEPRECATED. Please use the `post_test_iam_permissions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ReservationService server but before
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
        is returned by the ReservationService server but before it is returned to user code.

        We recommend only using this `post_test_iam_permissions_with_metadata`
        interceptor in new development instead of the `post_test_iam_permissions` interceptor.
        When both interceptors are used, this `post_test_iam_permissions_with_metadata` interceptor runs after the
        `post_test_iam_permissions` interceptor. The (possibly modified) response returned by
        `post_test_iam_permissions` will be passed to
        `post_test_iam_permissions_with_metadata`.
        """
        return response, metadata

    def pre_update_assignment(
        self,
        request: reservation.UpdateAssignmentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        reservation.UpdateAssignmentRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_assignment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ReservationService server.
        """
        return request, metadata

    def post_update_assignment(
        self, response: reservation.Assignment
    ) -> reservation.Assignment:
        """Post-rpc interceptor for update_assignment

        DEPRECATED. Please use the `post_update_assignment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ReservationService server but before
        it is returned to user code. This `post_update_assignment` interceptor runs
        before the `post_update_assignment_with_metadata` interceptor.
        """
        return response

    def post_update_assignment_with_metadata(
        self,
        response: reservation.Assignment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[reservation.Assignment, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_assignment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ReservationService server but before it is returned to user code.

        We recommend only using this `post_update_assignment_with_metadata`
        interceptor in new development instead of the `post_update_assignment` interceptor.
        When both interceptors are used, this `post_update_assignment_with_metadata` interceptor runs after the
        `post_update_assignment` interceptor. The (possibly modified) response returned by
        `post_update_assignment` will be passed to
        `post_update_assignment_with_metadata`.
        """
        return response, metadata

    def pre_update_bi_reservation(
        self,
        request: reservation.UpdateBiReservationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        reservation.UpdateBiReservationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_bi_reservation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ReservationService server.
        """
        return request, metadata

    def post_update_bi_reservation(
        self, response: reservation.BiReservation
    ) -> reservation.BiReservation:
        """Post-rpc interceptor for update_bi_reservation

        DEPRECATED. Please use the `post_update_bi_reservation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ReservationService server but before
        it is returned to user code. This `post_update_bi_reservation` interceptor runs
        before the `post_update_bi_reservation_with_metadata` interceptor.
        """
        return response

    def post_update_bi_reservation_with_metadata(
        self,
        response: reservation.BiReservation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[reservation.BiReservation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_bi_reservation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ReservationService server but before it is returned to user code.

        We recommend only using this `post_update_bi_reservation_with_metadata`
        interceptor in new development instead of the `post_update_bi_reservation` interceptor.
        When both interceptors are used, this `post_update_bi_reservation_with_metadata` interceptor runs after the
        `post_update_bi_reservation` interceptor. The (possibly modified) response returned by
        `post_update_bi_reservation` will be passed to
        `post_update_bi_reservation_with_metadata`.
        """
        return response, metadata

    def pre_update_capacity_commitment(
        self,
        request: reservation.UpdateCapacityCommitmentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        reservation.UpdateCapacityCommitmentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_capacity_commitment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ReservationService server.
        """
        return request, metadata

    def post_update_capacity_commitment(
        self, response: reservation.CapacityCommitment
    ) -> reservation.CapacityCommitment:
        """Post-rpc interceptor for update_capacity_commitment

        DEPRECATED. Please use the `post_update_capacity_commitment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ReservationService server but before
        it is returned to user code. This `post_update_capacity_commitment` interceptor runs
        before the `post_update_capacity_commitment_with_metadata` interceptor.
        """
        return response

    def post_update_capacity_commitment_with_metadata(
        self,
        response: reservation.CapacityCommitment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[reservation.CapacityCommitment, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_capacity_commitment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ReservationService server but before it is returned to user code.

        We recommend only using this `post_update_capacity_commitment_with_metadata`
        interceptor in new development instead of the `post_update_capacity_commitment` interceptor.
        When both interceptors are used, this `post_update_capacity_commitment_with_metadata` interceptor runs after the
        `post_update_capacity_commitment` interceptor. The (possibly modified) response returned by
        `post_update_capacity_commitment` will be passed to
        `post_update_capacity_commitment_with_metadata`.
        """
        return response, metadata

    def pre_update_reservation(
        self,
        request: gcbr_reservation.UpdateReservationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcbr_reservation.UpdateReservationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_reservation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ReservationService server.
        """
        return request, metadata

    def post_update_reservation(
        self, response: gcbr_reservation.Reservation
    ) -> gcbr_reservation.Reservation:
        """Post-rpc interceptor for update_reservation

        DEPRECATED. Please use the `post_update_reservation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ReservationService server but before
        it is returned to user code. This `post_update_reservation` interceptor runs
        before the `post_update_reservation_with_metadata` interceptor.
        """
        return response

    def post_update_reservation_with_metadata(
        self,
        response: gcbr_reservation.Reservation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcbr_reservation.Reservation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_reservation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ReservationService server but before it is returned to user code.

        We recommend only using this `post_update_reservation_with_metadata`
        interceptor in new development instead of the `post_update_reservation` interceptor.
        When both interceptors are used, this `post_update_reservation_with_metadata` interceptor runs after the
        `post_update_reservation` interceptor. The (possibly modified) response returned by
        `post_update_reservation` will be passed to
        `post_update_reservation_with_metadata`.
        """
        return response, metadata

    def pre_update_reservation_group(
        self,
        request: reservation.UpdateReservationGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        reservation.UpdateReservationGroupRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_reservation_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ReservationService server.
        """
        return request, metadata

    def post_update_reservation_group(
        self, response: reservation.ReservationGroup
    ) -> reservation.ReservationGroup:
        """Post-rpc interceptor for update_reservation_group

        DEPRECATED. Please use the `post_update_reservation_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ReservationService server but before
        it is returned to user code. This `post_update_reservation_group` interceptor runs
        before the `post_update_reservation_group_with_metadata` interceptor.
        """
        return response

    def post_update_reservation_group_with_metadata(
        self,
        response: reservation.ReservationGroup,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[reservation.ReservationGroup, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_reservation_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ReservationService server but before it is returned to user code.

        We recommend only using this `post_update_reservation_group_with_metadata`
        interceptor in new development instead of the `post_update_reservation_group` interceptor.
        When both interceptors are used, this `post_update_reservation_group_with_metadata` interceptor runs after the
        `post_update_reservation_group` interceptor. The (possibly modified) response returned by
        `post_update_reservation_group` will be passed to
        `post_update_reservation_group_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class ReservationServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: ReservationServiceRestInterceptor


class ReservationServiceRestTransport(_BaseReservationServiceRestTransport):
    """REST backend synchronous transport for ReservationService.

    This API allows users to manage their BigQuery reservations.

    A reservation provides computational resource guarantees, in the
    form of `slots <https://cloud.google.com/bigquery/docs/slots>`__, to
    users. A slot is a unit of computational power in BigQuery, and
    serves as the basic unit of parallelism. In a scan of a
    multi-partitioned table, a single slot operates on a single
    partition of the table. A reservation resource exists as a child
    resource of the admin project and location, e.g.:
    ``projects/myproject/locations/US/reservations/reservationName``.

    A capacity commitment is a way to purchase compute capacity for
    BigQuery jobs (in the form of slots) with some committed period of
    usage. A capacity commitment resource exists as a child resource of
    the admin project and location, e.g.:
    ``projects/myproject/locations/US/capacityCommitments/id``.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "bigqueryreservation.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[ReservationServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
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
            interceptor (Optional[ReservationServiceRestInterceptor]): Interceptor used
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
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or ReservationServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CreateAssignment(
        _BaseReservationServiceRestTransport._BaseCreateAssignment,
        ReservationServiceRestStub,
    ):
        def __hash__(self):
            return hash("ReservationServiceRestTransport.CreateAssignment")

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
            request: reservation.CreateAssignmentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> reservation.Assignment:
            r"""Call the create assignment method over HTTP.

            Args:
                request (~.reservation.CreateAssignmentRequest):
                    The request object. The request for
                [ReservationService.CreateAssignment][google.cloud.bigquery.reservation.v1.ReservationService.CreateAssignment].
                Note: "bigquery.reservationAssignments.create"
                permission is required on the related assignee.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.reservation.Assignment:
                    An assignment allows a project to
                submit jobs of a certain type using
                slots from the specified reservation.

            """

            http_options = _BaseReservationServiceRestTransport._BaseCreateAssignment._get_http_options()
            request, metadata = self._interceptor.pre_create_assignment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseReservationServiceRestTransport._BaseCreateAssignment,
                    "_BaseCreateAssignment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.reservation_v1.ReservationServiceClient.CreateAssignment",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "CreateAssignment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ReservationServiceRestTransport._CreateAssignment._get_response(
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
            resp = reservation.Assignment()
            pb_resp = reservation.Assignment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_assignment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_assignment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = reservation.Assignment.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.bigquery.reservation_v1.ReservationServiceClient.create_assignment",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "CreateAssignment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateCapacityCommitment(
        _BaseReservationServiceRestTransport._BaseCreateCapacityCommitment,
        ReservationServiceRestStub,
    ):
        def __hash__(self):
            return hash("ReservationServiceRestTransport.CreateCapacityCommitment")

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
            request: reservation.CreateCapacityCommitmentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> reservation.CapacityCommitment:
            r"""Call the create capacity
            commitment method over HTTP.

                Args:
                    request (~.reservation.CreateCapacityCommitmentRequest):
                        The request object. The request for
                    [ReservationService.CreateCapacityCommitment][google.cloud.bigquery.reservation.v1.ReservationService.CreateCapacityCommitment].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.reservation.CapacityCommitment:
                        Capacity commitment is a way to
                    purchase compute capacity for BigQuery
                    jobs (in the form of slots) with some
                    committed period of usage. Annual
                    commitments renew by default.
                    Commitments can be removed after their
                    commitment end time passes.

                    In order to remove annual commitment,
                    its plan needs to be changed to monthly
                    or flex first.

                    A capacity commitment resource exists as
                    a child resource of the admin project.

            """

            http_options = _BaseReservationServiceRestTransport._BaseCreateCapacityCommitment._get_http_options()
            request, metadata = self._interceptor.pre_create_capacity_commitment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseReservationServiceRestTransport._BaseCreateCapacityCommitment,
                    "_BaseCreateCapacityCommitment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.reservation_v1.ReservationServiceClient.CreateCapacityCommitment",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "CreateCapacityCommitment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ReservationServiceRestTransport._CreateCapacityCommitment._get_response(
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
            resp = reservation.CapacityCommitment()
            pb_resp = reservation.CapacityCommitment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_capacity_commitment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_capacity_commitment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = reservation.CapacityCommitment.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.bigquery.reservation_v1.ReservationServiceClient.create_capacity_commitment",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "CreateCapacityCommitment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateReservation(
        _BaseReservationServiceRestTransport._BaseCreateReservation,
        ReservationServiceRestStub,
    ):
        def __hash__(self):
            return hash("ReservationServiceRestTransport.CreateReservation")

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
            request: gcbr_reservation.CreateReservationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcbr_reservation.Reservation:
            r"""Call the create reservation method over HTTP.

            Args:
                request (~.gcbr_reservation.CreateReservationRequest):
                    The request object. The request for
                [ReservationService.CreateReservation][google.cloud.bigquery.reservation.v1.ReservationService.CreateReservation].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcbr_reservation.Reservation:
                    A reservation is a mechanism used to
                guarantee slots to users.

            """

            http_options = _BaseReservationServiceRestTransport._BaseCreateReservation._get_http_options()
            request, metadata = self._interceptor.pre_create_reservation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseReservationServiceRestTransport._BaseCreateReservation,
                    "_BaseCreateReservation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.reservation_v1.ReservationServiceClient.CreateReservation",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "CreateReservation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ReservationServiceRestTransport._CreateReservation._get_response(
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
            resp = gcbr_reservation.Reservation()
            pb_resp = gcbr_reservation.Reservation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_reservation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_reservation_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcbr_reservation.Reservation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.bigquery.reservation_v1.ReservationServiceClient.create_reservation",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "CreateReservation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateReservationGroup(
        _BaseReservationServiceRestTransport._BaseCreateReservationGroup,
        ReservationServiceRestStub,
    ):
        def __hash__(self):
            return hash("ReservationServiceRestTransport.CreateReservationGroup")

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
            request: reservation.CreateReservationGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> reservation.ReservationGroup:
            r"""Call the create reservation group method over HTTP.

            Args:
                request (~.reservation.CreateReservationGroupRequest):
                    The request object. The request for
                [ReservationService.CreateReservationGroup][google.cloud.bigquery.reservation.v1.ReservationService.CreateReservationGroup].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.reservation.ReservationGroup:
                    A reservation group is a container
                for reservations.

            """

            http_options = _BaseReservationServiceRestTransport._BaseCreateReservationGroup._get_http_options()
            request, metadata = self._interceptor.pre_create_reservation_group(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseReservationServiceRestTransport._BaseCreateReservationGroup,
                    "_BaseCreateReservationGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.reservation_v1.ReservationServiceClient.CreateReservationGroup",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "CreateReservationGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ReservationServiceRestTransport._CreateReservationGroup._get_response(
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
            resp = reservation.ReservationGroup()
            pb_resp = reservation.ReservationGroup.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_reservation_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_reservation_group_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = reservation.ReservationGroup.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.bigquery.reservation_v1.ReservationServiceClient.create_reservation_group",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "CreateReservationGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteAssignment(
        _BaseReservationServiceRestTransport._BaseDeleteAssignment,
        ReservationServiceRestStub,
    ):
        def __hash__(self):
            return hash("ReservationServiceRestTransport.DeleteAssignment")

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
            request: reservation.DeleteAssignmentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete assignment method over HTTP.

            Args:
                request (~.reservation.DeleteAssignmentRequest):
                    The request object. The request for
                [ReservationService.DeleteAssignment][google.cloud.bigquery.reservation.v1.ReservationService.DeleteAssignment].
                Note: "bigquery.reservationAssignments.delete"
                permission is required on the related assignee.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseReservationServiceRestTransport._BaseDeleteAssignment._get_http_options()
            request, metadata = self._interceptor.pre_delete_assignment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseReservationServiceRestTransport._BaseDeleteAssignment,
                    "_BaseDeleteAssignment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.reservation_v1.ReservationServiceClient.DeleteAssignment",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "DeleteAssignment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ReservationServiceRestTransport._DeleteAssignment._get_response(
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

    class _DeleteCapacityCommitment(
        _BaseReservationServiceRestTransport._BaseDeleteCapacityCommitment,
        ReservationServiceRestStub,
    ):
        def __hash__(self):
            return hash("ReservationServiceRestTransport.DeleteCapacityCommitment")

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
            request: reservation.DeleteCapacityCommitmentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete capacity
            commitment method over HTTP.

                Args:
                    request (~.reservation.DeleteCapacityCommitmentRequest):
                        The request object. The request for
                    [ReservationService.DeleteCapacityCommitment][google.cloud.bigquery.reservation.v1.ReservationService.DeleteCapacityCommitment].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.
            """

            http_options = _BaseReservationServiceRestTransport._BaseDeleteCapacityCommitment._get_http_options()
            request, metadata = self._interceptor.pre_delete_capacity_commitment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseReservationServiceRestTransport._BaseDeleteCapacityCommitment,
                    "_BaseDeleteCapacityCommitment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.reservation_v1.ReservationServiceClient.DeleteCapacityCommitment",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "DeleteCapacityCommitment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ReservationServiceRestTransport._DeleteCapacityCommitment._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

    class _DeleteReservation(
        _BaseReservationServiceRestTransport._BaseDeleteReservation,
        ReservationServiceRestStub,
    ):
        def __hash__(self):
            return hash("ReservationServiceRestTransport.DeleteReservation")

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
            request: reservation.DeleteReservationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete reservation method over HTTP.

            Args:
                request (~.reservation.DeleteReservationRequest):
                    The request object. The request for
                [ReservationService.DeleteReservation][google.cloud.bigquery.reservation.v1.ReservationService.DeleteReservation].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseReservationServiceRestTransport._BaseDeleteReservation._get_http_options()
            request, metadata = self._interceptor.pre_delete_reservation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseReservationServiceRestTransport._BaseDeleteReservation,
                    "_BaseDeleteReservation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.reservation_v1.ReservationServiceClient.DeleteReservation",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "DeleteReservation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ReservationServiceRestTransport._DeleteReservation._get_response(
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

    class _DeleteReservationGroup(
        _BaseReservationServiceRestTransport._BaseDeleteReservationGroup,
        ReservationServiceRestStub,
    ):
        def __hash__(self):
            return hash("ReservationServiceRestTransport.DeleteReservationGroup")

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
            request: reservation.DeleteReservationGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete reservation group method over HTTP.

            Args:
                request (~.reservation.DeleteReservationGroupRequest):
                    The request object. The request for
                [ReservationService.DeleteReservationGroup][google.cloud.bigquery.reservation.v1.ReservationService.DeleteReservationGroup].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseReservationServiceRestTransport._BaseDeleteReservationGroup._get_http_options()
            request, metadata = self._interceptor.pre_delete_reservation_group(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseReservationServiceRestTransport._BaseDeleteReservationGroup,
                    "_BaseDeleteReservationGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.reservation_v1.ReservationServiceClient.DeleteReservationGroup",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "DeleteReservationGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ReservationServiceRestTransport._DeleteReservationGroup._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

    class _FailoverReservation(
        _BaseReservationServiceRestTransport._BaseFailoverReservation,
        ReservationServiceRestStub,
    ):
        def __hash__(self):
            return hash("ReservationServiceRestTransport.FailoverReservation")

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
            request: reservation.FailoverReservationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> reservation.Reservation:
            r"""Call the failover reservation method over HTTP.

            Args:
                request (~.reservation.FailoverReservationRequest):
                    The request object. The request for
                ReservationService.FailoverReservation.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.reservation.Reservation:
                    A reservation is a mechanism used to
                guarantee slots to users.

            """

            http_options = _BaseReservationServiceRestTransport._BaseFailoverReservation._get_http_options()
            request, metadata = self._interceptor.pre_failover_reservation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseReservationServiceRestTransport._BaseFailoverReservation,
                    "_BaseFailoverReservation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.reservation_v1.ReservationServiceClient.FailoverReservation",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "FailoverReservation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ReservationServiceRestTransport._FailoverReservation._get_response(
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
            resp = reservation.Reservation()
            pb_resp = reservation.Reservation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_failover_reservation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_failover_reservation_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = reservation.Reservation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.bigquery.reservation_v1.ReservationServiceClient.failover_reservation",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "FailoverReservation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetBiReservation(
        _BaseReservationServiceRestTransport._BaseGetBiReservation,
        ReservationServiceRestStub,
    ):
        def __hash__(self):
            return hash("ReservationServiceRestTransport.GetBiReservation")

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
            request: reservation.GetBiReservationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> reservation.BiReservation:
            r"""Call the get bi reservation method over HTTP.

            Args:
                request (~.reservation.GetBiReservationRequest):
                    The request object. A request to get a singleton BI
                reservation.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.reservation.BiReservation:
                    Represents a BI Reservation.
            """

            http_options = _BaseReservationServiceRestTransport._BaseGetBiReservation._get_http_options()
            request, metadata = self._interceptor.pre_get_bi_reservation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseReservationServiceRestTransport._BaseGetBiReservation,
                    "_BaseGetBiReservation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.reservation_v1.ReservationServiceClient.GetBiReservation",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "GetBiReservation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ReservationServiceRestTransport._GetBiReservation._get_response(
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
            resp = reservation.BiReservation()
            pb_resp = reservation.BiReservation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_bi_reservation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_bi_reservation_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = reservation.BiReservation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.bigquery.reservation_v1.ReservationServiceClient.get_bi_reservation",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "GetBiReservation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetCapacityCommitment(
        _BaseReservationServiceRestTransport._BaseGetCapacityCommitment,
        ReservationServiceRestStub,
    ):
        def __hash__(self):
            return hash("ReservationServiceRestTransport.GetCapacityCommitment")

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
            request: reservation.GetCapacityCommitmentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> reservation.CapacityCommitment:
            r"""Call the get capacity commitment method over HTTP.

            Args:
                request (~.reservation.GetCapacityCommitmentRequest):
                    The request object. The request for
                [ReservationService.GetCapacityCommitment][google.cloud.bigquery.reservation.v1.ReservationService.GetCapacityCommitment].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.reservation.CapacityCommitment:
                    Capacity commitment is a way to
                purchase compute capacity for BigQuery
                jobs (in the form of slots) with some
                committed period of usage. Annual
                commitments renew by default.
                Commitments can be removed after their
                commitment end time passes.

                In order to remove annual commitment,
                its plan needs to be changed to monthly
                or flex first.

                A capacity commitment resource exists as
                a child resource of the admin project.

            """

            http_options = _BaseReservationServiceRestTransport._BaseGetCapacityCommitment._get_http_options()
            request, metadata = self._interceptor.pre_get_capacity_commitment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseReservationServiceRestTransport._BaseGetCapacityCommitment,
                    "_BaseGetCapacityCommitment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.reservation_v1.ReservationServiceClient.GetCapacityCommitment",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "GetCapacityCommitment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ReservationServiceRestTransport._GetCapacityCommitment._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = reservation.CapacityCommitment()
            pb_resp = reservation.CapacityCommitment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_capacity_commitment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_capacity_commitment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = reservation.CapacityCommitment.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.bigquery.reservation_v1.ReservationServiceClient.get_capacity_commitment",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "GetCapacityCommitment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetIamPolicy(
        _BaseReservationServiceRestTransport._BaseGetIamPolicy,
        ReservationServiceRestStub,
    ):
        def __hash__(self):
            return hash("ReservationServiceRestTransport.GetIamPolicy")

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

            http_options = _BaseReservationServiceRestTransport._BaseGetIamPolicy._get_http_options()
            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseReservationServiceRestTransport._BaseGetIamPolicy,
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
                    f"Sending request for google.cloud.bigquery.reservation_v1.ReservationServiceClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "GetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ReservationServiceRestTransport._GetIamPolicy._get_response(
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
                    "Received response for google.cloud.bigquery.reservation_v1.ReservationServiceClient.get_iam_policy",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "GetIamPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetReservation(
        _BaseReservationServiceRestTransport._BaseGetReservation,
        ReservationServiceRestStub,
    ):
        def __hash__(self):
            return hash("ReservationServiceRestTransport.GetReservation")

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
            request: reservation.GetReservationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> reservation.Reservation:
            r"""Call the get reservation method over HTTP.

            Args:
                request (~.reservation.GetReservationRequest):
                    The request object. The request for
                [ReservationService.GetReservation][google.cloud.bigquery.reservation.v1.ReservationService.GetReservation].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.reservation.Reservation:
                    A reservation is a mechanism used to
                guarantee slots to users.

            """

            http_options = _BaseReservationServiceRestTransport._BaseGetReservation._get_http_options()
            request, metadata = self._interceptor.pre_get_reservation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseReservationServiceRestTransport._BaseGetReservation,
                    "_BaseGetReservation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.reservation_v1.ReservationServiceClient.GetReservation",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "GetReservation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ReservationServiceRestTransport._GetReservation._get_response(
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
            resp = reservation.Reservation()
            pb_resp = reservation.Reservation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_reservation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_reservation_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = reservation.Reservation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.bigquery.reservation_v1.ReservationServiceClient.get_reservation",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "GetReservation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetReservationGroup(
        _BaseReservationServiceRestTransport._BaseGetReservationGroup,
        ReservationServiceRestStub,
    ):
        def __hash__(self):
            return hash("ReservationServiceRestTransport.GetReservationGroup")

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
            request: reservation.GetReservationGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> reservation.ReservationGroup:
            r"""Call the get reservation group method over HTTP.

            Args:
                request (~.reservation.GetReservationGroupRequest):
                    The request object. The request for
                [ReservationService.GetReservationGroup][google.cloud.bigquery.reservation.v1.ReservationService.GetReservationGroup].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.reservation.ReservationGroup:
                    A reservation group is a container
                for reservations.

            """

            http_options = _BaseReservationServiceRestTransport._BaseGetReservationGroup._get_http_options()
            request, metadata = self._interceptor.pre_get_reservation_group(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseReservationServiceRestTransport._BaseGetReservationGroup,
                    "_BaseGetReservationGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.reservation_v1.ReservationServiceClient.GetReservationGroup",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "GetReservationGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ReservationServiceRestTransport._GetReservationGroup._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = reservation.ReservationGroup()
            pb_resp = reservation.ReservationGroup.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_reservation_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_reservation_group_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = reservation.ReservationGroup.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.bigquery.reservation_v1.ReservationServiceClient.get_reservation_group",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "GetReservationGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAssignments(
        _BaseReservationServiceRestTransport._BaseListAssignments,
        ReservationServiceRestStub,
    ):
        def __hash__(self):
            return hash("ReservationServiceRestTransport.ListAssignments")

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
            request: reservation.ListAssignmentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> reservation.ListAssignmentsResponse:
            r"""Call the list assignments method over HTTP.

            Args:
                request (~.reservation.ListAssignmentsRequest):
                    The request object. The request for
                [ReservationService.ListAssignments][google.cloud.bigquery.reservation.v1.ReservationService.ListAssignments].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.reservation.ListAssignmentsResponse:
                    The response for
                [ReservationService.ListAssignments][google.cloud.bigquery.reservation.v1.ReservationService.ListAssignments].

            """

            http_options = _BaseReservationServiceRestTransport._BaseListAssignments._get_http_options()
            request, metadata = self._interceptor.pre_list_assignments(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseReservationServiceRestTransport._BaseListAssignments,
                    "_BaseListAssignments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.reservation_v1.ReservationServiceClient.ListAssignments",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "ListAssignments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ReservationServiceRestTransport._ListAssignments._get_response(
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
            resp = reservation.ListAssignmentsResponse()
            pb_resp = reservation.ListAssignmentsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_assignments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_assignments_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = reservation.ListAssignmentsResponse.to_json(
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
                    "Received response for google.cloud.bigquery.reservation_v1.ReservationServiceClient.list_assignments",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "ListAssignments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListCapacityCommitments(
        _BaseReservationServiceRestTransport._BaseListCapacityCommitments,
        ReservationServiceRestStub,
    ):
        def __hash__(self):
            return hash("ReservationServiceRestTransport.ListCapacityCommitments")

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
            request: reservation.ListCapacityCommitmentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> reservation.ListCapacityCommitmentsResponse:
            r"""Call the list capacity commitments method over HTTP.

            Args:
                request (~.reservation.ListCapacityCommitmentsRequest):
                    The request object. The request for
                [ReservationService.ListCapacityCommitments][google.cloud.bigquery.reservation.v1.ReservationService.ListCapacityCommitments].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.reservation.ListCapacityCommitmentsResponse:
                    The response for
                [ReservationService.ListCapacityCommitments][google.cloud.bigquery.reservation.v1.ReservationService.ListCapacityCommitments].

            """

            http_options = _BaseReservationServiceRestTransport._BaseListCapacityCommitments._get_http_options()
            request, metadata = self._interceptor.pre_list_capacity_commitments(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseReservationServiceRestTransport._BaseListCapacityCommitments,
                    "_BaseListCapacityCommitments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.reservation_v1.ReservationServiceClient.ListCapacityCommitments",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "ListCapacityCommitments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ReservationServiceRestTransport._ListCapacityCommitments._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = reservation.ListCapacityCommitmentsResponse()
            pb_resp = reservation.ListCapacityCommitmentsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_capacity_commitments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_capacity_commitments_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        reservation.ListCapacityCommitmentsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.bigquery.reservation_v1.ReservationServiceClient.list_capacity_commitments",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "ListCapacityCommitments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListReservationGroups(
        _BaseReservationServiceRestTransport._BaseListReservationGroups,
        ReservationServiceRestStub,
    ):
        def __hash__(self):
            return hash("ReservationServiceRestTransport.ListReservationGroups")

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
            request: reservation.ListReservationGroupsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> reservation.ListReservationGroupsResponse:
            r"""Call the list reservation groups method over HTTP.

            Args:
                request (~.reservation.ListReservationGroupsRequest):
                    The request object. The request for
                [ReservationService.ListReservationGroups][google.cloud.bigquery.reservation.v1.ReservationService.ListReservationGroups].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.reservation.ListReservationGroupsResponse:
                    The response for
                [ReservationService.ListReservationGroups][google.cloud.bigquery.reservation.v1.ReservationService.ListReservationGroups].

            """

            http_options = _BaseReservationServiceRestTransport._BaseListReservationGroups._get_http_options()
            request, metadata = self._interceptor.pre_list_reservation_groups(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseReservationServiceRestTransport._BaseListReservationGroups,
                    "_BaseListReservationGroups__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.reservation_v1.ReservationServiceClient.ListReservationGroups",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "ListReservationGroups",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ReservationServiceRestTransport._ListReservationGroups._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = reservation.ListReservationGroupsResponse()
            pb_resp = reservation.ListReservationGroupsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_reservation_groups(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_reservation_groups_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        reservation.ListReservationGroupsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.bigquery.reservation_v1.ReservationServiceClient.list_reservation_groups",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "ListReservationGroups",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListReservations(
        _BaseReservationServiceRestTransport._BaseListReservations,
        ReservationServiceRestStub,
    ):
        def __hash__(self):
            return hash("ReservationServiceRestTransport.ListReservations")

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
            request: reservation.ListReservationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> reservation.ListReservationsResponse:
            r"""Call the list reservations method over HTTP.

            Args:
                request (~.reservation.ListReservationsRequest):
                    The request object. The request for
                [ReservationService.ListReservations][google.cloud.bigquery.reservation.v1.ReservationService.ListReservations].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.reservation.ListReservationsResponse:
                    The response for
                [ReservationService.ListReservations][google.cloud.bigquery.reservation.v1.ReservationService.ListReservations].

            """

            http_options = _BaseReservationServiceRestTransport._BaseListReservations._get_http_options()
            request, metadata = self._interceptor.pre_list_reservations(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseReservationServiceRestTransport._BaseListReservations,
                    "_BaseListReservations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.reservation_v1.ReservationServiceClient.ListReservations",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "ListReservations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ReservationServiceRestTransport._ListReservations._get_response(
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
            resp = reservation.ListReservationsResponse()
            pb_resp = reservation.ListReservationsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_reservations(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_reservations_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = reservation.ListReservationsResponse.to_json(
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
                    "Received response for google.cloud.bigquery.reservation_v1.ReservationServiceClient.list_reservations",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "ListReservations",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _MergeCapacityCommitments(
        _BaseReservationServiceRestTransport._BaseMergeCapacityCommitments,
        ReservationServiceRestStub,
    ):
        def __hash__(self):
            return hash("ReservationServiceRestTransport.MergeCapacityCommitments")

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
            request: reservation.MergeCapacityCommitmentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> reservation.CapacityCommitment:
            r"""Call the merge capacity
            commitments method over HTTP.

                Args:
                    request (~.reservation.MergeCapacityCommitmentsRequest):
                        The request object. The request for
                    [ReservationService.MergeCapacityCommitments][google.cloud.bigquery.reservation.v1.ReservationService.MergeCapacityCommitments].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.reservation.CapacityCommitment:
                        Capacity commitment is a way to
                    purchase compute capacity for BigQuery
                    jobs (in the form of slots) with some
                    committed period of usage. Annual
                    commitments renew by default.
                    Commitments can be removed after their
                    commitment end time passes.

                    In order to remove annual commitment,
                    its plan needs to be changed to monthly
                    or flex first.

                    A capacity commitment resource exists as
                    a child resource of the admin project.

            """

            http_options = _BaseReservationServiceRestTransport._BaseMergeCapacityCommitments._get_http_options()
            request, metadata = self._interceptor.pre_merge_capacity_commitments(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseReservationServiceRestTransport._BaseMergeCapacityCommitments,
                    "_BaseMergeCapacityCommitments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.reservation_v1.ReservationServiceClient.MergeCapacityCommitments",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "MergeCapacityCommitments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ReservationServiceRestTransport._MergeCapacityCommitments._get_response(
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
            resp = reservation.CapacityCommitment()
            pb_resp = reservation.CapacityCommitment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_merge_capacity_commitments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_merge_capacity_commitments_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = reservation.CapacityCommitment.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.bigquery.reservation_v1.ReservationServiceClient.merge_capacity_commitments",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "MergeCapacityCommitments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _MoveAssignment(
        _BaseReservationServiceRestTransport._BaseMoveAssignment,
        ReservationServiceRestStub,
    ):
        def __hash__(self):
            return hash("ReservationServiceRestTransport.MoveAssignment")

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
            request: reservation.MoveAssignmentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> reservation.Assignment:
            r"""Call the move assignment method over HTTP.

            Args:
                request (~.reservation.MoveAssignmentRequest):
                    The request object. The request for
                [ReservationService.MoveAssignment][google.cloud.bigquery.reservation.v1.ReservationService.MoveAssignment].

                **Note**: "bigquery.reservationAssignments.create"
                permission is required on the destination_id.

                **Note**: "bigquery.reservationAssignments.create" and
                "bigquery.reservationAssignments.delete" permission are
                required on the related assignee.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.reservation.Assignment:
                    An assignment allows a project to
                submit jobs of a certain type using
                slots from the specified reservation.

            """

            http_options = _BaseReservationServiceRestTransport._BaseMoveAssignment._get_http_options()
            request, metadata = self._interceptor.pre_move_assignment(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseReservationServiceRestTransport._BaseMoveAssignment,
                    "_BaseMoveAssignment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.reservation_v1.ReservationServiceClient.MoveAssignment",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "MoveAssignment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ReservationServiceRestTransport._MoveAssignment._get_response(
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
            resp = reservation.Assignment()
            pb_resp = reservation.Assignment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_move_assignment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_move_assignment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = reservation.Assignment.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.bigquery.reservation_v1.ReservationServiceClient.move_assignment",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "MoveAssignment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SearchAllAssignments(
        _BaseReservationServiceRestTransport._BaseSearchAllAssignments,
        ReservationServiceRestStub,
    ):
        def __hash__(self):
            return hash("ReservationServiceRestTransport.SearchAllAssignments")

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
            request: reservation.SearchAllAssignmentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> reservation.SearchAllAssignmentsResponse:
            r"""Call the search all assignments method over HTTP.

            Args:
                request (~.reservation.SearchAllAssignmentsRequest):
                    The request object. The request for
                [ReservationService.SearchAllAssignments][google.cloud.bigquery.reservation.v1.ReservationService.SearchAllAssignments].
                Note: "bigquery.reservationAssignments.search"
                permission is required on the related assignee.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.reservation.SearchAllAssignmentsResponse:
                    The response for
                [ReservationService.SearchAllAssignments][google.cloud.bigquery.reservation.v1.ReservationService.SearchAllAssignments].

            """

            http_options = _BaseReservationServiceRestTransport._BaseSearchAllAssignments._get_http_options()
            request, metadata = self._interceptor.pre_search_all_assignments(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseReservationServiceRestTransport._BaseSearchAllAssignments,
                    "_BaseSearchAllAssignments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.reservation_v1.ReservationServiceClient.SearchAllAssignments",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "SearchAllAssignments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ReservationServiceRestTransport._SearchAllAssignments._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = reservation.SearchAllAssignmentsResponse()
            pb_resp = reservation.SearchAllAssignmentsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_search_all_assignments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_search_all_assignments_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = reservation.SearchAllAssignmentsResponse.to_json(
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
                    "Received response for google.cloud.bigquery.reservation_v1.ReservationServiceClient.search_all_assignments",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "SearchAllAssignments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SearchAssignments(
        _BaseReservationServiceRestTransport._BaseSearchAssignments,
        ReservationServiceRestStub,
    ):
        def __hash__(self):
            return hash("ReservationServiceRestTransport.SearchAssignments")

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
            request: reservation.SearchAssignmentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> reservation.SearchAssignmentsResponse:
            r"""Call the search assignments method over HTTP.

            Args:
                request (~.reservation.SearchAssignmentsRequest):
                    The request object. The request for
                [ReservationService.SearchAssignments][google.cloud.bigquery.reservation.v1.ReservationService.SearchAssignments].
                Note: "bigquery.reservationAssignments.search"
                permission is required on the related assignee.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.reservation.SearchAssignmentsResponse:
                    The response for
                [ReservationService.SearchAssignments][google.cloud.bigquery.reservation.v1.ReservationService.SearchAssignments].

            """

            http_options = _BaseReservationServiceRestTransport._BaseSearchAssignments._get_http_options()
            request, metadata = self._interceptor.pre_search_assignments(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseReservationServiceRestTransport._BaseSearchAssignments,
                    "_BaseSearchAssignments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.reservation_v1.ReservationServiceClient.SearchAssignments",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "SearchAssignments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ReservationServiceRestTransport._SearchAssignments._get_response(
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
            resp = reservation.SearchAssignmentsResponse()
            pb_resp = reservation.SearchAssignmentsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_search_assignments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_search_assignments_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = reservation.SearchAssignmentsResponse.to_json(
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
                    "Received response for google.cloud.bigquery.reservation_v1.ReservationServiceClient.search_assignments",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "SearchAssignments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetIamPolicy(
        _BaseReservationServiceRestTransport._BaseSetIamPolicy,
        ReservationServiceRestStub,
    ):
        def __hash__(self):
            return hash("ReservationServiceRestTransport.SetIamPolicy")

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

            http_options = _BaseReservationServiceRestTransport._BaseSetIamPolicy._get_http_options()
            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseReservationServiceRestTransport._BaseSetIamPolicy,
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
                    f"Sending request for google.cloud.bigquery.reservation_v1.ReservationServiceClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "SetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ReservationServiceRestTransport._SetIamPolicy._get_response(
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
                    "Received response for google.cloud.bigquery.reservation_v1.ReservationServiceClient.set_iam_policy",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "SetIamPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SplitCapacityCommitment(
        _BaseReservationServiceRestTransport._BaseSplitCapacityCommitment,
        ReservationServiceRestStub,
    ):
        def __hash__(self):
            return hash("ReservationServiceRestTransport.SplitCapacityCommitment")

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
            request: reservation.SplitCapacityCommitmentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> reservation.SplitCapacityCommitmentResponse:
            r"""Call the split capacity commitment method over HTTP.

            Args:
                request (~.reservation.SplitCapacityCommitmentRequest):
                    The request object. The request for
                [ReservationService.SplitCapacityCommitment][google.cloud.bigquery.reservation.v1.ReservationService.SplitCapacityCommitment].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.reservation.SplitCapacityCommitmentResponse:
                    The response for
                [ReservationService.SplitCapacityCommitment][google.cloud.bigquery.reservation.v1.ReservationService.SplitCapacityCommitment].

            """

            http_options = _BaseReservationServiceRestTransport._BaseSplitCapacityCommitment._get_http_options()
            request, metadata = self._interceptor.pre_split_capacity_commitment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseReservationServiceRestTransport._BaseSplitCapacityCommitment,
                    "_BaseSplitCapacityCommitment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.reservation_v1.ReservationServiceClient.SplitCapacityCommitment",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "SplitCapacityCommitment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ReservationServiceRestTransport._SplitCapacityCommitment._get_response(
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
            resp = reservation.SplitCapacityCommitmentResponse()
            pb_resp = reservation.SplitCapacityCommitmentResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_split_capacity_commitment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_split_capacity_commitment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        reservation.SplitCapacityCommitmentResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.bigquery.reservation_v1.ReservationServiceClient.split_capacity_commitment",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "SplitCapacityCommitment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _TestIamPermissions(
        _BaseReservationServiceRestTransport._BaseTestIamPermissions,
        ReservationServiceRestStub,
    ):
        def __hash__(self):
            return hash("ReservationServiceRestTransport.TestIamPermissions")

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

            http_options = _BaseReservationServiceRestTransport._BaseTestIamPermissions._get_http_options()
            request, metadata = self._interceptor.pre_test_iam_permissions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseReservationServiceRestTransport._BaseTestIamPermissions,
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
                    f"Sending request for google.cloud.bigquery.reservation_v1.ReservationServiceClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "TestIamPermissions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ReservationServiceRestTransport._TestIamPermissions._get_response(
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
                    "Received response for google.cloud.bigquery.reservation_v1.ReservationServiceClient.test_iam_permissions",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "TestIamPermissions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateAssignment(
        _BaseReservationServiceRestTransport._BaseUpdateAssignment,
        ReservationServiceRestStub,
    ):
        def __hash__(self):
            return hash("ReservationServiceRestTransport.UpdateAssignment")

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
            request: reservation.UpdateAssignmentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> reservation.Assignment:
            r"""Call the update assignment method over HTTP.

            Args:
                request (~.reservation.UpdateAssignmentRequest):
                    The request object. The request for
                [ReservationService.UpdateAssignment][google.cloud.bigquery.reservation.v1.ReservationService.UpdateAssignment].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.reservation.Assignment:
                    An assignment allows a project to
                submit jobs of a certain type using
                slots from the specified reservation.

            """

            http_options = _BaseReservationServiceRestTransport._BaseUpdateAssignment._get_http_options()
            request, metadata = self._interceptor.pre_update_assignment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseReservationServiceRestTransport._BaseUpdateAssignment,
                    "_BaseUpdateAssignment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.reservation_v1.ReservationServiceClient.UpdateAssignment",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "UpdateAssignment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ReservationServiceRestTransport._UpdateAssignment._get_response(
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
            resp = reservation.Assignment()
            pb_resp = reservation.Assignment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_assignment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_assignment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = reservation.Assignment.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.bigquery.reservation_v1.ReservationServiceClient.update_assignment",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "UpdateAssignment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateBiReservation(
        _BaseReservationServiceRestTransport._BaseUpdateBiReservation,
        ReservationServiceRestStub,
    ):
        def __hash__(self):
            return hash("ReservationServiceRestTransport.UpdateBiReservation")

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
            request: reservation.UpdateBiReservationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> reservation.BiReservation:
            r"""Call the update bi reservation method over HTTP.

            Args:
                request (~.reservation.UpdateBiReservationRequest):
                    The request object. A request to update a BI reservation.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.reservation.BiReservation:
                    Represents a BI Reservation.
            """

            http_options = _BaseReservationServiceRestTransport._BaseUpdateBiReservation._get_http_options()
            request, metadata = self._interceptor.pre_update_bi_reservation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseReservationServiceRestTransport._BaseUpdateBiReservation,
                    "_BaseUpdateBiReservation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.reservation_v1.ReservationServiceClient.UpdateBiReservation",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "UpdateBiReservation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ReservationServiceRestTransport._UpdateBiReservation._get_response(
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
            resp = reservation.BiReservation()
            pb_resp = reservation.BiReservation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_bi_reservation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_bi_reservation_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = reservation.BiReservation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.bigquery.reservation_v1.ReservationServiceClient.update_bi_reservation",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "UpdateBiReservation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateCapacityCommitment(
        _BaseReservationServiceRestTransport._BaseUpdateCapacityCommitment,
        ReservationServiceRestStub,
    ):
        def __hash__(self):
            return hash("ReservationServiceRestTransport.UpdateCapacityCommitment")

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
            request: reservation.UpdateCapacityCommitmentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> reservation.CapacityCommitment:
            r"""Call the update capacity
            commitment method over HTTP.

                Args:
                    request (~.reservation.UpdateCapacityCommitmentRequest):
                        The request object. The request for
                    [ReservationService.UpdateCapacityCommitment][google.cloud.bigquery.reservation.v1.ReservationService.UpdateCapacityCommitment].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.reservation.CapacityCommitment:
                        Capacity commitment is a way to
                    purchase compute capacity for BigQuery
                    jobs (in the form of slots) with some
                    committed period of usage. Annual
                    commitments renew by default.
                    Commitments can be removed after their
                    commitment end time passes.

                    In order to remove annual commitment,
                    its plan needs to be changed to monthly
                    or flex first.

                    A capacity commitment resource exists as
                    a child resource of the admin project.

            """

            http_options = _BaseReservationServiceRestTransport._BaseUpdateCapacityCommitment._get_http_options()
            request, metadata = self._interceptor.pre_update_capacity_commitment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseReservationServiceRestTransport._BaseUpdateCapacityCommitment,
                    "_BaseUpdateCapacityCommitment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.reservation_v1.ReservationServiceClient.UpdateCapacityCommitment",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "UpdateCapacityCommitment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ReservationServiceRestTransport._UpdateCapacityCommitment._get_response(
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
            resp = reservation.CapacityCommitment()
            pb_resp = reservation.CapacityCommitment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_capacity_commitment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_capacity_commitment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = reservation.CapacityCommitment.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.bigquery.reservation_v1.ReservationServiceClient.update_capacity_commitment",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "UpdateCapacityCommitment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateReservation(
        _BaseReservationServiceRestTransport._BaseUpdateReservation,
        ReservationServiceRestStub,
    ):
        def __hash__(self):
            return hash("ReservationServiceRestTransport.UpdateReservation")

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
            request: gcbr_reservation.UpdateReservationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcbr_reservation.Reservation:
            r"""Call the update reservation method over HTTP.

            Args:
                request (~.gcbr_reservation.UpdateReservationRequest):
                    The request object. The request for
                [ReservationService.UpdateReservation][google.cloud.bigquery.reservation.v1.ReservationService.UpdateReservation].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcbr_reservation.Reservation:
                    A reservation is a mechanism used to
                guarantee slots to users.

            """

            http_options = _BaseReservationServiceRestTransport._BaseUpdateReservation._get_http_options()
            request, metadata = self._interceptor.pre_update_reservation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseReservationServiceRestTransport._BaseUpdateReservation,
                    "_BaseUpdateReservation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.reservation_v1.ReservationServiceClient.UpdateReservation",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "UpdateReservation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ReservationServiceRestTransport._UpdateReservation._get_response(
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
            resp = gcbr_reservation.Reservation()
            pb_resp = gcbr_reservation.Reservation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_reservation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_reservation_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcbr_reservation.Reservation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.bigquery.reservation_v1.ReservationServiceClient.update_reservation",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "UpdateReservation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateReservationGroup(
        _BaseReservationServiceRestTransport._BaseUpdateReservationGroup,
        ReservationServiceRestStub,
    ):
        def __hash__(self):
            return hash("ReservationServiceRestTransport.UpdateReservationGroup")

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
            request: reservation.UpdateReservationGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> reservation.ReservationGroup:
            r"""Call the update reservation group method over HTTP.

            Args:
                request (~.reservation.UpdateReservationGroupRequest):
                    The request object. The request for
                [ReservationService.UpdateReservationGroup][google.cloud.bigquery.reservation.v1.ReservationService.UpdateReservationGroup].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.reservation.ReservationGroup:
                    A reservation group is a container
                for reservations.

            """

            http_options = _BaseReservationServiceRestTransport._BaseUpdateReservationGroup._get_http_options()
            request, metadata = self._interceptor.pre_update_reservation_group(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseReservationServiceRestTransport._BaseUpdateReservationGroup,
                    "_BaseUpdateReservationGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.bigquery.reservation_v1.ReservationServiceClient.UpdateReservationGroup",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "UpdateReservationGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ReservationServiceRestTransport._UpdateReservationGroup._get_response(
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
            resp = reservation.ReservationGroup()
            pb_resp = reservation.ReservationGroup.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_reservation_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_reservation_group_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = reservation.ReservationGroup.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.bigquery.reservation_v1.ReservationServiceClient.update_reservation_group",
                    extra={
                        "serviceName": "google.cloud.bigquery.reservation.v1.ReservationService",
                        "rpcName": "UpdateReservationGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_assignment(
        self,
    ) -> Callable[[reservation.CreateAssignmentRequest], reservation.Assignment]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateAssignment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_capacity_commitment(
        self,
    ) -> Callable[
        [reservation.CreateCapacityCommitmentRequest], reservation.CapacityCommitment
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateCapacityCommitment(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_reservation(
        self,
    ) -> Callable[
        [gcbr_reservation.CreateReservationRequest], gcbr_reservation.Reservation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateReservation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_reservation_group(
        self,
    ) -> Callable[
        [reservation.CreateReservationGroupRequest], reservation.ReservationGroup
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateReservationGroup(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_assignment(
        self,
    ) -> Callable[[reservation.DeleteAssignmentRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteAssignment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_capacity_commitment(
        self,
    ) -> Callable[[reservation.DeleteCapacityCommitmentRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteCapacityCommitment(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_reservation(
        self,
    ) -> Callable[[reservation.DeleteReservationRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteReservation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_reservation_group(
        self,
    ) -> Callable[[reservation.DeleteReservationGroupRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteReservationGroup(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def failover_reservation(
        self,
    ) -> Callable[[reservation.FailoverReservationRequest], reservation.Reservation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FailoverReservation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_bi_reservation(
        self,
    ) -> Callable[[reservation.GetBiReservationRequest], reservation.BiReservation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetBiReservation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_capacity_commitment(
        self,
    ) -> Callable[
        [reservation.GetCapacityCommitmentRequest], reservation.CapacityCommitment
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetCapacityCommitment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_iam_policy(
        self,
    ) -> Callable[[iam_policy_pb2.GetIamPolicyRequest], policy_pb2.Policy]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_reservation(
        self,
    ) -> Callable[[reservation.GetReservationRequest], reservation.Reservation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetReservation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_reservation_group(
        self,
    ) -> Callable[
        [reservation.GetReservationGroupRequest], reservation.ReservationGroup
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetReservationGroup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_assignments(
        self,
    ) -> Callable[
        [reservation.ListAssignmentsRequest], reservation.ListAssignmentsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAssignments(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_capacity_commitments(
        self,
    ) -> Callable[
        [reservation.ListCapacityCommitmentsRequest],
        reservation.ListCapacityCommitmentsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListCapacityCommitments(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_reservation_groups(
        self,
    ) -> Callable[
        [reservation.ListReservationGroupsRequest],
        reservation.ListReservationGroupsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListReservationGroups(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_reservations(
        self,
    ) -> Callable[
        [reservation.ListReservationsRequest], reservation.ListReservationsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListReservations(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def merge_capacity_commitments(
        self,
    ) -> Callable[
        [reservation.MergeCapacityCommitmentsRequest], reservation.CapacityCommitment
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._MergeCapacityCommitments(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def move_assignment(
        self,
    ) -> Callable[[reservation.MoveAssignmentRequest], reservation.Assignment]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._MoveAssignment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def search_all_assignments(
        self,
    ) -> Callable[
        [reservation.SearchAllAssignmentsRequest],
        reservation.SearchAllAssignmentsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SearchAllAssignments(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def search_assignments(
        self,
    ) -> Callable[
        [reservation.SearchAssignmentsRequest], reservation.SearchAssignmentsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SearchAssignments(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def set_iam_policy(
        self,
    ) -> Callable[[iam_policy_pb2.SetIamPolicyRequest], policy_pb2.Policy]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def split_capacity_commitment(
        self,
    ) -> Callable[
        [reservation.SplitCapacityCommitmentRequest],
        reservation.SplitCapacityCommitmentResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SplitCapacityCommitment(
            self._session, self._host, self._interceptor
        )  # type: ignore

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
    def update_assignment(
        self,
    ) -> Callable[[reservation.UpdateAssignmentRequest], reservation.Assignment]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateAssignment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_bi_reservation(
        self,
    ) -> Callable[[reservation.UpdateBiReservationRequest], reservation.BiReservation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateBiReservation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_capacity_commitment(
        self,
    ) -> Callable[
        [reservation.UpdateCapacityCommitmentRequest], reservation.CapacityCommitment
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateCapacityCommitment(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_reservation(
        self,
    ) -> Callable[
        [gcbr_reservation.UpdateReservationRequest], gcbr_reservation.Reservation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateReservation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_reservation_group(
        self,
    ) -> Callable[
        [reservation.UpdateReservationGroupRequest], reservation.ReservationGroup
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateReservationGroup(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("ReservationServiceRestTransport",)
