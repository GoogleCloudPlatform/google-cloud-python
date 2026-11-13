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
from google.ads.admanager_v1.types import proposal_messages, proposal_service

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class ProposalServiceTransport(abc.ABC):
    """Abstract transport class for ProposalService."""

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
            self.get_proposal: gapic_v1.method.wrap_method(
                self.get_proposal,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_proposals: gapic_v1.method.wrap_method(
                self.list_proposals,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_proposal: gapic_v1.method.wrap_method(
                self.create_proposal,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_create_proposals: gapic_v1.method.wrap_method(
                self.batch_create_proposals,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_proposal: gapic_v1.method.wrap_method(
                self.update_proposal,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_update_proposals: gapic_v1.method.wrap_method(
                self.batch_update_proposals,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_archive_proposals: gapic_v1.method.wrap_method(
                self.batch_archive_proposals,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_unarchive_proposals: gapic_v1.method.wrap_method(
                self.batch_unarchive_proposals,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_pause_proposals: gapic_v1.method.wrap_method(
                self.batch_pause_proposals,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_resume_proposals: gapic_v1.method.wrap_method(
                self.batch_resume_proposals,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_request_buyer_review_proposals: gapic_v1.method.wrap_method(
                self.batch_request_buyer_review_proposals,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_request_buyer_accept_proposals: gapic_v1.method.wrap_method(
                self.batch_request_buyer_accept_proposals,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_reserve_proposals: gapic_v1.method.wrap_method(
                self.batch_reserve_proposals,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_redraft_proposals: gapic_v1.method.wrap_method(
                self.batch_redraft_proposals,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_discard_draft_proposals: gapic_v1.method.wrap_method(
                self.batch_discard_draft_proposals,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_terminate_proposals: gapic_v1.method.wrap_method(
                self.batch_terminate_proposals,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_push_to_order_proposals: gapic_v1.method.wrap_method(
                self.batch_push_to_order_proposals,
                default_timeout=None,
                client_info=client_info,
            ),
            self.fetch_marketplace_comments: gapic_v1.method.wrap_method(
                self.fetch_marketplace_comments,
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
    def get_proposal(
        self,
    ) -> Callable[
        [proposal_service.GetProposalRequest],
        Union[proposal_messages.Proposal, Awaitable[proposal_messages.Proposal]],
    ]:
        raise NotImplementedError()

    @property
    def list_proposals(
        self,
    ) -> Callable[
        [proposal_service.ListProposalsRequest],
        Union[
            proposal_service.ListProposalsResponse,
            Awaitable[proposal_service.ListProposalsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_proposal(
        self,
    ) -> Callable[
        [proposal_service.CreateProposalRequest],
        Union[proposal_messages.Proposal, Awaitable[proposal_messages.Proposal]],
    ]:
        raise NotImplementedError()

    @property
    def batch_create_proposals(
        self,
    ) -> Callable[
        [proposal_service.BatchCreateProposalsRequest],
        Union[
            proposal_service.BatchCreateProposalsResponse,
            Awaitable[proposal_service.BatchCreateProposalsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_proposal(
        self,
    ) -> Callable[
        [proposal_service.UpdateProposalRequest],
        Union[proposal_messages.Proposal, Awaitable[proposal_messages.Proposal]],
    ]:
        raise NotImplementedError()

    @property
    def batch_update_proposals(
        self,
    ) -> Callable[
        [proposal_service.BatchUpdateProposalsRequest],
        Union[
            proposal_service.BatchUpdateProposalsResponse,
            Awaitable[proposal_service.BatchUpdateProposalsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def batch_archive_proposals(
        self,
    ) -> Callable[
        [proposal_service.BatchArchiveProposalsRequest],
        Union[
            proposal_service.BatchArchiveProposalsResponse,
            Awaitable[proposal_service.BatchArchiveProposalsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def batch_unarchive_proposals(
        self,
    ) -> Callable[
        [proposal_service.BatchUnarchiveProposalsRequest],
        Union[
            proposal_service.BatchUnarchiveProposalsResponse,
            Awaitable[proposal_service.BatchUnarchiveProposalsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def batch_pause_proposals(
        self,
    ) -> Callable[
        [proposal_service.BatchPauseProposalsRequest],
        Union[
            proposal_service.BatchPauseProposalsResponse,
            Awaitable[proposal_service.BatchPauseProposalsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def batch_resume_proposals(
        self,
    ) -> Callable[
        [proposal_service.BatchResumeProposalsRequest],
        Union[
            proposal_service.BatchResumeProposalsResponse,
            Awaitable[proposal_service.BatchResumeProposalsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def batch_request_buyer_review_proposals(
        self,
    ) -> Callable[
        [proposal_service.BatchRequestBuyerReviewProposalsRequest],
        Union[
            proposal_service.BatchRequestBuyerReviewProposalsResponse,
            Awaitable[proposal_service.BatchRequestBuyerReviewProposalsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def batch_request_buyer_accept_proposals(
        self,
    ) -> Callable[
        [proposal_service.BatchRequestBuyerAcceptProposalsRequest],
        Union[
            proposal_service.BatchRequestBuyerAcceptProposalsResponse,
            Awaitable[proposal_service.BatchRequestBuyerAcceptProposalsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def batch_reserve_proposals(
        self,
    ) -> Callable[
        [proposal_service.BatchReserveProposalsRequest],
        Union[
            proposal_service.BatchReserveProposalsResponse,
            Awaitable[proposal_service.BatchReserveProposalsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def batch_redraft_proposals(
        self,
    ) -> Callable[
        [proposal_service.BatchRedraftProposalsRequest],
        Union[
            proposal_service.BatchRedraftProposalsResponse,
            Awaitable[proposal_service.BatchRedraftProposalsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def batch_discard_draft_proposals(
        self,
    ) -> Callable[
        [proposal_service.BatchDiscardDraftProposalsRequest],
        Union[
            proposal_service.BatchDiscardDraftProposalsResponse,
            Awaitable[proposal_service.BatchDiscardDraftProposalsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def batch_terminate_proposals(
        self,
    ) -> Callable[
        [proposal_service.BatchTerminateProposalsRequest],
        Union[
            proposal_service.BatchTerminateProposalsResponse,
            Awaitable[proposal_service.BatchTerminateProposalsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def batch_push_to_order_proposals(
        self,
    ) -> Callable[
        [proposal_service.BatchPushToOrderProposalsRequest],
        Union[
            proposal_service.BatchPushToOrderProposalsResponse,
            Awaitable[proposal_service.BatchPushToOrderProposalsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def fetch_marketplace_comments(
        self,
    ) -> Callable[
        [proposal_service.FetchMarketplaceCommentsRequest],
        Union[
            proposal_service.FetchMarketplaceCommentsResponse,
            Awaitable[proposal_service.FetchMarketplaceCommentsResponse],
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


__all__ = ("ProposalServiceTransport",)
