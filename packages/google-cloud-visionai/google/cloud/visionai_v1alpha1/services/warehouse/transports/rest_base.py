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
from google.cloud.location import locations_pb2  # type: ignore
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format

from google.cloud.visionai_v1alpha1.types import warehouse

from .base import DEFAULT_CLIENT_INFO, WarehouseTransport


class _BaseWarehouseRestTransport(WarehouseTransport):
    """Base REST backend transport for Warehouse.

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
        host: str = "visionai.googleapis.com",
        credentials: Optional[Any] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.
        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'visionai.googleapis.com').
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

    class _BaseClipAsset:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1alpha1/{name=projects/*/locations/*/corpora/*/assets/*}:clip",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseCreateAnnotation:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1alpha1/{parent=projects/*/locations/*/corpora/*/assets/*}/annotations",
                    "body": "annotation",
                },
            ]
            return http_options

    class _BaseCreateAsset:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1alpha1/{parent=projects/*/locations/*/corpora/*}/assets",
                    "body": "asset",
                },
            ]
            return http_options

    class _BaseCreateCorpus:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1alpha1/{parent=projects/*/locations/*}/corpora",
                    "body": "corpus",
                },
            ]
            return http_options

    class _BaseCreateDataSchema:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1alpha1/{parent=projects/*/locations/*/corpora/*}/dataSchemas",
                    "body": "data_schema",
                },
            ]
            return http_options

    class _BaseCreateSearchConfig:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {
            "searchConfigId": "",
        }

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1alpha1/{parent=projects/*/locations/*/corpora/*}/searchConfigs",
                    "body": "search_config",
                },
            ]
            return http_options

    class _BaseDeleteAnnotation:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/v1alpha1/{name=projects/*/locations/*/corpora/*/assets/*/annotations/*}",
                },
            ]
            return http_options

    class _BaseDeleteAsset:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/v1alpha1/{name=projects/*/locations/*/corpora/*/assets/*}",
                },
            ]
            return http_options

    class _BaseDeleteCorpus:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/v1alpha1/{name=projects/*/locations/*/corpora/*}",
                },
            ]
            return http_options

    class _BaseDeleteDataSchema:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/v1alpha1/{name=projects/*/locations/*/corpora/*/dataSchemas/*}",
                },
            ]
            return http_options

    class _BaseDeleteSearchConfig:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/v1alpha1/{name=projects/*/locations/*/corpora/*/searchConfigs/*}",
                },
            ]
            return http_options

    class _BaseGenerateHlsUri:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1alpha1/{name=projects/*/locations/*/corpora/*/assets/*}:generateHlsUri",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseGetAnnotation:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1alpha1/{name=projects/*/locations/*/corpora/*/assets/*/annotations/*}",
                },
            ]
            return http_options

    class _BaseGetAsset:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1alpha1/{name=projects/*/locations/*/corpora/*/assets/*}",
                },
            ]
            return http_options

    class _BaseGetCorpus:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1alpha1/{name=projects/*/locations/*/corpora/*}",
                },
            ]
            return http_options

    class _BaseGetDataSchema:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1alpha1/{name=projects/*/locations/*/corpora/*/dataSchemas/*}",
                },
            ]
            return http_options

    class _BaseGetSearchConfig:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1alpha1/{name=projects/*/locations/*/corpora/*/searchConfigs/*}",
                },
            ]
            return http_options

    class _BaseIngestAsset:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

    class _BaseListAnnotations:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1alpha1/{parent=projects/*/locations/*/corpora/*/assets/*}/annotations",
                },
            ]
            return http_options

    class _BaseListAssets:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1alpha1/{parent=projects/*/locations/*/corpora/*}/assets",
                },
            ]
            return http_options

    class _BaseListCorpora:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1alpha1/{parent=projects/*/locations/*}/corpora",
                },
            ]
            return http_options

    class _BaseListDataSchemas:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1alpha1/{parent=projects/*/locations/*/corpora/*}/dataSchemas",
                },
            ]
            return http_options

    class _BaseListSearchConfigs:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1alpha1/{parent=projects/*/locations/*/corpora/*}/searchConfigs",
                },
            ]
            return http_options

    class _BaseSearchAssets:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1alpha1/{corpus=projects/*/locations/*/corpora/*}:searchAssets",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseUpdateAnnotation:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "patch",
                    "uri": "/v1alpha1/{annotation.name=projects/*/locations/*/corpora/*/assets/*/annotations/*}",
                    "body": "annotation",
                },
            ]
            return http_options

    class _BaseUpdateAsset:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "patch",
                    "uri": "/v1alpha1/{asset.name=projects/*/locations/*/corpora/*/assets/*}",
                    "body": "asset",
                },
            ]
            return http_options

    class _BaseUpdateCorpus:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "patch",
                    "uri": "/v1alpha1/{corpus.name=projects/*/locations/*/corpora/*}",
                    "body": "corpus",
                },
            ]
            return http_options

    class _BaseUpdateDataSchema:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "patch",
                    "uri": "/v1alpha1/{data_schema.name=projects/*/locations/*/corpora/*/dataSchemas/*}",
                    "body": "data_schema",
                },
            ]
            return http_options

    class _BaseUpdateSearchConfig:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "patch",
                    "uri": "/v1alpha1/{search_config.name=projects/*/locations/*/corpora/*/searchConfigs/*}",
                    "body": "search_config",
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
                    "uri": "/v1alpha1/{name=projects/*/locations/*}",
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
                    "uri": "/v1alpha1/{name=projects/*}/locations",
                },
            ]
            return http_options

    class _BaseGetIamPolicy:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1alpha1/{resource=projects/*/locations/*/clusters/*}:getIamPolicy",
                },
                {
                    "method": "get",
                    "uri": "/v1alpha1/{resource=projects/*/locations/*/clusters/*/streams/*}:getIamPolicy",
                },
                {
                    "method": "get",
                    "uri": "/v1alpha1/{resource=projects/*/locations/*/clusters/*/events/*}:getIamPolicy",
                },
                {
                    "method": "get",
                    "uri": "/v1alpha1/{resource=projects/*/locations/*/clusters/*/series/*}:getIamPolicy",
                },
                {
                    "method": "get",
                    "uri": "/v1alpha1/{resource=projects/*/locations/*/operators/*}:getIamPolicy",
                },
                {
                    "method": "get",
                    "uri": "/v1alpha1/{resource=projects/*/locations/*/operators/*/versions/*}:getIamPolicy",
                },
                {
                    "method": "get",
                    "uri": "/v1alpha1/{resource=projects/*/locations/*/clusters/*/analyses/*}:getIamPolicy",
                },
            ]
            return http_options

    class _BaseSetIamPolicy:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1alpha1/{resource=projects/*/locations/*/clusters/*}:setIamPolicy",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1alpha1/{resource=projects/*/locations/*/clusters/*/streams/*}:setIamPolicy",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1alpha1/{resource=projects/*/locations/*/clusters/*/events/*}:setIamPolicy",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1alpha1/{resource=projects/*/locations/*/clusters/*/series/*}:setIamPolicy",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1alpha1/{resource=projects/*/locations/*/operators/*}:setIamPolicy",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1alpha1/{resource=projects/*/locations/*/operators/*/versions/*}:setIamPolicy",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1alpha1/{resource=projects/*/locations/*/clusters/*/analyses/*}:setIamPolicy",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseTestIamPermissions:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1alpha1/{resource=projects/*/locations/*/clusters/*}:testIamPermissions",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1alpha1/{resource=projects/*/locations/*/clusters/*/streams/*}:testIamPermissions",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1alpha1/{resource=projects/*/locations/*/clusters/*/events/*}:testIamPermissions",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1alpha1/{resource=projects/*/locations/*/clusters/*/series/*}:testIamPermissions",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1alpha1/{resource=projects/*/locations/*/operators/*}:testIamPermissions",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1alpha1/{resource=projects/*/locations/*/operators/*/versions/*}:testIamPermissions",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1alpha1/{resource=projects/*/locations/*/clusters/*/analyses/*}:testIamPermissions",
                    "body": "*",
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
                    "uri": "/v1alpha1/{name=projects/*/locations/*/operations/*}:cancel",
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
                    "uri": "/v1alpha1/{name=projects/*/locations/*/operations/*}",
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
                    "uri": "/v1alpha1/{name=projects/*/locations/*/operations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1alpha1/{name=projects/*/locations/*/warehouseOperations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1alpha1/{name=projects/*/locations/*/corpora/*/assets/*/operations/*}",
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
                    "uri": "/v1alpha1/{name=projects/*/locations/*}/operations",
                },
            ]
            return http_options


__all__ = ("_BaseWarehouseRestTransport",)
