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

import google.api.httpbody_pb2 as httpbody_pb2  # type: ignore
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
from google.api_core import gapic_v1, path_template
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format

from google.cloud.managedkafka_schemaregistry_v1.types import (
    schema_registry,
    schema_registry_resources,
)
from google.cloud.managedkafka_schemaregistry_v1.types import (
    schema_registry as gcms_schema_registry,
)

from .base import DEFAULT_CLIENT_INFO, ManagedSchemaRegistryTransport


class _BaseManagedSchemaRegistryRestTransport(ManagedSchemaRegistryTransport):
    """Base REST backend transport for ManagedSchemaRegistry.

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
        host: str = "managedkafka.googleapis.com",
        credentials: Optional[Any] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.
        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'managedkafka.googleapis.com').
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

    class _BaseCheckCompatibility:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{name=projects/*/locations/*/schemaRegistries/*/compatibility/**}",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{name=projects/*/locations/*/schemaRegistries/*/contexts/*/compatibility/**}",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseCreateSchemaRegistry:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{parent=projects/*/locations/*}/schemaRegistries",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseCreateVersion:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{parent=projects/*/locations/*/schemaRegistries/*/subjects/*}/versions",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{parent=projects/*/locations/*/schemaRegistries/*/contexts/*/subjects/*}/versions",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseDeleteSchemaConfig:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/v1/{name=projects/*/locations/*/schemaRegistries/*/config/**}",
                },
                {
                    "method": "delete",
                    "uri": "/v1/{name=projects/*/locations/*/schemaRegistries/*/contexts/*/config/**}",
                },
            ]
            return http_options

    class _BaseDeleteSchemaMode:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/v1/{name=projects/*/locations/*/schemaRegistries/*/mode/**}",
                },
                {
                    "method": "delete",
                    "uri": "/v1/{name=projects/*/locations/*/schemaRegistries/*/contexts/*/mode/**}",
                },
            ]
            return http_options

    class _BaseDeleteSchemaRegistry:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/v1/{name=projects/*/locations/*/schemaRegistries/*}",
                },
            ]
            return http_options

    class _BaseDeleteSubject:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/v1/{name=projects/*/locations/*/schemaRegistries/*/subjects/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1/{name=projects/*/locations/*/schemaRegistries/*/contexts/*/subjects/*}",
                },
            ]
            return http_options

    class _BaseDeleteVersion:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/v1/{name=projects/*/locations/*/schemaRegistries/*/subjects/*/versions/*}",
                },
                {
                    "method": "delete",
                    "uri": "/v1/{name=projects/*/locations/*/schemaRegistries/*/contexts/*/subjects/*/versions/*}",
                },
            ]
            return http_options

    class _BaseGetContext:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/locations/*/schemaRegistries/*/contexts/*}",
                },
            ]
            return http_options

    class _BaseGetRawSchema:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/locations/*/schemaRegistries/*/schemas/**}/schema",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/locations/*/schemaRegistries/*/contexts/*/schemas/**}/schema",
                },
            ]
            return http_options

    class _BaseGetRawSchemaVersion:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/locations/*/schemaRegistries/*/subjects/*/versions/*}/schema",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/locations/*/schemaRegistries/*/contexts/*/subjects/*/versions/*}/schema",
                },
            ]
            return http_options

    class _BaseGetSchema:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/locations/*/schemaRegistries/*/schemas/**}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/locations/*/schemaRegistries/*/contexts/*/schemas/**}",
                },
            ]
            return http_options

    class _BaseGetSchemaConfig:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/locations/*/schemaRegistries/*/config/**}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/locations/*/schemaRegistries/*/contexts/*/config/**}",
                },
            ]
            return http_options

    class _BaseGetSchemaMode:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/locations/*/schemaRegistries/*/mode/**}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/locations/*/schemaRegistries/*/contexts/*/mode/**}",
                },
            ]
            return http_options

    class _BaseGetSchemaRegistry:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/locations/*/schemaRegistries/*}",
                },
            ]
            return http_options

    class _BaseGetVersion:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/locations/*/schemaRegistries/*/subjects/*/versions/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/locations/*/schemaRegistries/*/contexts/*/subjects/*/versions/*}",
                },
            ]
            return http_options

    class _BaseListContexts:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*/locations/*/schemaRegistries/*}/contexts",
                },
            ]
            return http_options

    class _BaseListReferencedSchemas:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*/locations/*/schemaRegistries/*/subjects/*/versions/*}/referencedby",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*/locations/*/schemaRegistries/*/contexts/*/subjects/*/versions/*}/referencedby",
                },
            ]
            return http_options

    class _BaseListSchemaRegistries:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*/locations/*}/schemaRegistries",
                },
            ]
            return http_options

    class _BaseListSchemaTypes:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*/locations/*/schemaRegistries/*}/schemas/types",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*/locations/*/schemaRegistries/*/contexts/*}/schemas/types",
                },
            ]
            return http_options

    class _BaseListSchemaVersions:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*/locations/*/schemaRegistries/*/schemas/**}/versions",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*/locations/*/schemaRegistries/*/contexts/*/schemas/**}/versions",
                },
            ]
            return http_options

    class _BaseListSubjects:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*/locations/*/schemaRegistries/*}/subjects",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*/locations/*/schemaRegistries/*/contexts/*}/subjects",
                },
            ]
            return http_options

    class _BaseListSubjectsBySchemaId:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*/locations/*/schemaRegistries/*/schemas/**}/subjects",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*/locations/*/schemaRegistries/*/contexts/*/schemas/**}/subjects",
                },
            ]
            return http_options

    class _BaseListVersions:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*/locations/*/schemaRegistries/*/subjects/*}/versions",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*/locations/*/schemaRegistries/*/contexts/*/subjects/*}/versions",
                },
            ]
            return http_options

    class _BaseLookupVersion:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{parent=projects/*/locations/*/schemaRegistries/*/subjects/*}",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{parent=projects/*/locations/*/schemaRegistries/*/contexts/*/subjects/*}",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseUpdateSchemaConfig:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "put",
                    "uri": "/v1/{name=projects/*/locations/*/schemaRegistries/*/config/**}",
                    "body": "*",
                },
                {
                    "method": "put",
                    "uri": "/v1/{name=projects/*/locations/*/schemaRegistries/*/contexts/*/config/**}",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseUpdateSchemaMode:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "put",
                    "uri": "/v1/{name=projects/*/locations/*/schemaRegistries/*/mode/**}",
                    "body": "*",
                },
                {
                    "method": "put",
                    "uri": "/v1/{name=projects/*/locations/*/schemaRegistries/*/contexts/*/mode/**}",
                    "body": "*",
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
            ]
            return http_options

    class _BaseCancelOperation:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{name=projects/*/locations/*/operations/*}:cancel",
                    "body": "*",
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
            ]
            return http_options


__all__ = ("_BaseManagedSchemaRegistryRestTransport",)
