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
import asyncio
import json
import math
import os
from collections.abc import AsyncIterable, Iterable, Mapping, Sequence
from unittest import mock
from unittest.mock import AsyncMock

import grpc
import pytest
from google.api_core import api_core_version
from google.protobuf import json_format
from grpc.experimental import aio
from proto.marshal.rules import wrappers
from proto.marshal.rules.dates import DurationRule, TimestampRule
from requests import PreparedRequest, Request, Response
from requests.sessions import Session

try:
    from google.auth.aio import credentials as ga_credentials_async

    HAS_GOOGLE_AUTH_AIO = True
except ImportError:  # pragma: NO COVER
    HAS_GOOGLE_AUTH_AIO = False

import google.api_core.extended_operation as extended_operation  # type: ignore
import google.auth
from google.api_core import (
    client_options,
    future,
    gapic_v1,
    grpc_helpers,
    grpc_helpers_async,
    path_template,
)
from google.api_core import exceptions as core_exceptions
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials
from google.auth.exceptions import MutualTLSChannelError
from google.oauth2 import service_account

from google.cloud.compute_v1.services.instance_group_managers import (
    InstanceGroupManagersClient,
    pagers,
    transports,
)
from google.cloud.compute_v1.types import compute

try:
    from google.api_core import version_header

    HAS_GOOGLE_API_CORE_VERSION_HEADER = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    HAS_GOOGLE_API_CORE_VERSION_HEADER = False


CRED_INFO_JSON = {
    "credential_source": "/path/to/file",
    "credential_type": "service account credentials",
    "principal": "service-account@example.com",
}
CRED_INFO_STRING = json.dumps(CRED_INFO_JSON)


@pytest.fixture(autouse=True)
def disable_mtls_env():
    with mock.patch.dict(
        os.environ,
        {
            "GOOGLE_API_USE_CLIENT_CERTIFICATE": "false",
            "CLOUDSDK_CONTEXT_AWARE_USE_CLIENT_CERTIFICATE": "false",
        },
    ):
        yield


async def mock_async_gen(data, chunk_size=1):
    for i in range(0, len(data)):  # pragma: NO COVER
        chunk = data[i : i + chunk_size]
        yield chunk.encode("utf-8")


def client_cert_source_callback():
    return b"cert bytes", b"key bytes"


# TODO: use async auth anon credentials by default once the minimum version of google-auth is upgraded.
# See related issue: https://github.com/googleapis/gapic-generator-python/issues/2107.
def async_anonymous_credentials():
    if HAS_GOOGLE_AUTH_AIO:
        return ga_credentials_async.AnonymousCredentials()
    return ga_credentials.AnonymousCredentials()


# If default endpoint is localhost, then default mtls endpoint will be the same.
# This method modifies the default endpoint so the client can produce a different
# mtls endpoint for endpoint testing purposes.
def modify_default_endpoint(client):
    return (
        "foo.googleapis.com"
        if ("localhost" in client.DEFAULT_ENDPOINT)
        else client.DEFAULT_ENDPOINT
    )


# If default endpoint template is localhost, then default mtls endpoint will be the same.
# This method modifies the default endpoint template so the client can produce a different
# mtls endpoint for endpoint testing purposes.
def modify_default_endpoint_template(client):
    return (
        "test.{UNIVERSE_DOMAIN}"
        if ("localhost" in client._DEFAULT_ENDPOINT_TEMPLATE)
        else client._DEFAULT_ENDPOINT_TEMPLATE
    )


@pytest.fixture(autouse=True)
def set_event_loop():
    try:
        asyncio.get_running_loop()
        yield
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            yield
        finally:
            loop.close()
            asyncio.set_event_loop(None)


def test__get_client_cert_source():
    mock_provided_cert_source = mock.Mock()
    mock_default_cert_source = mock.Mock()

    assert InstanceGroupManagersClient._get_client_cert_source(None, False) is None
    assert (
        InstanceGroupManagersClient._get_client_cert_source(
            mock_provided_cert_source, False
        )
        is None
    )
    assert (
        InstanceGroupManagersClient._get_client_cert_source(
            mock_provided_cert_source, True
        )
        == mock_provided_cert_source
    )

    with mock.patch(
        "google.auth.transport.mtls.has_default_client_cert_source", return_value=True
    ):
        with mock.patch(
            "google.auth.transport.mtls.default_client_cert_source",
            return_value=mock_default_cert_source,
        ):
            assert (
                InstanceGroupManagersClient._get_client_cert_source(None, True)
                is mock_default_cert_source
            )
            assert (
                InstanceGroupManagersClient._get_client_cert_source(
                    mock_provided_cert_source, "true"
                )
                is mock_provided_cert_source
            )


@pytest.mark.parametrize(
    "transport_name",
    [
        ("rest"),
    ],
)
def test_abandon_instances_api_version_header(transport_name):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport_name
    )
    # TODO: Make this test unconditional once the minimum supported version of
    # google-api-core becomes 2.19.0 or higher.
    api_core_major, api_core_minor = [
        int(part) for part in api_core_version.__version__.split(".")[0:2]
    ]
    if api_core_major > 2 or (api_core_major == 2 and api_core_minor >= 19):
        # Mock the actual call within the gRPC stub, and fake the request.
        with mock.patch.object(
            type(client.transport.abandon_instances), "__call__"
        ) as call:
            call.return_value = compute.Operation()
            client.abandon_instances()

        # Establish that the api version header was sent.
        _, _, kw = call.mock_calls[0]
        assert (
            version_header.API_VERSION_METADATA_KEY,
            "2026-09-01",
        ) in kw["metadata"]
    else:
        pytest.skip(
            "google-api-core>=2.19.0 is required for `google.api_core.version_header`"
        )


@pytest.mark.parametrize(
    "transport_name",
    [
        ("rest"),
    ],
)
def test_aggregated_list_api_version_header(transport_name):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport_name
    )
    # TODO: Make this test unconditional once the minimum supported version of
    # google-api-core becomes 2.19.0 or higher.
    api_core_major, api_core_minor = [
        int(part) for part in api_core_version.__version__.split(".")[0:2]
    ]
    if api_core_major > 2 or (api_core_major == 2 and api_core_minor >= 19):
        # Mock the actual call within the gRPC stub, and fake the request.
        with mock.patch.object(
            type(client.transport.aggregated_list), "__call__"
        ) as call:
            call.return_value = compute.InstanceGroupManagerAggregatedList()
            client.aggregated_list()

        # Establish that the api version header was sent.
        _, _, kw = call.mock_calls[0]
        assert (
            version_header.API_VERSION_METADATA_KEY,
            "2026-09-01",
        ) in kw["metadata"]
    else:
        pytest.skip(
            "google-api-core>=2.19.0 is required for `google.api_core.version_header`"
        )


@pytest.mark.parametrize(
    "transport_name",
    [
        ("rest"),
    ],
)
def test_apply_updates_to_instances_api_version_header(transport_name):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport_name
    )
    # TODO: Make this test unconditional once the minimum supported version of
    # google-api-core becomes 2.19.0 or higher.
    api_core_major, api_core_minor = [
        int(part) for part in api_core_version.__version__.split(".")[0:2]
    ]
    if api_core_major > 2 or (api_core_major == 2 and api_core_minor >= 19):
        # Mock the actual call within the gRPC stub, and fake the request.
        with mock.patch.object(
            type(client.transport.apply_updates_to_instances), "__call__"
        ) as call:
            call.return_value = compute.Operation()
            client.apply_updates_to_instances()

        # Establish that the api version header was sent.
        _, _, kw = call.mock_calls[0]
        assert (
            version_header.API_VERSION_METADATA_KEY,
            "2026-09-01",
        ) in kw["metadata"]
    else:
        pytest.skip(
            "google-api-core>=2.19.0 is required for `google.api_core.version_header`"
        )


@pytest.mark.parametrize(
    "transport_name",
    [
        ("rest"),
    ],
)
def test_create_instances_api_version_header(transport_name):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport_name
    )
    # TODO: Make this test unconditional once the minimum supported version of
    # google-api-core becomes 2.19.0 or higher.
    api_core_major, api_core_minor = [
        int(part) for part in api_core_version.__version__.split(".")[0:2]
    ]
    if api_core_major > 2 or (api_core_major == 2 and api_core_minor >= 19):
        # Mock the actual call within the gRPC stub, and fake the request.
        with mock.patch.object(
            type(client.transport.create_instances), "__call__"
        ) as call:
            call.return_value = compute.Operation()
            client.create_instances()

        # Establish that the api version header was sent.
        _, _, kw = call.mock_calls[0]
        assert (
            version_header.API_VERSION_METADATA_KEY,
            "2026-09-01",
        ) in kw["metadata"]
    else:
        pytest.skip(
            "google-api-core>=2.19.0 is required for `google.api_core.version_header`"
        )


@pytest.mark.parametrize(
    "transport_name",
    [
        ("rest"),
    ],
)
def test_delete_api_version_header(transport_name):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport_name
    )
    # TODO: Make this test unconditional once the minimum supported version of
    # google-api-core becomes 2.19.0 or higher.
    api_core_major, api_core_minor = [
        int(part) for part in api_core_version.__version__.split(".")[0:2]
    ]
    if api_core_major > 2 or (api_core_major == 2 and api_core_minor >= 19):
        # Mock the actual call within the gRPC stub, and fake the request.
        with mock.patch.object(type(client.transport.delete), "__call__") as call:
            call.return_value = compute.Operation()
            client.delete()

        # Establish that the api version header was sent.
        _, _, kw = call.mock_calls[0]
        assert (
            version_header.API_VERSION_METADATA_KEY,
            "2026-09-01",
        ) in kw["metadata"]
    else:
        pytest.skip(
            "google-api-core>=2.19.0 is required for `google.api_core.version_header`"
        )


@pytest.mark.parametrize(
    "transport_name",
    [
        ("rest"),
    ],
)
def test_delete_instances_api_version_header(transport_name):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport_name
    )
    # TODO: Make this test unconditional once the minimum supported version of
    # google-api-core becomes 2.19.0 or higher.
    api_core_major, api_core_minor = [
        int(part) for part in api_core_version.__version__.split(".")[0:2]
    ]
    if api_core_major > 2 or (api_core_major == 2 and api_core_minor >= 19):
        # Mock the actual call within the gRPC stub, and fake the request.
        with mock.patch.object(
            type(client.transport.delete_instances), "__call__"
        ) as call:
            call.return_value = compute.Operation()
            client.delete_instances()

        # Establish that the api version header was sent.
        _, _, kw = call.mock_calls[0]
        assert (
            version_header.API_VERSION_METADATA_KEY,
            "2026-09-01",
        ) in kw["metadata"]
    else:
        pytest.skip(
            "google-api-core>=2.19.0 is required for `google.api_core.version_header`"
        )


@pytest.mark.parametrize(
    "transport_name",
    [
        ("rest"),
    ],
)
def test_delete_per_instance_configs_api_version_header(transport_name):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport_name
    )
    # TODO: Make this test unconditional once the minimum supported version of
    # google-api-core becomes 2.19.0 or higher.
    api_core_major, api_core_minor = [
        int(part) for part in api_core_version.__version__.split(".")[0:2]
    ]
    if api_core_major > 2 or (api_core_major == 2 and api_core_minor >= 19):
        # Mock the actual call within the gRPC stub, and fake the request.
        with mock.patch.object(
            type(client.transport.delete_per_instance_configs), "__call__"
        ) as call:
            call.return_value = compute.Operation()
            client.delete_per_instance_configs()

        # Establish that the api version header was sent.
        _, _, kw = call.mock_calls[0]
        assert (
            version_header.API_VERSION_METADATA_KEY,
            "2026-09-01",
        ) in kw["metadata"]
    else:
        pytest.skip(
            "google-api-core>=2.19.0 is required for `google.api_core.version_header`"
        )


@pytest.mark.parametrize(
    "transport_name",
    [
        ("rest"),
    ],
)
def test_get_api_version_header(transport_name):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport_name
    )
    # TODO: Make this test unconditional once the minimum supported version of
    # google-api-core becomes 2.19.0 or higher.
    api_core_major, api_core_minor = [
        int(part) for part in api_core_version.__version__.split(".")[0:2]
    ]
    if api_core_major > 2 or (api_core_major == 2 and api_core_minor >= 19):
        # Mock the actual call within the gRPC stub, and fake the request.
        with mock.patch.object(type(client.transport.get), "__call__") as call:
            call.return_value = compute.InstanceGroupManager()
            client.get()

        # Establish that the api version header was sent.
        _, _, kw = call.mock_calls[0]
        assert (
            version_header.API_VERSION_METADATA_KEY,
            "2026-09-01",
        ) in kw["metadata"]
    else:
        pytest.skip(
            "google-api-core>=2.19.0 is required for `google.api_core.version_header`"
        )


@pytest.mark.parametrize(
    "transport_name",
    [
        ("rest"),
    ],
)
def test_insert_api_version_header(transport_name):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport_name
    )
    # TODO: Make this test unconditional once the minimum supported version of
    # google-api-core becomes 2.19.0 or higher.
    api_core_major, api_core_minor = [
        int(part) for part in api_core_version.__version__.split(".")[0:2]
    ]
    if api_core_major > 2 or (api_core_major == 2 and api_core_minor >= 19):
        # Mock the actual call within the gRPC stub, and fake the request.
        with mock.patch.object(type(client.transport.insert), "__call__") as call:
            call.return_value = compute.Operation()
            client.insert()

        # Establish that the api version header was sent.
        _, _, kw = call.mock_calls[0]
        assert (
            version_header.API_VERSION_METADATA_KEY,
            "2026-09-01",
        ) in kw["metadata"]
    else:
        pytest.skip(
            "google-api-core>=2.19.0 is required for `google.api_core.version_header`"
        )


@pytest.mark.parametrize(
    "transport_name",
    [
        ("rest"),
    ],
)
def test_list_api_version_header(transport_name):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport_name
    )
    # TODO: Make this test unconditional once the minimum supported version of
    # google-api-core becomes 2.19.0 or higher.
    api_core_major, api_core_minor = [
        int(part) for part in api_core_version.__version__.split(".")[0:2]
    ]
    if api_core_major > 2 or (api_core_major == 2 and api_core_minor >= 19):
        # Mock the actual call within the gRPC stub, and fake the request.
        with mock.patch.object(type(client.transport.list), "__call__") as call:
            call.return_value = compute.InstanceGroupManagerList()
            client.list()

        # Establish that the api version header was sent.
        _, _, kw = call.mock_calls[0]
        assert (
            version_header.API_VERSION_METADATA_KEY,
            "2026-09-01",
        ) in kw["metadata"]
    else:
        pytest.skip(
            "google-api-core>=2.19.0 is required for `google.api_core.version_header`"
        )


@pytest.mark.parametrize(
    "transport_name",
    [
        ("rest"),
    ],
)
def test_list_errors_api_version_header(transport_name):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport_name
    )
    # TODO: Make this test unconditional once the minimum supported version of
    # google-api-core becomes 2.19.0 or higher.
    api_core_major, api_core_minor = [
        int(part) for part in api_core_version.__version__.split(".")[0:2]
    ]
    if api_core_major > 2 or (api_core_major == 2 and api_core_minor >= 19):
        # Mock the actual call within the gRPC stub, and fake the request.
        with mock.patch.object(type(client.transport.list_errors), "__call__") as call:
            call.return_value = compute.InstanceGroupManagersListErrorsResponse()
            client.list_errors()

        # Establish that the api version header was sent.
        _, _, kw = call.mock_calls[0]
        assert (
            version_header.API_VERSION_METADATA_KEY,
            "2026-09-01",
        ) in kw["metadata"]
    else:
        pytest.skip(
            "google-api-core>=2.19.0 is required for `google.api_core.version_header`"
        )


@pytest.mark.parametrize(
    "transport_name",
    [
        ("rest"),
    ],
)
def test_list_managed_instances_api_version_header(transport_name):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport_name
    )
    # TODO: Make this test unconditional once the minimum supported version of
    # google-api-core becomes 2.19.0 or higher.
    api_core_major, api_core_minor = [
        int(part) for part in api_core_version.__version__.split(".")[0:2]
    ]
    if api_core_major > 2 or (api_core_major == 2 and api_core_minor >= 19):
        # Mock the actual call within the gRPC stub, and fake the request.
        with mock.patch.object(
            type(client.transport.list_managed_instances), "__call__"
        ) as call:
            call.return_value = (
                compute.InstanceGroupManagersListManagedInstancesResponse()
            )
            client.list_managed_instances()

        # Establish that the api version header was sent.
        _, _, kw = call.mock_calls[0]
        assert (
            version_header.API_VERSION_METADATA_KEY,
            "2026-09-01",
        ) in kw["metadata"]
    else:
        pytest.skip(
            "google-api-core>=2.19.0 is required for `google.api_core.version_header`"
        )


@pytest.mark.parametrize(
    "transport_name",
    [
        ("rest"),
    ],
)
def test_list_per_instance_configs_api_version_header(transport_name):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport_name
    )
    # TODO: Make this test unconditional once the minimum supported version of
    # google-api-core becomes 2.19.0 or higher.
    api_core_major, api_core_minor = [
        int(part) for part in api_core_version.__version__.split(".")[0:2]
    ]
    if api_core_major > 2 or (api_core_major == 2 and api_core_minor >= 19):
        # Mock the actual call within the gRPC stub, and fake the request.
        with mock.patch.object(
            type(client.transport.list_per_instance_configs), "__call__"
        ) as call:
            call.return_value = (
                compute.InstanceGroupManagersListPerInstanceConfigsResp()
            )
            client.list_per_instance_configs()

        # Establish that the api version header was sent.
        _, _, kw = call.mock_calls[0]
        assert (
            version_header.API_VERSION_METADATA_KEY,
            "2026-09-01",
        ) in kw["metadata"]
    else:
        pytest.skip(
            "google-api-core>=2.19.0 is required for `google.api_core.version_header`"
        )


@pytest.mark.parametrize(
    "transport_name",
    [
        ("rest"),
    ],
)
def test_patch_api_version_header(transport_name):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport_name
    )
    # TODO: Make this test unconditional once the minimum supported version of
    # google-api-core becomes 2.19.0 or higher.
    api_core_major, api_core_minor = [
        int(part) for part in api_core_version.__version__.split(".")[0:2]
    ]
    if api_core_major > 2 or (api_core_major == 2 and api_core_minor >= 19):
        # Mock the actual call within the gRPC stub, and fake the request.
        with mock.patch.object(type(client.transport.patch), "__call__") as call:
            call.return_value = compute.Operation()
            client.patch()

        # Establish that the api version header was sent.
        _, _, kw = call.mock_calls[0]
        assert (
            version_header.API_VERSION_METADATA_KEY,
            "2026-09-01",
        ) in kw["metadata"]
    else:
        pytest.skip(
            "google-api-core>=2.19.0 is required for `google.api_core.version_header`"
        )


@pytest.mark.parametrize(
    "transport_name",
    [
        ("rest"),
    ],
)
def test_patch_per_instance_configs_api_version_header(transport_name):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport_name
    )
    # TODO: Make this test unconditional once the minimum supported version of
    # google-api-core becomes 2.19.0 or higher.
    api_core_major, api_core_minor = [
        int(part) for part in api_core_version.__version__.split(".")[0:2]
    ]
    if api_core_major > 2 or (api_core_major == 2 and api_core_minor >= 19):
        # Mock the actual call within the gRPC stub, and fake the request.
        with mock.patch.object(
            type(client.transport.patch_per_instance_configs), "__call__"
        ) as call:
            call.return_value = compute.Operation()
            client.patch_per_instance_configs()

        # Establish that the api version header was sent.
        _, _, kw = call.mock_calls[0]
        assert (
            version_header.API_VERSION_METADATA_KEY,
            "2026-09-01",
        ) in kw["metadata"]
    else:
        pytest.skip(
            "google-api-core>=2.19.0 is required for `google.api_core.version_header`"
        )


@pytest.mark.parametrize(
    "transport_name",
    [
        ("rest"),
    ],
)
def test_recreate_instances_api_version_header(transport_name):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport_name
    )
    # TODO: Make this test unconditional once the minimum supported version of
    # google-api-core becomes 2.19.0 or higher.
    api_core_major, api_core_minor = [
        int(part) for part in api_core_version.__version__.split(".")[0:2]
    ]
    if api_core_major > 2 or (api_core_major == 2 and api_core_minor >= 19):
        # Mock the actual call within the gRPC stub, and fake the request.
        with mock.patch.object(
            type(client.transport.recreate_instances), "__call__"
        ) as call:
            call.return_value = compute.Operation()
            client.recreate_instances()

        # Establish that the api version header was sent.
        _, _, kw = call.mock_calls[0]
        assert (
            version_header.API_VERSION_METADATA_KEY,
            "2026-09-01",
        ) in kw["metadata"]
    else:
        pytest.skip(
            "google-api-core>=2.19.0 is required for `google.api_core.version_header`"
        )


@pytest.mark.parametrize(
    "transport_name",
    [
        ("rest"),
    ],
)
def test_resize_api_version_header(transport_name):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport_name
    )
    # TODO: Make this test unconditional once the minimum supported version of
    # google-api-core becomes 2.19.0 or higher.
    api_core_major, api_core_minor = [
        int(part) for part in api_core_version.__version__.split(".")[0:2]
    ]
    if api_core_major > 2 or (api_core_major == 2 and api_core_minor >= 19):
        # Mock the actual call within the gRPC stub, and fake the request.
        with mock.patch.object(type(client.transport.resize), "__call__") as call:
            call.return_value = compute.Operation()
            client.resize()

        # Establish that the api version header was sent.
        _, _, kw = call.mock_calls[0]
        assert (
            version_header.API_VERSION_METADATA_KEY,
            "2026-09-01",
        ) in kw["metadata"]
    else:
        pytest.skip(
            "google-api-core>=2.19.0 is required for `google.api_core.version_header`"
        )


@pytest.mark.parametrize(
    "transport_name",
    [
        ("rest"),
    ],
)
def test_resume_instances_api_version_header(transport_name):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport_name
    )
    # TODO: Make this test unconditional once the minimum supported version of
    # google-api-core becomes 2.19.0 or higher.
    api_core_major, api_core_minor = [
        int(part) for part in api_core_version.__version__.split(".")[0:2]
    ]
    if api_core_major > 2 or (api_core_major == 2 and api_core_minor >= 19):
        # Mock the actual call within the gRPC stub, and fake the request.
        with mock.patch.object(
            type(client.transport.resume_instances), "__call__"
        ) as call:
            call.return_value = compute.Operation()
            client.resume_instances()

        # Establish that the api version header was sent.
        _, _, kw = call.mock_calls[0]
        assert (
            version_header.API_VERSION_METADATA_KEY,
            "2026-09-01",
        ) in kw["metadata"]
    else:
        pytest.skip(
            "google-api-core>=2.19.0 is required for `google.api_core.version_header`"
        )


@pytest.mark.parametrize(
    "transport_name",
    [
        ("rest"),
    ],
)
def test_set_instance_template_api_version_header(transport_name):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport_name
    )
    # TODO: Make this test unconditional once the minimum supported version of
    # google-api-core becomes 2.19.0 or higher.
    api_core_major, api_core_minor = [
        int(part) for part in api_core_version.__version__.split(".")[0:2]
    ]
    if api_core_major > 2 or (api_core_major == 2 and api_core_minor >= 19):
        # Mock the actual call within the gRPC stub, and fake the request.
        with mock.patch.object(
            type(client.transport.set_instance_template), "__call__"
        ) as call:
            call.return_value = compute.Operation()
            client.set_instance_template()

        # Establish that the api version header was sent.
        _, _, kw = call.mock_calls[0]
        assert (
            version_header.API_VERSION_METADATA_KEY,
            "2026-09-01",
        ) in kw["metadata"]
    else:
        pytest.skip(
            "google-api-core>=2.19.0 is required for `google.api_core.version_header`"
        )


@pytest.mark.parametrize(
    "transport_name",
    [
        ("rest"),
    ],
)
def test_set_target_pools_api_version_header(transport_name):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport_name
    )
    # TODO: Make this test unconditional once the minimum supported version of
    # google-api-core becomes 2.19.0 or higher.
    api_core_major, api_core_minor = [
        int(part) for part in api_core_version.__version__.split(".")[0:2]
    ]
    if api_core_major > 2 or (api_core_major == 2 and api_core_minor >= 19):
        # Mock the actual call within the gRPC stub, and fake the request.
        with mock.patch.object(
            type(client.transport.set_target_pools), "__call__"
        ) as call:
            call.return_value = compute.Operation()
            client.set_target_pools()

        # Establish that the api version header was sent.
        _, _, kw = call.mock_calls[0]
        assert (
            version_header.API_VERSION_METADATA_KEY,
            "2026-09-01",
        ) in kw["metadata"]
    else:
        pytest.skip(
            "google-api-core>=2.19.0 is required for `google.api_core.version_header`"
        )


@pytest.mark.parametrize(
    "transport_name",
    [
        ("rest"),
    ],
)
def test_start_instances_api_version_header(transport_name):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport_name
    )
    # TODO: Make this test unconditional once the minimum supported version of
    # google-api-core becomes 2.19.0 or higher.
    api_core_major, api_core_minor = [
        int(part) for part in api_core_version.__version__.split(".")[0:2]
    ]
    if api_core_major > 2 or (api_core_major == 2 and api_core_minor >= 19):
        # Mock the actual call within the gRPC stub, and fake the request.
        with mock.patch.object(
            type(client.transport.start_instances), "__call__"
        ) as call:
            call.return_value = compute.Operation()
            client.start_instances()

        # Establish that the api version header was sent.
        _, _, kw = call.mock_calls[0]
        assert (
            version_header.API_VERSION_METADATA_KEY,
            "2026-09-01",
        ) in kw["metadata"]
    else:
        pytest.skip(
            "google-api-core>=2.19.0 is required for `google.api_core.version_header`"
        )


@pytest.mark.parametrize(
    "transport_name",
    [
        ("rest"),
    ],
)
def test_stop_instances_api_version_header(transport_name):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport_name
    )
    # TODO: Make this test unconditional once the minimum supported version of
    # google-api-core becomes 2.19.0 or higher.
    api_core_major, api_core_minor = [
        int(part) for part in api_core_version.__version__.split(".")[0:2]
    ]
    if api_core_major > 2 or (api_core_major == 2 and api_core_minor >= 19):
        # Mock the actual call within the gRPC stub, and fake the request.
        with mock.patch.object(
            type(client.transport.stop_instances), "__call__"
        ) as call:
            call.return_value = compute.Operation()
            client.stop_instances()

        # Establish that the api version header was sent.
        _, _, kw = call.mock_calls[0]
        assert (
            version_header.API_VERSION_METADATA_KEY,
            "2026-09-01",
        ) in kw["metadata"]
    else:
        pytest.skip(
            "google-api-core>=2.19.0 is required for `google.api_core.version_header`"
        )


@pytest.mark.parametrize(
    "transport_name",
    [
        ("rest"),
    ],
)
def test_suspend_instances_api_version_header(transport_name):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport_name
    )
    # TODO: Make this test unconditional once the minimum supported version of
    # google-api-core becomes 2.19.0 or higher.
    api_core_major, api_core_minor = [
        int(part) for part in api_core_version.__version__.split(".")[0:2]
    ]
    if api_core_major > 2 or (api_core_major == 2 and api_core_minor >= 19):
        # Mock the actual call within the gRPC stub, and fake the request.
        with mock.patch.object(
            type(client.transport.suspend_instances), "__call__"
        ) as call:
            call.return_value = compute.Operation()
            client.suspend_instances()

        # Establish that the api version header was sent.
        _, _, kw = call.mock_calls[0]
        assert (
            version_header.API_VERSION_METADATA_KEY,
            "2026-09-01",
        ) in kw["metadata"]
    else:
        pytest.skip(
            "google-api-core>=2.19.0 is required for `google.api_core.version_header`"
        )


@pytest.mark.parametrize(
    "transport_name",
    [
        ("rest"),
    ],
)
def test_update_per_instance_configs_api_version_header(transport_name):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport=transport_name
    )
    # TODO: Make this test unconditional once the minimum supported version of
    # google-api-core becomes 2.19.0 or higher.
    api_core_major, api_core_minor = [
        int(part) for part in api_core_version.__version__.split(".")[0:2]
    ]
    if api_core_major > 2 or (api_core_major == 2 and api_core_minor >= 19):
        # Mock the actual call within the gRPC stub, and fake the request.
        with mock.patch.object(
            type(client.transport.update_per_instance_configs), "__call__"
        ) as call:
            call.return_value = compute.Operation()
            client.update_per_instance_configs()

        # Establish that the api version header was sent.
        _, _, kw = call.mock_calls[0]
        assert (
            version_header.API_VERSION_METADATA_KEY,
            "2026-09-01",
        ) in kw["metadata"]
    else:
        pytest.skip(
            "google-api-core>=2.19.0 is required for `google.api_core.version_header`"
        )


@pytest.mark.parametrize(
    "error_code,cred_info_json,show_cred_info",
    [
        (401, CRED_INFO_JSON, True),
        (403, CRED_INFO_JSON, True),
        (404, CRED_INFO_JSON, True),
        (500, CRED_INFO_JSON, False),
        (401, None, False),
        (403, None, False),
        (404, None, False),
        (500, None, False),
    ],
)
def test__add_cred_info_for_auth_errors(error_code, cred_info_json, show_cred_info):
    cred = mock.Mock(["get_cred_info"])
    cred.get_cred_info = mock.Mock(return_value=cred_info_json)
    client = InstanceGroupManagersClient(credentials=cred)
    client._transport._credentials = cred

    error = core_exceptions.GoogleAPICallError("message", details=["foo"])
    error.code = error_code

    client._add_cred_info_for_auth_errors(error)
    if show_cred_info:
        assert error.details == ["foo", CRED_INFO_STRING]
    else:
        assert error.details == ["foo"]


@pytest.mark.parametrize("error_code", [401, 403, 404, 500])
def test__add_cred_info_for_auth_errors_no_get_cred_info(error_code):
    cred = mock.Mock([])
    assert not hasattr(cred, "get_cred_info")
    client = InstanceGroupManagersClient(credentials=cred)
    client._transport._credentials = cred

    error = core_exceptions.GoogleAPICallError("message", details=[])
    error.code = error_code

    client._add_cred_info_for_auth_errors(error)
    assert error.details == []


@pytest.mark.parametrize(
    "client_class,transport_name",
    [
        (InstanceGroupManagersClient, "rest"),
    ],
)
def test_instance_group_managers_client_from_service_account_info(
    client_class, transport_name
):
    creds = ga_credentials.AnonymousCredentials()
    with mock.patch.object(
        service_account.Credentials, "from_service_account_info"
    ) as factory:
        factory.return_value = creds
        info = {"valid": True}
        client = client_class.from_service_account_info(info, transport=transport_name)
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        assert client.transport._host == (
            "compute.googleapis.com:443"
            if transport_name in ["grpc", "grpc_asyncio"]
            else "https://compute.googleapis.com"
        )


@pytest.mark.parametrize(
    "transport_class,transport_name",
    [
        (transports.InstanceGroupManagersRestTransport, "rest"),
    ],
)
def test_instance_group_managers_client_service_account_always_use_jwt(
    transport_class, transport_name
):
    with mock.patch.object(
        service_account.Credentials, "with_always_use_jwt_access", create=True
    ) as use_jwt:
        creds = service_account.Credentials(None, None, None)
        transport = transport_class(credentials=creds, always_use_jwt_access=True)
        use_jwt.assert_called_once_with(True)

    with mock.patch.object(
        service_account.Credentials, "with_always_use_jwt_access", create=True
    ) as use_jwt:
        creds = service_account.Credentials(None, None, None)
        transport = transport_class(credentials=creds, always_use_jwt_access=False)
        use_jwt.assert_not_called()


