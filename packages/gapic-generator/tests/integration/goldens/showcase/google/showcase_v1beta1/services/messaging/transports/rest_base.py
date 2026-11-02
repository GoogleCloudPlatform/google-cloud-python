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
from google.api_core import path_template
from google.api_core import gapic_v1
from google.api_core.client_options import ClientOptions

from google.protobuf import json_format
from google.iam.v1 import iam_policy_pb2  # type: ignore
from google.iam.v1 import policy_pb2  # type: ignore
from google.cloud.location import locations_pb2 # type: ignore
from .base import MessagingTransport, DEFAULT_CLIENT_INFO

import re
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union


from google.showcase_v1beta1.types import messaging
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore


class _BaseMessagingRestTransport(MessagingTransport):
    """Base REST backend transport for Messaging.

    Note: This class is not meant to be used directly. Use its sync and
    async sub-classes instead.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(self, *,
            host: str = 'localhost:7469',
            credentials: Optional[Any] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            always_use_jwt_access: Optional[bool] = False,
            url_scheme: str = 'https',
            api_audience: Optional[str] = None,
            client_options: Optional[Union[ClientOptions, dict]] = None,
            **kwargs,
            ) -> None:
        """Instantiate the transport.
        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'localhost:7469').
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
            client_options (Optional[Union[google.api_core.client_options.ClientOptions, dict]]):
                Custom options for the client, containing options such as
                custom OpenTelemetry tracer providers.
        """
        # Run the base constructor
        maybe_url_match = re.match("^(?P<scheme>http(?:s)?://)?(?P<host>.*)$", host)
        if maybe_url_match is None:
            raise ValueError(f"Unexpected hostname structure: {host}")  # pragma: NO COVER

        url_match_items = maybe_url_match.groupdict()

        host = f"{url_scheme}://{host}" if not url_match_items["scheme"] else host

        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            api_audience=api_audience,
            client_options=client_options,
            **kwargs,
        )

    class _BaseConnect:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

    class _BaseCreateBlurb:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1beta1/{parent=rooms/*}/blurbs',
                'body': '*',
            },
        {
                'method': 'post',
                'uri': '/v1beta1/{parent=users/*/profile}/blurbs',
                'body': '*',
            },
            ]
            return http_options

    class _BaseCreateRoom:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1beta1/rooms',
                'body': '*',
            },
            ]
            return http_options

    class _BaseDeleteBlurb:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'delete',
                'uri': '/v1beta1/{name=rooms/*/blurbs/*}',
            },
        {
                'method': 'delete',
                'uri': '/v1beta1/{name=users/*/profile/blurbs/*}',
            },
            ]
            return http_options

    class _BaseDeleteRoom:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'delete',
                'uri': '/v1beta1/{name=rooms/*}',
            },
            ]
            return http_options

    class _BaseGetBlurb:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1beta1/{name=rooms/*/blurbs/*}',
            },
        {
                'method': 'get',
                'uri': '/v1beta1/{name=users/*/profile/blurbs/*}',
            },
            ]
            return http_options

    class _BaseGetRoom:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1beta1/{name=rooms/*}',
            },
            ]
            return http_options

    class _BaseListBlurbs:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1beta1/{parent=rooms/*}/blurbs',
            },
        {
                'method': 'get',
                'uri': '/v1beta1/{parent=users/*/profile}/blurbs',
            },
            ]
            return http_options

    class _BaseListRooms:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1beta1/rooms',
            },
            ]
            return http_options

    class _BaseSearchBlurbs:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1beta1/{parent=rooms/*}/blurbs:search',
                'body': '*',
            },
        {
                'method': 'post',
                'uri': '/v1beta1/{parent=users/*/profile}/blurbs:search',
            },
            ]
            return http_options

    class _BaseSendBlurbs:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

    class _BaseStreamBlurbs:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] =  {
        }

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1beta1/{name=rooms/*}/blurbs:stream',
                'body': '*',
            },
        {
                'method': 'post',
                'uri': '/v1beta1/{name=users/*/profile}/blurbs:stream',
                'body': '*',
            },
            ]
            return http_options

    class _BaseUpdateBlurb:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'patch',
                'uri': '/v1beta1/{blurb.name=rooms/*/blurbs/*}',
                'body': 'blurb',
            },
        {
                'method': 'patch',
                'uri': '/v1beta1/{blurb.name=users/*/profile/blurbs/*}',
                'body': 'blurb',
            },
            ]
            return http_options

    class _BaseUpdateRoom:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'patch',
                'uri': '/v1beta1/{room.name=rooms/*}',
                'body': 'room',
            },
            ]
            return http_options

    class _BaseListLocations:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1beta1/{name=projects/*}/locations',
            },
            ]
            return http_options

    class _BaseGetLocation:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1beta1/{name=projects/*/locations/*}',
            },
            ]
            return http_options

    class _BaseSetIamPolicy:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1beta1/{resource=users/*}:setIamPolicy',
                'body': '*',
            },
        {
                'method': 'post',
                'uri': '/v1beta1/{resource=rooms/*}:setIamPolicy',
                'body': '*',
            },
        {
                'method': 'post',
                'uri': '/v1beta1/{resource=rooms/*/blurbs/*}:setIamPolicy',
                'body': '*',
            },
        {
                'method': 'post',
                'uri': '/v1beta1/{resource=sequences/*}:setIamPolicy',
                'body': '*',
            },
            ]
            return http_options

    class _BaseGetIamPolicy:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1beta1/{resource=users/*}:getIamPolicy',
            },
        {
                'method': 'get',
                'uri': '/v1beta1/{resource=rooms/*}:getIamPolicy',
            },
        {
                'method': 'get',
                'uri': '/v1beta1/{resource=rooms/*/blurbs/*}:getIamPolicy',
            },
        {
                'method': 'get',
                'uri': '/v1beta1/{resource=sequences/*}:getIamPolicy',
            },
            ]
            return http_options

    class _BaseTestIamPermissions:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1beta1/{resource=users/*}:testIamPermissions',
                'body': '*',
            },
        {
                'method': 'post',
                'uri': '/v1beta1/{resource=rooms/*}:testIamPermissions',
                'body': '*',
            },
        {
                'method': 'post',
                'uri': '/v1beta1/{resource=rooms/*/blurbs/*}:testIamPermissions',
                'body': '*',
            },
        {
                'method': 'post',
                'uri': '/v1beta1/{resource=sequences/*}:testIamPermissions',
                'body': '*',
            },
            ]
            return http_options

    class _BaseListOperations:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1beta1/operations',
            },
            ]
            return http_options

    class _BaseGetOperation:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v1beta1/{name=operations/**}',
            },
            ]
            return http_options

    class _BaseDeleteOperation:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'delete',
                'uri': '/v1beta1/{name=operations/**}',
            },
            ]
            return http_options

    class _BaseCancelOperation:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1beta1/{name=operations/**}:cancel',
            },
            ]
            return http_options


__all__=(
    '_BaseMessagingRestTransport',
)
