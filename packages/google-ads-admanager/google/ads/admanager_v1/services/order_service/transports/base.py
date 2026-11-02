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
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.ads.admanager_v1 import gapic_version as package_version
from google.ads.admanager_v1.types import order_messages, order_service

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class OrderServiceTransport(abc.ABC):
    """Abstract transport class for OrderService."""

    AUTH_SCOPES = (
        "https://www.googleapis.com/auth/admanager",
        "https://www.googleapis.com/auth/admanager.readonly",
    )

    DEFAULT_HOST: str = "admanager.googleapis.com"

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
                 The hostname to connect to (default: 'admanager.googleapis.com').
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
            self.get_order: gapic_v1.method.wrap_method(
                self.get_order,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_orders: gapic_v1.method.wrap_method(
                self.list_orders,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_create_orders: gapic_v1.method.wrap_method(
                self.batch_create_orders,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_update_orders: gapic_v1.method.wrap_method(
                self.batch_update_orders,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_approve_orders: gapic_v1.method.wrap_method(
                self.batch_approve_orders,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_approve_and_overbook_orders: gapic_v1.method.wrap_method(
                self.batch_approve_and_overbook_orders,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_submit_orders_for_approval: gapic_v1.method.wrap_method(
                self.batch_submit_orders_for_approval,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_submit_orders_for_approval_and_overbook: gapic_v1.method.wrap_method(
                self.batch_submit_orders_for_approval_and_overbook,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_submit_orders_for_approval_without_reservation_changes: gapic_v1.method.wrap_method(
                self.batch_submit_orders_for_approval_without_reservation_changes,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_pause_orders: gapic_v1.method.wrap_method(
                self.batch_pause_orders,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_resume_orders: gapic_v1.method.wrap_method(
                self.batch_resume_orders,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_resume_and_overbook_orders: gapic_v1.method.wrap_method(
                self.batch_resume_and_overbook_orders,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_approve_orders_without_reservation: gapic_v1.method.wrap_method(
                self.batch_approve_orders_without_reservation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_archive_orders: gapic_v1.method.wrap_method(
                self.batch_archive_orders,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_unarchive_orders: gapic_v1.method.wrap_method(
                self.batch_unarchive_orders,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_delete_orders: gapic_v1.method.wrap_method(
                self.batch_delete_orders,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_disapprove_orders: gapic_v1.method.wrap_method(
                self.batch_disapprove_orders,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_disapprove_orders_without_reservation_changes: gapic_v1.method.wrap_method(
                self.batch_disapprove_orders_without_reservation_changes,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_retract_orders: gapic_v1.method.wrap_method(
                self.batch_retract_orders,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_retract_orders_without_reservation_changes: gapic_v1.method.wrap_method(
                self.batch_retract_orders_without_reservation_changes,
                default_timeout=None,
                client_info=client_info,
            ),
            self.cancel_operation: gapic_v1.method.wrap_method(
                self.cancel_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_operation: gapic_v1.method.wrap_method(
                self.get_operation,
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
    def get_order(
        self,
    ) -> Callable[
        [order_service.GetOrderRequest],
        Union[order_messages.Order, Awaitable[order_messages.Order]],
    ]:
        raise NotImplementedError()

    @property
    def list_orders(
        self,
    ) -> Callable[
        [order_service.ListOrdersRequest],
        Union[
            order_service.ListOrdersResponse,
            Awaitable[order_service.ListOrdersResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def batch_create_orders(
        self,
    ) -> Callable[
        [order_service.BatchCreateOrdersRequest],
        Union[
            order_service.BatchCreateOrdersResponse,
            Awaitable[order_service.BatchCreateOrdersResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def batch_update_orders(
        self,
    ) -> Callable[
        [order_service.BatchUpdateOrdersRequest],
        Union[
            order_service.BatchUpdateOrdersResponse,
            Awaitable[order_service.BatchUpdateOrdersResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def batch_approve_orders(
        self,
    ) -> Callable[
        [order_service.BatchApproveOrdersRequest],
        Union[
            order_service.BatchApproveOrdersResponse,
            Awaitable[order_service.BatchApproveOrdersResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def batch_approve_and_overbook_orders(
        self,
    ) -> Callable[
        [order_service.BatchApproveAndOverbookOrdersRequest],
        Union[
            order_service.BatchApproveAndOverbookOrdersResponse,
            Awaitable[order_service.BatchApproveAndOverbookOrdersResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def batch_submit_orders_for_approval(
        self,
    ) -> Callable[
        [order_service.BatchSubmitOrdersForApprovalRequest],
        Union[
            order_service.BatchSubmitOrdersForApprovalResponse,
            Awaitable[order_service.BatchSubmitOrdersForApprovalResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def batch_submit_orders_for_approval_and_overbook(
        self,
    ) -> Callable[
        [order_service.BatchSubmitOrdersForApprovalAndOverbookRequest],
        Union[
            order_service.BatchSubmitOrdersForApprovalAndOverbookResponse,
            Awaitable[order_service.BatchSubmitOrdersForApprovalAndOverbookResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def batch_submit_orders_for_approval_without_reservation_changes(
        self,
    ) -> Callable[
        [order_service.BatchSubmitOrdersForApprovalWithoutReservationChangesRequest],
        Union[
            order_service.BatchSubmitOrdersForApprovalWithoutReservationChangesResponse,
            Awaitable[
                order_service.BatchSubmitOrdersForApprovalWithoutReservationChangesResponse
            ],
        ],
    ]:
        raise NotImplementedError()

    @property
    def batch_pause_orders(
        self,
    ) -> Callable[
        [order_service.BatchPauseOrdersRequest],
        Union[
            order_service.BatchPauseOrdersResponse,
            Awaitable[order_service.BatchPauseOrdersResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def batch_resume_orders(
        self,
    ) -> Callable[
        [order_service.BatchResumeOrdersRequest],
        Union[
            order_service.BatchResumeOrdersResponse,
            Awaitable[order_service.BatchResumeOrdersResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def batch_resume_and_overbook_orders(
        self,
    ) -> Callable[
        [order_service.BatchResumeAndOverbookOrdersRequest],
        Union[
            order_service.BatchResumeAndOverbookOrdersResponse,
            Awaitable[order_service.BatchResumeAndOverbookOrdersResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def batch_approve_orders_without_reservation(
        self,
    ) -> Callable[
        [order_service.BatchApproveOrdersWithoutReservationRequest],
        Union[
            order_service.BatchApproveOrdersWithoutReservationResponse,
            Awaitable[order_service.BatchApproveOrdersWithoutReservationResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def batch_archive_orders(
        self,
    ) -> Callable[
        [order_service.BatchArchiveOrdersRequest],
        Union[
            order_service.BatchArchiveOrdersResponse,
            Awaitable[order_service.BatchArchiveOrdersResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def batch_unarchive_orders(
        self,
    ) -> Callable[
        [order_service.BatchUnarchiveOrdersRequest],
        Union[
            order_service.BatchUnarchiveOrdersResponse,
            Awaitable[order_service.BatchUnarchiveOrdersResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def batch_delete_orders(
        self,
    ) -> Callable[
        [order_service.BatchDeleteOrdersRequest],
        Union[
            order_service.BatchDeleteOrdersResponse,
            Awaitable[order_service.BatchDeleteOrdersResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def batch_disapprove_orders(
        self,
    ) -> Callable[
        [order_service.BatchDisapproveOrdersRequest],
        Union[
            order_service.BatchDisapproveOrdersResponse,
            Awaitable[order_service.BatchDisapproveOrdersResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def batch_disapprove_orders_without_reservation_changes(
        self,
    ) -> Callable[
        [order_service.BatchDisapproveOrdersWithoutReservationChangesRequest],
        Union[
            order_service.BatchDisapproveOrdersWithoutReservationChangesResponse,
            Awaitable[
                order_service.BatchDisapproveOrdersWithoutReservationChangesResponse
            ],
        ],
    ]:
        raise NotImplementedError()

    @property
    def batch_retract_orders(
        self,
    ) -> Callable[
        [order_service.BatchRetractOrdersRequest],
        Union[
            order_service.BatchRetractOrdersResponse,
            Awaitable[order_service.BatchRetractOrdersResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def batch_retract_orders_without_reservation_changes(
        self,
    ) -> Callable[
        [order_service.BatchRetractOrdersWithoutReservationChangesRequest],
        Union[
            order_service.BatchRetractOrdersWithoutReservationChangesResponse,
            Awaitable[
                order_service.BatchRetractOrdersWithoutReservationChangesResponse
            ],
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
    def kind(self) -> str:
        raise NotImplementedError()


__all__ = ("OrderServiceTransport",)
