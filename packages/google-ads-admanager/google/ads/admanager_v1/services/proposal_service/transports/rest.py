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

import google.protobuf
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.ads.admanager_v1._compat import transcode_request
from google.ads.admanager_v1.types import proposal_messages, proposal_service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseProposalServiceRestTransport

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


class ProposalServiceRestInterceptor:
    """Interceptor for ProposalService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the ProposalServiceRestTransport.

    .. code-block:: python
        class MyCustomProposalServiceInterceptor(ProposalServiceRestInterceptor):
            def pre_batch_archive_proposals(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_archive_proposals(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_create_proposals(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_create_proposals(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_discard_draft_proposals(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_discard_draft_proposals(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_pause_proposals(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_pause_proposals(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_push_to_order_proposals(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_push_to_order_proposals(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_redraft_proposals(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_redraft_proposals(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_request_buyer_accept_proposals(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_request_buyer_accept_proposals(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_request_buyer_review_proposals(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_request_buyer_review_proposals(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_reserve_proposals(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_reserve_proposals(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_resume_proposals(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_resume_proposals(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_terminate_proposals(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_terminate_proposals(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_unarchive_proposals(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_unarchive_proposals(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_update_proposals(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_update_proposals(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_proposal(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_proposal(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_fetch_marketplace_comments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_marketplace_comments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_proposal(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_proposal(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_proposals(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_proposals(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_proposal(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_proposal(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = ProposalServiceRestTransport(interceptor=MyCustomProposalServiceInterceptor())
        client = ProposalServiceClient(transport=transport)


    """

    def pre_batch_archive_proposals(
        self,
        request: proposal_service.BatchArchiveProposalsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        proposal_service.BatchArchiveProposalsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_archive_proposals

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProposalService server.
        """
        return request, metadata

    def post_batch_archive_proposals(
        self, response: proposal_service.BatchArchiveProposalsResponse
    ) -> proposal_service.BatchArchiveProposalsResponse:
        """Post-rpc interceptor for batch_archive_proposals

        DEPRECATED. Please use the `post_batch_archive_proposals_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProposalService server but before
        it is returned to user code. This `post_batch_archive_proposals` interceptor runs
        before the `post_batch_archive_proposals_with_metadata` interceptor.
        """
        return response

    def post_batch_archive_proposals_with_metadata(
        self,
        response: proposal_service.BatchArchiveProposalsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        proposal_service.BatchArchiveProposalsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_archive_proposals

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProposalService server but before it is returned to user code.

        We recommend only using this `post_batch_archive_proposals_with_metadata`
        interceptor in new development instead of the `post_batch_archive_proposals` interceptor.
        When both interceptors are used, this `post_batch_archive_proposals_with_metadata` interceptor runs after the
        `post_batch_archive_proposals` interceptor. The (possibly modified) response returned by
        `post_batch_archive_proposals` will be passed to
        `post_batch_archive_proposals_with_metadata`.
        """
        return response, metadata

    def pre_batch_create_proposals(
        self,
        request: proposal_service.BatchCreateProposalsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        proposal_service.BatchCreateProposalsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_create_proposals

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProposalService server.
        """
        return request, metadata

    def post_batch_create_proposals(
        self, response: proposal_service.BatchCreateProposalsResponse
    ) -> proposal_service.BatchCreateProposalsResponse:
        """Post-rpc interceptor for batch_create_proposals

        DEPRECATED. Please use the `post_batch_create_proposals_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProposalService server but before
        it is returned to user code. This `post_batch_create_proposals` interceptor runs
        before the `post_batch_create_proposals_with_metadata` interceptor.
        """
        return response

    def post_batch_create_proposals_with_metadata(
        self,
        response: proposal_service.BatchCreateProposalsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        proposal_service.BatchCreateProposalsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_create_proposals

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProposalService server but before it is returned to user code.

        We recommend only using this `post_batch_create_proposals_with_metadata`
        interceptor in new development instead of the `post_batch_create_proposals` interceptor.
        When both interceptors are used, this `post_batch_create_proposals_with_metadata` interceptor runs after the
        `post_batch_create_proposals` interceptor. The (possibly modified) response returned by
        `post_batch_create_proposals` will be passed to
        `post_batch_create_proposals_with_metadata`.
        """
        return response, metadata

    def pre_batch_discard_draft_proposals(
        self,
        request: proposal_service.BatchDiscardDraftProposalsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        proposal_service.BatchDiscardDraftProposalsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_discard_draft_proposals

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProposalService server.
        """
        return request, metadata

    def post_batch_discard_draft_proposals(
        self, response: proposal_service.BatchDiscardDraftProposalsResponse
    ) -> proposal_service.BatchDiscardDraftProposalsResponse:
        """Post-rpc interceptor for batch_discard_draft_proposals

        DEPRECATED. Please use the `post_batch_discard_draft_proposals_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProposalService server but before
        it is returned to user code. This `post_batch_discard_draft_proposals` interceptor runs
        before the `post_batch_discard_draft_proposals_with_metadata` interceptor.
        """
        return response

    def post_batch_discard_draft_proposals_with_metadata(
        self,
        response: proposal_service.BatchDiscardDraftProposalsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        proposal_service.BatchDiscardDraftProposalsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_discard_draft_proposals

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProposalService server but before it is returned to user code.

        We recommend only using this `post_batch_discard_draft_proposals_with_metadata`
        interceptor in new development instead of the `post_batch_discard_draft_proposals` interceptor.
        When both interceptors are used, this `post_batch_discard_draft_proposals_with_metadata` interceptor runs after the
        `post_batch_discard_draft_proposals` interceptor. The (possibly modified) response returned by
        `post_batch_discard_draft_proposals` will be passed to
        `post_batch_discard_draft_proposals_with_metadata`.
        """
        return response, metadata

    def pre_batch_pause_proposals(
        self,
        request: proposal_service.BatchPauseProposalsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        proposal_service.BatchPauseProposalsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_pause_proposals

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProposalService server.
        """
        return request, metadata

    def post_batch_pause_proposals(
        self, response: proposal_service.BatchPauseProposalsResponse
    ) -> proposal_service.BatchPauseProposalsResponse:
        """Post-rpc interceptor for batch_pause_proposals

        DEPRECATED. Please use the `post_batch_pause_proposals_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProposalService server but before
        it is returned to user code. This `post_batch_pause_proposals` interceptor runs
        before the `post_batch_pause_proposals_with_metadata` interceptor.
        """
        return response

    def post_batch_pause_proposals_with_metadata(
        self,
        response: proposal_service.BatchPauseProposalsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        proposal_service.BatchPauseProposalsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_pause_proposals

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProposalService server but before it is returned to user code.

        We recommend only using this `post_batch_pause_proposals_with_metadata`
        interceptor in new development instead of the `post_batch_pause_proposals` interceptor.
        When both interceptors are used, this `post_batch_pause_proposals_with_metadata` interceptor runs after the
        `post_batch_pause_proposals` interceptor. The (possibly modified) response returned by
        `post_batch_pause_proposals` will be passed to
        `post_batch_pause_proposals_with_metadata`.
        """
        return response, metadata

    def pre_batch_push_to_order_proposals(
        self,
        request: proposal_service.BatchPushToOrderProposalsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        proposal_service.BatchPushToOrderProposalsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_push_to_order_proposals

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProposalService server.
        """
        return request, metadata

    def post_batch_push_to_order_proposals(
        self, response: proposal_service.BatchPushToOrderProposalsResponse
    ) -> proposal_service.BatchPushToOrderProposalsResponse:
        """Post-rpc interceptor for batch_push_to_order_proposals

        DEPRECATED. Please use the `post_batch_push_to_order_proposals_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProposalService server but before
        it is returned to user code. This `post_batch_push_to_order_proposals` interceptor runs
        before the `post_batch_push_to_order_proposals_with_metadata` interceptor.
        """
        return response

    def post_batch_push_to_order_proposals_with_metadata(
        self,
        response: proposal_service.BatchPushToOrderProposalsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        proposal_service.BatchPushToOrderProposalsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_push_to_order_proposals

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProposalService server but before it is returned to user code.

        We recommend only using this `post_batch_push_to_order_proposals_with_metadata`
        interceptor in new development instead of the `post_batch_push_to_order_proposals` interceptor.
        When both interceptors are used, this `post_batch_push_to_order_proposals_with_metadata` interceptor runs after the
        `post_batch_push_to_order_proposals` interceptor. The (possibly modified) response returned by
        `post_batch_push_to_order_proposals` will be passed to
        `post_batch_push_to_order_proposals_with_metadata`.
        """
        return response, metadata

    def pre_batch_redraft_proposals(
        self,
        request: proposal_service.BatchRedraftProposalsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        proposal_service.BatchRedraftProposalsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_redraft_proposals

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProposalService server.
        """
        return request, metadata

    def post_batch_redraft_proposals(
        self, response: proposal_service.BatchRedraftProposalsResponse
    ) -> proposal_service.BatchRedraftProposalsResponse:
        """Post-rpc interceptor for batch_redraft_proposals

        DEPRECATED. Please use the `post_batch_redraft_proposals_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProposalService server but before
        it is returned to user code. This `post_batch_redraft_proposals` interceptor runs
        before the `post_batch_redraft_proposals_with_metadata` interceptor.
        """
        return response

    def post_batch_redraft_proposals_with_metadata(
        self,
        response: proposal_service.BatchRedraftProposalsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        proposal_service.BatchRedraftProposalsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_redraft_proposals

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProposalService server but before it is returned to user code.

        We recommend only using this `post_batch_redraft_proposals_with_metadata`
        interceptor in new development instead of the `post_batch_redraft_proposals` interceptor.
        When both interceptors are used, this `post_batch_redraft_proposals_with_metadata` interceptor runs after the
        `post_batch_redraft_proposals` interceptor. The (possibly modified) response returned by
        `post_batch_redraft_proposals` will be passed to
        `post_batch_redraft_proposals_with_metadata`.
        """
        return response, metadata

    def pre_batch_request_buyer_accept_proposals(
        self,
        request: proposal_service.BatchRequestBuyerAcceptProposalsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        proposal_service.BatchRequestBuyerAcceptProposalsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_request_buyer_accept_proposals

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProposalService server.
        """
        return request, metadata

    def post_batch_request_buyer_accept_proposals(
        self, response: proposal_service.BatchRequestBuyerAcceptProposalsResponse
    ) -> proposal_service.BatchRequestBuyerAcceptProposalsResponse:
        """Post-rpc interceptor for batch_request_buyer_accept_proposals

        DEPRECATED. Please use the `post_batch_request_buyer_accept_proposals_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProposalService server but before
        it is returned to user code. This `post_batch_request_buyer_accept_proposals` interceptor runs
        before the `post_batch_request_buyer_accept_proposals_with_metadata` interceptor.
        """
        return response

    def post_batch_request_buyer_accept_proposals_with_metadata(
        self,
        response: proposal_service.BatchRequestBuyerAcceptProposalsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        proposal_service.BatchRequestBuyerAcceptProposalsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_request_buyer_accept_proposals

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProposalService server but before it is returned to user code.

        We recommend only using this `post_batch_request_buyer_accept_proposals_with_metadata`
        interceptor in new development instead of the `post_batch_request_buyer_accept_proposals` interceptor.
        When both interceptors are used, this `post_batch_request_buyer_accept_proposals_with_metadata` interceptor runs after the
        `post_batch_request_buyer_accept_proposals` interceptor. The (possibly modified) response returned by
        `post_batch_request_buyer_accept_proposals` will be passed to
        `post_batch_request_buyer_accept_proposals_with_metadata`.
        """
        return response, metadata

    def pre_batch_request_buyer_review_proposals(
        self,
        request: proposal_service.BatchRequestBuyerReviewProposalsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        proposal_service.BatchRequestBuyerReviewProposalsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_request_buyer_review_proposals

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProposalService server.
        """
        return request, metadata

    def post_batch_request_buyer_review_proposals(
        self, response: proposal_service.BatchRequestBuyerReviewProposalsResponse
    ) -> proposal_service.BatchRequestBuyerReviewProposalsResponse:
        """Post-rpc interceptor for batch_request_buyer_review_proposals

        DEPRECATED. Please use the `post_batch_request_buyer_review_proposals_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProposalService server but before
        it is returned to user code. This `post_batch_request_buyer_review_proposals` interceptor runs
        before the `post_batch_request_buyer_review_proposals_with_metadata` interceptor.
        """
        return response

    def post_batch_request_buyer_review_proposals_with_metadata(
        self,
        response: proposal_service.BatchRequestBuyerReviewProposalsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        proposal_service.BatchRequestBuyerReviewProposalsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_request_buyer_review_proposals

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProposalService server but before it is returned to user code.

        We recommend only using this `post_batch_request_buyer_review_proposals_with_metadata`
        interceptor in new development instead of the `post_batch_request_buyer_review_proposals` interceptor.
        When both interceptors are used, this `post_batch_request_buyer_review_proposals_with_metadata` interceptor runs after the
        `post_batch_request_buyer_review_proposals` interceptor. The (possibly modified) response returned by
        `post_batch_request_buyer_review_proposals` will be passed to
        `post_batch_request_buyer_review_proposals_with_metadata`.
        """
        return response, metadata

    def pre_batch_reserve_proposals(
        self,
        request: proposal_service.BatchReserveProposalsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        proposal_service.BatchReserveProposalsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_reserve_proposals

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProposalService server.
        """
        return request, metadata

    def post_batch_reserve_proposals(
        self, response: proposal_service.BatchReserveProposalsResponse
    ) -> proposal_service.BatchReserveProposalsResponse:
        """Post-rpc interceptor for batch_reserve_proposals

        DEPRECATED. Please use the `post_batch_reserve_proposals_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProposalService server but before
        it is returned to user code. This `post_batch_reserve_proposals` interceptor runs
        before the `post_batch_reserve_proposals_with_metadata` interceptor.
        """
        return response

    def post_batch_reserve_proposals_with_metadata(
        self,
        response: proposal_service.BatchReserveProposalsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        proposal_service.BatchReserveProposalsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_reserve_proposals

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProposalService server but before it is returned to user code.

        We recommend only using this `post_batch_reserve_proposals_with_metadata`
        interceptor in new development instead of the `post_batch_reserve_proposals` interceptor.
        When both interceptors are used, this `post_batch_reserve_proposals_with_metadata` interceptor runs after the
        `post_batch_reserve_proposals` interceptor. The (possibly modified) response returned by
        `post_batch_reserve_proposals` will be passed to
        `post_batch_reserve_proposals_with_metadata`.
        """
        return response, metadata

    def pre_batch_resume_proposals(
        self,
        request: proposal_service.BatchResumeProposalsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        proposal_service.BatchResumeProposalsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_resume_proposals

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProposalService server.
        """
        return request, metadata

    def post_batch_resume_proposals(
        self, response: proposal_service.BatchResumeProposalsResponse
    ) -> proposal_service.BatchResumeProposalsResponse:
        """Post-rpc interceptor for batch_resume_proposals

        DEPRECATED. Please use the `post_batch_resume_proposals_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProposalService server but before
        it is returned to user code. This `post_batch_resume_proposals` interceptor runs
        before the `post_batch_resume_proposals_with_metadata` interceptor.
        """
        return response

    def post_batch_resume_proposals_with_metadata(
        self,
        response: proposal_service.BatchResumeProposalsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        proposal_service.BatchResumeProposalsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_resume_proposals

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProposalService server but before it is returned to user code.

        We recommend only using this `post_batch_resume_proposals_with_metadata`
        interceptor in new development instead of the `post_batch_resume_proposals` interceptor.
        When both interceptors are used, this `post_batch_resume_proposals_with_metadata` interceptor runs after the
        `post_batch_resume_proposals` interceptor. The (possibly modified) response returned by
        `post_batch_resume_proposals` will be passed to
        `post_batch_resume_proposals_with_metadata`.
        """
        return response, metadata

    def pre_batch_terminate_proposals(
        self,
        request: proposal_service.BatchTerminateProposalsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        proposal_service.BatchTerminateProposalsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_terminate_proposals

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProposalService server.
        """
        return request, metadata

    def post_batch_terminate_proposals(
        self, response: proposal_service.BatchTerminateProposalsResponse
    ) -> proposal_service.BatchTerminateProposalsResponse:
        """Post-rpc interceptor for batch_terminate_proposals

        DEPRECATED. Please use the `post_batch_terminate_proposals_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProposalService server but before
        it is returned to user code. This `post_batch_terminate_proposals` interceptor runs
        before the `post_batch_terminate_proposals_with_metadata` interceptor.
        """
        return response

    def post_batch_terminate_proposals_with_metadata(
        self,
        response: proposal_service.BatchTerminateProposalsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        proposal_service.BatchTerminateProposalsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_terminate_proposals

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProposalService server but before it is returned to user code.

        We recommend only using this `post_batch_terminate_proposals_with_metadata`
        interceptor in new development instead of the `post_batch_terminate_proposals` interceptor.
        When both interceptors are used, this `post_batch_terminate_proposals_with_metadata` interceptor runs after the
        `post_batch_terminate_proposals` interceptor. The (possibly modified) response returned by
        `post_batch_terminate_proposals` will be passed to
        `post_batch_terminate_proposals_with_metadata`.
        """
        return response, metadata

    def pre_batch_unarchive_proposals(
        self,
        request: proposal_service.BatchUnarchiveProposalsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        proposal_service.BatchUnarchiveProposalsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_unarchive_proposals

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProposalService server.
        """
        return request, metadata

    def post_batch_unarchive_proposals(
        self, response: proposal_service.BatchUnarchiveProposalsResponse
    ) -> proposal_service.BatchUnarchiveProposalsResponse:
        """Post-rpc interceptor for batch_unarchive_proposals

        DEPRECATED. Please use the `post_batch_unarchive_proposals_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProposalService server but before
        it is returned to user code. This `post_batch_unarchive_proposals` interceptor runs
        before the `post_batch_unarchive_proposals_with_metadata` interceptor.
        """
        return response

    def post_batch_unarchive_proposals_with_metadata(
        self,
        response: proposal_service.BatchUnarchiveProposalsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        proposal_service.BatchUnarchiveProposalsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_unarchive_proposals

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProposalService server but before it is returned to user code.

        We recommend only using this `post_batch_unarchive_proposals_with_metadata`
        interceptor in new development instead of the `post_batch_unarchive_proposals` interceptor.
        When both interceptors are used, this `post_batch_unarchive_proposals_with_metadata` interceptor runs after the
        `post_batch_unarchive_proposals` interceptor. The (possibly modified) response returned by
        `post_batch_unarchive_proposals` will be passed to
        `post_batch_unarchive_proposals_with_metadata`.
        """
        return response, metadata

    def pre_batch_update_proposals(
        self,
        request: proposal_service.BatchUpdateProposalsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        proposal_service.BatchUpdateProposalsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_update_proposals

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProposalService server.
        """
        return request, metadata

    def post_batch_update_proposals(
        self, response: proposal_service.BatchUpdateProposalsResponse
    ) -> proposal_service.BatchUpdateProposalsResponse:
        """Post-rpc interceptor for batch_update_proposals

        DEPRECATED. Please use the `post_batch_update_proposals_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProposalService server but before
        it is returned to user code. This `post_batch_update_proposals` interceptor runs
        before the `post_batch_update_proposals_with_metadata` interceptor.
        """
        return response

    def post_batch_update_proposals_with_metadata(
        self,
        response: proposal_service.BatchUpdateProposalsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        proposal_service.BatchUpdateProposalsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_update_proposals

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProposalService server but before it is returned to user code.

        We recommend only using this `post_batch_update_proposals_with_metadata`
        interceptor in new development instead of the `post_batch_update_proposals` interceptor.
        When both interceptors are used, this `post_batch_update_proposals_with_metadata` interceptor runs after the
        `post_batch_update_proposals` interceptor. The (possibly modified) response returned by
        `post_batch_update_proposals` will be passed to
        `post_batch_update_proposals_with_metadata`.
        """
        return response, metadata

    def pre_create_proposal(
        self,
        request: proposal_service.CreateProposalRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        proposal_service.CreateProposalRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_proposal

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProposalService server.
        """
        return request, metadata

    def post_create_proposal(
        self, response: proposal_messages.Proposal
    ) -> proposal_messages.Proposal:
        """Post-rpc interceptor for create_proposal

        DEPRECATED. Please use the `post_create_proposal_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProposalService server but before
        it is returned to user code. This `post_create_proposal` interceptor runs
        before the `post_create_proposal_with_metadata` interceptor.
        """
        return response

    def post_create_proposal_with_metadata(
        self,
        response: proposal_messages.Proposal,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[proposal_messages.Proposal, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_proposal

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProposalService server but before it is returned to user code.

        We recommend only using this `post_create_proposal_with_metadata`
        interceptor in new development instead of the `post_create_proposal` interceptor.
        When both interceptors are used, this `post_create_proposal_with_metadata` interceptor runs after the
        `post_create_proposal` interceptor. The (possibly modified) response returned by
        `post_create_proposal` will be passed to
        `post_create_proposal_with_metadata`.
        """
        return response, metadata

    def pre_fetch_marketplace_comments(
        self,
        request: proposal_service.FetchMarketplaceCommentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        proposal_service.FetchMarketplaceCommentsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for fetch_marketplace_comments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProposalService server.
        """
        return request, metadata

    def post_fetch_marketplace_comments(
        self, response: proposal_service.FetchMarketplaceCommentsResponse
    ) -> proposal_service.FetchMarketplaceCommentsResponse:
        """Post-rpc interceptor for fetch_marketplace_comments

        DEPRECATED. Please use the `post_fetch_marketplace_comments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProposalService server but before
        it is returned to user code. This `post_fetch_marketplace_comments` interceptor runs
        before the `post_fetch_marketplace_comments_with_metadata` interceptor.
        """
        return response

    def post_fetch_marketplace_comments_with_metadata(
        self,
        response: proposal_service.FetchMarketplaceCommentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        proposal_service.FetchMarketplaceCommentsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for fetch_marketplace_comments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProposalService server but before it is returned to user code.

        We recommend only using this `post_fetch_marketplace_comments_with_metadata`
        interceptor in new development instead of the `post_fetch_marketplace_comments` interceptor.
        When both interceptors are used, this `post_fetch_marketplace_comments_with_metadata` interceptor runs after the
        `post_fetch_marketplace_comments` interceptor. The (possibly modified) response returned by
        `post_fetch_marketplace_comments` will be passed to
        `post_fetch_marketplace_comments_with_metadata`.
        """
        return response, metadata

    def pre_get_proposal(
        self,
        request: proposal_service.GetProposalRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        proposal_service.GetProposalRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_proposal

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProposalService server.
        """
        return request, metadata

    def post_get_proposal(
        self, response: proposal_messages.Proposal
    ) -> proposal_messages.Proposal:
        """Post-rpc interceptor for get_proposal

        DEPRECATED. Please use the `post_get_proposal_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProposalService server but before
        it is returned to user code. This `post_get_proposal` interceptor runs
        before the `post_get_proposal_with_metadata` interceptor.
        """
        return response

    def post_get_proposal_with_metadata(
        self,
        response: proposal_messages.Proposal,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[proposal_messages.Proposal, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_proposal

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProposalService server but before it is returned to user code.

        We recommend only using this `post_get_proposal_with_metadata`
        interceptor in new development instead of the `post_get_proposal` interceptor.
        When both interceptors are used, this `post_get_proposal_with_metadata` interceptor runs after the
        `post_get_proposal` interceptor. The (possibly modified) response returned by
        `post_get_proposal` will be passed to
        `post_get_proposal_with_metadata`.
        """
        return response, metadata

    def pre_list_proposals(
        self,
        request: proposal_service.ListProposalsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        proposal_service.ListProposalsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_proposals

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProposalService server.
        """
        return request, metadata

    def post_list_proposals(
        self, response: proposal_service.ListProposalsResponse
    ) -> proposal_service.ListProposalsResponse:
        """Post-rpc interceptor for list_proposals

        DEPRECATED. Please use the `post_list_proposals_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProposalService server but before
        it is returned to user code. This `post_list_proposals` interceptor runs
        before the `post_list_proposals_with_metadata` interceptor.
        """
        return response

    def post_list_proposals_with_metadata(
        self,
        response: proposal_service.ListProposalsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        proposal_service.ListProposalsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_proposals

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProposalService server but before it is returned to user code.

        We recommend only using this `post_list_proposals_with_metadata`
        interceptor in new development instead of the `post_list_proposals` interceptor.
        When both interceptors are used, this `post_list_proposals_with_metadata` interceptor runs after the
        `post_list_proposals` interceptor. The (possibly modified) response returned by
        `post_list_proposals` will be passed to
        `post_list_proposals_with_metadata`.
        """
        return response, metadata

    def pre_update_proposal(
        self,
        request: proposal_service.UpdateProposalRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        proposal_service.UpdateProposalRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_proposal

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProposalService server.
        """
        return request, metadata

    def post_update_proposal(
        self, response: proposal_messages.Proposal
    ) -> proposal_messages.Proposal:
        """Post-rpc interceptor for update_proposal

        DEPRECATED. Please use the `post_update_proposal_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProposalService server but before
        it is returned to user code. This `post_update_proposal` interceptor runs
        before the `post_update_proposal_with_metadata` interceptor.
        """
        return response

    def post_update_proposal_with_metadata(
        self,
        response: proposal_messages.Proposal,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[proposal_messages.Proposal, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_proposal

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProposalService server but before it is returned to user code.

        We recommend only using this `post_update_proposal_with_metadata`
        interceptor in new development instead of the `post_update_proposal` interceptor.
        When both interceptors are used, this `post_update_proposal_with_metadata` interceptor runs after the
        `post_update_proposal` interceptor. The (possibly modified) response returned by
        `post_update_proposal` will be passed to
        `post_update_proposal_with_metadata`.
        """
        return response, metadata

    def pre_cancel_operation(
        self,
        request: operations_pb2.CancelOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.CancelOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProposalService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the ProposalService server but before
        it is returned to user code.
        """
        return response

    def pre_get_operation(
        self,
        request: operations_pb2.GetOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.GetOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProposalService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the ProposalService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class ProposalServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: ProposalServiceRestInterceptor


class ProposalServiceRestTransport(_BaseProposalServiceRestTransport):
    """REST backend synchronous transport for ProposalService.

    Provides methods for handling ``Proposal`` objects.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "admanager.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[ProposalServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
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
            interceptor (Optional[ProposalServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or ProposalServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _BatchArchiveProposals(
        _BaseProposalServiceRestTransport._BaseBatchArchiveProposals,
        ProposalServiceRestStub,
    ):
        def __hash__(self):
            return hash("ProposalServiceRestTransport.BatchArchiveProposals")

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
            request: proposal_service.BatchArchiveProposalsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> proposal_service.BatchArchiveProposalsResponse:
            r"""Call the batch archive proposals method over HTTP.

            Args:
                request (~.proposal_service.BatchArchiveProposalsRequest):
                    The request object. Request message for ``BatchArchiveProposals`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.proposal_service.BatchArchiveProposalsResponse:
                    Response message for ``BatchArchiveProposals`` method.
            """

            http_options = _BaseProposalServiceRestTransport._BaseBatchArchiveProposals._get_http_options()
            request, metadata = self._interceptor.pre_batch_archive_proposals(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProposalServiceRestTransport._BaseBatchArchiveProposals,
                    "_BaseBatchArchiveProposals__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ProposalServiceClient.BatchArchiveProposals",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ProposalService",
                        "rpcName": "BatchArchiveProposals",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ProposalServiceRestTransport._BatchArchiveProposals._get_response(
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
            resp = proposal_service.BatchArchiveProposalsResponse()
            pb_resp = proposal_service.BatchArchiveProposalsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_archive_proposals(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_archive_proposals_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        proposal_service.BatchArchiveProposalsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.ProposalServiceClient.batch_archive_proposals",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ProposalService",
                        "rpcName": "BatchArchiveProposals",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchCreateProposals(
        _BaseProposalServiceRestTransport._BaseBatchCreateProposals,
        ProposalServiceRestStub,
    ):
        def __hash__(self):
            return hash("ProposalServiceRestTransport.BatchCreateProposals")

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
            request: proposal_service.BatchCreateProposalsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> proposal_service.BatchCreateProposalsResponse:
            r"""Call the batch create proposals method over HTTP.

            Args:
                request (~.proposal_service.BatchCreateProposalsRequest):
                    The request object. Request object for ``BatchCreateProposals`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.proposal_service.BatchCreateProposalsResponse:
                    Response object for ``BatchCreateProposals`` method.
            """

            http_options = _BaseProposalServiceRestTransport._BaseBatchCreateProposals._get_http_options()
            request, metadata = self._interceptor.pre_batch_create_proposals(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProposalServiceRestTransport._BaseBatchCreateProposals,
                    "_BaseBatchCreateProposals__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ProposalServiceClient.BatchCreateProposals",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ProposalService",
                        "rpcName": "BatchCreateProposals",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProposalServiceRestTransport._BatchCreateProposals._get_response(
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
            resp = proposal_service.BatchCreateProposalsResponse()
            pb_resp = proposal_service.BatchCreateProposalsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_create_proposals(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_create_proposals_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        proposal_service.BatchCreateProposalsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.ProposalServiceClient.batch_create_proposals",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ProposalService",
                        "rpcName": "BatchCreateProposals",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchDiscardDraftProposals(
        _BaseProposalServiceRestTransport._BaseBatchDiscardDraftProposals,
        ProposalServiceRestStub,
    ):
        def __hash__(self):
            return hash("ProposalServiceRestTransport.BatchDiscardDraftProposals")

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
            request: proposal_service.BatchDiscardDraftProposalsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> proposal_service.BatchDiscardDraftProposalsResponse:
            r"""Call the batch discard draft
            proposals method over HTTP.

                Args:
                    request (~.proposal_service.BatchDiscardDraftProposalsRequest):
                        The request object. Request message for ``BatchDiscardDraftProposals``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.proposal_service.BatchDiscardDraftProposalsResponse:
                        Response message for ``BatchDiscardDraftProposals``
                    method.

            """

            http_options = _BaseProposalServiceRestTransport._BaseBatchDiscardDraftProposals._get_http_options()
            request, metadata = self._interceptor.pre_batch_discard_draft_proposals(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProposalServiceRestTransport._BaseBatchDiscardDraftProposals,
                    "_BaseBatchDiscardDraftProposals__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ProposalServiceClient.BatchDiscardDraftProposals",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ProposalService",
                        "rpcName": "BatchDiscardDraftProposals",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ProposalServiceRestTransport._BatchDiscardDraftProposals._get_response(
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
            resp = proposal_service.BatchDiscardDraftProposalsResponse()
            pb_resp = proposal_service.BatchDiscardDraftProposalsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_discard_draft_proposals(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_discard_draft_proposals_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        proposal_service.BatchDiscardDraftProposalsResponse.to_json(
                            response
                        )
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.ProposalServiceClient.batch_discard_draft_proposals",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ProposalService",
                        "rpcName": "BatchDiscardDraftProposals",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchPauseProposals(
        _BaseProposalServiceRestTransport._BaseBatchPauseProposals,
        ProposalServiceRestStub,
    ):
        def __hash__(self):
            return hash("ProposalServiceRestTransport.BatchPauseProposals")

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
            request: proposal_service.BatchPauseProposalsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> proposal_service.BatchPauseProposalsResponse:
            r"""Call the batch pause proposals method over HTTP.

            Args:
                request (~.proposal_service.BatchPauseProposalsRequest):
                    The request object. Request message for ``BatchPauseProposals`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.proposal_service.BatchPauseProposalsResponse:
                    Response message for ``BatchPauseProposals`` method.
            """

            http_options = _BaseProposalServiceRestTransport._BaseBatchPauseProposals._get_http_options()
            request, metadata = self._interceptor.pre_batch_pause_proposals(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProposalServiceRestTransport._BaseBatchPauseProposals,
                    "_BaseBatchPauseProposals__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ProposalServiceClient.BatchPauseProposals",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ProposalService",
                        "rpcName": "BatchPauseProposals",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProposalServiceRestTransport._BatchPauseProposals._get_response(
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
            resp = proposal_service.BatchPauseProposalsResponse()
            pb_resp = proposal_service.BatchPauseProposalsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_pause_proposals(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_pause_proposals_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        proposal_service.BatchPauseProposalsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.ProposalServiceClient.batch_pause_proposals",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ProposalService",
                        "rpcName": "BatchPauseProposals",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchPushToOrderProposals(
        _BaseProposalServiceRestTransport._BaseBatchPushToOrderProposals,
        ProposalServiceRestStub,
    ):
        def __hash__(self):
            return hash("ProposalServiceRestTransport.BatchPushToOrderProposals")

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
            request: proposal_service.BatchPushToOrderProposalsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> proposal_service.BatchPushToOrderProposalsResponse:
            r"""Call the batch push to order
            proposals method over HTTP.

                Args:
                    request (~.proposal_service.BatchPushToOrderProposalsRequest):
                        The request object. Request message for ``BatchPushToOrderProposals``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.proposal_service.BatchPushToOrderProposalsResponse:
                        Response message for ``BatchPushToOrderProposals``
                    method.

            """

            http_options = _BaseProposalServiceRestTransport._BaseBatchPushToOrderProposals._get_http_options()
            request, metadata = self._interceptor.pre_batch_push_to_order_proposals(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProposalServiceRestTransport._BaseBatchPushToOrderProposals,
                    "_BaseBatchPushToOrderProposals__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ProposalServiceClient.BatchPushToOrderProposals",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ProposalService",
                        "rpcName": "BatchPushToOrderProposals",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ProposalServiceRestTransport._BatchPushToOrderProposals._get_response(
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
            resp = proposal_service.BatchPushToOrderProposalsResponse()
            pb_resp = proposal_service.BatchPushToOrderProposalsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_push_to_order_proposals(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_push_to_order_proposals_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        proposal_service.BatchPushToOrderProposalsResponse.to_json(
                            response
                        )
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.ProposalServiceClient.batch_push_to_order_proposals",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ProposalService",
                        "rpcName": "BatchPushToOrderProposals",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchRedraftProposals(
        _BaseProposalServiceRestTransport._BaseBatchRedraftProposals,
        ProposalServiceRestStub,
    ):
        def __hash__(self):
            return hash("ProposalServiceRestTransport.BatchRedraftProposals")

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
            request: proposal_service.BatchRedraftProposalsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> proposal_service.BatchRedraftProposalsResponse:
            r"""Call the batch redraft proposals method over HTTP.

            Args:
                request (~.proposal_service.BatchRedraftProposalsRequest):
                    The request object. Request message for ``BatchRedraftProposals`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.proposal_service.BatchRedraftProposalsResponse:
                    Response message for ``BatchRedraftProposals`` method.
            """

            http_options = _BaseProposalServiceRestTransport._BaseBatchRedraftProposals._get_http_options()
            request, metadata = self._interceptor.pre_batch_redraft_proposals(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProposalServiceRestTransport._BaseBatchRedraftProposals,
                    "_BaseBatchRedraftProposals__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ProposalServiceClient.BatchRedraftProposals",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ProposalService",
                        "rpcName": "BatchRedraftProposals",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ProposalServiceRestTransport._BatchRedraftProposals._get_response(
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
            resp = proposal_service.BatchRedraftProposalsResponse()
            pb_resp = proposal_service.BatchRedraftProposalsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_redraft_proposals(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_redraft_proposals_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        proposal_service.BatchRedraftProposalsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.ProposalServiceClient.batch_redraft_proposals",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ProposalService",
                        "rpcName": "BatchRedraftProposals",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchRequestBuyerAcceptProposals(
        _BaseProposalServiceRestTransport._BaseBatchRequestBuyerAcceptProposals,
        ProposalServiceRestStub,
    ):
        def __hash__(self):
            return hash("ProposalServiceRestTransport.BatchRequestBuyerAcceptProposals")

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
            request: proposal_service.BatchRequestBuyerAcceptProposalsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> proposal_service.BatchRequestBuyerAcceptProposalsResponse:
            r"""Call the batch request buyer
            accept proposals method over HTTP.

                Args:
                    request (~.proposal_service.BatchRequestBuyerAcceptProposalsRequest):
                        The request object. Request message for ``BatchRequestBuyerAcceptProposals``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.proposal_service.BatchRequestBuyerAcceptProposalsResponse:
                        Response message for
                    ``BatchRequestBuyerAcceptProposals`` method.

            """

            http_options = _BaseProposalServiceRestTransport._BaseBatchRequestBuyerAcceptProposals._get_http_options()
            request, metadata = (
                self._interceptor.pre_batch_request_buyer_accept_proposals(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProposalServiceRestTransport._BaseBatchRequestBuyerAcceptProposals,
                    "_BaseBatchRequestBuyerAcceptProposals__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ProposalServiceClient.BatchRequestBuyerAcceptProposals",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ProposalService",
                        "rpcName": "BatchRequestBuyerAcceptProposals",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProposalServiceRestTransport._BatchRequestBuyerAcceptProposals._get_response(
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
            resp = proposal_service.BatchRequestBuyerAcceptProposalsResponse()
            pb_resp = proposal_service.BatchRequestBuyerAcceptProposalsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_request_buyer_accept_proposals(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_request_buyer_accept_proposals_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = proposal_service.BatchRequestBuyerAcceptProposalsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.ProposalServiceClient.batch_request_buyer_accept_proposals",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ProposalService",
                        "rpcName": "BatchRequestBuyerAcceptProposals",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchRequestBuyerReviewProposals(
        _BaseProposalServiceRestTransport._BaseBatchRequestBuyerReviewProposals,
        ProposalServiceRestStub,
    ):
        def __hash__(self):
            return hash("ProposalServiceRestTransport.BatchRequestBuyerReviewProposals")

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
            request: proposal_service.BatchRequestBuyerReviewProposalsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> proposal_service.BatchRequestBuyerReviewProposalsResponse:
            r"""Call the batch request buyer
            review proposals method over HTTP.

                Args:
                    request (~.proposal_service.BatchRequestBuyerReviewProposalsRequest):
                        The request object. Request message for ``BatchRequestBuyerReviewProposals``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.proposal_service.BatchRequestBuyerReviewProposalsResponse:
                        Response message for
                    ``BatchRequestBuyerReviewProposals`` method.

            """

            http_options = _BaseProposalServiceRestTransport._BaseBatchRequestBuyerReviewProposals._get_http_options()
            request, metadata = (
                self._interceptor.pre_batch_request_buyer_review_proposals(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProposalServiceRestTransport._BaseBatchRequestBuyerReviewProposals,
                    "_BaseBatchRequestBuyerReviewProposals__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ProposalServiceClient.BatchRequestBuyerReviewProposals",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ProposalService",
                        "rpcName": "BatchRequestBuyerReviewProposals",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProposalServiceRestTransport._BatchRequestBuyerReviewProposals._get_response(
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
            resp = proposal_service.BatchRequestBuyerReviewProposalsResponse()
            pb_resp = proposal_service.BatchRequestBuyerReviewProposalsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_request_buyer_review_proposals(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_request_buyer_review_proposals_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = proposal_service.BatchRequestBuyerReviewProposalsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.ProposalServiceClient.batch_request_buyer_review_proposals",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ProposalService",
                        "rpcName": "BatchRequestBuyerReviewProposals",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchReserveProposals(
        _BaseProposalServiceRestTransport._BaseBatchReserveProposals,
        ProposalServiceRestStub,
    ):
        def __hash__(self):
            return hash("ProposalServiceRestTransport.BatchReserveProposals")

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
            request: proposal_service.BatchReserveProposalsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> proposal_service.BatchReserveProposalsResponse:
            r"""Call the batch reserve proposals method over HTTP.

            Args:
                request (~.proposal_service.BatchReserveProposalsRequest):
                    The request object. Request message for ``BatchReserveProposals`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.proposal_service.BatchReserveProposalsResponse:
                    Response message for ``BatchReserveProposals`` method.
            """

            http_options = _BaseProposalServiceRestTransport._BaseBatchReserveProposals._get_http_options()
            request, metadata = self._interceptor.pre_batch_reserve_proposals(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProposalServiceRestTransport._BaseBatchReserveProposals,
                    "_BaseBatchReserveProposals__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ProposalServiceClient.BatchReserveProposals",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ProposalService",
                        "rpcName": "BatchReserveProposals",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ProposalServiceRestTransport._BatchReserveProposals._get_response(
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
            resp = proposal_service.BatchReserveProposalsResponse()
            pb_resp = proposal_service.BatchReserveProposalsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_reserve_proposals(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_reserve_proposals_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        proposal_service.BatchReserveProposalsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.ProposalServiceClient.batch_reserve_proposals",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ProposalService",
                        "rpcName": "BatchReserveProposals",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchResumeProposals(
        _BaseProposalServiceRestTransport._BaseBatchResumeProposals,
        ProposalServiceRestStub,
    ):
        def __hash__(self):
            return hash("ProposalServiceRestTransport.BatchResumeProposals")

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
            request: proposal_service.BatchResumeProposalsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> proposal_service.BatchResumeProposalsResponse:
            r"""Call the batch resume proposals method over HTTP.

            Args:
                request (~.proposal_service.BatchResumeProposalsRequest):
                    The request object. Request message for ``BatchResumeProposals`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.proposal_service.BatchResumeProposalsResponse:
                    Response message for ``BatchResumeProposals`` method.
            """

            http_options = _BaseProposalServiceRestTransport._BaseBatchResumeProposals._get_http_options()
            request, metadata = self._interceptor.pre_batch_resume_proposals(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProposalServiceRestTransport._BaseBatchResumeProposals,
                    "_BaseBatchResumeProposals__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ProposalServiceClient.BatchResumeProposals",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ProposalService",
                        "rpcName": "BatchResumeProposals",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProposalServiceRestTransport._BatchResumeProposals._get_response(
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
            resp = proposal_service.BatchResumeProposalsResponse()
            pb_resp = proposal_service.BatchResumeProposalsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_resume_proposals(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_resume_proposals_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        proposal_service.BatchResumeProposalsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.ProposalServiceClient.batch_resume_proposals",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ProposalService",
                        "rpcName": "BatchResumeProposals",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchTerminateProposals(
        _BaseProposalServiceRestTransport._BaseBatchTerminateProposals,
        ProposalServiceRestStub,
    ):
        def __hash__(self):
            return hash("ProposalServiceRestTransport.BatchTerminateProposals")

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
            request: proposal_service.BatchTerminateProposalsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> proposal_service.BatchTerminateProposalsResponse:
            r"""Call the batch terminate proposals method over HTTP.

            Args:
                request (~.proposal_service.BatchTerminateProposalsRequest):
                    The request object. Request message for ``BatchTerminateProposals`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.proposal_service.BatchTerminateProposalsResponse:
                    Response message for ``BatchTerminateProposals`` method.
            """

            http_options = _BaseProposalServiceRestTransport._BaseBatchTerminateProposals._get_http_options()
            request, metadata = self._interceptor.pre_batch_terminate_proposals(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProposalServiceRestTransport._BaseBatchTerminateProposals,
                    "_BaseBatchTerminateProposals__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ProposalServiceClient.BatchTerminateProposals",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ProposalService",
                        "rpcName": "BatchTerminateProposals",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ProposalServiceRestTransport._BatchTerminateProposals._get_response(
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
            resp = proposal_service.BatchTerminateProposalsResponse()
            pb_resp = proposal_service.BatchTerminateProposalsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_terminate_proposals(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_terminate_proposals_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        proposal_service.BatchTerminateProposalsResponse.to_json(
                            response
                        )
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.ProposalServiceClient.batch_terminate_proposals",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ProposalService",
                        "rpcName": "BatchTerminateProposals",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchUnarchiveProposals(
        _BaseProposalServiceRestTransport._BaseBatchUnarchiveProposals,
        ProposalServiceRestStub,
    ):
        def __hash__(self):
            return hash("ProposalServiceRestTransport.BatchUnarchiveProposals")

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
            request: proposal_service.BatchUnarchiveProposalsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> proposal_service.BatchUnarchiveProposalsResponse:
            r"""Call the batch unarchive proposals method over HTTP.

            Args:
                request (~.proposal_service.BatchUnarchiveProposalsRequest):
                    The request object. Request message for ``BatchUnarchiveProposals`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.proposal_service.BatchUnarchiveProposalsResponse:
                    Response message for ``BatchUnarchiveProposals`` method.
            """

            http_options = _BaseProposalServiceRestTransport._BaseBatchUnarchiveProposals._get_http_options()
            request, metadata = self._interceptor.pre_batch_unarchive_proposals(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProposalServiceRestTransport._BaseBatchUnarchiveProposals,
                    "_BaseBatchUnarchiveProposals__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ProposalServiceClient.BatchUnarchiveProposals",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ProposalService",
                        "rpcName": "BatchUnarchiveProposals",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ProposalServiceRestTransport._BatchUnarchiveProposals._get_response(
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
            resp = proposal_service.BatchUnarchiveProposalsResponse()
            pb_resp = proposal_service.BatchUnarchiveProposalsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_unarchive_proposals(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_unarchive_proposals_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        proposal_service.BatchUnarchiveProposalsResponse.to_json(
                            response
                        )
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.ProposalServiceClient.batch_unarchive_proposals",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ProposalService",
                        "rpcName": "BatchUnarchiveProposals",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchUpdateProposals(
        _BaseProposalServiceRestTransport._BaseBatchUpdateProposals,
        ProposalServiceRestStub,
    ):
        def __hash__(self):
            return hash("ProposalServiceRestTransport.BatchUpdateProposals")

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
            request: proposal_service.BatchUpdateProposalsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> proposal_service.BatchUpdateProposalsResponse:
            r"""Call the batch update proposals method over HTTP.

            Args:
                request (~.proposal_service.BatchUpdateProposalsRequest):
                    The request object. Request object for ``BatchUpdateProposals`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.proposal_service.BatchUpdateProposalsResponse:
                    Response object for ``BatchUpdateProposals`` method.
            """

            http_options = _BaseProposalServiceRestTransport._BaseBatchUpdateProposals._get_http_options()
            request, metadata = self._interceptor.pre_batch_update_proposals(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProposalServiceRestTransport._BaseBatchUpdateProposals,
                    "_BaseBatchUpdateProposals__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ProposalServiceClient.BatchUpdateProposals",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ProposalService",
                        "rpcName": "BatchUpdateProposals",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProposalServiceRestTransport._BatchUpdateProposals._get_response(
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
            resp = proposal_service.BatchUpdateProposalsResponse()
            pb_resp = proposal_service.BatchUpdateProposalsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_update_proposals(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_update_proposals_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        proposal_service.BatchUpdateProposalsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.ProposalServiceClient.batch_update_proposals",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ProposalService",
                        "rpcName": "BatchUpdateProposals",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateProposal(
        _BaseProposalServiceRestTransport._BaseCreateProposal, ProposalServiceRestStub
    ):
        def __hash__(self):
            return hash("ProposalServiceRestTransport.CreateProposal")

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
            request: proposal_service.CreateProposalRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> proposal_messages.Proposal:
            r"""Call the create proposal method over HTTP.

            Args:
                request (~.proposal_service.CreateProposalRequest):
                    The request object. Request object for ``CreateProposal`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.proposal_messages.Proposal:
                    A Proposal represents an agreement
                between an interactive advertising
                seller and a buyer that specifies the
                details of an advertising campaign.

            """

            http_options = _BaseProposalServiceRestTransport._BaseCreateProposal._get_http_options()
            request, metadata = self._interceptor.pre_create_proposal(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProposalServiceRestTransport._BaseCreateProposal,
                    "_BaseCreateProposal__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ProposalServiceClient.CreateProposal",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ProposalService",
                        "rpcName": "CreateProposal",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProposalServiceRestTransport._CreateProposal._get_response(
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
            resp = proposal_messages.Proposal()
            pb_resp = proposal_messages.Proposal.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_proposal(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_proposal_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = proposal_messages.Proposal.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.ProposalServiceClient.create_proposal",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ProposalService",
                        "rpcName": "CreateProposal",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FetchMarketplaceComments(
        _BaseProposalServiceRestTransport._BaseFetchMarketplaceComments,
        ProposalServiceRestStub,
    ):
        def __hash__(self):
            return hash("ProposalServiceRestTransport.FetchMarketplaceComments")

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
            request: proposal_service.FetchMarketplaceCommentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> proposal_service.FetchMarketplaceCommentsResponse:
            r"""Call the fetch marketplace
            comments method over HTTP.

                Args:
                    request (~.proposal_service.FetchMarketplaceCommentsRequest):
                        The request object. Request message for ``FetchMarketplaceComments`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.proposal_service.FetchMarketplaceCommentsResponse:
                        Response message for ``FetchMarketplaceComments``
                    method.

            """

            http_options = _BaseProposalServiceRestTransport._BaseFetchMarketplaceComments._get_http_options()
            request, metadata = self._interceptor.pre_fetch_marketplace_comments(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProposalServiceRestTransport._BaseFetchMarketplaceComments,
                    "_BaseFetchMarketplaceComments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ProposalServiceClient.FetchMarketplaceComments",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ProposalService",
                        "rpcName": "FetchMarketplaceComments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ProposalServiceRestTransport._FetchMarketplaceComments._get_response(
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
            resp = proposal_service.FetchMarketplaceCommentsResponse()
            pb_resp = proposal_service.FetchMarketplaceCommentsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_fetch_marketplace_comments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_fetch_marketplace_comments_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        proposal_service.FetchMarketplaceCommentsResponse.to_json(
                            response
                        )
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.ProposalServiceClient.fetch_marketplace_comments",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ProposalService",
                        "rpcName": "FetchMarketplaceComments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetProposal(
        _BaseProposalServiceRestTransport._BaseGetProposal, ProposalServiceRestStub
    ):
        def __hash__(self):
            return hash("ProposalServiceRestTransport.GetProposal")

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
            request: proposal_service.GetProposalRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> proposal_messages.Proposal:
            r"""Call the get proposal method over HTTP.

            Args:
                request (~.proposal_service.GetProposalRequest):
                    The request object. Request object for ``GetProposal`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.proposal_messages.Proposal:
                    A Proposal represents an agreement
                between an interactive advertising
                seller and a buyer that specifies the
                details of an advertising campaign.

            """

            http_options = (
                _BaseProposalServiceRestTransport._BaseGetProposal._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_proposal(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProposalServiceRestTransport._BaseGetProposal,
                    "_BaseGetProposal__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ProposalServiceClient.GetProposal",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ProposalService",
                        "rpcName": "GetProposal",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProposalServiceRestTransport._GetProposal._get_response(
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
            resp = proposal_messages.Proposal()
            pb_resp = proposal_messages.Proposal.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_proposal(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_proposal_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = proposal_messages.Proposal.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.ProposalServiceClient.get_proposal",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ProposalService",
                        "rpcName": "GetProposal",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListProposals(
        _BaseProposalServiceRestTransport._BaseListProposals, ProposalServiceRestStub
    ):
        def __hash__(self):
            return hash("ProposalServiceRestTransport.ListProposals")

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
            request: proposal_service.ListProposalsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> proposal_service.ListProposalsResponse:
            r"""Call the list proposals method over HTTP.

            Args:
                request (~.proposal_service.ListProposalsRequest):
                    The request object. Request object for ``ListProposals`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.proposal_service.ListProposalsResponse:
                    Response object for ``ListProposalsRequest`` containing
                matching ``Proposal`` objects.

            """

            http_options = (
                _BaseProposalServiceRestTransport._BaseListProposals._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_proposals(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProposalServiceRestTransport._BaseListProposals,
                    "_BaseListProposals__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ProposalServiceClient.ListProposals",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ProposalService",
                        "rpcName": "ListProposals",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProposalServiceRestTransport._ListProposals._get_response(
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
            resp = proposal_service.ListProposalsResponse()
            pb_resp = proposal_service.ListProposalsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_proposals(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_proposals_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = proposal_service.ListProposalsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.ProposalServiceClient.list_proposals",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ProposalService",
                        "rpcName": "ListProposals",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateProposal(
        _BaseProposalServiceRestTransport._BaseUpdateProposal, ProposalServiceRestStub
    ):
        def __hash__(self):
            return hash("ProposalServiceRestTransport.UpdateProposal")

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
            request: proposal_service.UpdateProposalRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> proposal_messages.Proposal:
            r"""Call the update proposal method over HTTP.

            Args:
                request (~.proposal_service.UpdateProposalRequest):
                    The request object. Request object for ``UpdateProposal`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.proposal_messages.Proposal:
                    A Proposal represents an agreement
                between an interactive advertising
                seller and a buyer that specifies the
                details of an advertising campaign.

            """

            http_options = _BaseProposalServiceRestTransport._BaseUpdateProposal._get_http_options()
            request, metadata = self._interceptor.pre_update_proposal(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProposalServiceRestTransport._BaseUpdateProposal,
                    "_BaseUpdateProposal__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ProposalServiceClient.UpdateProposal",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ProposalService",
                        "rpcName": "UpdateProposal",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProposalServiceRestTransport._UpdateProposal._get_response(
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
            resp = proposal_messages.Proposal()
            pb_resp = proposal_messages.Proposal.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_proposal(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_proposal_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = proposal_messages.Proposal.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.ProposalServiceClient.update_proposal",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ProposalService",
                        "rpcName": "UpdateProposal",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_archive_proposals(
        self,
    ) -> Callable[
        [proposal_service.BatchArchiveProposalsRequest],
        proposal_service.BatchArchiveProposalsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchArchiveProposals(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_create_proposals(
        self,
    ) -> Callable[
        [proposal_service.BatchCreateProposalsRequest],
        proposal_service.BatchCreateProposalsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchCreateProposals(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_discard_draft_proposals(
        self,
    ) -> Callable[
        [proposal_service.BatchDiscardDraftProposalsRequest],
        proposal_service.BatchDiscardDraftProposalsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchDiscardDraftProposals(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_pause_proposals(
        self,
    ) -> Callable[
        [proposal_service.BatchPauseProposalsRequest],
        proposal_service.BatchPauseProposalsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchPauseProposals(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_push_to_order_proposals(
        self,
    ) -> Callable[
        [proposal_service.BatchPushToOrderProposalsRequest],
        proposal_service.BatchPushToOrderProposalsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchPushToOrderProposals(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_redraft_proposals(
        self,
    ) -> Callable[
        [proposal_service.BatchRedraftProposalsRequest],
        proposal_service.BatchRedraftProposalsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchRedraftProposals(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_request_buyer_accept_proposals(
        self,
    ) -> Callable[
        [proposal_service.BatchRequestBuyerAcceptProposalsRequest],
        proposal_service.BatchRequestBuyerAcceptProposalsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchRequestBuyerAcceptProposals(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_request_buyer_review_proposals(
        self,
    ) -> Callable[
        [proposal_service.BatchRequestBuyerReviewProposalsRequest],
        proposal_service.BatchRequestBuyerReviewProposalsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchRequestBuyerReviewProposals(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_reserve_proposals(
        self,
    ) -> Callable[
        [proposal_service.BatchReserveProposalsRequest],
        proposal_service.BatchReserveProposalsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchReserveProposals(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_resume_proposals(
        self,
    ) -> Callable[
        [proposal_service.BatchResumeProposalsRequest],
        proposal_service.BatchResumeProposalsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchResumeProposals(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_terminate_proposals(
        self,
    ) -> Callable[
        [proposal_service.BatchTerminateProposalsRequest],
        proposal_service.BatchTerminateProposalsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchTerminateProposals(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_unarchive_proposals(
        self,
    ) -> Callable[
        [proposal_service.BatchUnarchiveProposalsRequest],
        proposal_service.BatchUnarchiveProposalsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchUnarchiveProposals(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_update_proposals(
        self,
    ) -> Callable[
        [proposal_service.BatchUpdateProposalsRequest],
        proposal_service.BatchUpdateProposalsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchUpdateProposals(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_proposal(
        self,
    ) -> Callable[[proposal_service.CreateProposalRequest], proposal_messages.Proposal]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateProposal(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def fetch_marketplace_comments(
        self,
    ) -> Callable[
        [proposal_service.FetchMarketplaceCommentsRequest],
        proposal_service.FetchMarketplaceCommentsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchMarketplaceComments(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_proposal(
        self,
    ) -> Callable[[proposal_service.GetProposalRequest], proposal_messages.Proposal]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetProposal(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_proposals(
        self,
    ) -> Callable[
        [proposal_service.ListProposalsRequest], proposal_service.ListProposalsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListProposals(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_proposal(
        self,
    ) -> Callable[[proposal_service.UpdateProposalRequest], proposal_messages.Proposal]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateProposal(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseProposalServiceRestTransport._BaseCancelOperation, ProposalServiceRestStub
    ):
        def __hash__(self):
            return hash("ProposalServiceRestTransport.CancelOperation")

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
            request: operations_pb2.CancelOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> None:
            r"""Call the cancel operation method over HTTP.

            Args:
                request (operations_pb2.CancelOperationRequest):
                    The request object for CancelOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseProposalServiceRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProposalServiceRestTransport._BaseCancelOperation,
                    "_BaseCancelOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ProposalServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ProposalService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProposalServiceRestTransport._CancelOperation._get_response(
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

            return self._interceptor.post_cancel_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseProposalServiceRestTransport._BaseGetOperation, ProposalServiceRestStub
    ):
        def __hash__(self):
            return hash("ProposalServiceRestTransport.GetOperation")

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
            request: operations_pb2.GetOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the get operation method over HTTP.

            Args:
                request (operations_pb2.GetOperationRequest):
                    The request object for GetOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                operations_pb2.Operation: Response from GetOperation method.
            """

            http_options = (
                _BaseProposalServiceRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProposalServiceRestTransport._BaseGetOperation,
                    "_BaseGetOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ProposalServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ProposalService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProposalServiceRestTransport._GetOperation._get_response(
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
            resp = operations_pb2.Operation()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_operation(resp)
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
                    "Received response for google.ads.admanager_v1.ProposalServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ProposalService",
                        "rpcName": "GetOperation",
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


__all__ = ("ProposalServiceRestTransport",)
