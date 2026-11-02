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

from google.cloud.orgpolicy_v2.types import constraint, orgpolicy

from .base import DEFAULT_CLIENT_INFO, OrgPolicyTransport


class _BaseOrgPolicyRestTransport(OrgPolicyTransport):
    """Base REST backend transport for OrgPolicy.

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
        host: str = "orgpolicy.googleapis.com",
        credentials: Optional[Any] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.
        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'orgpolicy.googleapis.com').
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

    class _BaseCreateCustomConstraint:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v2/{parent=organizations/*}/customConstraints",
                    "body": "custom_constraint",
                },
            ]
            return http_options

    class _BaseCreatePolicy:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v2/{parent=projects/*}/policies",
                    "body": "policy",
                },
                {
                    "method": "post",
                    "uri": "/v2/{parent=folders/*}/policies",
                    "body": "policy",
                },
                {
                    "method": "post",
                    "uri": "/v2/{parent=organizations/*}/policies",
                    "body": "policy",
                },
            ]
            return http_options

    class _BaseDeleteCustomConstraint:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/v2/{name=organizations/*/customConstraints/*}",
                },
            ]
            return http_options

    class _BaseDeletePolicy:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/v2/{name=projects/*/policies/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v2/{name=folders/*/policies/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v2/{name=organizations/*/policies/*}",
                },
            ]
            return http_options

    class _BaseGetCustomConstraint:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v2/{name=organizations/*/customConstraints/*}",
                },
            ]
            return http_options

    class _BaseGetEffectivePolicy:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v2/{name=projects/*/policies/*}:getEffectivePolicy",
                },
                {
                    "method": "get",
                    "uri": "/v2/{name=folders/*/policies/*}:getEffectivePolicy",
                },
                {
                    "method": "get",
                    "uri": "/v2/{name=organizations/*/policies/*}:getEffectivePolicy",
                },
            ]
            return http_options

    class _BaseGetPolicy:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v2/{name=projects/*/policies/*}",
                },
                {
                    "method": "get",
                    "uri": "/v2/{name=folders/*/policies/*}",
                },
                {
                    "method": "get",
                    "uri": "/v2/{name=organizations/*/policies/*}",
                },
            ]
            return http_options

    class _BaseListConstraints:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v2/{parent=projects/*}/constraints",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=folders/*}/constraints",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=organizations/*}/constraints",
                },
            ]
            return http_options

    class _BaseListCustomConstraints:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v2/{parent=organizations/*}/customConstraints",
                },
            ]
            return http_options

    class _BaseListPolicies:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v2/{parent=projects/*}/policies",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=folders/*}/policies",
                },
                {
                    "method": "get",
                    "uri": "/v2/{parent=organizations/*}/policies",
                },
            ]
            return http_options

    class _BaseUpdateCustomConstraint:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "patch",
                    "uri": "/v2/{custom_constraint.name=organizations/*/customConstraints/*}",
                    "body": "custom_constraint",
                },
            ]
            return http_options

    class _BaseUpdatePolicy:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "patch",
                    "uri": "/v2/{policy.name=projects/*/policies/*}",
                    "body": "policy",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{policy.name=folders/*/policies/*}",
                    "body": "policy",
                },
                {
                    "method": "patch",
                    "uri": "/v2/{policy.name=organizations/*/policies/*}",
                    "body": "policy",
                },
            ]
            return http_options


__all__ = ("_BaseOrgPolicyRestTransport",)
