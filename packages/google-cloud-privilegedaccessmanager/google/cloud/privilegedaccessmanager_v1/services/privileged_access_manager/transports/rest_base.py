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

from google.api_core import gapic_v1, path_template
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format

from google.cloud.privilegedaccessmanager_v1.types import privilegedaccessmanager

from .base import DEFAULT_CLIENT_INFO, PrivilegedAccessManagerTransport


class _BasePrivilegedAccessManagerRestTransport(PrivilegedAccessManagerTransport):
    """Base REST backend transport for PrivilegedAccessManager.

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
        host: str = "privilegedaccessmanager.googleapis.com",
        credentials: Optional[Any] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.
        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'privilegedaccessmanager.googleapis.com').
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

    class _BaseApproveGrant:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{name=projects/*/locations/*/entitlements/*/grants/*}:approve",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{name=organizations/*/locations/*/entitlements/*/grants/*}:approve",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{name=folders/*/locations/*/entitlements/*/grants/*}:approve",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseCheckOnboardingStatus:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*/locations/*}:checkOnboardingStatus",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=organizations/*/locations/*}:checkOnboardingStatus",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=folders/*/locations/*}:checkOnboardingStatus",
                },
            ]
            return http_options

    class _BaseCreateEntitlement:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {
            "entitlementId": "",
        }

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{parent=projects/*/locations/*}/entitlements",
                    "body": "entitlement",
                },
                {
                    "method": "post",
                    "uri": "/v1/{parent=organizations/*/locations/*}/entitlements",
                    "body": "entitlement",
                },
                {
                    "method": "post",
                    "uri": "/v1/{parent=folders/*/locations/*}/entitlements",
                    "body": "entitlement",
                },
            ]
            return http_options

    class _BaseCreateGrant:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{parent=projects/*/locations/*/entitlements/*}/grants",
                    "body": "grant",
                },
                {
                    "method": "post",
                    "uri": "/v1/{parent=organizations/*/locations/*/entitlements/*}/grants",
                    "body": "grant",
                },
                {
                    "method": "post",
                    "uri": "/v1/{parent=folders/*/locations/*/entitlements/*}/grants",
                    "body": "grant",
                },
            ]
            return http_options

    class _BaseDeleteEntitlement:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/v1/{name=projects/*/locations/*/entitlements/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1/{name=organizations/*/locations/*/entitlements/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1/{name=folders/*/locations/*/entitlements/*}",
                },
            ]
            return http_options

    class _BaseDenyGrant:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{name=projects/*/locations/*/entitlements/*/grants/*}:deny",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{name=organizations/*/locations/*/entitlements/*/grants/*}:deny",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{name=folders/*/locations/*/entitlements/*/grants/*}:deny",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseGetEntitlement:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/locations/*/entitlements/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=organizations/*/locations/*/entitlements/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=folders/*/locations/*/entitlements/*}",
                },
            ]
            return http_options

    class _BaseGetGrant:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/locations/*/entitlements/*/grants/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=organizations/*/locations/*/entitlements/*/grants/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=folders/*/locations/*/entitlements/*/grants/*}",
                },
            ]
            return http_options

    class _BaseListEntitlements:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*/locations/*}/entitlements",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=organizations/*/locations/*}/entitlements",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=folders/*/locations/*}/entitlements",
                },
            ]
            return http_options

    class _BaseListGrants:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*/locations/*/entitlements/*}/grants",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=organizations/*/locations/*/entitlements/*}/grants",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=folders/*/locations/*/entitlements/*}/grants",
                },
            ]
            return http_options

    class _BaseRevokeGrant:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{name=projects/*/locations/*/entitlements/*/grants/*}:revoke",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{name=organizations/*/locations/*/entitlements/*/grants/*}:revoke",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{name=folders/*/locations/*/entitlements/*/grants/*}:revoke",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseSearchEntitlements:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {
            "callerAccessType": {},
        }

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*/locations/*}/entitlements:search",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=organizations/*/locations/*}/entitlements:search",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=folders/*/locations/*}/entitlements:search",
                },
            ]
            return http_options

    class _BaseSearchGrants:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {
            "callerRelationship": {},
        }

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*/locations/*/entitlements/*}/grants:search",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=organizations/*/locations/*/entitlements/*}/grants:search",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=folders/*/locations/*/entitlements/*}/grants:search",
                },
            ]
            return http_options

    class _BaseUpdateEntitlement:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {
            "updateMask": {},
        }

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "patch",
                    "uri": "/v1/{entitlement.name=projects/*/locations/*/entitlements/*}",
                    "body": "entitlement",
                },
                {
                    "method": "patch",
                    "uri": "/v1/{entitlement.name=organizations/*/locations/*/entitlements/*}",
                    "body": "entitlement",
                },
                {
                    "method": "patch",
                    "uri": "/v1/{entitlement.name=folders/*/locations/*/entitlements/*}",
                    "body": "entitlement",
                },
            ]
            return http_options

    class _BaseGetLocation:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/locations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=organizations/*/locations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=folders/*/locations/*}",
                },
            ]
            return http_options

    class _BaseListLocations:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*}/locations",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=organizations/*}/locations",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=folders/*}/locations",
                },
            ]
            return http_options

    class _BaseDeleteOperation:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/v1/{name=projects/*/locations/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1/{name=organizations/*/locations/*/operations/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1/{name=folders/*/locations/*/operations/*}",
                },
            ]
            return http_options

    class _BaseGetOperation:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/locations/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=organizations/*/locations/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=folders/*/locations/*/operations/*}",
                },
            ]
            return http_options

    class _BaseListOperations:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/locations/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=organizations/*/locations/*}/operations",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=folders/*/locations/*}/operations",
                },
            ]
            return http_options


__all__ = ("_BasePrivilegedAccessManagerRestTransport",)
