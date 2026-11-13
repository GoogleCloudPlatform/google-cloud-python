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
import json  # type: ignore
import re
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union

import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
from google.api_core import gapic_v1, path_template
from google.protobuf import json_format

from google.cloud.accessapproval_v1.types import accessapproval

from .base import DEFAULT_CLIENT_INFO, AccessApprovalTransport


class _BaseAccessApprovalRestTransport(AccessApprovalTransport):
    """Base REST backend transport for AccessApproval.

    Note: This class is not meant to be used directly. Use its sync and
    async sub-classes instead.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "accessapproval.googleapis.com",
        credentials: Optional[Any] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.
        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'accessapproval.googleapis.com').
            credentials (Optional[Any]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
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
        """
        # Run the base constructor
        maybe_url_match = re.match("^(?P<scheme>http(?:s)?://)?(?P<host>.*)$", host)
        if maybe_url_match is None:
            raise ValueError(
                f"Unexpected hostname structure: {host}"
            )  # pragma: NO COVER

        url_match_items = maybe_url_match.groupdict()

        host = f"{url_scheme}://{host}" if not url_match_items["scheme"] else host

        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            api_audience=api_audience,
        )

    class _BaseApproveApprovalRequest:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{name=projects/*/approvalRequests/*}:approve",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{name=folders/*/approvalRequests/*}:approve",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{name=organizations/*/approvalRequests/*}:approve",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseDeleteAccessApprovalSettings:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/v1/{name=projects/*/accessApprovalSettings}",
                },
                {
                    "method": "delete",
                    "uri": "/v1/{name=folders/*/accessApprovalSettings}",
                },
                {
                    "method": "delete",
                    "uri": "/v1/{name=organizations/*/accessApprovalSettings}",
                },
            ]
            return http_options

    class _BaseDismissApprovalRequest:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{name=projects/*/approvalRequests/*}:dismiss",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{name=folders/*/approvalRequests/*}:dismiss",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{name=organizations/*/approvalRequests/*}:dismiss",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseGetAccessApprovalServiceAccount:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/serviceAccount}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=folders/*/serviceAccount}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=organizations/*/serviceAccount}",
                },
            ]
            return http_options

    class _BaseGetAccessApprovalSettings:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/accessApprovalSettings}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=folders/*/accessApprovalSettings}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=organizations/*/accessApprovalSettings}",
                },
            ]
            return http_options

    class _BaseGetApprovalRequest:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/approvalRequests/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=folders/*/approvalRequests/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=organizations/*/approvalRequests/*}",
                },
            ]
            return http_options

    class _BaseInvalidateApprovalRequest:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{name=projects/*/approvalRequests/*}:invalidate",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{name=folders/*/approvalRequests/*}:invalidate",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{name=organizations/*/approvalRequests/*}:invalidate",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseListApprovalRequests:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*}/approvalRequests",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=folders/*}/approvalRequests",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=organizations/*}/approvalRequests",
                },
            ]
            return http_options

    class _BaseUpdateAccessApprovalSettings:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "patch",
                    "uri": "/v1/{settings.name=projects/*/accessApprovalSettings}",
                    "body": "settings",
                },
                {
                    "method": "patch",
                    "uri": "/v1/{settings.name=folders/*/accessApprovalSettings}",
                    "body": "settings",
                },
                {
                    "method": "patch",
                    "uri": "/v1/{settings.name=organizations/*/accessApprovalSettings}",
                    "body": "settings",
                },
            ]
            return http_options


__all__ = ("_BaseAccessApprovalRestTransport",)
