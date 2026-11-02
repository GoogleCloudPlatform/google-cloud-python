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
from google.ads.admanager_v1.types import (
    child_publisher_messages,
    child_publisher_service,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseChildPublisherServiceRestTransport

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


class ChildPublisherServiceRestInterceptor:
    """Interceptor for ChildPublisherService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the ChildPublisherServiceRestTransport.

    .. code-block:: python
        class MyCustomChildPublisherServiceInterceptor(ChildPublisherServiceRestInterceptor):
            def pre_batch_create_child_publishers(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_create_child_publishers(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_reject_child_publishers(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_reject_child_publishers(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_renegotiate_child_publisher_agreements(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_renegotiate_child_publisher_agreements(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_resend_child_publisher_invitation_emails(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_resend_child_publisher_invitation_emails(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_update_child_publishers(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_update_child_publishers(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_withdraw_child_publishers(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_withdraw_child_publishers(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_child_publisher(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_child_publisher(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_child_publisher(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_child_publisher(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_child_publishers(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_child_publishers(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_child_publisher(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_child_publisher(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = ChildPublisherServiceRestTransport(interceptor=MyCustomChildPublisherServiceInterceptor())
        client = ChildPublisherServiceClient(transport=transport)


    """

    def pre_batch_create_child_publishers(
        self,
        request: child_publisher_service.BatchCreateChildPublishersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        child_publisher_service.BatchCreateChildPublishersRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_create_child_publishers

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ChildPublisherService server.
        """
        return request, metadata

    def post_batch_create_child_publishers(
        self, response: child_publisher_service.BatchCreateChildPublishersResponse
    ) -> child_publisher_service.BatchCreateChildPublishersResponse:
        """Post-rpc interceptor for batch_create_child_publishers

        DEPRECATED. Please use the `post_batch_create_child_publishers_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ChildPublisherService server but before
        it is returned to user code. This `post_batch_create_child_publishers` interceptor runs
        before the `post_batch_create_child_publishers_with_metadata` interceptor.
        """
        return response

    def post_batch_create_child_publishers_with_metadata(
        self,
        response: child_publisher_service.BatchCreateChildPublishersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        child_publisher_service.BatchCreateChildPublishersResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_create_child_publishers

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ChildPublisherService server but before it is returned to user code.

        We recommend only using this `post_batch_create_child_publishers_with_metadata`
        interceptor in new development instead of the `post_batch_create_child_publishers` interceptor.
        When both interceptors are used, this `post_batch_create_child_publishers_with_metadata` interceptor runs after the
        `post_batch_create_child_publishers` interceptor. The (possibly modified) response returned by
        `post_batch_create_child_publishers` will be passed to
        `post_batch_create_child_publishers_with_metadata`.
        """
        return response, metadata

    def pre_batch_reject_child_publishers(
        self,
        request: child_publisher_service.BatchRejectChildPublishersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        child_publisher_service.BatchRejectChildPublishersRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_reject_child_publishers

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ChildPublisherService server.
        """
        return request, metadata

    def post_batch_reject_child_publishers(
        self, response: child_publisher_service.BatchRejectChildPublishersResponse
    ) -> child_publisher_service.BatchRejectChildPublishersResponse:
        """Post-rpc interceptor for batch_reject_child_publishers

        DEPRECATED. Please use the `post_batch_reject_child_publishers_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ChildPublisherService server but before
        it is returned to user code. This `post_batch_reject_child_publishers` interceptor runs
        before the `post_batch_reject_child_publishers_with_metadata` interceptor.
        """
        return response

    def post_batch_reject_child_publishers_with_metadata(
        self,
        response: child_publisher_service.BatchRejectChildPublishersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        child_publisher_service.BatchRejectChildPublishersResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_reject_child_publishers

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ChildPublisherService server but before it is returned to user code.

        We recommend only using this `post_batch_reject_child_publishers_with_metadata`
        interceptor in new development instead of the `post_batch_reject_child_publishers` interceptor.
        When both interceptors are used, this `post_batch_reject_child_publishers_with_metadata` interceptor runs after the
        `post_batch_reject_child_publishers` interceptor. The (possibly modified) response returned by
        `post_batch_reject_child_publishers` will be passed to
        `post_batch_reject_child_publishers_with_metadata`.
        """
        return response, metadata

    def pre_batch_renegotiate_child_publisher_agreements(
        self,
        request: child_publisher_service.BatchRenegotiateChildPublisherAgreementsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        child_publisher_service.BatchRenegotiateChildPublisherAgreementsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_renegotiate_child_publisher_agreements

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ChildPublisherService server.
        """
        return request, metadata

    def post_batch_renegotiate_child_publisher_agreements(
        self,
        response: child_publisher_service.BatchRenegotiateChildPublisherAgreementsResponse,
    ) -> child_publisher_service.BatchRenegotiateChildPublisherAgreementsResponse:
        """Post-rpc interceptor for batch_renegotiate_child_publisher_agreements

        DEPRECATED. Please use the `post_batch_renegotiate_child_publisher_agreements_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ChildPublisherService server but before
        it is returned to user code. This `post_batch_renegotiate_child_publisher_agreements` interceptor runs
        before the `post_batch_renegotiate_child_publisher_agreements_with_metadata` interceptor.
        """
        return response

    def post_batch_renegotiate_child_publisher_agreements_with_metadata(
        self,
        response: child_publisher_service.BatchRenegotiateChildPublisherAgreementsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        child_publisher_service.BatchRenegotiateChildPublisherAgreementsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_renegotiate_child_publisher_agreements

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ChildPublisherService server but before it is returned to user code.

        We recommend only using this `post_batch_renegotiate_child_publisher_agreements_with_metadata`
        interceptor in new development instead of the `post_batch_renegotiate_child_publisher_agreements` interceptor.
        When both interceptors are used, this `post_batch_renegotiate_child_publisher_agreements_with_metadata` interceptor runs after the
        `post_batch_renegotiate_child_publisher_agreements` interceptor. The (possibly modified) response returned by
        `post_batch_renegotiate_child_publisher_agreements` will be passed to
        `post_batch_renegotiate_child_publisher_agreements_with_metadata`.
        """
        return response, metadata

    def pre_batch_resend_child_publisher_invitation_emails(
        self,
        request: child_publisher_service.BatchResendChildPublisherInvitationEmailsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        child_publisher_service.BatchResendChildPublisherInvitationEmailsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_resend_child_publisher_invitation_emails

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ChildPublisherService server.
        """
        return request, metadata

    def post_batch_resend_child_publisher_invitation_emails(
        self,
        response: child_publisher_service.BatchResendChildPublisherInvitationEmailsResponse,
    ) -> child_publisher_service.BatchResendChildPublisherInvitationEmailsResponse:
        """Post-rpc interceptor for batch_resend_child_publisher_invitation_emails

        DEPRECATED. Please use the `post_batch_resend_child_publisher_invitation_emails_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ChildPublisherService server but before
        it is returned to user code. This `post_batch_resend_child_publisher_invitation_emails` interceptor runs
        before the `post_batch_resend_child_publisher_invitation_emails_with_metadata` interceptor.
        """
        return response

    def post_batch_resend_child_publisher_invitation_emails_with_metadata(
        self,
        response: child_publisher_service.BatchResendChildPublisherInvitationEmailsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        child_publisher_service.BatchResendChildPublisherInvitationEmailsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_resend_child_publisher_invitation_emails

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ChildPublisherService server but before it is returned to user code.

        We recommend only using this `post_batch_resend_child_publisher_invitation_emails_with_metadata`
        interceptor in new development instead of the `post_batch_resend_child_publisher_invitation_emails` interceptor.
        When both interceptors are used, this `post_batch_resend_child_publisher_invitation_emails_with_metadata` interceptor runs after the
        `post_batch_resend_child_publisher_invitation_emails` interceptor. The (possibly modified) response returned by
        `post_batch_resend_child_publisher_invitation_emails` will be passed to
        `post_batch_resend_child_publisher_invitation_emails_with_metadata`.
        """
        return response, metadata

    def pre_batch_update_child_publishers(
        self,
        request: child_publisher_service.BatchUpdateChildPublishersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        child_publisher_service.BatchUpdateChildPublishersRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_update_child_publishers

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ChildPublisherService server.
        """
        return request, metadata

    def post_batch_update_child_publishers(
        self, response: child_publisher_service.BatchUpdateChildPublishersResponse
    ) -> child_publisher_service.BatchUpdateChildPublishersResponse:
        """Post-rpc interceptor for batch_update_child_publishers

        DEPRECATED. Please use the `post_batch_update_child_publishers_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ChildPublisherService server but before
        it is returned to user code. This `post_batch_update_child_publishers` interceptor runs
        before the `post_batch_update_child_publishers_with_metadata` interceptor.
        """
        return response

    def post_batch_update_child_publishers_with_metadata(
        self,
        response: child_publisher_service.BatchUpdateChildPublishersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        child_publisher_service.BatchUpdateChildPublishersResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_update_child_publishers

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ChildPublisherService server but before it is returned to user code.

        We recommend only using this `post_batch_update_child_publishers_with_metadata`
        interceptor in new development instead of the `post_batch_update_child_publishers` interceptor.
        When both interceptors are used, this `post_batch_update_child_publishers_with_metadata` interceptor runs after the
        `post_batch_update_child_publishers` interceptor. The (possibly modified) response returned by
        `post_batch_update_child_publishers` will be passed to
        `post_batch_update_child_publishers_with_metadata`.
        """
        return response, metadata

    def pre_batch_withdraw_child_publishers(
        self,
        request: child_publisher_service.BatchWithdrawChildPublishersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        child_publisher_service.BatchWithdrawChildPublishersRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_withdraw_child_publishers

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ChildPublisherService server.
        """
        return request, metadata

    def post_batch_withdraw_child_publishers(
        self, response: child_publisher_service.BatchWithdrawChildPublishersResponse
    ) -> child_publisher_service.BatchWithdrawChildPublishersResponse:
        """Post-rpc interceptor for batch_withdraw_child_publishers

        DEPRECATED. Please use the `post_batch_withdraw_child_publishers_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ChildPublisherService server but before
        it is returned to user code. This `post_batch_withdraw_child_publishers` interceptor runs
        before the `post_batch_withdraw_child_publishers_with_metadata` interceptor.
        """
        return response

    def post_batch_withdraw_child_publishers_with_metadata(
        self,
        response: child_publisher_service.BatchWithdrawChildPublishersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        child_publisher_service.BatchWithdrawChildPublishersResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_withdraw_child_publishers

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ChildPublisherService server but before it is returned to user code.

        We recommend only using this `post_batch_withdraw_child_publishers_with_metadata`
        interceptor in new development instead of the `post_batch_withdraw_child_publishers` interceptor.
        When both interceptors are used, this `post_batch_withdraw_child_publishers_with_metadata` interceptor runs after the
        `post_batch_withdraw_child_publishers` interceptor. The (possibly modified) response returned by
        `post_batch_withdraw_child_publishers` will be passed to
        `post_batch_withdraw_child_publishers_with_metadata`.
        """
        return response, metadata

    def pre_create_child_publisher(
        self,
        request: child_publisher_service.CreateChildPublisherRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        child_publisher_service.CreateChildPublisherRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_child_publisher

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ChildPublisherService server.
        """
        return request, metadata

    def post_create_child_publisher(
        self, response: child_publisher_messages.ChildPublisher
    ) -> child_publisher_messages.ChildPublisher:
        """Post-rpc interceptor for create_child_publisher

        DEPRECATED. Please use the `post_create_child_publisher_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ChildPublisherService server but before
        it is returned to user code. This `post_create_child_publisher` interceptor runs
        before the `post_create_child_publisher_with_metadata` interceptor.
        """
        return response

    def post_create_child_publisher_with_metadata(
        self,
        response: child_publisher_messages.ChildPublisher,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        child_publisher_messages.ChildPublisher, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for create_child_publisher

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ChildPublisherService server but before it is returned to user code.

        We recommend only using this `post_create_child_publisher_with_metadata`
        interceptor in new development instead of the `post_create_child_publisher` interceptor.
        When both interceptors are used, this `post_create_child_publisher_with_metadata` interceptor runs after the
        `post_create_child_publisher` interceptor. The (possibly modified) response returned by
        `post_create_child_publisher` will be passed to
        `post_create_child_publisher_with_metadata`.
        """
        return response, metadata

    def pre_get_child_publisher(
        self,
        request: child_publisher_service.GetChildPublisherRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        child_publisher_service.GetChildPublisherRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_child_publisher

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ChildPublisherService server.
        """
        return request, metadata

    def post_get_child_publisher(
        self, response: child_publisher_messages.ChildPublisher
    ) -> child_publisher_messages.ChildPublisher:
        """Post-rpc interceptor for get_child_publisher

        DEPRECATED. Please use the `post_get_child_publisher_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ChildPublisherService server but before
        it is returned to user code. This `post_get_child_publisher` interceptor runs
        before the `post_get_child_publisher_with_metadata` interceptor.
        """
        return response

    def post_get_child_publisher_with_metadata(
        self,
        response: child_publisher_messages.ChildPublisher,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        child_publisher_messages.ChildPublisher, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_child_publisher

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ChildPublisherService server but before it is returned to user code.

        We recommend only using this `post_get_child_publisher_with_metadata`
        interceptor in new development instead of the `post_get_child_publisher` interceptor.
        When both interceptors are used, this `post_get_child_publisher_with_metadata` interceptor runs after the
        `post_get_child_publisher` interceptor. The (possibly modified) response returned by
        `post_get_child_publisher` will be passed to
        `post_get_child_publisher_with_metadata`.
        """
        return response, metadata

    def pre_list_child_publishers(
        self,
        request: child_publisher_service.ListChildPublishersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        child_publisher_service.ListChildPublishersRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_child_publishers

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ChildPublisherService server.
        """
        return request, metadata

    def post_list_child_publishers(
        self, response: child_publisher_service.ListChildPublishersResponse
    ) -> child_publisher_service.ListChildPublishersResponse:
        """Post-rpc interceptor for list_child_publishers

        DEPRECATED. Please use the `post_list_child_publishers_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ChildPublisherService server but before
        it is returned to user code. This `post_list_child_publishers` interceptor runs
        before the `post_list_child_publishers_with_metadata` interceptor.
        """
        return response

    def post_list_child_publishers_with_metadata(
        self,
        response: child_publisher_service.ListChildPublishersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        child_publisher_service.ListChildPublishersResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_child_publishers

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ChildPublisherService server but before it is returned to user code.

        We recommend only using this `post_list_child_publishers_with_metadata`
        interceptor in new development instead of the `post_list_child_publishers` interceptor.
        When both interceptors are used, this `post_list_child_publishers_with_metadata` interceptor runs after the
        `post_list_child_publishers` interceptor. The (possibly modified) response returned by
        `post_list_child_publishers` will be passed to
        `post_list_child_publishers_with_metadata`.
        """
        return response, metadata

    def pre_update_child_publisher(
        self,
        request: child_publisher_service.UpdateChildPublisherRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        child_publisher_service.UpdateChildPublisherRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_child_publisher

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ChildPublisherService server.
        """
        return request, metadata

    def post_update_child_publisher(
        self, response: child_publisher_messages.ChildPublisher
    ) -> child_publisher_messages.ChildPublisher:
        """Post-rpc interceptor for update_child_publisher

        DEPRECATED. Please use the `post_update_child_publisher_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ChildPublisherService server but before
        it is returned to user code. This `post_update_child_publisher` interceptor runs
        before the `post_update_child_publisher_with_metadata` interceptor.
        """
        return response

    def post_update_child_publisher_with_metadata(
        self,
        response: child_publisher_messages.ChildPublisher,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        child_publisher_messages.ChildPublisher, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for update_child_publisher

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ChildPublisherService server but before it is returned to user code.

        We recommend only using this `post_update_child_publisher_with_metadata`
        interceptor in new development instead of the `post_update_child_publisher` interceptor.
        When both interceptors are used, this `post_update_child_publisher_with_metadata` interceptor runs after the
        `post_update_child_publisher` interceptor. The (possibly modified) response returned by
        `post_update_child_publisher` will be passed to
        `post_update_child_publisher_with_metadata`.
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
        before they are sent to the ChildPublisherService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the ChildPublisherService server but before
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
        before they are sent to the ChildPublisherService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the ChildPublisherService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class ChildPublisherServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: ChildPublisherServiceRestInterceptor


class ChildPublisherServiceRestTransport(_BaseChildPublisherServiceRestTransport):
    """REST backend synchronous transport for ChildPublisherService.

    Provides methods for handling
    [ChildPublisher][google.ads.admanager.v1.ChildPublisher] objects.

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
        interceptor: Optional[ChildPublisherServiceRestInterceptor] = None,
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
            interceptor (Optional[ChildPublisherServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or ChildPublisherServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _BatchCreateChildPublishers(
        _BaseChildPublisherServiceRestTransport._BaseBatchCreateChildPublishers,
        ChildPublisherServiceRestStub,
    ):
        def __hash__(self):
            return hash("ChildPublisherServiceRestTransport.BatchCreateChildPublishers")

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
            request: child_publisher_service.BatchCreateChildPublishersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> child_publisher_service.BatchCreateChildPublishersResponse:
            r"""Call the batch create child
            publishers method over HTTP.

                Args:
                    request (~.child_publisher_service.BatchCreateChildPublishersRequest):
                        The request object. Request object for ``BatchCreateChildPublishers``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.child_publisher_service.BatchCreateChildPublishersResponse:
                        Response object for ``BatchCreateChildPublishers``
                    method.

            """

            http_options = _BaseChildPublisherServiceRestTransport._BaseBatchCreateChildPublishers._get_http_options()
            request, metadata = self._interceptor.pre_batch_create_child_publishers(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseChildPublisherServiceRestTransport._BaseBatchCreateChildPublishers,
                    "_BaseBatchCreateChildPublishers__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ChildPublisherServiceClient.BatchCreateChildPublishers",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ChildPublisherService",
                        "rpcName": "BatchCreateChildPublishers",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ChildPublisherServiceRestTransport._BatchCreateChildPublishers._get_response(
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
            resp = child_publisher_service.BatchCreateChildPublishersResponse()
            pb_resp = child_publisher_service.BatchCreateChildPublishersResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_create_child_publishers(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_create_child_publishers_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = child_publisher_service.BatchCreateChildPublishersResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.ChildPublisherServiceClient.batch_create_child_publishers",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ChildPublisherService",
                        "rpcName": "BatchCreateChildPublishers",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchRejectChildPublishers(
        _BaseChildPublisherServiceRestTransport._BaseBatchRejectChildPublishers,
        ChildPublisherServiceRestStub,
    ):
        def __hash__(self):
            return hash("ChildPublisherServiceRestTransport.BatchRejectChildPublishers")

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
            request: child_publisher_service.BatchRejectChildPublishersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> child_publisher_service.BatchRejectChildPublishersResponse:
            r"""Call the batch reject child
            publishers method over HTTP.

                Args:
                    request (~.child_publisher_service.BatchRejectChildPublishersRequest):
                        The request object. Request message for ``BatchRejectChildPublishers``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.child_publisher_service.BatchRejectChildPublishersResponse:
                        Response message for ``BatchRejectChildPublishers``
                    method.

            """

            http_options = _BaseChildPublisherServiceRestTransport._BaseBatchRejectChildPublishers._get_http_options()
            request, metadata = self._interceptor.pre_batch_reject_child_publishers(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseChildPublisherServiceRestTransport._BaseBatchRejectChildPublishers,
                    "_BaseBatchRejectChildPublishers__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ChildPublisherServiceClient.BatchRejectChildPublishers",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ChildPublisherService",
                        "rpcName": "BatchRejectChildPublishers",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ChildPublisherServiceRestTransport._BatchRejectChildPublishers._get_response(
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
            resp = child_publisher_service.BatchRejectChildPublishersResponse()
            pb_resp = child_publisher_service.BatchRejectChildPublishersResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_reject_child_publishers(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_reject_child_publishers_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = child_publisher_service.BatchRejectChildPublishersResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.ChildPublisherServiceClient.batch_reject_child_publishers",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ChildPublisherService",
                        "rpcName": "BatchRejectChildPublishers",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchRenegotiateChildPublisherAgreements(
        _BaseChildPublisherServiceRestTransport._BaseBatchRenegotiateChildPublisherAgreements,
        ChildPublisherServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "ChildPublisherServiceRestTransport.BatchRenegotiateChildPublisherAgreements"
            )

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
            request: child_publisher_service.BatchRenegotiateChildPublisherAgreementsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> child_publisher_service.BatchRenegotiateChildPublisherAgreementsResponse:
            r"""Call the batch renegotiate child
            publisher agreements method over HTTP.

                Args:
                    request (~.child_publisher_service.BatchRenegotiateChildPublisherAgreementsRequest):
                        The request object. Request message for
                    ``BatchRenegotiateChildPublisherAgreements`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.child_publisher_service.BatchRenegotiateChildPublisherAgreementsResponse:
                        Response message for
                    ``BatchRenegotiateChildPublisherAgreements`` method.

            """

            http_options = _BaseChildPublisherServiceRestTransport._BaseBatchRenegotiateChildPublisherAgreements._get_http_options()
            request, metadata = (
                self._interceptor.pre_batch_renegotiate_child_publisher_agreements(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseChildPublisherServiceRestTransport._BaseBatchRenegotiateChildPublisherAgreements,
                    "_BaseBatchRenegotiateChildPublisherAgreements__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ChildPublisherServiceClient.BatchRenegotiateChildPublisherAgreements",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ChildPublisherService",
                        "rpcName": "BatchRenegotiateChildPublisherAgreements",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ChildPublisherServiceRestTransport._BatchRenegotiateChildPublisherAgreements._get_response(
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
            resp = child_publisher_service.BatchRenegotiateChildPublisherAgreementsResponse()
            pb_resp = child_publisher_service.BatchRenegotiateChildPublisherAgreementsResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_renegotiate_child_publisher_agreements(
                resp
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_renegotiate_child_publisher_agreements_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = child_publisher_service.BatchRenegotiateChildPublisherAgreementsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.ChildPublisherServiceClient.batch_renegotiate_child_publisher_agreements",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ChildPublisherService",
                        "rpcName": "BatchRenegotiateChildPublisherAgreements",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchResendChildPublisherInvitationEmails(
        _BaseChildPublisherServiceRestTransport._BaseBatchResendChildPublisherInvitationEmails,
        ChildPublisherServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "ChildPublisherServiceRestTransport.BatchResendChildPublisherInvitationEmails"
            )

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
            request: child_publisher_service.BatchResendChildPublisherInvitationEmailsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> child_publisher_service.BatchResendChildPublisherInvitationEmailsResponse:
            r"""Call the batch resend child
            publisher invitation emails method over HTTP.

                Args:
                    request (~.child_publisher_service.BatchResendChildPublisherInvitationEmailsRequest):
                        The request object. Request message for
                    ``BatchResendChildPublisherInvitationEmails`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.child_publisher_service.BatchResendChildPublisherInvitationEmailsResponse:
                        Response message for
                    ``BatchResendChildPublisherInvitationEmails`` method.

            """

            http_options = _BaseChildPublisherServiceRestTransport._BaseBatchResendChildPublisherInvitationEmails._get_http_options()
            request, metadata = (
                self._interceptor.pre_batch_resend_child_publisher_invitation_emails(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseChildPublisherServiceRestTransport._BaseBatchResendChildPublisherInvitationEmails,
                    "_BaseBatchResendChildPublisherInvitationEmails__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ChildPublisherServiceClient.BatchResendChildPublisherInvitationEmails",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ChildPublisherService",
                        "rpcName": "BatchResendChildPublisherInvitationEmails",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ChildPublisherServiceRestTransport._BatchResendChildPublisherInvitationEmails._get_response(
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
            resp = child_publisher_service.BatchResendChildPublisherInvitationEmailsResponse()
            pb_resp = child_publisher_service.BatchResendChildPublisherInvitationEmailsResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = (
                self._interceptor.post_batch_resend_child_publisher_invitation_emails(
                    resp
                )
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_resend_child_publisher_invitation_emails_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = child_publisher_service.BatchResendChildPublisherInvitationEmailsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.ChildPublisherServiceClient.batch_resend_child_publisher_invitation_emails",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ChildPublisherService",
                        "rpcName": "BatchResendChildPublisherInvitationEmails",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchUpdateChildPublishers(
        _BaseChildPublisherServiceRestTransport._BaseBatchUpdateChildPublishers,
        ChildPublisherServiceRestStub,
    ):
        def __hash__(self):
            return hash("ChildPublisherServiceRestTransport.BatchUpdateChildPublishers")

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
            request: child_publisher_service.BatchUpdateChildPublishersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> child_publisher_service.BatchUpdateChildPublishersResponse:
            r"""Call the batch update child
            publishers method over HTTP.

                Args:
                    request (~.child_publisher_service.BatchUpdateChildPublishersRequest):
                        The request object. Request object for ``BatchUpdateChildPublishers``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.child_publisher_service.BatchUpdateChildPublishersResponse:
                        Response object for ``BatchUpdateChildPublishers``
                    method.

            """

            http_options = _BaseChildPublisherServiceRestTransport._BaseBatchUpdateChildPublishers._get_http_options()
            request, metadata = self._interceptor.pre_batch_update_child_publishers(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseChildPublisherServiceRestTransport._BaseBatchUpdateChildPublishers,
                    "_BaseBatchUpdateChildPublishers__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ChildPublisherServiceClient.BatchUpdateChildPublishers",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ChildPublisherService",
                        "rpcName": "BatchUpdateChildPublishers",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ChildPublisherServiceRestTransport._BatchUpdateChildPublishers._get_response(
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
            resp = child_publisher_service.BatchUpdateChildPublishersResponse()
            pb_resp = child_publisher_service.BatchUpdateChildPublishersResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_update_child_publishers(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_update_child_publishers_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = child_publisher_service.BatchUpdateChildPublishersResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.ChildPublisherServiceClient.batch_update_child_publishers",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ChildPublisherService",
                        "rpcName": "BatchUpdateChildPublishers",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchWithdrawChildPublishers(
        _BaseChildPublisherServiceRestTransport._BaseBatchWithdrawChildPublishers,
        ChildPublisherServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "ChildPublisherServiceRestTransport.BatchWithdrawChildPublishers"
            )

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
            request: child_publisher_service.BatchWithdrawChildPublishersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> child_publisher_service.BatchWithdrawChildPublishersResponse:
            r"""Call the batch withdraw child
            publishers method over HTTP.

                Args:
                    request (~.child_publisher_service.BatchWithdrawChildPublishersRequest):
                        The request object. Request message for ``BatchWithdrawChildPublishers``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.child_publisher_service.BatchWithdrawChildPublishersResponse:
                        Response message for ``BatchWithdrawChildPublishers``
                    method.

            """

            http_options = _BaseChildPublisherServiceRestTransport._BaseBatchWithdrawChildPublishers._get_http_options()
            request, metadata = self._interceptor.pre_batch_withdraw_child_publishers(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseChildPublisherServiceRestTransport._BaseBatchWithdrawChildPublishers,
                    "_BaseBatchWithdrawChildPublishers__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ChildPublisherServiceClient.BatchWithdrawChildPublishers",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ChildPublisherService",
                        "rpcName": "BatchWithdrawChildPublishers",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ChildPublisherServiceRestTransport._BatchWithdrawChildPublishers._get_response(
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
            resp = child_publisher_service.BatchWithdrawChildPublishersResponse()
            pb_resp = child_publisher_service.BatchWithdrawChildPublishersResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_withdraw_child_publishers(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_withdraw_child_publishers_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = child_publisher_service.BatchWithdrawChildPublishersResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.ChildPublisherServiceClient.batch_withdraw_child_publishers",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ChildPublisherService",
                        "rpcName": "BatchWithdrawChildPublishers",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateChildPublisher(
        _BaseChildPublisherServiceRestTransport._BaseCreateChildPublisher,
        ChildPublisherServiceRestStub,
    ):
        def __hash__(self):
            return hash("ChildPublisherServiceRestTransport.CreateChildPublisher")

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
            request: child_publisher_service.CreateChildPublisherRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> child_publisher_messages.ChildPublisher:
            r"""Call the create child publisher method over HTTP.

            Args:
                request (~.child_publisher_service.CreateChildPublisherRequest):
                    The request object. Request object for ``CreateChildPublisher`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.child_publisher_messages.ChildPublisher:
                    The
                [ChildPublisher][google.ads.admanager.v1.ChildPublisher]
                resource.

            """

            http_options = _BaseChildPublisherServiceRestTransport._BaseCreateChildPublisher._get_http_options()
            request, metadata = self._interceptor.pre_create_child_publisher(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseChildPublisherServiceRestTransport._BaseCreateChildPublisher,
                    "_BaseCreateChildPublisher__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ChildPublisherServiceClient.CreateChildPublisher",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ChildPublisherService",
                        "rpcName": "CreateChildPublisher",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ChildPublisherServiceRestTransport._CreateChildPublisher._get_response(
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
            resp = child_publisher_messages.ChildPublisher()
            pb_resp = child_publisher_messages.ChildPublisher.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_child_publisher(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_child_publisher_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = child_publisher_messages.ChildPublisher.to_json(
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
                    "Received response for google.ads.admanager_v1.ChildPublisherServiceClient.create_child_publisher",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ChildPublisherService",
                        "rpcName": "CreateChildPublisher",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetChildPublisher(
        _BaseChildPublisherServiceRestTransport._BaseGetChildPublisher,
        ChildPublisherServiceRestStub,
    ):
        def __hash__(self):
            return hash("ChildPublisherServiceRestTransport.GetChildPublisher")

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
            request: child_publisher_service.GetChildPublisherRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> child_publisher_messages.ChildPublisher:
            r"""Call the get child publisher method over HTTP.

            Args:
                request (~.child_publisher_service.GetChildPublisherRequest):
                    The request object. Request object for ``GetChildPublisher`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.child_publisher_messages.ChildPublisher:
                    The
                [ChildPublisher][google.ads.admanager.v1.ChildPublisher]
                resource.

            """

            http_options = _BaseChildPublisherServiceRestTransport._BaseGetChildPublisher._get_http_options()
            request, metadata = self._interceptor.pre_get_child_publisher(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseChildPublisherServiceRestTransport._BaseGetChildPublisher,
                    "_BaseGetChildPublisher__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ChildPublisherServiceClient.GetChildPublisher",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ChildPublisherService",
                        "rpcName": "GetChildPublisher",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ChildPublisherServiceRestTransport._GetChildPublisher._get_response(
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
            resp = child_publisher_messages.ChildPublisher()
            pb_resp = child_publisher_messages.ChildPublisher.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_child_publisher(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_child_publisher_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = child_publisher_messages.ChildPublisher.to_json(
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
                    "Received response for google.ads.admanager_v1.ChildPublisherServiceClient.get_child_publisher",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ChildPublisherService",
                        "rpcName": "GetChildPublisher",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListChildPublishers(
        _BaseChildPublisherServiceRestTransport._BaseListChildPublishers,
        ChildPublisherServiceRestStub,
    ):
        def __hash__(self):
            return hash("ChildPublisherServiceRestTransport.ListChildPublishers")

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
            request: child_publisher_service.ListChildPublishersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> child_publisher_service.ListChildPublishersResponse:
            r"""Call the list child publishers method over HTTP.

            Args:
                request (~.child_publisher_service.ListChildPublishersRequest):
                    The request object. Request object for ``ListChildPublishers`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.child_publisher_service.ListChildPublishersResponse:
                    Response object for ``ListChildPublishers`` containing
                matching
                [ChildPublisher][google.ads.admanager.v1.ChildPublisher]
                objects.

            """

            http_options = _BaseChildPublisherServiceRestTransport._BaseListChildPublishers._get_http_options()
            request, metadata = self._interceptor.pre_list_child_publishers(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseChildPublisherServiceRestTransport._BaseListChildPublishers,
                    "_BaseListChildPublishers__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ChildPublisherServiceClient.ListChildPublishers",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ChildPublisherService",
                        "rpcName": "ListChildPublishers",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ChildPublisherServiceRestTransport._ListChildPublishers._get_response(
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
            resp = child_publisher_service.ListChildPublishersResponse()
            pb_resp = child_publisher_service.ListChildPublishersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_child_publishers(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_child_publishers_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        child_publisher_service.ListChildPublishersResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.ChildPublisherServiceClient.list_child_publishers",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ChildPublisherService",
                        "rpcName": "ListChildPublishers",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateChildPublisher(
        _BaseChildPublisherServiceRestTransport._BaseUpdateChildPublisher,
        ChildPublisherServiceRestStub,
    ):
        def __hash__(self):
            return hash("ChildPublisherServiceRestTransport.UpdateChildPublisher")

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
            request: child_publisher_service.UpdateChildPublisherRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> child_publisher_messages.ChildPublisher:
            r"""Call the update child publisher method over HTTP.

            Args:
                request (~.child_publisher_service.UpdateChildPublisherRequest):
                    The request object. Request object for ``UpdateChildPublisher`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.child_publisher_messages.ChildPublisher:
                    The
                [ChildPublisher][google.ads.admanager.v1.ChildPublisher]
                resource.

            """

            http_options = _BaseChildPublisherServiceRestTransport._BaseUpdateChildPublisher._get_http_options()
            request, metadata = self._interceptor.pre_update_child_publisher(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseChildPublisherServiceRestTransport._BaseUpdateChildPublisher,
                    "_BaseUpdateChildPublisher__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ChildPublisherServiceClient.UpdateChildPublisher",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ChildPublisherService",
                        "rpcName": "UpdateChildPublisher",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ChildPublisherServiceRestTransport._UpdateChildPublisher._get_response(
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
            resp = child_publisher_messages.ChildPublisher()
            pb_resp = child_publisher_messages.ChildPublisher.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_child_publisher(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_child_publisher_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = child_publisher_messages.ChildPublisher.to_json(
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
                    "Received response for google.ads.admanager_v1.ChildPublisherServiceClient.update_child_publisher",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ChildPublisherService",
                        "rpcName": "UpdateChildPublisher",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_create_child_publishers(
        self,
    ) -> Callable[
        [child_publisher_service.BatchCreateChildPublishersRequest],
        child_publisher_service.BatchCreateChildPublishersResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchCreateChildPublishers(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_reject_child_publishers(
        self,
    ) -> Callable[
        [child_publisher_service.BatchRejectChildPublishersRequest],
        child_publisher_service.BatchRejectChildPublishersResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchRejectChildPublishers(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_renegotiate_child_publisher_agreements(
        self,
    ) -> Callable[
        [child_publisher_service.BatchRenegotiateChildPublisherAgreementsRequest],
        child_publisher_service.BatchRenegotiateChildPublisherAgreementsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchRenegotiateChildPublisherAgreements(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_resend_child_publisher_invitation_emails(
        self,
    ) -> Callable[
        [child_publisher_service.BatchResendChildPublisherInvitationEmailsRequest],
        child_publisher_service.BatchResendChildPublisherInvitationEmailsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchResendChildPublisherInvitationEmails(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_update_child_publishers(
        self,
    ) -> Callable[
        [child_publisher_service.BatchUpdateChildPublishersRequest],
        child_publisher_service.BatchUpdateChildPublishersResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchUpdateChildPublishers(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_withdraw_child_publishers(
        self,
    ) -> Callable[
        [child_publisher_service.BatchWithdrawChildPublishersRequest],
        child_publisher_service.BatchWithdrawChildPublishersResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchWithdrawChildPublishers(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_child_publisher(
        self,
    ) -> Callable[
        [child_publisher_service.CreateChildPublisherRequest],
        child_publisher_messages.ChildPublisher,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateChildPublisher(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_child_publisher(
        self,
    ) -> Callable[
        [child_publisher_service.GetChildPublisherRequest],
        child_publisher_messages.ChildPublisher,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetChildPublisher(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_child_publishers(
        self,
    ) -> Callable[
        [child_publisher_service.ListChildPublishersRequest],
        child_publisher_service.ListChildPublishersResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListChildPublishers(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_child_publisher(
        self,
    ) -> Callable[
        [child_publisher_service.UpdateChildPublisherRequest],
        child_publisher_messages.ChildPublisher,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateChildPublisher(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseChildPublisherServiceRestTransport._BaseCancelOperation,
        ChildPublisherServiceRestStub,
    ):
        def __hash__(self):
            return hash("ChildPublisherServiceRestTransport.CancelOperation")

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

            http_options = _BaseChildPublisherServiceRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseChildPublisherServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.ads.admanager_v1.ChildPublisherServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ChildPublisherService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ChildPublisherServiceRestTransport._CancelOperation._get_response(
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

            return self._interceptor.post_cancel_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseChildPublisherServiceRestTransport._BaseGetOperation,
        ChildPublisherServiceRestStub,
    ):
        def __hash__(self):
            return hash("ChildPublisherServiceRestTransport.GetOperation")

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

            http_options = _BaseChildPublisherServiceRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseChildPublisherServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.ads.admanager_v1.ChildPublisherServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ChildPublisherService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ChildPublisherServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.ads.admanager_v1.ChildPublisherServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ChildPublisherService",
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


__all__ = ("ChildPublisherServiceRestTransport",)