@pytest.mark.parametrize(
    "client_class,transport_name",
    [
        (InstanceGroupManagersClient, "rest"),
    ],
)
def test_instance_group_managers_client_from_service_account_file(
    client_class, transport_name
):
    creds = ga_credentials.AnonymousCredentials()
    with mock.patch.object(
        service_account.Credentials, "from_service_account_file"
    ) as factory:
        factory.return_value = creds
        client = client_class.from_service_account_file(
            "dummy/file/path.json", transport=transport_name
        )
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        client = client_class.from_service_account_json(
            "dummy/file/path.json", transport=transport_name
        )
        assert client.transport._credentials == creds
        assert isinstance(client, client_class)

        assert client.transport._host == (
            "compute.googleapis.com:443"
            if transport_name in ["grpc", "grpc_asyncio"]
            else "https://compute.googleapis.com"
        )


def test_instance_group_managers_client_get_transport_class():
    transport = InstanceGroupManagersClient.get_transport_class()
    available_transports = [
        transports.InstanceGroupManagersRestTransport,
    ]
    assert transport in available_transports

    transport = InstanceGroupManagersClient.get_transport_class("rest")
    assert transport == transports.InstanceGroupManagersRestTransport


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (
            InstanceGroupManagersClient,
            transports.InstanceGroupManagersRestTransport,
            "rest",
        ),
    ],
)
@mock.patch.object(
    InstanceGroupManagersClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(InstanceGroupManagersClient),
)
def test_instance_group_managers_client_client_options(
    client_class, transport_class, transport_name
):
    # Check that if channel is provided we won't create a new one.
    with mock.patch.object(InstanceGroupManagersClient, "get_transport_class") as gtc:
        transport = transport_class(credentials=ga_credentials.AnonymousCredentials())
        client = client_class(transport=transport)
        gtc.assert_not_called()

    # Check that if channel is provided via str we will create a new one.
    with mock.patch.object(InstanceGroupManagersClient, "get_transport_class") as gtc:
        client = client_class(transport=transport_name)
        gtc.assert_called()

    # Check the case api_endpoint is provided.
    options = client_options.ClientOptions(api_endpoint="squid.clam.whelk")
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(transport=transport_name, client_options=options)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host="squid.clam.whelk",
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience=None,
        )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT is
    # "never".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "never"}):
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class(transport=transport_name)
            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=client._DEFAULT_ENDPOINT_TEMPLATE.format(
                    UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE
                ),
                scopes=None,
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
                api_audience=None,
            )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT is
    # "always".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "always"}):
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class(transport=transport_name)
            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=client.DEFAULT_MTLS_ENDPOINT,
                scopes=None,
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
                api_audience=None,
            )

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT has
    # unsupported value.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "Unsupported"}):
        with pytest.raises(MutualTLSChannelError) as excinfo:
            client = client_class(transport=transport_name)
    assert (
        str(excinfo.value)
        == "Environment variable `GOOGLE_API_USE_MTLS_ENDPOINT` must be `never`, `auto` or `always`"
    )

    # Check the case quota_project_id is provided
    options = client_options.ClientOptions(quota_project_id="octopus")
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client._DEFAULT_ENDPOINT_TEMPLATE.format(
                UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE
            ),
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id="octopus",
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience=None,
        )
    # Check the case api_endpoint is provided
    options = client_options.ClientOptions(
        api_audience="https://language.googleapis.com"
    )
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client._DEFAULT_ENDPOINT_TEMPLATE.format(
                UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE
            ),
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience="https://language.googleapis.com",
        )


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name,use_client_cert_env",
    [
        (
            InstanceGroupManagersClient,
            transports.InstanceGroupManagersRestTransport,
            "rest",
            "true",
        ),
        (
            InstanceGroupManagersClient,
            transports.InstanceGroupManagersRestTransport,
            "rest",
            "false",
        ),
    ],
)
@mock.patch.object(
    InstanceGroupManagersClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(InstanceGroupManagersClient),
)
@mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "auto"})
def test_instance_group_managers_client_mtls_env_auto(
    client_class, transport_class, transport_name, use_client_cert_env
):
    # This tests the endpoint autoswitch behavior. Endpoint is autoswitched to the default
    # mtls endpoint, if GOOGLE_API_USE_CLIENT_CERTIFICATE is "true" and client cert exists.

    # Check the case client_cert_source is provided. Whether client cert is used depends on
    # GOOGLE_API_USE_CLIENT_CERTIFICATE value.
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}
    ):
        options = client_options.ClientOptions(
            client_cert_source=client_cert_source_callback
        )
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class(client_options=options, transport=transport_name)

            if use_client_cert_env == "false":
                expected_client_cert_source = None
                expected_host = client._DEFAULT_ENDPOINT_TEMPLATE.format(
                    UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE
                )
            else:
                expected_client_cert_source = client_cert_source_callback
                expected_host = client.DEFAULT_MTLS_ENDPOINT

            patched.assert_called_once_with(
                credentials=None,
                credentials_file=None,
                host=expected_host,
                scopes=None,
                client_cert_source_for_mtls=expected_client_cert_source,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
                api_audience=None,
            )

    # Check the case ADC client cert is provided. Whether client cert is used depends on
    # GOOGLE_API_USE_CLIENT_CERTIFICATE value.
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}
    ):
        with mock.patch.object(transport_class, "__init__") as patched:
            with mock.patch(
                "google.auth.transport.mtls.has_default_client_cert_source",
                return_value=True,
            ):
                with mock.patch(
                    "google.auth.transport.mtls.default_client_cert_source",
                    return_value=client_cert_source_callback,
                ):
                    if use_client_cert_env == "false":
                        expected_host = client._DEFAULT_ENDPOINT_TEMPLATE.format(
                            UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE
                        )
                        expected_client_cert_source = None
                    else:
                        expected_host = client.DEFAULT_MTLS_ENDPOINT
                        expected_client_cert_source = client_cert_source_callback

                    patched.return_value = None
                    client = client_class(transport=transport_name)
                    patched.assert_called_once_with(
                        credentials=None,
                        credentials_file=None,
                        host=expected_host,
                        scopes=None,
                        client_cert_source_for_mtls=expected_client_cert_source,
                        quota_project_id=None,
                        client_info=transports.base.DEFAULT_CLIENT_INFO,
                        always_use_jwt_access=True,
                        api_audience=None,
                    )

    # Check the case client_cert_source and ADC client cert are not provided.
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": use_client_cert_env}
    ):
        with mock.patch.object(transport_class, "__init__") as patched:
            with mock.patch(
                "google.auth.transport.mtls.has_default_client_cert_source",
                return_value=False,
            ):
                patched.return_value = None
                client = client_class(transport=transport_name)
                patched.assert_called_once_with(
                    credentials=None,
                    credentials_file=None,
                    host=client._DEFAULT_ENDPOINT_TEMPLATE.format(
                        UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE
                    ),
                    scopes=None,
                    client_cert_source_for_mtls=None,
                    quota_project_id=None,
                    client_info=transports.base.DEFAULT_CLIENT_INFO,
                    always_use_jwt_access=True,
                    api_audience=None,
                )


@pytest.mark.parametrize("client_class", [InstanceGroupManagersClient])
@mock.patch.object(
    InstanceGroupManagersClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(InstanceGroupManagersClient),
)
def test_instance_group_managers_client_get_mtls_endpoint_and_cert_source(client_class):
    mock_client_cert_source = mock.Mock()

    # Test the case GOOGLE_API_USE_CLIENT_CERTIFICATE is "true".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}):
        mock_api_endpoint = "foo"
        options = client_options.ClientOptions(
            client_cert_source=mock_client_cert_source, api_endpoint=mock_api_endpoint
        )
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source(
            options
        )
        assert api_endpoint == mock_api_endpoint
        assert cert_source == mock_client_cert_source

    # Test the case GOOGLE_API_USE_CLIENT_CERTIFICATE is "false".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "false"}):
        mock_client_cert_source = mock.Mock()
        mock_api_endpoint = "foo"
        options = client_options.ClientOptions(
            client_cert_source=mock_client_cert_source, api_endpoint=mock_api_endpoint
        )
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source(
            options
        )
        assert api_endpoint == mock_api_endpoint
        assert cert_source is None

    # Test the case GOOGLE_API_USE_CLIENT_CERTIFICATE is "Unsupported".
    with mock.patch.dict(
        os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "Unsupported"}
    ):
        if hasattr(google.auth.transport.mtls, "should_use_client_cert"):
            mock_client_cert_source = mock.Mock()
            mock_api_endpoint = "foo"
            options = client_options.ClientOptions(
                client_cert_source=mock_client_cert_source,
                api_endpoint=mock_api_endpoint,
            )
            api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source(
                options
            )
            assert api_endpoint == mock_api_endpoint
            assert cert_source is None

    # Test cases for mTLS enablement when GOOGLE_API_USE_CLIENT_CERTIFICATE is unset.
    test_cases = [
        (
            # With workloads present in config, mTLS is enabled.
            {
                "version": 1,
                "cert_configs": {
                    "workload": {
                        "cert_path": "path/to/cert/file",
                        "key_path": "path/to/key/file",
                    }
                },
            },
            mock_client_cert_source,
        ),
        (
            # With workloads not present in config, mTLS is disabled.
            {
                "version": 1,
                "cert_configs": {},
            },
            None,
        ),
    ]
    if hasattr(google.auth.transport.mtls, "should_use_client_cert"):
        for config_data, expected_cert_source in test_cases:
            env = os.environ.copy()
            env.pop("GOOGLE_API_USE_CLIENT_CERTIFICATE", None)
            env.pop("CLOUDSDK_CONTEXT_AWARE_USE_CLIENT_CERTIFICATE", None)
            with mock.patch.dict(os.environ, env, clear=True):
                config_filename = "mock_certificate_config.json"
                config_file_content = json.dumps(config_data)
                m = mock.mock_open(read_data=config_file_content)
                with (
                    mock.patch("builtins.open", m),
                    mock.patch(
                        "os.path.exists",
                        side_effect=lambda path: os.path.basename(path)
                        == config_filename,
                    ),
                ):
                    with mock.patch.dict(
                        os.environ, {"GOOGLE_API_CERTIFICATE_CONFIG": config_filename}
                    ):
                        mock_api_endpoint = "foo"
                        options = client_options.ClientOptions(
                            client_cert_source=mock_client_cert_source,
                            api_endpoint=mock_api_endpoint,
                        )
                        api_endpoint, cert_source = (
                            client_class.get_mtls_endpoint_and_cert_source(options)
                        )
                        assert api_endpoint == mock_api_endpoint
                        assert cert_source is expected_cert_source

    # Test cases for mTLS enablement when GOOGLE_API_USE_CLIENT_CERTIFICATE is unset(empty).
    test_cases = [
        (
            # With workloads present in config, mTLS is enabled.
            {
                "version": 1,
                "cert_configs": {
                    "workload": {
                        "cert_path": "path/to/cert/file",
                        "key_path": "path/to/key/file",
                    }
                },
            },
            mock_client_cert_source,
        ),
        (
            # With workloads not present in config, mTLS is disabled.
            {
                "version": 1,
                "cert_configs": {},
            },
            None,
        ),
    ]
    if hasattr(google.auth.transport.mtls, "should_use_client_cert"):
        for config_data, expected_cert_source in test_cases:
            env = os.environ.copy()
            env.pop("GOOGLE_API_USE_CLIENT_CERTIFICATE", "")
            env.pop("CLOUDSDK_CONTEXT_AWARE_USE_CLIENT_CERTIFICATE", "")
            with mock.patch.dict(os.environ, env, clear=True):
                config_filename = "mock_certificate_config.json"
                config_file_content = json.dumps(config_data)
                m = mock.mock_open(read_data=config_file_content)
                with (
                    mock.patch("builtins.open", m),
                    mock.patch(
                        "os.path.exists",
                        side_effect=lambda path: os.path.basename(path)
                        == config_filename,
                    ),
                ):
                    with mock.patch.dict(
                        os.environ, {"GOOGLE_API_CERTIFICATE_CONFIG": config_filename}
                    ):
                        mock_api_endpoint = "foo"
                        options = client_options.ClientOptions(
                            client_cert_source=mock_client_cert_source,
                            api_endpoint=mock_api_endpoint,
                        )
                        api_endpoint, cert_source = (
                            client_class.get_mtls_endpoint_and_cert_source(options)
                        )
                        assert api_endpoint == mock_api_endpoint
                        assert cert_source is expected_cert_source

    # Test the case GOOGLE_API_USE_MTLS_ENDPOINT is "never".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "never"}):
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source()
        assert api_endpoint == client_class.DEFAULT_ENDPOINT
        assert cert_source is None

    # Test the case GOOGLE_API_USE_MTLS_ENDPOINT is "always".
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "always"}):
        api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source()
        assert api_endpoint == client_class.DEFAULT_MTLS_ENDPOINT
        assert cert_source is None

    # Test the case GOOGLE_API_USE_MTLS_ENDPOINT is "auto" and default cert doesn't exist.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}):
        with mock.patch(
            "google.auth.transport.mtls.has_default_client_cert_source",
            return_value=False,
        ):
            api_endpoint, cert_source = client_class.get_mtls_endpoint_and_cert_source()
            assert api_endpoint == client_class.DEFAULT_ENDPOINT
            assert cert_source is None

    # Test the case GOOGLE_API_USE_MTLS_ENDPOINT is "auto" and default cert exists.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}):
        with mock.patch(
            "google.auth.transport.mtls.has_default_client_cert_source",
            return_value=True,
        ):
            with mock.patch(
                "google.auth.transport.mtls.default_client_cert_source",
                return_value=mock_client_cert_source,
            ):
                api_endpoint, cert_source = (
                    client_class.get_mtls_endpoint_and_cert_source()
                )
                assert api_endpoint == client_class.DEFAULT_MTLS_ENDPOINT
                assert cert_source == mock_client_cert_source

    # Check the case api_endpoint is not provided and GOOGLE_API_USE_MTLS_ENDPOINT has
    # unsupported value.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "Unsupported"}):
        with pytest.raises(MutualTLSChannelError) as excinfo:
            client_class.get_mtls_endpoint_and_cert_source()

        assert (
            str(excinfo.value)
            == "Environment variable `GOOGLE_API_USE_MTLS_ENDPOINT` must be `never`, `auto` or `always`"
        )


@pytest.mark.parametrize("client_class", [InstanceGroupManagersClient])
@mock.patch.object(
    InstanceGroupManagersClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(InstanceGroupManagersClient),
)
def test_instance_group_managers_client_client_api_endpoint(client_class):
    mock_client_cert_source = client_cert_source_callback
    api_override = "foo.com"
    default_universe = InstanceGroupManagersClient._DEFAULT_UNIVERSE
    default_endpoint = InstanceGroupManagersClient._DEFAULT_ENDPOINT_TEMPLATE.format(
        UNIVERSE_DOMAIN=default_universe
    )
    mock_universe = "bar.com"
    mock_endpoint = InstanceGroupManagersClient._DEFAULT_ENDPOINT_TEMPLATE.format(
        UNIVERSE_DOMAIN=mock_universe
    )

    # If ClientOptions.api_endpoint is set and GOOGLE_API_USE_CLIENT_CERTIFICATE="true",
    # use ClientOptions.api_endpoint as the api endpoint regardless.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_CLIENT_CERTIFICATE": "true"}):
        with mock.patch(
            "google.auth.transport.requests.AuthorizedSession.configure_mtls_channel"
        ):
            options = client_options.ClientOptions(
                client_cert_source=mock_client_cert_source, api_endpoint=api_override
            )
            client = client_class(
                client_options=options,
                credentials=ga_credentials.AnonymousCredentials(),
            )
            assert client.api_endpoint == api_override

    # If ClientOptions.api_endpoint is not set and GOOGLE_API_USE_MTLS_ENDPOINT="never",
    # use the _DEFAULT_ENDPOINT_TEMPLATE populated with GDU as the api endpoint.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "never"}):
        client = client_class(credentials=ga_credentials.AnonymousCredentials())
        assert client.api_endpoint == default_endpoint

    # If ClientOptions.api_endpoint is not set and GOOGLE_API_USE_MTLS_ENDPOINT="always",
    # use the DEFAULT_MTLS_ENDPOINT as the api endpoint.
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "always"}):
        client = client_class(credentials=ga_credentials.AnonymousCredentials())
        assert client.api_endpoint == client_class.DEFAULT_MTLS_ENDPOINT

    # If ClientOptions.api_endpoint is not set, GOOGLE_API_USE_MTLS_ENDPOINT="auto" (default),
    # GOOGLE_API_USE_CLIENT_CERTIFICATE="false" (default), default cert source doesn't exist,
    # and ClientOptions.universe_domain="bar.com",
    # use the _DEFAULT_ENDPOINT_TEMPLATE populated with universe domain as the api endpoint.
    options = client_options.ClientOptions()
    universe_exists = hasattr(options, "universe_domain")
    if universe_exists:
        options = client_options.ClientOptions(universe_domain=mock_universe)
        client = client_class(
            client_options=options, credentials=ga_credentials.AnonymousCredentials()
        )
    else:
        client = client_class(
            client_options=options, credentials=ga_credentials.AnonymousCredentials()
        )
    assert client.api_endpoint == (
        mock_endpoint if universe_exists else default_endpoint
    )
    assert client.universe_domain == (
        mock_universe if universe_exists else default_universe
    )

    # If ClientOptions does not have a universe domain attribute and GOOGLE_API_USE_MTLS_ENDPOINT="never",
    # use the _DEFAULT_ENDPOINT_TEMPLATE populated with GDU as the api endpoint.
    options = client_options.ClientOptions()
    if hasattr(options, "universe_domain"):
        delattr(options, "universe_domain")
    with mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "never"}):
        client = client_class(
            client_options=options, credentials=ga_credentials.AnonymousCredentials()
        )
        assert client.api_endpoint == default_endpoint


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (
            InstanceGroupManagersClient,
            transports.InstanceGroupManagersRestTransport,
            "rest",
        ),
    ],
)
def test_instance_group_managers_client_client_options_scopes(
    client_class, transport_class, transport_name
):
    # Check the case scopes are provided.
    options = client_options.ClientOptions(
        scopes=["1", "2"],
    )
    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file=None,
            host=client._DEFAULT_ENDPOINT_TEMPLATE.format(
                UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE
            ),
            scopes=["1", "2"],
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience=None,
        )


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name,grpc_helpers",
    [
        (
            InstanceGroupManagersClient,
            transports.InstanceGroupManagersRestTransport,
            "rest",
            None,
        ),
    ],
)
def test_instance_group_managers_client_client_options_credentials_file(
    client_class, transport_class, transport_name, grpc_helpers
):
    # Check the case credentials file is provided.
    options = client_options.ClientOptions(credentials_file="credentials.json")

    with mock.patch.object(transport_class, "__init__") as patched:
        patched.return_value = None
        client = client_class(client_options=options, transport=transport_name)
        patched.assert_called_once_with(
            credentials=None,
            credentials_file="credentials.json",
            host=client._DEFAULT_ENDPOINT_TEMPLATE.format(
                UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE
            ),
            scopes=None,
            client_cert_source_for_mtls=None,
            quota_project_id=None,
            client_info=transports.base.DEFAULT_CLIENT_INFO,
            always_use_jwt_access=True,
            api_audience=None,
        )


