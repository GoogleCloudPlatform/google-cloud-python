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

from google.cloud.kms_v1._compat import transcode_request
from google.cloud.kms_v1.types import resources, service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseKeyManagementServiceRestTransport

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


class KeyManagementServiceRestInterceptor:
    """Interceptor for KeyManagementService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the KeyManagementServiceRestTransport.

    .. code-block:: python
        class MyCustomKeyManagementServiceInterceptor(KeyManagementServiceRestInterceptor):
            def pre_asymmetric_decrypt(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_asymmetric_decrypt(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_asymmetric_sign(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_asymmetric_sign(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_crypto_key(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_crypto_key(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_crypto_key_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_crypto_key_version(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_import_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_import_job(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_key_ring(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_key_ring(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_decapsulate(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_decapsulate(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_decrypt(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_decrypt(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_crypto_key(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_crypto_key(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_crypto_key_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_crypto_key_version(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_destroy_crypto_key_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_destroy_crypto_key_version(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_encrypt(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_encrypt(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_export_trusted_key_wrapped_crypto_key_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_export_trusted_key_wrapped_crypto_key_version(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_generate_random_bytes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_generate_random_bytes(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_crypto_key(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_crypto_key(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_crypto_key_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_crypto_key_version(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_import_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_import_job(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_key_ring(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_key_ring(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_public_key(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_public_key(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_retired_resource(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_retired_resource(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_import_crypto_key_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_import_crypto_key_version(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_import_trusted_key_wrapped_crypto_key_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_import_trusted_key_wrapped_crypto_key_version(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_crypto_keys(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_crypto_keys(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_crypto_key_versions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_crypto_key_versions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_import_jobs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_import_jobs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_key_rings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_key_rings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_retired_resources(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_retired_resources(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_mac_sign(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_mac_sign(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_mac_verify(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_mac_verify(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_raw_decrypt(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_raw_decrypt(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_raw_encrypt(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_raw_encrypt(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_restore_crypto_key_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_restore_crypto_key_version(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_crypto_key(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_crypto_key(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_crypto_key_primary_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_crypto_key_primary_version(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_crypto_key_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_crypto_key_version(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = KeyManagementServiceRestTransport(interceptor=MyCustomKeyManagementServiceInterceptor())
        client = KeyManagementServiceClient(transport=transport)


    """

    def pre_asymmetric_decrypt(
        self,
        request: service.AsymmetricDecryptRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.AsymmetricDecryptRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for asymmetric_decrypt

        Override in a subclass to manipulate the request or metadata
        before they are sent to the KeyManagementService server.
        """
        return request, metadata

    def post_asymmetric_decrypt(
        self, response: service.AsymmetricDecryptResponse
    ) -> service.AsymmetricDecryptResponse:
        """Post-rpc interceptor for asymmetric_decrypt

        DEPRECATED. Please use the `post_asymmetric_decrypt_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the KeyManagementService server but before
        it is returned to user code. This `post_asymmetric_decrypt` interceptor runs
        before the `post_asymmetric_decrypt_with_metadata` interceptor.
        """
        return response

    def post_asymmetric_decrypt_with_metadata(
        self,
        response: service.AsymmetricDecryptResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.AsymmetricDecryptResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for asymmetric_decrypt

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the KeyManagementService server but before it is returned to user code.

        We recommend only using this `post_asymmetric_decrypt_with_metadata`
        interceptor in new development instead of the `post_asymmetric_decrypt` interceptor.
        When both interceptors are used, this `post_asymmetric_decrypt_with_metadata` interceptor runs after the
        `post_asymmetric_decrypt` interceptor. The (possibly modified) response returned by
        `post_asymmetric_decrypt` will be passed to
        `post_asymmetric_decrypt_with_metadata`.
        """
        return response, metadata

    def pre_asymmetric_sign(
        self,
        request: service.AsymmetricSignRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.AsymmetricSignRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for asymmetric_sign

        Override in a subclass to manipulate the request or metadata
        before they are sent to the KeyManagementService server.
        """
        return request, metadata

    def post_asymmetric_sign(
        self, response: service.AsymmetricSignResponse
    ) -> service.AsymmetricSignResponse:
        """Post-rpc interceptor for asymmetric_sign

        DEPRECATED. Please use the `post_asymmetric_sign_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the KeyManagementService server but before
        it is returned to user code. This `post_asymmetric_sign` interceptor runs
        before the `post_asymmetric_sign_with_metadata` interceptor.
        """
        return response

    def post_asymmetric_sign_with_metadata(
        self,
        response: service.AsymmetricSignResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.AsymmetricSignResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for asymmetric_sign

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the KeyManagementService server but before it is returned to user code.

        We recommend only using this `post_asymmetric_sign_with_metadata`
        interceptor in new development instead of the `post_asymmetric_sign` interceptor.
        When both interceptors are used, this `post_asymmetric_sign_with_metadata` interceptor runs after the
        `post_asymmetric_sign` interceptor. The (possibly modified) response returned by
        `post_asymmetric_sign` will be passed to
        `post_asymmetric_sign_with_metadata`.
        """
        return response, metadata

    def pre_create_crypto_key(
        self,
        request: service.CreateCryptoKeyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.CreateCryptoKeyRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_crypto_key

        Override in a subclass to manipulate the request or metadata
        before they are sent to the KeyManagementService server.
        """
        return request, metadata

    def post_create_crypto_key(
        self, response: resources.CryptoKey
    ) -> resources.CryptoKey:
        """Post-rpc interceptor for create_crypto_key

        DEPRECATED. Please use the `post_create_crypto_key_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the KeyManagementService server but before
        it is returned to user code. This `post_create_crypto_key` interceptor runs
        before the `post_create_crypto_key_with_metadata` interceptor.
        """
        return response

    def post_create_crypto_key_with_metadata(
        self,
        response: resources.CryptoKey,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.CryptoKey, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_crypto_key

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the KeyManagementService server but before it is returned to user code.

        We recommend only using this `post_create_crypto_key_with_metadata`
        interceptor in new development instead of the `post_create_crypto_key` interceptor.
        When both interceptors are used, this `post_create_crypto_key_with_metadata` interceptor runs after the
        `post_create_crypto_key` interceptor. The (possibly modified) response returned by
        `post_create_crypto_key` will be passed to
        `post_create_crypto_key_with_metadata`.
        """
        return response, metadata

    def pre_create_crypto_key_version(
        self,
        request: service.CreateCryptoKeyVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.CreateCryptoKeyVersionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_crypto_key_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the KeyManagementService server.
        """
        return request, metadata

    def post_create_crypto_key_version(
        self, response: resources.CryptoKeyVersion
    ) -> resources.CryptoKeyVersion:
        """Post-rpc interceptor for create_crypto_key_version

        DEPRECATED. Please use the `post_create_crypto_key_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the KeyManagementService server but before
        it is returned to user code. This `post_create_crypto_key_version` interceptor runs
        before the `post_create_crypto_key_version_with_metadata` interceptor.
        """
        return response

    def post_create_crypto_key_version_with_metadata(
        self,
        response: resources.CryptoKeyVersion,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.CryptoKeyVersion, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_crypto_key_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the KeyManagementService server but before it is returned to user code.

        We recommend only using this `post_create_crypto_key_version_with_metadata`
        interceptor in new development instead of the `post_create_crypto_key_version` interceptor.
        When both interceptors are used, this `post_create_crypto_key_version_with_metadata` interceptor runs after the
        `post_create_crypto_key_version` interceptor. The (possibly modified) response returned by
        `post_create_crypto_key_version` will be passed to
        `post_create_crypto_key_version_with_metadata`.
        """
        return response, metadata

    def pre_create_import_job(
        self,
        request: service.CreateImportJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.CreateImportJobRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_import_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the KeyManagementService server.
        """
        return request, metadata

    def post_create_import_job(
        self, response: resources.ImportJob
    ) -> resources.ImportJob:
        """Post-rpc interceptor for create_import_job

        DEPRECATED. Please use the `post_create_import_job_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the KeyManagementService server but before
        it is returned to user code. This `post_create_import_job` interceptor runs
        before the `post_create_import_job_with_metadata` interceptor.
        """
        return response

    def post_create_import_job_with_metadata(
        self,
        response: resources.ImportJob,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.ImportJob, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_import_job

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the KeyManagementService server but before it is returned to user code.

        We recommend only using this `post_create_import_job_with_metadata`
        interceptor in new development instead of the `post_create_import_job` interceptor.
        When both interceptors are used, this `post_create_import_job_with_metadata` interceptor runs after the
        `post_create_import_job` interceptor. The (possibly modified) response returned by
        `post_create_import_job` will be passed to
        `post_create_import_job_with_metadata`.
        """
        return response, metadata

    def pre_create_key_ring(
        self,
        request: service.CreateKeyRingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.CreateKeyRingRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_key_ring

        Override in a subclass to manipulate the request or metadata
        before they are sent to the KeyManagementService server.
        """
        return request, metadata

    def post_create_key_ring(self, response: resources.KeyRing) -> resources.KeyRing:
        """Post-rpc interceptor for create_key_ring

        DEPRECATED. Please use the `post_create_key_ring_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the KeyManagementService server but before
        it is returned to user code. This `post_create_key_ring` interceptor runs
        before the `post_create_key_ring_with_metadata` interceptor.
        """
        return response

    def post_create_key_ring_with_metadata(
        self,
        response: resources.KeyRing,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.KeyRing, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_key_ring

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the KeyManagementService server but before it is returned to user code.

        We recommend only using this `post_create_key_ring_with_metadata`
        interceptor in new development instead of the `post_create_key_ring` interceptor.
        When both interceptors are used, this `post_create_key_ring_with_metadata` interceptor runs after the
        `post_create_key_ring` interceptor. The (possibly modified) response returned by
        `post_create_key_ring` will be passed to
        `post_create_key_ring_with_metadata`.
        """
        return response, metadata

    def pre_decapsulate(
        self,
        request: service.DecapsulateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.DecapsulateRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for decapsulate

        Override in a subclass to manipulate the request or metadata
        before they are sent to the KeyManagementService server.
        """
        return request, metadata

    def post_decapsulate(
        self, response: service.DecapsulateResponse
    ) -> service.DecapsulateResponse:
        """Post-rpc interceptor for decapsulate

        DEPRECATED. Please use the `post_decapsulate_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the KeyManagementService server but before
        it is returned to user code. This `post_decapsulate` interceptor runs
        before the `post_decapsulate_with_metadata` interceptor.
        """
        return response

    def post_decapsulate_with_metadata(
        self,
        response: service.DecapsulateResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.DecapsulateResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for decapsulate

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the KeyManagementService server but before it is returned to user code.

        We recommend only using this `post_decapsulate_with_metadata`
        interceptor in new development instead of the `post_decapsulate` interceptor.
        When both interceptors are used, this `post_decapsulate_with_metadata` interceptor runs after the
        `post_decapsulate` interceptor. The (possibly modified) response returned by
        `post_decapsulate` will be passed to
        `post_decapsulate_with_metadata`.
        """
        return response, metadata

    def pre_decrypt(
        self,
        request: service.DecryptRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.DecryptRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for decrypt

        Override in a subclass to manipulate the request or metadata
        before they are sent to the KeyManagementService server.
        """
        return request, metadata

    def post_decrypt(
        self, response: service.DecryptResponse
    ) -> service.DecryptResponse:
        """Post-rpc interceptor for decrypt

        DEPRECATED. Please use the `post_decrypt_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the KeyManagementService server but before
        it is returned to user code. This `post_decrypt` interceptor runs
        before the `post_decrypt_with_metadata` interceptor.
        """
        return response

    def post_decrypt_with_metadata(
        self,
        response: service.DecryptResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.DecryptResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for decrypt

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the KeyManagementService server but before it is returned to user code.

        We recommend only using this `post_decrypt_with_metadata`
        interceptor in new development instead of the `post_decrypt` interceptor.
        When both interceptors are used, this `post_decrypt_with_metadata` interceptor runs after the
        `post_decrypt` interceptor. The (possibly modified) response returned by
        `post_decrypt` will be passed to
        `post_decrypt_with_metadata`.
        """
        return response, metadata

    def pre_delete_crypto_key(
        self,
        request: service.DeleteCryptoKeyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.DeleteCryptoKeyRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_crypto_key

        Override in a subclass to manipulate the request or metadata
        before they are sent to the KeyManagementService server.
        """
        return request, metadata

    def post_delete_crypto_key(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_crypto_key

        DEPRECATED. Please use the `post_delete_crypto_key_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the KeyManagementService server but before
        it is returned to user code. This `post_delete_crypto_key` interceptor runs
        before the `post_delete_crypto_key_with_metadata` interceptor.
        """
        return response

    def post_delete_crypto_key_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_crypto_key

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the KeyManagementService server but before it is returned to user code.

        We recommend only using this `post_delete_crypto_key_with_metadata`
        interceptor in new development instead of the `post_delete_crypto_key` interceptor.
        When both interceptors are used, this `post_delete_crypto_key_with_metadata` interceptor runs after the
        `post_delete_crypto_key` interceptor. The (possibly modified) response returned by
        `post_delete_crypto_key` will be passed to
        `post_delete_crypto_key_with_metadata`.
        """
        return response, metadata

    def pre_delete_crypto_key_version(
        self,
        request: service.DeleteCryptoKeyVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.DeleteCryptoKeyVersionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_crypto_key_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the KeyManagementService server.
        """
        return request, metadata

    def post_delete_crypto_key_version(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_crypto_key_version

        DEPRECATED. Please use the `post_delete_crypto_key_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the KeyManagementService server but before
        it is returned to user code. This `post_delete_crypto_key_version` interceptor runs
        before the `post_delete_crypto_key_version_with_metadata` interceptor.
        """
        return response

    def post_delete_crypto_key_version_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_crypto_key_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the KeyManagementService server but before it is returned to user code.

        We recommend only using this `post_delete_crypto_key_version_with_metadata`
        interceptor in new development instead of the `post_delete_crypto_key_version` interceptor.
        When both interceptors are used, this `post_delete_crypto_key_version_with_metadata` interceptor runs after the
        `post_delete_crypto_key_version` interceptor. The (possibly modified) response returned by
        `post_delete_crypto_key_version` will be passed to
        `post_delete_crypto_key_version_with_metadata`.
        """
        return response, metadata

    def pre_destroy_crypto_key_version(
        self,
        request: service.DestroyCryptoKeyVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.DestroyCryptoKeyVersionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for destroy_crypto_key_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the KeyManagementService server.
        """
        return request, metadata

    def post_destroy_crypto_key_version(
        self, response: resources.CryptoKeyVersion
    ) -> resources.CryptoKeyVersion:
        """Post-rpc interceptor for destroy_crypto_key_version

        DEPRECATED. Please use the `post_destroy_crypto_key_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the KeyManagementService server but before
        it is returned to user code. This `post_destroy_crypto_key_version` interceptor runs
        before the `post_destroy_crypto_key_version_with_metadata` interceptor.
        """
        return response

    def post_destroy_crypto_key_version_with_metadata(
        self,
        response: resources.CryptoKeyVersion,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.CryptoKeyVersion, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for destroy_crypto_key_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the KeyManagementService server but before it is returned to user code.

        We recommend only using this `post_destroy_crypto_key_version_with_metadata`
        interceptor in new development instead of the `post_destroy_crypto_key_version` interceptor.
        When both interceptors are used, this `post_destroy_crypto_key_version_with_metadata` interceptor runs after the
        `post_destroy_crypto_key_version` interceptor. The (possibly modified) response returned by
        `post_destroy_crypto_key_version` will be passed to
        `post_destroy_crypto_key_version_with_metadata`.
        """
        return response, metadata

    def pre_encrypt(
        self,
        request: service.EncryptRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.EncryptRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for encrypt

        Override in a subclass to manipulate the request or metadata
        before they are sent to the KeyManagementService server.
        """
        return request, metadata

    def post_encrypt(
        self, response: service.EncryptResponse
    ) -> service.EncryptResponse:
        """Post-rpc interceptor for encrypt

        DEPRECATED. Please use the `post_encrypt_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the KeyManagementService server but before
        it is returned to user code. This `post_encrypt` interceptor runs
        before the `post_encrypt_with_metadata` interceptor.
        """
        return response

    def post_encrypt_with_metadata(
        self,
        response: service.EncryptResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.EncryptResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for encrypt

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the KeyManagementService server but before it is returned to user code.

        We recommend only using this `post_encrypt_with_metadata`
        interceptor in new development instead of the `post_encrypt` interceptor.
        When both interceptors are used, this `post_encrypt_with_metadata` interceptor runs after the
        `post_encrypt` interceptor. The (possibly modified) response returned by
        `post_encrypt` will be passed to
        `post_encrypt_with_metadata`.
        """
        return response, metadata

    def pre_export_trusted_key_wrapped_crypto_key_version(
        self,
        request: service.ExportTrustedKeyWrappedCryptoKeyVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ExportTrustedKeyWrappedCryptoKeyVersionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for export_trusted_key_wrapped_crypto_key_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the KeyManagementService server.
        """
        return request, metadata

    def post_export_trusted_key_wrapped_crypto_key_version(
        self, response: service.ExportTrustedKeyWrappedCryptoKeyVersionResponse
    ) -> service.ExportTrustedKeyWrappedCryptoKeyVersionResponse:
        """Post-rpc interceptor for export_trusted_key_wrapped_crypto_key_version

        DEPRECATED. Please use the `post_export_trusted_key_wrapped_crypto_key_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the KeyManagementService server but before
        it is returned to user code. This `post_export_trusted_key_wrapped_crypto_key_version` interceptor runs
        before the `post_export_trusted_key_wrapped_crypto_key_version_with_metadata` interceptor.
        """
        return response

    def post_export_trusted_key_wrapped_crypto_key_version_with_metadata(
        self,
        response: service.ExportTrustedKeyWrappedCryptoKeyVersionResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ExportTrustedKeyWrappedCryptoKeyVersionResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for export_trusted_key_wrapped_crypto_key_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the KeyManagementService server but before it is returned to user code.

        We recommend only using this `post_export_trusted_key_wrapped_crypto_key_version_with_metadata`
        interceptor in new development instead of the `post_export_trusted_key_wrapped_crypto_key_version` interceptor.
        When both interceptors are used, this `post_export_trusted_key_wrapped_crypto_key_version_with_metadata` interceptor runs after the
        `post_export_trusted_key_wrapped_crypto_key_version` interceptor. The (possibly modified) response returned by
        `post_export_trusted_key_wrapped_crypto_key_version` will be passed to
        `post_export_trusted_key_wrapped_crypto_key_version_with_metadata`.
        """
        return response, metadata

    def pre_generate_random_bytes(
        self,
        request: service.GenerateRandomBytesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.GenerateRandomBytesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for generate_random_bytes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the KeyManagementService server.
        """
        return request, metadata

    def post_generate_random_bytes(
        self, response: service.GenerateRandomBytesResponse
    ) -> service.GenerateRandomBytesResponse:
        """Post-rpc interceptor for generate_random_bytes

        DEPRECATED. Please use the `post_generate_random_bytes_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the KeyManagementService server but before
        it is returned to user code. This `post_generate_random_bytes` interceptor runs
        before the `post_generate_random_bytes_with_metadata` interceptor.
        """
        return response

    def post_generate_random_bytes_with_metadata(
        self,
        response: service.GenerateRandomBytesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.GenerateRandomBytesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for generate_random_bytes

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the KeyManagementService server but before it is returned to user code.

        We recommend only using this `post_generate_random_bytes_with_metadata`
        interceptor in new development instead of the `post_generate_random_bytes` interceptor.
        When both interceptors are used, this `post_generate_random_bytes_with_metadata` interceptor runs after the
        `post_generate_random_bytes` interceptor. The (possibly modified) response returned by
        `post_generate_random_bytes` will be passed to
        `post_generate_random_bytes_with_metadata`.
        """
        return response, metadata

    def pre_get_crypto_key(
        self,
        request: service.GetCryptoKeyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.GetCryptoKeyRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_crypto_key

        Override in a subclass to manipulate the request or metadata
        before they are sent to the KeyManagementService server.
        """
        return request, metadata

    def post_get_crypto_key(self, response: resources.CryptoKey) -> resources.CryptoKey:
        """Post-rpc interceptor for get_crypto_key

        DEPRECATED. Please use the `post_get_crypto_key_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the KeyManagementService server but before
        it is returned to user code. This `post_get_crypto_key` interceptor runs
        before the `post_get_crypto_key_with_metadata` interceptor.
        """
        return response

    def post_get_crypto_key_with_metadata(
        self,
        response: resources.CryptoKey,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.CryptoKey, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_crypto_key

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the KeyManagementService server but before it is returned to user code.

        We recommend only using this `post_get_crypto_key_with_metadata`
        interceptor in new development instead of the `post_get_crypto_key` interceptor.
        When both interceptors are used, this `post_get_crypto_key_with_metadata` interceptor runs after the
        `post_get_crypto_key` interceptor. The (possibly modified) response returned by
        `post_get_crypto_key` will be passed to
        `post_get_crypto_key_with_metadata`.
        """
        return response, metadata

    def pre_get_crypto_key_version(
        self,
        request: service.GetCryptoKeyVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.GetCryptoKeyVersionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_crypto_key_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the KeyManagementService server.
        """
        return request, metadata

    def post_get_crypto_key_version(
        self, response: resources.CryptoKeyVersion
    ) -> resources.CryptoKeyVersion:
        """Post-rpc interceptor for get_crypto_key_version

        DEPRECATED. Please use the `post_get_crypto_key_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the KeyManagementService server but before
        it is returned to user code. This `post_get_crypto_key_version` interceptor runs
        before the `post_get_crypto_key_version_with_metadata` interceptor.
        """
        return response

    def post_get_crypto_key_version_with_metadata(
        self,
        response: resources.CryptoKeyVersion,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.CryptoKeyVersion, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_crypto_key_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the KeyManagementService server but before it is returned to user code.

        We recommend only using this `post_get_crypto_key_version_with_metadata`
        interceptor in new development instead of the `post_get_crypto_key_version` interceptor.
        When both interceptors are used, this `post_get_crypto_key_version_with_metadata` interceptor runs after the
        `post_get_crypto_key_version` interceptor. The (possibly modified) response returned by
        `post_get_crypto_key_version` will be passed to
        `post_get_crypto_key_version_with_metadata`.
        """
        return response, metadata

    def pre_get_import_job(
        self,
        request: service.GetImportJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.GetImportJobRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_import_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the KeyManagementService server.
        """
        return request, metadata

    def post_get_import_job(self, response: resources.ImportJob) -> resources.ImportJob:
        """Post-rpc interceptor for get_import_job

        DEPRECATED. Please use the `post_get_import_job_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the KeyManagementService server but before
        it is returned to user code. This `post_get_import_job` interceptor runs
        before the `post_get_import_job_with_metadata` interceptor.
        """
        return response

    def post_get_import_job_with_metadata(
        self,
        response: resources.ImportJob,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.ImportJob, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_import_job

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the KeyManagementService server but before it is returned to user code.

        We recommend only using this `post_get_import_job_with_metadata`
        interceptor in new development instead of the `post_get_import_job` interceptor.
        When both interceptors are used, this `post_get_import_job_with_metadata` interceptor runs after the
        `post_get_import_job` interceptor. The (possibly modified) response returned by
        `post_get_import_job` will be passed to
        `post_get_import_job_with_metadata`.
        """
        return response, metadata

    def pre_get_key_ring(
        self,
        request: service.GetKeyRingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.GetKeyRingRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_key_ring

        Override in a subclass to manipulate the request or metadata
        before they are sent to the KeyManagementService server.
        """
        return request, metadata

    def post_get_key_ring(self, response: resources.KeyRing) -> resources.KeyRing:
        """Post-rpc interceptor for get_key_ring

        DEPRECATED. Please use the `post_get_key_ring_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the KeyManagementService server but before
        it is returned to user code. This `post_get_key_ring` interceptor runs
        before the `post_get_key_ring_with_metadata` interceptor.
        """
        return response

    def post_get_key_ring_with_metadata(
        self,
        response: resources.KeyRing,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.KeyRing, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_key_ring

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the KeyManagementService server but before it is returned to user code.

        We recommend only using this `post_get_key_ring_with_metadata`
        interceptor in new development instead of the `post_get_key_ring` interceptor.
        When both interceptors are used, this `post_get_key_ring_with_metadata` interceptor runs after the
        `post_get_key_ring` interceptor. The (possibly modified) response returned by
        `post_get_key_ring` will be passed to
        `post_get_key_ring_with_metadata`.
        """
        return response, metadata

    def pre_get_public_key(
        self,
        request: service.GetPublicKeyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.GetPublicKeyRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_public_key

        Override in a subclass to manipulate the request or metadata
        before they are sent to the KeyManagementService server.
        """
        return request, metadata

    def post_get_public_key(self, response: resources.PublicKey) -> resources.PublicKey:
        """Post-rpc interceptor for get_public_key

        DEPRECATED. Please use the `post_get_public_key_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the KeyManagementService server but before
        it is returned to user code. This `post_get_public_key` interceptor runs
        before the `post_get_public_key_with_metadata` interceptor.
        """
        return response

    def post_get_public_key_with_metadata(
        self,
        response: resources.PublicKey,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.PublicKey, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_public_key

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the KeyManagementService server but before it is returned to user code.

        We recommend only using this `post_get_public_key_with_metadata`
        interceptor in new development instead of the `post_get_public_key` interceptor.
        When both interceptors are used, this `post_get_public_key_with_metadata` interceptor runs after the
        `post_get_public_key` interceptor. The (possibly modified) response returned by
        `post_get_public_key` will be passed to
        `post_get_public_key_with_metadata`.
        """
        return response, metadata

    def pre_get_retired_resource(
        self,
        request: service.GetRetiredResourceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.GetRetiredResourceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_retired_resource

        Override in a subclass to manipulate the request or metadata
        before they are sent to the KeyManagementService server.
        """
        return request, metadata

    def post_get_retired_resource(
        self, response: resources.RetiredResource
    ) -> resources.RetiredResource:
        """Post-rpc interceptor for get_retired_resource

        DEPRECATED. Please use the `post_get_retired_resource_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the KeyManagementService server but before
        it is returned to user code. This `post_get_retired_resource` interceptor runs
        before the `post_get_retired_resource_with_metadata` interceptor.
        """
        return response

    def post_get_retired_resource_with_metadata(
        self,
        response: resources.RetiredResource,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.RetiredResource, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_retired_resource

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the KeyManagementService server but before it is returned to user code.

        We recommend only using this `post_get_retired_resource_with_metadata`
        interceptor in new development instead of the `post_get_retired_resource` interceptor.
        When both interceptors are used, this `post_get_retired_resource_with_metadata` interceptor runs after the
        `post_get_retired_resource` interceptor. The (possibly modified) response returned by
        `post_get_retired_resource` will be passed to
        `post_get_retired_resource_with_metadata`.
        """
        return response, metadata

    def pre_import_crypto_key_version(
        self,
        request: service.ImportCryptoKeyVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ImportCryptoKeyVersionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for import_crypto_key_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the KeyManagementService server.
        """
        return request, metadata

    def post_import_crypto_key_version(
        self, response: resources.CryptoKeyVersion
    ) -> resources.CryptoKeyVersion:
        """Post-rpc interceptor for import_crypto_key_version

        DEPRECATED. Please use the `post_import_crypto_key_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the KeyManagementService server but before
        it is returned to user code. This `post_import_crypto_key_version` interceptor runs
        before the `post_import_crypto_key_version_with_metadata` interceptor.
        """
        return response

    def post_import_crypto_key_version_with_metadata(
        self,
        response: resources.CryptoKeyVersion,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.CryptoKeyVersion, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for import_crypto_key_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the KeyManagementService server but before it is returned to user code.

        We recommend only using this `post_import_crypto_key_version_with_metadata`
        interceptor in new development instead of the `post_import_crypto_key_version` interceptor.
        When both interceptors are used, this `post_import_crypto_key_version_with_metadata` interceptor runs after the
        `post_import_crypto_key_version` interceptor. The (possibly modified) response returned by
        `post_import_crypto_key_version` will be passed to
        `post_import_crypto_key_version_with_metadata`.
        """
        return response, metadata

    def pre_import_trusted_key_wrapped_crypto_key_version(
        self,
        request: service.ImportTrustedKeyWrappedCryptoKeyVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ImportTrustedKeyWrappedCryptoKeyVersionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for import_trusted_key_wrapped_crypto_key_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the KeyManagementService server.
        """
        return request, metadata

    def post_import_trusted_key_wrapped_crypto_key_version(
        self, response: resources.CryptoKeyVersion
    ) -> resources.CryptoKeyVersion:
        """Post-rpc interceptor for import_trusted_key_wrapped_crypto_key_version

        DEPRECATED. Please use the `post_import_trusted_key_wrapped_crypto_key_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the KeyManagementService server but before
        it is returned to user code. This `post_import_trusted_key_wrapped_crypto_key_version` interceptor runs
        before the `post_import_trusted_key_wrapped_crypto_key_version_with_metadata` interceptor.
        """
        return response

    def post_import_trusted_key_wrapped_crypto_key_version_with_metadata(
        self,
        response: resources.CryptoKeyVersion,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.CryptoKeyVersion, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for import_trusted_key_wrapped_crypto_key_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the KeyManagementService server but before it is returned to user code.

        We recommend only using this `post_import_trusted_key_wrapped_crypto_key_version_with_metadata`
        interceptor in new development instead of the `post_import_trusted_key_wrapped_crypto_key_version` interceptor.
        When both interceptors are used, this `post_import_trusted_key_wrapped_crypto_key_version_with_metadata` interceptor runs after the
        `post_import_trusted_key_wrapped_crypto_key_version` interceptor. The (possibly modified) response returned by
        `post_import_trusted_key_wrapped_crypto_key_version` will be passed to
        `post_import_trusted_key_wrapped_crypto_key_version_with_metadata`.
        """
        return response, metadata

    def pre_list_crypto_keys(
        self,
        request: service.ListCryptoKeysRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListCryptoKeysRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_crypto_keys

        Override in a subclass to manipulate the request or metadata
        before they are sent to the KeyManagementService server.
        """
        return request, metadata

    def post_list_crypto_keys(
        self, response: service.ListCryptoKeysResponse
    ) -> service.ListCryptoKeysResponse:
        """Post-rpc interceptor for list_crypto_keys

        DEPRECATED. Please use the `post_list_crypto_keys_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the KeyManagementService server but before
        it is returned to user code. This `post_list_crypto_keys` interceptor runs
        before the `post_list_crypto_keys_with_metadata` interceptor.
        """
        return response

    def post_list_crypto_keys_with_metadata(
        self,
        response: service.ListCryptoKeysResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListCryptoKeysResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_crypto_keys

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the KeyManagementService server but before it is returned to user code.

        We recommend only using this `post_list_crypto_keys_with_metadata`
        interceptor in new development instead of the `post_list_crypto_keys` interceptor.
        When both interceptors are used, this `post_list_crypto_keys_with_metadata` interceptor runs after the
        `post_list_crypto_keys` interceptor. The (possibly modified) response returned by
        `post_list_crypto_keys` will be passed to
        `post_list_crypto_keys_with_metadata`.
        """
        return response, metadata

    def pre_list_crypto_key_versions(
        self,
        request: service.ListCryptoKeyVersionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ListCryptoKeyVersionsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_crypto_key_versions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the KeyManagementService server.
        """
        return request, metadata

    def post_list_crypto_key_versions(
        self, response: service.ListCryptoKeyVersionsResponse
    ) -> service.ListCryptoKeyVersionsResponse:
        """Post-rpc interceptor for list_crypto_key_versions

        DEPRECATED. Please use the `post_list_crypto_key_versions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the KeyManagementService server but before
        it is returned to user code. This `post_list_crypto_key_versions` interceptor runs
        before the `post_list_crypto_key_versions_with_metadata` interceptor.
        """
        return response

    def post_list_crypto_key_versions_with_metadata(
        self,
        response: service.ListCryptoKeyVersionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ListCryptoKeyVersionsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_crypto_key_versions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the KeyManagementService server but before it is returned to user code.

        We recommend only using this `post_list_crypto_key_versions_with_metadata`
        interceptor in new development instead of the `post_list_crypto_key_versions` interceptor.
        When both interceptors are used, this `post_list_crypto_key_versions_with_metadata` interceptor runs after the
        `post_list_crypto_key_versions` interceptor. The (possibly modified) response returned by
        `post_list_crypto_key_versions` will be passed to
        `post_list_crypto_key_versions_with_metadata`.
        """
        return response, metadata

    def pre_list_import_jobs(
        self,
        request: service.ListImportJobsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListImportJobsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_import_jobs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the KeyManagementService server.
        """
        return request, metadata

    def post_list_import_jobs(
        self, response: service.ListImportJobsResponse
    ) -> service.ListImportJobsResponse:
        """Post-rpc interceptor for list_import_jobs

        DEPRECATED. Please use the `post_list_import_jobs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the KeyManagementService server but before
        it is returned to user code. This `post_list_import_jobs` interceptor runs
        before the `post_list_import_jobs_with_metadata` interceptor.
        """
        return response

    def post_list_import_jobs_with_metadata(
        self,
        response: service.ListImportJobsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListImportJobsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_import_jobs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the KeyManagementService server but before it is returned to user code.

        We recommend only using this `post_list_import_jobs_with_metadata`
        interceptor in new development instead of the `post_list_import_jobs` interceptor.
        When both interceptors are used, this `post_list_import_jobs_with_metadata` interceptor runs after the
        `post_list_import_jobs` interceptor. The (possibly modified) response returned by
        `post_list_import_jobs` will be passed to
        `post_list_import_jobs_with_metadata`.
        """
        return response, metadata

    def pre_list_key_rings(
        self,
        request: service.ListKeyRingsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListKeyRingsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_key_rings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the KeyManagementService server.
        """
        return request, metadata

    def post_list_key_rings(
        self, response: service.ListKeyRingsResponse
    ) -> service.ListKeyRingsResponse:
        """Post-rpc interceptor for list_key_rings

        DEPRECATED. Please use the `post_list_key_rings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the KeyManagementService server but before
        it is returned to user code. This `post_list_key_rings` interceptor runs
        before the `post_list_key_rings_with_metadata` interceptor.
        """
        return response

    def post_list_key_rings_with_metadata(
        self,
        response: service.ListKeyRingsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListKeyRingsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_key_rings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the KeyManagementService server but before it is returned to user code.

        We recommend only using this `post_list_key_rings_with_metadata`
        interceptor in new development instead of the `post_list_key_rings` interceptor.
        When both interceptors are used, this `post_list_key_rings_with_metadata` interceptor runs after the
        `post_list_key_rings` interceptor. The (possibly modified) response returned by
        `post_list_key_rings` will be passed to
        `post_list_key_rings_with_metadata`.
        """
        return response, metadata

    def pre_list_retired_resources(
        self,
        request: service.ListRetiredResourcesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ListRetiredResourcesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_retired_resources

        Override in a subclass to manipulate the request or metadata
        before they are sent to the KeyManagementService server.
        """
        return request, metadata

    def post_list_retired_resources(
        self, response: service.ListRetiredResourcesResponse
    ) -> service.ListRetiredResourcesResponse:
        """Post-rpc interceptor for list_retired_resources

        DEPRECATED. Please use the `post_list_retired_resources_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the KeyManagementService server but before
        it is returned to user code. This `post_list_retired_resources` interceptor runs
        before the `post_list_retired_resources_with_metadata` interceptor.
        """
        return response

    def post_list_retired_resources_with_metadata(
        self,
        response: service.ListRetiredResourcesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ListRetiredResourcesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_retired_resources

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the KeyManagementService server but before it is returned to user code.

        We recommend only using this `post_list_retired_resources_with_metadata`
        interceptor in new development instead of the `post_list_retired_resources` interceptor.
        When both interceptors are used, this `post_list_retired_resources_with_metadata` interceptor runs after the
        `post_list_retired_resources` interceptor. The (possibly modified) response returned by
        `post_list_retired_resources` will be passed to
        `post_list_retired_resources_with_metadata`.
        """
        return response, metadata

    def pre_mac_sign(
        self,
        request: service.MacSignRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.MacSignRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for mac_sign

        Override in a subclass to manipulate the request or metadata
        before they are sent to the KeyManagementService server.
        """
        return request, metadata

    def post_mac_sign(
        self, response: service.MacSignResponse
    ) -> service.MacSignResponse:
        """Post-rpc interceptor for mac_sign

        DEPRECATED. Please use the `post_mac_sign_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the KeyManagementService server but before
        it is returned to user code. This `post_mac_sign` interceptor runs
        before the `post_mac_sign_with_metadata` interceptor.
        """
        return response

    def post_mac_sign_with_metadata(
        self,
        response: service.MacSignResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.MacSignResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for mac_sign

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the KeyManagementService server but before it is returned to user code.

        We recommend only using this `post_mac_sign_with_metadata`
        interceptor in new development instead of the `post_mac_sign` interceptor.
        When both interceptors are used, this `post_mac_sign_with_metadata` interceptor runs after the
        `post_mac_sign` interceptor. The (possibly modified) response returned by
        `post_mac_sign` will be passed to
        `post_mac_sign_with_metadata`.
        """
        return response, metadata

    def pre_mac_verify(
        self,
        request: service.MacVerifyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.MacVerifyRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for mac_verify

        Override in a subclass to manipulate the request or metadata
        before they are sent to the KeyManagementService server.
        """
        return request, metadata

    def post_mac_verify(
        self, response: service.MacVerifyResponse
    ) -> service.MacVerifyResponse:
        """Post-rpc interceptor for mac_verify

        DEPRECATED. Please use the `post_mac_verify_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the KeyManagementService server but before
        it is returned to user code. This `post_mac_verify` interceptor runs
        before the `post_mac_verify_with_metadata` interceptor.
        """
        return response

    def post_mac_verify_with_metadata(
        self,
        response: service.MacVerifyResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.MacVerifyResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for mac_verify

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the KeyManagementService server but before it is returned to user code.

        We recommend only using this `post_mac_verify_with_metadata`
        interceptor in new development instead of the `post_mac_verify` interceptor.
        When both interceptors are used, this `post_mac_verify_with_metadata` interceptor runs after the
        `post_mac_verify` interceptor. The (possibly modified) response returned by
        `post_mac_verify` will be passed to
        `post_mac_verify_with_metadata`.
        """
        return response, metadata

    def pre_raw_decrypt(
        self,
        request: service.RawDecryptRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.RawDecryptRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for raw_decrypt

        Override in a subclass to manipulate the request or metadata
        before they are sent to the KeyManagementService server.
        """
        return request, metadata

    def post_raw_decrypt(
        self, response: service.RawDecryptResponse
    ) -> service.RawDecryptResponse:
        """Post-rpc interceptor for raw_decrypt

        DEPRECATED. Please use the `post_raw_decrypt_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the KeyManagementService server but before
        it is returned to user code. This `post_raw_decrypt` interceptor runs
        before the `post_raw_decrypt_with_metadata` interceptor.
        """
        return response

    def post_raw_decrypt_with_metadata(
        self,
        response: service.RawDecryptResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.RawDecryptResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for raw_decrypt

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the KeyManagementService server but before it is returned to user code.

        We recommend only using this `post_raw_decrypt_with_metadata`
        interceptor in new development instead of the `post_raw_decrypt` interceptor.
        When both interceptors are used, this `post_raw_decrypt_with_metadata` interceptor runs after the
        `post_raw_decrypt` interceptor. The (possibly modified) response returned by
        `post_raw_decrypt` will be passed to
        `post_raw_decrypt_with_metadata`.
        """
        return response, metadata

    def pre_raw_encrypt(
        self,
        request: service.RawEncryptRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.RawEncryptRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for raw_encrypt

        Override in a subclass to manipulate the request or metadata
        before they are sent to the KeyManagementService server.
        """
        return request, metadata

    def post_raw_encrypt(
        self, response: service.RawEncryptResponse
    ) -> service.RawEncryptResponse:
        """Post-rpc interceptor for raw_encrypt

        DEPRECATED. Please use the `post_raw_encrypt_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the KeyManagementService server but before
        it is returned to user code. This `post_raw_encrypt` interceptor runs
        before the `post_raw_encrypt_with_metadata` interceptor.
        """
        return response

    def post_raw_encrypt_with_metadata(
        self,
        response: service.RawEncryptResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.RawEncryptResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for raw_encrypt

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the KeyManagementService server but before it is returned to user code.

        We recommend only using this `post_raw_encrypt_with_metadata`
        interceptor in new development instead of the `post_raw_encrypt` interceptor.
        When both interceptors are used, this `post_raw_encrypt_with_metadata` interceptor runs after the
        `post_raw_encrypt` interceptor. The (possibly modified) response returned by
        `post_raw_encrypt` will be passed to
        `post_raw_encrypt_with_metadata`.
        """
        return response, metadata

    def pre_restore_crypto_key_version(
        self,
        request: service.RestoreCryptoKeyVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.RestoreCryptoKeyVersionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for restore_crypto_key_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the KeyManagementService server.
        """
        return request, metadata

    def post_restore_crypto_key_version(
        self, response: resources.CryptoKeyVersion
    ) -> resources.CryptoKeyVersion:
        """Post-rpc interceptor for restore_crypto_key_version

        DEPRECATED. Please use the `post_restore_crypto_key_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the KeyManagementService server but before
        it is returned to user code. This `post_restore_crypto_key_version` interceptor runs
        before the `post_restore_crypto_key_version_with_metadata` interceptor.
        """
        return response

    def post_restore_crypto_key_version_with_metadata(
        self,
        response: resources.CryptoKeyVersion,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.CryptoKeyVersion, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for restore_crypto_key_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the KeyManagementService server but before it is returned to user code.

        We recommend only using this `post_restore_crypto_key_version_with_metadata`
        interceptor in new development instead of the `post_restore_crypto_key_version` interceptor.
        When both interceptors are used, this `post_restore_crypto_key_version_with_metadata` interceptor runs after the
        `post_restore_crypto_key_version` interceptor. The (possibly modified) response returned by
        `post_restore_crypto_key_version` will be passed to
        `post_restore_crypto_key_version_with_metadata`.
        """
        return response, metadata

    def pre_update_crypto_key(
        self,
        request: service.UpdateCryptoKeyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.UpdateCryptoKeyRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_crypto_key

        Override in a subclass to manipulate the request or metadata
        before they are sent to the KeyManagementService server.
        """
        return request, metadata

    def post_update_crypto_key(
        self, response: resources.CryptoKey
    ) -> resources.CryptoKey:
        """Post-rpc interceptor for update_crypto_key

        DEPRECATED. Please use the `post_update_crypto_key_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the KeyManagementService server but before
        it is returned to user code. This `post_update_crypto_key` interceptor runs
        before the `post_update_crypto_key_with_metadata` interceptor.
        """
        return response

    def post_update_crypto_key_with_metadata(
        self,
        response: resources.CryptoKey,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.CryptoKey, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_crypto_key

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the KeyManagementService server but before it is returned to user code.

        We recommend only using this `post_update_crypto_key_with_metadata`
        interceptor in new development instead of the `post_update_crypto_key` interceptor.
        When both interceptors are used, this `post_update_crypto_key_with_metadata` interceptor runs after the
        `post_update_crypto_key` interceptor. The (possibly modified) response returned by
        `post_update_crypto_key` will be passed to
        `post_update_crypto_key_with_metadata`.
        """
        return response, metadata

    def pre_update_crypto_key_primary_version(
        self,
        request: service.UpdateCryptoKeyPrimaryVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.UpdateCryptoKeyPrimaryVersionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_crypto_key_primary_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the KeyManagementService server.
        """
        return request, metadata

    def post_update_crypto_key_primary_version(
        self, response: resources.CryptoKey
    ) -> resources.CryptoKey:
        """Post-rpc interceptor for update_crypto_key_primary_version

        DEPRECATED. Please use the `post_update_crypto_key_primary_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the KeyManagementService server but before
        it is returned to user code. This `post_update_crypto_key_primary_version` interceptor runs
        before the `post_update_crypto_key_primary_version_with_metadata` interceptor.
        """
        return response

    def post_update_crypto_key_primary_version_with_metadata(
        self,
        response: resources.CryptoKey,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.CryptoKey, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_crypto_key_primary_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the KeyManagementService server but before it is returned to user code.

        We recommend only using this `post_update_crypto_key_primary_version_with_metadata`
        interceptor in new development instead of the `post_update_crypto_key_primary_version` interceptor.
        When both interceptors are used, this `post_update_crypto_key_primary_version_with_metadata` interceptor runs after the
        `post_update_crypto_key_primary_version` interceptor. The (possibly modified) response returned by
        `post_update_crypto_key_primary_version` will be passed to
        `post_update_crypto_key_primary_version_with_metadata`.
        """
        return response, metadata

    def pre_update_crypto_key_version(
        self,
        request: service.UpdateCryptoKeyVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.UpdateCryptoKeyVersionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_crypto_key_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the KeyManagementService server.
        """
        return request, metadata

    def post_update_crypto_key_version(
        self, response: resources.CryptoKeyVersion
    ) -> resources.CryptoKeyVersion:
        """Post-rpc interceptor for update_crypto_key_version

        DEPRECATED. Please use the `post_update_crypto_key_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the KeyManagementService server but before
        it is returned to user code. This `post_update_crypto_key_version` interceptor runs
        before the `post_update_crypto_key_version_with_metadata` interceptor.
        """
        return response

    def post_update_crypto_key_version_with_metadata(
        self,
        response: resources.CryptoKeyVersion,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.CryptoKeyVersion, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_crypto_key_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the KeyManagementService server but before it is returned to user code.

        We recommend only using this `post_update_crypto_key_version_with_metadata`
        interceptor in new development instead of the `post_update_crypto_key_version` interceptor.
        When both interceptors are used, this `post_update_crypto_key_version_with_metadata` interceptor runs after the
        `post_update_crypto_key_version` interceptor. The (possibly modified) response returned by
        `post_update_crypto_key_version` will be passed to
        `post_update_crypto_key_version_with_metadata`.
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
        before they are sent to the KeyManagementService server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the KeyManagementService server but before
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
        before they are sent to the KeyManagementService server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the KeyManagementService server but before
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
        before they are sent to the KeyManagementService server.
        """
        return request, metadata

    def post_get_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the KeyManagementService server but before
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
        before they are sent to the KeyManagementService server.
        """
        return request, metadata

    def post_set_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the KeyManagementService server but before
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
        before they are sent to the KeyManagementService server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the response
        after it is returned by the KeyManagementService server but before
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
        before they are sent to the KeyManagementService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the KeyManagementService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class KeyManagementServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: KeyManagementServiceRestInterceptor


class KeyManagementServiceRestTransport(_BaseKeyManagementServiceRestTransport):
    """REST backend synchronous transport for KeyManagementService.

    Google Cloud Key Management Service

    Manages cryptographic keys and operations using those keys.
    Implements a REST model with the following objects:

    - [KeyRing][google.cloud.kms.v1.KeyRing]
    - [CryptoKey][google.cloud.kms.v1.CryptoKey]
    - [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
    - [ImportJob][google.cloud.kms.v1.ImportJob]

    If you are using manual gRPC libraries, see `Using gRPC with Cloud
    KMS <https://cloud.google.com/kms/docs/grpc>`__.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "cloudkms.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[KeyManagementServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'cloudkms.googleapis.com').
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
            interceptor (Optional[KeyManagementServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or KeyManagementServiceRestInterceptor()
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
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}",
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

    class _AsymmetricDecrypt(
        _BaseKeyManagementServiceRestTransport._BaseAsymmetricDecrypt,
        KeyManagementServiceRestStub,
    ):
        def __hash__(self):
            return hash("KeyManagementServiceRestTransport.AsymmetricDecrypt")

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
            request: service.AsymmetricDecryptRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.AsymmetricDecryptResponse:
            r"""Call the asymmetric decrypt method over HTTP.

            Args:
                request (~.service.AsymmetricDecryptRequest):
                    The request object. Request message for
                [KeyManagementService.AsymmetricDecrypt][google.cloud.kms.v1.KeyManagementService.AsymmetricDecrypt].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.AsymmetricDecryptResponse:
                    Response message for
                [KeyManagementService.AsymmetricDecrypt][google.cloud.kms.v1.KeyManagementService.AsymmetricDecrypt].

            """

            http_options = _BaseKeyManagementServiceRestTransport._BaseAsymmetricDecrypt._get_http_options()
            request, metadata = self._interceptor.pre_asymmetric_decrypt(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyManagementServiceRestTransport._BaseAsymmetricDecrypt,
                    "_BaseAsymmetricDecrypt__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.KeyManagementServiceClient.AsymmetricDecrypt",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "AsymmetricDecrypt",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                KeyManagementServiceRestTransport._AsymmetricDecrypt._get_response(
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
            resp = service.AsymmetricDecryptResponse()
            pb_resp = service.AsymmetricDecryptResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_asymmetric_decrypt(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_asymmetric_decrypt_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.AsymmetricDecryptResponse.to_json(
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
                    "Received response for google.cloud.kms_v1.KeyManagementServiceClient.asymmetric_decrypt",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "AsymmetricDecrypt",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _AsymmetricSign(
        _BaseKeyManagementServiceRestTransport._BaseAsymmetricSign,
        KeyManagementServiceRestStub,
    ):
        def __hash__(self):
            return hash("KeyManagementServiceRestTransport.AsymmetricSign")

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
            request: service.AsymmetricSignRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.AsymmetricSignResponse:
            r"""Call the asymmetric sign method over HTTP.

            Args:
                request (~.service.AsymmetricSignRequest):
                    The request object. Request message for
                [KeyManagementService.AsymmetricSign][google.cloud.kms.v1.KeyManagementService.AsymmetricSign].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.AsymmetricSignResponse:
                    Response message for
                [KeyManagementService.AsymmetricSign][google.cloud.kms.v1.KeyManagementService.AsymmetricSign].

            """

            http_options = _BaseKeyManagementServiceRestTransport._BaseAsymmetricSign._get_http_options()
            request, metadata = self._interceptor.pre_asymmetric_sign(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyManagementServiceRestTransport._BaseAsymmetricSign,
                    "_BaseAsymmetricSign__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.KeyManagementServiceClient.AsymmetricSign",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "AsymmetricSign",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = KeyManagementServiceRestTransport._AsymmetricSign._get_response(
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
            resp = service.AsymmetricSignResponse()
            pb_resp = service.AsymmetricSignResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_asymmetric_sign(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_asymmetric_sign_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.AsymmetricSignResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.kms_v1.KeyManagementServiceClient.asymmetric_sign",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "AsymmetricSign",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateCryptoKey(
        _BaseKeyManagementServiceRestTransport._BaseCreateCryptoKey,
        KeyManagementServiceRestStub,
    ):
        def __hash__(self):
            return hash("KeyManagementServiceRestTransport.CreateCryptoKey")

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
            request: service.CreateCryptoKeyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.CryptoKey:
            r"""Call the create crypto key method over HTTP.

            Args:
                request (~.service.CreateCryptoKeyRequest):
                    The request object. Request message for
                [KeyManagementService.CreateCryptoKey][google.cloud.kms.v1.KeyManagementService.CreateCryptoKey].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.CryptoKey:
                    A [CryptoKey][google.cloud.kms.v1.CryptoKey] represents
                a logical key that can be used for cryptographic
                operations.

                A [CryptoKey][google.cloud.kms.v1.CryptoKey] is made up
                of zero or more
                [versions][google.cloud.kms.v1.CryptoKeyVersion], which
                represent the actual key material used in cryptographic
                operations.

            """

            http_options = _BaseKeyManagementServiceRestTransport._BaseCreateCryptoKey._get_http_options()
            request, metadata = self._interceptor.pre_create_crypto_key(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyManagementServiceRestTransport._BaseCreateCryptoKey,
                    "_BaseCreateCryptoKey__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.KeyManagementServiceClient.CreateCryptoKey",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "CreateCryptoKey",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = KeyManagementServiceRestTransport._CreateCryptoKey._get_response(
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
            resp = resources.CryptoKey()
            pb_resp = resources.CryptoKey.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_crypto_key(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_crypto_key_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.CryptoKey.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.kms_v1.KeyManagementServiceClient.create_crypto_key",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "CreateCryptoKey",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateCryptoKeyVersion(
        _BaseKeyManagementServiceRestTransport._BaseCreateCryptoKeyVersion,
        KeyManagementServiceRestStub,
    ):
        def __hash__(self):
            return hash("KeyManagementServiceRestTransport.CreateCryptoKeyVersion")

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
            request: service.CreateCryptoKeyVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.CryptoKeyVersion:
            r"""Call the create crypto key version method over HTTP.

            Args:
                request (~.service.CreateCryptoKeyVersionRequest):
                    The request object. Request message for
                [KeyManagementService.CreateCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.CreateCryptoKeyVersion].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.CryptoKeyVersion:
                    A
                [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
                represents an individual cryptographic key, and the
                associated key material.

                An
                [ENABLED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.ENABLED]
                version can be used for cryptographic operations.

                For security reasons, the raw cryptographic key material
                represented by a
                [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
                can never be viewed or exported. It can only be used to
                encrypt, decrypt, or sign data when an authorized user
                or application invokes Cloud KMS.

            """

            http_options = _BaseKeyManagementServiceRestTransport._BaseCreateCryptoKeyVersion._get_http_options()
            request, metadata = self._interceptor.pre_create_crypto_key_version(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyManagementServiceRestTransport._BaseCreateCryptoKeyVersion,
                    "_BaseCreateCryptoKeyVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.KeyManagementServiceClient.CreateCryptoKeyVersion",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "CreateCryptoKeyVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                KeyManagementServiceRestTransport._CreateCryptoKeyVersion._get_response(
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
            resp = resources.CryptoKeyVersion()
            pb_resp = resources.CryptoKeyVersion.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_crypto_key_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_crypto_key_version_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.CryptoKeyVersion.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.kms_v1.KeyManagementServiceClient.create_crypto_key_version",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "CreateCryptoKeyVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateImportJob(
        _BaseKeyManagementServiceRestTransport._BaseCreateImportJob,
        KeyManagementServiceRestStub,
    ):
        def __hash__(self):
            return hash("KeyManagementServiceRestTransport.CreateImportJob")

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
            request: service.CreateImportJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.ImportJob:
            r"""Call the create import job method over HTTP.

            Args:
                request (~.service.CreateImportJobRequest):
                    The request object. Request message for
                [KeyManagementService.CreateImportJob][google.cloud.kms.v1.KeyManagementService.CreateImportJob].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.ImportJob:
                    An [ImportJob][google.cloud.kms.v1.ImportJob] can be
                used to create
                [CryptoKeys][google.cloud.kms.v1.CryptoKey] and
                [CryptoKeyVersions][google.cloud.kms.v1.CryptoKeyVersion]
                using pre-existing key material, generated outside of
                Cloud KMS.

                When an [ImportJob][google.cloud.kms.v1.ImportJob] is
                created, Cloud KMS will generate a "wrapping key", which
                is a public/private key pair. You use the wrapping key
                to encrypt (also known as wrap) the pre-existing key
                material to protect it during the import process. The
                nature of the wrapping key depends on the choice of
                [import_method][google.cloud.kms.v1.ImportJob.import_method].
                When the wrapping key generation is complete, the
                [state][google.cloud.kms.v1.ImportJob.state] will be set
                to
                [ACTIVE][google.cloud.kms.v1.ImportJob.ImportJobState.ACTIVE]
                and the
                [public_key][google.cloud.kms.v1.ImportJob.public_key]
                can be fetched. The fetched public key can then be used
                to wrap your pre-existing key material.

                Once the key material is wrapped, it can be imported
                into a new
                [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
                in an existing
                [CryptoKey][google.cloud.kms.v1.CryptoKey] by calling
                [ImportCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.ImportCryptoKeyVersion].
                Multiple
                [CryptoKeyVersions][google.cloud.kms.v1.CryptoKeyVersion]
                can be imported with a single
                [ImportJob][google.cloud.kms.v1.ImportJob]. Cloud KMS
                uses the private key portion of the wrapping key to
                unwrap the key material. Only Cloud KMS has access to
                the private key.

                An [ImportJob][google.cloud.kms.v1.ImportJob] expires 3
                days after it is created. Once expired, Cloud KMS will
                no longer be able to import or unwrap any key material
                that was wrapped with the
                [ImportJob][google.cloud.kms.v1.ImportJob]'s public key.

                For more information, see `Importing a
                key <https://cloud.google.com/kms/docs/importing-a-key>`__.

            """

            http_options = _BaseKeyManagementServiceRestTransport._BaseCreateImportJob._get_http_options()
            request, metadata = self._interceptor.pre_create_import_job(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyManagementServiceRestTransport._BaseCreateImportJob,
                    "_BaseCreateImportJob__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.KeyManagementServiceClient.CreateImportJob",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "CreateImportJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = KeyManagementServiceRestTransport._CreateImportJob._get_response(
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
            resp = resources.ImportJob()
            pb_resp = resources.ImportJob.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_import_job(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_import_job_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.ImportJob.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.kms_v1.KeyManagementServiceClient.create_import_job",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "CreateImportJob",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateKeyRing(
        _BaseKeyManagementServiceRestTransport._BaseCreateKeyRing,
        KeyManagementServiceRestStub,
    ):
        def __hash__(self):
            return hash("KeyManagementServiceRestTransport.CreateKeyRing")

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
            request: service.CreateKeyRingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.KeyRing:
            r"""Call the create key ring method over HTTP.

            Args:
                request (~.service.CreateKeyRingRequest):
                    The request object. Request message for
                [KeyManagementService.CreateKeyRing][google.cloud.kms.v1.KeyManagementService.CreateKeyRing].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.KeyRing:
                    A [KeyRing][google.cloud.kms.v1.KeyRing] is a toplevel
                logical grouping of
                [CryptoKeys][google.cloud.kms.v1.CryptoKey].

            """

            http_options = _BaseKeyManagementServiceRestTransport._BaseCreateKeyRing._get_http_options()
            request, metadata = self._interceptor.pre_create_key_ring(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyManagementServiceRestTransport._BaseCreateKeyRing,
                    "_BaseCreateKeyRing__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.KeyManagementServiceClient.CreateKeyRing",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "CreateKeyRing",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = KeyManagementServiceRestTransport._CreateKeyRing._get_response(
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
            resp = resources.KeyRing()
            pb_resp = resources.KeyRing.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_key_ring(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_key_ring_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.KeyRing.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.kms_v1.KeyManagementServiceClient.create_key_ring",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "CreateKeyRing",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Decapsulate(
        _BaseKeyManagementServiceRestTransport._BaseDecapsulate,
        KeyManagementServiceRestStub,
    ):
        def __hash__(self):
            return hash("KeyManagementServiceRestTransport.Decapsulate")

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
            request: service.DecapsulateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.DecapsulateResponse:
            r"""Call the decapsulate method over HTTP.

            Args:
                request (~.service.DecapsulateRequest):
                    The request object. Request message for
                [KeyManagementService.Decapsulate][google.cloud.kms.v1.KeyManagementService.Decapsulate].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.DecapsulateResponse:
                    Response message for
                [KeyManagementService.Decapsulate][google.cloud.kms.v1.KeyManagementService.Decapsulate].

            """

            http_options = _BaseKeyManagementServiceRestTransport._BaseDecapsulate._get_http_options()
            request, metadata = self._interceptor.pre_decapsulate(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyManagementServiceRestTransport._BaseDecapsulate,
                    "_BaseDecapsulate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.KeyManagementServiceClient.Decapsulate",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "Decapsulate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = KeyManagementServiceRestTransport._Decapsulate._get_response(
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
            resp = service.DecapsulateResponse()
            pb_resp = service.DecapsulateResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_decapsulate(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_decapsulate_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.DecapsulateResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.kms_v1.KeyManagementServiceClient.decapsulate",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "Decapsulate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Decrypt(
        _BaseKeyManagementServiceRestTransport._BaseDecrypt,
        KeyManagementServiceRestStub,
    ):
        def __hash__(self):
            return hash("KeyManagementServiceRestTransport.Decrypt")

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
            request: service.DecryptRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.DecryptResponse:
            r"""Call the decrypt method over HTTP.

            Args:
                request (~.service.DecryptRequest):
                    The request object. Request message for
                [KeyManagementService.Decrypt][google.cloud.kms.v1.KeyManagementService.Decrypt].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.DecryptResponse:
                    Response message for
                [KeyManagementService.Decrypt][google.cloud.kms.v1.KeyManagementService.Decrypt].

            """

            http_options = (
                _BaseKeyManagementServiceRestTransport._BaseDecrypt._get_http_options()
            )
            request, metadata = self._interceptor.pre_decrypt(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyManagementServiceRestTransport._BaseDecrypt,
                    "_BaseDecrypt__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.KeyManagementServiceClient.Decrypt",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "Decrypt",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = KeyManagementServiceRestTransport._Decrypt._get_response(
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
            resp = service.DecryptResponse()
            pb_resp = service.DecryptResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_decrypt(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_decrypt_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.DecryptResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.kms_v1.KeyManagementServiceClient.decrypt",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "Decrypt",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteCryptoKey(
        _BaseKeyManagementServiceRestTransport._BaseDeleteCryptoKey,
        KeyManagementServiceRestStub,
    ):
        def __hash__(self):
            return hash("KeyManagementServiceRestTransport.DeleteCryptoKey")

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
            request: service.DeleteCryptoKeyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete crypto key method over HTTP.

            Args:
                request (~.service.DeleteCryptoKeyRequest):
                    The request object. Request message for
                [KeyManagementService.DeleteCryptoKey][google.cloud.kms.v1.KeyManagementService.DeleteCryptoKey].
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

            http_options = _BaseKeyManagementServiceRestTransport._BaseDeleteCryptoKey._get_http_options()
            request, metadata = self._interceptor.pre_delete_crypto_key(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyManagementServiceRestTransport._BaseDeleteCryptoKey,
                    "_BaseDeleteCryptoKey__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.KeyManagementServiceClient.DeleteCryptoKey",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "DeleteCryptoKey",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = KeyManagementServiceRestTransport._DeleteCryptoKey._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_crypto_key(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_crypto_key_with_metadata(
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
                    "Received response for google.cloud.kms_v1.KeyManagementServiceClient.delete_crypto_key",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "DeleteCryptoKey",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteCryptoKeyVersion(
        _BaseKeyManagementServiceRestTransport._BaseDeleteCryptoKeyVersion,
        KeyManagementServiceRestStub,
    ):
        def __hash__(self):
            return hash("KeyManagementServiceRestTransport.DeleteCryptoKeyVersion")

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
            request: service.DeleteCryptoKeyVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete crypto key version method over HTTP.

            Args:
                request (~.service.DeleteCryptoKeyVersionRequest):
                    The request object. Request message for
                [KeyManagementService.DeleteCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.DeleteCryptoKeyVersion].
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

            http_options = _BaseKeyManagementServiceRestTransport._BaseDeleteCryptoKeyVersion._get_http_options()
            request, metadata = self._interceptor.pre_delete_crypto_key_version(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyManagementServiceRestTransport._BaseDeleteCryptoKeyVersion,
                    "_BaseDeleteCryptoKeyVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.KeyManagementServiceClient.DeleteCryptoKeyVersion",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "DeleteCryptoKeyVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                KeyManagementServiceRestTransport._DeleteCryptoKeyVersion._get_response(
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

            resp = self._interceptor.post_delete_crypto_key_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_crypto_key_version_with_metadata(
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
                    "Received response for google.cloud.kms_v1.KeyManagementServiceClient.delete_crypto_key_version",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "DeleteCryptoKeyVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DestroyCryptoKeyVersion(
        _BaseKeyManagementServiceRestTransport._BaseDestroyCryptoKeyVersion,
        KeyManagementServiceRestStub,
    ):
        def __hash__(self):
            return hash("KeyManagementServiceRestTransport.DestroyCryptoKeyVersion")

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
            request: service.DestroyCryptoKeyVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.CryptoKeyVersion:
            r"""Call the destroy crypto key
            version method over HTTP.

                Args:
                    request (~.service.DestroyCryptoKeyVersionRequest):
                        The request object. Request message for
                    [KeyManagementService.DestroyCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.DestroyCryptoKeyVersion].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.resources.CryptoKeyVersion:
                        A
                    [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
                    represents an individual cryptographic key, and the
                    associated key material.

                    An
                    [ENABLED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.ENABLED]
                    version can be used for cryptographic operations.

                    For security reasons, the raw cryptographic key material
                    represented by a
                    [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
                    can never be viewed or exported. It can only be used to
                    encrypt, decrypt, or sign data when an authorized user
                    or application invokes Cloud KMS.

            """

            http_options = _BaseKeyManagementServiceRestTransport._BaseDestroyCryptoKeyVersion._get_http_options()
            request, metadata = self._interceptor.pre_destroy_crypto_key_version(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyManagementServiceRestTransport._BaseDestroyCryptoKeyVersion,
                    "_BaseDestroyCryptoKeyVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.KeyManagementServiceClient.DestroyCryptoKeyVersion",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "DestroyCryptoKeyVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = KeyManagementServiceRestTransport._DestroyCryptoKeyVersion._get_response(
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
            resp = resources.CryptoKeyVersion()
            pb_resp = resources.CryptoKeyVersion.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_destroy_crypto_key_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_destroy_crypto_key_version_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.CryptoKeyVersion.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.kms_v1.KeyManagementServiceClient.destroy_crypto_key_version",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "DestroyCryptoKeyVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Encrypt(
        _BaseKeyManagementServiceRestTransport._BaseEncrypt,
        KeyManagementServiceRestStub,
    ):
        def __hash__(self):
            return hash("KeyManagementServiceRestTransport.Encrypt")

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
            request: service.EncryptRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.EncryptResponse:
            r"""Call the encrypt method over HTTP.

            Args:
                request (~.service.EncryptRequest):
                    The request object. Request message for
                [KeyManagementService.Encrypt][google.cloud.kms.v1.KeyManagementService.Encrypt].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.EncryptResponse:
                    Response message for
                [KeyManagementService.Encrypt][google.cloud.kms.v1.KeyManagementService.Encrypt].

            """

            http_options = (
                _BaseKeyManagementServiceRestTransport._BaseEncrypt._get_http_options()
            )
            request, metadata = self._interceptor.pre_encrypt(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyManagementServiceRestTransport._BaseEncrypt,
                    "_BaseEncrypt__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.KeyManagementServiceClient.Encrypt",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "Encrypt",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = KeyManagementServiceRestTransport._Encrypt._get_response(
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
            resp = service.EncryptResponse()
            pb_resp = service.EncryptResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_encrypt(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_encrypt_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.EncryptResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.kms_v1.KeyManagementServiceClient.encrypt",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "Encrypt",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ExportTrustedKeyWrappedCryptoKeyVersion(
        _BaseKeyManagementServiceRestTransport._BaseExportTrustedKeyWrappedCryptoKeyVersion,
        KeyManagementServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "KeyManagementServiceRestTransport.ExportTrustedKeyWrappedCryptoKeyVersion"
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
            )
            return response

        def __call__(
            self,
            request: service.ExportTrustedKeyWrappedCryptoKeyVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ExportTrustedKeyWrappedCryptoKeyVersionResponse:
            r"""Call the export trusted key
            wrapped crypto key version method over HTTP.

                Args:
                    request (~.service.ExportTrustedKeyWrappedCryptoKeyVersionRequest):
                        The request object. Request message for
                    [KeyManagementService.ExportTrustedKeyWrappedCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.ExportTrustedKeyWrappedCryptoKeyVersion].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.service.ExportTrustedKeyWrappedCryptoKeyVersionResponse:
                        Response message for
                    [KeyManagementService.ExportTrustedKeyWrappedCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.ExportTrustedKeyWrappedCryptoKeyVersion].

            """

            http_options = _BaseKeyManagementServiceRestTransport._BaseExportTrustedKeyWrappedCryptoKeyVersion._get_http_options()
            request, metadata = (
                self._interceptor.pre_export_trusted_key_wrapped_crypto_key_version(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyManagementServiceRestTransport._BaseExportTrustedKeyWrappedCryptoKeyVersion,
                    "_BaseExportTrustedKeyWrappedCryptoKeyVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.KeyManagementServiceClient.ExportTrustedKeyWrappedCryptoKeyVersion",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "ExportTrustedKeyWrappedCryptoKeyVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = KeyManagementServiceRestTransport._ExportTrustedKeyWrappedCryptoKeyVersion._get_response(
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
            resp = service.ExportTrustedKeyWrappedCryptoKeyVersionResponse()
            pb_resp = service.ExportTrustedKeyWrappedCryptoKeyVersionResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_export_trusted_key_wrapped_crypto_key_version(
                resp
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_export_trusted_key_wrapped_crypto_key_version_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        service.ExportTrustedKeyWrappedCryptoKeyVersionResponse.to_json(
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
                    "Received response for google.cloud.kms_v1.KeyManagementServiceClient.export_trusted_key_wrapped_crypto_key_version",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "ExportTrustedKeyWrappedCryptoKeyVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GenerateRandomBytes(
        _BaseKeyManagementServiceRestTransport._BaseGenerateRandomBytes,
        KeyManagementServiceRestStub,
    ):
        def __hash__(self):
            return hash("KeyManagementServiceRestTransport.GenerateRandomBytes")

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
            request: service.GenerateRandomBytesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.GenerateRandomBytesResponse:
            r"""Call the generate random bytes method over HTTP.

            Args:
                request (~.service.GenerateRandomBytesRequest):
                    The request object. Request message for
                [KeyManagementService.GenerateRandomBytes][google.cloud.kms.v1.KeyManagementService.GenerateRandomBytes].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.GenerateRandomBytesResponse:
                    Response message for
                [KeyManagementService.GenerateRandomBytes][google.cloud.kms.v1.KeyManagementService.GenerateRandomBytes].

            """

            http_options = _BaseKeyManagementServiceRestTransport._BaseGenerateRandomBytes._get_http_options()
            request, metadata = self._interceptor.pre_generate_random_bytes(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyManagementServiceRestTransport._BaseGenerateRandomBytes,
                    "_BaseGenerateRandomBytes__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.KeyManagementServiceClient.GenerateRandomBytes",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "GenerateRandomBytes",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                KeyManagementServiceRestTransport._GenerateRandomBytes._get_response(
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
            resp = service.GenerateRandomBytesResponse()
            pb_resp = service.GenerateRandomBytesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_generate_random_bytes(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_generate_random_bytes_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.GenerateRandomBytesResponse.to_json(
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
                    "Received response for google.cloud.kms_v1.KeyManagementServiceClient.generate_random_bytes",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "GenerateRandomBytes",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetCryptoKey(
        _BaseKeyManagementServiceRestTransport._BaseGetCryptoKey,
        KeyManagementServiceRestStub,
    ):
        def __hash__(self):
            return hash("KeyManagementServiceRestTransport.GetCryptoKey")

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
            request: service.GetCryptoKeyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.CryptoKey:
            r"""Call the get crypto key method over HTTP.

            Args:
                request (~.service.GetCryptoKeyRequest):
                    The request object. Request message for
                [KeyManagementService.GetCryptoKey][google.cloud.kms.v1.KeyManagementService.GetCryptoKey].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.CryptoKey:
                    A [CryptoKey][google.cloud.kms.v1.CryptoKey] represents
                a logical key that can be used for cryptographic
                operations.

                A [CryptoKey][google.cloud.kms.v1.CryptoKey] is made up
                of zero or more
                [versions][google.cloud.kms.v1.CryptoKeyVersion], which
                represent the actual key material used in cryptographic
                operations.

            """

            http_options = _BaseKeyManagementServiceRestTransport._BaseGetCryptoKey._get_http_options()
            request, metadata = self._interceptor.pre_get_crypto_key(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyManagementServiceRestTransport._BaseGetCryptoKey,
                    "_BaseGetCryptoKey__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.KeyManagementServiceClient.GetCryptoKey",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "GetCryptoKey",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = KeyManagementServiceRestTransport._GetCryptoKey._get_response(
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
            resp = resources.CryptoKey()
            pb_resp = resources.CryptoKey.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_crypto_key(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_crypto_key_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.CryptoKey.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.kms_v1.KeyManagementServiceClient.get_crypto_key",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "GetCryptoKey",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetCryptoKeyVersion(
        _BaseKeyManagementServiceRestTransport._BaseGetCryptoKeyVersion,
        KeyManagementServiceRestStub,
    ):
        def __hash__(self):
            return hash("KeyManagementServiceRestTransport.GetCryptoKeyVersion")

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
            request: service.GetCryptoKeyVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.CryptoKeyVersion:
            r"""Call the get crypto key version method over HTTP.

            Args:
                request (~.service.GetCryptoKeyVersionRequest):
                    The request object. Request message for
                [KeyManagementService.GetCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.GetCryptoKeyVersion].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.CryptoKeyVersion:
                    A
                [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
                represents an individual cryptographic key, and the
                associated key material.

                An
                [ENABLED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.ENABLED]
                version can be used for cryptographic operations.

                For security reasons, the raw cryptographic key material
                represented by a
                [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
                can never be viewed or exported. It can only be used to
                encrypt, decrypt, or sign data when an authorized user
                or application invokes Cloud KMS.

            """

            http_options = _BaseKeyManagementServiceRestTransport._BaseGetCryptoKeyVersion._get_http_options()
            request, metadata = self._interceptor.pre_get_crypto_key_version(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyManagementServiceRestTransport._BaseGetCryptoKeyVersion,
                    "_BaseGetCryptoKeyVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.KeyManagementServiceClient.GetCryptoKeyVersion",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "GetCryptoKeyVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                KeyManagementServiceRestTransport._GetCryptoKeyVersion._get_response(
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
            resp = resources.CryptoKeyVersion()
            pb_resp = resources.CryptoKeyVersion.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_crypto_key_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_crypto_key_version_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.CryptoKeyVersion.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.kms_v1.KeyManagementServiceClient.get_crypto_key_version",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "GetCryptoKeyVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetImportJob(
        _BaseKeyManagementServiceRestTransport._BaseGetImportJob,
        KeyManagementServiceRestStub,
    ):
        def __hash__(self):
            return hash("KeyManagementServiceRestTransport.GetImportJob")

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
            request: service.GetImportJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.ImportJob:
            r"""Call the get import job method over HTTP.

            Args:
                request (~.service.GetImportJobRequest):
                    The request object. Request message for
                [KeyManagementService.GetImportJob][google.cloud.kms.v1.KeyManagementService.GetImportJob].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.ImportJob:
                    An [ImportJob][google.cloud.kms.v1.ImportJob] can be
                used to create
                [CryptoKeys][google.cloud.kms.v1.CryptoKey] and
                [CryptoKeyVersions][google.cloud.kms.v1.CryptoKeyVersion]
                using pre-existing key material, generated outside of
                Cloud KMS.

                When an [ImportJob][google.cloud.kms.v1.ImportJob] is
                created, Cloud KMS will generate a "wrapping key", which
                is a public/private key pair. You use the wrapping key
                to encrypt (also known as wrap) the pre-existing key
                material to protect it during the import process. The
                nature of the wrapping key depends on the choice of
                [import_method][google.cloud.kms.v1.ImportJob.import_method].
                When the wrapping key generation is complete, the
                [state][google.cloud.kms.v1.ImportJob.state] will be set
                to
                [ACTIVE][google.cloud.kms.v1.ImportJob.ImportJobState.ACTIVE]
                and the
                [public_key][google.cloud.kms.v1.ImportJob.public_key]
                can be fetched. The fetched public key can then be used
                to wrap your pre-existing key material.

                Once the key material is wrapped, it can be imported
                into a new
                [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
                in an existing
                [CryptoKey][google.cloud.kms.v1.CryptoKey] by calling
                [ImportCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.ImportCryptoKeyVersion].
                Multiple
                [CryptoKeyVersions][google.cloud.kms.v1.CryptoKeyVersion]
                can be imported with a single
                [ImportJob][google.cloud.kms.v1.ImportJob]. Cloud KMS
                uses the private key portion of the wrapping key to
                unwrap the key material. Only Cloud KMS has access to
                the private key.

                An [ImportJob][google.cloud.kms.v1.ImportJob] expires 3
                days after it is created. Once expired, Cloud KMS will
                no longer be able to import or unwrap any key material
                that was wrapped with the
                [ImportJob][google.cloud.kms.v1.ImportJob]'s public key.

                For more information, see `Importing a
                key <https://cloud.google.com/kms/docs/importing-a-key>`__.

            """

            http_options = _BaseKeyManagementServiceRestTransport._BaseGetImportJob._get_http_options()
            request, metadata = self._interceptor.pre_get_import_job(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyManagementServiceRestTransport._BaseGetImportJob,
                    "_BaseGetImportJob__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.KeyManagementServiceClient.GetImportJob",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "GetImportJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = KeyManagementServiceRestTransport._GetImportJob._get_response(
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
            resp = resources.ImportJob()
            pb_resp = resources.ImportJob.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_import_job(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_import_job_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.ImportJob.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.kms_v1.KeyManagementServiceClient.get_import_job",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "GetImportJob",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetKeyRing(
        _BaseKeyManagementServiceRestTransport._BaseGetKeyRing,
        KeyManagementServiceRestStub,
    ):
        def __hash__(self):
            return hash("KeyManagementServiceRestTransport.GetKeyRing")

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
            request: service.GetKeyRingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.KeyRing:
            r"""Call the get key ring method over HTTP.

            Args:
                request (~.service.GetKeyRingRequest):
                    The request object. Request message for
                [KeyManagementService.GetKeyRing][google.cloud.kms.v1.KeyManagementService.GetKeyRing].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.KeyRing:
                    A [KeyRing][google.cloud.kms.v1.KeyRing] is a toplevel
                logical grouping of
                [CryptoKeys][google.cloud.kms.v1.CryptoKey].

            """

            http_options = _BaseKeyManagementServiceRestTransport._BaseGetKeyRing._get_http_options()
            request, metadata = self._interceptor.pre_get_key_ring(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyManagementServiceRestTransport._BaseGetKeyRing,
                    "_BaseGetKeyRing__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.KeyManagementServiceClient.GetKeyRing",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "GetKeyRing",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = KeyManagementServiceRestTransport._GetKeyRing._get_response(
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
            resp = resources.KeyRing()
            pb_resp = resources.KeyRing.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_key_ring(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_key_ring_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.KeyRing.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.kms_v1.KeyManagementServiceClient.get_key_ring",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "GetKeyRing",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetPublicKey(
        _BaseKeyManagementServiceRestTransport._BaseGetPublicKey,
        KeyManagementServiceRestStub,
    ):
        def __hash__(self):
            return hash("KeyManagementServiceRestTransport.GetPublicKey")

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
            request: service.GetPublicKeyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.PublicKey:
            r"""Call the get public key method over HTTP.

            Args:
                request (~.service.GetPublicKeyRequest):
                    The request object. Request message for
                [KeyManagementService.GetPublicKey][google.cloud.kms.v1.KeyManagementService.GetPublicKey].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.PublicKey:
                    The public keys for a given
                [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion].
                Obtained via
                [GetPublicKey][google.cloud.kms.v1.KeyManagementService.GetPublicKey].

            """

            http_options = _BaseKeyManagementServiceRestTransport._BaseGetPublicKey._get_http_options()
            request, metadata = self._interceptor.pre_get_public_key(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyManagementServiceRestTransport._BaseGetPublicKey,
                    "_BaseGetPublicKey__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.KeyManagementServiceClient.GetPublicKey",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "GetPublicKey",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = KeyManagementServiceRestTransport._GetPublicKey._get_response(
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
            resp = resources.PublicKey()
            pb_resp = resources.PublicKey.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_public_key(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_public_key_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.PublicKey.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.kms_v1.KeyManagementServiceClient.get_public_key",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "GetPublicKey",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetRetiredResource(
        _BaseKeyManagementServiceRestTransport._BaseGetRetiredResource,
        KeyManagementServiceRestStub,
    ):
        def __hash__(self):
            return hash("KeyManagementServiceRestTransport.GetRetiredResource")

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
            request: service.GetRetiredResourceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.RetiredResource:
            r"""Call the get retired resource method over HTTP.

            Args:
                request (~.service.GetRetiredResourceRequest):
                    The request object. Request message for
                [KeyManagementService.GetRetiredResource][google.cloud.kms.v1.KeyManagementService.GetRetiredResource].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.RetiredResource:
                    A RetiredResource resource represents the record of a
                deleted [CryptoKey][google.cloud.kms.v1.CryptoKey]. Its
                purpose is to provide visibility into retained user data
                and to prevent reuse of these names for new
                [CryptoKeys][google.cloud.kms.v1.CryptoKey].

            """

            http_options = _BaseKeyManagementServiceRestTransport._BaseGetRetiredResource._get_http_options()
            request, metadata = self._interceptor.pre_get_retired_resource(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyManagementServiceRestTransport._BaseGetRetiredResource,
                    "_BaseGetRetiredResource__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.KeyManagementServiceClient.GetRetiredResource",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "GetRetiredResource",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                KeyManagementServiceRestTransport._GetRetiredResource._get_response(
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
            resp = resources.RetiredResource()
            pb_resp = resources.RetiredResource.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_retired_resource(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_retired_resource_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.RetiredResource.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.kms_v1.KeyManagementServiceClient.get_retired_resource",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "GetRetiredResource",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ImportCryptoKeyVersion(
        _BaseKeyManagementServiceRestTransport._BaseImportCryptoKeyVersion,
        KeyManagementServiceRestStub,
    ):
        def __hash__(self):
            return hash("KeyManagementServiceRestTransport.ImportCryptoKeyVersion")

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
            request: service.ImportCryptoKeyVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.CryptoKeyVersion:
            r"""Call the import crypto key version method over HTTP.

            Args:
                request (~.service.ImportCryptoKeyVersionRequest):
                    The request object. Request message for
                [KeyManagementService.ImportCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.ImportCryptoKeyVersion].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.CryptoKeyVersion:
                    A
                [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
                represents an individual cryptographic key, and the
                associated key material.

                An
                [ENABLED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.ENABLED]
                version can be used for cryptographic operations.

                For security reasons, the raw cryptographic key material
                represented by a
                [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
                can never be viewed or exported. It can only be used to
                encrypt, decrypt, or sign data when an authorized user
                or application invokes Cloud KMS.

            """

            http_options = _BaseKeyManagementServiceRestTransport._BaseImportCryptoKeyVersion._get_http_options()
            request, metadata = self._interceptor.pre_import_crypto_key_version(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyManagementServiceRestTransport._BaseImportCryptoKeyVersion,
                    "_BaseImportCryptoKeyVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.KeyManagementServiceClient.ImportCryptoKeyVersion",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "ImportCryptoKeyVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                KeyManagementServiceRestTransport._ImportCryptoKeyVersion._get_response(
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
            resp = resources.CryptoKeyVersion()
            pb_resp = resources.CryptoKeyVersion.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_import_crypto_key_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_import_crypto_key_version_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.CryptoKeyVersion.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.kms_v1.KeyManagementServiceClient.import_crypto_key_version",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "ImportCryptoKeyVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ImportTrustedKeyWrappedCryptoKeyVersion(
        _BaseKeyManagementServiceRestTransport._BaseImportTrustedKeyWrappedCryptoKeyVersion,
        KeyManagementServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "KeyManagementServiceRestTransport.ImportTrustedKeyWrappedCryptoKeyVersion"
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
            request: service.ImportTrustedKeyWrappedCryptoKeyVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.CryptoKeyVersion:
            r"""Call the import trusted key
            wrapped crypto key version method over HTTP.

                Args:
                    request (~.service.ImportTrustedKeyWrappedCryptoKeyVersionRequest):
                        The request object. Request message for
                    [KeyManagementService.ImportTrustedKeyWrappedCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.ImportTrustedKeyWrappedCryptoKeyVersion].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.resources.CryptoKeyVersion:
                        A
                    [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
                    represents an individual cryptographic key, and the
                    associated key material.

                    An
                    [ENABLED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.ENABLED]
                    version can be used for cryptographic operations.

                    For security reasons, the raw cryptographic key material
                    represented by a
                    [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
                    can never be viewed or exported. It can only be used to
                    encrypt, decrypt, or sign data when an authorized user
                    or application invokes Cloud KMS.

            """

            http_options = _BaseKeyManagementServiceRestTransport._BaseImportTrustedKeyWrappedCryptoKeyVersion._get_http_options()
            request, metadata = (
                self._interceptor.pre_import_trusted_key_wrapped_crypto_key_version(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyManagementServiceRestTransport._BaseImportTrustedKeyWrappedCryptoKeyVersion,
                    "_BaseImportTrustedKeyWrappedCryptoKeyVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.KeyManagementServiceClient.ImportTrustedKeyWrappedCryptoKeyVersion",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "ImportTrustedKeyWrappedCryptoKeyVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = KeyManagementServiceRestTransport._ImportTrustedKeyWrappedCryptoKeyVersion._get_response(
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
            resp = resources.CryptoKeyVersion()
            pb_resp = resources.CryptoKeyVersion.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_import_trusted_key_wrapped_crypto_key_version(
                resp
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_import_trusted_key_wrapped_crypto_key_version_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.CryptoKeyVersion.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.kms_v1.KeyManagementServiceClient.import_trusted_key_wrapped_crypto_key_version",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "ImportTrustedKeyWrappedCryptoKeyVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListCryptoKeys(
        _BaseKeyManagementServiceRestTransport._BaseListCryptoKeys,
        KeyManagementServiceRestStub,
    ):
        def __hash__(self):
            return hash("KeyManagementServiceRestTransport.ListCryptoKeys")

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
            request: service.ListCryptoKeysRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListCryptoKeysResponse:
            r"""Call the list crypto keys method over HTTP.

            Args:
                request (~.service.ListCryptoKeysRequest):
                    The request object. Request message for
                [KeyManagementService.ListCryptoKeys][google.cloud.kms.v1.KeyManagementService.ListCryptoKeys].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListCryptoKeysResponse:
                    Response message for
                [KeyManagementService.ListCryptoKeys][google.cloud.kms.v1.KeyManagementService.ListCryptoKeys].

            """

            http_options = _BaseKeyManagementServiceRestTransport._BaseListCryptoKeys._get_http_options()
            request, metadata = self._interceptor.pre_list_crypto_keys(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyManagementServiceRestTransport._BaseListCryptoKeys,
                    "_BaseListCryptoKeys__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.KeyManagementServiceClient.ListCryptoKeys",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "ListCryptoKeys",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = KeyManagementServiceRestTransport._ListCryptoKeys._get_response(
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
            resp = service.ListCryptoKeysResponse()
            pb_resp = service.ListCryptoKeysResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_crypto_keys(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_crypto_keys_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListCryptoKeysResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.kms_v1.KeyManagementServiceClient.list_crypto_keys",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "ListCryptoKeys",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListCryptoKeyVersions(
        _BaseKeyManagementServiceRestTransport._BaseListCryptoKeyVersions,
        KeyManagementServiceRestStub,
    ):
        def __hash__(self):
            return hash("KeyManagementServiceRestTransport.ListCryptoKeyVersions")

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
            request: service.ListCryptoKeyVersionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListCryptoKeyVersionsResponse:
            r"""Call the list crypto key versions method over HTTP.

            Args:
                request (~.service.ListCryptoKeyVersionsRequest):
                    The request object. Request message for
                [KeyManagementService.ListCryptoKeyVersions][google.cloud.kms.v1.KeyManagementService.ListCryptoKeyVersions].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListCryptoKeyVersionsResponse:
                    Response message for
                [KeyManagementService.ListCryptoKeyVersions][google.cloud.kms.v1.KeyManagementService.ListCryptoKeyVersions].

            """

            http_options = _BaseKeyManagementServiceRestTransport._BaseListCryptoKeyVersions._get_http_options()
            request, metadata = self._interceptor.pre_list_crypto_key_versions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyManagementServiceRestTransport._BaseListCryptoKeyVersions,
                    "_BaseListCryptoKeyVersions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.KeyManagementServiceClient.ListCryptoKeyVersions",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "ListCryptoKeyVersions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                KeyManagementServiceRestTransport._ListCryptoKeyVersions._get_response(
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
            resp = service.ListCryptoKeyVersionsResponse()
            pb_resp = service.ListCryptoKeyVersionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_crypto_key_versions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_crypto_key_versions_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListCryptoKeyVersionsResponse.to_json(
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
                    "Received response for google.cloud.kms_v1.KeyManagementServiceClient.list_crypto_key_versions",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "ListCryptoKeyVersions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListImportJobs(
        _BaseKeyManagementServiceRestTransport._BaseListImportJobs,
        KeyManagementServiceRestStub,
    ):
        def __hash__(self):
            return hash("KeyManagementServiceRestTransport.ListImportJobs")

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
            request: service.ListImportJobsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListImportJobsResponse:
            r"""Call the list import jobs method over HTTP.

            Args:
                request (~.service.ListImportJobsRequest):
                    The request object. Request message for
                [KeyManagementService.ListImportJobs][google.cloud.kms.v1.KeyManagementService.ListImportJobs].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListImportJobsResponse:
                    Response message for
                [KeyManagementService.ListImportJobs][google.cloud.kms.v1.KeyManagementService.ListImportJobs].

            """

            http_options = _BaseKeyManagementServiceRestTransport._BaseListImportJobs._get_http_options()
            request, metadata = self._interceptor.pre_list_import_jobs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyManagementServiceRestTransport._BaseListImportJobs,
                    "_BaseListImportJobs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.KeyManagementServiceClient.ListImportJobs",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "ListImportJobs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = KeyManagementServiceRestTransport._ListImportJobs._get_response(
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
            resp = service.ListImportJobsResponse()
            pb_resp = service.ListImportJobsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_import_jobs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_import_jobs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListImportJobsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.kms_v1.KeyManagementServiceClient.list_import_jobs",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "ListImportJobs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListKeyRings(
        _BaseKeyManagementServiceRestTransport._BaseListKeyRings,
        KeyManagementServiceRestStub,
    ):
        def __hash__(self):
            return hash("KeyManagementServiceRestTransport.ListKeyRings")

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
            request: service.ListKeyRingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListKeyRingsResponse:
            r"""Call the list key rings method over HTTP.

            Args:
                request (~.service.ListKeyRingsRequest):
                    The request object. Request message for
                [KeyManagementService.ListKeyRings][google.cloud.kms.v1.KeyManagementService.ListKeyRings].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListKeyRingsResponse:
                    Response message for
                [KeyManagementService.ListKeyRings][google.cloud.kms.v1.KeyManagementService.ListKeyRings].

            """

            http_options = _BaseKeyManagementServiceRestTransport._BaseListKeyRings._get_http_options()
            request, metadata = self._interceptor.pre_list_key_rings(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyManagementServiceRestTransport._BaseListKeyRings,
                    "_BaseListKeyRings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.KeyManagementServiceClient.ListKeyRings",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "ListKeyRings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = KeyManagementServiceRestTransport._ListKeyRings._get_response(
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
            resp = service.ListKeyRingsResponse()
            pb_resp = service.ListKeyRingsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_key_rings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_key_rings_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListKeyRingsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.kms_v1.KeyManagementServiceClient.list_key_rings",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "ListKeyRings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListRetiredResources(
        _BaseKeyManagementServiceRestTransport._BaseListRetiredResources,
        KeyManagementServiceRestStub,
    ):
        def __hash__(self):
            return hash("KeyManagementServiceRestTransport.ListRetiredResources")

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
            request: service.ListRetiredResourcesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListRetiredResourcesResponse:
            r"""Call the list retired resources method over HTTP.

            Args:
                request (~.service.ListRetiredResourcesRequest):
                    The request object. Request message for
                [KeyManagementService.ListRetiredResources][google.cloud.kms.v1.KeyManagementService.ListRetiredResources].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListRetiredResourcesResponse:
                    Response message for
                [KeyManagementService.ListRetiredResources][google.cloud.kms.v1.KeyManagementService.ListRetiredResources].

            """

            http_options = _BaseKeyManagementServiceRestTransport._BaseListRetiredResources._get_http_options()
            request, metadata = self._interceptor.pre_list_retired_resources(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyManagementServiceRestTransport._BaseListRetiredResources,
                    "_BaseListRetiredResources__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.KeyManagementServiceClient.ListRetiredResources",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "ListRetiredResources",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                KeyManagementServiceRestTransport._ListRetiredResources._get_response(
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
            resp = service.ListRetiredResourcesResponse()
            pb_resp = service.ListRetiredResourcesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_retired_resources(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_retired_resources_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListRetiredResourcesResponse.to_json(
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
                    "Received response for google.cloud.kms_v1.KeyManagementServiceClient.list_retired_resources",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "ListRetiredResources",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _MacSign(
        _BaseKeyManagementServiceRestTransport._BaseMacSign,
        KeyManagementServiceRestStub,
    ):
        def __hash__(self):
            return hash("KeyManagementServiceRestTransport.MacSign")

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
            request: service.MacSignRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.MacSignResponse:
            r"""Call the mac sign method over HTTP.

            Args:
                request (~.service.MacSignRequest):
                    The request object. Request message for
                [KeyManagementService.MacSign][google.cloud.kms.v1.KeyManagementService.MacSign].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.MacSignResponse:
                    Response message for
                [KeyManagementService.MacSign][google.cloud.kms.v1.KeyManagementService.MacSign].

            """

            http_options = (
                _BaseKeyManagementServiceRestTransport._BaseMacSign._get_http_options()
            )
            request, metadata = self._interceptor.pre_mac_sign(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyManagementServiceRestTransport._BaseMacSign,
                    "_BaseMacSign__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.KeyManagementServiceClient.MacSign",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "MacSign",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = KeyManagementServiceRestTransport._MacSign._get_response(
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
            resp = service.MacSignResponse()
            pb_resp = service.MacSignResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_mac_sign(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_mac_sign_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.MacSignResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.kms_v1.KeyManagementServiceClient.mac_sign",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "MacSign",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _MacVerify(
        _BaseKeyManagementServiceRestTransport._BaseMacVerify,
        KeyManagementServiceRestStub,
    ):
        def __hash__(self):
            return hash("KeyManagementServiceRestTransport.MacVerify")

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
            request: service.MacVerifyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.MacVerifyResponse:
            r"""Call the mac verify method over HTTP.

            Args:
                request (~.service.MacVerifyRequest):
                    The request object. Request message for
                [KeyManagementService.MacVerify][google.cloud.kms.v1.KeyManagementService.MacVerify].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.MacVerifyResponse:
                    Response message for
                [KeyManagementService.MacVerify][google.cloud.kms.v1.KeyManagementService.MacVerify].

            """

            http_options = _BaseKeyManagementServiceRestTransport._BaseMacVerify._get_http_options()
            request, metadata = self._interceptor.pre_mac_verify(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyManagementServiceRestTransport._BaseMacVerify,
                    "_BaseMacVerify__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.KeyManagementServiceClient.MacVerify",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "MacVerify",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = KeyManagementServiceRestTransport._MacVerify._get_response(
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
            resp = service.MacVerifyResponse()
            pb_resp = service.MacVerifyResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_mac_verify(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_mac_verify_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.MacVerifyResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.kms_v1.KeyManagementServiceClient.mac_verify",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "MacVerify",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RawDecrypt(
        _BaseKeyManagementServiceRestTransport._BaseRawDecrypt,
        KeyManagementServiceRestStub,
    ):
        def __hash__(self):
            return hash("KeyManagementServiceRestTransport.RawDecrypt")

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
            request: service.RawDecryptRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.RawDecryptResponse:
            r"""Call the raw decrypt method over HTTP.

            Args:
                request (~.service.RawDecryptRequest):
                    The request object. Request message for
                [KeyManagementService.RawDecrypt][google.cloud.kms.v1.KeyManagementService.RawDecrypt].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.RawDecryptResponse:
                    Response message for
                [KeyManagementService.RawDecrypt][google.cloud.kms.v1.KeyManagementService.RawDecrypt].

            """

            http_options = _BaseKeyManagementServiceRestTransport._BaseRawDecrypt._get_http_options()
            request, metadata = self._interceptor.pre_raw_decrypt(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyManagementServiceRestTransport._BaseRawDecrypt,
                    "_BaseRawDecrypt__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.KeyManagementServiceClient.RawDecrypt",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "RawDecrypt",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = KeyManagementServiceRestTransport._RawDecrypt._get_response(
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
            resp = service.RawDecryptResponse()
            pb_resp = service.RawDecryptResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_raw_decrypt(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_raw_decrypt_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.RawDecryptResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.kms_v1.KeyManagementServiceClient.raw_decrypt",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "RawDecrypt",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RawEncrypt(
        _BaseKeyManagementServiceRestTransport._BaseRawEncrypt,
        KeyManagementServiceRestStub,
    ):
        def __hash__(self):
            return hash("KeyManagementServiceRestTransport.RawEncrypt")

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
            request: service.RawEncryptRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.RawEncryptResponse:
            r"""Call the raw encrypt method over HTTP.

            Args:
                request (~.service.RawEncryptRequest):
                    The request object. Request message for
                [KeyManagementService.RawEncrypt][google.cloud.kms.v1.KeyManagementService.RawEncrypt].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.RawEncryptResponse:
                    Response message for
                [KeyManagementService.RawEncrypt][google.cloud.kms.v1.KeyManagementService.RawEncrypt].

            """

            http_options = _BaseKeyManagementServiceRestTransport._BaseRawEncrypt._get_http_options()
            request, metadata = self._interceptor.pre_raw_encrypt(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyManagementServiceRestTransport._BaseRawEncrypt,
                    "_BaseRawEncrypt__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.KeyManagementServiceClient.RawEncrypt",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "RawEncrypt",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = KeyManagementServiceRestTransport._RawEncrypt._get_response(
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
            resp = service.RawEncryptResponse()
            pb_resp = service.RawEncryptResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_raw_encrypt(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_raw_encrypt_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.RawEncryptResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.kms_v1.KeyManagementServiceClient.raw_encrypt",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "RawEncrypt",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RestoreCryptoKeyVersion(
        _BaseKeyManagementServiceRestTransport._BaseRestoreCryptoKeyVersion,
        KeyManagementServiceRestStub,
    ):
        def __hash__(self):
            return hash("KeyManagementServiceRestTransport.RestoreCryptoKeyVersion")

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
            request: service.RestoreCryptoKeyVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.CryptoKeyVersion:
            r"""Call the restore crypto key
            version method over HTTP.

                Args:
                    request (~.service.RestoreCryptoKeyVersionRequest):
                        The request object. Request message for
                    [KeyManagementService.RestoreCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.RestoreCryptoKeyVersion].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.resources.CryptoKeyVersion:
                        A
                    [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
                    represents an individual cryptographic key, and the
                    associated key material.

                    An
                    [ENABLED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.ENABLED]
                    version can be used for cryptographic operations.

                    For security reasons, the raw cryptographic key material
                    represented by a
                    [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
                    can never be viewed or exported. It can only be used to
                    encrypt, decrypt, or sign data when an authorized user
                    or application invokes Cloud KMS.

            """

            http_options = _BaseKeyManagementServiceRestTransport._BaseRestoreCryptoKeyVersion._get_http_options()
            request, metadata = self._interceptor.pre_restore_crypto_key_version(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyManagementServiceRestTransport._BaseRestoreCryptoKeyVersion,
                    "_BaseRestoreCryptoKeyVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.KeyManagementServiceClient.RestoreCryptoKeyVersion",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "RestoreCryptoKeyVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = KeyManagementServiceRestTransport._RestoreCryptoKeyVersion._get_response(
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
            resp = resources.CryptoKeyVersion()
            pb_resp = resources.CryptoKeyVersion.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_restore_crypto_key_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_restore_crypto_key_version_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.CryptoKeyVersion.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.kms_v1.KeyManagementServiceClient.restore_crypto_key_version",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "RestoreCryptoKeyVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateCryptoKey(
        _BaseKeyManagementServiceRestTransport._BaseUpdateCryptoKey,
        KeyManagementServiceRestStub,
    ):
        def __hash__(self):
            return hash("KeyManagementServiceRestTransport.UpdateCryptoKey")

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
            request: service.UpdateCryptoKeyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.CryptoKey:
            r"""Call the update crypto key method over HTTP.

            Args:
                request (~.service.UpdateCryptoKeyRequest):
                    The request object. Request message for
                [KeyManagementService.UpdateCryptoKey][google.cloud.kms.v1.KeyManagementService.UpdateCryptoKey].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.CryptoKey:
                    A [CryptoKey][google.cloud.kms.v1.CryptoKey] represents
                a logical key that can be used for cryptographic
                operations.

                A [CryptoKey][google.cloud.kms.v1.CryptoKey] is made up
                of zero or more
                [versions][google.cloud.kms.v1.CryptoKeyVersion], which
                represent the actual key material used in cryptographic
                operations.

            """

            http_options = _BaseKeyManagementServiceRestTransport._BaseUpdateCryptoKey._get_http_options()
            request, metadata = self._interceptor.pre_update_crypto_key(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyManagementServiceRestTransport._BaseUpdateCryptoKey,
                    "_BaseUpdateCryptoKey__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.KeyManagementServiceClient.UpdateCryptoKey",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "UpdateCryptoKey",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = KeyManagementServiceRestTransport._UpdateCryptoKey._get_response(
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
            resp = resources.CryptoKey()
            pb_resp = resources.CryptoKey.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_crypto_key(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_crypto_key_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.CryptoKey.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.kms_v1.KeyManagementServiceClient.update_crypto_key",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "UpdateCryptoKey",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateCryptoKeyPrimaryVersion(
        _BaseKeyManagementServiceRestTransport._BaseUpdateCryptoKeyPrimaryVersion,
        KeyManagementServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "KeyManagementServiceRestTransport.UpdateCryptoKeyPrimaryVersion"
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
            request: service.UpdateCryptoKeyPrimaryVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.CryptoKey:
            r"""Call the update crypto key primary
            version method over HTTP.

                Args:
                    request (~.service.UpdateCryptoKeyPrimaryVersionRequest):
                        The request object. Request message for
                    [KeyManagementService.UpdateCryptoKeyPrimaryVersion][google.cloud.kms.v1.KeyManagementService.UpdateCryptoKeyPrimaryVersion].
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.resources.CryptoKey:
                        A [CryptoKey][google.cloud.kms.v1.CryptoKey] represents
                    a logical key that can be used for cryptographic
                    operations.

                    A [CryptoKey][google.cloud.kms.v1.CryptoKey] is made up
                    of zero or more
                    [versions][google.cloud.kms.v1.CryptoKeyVersion], which
                    represent the actual key material used in cryptographic
                    operations.

            """

            http_options = _BaseKeyManagementServiceRestTransport._BaseUpdateCryptoKeyPrimaryVersion._get_http_options()
            request, metadata = self._interceptor.pre_update_crypto_key_primary_version(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyManagementServiceRestTransport._BaseUpdateCryptoKeyPrimaryVersion,
                    "_BaseUpdateCryptoKeyPrimaryVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.KeyManagementServiceClient.UpdateCryptoKeyPrimaryVersion",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "UpdateCryptoKeyPrimaryVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = KeyManagementServiceRestTransport._UpdateCryptoKeyPrimaryVersion._get_response(
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
            resp = resources.CryptoKey()
            pb_resp = resources.CryptoKey.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_crypto_key_primary_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_update_crypto_key_primary_version_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.CryptoKey.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.kms_v1.KeyManagementServiceClient.update_crypto_key_primary_version",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "UpdateCryptoKeyPrimaryVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateCryptoKeyVersion(
        _BaseKeyManagementServiceRestTransport._BaseUpdateCryptoKeyVersion,
        KeyManagementServiceRestStub,
    ):
        def __hash__(self):
            return hash("KeyManagementServiceRestTransport.UpdateCryptoKeyVersion")

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
            request: service.UpdateCryptoKeyVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.CryptoKeyVersion:
            r"""Call the update crypto key version method over HTTP.

            Args:
                request (~.service.UpdateCryptoKeyVersionRequest):
                    The request object. Request message for
                [KeyManagementService.UpdateCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.UpdateCryptoKeyVersion].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.CryptoKeyVersion:
                    A
                [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
                represents an individual cryptographic key, and the
                associated key material.

                An
                [ENABLED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.ENABLED]
                version can be used for cryptographic operations.

                For security reasons, the raw cryptographic key material
                represented by a
                [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]
                can never be viewed or exported. It can only be used to
                encrypt, decrypt, or sign data when an authorized user
                or application invokes Cloud KMS.

            """

            http_options = _BaseKeyManagementServiceRestTransport._BaseUpdateCryptoKeyVersion._get_http_options()
            request, metadata = self._interceptor.pre_update_crypto_key_version(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyManagementServiceRestTransport._BaseUpdateCryptoKeyVersion,
                    "_BaseUpdateCryptoKeyVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.KeyManagementServiceClient.UpdateCryptoKeyVersion",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "UpdateCryptoKeyVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                KeyManagementServiceRestTransport._UpdateCryptoKeyVersion._get_response(
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
            resp = resources.CryptoKeyVersion()
            pb_resp = resources.CryptoKeyVersion.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_crypto_key_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_crypto_key_version_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.CryptoKeyVersion.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.kms_v1.KeyManagementServiceClient.update_crypto_key_version",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "UpdateCryptoKeyVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def asymmetric_decrypt(
        self,
    ) -> Callable[
        [service.AsymmetricDecryptRequest], service.AsymmetricDecryptResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._AsymmetricDecrypt(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def asymmetric_sign(
        self,
    ) -> Callable[[service.AsymmetricSignRequest], service.AsymmetricSignResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._AsymmetricSign(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_crypto_key(
        self,
    ) -> Callable[[service.CreateCryptoKeyRequest], resources.CryptoKey]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateCryptoKey(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_crypto_key_version(
        self,
    ) -> Callable[[service.CreateCryptoKeyVersionRequest], resources.CryptoKeyVersion]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateCryptoKeyVersion(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_import_job(
        self,
    ) -> Callable[[service.CreateImportJobRequest], resources.ImportJob]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateImportJob(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_key_ring(
        self,
    ) -> Callable[[service.CreateKeyRingRequest], resources.KeyRing]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateKeyRing(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def decapsulate(
        self,
    ) -> Callable[[service.DecapsulateRequest], service.DecapsulateResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Decapsulate(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def decrypt(self) -> Callable[[service.DecryptRequest], service.DecryptResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Decrypt(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_crypto_key(
        self,
    ) -> Callable[[service.DeleteCryptoKeyRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteCryptoKey(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_crypto_key_version(
        self,
    ) -> Callable[[service.DeleteCryptoKeyVersionRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteCryptoKeyVersion(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def destroy_crypto_key_version(
        self,
    ) -> Callable[[service.DestroyCryptoKeyVersionRequest], resources.CryptoKeyVersion]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DestroyCryptoKeyVersion(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def encrypt(self) -> Callable[[service.EncryptRequest], service.EncryptResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Encrypt(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def export_trusted_key_wrapped_crypto_key_version(
        self,
    ) -> Callable[
        [service.ExportTrustedKeyWrappedCryptoKeyVersionRequest],
        service.ExportTrustedKeyWrappedCryptoKeyVersionResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExportTrustedKeyWrappedCryptoKeyVersion(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def generate_random_bytes(
        self,
    ) -> Callable[
        [service.GenerateRandomBytesRequest], service.GenerateRandomBytesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GenerateRandomBytes(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_crypto_key(
        self,
    ) -> Callable[[service.GetCryptoKeyRequest], resources.CryptoKey]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetCryptoKey(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_crypto_key_version(
        self,
    ) -> Callable[[service.GetCryptoKeyVersionRequest], resources.CryptoKeyVersion]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetCryptoKeyVersion(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_import_job(
        self,
    ) -> Callable[[service.GetImportJobRequest], resources.ImportJob]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetImportJob(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_key_ring(self) -> Callable[[service.GetKeyRingRequest], resources.KeyRing]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetKeyRing(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_public_key(
        self,
    ) -> Callable[[service.GetPublicKeyRequest], resources.PublicKey]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetPublicKey(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_retired_resource(
        self,
    ) -> Callable[[service.GetRetiredResourceRequest], resources.RetiredResource]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetRetiredResource(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def import_crypto_key_version(
        self,
    ) -> Callable[[service.ImportCryptoKeyVersionRequest], resources.CryptoKeyVersion]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ImportCryptoKeyVersion(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def import_trusted_key_wrapped_crypto_key_version(
        self,
    ) -> Callable[
        [service.ImportTrustedKeyWrappedCryptoKeyVersionRequest],
        resources.CryptoKeyVersion,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ImportTrustedKeyWrappedCryptoKeyVersion(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_crypto_keys(
        self,
    ) -> Callable[[service.ListCryptoKeysRequest], service.ListCryptoKeysResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListCryptoKeys(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_crypto_key_versions(
        self,
    ) -> Callable[
        [service.ListCryptoKeyVersionsRequest], service.ListCryptoKeyVersionsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListCryptoKeyVersions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_import_jobs(
        self,
    ) -> Callable[[service.ListImportJobsRequest], service.ListImportJobsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListImportJobs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_key_rings(
        self,
    ) -> Callable[[service.ListKeyRingsRequest], service.ListKeyRingsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListKeyRings(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_retired_resources(
        self,
    ) -> Callable[
        [service.ListRetiredResourcesRequest], service.ListRetiredResourcesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListRetiredResources(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def mac_sign(self) -> Callable[[service.MacSignRequest], service.MacSignResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._MacSign(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def mac_verify(
        self,
    ) -> Callable[[service.MacVerifyRequest], service.MacVerifyResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._MacVerify(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def raw_decrypt(
        self,
    ) -> Callable[[service.RawDecryptRequest], service.RawDecryptResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RawDecrypt(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def raw_encrypt(
        self,
    ) -> Callable[[service.RawEncryptRequest], service.RawEncryptResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RawEncrypt(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def restore_crypto_key_version(
        self,
    ) -> Callable[[service.RestoreCryptoKeyVersionRequest], resources.CryptoKeyVersion]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RestoreCryptoKeyVersion(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_crypto_key(
        self,
    ) -> Callable[[service.UpdateCryptoKeyRequest], resources.CryptoKey]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateCryptoKey(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_crypto_key_primary_version(
        self,
    ) -> Callable[[service.UpdateCryptoKeyPrimaryVersionRequest], resources.CryptoKey]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateCryptoKeyPrimaryVersion(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_crypto_key_version(
        self,
    ) -> Callable[[service.UpdateCryptoKeyVersionRequest], resources.CryptoKeyVersion]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateCryptoKeyVersion(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseKeyManagementServiceRestTransport._BaseGetLocation,
        KeyManagementServiceRestStub,
    ):
        def __hash__(self):
            return hash("KeyManagementServiceRestTransport.GetLocation")

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

            http_options = _BaseKeyManagementServiceRestTransport._BaseGetLocation._get_http_options()
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyManagementServiceRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.kms_v1.KeyManagementServiceClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = KeyManagementServiceRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.kms_v1.KeyManagementServiceAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
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
        _BaseKeyManagementServiceRestTransport._BaseListLocations,
        KeyManagementServiceRestStub,
    ):
        def __hash__(self):
            return hash("KeyManagementServiceRestTransport.ListLocations")

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

            http_options = _BaseKeyManagementServiceRestTransport._BaseListLocations._get_http_options()
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyManagementServiceRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.kms_v1.KeyManagementServiceClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = KeyManagementServiceRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.kms_v1.KeyManagementServiceAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
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
        _BaseKeyManagementServiceRestTransport._BaseGetIamPolicy,
        KeyManagementServiceRestStub,
    ):
        def __hash__(self):
            return hash("KeyManagementServiceRestTransport.GetIamPolicy")

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

            http_options = _BaseKeyManagementServiceRestTransport._BaseGetIamPolicy._get_http_options()
            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyManagementServiceRestTransport._BaseGetIamPolicy,
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
                    f"Sending request for google.cloud.kms_v1.KeyManagementServiceClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "GetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = KeyManagementServiceRestTransport._GetIamPolicy._get_response(
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
                    "Received response for google.cloud.kms_v1.KeyManagementServiceAsyncClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
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
        _BaseKeyManagementServiceRestTransport._BaseSetIamPolicy,
        KeyManagementServiceRestStub,
    ):
        def __hash__(self):
            return hash("KeyManagementServiceRestTransport.SetIamPolicy")

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

            http_options = _BaseKeyManagementServiceRestTransport._BaseSetIamPolicy._get_http_options()
            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyManagementServiceRestTransport._BaseSetIamPolicy,
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
                    f"Sending request for google.cloud.kms_v1.KeyManagementServiceClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "SetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = KeyManagementServiceRestTransport._SetIamPolicy._get_response(
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
                    "Received response for google.cloud.kms_v1.KeyManagementServiceAsyncClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
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
        _BaseKeyManagementServiceRestTransport._BaseTestIamPermissions,
        KeyManagementServiceRestStub,
    ):
        def __hash__(self):
            return hash("KeyManagementServiceRestTransport.TestIamPermissions")

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

            http_options = _BaseKeyManagementServiceRestTransport._BaseTestIamPermissions._get_http_options()
            request, metadata = self._interceptor.pre_test_iam_permissions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyManagementServiceRestTransport._BaseTestIamPermissions,
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
                    f"Sending request for google.cloud.kms_v1.KeyManagementServiceClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "TestIamPermissions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                KeyManagementServiceRestTransport._TestIamPermissions._get_response(
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
                    "Received response for google.cloud.kms_v1.KeyManagementServiceAsyncClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "TestIamPermissions",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseKeyManagementServiceRestTransport._BaseGetOperation,
        KeyManagementServiceRestStub,
    ):
        def __hash__(self):
            return hash("KeyManagementServiceRestTransport.GetOperation")

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

            http_options = _BaseKeyManagementServiceRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseKeyManagementServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.kms_v1.KeyManagementServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = KeyManagementServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.kms_v1.KeyManagementServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.kms.v1.KeyManagementService",
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


__all__ = ("KeyManagementServiceRestTransport",)
