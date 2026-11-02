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
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, operations_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.dataplex_v1._compat import transcode_request
from google.cloud.dataplex_v1.types import business_glossary

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseBusinessGlossaryServiceRestTransport

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


class BusinessGlossaryServiceRestInterceptor:
    """Interceptor for BusinessGlossaryService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the BusinessGlossaryServiceRestTransport.

    .. code-block:: python
        class MyCustomBusinessGlossaryServiceInterceptor(BusinessGlossaryServiceRestInterceptor):
            def pre_create_glossary(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_glossary(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_glossary_category(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_glossary_category(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_glossary_term(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_glossary_term(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_glossary(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_glossary(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_glossary_category(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_glossary_term(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_glossary(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_glossary(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_glossary_category(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_glossary_category(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_glossary_term(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_glossary_term(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_glossaries(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_glossaries(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_glossary_categories(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_glossary_categories(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_glossary_terms(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_glossary_terms(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_glossary(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_glossary(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_glossary_category(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_glossary_category(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_glossary_term(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_glossary_term(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = BusinessGlossaryServiceRestTransport(interceptor=MyCustomBusinessGlossaryServiceInterceptor())
        client = BusinessGlossaryServiceClient(transport=transport)


    """

    def pre_create_glossary(
        self,
        request: business_glossary.CreateGlossaryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        business_glossary.CreateGlossaryRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_glossary

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BusinessGlossaryService server.
        """
        return request, metadata

    def post_create_glossary(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_glossary

        DEPRECATED. Please use the `post_create_glossary_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BusinessGlossaryService server but before
        it is returned to user code. This `post_create_glossary` interceptor runs
        before the `post_create_glossary_with_metadata` interceptor.
        """
        return response

    def post_create_glossary_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_glossary

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BusinessGlossaryService server but before it is returned to user code.

        We recommend only using this `post_create_glossary_with_metadata`
        interceptor in new development instead of the `post_create_glossary` interceptor.
        When both interceptors are used, this `post_create_glossary_with_metadata` interceptor runs after the
        `post_create_glossary` interceptor. The (possibly modified) response returned by
        `post_create_glossary` will be passed to
        `post_create_glossary_with_metadata`.
        """
        return response, metadata

    def pre_create_glossary_category(
        self,
        request: business_glossary.CreateGlossaryCategoryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        business_glossary.CreateGlossaryCategoryRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_glossary_category

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BusinessGlossaryService server.
        """
        return request, metadata

    def post_create_glossary_category(
        self, response: business_glossary.GlossaryCategory
    ) -> business_glossary.GlossaryCategory:
        """Post-rpc interceptor for create_glossary_category

        DEPRECATED. Please use the `post_create_glossary_category_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BusinessGlossaryService server but before
        it is returned to user code. This `post_create_glossary_category` interceptor runs
        before the `post_create_glossary_category_with_metadata` interceptor.
        """
        return response

    def post_create_glossary_category_with_metadata(
        self,
        response: business_glossary.GlossaryCategory,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        business_glossary.GlossaryCategory, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for create_glossary_category

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BusinessGlossaryService server but before it is returned to user code.

        We recommend only using this `post_create_glossary_category_with_metadata`
        interceptor in new development instead of the `post_create_glossary_category` interceptor.
        When both interceptors are used, this `post_create_glossary_category_with_metadata` interceptor runs after the
        `post_create_glossary_category` interceptor. The (possibly modified) response returned by
        `post_create_glossary_category` will be passed to
        `post_create_glossary_category_with_metadata`.
        """
        return response, metadata

    def pre_create_glossary_term(
        self,
        request: business_glossary.CreateGlossaryTermRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        business_glossary.CreateGlossaryTermRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_glossary_term

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BusinessGlossaryService server.
        """
        return request, metadata

    def post_create_glossary_term(
        self, response: business_glossary.GlossaryTerm
    ) -> business_glossary.GlossaryTerm:
        """Post-rpc interceptor for create_glossary_term

        DEPRECATED. Please use the `post_create_glossary_term_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BusinessGlossaryService server but before
        it is returned to user code. This `post_create_glossary_term` interceptor runs
        before the `post_create_glossary_term_with_metadata` interceptor.
        """
        return response

    def post_create_glossary_term_with_metadata(
        self,
        response: business_glossary.GlossaryTerm,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[business_glossary.GlossaryTerm, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_glossary_term

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BusinessGlossaryService server but before it is returned to user code.

        We recommend only using this `post_create_glossary_term_with_metadata`
        interceptor in new development instead of the `post_create_glossary_term` interceptor.
        When both interceptors are used, this `post_create_glossary_term_with_metadata` interceptor runs after the
        `post_create_glossary_term` interceptor. The (possibly modified) response returned by
        `post_create_glossary_term` will be passed to
        `post_create_glossary_term_with_metadata`.
        """
        return response, metadata

    def pre_delete_glossary(
        self,
        request: business_glossary.DeleteGlossaryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        business_glossary.DeleteGlossaryRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_glossary

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BusinessGlossaryService server.
        """
        return request, metadata

    def post_delete_glossary(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_glossary

        DEPRECATED. Please use the `post_delete_glossary_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BusinessGlossaryService server but before
        it is returned to user code. This `post_delete_glossary` interceptor runs
        before the `post_delete_glossary_with_metadata` interceptor.
        """
        return response

    def post_delete_glossary_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_glossary

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BusinessGlossaryService server but before it is returned to user code.

        We recommend only using this `post_delete_glossary_with_metadata`
        interceptor in new development instead of the `post_delete_glossary` interceptor.
        When both interceptors are used, this `post_delete_glossary_with_metadata` interceptor runs after the
        `post_delete_glossary` interceptor. The (possibly modified) response returned by
        `post_delete_glossary` will be passed to
        `post_delete_glossary_with_metadata`.
        """
        return response, metadata

    def pre_delete_glossary_category(
        self,
        request: business_glossary.DeleteGlossaryCategoryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        business_glossary.DeleteGlossaryCategoryRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_glossary_category

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BusinessGlossaryService server.
        """
        return request, metadata

    def pre_delete_glossary_term(
        self,
        request: business_glossary.DeleteGlossaryTermRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        business_glossary.DeleteGlossaryTermRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_glossary_term

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BusinessGlossaryService server.
        """
        return request, metadata

    def pre_get_glossary(
        self,
        request: business_glossary.GetGlossaryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        business_glossary.GetGlossaryRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_glossary

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BusinessGlossaryService server.
        """
        return request, metadata

    def post_get_glossary(
        self, response: business_glossary.Glossary
    ) -> business_glossary.Glossary:
        """Post-rpc interceptor for get_glossary

        DEPRECATED. Please use the `post_get_glossary_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BusinessGlossaryService server but before
        it is returned to user code. This `post_get_glossary` interceptor runs
        before the `post_get_glossary_with_metadata` interceptor.
        """
        return response

    def post_get_glossary_with_metadata(
        self,
        response: business_glossary.Glossary,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[business_glossary.Glossary, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_glossary

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BusinessGlossaryService server but before it is returned to user code.

        We recommend only using this `post_get_glossary_with_metadata`
        interceptor in new development instead of the `post_get_glossary` interceptor.
        When both interceptors are used, this `post_get_glossary_with_metadata` interceptor runs after the
        `post_get_glossary` interceptor. The (possibly modified) response returned by
        `post_get_glossary` will be passed to
        `post_get_glossary_with_metadata`.
        """
        return response, metadata

    def pre_get_glossary_category(
        self,
        request: business_glossary.GetGlossaryCategoryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        business_glossary.GetGlossaryCategoryRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_glossary_category

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BusinessGlossaryService server.
        """
        return request, metadata

    def post_get_glossary_category(
        self, response: business_glossary.GlossaryCategory
    ) -> business_glossary.GlossaryCategory:
        """Post-rpc interceptor for get_glossary_category

        DEPRECATED. Please use the `post_get_glossary_category_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BusinessGlossaryService server but before
        it is returned to user code. This `post_get_glossary_category` interceptor runs
        before the `post_get_glossary_category_with_metadata` interceptor.
        """
        return response

    def post_get_glossary_category_with_metadata(
        self,
        response: business_glossary.GlossaryCategory,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        business_glossary.GlossaryCategory, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_glossary_category

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BusinessGlossaryService server but before it is returned to user code.

        We recommend only using this `post_get_glossary_category_with_metadata`
        interceptor in new development instead of the `post_get_glossary_category` interceptor.
        When both interceptors are used, this `post_get_glossary_category_with_metadata` interceptor runs after the
        `post_get_glossary_category` interceptor. The (possibly modified) response returned by
        `post_get_glossary_category` will be passed to
        `post_get_glossary_category_with_metadata`.
        """
        return response, metadata

    def pre_get_glossary_term(
        self,
        request: business_glossary.GetGlossaryTermRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        business_glossary.GetGlossaryTermRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_glossary_term

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BusinessGlossaryService server.
        """
        return request, metadata

    def post_get_glossary_term(
        self, response: business_glossary.GlossaryTerm
    ) -> business_glossary.GlossaryTerm:
        """Post-rpc interceptor for get_glossary_term

        DEPRECATED. Please use the `post_get_glossary_term_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BusinessGlossaryService server but before
        it is returned to user code. This `post_get_glossary_term` interceptor runs
        before the `post_get_glossary_term_with_metadata` interceptor.
        """
        return response

    def post_get_glossary_term_with_metadata(
        self,
        response: business_glossary.GlossaryTerm,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[business_glossary.GlossaryTerm, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_glossary_term

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BusinessGlossaryService server but before it is returned to user code.

        We recommend only using this `post_get_glossary_term_with_metadata`
        interceptor in new development instead of the `post_get_glossary_term` interceptor.
        When both interceptors are used, this `post_get_glossary_term_with_metadata` interceptor runs after the
        `post_get_glossary_term` interceptor. The (possibly modified) response returned by
        `post_get_glossary_term` will be passed to
        `post_get_glossary_term_with_metadata`.
        """
        return response, metadata

    def pre_list_glossaries(
        self,
        request: business_glossary.ListGlossariesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        business_glossary.ListGlossariesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_glossaries

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BusinessGlossaryService server.
        """
        return request, metadata

    def post_list_glossaries(
        self, response: business_glossary.ListGlossariesResponse
    ) -> business_glossary.ListGlossariesResponse:
        """Post-rpc interceptor for list_glossaries

        DEPRECATED. Please use the `post_list_glossaries_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BusinessGlossaryService server but before
        it is returned to user code. This `post_list_glossaries` interceptor runs
        before the `post_list_glossaries_with_metadata` interceptor.
        """
        return response

    def post_list_glossaries_with_metadata(
        self,
        response: business_glossary.ListGlossariesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        business_glossary.ListGlossariesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_glossaries

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BusinessGlossaryService server but before it is returned to user code.

        We recommend only using this `post_list_glossaries_with_metadata`
        interceptor in new development instead of the `post_list_glossaries` interceptor.
        When both interceptors are used, this `post_list_glossaries_with_metadata` interceptor runs after the
        `post_list_glossaries` interceptor. The (possibly modified) response returned by
        `post_list_glossaries` will be passed to
        `post_list_glossaries_with_metadata`.
        """
        return response, metadata

    def pre_list_glossary_categories(
        self,
        request: business_glossary.ListGlossaryCategoriesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        business_glossary.ListGlossaryCategoriesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_glossary_categories

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BusinessGlossaryService server.
        """
        return request, metadata

    def post_list_glossary_categories(
        self, response: business_glossary.ListGlossaryCategoriesResponse
    ) -> business_glossary.ListGlossaryCategoriesResponse:
        """Post-rpc interceptor for list_glossary_categories

        DEPRECATED. Please use the `post_list_glossary_categories_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BusinessGlossaryService server but before
        it is returned to user code. This `post_list_glossary_categories` interceptor runs
        before the `post_list_glossary_categories_with_metadata` interceptor.
        """
        return response

    def post_list_glossary_categories_with_metadata(
        self,
        response: business_glossary.ListGlossaryCategoriesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        business_glossary.ListGlossaryCategoriesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_glossary_categories

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BusinessGlossaryService server but before it is returned to user code.

        We recommend only using this `post_list_glossary_categories_with_metadata`
        interceptor in new development instead of the `post_list_glossary_categories` interceptor.
        When both interceptors are used, this `post_list_glossary_categories_with_metadata` interceptor runs after the
        `post_list_glossary_categories` interceptor. The (possibly modified) response returned by
        `post_list_glossary_categories` will be passed to
        `post_list_glossary_categories_with_metadata`.
        """
        return response, metadata

    def pre_list_glossary_terms(
        self,
        request: business_glossary.ListGlossaryTermsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        business_glossary.ListGlossaryTermsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_glossary_terms

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BusinessGlossaryService server.
        """
        return request, metadata

    def post_list_glossary_terms(
        self, response: business_glossary.ListGlossaryTermsResponse
    ) -> business_glossary.ListGlossaryTermsResponse:
        """Post-rpc interceptor for list_glossary_terms

        DEPRECATED. Please use the `post_list_glossary_terms_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BusinessGlossaryService server but before
        it is returned to user code. This `post_list_glossary_terms` interceptor runs
        before the `post_list_glossary_terms_with_metadata` interceptor.
        """
        return response

    def post_list_glossary_terms_with_metadata(
        self,
        response: business_glossary.ListGlossaryTermsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        business_glossary.ListGlossaryTermsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_glossary_terms

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BusinessGlossaryService server but before it is returned to user code.

        We recommend only using this `post_list_glossary_terms_with_metadata`
        interceptor in new development instead of the `post_list_glossary_terms` interceptor.
        When both interceptors are used, this `post_list_glossary_terms_with_metadata` interceptor runs after the
        `post_list_glossary_terms` interceptor. The (possibly modified) response returned by
        `post_list_glossary_terms` will be passed to
        `post_list_glossary_terms_with_metadata`.
        """
        return response, metadata

    def pre_update_glossary(
        self,
        request: business_glossary.UpdateGlossaryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        business_glossary.UpdateGlossaryRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_glossary

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BusinessGlossaryService server.
        """
        return request, metadata

    def post_update_glossary(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_glossary

        DEPRECATED. Please use the `post_update_glossary_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BusinessGlossaryService server but before
        it is returned to user code. This `post_update_glossary` interceptor runs
        before the `post_update_glossary_with_metadata` interceptor.
        """
        return response

    def post_update_glossary_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_glossary

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BusinessGlossaryService server but before it is returned to user code.

        We recommend only using this `post_update_glossary_with_metadata`
        interceptor in new development instead of the `post_update_glossary` interceptor.
        When both interceptors are used, this `post_update_glossary_with_metadata` interceptor runs after the
        `post_update_glossary` interceptor. The (possibly modified) response returned by
        `post_update_glossary` will be passed to
        `post_update_glossary_with_metadata`.
        """
        return response, metadata

    def pre_update_glossary_category(
        self,
        request: business_glossary.UpdateGlossaryCategoryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        business_glossary.UpdateGlossaryCategoryRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_glossary_category

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BusinessGlossaryService server.
        """
        return request, metadata

    def post_update_glossary_category(
        self, response: business_glossary.GlossaryCategory
    ) -> business_glossary.GlossaryCategory:
        """Post-rpc interceptor for update_glossary_category

        DEPRECATED. Please use the `post_update_glossary_category_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BusinessGlossaryService server but before
        it is returned to user code. This `post_update_glossary_category` interceptor runs
        before the `post_update_glossary_category_with_metadata` interceptor.
        """
        return response

    def post_update_glossary_category_with_metadata(
        self,
        response: business_glossary.GlossaryCategory,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        business_glossary.GlossaryCategory, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for update_glossary_category

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BusinessGlossaryService server but before it is returned to user code.

        We recommend only using this `post_update_glossary_category_with_metadata`
        interceptor in new development instead of the `post_update_glossary_category` interceptor.
        When both interceptors are used, this `post_update_glossary_category_with_metadata` interceptor runs after the
        `post_update_glossary_category` interceptor. The (possibly modified) response returned by
        `post_update_glossary_category` will be passed to
        `post_update_glossary_category_with_metadata`.
        """
        return response, metadata

    def pre_update_glossary_term(
        self,
        request: business_glossary.UpdateGlossaryTermRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        business_glossary.UpdateGlossaryTermRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_glossary_term

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BusinessGlossaryService server.
        """
        return request, metadata

    def post_update_glossary_term(
        self, response: business_glossary.GlossaryTerm
    ) -> business_glossary.GlossaryTerm:
        """Post-rpc interceptor for update_glossary_term

        DEPRECATED. Please use the `post_update_glossary_term_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BusinessGlossaryService server but before
        it is returned to user code. This `post_update_glossary_term` interceptor runs
        before the `post_update_glossary_term_with_metadata` interceptor.
        """
        return response

    def post_update_glossary_term_with_metadata(
        self,
        response: business_glossary.GlossaryTerm,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[business_glossary.GlossaryTerm, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_glossary_term

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BusinessGlossaryService server but before it is returned to user code.

        We recommend only using this `post_update_glossary_term_with_metadata`
        interceptor in new development instead of the `post_update_glossary_term` interceptor.
        When both interceptors are used, this `post_update_glossary_term_with_metadata` interceptor runs after the
        `post_update_glossary_term` interceptor. The (possibly modified) response returned by
        `post_update_glossary_term` will be passed to
        `post_update_glossary_term_with_metadata`.
        """
        return response, metadata

    def pre_get_location(
        self,
        request: locations_pb2.GetLocationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        locations_pb2.GetLocationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_location

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BusinessGlossaryService server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the BusinessGlossaryService server but before
        it is returned to user code.
        """
        return response

    def pre_list_locations(
        self,
        request: locations_pb2.ListLocationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        locations_pb2.ListLocationsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_locations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BusinessGlossaryService server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the BusinessGlossaryService server but before
        it is returned to user code.
        """
        return response

    def pre_get_iam_policy(
        self,
        request: iam_policy_pb2.GetIamPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.GetIamPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BusinessGlossaryService server.
        """
        return request, metadata

    def post_get_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the BusinessGlossaryService server but before
        it is returned to user code.
        """
        return response

    def pre_set_iam_policy(
        self,
        request: iam_policy_pb2.SetIamPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.SetIamPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BusinessGlossaryService server.
        """
        return request, metadata

    def post_set_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the BusinessGlossaryService server but before
        it is returned to user code.
        """
        return response

    def pre_test_iam_permissions(
        self,
        request: iam_policy_pb2.TestIamPermissionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.TestIamPermissionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BusinessGlossaryService server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the response
        after it is returned by the BusinessGlossaryService server but before
        it is returned to user code.
        """
        return response

    def pre_cancel_operation(
        self,
        request: operations_pb2.CancelOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.CancelOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BusinessGlossaryService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the BusinessGlossaryService server but before
        it is returned to user code.
        """
        return response

    def pre_delete_operation(
        self,
        request: operations_pb2.DeleteOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.DeleteOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BusinessGlossaryService server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the BusinessGlossaryService server but before
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
        before they are sent to the BusinessGlossaryService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the BusinessGlossaryService server but before
        it is returned to user code.
        """
        return response

    def pre_list_operations(
        self,
        request: operations_pb2.ListOperationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.ListOperationsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_operations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BusinessGlossaryService server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the BusinessGlossaryService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class BusinessGlossaryServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: BusinessGlossaryServiceRestInterceptor


class BusinessGlossaryServiceRestTransport(_BaseBusinessGlossaryServiceRestTransport):
    """REST backend synchronous transport for BusinessGlossaryService.

    BusinessGlossaryService provides APIs for managing business
    glossary resources for enterprise customers.
    The resources currently supported in Business Glossary are:

    1. Glossary
    2. GlossaryCategory
    3. GlossaryTerm

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "dataplex.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[BusinessGlossaryServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'dataplex.googleapis.com').
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
            interceptor (Optional[BusinessGlossaryServiceRestInterceptor]): Interceptor used
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
        self._operations_client: Optional[operations_v1.AbstractOperationsClient] = None
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or BusinessGlossaryServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    @property
    def operations_client(self) -> operations_v1.AbstractOperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Only create a new client if we do not already have one.
        if self._operations_client is None:
            http_options: Dict[str, List[Dict[str, str]]] = {
                "google.longrunning.Operations.CancelOperation": [
                    {
                        "method": "post",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}:cancel",
                        "body": "*",
                    },
                    {
                        "method": "post",
                        "uri": "/v1/{name=organizations/*/locations/*/operations/*}:cancel",
                        "body": "*",
                    },
                ],
                "google.longrunning.Operations.DeleteOperation": [
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}",
                    },
                    {
                        "method": "delete",
                        "uri": "/v1/{name=organizations/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=organizations/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.ListOperations": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v1/{name=organizations/*/locations/*}/operations",
                    },
                ],
            }

            rest_transport = operations_v1.OperationsRestTransport(
                host=self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                scopes=self._scopes,
                http_options=http_options,
                path_prefix="v1",
            )

            self._operations_client = operations_v1.AbstractOperationsClient(
                transport=rest_transport
            )

        # Return the client from cache.
        return self._operations_client

    class _CreateGlossary(
        _BaseBusinessGlossaryServiceRestTransport._BaseCreateGlossary,
        BusinessGlossaryServiceRestStub,
    ):
        def __hash__(self):
            return hash("BusinessGlossaryServiceRestTransport.CreateGlossary")

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
            request: business_glossary.CreateGlossaryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create glossary method over HTTP.

            Args:
                request (~.business_glossary.CreateGlossaryRequest):
                    The request object. Create Glossary Request
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = _BaseBusinessGlossaryServiceRestTransport._BaseCreateGlossary._get_http_options()
            request, metadata = self._interceptor.pre_create_glossary(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBusinessGlossaryServiceRestTransport._BaseCreateGlossary,
                    "_BaseCreateGlossary__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dataplex_v1.BusinessGlossaryServiceClient.CreateGlossary",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "CreateGlossary",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                BusinessGlossaryServiceRestTransport._CreateGlossary._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_glossary(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_glossary_with_metadata(
                resp, response_metadata
            )
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
                    "Received response for google.cloud.dataplex_v1.BusinessGlossaryServiceClient.create_glossary",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "CreateGlossary",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateGlossaryCategory(
        _BaseBusinessGlossaryServiceRestTransport._BaseCreateGlossaryCategory,
        BusinessGlossaryServiceRestStub,
    ):
        def __hash__(self):
            return hash("BusinessGlossaryServiceRestTransport.CreateGlossaryCategory")

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
            request: business_glossary.CreateGlossaryCategoryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> business_glossary.GlossaryCategory:
            r"""Call the create glossary category method over HTTP.

            Args:
                request (~.business_glossary.CreateGlossaryCategoryRequest):
                    The request object. Creates a new GlossaryCategory under
                the specified Glossary.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.business_glossary.GlossaryCategory:
                    A GlossaryCategory represents a
                collection of GlossaryCategories and
                GlossaryTerms within a Glossary that are
                related to each other.

            """

            http_options = _BaseBusinessGlossaryServiceRestTransport._BaseCreateGlossaryCategory._get_http_options()
            request, metadata = self._interceptor.pre_create_glossary_category(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBusinessGlossaryServiceRestTransport._BaseCreateGlossaryCategory,
                    "_BaseCreateGlossaryCategory__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dataplex_v1.BusinessGlossaryServiceClient.CreateGlossaryCategory",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "CreateGlossaryCategory",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BusinessGlossaryServiceRestTransport._CreateGlossaryCategory._get_response(
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
            resp = business_glossary.GlossaryCategory()
            pb_resp = business_glossary.GlossaryCategory.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_glossary_category(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_glossary_category_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = business_glossary.GlossaryCategory.to_json(
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
                    "Received response for google.cloud.dataplex_v1.BusinessGlossaryServiceClient.create_glossary_category",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "CreateGlossaryCategory",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateGlossaryTerm(
        _BaseBusinessGlossaryServiceRestTransport._BaseCreateGlossaryTerm,
        BusinessGlossaryServiceRestStub,
    ):
        def __hash__(self):
            return hash("BusinessGlossaryServiceRestTransport.CreateGlossaryTerm")

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
            request: business_glossary.CreateGlossaryTermRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> business_glossary.GlossaryTerm:
            r"""Call the create glossary term method over HTTP.

            Args:
                request (~.business_glossary.CreateGlossaryTermRequest):
                    The request object. Creates a new GlossaryTerm under the
                specified Glossary.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.business_glossary.GlossaryTerm:
                    GlossaryTerms are the core of
                Glossary. A GlossaryTerm holds a rich
                text description that can be attached to
                Entries or specific columns to enrich
                them.

            """

            http_options = _BaseBusinessGlossaryServiceRestTransport._BaseCreateGlossaryTerm._get_http_options()
            request, metadata = self._interceptor.pre_create_glossary_term(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBusinessGlossaryServiceRestTransport._BaseCreateGlossaryTerm,
                    "_BaseCreateGlossaryTerm__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dataplex_v1.BusinessGlossaryServiceClient.CreateGlossaryTerm",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "CreateGlossaryTerm",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                BusinessGlossaryServiceRestTransport._CreateGlossaryTerm._get_response(
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
            resp = business_glossary.GlossaryTerm()
            pb_resp = business_glossary.GlossaryTerm.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_glossary_term(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_glossary_term_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = business_glossary.GlossaryTerm.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataplex_v1.BusinessGlossaryServiceClient.create_glossary_term",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "CreateGlossaryTerm",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteGlossary(
        _BaseBusinessGlossaryServiceRestTransport._BaseDeleteGlossary,
        BusinessGlossaryServiceRestStub,
    ):
        def __hash__(self):
            return hash("BusinessGlossaryServiceRestTransport.DeleteGlossary")

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
            request: business_glossary.DeleteGlossaryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete glossary method over HTTP.

            Args:
                request (~.business_glossary.DeleteGlossaryRequest):
                    The request object. Delete Glossary Request
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = _BaseBusinessGlossaryServiceRestTransport._BaseDeleteGlossary._get_http_options()
            request, metadata = self._interceptor.pre_delete_glossary(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBusinessGlossaryServiceRestTransport._BaseDeleteGlossary,
                    "_BaseDeleteGlossary__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dataplex_v1.BusinessGlossaryServiceClient.DeleteGlossary",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "DeleteGlossary",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                BusinessGlossaryServiceRestTransport._DeleteGlossary._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_glossary(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_glossary_with_metadata(
                resp, response_metadata
            )
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
                    "Received response for google.cloud.dataplex_v1.BusinessGlossaryServiceClient.delete_glossary",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "DeleteGlossary",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteGlossaryCategory(
        _BaseBusinessGlossaryServiceRestTransport._BaseDeleteGlossaryCategory,
        BusinessGlossaryServiceRestStub,
    ):
        def __hash__(self):
            return hash("BusinessGlossaryServiceRestTransport.DeleteGlossaryCategory")

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
            request: business_glossary.DeleteGlossaryCategoryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete glossary category method over HTTP.

            Args:
                request (~.business_glossary.DeleteGlossaryCategoryRequest):
                    The request object. Delete GlossaryCategory Request
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseBusinessGlossaryServiceRestTransport._BaseDeleteGlossaryCategory._get_http_options()
            request, metadata = self._interceptor.pre_delete_glossary_category(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBusinessGlossaryServiceRestTransport._BaseDeleteGlossaryCategory,
                    "_BaseDeleteGlossaryCategory__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dataplex_v1.BusinessGlossaryServiceClient.DeleteGlossaryCategory",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "DeleteGlossaryCategory",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BusinessGlossaryServiceRestTransport._DeleteGlossaryCategory._get_response(
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

    class _DeleteGlossaryTerm(
        _BaseBusinessGlossaryServiceRestTransport._BaseDeleteGlossaryTerm,
        BusinessGlossaryServiceRestStub,
    ):
        def __hash__(self):
            return hash("BusinessGlossaryServiceRestTransport.DeleteGlossaryTerm")

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
            request: business_glossary.DeleteGlossaryTermRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete glossary term method over HTTP.

            Args:
                request (~.business_glossary.DeleteGlossaryTermRequest):
                    The request object. Delete GlossaryTerm Request
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseBusinessGlossaryServiceRestTransport._BaseDeleteGlossaryTerm._get_http_options()
            request, metadata = self._interceptor.pre_delete_glossary_term(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBusinessGlossaryServiceRestTransport._BaseDeleteGlossaryTerm,
                    "_BaseDeleteGlossaryTerm__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dataplex_v1.BusinessGlossaryServiceClient.DeleteGlossaryTerm",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "DeleteGlossaryTerm",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                BusinessGlossaryServiceRestTransport._DeleteGlossaryTerm._get_response(
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

    class _GetGlossary(
        _BaseBusinessGlossaryServiceRestTransport._BaseGetGlossary,
        BusinessGlossaryServiceRestStub,
    ):
        def __hash__(self):
            return hash("BusinessGlossaryServiceRestTransport.GetGlossary")

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
            request: business_glossary.GetGlossaryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> business_glossary.Glossary:
            r"""Call the get glossary method over HTTP.

            Args:
                request (~.business_glossary.GetGlossaryRequest):
                    The request object. Get Glossary Request
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.business_glossary.Glossary:
                    A Glossary represents a collection of
                GlossaryCategories and GlossaryTerms
                defined by the user. Glossary is a top
                level resource and is the Google Cloud
                parent resource of all the
                GlossaryCategories and GlossaryTerms
                within it.

            """

            http_options = _BaseBusinessGlossaryServiceRestTransport._BaseGetGlossary._get_http_options()
            request, metadata = self._interceptor.pre_get_glossary(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBusinessGlossaryServiceRestTransport._BaseGetGlossary,
                    "_BaseGetGlossary__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dataplex_v1.BusinessGlossaryServiceClient.GetGlossary",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "GetGlossary",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BusinessGlossaryServiceRestTransport._GetGlossary._get_response(
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
            resp = business_glossary.Glossary()
            pb_resp = business_glossary.Glossary.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_glossary(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_glossary_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = business_glossary.Glossary.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataplex_v1.BusinessGlossaryServiceClient.get_glossary",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "GetGlossary",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetGlossaryCategory(
        _BaseBusinessGlossaryServiceRestTransport._BaseGetGlossaryCategory,
        BusinessGlossaryServiceRestStub,
    ):
        def __hash__(self):
            return hash("BusinessGlossaryServiceRestTransport.GetGlossaryCategory")

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
            request: business_glossary.GetGlossaryCategoryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> business_glossary.GlossaryCategory:
            r"""Call the get glossary category method over HTTP.

            Args:
                request (~.business_glossary.GetGlossaryCategoryRequest):
                    The request object. Get GlossaryCategory Request
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.business_glossary.GlossaryCategory:
                    A GlossaryCategory represents a
                collection of GlossaryCategories and
                GlossaryTerms within a Glossary that are
                related to each other.

            """

            http_options = _BaseBusinessGlossaryServiceRestTransport._BaseGetGlossaryCategory._get_http_options()
            request, metadata = self._interceptor.pre_get_glossary_category(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBusinessGlossaryServiceRestTransport._BaseGetGlossaryCategory,
                    "_BaseGetGlossaryCategory__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dataplex_v1.BusinessGlossaryServiceClient.GetGlossaryCategory",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "GetGlossaryCategory",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                BusinessGlossaryServiceRestTransport._GetGlossaryCategory._get_response(
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
            resp = business_glossary.GlossaryCategory()
            pb_resp = business_glossary.GlossaryCategory.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_glossary_category(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_glossary_category_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = business_glossary.GlossaryCategory.to_json(
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
                    "Received response for google.cloud.dataplex_v1.BusinessGlossaryServiceClient.get_glossary_category",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "GetGlossaryCategory",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetGlossaryTerm(
        _BaseBusinessGlossaryServiceRestTransport._BaseGetGlossaryTerm,
        BusinessGlossaryServiceRestStub,
    ):
        def __hash__(self):
            return hash("BusinessGlossaryServiceRestTransport.GetGlossaryTerm")

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
            request: business_glossary.GetGlossaryTermRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> business_glossary.GlossaryTerm:
            r"""Call the get glossary term method over HTTP.

            Args:
                request (~.business_glossary.GetGlossaryTermRequest):
                    The request object. Get GlossaryTerm Request
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.business_glossary.GlossaryTerm:
                    GlossaryTerms are the core of
                Glossary. A GlossaryTerm holds a rich
                text description that can be attached to
                Entries or specific columns to enrich
                them.

            """

            http_options = _BaseBusinessGlossaryServiceRestTransport._BaseGetGlossaryTerm._get_http_options()
            request, metadata = self._interceptor.pre_get_glossary_term(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBusinessGlossaryServiceRestTransport._BaseGetGlossaryTerm,
                    "_BaseGetGlossaryTerm__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dataplex_v1.BusinessGlossaryServiceClient.GetGlossaryTerm",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "GetGlossaryTerm",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                BusinessGlossaryServiceRestTransport._GetGlossaryTerm._get_response(
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
            resp = business_glossary.GlossaryTerm()
            pb_resp = business_glossary.GlossaryTerm.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_glossary_term(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_glossary_term_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = business_glossary.GlossaryTerm.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataplex_v1.BusinessGlossaryServiceClient.get_glossary_term",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "GetGlossaryTerm",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListGlossaries(
        _BaseBusinessGlossaryServiceRestTransport._BaseListGlossaries,
        BusinessGlossaryServiceRestStub,
    ):
        def __hash__(self):
            return hash("BusinessGlossaryServiceRestTransport.ListGlossaries")

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
            request: business_glossary.ListGlossariesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> business_glossary.ListGlossariesResponse:
            r"""Call the list glossaries method over HTTP.

            Args:
                request (~.business_glossary.ListGlossariesRequest):
                    The request object. List Glossaries Request
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.business_glossary.ListGlossariesResponse:
                    List Glossaries Response
            """

            http_options = _BaseBusinessGlossaryServiceRestTransport._BaseListGlossaries._get_http_options()
            request, metadata = self._interceptor.pre_list_glossaries(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBusinessGlossaryServiceRestTransport._BaseListGlossaries,
                    "_BaseListGlossaries__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dataplex_v1.BusinessGlossaryServiceClient.ListGlossaries",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "ListGlossaries",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                BusinessGlossaryServiceRestTransport._ListGlossaries._get_response(
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
            resp = business_glossary.ListGlossariesResponse()
            pb_resp = business_glossary.ListGlossariesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_glossaries(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_glossaries_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = business_glossary.ListGlossariesResponse.to_json(
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
                    "Received response for google.cloud.dataplex_v1.BusinessGlossaryServiceClient.list_glossaries",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "ListGlossaries",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListGlossaryCategories(
        _BaseBusinessGlossaryServiceRestTransport._BaseListGlossaryCategories,
        BusinessGlossaryServiceRestStub,
    ):
        def __hash__(self):
            return hash("BusinessGlossaryServiceRestTransport.ListGlossaryCategories")

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
            request: business_glossary.ListGlossaryCategoriesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> business_glossary.ListGlossaryCategoriesResponse:
            r"""Call the list glossary categories method over HTTP.

            Args:
                request (~.business_glossary.ListGlossaryCategoriesRequest):
                    The request object. List GlossaryCategories Request
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.business_glossary.ListGlossaryCategoriesResponse:
                    List GlossaryCategories Response
            """

            http_options = _BaseBusinessGlossaryServiceRestTransport._BaseListGlossaryCategories._get_http_options()
            request, metadata = self._interceptor.pre_list_glossary_categories(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBusinessGlossaryServiceRestTransport._BaseListGlossaryCategories,
                    "_BaseListGlossaryCategories__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dataplex_v1.BusinessGlossaryServiceClient.ListGlossaryCategories",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "ListGlossaryCategories",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BusinessGlossaryServiceRestTransport._ListGlossaryCategories._get_response(
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
            resp = business_glossary.ListGlossaryCategoriesResponse()
            pb_resp = business_glossary.ListGlossaryCategoriesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_glossary_categories(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_glossary_categories_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        business_glossary.ListGlossaryCategoriesResponse.to_json(
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
                    "Received response for google.cloud.dataplex_v1.BusinessGlossaryServiceClient.list_glossary_categories",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "ListGlossaryCategories",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListGlossaryTerms(
        _BaseBusinessGlossaryServiceRestTransport._BaseListGlossaryTerms,
        BusinessGlossaryServiceRestStub,
    ):
        def __hash__(self):
            return hash("BusinessGlossaryServiceRestTransport.ListGlossaryTerms")

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
            request: business_glossary.ListGlossaryTermsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> business_glossary.ListGlossaryTermsResponse:
            r"""Call the list glossary terms method over HTTP.

            Args:
                request (~.business_glossary.ListGlossaryTermsRequest):
                    The request object. List GlossaryTerms Request
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.business_glossary.ListGlossaryTermsResponse:
                    List GlossaryTerms Response
            """

            http_options = _BaseBusinessGlossaryServiceRestTransport._BaseListGlossaryTerms._get_http_options()
            request, metadata = self._interceptor.pre_list_glossary_terms(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBusinessGlossaryServiceRestTransport._BaseListGlossaryTerms,
                    "_BaseListGlossaryTerms__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dataplex_v1.BusinessGlossaryServiceClient.ListGlossaryTerms",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "ListGlossaryTerms",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                BusinessGlossaryServiceRestTransport._ListGlossaryTerms._get_response(
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
            resp = business_glossary.ListGlossaryTermsResponse()
            pb_resp = business_glossary.ListGlossaryTermsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_glossary_terms(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_glossary_terms_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        business_glossary.ListGlossaryTermsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataplex_v1.BusinessGlossaryServiceClient.list_glossary_terms",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "ListGlossaryTerms",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateGlossary(
        _BaseBusinessGlossaryServiceRestTransport._BaseUpdateGlossary,
        BusinessGlossaryServiceRestStub,
    ):
        def __hash__(self):
            return hash("BusinessGlossaryServiceRestTransport.UpdateGlossary")

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
            request: business_glossary.UpdateGlossaryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update glossary method over HTTP.

            Args:
                request (~.business_glossary.UpdateGlossaryRequest):
                    The request object. Update Glossary Request
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = _BaseBusinessGlossaryServiceRestTransport._BaseUpdateGlossary._get_http_options()
            request, metadata = self._interceptor.pre_update_glossary(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBusinessGlossaryServiceRestTransport._BaseUpdateGlossary,
                    "_BaseUpdateGlossary__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dataplex_v1.BusinessGlossaryServiceClient.UpdateGlossary",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "UpdateGlossary",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                BusinessGlossaryServiceRestTransport._UpdateGlossary._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_glossary(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_glossary_with_metadata(
                resp, response_metadata
            )
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
                    "Received response for google.cloud.dataplex_v1.BusinessGlossaryServiceClient.update_glossary",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "UpdateGlossary",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateGlossaryCategory(
        _BaseBusinessGlossaryServiceRestTransport._BaseUpdateGlossaryCategory,
        BusinessGlossaryServiceRestStub,
    ):
        def __hash__(self):
            return hash("BusinessGlossaryServiceRestTransport.UpdateGlossaryCategory")

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
            request: business_glossary.UpdateGlossaryCategoryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> business_glossary.GlossaryCategory:
            r"""Call the update glossary category method over HTTP.

            Args:
                request (~.business_glossary.UpdateGlossaryCategoryRequest):
                    The request object. Update GlossaryCategory Request
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.business_glossary.GlossaryCategory:
                    A GlossaryCategory represents a
                collection of GlossaryCategories and
                GlossaryTerms within a Glossary that are
                related to each other.

            """

            http_options = _BaseBusinessGlossaryServiceRestTransport._BaseUpdateGlossaryCategory._get_http_options()
            request, metadata = self._interceptor.pre_update_glossary_category(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBusinessGlossaryServiceRestTransport._BaseUpdateGlossaryCategory,
                    "_BaseUpdateGlossaryCategory__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dataplex_v1.BusinessGlossaryServiceClient.UpdateGlossaryCategory",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "UpdateGlossaryCategory",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BusinessGlossaryServiceRestTransport._UpdateGlossaryCategory._get_response(
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
            resp = business_glossary.GlossaryCategory()
            pb_resp = business_glossary.GlossaryCategory.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_glossary_category(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_glossary_category_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = business_glossary.GlossaryCategory.to_json(
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
                    "Received response for google.cloud.dataplex_v1.BusinessGlossaryServiceClient.update_glossary_category",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "UpdateGlossaryCategory",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateGlossaryTerm(
        _BaseBusinessGlossaryServiceRestTransport._BaseUpdateGlossaryTerm,
        BusinessGlossaryServiceRestStub,
    ):
        def __hash__(self):
            return hash("BusinessGlossaryServiceRestTransport.UpdateGlossaryTerm")

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
            request: business_glossary.UpdateGlossaryTermRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> business_glossary.GlossaryTerm:
            r"""Call the update glossary term method over HTTP.

            Args:
                request (~.business_glossary.UpdateGlossaryTermRequest):
                    The request object. Update GlossaryTerm Request
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.business_glossary.GlossaryTerm:
                    GlossaryTerms are the core of
                Glossary. A GlossaryTerm holds a rich
                text description that can be attached to
                Entries or specific columns to enrich
                them.

            """

            http_options = _BaseBusinessGlossaryServiceRestTransport._BaseUpdateGlossaryTerm._get_http_options()
            request, metadata = self._interceptor.pre_update_glossary_term(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBusinessGlossaryServiceRestTransport._BaseUpdateGlossaryTerm,
                    "_BaseUpdateGlossaryTerm__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dataplex_v1.BusinessGlossaryServiceClient.UpdateGlossaryTerm",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "UpdateGlossaryTerm",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                BusinessGlossaryServiceRestTransport._UpdateGlossaryTerm._get_response(
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
            resp = business_glossary.GlossaryTerm()
            pb_resp = business_glossary.GlossaryTerm.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_glossary_term(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_glossary_term_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = business_glossary.GlossaryTerm.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dataplex_v1.BusinessGlossaryServiceClient.update_glossary_term",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "UpdateGlossaryTerm",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_glossary(
        self,
    ) -> Callable[[business_glossary.CreateGlossaryRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateGlossary(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_glossary_category(
        self,
    ) -> Callable[
        [business_glossary.CreateGlossaryCategoryRequest],
        business_glossary.GlossaryCategory,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateGlossaryCategory(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_glossary_term(
        self,
    ) -> Callable[
        [business_glossary.CreateGlossaryTermRequest], business_glossary.GlossaryTerm
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateGlossaryTerm(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_glossary(
        self,
    ) -> Callable[[business_glossary.DeleteGlossaryRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteGlossary(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_glossary_category(
        self,
    ) -> Callable[[business_glossary.DeleteGlossaryCategoryRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteGlossaryCategory(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_glossary_term(
        self,
    ) -> Callable[[business_glossary.DeleteGlossaryTermRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteGlossaryTerm(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_glossary(
        self,
    ) -> Callable[[business_glossary.GetGlossaryRequest], business_glossary.Glossary]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetGlossary(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_glossary_category(
        self,
    ) -> Callable[
        [business_glossary.GetGlossaryCategoryRequest],
        business_glossary.GlossaryCategory,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetGlossaryCategory(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_glossary_term(
        self,
    ) -> Callable[
        [business_glossary.GetGlossaryTermRequest], business_glossary.GlossaryTerm
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetGlossaryTerm(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_glossaries(
        self,
    ) -> Callable[
        [business_glossary.ListGlossariesRequest],
        business_glossary.ListGlossariesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListGlossaries(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_glossary_categories(
        self,
    ) -> Callable[
        [business_glossary.ListGlossaryCategoriesRequest],
        business_glossary.ListGlossaryCategoriesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListGlossaryCategories(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_glossary_terms(
        self,
    ) -> Callable[
        [business_glossary.ListGlossaryTermsRequest],
        business_glossary.ListGlossaryTermsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListGlossaryTerms(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_glossary(
        self,
    ) -> Callable[[business_glossary.UpdateGlossaryRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateGlossary(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_glossary_category(
        self,
    ) -> Callable[
        [business_glossary.UpdateGlossaryCategoryRequest],
        business_glossary.GlossaryCategory,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateGlossaryCategory(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_glossary_term(
        self,
    ) -> Callable[
        [business_glossary.UpdateGlossaryTermRequest], business_glossary.GlossaryTerm
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateGlossaryTerm(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseBusinessGlossaryServiceRestTransport._BaseGetLocation,
        BusinessGlossaryServiceRestStub,
    ):
        def __hash__(self):
            return hash("BusinessGlossaryServiceRestTransport.GetLocation")

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
            request: locations_pb2.GetLocationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> locations_pb2.Location:
            r"""Call the get location method over HTTP.

            Args:
                request (locations_pb2.GetLocationRequest):
                    The request object for GetLocation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                locations_pb2.Location: Response from GetLocation method.
            """

            http_options = _BaseBusinessGlossaryServiceRestTransport._BaseGetLocation._get_http_options()
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBusinessGlossaryServiceRestTransport._BaseGetLocation,
                    "_BaseGetLocation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dataplex_v1.BusinessGlossaryServiceClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BusinessGlossaryServiceRestTransport._GetLocation._get_response(
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
            resp = locations_pb2.Location()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_location(resp)
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
                    "Received response for google.cloud.dataplex_v1.BusinessGlossaryServiceAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "GetLocation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_locations(self):
        return self._ListLocations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListLocations(
        _BaseBusinessGlossaryServiceRestTransport._BaseListLocations,
        BusinessGlossaryServiceRestStub,
    ):
        def __hash__(self):
            return hash("BusinessGlossaryServiceRestTransport.ListLocations")

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
            request: locations_pb2.ListLocationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> locations_pb2.ListLocationsResponse:
            r"""Call the list locations method over HTTP.

            Args:
                request (locations_pb2.ListLocationsRequest):
                    The request object for ListLocations method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                locations_pb2.ListLocationsResponse: Response from ListLocations method.
            """

            http_options = _BaseBusinessGlossaryServiceRestTransport._BaseListLocations._get_http_options()
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBusinessGlossaryServiceRestTransport._BaseListLocations,
                    "_BaseListLocations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dataplex_v1.BusinessGlossaryServiceClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                BusinessGlossaryServiceRestTransport._ListLocations._get_response(
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

            content = response.content.decode("utf-8")
            resp = locations_pb2.ListLocationsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_list_locations(resp)
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
                    "Received response for google.cloud.dataplex_v1.BusinessGlossaryServiceAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "ListLocations",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def get_iam_policy(self):
        return self._GetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    class _GetIamPolicy(
        _BaseBusinessGlossaryServiceRestTransport._BaseGetIamPolicy,
        BusinessGlossaryServiceRestStub,
    ):
        def __hash__(self):
            return hash("BusinessGlossaryServiceRestTransport.GetIamPolicy")

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
            request: iam_policy_pb2.GetIamPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> policy_pb2.Policy:
            r"""Call the get iam policy method over HTTP.

            Args:
                request (iam_policy_pb2.GetIamPolicyRequest):
                    The request object for GetIamPolicy method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                policy_pb2.Policy: Response from GetIamPolicy method.
            """

            http_options = _BaseBusinessGlossaryServiceRestTransport._BaseGetIamPolicy._get_http_options()
            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBusinessGlossaryServiceRestTransport._BaseGetIamPolicy,
                    "_BaseGetIamPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dataplex_v1.BusinessGlossaryServiceClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "GetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BusinessGlossaryServiceRestTransport._GetIamPolicy._get_response(
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
            resp = policy_pb2.Policy()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_iam_policy(resp)
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
                    "Received response for google.cloud.dataplex_v1.BusinessGlossaryServiceAsyncClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "GetIamPolicy",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def set_iam_policy(self):
        return self._SetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    class _SetIamPolicy(
        _BaseBusinessGlossaryServiceRestTransport._BaseSetIamPolicy,
        BusinessGlossaryServiceRestStub,
    ):
        def __hash__(self):
            return hash("BusinessGlossaryServiceRestTransport.SetIamPolicy")

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
            request: iam_policy_pb2.SetIamPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> policy_pb2.Policy:
            r"""Call the set iam policy method over HTTP.

            Args:
                request (iam_policy_pb2.SetIamPolicyRequest):
                    The request object for SetIamPolicy method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                policy_pb2.Policy: Response from SetIamPolicy method.
            """

            http_options = _BaseBusinessGlossaryServiceRestTransport._BaseSetIamPolicy._get_http_options()
            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBusinessGlossaryServiceRestTransport._BaseSetIamPolicy,
                    "_BaseSetIamPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dataplex_v1.BusinessGlossaryServiceClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "SetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BusinessGlossaryServiceRestTransport._SetIamPolicy._get_response(
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

            content = response.content.decode("utf-8")
            resp = policy_pb2.Policy()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_set_iam_policy(resp)
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
                    "Received response for google.cloud.dataplex_v1.BusinessGlossaryServiceAsyncClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "SetIamPolicy",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def test_iam_permissions(self):
        return self._TestIamPermissions(self._session, self._host, self._interceptor)  # type: ignore

    class _TestIamPermissions(
        _BaseBusinessGlossaryServiceRestTransport._BaseTestIamPermissions,
        BusinessGlossaryServiceRestStub,
    ):
        def __hash__(self):
            return hash("BusinessGlossaryServiceRestTransport.TestIamPermissions")

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
            request: iam_policy_pb2.TestIamPermissionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> iam_policy_pb2.TestIamPermissionsResponse:
            r"""Call the test iam permissions method over HTTP.

            Args:
                request (iam_policy_pb2.TestIamPermissionsRequest):
                    The request object for TestIamPermissions method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                iam_policy_pb2.TestIamPermissionsResponse: Response from TestIamPermissions method.
            """

            http_options = _BaseBusinessGlossaryServiceRestTransport._BaseTestIamPermissions._get_http_options()
            request, metadata = self._interceptor.pre_test_iam_permissions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBusinessGlossaryServiceRestTransport._BaseTestIamPermissions,
                    "_BaseTestIamPermissions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dataplex_v1.BusinessGlossaryServiceClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "TestIamPermissions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                BusinessGlossaryServiceRestTransport._TestIamPermissions._get_response(
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

            content = response.content.decode("utf-8")
            resp = iam_policy_pb2.TestIamPermissionsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_test_iam_permissions(resp)
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
                    "Received response for google.cloud.dataplex_v1.BusinessGlossaryServiceAsyncClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "TestIamPermissions",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseBusinessGlossaryServiceRestTransport._BaseCancelOperation,
        BusinessGlossaryServiceRestStub,
    ):
        def __hash__(self):
            return hash("BusinessGlossaryServiceRestTransport.CancelOperation")

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

            http_options = _BaseBusinessGlossaryServiceRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBusinessGlossaryServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.dataplex_v1.BusinessGlossaryServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                BusinessGlossaryServiceRestTransport._CancelOperation._get_response(
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

            return self._interceptor.post_cancel_operation(None)

    @property
    def delete_operation(self):
        return self._DeleteOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _DeleteOperation(
        _BaseBusinessGlossaryServiceRestTransport._BaseDeleteOperation,
        BusinessGlossaryServiceRestStub,
    ):
        def __hash__(self):
            return hash("BusinessGlossaryServiceRestTransport.DeleteOperation")

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
            request: operations_pb2.DeleteOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> None:
            r"""Call the delete operation method over HTTP.

            Args:
                request (operations_pb2.DeleteOperationRequest):
                    The request object for DeleteOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseBusinessGlossaryServiceRestTransport._BaseDeleteOperation._get_http_options()
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBusinessGlossaryServiceRestTransport._BaseDeleteOperation,
                    "_BaseDeleteOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dataplex_v1.BusinessGlossaryServiceClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                BusinessGlossaryServiceRestTransport._DeleteOperation._get_response(
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

            return self._interceptor.post_delete_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseBusinessGlossaryServiceRestTransport._BaseGetOperation,
        BusinessGlossaryServiceRestStub,
    ):
        def __hash__(self):
            return hash("BusinessGlossaryServiceRestTransport.GetOperation")

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

            http_options = _BaseBusinessGlossaryServiceRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBusinessGlossaryServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.dataplex_v1.BusinessGlossaryServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BusinessGlossaryServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.dataplex_v1.BusinessGlossaryServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "GetOperation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_operations(self):
        return self._ListOperations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListOperations(
        _BaseBusinessGlossaryServiceRestTransport._BaseListOperations,
        BusinessGlossaryServiceRestStub,
    ):
        def __hash__(self):
            return hash("BusinessGlossaryServiceRestTransport.ListOperations")

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
            request: operations_pb2.ListOperationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.ListOperationsResponse:
            r"""Call the list operations method over HTTP.

            Args:
                request (operations_pb2.ListOperationsRequest):
                    The request object for ListOperations method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                operations_pb2.ListOperationsResponse: Response from ListOperations method.
            """

            http_options = _BaseBusinessGlossaryServiceRestTransport._BaseListOperations._get_http_options()
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBusinessGlossaryServiceRestTransport._BaseListOperations,
                    "_BaseListOperations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dataplex_v1.BusinessGlossaryServiceClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                BusinessGlossaryServiceRestTransport._ListOperations._get_response(
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

            content = response.content.decode("utf-8")
            resp = operations_pb2.ListOperationsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_list_operations(resp)
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
                    "Received response for google.cloud.dataplex_v1.BusinessGlossaryServiceAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.dataplex.v1.BusinessGlossaryService",
                        "rpcName": "ListOperations",
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


__all__ = ("BusinessGlossaryServiceRestTransport",)