def test_abandon_instances_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.abandon_instances in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.abandon_instances] = (
            mock_rpc
        )

        request = {}
        client.abandon_instances(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.abandon_instances(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_abandon_instances_rest_required_fields(
    request_type=compute.AbandonInstancesInstanceGroupManagerRequest,
):
    transport_class = transports.InstanceGroupManagersRestTransport

    request_init = {}
    request_init["instance_group_manager"] = ""
    request_init["project"] = ""
    request_init["zone"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseAbandonInstances,
        "_BaseAbandonInstances__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["instanceGroupManager"] = "instance_group_manager_value"
    jsonified_request["project"] = "project_value"
    jsonified_request["zone"] = "zone_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("requestId",))

    # verify required fields with non-default values are left alone
    assert "instanceGroupManager" in jsonified_request
    assert jsonified_request["instanceGroupManager"] == "instance_group_manager_value"
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "zone" in jsonified_request
    assert jsonified_request["zone"] == "zone_value"

    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.Operation()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = compute.Operation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.abandon_instances(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_abandon_instances_rest_flattened():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "zone": "sample2",
            "instance_group_manager": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_abandon_instances_request_resource=compute.InstanceGroupManagersAbandonInstancesRequest(
                instances=["instances_value"]
            ),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.abandon_instances(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}/abandonInstances"
            % client.transport._host,
            args[1],
        )


def test_abandon_instances_rest_flattened_error(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.abandon_instances(
            compute.AbandonInstancesInstanceGroupManagerRequest(),
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_abandon_instances_request_resource=compute.InstanceGroupManagersAbandonInstancesRequest(
                instances=["instances_value"]
            ),
        )


def test_abandon_instances_unary_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.abandon_instances in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.abandon_instances] = (
            mock_rpc
        )

        request = {}
        client.abandon_instances_unary(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.abandon_instances_unary(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_abandon_instances_unary_rest_required_fields(
    request_type=compute.AbandonInstancesInstanceGroupManagerRequest,
):
    transport_class = transports.InstanceGroupManagersRestTransport

    request_init = {}
    request_init["instance_group_manager"] = ""
    request_init["project"] = ""
    request_init["zone"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseAbandonInstances,
        "_BaseAbandonInstances__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["instanceGroupManager"] = "instance_group_manager_value"
    jsonified_request["project"] = "project_value"
    jsonified_request["zone"] = "zone_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("requestId",))

    # verify required fields with non-default values are left alone
    assert "instanceGroupManager" in jsonified_request
    assert jsonified_request["instanceGroupManager"] == "instance_group_manager_value"
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "zone" in jsonified_request
    assert jsonified_request["zone"] == "zone_value"

    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.Operation()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = compute.Operation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.abandon_instances_unary(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_abandon_instances_unary_rest_flattened():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "zone": "sample2",
            "instance_group_manager": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_abandon_instances_request_resource=compute.InstanceGroupManagersAbandonInstancesRequest(
                instances=["instances_value"]
            ),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.abandon_instances_unary(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}/abandonInstances"
            % client.transport._host,
            args[1],
        )


def test_abandon_instances_unary_rest_flattened_error(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.abandon_instances_unary(
            compute.AbandonInstancesInstanceGroupManagerRequest(),
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_abandon_instances_request_resource=compute.InstanceGroupManagersAbandonInstancesRequest(
                instances=["instances_value"]
            ),
        )


def test_aggregated_list_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.aggregated_list in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.aggregated_list] = mock_rpc

        request = {}
        client.aggregated_list(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.aggregated_list(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_aggregated_list_rest_required_fields(
    request_type=compute.AggregatedListInstanceGroupManagersRequest,
):
    transport_class = transports.InstanceGroupManagersRestTransport

    request_init = {}
    request_init["project"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseAggregatedList,
        "_BaseAggregatedList__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["project"] = "project_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "filter",
            "includeAllScopes",
            "maxResults",
            "orderBy",
            "pageToken",
            "serviceProjectNumber",
        )
    )

    # verify required fields with non-default values are left alone
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"

    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.InstanceGroupManagerAggregatedList()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "get",
                "query_params": pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = compute.InstanceGroupManagerAggregatedList.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.aggregated_list(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_aggregated_list_rest_flattened():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.InstanceGroupManagerAggregatedList()

        # get arguments that satisfy an http rule for this method
        sample_request = {"project": "sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = compute.InstanceGroupManagerAggregatedList.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.aggregated_list(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/aggregated/instanceGroupManagers"
            % client.transport._host,
            args[1],
        )


def test_aggregated_list_rest_flattened_error(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.aggregated_list(
            compute.AggregatedListInstanceGroupManagersRequest(),
            project="project_value",
        )


def test_aggregated_list_rest_pager(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            compute.InstanceGroupManagerAggregatedList(
                items={
                    "a": compute.InstanceGroupManagersScopedList(),
                    "b": compute.InstanceGroupManagersScopedList(),
                    "c": compute.InstanceGroupManagersScopedList(),
                },
                next_page_token="abc",
            ),
            compute.InstanceGroupManagerAggregatedList(
                items={},
                next_page_token="def",
            ),
            compute.InstanceGroupManagerAggregatedList(
                items={
                    "g": compute.InstanceGroupManagersScopedList(),
                },
                next_page_token="ghi",
            ),
            compute.InstanceGroupManagerAggregatedList(
                items={
                    "h": compute.InstanceGroupManagersScopedList(),
                    "i": compute.InstanceGroupManagersScopedList(),
                },
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            compute.InstanceGroupManagerAggregatedList.to_json(x) for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {"project": "sample1"}

        pager = client.aggregated_list(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        assert isinstance(pager.get("a"), compute.InstanceGroupManagersScopedList)
        assert pager.get("h") is None

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, tuple) for i in results)
        for result in results:
            assert isinstance(result, tuple)
            assert tuple(type(t) for t in result) == (
                str,
                compute.InstanceGroupManagersScopedList,
            )

        assert pager.get("a") is None
        assert isinstance(pager.get("h"), compute.InstanceGroupManagersScopedList)

        pages = list(client.aggregated_list(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_apply_updates_to_instances_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.apply_updates_to_instances
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.apply_updates_to_instances
        ] = mock_rpc

        request = {}
        client.apply_updates_to_instances(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.apply_updates_to_instances(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_apply_updates_to_instances_rest_required_fields(
    request_type=compute.ApplyUpdatesToInstancesInstanceGroupManagerRequest,
):
    transport_class = transports.InstanceGroupManagersRestTransport

    request_init = {}
    request_init["instance_group_manager"] = ""
    request_init["project"] = ""
    request_init["zone"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseApplyUpdatesToInstances,
        "_BaseApplyUpdatesToInstances__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["instanceGroupManager"] = "instance_group_manager_value"
    jsonified_request["project"] = "project_value"
    jsonified_request["zone"] = "zone_value"

    # verify required fields with non-default values are left alone
    assert "instanceGroupManager" in jsonified_request
    assert jsonified_request["instanceGroupManager"] == "instance_group_manager_value"
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "zone" in jsonified_request
    assert jsonified_request["zone"] == "zone_value"

    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.Operation()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = compute.Operation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.apply_updates_to_instances(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_apply_updates_to_instances_rest_flattened():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "zone": "sample2",
            "instance_group_manager": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_apply_updates_request_resource=compute.InstanceGroupManagersApplyUpdatesRequest(
                all_instances=True
            ),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.apply_updates_to_instances(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}/applyUpdatesToInstances"
            % client.transport._host,
            args[1],
        )


def test_apply_updates_to_instances_rest_flattened_error(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.apply_updates_to_instances(
            compute.ApplyUpdatesToInstancesInstanceGroupManagerRequest(),
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_apply_updates_request_resource=compute.InstanceGroupManagersApplyUpdatesRequest(
                all_instances=True
            ),
        )


def test_apply_updates_to_instances_unary_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.apply_updates_to_instances
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.apply_updates_to_instances
        ] = mock_rpc

        request = {}
        client.apply_updates_to_instances_unary(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.apply_updates_to_instances_unary(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_apply_updates_to_instances_unary_rest_required_fields(
    request_type=compute.ApplyUpdatesToInstancesInstanceGroupManagerRequest,
):
    transport_class = transports.InstanceGroupManagersRestTransport

    request_init = {}
    request_init["instance_group_manager"] = ""
    request_init["project"] = ""
    request_init["zone"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseApplyUpdatesToInstances,
        "_BaseApplyUpdatesToInstances__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["instanceGroupManager"] = "instance_group_manager_value"
    jsonified_request["project"] = "project_value"
    jsonified_request["zone"] = "zone_value"

    # verify required fields with non-default values are left alone
    assert "instanceGroupManager" in jsonified_request
    assert jsonified_request["instanceGroupManager"] == "instance_group_manager_value"
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "zone" in jsonified_request
    assert jsonified_request["zone"] == "zone_value"

    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.Operation()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = compute.Operation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.apply_updates_to_instances_unary(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_apply_updates_to_instances_unary_rest_flattened():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "zone": "sample2",
            "instance_group_manager": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_apply_updates_request_resource=compute.InstanceGroupManagersApplyUpdatesRequest(
                all_instances=True
            ),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.apply_updates_to_instances_unary(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}/applyUpdatesToInstances"
            % client.transport._host,
            args[1],
        )


def test_apply_updates_to_instances_unary_rest_flattened_error(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.apply_updates_to_instances_unary(
            compute.ApplyUpdatesToInstancesInstanceGroupManagerRequest(),
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_apply_updates_request_resource=compute.InstanceGroupManagersApplyUpdatesRequest(
                all_instances=True
            ),
        )


def test_create_instances_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.create_instances in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.create_instances] = (
            mock_rpc
        )

        request = {}
        client.create_instances(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.create_instances(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_create_instances_rest_required_fields(
    request_type=compute.CreateInstancesInstanceGroupManagerRequest,
):
    transport_class = transports.InstanceGroupManagersRestTransport

    request_init = {}
    request_init["instance_group_manager"] = ""
    request_init["project"] = ""
    request_init["zone"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseCreateInstances,
        "_BaseCreateInstances__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["instanceGroupManager"] = "instance_group_manager_value"
    jsonified_request["project"] = "project_value"
    jsonified_request["zone"] = "zone_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("requestId",))

    # verify required fields with non-default values are left alone
    assert "instanceGroupManager" in jsonified_request
    assert jsonified_request["instanceGroupManager"] == "instance_group_manager_value"
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "zone" in jsonified_request
    assert jsonified_request["zone"] == "zone_value"

    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.Operation()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = compute.Operation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.create_instances(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_create_instances_rest_flattened():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "zone": "sample2",
            "instance_group_manager": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_create_instances_request_resource=compute.InstanceGroupManagersCreateInstancesRequest(
                instances=[compute.PerInstanceConfig(fingerprint="fingerprint_value")]
            ),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.create_instances(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}/createInstances"
            % client.transport._host,
            args[1],
        )


def test_create_instances_rest_flattened_error(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_instances(
            compute.CreateInstancesInstanceGroupManagerRequest(),
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_create_instances_request_resource=compute.InstanceGroupManagersCreateInstancesRequest(
                instances=[compute.PerInstanceConfig(fingerprint="fingerprint_value")]
            ),
        )


def test_create_instances_unary_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.create_instances in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.create_instances] = (
            mock_rpc
        )

        request = {}
        client.create_instances_unary(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.create_instances_unary(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_create_instances_unary_rest_required_fields(
    request_type=compute.CreateInstancesInstanceGroupManagerRequest,
):
    transport_class = transports.InstanceGroupManagersRestTransport

    request_init = {}
    request_init["instance_group_manager"] = ""
    request_init["project"] = ""
    request_init["zone"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseCreateInstances,
        "_BaseCreateInstances__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["instanceGroupManager"] = "instance_group_manager_value"
    jsonified_request["project"] = "project_value"
    jsonified_request["zone"] = "zone_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("requestId",))

    # verify required fields with non-default values are left alone
    assert "instanceGroupManager" in jsonified_request
    assert jsonified_request["instanceGroupManager"] == "instance_group_manager_value"
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "zone" in jsonified_request
    assert jsonified_request["zone"] == "zone_value"

    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.Operation()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = compute.Operation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.create_instances_unary(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_create_instances_unary_rest_flattened():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "zone": "sample2",
            "instance_group_manager": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_create_instances_request_resource=compute.InstanceGroupManagersCreateInstancesRequest(
                instances=[compute.PerInstanceConfig(fingerprint="fingerprint_value")]
            ),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.create_instances_unary(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}/createInstances"
            % client.transport._host,
            args[1],
        )


def test_create_instances_unary_rest_flattened_error(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_instances_unary(
            compute.CreateInstancesInstanceGroupManagerRequest(),
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_create_instances_request_resource=compute.InstanceGroupManagersCreateInstancesRequest(
                instances=[compute.PerInstanceConfig(fingerprint="fingerprint_value")]
            ),
        )


def test_delete_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.delete in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.delete] = mock_rpc

        request = {}
        client.delete(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.delete(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_delete_rest_required_fields(
    request_type=compute.DeleteInstanceGroupManagerRequest,
):
    transport_class = transports.InstanceGroupManagersRestTransport

    request_init = {}
    request_init["instance_group_manager"] = ""
    request_init["project"] = ""
    request_init["zone"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseDelete,
        "_BaseDelete__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["instanceGroupManager"] = "instance_group_manager_value"
    jsonified_request["project"] = "project_value"
    jsonified_request["zone"] = "zone_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "noGracefulShutdown",
            "requestId",
        )
    )

    # verify required fields with non-default values are left alone
    assert "instanceGroupManager" in jsonified_request
    assert jsonified_request["instanceGroupManager"] == "instance_group_manager_value"
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "zone" in jsonified_request
    assert jsonified_request["zone"] == "zone_value"

    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.Operation()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "delete",
                "query_params": pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = compute.Operation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.delete(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_delete_rest_flattened():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "zone": "sample2",
            "instance_group_manager": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.delete(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}"
            % client.transport._host,
            args[1],
        )


def test_delete_rest_flattened_error(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete(
            compute.DeleteInstanceGroupManagerRequest(),
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
        )


def test_delete_unary_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.delete in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.delete] = mock_rpc

        request = {}
        client.delete_unary(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.delete_unary(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_delete_unary_rest_required_fields(
    request_type=compute.DeleteInstanceGroupManagerRequest,
):
    transport_class = transports.InstanceGroupManagersRestTransport

    request_init = {}
    request_init["instance_group_manager"] = ""
    request_init["project"] = ""
    request_init["zone"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseDelete,
        "_BaseDelete__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["instanceGroupManager"] = "instance_group_manager_value"
    jsonified_request["project"] = "project_value"
    jsonified_request["zone"] = "zone_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "noGracefulShutdown",
            "requestId",
        )
    )

    # verify required fields with non-default values are left alone
    assert "instanceGroupManager" in jsonified_request
    assert jsonified_request["instanceGroupManager"] == "instance_group_manager_value"
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "zone" in jsonified_request
    assert jsonified_request["zone"] == "zone_value"

    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.Operation()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "delete",
                "query_params": pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = compute.Operation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.delete_unary(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_delete_unary_rest_flattened():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "zone": "sample2",
            "instance_group_manager": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.delete_unary(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}"
            % client.transport._host,
            args[1],
        )


def test_delete_unary_rest_flattened_error(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_unary(
            compute.DeleteInstanceGroupManagerRequest(),
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
        )


def test_delete_instances_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.delete_instances in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.delete_instances] = (
            mock_rpc
        )

        request = {}
        client.delete_instances(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.delete_instances(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_delete_instances_rest_required_fields(
    request_type=compute.DeleteInstancesInstanceGroupManagerRequest,
):
    transport_class = transports.InstanceGroupManagersRestTransport

    request_init = {}
    request_init["instance_group_manager"] = ""
    request_init["project"] = ""
    request_init["zone"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseDeleteInstances,
        "_BaseDeleteInstances__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["instanceGroupManager"] = "instance_group_manager_value"
    jsonified_request["project"] = "project_value"
    jsonified_request["zone"] = "zone_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "noGracefulShutdown",
            "requestId",
        )
    )

    # verify required fields with non-default values are left alone
    assert "instanceGroupManager" in jsonified_request
    assert jsonified_request["instanceGroupManager"] == "instance_group_manager_value"
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "zone" in jsonified_request
    assert jsonified_request["zone"] == "zone_value"

    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.Operation()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = compute.Operation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.delete_instances(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_delete_instances_rest_flattened():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "zone": "sample2",
            "instance_group_manager": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_delete_instances_request_resource=compute.InstanceGroupManagersDeleteInstancesRequest(
                instances=["instances_value"]
            ),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.delete_instances(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}/deleteInstances"
            % client.transport._host,
            args[1],
        )


def test_delete_instances_rest_flattened_error(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_instances(
            compute.DeleteInstancesInstanceGroupManagerRequest(),
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_delete_instances_request_resource=compute.InstanceGroupManagersDeleteInstancesRequest(
                instances=["instances_value"]
            ),
        )


def test_delete_instances_unary_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.delete_instances in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.delete_instances] = (
            mock_rpc
        )

        request = {}
        client.delete_instances_unary(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.delete_instances_unary(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_delete_instances_unary_rest_required_fields(
    request_type=compute.DeleteInstancesInstanceGroupManagerRequest,
):
    transport_class = transports.InstanceGroupManagersRestTransport

    request_init = {}
    request_init["instance_group_manager"] = ""
    request_init["project"] = ""
    request_init["zone"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseDeleteInstances,
        "_BaseDeleteInstances__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["instanceGroupManager"] = "instance_group_manager_value"
    jsonified_request["project"] = "project_value"
    jsonified_request["zone"] = "zone_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "noGracefulShutdown",
            "requestId",
        )
    )

    # verify required fields with non-default values are left alone
    assert "instanceGroupManager" in jsonified_request
    assert jsonified_request["instanceGroupManager"] == "instance_group_manager_value"
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "zone" in jsonified_request
    assert jsonified_request["zone"] == "zone_value"

    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.Operation()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = compute.Operation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.delete_instances_unary(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_delete_instances_unary_rest_flattened():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "zone": "sample2",
            "instance_group_manager": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_delete_instances_request_resource=compute.InstanceGroupManagersDeleteInstancesRequest(
                instances=["instances_value"]
            ),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.delete_instances_unary(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}/deleteInstances"
            % client.transport._host,
            args[1],
        )


def test_delete_instances_unary_rest_flattened_error(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_instances_unary(
            compute.DeleteInstancesInstanceGroupManagerRequest(),
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_delete_instances_request_resource=compute.InstanceGroupManagersDeleteInstancesRequest(
                instances=["instances_value"]
            ),
        )


def test_delete_per_instance_configs_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.delete_per_instance_configs
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.delete_per_instance_configs
        ] = mock_rpc

        request = {}
        client.delete_per_instance_configs(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.delete_per_instance_configs(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_delete_per_instance_configs_rest_required_fields(
    request_type=compute.DeletePerInstanceConfigsInstanceGroupManagerRequest,
):
    transport_class = transports.InstanceGroupManagersRestTransport

    request_init = {}
    request_init["instance_group_manager"] = ""
    request_init["project"] = ""
    request_init["zone"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseDeletePerInstanceConfigs,
        "_BaseDeletePerInstanceConfigs__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["instanceGroupManager"] = "instance_group_manager_value"
    jsonified_request["project"] = "project_value"
    jsonified_request["zone"] = "zone_value"

    # verify required fields with non-default values are left alone
    assert "instanceGroupManager" in jsonified_request
    assert jsonified_request["instanceGroupManager"] == "instance_group_manager_value"
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "zone" in jsonified_request
    assert jsonified_request["zone"] == "zone_value"

    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.Operation()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = compute.Operation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.delete_per_instance_configs(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_delete_per_instance_configs_rest_flattened():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "zone": "sample2",
            "instance_group_manager": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_delete_per_instance_configs_req_resource=compute.InstanceGroupManagersDeletePerInstanceConfigsReq(
                names=["names_value"]
            ),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.delete_per_instance_configs(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}/deletePerInstanceConfigs"
            % client.transport._host,
            args[1],
        )


def test_delete_per_instance_configs_rest_flattened_error(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_per_instance_configs(
            compute.DeletePerInstanceConfigsInstanceGroupManagerRequest(),
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_delete_per_instance_configs_req_resource=compute.InstanceGroupManagersDeletePerInstanceConfigsReq(
                names=["names_value"]
            ),
        )


def test_delete_per_instance_configs_unary_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.delete_per_instance_configs
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.delete_per_instance_configs
        ] = mock_rpc

        request = {}
        client.delete_per_instance_configs_unary(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.delete_per_instance_configs_unary(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_delete_per_instance_configs_unary_rest_required_fields(
    request_type=compute.DeletePerInstanceConfigsInstanceGroupManagerRequest,
):
    transport_class = transports.InstanceGroupManagersRestTransport

    request_init = {}
    request_init["instance_group_manager"] = ""
    request_init["project"] = ""
    request_init["zone"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseDeletePerInstanceConfigs,
        "_BaseDeletePerInstanceConfigs__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["instanceGroupManager"] = "instance_group_manager_value"
    jsonified_request["project"] = "project_value"
    jsonified_request["zone"] = "zone_value"

    # verify required fields with non-default values are left alone
    assert "instanceGroupManager" in jsonified_request
    assert jsonified_request["instanceGroupManager"] == "instance_group_manager_value"
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "zone" in jsonified_request
    assert jsonified_request["zone"] == "zone_value"

    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.Operation()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = compute.Operation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.delete_per_instance_configs_unary(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_delete_per_instance_configs_unary_rest_flattened():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "zone": "sample2",
            "instance_group_manager": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_delete_per_instance_configs_req_resource=compute.InstanceGroupManagersDeletePerInstanceConfigsReq(
                names=["names_value"]
            ),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.delete_per_instance_configs_unary(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}/deletePerInstanceConfigs"
            % client.transport._host,
            args[1],
        )


def test_delete_per_instance_configs_unary_rest_flattened_error(
    transport: str = "rest",
):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.delete_per_instance_configs_unary(
            compute.DeletePerInstanceConfigsInstanceGroupManagerRequest(),
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_delete_per_instance_configs_req_resource=compute.InstanceGroupManagersDeletePerInstanceConfigsReq(
                names=["names_value"]
            ),
        )


def test_get_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get] = mock_rpc

        request = {}
        client.get(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_rest_required_fields(request_type=compute.GetInstanceGroupManagerRequest):
    transport_class = transports.InstanceGroupManagersRestTransport

    request_init = {}
    request_init["instance_group_manager"] = ""
    request_init["project"] = ""
    request_init["zone"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGet,
        "_BaseGet__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["instanceGroupManager"] = "instance_group_manager_value"
    jsonified_request["project"] = "project_value"
    jsonified_request["zone"] = "zone_value"

    # verify required fields with non-default values are left alone
    assert "instanceGroupManager" in jsonified_request
    assert jsonified_request["instanceGroupManager"] == "instance_group_manager_value"
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "zone" in jsonified_request
    assert jsonified_request["zone"] == "zone_value"

    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.InstanceGroupManager()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "get",
                "query_params": pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = compute.InstanceGroupManager.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_rest_flattened():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.InstanceGroupManager()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "zone": "sample2",
            "instance_group_manager": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = compute.InstanceGroupManager.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}"
            % client.transport._host,
            args[1],
        )


def test_get_rest_flattened_error(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get(
            compute.GetInstanceGroupManagerRequest(),
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
        )


def test_insert_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.insert in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.insert] = mock_rpc

        request = {}
        client.insert(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.insert(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_insert_rest_required_fields(
    request_type=compute.InsertInstanceGroupManagerRequest,
):
    transport_class = transports.InstanceGroupManagersRestTransport

    request_init = {}
    request_init["project"] = ""
    request_init["zone"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseInsert,
        "_BaseInsert__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["project"] = "project_value"
    jsonified_request["zone"] = "zone_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("requestId",))

    # verify required fields with non-default values are left alone
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "zone" in jsonified_request
    assert jsonified_request["zone"] == "zone_value"

    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.Operation()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = compute.Operation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.insert(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_insert_rest_flattened():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {"project": "sample1", "zone": "sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            zone="zone_value",
            instance_group_manager_resource=compute.InstanceGroupManager(
                all_instances_config=compute.InstanceGroupManagerAllInstancesConfig(
                    properties=compute.InstancePropertiesPatch(
                        expose_host_topology=True
                    )
                )
            ),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.insert(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers"
            % client.transport._host,
            args[1],
        )


def test_insert_rest_flattened_error(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.insert(
            compute.InsertInstanceGroupManagerRequest(),
            project="project_value",
            zone="zone_value",
            instance_group_manager_resource=compute.InstanceGroupManager(
                all_instances_config=compute.InstanceGroupManagerAllInstancesConfig(
                    properties=compute.InstancePropertiesPatch(
                        expose_host_topology=True
                    )
                )
            ),
        )


def test_insert_unary_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.insert in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.insert] = mock_rpc

        request = {}
        client.insert_unary(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.insert_unary(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_insert_unary_rest_required_fields(
    request_type=compute.InsertInstanceGroupManagerRequest,
):
    transport_class = transports.InstanceGroupManagersRestTransport

    request_init = {}
    request_init["project"] = ""
    request_init["zone"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseInsert,
        "_BaseInsert__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["project"] = "project_value"
    jsonified_request["zone"] = "zone_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("requestId",))

    # verify required fields with non-default values are left alone
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "zone" in jsonified_request
    assert jsonified_request["zone"] == "zone_value"

    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.Operation()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = compute.Operation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.insert_unary(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_insert_unary_rest_flattened():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {"project": "sample1", "zone": "sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            zone="zone_value",
            instance_group_manager_resource=compute.InstanceGroupManager(
                all_instances_config=compute.InstanceGroupManagerAllInstancesConfig(
                    properties=compute.InstancePropertiesPatch(
                        expose_host_topology=True
                    )
                )
            ),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.insert_unary(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers"
            % client.transport._host,
            args[1],
        )


def test_insert_unary_rest_flattened_error(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.insert_unary(
            compute.InsertInstanceGroupManagerRequest(),
            project="project_value",
            zone="zone_value",
            instance_group_manager_resource=compute.InstanceGroupManager(
                all_instances_config=compute.InstanceGroupManagerAllInstancesConfig(
                    properties=compute.InstancePropertiesPatch(
                        expose_host_topology=True
                    )
                )
            ),
        )


def test_list_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list] = mock_rpc

        request = {}
        client.list(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_rest_required_fields(
    request_type=compute.ListInstanceGroupManagersRequest,
):
    transport_class = transports.InstanceGroupManagersRestTransport

    request_init = {}
    request_init["project"] = ""
    request_init["zone"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseList,
        "_BaseList__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["project"] = "project_value"
    jsonified_request["zone"] = "zone_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "filter",
            "maxResults",
            "orderBy",
            "pageToken",
        )
    )

    # verify required fields with non-default values are left alone
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "zone" in jsonified_request
    assert jsonified_request["zone"] == "zone_value"

    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.InstanceGroupManagerList()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "get",
                "query_params": pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = compute.InstanceGroupManagerList.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_rest_flattened():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.InstanceGroupManagerList()

        # get arguments that satisfy an http rule for this method
        sample_request = {"project": "sample1", "zone": "sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            zone="zone_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = compute.InstanceGroupManagerList.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers"
            % client.transport._host,
            args[1],
        )


def test_list_rest_flattened_error(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list(
            compute.ListInstanceGroupManagersRequest(),
            project="project_value",
            zone="zone_value",
        )


def test_list_rest_pager(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            compute.InstanceGroupManagerList(
                items=[
                    compute.InstanceGroupManager(),
                    compute.InstanceGroupManager(),
                    compute.InstanceGroupManager(),
                ],
                next_page_token="abc",
            ),
            compute.InstanceGroupManagerList(
                items=[],
                next_page_token="def",
            ),
            compute.InstanceGroupManagerList(
                items=[
                    compute.InstanceGroupManager(),
                ],
                next_page_token="ghi",
            ),
            compute.InstanceGroupManagerList(
                items=[
                    compute.InstanceGroupManager(),
                    compute.InstanceGroupManager(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(compute.InstanceGroupManagerList.to_json(x) for x in response)
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {"project": "sample1", "zone": "sample2"}

        pager = client.list(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, compute.InstanceGroupManager) for i in results)

        pages = list(client.list(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_list_errors_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_errors in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_errors] = mock_rpc

        request = {}
        client.list_errors(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_errors(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_errors_rest_required_fields(
    request_type=compute.ListErrorsInstanceGroupManagersRequest,
):
    transport_class = transports.InstanceGroupManagersRestTransport

    request_init = {}
    request_init["instance_group_manager"] = ""
    request_init["project"] = ""
    request_init["zone"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseListErrors,
        "_BaseListErrors__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["instanceGroupManager"] = "instance_group_manager_value"
    jsonified_request["project"] = "project_value"
    jsonified_request["zone"] = "zone_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "filter",
            "maxResults",
            "orderBy",
            "pageToken",
        )
    )

    # verify required fields with non-default values are left alone
    assert "instanceGroupManager" in jsonified_request
    assert jsonified_request["instanceGroupManager"] == "instance_group_manager_value"
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "zone" in jsonified_request
    assert jsonified_request["zone"] == "zone_value"

    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.InstanceGroupManagersListErrorsResponse()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "get",
                "query_params": pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = compute.InstanceGroupManagersListErrorsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_errors(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_errors_rest_flattened():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.InstanceGroupManagersListErrorsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "zone": "sample2",
            "instance_group_manager": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = compute.InstanceGroupManagersListErrorsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_errors(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}/listErrors"
            % client.transport._host,
            args[1],
        )


def test_list_errors_rest_flattened_error(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_errors(
            compute.ListErrorsInstanceGroupManagersRequest(),
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
        )


def test_list_errors_rest_pager(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            compute.InstanceGroupManagersListErrorsResponse(
                items=[
                    compute.InstanceManagedByIgmError(),
                    compute.InstanceManagedByIgmError(),
                    compute.InstanceManagedByIgmError(),
                ],
                next_page_token="abc",
            ),
            compute.InstanceGroupManagersListErrorsResponse(
                items=[],
                next_page_token="def",
            ),
            compute.InstanceGroupManagersListErrorsResponse(
                items=[
                    compute.InstanceManagedByIgmError(),
                ],
                next_page_token="ghi",
            ),
            compute.InstanceGroupManagersListErrorsResponse(
                items=[
                    compute.InstanceManagedByIgmError(),
                    compute.InstanceManagedByIgmError(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            compute.InstanceGroupManagersListErrorsResponse.to_json(x) for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {
            "project": "sample1",
            "zone": "sample2",
            "instance_group_manager": "sample3",
        }

        pager = client.list_errors(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, compute.InstanceManagedByIgmError) for i in results)

        pages = list(client.list_errors(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_list_managed_instances_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_managed_instances
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_managed_instances] = (
            mock_rpc
        )

        request = {}
        client.list_managed_instances(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_managed_instances(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_managed_instances_rest_required_fields(
    request_type=compute.ListManagedInstancesInstanceGroupManagersRequest,
):
    transport_class = transports.InstanceGroupManagersRestTransport

    request_init = {}
    request_init["instance_group_manager"] = ""
    request_init["project"] = ""
    request_init["zone"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseListManagedInstances,
        "_BaseListManagedInstances__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["instanceGroupManager"] = "instance_group_manager_value"
    jsonified_request["project"] = "project_value"
    jsonified_request["zone"] = "zone_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "filter",
            "maxResults",
            "orderBy",
            "pageToken",
        )
    )

    # verify required fields with non-default values are left alone
    assert "instanceGroupManager" in jsonified_request
    assert jsonified_request["instanceGroupManager"] == "instance_group_manager_value"
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "zone" in jsonified_request
    assert jsonified_request["zone"] == "zone_value"

    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.InstanceGroupManagersListManagedInstancesResponse()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = compute.InstanceGroupManagersListManagedInstancesResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_managed_instances(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_managed_instances_rest_flattened():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.InstanceGroupManagersListManagedInstancesResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "zone": "sample2",
            "instance_group_manager": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = compute.InstanceGroupManagersListManagedInstancesResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_managed_instances(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}/listManagedInstances"
            % client.transport._host,
            args[1],
        )


def test_list_managed_instances_rest_flattened_error(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_managed_instances(
            compute.ListManagedInstancesInstanceGroupManagersRequest(),
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
        )


def test_list_managed_instances_rest_pager(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            compute.InstanceGroupManagersListManagedInstancesResponse(
                managed_instances=[
                    compute.ManagedInstance(),
                    compute.ManagedInstance(),
                    compute.ManagedInstance(),
                ],
                next_page_token="abc",
            ),
            compute.InstanceGroupManagersListManagedInstancesResponse(
                managed_instances=[],
                next_page_token="def",
            ),
            compute.InstanceGroupManagersListManagedInstancesResponse(
                managed_instances=[
                    compute.ManagedInstance(),
                ],
                next_page_token="ghi",
            ),
            compute.InstanceGroupManagersListManagedInstancesResponse(
                managed_instances=[
                    compute.ManagedInstance(),
                    compute.ManagedInstance(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            compute.InstanceGroupManagersListManagedInstancesResponse.to_json(x)
            for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {
            "project": "sample1",
            "zone": "sample2",
            "instance_group_manager": "sample3",
        }

        pager = client.list_managed_instances(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, compute.ManagedInstance) for i in results)

        pages = list(client.list_managed_instances(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_list_per_instance_configs_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_per_instance_configs
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.list_per_instance_configs
        ] = mock_rpc

        request = {}
        client.list_per_instance_configs(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_per_instance_configs(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_per_instance_configs_rest_required_fields(
    request_type=compute.ListPerInstanceConfigsInstanceGroupManagersRequest,
):
    transport_class = transports.InstanceGroupManagersRestTransport

    request_init = {}
    request_init["instance_group_manager"] = ""
    request_init["project"] = ""
    request_init["zone"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseListPerInstanceConfigs,
        "_BaseListPerInstanceConfigs__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["instanceGroupManager"] = "instance_group_manager_value"
    jsonified_request["project"] = "project_value"
    jsonified_request["zone"] = "zone_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "filter",
            "maxResults",
            "orderBy",
            "pageToken",
        )
    )

    # verify required fields with non-default values are left alone
    assert "instanceGroupManager" in jsonified_request
    assert jsonified_request["instanceGroupManager"] == "instance_group_manager_value"
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "zone" in jsonified_request
    assert jsonified_request["zone"] == "zone_value"

    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.InstanceGroupManagersListPerInstanceConfigsResp()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = compute.InstanceGroupManagersListPerInstanceConfigsResp.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_per_instance_configs(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_per_instance_configs_rest_flattened():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.InstanceGroupManagersListPerInstanceConfigsResp()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "zone": "sample2",
            "instance_group_manager": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = compute.InstanceGroupManagersListPerInstanceConfigsResp.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_per_instance_configs(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}/listPerInstanceConfigs"
            % client.transport._host,
            args[1],
        )


def test_list_per_instance_configs_rest_flattened_error(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_per_instance_configs(
            compute.ListPerInstanceConfigsInstanceGroupManagersRequest(),
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
        )


def test_list_per_instance_configs_rest_pager(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            compute.InstanceGroupManagersListPerInstanceConfigsResp(
                items=[
                    compute.PerInstanceConfig(),
                    compute.PerInstanceConfig(),
                    compute.PerInstanceConfig(),
                ],
                next_page_token="abc",
            ),
            compute.InstanceGroupManagersListPerInstanceConfigsResp(
                items=[],
                next_page_token="def",
            ),
            compute.InstanceGroupManagersListPerInstanceConfigsResp(
                items=[
                    compute.PerInstanceConfig(),
                ],
                next_page_token="ghi",
            ),
            compute.InstanceGroupManagersListPerInstanceConfigsResp(
                items=[
                    compute.PerInstanceConfig(),
                    compute.PerInstanceConfig(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            compute.InstanceGroupManagersListPerInstanceConfigsResp.to_json(x)
            for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {
            "project": "sample1",
            "zone": "sample2",
            "instance_group_manager": "sample3",
        }

        pager = client.list_per_instance_configs(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, compute.PerInstanceConfig) for i in results)

        pages = list(client.list_per_instance_configs(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_patch_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.patch in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.patch] = mock_rpc

        request = {}
        client.patch(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.patch(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_patch_rest_required_fields(
    request_type=compute.PatchInstanceGroupManagerRequest,
):
    transport_class = transports.InstanceGroupManagersRestTransport

    request_init = {}
    request_init["instance_group_manager"] = ""
    request_init["project"] = ""
    request_init["zone"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BasePatch,
        "_BasePatch__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["instanceGroupManager"] = "instance_group_manager_value"
    jsonified_request["project"] = "project_value"
    jsonified_request["zone"] = "zone_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("requestId",))

    # verify required fields with non-default values are left alone
    assert "instanceGroupManager" in jsonified_request
    assert jsonified_request["instanceGroupManager"] == "instance_group_manager_value"
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "zone" in jsonified_request
    assert jsonified_request["zone"] == "zone_value"

    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.Operation()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "patch",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = compute.Operation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.patch(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_patch_rest_flattened():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "zone": "sample2",
            "instance_group_manager": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_manager_resource=compute.InstanceGroupManager(
                all_instances_config=compute.InstanceGroupManagerAllInstancesConfig(
                    properties=compute.InstancePropertiesPatch(
                        expose_host_topology=True
                    )
                )
            ),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.patch(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}"
            % client.transport._host,
            args[1],
        )


def test_patch_rest_flattened_error(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.patch(
            compute.PatchInstanceGroupManagerRequest(),
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_manager_resource=compute.InstanceGroupManager(
                all_instances_config=compute.InstanceGroupManagerAllInstancesConfig(
                    properties=compute.InstancePropertiesPatch(
                        expose_host_topology=True
                    )
                )
            ),
        )


def test_patch_unary_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.patch in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.patch] = mock_rpc

        request = {}
        client.patch_unary(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.patch_unary(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_patch_unary_rest_required_fields(
    request_type=compute.PatchInstanceGroupManagerRequest,
):
    transport_class = transports.InstanceGroupManagersRestTransport

    request_init = {}
    request_init["instance_group_manager"] = ""
    request_init["project"] = ""
    request_init["zone"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BasePatch,
        "_BasePatch__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["instanceGroupManager"] = "instance_group_manager_value"
    jsonified_request["project"] = "project_value"
    jsonified_request["zone"] = "zone_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("requestId",))

    # verify required fields with non-default values are left alone
    assert "instanceGroupManager" in jsonified_request
    assert jsonified_request["instanceGroupManager"] == "instance_group_manager_value"
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "zone" in jsonified_request
    assert jsonified_request["zone"] == "zone_value"

    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.Operation()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "patch",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = compute.Operation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.patch_unary(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_patch_unary_rest_flattened():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "zone": "sample2",
            "instance_group_manager": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_manager_resource=compute.InstanceGroupManager(
                all_instances_config=compute.InstanceGroupManagerAllInstancesConfig(
                    properties=compute.InstancePropertiesPatch(
                        expose_host_topology=True
                    )
                )
            ),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.patch_unary(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}"
            % client.transport._host,
            args[1],
        )


def test_patch_unary_rest_flattened_error(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.patch_unary(
            compute.PatchInstanceGroupManagerRequest(),
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_manager_resource=compute.InstanceGroupManager(
                all_instances_config=compute.InstanceGroupManagerAllInstancesConfig(
                    properties=compute.InstancePropertiesPatch(
                        expose_host_topology=True
                    )
                )
            ),
        )


def test_patch_per_instance_configs_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.patch_per_instance_configs
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.patch_per_instance_configs
        ] = mock_rpc

        request = {}
        client.patch_per_instance_configs(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.patch_per_instance_configs(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_patch_per_instance_configs_rest_required_fields(
    request_type=compute.PatchPerInstanceConfigsInstanceGroupManagerRequest,
):
    transport_class = transports.InstanceGroupManagersRestTransport

    request_init = {}
    request_init["instance_group_manager"] = ""
    request_init["project"] = ""
    request_init["zone"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BasePatchPerInstanceConfigs,
        "_BasePatchPerInstanceConfigs__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["instanceGroupManager"] = "instance_group_manager_value"
    jsonified_request["project"] = "project_value"
    jsonified_request["zone"] = "zone_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("requestId",))

    # verify required fields with non-default values are left alone
    assert "instanceGroupManager" in jsonified_request
    assert jsonified_request["instanceGroupManager"] == "instance_group_manager_value"
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "zone" in jsonified_request
    assert jsonified_request["zone"] == "zone_value"

    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.Operation()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = compute.Operation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.patch_per_instance_configs(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_patch_per_instance_configs_rest_flattened():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "zone": "sample2",
            "instance_group_manager": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_patch_per_instance_configs_req_resource=compute.InstanceGroupManagersPatchPerInstanceConfigsReq(
                per_instance_configs=[
                    compute.PerInstanceConfig(fingerprint="fingerprint_value")
                ]
            ),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.patch_per_instance_configs(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}/patchPerInstanceConfigs"
            % client.transport._host,
            args[1],
        )


def test_patch_per_instance_configs_rest_flattened_error(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.patch_per_instance_configs(
            compute.PatchPerInstanceConfigsInstanceGroupManagerRequest(),
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_patch_per_instance_configs_req_resource=compute.InstanceGroupManagersPatchPerInstanceConfigsReq(
                per_instance_configs=[
                    compute.PerInstanceConfig(fingerprint="fingerprint_value")
                ]
            ),
        )


def test_patch_per_instance_configs_unary_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.patch_per_instance_configs
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.patch_per_instance_configs
        ] = mock_rpc

        request = {}
        client.patch_per_instance_configs_unary(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.patch_per_instance_configs_unary(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_patch_per_instance_configs_unary_rest_required_fields(
    request_type=compute.PatchPerInstanceConfigsInstanceGroupManagerRequest,
):
    transport_class = transports.InstanceGroupManagersRestTransport

    request_init = {}
    request_init["instance_group_manager"] = ""
    request_init["project"] = ""
    request_init["zone"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BasePatchPerInstanceConfigs,
        "_BasePatchPerInstanceConfigs__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["instanceGroupManager"] = "instance_group_manager_value"
    jsonified_request["project"] = "project_value"
    jsonified_request["zone"] = "zone_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("requestId",))

    # verify required fields with non-default values are left alone
    assert "instanceGroupManager" in jsonified_request
    assert jsonified_request["instanceGroupManager"] == "instance_group_manager_value"
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "zone" in jsonified_request
    assert jsonified_request["zone"] == "zone_value"

    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.Operation()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = compute.Operation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.patch_per_instance_configs_unary(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_patch_per_instance_configs_unary_rest_flattened():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "zone": "sample2",
            "instance_group_manager": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_patch_per_instance_configs_req_resource=compute.InstanceGroupManagersPatchPerInstanceConfigsReq(
                per_instance_configs=[
                    compute.PerInstanceConfig(fingerprint="fingerprint_value")
                ]
            ),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.patch_per_instance_configs_unary(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}/patchPerInstanceConfigs"
            % client.transport._host,
            args[1],
        )


def test_patch_per_instance_configs_unary_rest_flattened_error(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.patch_per_instance_configs_unary(
            compute.PatchPerInstanceConfigsInstanceGroupManagerRequest(),
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_patch_per_instance_configs_req_resource=compute.InstanceGroupManagersPatchPerInstanceConfigsReq(
                per_instance_configs=[
                    compute.PerInstanceConfig(fingerprint="fingerprint_value")
                ]
            ),
        )


def test_recreate_instances_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.recreate_instances in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.recreate_instances] = (
            mock_rpc
        )

        request = {}
        client.recreate_instances(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.recreate_instances(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_recreate_instances_rest_required_fields(
    request_type=compute.RecreateInstancesInstanceGroupManagerRequest,
):
    transport_class = transports.InstanceGroupManagersRestTransport

    request_init = {}
    request_init["instance_group_manager"] = ""
    request_init["project"] = ""
    request_init["zone"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseRecreateInstances,
        "_BaseRecreateInstances__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["instanceGroupManager"] = "instance_group_manager_value"
    jsonified_request["project"] = "project_value"
    jsonified_request["zone"] = "zone_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "noGracefulShutdown",
            "requestId",
        )
    )

    # verify required fields with non-default values are left alone
    assert "instanceGroupManager" in jsonified_request
    assert jsonified_request["instanceGroupManager"] == "instance_group_manager_value"
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "zone" in jsonified_request
    assert jsonified_request["zone"] == "zone_value"

    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.Operation()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = compute.Operation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.recreate_instances(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_recreate_instances_rest_flattened():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "zone": "sample2",
            "instance_group_manager": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_recreate_instances_request_resource=compute.InstanceGroupManagersRecreateInstancesRequest(
                instances=["instances_value"]
            ),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.recreate_instances(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}/recreateInstances"
            % client.transport._host,
            args[1],
        )


def test_recreate_instances_rest_flattened_error(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.recreate_instances(
            compute.RecreateInstancesInstanceGroupManagerRequest(),
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_recreate_instances_request_resource=compute.InstanceGroupManagersRecreateInstancesRequest(
                instances=["instances_value"]
            ),
        )


def test_recreate_instances_unary_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.recreate_instances in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.recreate_instances] = (
            mock_rpc
        )

        request = {}
        client.recreate_instances_unary(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.recreate_instances_unary(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_recreate_instances_unary_rest_required_fields(
    request_type=compute.RecreateInstancesInstanceGroupManagerRequest,
):
    transport_class = transports.InstanceGroupManagersRestTransport

    request_init = {}
    request_init["instance_group_manager"] = ""
    request_init["project"] = ""
    request_init["zone"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseRecreateInstances,
        "_BaseRecreateInstances__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["instanceGroupManager"] = "instance_group_manager_value"
    jsonified_request["project"] = "project_value"
    jsonified_request["zone"] = "zone_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "noGracefulShutdown",
            "requestId",
        )
    )

    # verify required fields with non-default values are left alone
    assert "instanceGroupManager" in jsonified_request
    assert jsonified_request["instanceGroupManager"] == "instance_group_manager_value"
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "zone" in jsonified_request
    assert jsonified_request["zone"] == "zone_value"

    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.Operation()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = compute.Operation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.recreate_instances_unary(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_recreate_instances_unary_rest_flattened():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "zone": "sample2",
            "instance_group_manager": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_recreate_instances_request_resource=compute.InstanceGroupManagersRecreateInstancesRequest(
                instances=["instances_value"]
            ),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.recreate_instances_unary(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}/recreateInstances"
            % client.transport._host,
            args[1],
        )


def test_recreate_instances_unary_rest_flattened_error(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.recreate_instances_unary(
            compute.RecreateInstancesInstanceGroupManagerRequest(),
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_recreate_instances_request_resource=compute.InstanceGroupManagersRecreateInstancesRequest(
                instances=["instances_value"]
            ),
        )


def test_resize_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.resize in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.resize] = mock_rpc

        request = {}
        client.resize(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.resize(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_resize_rest_required_fields(
    request_type=compute.ResizeInstanceGroupManagerRequest,
):
    transport_class = transports.InstanceGroupManagersRestTransport

    request_init = {}
    request_init["instance_group_manager"] = ""
    request_init["project"] = ""
    request_init["size"] = 0
    request_init["zone"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped
    assert "size" not in jsonified_request

    default_values = getattr(
        transport_class._BaseResize,
        "_BaseResize__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present
    assert "size" in jsonified_request
    assert jsonified_request["size"] == request_init["size"]

    jsonified_request["instanceGroupManager"] = "instance_group_manager_value"
    jsonified_request["project"] = "project_value"
    jsonified_request["size"] = 443
    jsonified_request["zone"] = "zone_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "requestId",
            "size",
        )
    )

    # verify required fields with non-default values are left alone
    assert "instanceGroupManager" in jsonified_request
    assert jsonified_request["instanceGroupManager"] == "instance_group_manager_value"
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "size" in jsonified_request
    assert jsonified_request["size"] == 443
    assert "zone" in jsonified_request
    assert jsonified_request["zone"] == "zone_value"

    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.Operation()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = compute.Operation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.resize(request)

            expected_params = [
                (
                    "size",
                    str(0),
                ),
            ]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_resize_rest_flattened():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "zone": "sample2",
            "instance_group_manager": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            size=443,
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.resize(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}/resize"
            % client.transport._host,
            args[1],
        )


def test_resize_rest_flattened_error(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.resize(
            compute.ResizeInstanceGroupManagerRequest(),
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            size=443,
        )


def test_resize_unary_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.resize in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.resize] = mock_rpc

        request = {}
        client.resize_unary(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.resize_unary(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_resize_unary_rest_required_fields(
    request_type=compute.ResizeInstanceGroupManagerRequest,
):
    transport_class = transports.InstanceGroupManagersRestTransport

    request_init = {}
    request_init["instance_group_manager"] = ""
    request_init["project"] = ""
    request_init["size"] = 0
    request_init["zone"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped
    assert "size" not in jsonified_request

    default_values = getattr(
        transport_class._BaseResize,
        "_BaseResize__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present
    assert "size" in jsonified_request
    assert jsonified_request["size"] == request_init["size"]

    jsonified_request["instanceGroupManager"] = "instance_group_manager_value"
    jsonified_request["project"] = "project_value"
    jsonified_request["size"] = 443
    jsonified_request["zone"] = "zone_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "requestId",
            "size",
        )
    )

    # verify required fields with non-default values are left alone
    assert "instanceGroupManager" in jsonified_request
    assert jsonified_request["instanceGroupManager"] == "instance_group_manager_value"
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "size" in jsonified_request
    assert jsonified_request["size"] == 443
    assert "zone" in jsonified_request
    assert jsonified_request["zone"] == "zone_value"

    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.Operation()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = compute.Operation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.resize_unary(request)

            expected_params = [
                (
                    "size",
                    str(0),
                ),
            ]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_resize_unary_rest_flattened():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "zone": "sample2",
            "instance_group_manager": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            size=443,
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.resize_unary(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}/resize"
            % client.transport._host,
            args[1],
        )


def test_resize_unary_rest_flattened_error(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.resize_unary(
            compute.ResizeInstanceGroupManagerRequest(),
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            size=443,
        )


def test_resume_instances_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.resume_instances in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.resume_instances] = (
            mock_rpc
        )

        request = {}
        client.resume_instances(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.resume_instances(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_resume_instances_rest_required_fields(
    request_type=compute.ResumeInstancesInstanceGroupManagerRequest,
):
    transport_class = transports.InstanceGroupManagersRestTransport

    request_init = {}
    request_init["instance_group_manager"] = ""
    request_init["project"] = ""
    request_init["zone"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseResumeInstances,
        "_BaseResumeInstances__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["instanceGroupManager"] = "instance_group_manager_value"
    jsonified_request["project"] = "project_value"
    jsonified_request["zone"] = "zone_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("requestId",))

    # verify required fields with non-default values are left alone
    assert "instanceGroupManager" in jsonified_request
    assert jsonified_request["instanceGroupManager"] == "instance_group_manager_value"
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "zone" in jsonified_request
    assert jsonified_request["zone"] == "zone_value"

    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.Operation()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = compute.Operation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.resume_instances(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_resume_instances_rest_flattened():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "zone": "sample2",
            "instance_group_manager": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_resume_instances_request_resource=compute.InstanceGroupManagersResumeInstancesRequest(
                instances=["instances_value"]
            ),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.resume_instances(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}/resumeInstances"
            % client.transport._host,
            args[1],
        )


def test_resume_instances_rest_flattened_error(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.resume_instances(
            compute.ResumeInstancesInstanceGroupManagerRequest(),
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_resume_instances_request_resource=compute.InstanceGroupManagersResumeInstancesRequest(
                instances=["instances_value"]
            ),
        )


def test_resume_instances_unary_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.resume_instances in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.resume_instances] = (
            mock_rpc
        )

        request = {}
        client.resume_instances_unary(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.resume_instances_unary(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_resume_instances_unary_rest_required_fields(
    request_type=compute.ResumeInstancesInstanceGroupManagerRequest,
):
    transport_class = transports.InstanceGroupManagersRestTransport

    request_init = {}
    request_init["instance_group_manager"] = ""
    request_init["project"] = ""
    request_init["zone"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseResumeInstances,
        "_BaseResumeInstances__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["instanceGroupManager"] = "instance_group_manager_value"
    jsonified_request["project"] = "project_value"
    jsonified_request["zone"] = "zone_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("requestId",))

    # verify required fields with non-default values are left alone
    assert "instanceGroupManager" in jsonified_request
    assert jsonified_request["instanceGroupManager"] == "instance_group_manager_value"
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "zone" in jsonified_request
    assert jsonified_request["zone"] == "zone_value"

    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.Operation()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = compute.Operation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.resume_instances_unary(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_resume_instances_unary_rest_flattened():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "zone": "sample2",
            "instance_group_manager": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_resume_instances_request_resource=compute.InstanceGroupManagersResumeInstancesRequest(
                instances=["instances_value"]
            ),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.resume_instances_unary(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}/resumeInstances"
            % client.transport._host,
            args[1],
        )


def test_resume_instances_unary_rest_flattened_error(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.resume_instances_unary(
            compute.ResumeInstancesInstanceGroupManagerRequest(),
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_resume_instances_request_resource=compute.InstanceGroupManagersResumeInstancesRequest(
                instances=["instances_value"]
            ),
        )


def test_set_instance_template_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.set_instance_template
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.set_instance_template] = (
            mock_rpc
        )

        request = {}
        client.set_instance_template(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.set_instance_template(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_set_instance_template_rest_required_fields(
    request_type=compute.SetInstanceTemplateInstanceGroupManagerRequest,
):
    transport_class = transports.InstanceGroupManagersRestTransport

    request_init = {}
    request_init["instance_group_manager"] = ""
    request_init["project"] = ""
    request_init["zone"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseSetInstanceTemplate,
        "_BaseSetInstanceTemplate__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["instanceGroupManager"] = "instance_group_manager_value"
    jsonified_request["project"] = "project_value"
    jsonified_request["zone"] = "zone_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("requestId",))

    # verify required fields with non-default values are left alone
    assert "instanceGroupManager" in jsonified_request
    assert jsonified_request["instanceGroupManager"] == "instance_group_manager_value"
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "zone" in jsonified_request
    assert jsonified_request["zone"] == "zone_value"

    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.Operation()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = compute.Operation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.set_instance_template(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_set_instance_template_rest_flattened():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "zone": "sample2",
            "instance_group_manager": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_set_instance_template_request_resource=compute.InstanceGroupManagersSetInstanceTemplateRequest(
                instance_template="instance_template_value"
            ),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.set_instance_template(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}/setInstanceTemplate"
            % client.transport._host,
            args[1],
        )


def test_set_instance_template_rest_flattened_error(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.set_instance_template(
            compute.SetInstanceTemplateInstanceGroupManagerRequest(),
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_set_instance_template_request_resource=compute.InstanceGroupManagersSetInstanceTemplateRequest(
                instance_template="instance_template_value"
            ),
        )


def test_set_instance_template_unary_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.set_instance_template
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.set_instance_template] = (
            mock_rpc
        )

        request = {}
        client.set_instance_template_unary(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.set_instance_template_unary(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_set_instance_template_unary_rest_required_fields(
    request_type=compute.SetInstanceTemplateInstanceGroupManagerRequest,
):
    transport_class = transports.InstanceGroupManagersRestTransport

    request_init = {}
    request_init["instance_group_manager"] = ""
    request_init["project"] = ""
    request_init["zone"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseSetInstanceTemplate,
        "_BaseSetInstanceTemplate__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["instanceGroupManager"] = "instance_group_manager_value"
    jsonified_request["project"] = "project_value"
    jsonified_request["zone"] = "zone_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("requestId",))

    # verify required fields with non-default values are left alone
    assert "instanceGroupManager" in jsonified_request
    assert jsonified_request["instanceGroupManager"] == "instance_group_manager_value"
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "zone" in jsonified_request
    assert jsonified_request["zone"] == "zone_value"

    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.Operation()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = compute.Operation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.set_instance_template_unary(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_set_instance_template_unary_rest_flattened():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "zone": "sample2",
            "instance_group_manager": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_set_instance_template_request_resource=compute.InstanceGroupManagersSetInstanceTemplateRequest(
                instance_template="instance_template_value"
            ),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.set_instance_template_unary(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}/setInstanceTemplate"
            % client.transport._host,
            args[1],
        )


def test_set_instance_template_unary_rest_flattened_error(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.set_instance_template_unary(
            compute.SetInstanceTemplateInstanceGroupManagerRequest(),
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_set_instance_template_request_resource=compute.InstanceGroupManagersSetInstanceTemplateRequest(
                instance_template="instance_template_value"
            ),
        )


def test_set_target_pools_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.set_target_pools in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.set_target_pools] = (
            mock_rpc
        )

        request = {}
        client.set_target_pools(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.set_target_pools(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_set_target_pools_rest_required_fields(
    request_type=compute.SetTargetPoolsInstanceGroupManagerRequest,
):
    transport_class = transports.InstanceGroupManagersRestTransport

    request_init = {}
    request_init["instance_group_manager"] = ""
    request_init["project"] = ""
    request_init["zone"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseSetTargetPools,
        "_BaseSetTargetPools__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["instanceGroupManager"] = "instance_group_manager_value"
    jsonified_request["project"] = "project_value"
    jsonified_request["zone"] = "zone_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("requestId",))

    # verify required fields with non-default values are left alone
    assert "instanceGroupManager" in jsonified_request
    assert jsonified_request["instanceGroupManager"] == "instance_group_manager_value"
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "zone" in jsonified_request
    assert jsonified_request["zone"] == "zone_value"

    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.Operation()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = compute.Operation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.set_target_pools(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_set_target_pools_rest_flattened():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "zone": "sample2",
            "instance_group_manager": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_set_target_pools_request_resource=compute.InstanceGroupManagersSetTargetPoolsRequest(
                fingerprint="fingerprint_value"
            ),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.set_target_pools(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}/setTargetPools"
            % client.transport._host,
            args[1],
        )


def test_set_target_pools_rest_flattened_error(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.set_target_pools(
            compute.SetTargetPoolsInstanceGroupManagerRequest(),
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_set_target_pools_request_resource=compute.InstanceGroupManagersSetTargetPoolsRequest(
                fingerprint="fingerprint_value"
            ),
        )


def test_set_target_pools_unary_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.set_target_pools in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.set_target_pools] = (
            mock_rpc
        )

        request = {}
        client.set_target_pools_unary(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.set_target_pools_unary(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_set_target_pools_unary_rest_required_fields(
    request_type=compute.SetTargetPoolsInstanceGroupManagerRequest,
):
    transport_class = transports.InstanceGroupManagersRestTransport

    request_init = {}
    request_init["instance_group_manager"] = ""
    request_init["project"] = ""
    request_init["zone"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseSetTargetPools,
        "_BaseSetTargetPools__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["instanceGroupManager"] = "instance_group_manager_value"
    jsonified_request["project"] = "project_value"
    jsonified_request["zone"] = "zone_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("requestId",))

    # verify required fields with non-default values are left alone
    assert "instanceGroupManager" in jsonified_request
    assert jsonified_request["instanceGroupManager"] == "instance_group_manager_value"
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "zone" in jsonified_request
    assert jsonified_request["zone"] == "zone_value"

    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.Operation()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = compute.Operation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.set_target_pools_unary(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_set_target_pools_unary_rest_flattened():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "zone": "sample2",
            "instance_group_manager": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_set_target_pools_request_resource=compute.InstanceGroupManagersSetTargetPoolsRequest(
                fingerprint="fingerprint_value"
            ),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.set_target_pools_unary(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}/setTargetPools"
            % client.transport._host,
            args[1],
        )


def test_set_target_pools_unary_rest_flattened_error(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.set_target_pools_unary(
            compute.SetTargetPoolsInstanceGroupManagerRequest(),
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_set_target_pools_request_resource=compute.InstanceGroupManagersSetTargetPoolsRequest(
                fingerprint="fingerprint_value"
            ),
        )


def test_start_instances_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.start_instances in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.start_instances] = mock_rpc

        request = {}
        client.start_instances(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.start_instances(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_start_instances_rest_required_fields(
    request_type=compute.StartInstancesInstanceGroupManagerRequest,
):
    transport_class = transports.InstanceGroupManagersRestTransport

    request_init = {}
    request_init["instance_group_manager"] = ""
    request_init["project"] = ""
    request_init["zone"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseStartInstances,
        "_BaseStartInstances__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["instanceGroupManager"] = "instance_group_manager_value"
    jsonified_request["project"] = "project_value"
    jsonified_request["zone"] = "zone_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("requestId",))

    # verify required fields with non-default values are left alone
    assert "instanceGroupManager" in jsonified_request
    assert jsonified_request["instanceGroupManager"] == "instance_group_manager_value"
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "zone" in jsonified_request
    assert jsonified_request["zone"] == "zone_value"

    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.Operation()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = compute.Operation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.start_instances(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_start_instances_rest_flattened():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "zone": "sample2",
            "instance_group_manager": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_start_instances_request_resource=compute.InstanceGroupManagersStartInstancesRequest(
                instances=["instances_value"]
            ),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.start_instances(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}/startInstances"
            % client.transport._host,
            args[1],
        )


def test_start_instances_rest_flattened_error(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.start_instances(
            compute.StartInstancesInstanceGroupManagerRequest(),
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_start_instances_request_resource=compute.InstanceGroupManagersStartInstancesRequest(
                instances=["instances_value"]
            ),
        )


def test_start_instances_unary_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.start_instances in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.start_instances] = mock_rpc

        request = {}
        client.start_instances_unary(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.start_instances_unary(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_start_instances_unary_rest_required_fields(
    request_type=compute.StartInstancesInstanceGroupManagerRequest,
):
    transport_class = transports.InstanceGroupManagersRestTransport

    request_init = {}
    request_init["instance_group_manager"] = ""
    request_init["project"] = ""
    request_init["zone"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseStartInstances,
        "_BaseStartInstances__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["instanceGroupManager"] = "instance_group_manager_value"
    jsonified_request["project"] = "project_value"
    jsonified_request["zone"] = "zone_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("requestId",))

    # verify required fields with non-default values are left alone
    assert "instanceGroupManager" in jsonified_request
    assert jsonified_request["instanceGroupManager"] == "instance_group_manager_value"
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "zone" in jsonified_request
    assert jsonified_request["zone"] == "zone_value"

    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.Operation()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = compute.Operation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.start_instances_unary(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_start_instances_unary_rest_flattened():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "zone": "sample2",
            "instance_group_manager": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_start_instances_request_resource=compute.InstanceGroupManagersStartInstancesRequest(
                instances=["instances_value"]
            ),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.start_instances_unary(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}/startInstances"
            % client.transport._host,
            args[1],
        )


def test_start_instances_unary_rest_flattened_error(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.start_instances_unary(
            compute.StartInstancesInstanceGroupManagerRequest(),
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_start_instances_request_resource=compute.InstanceGroupManagersStartInstancesRequest(
                instances=["instances_value"]
            ),
        )


def test_stop_instances_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.stop_instances in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.stop_instances] = mock_rpc

        request = {}
        client.stop_instances(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.stop_instances(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_stop_instances_rest_required_fields(
    request_type=compute.StopInstancesInstanceGroupManagerRequest,
):
    transport_class = transports.InstanceGroupManagersRestTransport

    request_init = {}
    request_init["instance_group_manager"] = ""
    request_init["project"] = ""
    request_init["zone"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseStopInstances,
        "_BaseStopInstances__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["instanceGroupManager"] = "instance_group_manager_value"
    jsonified_request["project"] = "project_value"
    jsonified_request["zone"] = "zone_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "noGracefulShutdown",
            "requestId",
        )
    )

    # verify required fields with non-default values are left alone
    assert "instanceGroupManager" in jsonified_request
    assert jsonified_request["instanceGroupManager"] == "instance_group_manager_value"
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "zone" in jsonified_request
    assert jsonified_request["zone"] == "zone_value"

    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.Operation()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = compute.Operation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.stop_instances(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_stop_instances_rest_flattened():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "zone": "sample2",
            "instance_group_manager": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_stop_instances_request_resource=compute.InstanceGroupManagersStopInstancesRequest(
                force_stop=True
            ),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.stop_instances(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}/stopInstances"
            % client.transport._host,
            args[1],
        )


def test_stop_instances_rest_flattened_error(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.stop_instances(
            compute.StopInstancesInstanceGroupManagerRequest(),
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_stop_instances_request_resource=compute.InstanceGroupManagersStopInstancesRequest(
                force_stop=True
            ),
        )


def test_stop_instances_unary_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.stop_instances in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.stop_instances] = mock_rpc

        request = {}
        client.stop_instances_unary(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.stop_instances_unary(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_stop_instances_unary_rest_required_fields(
    request_type=compute.StopInstancesInstanceGroupManagerRequest,
):
    transport_class = transports.InstanceGroupManagersRestTransport

    request_init = {}
    request_init["instance_group_manager"] = ""
    request_init["project"] = ""
    request_init["zone"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseStopInstances,
        "_BaseStopInstances__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["instanceGroupManager"] = "instance_group_manager_value"
    jsonified_request["project"] = "project_value"
    jsonified_request["zone"] = "zone_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "noGracefulShutdown",
            "requestId",
        )
    )

    # verify required fields with non-default values are left alone
    assert "instanceGroupManager" in jsonified_request
    assert jsonified_request["instanceGroupManager"] == "instance_group_manager_value"
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "zone" in jsonified_request
    assert jsonified_request["zone"] == "zone_value"

    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.Operation()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = compute.Operation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.stop_instances_unary(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_stop_instances_unary_rest_flattened():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "zone": "sample2",
            "instance_group_manager": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_stop_instances_request_resource=compute.InstanceGroupManagersStopInstancesRequest(
                force_stop=True
            ),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.stop_instances_unary(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}/stopInstances"
            % client.transport._host,
            args[1],
        )


def test_stop_instances_unary_rest_flattened_error(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.stop_instances_unary(
            compute.StopInstancesInstanceGroupManagerRequest(),
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_stop_instances_request_resource=compute.InstanceGroupManagersStopInstancesRequest(
                force_stop=True
            ),
        )


def test_suspend_instances_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.suspend_instances in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.suspend_instances] = (
            mock_rpc
        )

        request = {}
        client.suspend_instances(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.suspend_instances(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_suspend_instances_rest_required_fields(
    request_type=compute.SuspendInstancesInstanceGroupManagerRequest,
):
    transport_class = transports.InstanceGroupManagersRestTransport

    request_init = {}
    request_init["instance_group_manager"] = ""
    request_init["project"] = ""
    request_init["zone"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseSuspendInstances,
        "_BaseSuspendInstances__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["instanceGroupManager"] = "instance_group_manager_value"
    jsonified_request["project"] = "project_value"
    jsonified_request["zone"] = "zone_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("requestId",))

    # verify required fields with non-default values are left alone
    assert "instanceGroupManager" in jsonified_request
    assert jsonified_request["instanceGroupManager"] == "instance_group_manager_value"
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "zone" in jsonified_request
    assert jsonified_request["zone"] == "zone_value"

    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.Operation()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = compute.Operation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.suspend_instances(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_suspend_instances_rest_flattened():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "zone": "sample2",
            "instance_group_manager": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_suspend_instances_request_resource=compute.InstanceGroupManagersSuspendInstancesRequest(
                force_suspend=True
            ),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.suspend_instances(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}/suspendInstances"
            % client.transport._host,
            args[1],
        )


def test_suspend_instances_rest_flattened_error(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.suspend_instances(
            compute.SuspendInstancesInstanceGroupManagerRequest(),
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_suspend_instances_request_resource=compute.InstanceGroupManagersSuspendInstancesRequest(
                force_suspend=True
            ),
        )


def test_suspend_instances_unary_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.suspend_instances in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.suspend_instances] = (
            mock_rpc
        )

        request = {}
        client.suspend_instances_unary(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.suspend_instances_unary(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_suspend_instances_unary_rest_required_fields(
    request_type=compute.SuspendInstancesInstanceGroupManagerRequest,
):
    transport_class = transports.InstanceGroupManagersRestTransport

    request_init = {}
    request_init["instance_group_manager"] = ""
    request_init["project"] = ""
    request_init["zone"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseSuspendInstances,
        "_BaseSuspendInstances__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["instanceGroupManager"] = "instance_group_manager_value"
    jsonified_request["project"] = "project_value"
    jsonified_request["zone"] = "zone_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("requestId",))

    # verify required fields with non-default values are left alone
    assert "instanceGroupManager" in jsonified_request
    assert jsonified_request["instanceGroupManager"] == "instance_group_manager_value"
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "zone" in jsonified_request
    assert jsonified_request["zone"] == "zone_value"

    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.Operation()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = compute.Operation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.suspend_instances_unary(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_suspend_instances_unary_rest_flattened():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "zone": "sample2",
            "instance_group_manager": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_suspend_instances_request_resource=compute.InstanceGroupManagersSuspendInstancesRequest(
                force_suspend=True
            ),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.suspend_instances_unary(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}/suspendInstances"
            % client.transport._host,
            args[1],
        )


def test_suspend_instances_unary_rest_flattened_error(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.suspend_instances_unary(
            compute.SuspendInstancesInstanceGroupManagerRequest(),
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_suspend_instances_request_resource=compute.InstanceGroupManagersSuspendInstancesRequest(
                force_suspend=True
            ),
        )


def test_update_per_instance_configs_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.update_per_instance_configs
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.update_per_instance_configs
        ] = mock_rpc

        request = {}
        client.update_per_instance_configs(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.update_per_instance_configs(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_update_per_instance_configs_rest_required_fields(
    request_type=compute.UpdatePerInstanceConfigsInstanceGroupManagerRequest,
):
    transport_class = transports.InstanceGroupManagersRestTransport

    request_init = {}
    request_init["instance_group_manager"] = ""
    request_init["project"] = ""
    request_init["zone"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseUpdatePerInstanceConfigs,
        "_BaseUpdatePerInstanceConfigs__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["instanceGroupManager"] = "instance_group_manager_value"
    jsonified_request["project"] = "project_value"
    jsonified_request["zone"] = "zone_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("requestId",))

    # verify required fields with non-default values are left alone
    assert "instanceGroupManager" in jsonified_request
    assert jsonified_request["instanceGroupManager"] == "instance_group_manager_value"
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "zone" in jsonified_request
    assert jsonified_request["zone"] == "zone_value"

    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.Operation()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = compute.Operation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.update_per_instance_configs(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_update_per_instance_configs_rest_flattened():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "zone": "sample2",
            "instance_group_manager": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_update_per_instance_configs_req_resource=compute.InstanceGroupManagersUpdatePerInstanceConfigsReq(
                per_instance_configs=[
                    compute.PerInstanceConfig(fingerprint="fingerprint_value")
                ]
            ),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.update_per_instance_configs(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}/updatePerInstanceConfigs"
            % client.transport._host,
            args[1],
        )


def test_update_per_instance_configs_rest_flattened_error(transport: str = "rest"):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_per_instance_configs(
            compute.UpdatePerInstanceConfigsInstanceGroupManagerRequest(),
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_update_per_instance_configs_req_resource=compute.InstanceGroupManagersUpdatePerInstanceConfigsReq(
                per_instance_configs=[
                    compute.PerInstanceConfig(fingerprint="fingerprint_value")
                ]
            ),
        )


def test_update_per_instance_configs_unary_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.update_per_instance_configs
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.update_per_instance_configs
        ] = mock_rpc

        request = {}
        client.update_per_instance_configs_unary(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        # Operation methods build a cached wrapper on first rpc call
        # subsequent calls should use the cached wrapper
        wrapper_fn.reset_mock()

        client.update_per_instance_configs_unary(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_update_per_instance_configs_unary_rest_required_fields(
    request_type=compute.UpdatePerInstanceConfigsInstanceGroupManagerRequest,
):
    transport_class = transports.InstanceGroupManagersRestTransport

    request_init = {}
    request_init["instance_group_manager"] = ""
    request_init["project"] = ""
    request_init["zone"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseUpdatePerInstanceConfigs,
        "_BaseUpdatePerInstanceConfigs__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["instanceGroupManager"] = "instance_group_manager_value"
    jsonified_request["project"] = "project_value"
    jsonified_request["zone"] = "zone_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("requestId",))

    # verify required fields with non-default values are left alone
    assert "instanceGroupManager" in jsonified_request
    assert jsonified_request["instanceGroupManager"] == "instance_group_manager_value"
    assert "project" in jsonified_request
    assert jsonified_request["project"] == "project_value"
    assert "zone" in jsonified_request
    assert jsonified_request["zone"] == "zone_value"

    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = compute.Operation()
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # We need to mock transcode() because providing default values
        # for required fields will fail the real version if the http_options
        # expect actual values for those fields.
        with mock.patch.object(path_template, "transcode") as transcode:
            # A uri without fields and an empty body will force all the
            # request fields to show up in the query_params.
            pb_request = request_type.pb(request)
            transcode_result = {
                "uri": "v1/sample_method",
                "method": "post",
                "query_params": pb_request,
            }
            transcode_result["body"] = pb_request
            transcode.return_value = transcode_result

            response_value = Response()
            response_value.status_code = 200

            # Convert return value to protobuf type
            return_value = compute.Operation.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.update_per_instance_configs_unary(request)

            expected_params = []
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_update_per_instance_configs_unary_rest_flattened():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "project": "sample1",
            "zone": "sample2",
            "instance_group_manager": "sample3",
        }

        # get truthy value for each flattened field
        mock_args = dict(
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_update_per_instance_configs_req_resource=compute.InstanceGroupManagersUpdatePerInstanceConfigsReq(
                per_instance_configs=[
                    compute.PerInstanceConfig(fingerprint="fingerprint_value")
                ]
            ),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.update_per_instance_configs_unary(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/compute/v1/projects/{project}/zones/{zone}/instanceGroupManagers/{instance_group_manager}/updatePerInstanceConfigs"
            % client.transport._host,
            args[1],
        )


def test_update_per_instance_configs_unary_rest_flattened_error(
    transport: str = "rest",
):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_per_instance_configs_unary(
            compute.UpdatePerInstanceConfigsInstanceGroupManagerRequest(),
            project="project_value",
            zone="zone_value",
            instance_group_manager="instance_group_manager_value",
            instance_group_managers_update_per_instance_configs_req_resource=compute.InstanceGroupManagersUpdatePerInstanceConfigsReq(
                per_instance_configs=[
                    compute.PerInstanceConfig(fingerprint="fingerprint_value")
                ]
            ),
        )


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.InstanceGroupManagersRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport=transport,
        )

    # It is an error to provide a credentials file and a transport instance.
    transport = transports.InstanceGroupManagersRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = InstanceGroupManagersClient(
            client_options={"credentials_file": "credentials.json"},
            transport=transport,
        )

    # It is an error to provide an api_key and a transport instance.
    transport = transports.InstanceGroupManagersRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = InstanceGroupManagersClient(
            client_options=options,
            transport=transport,
        )

    # It is an error to provide an api_key and a credential.
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = InstanceGroupManagersClient(
            client_options=options, credentials=ga_credentials.AnonymousCredentials()
        )

    # It is an error to provide scopes and a transport instance.
    transport = transports.InstanceGroupManagersRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = InstanceGroupManagersClient(
            client_options={"scopes": ["1", "2"]},
            transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.InstanceGroupManagersRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    client = InstanceGroupManagersClient(transport=transport)
    assert client.transport is transport


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.InstanceGroupManagersRestTransport,
    ],
)
def test_transport_adc(transport_class):
    # Test default credentials are used if not provided.
    with mock.patch.object(google.auth, "default") as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class()
        adc.assert_called_once()


def test_transport_kind_rest():
    transport = InstanceGroupManagersClient.get_transport_class("rest")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "rest"


def test_abandon_instances_rest_bad_request(
    request_type=compute.AbandonInstancesInstanceGroupManagerRequest,
):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "zone": "sample2",
        "instance_group_manager": "sample3",
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.abandon_instances(request)


@pytest.mark.parametrize(
    "request_type",
    [
        compute.AbandonInstancesInstanceGroupManagerRequest,
        dict,
    ],
)
def test_abandon_instances_rest_call_success(request_type):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "zone": "sample2",
        "instance_group_manager": "sample3",
    }
    request_init["instance_group_managers_abandon_instances_request_resource"] = {
        "instances": ["instances_value1", "instances_value2"]
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = compute.AbandonInstancesInstanceGroupManagerRequest.meta.fields[
        "instance_group_managers_abandon_instances_request_resource"
    ]

    def get_message_fields(field):
        # Given a field which is a message (composite type), return a list with
        # all the fields of the message.
        # If the field is not a composite type, return an empty list.
        message_fields = []

        if hasattr(field, "message") and field.message:
            is_field_type_proto_plus_type = not hasattr(field.message, "DESCRIPTOR")

            if is_field_type_proto_plus_type:
                message_fields = field.message.meta.fields.values()
            # Add `# pragma: NO COVER` because there may not be any `*_pb2` field types
            else:  # pragma: NO COVER
                message_fields = field.message.DESCRIPTOR.fields
        return message_fields

    runtime_nested_fields = [
        (field.name, nested_field.name)
        for field in get_message_fields(test_field)
        for nested_field in get_message_fields(field)
    ]

    subfields_not_in_runtime = []

    # For each item in the sample request, create a list of sub fields which are not present at runtime
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for field, value in request_init[
        "instance_group_managers_abandon_instances_request_resource"
    ].items():  # pragma: NO COVER
        result = None
        is_repeated = False
        # For repeated fields
        if isinstance(value, list) and len(value):
            is_repeated = True
            result = value[0]
        # For fields where the type is another message
        if isinstance(value, dict):
            result = value

        if result and hasattr(result, "keys"):
            for subfield in result.keys():
                if (field, subfield) not in runtime_nested_fields:
                    subfields_not_in_runtime.append(
                        {
                            "field": field,
                            "subfield": subfield,
                            "is_repeated": is_repeated,
                        }
                    )

    # Remove fields from the sample request which are not present in the runtime version of the dependency
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for subfield_to_delete in subfields_not_in_runtime:  # pragma: NO COVER
        field = subfield_to_delete.get("field")
        field_repeated = subfield_to_delete.get("is_repeated")
        subfield = subfield_to_delete.get("subfield")
        if subfield:
            if field_repeated:
                for i in range(
                    0,
                    len(
                        request_init[
                            "instance_group_managers_abandon_instances_request_resource"
                        ][field]
                    ),
                ):
                    del request_init[
                        "instance_group_managers_abandon_instances_request_resource"
                    ][field][i][subfield]
            else:
                del request_init[
                    "instance_group_managers_abandon_instances_request_resource"
                ][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation(
            client_operation_id="client_operation_id_value",
            creation_timestamp="creation_timestamp_value",
            description="description_value",
            end_time="end_time_value",
            http_error_message="http_error_message_value",
            http_error_status_code=2374,
            id=205,
            insert_time="insert_time_value",
            kind="kind_value",
            name="name_value",
            operation_group_id="operation_group_id_value",
            operation_type="operation_type_value",
            progress=885,
            region="region_value",
            self_link="self_link_value",
            start_time="start_time_value",
            status=compute.Operation.Status.DONE,
            status_message="status_message_value",
            target_id=947,
            target_link="target_link_value",
            user="user_value",
            zone="zone_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.abandon_instances(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, extended_operation.ExtendedOperation)
    assert response.client_operation_id == "client_operation_id_value"
    assert response.creation_timestamp == "creation_timestamp_value"
    assert response.description == "description_value"
    assert response.end_time == "end_time_value"
    assert response.http_error_message == "http_error_message_value"
    assert response.http_error_status_code == 2374
    assert response.id == 205
    assert response.insert_time == "insert_time_value"
    assert response.kind == "kind_value"
    assert response.name == "name_value"
    assert response.operation_group_id == "operation_group_id_value"
    assert response.operation_type == "operation_type_value"
    assert response.progress == 885
    assert response.region == "region_value"
    assert response.self_link == "self_link_value"
    assert response.start_time == "start_time_value"
    assert response.status == compute.Operation.Status.DONE
    assert response.status_message == "status_message_value"
    assert response.target_id == 947
    assert response.target_link == "target_link_value"
    assert response.user == "user_value"
    assert response.zone == "zone_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_abandon_instances_rest_interceptors(null_interceptor):
    transport = transports.InstanceGroupManagersRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.InstanceGroupManagersRestInterceptor(),
    )
    client = InstanceGroupManagersClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor, "post_abandon_instances"
        ) as post,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor,
            "post_abandon_instances_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor, "pre_abandon_instances"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = compute.AbandonInstancesInstanceGroupManagerRequest.pb(
            compute.AbandonInstancesInstanceGroupManagerRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = compute.Operation.to_json(compute.Operation())
        req.return_value.content = return_value

        request = compute.AbandonInstancesInstanceGroupManagerRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = compute.Operation()
        post_with_metadata.return_value = compute.Operation(), metadata

        client.abandon_instances(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_aggregated_list_rest_bad_request(
    request_type=compute.AggregatedListInstanceGroupManagersRequest,
):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"project": "sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.aggregated_list(request)


@pytest.mark.parametrize(
    "request_type",
    [
        compute.AggregatedListInstanceGroupManagersRequest,
        dict,
    ],
)
def test_aggregated_list_rest_call_success(request_type):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"project": "sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.InstanceGroupManagerAggregatedList(
            id="id_value",
            kind="kind_value",
            next_page_token="next_page_token_value",
            self_link="self_link_value",
            unreachables=["unreachables_value"],
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = compute.InstanceGroupManagerAggregatedList.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.aggregated_list(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.AggregatedListPager)
    assert response.id == "id_value"
    assert response.kind == "kind_value"
    assert response.next_page_token == "next_page_token_value"
    assert response.self_link == "self_link_value"
    assert response.unreachables == ["unreachables_value"]


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_aggregated_list_rest_interceptors(null_interceptor):
    transport = transports.InstanceGroupManagersRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.InstanceGroupManagersRestInterceptor(),
    )
    client = InstanceGroupManagersClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor, "post_aggregated_list"
        ) as post,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor,
            "post_aggregated_list_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor, "pre_aggregated_list"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = compute.AggregatedListInstanceGroupManagersRequest.pb(
            compute.AggregatedListInstanceGroupManagersRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = compute.InstanceGroupManagerAggregatedList.to_json(
            compute.InstanceGroupManagerAggregatedList()
        )
        req.return_value.content = return_value

        request = compute.AggregatedListInstanceGroupManagersRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = compute.InstanceGroupManagerAggregatedList()
        post_with_metadata.return_value = (
            compute.InstanceGroupManagerAggregatedList(),
            metadata,
        )

        client.aggregated_list(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_apply_updates_to_instances_rest_bad_request(
    request_type=compute.ApplyUpdatesToInstancesInstanceGroupManagerRequest,
):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "zone": "sample2",
        "instance_group_manager": "sample3",
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.apply_updates_to_instances(request)


@pytest.mark.parametrize(
    "request_type",
    [
        compute.ApplyUpdatesToInstancesInstanceGroupManagerRequest,
        dict,
    ],
)
def test_apply_updates_to_instances_rest_call_success(request_type):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "zone": "sample2",
        "instance_group_manager": "sample3",
    }
    request_init["instance_group_managers_apply_updates_request_resource"] = {
        "all_instances": True,
        "instances": ["instances_value1", "instances_value2"],
        "minimal_action": "minimal_action_value",
        "most_disruptive_allowed_action": "most_disruptive_allowed_action_value",
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = compute.ApplyUpdatesToInstancesInstanceGroupManagerRequest.meta.fields[
        "instance_group_managers_apply_updates_request_resource"
    ]

    def get_message_fields(field):
        # Given a field which is a message (composite type), return a list with
        # all the fields of the message.
        # If the field is not a composite type, return an empty list.
        message_fields = []

        if hasattr(field, "message") and field.message:
            is_field_type_proto_plus_type = not hasattr(field.message, "DESCRIPTOR")

            if is_field_type_proto_plus_type:
                message_fields = field.message.meta.fields.values()
            # Add `# pragma: NO COVER` because there may not be any `*_pb2` field types
            else:  # pragma: NO COVER
                message_fields = field.message.DESCRIPTOR.fields
        return message_fields

    runtime_nested_fields = [
        (field.name, nested_field.name)
        for field in get_message_fields(test_field)
        for nested_field in get_message_fields(field)
    ]

    subfields_not_in_runtime = []

    # For each item in the sample request, create a list of sub fields which are not present at runtime
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for field, value in request_init[
        "instance_group_managers_apply_updates_request_resource"
    ].items():  # pragma: NO COVER
        result = None
        is_repeated = False
        # For repeated fields
        if isinstance(value, list) and len(value):
            is_repeated = True
            result = value[0]
        # For fields where the type is another message
        if isinstance(value, dict):
            result = value

        if result and hasattr(result, "keys"):
            for subfield in result.keys():
                if (field, subfield) not in runtime_nested_fields:
                    subfields_not_in_runtime.append(
                        {
                            "field": field,
                            "subfield": subfield,
                            "is_repeated": is_repeated,
                        }
                    )

    # Remove fields from the sample request which are not present in the runtime version of the dependency
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for subfield_to_delete in subfields_not_in_runtime:  # pragma: NO COVER
        field = subfield_to_delete.get("field")
        field_repeated = subfield_to_delete.get("is_repeated")
        subfield = subfield_to_delete.get("subfield")
        if subfield:
            if field_repeated:
                for i in range(
                    0,
                    len(
                        request_init[
                            "instance_group_managers_apply_updates_request_resource"
                        ][field]
                    ),
                ):
                    del request_init[
                        "instance_group_managers_apply_updates_request_resource"
                    ][field][i][subfield]
            else:
                del request_init[
                    "instance_group_managers_apply_updates_request_resource"
                ][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation(
            client_operation_id="client_operation_id_value",
            creation_timestamp="creation_timestamp_value",
            description="description_value",
            end_time="end_time_value",
            http_error_message="http_error_message_value",
            http_error_status_code=2374,
            id=205,
            insert_time="insert_time_value",
            kind="kind_value",
            name="name_value",
            operation_group_id="operation_group_id_value",
            operation_type="operation_type_value",
            progress=885,
            region="region_value",
            self_link="self_link_value",
            start_time="start_time_value",
            status=compute.Operation.Status.DONE,
            status_message="status_message_value",
            target_id=947,
            target_link="target_link_value",
            user="user_value",
            zone="zone_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.apply_updates_to_instances(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, extended_operation.ExtendedOperation)
    assert response.client_operation_id == "client_operation_id_value"
    assert response.creation_timestamp == "creation_timestamp_value"
    assert response.description == "description_value"
    assert response.end_time == "end_time_value"
    assert response.http_error_message == "http_error_message_value"
    assert response.http_error_status_code == 2374
    assert response.id == 205
    assert response.insert_time == "insert_time_value"
    assert response.kind == "kind_value"
    assert response.name == "name_value"
    assert response.operation_group_id == "operation_group_id_value"
    assert response.operation_type == "operation_type_value"
    assert response.progress == 885
    assert response.region == "region_value"
    assert response.self_link == "self_link_value"
    assert response.start_time == "start_time_value"
    assert response.status == compute.Operation.Status.DONE
    assert response.status_message == "status_message_value"
    assert response.target_id == 947
    assert response.target_link == "target_link_value"
    assert response.user == "user_value"
    assert response.zone == "zone_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_apply_updates_to_instances_rest_interceptors(null_interceptor):
    transport = transports.InstanceGroupManagersRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.InstanceGroupManagersRestInterceptor(),
    )
    client = InstanceGroupManagersClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor,
            "post_apply_updates_to_instances",
        ) as post,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor,
            "post_apply_updates_to_instances_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor,
            "pre_apply_updates_to_instances",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = compute.ApplyUpdatesToInstancesInstanceGroupManagerRequest.pb(
            compute.ApplyUpdatesToInstancesInstanceGroupManagerRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = compute.Operation.to_json(compute.Operation())
        req.return_value.content = return_value

        request = compute.ApplyUpdatesToInstancesInstanceGroupManagerRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = compute.Operation()
        post_with_metadata.return_value = compute.Operation(), metadata

        client.apply_updates_to_instances(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_create_instances_rest_bad_request(
    request_type=compute.CreateInstancesInstanceGroupManagerRequest,
):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "zone": "sample2",
        "instance_group_manager": "sample3",
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.create_instances(request)


@pytest.mark.parametrize(
    "request_type",
    [
        compute.CreateInstancesInstanceGroupManagerRequest,
        dict,
    ],
)
def test_create_instances_rest_call_success(request_type):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "zone": "sample2",
        "instance_group_manager": "sample3",
    }
    request_init["instance_group_managers_create_instances_request_resource"] = {
        "instances": [
            {
                "fingerprint": "fingerprint_value",
                "name": "name_value",
                "preserved_state": {
                    "disks": {},
                    "external_i_ps": {},
                    "internal_i_ps": {},
                    "metadata": {},
                },
                "status": "status_value",
            }
        ]
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = compute.CreateInstancesInstanceGroupManagerRequest.meta.fields[
        "instance_group_managers_create_instances_request_resource"
    ]

    def get_message_fields(field):
        # Given a field which is a message (composite type), return a list with
        # all the fields of the message.
        # If the field is not a composite type, return an empty list.
        message_fields = []

        if hasattr(field, "message") and field.message:
            is_field_type_proto_plus_type = not hasattr(field.message, "DESCRIPTOR")

            if is_field_type_proto_plus_type:
                message_fields = field.message.meta.fields.values()
            # Add `# pragma: NO COVER` because there may not be any `*_pb2` field types
            else:  # pragma: NO COVER
                message_fields = field.message.DESCRIPTOR.fields
        return message_fields

    runtime_nested_fields = [
        (field.name, nested_field.name)
        for field in get_message_fields(test_field)
        for nested_field in get_message_fields(field)
    ]

    subfields_not_in_runtime = []

    # For each item in the sample request, create a list of sub fields which are not present at runtime
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for field, value in request_init[
        "instance_group_managers_create_instances_request_resource"
    ].items():  # pragma: NO COVER
        result = None
        is_repeated = False
        # For repeated fields
        if isinstance(value, list) and len(value):
            is_repeated = True
            result = value[0]
        # For fields where the type is another message
        if isinstance(value, dict):
            result = value

        if result and hasattr(result, "keys"):
            for subfield in result.keys():
                if (field, subfield) not in runtime_nested_fields:
                    subfields_not_in_runtime.append(
                        {
                            "field": field,
                            "subfield": subfield,
                            "is_repeated": is_repeated,
                        }
                    )

    # Remove fields from the sample request which are not present in the runtime version of the dependency
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for subfield_to_delete in subfields_not_in_runtime:  # pragma: NO COVER
        field = subfield_to_delete.get("field")
        field_repeated = subfield_to_delete.get("is_repeated")
        subfield = subfield_to_delete.get("subfield")
        if subfield:
            if field_repeated:
                for i in range(
                    0,
                    len(
                        request_init[
                            "instance_group_managers_create_instances_request_resource"
                        ][field]
                    ),
                ):
                    del request_init[
                        "instance_group_managers_create_instances_request_resource"
                    ][field][i][subfield]
            else:
                del request_init[
                    "instance_group_managers_create_instances_request_resource"
                ][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation(
            client_operation_id="client_operation_id_value",
            creation_timestamp="creation_timestamp_value",
            description="description_value",
            end_time="end_time_value",
            http_error_message="http_error_message_value",
            http_error_status_code=2374,
            id=205,
            insert_time="insert_time_value",
            kind="kind_value",
            name="name_value",
            operation_group_id="operation_group_id_value",
            operation_type="operation_type_value",
            progress=885,
            region="region_value",
            self_link="self_link_value",
            start_time="start_time_value",
            status=compute.Operation.Status.DONE,
            status_message="status_message_value",
            target_id=947,
            target_link="target_link_value",
            user="user_value",
            zone="zone_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.create_instances(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, extended_operation.ExtendedOperation)
    assert response.client_operation_id == "client_operation_id_value"
    assert response.creation_timestamp == "creation_timestamp_value"
    assert response.description == "description_value"
    assert response.end_time == "end_time_value"
    assert response.http_error_message == "http_error_message_value"
    assert response.http_error_status_code == 2374
    assert response.id == 205
    assert response.insert_time == "insert_time_value"
    assert response.kind == "kind_value"
    assert response.name == "name_value"
    assert response.operation_group_id == "operation_group_id_value"
    assert response.operation_type == "operation_type_value"
    assert response.progress == 885
    assert response.region == "region_value"
    assert response.self_link == "self_link_value"
    assert response.start_time == "start_time_value"
    assert response.status == compute.Operation.Status.DONE
    assert response.status_message == "status_message_value"
    assert response.target_id == 947
    assert response.target_link == "target_link_value"
    assert response.user == "user_value"
    assert response.zone == "zone_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_create_instances_rest_interceptors(null_interceptor):
    transport = transports.InstanceGroupManagersRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.InstanceGroupManagersRestInterceptor(),
    )
    client = InstanceGroupManagersClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor, "post_create_instances"
        ) as post,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor,
            "post_create_instances_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor, "pre_create_instances"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = compute.CreateInstancesInstanceGroupManagerRequest.pb(
            compute.CreateInstancesInstanceGroupManagerRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = compute.Operation.to_json(compute.Operation())
        req.return_value.content = return_value

        request = compute.CreateInstancesInstanceGroupManagerRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = compute.Operation()
        post_with_metadata.return_value = compute.Operation(), metadata

        client.create_instances(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_delete_rest_bad_request(
    request_type=compute.DeleteInstanceGroupManagerRequest,
):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "zone": "sample2",
        "instance_group_manager": "sample3",
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.delete(request)


@pytest.mark.parametrize(
    "request_type",
    [
        compute.DeleteInstanceGroupManagerRequest,
        dict,
    ],
)
def test_delete_rest_call_success(request_type):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "zone": "sample2",
        "instance_group_manager": "sample3",
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation(
            client_operation_id="client_operation_id_value",
            creation_timestamp="creation_timestamp_value",
            description="description_value",
            end_time="end_time_value",
            http_error_message="http_error_message_value",
            http_error_status_code=2374,
            id=205,
            insert_time="insert_time_value",
            kind="kind_value",
            name="name_value",
            operation_group_id="operation_group_id_value",
            operation_type="operation_type_value",
            progress=885,
            region="region_value",
            self_link="self_link_value",
            start_time="start_time_value",
            status=compute.Operation.Status.DONE,
            status_message="status_message_value",
            target_id=947,
            target_link="target_link_value",
            user="user_value",
            zone="zone_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.delete(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, extended_operation.ExtendedOperation)
    assert response.client_operation_id == "client_operation_id_value"
    assert response.creation_timestamp == "creation_timestamp_value"
    assert response.description == "description_value"
    assert response.end_time == "end_time_value"
    assert response.http_error_message == "http_error_message_value"
    assert response.http_error_status_code == 2374
    assert response.id == 205
    assert response.insert_time == "insert_time_value"
    assert response.kind == "kind_value"
    assert response.name == "name_value"
    assert response.operation_group_id == "operation_group_id_value"
    assert response.operation_type == "operation_type_value"
    assert response.progress == 885
    assert response.region == "region_value"
    assert response.self_link == "self_link_value"
    assert response.start_time == "start_time_value"
    assert response.status == compute.Operation.Status.DONE
    assert response.status_message == "status_message_value"
    assert response.target_id == 947
    assert response.target_link == "target_link_value"
    assert response.user == "user_value"
    assert response.zone == "zone_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_delete_rest_interceptors(null_interceptor):
    transport = transports.InstanceGroupManagersRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.InstanceGroupManagersRestInterceptor(),
    )
    client = InstanceGroupManagersClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor, "post_delete"
        ) as post,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor, "post_delete_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor, "pre_delete"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = compute.DeleteInstanceGroupManagerRequest.pb(
            compute.DeleteInstanceGroupManagerRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = compute.Operation.to_json(compute.Operation())
        req.return_value.content = return_value

        request = compute.DeleteInstanceGroupManagerRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = compute.Operation()
        post_with_metadata.return_value = compute.Operation(), metadata

        client.delete(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_delete_instances_rest_bad_request(
    request_type=compute.DeleteInstancesInstanceGroupManagerRequest,
):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "zone": "sample2",
        "instance_group_manager": "sample3",
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.delete_instances(request)


@pytest.mark.parametrize(
    "request_type",
    [
        compute.DeleteInstancesInstanceGroupManagerRequest,
        dict,
    ],
)
def test_delete_instances_rest_call_success(request_type):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "zone": "sample2",
        "instance_group_manager": "sample3",
    }
    request_init["instance_group_managers_delete_instances_request_resource"] = {
        "instances": ["instances_value1", "instances_value2"],
        "skip_instances_on_validation_error": True,
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = compute.DeleteInstancesInstanceGroupManagerRequest.meta.fields[
        "instance_group_managers_delete_instances_request_resource"
    ]

    def get_message_fields(field):
        # Given a field which is a message (composite type), return a list with
        # all the fields of the message.
        # If the field is not a composite type, return an empty list.
        message_fields = []

        if hasattr(field, "message") and field.message:
            is_field_type_proto_plus_type = not hasattr(field.message, "DESCRIPTOR")

            if is_field_type_proto_plus_type:
                message_fields = field.message.meta.fields.values()
            # Add `# pragma: NO COVER` because there may not be any `*_pb2` field types
            else:  # pragma: NO COVER
                message_fields = field.message.DESCRIPTOR.fields
        return message_fields

    runtime_nested_fields = [
        (field.name, nested_field.name)
        for field in get_message_fields(test_field)
        for nested_field in get_message_fields(field)
    ]

    subfields_not_in_runtime = []

    # For each item in the sample request, create a list of sub fields which are not present at runtime
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for field, value in request_init[
        "instance_group_managers_delete_instances_request_resource"
    ].items():  # pragma: NO COVER
        result = None
        is_repeated = False
        # For repeated fields
        if isinstance(value, list) and len(value):
            is_repeated = True
            result = value[0]
        # For fields where the type is another message
        if isinstance(value, dict):
            result = value

        if result and hasattr(result, "keys"):
            for subfield in result.keys():
                if (field, subfield) not in runtime_nested_fields:
                    subfields_not_in_runtime.append(
                        {
                            "field": field,
                            "subfield": subfield,
                            "is_repeated": is_repeated,
                        }
                    )

    # Remove fields from the sample request which are not present in the runtime version of the dependency
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for subfield_to_delete in subfields_not_in_runtime:  # pragma: NO COVER
        field = subfield_to_delete.get("field")
        field_repeated = subfield_to_delete.get("is_repeated")
        subfield = subfield_to_delete.get("subfield")
        if subfield:
            if field_repeated:
                for i in range(
                    0,
                    len(
                        request_init[
                            "instance_group_managers_delete_instances_request_resource"
                        ][field]
                    ),
                ):
                    del request_init[
                        "instance_group_managers_delete_instances_request_resource"
                    ][field][i][subfield]
            else:
                del request_init[
                    "instance_group_managers_delete_instances_request_resource"
                ][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation(
            client_operation_id="client_operation_id_value",
            creation_timestamp="creation_timestamp_value",
            description="description_value",
            end_time="end_time_value",
            http_error_message="http_error_message_value",
            http_error_status_code=2374,
            id=205,
            insert_time="insert_time_value",
            kind="kind_value",
            name="name_value",
            operation_group_id="operation_group_id_value",
            operation_type="operation_type_value",
            progress=885,
            region="region_value",
            self_link="self_link_value",
            start_time="start_time_value",
            status=compute.Operation.Status.DONE,
            status_message="status_message_value",
            target_id=947,
            target_link="target_link_value",
            user="user_value",
            zone="zone_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.delete_instances(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, extended_operation.ExtendedOperation)
    assert response.client_operation_id == "client_operation_id_value"
    assert response.creation_timestamp == "creation_timestamp_value"
    assert response.description == "description_value"
    assert response.end_time == "end_time_value"
    assert response.http_error_message == "http_error_message_value"
    assert response.http_error_status_code == 2374
    assert response.id == 205
    assert response.insert_time == "insert_time_value"
    assert response.kind == "kind_value"
    assert response.name == "name_value"
    assert response.operation_group_id == "operation_group_id_value"
    assert response.operation_type == "operation_type_value"
    assert response.progress == 885
    assert response.region == "region_value"
    assert response.self_link == "self_link_value"
    assert response.start_time == "start_time_value"
    assert response.status == compute.Operation.Status.DONE
    assert response.status_message == "status_message_value"
    assert response.target_id == 947
    assert response.target_link == "target_link_value"
    assert response.user == "user_value"
    assert response.zone == "zone_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_delete_instances_rest_interceptors(null_interceptor):
    transport = transports.InstanceGroupManagersRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.InstanceGroupManagersRestInterceptor(),
    )
    client = InstanceGroupManagersClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor, "post_delete_instances"
        ) as post,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor,
            "post_delete_instances_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor, "pre_delete_instances"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = compute.DeleteInstancesInstanceGroupManagerRequest.pb(
            compute.DeleteInstancesInstanceGroupManagerRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = compute.Operation.to_json(compute.Operation())
        req.return_value.content = return_value

        request = compute.DeleteInstancesInstanceGroupManagerRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = compute.Operation()
        post_with_metadata.return_value = compute.Operation(), metadata

        client.delete_instances(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_delete_per_instance_configs_rest_bad_request(
    request_type=compute.DeletePerInstanceConfigsInstanceGroupManagerRequest,
):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "zone": "sample2",
        "instance_group_manager": "sample3",
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.delete_per_instance_configs(request)


@pytest.mark.parametrize(
    "request_type",
    [
        compute.DeletePerInstanceConfigsInstanceGroupManagerRequest,
        dict,
    ],
)
def test_delete_per_instance_configs_rest_call_success(request_type):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "zone": "sample2",
        "instance_group_manager": "sample3",
    }
    request_init["instance_group_managers_delete_per_instance_configs_req_resource"] = {
        "names": ["names_value1", "names_value2"]
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = (
        compute.DeletePerInstanceConfigsInstanceGroupManagerRequest.meta.fields[
            "instance_group_managers_delete_per_instance_configs_req_resource"
        ]
    )

    def get_message_fields(field):
        # Given a field which is a message (composite type), return a list with
        # all the fields of the message.
        # If the field is not a composite type, return an empty list.
        message_fields = []

        if hasattr(field, "message") and field.message:
            is_field_type_proto_plus_type = not hasattr(field.message, "DESCRIPTOR")

            if is_field_type_proto_plus_type:
                message_fields = field.message.meta.fields.values()
            # Add `# pragma: NO COVER` because there may not be any `*_pb2` field types
            else:  # pragma: NO COVER
                message_fields = field.message.DESCRIPTOR.fields
        return message_fields

    runtime_nested_fields = [
        (field.name, nested_field.name)
        for field in get_message_fields(test_field)
        for nested_field in get_message_fields(field)
    ]

    subfields_not_in_runtime = []

    # For each item in the sample request, create a list of sub fields which are not present at runtime
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for field, value in request_init[
        "instance_group_managers_delete_per_instance_configs_req_resource"
    ].items():  # pragma: NO COVER
        result = None
        is_repeated = False
        # For repeated fields
        if isinstance(value, list) and len(value):
            is_repeated = True
            result = value[0]
        # For fields where the type is another message
        if isinstance(value, dict):
            result = value

        if result and hasattr(result, "keys"):
            for subfield in result.keys():
                if (field, subfield) not in runtime_nested_fields:
                    subfields_not_in_runtime.append(
                        {
                            "field": field,
                            "subfield": subfield,
                            "is_repeated": is_repeated,
                        }
                    )

    # Remove fields from the sample request which are not present in the runtime version of the dependency
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for subfield_to_delete in subfields_not_in_runtime:  # pragma: NO COVER
        field = subfield_to_delete.get("field")
        field_repeated = subfield_to_delete.get("is_repeated")
        subfield = subfield_to_delete.get("subfield")
        if subfield:
            if field_repeated:
                for i in range(
                    0,
                    len(
                        request_init[
                            "instance_group_managers_delete_per_instance_configs_req_resource"
                        ][field]
                    ),
                ):
                    del request_init[
                        "instance_group_managers_delete_per_instance_configs_req_resource"
                    ][field][i][subfield]
            else:
                del request_init[
                    "instance_group_managers_delete_per_instance_configs_req_resource"
                ][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation(
            client_operation_id="client_operation_id_value",
            creation_timestamp="creation_timestamp_value",
            description="description_value",
            end_time="end_time_value",
            http_error_message="http_error_message_value",
            http_error_status_code=2374,
            id=205,
            insert_time="insert_time_value",
            kind="kind_value",
            name="name_value",
            operation_group_id="operation_group_id_value",
            operation_type="operation_type_value",
            progress=885,
            region="region_value",
            self_link="self_link_value",
            start_time="start_time_value",
            status=compute.Operation.Status.DONE,
            status_message="status_message_value",
            target_id=947,
            target_link="target_link_value",
            user="user_value",
            zone="zone_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.delete_per_instance_configs(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, extended_operation.ExtendedOperation)
    assert response.client_operation_id == "client_operation_id_value"
    assert response.creation_timestamp == "creation_timestamp_value"
    assert response.description == "description_value"
    assert response.end_time == "end_time_value"
    assert response.http_error_message == "http_error_message_value"
    assert response.http_error_status_code == 2374
    assert response.id == 205
    assert response.insert_time == "insert_time_value"
    assert response.kind == "kind_value"
    assert response.name == "name_value"
    assert response.operation_group_id == "operation_group_id_value"
    assert response.operation_type == "operation_type_value"
    assert response.progress == 885
    assert response.region == "region_value"
    assert response.self_link == "self_link_value"
    assert response.start_time == "start_time_value"
    assert response.status == compute.Operation.Status.DONE
    assert response.status_message == "status_message_value"
    assert response.target_id == 947
    assert response.target_link == "target_link_value"
    assert response.user == "user_value"
    assert response.zone == "zone_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_delete_per_instance_configs_rest_interceptors(null_interceptor):
    transport = transports.InstanceGroupManagersRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.InstanceGroupManagersRestInterceptor(),
    )
    client = InstanceGroupManagersClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor,
            "post_delete_per_instance_configs",
        ) as post,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor,
            "post_delete_per_instance_configs_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor,
            "pre_delete_per_instance_configs",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = compute.DeletePerInstanceConfigsInstanceGroupManagerRequest.pb(
            compute.DeletePerInstanceConfigsInstanceGroupManagerRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = compute.Operation.to_json(compute.Operation())
        req.return_value.content = return_value

        request = compute.DeletePerInstanceConfigsInstanceGroupManagerRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = compute.Operation()
        post_with_metadata.return_value = compute.Operation(), metadata

        client.delete_per_instance_configs(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_get_rest_bad_request(request_type=compute.GetInstanceGroupManagerRequest):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "zone": "sample2",
        "instance_group_manager": "sample3",
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.get(request)


@pytest.mark.parametrize(
    "request_type",
    [
        compute.GetInstanceGroupManagerRequest,
        dict,
    ],
)
def test_get_rest_call_success(request_type):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "zone": "sample2",
        "instance_group_manager": "sample3",
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.InstanceGroupManager(
            base_instance_name="base_instance_name_value",
            creation_timestamp="creation_timestamp_value",
            description="description_value",
            fingerprint="fingerprint_value",
            id=205,
            instance_group="instance_group_value",
            instance_template="instance_template_value",
            kind="kind_value",
            list_managed_instances_results="list_managed_instances_results_value",
            name="name_value",
            region="region_value",
            satisfies_pzi=True,
            satisfies_pzs=True,
            self_link="self_link_value",
            target_pools=["target_pools_value"],
            target_size=1185,
            target_stopped_size=2047,
            target_suspended_size=2251,
            zone="zone_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = compute.InstanceGroupManager.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, compute.InstanceGroupManager)
    assert response.base_instance_name == "base_instance_name_value"
    assert response.creation_timestamp == "creation_timestamp_value"
    assert response.description == "description_value"
    assert response.fingerprint == "fingerprint_value"
    assert response.id == 205
    assert response.instance_group == "instance_group_value"
    assert response.instance_template == "instance_template_value"
    assert response.kind == "kind_value"
    assert (
        response.list_managed_instances_results
        == "list_managed_instances_results_value"
    )
    assert response.name == "name_value"
    assert response.region == "region_value"
    assert response.satisfies_pzi is True
    assert response.satisfies_pzs is True
    assert response.self_link == "self_link_value"
    assert response.target_pools == ["target_pools_value"]
    assert response.target_size == 1185
    assert response.target_stopped_size == 2047
    assert response.target_suspended_size == 2251
    assert response.zone == "zone_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_rest_interceptors(null_interceptor):
    transport = transports.InstanceGroupManagersRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.InstanceGroupManagersRestInterceptor(),
    )
    client = InstanceGroupManagersClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor, "post_get"
        ) as post,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor, "post_get_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor, "pre_get"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = compute.GetInstanceGroupManagerRequest.pb(
            compute.GetInstanceGroupManagerRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = compute.InstanceGroupManager.to_json(
            compute.InstanceGroupManager()
        )
        req.return_value.content = return_value

        request = compute.GetInstanceGroupManagerRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = compute.InstanceGroupManager()
        post_with_metadata.return_value = compute.InstanceGroupManager(), metadata

        client.get(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_insert_rest_bad_request(
    request_type=compute.InsertInstanceGroupManagerRequest,
):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"project": "sample1", "zone": "sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.insert(request)


@pytest.mark.parametrize(
    "request_type",
    [
        compute.InsertInstanceGroupManagerRequest,
        dict,
    ],
)
def test_insert_rest_call_success(request_type):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"project": "sample1", "zone": "sample2"}
    request_init["instance_group_manager_resource"] = {
        "all_instances_config": {
            "properties": {"expose_host_topology": True, "labels": {}, "metadata": {}}
        },
        "auto_healing_policies": [
            {"health_check": "health_check_value", "initial_delay_sec": 1778}
        ],
        "base_instance_name": "base_instance_name_value",
        "creation_timestamp": "creation_timestamp_value",
        "current_actions": {
            "abandoning": 1041,
            "creating": 845,
            "creating_without_retries": 2589,
            "deleting": 844,
            "none": 432,
            "recreating": 1060,
            "refreshing": 1069,
            "restarting": 1091,
            "resuming": 874,
            "starting": 876,
            "stopping": 884,
            "suspending": 1088,
            "verifying": 979,
        },
        "description": "description_value",
        "distribution_policy": {
            "target_shape": "target_shape_value",
            "zones": [{"zone": "zone_value"}],
        },
        "fingerprint": "fingerprint_value",
        "id": 205,
        "instance_flexibility_policy": {"instance_selections": {}},
        "instance_group": "instance_group_value",
        "instance_lifecycle_policy": {
            "default_action_on_failure": "default_action_on_failure_value",
            "force_update_on_repair": "force_update_on_repair_value",
            "on_failed_health_check": "on_failed_health_check_value",
            "on_repair": {"allow_changing_zone": "allow_changing_zone_value"},
        },
        "instance_template": "instance_template_value",
        "kind": "kind_value",
        "list_managed_instances_results": "list_managed_instances_results_value",
        "name": "name_value",
        "named_ports": [{"name": "name_value", "port": 453}],
        "region": "region_value",
        "resource_policies": {"workload_policy": "workload_policy_value"},
        "satisfies_pzi": True,
        "satisfies_pzs": True,
        "self_link": "self_link_value",
        "standby_policy": {"initial_delay_sec": 1778, "mode": "mode_value"},
        "stateful_policy": {
            "preserved_state": {"disks": {}, "external_i_ps": {}, "internal_i_ps": {}}
        },
        "status": {
            "all_instances_config": {
                "current_revision": "current_revision_value",
                "effective": True,
            },
            "applied_accelerator_topologies": [
                {
                    "accelerator_topology": "accelerator_topology_value",
                    "state": "state_value",
                    "state_details": {
                        "error": {
                            "errors": [
                                {
                                    "code": "code_value",
                                    "error_details": [
                                        {
                                            "error_info": {
                                                "domain": "domain_value",
                                                "metadatas": {},
                                                "reason": "reason_value",
                                            },
                                            "help_": {
                                                "links": [
                                                    {
                                                        "description": "description_value",
                                                        "url": "url_value",
                                                    }
                                                ]
                                            },
                                            "localized_message": {
                                                "locale": "locale_value",
                                                "message": "message_value",
                                            },
                                            "quota_info": {
                                                "dimensions": {},
                                                "future_limit": 0.1305,
                                                "limit": 0.543,
                                                "limit_name": "limit_name_value",
                                                "metric_name": "metric_name_value",
                                                "rollout_status": "rollout_status_value",
                                            },
                                        }
                                    ],
                                    "location": "location_value",
                                    "message": "message_value",
                                }
                            ]
                        },
                        "timestamp": "timestamp_value",
                    },
                }
            ],
            "autoscaler": "autoscaler_value",
            "bulk_instance_operation": {
                "in_progress": True,
                "last_progress_check": {"error": {}, "timestamp": "timestamp_value"},
            },
            "current_instance_statuses": {
                "deprovisioning": 1520,
                "non_existent": 1310,
                "pending": 741,
                "pending_stop": 1290,
                "provisioning": 1319,
                "repairing": 961,
                "running": 769,
                "staging": 749,
                "stopped": 767,
                "stopping": 884,
                "suspended": 971,
                "suspending": 1088,
                "terminated": 1069,
            },
            "is_stable": True,
            "stateful": {
                "has_stateful_config": True,
                "per_instance_configs": {"all_effective": True},
            },
            "version_target": {"is_reached": True},
        },
        "target_pools": ["target_pools_value1", "target_pools_value2"],
        "target_size": 1185,
        "target_size_policy": {"mode": "mode_value"},
        "target_stopped_size": 2047,
        "target_suspended_size": 2251,
        "update_policy": {
            "instance_redistribution_type": "instance_redistribution_type_value",
            "max_surge": {"calculated": 1042, "fixed": 528, "percent": 753},
            "max_unavailable": {},
            "minimal_action": "minimal_action_value",
            "most_disruptive_allowed_action": "most_disruptive_allowed_action_value",
            "replacement_method": "replacement_method_value",
            "type_": "type__value",
        },
        "versions": [
            {
                "instance_template": "instance_template_value",
                "name": "name_value",
                "target_size": {},
            }
        ],
        "zone": "zone_value",
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = compute.InsertInstanceGroupManagerRequest.meta.fields[
        "instance_group_manager_resource"
    ]

    def get_message_fields(field):
        # Given a field which is a message (composite type), return a list with
        # all the fields of the message.
        # If the field is not a composite type, return an empty list.
        message_fields = []

        if hasattr(field, "message") and field.message:
            is_field_type_proto_plus_type = not hasattr(field.message, "DESCRIPTOR")

            if is_field_type_proto_plus_type:
                message_fields = field.message.meta.fields.values()
            # Add `# pragma: NO COVER` because there may not be any `*_pb2` field types
            else:  # pragma: NO COVER
                message_fields = field.message.DESCRIPTOR.fields
        return message_fields

    runtime_nested_fields = [
        (field.name, nested_field.name)
        for field in get_message_fields(test_field)
        for nested_field in get_message_fields(field)
    ]

    subfields_not_in_runtime = []

    # For each item in the sample request, create a list of sub fields which are not present at runtime
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for field, value in request_init[
        "instance_group_manager_resource"
    ].items():  # pragma: NO COVER
        result = None
        is_repeated = False
        # For repeated fields
        if isinstance(value, list) and len(value):
            is_repeated = True
            result = value[0]
        # For fields where the type is another message
        if isinstance(value, dict):
            result = value

        if result and hasattr(result, "keys"):
            for subfield in result.keys():
                if (field, subfield) not in runtime_nested_fields:
                    subfields_not_in_runtime.append(
                        {
                            "field": field,
                            "subfield": subfield,
                            "is_repeated": is_repeated,
                        }
                    )

    # Remove fields from the sample request which are not present in the runtime version of the dependency
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for subfield_to_delete in subfields_not_in_runtime:  # pragma: NO COVER
        field = subfield_to_delete.get("field")
        field_repeated = subfield_to_delete.get("is_repeated")
        subfield = subfield_to_delete.get("subfield")
        if subfield:
            if field_repeated:
                for i in range(
                    0, len(request_init["instance_group_manager_resource"][field])
                ):
                    del request_init["instance_group_manager_resource"][field][i][
                        subfield
                    ]
            else:
                del request_init["instance_group_manager_resource"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation(
            client_operation_id="client_operation_id_value",
            creation_timestamp="creation_timestamp_value",
            description="description_value",
            end_time="end_time_value",
            http_error_message="http_error_message_value",
            http_error_status_code=2374,
            id=205,
            insert_time="insert_time_value",
            kind="kind_value",
            name="name_value",
            operation_group_id="operation_group_id_value",
            operation_type="operation_type_value",
            progress=885,
            region="region_value",
            self_link="self_link_value",
            start_time="start_time_value",
            status=compute.Operation.Status.DONE,
            status_message="status_message_value",
            target_id=947,
            target_link="target_link_value",
            user="user_value",
            zone="zone_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.insert(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, extended_operation.ExtendedOperation)
    assert response.client_operation_id == "client_operation_id_value"
    assert response.creation_timestamp == "creation_timestamp_value"
    assert response.description == "description_value"
    assert response.end_time == "end_time_value"
    assert response.http_error_message == "http_error_message_value"
    assert response.http_error_status_code == 2374
    assert response.id == 205
    assert response.insert_time == "insert_time_value"
    assert response.kind == "kind_value"
    assert response.name == "name_value"
    assert response.operation_group_id == "operation_group_id_value"
    assert response.operation_type == "operation_type_value"
    assert response.progress == 885
    assert response.region == "region_value"
    assert response.self_link == "self_link_value"
    assert response.start_time == "start_time_value"
    assert response.status == compute.Operation.Status.DONE
    assert response.status_message == "status_message_value"
    assert response.target_id == 947
    assert response.target_link == "target_link_value"
    assert response.user == "user_value"
    assert response.zone == "zone_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_insert_rest_interceptors(null_interceptor):
    transport = transports.InstanceGroupManagersRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.InstanceGroupManagersRestInterceptor(),
    )
    client = InstanceGroupManagersClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor, "post_insert"
        ) as post,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor, "post_insert_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor, "pre_insert"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = compute.InsertInstanceGroupManagerRequest.pb(
            compute.InsertInstanceGroupManagerRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = compute.Operation.to_json(compute.Operation())
        req.return_value.content = return_value

        request = compute.InsertInstanceGroupManagerRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = compute.Operation()
        post_with_metadata.return_value = compute.Operation(), metadata

        client.insert(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_rest_bad_request(request_type=compute.ListInstanceGroupManagersRequest):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"project": "sample1", "zone": "sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.list(request)


@pytest.mark.parametrize(
    "request_type",
    [
        compute.ListInstanceGroupManagersRequest,
        dict,
    ],
)
def test_list_rest_call_success(request_type):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"project": "sample1", "zone": "sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.InstanceGroupManagerList(
            id="id_value",
            kind="kind_value",
            next_page_token="next_page_token_value",
            self_link="self_link_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = compute.InstanceGroupManagerList.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListPager)
    assert response.id == "id_value"
    assert response.kind == "kind_value"
    assert response.next_page_token == "next_page_token_value"
    assert response.self_link == "self_link_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_rest_interceptors(null_interceptor):
    transport = transports.InstanceGroupManagersRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.InstanceGroupManagersRestInterceptor(),
    )
    client = InstanceGroupManagersClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor, "post_list"
        ) as post,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor, "post_list_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor, "pre_list"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = compute.ListInstanceGroupManagersRequest.pb(
            compute.ListInstanceGroupManagersRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = compute.InstanceGroupManagerList.to_json(
            compute.InstanceGroupManagerList()
        )
        req.return_value.content = return_value

        request = compute.ListInstanceGroupManagersRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = compute.InstanceGroupManagerList()
        post_with_metadata.return_value = compute.InstanceGroupManagerList(), metadata

        client.list(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_errors_rest_bad_request(
    request_type=compute.ListErrorsInstanceGroupManagersRequest,
):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "zone": "sample2",
        "instance_group_manager": "sample3",
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.list_errors(request)


@pytest.mark.parametrize(
    "request_type",
    [
        compute.ListErrorsInstanceGroupManagersRequest,
        dict,
    ],
)
def test_list_errors_rest_call_success(request_type):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "zone": "sample2",
        "instance_group_manager": "sample3",
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.InstanceGroupManagersListErrorsResponse(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = compute.InstanceGroupManagersListErrorsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_errors(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListErrorsPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_errors_rest_interceptors(null_interceptor):
    transport = transports.InstanceGroupManagersRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.InstanceGroupManagersRestInterceptor(),
    )
    client = InstanceGroupManagersClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor, "post_list_errors"
        ) as post,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor,
            "post_list_errors_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor, "pre_list_errors"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = compute.ListErrorsInstanceGroupManagersRequest.pb(
            compute.ListErrorsInstanceGroupManagersRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = compute.InstanceGroupManagersListErrorsResponse.to_json(
            compute.InstanceGroupManagersListErrorsResponse()
        )
        req.return_value.content = return_value

        request = compute.ListErrorsInstanceGroupManagersRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = compute.InstanceGroupManagersListErrorsResponse()
        post_with_metadata.return_value = (
            compute.InstanceGroupManagersListErrorsResponse(),
            metadata,
        )

        client.list_errors(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_managed_instances_rest_bad_request(
    request_type=compute.ListManagedInstancesInstanceGroupManagersRequest,
):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "zone": "sample2",
        "instance_group_manager": "sample3",
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.list_managed_instances(request)


@pytest.mark.parametrize(
    "request_type",
    [
        compute.ListManagedInstancesInstanceGroupManagersRequest,
        dict,
    ],
)
def test_list_managed_instances_rest_call_success(request_type):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "zone": "sample2",
        "instance_group_manager": "sample3",
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.InstanceGroupManagersListManagedInstancesResponse(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = compute.InstanceGroupManagersListManagedInstancesResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_managed_instances(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListManagedInstancesPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_managed_instances_rest_interceptors(null_interceptor):
    transport = transports.InstanceGroupManagersRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.InstanceGroupManagersRestInterceptor(),
    )
    client = InstanceGroupManagersClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor,
            "post_list_managed_instances",
        ) as post,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor,
            "post_list_managed_instances_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor,
            "pre_list_managed_instances",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = compute.ListManagedInstancesInstanceGroupManagersRequest.pb(
            compute.ListManagedInstancesInstanceGroupManagersRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = (
            compute.InstanceGroupManagersListManagedInstancesResponse.to_json(
                compute.InstanceGroupManagersListManagedInstancesResponse()
            )
        )
        req.return_value.content = return_value

        request = compute.ListManagedInstancesInstanceGroupManagersRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = compute.InstanceGroupManagersListManagedInstancesResponse()
        post_with_metadata.return_value = (
            compute.InstanceGroupManagersListManagedInstancesResponse(),
            metadata,
        )

        client.list_managed_instances(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_per_instance_configs_rest_bad_request(
    request_type=compute.ListPerInstanceConfigsInstanceGroupManagersRequest,
):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "zone": "sample2",
        "instance_group_manager": "sample3",
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.list_per_instance_configs(request)


@pytest.mark.parametrize(
    "request_type",
    [
        compute.ListPerInstanceConfigsInstanceGroupManagersRequest,
        dict,
    ],
)
def test_list_per_instance_configs_rest_call_success(request_type):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "zone": "sample2",
        "instance_group_manager": "sample3",
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.InstanceGroupManagersListPerInstanceConfigsResp(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = compute.InstanceGroupManagersListPerInstanceConfigsResp.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_per_instance_configs(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListPerInstanceConfigsPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_per_instance_configs_rest_interceptors(null_interceptor):
    transport = transports.InstanceGroupManagersRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.InstanceGroupManagersRestInterceptor(),
    )
    client = InstanceGroupManagersClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor,
            "post_list_per_instance_configs",
        ) as post,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor,
            "post_list_per_instance_configs_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor,
            "pre_list_per_instance_configs",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = compute.ListPerInstanceConfigsInstanceGroupManagersRequest.pb(
            compute.ListPerInstanceConfigsInstanceGroupManagersRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = compute.InstanceGroupManagersListPerInstanceConfigsResp.to_json(
            compute.InstanceGroupManagersListPerInstanceConfigsResp()
        )
        req.return_value.content = return_value

        request = compute.ListPerInstanceConfigsInstanceGroupManagersRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = compute.InstanceGroupManagersListPerInstanceConfigsResp()
        post_with_metadata.return_value = (
            compute.InstanceGroupManagersListPerInstanceConfigsResp(),
            metadata,
        )

        client.list_per_instance_configs(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_patch_rest_bad_request(request_type=compute.PatchInstanceGroupManagerRequest):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "zone": "sample2",
        "instance_group_manager": "sample3",
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.patch(request)


@pytest.mark.parametrize(
    "request_type",
    [
        compute.PatchInstanceGroupManagerRequest,
        dict,
    ],
)
def test_patch_rest_call_success(request_type):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "zone": "sample2",
        "instance_group_manager": "sample3",
    }
    request_init["instance_group_manager_resource"] = {
        "all_instances_config": {
            "properties": {"expose_host_topology": True, "labels": {}, "metadata": {}}
        },
        "auto_healing_policies": [
            {"health_check": "health_check_value", "initial_delay_sec": 1778}
        ],
        "base_instance_name": "base_instance_name_value",
        "creation_timestamp": "creation_timestamp_value",
        "current_actions": {
            "abandoning": 1041,
            "creating": 845,
            "creating_without_retries": 2589,
            "deleting": 844,
            "none": 432,
            "recreating": 1060,
            "refreshing": 1069,
            "restarting": 1091,
            "resuming": 874,
            "starting": 876,
            "stopping": 884,
            "suspending": 1088,
            "verifying": 979,
        },
        "description": "description_value",
        "distribution_policy": {
            "target_shape": "target_shape_value",
            "zones": [{"zone": "zone_value"}],
        },
        "fingerprint": "fingerprint_value",
        "id": 205,
        "instance_flexibility_policy": {"instance_selections": {}},
        "instance_group": "instance_group_value",
        "instance_lifecycle_policy": {
            "default_action_on_failure": "default_action_on_failure_value",
            "force_update_on_repair": "force_update_on_repair_value",
            "on_failed_health_check": "on_failed_health_check_value",
            "on_repair": {"allow_changing_zone": "allow_changing_zone_value"},
        },
        "instance_template": "instance_template_value",
        "kind": "kind_value",
        "list_managed_instances_results": "list_managed_instances_results_value",
        "name": "name_value",
        "named_ports": [{"name": "name_value", "port": 453}],
        "region": "region_value",
        "resource_policies": {"workload_policy": "workload_policy_value"},
        "satisfies_pzi": True,
        "satisfies_pzs": True,
        "self_link": "self_link_value",
        "standby_policy": {"initial_delay_sec": 1778, "mode": "mode_value"},
        "stateful_policy": {
            "preserved_state": {"disks": {}, "external_i_ps": {}, "internal_i_ps": {}}
        },
        "status": {
            "all_instances_config": {
                "current_revision": "current_revision_value",
                "effective": True,
            },
            "applied_accelerator_topologies": [
                {
                    "accelerator_topology": "accelerator_topology_value",
                    "state": "state_value",
                    "state_details": {
                        "error": {
                            "errors": [
                                {
                                    "code": "code_value",
                                    "error_details": [
                                        {
                                            "error_info": {
                                                "domain": "domain_value",
                                                "metadatas": {},
                                                "reason": "reason_value",
                                            },
                                            "help_": {
                                                "links": [
                                                    {
                                                        "description": "description_value",
                                                        "url": "url_value",
                                                    }
                                                ]
                                            },
                                            "localized_message": {
                                                "locale": "locale_value",
                                                "message": "message_value",
                                            },
                                            "quota_info": {
                                                "dimensions": {},
                                                "future_limit": 0.1305,
                                                "limit": 0.543,
                                                "limit_name": "limit_name_value",
                                                "metric_name": "metric_name_value",
                                                "rollout_status": "rollout_status_value",
                                            },
                                        }
                                    ],
                                    "location": "location_value",
                                    "message": "message_value",
                                }
                            ]
                        },
                        "timestamp": "timestamp_value",
                    },
                }
            ],
            "autoscaler": "autoscaler_value",
            "bulk_instance_operation": {
                "in_progress": True,
                "last_progress_check": {"error": {}, "timestamp": "timestamp_value"},
            },
            "current_instance_statuses": {
                "deprovisioning": 1520,
                "non_existent": 1310,
                "pending": 741,
                "pending_stop": 1290,
                "provisioning": 1319,
                "repairing": 961,
                "running": 769,
                "staging": 749,
                "stopped": 767,
                "stopping": 884,
                "suspended": 971,
                "suspending": 1088,
                "terminated": 1069,
            },
            "is_stable": True,
            "stateful": {
                "has_stateful_config": True,
                "per_instance_configs": {"all_effective": True},
            },
            "version_target": {"is_reached": True},
        },
        "target_pools": ["target_pools_value1", "target_pools_value2"],
        "target_size": 1185,
        "target_size_policy": {"mode": "mode_value"},
        "target_stopped_size": 2047,
        "target_suspended_size": 2251,
        "update_policy": {
            "instance_redistribution_type": "instance_redistribution_type_value",
            "max_surge": {"calculated": 1042, "fixed": 528, "percent": 753},
            "max_unavailable": {},
            "minimal_action": "minimal_action_value",
            "most_disruptive_allowed_action": "most_disruptive_allowed_action_value",
            "replacement_method": "replacement_method_value",
            "type_": "type__value",
        },
        "versions": [
            {
                "instance_template": "instance_template_value",
                "name": "name_value",
                "target_size": {},
            }
        ],
        "zone": "zone_value",
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = compute.PatchInstanceGroupManagerRequest.meta.fields[
        "instance_group_manager_resource"
    ]

    def get_message_fields(field):
        # Given a field which is a message (composite type), return a list with
        # all the fields of the message.
        # If the field is not a composite type, return an empty list.
        message_fields = []

        if hasattr(field, "message") and field.message:
            is_field_type_proto_plus_type = not hasattr(field.message, "DESCRIPTOR")

            if is_field_type_proto_plus_type:
                message_fields = field.message.meta.fields.values()
            # Add `# pragma: NO COVER` because there may not be any `*_pb2` field types
            else:  # pragma: NO COVER
                message_fields = field.message.DESCRIPTOR.fields
        return message_fields

    runtime_nested_fields = [
        (field.name, nested_field.name)
        for field in get_message_fields(test_field)
        for nested_field in get_message_fields(field)
    ]

    subfields_not_in_runtime = []

    # For each item in the sample request, create a list of sub fields which are not present at runtime
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for field, value in request_init[
        "instance_group_manager_resource"
    ].items():  # pragma: NO COVER
        result = None
        is_repeated = False
        # For repeated fields
        if isinstance(value, list) and len(value):
            is_repeated = True
            result = value[0]
        # For fields where the type is another message
        if isinstance(value, dict):
            result = value

        if result and hasattr(result, "keys"):
            for subfield in result.keys():
                if (field, subfield) not in runtime_nested_fields:
                    subfields_not_in_runtime.append(
                        {
                            "field": field,
                            "subfield": subfield,
                            "is_repeated": is_repeated,
                        }
                    )

    # Remove fields from the sample request which are not present in the runtime version of the dependency
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for subfield_to_delete in subfields_not_in_runtime:  # pragma: NO COVER
        field = subfield_to_delete.get("field")
        field_repeated = subfield_to_delete.get("is_repeated")
        subfield = subfield_to_delete.get("subfield")
        if subfield:
            if field_repeated:
                for i in range(
                    0, len(request_init["instance_group_manager_resource"][field])
                ):
                    del request_init["instance_group_manager_resource"][field][i][
                        subfield
                    ]
            else:
                del request_init["instance_group_manager_resource"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation(
            client_operation_id="client_operation_id_value",
            creation_timestamp="creation_timestamp_value",
            description="description_value",
            end_time="end_time_value",
            http_error_message="http_error_message_value",
            http_error_status_code=2374,
            id=205,
            insert_time="insert_time_value",
            kind="kind_value",
            name="name_value",
            operation_group_id="operation_group_id_value",
            operation_type="operation_type_value",
            progress=885,
            region="region_value",
            self_link="self_link_value",
            start_time="start_time_value",
            status=compute.Operation.Status.DONE,
            status_message="status_message_value",
            target_id=947,
            target_link="target_link_value",
            user="user_value",
            zone="zone_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.patch(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, extended_operation.ExtendedOperation)
    assert response.client_operation_id == "client_operation_id_value"
    assert response.creation_timestamp == "creation_timestamp_value"
    assert response.description == "description_value"
    assert response.end_time == "end_time_value"
    assert response.http_error_message == "http_error_message_value"
    assert response.http_error_status_code == 2374
    assert response.id == 205
    assert response.insert_time == "insert_time_value"
    assert response.kind == "kind_value"
    assert response.name == "name_value"
    assert response.operation_group_id == "operation_group_id_value"
    assert response.operation_type == "operation_type_value"
    assert response.progress == 885
    assert response.region == "region_value"
    assert response.self_link == "self_link_value"
    assert response.start_time == "start_time_value"
    assert response.status == compute.Operation.Status.DONE
    assert response.status_message == "status_message_value"
    assert response.target_id == 947
    assert response.target_link == "target_link_value"
    assert response.user == "user_value"
    assert response.zone == "zone_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_patch_rest_interceptors(null_interceptor):
    transport = transports.InstanceGroupManagersRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.InstanceGroupManagersRestInterceptor(),
    )
    client = InstanceGroupManagersClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor, "post_patch"
        ) as post,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor, "post_patch_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor, "pre_patch"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = compute.PatchInstanceGroupManagerRequest.pb(
            compute.PatchInstanceGroupManagerRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = compute.Operation.to_json(compute.Operation())
        req.return_value.content = return_value

        request = compute.PatchInstanceGroupManagerRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = compute.Operation()
        post_with_metadata.return_value = compute.Operation(), metadata

        client.patch(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_patch_per_instance_configs_rest_bad_request(
    request_type=compute.PatchPerInstanceConfigsInstanceGroupManagerRequest,
):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "zone": "sample2",
        "instance_group_manager": "sample3",
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.patch_per_instance_configs(request)


@pytest.mark.parametrize(
    "request_type",
    [
        compute.PatchPerInstanceConfigsInstanceGroupManagerRequest,
        dict,
    ],
)
def test_patch_per_instance_configs_rest_call_success(request_type):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "zone": "sample2",
        "instance_group_manager": "sample3",
    }
    request_init["instance_group_managers_patch_per_instance_configs_req_resource"] = {
        "per_instance_configs": [
            {
                "fingerprint": "fingerprint_value",
                "name": "name_value",
                "preserved_state": {
                    "disks": {},
                    "external_i_ps": {},
                    "internal_i_ps": {},
                    "metadata": {},
                },
                "status": "status_value",
            }
        ]
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = compute.PatchPerInstanceConfigsInstanceGroupManagerRequest.meta.fields[
        "instance_group_managers_patch_per_instance_configs_req_resource"
    ]

    def get_message_fields(field):
        # Given a field which is a message (composite type), return a list with
        # all the fields of the message.
        # If the field is not a composite type, return an empty list.
        message_fields = []

        if hasattr(field, "message") and field.message:
            is_field_type_proto_plus_type = not hasattr(field.message, "DESCRIPTOR")

            if is_field_type_proto_plus_type:
                message_fields = field.message.meta.fields.values()
            # Add `# pragma: NO COVER` because there may not be any `*_pb2` field types
            else:  # pragma: NO COVER
                message_fields = field.message.DESCRIPTOR.fields
        return message_fields

    runtime_nested_fields = [
        (field.name, nested_field.name)
        for field in get_message_fields(test_field)
        for nested_field in get_message_fields(field)
    ]

    subfields_not_in_runtime = []

    # For each item in the sample request, create a list of sub fields which are not present at runtime
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for field, value in request_init[
        "instance_group_managers_patch_per_instance_configs_req_resource"
    ].items():  # pragma: NO COVER
        result = None
        is_repeated = False
        # For repeated fields
        if isinstance(value, list) and len(value):
            is_repeated = True
            result = value[0]
        # For fields where the type is another message
        if isinstance(value, dict):
            result = value

        if result and hasattr(result, "keys"):
            for subfield in result.keys():
                if (field, subfield) not in runtime_nested_fields:
                    subfields_not_in_runtime.append(
                        {
                            "field": field,
                            "subfield": subfield,
                            "is_repeated": is_repeated,
                        }
                    )

    # Remove fields from the sample request which are not present in the runtime version of the dependency
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for subfield_to_delete in subfields_not_in_runtime:  # pragma: NO COVER
        field = subfield_to_delete.get("field")
        field_repeated = subfield_to_delete.get("is_repeated")
        subfield = subfield_to_delete.get("subfield")
        if subfield:
            if field_repeated:
                for i in range(
                    0,
                    len(
                        request_init[
                            "instance_group_managers_patch_per_instance_configs_req_resource"
                        ][field]
                    ),
                ):
                    del request_init[
                        "instance_group_managers_patch_per_instance_configs_req_resource"
                    ][field][i][subfield]
            else:
                del request_init[
                    "instance_group_managers_patch_per_instance_configs_req_resource"
                ][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation(
            client_operation_id="client_operation_id_value",
            creation_timestamp="creation_timestamp_value",
            description="description_value",
            end_time="end_time_value",
            http_error_message="http_error_message_value",
            http_error_status_code=2374,
            id=205,
            insert_time="insert_time_value",
            kind="kind_value",
            name="name_value",
            operation_group_id="operation_group_id_value",
            operation_type="operation_type_value",
            progress=885,
            region="region_value",
            self_link="self_link_value",
            start_time="start_time_value",
            status=compute.Operation.Status.DONE,
            status_message="status_message_value",
            target_id=947,
            target_link="target_link_value",
            user="user_value",
            zone="zone_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.patch_per_instance_configs(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, extended_operation.ExtendedOperation)
    assert response.client_operation_id == "client_operation_id_value"
    assert response.creation_timestamp == "creation_timestamp_value"
    assert response.description == "description_value"
    assert response.end_time == "end_time_value"
    assert response.http_error_message == "http_error_message_value"
    assert response.http_error_status_code == 2374
    assert response.id == 205
    assert response.insert_time == "insert_time_value"
    assert response.kind == "kind_value"
    assert response.name == "name_value"
    assert response.operation_group_id == "operation_group_id_value"
    assert response.operation_type == "operation_type_value"
    assert response.progress == 885
    assert response.region == "region_value"
    assert response.self_link == "self_link_value"
    assert response.start_time == "start_time_value"
    assert response.status == compute.Operation.Status.DONE
    assert response.status_message == "status_message_value"
    assert response.target_id == 947
    assert response.target_link == "target_link_value"
    assert response.user == "user_value"
    assert response.zone == "zone_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_patch_per_instance_configs_rest_interceptors(null_interceptor):
    transport = transports.InstanceGroupManagersRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.InstanceGroupManagersRestInterceptor(),
    )
    client = InstanceGroupManagersClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor,
            "post_patch_per_instance_configs",
        ) as post,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor,
            "post_patch_per_instance_configs_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor,
            "pre_patch_per_instance_configs",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = compute.PatchPerInstanceConfigsInstanceGroupManagerRequest.pb(
            compute.PatchPerInstanceConfigsInstanceGroupManagerRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = compute.Operation.to_json(compute.Operation())
        req.return_value.content = return_value

        request = compute.PatchPerInstanceConfigsInstanceGroupManagerRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = compute.Operation()
        post_with_metadata.return_value = compute.Operation(), metadata

        client.patch_per_instance_configs(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_recreate_instances_rest_bad_request(
    request_type=compute.RecreateInstancesInstanceGroupManagerRequest,
):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "zone": "sample2",
        "instance_group_manager": "sample3",
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.recreate_instances(request)


@pytest.mark.parametrize(
    "request_type",
    [
        compute.RecreateInstancesInstanceGroupManagerRequest,
        dict,
    ],
)
def test_recreate_instances_rest_call_success(request_type):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "zone": "sample2",
        "instance_group_manager": "sample3",
    }
    request_init["instance_group_managers_recreate_instances_request_resource"] = {
        "instances": ["instances_value1", "instances_value2"]
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = compute.RecreateInstancesInstanceGroupManagerRequest.meta.fields[
        "instance_group_managers_recreate_instances_request_resource"
    ]

    def get_message_fields(field):
        # Given a field which is a message (composite type), return a list with
        # all the fields of the message.
        # If the field is not a composite type, return an empty list.
        message_fields = []

        if hasattr(field, "message") and field.message:
            is_field_type_proto_plus_type = not hasattr(field.message, "DESCRIPTOR")

            if is_field_type_proto_plus_type:
                message_fields = field.message.meta.fields.values()
            # Add `# pragma: NO COVER` because there may not be any `*_pb2` field types
            else:  # pragma: NO COVER
                message_fields = field.message.DESCRIPTOR.fields
        return message_fields

    runtime_nested_fields = [
        (field.name, nested_field.name)
        for field in get_message_fields(test_field)
        for nested_field in get_message_fields(field)
    ]

    subfields_not_in_runtime = []

    # For each item in the sample request, create a list of sub fields which are not present at runtime
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for field, value in request_init[
        "instance_group_managers_recreate_instances_request_resource"
    ].items():  # pragma: NO COVER
        result = None
        is_repeated = False
        # For repeated fields
        if isinstance(value, list) and len(value):
            is_repeated = True
            result = value[0]
        # For fields where the type is another message
        if isinstance(value, dict):
            result = value

        if result and hasattr(result, "keys"):
            for subfield in result.keys():
                if (field, subfield) not in runtime_nested_fields:
                    subfields_not_in_runtime.append(
                        {
                            "field": field,
                            "subfield": subfield,
                            "is_repeated": is_repeated,
                        }
                    )

    # Remove fields from the sample request which are not present in the runtime version of the dependency
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for subfield_to_delete in subfields_not_in_runtime:  # pragma: NO COVER
        field = subfield_to_delete.get("field")
        field_repeated = subfield_to_delete.get("is_repeated")
        subfield = subfield_to_delete.get("subfield")
        if subfield:
            if field_repeated:
                for i in range(
                    0,
                    len(
                        request_init[
                            "instance_group_managers_recreate_instances_request_resource"
                        ][field]
                    ),
                ):
                    del request_init[
                        "instance_group_managers_recreate_instances_request_resource"
                    ][field][i][subfield]
            else:
                del request_init[
                    "instance_group_managers_recreate_instances_request_resource"
                ][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation(
            client_operation_id="client_operation_id_value",
            creation_timestamp="creation_timestamp_value",
            description="description_value",
            end_time="end_time_value",
            http_error_message="http_error_message_value",
            http_error_status_code=2374,
            id=205,
            insert_time="insert_time_value",
            kind="kind_value",
            name="name_value",
            operation_group_id="operation_group_id_value",
            operation_type="operation_type_value",
            progress=885,
            region="region_value",
            self_link="self_link_value",
            start_time="start_time_value",
            status=compute.Operation.Status.DONE,
            status_message="status_message_value",
            target_id=947,
            target_link="target_link_value",
            user="user_value",
            zone="zone_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.recreate_instances(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, extended_operation.ExtendedOperation)
    assert response.client_operation_id == "client_operation_id_value"
    assert response.creation_timestamp == "creation_timestamp_value"
    assert response.description == "description_value"
    assert response.end_time == "end_time_value"
    assert response.http_error_message == "http_error_message_value"
    assert response.http_error_status_code == 2374
    assert response.id == 205
    assert response.insert_time == "insert_time_value"
    assert response.kind == "kind_value"
    assert response.name == "name_value"
    assert response.operation_group_id == "operation_group_id_value"
    assert response.operation_type == "operation_type_value"
    assert response.progress == 885
    assert response.region == "region_value"
    assert response.self_link == "self_link_value"
    assert response.start_time == "start_time_value"
    assert response.status == compute.Operation.Status.DONE
    assert response.status_message == "status_message_value"
    assert response.target_id == 947
    assert response.target_link == "target_link_value"
    assert response.user == "user_value"
    assert response.zone == "zone_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_recreate_instances_rest_interceptors(null_interceptor):
    transport = transports.InstanceGroupManagersRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.InstanceGroupManagersRestInterceptor(),
    )
    client = InstanceGroupManagersClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor, "post_recreate_instances"
        ) as post,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor,
            "post_recreate_instances_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor, "pre_recreate_instances"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = compute.RecreateInstancesInstanceGroupManagerRequest.pb(
            compute.RecreateInstancesInstanceGroupManagerRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = compute.Operation.to_json(compute.Operation())
        req.return_value.content = return_value

        request = compute.RecreateInstancesInstanceGroupManagerRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = compute.Operation()
        post_with_metadata.return_value = compute.Operation(), metadata

        client.recreate_instances(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_resize_rest_bad_request(
    request_type=compute.ResizeInstanceGroupManagerRequest,
):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "zone": "sample2",
        "instance_group_manager": "sample3",
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.resize(request)


@pytest.mark.parametrize(
    "request_type",
    [
        compute.ResizeInstanceGroupManagerRequest,
        dict,
    ],
)
def test_resize_rest_call_success(request_type):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "zone": "sample2",
        "instance_group_manager": "sample3",
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation(
            client_operation_id="client_operation_id_value",
            creation_timestamp="creation_timestamp_value",
            description="description_value",
            end_time="end_time_value",
            http_error_message="http_error_message_value",
            http_error_status_code=2374,
            id=205,
            insert_time="insert_time_value",
            kind="kind_value",
            name="name_value",
            operation_group_id="operation_group_id_value",
            operation_type="operation_type_value",
            progress=885,
            region="region_value",
            self_link="self_link_value",
            start_time="start_time_value",
            status=compute.Operation.Status.DONE,
            status_message="status_message_value",
            target_id=947,
            target_link="target_link_value",
            user="user_value",
            zone="zone_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.resize(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, extended_operation.ExtendedOperation)
    assert response.client_operation_id == "client_operation_id_value"
    assert response.creation_timestamp == "creation_timestamp_value"
    assert response.description == "description_value"
    assert response.end_time == "end_time_value"
    assert response.http_error_message == "http_error_message_value"
    assert response.http_error_status_code == 2374
    assert response.id == 205
    assert response.insert_time == "insert_time_value"
    assert response.kind == "kind_value"
    assert response.name == "name_value"
    assert response.operation_group_id == "operation_group_id_value"
    assert response.operation_type == "operation_type_value"
    assert response.progress == 885
    assert response.region == "region_value"
    assert response.self_link == "self_link_value"
    assert response.start_time == "start_time_value"
    assert response.status == compute.Operation.Status.DONE
    assert response.status_message == "status_message_value"
    assert response.target_id == 947
    assert response.target_link == "target_link_value"
    assert response.user == "user_value"
    assert response.zone == "zone_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_resize_rest_interceptors(null_interceptor):
    transport = transports.InstanceGroupManagersRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.InstanceGroupManagersRestInterceptor(),
    )
    client = InstanceGroupManagersClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor, "post_resize"
        ) as post,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor, "post_resize_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor, "pre_resize"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = compute.ResizeInstanceGroupManagerRequest.pb(
            compute.ResizeInstanceGroupManagerRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = compute.Operation.to_json(compute.Operation())
        req.return_value.content = return_value

        request = compute.ResizeInstanceGroupManagerRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = compute.Operation()
        post_with_metadata.return_value = compute.Operation(), metadata

        client.resize(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_resume_instances_rest_bad_request(
    request_type=compute.ResumeInstancesInstanceGroupManagerRequest,
):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "zone": "sample2",
        "instance_group_manager": "sample3",
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.resume_instances(request)


@pytest.mark.parametrize(
    "request_type",
    [
        compute.ResumeInstancesInstanceGroupManagerRequest,
        dict,
    ],
)
def test_resume_instances_rest_call_success(request_type):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "zone": "sample2",
        "instance_group_manager": "sample3",
    }
    request_init["instance_group_managers_resume_instances_request_resource"] = {
        "instances": ["instances_value1", "instances_value2"]
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = compute.ResumeInstancesInstanceGroupManagerRequest.meta.fields[
        "instance_group_managers_resume_instances_request_resource"
    ]

    def get_message_fields(field):
        # Given a field which is a message (composite type), return a list with
        # all the fields of the message.
        # If the field is not a composite type, return an empty list.
        message_fields = []

        if hasattr(field, "message") and field.message:
            is_field_type_proto_plus_type = not hasattr(field.message, "DESCRIPTOR")

            if is_field_type_proto_plus_type:
                message_fields = field.message.meta.fields.values()
            # Add `# pragma: NO COVER` because there may not be any `*_pb2` field types
            else:  # pragma: NO COVER
                message_fields = field.message.DESCRIPTOR.fields
        return message_fields

    runtime_nested_fields = [
        (field.name, nested_field.name)
        for field in get_message_fields(test_field)
        for nested_field in get_message_fields(field)
    ]

    subfields_not_in_runtime = []

    # For each item in the sample request, create a list of sub fields which are not present at runtime
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for field, value in request_init[
        "instance_group_managers_resume_instances_request_resource"
    ].items():  # pragma: NO COVER
        result = None
        is_repeated = False
        # For repeated fields
        if isinstance(value, list) and len(value):
            is_repeated = True
            result = value[0]
        # For fields where the type is another message
        if isinstance(value, dict):
            result = value

        if result and hasattr(result, "keys"):
            for subfield in result.keys():
                if (field, subfield) not in runtime_nested_fields:
                    subfields_not_in_runtime.append(
                        {
                            "field": field,
                            "subfield": subfield,
                            "is_repeated": is_repeated,
                        }
                    )

    # Remove fields from the sample request which are not present in the runtime version of the dependency
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for subfield_to_delete in subfields_not_in_runtime:  # pragma: NO COVER
        field = subfield_to_delete.get("field")
        field_repeated = subfield_to_delete.get("is_repeated")
        subfield = subfield_to_delete.get("subfield")
        if subfield:
            if field_repeated:
                for i in range(
                    0,
                    len(
                        request_init[
                            "instance_group_managers_resume_instances_request_resource"
                        ][field]
                    ),
                ):
                    del request_init[
                        "instance_group_managers_resume_instances_request_resource"
                    ][field][i][subfield]
            else:
                del request_init[
                    "instance_group_managers_resume_instances_request_resource"
                ][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation(
            client_operation_id="client_operation_id_value",
            creation_timestamp="creation_timestamp_value",
            description="description_value",
            end_time="end_time_value",
            http_error_message="http_error_message_value",
            http_error_status_code=2374,
            id=205,
            insert_time="insert_time_value",
            kind="kind_value",
            name="name_value",
            operation_group_id="operation_group_id_value",
            operation_type="operation_type_value",
            progress=885,
            region="region_value",
            self_link="self_link_value",
            start_time="start_time_value",
            status=compute.Operation.Status.DONE,
            status_message="status_message_value",
            target_id=947,
            target_link="target_link_value",
            user="user_value",
            zone="zone_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.resume_instances(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, extended_operation.ExtendedOperation)
    assert response.client_operation_id == "client_operation_id_value"
    assert response.creation_timestamp == "creation_timestamp_value"
    assert response.description == "description_value"
    assert response.end_time == "end_time_value"
    assert response.http_error_message == "http_error_message_value"
    assert response.http_error_status_code == 2374
    assert response.id == 205
    assert response.insert_time == "insert_time_value"
    assert response.kind == "kind_value"
    assert response.name == "name_value"
    assert response.operation_group_id == "operation_group_id_value"
    assert response.operation_type == "operation_type_value"
    assert response.progress == 885
    assert response.region == "region_value"
    assert response.self_link == "self_link_value"
    assert response.start_time == "start_time_value"
    assert response.status == compute.Operation.Status.DONE
    assert response.status_message == "status_message_value"
    assert response.target_id == 947
    assert response.target_link == "target_link_value"
    assert response.user == "user_value"
    assert response.zone == "zone_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_resume_instances_rest_interceptors(null_interceptor):
    transport = transports.InstanceGroupManagersRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.InstanceGroupManagersRestInterceptor(),
    )
    client = InstanceGroupManagersClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor, "post_resume_instances"
        ) as post,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor,
            "post_resume_instances_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor, "pre_resume_instances"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = compute.ResumeInstancesInstanceGroupManagerRequest.pb(
            compute.ResumeInstancesInstanceGroupManagerRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = compute.Operation.to_json(compute.Operation())
        req.return_value.content = return_value

        request = compute.ResumeInstancesInstanceGroupManagerRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = compute.Operation()
        post_with_metadata.return_value = compute.Operation(), metadata

        client.resume_instances(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_set_instance_template_rest_bad_request(
    request_type=compute.SetInstanceTemplateInstanceGroupManagerRequest,
):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "zone": "sample2",
        "instance_group_manager": "sample3",
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.set_instance_template(request)


@pytest.mark.parametrize(
    "request_type",
    [
        compute.SetInstanceTemplateInstanceGroupManagerRequest,
        dict,
    ],
)
def test_set_instance_template_rest_call_success(request_type):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "zone": "sample2",
        "instance_group_manager": "sample3",
    }
    request_init["instance_group_managers_set_instance_template_request_resource"] = {
        "instance_template": "instance_template_value"
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = compute.SetInstanceTemplateInstanceGroupManagerRequest.meta.fields[
        "instance_group_managers_set_instance_template_request_resource"
    ]

    def get_message_fields(field):
        # Given a field which is a message (composite type), return a list with
        # all the fields of the message.
        # If the field is not a composite type, return an empty list.
        message_fields = []

        if hasattr(field, "message") and field.message:
            is_field_type_proto_plus_type = not hasattr(field.message, "DESCRIPTOR")

            if is_field_type_proto_plus_type:
                message_fields = field.message.meta.fields.values()
            # Add `# pragma: NO COVER` because there may not be any `*_pb2` field types
            else:  # pragma: NO COVER
                message_fields = field.message.DESCRIPTOR.fields
        return message_fields

    runtime_nested_fields = [
        (field.name, nested_field.name)
        for field in get_message_fields(test_field)
        for nested_field in get_message_fields(field)
    ]

    subfields_not_in_runtime = []

    # For each item in the sample request, create a list of sub fields which are not present at runtime
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for field, value in request_init[
        "instance_group_managers_set_instance_template_request_resource"
    ].items():  # pragma: NO COVER
        result = None
        is_repeated = False
        # For repeated fields
        if isinstance(value, list) and len(value):
            is_repeated = True
            result = value[0]
        # For fields where the type is another message
        if isinstance(value, dict):
            result = value

        if result and hasattr(result, "keys"):
            for subfield in result.keys():
                if (field, subfield) not in runtime_nested_fields:
                    subfields_not_in_runtime.append(
                        {
                            "field": field,
                            "subfield": subfield,
                            "is_repeated": is_repeated,
                        }
                    )

    # Remove fields from the sample request which are not present in the runtime version of the dependency
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for subfield_to_delete in subfields_not_in_runtime:  # pragma: NO COVER
        field = subfield_to_delete.get("field")
        field_repeated = subfield_to_delete.get("is_repeated")
        subfield = subfield_to_delete.get("subfield")
        if subfield:
            if field_repeated:
                for i in range(
                    0,
                    len(
                        request_init[
                            "instance_group_managers_set_instance_template_request_resource"
                        ][field]
                    ),
                ):
                    del request_init[
                        "instance_group_managers_set_instance_template_request_resource"
                    ][field][i][subfield]
            else:
                del request_init[
                    "instance_group_managers_set_instance_template_request_resource"
                ][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation(
            client_operation_id="client_operation_id_value",
            creation_timestamp="creation_timestamp_value",
            description="description_value",
            end_time="end_time_value",
            http_error_message="http_error_message_value",
            http_error_status_code=2374,
            id=205,
            insert_time="insert_time_value",
            kind="kind_value",
            name="name_value",
            operation_group_id="operation_group_id_value",
            operation_type="operation_type_value",
            progress=885,
            region="region_value",
            self_link="self_link_value",
            start_time="start_time_value",
            status=compute.Operation.Status.DONE,
            status_message="status_message_value",
            target_id=947,
            target_link="target_link_value",
            user="user_value",
            zone="zone_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.set_instance_template(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, extended_operation.ExtendedOperation)
    assert response.client_operation_id == "client_operation_id_value"
    assert response.creation_timestamp == "creation_timestamp_value"
    assert response.description == "description_value"
    assert response.end_time == "end_time_value"
    assert response.http_error_message == "http_error_message_value"
    assert response.http_error_status_code == 2374
    assert response.id == 205
    assert response.insert_time == "insert_time_value"
    assert response.kind == "kind_value"
    assert response.name == "name_value"
    assert response.operation_group_id == "operation_group_id_value"
    assert response.operation_type == "operation_type_value"
    assert response.progress == 885
    assert response.region == "region_value"
    assert response.self_link == "self_link_value"
    assert response.start_time == "start_time_value"
    assert response.status == compute.Operation.Status.DONE
    assert response.status_message == "status_message_value"
    assert response.target_id == 947
    assert response.target_link == "target_link_value"
    assert response.user == "user_value"
    assert response.zone == "zone_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_set_instance_template_rest_interceptors(null_interceptor):
    transport = transports.InstanceGroupManagersRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.InstanceGroupManagersRestInterceptor(),
    )
    client = InstanceGroupManagersClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor,
            "post_set_instance_template",
        ) as post,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor,
            "post_set_instance_template_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor, "pre_set_instance_template"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = compute.SetInstanceTemplateInstanceGroupManagerRequest.pb(
            compute.SetInstanceTemplateInstanceGroupManagerRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = compute.Operation.to_json(compute.Operation())
        req.return_value.content = return_value

        request = compute.SetInstanceTemplateInstanceGroupManagerRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = compute.Operation()
        post_with_metadata.return_value = compute.Operation(), metadata

        client.set_instance_template(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_set_target_pools_rest_bad_request(
    request_type=compute.SetTargetPoolsInstanceGroupManagerRequest,
):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "zone": "sample2",
        "instance_group_manager": "sample3",
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.set_target_pools(request)


@pytest.mark.parametrize(
    "request_type",
    [
        compute.SetTargetPoolsInstanceGroupManagerRequest,
        dict,
    ],
)
def test_set_target_pools_rest_call_success(request_type):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "zone": "sample2",
        "instance_group_manager": "sample3",
    }
    request_init["instance_group_managers_set_target_pools_request_resource"] = {
        "fingerprint": "fingerprint_value",
        "target_pools": ["target_pools_value1", "target_pools_value2"],
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = compute.SetTargetPoolsInstanceGroupManagerRequest.meta.fields[
        "instance_group_managers_set_target_pools_request_resource"
    ]

    def get_message_fields(field):
        # Given a field which is a message (composite type), return a list with
        # all the fields of the message.
        # If the field is not a composite type, return an empty list.
        message_fields = []

        if hasattr(field, "message") and field.message:
            is_field_type_proto_plus_type = not hasattr(field.message, "DESCRIPTOR")

            if is_field_type_proto_plus_type:
                message_fields = field.message.meta.fields.values()
            # Add `# pragma: NO COVER` because there may not be any `*_pb2` field types
            else:  # pragma: NO COVER
                message_fields = field.message.DESCRIPTOR.fields
        return message_fields

    runtime_nested_fields = [
        (field.name, nested_field.name)
        for field in get_message_fields(test_field)
        for nested_field in get_message_fields(field)
    ]

    subfields_not_in_runtime = []

    # For each item in the sample request, create a list of sub fields which are not present at runtime
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for field, value in request_init[
        "instance_group_managers_set_target_pools_request_resource"
    ].items():  # pragma: NO COVER
        result = None
        is_repeated = False
        # For repeated fields
        if isinstance(value, list) and len(value):
            is_repeated = True
            result = value[0]
        # For fields where the type is another message
        if isinstance(value, dict):
            result = value

        if result and hasattr(result, "keys"):
            for subfield in result.keys():
                if (field, subfield) not in runtime_nested_fields:
                    subfields_not_in_runtime.append(
                        {
                            "field": field,
                            "subfield": subfield,
                            "is_repeated": is_repeated,
                        }
                    )

    # Remove fields from the sample request which are not present in the runtime version of the dependency
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for subfield_to_delete in subfields_not_in_runtime:  # pragma: NO COVER
        field = subfield_to_delete.get("field")
        field_repeated = subfield_to_delete.get("is_repeated")
        subfield = subfield_to_delete.get("subfield")
        if subfield:
            if field_repeated:
                for i in range(
                    0,
                    len(
                        request_init[
                            "instance_group_managers_set_target_pools_request_resource"
                        ][field]
                    ),
                ):
                    del request_init[
                        "instance_group_managers_set_target_pools_request_resource"
                    ][field][i][subfield]
            else:
                del request_init[
                    "instance_group_managers_set_target_pools_request_resource"
                ][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation(
            client_operation_id="client_operation_id_value",
            creation_timestamp="creation_timestamp_value",
            description="description_value",
            end_time="end_time_value",
            http_error_message="http_error_message_value",
            http_error_status_code=2374,
            id=205,
            insert_time="insert_time_value",
            kind="kind_value",
            name="name_value",
            operation_group_id="operation_group_id_value",
            operation_type="operation_type_value",
            progress=885,
            region="region_value",
            self_link="self_link_value",
            start_time="start_time_value",
            status=compute.Operation.Status.DONE,
            status_message="status_message_value",
            target_id=947,
            target_link="target_link_value",
            user="user_value",
            zone="zone_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.set_target_pools(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, extended_operation.ExtendedOperation)
    assert response.client_operation_id == "client_operation_id_value"
    assert response.creation_timestamp == "creation_timestamp_value"
    assert response.description == "description_value"
    assert response.end_time == "end_time_value"
    assert response.http_error_message == "http_error_message_value"
    assert response.http_error_status_code == 2374
    assert response.id == 205
    assert response.insert_time == "insert_time_value"
    assert response.kind == "kind_value"
    assert response.name == "name_value"
    assert response.operation_group_id == "operation_group_id_value"
    assert response.operation_type == "operation_type_value"
    assert response.progress == 885
    assert response.region == "region_value"
    assert response.self_link == "self_link_value"
    assert response.start_time == "start_time_value"
    assert response.status == compute.Operation.Status.DONE
    assert response.status_message == "status_message_value"
    assert response.target_id == 947
    assert response.target_link == "target_link_value"
    assert response.user == "user_value"
    assert response.zone == "zone_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_set_target_pools_rest_interceptors(null_interceptor):
    transport = transports.InstanceGroupManagersRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.InstanceGroupManagersRestInterceptor(),
    )
    client = InstanceGroupManagersClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor, "post_set_target_pools"
        ) as post,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor,
            "post_set_target_pools_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor, "pre_set_target_pools"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = compute.SetTargetPoolsInstanceGroupManagerRequest.pb(
            compute.SetTargetPoolsInstanceGroupManagerRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = compute.Operation.to_json(compute.Operation())
        req.return_value.content = return_value

        request = compute.SetTargetPoolsInstanceGroupManagerRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = compute.Operation()
        post_with_metadata.return_value = compute.Operation(), metadata

        client.set_target_pools(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_start_instances_rest_bad_request(
    request_type=compute.StartInstancesInstanceGroupManagerRequest,
):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "zone": "sample2",
        "instance_group_manager": "sample3",
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.start_instances(request)


@pytest.mark.parametrize(
    "request_type",
    [
        compute.StartInstancesInstanceGroupManagerRequest,
        dict,
    ],
)
def test_start_instances_rest_call_success(request_type):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "zone": "sample2",
        "instance_group_manager": "sample3",
    }
    request_init["instance_group_managers_start_instances_request_resource"] = {
        "instances": ["instances_value1", "instances_value2"]
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = compute.StartInstancesInstanceGroupManagerRequest.meta.fields[
        "instance_group_managers_start_instances_request_resource"
    ]

    def get_message_fields(field):
        # Given a field which is a message (composite type), return a list with
        # all the fields of the message.
        # If the field is not a composite type, return an empty list.
        message_fields = []

        if hasattr(field, "message") and field.message:
            is_field_type_proto_plus_type = not hasattr(field.message, "DESCRIPTOR")

            if is_field_type_proto_plus_type:
                message_fields = field.message.meta.fields.values()
            # Add `# pragma: NO COVER` because there may not be any `*_pb2` field types
            else:  # pragma: NO COVER
                message_fields = field.message.DESCRIPTOR.fields
        return message_fields

    runtime_nested_fields = [
        (field.name, nested_field.name)
        for field in get_message_fields(test_field)
        for nested_field in get_message_fields(field)
    ]

    subfields_not_in_runtime = []

    # For each item in the sample request, create a list of sub fields which are not present at runtime
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for field, value in request_init[
        "instance_group_managers_start_instances_request_resource"
    ].items():  # pragma: NO COVER
        result = None
        is_repeated = False
        # For repeated fields
        if isinstance(value, list) and len(value):
            is_repeated = True
            result = value[0]
        # For fields where the type is another message
        if isinstance(value, dict):
            result = value

        if result and hasattr(result, "keys"):
            for subfield in result.keys():
                if (field, subfield) not in runtime_nested_fields:
                    subfields_not_in_runtime.append(
                        {
                            "field": field,
                            "subfield": subfield,
                            "is_repeated": is_repeated,
                        }
                    )

    # Remove fields from the sample request which are not present in the runtime version of the dependency
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for subfield_to_delete in subfields_not_in_runtime:  # pragma: NO COVER
        field = subfield_to_delete.get("field")
        field_repeated = subfield_to_delete.get("is_repeated")
        subfield = subfield_to_delete.get("subfield")
        if subfield:
            if field_repeated:
                for i in range(
                    0,
                    len(
                        request_init[
                            "instance_group_managers_start_instances_request_resource"
                        ][field]
                    ),
                ):
                    del request_init[
                        "instance_group_managers_start_instances_request_resource"
                    ][field][i][subfield]
            else:
                del request_init[
                    "instance_group_managers_start_instances_request_resource"
                ][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation(
            client_operation_id="client_operation_id_value",
            creation_timestamp="creation_timestamp_value",
            description="description_value",
            end_time="end_time_value",
            http_error_message="http_error_message_value",
            http_error_status_code=2374,
            id=205,
            insert_time="insert_time_value",
            kind="kind_value",
            name="name_value",
            operation_group_id="operation_group_id_value",
            operation_type="operation_type_value",
            progress=885,
            region="region_value",
            self_link="self_link_value",
            start_time="start_time_value",
            status=compute.Operation.Status.DONE,
            status_message="status_message_value",
            target_id=947,
            target_link="target_link_value",
            user="user_value",
            zone="zone_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.start_instances(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, extended_operation.ExtendedOperation)
    assert response.client_operation_id == "client_operation_id_value"
    assert response.creation_timestamp == "creation_timestamp_value"
    assert response.description == "description_value"
    assert response.end_time == "end_time_value"
    assert response.http_error_message == "http_error_message_value"
    assert response.http_error_status_code == 2374
    assert response.id == 205
    assert response.insert_time == "insert_time_value"
    assert response.kind == "kind_value"
    assert response.name == "name_value"
    assert response.operation_group_id == "operation_group_id_value"
    assert response.operation_type == "operation_type_value"
    assert response.progress == 885
    assert response.region == "region_value"
    assert response.self_link == "self_link_value"
    assert response.start_time == "start_time_value"
    assert response.status == compute.Operation.Status.DONE
    assert response.status_message == "status_message_value"
    assert response.target_id == 947
    assert response.target_link == "target_link_value"
    assert response.user == "user_value"
    assert response.zone == "zone_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_start_instances_rest_interceptors(null_interceptor):
    transport = transports.InstanceGroupManagersRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.InstanceGroupManagersRestInterceptor(),
    )
    client = InstanceGroupManagersClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor, "post_start_instances"
        ) as post,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor,
            "post_start_instances_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor, "pre_start_instances"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = compute.StartInstancesInstanceGroupManagerRequest.pb(
            compute.StartInstancesInstanceGroupManagerRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = compute.Operation.to_json(compute.Operation())
        req.return_value.content = return_value

        request = compute.StartInstancesInstanceGroupManagerRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = compute.Operation()
        post_with_metadata.return_value = compute.Operation(), metadata

        client.start_instances(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_stop_instances_rest_bad_request(
    request_type=compute.StopInstancesInstanceGroupManagerRequest,
):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "zone": "sample2",
        "instance_group_manager": "sample3",
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.stop_instances(request)


@pytest.mark.parametrize(
    "request_type",
    [
        compute.StopInstancesInstanceGroupManagerRequest,
        dict,
    ],
)
def test_stop_instances_rest_call_success(request_type):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "zone": "sample2",
        "instance_group_manager": "sample3",
    }
    request_init["instance_group_managers_stop_instances_request_resource"] = {
        "force_stop": True,
        "instances": ["instances_value1", "instances_value2"],
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = compute.StopInstancesInstanceGroupManagerRequest.meta.fields[
        "instance_group_managers_stop_instances_request_resource"
    ]

    def get_message_fields(field):
        # Given a field which is a message (composite type), return a list with
        # all the fields of the message.
        # If the field is not a composite type, return an empty list.
        message_fields = []

        if hasattr(field, "message") and field.message:
            is_field_type_proto_plus_type = not hasattr(field.message, "DESCRIPTOR")

            if is_field_type_proto_plus_type:
                message_fields = field.message.meta.fields.values()
            # Add `# pragma: NO COVER` because there may not be any `*_pb2` field types
            else:  # pragma: NO COVER
                message_fields = field.message.DESCRIPTOR.fields
        return message_fields

    runtime_nested_fields = [
        (field.name, nested_field.name)
        for field in get_message_fields(test_field)
        for nested_field in get_message_fields(field)
    ]

    subfields_not_in_runtime = []

    # For each item in the sample request, create a list of sub fields which are not present at runtime
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for field, value in request_init[
        "instance_group_managers_stop_instances_request_resource"
    ].items():  # pragma: NO COVER
        result = None
        is_repeated = False
        # For repeated fields
        if isinstance(value, list) and len(value):
            is_repeated = True
            result = value[0]
        # For fields where the type is another message
        if isinstance(value, dict):
            result = value

        if result and hasattr(result, "keys"):
            for subfield in result.keys():
                if (field, subfield) not in runtime_nested_fields:
                    subfields_not_in_runtime.append(
                        {
                            "field": field,
                            "subfield": subfield,
                            "is_repeated": is_repeated,
                        }
                    )

    # Remove fields from the sample request which are not present in the runtime version of the dependency
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for subfield_to_delete in subfields_not_in_runtime:  # pragma: NO COVER
        field = subfield_to_delete.get("field")
        field_repeated = subfield_to_delete.get("is_repeated")
        subfield = subfield_to_delete.get("subfield")
        if subfield:
            if field_repeated:
                for i in range(
                    0,
                    len(
                        request_init[
                            "instance_group_managers_stop_instances_request_resource"
                        ][field]
                    ),
                ):
                    del request_init[
                        "instance_group_managers_stop_instances_request_resource"
                    ][field][i][subfield]
            else:
                del request_init[
                    "instance_group_managers_stop_instances_request_resource"
                ][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation(
            client_operation_id="client_operation_id_value",
            creation_timestamp="creation_timestamp_value",
            description="description_value",
            end_time="end_time_value",
            http_error_message="http_error_message_value",
            http_error_status_code=2374,
            id=205,
            insert_time="insert_time_value",
            kind="kind_value",
            name="name_value",
            operation_group_id="operation_group_id_value",
            operation_type="operation_type_value",
            progress=885,
            region="region_value",
            self_link="self_link_value",
            start_time="start_time_value",
            status=compute.Operation.Status.DONE,
            status_message="status_message_value",
            target_id=947,
            target_link="target_link_value",
            user="user_value",
            zone="zone_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.stop_instances(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, extended_operation.ExtendedOperation)
    assert response.client_operation_id == "client_operation_id_value"
    assert response.creation_timestamp == "creation_timestamp_value"
    assert response.description == "description_value"
    assert response.end_time == "end_time_value"
    assert response.http_error_message == "http_error_message_value"
    assert response.http_error_status_code == 2374
    assert response.id == 205
    assert response.insert_time == "insert_time_value"
    assert response.kind == "kind_value"
    assert response.name == "name_value"
    assert response.operation_group_id == "operation_group_id_value"
    assert response.operation_type == "operation_type_value"
    assert response.progress == 885
    assert response.region == "region_value"
    assert response.self_link == "self_link_value"
    assert response.start_time == "start_time_value"
    assert response.status == compute.Operation.Status.DONE
    assert response.status_message == "status_message_value"
    assert response.target_id == 947
    assert response.target_link == "target_link_value"
    assert response.user == "user_value"
    assert response.zone == "zone_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_stop_instances_rest_interceptors(null_interceptor):
    transport = transports.InstanceGroupManagersRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.InstanceGroupManagersRestInterceptor(),
    )
    client = InstanceGroupManagersClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor, "post_stop_instances"
        ) as post,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor,
            "post_stop_instances_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor, "pre_stop_instances"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = compute.StopInstancesInstanceGroupManagerRequest.pb(
            compute.StopInstancesInstanceGroupManagerRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = compute.Operation.to_json(compute.Operation())
        req.return_value.content = return_value

        request = compute.StopInstancesInstanceGroupManagerRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = compute.Operation()
        post_with_metadata.return_value = compute.Operation(), metadata

        client.stop_instances(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_suspend_instances_rest_bad_request(
    request_type=compute.SuspendInstancesInstanceGroupManagerRequest,
):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "zone": "sample2",
        "instance_group_manager": "sample3",
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.suspend_instances(request)


@pytest.mark.parametrize(
    "request_type",
    [
        compute.SuspendInstancesInstanceGroupManagerRequest,
        dict,
    ],
)
def test_suspend_instances_rest_call_success(request_type):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "zone": "sample2",
        "instance_group_manager": "sample3",
    }
    request_init["instance_group_managers_suspend_instances_request_resource"] = {
        "force_suspend": True,
        "instances": ["instances_value1", "instances_value2"],
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = compute.SuspendInstancesInstanceGroupManagerRequest.meta.fields[
        "instance_group_managers_suspend_instances_request_resource"
    ]

    def get_message_fields(field):
        # Given a field which is a message (composite type), return a list with
        # all the fields of the message.
        # If the field is not a composite type, return an empty list.
        message_fields = []

        if hasattr(field, "message") and field.message:
            is_field_type_proto_plus_type = not hasattr(field.message, "DESCRIPTOR")

            if is_field_type_proto_plus_type:
                message_fields = field.message.meta.fields.values()
            # Add `# pragma: NO COVER` because there may not be any `*_pb2` field types
            else:  # pragma: NO COVER
                message_fields = field.message.DESCRIPTOR.fields
        return message_fields

    runtime_nested_fields = [
        (field.name, nested_field.name)
        for field in get_message_fields(test_field)
        for nested_field in get_message_fields(field)
    ]

    subfields_not_in_runtime = []

    # For each item in the sample request, create a list of sub fields which are not present at runtime
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for field, value in request_init[
        "instance_group_managers_suspend_instances_request_resource"
    ].items():  # pragma: NO COVER
        result = None
        is_repeated = False
        # For repeated fields
        if isinstance(value, list) and len(value):
            is_repeated = True
            result = value[0]
        # For fields where the type is another message
        if isinstance(value, dict):
            result = value

        if result and hasattr(result, "keys"):
            for subfield in result.keys():
                if (field, subfield) not in runtime_nested_fields:
                    subfields_not_in_runtime.append(
                        {
                            "field": field,
                            "subfield": subfield,
                            "is_repeated": is_repeated,
                        }
                    )

    # Remove fields from the sample request which are not present in the runtime version of the dependency
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for subfield_to_delete in subfields_not_in_runtime:  # pragma: NO COVER
        field = subfield_to_delete.get("field")
        field_repeated = subfield_to_delete.get("is_repeated")
        subfield = subfield_to_delete.get("subfield")
        if subfield:
            if field_repeated:
                for i in range(
                    0,
                    len(
                        request_init[
                            "instance_group_managers_suspend_instances_request_resource"
                        ][field]
                    ),
                ):
                    del request_init[
                        "instance_group_managers_suspend_instances_request_resource"
                    ][field][i][subfield]
            else:
                del request_init[
                    "instance_group_managers_suspend_instances_request_resource"
                ][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation(
            client_operation_id="client_operation_id_value",
            creation_timestamp="creation_timestamp_value",
            description="description_value",
            end_time="end_time_value",
            http_error_message="http_error_message_value",
            http_error_status_code=2374,
            id=205,
            insert_time="insert_time_value",
            kind="kind_value",
            name="name_value",
            operation_group_id="operation_group_id_value",
            operation_type="operation_type_value",
            progress=885,
            region="region_value",
            self_link="self_link_value",
            start_time="start_time_value",
            status=compute.Operation.Status.DONE,
            status_message="status_message_value",
            target_id=947,
            target_link="target_link_value",
            user="user_value",
            zone="zone_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.suspend_instances(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, extended_operation.ExtendedOperation)
    assert response.client_operation_id == "client_operation_id_value"
    assert response.creation_timestamp == "creation_timestamp_value"
    assert response.description == "description_value"
    assert response.end_time == "end_time_value"
    assert response.http_error_message == "http_error_message_value"
    assert response.http_error_status_code == 2374
    assert response.id == 205
    assert response.insert_time == "insert_time_value"
    assert response.kind == "kind_value"
    assert response.name == "name_value"
    assert response.operation_group_id == "operation_group_id_value"
    assert response.operation_type == "operation_type_value"
    assert response.progress == 885
    assert response.region == "region_value"
    assert response.self_link == "self_link_value"
    assert response.start_time == "start_time_value"
    assert response.status == compute.Operation.Status.DONE
    assert response.status_message == "status_message_value"
    assert response.target_id == 947
    assert response.target_link == "target_link_value"
    assert response.user == "user_value"
    assert response.zone == "zone_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_suspend_instances_rest_interceptors(null_interceptor):
    transport = transports.InstanceGroupManagersRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.InstanceGroupManagersRestInterceptor(),
    )
    client = InstanceGroupManagersClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor, "post_suspend_instances"
        ) as post,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor,
            "post_suspend_instances_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor, "pre_suspend_instances"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = compute.SuspendInstancesInstanceGroupManagerRequest.pb(
            compute.SuspendInstancesInstanceGroupManagerRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = compute.Operation.to_json(compute.Operation())
        req.return_value.content = return_value

        request = compute.SuspendInstancesInstanceGroupManagerRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = compute.Operation()
        post_with_metadata.return_value = compute.Operation(), metadata

        client.suspend_instances(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_update_per_instance_configs_rest_bad_request(
    request_type=compute.UpdatePerInstanceConfigsInstanceGroupManagerRequest,
):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "zone": "sample2",
        "instance_group_manager": "sample3",
    }
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = mock.Mock()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.update_per_instance_configs(request)


@pytest.mark.parametrize(
    "request_type",
    [
        compute.UpdatePerInstanceConfigsInstanceGroupManagerRequest,
        dict,
    ],
)
def test_update_per_instance_configs_rest_call_success(request_type):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "project": "sample1",
        "zone": "sample2",
        "instance_group_manager": "sample3",
    }
    request_init["instance_group_managers_update_per_instance_configs_req_resource"] = {
        "per_instance_configs": [
            {
                "fingerprint": "fingerprint_value",
                "name": "name_value",
                "preserved_state": {
                    "disks": {},
                    "external_i_ps": {},
                    "internal_i_ps": {},
                    "metadata": {},
                },
                "status": "status_value",
            }
        ]
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = (
        compute.UpdatePerInstanceConfigsInstanceGroupManagerRequest.meta.fields[
            "instance_group_managers_update_per_instance_configs_req_resource"
        ]
    )

    def get_message_fields(field):
        # Given a field which is a message (composite type), return a list with
        # all the fields of the message.
        # If the field is not a composite type, return an empty list.
        message_fields = []

        if hasattr(field, "message") and field.message:
            is_field_type_proto_plus_type = not hasattr(field.message, "DESCRIPTOR")

            if is_field_type_proto_plus_type:
                message_fields = field.message.meta.fields.values()
            # Add `# pragma: NO COVER` because there may not be any `*_pb2` field types
            else:  # pragma: NO COVER
                message_fields = field.message.DESCRIPTOR.fields
        return message_fields

    runtime_nested_fields = [
        (field.name, nested_field.name)
        for field in get_message_fields(test_field)
        for nested_field in get_message_fields(field)
    ]

    subfields_not_in_runtime = []

    # For each item in the sample request, create a list of sub fields which are not present at runtime
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for field, value in request_init[
        "instance_group_managers_update_per_instance_configs_req_resource"
    ].items():  # pragma: NO COVER
        result = None
        is_repeated = False
        # For repeated fields
        if isinstance(value, list) and len(value):
            is_repeated = True
            result = value[0]
        # For fields where the type is another message
        if isinstance(value, dict):
            result = value

        if result and hasattr(result, "keys"):
            for subfield in result.keys():
                if (field, subfield) not in runtime_nested_fields:
                    subfields_not_in_runtime.append(
                        {
                            "field": field,
                            "subfield": subfield,
                            "is_repeated": is_repeated,
                        }
                    )

    # Remove fields from the sample request which are not present in the runtime version of the dependency
    # Add `# pragma: NO COVER` because this test code will not run if all subfields are present at runtime
    for subfield_to_delete in subfields_not_in_runtime:  # pragma: NO COVER
        field = subfield_to_delete.get("field")
        field_repeated = subfield_to_delete.get("is_repeated")
        subfield = subfield_to_delete.get("subfield")
        if subfield:
            if field_repeated:
                for i in range(
                    0,
                    len(
                        request_init[
                            "instance_group_managers_update_per_instance_configs_req_resource"
                        ][field]
                    ),
                ):
                    del request_init[
                        "instance_group_managers_update_per_instance_configs_req_resource"
                    ][field][i][subfield]
            else:
                del request_init[
                    "instance_group_managers_update_per_instance_configs_req_resource"
                ][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = compute.Operation(
            client_operation_id="client_operation_id_value",
            creation_timestamp="creation_timestamp_value",
            description="description_value",
            end_time="end_time_value",
            http_error_message="http_error_message_value",
            http_error_status_code=2374,
            id=205,
            insert_time="insert_time_value",
            kind="kind_value",
            name="name_value",
            operation_group_id="operation_group_id_value",
            operation_type="operation_type_value",
            progress=885,
            region="region_value",
            self_link="self_link_value",
            start_time="start_time_value",
            status=compute.Operation.Status.DONE,
            status_message="status_message_value",
            target_id=947,
            target_link="target_link_value",
            user="user_value",
            zone="zone_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = compute.Operation.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.update_per_instance_configs(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, extended_operation.ExtendedOperation)
    assert response.client_operation_id == "client_operation_id_value"
    assert response.creation_timestamp == "creation_timestamp_value"
    assert response.description == "description_value"
    assert response.end_time == "end_time_value"
    assert response.http_error_message == "http_error_message_value"
    assert response.http_error_status_code == 2374
    assert response.id == 205
    assert response.insert_time == "insert_time_value"
    assert response.kind == "kind_value"
    assert response.name == "name_value"
    assert response.operation_group_id == "operation_group_id_value"
    assert response.operation_type == "operation_type_value"
    assert response.progress == 885
    assert response.region == "region_value"
    assert response.self_link == "self_link_value"
    assert response.start_time == "start_time_value"
    assert response.status == compute.Operation.Status.DONE
    assert response.status_message == "status_message_value"
    assert response.target_id == 947
    assert response.target_link == "target_link_value"
    assert response.user == "user_value"
    assert response.zone == "zone_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_update_per_instance_configs_rest_interceptors(null_interceptor):
    transport = transports.InstanceGroupManagersRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.InstanceGroupManagersRestInterceptor(),
    )
    client = InstanceGroupManagersClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor,
            "post_update_per_instance_configs",
        ) as post,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor,
            "post_update_per_instance_configs_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.InstanceGroupManagersRestInterceptor,
            "pre_update_per_instance_configs",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = compute.UpdatePerInstanceConfigsInstanceGroupManagerRequest.pb(
            compute.UpdatePerInstanceConfigsInstanceGroupManagerRequest()
        )
        transcode.return_value = {
            "method": "post",
            "uri": "my_uri",
            "body": pb_message,
            "query_params": pb_message,
        }

        req.return_value = mock.Mock()
        req.return_value.status_code = 200
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        return_value = compute.Operation.to_json(compute.Operation())
        req.return_value.content = return_value

        request = compute.UpdatePerInstanceConfigsInstanceGroupManagerRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = compute.Operation()
        post_with_metadata.return_value = compute.Operation(), metadata

        client.update_per_instance_configs(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_initialize_client_w_rest():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_abandon_instances_unary_empty_call_rest():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.abandon_instances), "__call__"
    ) as call:
        client.abandon_instances_unary(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = compute.AbandonInstancesInstanceGroupManagerRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_aggregated_list_empty_call_rest():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.aggregated_list), "__call__") as call:
        client.aggregated_list(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = compute.AggregatedListInstanceGroupManagersRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_apply_updates_to_instances_unary_empty_call_rest():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.apply_updates_to_instances), "__call__"
    ) as call:
        client.apply_updates_to_instances_unary(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = compute.ApplyUpdatesToInstancesInstanceGroupManagerRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_instances_unary_empty_call_rest():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.create_instances), "__call__") as call:
        client.create_instances_unary(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = compute.CreateInstancesInstanceGroupManagerRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_delete_unary_empty_call_rest():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.delete), "__call__") as call:
        client.delete_unary(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = compute.DeleteInstanceGroupManagerRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_delete_instances_unary_empty_call_rest():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.delete_instances), "__call__") as call:
        client.delete_instances_unary(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = compute.DeleteInstancesInstanceGroupManagerRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_delete_per_instance_configs_unary_empty_call_rest():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.delete_per_instance_configs), "__call__"
    ) as call:
        client.delete_per_instance_configs_unary(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = compute.DeletePerInstanceConfigsInstanceGroupManagerRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_empty_call_rest():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get), "__call__") as call:
        client.get(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = compute.GetInstanceGroupManagerRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_insert_unary_empty_call_rest():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.insert), "__call__") as call:
        client.insert_unary(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = compute.InsertInstanceGroupManagerRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_empty_call_rest():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list), "__call__") as call:
        client.list(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = compute.ListInstanceGroupManagersRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_errors_empty_call_rest():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_errors), "__call__") as call:
        client.list_errors(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = compute.ListErrorsInstanceGroupManagersRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_managed_instances_empty_call_rest():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_managed_instances), "__call__"
    ) as call:
        client.list_managed_instances(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = compute.ListManagedInstancesInstanceGroupManagersRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_per_instance_configs_empty_call_rest():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_per_instance_configs), "__call__"
    ) as call:
        client.list_per_instance_configs(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = compute.ListPerInstanceConfigsInstanceGroupManagersRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_patch_unary_empty_call_rest():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.patch), "__call__") as call:
        client.patch_unary(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = compute.PatchInstanceGroupManagerRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_patch_per_instance_configs_unary_empty_call_rest():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.patch_per_instance_configs), "__call__"
    ) as call:
        client.patch_per_instance_configs_unary(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = compute.PatchPerInstanceConfigsInstanceGroupManagerRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_recreate_instances_unary_empty_call_rest():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.recreate_instances), "__call__"
    ) as call:
        client.recreate_instances_unary(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = compute.RecreateInstancesInstanceGroupManagerRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_resize_unary_empty_call_rest():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.resize), "__call__") as call:
        client.resize_unary(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = compute.ResizeInstanceGroupManagerRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_resume_instances_unary_empty_call_rest():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.resume_instances), "__call__") as call:
        client.resume_instances_unary(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = compute.ResumeInstancesInstanceGroupManagerRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_set_instance_template_unary_empty_call_rest():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.set_instance_template), "__call__"
    ) as call:
        client.set_instance_template_unary(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = compute.SetInstanceTemplateInstanceGroupManagerRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_set_target_pools_unary_empty_call_rest():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.set_target_pools), "__call__") as call:
        client.set_target_pools_unary(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = compute.SetTargetPoolsInstanceGroupManagerRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_start_instances_unary_empty_call_rest():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.start_instances), "__call__") as call:
        client.start_instances_unary(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = compute.StartInstancesInstanceGroupManagerRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_stop_instances_unary_empty_call_rest():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.stop_instances), "__call__") as call:
        client.stop_instances_unary(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = compute.StopInstancesInstanceGroupManagerRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_suspend_instances_unary_empty_call_rest():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.suspend_instances), "__call__"
    ) as call:
        client.suspend_instances_unary(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = compute.SuspendInstancesInstanceGroupManagerRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_per_instance_configs_unary_empty_call_rest():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_per_instance_configs), "__call__"
    ) as call:
        client.update_per_instance_configs_unary(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = compute.UpdatePerInstanceConfigsInstanceGroupManagerRequest()
        assert args[0] == request_msg


def test_instance_group_managers_base_transport_error():
    # Passing both a credentials object and credentials_file should raise an error
    with pytest.raises(core_exceptions.DuplicateCredentialArgs):
        transport = transports.InstanceGroupManagersTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            credentials_file="credentials.json",
        )


def test_instance_group_managers_base_transport():
    # Instantiate the base transport.
    with mock.patch(
        "google.cloud.compute_v1.services.instance_group_managers.transports.InstanceGroupManagersTransport.__init__"
    ) as Transport:
        Transport.return_value = None
        transport = transports.InstanceGroupManagersTransport(
            credentials=ga_credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        "abandon_instances",
        "aggregated_list",
        "apply_updates_to_instances",
        "create_instances",
        "delete",
        "delete_instances",
        "delete_per_instance_configs",
        "get",
        "insert",
        "list",
        "list_errors",
        "list_managed_instances",
        "list_per_instance_configs",
        "patch",
        "patch_per_instance_configs",
        "recreate_instances",
        "resize",
        "resume_instances",
        "set_instance_template",
        "set_target_pools",
        "start_instances",
        "stop_instances",
        "suspend_instances",
        "update_per_instance_configs",
    )
    for method in methods:
        with pytest.raises(NotImplementedError):
            getattr(transport, method)(request=object())

    with pytest.raises(NotImplementedError):
        transport.close()

    # Catch all for all remaining methods and properties
    remainder = [
        "kind",
    ]
    for r in remainder:
        with pytest.raises(NotImplementedError):
            getattr(transport, r)()


def test_instance_group_managers_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with (
        mock.patch.object(
            google.auth, "load_credentials_from_file", autospec=True
        ) as load_creds,
        mock.patch(
            "google.cloud.compute_v1.services.instance_group_managers.transports.InstanceGroupManagersTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        load_creds.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.InstanceGroupManagersTransport(
            credentials_file="credentials.json",
            quota_project_id="octopus",
        )
        load_creds.assert_called_once_with(
            "credentials.json",
            scopes=None,
            default_scopes=(
                "https://www.googleapis.com/auth/compute",
                "https://www.googleapis.com/auth/cloud-platform",
            ),
            quota_project_id="octopus",
        )


def test_instance_group_managers_base_transport_with_adc():
    # Test the default credentials are used if credentials and credentials_file are None.
    with (
        mock.patch.object(google.auth, "default", autospec=True) as adc,
        mock.patch(
            "google.cloud.compute_v1.services.instance_group_managers.transports.InstanceGroupManagersTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.InstanceGroupManagersTransport()
        adc.assert_called_once()


def test_instance_group_managers_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        InstanceGroupManagersClient()
        adc.assert_called_once_with(
            scopes=None,
            default_scopes=(
                "https://www.googleapis.com/auth/compute",
                "https://www.googleapis.com/auth/cloud-platform",
            ),
            quota_project_id=None,
        )


def test_instance_group_managers_http_transport_client_cert_source_for_mtls():
    cred = ga_credentials.AnonymousCredentials()
    with mock.patch(
        "google.auth.transport.requests.AuthorizedSession.configure_mtls_channel"
    ) as mock_configure_mtls_channel:
        transports.InstanceGroupManagersRestTransport(
            credentials=cred, client_cert_source_for_mtls=client_cert_source_callback
        )
        mock_configure_mtls_channel.assert_called_once_with(client_cert_source_callback)


@pytest.mark.parametrize(
    "transport_name",
    [
        "rest",
    ],
)
def test_instance_group_managers_host_no_port(transport_name):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="compute.googleapis.com"
        ),
        transport=transport_name,
    )
    assert client.transport._host == (
        "compute.googleapis.com:443"
        if transport_name in ["grpc", "grpc_asyncio"]
        else "https://compute.googleapis.com"
    )


@pytest.mark.parametrize(
    "transport_name",
    [
        "rest",
    ],
)
def test_instance_group_managers_host_with_port(transport_name):
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="compute.googleapis.com:8000"
        ),
        transport=transport_name,
    )
    assert client.transport._host == (
        "compute.googleapis.com:8000"
        if transport_name in ["grpc", "grpc_asyncio"]
        else "https://compute.googleapis.com:8000"
    )


@pytest.mark.parametrize(
    "transport_name",
    [
        "rest",
    ],
)
def test_instance_group_managers_client_transport_session_collision(transport_name):
    creds1 = ga_credentials.AnonymousCredentials()
    creds2 = ga_credentials.AnonymousCredentials()
    client1 = InstanceGroupManagersClient(
        credentials=creds1,
        transport=transport_name,
    )
    client2 = InstanceGroupManagersClient(
        credentials=creds2,
        transport=transport_name,
    )
    session1 = client1.transport.abandon_instances._session
    session2 = client2.transport.abandon_instances._session
    assert session1 != session2
    session1 = client1.transport.aggregated_list._session
    session2 = client2.transport.aggregated_list._session
    assert session1 != session2
    session1 = client1.transport.apply_updates_to_instances._session
    session2 = client2.transport.apply_updates_to_instances._session
    assert session1 != session2
    session1 = client1.transport.create_instances._session
    session2 = client2.transport.create_instances._session
    assert session1 != session2
    session1 = client1.transport.delete._session
    session2 = client2.transport.delete._session
    assert session1 != session2
    session1 = client1.transport.delete_instances._session
    session2 = client2.transport.delete_instances._session
    assert session1 != session2
    session1 = client1.transport.delete_per_instance_configs._session
    session2 = client2.transport.delete_per_instance_configs._session
    assert session1 != session2
    session1 = client1.transport.get._session
    session2 = client2.transport.get._session
    assert session1 != session2
    session1 = client1.transport.insert._session
    session2 = client2.transport.insert._session
    assert session1 != session2
    session1 = client1.transport.list._session
    session2 = client2.transport.list._session
    assert session1 != session2
    session1 = client1.transport.list_errors._session
    session2 = client2.transport.list_errors._session
    assert session1 != session2
    session1 = client1.transport.list_managed_instances._session
    session2 = client2.transport.list_managed_instances._session
    assert session1 != session2
    session1 = client1.transport.list_per_instance_configs._session
    session2 = client2.transport.list_per_instance_configs._session
    assert session1 != session2
    session1 = client1.transport.patch._session
    session2 = client2.transport.patch._session
    assert session1 != session2
    session1 = client1.transport.patch_per_instance_configs._session
    session2 = client2.transport.patch_per_instance_configs._session
    assert session1 != session2
    session1 = client1.transport.recreate_instances._session
    session2 = client2.transport.recreate_instances._session
    assert session1 != session2
    session1 = client1.transport.resize._session
    session2 = client2.transport.resize._session
    assert session1 != session2
    session1 = client1.transport.resume_instances._session
    session2 = client2.transport.resume_instances._session
    assert session1 != session2
    session1 = client1.transport.set_instance_template._session
    session2 = client2.transport.set_instance_template._session
    assert session1 != session2
    session1 = client1.transport.set_target_pools._session
    session2 = client2.transport.set_target_pools._session
    assert session1 != session2
    session1 = client1.transport.start_instances._session
    session2 = client2.transport.start_instances._session
    assert session1 != session2
    session1 = client1.transport.stop_instances._session
    session2 = client2.transport.stop_instances._session
    assert session1 != session2
    session1 = client1.transport.suspend_instances._session
    session2 = client2.transport.suspend_instances._session
    assert session1 != session2
    session1 = client1.transport.update_per_instance_configs._session
    session2 = client2.transport.update_per_instance_configs._session
    assert session1 != session2


def test_common_billing_account_path():
    billing_account = "squid"
    expected = "billingAccounts/{billing_account}".format(
        billing_account=billing_account,
    )
    actual = InstanceGroupManagersClient.common_billing_account_path(billing_account)
    assert expected == actual


def test_parse_common_billing_account_path():
    expected = {
        "billing_account": "clam",
    }
    path = InstanceGroupManagersClient.common_billing_account_path(**expected)

    # Check that the path construction is reversible.
    actual = InstanceGroupManagersClient.parse_common_billing_account_path(path)
    assert expected == actual


def test_common_folder_path():
    folder = "whelk"
    expected = "folders/{folder}".format(
        folder=folder,
    )
    actual = InstanceGroupManagersClient.common_folder_path(folder)
    assert expected == actual


def test_parse_common_folder_path():
    expected = {
        "folder": "octopus",
    }
    path = InstanceGroupManagersClient.common_folder_path(**expected)

    # Check that the path construction is reversible.
    actual = InstanceGroupManagersClient.parse_common_folder_path(path)
    assert expected == actual


def test_common_organization_path():
    organization = "oyster"
    expected = "organizations/{organization}".format(
        organization=organization,
    )
    actual = InstanceGroupManagersClient.common_organization_path(organization)
    assert expected == actual


def test_parse_common_organization_path():
    expected = {
        "organization": "nudibranch",
    }
    path = InstanceGroupManagersClient.common_organization_path(**expected)

    # Check that the path construction is reversible.
    actual = InstanceGroupManagersClient.parse_common_organization_path(path)
    assert expected == actual


def test_common_project_path():
    project = "cuttlefish"
    expected = "projects/{project}".format(
        project=project,
    )
    actual = InstanceGroupManagersClient.common_project_path(project)
    assert expected == actual


def test_parse_common_project_path():
    expected = {
        "project": "mussel",
    }
    path = InstanceGroupManagersClient.common_project_path(**expected)

    # Check that the path construction is reversible.
    actual = InstanceGroupManagersClient.parse_common_project_path(path)
    assert expected == actual


def test_common_location_path():
    project = "winkle"
    location = "nautilus"
    expected = "projects/{project}/locations/{location}".format(
        project=project,
        location=location,
    )
    actual = InstanceGroupManagersClient.common_location_path(project, location)
    assert expected == actual


def test_parse_common_location_path():
    expected = {
        "project": "scallop",
        "location": "abalone",
    }
    path = InstanceGroupManagersClient.common_location_path(**expected)

    # Check that the path construction is reversible.
    actual = InstanceGroupManagersClient.parse_common_location_path(path)
    assert expected == actual


def test_client_with_default_client_info():
    client_info = gapic_v1.client_info.ClientInfo()

    with mock.patch.object(
        transports.InstanceGroupManagersTransport, "_prep_wrapped_messages"
    ) as prep:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

    with mock.patch.object(
        transports.InstanceGroupManagersTransport, "_prep_wrapped_messages"
    ) as prep:
        transport_class = InstanceGroupManagersClient.get_transport_class()
        transport = transport_class(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)


def test_transport_close_rest():
    client = InstanceGroupManagersClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    with mock.patch.object(
        type(getattr(client.transport, "_session")), "close"
    ) as close:
        with client:
            close.assert_not_called()
        close.assert_called_once()


def test_client_ctx():
    transports = [
        "rest",
    ]
    for transport in transports:
        client = InstanceGroupManagersClient(
            credentials=ga_credentials.AnonymousCredentials(), transport=transport
        )
        # Test client calls underlying transport.
        with mock.patch.object(type(client.transport), "close") as close:
            close.assert_not_called()
            with client:
                pass
            close.assert_called()


@pytest.mark.parametrize(
    "client_class,transport_class",
    [
        (InstanceGroupManagersClient, transports.InstanceGroupManagersRestTransport),
    ],
)
def test_api_key_credentials(client_class, transport_class):
    with mock.patch.object(
        google.auth._default, "get_api_key_credentials", create=True
    ) as get_api_key_credentials:
        mock_cred = mock.Mock()
        get_api_key_credentials.return_value = mock_cred
        options = client_options.ClientOptions()
        options.api_key = "api_key"
        with mock.patch.object(transport_class, "__init__") as patched:
            patched.return_value = None
            client = client_class(client_options=options)
            patched.assert_called_once_with(
                credentials=mock_cred,
                credentials_file=None,
                host=client._DEFAULT_ENDPOINT_TEMPLATE.format(
                    UNIVERSE_DOMAIN=client._DEFAULT_UNIVERSE
                ),
                scopes=None,
                client_cert_source_for_mtls=None,
                quota_project_id=None,
                client_info=transports.base.DEFAULT_CLIENT_INFO,
                always_use_jwt_access=True,
                api_audience=None,
            )
