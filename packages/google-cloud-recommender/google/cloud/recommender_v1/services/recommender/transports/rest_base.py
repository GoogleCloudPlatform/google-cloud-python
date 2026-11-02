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
from google.protobuf import json_format

from google.cloud.recommender_v1.types import (
    insight,
    insight_type_config,
    recommendation,
    recommender_config,
    recommender_service,
)
from google.cloud.recommender_v1.types import (
    insight_type_config as gcr_insight_type_config,
)
from google.cloud.recommender_v1.types import (
    recommender_config as gcr_recommender_config,
)

from .base import DEFAULT_CLIENT_INFO, RecommenderTransport


class _BaseRecommenderRestTransport(RecommenderTransport):
    """Base REST backend transport for Recommender.

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
        host: str = "recommender.googleapis.com",
        credentials: Optional[Any] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.
        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'recommender.googleapis.com').
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

    class _BaseGetInsight:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/locations/*/insightTypes/*/insights/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=billingAccounts/*/locations/*/insightTypes/*/insights/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=folders/*/locations/*/insightTypes/*/insights/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=organizations/*/locations/*/insightTypes/*/insights/*}",
                },
            ]
            return http_options

    class _BaseGetInsightTypeConfig:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/locations/*/insightTypes/*/config}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=organizations/*/locations/*/insightTypes/*/config}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=billingAccounts/*/locations/*/insightTypes/*/config}",
                },
            ]
            return http_options

    class _BaseGetRecommendation:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/locations/*/recommenders/*/recommendations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=billingAccounts/*/locations/*/recommenders/*/recommendations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=folders/*/locations/*/recommenders/*/recommendations/*}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=organizations/*/locations/*/recommenders/*/recommendations/*}",
                },
            ]
            return http_options

    class _BaseGetRecommenderConfig:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{name=projects/*/locations/*/recommenders/*/config}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=organizations/*/locations/*/recommenders/*/config}",
                },
                {
                    "method": "get",
                    "uri": "/v1/{name=billingAccounts/*/locations/*/recommenders/*/config}",
                },
            ]
            return http_options

    class _BaseListInsights:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*/locations/*/insightTypes/*}/insights",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=billingAccounts/*/locations/*/insightTypes/*}/insights",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=folders/*/locations/*/insightTypes/*}/insights",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=organizations/*/locations/*/insightTypes/*}/insights",
                },
            ]
            return http_options

    class _BaseListRecommendations:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/v1/{parent=projects/*/locations/*/recommenders/*}/recommendations",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=billingAccounts/*/locations/*/recommenders/*}/recommendations",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=folders/*/locations/*/recommenders/*}/recommendations",
                },
                {
                    "method": "get",
                    "uri": "/v1/{parent=organizations/*/locations/*/recommenders/*}/recommendations",
                },
            ]
            return http_options

    class _BaseMarkInsightAccepted:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{name=projects/*/locations/*/insightTypes/*/insights/*}:markAccepted",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{name=billingAccounts/*/locations/*/insightTypes/*/insights/*}:markAccepted",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{name=folders/*/locations/*/insightTypes/*/insights/*}:markAccepted",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{name=organizations/*/locations/*/insightTypes/*/insights/*}:markAccepted",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseMarkRecommendationClaimed:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{name=projects/*/locations/*/recommenders/*/recommendations/*}:markClaimed",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{name=billingAccounts/*/locations/*/recommenders/*/recommendations/*}:markClaimed",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{name=folders/*/locations/*/recommenders/*/recommendations/*}:markClaimed",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{name=organizations/*/locations/*/recommenders/*/recommendations/*}:markClaimed",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseMarkRecommendationDismissed:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{name=projects/*/locations/*/recommenders/*/recommendations/*}:markDismissed",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{name=billingAccounts/*/locations/*/recommenders/*/recommendations/*}:markDismissed",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{name=folders/*/locations/*/recommenders/*/recommendations/*}:markDismissed",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{name=organizations/*/locations/*/recommenders/*/recommendations/*}:markDismissed",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseMarkRecommendationFailed:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{name=projects/*/locations/*/recommenders/*/recommendations/*}:markFailed",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{name=billingAccounts/*/locations/*/recommenders/*/recommendations/*}:markFailed",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{name=folders/*/locations/*/recommenders/*/recommendations/*}:markFailed",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{name=organizations/*/locations/*/recommenders/*/recommendations/*}:markFailed",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseMarkRecommendationSucceeded:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/v1/{name=projects/*/locations/*/recommenders/*/recommendations/*}:markSucceeded",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{name=billingAccounts/*/locations/*/recommenders/*/recommendations/*}:markSucceeded",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{name=folders/*/locations/*/recommenders/*/recommendations/*}:markSucceeded",
                    "body": "*",
                },
                {
                    "method": "post",
                    "uri": "/v1/{name=organizations/*/locations/*/recommenders/*/recommendations/*}:markSucceeded",
                    "body": "*",
                },
            ]
            return http_options

    class _BaseUpdateInsightTypeConfig:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "patch",
                    "uri": "/v1/{insight_type_config.name=projects/*/locations/*/insightTypes/*/config}",
                    "body": "insight_type_config",
                },
                {
                    "method": "patch",
                    "uri": "/v1/{insight_type_config.name=organizations/*/locations/*/insightTypes/*/config}",
                    "body": "insight_type_config",
                },
                {
                    "method": "patch",
                    "uri": "/v1/{insight_type_config.name=billingAccounts/*/locations/*/insightTypes/*/config}",
                    "body": "insight_type_config",
                },
            ]
            return http_options

    class _BaseUpdateRecommenderConfig:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "patch",
                    "uri": "/v1/{recommender_config.name=projects/*/locations/*/recommenders/*/config}",
                    "body": "recommender_config",
                },
                {
                    "method": "patch",
                    "uri": "/v1/{recommender_config.name=organizations/*/locations/*/recommenders/*/config}",
                    "body": "recommender_config",
                },
                {
                    "method": "patch",
                    "uri": "/v1/{recommender_config.name=billingAccounts/*/locations/*/recommenders/*/config}",
                    "body": "recommender_config",
                },
            ]
            return http_options


__all__ = ("_BaseRecommenderRestTransport",)
