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

import google.auth
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.type.dayofweek_pb2 as dayofweek_pb2  # type: ignore
import google.type.interval_pb2 as interval_pb2  # type: ignore
import google.type.money_pb2 as money_pb2  # type: ignore
import google.type.timeofday_pb2 as timeofday_pb2  # type: ignore
from google.api_core import (
    client_options,
    gapic_v1,
    grpc_helpers,
    grpc_helpers_async,
    path_template,
)
from google.api_core import exceptions as core_exceptions
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials
from google.auth.exceptions import MutualTLSChannelError
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account

from google.ads.admanager_v1.services.proposal_service import (
    ProposalServiceClient,
    pagers,
    transports,
)
from google.ads.admanager_v1.types import (
    applied_label,
    creative_placeholder,
    custom_field_value,
    dayparting_time_zone_enum,
    proposal_enums,
    proposal_environment_type_enum,
    proposal_messages,
    proposal_negotiation_status_enum,
    proposal_service,
    request_platform_enum,
    size,
    size_type_enum,
    supply_path_type_enum,
    targeted_video_bumper_type_enum,
    targeting,
    video_position_enum,
)

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

    assert ProposalServiceClient._get_client_cert_source(None, False) is None
    assert (
        ProposalServiceClient._get_client_cert_source(mock_provided_cert_source, False)
        is None
    )
    assert (
        ProposalServiceClient._get_client_cert_source(mock_provided_cert_source, True)
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
                ProposalServiceClient._get_client_cert_source(None, True)
                is mock_default_cert_source
            )
            assert (
                ProposalServiceClient._get_client_cert_source(
                    mock_provided_cert_source, "true"
                )
                is mock_provided_cert_source
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
    client = ProposalServiceClient(credentials=cred)
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
    client = ProposalServiceClient(credentials=cred)
    client._transport._credentials = cred

    error = core_exceptions.GoogleAPICallError("message", details=[])
    error.code = error_code

    client._add_cred_info_for_auth_errors(error)
    assert error.details == []


@pytest.mark.parametrize(
    "client_class,transport_name",
    [
        (ProposalServiceClient, "rest"),
    ],
)
def test_proposal_service_client_from_service_account_info(
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
            "admanager.googleapis.com:443"
            if transport_name in ["grpc", "grpc_asyncio"]
            else "https://admanager.googleapis.com"
        )


@pytest.mark.parametrize(
    "transport_class,transport_name",
    [
        (transports.ProposalServiceRestTransport, "rest"),
    ],
)
def test_proposal_service_client_service_account_always_use_jwt(
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
        (ProposalServiceClient, "rest"),
    ],
)
def test_proposal_service_client_from_service_account_file(
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
            "admanager.googleapis.com:443"
            if transport_name in ["grpc", "grpc_asyncio"]
            else "https://admanager.googleapis.com"
        )


def test_proposal_service_client_get_transport_class():
    transport = ProposalServiceClient.get_transport_class()
    available_transports = [
        transports.ProposalServiceRestTransport,
    ]
    assert transport in available_transports

    transport = ProposalServiceClient.get_transport_class("rest")
    assert transport == transports.ProposalServiceRestTransport


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (ProposalServiceClient, transports.ProposalServiceRestTransport, "rest"),
    ],
)
@mock.patch.object(
    ProposalServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(ProposalServiceClient),
)
def test_proposal_service_client_client_options(
    client_class, transport_class, transport_name
):
    # Check that if channel is provided we won't create a new one.
    with mock.patch.object(ProposalServiceClient, "get_transport_class") as gtc:
        transport = transport_class(credentials=ga_credentials.AnonymousCredentials())
        client = client_class(transport=transport)
        gtc.assert_not_called()

    # Check that if channel is provided via str we will create a new one.
    with mock.patch.object(ProposalServiceClient, "get_transport_class") as gtc:
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
            ProposalServiceClient,
            transports.ProposalServiceRestTransport,
            "rest",
            "true",
        ),
        (
            ProposalServiceClient,
            transports.ProposalServiceRestTransport,
            "rest",
            "false",
        ),
    ],
)
@mock.patch.object(
    ProposalServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(ProposalServiceClient),
)
@mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "auto"})
def test_proposal_service_client_mtls_env_auto(
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


@pytest.mark.parametrize("client_class", [ProposalServiceClient])
@mock.patch.object(
    ProposalServiceClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(ProposalServiceClient),
)
def test_proposal_service_client_get_mtls_endpoint_and_cert_source(client_class):
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


@pytest.mark.parametrize("client_class", [ProposalServiceClient])
@mock.patch.object(
    ProposalServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(ProposalServiceClient),
)
def test_proposal_service_client_client_api_endpoint(client_class):
    mock_client_cert_source = client_cert_source_callback
    api_override = "foo.com"
    default_universe = ProposalServiceClient._DEFAULT_UNIVERSE
    default_endpoint = ProposalServiceClient._DEFAULT_ENDPOINT_TEMPLATE.format(
        UNIVERSE_DOMAIN=default_universe
    )
    mock_universe = "bar.com"
    mock_endpoint = ProposalServiceClient._DEFAULT_ENDPOINT_TEMPLATE.format(
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
        (ProposalServiceClient, transports.ProposalServiceRestTransport, "rest"),
    ],
)
def test_proposal_service_client_client_options_scopes(
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
        (ProposalServiceClient, transports.ProposalServiceRestTransport, "rest", None),
    ],
)
def test_proposal_service_client_client_options_credentials_file(
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


def test_get_proposal_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = ProposalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_proposal in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_proposal] = mock_rpc

        request = {}
        client.get_proposal(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_proposal(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_proposal_rest_required_fields(
    request_type=proposal_service.GetProposalRequest,
):
    transport_class = transports.ProposalServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGetProposal,
        "_BaseGetProposal__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["name"] = "name_value"

    # verify required fields with non-default values are left alone
    assert "name" in jsonified_request
    assert jsonified_request["name"] == "name_value"

    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = proposal_messages.Proposal()
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
            return_value = proposal_messages.Proposal.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get_proposal(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_proposal_rest_flattened():
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = proposal_messages.Proposal()

        # get arguments that satisfy an http rule for this method
        sample_request = {"name": "networks/sample1/proposals/sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = proposal_messages.Proposal.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get_proposal(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{name=networks/*/proposals/*}" % client.transport._host, args[1]
        )


def test_get_proposal_rest_flattened_error(transport: str = "rest"):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_proposal(
            proposal_service.GetProposalRequest(),
            name="name_value",
        )


def test_list_proposals_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = ProposalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_proposals in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_proposals] = mock_rpc

        request = {}
        client.list_proposals(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_proposals(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_proposals_rest_required_fields(
    request_type=proposal_service.ListProposalsRequest,
):
    transport_class = transports.ProposalServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseListProposals,
        "_BaseListProposals__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["parent"] = "parent_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "filter",
            "orderBy",
            "pageSize",
            "pageToken",
            "skip",
        )
    )

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"

    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = proposal_service.ListProposalsResponse()
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
            return_value = proposal_service.ListProposalsResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_proposals(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_proposals_rest_flattened():
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = proposal_service.ListProposalsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "networks/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = proposal_service.ListProposalsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_proposals(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/proposals" % client.transport._host, args[1]
        )


def test_list_proposals_rest_flattened_error(transport: str = "rest"):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_proposals(
            proposal_service.ListProposalsRequest(),
            parent="parent_value",
        )


def test_list_proposals_rest_pager(transport: str = "rest"):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            proposal_service.ListProposalsResponse(
                proposals=[
                    proposal_messages.Proposal(),
                    proposal_messages.Proposal(),
                    proposal_messages.Proposal(),
                ],
                next_page_token="abc",
            ),
            proposal_service.ListProposalsResponse(
                proposals=[],
                next_page_token="def",
            ),
            proposal_service.ListProposalsResponse(
                proposals=[
                    proposal_messages.Proposal(),
                ],
                next_page_token="ghi",
            ),
            proposal_service.ListProposalsResponse(
                proposals=[
                    proposal_messages.Proposal(),
                    proposal_messages.Proposal(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            proposal_service.ListProposalsResponse.to_json(x) for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {"parent": "networks/sample1"}

        pager = client.list_proposals(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, proposal_messages.Proposal) for i in results)

        pages = list(client.list_proposals(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_create_proposal_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = ProposalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.create_proposal in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.create_proposal] = mock_rpc

        request = {}
        client.create_proposal(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.create_proposal(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_create_proposal_rest_required_fields(
    request_type=proposal_service.CreateProposalRequest,
):
    transport_class = transports.ProposalServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseCreateProposal,
        "_BaseCreateProposal__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["parent"] = "parent_value"

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"

    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = proposal_messages.Proposal()
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
            return_value = proposal_messages.Proposal.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.create_proposal(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_create_proposal_rest_flattened():
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = proposal_messages.Proposal()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "networks/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            proposal=proposal_messages.Proposal(name="name_value"),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = proposal_messages.Proposal.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.create_proposal(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/proposals" % client.transport._host, args[1]
        )


def test_create_proposal_rest_flattened_error(transport: str = "rest"):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_proposal(
            proposal_service.CreateProposalRequest(),
            parent="parent_value",
            proposal=proposal_messages.Proposal(name="name_value"),
        )


def test_batch_create_proposals_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = ProposalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_create_proposals
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.batch_create_proposals] = (
            mock_rpc
        )

        request = {}
        client.batch_create_proposals(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_create_proposals(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_create_proposals_rest_required_fields(
    request_type=proposal_service.BatchCreateProposalsRequest,
):
    transport_class = transports.ProposalServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseBatchCreateProposals,
        "_BaseBatchCreateProposals__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["parent"] = "parent_value"

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"

    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = proposal_service.BatchCreateProposalsResponse()
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
            return_value = proposal_service.BatchCreateProposalsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.batch_create_proposals(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_create_proposals_rest_flattened():
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = proposal_service.BatchCreateProposalsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "networks/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            requests=[proposal_service.CreateProposalRequest(parent="parent_value")],
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = proposal_service.BatchCreateProposalsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.batch_create_proposals(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/proposals:batchCreate" % client.transport._host,
            args[1],
        )


def test_batch_create_proposals_rest_flattened_error(transport: str = "rest"):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_create_proposals(
            proposal_service.BatchCreateProposalsRequest(),
            parent="parent_value",
            requests=[proposal_service.CreateProposalRequest(parent="parent_value")],
        )


def test_update_proposal_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = ProposalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.update_proposal in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.update_proposal] = mock_rpc

        request = {}
        client.update_proposal(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.update_proposal(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_update_proposal_rest_required_fields(
    request_type=proposal_service.UpdateProposalRequest,
):
    transport_class = transports.ProposalServiceRestTransport

    request_init = {}
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseUpdateProposal,
        "_BaseUpdateProposal__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(("updateMask",))

    # verify required fields with non-default values are left alone

    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = proposal_messages.Proposal()
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
            return_value = proposal_messages.Proposal.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.update_proposal(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_update_proposal_rest_flattened():
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = proposal_messages.Proposal()

        # get arguments that satisfy an http rule for this method
        sample_request = {"proposal": {"name": "networks/sample1/proposals/sample2"}}

        # get truthy value for each flattened field
        mock_args = dict(
            proposal=proposal_messages.Proposal(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = proposal_messages.Proposal.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.update_proposal(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{proposal.name=networks/*/proposals/*}" % client.transport._host,
            args[1],
        )


def test_update_proposal_rest_flattened_error(transport: str = "rest"):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_proposal(
            proposal_service.UpdateProposalRequest(),
            proposal=proposal_messages.Proposal(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


def test_batch_update_proposals_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = ProposalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_update_proposals
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.batch_update_proposals] = (
            mock_rpc
        )

        request = {}
        client.batch_update_proposals(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_update_proposals(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_update_proposals_rest_required_fields(
    request_type=proposal_service.BatchUpdateProposalsRequest,
):
    transport_class = transports.ProposalServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseBatchUpdateProposals,
        "_BaseBatchUpdateProposals__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["parent"] = "parent_value"

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"

    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = proposal_service.BatchUpdateProposalsResponse()
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
            return_value = proposal_service.BatchUpdateProposalsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.batch_update_proposals(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_update_proposals_rest_flattened():
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = proposal_service.BatchUpdateProposalsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "networks/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            requests=[
                proposal_service.UpdateProposalRequest(
                    proposal=proposal_messages.Proposal(name="name_value")
                )
            ],
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = proposal_service.BatchUpdateProposalsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.batch_update_proposals(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/proposals:batchUpdate" % client.transport._host,
            args[1],
        )


def test_batch_update_proposals_rest_flattened_error(transport: str = "rest"):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_update_proposals(
            proposal_service.BatchUpdateProposalsRequest(),
            parent="parent_value",
            requests=[
                proposal_service.UpdateProposalRequest(
                    proposal=proposal_messages.Proposal(name="name_value")
                )
            ],
        )


def test_batch_archive_proposals_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = ProposalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_archive_proposals
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.batch_archive_proposals
        ] = mock_rpc

        request = {}
        client.batch_archive_proposals(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_archive_proposals(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_archive_proposals_rest_required_fields(
    request_type=proposal_service.BatchArchiveProposalsRequest,
):
    transport_class = transports.ProposalServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request_init["names"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseBatchArchiveProposals,
        "_BaseBatchArchiveProposals__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["parent"] = "parent_value"
    jsonified_request["names"] = "names_value"

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"
    assert "names" in jsonified_request
    assert jsonified_request["names"] == "names_value"

    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = proposal_service.BatchArchiveProposalsResponse()
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
            return_value = proposal_service.BatchArchiveProposalsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.batch_archive_proposals(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_archive_proposals_rest_flattened():
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = proposal_service.BatchArchiveProposalsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "networks/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            names=["names_value"],
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = proposal_service.BatchArchiveProposalsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.batch_archive_proposals(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/proposals:batchArchive" % client.transport._host,
            args[1],
        )


def test_batch_archive_proposals_rest_flattened_error(transport: str = "rest"):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_archive_proposals(
            proposal_service.BatchArchiveProposalsRequest(),
            parent="parent_value",
            names=["names_value"],
        )


def test_batch_unarchive_proposals_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = ProposalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_unarchive_proposals
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.batch_unarchive_proposals
        ] = mock_rpc

        request = {}
        client.batch_unarchive_proposals(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_unarchive_proposals(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_unarchive_proposals_rest_required_fields(
    request_type=proposal_service.BatchUnarchiveProposalsRequest,
):
    transport_class = transports.ProposalServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request_init["names"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseBatchUnarchiveProposals,
        "_BaseBatchUnarchiveProposals__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["parent"] = "parent_value"
    jsonified_request["names"] = "names_value"

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"
    assert "names" in jsonified_request
    assert jsonified_request["names"] == "names_value"

    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = proposal_service.BatchUnarchiveProposalsResponse()
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
            return_value = proposal_service.BatchUnarchiveProposalsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.batch_unarchive_proposals(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_unarchive_proposals_rest_flattened():
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = proposal_service.BatchUnarchiveProposalsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "networks/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            names=["names_value"],
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = proposal_service.BatchUnarchiveProposalsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.batch_unarchive_proposals(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/proposals:batchUnarchive"
            % client.transport._host,
            args[1],
        )


def test_batch_unarchive_proposals_rest_flattened_error(transport: str = "rest"):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_unarchive_proposals(
            proposal_service.BatchUnarchiveProposalsRequest(),
            parent="parent_value",
            names=["names_value"],
        )


def test_batch_pause_proposals_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = ProposalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_pause_proposals
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.batch_pause_proposals] = (
            mock_rpc
        )

        request = {}
        client.batch_pause_proposals(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_pause_proposals(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_pause_proposals_rest_required_fields(
    request_type=proposal_service.BatchPauseProposalsRequest,
):
    transport_class = transports.ProposalServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request_init["names"] = ""
    request_init["reason"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseBatchPauseProposals,
        "_BaseBatchPauseProposals__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["parent"] = "parent_value"
    jsonified_request["names"] = "names_value"
    jsonified_request["reason"] = "reason_value"

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"
    assert "names" in jsonified_request
    assert jsonified_request["names"] == "names_value"
    assert "reason" in jsonified_request
    assert jsonified_request["reason"] == "reason_value"

    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = proposal_service.BatchPauseProposalsResponse()
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
            return_value = proposal_service.BatchPauseProposalsResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.batch_pause_proposals(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_pause_proposals_rest_flattened():
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = proposal_service.BatchPauseProposalsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "networks/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            names=["names_value"],
            reason="reason_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = proposal_service.BatchPauseProposalsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.batch_pause_proposals(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/proposals:batchPause" % client.transport._host,
            args[1],
        )


def test_batch_pause_proposals_rest_flattened_error(transport: str = "rest"):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_pause_proposals(
            proposal_service.BatchPauseProposalsRequest(),
            parent="parent_value",
            names=["names_value"],
            reason="reason_value",
        )


def test_batch_resume_proposals_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = ProposalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_resume_proposals
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.batch_resume_proposals] = (
            mock_rpc
        )

        request = {}
        client.batch_resume_proposals(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_resume_proposals(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_resume_proposals_rest_required_fields(
    request_type=proposal_service.BatchResumeProposalsRequest,
):
    transport_class = transports.ProposalServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request_init["names"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseBatchResumeProposals,
        "_BaseBatchResumeProposals__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["parent"] = "parent_value"
    jsonified_request["names"] = "names_value"

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"
    assert "names" in jsonified_request
    assert jsonified_request["names"] == "names_value"

    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = proposal_service.BatchResumeProposalsResponse()
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
            return_value = proposal_service.BatchResumeProposalsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.batch_resume_proposals(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_resume_proposals_rest_flattened():
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = proposal_service.BatchResumeProposalsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "networks/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            names=["names_value"],
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = proposal_service.BatchResumeProposalsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.batch_resume_proposals(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/proposals:batchResume" % client.transport._host,
            args[1],
        )


def test_batch_resume_proposals_rest_flattened_error(transport: str = "rest"):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_resume_proposals(
            proposal_service.BatchResumeProposalsRequest(),
            parent="parent_value",
            names=["names_value"],
        )


def test_batch_request_buyer_review_proposals_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = ProposalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_request_buyer_review_proposals
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.batch_request_buyer_review_proposals
        ] = mock_rpc

        request = {}
        client.batch_request_buyer_review_proposals(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_request_buyer_review_proposals(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_request_buyer_review_proposals_rest_required_fields(
    request_type=proposal_service.BatchRequestBuyerReviewProposalsRequest,
):
    transport_class = transports.ProposalServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request_init["names"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseBatchRequestBuyerReviewProposals,
        "_BaseBatchRequestBuyerReviewProposals__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["parent"] = "parent_value"
    jsonified_request["names"] = "names_value"

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"
    assert "names" in jsonified_request
    assert jsonified_request["names"] == "names_value"

    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = proposal_service.BatchRequestBuyerReviewProposalsResponse()
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
            return_value = proposal_service.BatchRequestBuyerReviewProposalsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.batch_request_buyer_review_proposals(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_request_buyer_review_proposals_rest_flattened():
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = proposal_service.BatchRequestBuyerReviewProposalsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "networks/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            names=["names_value"],
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = proposal_service.BatchRequestBuyerReviewProposalsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.batch_request_buyer_review_proposals(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/proposals:batchRequestBuyerReview"
            % client.transport._host,
            args[1],
        )


def test_batch_request_buyer_review_proposals_rest_flattened_error(
    transport: str = "rest",
):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_request_buyer_review_proposals(
            proposal_service.BatchRequestBuyerReviewProposalsRequest(),
            parent="parent_value",
            names=["names_value"],
        )


def test_batch_request_buyer_accept_proposals_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = ProposalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_request_buyer_accept_proposals
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.batch_request_buyer_accept_proposals
        ] = mock_rpc

        request = {}
        client.batch_request_buyer_accept_proposals(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_request_buyer_accept_proposals(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_request_buyer_accept_proposals_rest_required_fields(
    request_type=proposal_service.BatchRequestBuyerAcceptProposalsRequest,
):
    transport_class = transports.ProposalServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request_init["names"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseBatchRequestBuyerAcceptProposals,
        "_BaseBatchRequestBuyerAcceptProposals__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["parent"] = "parent_value"
    jsonified_request["names"] = "names_value"

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"
    assert "names" in jsonified_request
    assert jsonified_request["names"] == "names_value"

    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = proposal_service.BatchRequestBuyerAcceptProposalsResponse()
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
            return_value = proposal_service.BatchRequestBuyerAcceptProposalsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.batch_request_buyer_accept_proposals(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_request_buyer_accept_proposals_rest_flattened():
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = proposal_service.BatchRequestBuyerAcceptProposalsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "networks/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            names=["names_value"],
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = proposal_service.BatchRequestBuyerAcceptProposalsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.batch_request_buyer_accept_proposals(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/proposals:batchRequestBuyerAccept"
            % client.transport._host,
            args[1],
        )


def test_batch_request_buyer_accept_proposals_rest_flattened_error(
    transport: str = "rest",
):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_request_buyer_accept_proposals(
            proposal_service.BatchRequestBuyerAcceptProposalsRequest(),
            parent="parent_value",
            names=["names_value"],
        )


def test_batch_reserve_proposals_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = ProposalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_reserve_proposals
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.batch_reserve_proposals
        ] = mock_rpc

        request = {}
        client.batch_reserve_proposals(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_reserve_proposals(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_reserve_proposals_rest_required_fields(
    request_type=proposal_service.BatchReserveProposalsRequest,
):
    transport_class = transports.ProposalServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request_init["names"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseBatchReserveProposals,
        "_BaseBatchReserveProposals__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["parent"] = "parent_value"
    jsonified_request["names"] = "names_value"

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"
    assert "names" in jsonified_request
    assert jsonified_request["names"] == "names_value"

    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = proposal_service.BatchReserveProposalsResponse()
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
            return_value = proposal_service.BatchReserveProposalsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.batch_reserve_proposals(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_reserve_proposals_rest_flattened():
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = proposal_service.BatchReserveProposalsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "networks/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            names=["names_value"],
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = proposal_service.BatchReserveProposalsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.batch_reserve_proposals(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/proposals:batchReserve" % client.transport._host,
            args[1],
        )


def test_batch_reserve_proposals_rest_flattened_error(transport: str = "rest"):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_reserve_proposals(
            proposal_service.BatchReserveProposalsRequest(),
            parent="parent_value",
            names=["names_value"],
        )


def test_batch_redraft_proposals_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = ProposalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_redraft_proposals
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.batch_redraft_proposals
        ] = mock_rpc

        request = {}
        client.batch_redraft_proposals(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_redraft_proposals(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_redraft_proposals_rest_required_fields(
    request_type=proposal_service.BatchRedraftProposalsRequest,
):
    transport_class = transports.ProposalServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request_init["names"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseBatchRedraftProposals,
        "_BaseBatchRedraftProposals__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["parent"] = "parent_value"
    jsonified_request["names"] = "names_value"

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"
    assert "names" in jsonified_request
    assert jsonified_request["names"] == "names_value"

    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = proposal_service.BatchRedraftProposalsResponse()
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
            return_value = proposal_service.BatchRedraftProposalsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.batch_redraft_proposals(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_redraft_proposals_rest_flattened():
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = proposal_service.BatchRedraftProposalsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "networks/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            names=["names_value"],
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = proposal_service.BatchRedraftProposalsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.batch_redraft_proposals(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/proposals:batchRedraft" % client.transport._host,
            args[1],
        )


def test_batch_redraft_proposals_rest_flattened_error(transport: str = "rest"):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_redraft_proposals(
            proposal_service.BatchRedraftProposalsRequest(),
            parent="parent_value",
            names=["names_value"],
        )


def test_batch_discard_draft_proposals_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = ProposalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_discard_draft_proposals
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.batch_discard_draft_proposals
        ] = mock_rpc

        request = {}
        client.batch_discard_draft_proposals(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_discard_draft_proposals(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_discard_draft_proposals_rest_required_fields(
    request_type=proposal_service.BatchDiscardDraftProposalsRequest,
):
    transport_class = transports.ProposalServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request_init["names"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseBatchDiscardDraftProposals,
        "_BaseBatchDiscardDraftProposals__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["parent"] = "parent_value"
    jsonified_request["names"] = "names_value"

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"
    assert "names" in jsonified_request
    assert jsonified_request["names"] == "names_value"

    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = proposal_service.BatchDiscardDraftProposalsResponse()
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
            return_value = proposal_service.BatchDiscardDraftProposalsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.batch_discard_draft_proposals(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_discard_draft_proposals_rest_flattened():
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = proposal_service.BatchDiscardDraftProposalsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "networks/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            names=["names_value"],
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = proposal_service.BatchDiscardDraftProposalsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.batch_discard_draft_proposals(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/proposals:batchDiscardDraft"
            % client.transport._host,
            args[1],
        )


def test_batch_discard_draft_proposals_rest_flattened_error(transport: str = "rest"):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_discard_draft_proposals(
            proposal_service.BatchDiscardDraftProposalsRequest(),
            parent="parent_value",
            names=["names_value"],
        )


def test_batch_terminate_proposals_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = ProposalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_terminate_proposals
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.batch_terminate_proposals
        ] = mock_rpc

        request = {}
        client.batch_terminate_proposals(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_terminate_proposals(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_terminate_proposals_rest_required_fields(
    request_type=proposal_service.BatchTerminateProposalsRequest,
):
    transport_class = transports.ProposalServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request_init["names"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseBatchTerminateProposals,
        "_BaseBatchTerminateProposals__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["parent"] = "parent_value"
    jsonified_request["names"] = "names_value"

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"
    assert "names" in jsonified_request
    assert jsonified_request["names"] == "names_value"

    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = proposal_service.BatchTerminateProposalsResponse()
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
            return_value = proposal_service.BatchTerminateProposalsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.batch_terminate_proposals(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_terminate_proposals_rest_flattened():
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = proposal_service.BatchTerminateProposalsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "networks/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            names=["names_value"],
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = proposal_service.BatchTerminateProposalsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.batch_terminate_proposals(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/proposals:batchTerminate"
            % client.transport._host,
            args[1],
        )


def test_batch_terminate_proposals_rest_flattened_error(transport: str = "rest"):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_terminate_proposals(
            proposal_service.BatchTerminateProposalsRequest(),
            parent="parent_value",
            names=["names_value"],
        )


def test_batch_push_to_order_proposals_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = ProposalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_push_to_order_proposals
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.batch_push_to_order_proposals
        ] = mock_rpc

        request = {}
        client.batch_push_to_order_proposals(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_push_to_order_proposals(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_push_to_order_proposals_rest_required_fields(
    request_type=proposal_service.BatchPushToOrderProposalsRequest,
):
    transport_class = transports.ProposalServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request_init["names"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseBatchPushToOrderProposals,
        "_BaseBatchPushToOrderProposals__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present

    jsonified_request["parent"] = "parent_value"
    jsonified_request["names"] = "names_value"

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"
    assert "names" in jsonified_request
    assert jsonified_request["names"] == "names_value"

    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = proposal_service.BatchPushToOrderProposalsResponse()
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
            return_value = proposal_service.BatchPushToOrderProposalsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.batch_push_to_order_proposals(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_push_to_order_proposals_rest_flattened():
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = proposal_service.BatchPushToOrderProposalsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "networks/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            names=["names_value"],
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = proposal_service.BatchPushToOrderProposalsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.batch_push_to_order_proposals(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/proposals:batchPushToOrder"
            % client.transport._host,
            args[1],
        )


def test_batch_push_to_order_proposals_rest_flattened_error(transport: str = "rest"):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_push_to_order_proposals(
            proposal_service.BatchPushToOrderProposalsRequest(),
            parent="parent_value",
            names=["names_value"],
        )


def test_fetch_marketplace_comments_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = ProposalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.fetch_marketplace_comments
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.fetch_marketplace_comments
        ] = mock_rpc

        request = {}
        client.fetch_marketplace_comments(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.fetch_marketplace_comments(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_fetch_marketplace_comments_rest_required_fields(
    request_type=proposal_service.FetchMarketplaceCommentsRequest,
):
    transport_class = transports.ProposalServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request_init["names"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped
    assert "names" not in jsonified_request

    default_values = getattr(
        transport_class._BaseFetchMarketplaceComments,
        "_BaseFetchMarketplaceComments__REQUIRED_FIELDS_DEFAULT_VALUES",
        {},
    )
    unset_fields = {
        k: v for k, v in default_values.items() if k not in jsonified_request
    }
    jsonified_request.update(unset_fields)

    # verify required fields with default values are now present
    assert "names" in jsonified_request
    assert jsonified_request["names"] == request_init["names"]

    jsonified_request["parent"] = "parent_value"
    jsonified_request["names"] = "names_value"

    # Check that path parameters and body parameters are not mixing in.
    assert not set(unset_fields) - set(
        (
            "names",
            "pageSize",
            "pageToken",
            "skip",
        )
    )

    # verify required fields with non-default values are left alone
    assert "parent" in jsonified_request
    assert jsonified_request["parent"] == "parent_value"
    assert "names" in jsonified_request
    assert jsonified_request["names"] == "names_value"

    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = proposal_service.FetchMarketplaceCommentsResponse()
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
            return_value = proposal_service.FetchMarketplaceCommentsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.fetch_marketplace_comments(request)

            expected_params = [
                (
                    "names",
                    "",
                ),
                ("$alt", "json;enum-encoding=int"),
            ]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_fetch_marketplace_comments_rest_flattened():
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = proposal_service.FetchMarketplaceCommentsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "networks/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            names=["names_value"],
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = proposal_service.FetchMarketplaceCommentsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.fetch_marketplace_comments(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/proposals:fetchMarketplaceComments"
            % client.transport._host,
            args[1],
        )


def test_fetch_marketplace_comments_rest_flattened_error(transport: str = "rest"):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.fetch_marketplace_comments(
            proposal_service.FetchMarketplaceCommentsRequest(),
            parent="parent_value",
            names=["names_value"],
        )


def test_fetch_marketplace_comments_rest_pager(transport: str = "rest"):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            proposal_service.FetchMarketplaceCommentsResponse(
                marketplace_comments=[
                    proposal_messages.MarketplaceComment(),
                    proposal_messages.MarketplaceComment(),
                    proposal_messages.MarketplaceComment(),
                ],
                next_page_token="abc",
            ),
            proposal_service.FetchMarketplaceCommentsResponse(
                marketplace_comments=[],
                next_page_token="def",
            ),
            proposal_service.FetchMarketplaceCommentsResponse(
                marketplace_comments=[
                    proposal_messages.MarketplaceComment(),
                ],
                next_page_token="ghi",
            ),
            proposal_service.FetchMarketplaceCommentsResponse(
                marketplace_comments=[
                    proposal_messages.MarketplaceComment(),
                    proposal_messages.MarketplaceComment(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            proposal_service.FetchMarketplaceCommentsResponse.to_json(x)
            for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {"parent": "networks/sample1"}

        pager = client.fetch_marketplace_comments(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, proposal_messages.MarketplaceComment) for i in results)

        pages = list(client.fetch_marketplace_comments(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.ProposalServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = ProposalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport=transport,
        )

    # It is an error to provide a credentials file and a transport instance.
    transport = transports.ProposalServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = ProposalServiceClient(
            client_options={"credentials_file": "credentials.json"},
            transport=transport,
        )

    # It is an error to provide an api_key and a transport instance.
    transport = transports.ProposalServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = ProposalServiceClient(
            client_options=options,
            transport=transport,
        )

    # It is an error to provide an api_key and a credential.
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = ProposalServiceClient(
            client_options=options, credentials=ga_credentials.AnonymousCredentials()
        )

    # It is an error to provide scopes and a transport instance.
    transport = transports.ProposalServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = ProposalServiceClient(
            client_options={"scopes": ["1", "2"]},
            transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.ProposalServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    client = ProposalServiceClient(transport=transport)
    assert client.transport is transport


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.ProposalServiceRestTransport,
    ],
)
def test_transport_adc(transport_class):
    # Test default credentials are used if not provided.
    with mock.patch.object(google.auth, "default") as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class()
        adc.assert_called_once()


def test_transport_kind_rest():
    transport = ProposalServiceClient.get_transport_class("rest")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "rest"


def test_get_proposal_rest_bad_request(
    request_type=proposal_service.GetProposalRequest,
):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"name": "networks/sample1/proposals/sample2"}
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
        client.get_proposal(request)


@pytest.mark.parametrize(
    "request_type",
    [
        proposal_service.GetProposalRequest,
        dict,
    ],
)
def test_get_proposal_rest_call_success(request_type):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "networks/sample1/proposals/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = proposal_messages.Proposal(
            name="name_value",
            order="order_value",
            display_name="display_name_value",
            archived=True,
            advertiser="advertiser_value",
            notes="notes_value",
            primary_salesperson="primary_salesperson_value",
            sales_planner_users=["sales_planner_users_value"],
            trafficker="trafficker_value",
            seller_contact_users=["seller_contact_users_value"],
            applied_teams=["applied_teams_value"],
            currency_code="currency_code_value",
            sold=True,
            delivery_pausing_enabled=True,
            supply_path=supply_path_type_enum.SupplyPathTypeEnum.SupplyPathType.DIRECT,
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = proposal_messages.Proposal.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_proposal(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, proposal_messages.Proposal)
    assert response.name == "name_value"
    assert response.order == "order_value"
    assert response.display_name == "display_name_value"
    assert response.archived is True
    assert response.advertiser == "advertiser_value"
    assert response.notes == "notes_value"
    assert response.primary_salesperson == "primary_salesperson_value"
    assert response.sales_planner_users == ["sales_planner_users_value"]
    assert response.trafficker == "trafficker_value"
    assert response.seller_contact_users == ["seller_contact_users_value"]
    assert response.applied_teams == ["applied_teams_value"]
    assert response.currency_code == "currency_code_value"
    assert response.sold is True
    assert response.delivery_pausing_enabled is True
    assert (
        response.supply_path
        == supply_path_type_enum.SupplyPathTypeEnum.SupplyPathType.DIRECT
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_proposal_rest_interceptors(null_interceptor):
    transport = transports.ProposalServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.ProposalServiceRestInterceptor(),
    )
    client = ProposalServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor, "post_get_proposal"
        ) as post,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor, "post_get_proposal_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor, "pre_get_proposal"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = proposal_service.GetProposalRequest.pb(
            proposal_service.GetProposalRequest()
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
        return_value = proposal_messages.Proposal.to_json(proposal_messages.Proposal())
        req.return_value.content = return_value

        request = proposal_service.GetProposalRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = proposal_messages.Proposal()
        post_with_metadata.return_value = proposal_messages.Proposal(), metadata

        client.get_proposal(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_proposals_rest_bad_request(
    request_type=proposal_service.ListProposalsRequest,
):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
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
        client.list_proposals(request)


@pytest.mark.parametrize(
    "request_type",
    [
        proposal_service.ListProposalsRequest,
        dict,
    ],
)
def test_list_proposals_rest_call_success(request_type):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = proposal_service.ListProposalsResponse(
            next_page_token="next_page_token_value",
            total_size=1086,
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = proposal_service.ListProposalsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_proposals(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListProposalsPager)
    assert response.next_page_token == "next_page_token_value"
    assert response.total_size == 1086


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_proposals_rest_interceptors(null_interceptor):
    transport = transports.ProposalServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.ProposalServiceRestInterceptor(),
    )
    client = ProposalServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor, "post_list_proposals"
        ) as post,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor,
            "post_list_proposals_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor, "pre_list_proposals"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = proposal_service.ListProposalsRequest.pb(
            proposal_service.ListProposalsRequest()
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
        return_value = proposal_service.ListProposalsResponse.to_json(
            proposal_service.ListProposalsResponse()
        )
        req.return_value.content = return_value

        request = proposal_service.ListProposalsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = proposal_service.ListProposalsResponse()
        post_with_metadata.return_value = (
            proposal_service.ListProposalsResponse(),
            metadata,
        )

        client.list_proposals(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_create_proposal_rest_bad_request(
    request_type=proposal_service.CreateProposalRequest,
):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
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
        client.create_proposal(request)


@pytest.mark.parametrize(
    "request_type",
    [
        proposal_service.CreateProposalRequest,
        dict,
    ],
)
def test_create_proposal_rest_call_success(request_type):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request_init["proposal"] = {
        "name": "name_value",
        "order": "order_value",
        "display_name": "display_name_value",
        "start_time": {"seconds": 751, "nanos": 543},
        "end_time": {},
        "archived": True,
        "advertiser": "advertiser_value",
        "agencies": [
            {
                "company": "company_value",
                "type_": 2,
                "seller_contacts": ["seller_contacts_value1", "seller_contacts_value2"],
            }
        ],
        "notes": "notes_value",
        "primary_salesperson": "primary_salesperson_value",
        "sales_planner_users": [
            "sales_planner_users_value1",
            "sales_planner_users_value2",
        ],
        "trafficker": "trafficker_value",
        "seller_contact_users": [
            "seller_contact_users_value1",
            "seller_contact_users_value2",
        ],
        "applied_teams": ["applied_teams_value1", "applied_teams_value2"],
        "custom_field_values": [
            {
                "custom_field": "custom_field_value",
                "value": {
                    "dropdown_value": 1513,
                    "string_value": "string_value_value",
                    "number_value": 0.1285,
                    "toggle_value": True,
                },
            }
        ],
        "applied_labels": [{"label": "label_value", "negated": True}],
        "effective_applied_labels": {},
        "currency_code": "currency_code_value",
        "sold": True,
        "update_time": {},
        "marketplace_info": {
            "marketplace_order_id": "marketplace_order_id_value",
            "draft_proposal": True,
            "negotiation_status": 1,
            "marketplace_comment": "marketplace_comment_value",
            "new_version_from_buyer": True,
            "buyer_account_id": 1695,
            "partner_client_id": "partner_client_id_value",
        },
        "buyer_rfp": {
            "cost_per_unit": {
                "currency_code": "currency_code_value",
                "units": 563,
                "nanos": 543,
            },
            "units": 563,
            "budget": {},
            "start_time": {},
            "end_time": {},
            "description": "description_value",
            "creative_placeholders": [
                {
                    "size": {"width": 544, "height": 633, "size_type": 1},
                    "companions": [{"size": {}}],
                    "expected_creative_count": 2444,
                    "applied_labels": {},
                    "amp_only": True,
                    "creative_targeting_display_name": "creative_targeting_display_name_value",
                }
            ],
            "targeting": {
                "inventory_url_targeting": {
                    "targeted_inventory_urls": [
                        "targeted_inventory_urls_value1",
                        "targeted_inventory_urls_value2",
                    ],
                    "excluded_inventory_urls": [
                        "excluded_inventory_urls_value1",
                        "excluded_inventory_urls_value2",
                    ],
                },
                "geo_targeting": {
                    "targeted_geos": ["targeted_geos_value1", "targeted_geos_value2"],
                    "excluded_geos": ["excluded_geos_value1", "excluded_geos_value2"],
                },
                "technology_targeting": {
                    "bandwidth_targeting": {
                        "targeted_bandwidth_groups": [
                            "targeted_bandwidth_groups_value1",
                            "targeted_bandwidth_groups_value2",
                        ],
                        "excluded_bandwidth_groups": [
                            "excluded_bandwidth_groups_value1",
                            "excluded_bandwidth_groups_value2",
                        ],
                    },
                    "browser_targeting": {
                        "targeted_browsers": [
                            "targeted_browsers_value1",
                            "targeted_browsers_value2",
                        ],
                        "excluded_browsers": [
                            "excluded_browsers_value1",
                            "excluded_browsers_value2",
                        ],
                    },
                    "browser_language_targeting": {
                        "targeted_browser_languages": [
                            "targeted_browser_languages_value1",
                            "targeted_browser_languages_value2",
                        ],
                        "excluded_browser_languages": [
                            "excluded_browser_languages_value1",
                            "excluded_browser_languages_value2",
                        ],
                    },
                    "device_capability_targeting": {
                        "targeted_capabilities": [
                            "targeted_capabilities_value1",
                            "targeted_capabilities_value2",
                        ],
                        "excluded_capabilities": [
                            "excluded_capabilities_value1",
                            "excluded_capabilities_value2",
                        ],
                    },
                    "device_category_targeting": {
                        "targeted_categories": [
                            "targeted_categories_value1",
                            "targeted_categories_value2",
                        ],
                        "excluded_categories": [
                            "excluded_categories_value1",
                            "excluded_categories_value2",
                        ],
                    },
                    "device_manufacturer_targeting": {
                        "targeted_device_manufacturers": [
                            "targeted_device_manufacturers_value1",
                            "targeted_device_manufacturers_value2",
                        ],
                        "excluded_device_manufacturers": [
                            "excluded_device_manufacturers_value1",
                            "excluded_device_manufacturers_value2",
                        ],
                        "targeted_mobile_devices": [
                            "targeted_mobile_devices_value1",
                            "targeted_mobile_devices_value2",
                        ],
                        "excluded_mobile_devices": [
                            "excluded_mobile_devices_value1",
                            "excluded_mobile_devices_value2",
                        ],
                        "targeted_mobile_device_submodels": [
                            "targeted_mobile_device_submodels_value1",
                            "targeted_mobile_device_submodels_value2",
                        ],
                        "excluded_mobile_device_submodels": [
                            "excluded_mobile_device_submodels_value1",
                            "excluded_mobile_device_submodels_value2",
                        ],
                    },
                    "mobile_carrier_targeting": {
                        "targeted_mobile_carriers": [
                            "targeted_mobile_carriers_value1",
                            "targeted_mobile_carriers_value2",
                        ],
                        "excluded_mobile_carriers": [
                            "excluded_mobile_carriers_value1",
                            "excluded_mobile_carriers_value2",
                        ],
                    },
                    "operating_system_targeting": {
                        "targeted_operating_systems": [
                            "targeted_operating_systems_value1",
                            "targeted_operating_systems_value2",
                        ],
                        "excluded_operating_systems": [
                            "excluded_operating_systems_value1",
                            "excluded_operating_systems_value2",
                        ],
                        "targeted_operating_system_versions": [
                            "targeted_operating_system_versions_value1",
                            "targeted_operating_system_versions_value2",
                        ],
                        "excluded_operating_system_versions": [
                            "excluded_operating_system_versions_value1",
                            "excluded_operating_system_versions_value2",
                        ],
                    },
                },
                "inventory_size_targeting": {
                    "targeted_inventory_sizes": {},
                    "excluded_inventory_sizes": {},
                },
                "inventory_targeting": {
                    "targeted_ad_units": [
                        {"include_descendants": True, "ad_unit": "ad_unit_value"}
                    ],
                    "excluded_ad_units": {},
                    "targeted_placements": [
                        "targeted_placements_value1",
                        "targeted_placements_value2",
                    ],
                },
                "request_platform_targeting": {"request_platforms": [1]},
                "custom_targeting": {
                    "custom_targeting_clauses": [
                        {
                            "custom_targeting_literals": [
                                {
                                    "negative": True,
                                    "custom_targeting_key": "custom_targeting_key_value",
                                    "custom_targeting_values": [
                                        "custom_targeting_values_value1",
                                        "custom_targeting_values_value2",
                                    ],
                                }
                            ],
                            "audience_segment_targetings": [
                                {
                                    "negative": True,
                                    "audience_segments": [
                                        "audience_segments_value1",
                                        "audience_segments_value2",
                                    ],
                                }
                            ],
                            "cms_metadata_targetings": [
                                {
                                    "negative": True,
                                    "cms_metadata_values": [
                                        "cms_metadata_values_value1",
                                        "cms_metadata_values_value2",
                                    ],
                                }
                            ],
                        }
                    ]
                },
                "date_time_range_targeting": {
                    "targeted_range": [{"start_time": {}, "end_time": {}}]
                },
                "publisher_provided_signals_targeting": {
                    "targeted_taxonomy_categories": [
                        "targeted_taxonomy_categories_value1",
                        "targeted_taxonomy_categories_value2",
                    ],
                    "excluded_taxonomy_categories": [
                        "excluded_taxonomy_categories_value1",
                        "excluded_taxonomy_categories_value2",
                    ],
                },
                "user_domain_targeting": {
                    "targeted_user_domains": [
                        "targeted_user_domains_value1",
                        "targeted_user_domains_value2",
                    ],
                    "excluded_user_domains": [
                        "excluded_user_domains_value1",
                        "excluded_user_domains_value2",
                    ],
                },
                "contextual_targeting": {
                    "targeted_verticals": [
                        "targeted_verticals_value1",
                        "targeted_verticals_value2",
                    ],
                    "excluded_verticals": [
                        "excluded_verticals_value1",
                        "excluded_verticals_value2",
                    ],
                    "excluded_content_labels": [
                        "excluded_content_labels_value1",
                        "excluded_content_labels_value2",
                    ],
                },
                "video_position_targeting": {
                    "video_positions": [
                        {
                            "midroll_index": 1386,
                            "reverse_midroll_index": 2245,
                            "pod_position": 1303,
                            "ad_spot": "ad_spot_value",
                            "position_type": 1,
                            "bumper_type": 1,
                        }
                    ]
                },
                "data_segment_targeting": {"has_data_segment_targeting": True},
                "request_format_targeting": {
                    "app_open_enabled": True,
                    "rewarded_enabled": True,
                    "rewarded_interstitial_enabled": True,
                    "interstitial_enabled": True,
                    "anchor_enabled": True,
                    "banner_enabled": True,
                    "instream_video_enabled": True,
                    "instream_audio_enabled": True,
                    "native_advanced_enabled": True,
                },
                "content_targeting": {
                    "targeted_content": [
                        "targeted_content_value1",
                        "targeted_content_value2",
                    ],
                    "excluded_content": [
                        "excluded_content_value1",
                        "excluded_content_value2",
                    ],
                    "targeted_content_bundles": [
                        "targeted_content_bundles_value1",
                        "targeted_content_bundles_value2",
                    ],
                    "excluded_content_bundles": [
                        "excluded_content_bundles_value1",
                        "excluded_content_bundles_value2",
                    ],
                },
                "mobile_application_targeting": {
                    "first_party_targeting": {
                        "targeted_applications": [
                            "targeted_applications_value1",
                            "targeted_applications_value2",
                        ],
                        "excluded_applications": [
                            "excluded_applications_value1",
                            "excluded_applications_value2",
                        ],
                    }
                },
                "day_part_targeting": {
                    "targeted_day_parts": [
                        {
                            "day_of_week": 1,
                            "start_time": {
                                "hours": 561,
                                "minutes": 773,
                                "seconds": 751,
                                "nanos": 543,
                            },
                            "end_time": {},
                        }
                    ],
                    "dayparting_time_zone": 1,
                },
                "buyer_user_list_targeting": {"has_buyer_user_list_targeting": True},
            },
            "additional_terms": "additional_terms_value",
            "ad_exchange_environment": 1,
            "rfp_type": 1,
        },
        "delivery_pausing_enabled": True,
        "supply_path": 1,
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = proposal_service.CreateProposalRequest.meta.fields["proposal"]

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
    for field, value in request_init["proposal"].items():  # pragma: NO COVER
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
                for i in range(0, len(request_init["proposal"][field])):
                    del request_init["proposal"][field][i][subfield]
            else:
                del request_init["proposal"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = proposal_messages.Proposal(
            name="name_value",
            order="order_value",
            display_name="display_name_value",
            archived=True,
            advertiser="advertiser_value",
            notes="notes_value",
            primary_salesperson="primary_salesperson_value",
            sales_planner_users=["sales_planner_users_value"],
            trafficker="trafficker_value",
            seller_contact_users=["seller_contact_users_value"],
            applied_teams=["applied_teams_value"],
            currency_code="currency_code_value",
            sold=True,
            delivery_pausing_enabled=True,
            supply_path=supply_path_type_enum.SupplyPathTypeEnum.SupplyPathType.DIRECT,
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = proposal_messages.Proposal.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.create_proposal(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, proposal_messages.Proposal)
    assert response.name == "name_value"
    assert response.order == "order_value"
    assert response.display_name == "display_name_value"
    assert response.archived is True
    assert response.advertiser == "advertiser_value"
    assert response.notes == "notes_value"
    assert response.primary_salesperson == "primary_salesperson_value"
    assert response.sales_planner_users == ["sales_planner_users_value"]
    assert response.trafficker == "trafficker_value"
    assert response.seller_contact_users == ["seller_contact_users_value"]
    assert response.applied_teams == ["applied_teams_value"]
    assert response.currency_code == "currency_code_value"
    assert response.sold is True
    assert response.delivery_pausing_enabled is True
    assert (
        response.supply_path
        == supply_path_type_enum.SupplyPathTypeEnum.SupplyPathType.DIRECT
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_create_proposal_rest_interceptors(null_interceptor):
    transport = transports.ProposalServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.ProposalServiceRestInterceptor(),
    )
    client = ProposalServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor, "post_create_proposal"
        ) as post,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor,
            "post_create_proposal_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor, "pre_create_proposal"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = proposal_service.CreateProposalRequest.pb(
            proposal_service.CreateProposalRequest()
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
        return_value = proposal_messages.Proposal.to_json(proposal_messages.Proposal())
        req.return_value.content = return_value

        request = proposal_service.CreateProposalRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = proposal_messages.Proposal()
        post_with_metadata.return_value = proposal_messages.Proposal(), metadata

        client.create_proposal(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_create_proposals_rest_bad_request(
    request_type=proposal_service.BatchCreateProposalsRequest,
):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
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
        client.batch_create_proposals(request)


@pytest.mark.parametrize(
    "request_type",
    [
        proposal_service.BatchCreateProposalsRequest,
        dict,
    ],
)
def test_batch_create_proposals_rest_call_success(request_type):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = proposal_service.BatchCreateProposalsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = proposal_service.BatchCreateProposalsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.batch_create_proposals(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, proposal_service.BatchCreateProposalsResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_create_proposals_rest_interceptors(null_interceptor):
    transport = transports.ProposalServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.ProposalServiceRestInterceptor(),
    )
    client = ProposalServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor, "post_batch_create_proposals"
        ) as post,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor,
            "post_batch_create_proposals_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor, "pre_batch_create_proposals"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = proposal_service.BatchCreateProposalsRequest.pb(
            proposal_service.BatchCreateProposalsRequest()
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
        return_value = proposal_service.BatchCreateProposalsResponse.to_json(
            proposal_service.BatchCreateProposalsResponse()
        )
        req.return_value.content = return_value

        request = proposal_service.BatchCreateProposalsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = proposal_service.BatchCreateProposalsResponse()
        post_with_metadata.return_value = (
            proposal_service.BatchCreateProposalsResponse(),
            metadata,
        )

        client.batch_create_proposals(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_update_proposal_rest_bad_request(
    request_type=proposal_service.UpdateProposalRequest,
):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"proposal": {"name": "networks/sample1/proposals/sample2"}}
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
        client.update_proposal(request)


@pytest.mark.parametrize(
    "request_type",
    [
        proposal_service.UpdateProposalRequest,
        dict,
    ],
)
def test_update_proposal_rest_call_success(request_type):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"proposal": {"name": "networks/sample1/proposals/sample2"}}
    request_init["proposal"] = {
        "name": "networks/sample1/proposals/sample2",
        "order": "order_value",
        "display_name": "display_name_value",
        "start_time": {"seconds": 751, "nanos": 543},
        "end_time": {},
        "archived": True,
        "advertiser": "advertiser_value",
        "agencies": [
            {
                "company": "company_value",
                "type_": 2,
                "seller_contacts": ["seller_contacts_value1", "seller_contacts_value2"],
            }
        ],
        "notes": "notes_value",
        "primary_salesperson": "primary_salesperson_value",
        "sales_planner_users": [
            "sales_planner_users_value1",
            "sales_planner_users_value2",
        ],
        "trafficker": "trafficker_value",
        "seller_contact_users": [
            "seller_contact_users_value1",
            "seller_contact_users_value2",
        ],
        "applied_teams": ["applied_teams_value1", "applied_teams_value2"],
        "custom_field_values": [
            {
                "custom_field": "custom_field_value",
                "value": {
                    "dropdown_value": 1513,
                    "string_value": "string_value_value",
                    "number_value": 0.1285,
                    "toggle_value": True,
                },
            }
        ],
        "applied_labels": [{"label": "label_value", "negated": True}],
        "effective_applied_labels": {},
        "currency_code": "currency_code_value",
        "sold": True,
        "update_time": {},
        "marketplace_info": {
            "marketplace_order_id": "marketplace_order_id_value",
            "draft_proposal": True,
            "negotiation_status": 1,
            "marketplace_comment": "marketplace_comment_value",
            "new_version_from_buyer": True,
            "buyer_account_id": 1695,
            "partner_client_id": "partner_client_id_value",
        },
        "buyer_rfp": {
            "cost_per_unit": {
                "currency_code": "currency_code_value",
                "units": 563,
                "nanos": 543,
            },
            "units": 563,
            "budget": {},
            "start_time": {},
            "end_time": {},
            "description": "description_value",
            "creative_placeholders": [
                {
                    "size": {"width": 544, "height": 633, "size_type": 1},
                    "companions": [{"size": {}}],
                    "expected_creative_count": 2444,
                    "applied_labels": {},
                    "amp_only": True,
                    "creative_targeting_display_name": "creative_targeting_display_name_value",
                }
            ],
            "targeting": {
                "inventory_url_targeting": {
                    "targeted_inventory_urls": [
                        "targeted_inventory_urls_value1",
                        "targeted_inventory_urls_value2",
                    ],
                    "excluded_inventory_urls": [
                        "excluded_inventory_urls_value1",
                        "excluded_inventory_urls_value2",
                    ],
                },
                "geo_targeting": {
                    "targeted_geos": ["targeted_geos_value1", "targeted_geos_value2"],
                    "excluded_geos": ["excluded_geos_value1", "excluded_geos_value2"],
                },
                "technology_targeting": {
                    "bandwidth_targeting": {
                        "targeted_bandwidth_groups": [
                            "targeted_bandwidth_groups_value1",
                            "targeted_bandwidth_groups_value2",
                        ],
                        "excluded_bandwidth_groups": [
                            "excluded_bandwidth_groups_value1",
                            "excluded_bandwidth_groups_value2",
                        ],
                    },
                    "browser_targeting": {
                        "targeted_browsers": [
                            "targeted_browsers_value1",
                            "targeted_browsers_value2",
                        ],
                        "excluded_browsers": [
                            "excluded_browsers_value1",
                            "excluded_browsers_value2",
                        ],
                    },
                    "browser_language_targeting": {
                        "targeted_browser_languages": [
                            "targeted_browser_languages_value1",
                            "targeted_browser_languages_value2",
                        ],
                        "excluded_browser_languages": [
                            "excluded_browser_languages_value1",
                            "excluded_browser_languages_value2",
                        ],
                    },
                    "device_capability_targeting": {
                        "targeted_capabilities": [
                            "targeted_capabilities_value1",
                            "targeted_capabilities_value2",
                        ],
                        "excluded_capabilities": [
                            "excluded_capabilities_value1",
                            "excluded_capabilities_value2",
                        ],
                    },
                    "device_category_targeting": {
                        "targeted_categories": [
                            "targeted_categories_value1",
                            "targeted_categories_value2",
                        ],
                        "excluded_categories": [
                            "excluded_categories_value1",
                            "excluded_categories_value2",
                        ],
                    },
                    "device_manufacturer_targeting": {
                        "targeted_device_manufacturers": [
                            "targeted_device_manufacturers_value1",
                            "targeted_device_manufacturers_value2",
                        ],
                        "excluded_device_manufacturers": [
                            "excluded_device_manufacturers_value1",
                            "excluded_device_manufacturers_value2",
                        ],
                        "targeted_mobile_devices": [
                            "targeted_mobile_devices_value1",
                            "targeted_mobile_devices_value2",
                        ],
                        "excluded_mobile_devices": [
                            "excluded_mobile_devices_value1",
                            "excluded_mobile_devices_value2",
                        ],
                        "targeted_mobile_device_submodels": [
                            "targeted_mobile_device_submodels_value1",
                            "targeted_mobile_device_submodels_value2",
                        ],
                        "excluded_mobile_device_submodels": [
                            "excluded_mobile_device_submodels_value1",
                            "excluded_mobile_device_submodels_value2",
                        ],
                    },
                    "mobile_carrier_targeting": {
                        "targeted_mobile_carriers": [
                            "targeted_mobile_carriers_value1",
                            "targeted_mobile_carriers_value2",
                        ],
                        "excluded_mobile_carriers": [
                            "excluded_mobile_carriers_value1",
                            "excluded_mobile_carriers_value2",
                        ],
                    },
                    "operating_system_targeting": {
                        "targeted_operating_systems": [
                            "targeted_operating_systems_value1",
                            "targeted_operating_systems_value2",
                        ],
                        "excluded_operating_systems": [
                            "excluded_operating_systems_value1",
                            "excluded_operating_systems_value2",
                        ],
                        "targeted_operating_system_versions": [
                            "targeted_operating_system_versions_value1",
                            "targeted_operating_system_versions_value2",
                        ],
                        "excluded_operating_system_versions": [
                            "excluded_operating_system_versions_value1",
                            "excluded_operating_system_versions_value2",
                        ],
                    },
                },
                "inventory_size_targeting": {
                    "targeted_inventory_sizes": {},
                    "excluded_inventory_sizes": {},
                },
                "inventory_targeting": {
                    "targeted_ad_units": [
                        {"include_descendants": True, "ad_unit": "ad_unit_value"}
                    ],
                    "excluded_ad_units": {},
                    "targeted_placements": [
                        "targeted_placements_value1",
                        "targeted_placements_value2",
                    ],
                },
                "request_platform_targeting": {"request_platforms": [1]},
                "custom_targeting": {
                    "custom_targeting_clauses": [
                        {
                            "custom_targeting_literals": [
                                {
                                    "negative": True,
                                    "custom_targeting_key": "custom_targeting_key_value",
                                    "custom_targeting_values": [
                                        "custom_targeting_values_value1",
                                        "custom_targeting_values_value2",
                                    ],
                                }
                            ],
                            "audience_segment_targetings": [
                                {
                                    "negative": True,
                                    "audience_segments": [
                                        "audience_segments_value1",
                                        "audience_segments_value2",
                                    ],
                                }
                            ],
                            "cms_metadata_targetings": [
                                {
                                    "negative": True,
                                    "cms_metadata_values": [
                                        "cms_metadata_values_value1",
                                        "cms_metadata_values_value2",
                                    ],
                                }
                            ],
                        }
                    ]
                },
                "date_time_range_targeting": {
                    "targeted_range": [{"start_time": {}, "end_time": {}}]
                },
                "publisher_provided_signals_targeting": {
                    "targeted_taxonomy_categories": [
                        "targeted_taxonomy_categories_value1",
                        "targeted_taxonomy_categories_value2",
                    ],
                    "excluded_taxonomy_categories": [
                        "excluded_taxonomy_categories_value1",
                        "excluded_taxonomy_categories_value2",
                    ],
                },
                "user_domain_targeting": {
                    "targeted_user_domains": [
                        "targeted_user_domains_value1",
                        "targeted_user_domains_value2",
                    ],
                    "excluded_user_domains": [
                        "excluded_user_domains_value1",
                        "excluded_user_domains_value2",
                    ],
                },
                "contextual_targeting": {
                    "targeted_verticals": [
                        "targeted_verticals_value1",
                        "targeted_verticals_value2",
                    ],
                    "excluded_verticals": [
                        "excluded_verticals_value1",
                        "excluded_verticals_value2",
                    ],
                    "excluded_content_labels": [
                        "excluded_content_labels_value1",
                        "excluded_content_labels_value2",
                    ],
                },
                "video_position_targeting": {
                    "video_positions": [
                        {
                            "midroll_index": 1386,
                            "reverse_midroll_index": 2245,
                            "pod_position": 1303,
                            "ad_spot": "ad_spot_value",
                            "position_type": 1,
                            "bumper_type": 1,
                        }
                    ]
                },
                "data_segment_targeting": {"has_data_segment_targeting": True},
                "request_format_targeting": {
                    "app_open_enabled": True,
                    "rewarded_enabled": True,
                    "rewarded_interstitial_enabled": True,
                    "interstitial_enabled": True,
                    "anchor_enabled": True,
                    "banner_enabled": True,
                    "instream_video_enabled": True,
                    "instream_audio_enabled": True,
                    "native_advanced_enabled": True,
                },
                "content_targeting": {
                    "targeted_content": [
                        "targeted_content_value1",
                        "targeted_content_value2",
                    ],
                    "excluded_content": [
                        "excluded_content_value1",
                        "excluded_content_value2",
                    ],
                    "targeted_content_bundles": [
                        "targeted_content_bundles_value1",
                        "targeted_content_bundles_value2",
                    ],
                    "excluded_content_bundles": [
                        "excluded_content_bundles_value1",
                        "excluded_content_bundles_value2",
                    ],
                },
                "mobile_application_targeting": {
                    "first_party_targeting": {
                        "targeted_applications": [
                            "targeted_applications_value1",
                            "targeted_applications_value2",
                        ],
                        "excluded_applications": [
                            "excluded_applications_value1",
                            "excluded_applications_value2",
                        ],
                    }
                },
                "day_part_targeting": {
                    "targeted_day_parts": [
                        {
                            "day_of_week": 1,
                            "start_time": {
                                "hours": 561,
                                "minutes": 773,
                                "seconds": 751,
                                "nanos": 543,
                            },
                            "end_time": {},
                        }
                    ],
                    "dayparting_time_zone": 1,
                },
                "buyer_user_list_targeting": {"has_buyer_user_list_targeting": True},
            },
            "additional_terms": "additional_terms_value",
            "ad_exchange_environment": 1,
            "rfp_type": 1,
        },
        "delivery_pausing_enabled": True,
        "supply_path": 1,
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = proposal_service.UpdateProposalRequest.meta.fields["proposal"]

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
    for field, value in request_init["proposal"].items():  # pragma: NO COVER
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
                for i in range(0, len(request_init["proposal"][field])):
                    del request_init["proposal"][field][i][subfield]
            else:
                del request_init["proposal"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = proposal_messages.Proposal(
            name="name_value",
            order="order_value",
            display_name="display_name_value",
            archived=True,
            advertiser="advertiser_value",
            notes="notes_value",
            primary_salesperson="primary_salesperson_value",
            sales_planner_users=["sales_planner_users_value"],
            trafficker="trafficker_value",
            seller_contact_users=["seller_contact_users_value"],
            applied_teams=["applied_teams_value"],
            currency_code="currency_code_value",
            sold=True,
            delivery_pausing_enabled=True,
            supply_path=supply_path_type_enum.SupplyPathTypeEnum.SupplyPathType.DIRECT,
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = proposal_messages.Proposal.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.update_proposal(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, proposal_messages.Proposal)
    assert response.name == "name_value"
    assert response.order == "order_value"
    assert response.display_name == "display_name_value"
    assert response.archived is True
    assert response.advertiser == "advertiser_value"
    assert response.notes == "notes_value"
    assert response.primary_salesperson == "primary_salesperson_value"
    assert response.sales_planner_users == ["sales_planner_users_value"]
    assert response.trafficker == "trafficker_value"
    assert response.seller_contact_users == ["seller_contact_users_value"]
    assert response.applied_teams == ["applied_teams_value"]
    assert response.currency_code == "currency_code_value"
    assert response.sold is True
    assert response.delivery_pausing_enabled is True
    assert (
        response.supply_path
        == supply_path_type_enum.SupplyPathTypeEnum.SupplyPathType.DIRECT
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_update_proposal_rest_interceptors(null_interceptor):
    transport = transports.ProposalServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.ProposalServiceRestInterceptor(),
    )
    client = ProposalServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor, "post_update_proposal"
        ) as post,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor,
            "post_update_proposal_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor, "pre_update_proposal"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = proposal_service.UpdateProposalRequest.pb(
            proposal_service.UpdateProposalRequest()
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
        return_value = proposal_messages.Proposal.to_json(proposal_messages.Proposal())
        req.return_value.content = return_value

        request = proposal_service.UpdateProposalRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = proposal_messages.Proposal()
        post_with_metadata.return_value = proposal_messages.Proposal(), metadata

        client.update_proposal(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_update_proposals_rest_bad_request(
    request_type=proposal_service.BatchUpdateProposalsRequest,
):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
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
        client.batch_update_proposals(request)


@pytest.mark.parametrize(
    "request_type",
    [
        proposal_service.BatchUpdateProposalsRequest,
        dict,
    ],
)
def test_batch_update_proposals_rest_call_success(request_type):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = proposal_service.BatchUpdateProposalsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = proposal_service.BatchUpdateProposalsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.batch_update_proposals(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, proposal_service.BatchUpdateProposalsResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_update_proposals_rest_interceptors(null_interceptor):
    transport = transports.ProposalServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.ProposalServiceRestInterceptor(),
    )
    client = ProposalServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor, "post_batch_update_proposals"
        ) as post,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor,
            "post_batch_update_proposals_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor, "pre_batch_update_proposals"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = proposal_service.BatchUpdateProposalsRequest.pb(
            proposal_service.BatchUpdateProposalsRequest()
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
        return_value = proposal_service.BatchUpdateProposalsResponse.to_json(
            proposal_service.BatchUpdateProposalsResponse()
        )
        req.return_value.content = return_value

        request = proposal_service.BatchUpdateProposalsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = proposal_service.BatchUpdateProposalsResponse()
        post_with_metadata.return_value = (
            proposal_service.BatchUpdateProposalsResponse(),
            metadata,
        )

        client.batch_update_proposals(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_archive_proposals_rest_bad_request(
    request_type=proposal_service.BatchArchiveProposalsRequest,
):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
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
        client.batch_archive_proposals(request)


@pytest.mark.parametrize(
    "request_type",
    [
        proposal_service.BatchArchiveProposalsRequest,
        dict,
    ],
)
def test_batch_archive_proposals_rest_call_success(request_type):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = proposal_service.BatchArchiveProposalsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = proposal_service.BatchArchiveProposalsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.batch_archive_proposals(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, proposal_service.BatchArchiveProposalsResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_archive_proposals_rest_interceptors(null_interceptor):
    transport = transports.ProposalServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.ProposalServiceRestInterceptor(),
    )
    client = ProposalServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor, "post_batch_archive_proposals"
        ) as post,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor,
            "post_batch_archive_proposals_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor, "pre_batch_archive_proposals"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = proposal_service.BatchArchiveProposalsRequest.pb(
            proposal_service.BatchArchiveProposalsRequest()
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
        return_value = proposal_service.BatchArchiveProposalsResponse.to_json(
            proposal_service.BatchArchiveProposalsResponse()
        )
        req.return_value.content = return_value

        request = proposal_service.BatchArchiveProposalsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = proposal_service.BatchArchiveProposalsResponse()
        post_with_metadata.return_value = (
            proposal_service.BatchArchiveProposalsResponse(),
            metadata,
        )

        client.batch_archive_proposals(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_unarchive_proposals_rest_bad_request(
    request_type=proposal_service.BatchUnarchiveProposalsRequest,
):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
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
        client.batch_unarchive_proposals(request)


@pytest.mark.parametrize(
    "request_type",
    [
        proposal_service.BatchUnarchiveProposalsRequest,
        dict,
    ],
)
def test_batch_unarchive_proposals_rest_call_success(request_type):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = proposal_service.BatchUnarchiveProposalsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = proposal_service.BatchUnarchiveProposalsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.batch_unarchive_proposals(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, proposal_service.BatchUnarchiveProposalsResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_unarchive_proposals_rest_interceptors(null_interceptor):
    transport = transports.ProposalServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.ProposalServiceRestInterceptor(),
    )
    client = ProposalServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor, "post_batch_unarchive_proposals"
        ) as post,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor,
            "post_batch_unarchive_proposals_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor, "pre_batch_unarchive_proposals"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = proposal_service.BatchUnarchiveProposalsRequest.pb(
            proposal_service.BatchUnarchiveProposalsRequest()
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
        return_value = proposal_service.BatchUnarchiveProposalsResponse.to_json(
            proposal_service.BatchUnarchiveProposalsResponse()
        )
        req.return_value.content = return_value

        request = proposal_service.BatchUnarchiveProposalsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = proposal_service.BatchUnarchiveProposalsResponse()
        post_with_metadata.return_value = (
            proposal_service.BatchUnarchiveProposalsResponse(),
            metadata,
        )

        client.batch_unarchive_proposals(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_pause_proposals_rest_bad_request(
    request_type=proposal_service.BatchPauseProposalsRequest,
):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
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
        client.batch_pause_proposals(request)


@pytest.mark.parametrize(
    "request_type",
    [
        proposal_service.BatchPauseProposalsRequest,
        dict,
    ],
)
def test_batch_pause_proposals_rest_call_success(request_type):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = proposal_service.BatchPauseProposalsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = proposal_service.BatchPauseProposalsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.batch_pause_proposals(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, proposal_service.BatchPauseProposalsResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_pause_proposals_rest_interceptors(null_interceptor):
    transport = transports.ProposalServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.ProposalServiceRestInterceptor(),
    )
    client = ProposalServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor, "post_batch_pause_proposals"
        ) as post,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor,
            "post_batch_pause_proposals_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor, "pre_batch_pause_proposals"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = proposal_service.BatchPauseProposalsRequest.pb(
            proposal_service.BatchPauseProposalsRequest()
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
        return_value = proposal_service.BatchPauseProposalsResponse.to_json(
            proposal_service.BatchPauseProposalsResponse()
        )
        req.return_value.content = return_value

        request = proposal_service.BatchPauseProposalsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = proposal_service.BatchPauseProposalsResponse()
        post_with_metadata.return_value = (
            proposal_service.BatchPauseProposalsResponse(),
            metadata,
        )

        client.batch_pause_proposals(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_resume_proposals_rest_bad_request(
    request_type=proposal_service.BatchResumeProposalsRequest,
):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
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
        client.batch_resume_proposals(request)


@pytest.mark.parametrize(
    "request_type",
    [
        proposal_service.BatchResumeProposalsRequest,
        dict,
    ],
)
def test_batch_resume_proposals_rest_call_success(request_type):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = proposal_service.BatchResumeProposalsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = proposal_service.BatchResumeProposalsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.batch_resume_proposals(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, proposal_service.BatchResumeProposalsResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_resume_proposals_rest_interceptors(null_interceptor):
    transport = transports.ProposalServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.ProposalServiceRestInterceptor(),
    )
    client = ProposalServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor, "post_batch_resume_proposals"
        ) as post,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor,
            "post_batch_resume_proposals_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor, "pre_batch_resume_proposals"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = proposal_service.BatchResumeProposalsRequest.pb(
            proposal_service.BatchResumeProposalsRequest()
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
        return_value = proposal_service.BatchResumeProposalsResponse.to_json(
            proposal_service.BatchResumeProposalsResponse()
        )
        req.return_value.content = return_value

        request = proposal_service.BatchResumeProposalsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = proposal_service.BatchResumeProposalsResponse()
        post_with_metadata.return_value = (
            proposal_service.BatchResumeProposalsResponse(),
            metadata,
        )

        client.batch_resume_proposals(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_request_buyer_review_proposals_rest_bad_request(
    request_type=proposal_service.BatchRequestBuyerReviewProposalsRequest,
):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
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
        client.batch_request_buyer_review_proposals(request)


@pytest.mark.parametrize(
    "request_type",
    [
        proposal_service.BatchRequestBuyerReviewProposalsRequest,
        dict,
    ],
)
def test_batch_request_buyer_review_proposals_rest_call_success(request_type):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = proposal_service.BatchRequestBuyerReviewProposalsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = proposal_service.BatchRequestBuyerReviewProposalsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.batch_request_buyer_review_proposals(request)

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, proposal_service.BatchRequestBuyerReviewProposalsResponse
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_request_buyer_review_proposals_rest_interceptors(null_interceptor):
    transport = transports.ProposalServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.ProposalServiceRestInterceptor(),
    )
    client = ProposalServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor,
            "post_batch_request_buyer_review_proposals",
        ) as post,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor,
            "post_batch_request_buyer_review_proposals_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor,
            "pre_batch_request_buyer_review_proposals",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = proposal_service.BatchRequestBuyerReviewProposalsRequest.pb(
            proposal_service.BatchRequestBuyerReviewProposalsRequest()
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
            proposal_service.BatchRequestBuyerReviewProposalsResponse.to_json(
                proposal_service.BatchRequestBuyerReviewProposalsResponse()
            )
        )
        req.return_value.content = return_value

        request = proposal_service.BatchRequestBuyerReviewProposalsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = proposal_service.BatchRequestBuyerReviewProposalsResponse()
        post_with_metadata.return_value = (
            proposal_service.BatchRequestBuyerReviewProposalsResponse(),
            metadata,
        )

        client.batch_request_buyer_review_proposals(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_request_buyer_accept_proposals_rest_bad_request(
    request_type=proposal_service.BatchRequestBuyerAcceptProposalsRequest,
):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
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
        client.batch_request_buyer_accept_proposals(request)


@pytest.mark.parametrize(
    "request_type",
    [
        proposal_service.BatchRequestBuyerAcceptProposalsRequest,
        dict,
    ],
)
def test_batch_request_buyer_accept_proposals_rest_call_success(request_type):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = proposal_service.BatchRequestBuyerAcceptProposalsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = proposal_service.BatchRequestBuyerAcceptProposalsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.batch_request_buyer_accept_proposals(request)

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, proposal_service.BatchRequestBuyerAcceptProposalsResponse
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_request_buyer_accept_proposals_rest_interceptors(null_interceptor):
    transport = transports.ProposalServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.ProposalServiceRestInterceptor(),
    )
    client = ProposalServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor,
            "post_batch_request_buyer_accept_proposals",
        ) as post,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor,
            "post_batch_request_buyer_accept_proposals_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor,
            "pre_batch_request_buyer_accept_proposals",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = proposal_service.BatchRequestBuyerAcceptProposalsRequest.pb(
            proposal_service.BatchRequestBuyerAcceptProposalsRequest()
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
            proposal_service.BatchRequestBuyerAcceptProposalsResponse.to_json(
                proposal_service.BatchRequestBuyerAcceptProposalsResponse()
            )
        )
        req.return_value.content = return_value

        request = proposal_service.BatchRequestBuyerAcceptProposalsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = proposal_service.BatchRequestBuyerAcceptProposalsResponse()
        post_with_metadata.return_value = (
            proposal_service.BatchRequestBuyerAcceptProposalsResponse(),
            metadata,
        )

        client.batch_request_buyer_accept_proposals(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_reserve_proposals_rest_bad_request(
    request_type=proposal_service.BatchReserveProposalsRequest,
):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
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
        client.batch_reserve_proposals(request)


@pytest.mark.parametrize(
    "request_type",
    [
        proposal_service.BatchReserveProposalsRequest,
        dict,
    ],
)
def test_batch_reserve_proposals_rest_call_success(request_type):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = proposal_service.BatchReserveProposalsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = proposal_service.BatchReserveProposalsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.batch_reserve_proposals(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, proposal_service.BatchReserveProposalsResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_reserve_proposals_rest_interceptors(null_interceptor):
    transport = transports.ProposalServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.ProposalServiceRestInterceptor(),
    )
    client = ProposalServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor, "post_batch_reserve_proposals"
        ) as post,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor,
            "post_batch_reserve_proposals_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor, "pre_batch_reserve_proposals"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = proposal_service.BatchReserveProposalsRequest.pb(
            proposal_service.BatchReserveProposalsRequest()
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
        return_value = proposal_service.BatchReserveProposalsResponse.to_json(
            proposal_service.BatchReserveProposalsResponse()
        )
        req.return_value.content = return_value

        request = proposal_service.BatchReserveProposalsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = proposal_service.BatchReserveProposalsResponse()
        post_with_metadata.return_value = (
            proposal_service.BatchReserveProposalsResponse(),
            metadata,
        )

        client.batch_reserve_proposals(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_redraft_proposals_rest_bad_request(
    request_type=proposal_service.BatchRedraftProposalsRequest,
):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
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
        client.batch_redraft_proposals(request)


@pytest.mark.parametrize(
    "request_type",
    [
        proposal_service.BatchRedraftProposalsRequest,
        dict,
    ],
)
def test_batch_redraft_proposals_rest_call_success(request_type):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = proposal_service.BatchRedraftProposalsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = proposal_service.BatchRedraftProposalsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.batch_redraft_proposals(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, proposal_service.BatchRedraftProposalsResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_redraft_proposals_rest_interceptors(null_interceptor):
    transport = transports.ProposalServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.ProposalServiceRestInterceptor(),
    )
    client = ProposalServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor, "post_batch_redraft_proposals"
        ) as post,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor,
            "post_batch_redraft_proposals_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor, "pre_batch_redraft_proposals"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = proposal_service.BatchRedraftProposalsRequest.pb(
            proposal_service.BatchRedraftProposalsRequest()
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
        return_value = proposal_service.BatchRedraftProposalsResponse.to_json(
            proposal_service.BatchRedraftProposalsResponse()
        )
        req.return_value.content = return_value

        request = proposal_service.BatchRedraftProposalsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = proposal_service.BatchRedraftProposalsResponse()
        post_with_metadata.return_value = (
            proposal_service.BatchRedraftProposalsResponse(),
            metadata,
        )

        client.batch_redraft_proposals(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_discard_draft_proposals_rest_bad_request(
    request_type=proposal_service.BatchDiscardDraftProposalsRequest,
):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
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
        client.batch_discard_draft_proposals(request)


@pytest.mark.parametrize(
    "request_type",
    [
        proposal_service.BatchDiscardDraftProposalsRequest,
        dict,
    ],
)
def test_batch_discard_draft_proposals_rest_call_success(request_type):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = proposal_service.BatchDiscardDraftProposalsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = proposal_service.BatchDiscardDraftProposalsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.batch_discard_draft_proposals(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, proposal_service.BatchDiscardDraftProposalsResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_discard_draft_proposals_rest_interceptors(null_interceptor):
    transport = transports.ProposalServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.ProposalServiceRestInterceptor(),
    )
    client = ProposalServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor,
            "post_batch_discard_draft_proposals",
        ) as post,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor,
            "post_batch_discard_draft_proposals_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor,
            "pre_batch_discard_draft_proposals",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = proposal_service.BatchDiscardDraftProposalsRequest.pb(
            proposal_service.BatchDiscardDraftProposalsRequest()
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
        return_value = proposal_service.BatchDiscardDraftProposalsResponse.to_json(
            proposal_service.BatchDiscardDraftProposalsResponse()
        )
        req.return_value.content = return_value

        request = proposal_service.BatchDiscardDraftProposalsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = proposal_service.BatchDiscardDraftProposalsResponse()
        post_with_metadata.return_value = (
            proposal_service.BatchDiscardDraftProposalsResponse(),
            metadata,
        )

        client.batch_discard_draft_proposals(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_terminate_proposals_rest_bad_request(
    request_type=proposal_service.BatchTerminateProposalsRequest,
):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
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
        client.batch_terminate_proposals(request)


@pytest.mark.parametrize(
    "request_type",
    [
        proposal_service.BatchTerminateProposalsRequest,
        dict,
    ],
)
def test_batch_terminate_proposals_rest_call_success(request_type):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = proposal_service.BatchTerminateProposalsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = proposal_service.BatchTerminateProposalsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.batch_terminate_proposals(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, proposal_service.BatchTerminateProposalsResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_terminate_proposals_rest_interceptors(null_interceptor):
    transport = transports.ProposalServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.ProposalServiceRestInterceptor(),
    )
    client = ProposalServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor, "post_batch_terminate_proposals"
        ) as post,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor,
            "post_batch_terminate_proposals_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor, "pre_batch_terminate_proposals"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = proposal_service.BatchTerminateProposalsRequest.pb(
            proposal_service.BatchTerminateProposalsRequest()
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
        return_value = proposal_service.BatchTerminateProposalsResponse.to_json(
            proposal_service.BatchTerminateProposalsResponse()
        )
        req.return_value.content = return_value

        request = proposal_service.BatchTerminateProposalsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = proposal_service.BatchTerminateProposalsResponse()
        post_with_metadata.return_value = (
            proposal_service.BatchTerminateProposalsResponse(),
            metadata,
        )

        client.batch_terminate_proposals(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_push_to_order_proposals_rest_bad_request(
    request_type=proposal_service.BatchPushToOrderProposalsRequest,
):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
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
        client.batch_push_to_order_proposals(request)


@pytest.mark.parametrize(
    "request_type",
    [
        proposal_service.BatchPushToOrderProposalsRequest,
        dict,
    ],
)
def test_batch_push_to_order_proposals_rest_call_success(request_type):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = proposal_service.BatchPushToOrderProposalsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = proposal_service.BatchPushToOrderProposalsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.batch_push_to_order_proposals(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, proposal_service.BatchPushToOrderProposalsResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_push_to_order_proposals_rest_interceptors(null_interceptor):
    transport = transports.ProposalServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.ProposalServiceRestInterceptor(),
    )
    client = ProposalServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor,
            "post_batch_push_to_order_proposals",
        ) as post,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor,
            "post_batch_push_to_order_proposals_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor,
            "pre_batch_push_to_order_proposals",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = proposal_service.BatchPushToOrderProposalsRequest.pb(
            proposal_service.BatchPushToOrderProposalsRequest()
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
        return_value = proposal_service.BatchPushToOrderProposalsResponse.to_json(
            proposal_service.BatchPushToOrderProposalsResponse()
        )
        req.return_value.content = return_value

        request = proposal_service.BatchPushToOrderProposalsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = proposal_service.BatchPushToOrderProposalsResponse()
        post_with_metadata.return_value = (
            proposal_service.BatchPushToOrderProposalsResponse(),
            metadata,
        )

        client.batch_push_to_order_proposals(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_fetch_marketplace_comments_rest_bad_request(
    request_type=proposal_service.FetchMarketplaceCommentsRequest,
):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
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
        client.fetch_marketplace_comments(request)


@pytest.mark.parametrize(
    "request_type",
    [
        proposal_service.FetchMarketplaceCommentsRequest,
        dict,
    ],
)
def test_fetch_marketplace_comments_rest_call_success(request_type):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = proposal_service.FetchMarketplaceCommentsResponse(
            next_page_token="next_page_token_value",
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = proposal_service.FetchMarketplaceCommentsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.fetch_marketplace_comments(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.FetchMarketplaceCommentsPager)
    assert response.next_page_token == "next_page_token_value"


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_fetch_marketplace_comments_rest_interceptors(null_interceptor):
    transport = transports.ProposalServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.ProposalServiceRestInterceptor(),
    )
    client = ProposalServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor, "post_fetch_marketplace_comments"
        ) as post,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor,
            "post_fetch_marketplace_comments_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.ProposalServiceRestInterceptor, "pre_fetch_marketplace_comments"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = proposal_service.FetchMarketplaceCommentsRequest.pb(
            proposal_service.FetchMarketplaceCommentsRequest()
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
        return_value = proposal_service.FetchMarketplaceCommentsResponse.to_json(
            proposal_service.FetchMarketplaceCommentsResponse()
        )
        req.return_value.content = return_value

        request = proposal_service.FetchMarketplaceCommentsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = proposal_service.FetchMarketplaceCommentsResponse()
        post_with_metadata.return_value = (
            proposal_service.FetchMarketplaceCommentsResponse(),
            metadata,
        )

        client.fetch_marketplace_comments(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_cancel_operation_rest_bad_request(
    request_type=operations_pb2.CancelOperationRequest,
):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type()
    request = json_format.ParseDict(
        {"name": "networks/sample1/operations/reports/runs/sample2"}, request
    )

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.cancel_operation(request)


@pytest.mark.parametrize(
    "request_type",
    [
        operations_pb2.CancelOperationRequest,
        dict,
    ],
)
def test_cancel_operation_rest(request_type):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    request_init = {"name": "networks/sample1/operations/reports/runs/sample2"}
    request = request_type(**request_init)
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = None

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200
        json_return_value = "{}"
        response_value.content = json_return_value.encode("UTF-8")

        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        response = client.cancel_operation(request)

    # Establish that the response is the type that we expect.
    assert response is None


def test_get_operation_rest_bad_request(
    request_type=operations_pb2.GetOperationRequest,
):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type()
    request = json_format.ParseDict(
        {"name": "networks/sample1/operations/reports/runs/sample2"}, request
    )

    # Mock the http request call within the method and fake a BadRequest error.
    with (
        mock.patch.object(Session, "request") as req,
        pytest.raises(core_exceptions.BadRequest),
    ):
        # Wrap the value into a proper Response obj
        response_value = Response()
        json_return_value = ""
        response_value.json = mock.Mock(return_value={})
        response_value.status_code = 400
        response_value.request = Request()
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        client.get_operation(request)


@pytest.mark.parametrize(
    "request_type",
    [
        operations_pb2.GetOperationRequest,
        dict,
    ],
)
def test_get_operation_rest(request_type):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    request_init = {"name": "networks/sample1/operations/reports/runs/sample2"}
    request = request_type(**request_init)
    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = operations_pb2.Operation()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")

        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        response = client.get_operation(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, operations_pb2.Operation)


def test_initialize_client_w_rest():
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_proposal_empty_call_rest():
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_proposal), "__call__") as call:
        client.get_proposal(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = proposal_service.GetProposalRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_proposals_empty_call_rest():
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_proposals), "__call__") as call:
        client.list_proposals(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = proposal_service.ListProposalsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_proposal_empty_call_rest():
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.create_proposal), "__call__") as call:
        client.create_proposal(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = proposal_service.CreateProposalRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_create_proposals_empty_call_rest():
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_create_proposals), "__call__"
    ) as call:
        client.batch_create_proposals(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = proposal_service.BatchCreateProposalsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_proposal_empty_call_rest():
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.update_proposal), "__call__") as call:
        client.update_proposal(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = proposal_service.UpdateProposalRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_update_proposals_empty_call_rest():
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_update_proposals), "__call__"
    ) as call:
        client.batch_update_proposals(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = proposal_service.BatchUpdateProposalsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_archive_proposals_empty_call_rest():
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_archive_proposals), "__call__"
    ) as call:
        client.batch_archive_proposals(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = proposal_service.BatchArchiveProposalsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_unarchive_proposals_empty_call_rest():
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_unarchive_proposals), "__call__"
    ) as call:
        client.batch_unarchive_proposals(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = proposal_service.BatchUnarchiveProposalsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_pause_proposals_empty_call_rest():
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_pause_proposals), "__call__"
    ) as call:
        client.batch_pause_proposals(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = proposal_service.BatchPauseProposalsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_resume_proposals_empty_call_rest():
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_resume_proposals), "__call__"
    ) as call:
        client.batch_resume_proposals(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = proposal_service.BatchResumeProposalsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_request_buyer_review_proposals_empty_call_rest():
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_request_buyer_review_proposals), "__call__"
    ) as call:
        client.batch_request_buyer_review_proposals(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = proposal_service.BatchRequestBuyerReviewProposalsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_request_buyer_accept_proposals_empty_call_rest():
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_request_buyer_accept_proposals), "__call__"
    ) as call:
        client.batch_request_buyer_accept_proposals(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = proposal_service.BatchRequestBuyerAcceptProposalsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_reserve_proposals_empty_call_rest():
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_reserve_proposals), "__call__"
    ) as call:
        client.batch_reserve_proposals(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = proposal_service.BatchReserveProposalsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_redraft_proposals_empty_call_rest():
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_redraft_proposals), "__call__"
    ) as call:
        client.batch_redraft_proposals(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = proposal_service.BatchRedraftProposalsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_discard_draft_proposals_empty_call_rest():
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_discard_draft_proposals), "__call__"
    ) as call:
        client.batch_discard_draft_proposals(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = proposal_service.BatchDiscardDraftProposalsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_terminate_proposals_empty_call_rest():
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_terminate_proposals), "__call__"
    ) as call:
        client.batch_terminate_proposals(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = proposal_service.BatchTerminateProposalsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_push_to_order_proposals_empty_call_rest():
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_push_to_order_proposals), "__call__"
    ) as call:
        client.batch_push_to_order_proposals(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = proposal_service.BatchPushToOrderProposalsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_fetch_marketplace_comments_empty_call_rest():
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.fetch_marketplace_comments), "__call__"
    ) as call:
        client.fetch_marketplace_comments(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = proposal_service.FetchMarketplaceCommentsRequest()
        assert args[0] == request_msg


def test_proposal_service_base_transport_error():
    # Passing both a credentials object and credentials_file should raise an error
    with pytest.raises(core_exceptions.DuplicateCredentialArgs):
        transport = transports.ProposalServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            credentials_file="credentials.json",
        )


def test_proposal_service_base_transport():
    # Instantiate the base transport.
    with mock.patch(
        "google.ads.admanager_v1.services.proposal_service.transports.ProposalServiceTransport.__init__"
    ) as Transport:
        Transport.return_value = None
        transport = transports.ProposalServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        "get_proposal",
        "list_proposals",
        "create_proposal",
        "batch_create_proposals",
        "update_proposal",
        "batch_update_proposals",
        "batch_archive_proposals",
        "batch_unarchive_proposals",
        "batch_pause_proposals",
        "batch_resume_proposals",
        "batch_request_buyer_review_proposals",
        "batch_request_buyer_accept_proposals",
        "batch_reserve_proposals",
        "batch_redraft_proposals",
        "batch_discard_draft_proposals",
        "batch_terminate_proposals",
        "batch_push_to_order_proposals",
        "fetch_marketplace_comments",
        "get_operation",
        "cancel_operation",
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


def test_proposal_service_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with (
        mock.patch.object(
            google.auth, "load_credentials_from_file", autospec=True
        ) as load_creds,
        mock.patch(
            "google.ads.admanager_v1.services.proposal_service.transports.ProposalServiceTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        load_creds.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.ProposalServiceTransport(
            credentials_file="credentials.json",
            quota_project_id="octopus",
        )
        load_creds.assert_called_once_with(
            "credentials.json",
            scopes=None,
            default_scopes=(
                "https://www.googleapis.com/auth/admanager",
                "https://www.googleapis.com/auth/admanager.readonly",
            ),
            quota_project_id="octopus",
        )


def test_proposal_service_base_transport_with_adc():
    # Test the default credentials are used if credentials and credentials_file are None.
    with (
        mock.patch.object(google.auth, "default", autospec=True) as adc,
        mock.patch(
            "google.ads.admanager_v1.services.proposal_service.transports.ProposalServiceTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.ProposalServiceTransport()
        adc.assert_called_once()


def test_proposal_service_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        ProposalServiceClient()
        adc.assert_called_once_with(
            scopes=None,
            default_scopes=(
                "https://www.googleapis.com/auth/admanager",
                "https://www.googleapis.com/auth/admanager.readonly",
            ),
            quota_project_id=None,
        )


def test_proposal_service_http_transport_client_cert_source_for_mtls():
    cred = ga_credentials.AnonymousCredentials()
    with mock.patch(
        "google.auth.transport.requests.AuthorizedSession.configure_mtls_channel"
    ) as mock_configure_mtls_channel:
        transports.ProposalServiceRestTransport(
            credentials=cred, client_cert_source_for_mtls=client_cert_source_callback
        )
        mock_configure_mtls_channel.assert_called_once_with(client_cert_source_callback)


@pytest.mark.parametrize(
    "transport_name",
    [
        "rest",
    ],
)
def test_proposal_service_host_no_port(transport_name):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="admanager.googleapis.com"
        ),
        transport=transport_name,
    )
    assert client.transport._host == (
        "admanager.googleapis.com:443"
        if transport_name in ["grpc", "grpc_asyncio"]
        else "https://admanager.googleapis.com"
    )


@pytest.mark.parametrize(
    "transport_name",
    [
        "rest",
    ],
)
def test_proposal_service_host_with_port(transport_name):
    client = ProposalServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options=client_options.ClientOptions(
            api_endpoint="admanager.googleapis.com:8000"
        ),
        transport=transport_name,
    )
    assert client.transport._host == (
        "admanager.googleapis.com:8000"
        if transport_name in ["grpc", "grpc_asyncio"]
        else "https://admanager.googleapis.com:8000"
    )


@pytest.mark.parametrize(
    "transport_name",
    [
        "rest",
    ],
)
def test_proposal_service_client_transport_session_collision(transport_name):
    creds1 = ga_credentials.AnonymousCredentials()
    creds2 = ga_credentials.AnonymousCredentials()
    client1 = ProposalServiceClient(
        credentials=creds1,
        transport=transport_name,
    )
    client2 = ProposalServiceClient(
        credentials=creds2,
        transport=transport_name,
    )
    session1 = client1.transport.get_proposal._session
    session2 = client2.transport.get_proposal._session
    assert session1 != session2
    session1 = client1.transport.list_proposals._session
    session2 = client2.transport.list_proposals._session
    assert session1 != session2
    session1 = client1.transport.create_proposal._session
    session2 = client2.transport.create_proposal._session
    assert session1 != session2
    session1 = client1.transport.batch_create_proposals._session
    session2 = client2.transport.batch_create_proposals._session
    assert session1 != session2
    session1 = client1.transport.update_proposal._session
    session2 = client2.transport.update_proposal._session
    assert session1 != session2
    session1 = client1.transport.batch_update_proposals._session
    session2 = client2.transport.batch_update_proposals._session
    assert session1 != session2
    session1 = client1.transport.batch_archive_proposals._session
    session2 = client2.transport.batch_archive_proposals._session
    assert session1 != session2
    session1 = client1.transport.batch_unarchive_proposals._session
    session2 = client2.transport.batch_unarchive_proposals._session
    assert session1 != session2
    session1 = client1.transport.batch_pause_proposals._session
    session2 = client2.transport.batch_pause_proposals._session
    assert session1 != session2
    session1 = client1.transport.batch_resume_proposals._session
    session2 = client2.transport.batch_resume_proposals._session
    assert session1 != session2
    session1 = client1.transport.batch_request_buyer_review_proposals._session
    session2 = client2.transport.batch_request_buyer_review_proposals._session
    assert session1 != session2
    session1 = client1.transport.batch_request_buyer_accept_proposals._session
    session2 = client2.transport.batch_request_buyer_accept_proposals._session
    assert session1 != session2
    session1 = client1.transport.batch_reserve_proposals._session
    session2 = client2.transport.batch_reserve_proposals._session
    assert session1 != session2
    session1 = client1.transport.batch_redraft_proposals._session
    session2 = client2.transport.batch_redraft_proposals._session
    assert session1 != session2
    session1 = client1.transport.batch_discard_draft_proposals._session
    session2 = client2.transport.batch_discard_draft_proposals._session
    assert session1 != session2
    session1 = client1.transport.batch_terminate_proposals._session
    session2 = client2.transport.batch_terminate_proposals._session
    assert session1 != session2
    session1 = client1.transport.batch_push_to_order_proposals._session
    session2 = client2.transport.batch_push_to_order_proposals._session
    assert session1 != session2
    session1 = client1.transport.fetch_marketplace_comments._session
    session2 = client2.transport.fetch_marketplace_comments._session
    assert session1 != session2


def test_ad_category_path():
    network_code = "squid"
    ad_category = "clam"
    expected = "networks/{network_code}/adCategories/{ad_category}".format(
        network_code=network_code,
        ad_category=ad_category,
    )
    actual = ProposalServiceClient.ad_category_path(network_code, ad_category)
    assert expected == actual


def test_parse_ad_category_path():
    expected = {
        "network_code": "whelk",
        "ad_category": "octopus",
    }
    path = ProposalServiceClient.ad_category_path(**expected)

    # Check that the path construction is reversible.
    actual = ProposalServiceClient.parse_ad_category_path(path)
    assert expected == actual


def test_ad_spot_path():
    network_code = "oyster"
    ad_spot = "nudibranch"
    expected = "networks/{network_code}/adSpots/{ad_spot}".format(
        network_code=network_code,
        ad_spot=ad_spot,
    )
    actual = ProposalServiceClient.ad_spot_path(network_code, ad_spot)
    assert expected == actual


def test_parse_ad_spot_path():
    expected = {
        "network_code": "cuttlefish",
        "ad_spot": "mussel",
    }
    path = ProposalServiceClient.ad_spot_path(**expected)

    # Check that the path construction is reversible.
    actual = ProposalServiceClient.parse_ad_spot_path(path)
    assert expected == actual


def test_ad_unit_path():
    network_code = "winkle"
    ad_unit = "nautilus"
    expected = "networks/{network_code}/adUnits/{ad_unit}".format(
        network_code=network_code,
        ad_unit=ad_unit,
    )
    actual = ProposalServiceClient.ad_unit_path(network_code, ad_unit)
    assert expected == actual


def test_parse_ad_unit_path():
    expected = {
        "network_code": "scallop",
        "ad_unit": "abalone",
    }
    path = ProposalServiceClient.ad_unit_path(**expected)

    # Check that the path construction is reversible.
    actual = ProposalServiceClient.parse_ad_unit_path(path)
    assert expected == actual


def test_application_path():
    network_code = "squid"
    application = "clam"
    expected = "networks/{network_code}/applications/{application}".format(
        network_code=network_code,
        application=application,
    )
    actual = ProposalServiceClient.application_path(network_code, application)
    assert expected == actual


def test_parse_application_path():
    expected = {
        "network_code": "whelk",
        "application": "octopus",
    }
    path = ProposalServiceClient.application_path(**expected)

    # Check that the path construction is reversible.
    actual = ProposalServiceClient.parse_application_path(path)
    assert expected == actual


def test_audience_segment_path():
    network_code = "oyster"
    audience_segment = "nudibranch"
    expected = "networks/{network_code}/audienceSegments/{audience_segment}".format(
        network_code=network_code,
        audience_segment=audience_segment,
    )
    actual = ProposalServiceClient.audience_segment_path(network_code, audience_segment)
    assert expected == actual


def test_parse_audience_segment_path():
    expected = {
        "network_code": "cuttlefish",
        "audience_segment": "mussel",
    }
    path = ProposalServiceClient.audience_segment_path(**expected)

    # Check that the path construction is reversible.
    actual = ProposalServiceClient.parse_audience_segment_path(path)
    assert expected == actual


def test_bandwidth_group_path():
    network_code = "winkle"
    bandwidth_group = "nautilus"
    expected = "networks/{network_code}/bandwidthGroups/{bandwidth_group}".format(
        network_code=network_code,
        bandwidth_group=bandwidth_group,
    )
    actual = ProposalServiceClient.bandwidth_group_path(network_code, bandwidth_group)
    assert expected == actual


def test_parse_bandwidth_group_path():
    expected = {
        "network_code": "scallop",
        "bandwidth_group": "abalone",
    }
    path = ProposalServiceClient.bandwidth_group_path(**expected)

    # Check that the path construction is reversible.
    actual = ProposalServiceClient.parse_bandwidth_group_path(path)
    assert expected == actual


def test_browser_path():
    network_code = "squid"
    browser = "clam"
    expected = "networks/{network_code}/browsers/{browser}".format(
        network_code=network_code,
        browser=browser,
    )
    actual = ProposalServiceClient.browser_path(network_code, browser)
    assert expected == actual


def test_parse_browser_path():
    expected = {
        "network_code": "whelk",
        "browser": "octopus",
    }
    path = ProposalServiceClient.browser_path(**expected)

    # Check that the path construction is reversible.
    actual = ProposalServiceClient.parse_browser_path(path)
    assert expected == actual


def test_browser_language_path():
    network_code = "oyster"
    browser_language = "nudibranch"
    expected = "networks/{network_code}/browserLanguages/{browser_language}".format(
        network_code=network_code,
        browser_language=browser_language,
    )
    actual = ProposalServiceClient.browser_language_path(network_code, browser_language)
    assert expected == actual


def test_parse_browser_language_path():
    expected = {
        "network_code": "cuttlefish",
        "browser_language": "mussel",
    }
    path = ProposalServiceClient.browser_language_path(**expected)

    # Check that the path construction is reversible.
    actual = ProposalServiceClient.parse_browser_language_path(path)
    assert expected == actual


def test_cms_metadata_value_path():
    network_code = "winkle"
    cms_metadata_value = "nautilus"
    expected = "networks/{network_code}/cmsMetadataValues/{cms_metadata_value}".format(
        network_code=network_code,
        cms_metadata_value=cms_metadata_value,
    )
    actual = ProposalServiceClient.cms_metadata_value_path(
        network_code, cms_metadata_value
    )
    assert expected == actual


def test_parse_cms_metadata_value_path():
    expected = {
        "network_code": "scallop",
        "cms_metadata_value": "abalone",
    }
    path = ProposalServiceClient.cms_metadata_value_path(**expected)

    # Check that the path construction is reversible.
    actual = ProposalServiceClient.parse_cms_metadata_value_path(path)
    assert expected == actual


def test_company_path():
    network_code = "squid"
    company = "clam"
    expected = "networks/{network_code}/companies/{company}".format(
        network_code=network_code,
        company=company,
    )
    actual = ProposalServiceClient.company_path(network_code, company)
    assert expected == actual


def test_parse_company_path():
    expected = {
        "network_code": "whelk",
        "company": "octopus",
    }
    path = ProposalServiceClient.company_path(**expected)

    # Check that the path construction is reversible.
    actual = ProposalServiceClient.parse_company_path(path)
    assert expected == actual


def test_contact_path():
    network_code = "oyster"
    contact = "nudibranch"
    expected = "networks/{network_code}/contacts/{contact}".format(
        network_code=network_code,
        contact=contact,
    )
    actual = ProposalServiceClient.contact_path(network_code, contact)
    assert expected == actual


def test_parse_contact_path():
    expected = {
        "network_code": "cuttlefish",
        "contact": "mussel",
    }
    path = ProposalServiceClient.contact_path(**expected)

    # Check that the path construction is reversible.
    actual = ProposalServiceClient.parse_contact_path(path)
    assert expected == actual


def test_content_path():
    network_code = "winkle"
    content = "nautilus"
    expected = "networks/{network_code}/content/{content}".format(
        network_code=network_code,
        content=content,
    )
    actual = ProposalServiceClient.content_path(network_code, content)
    assert expected == actual


def test_parse_content_path():
    expected = {
        "network_code": "scallop",
        "content": "abalone",
    }
    path = ProposalServiceClient.content_path(**expected)

    # Check that the path construction is reversible.
    actual = ProposalServiceClient.parse_content_path(path)
    assert expected == actual


def test_content_bundle_path():
    network_code = "squid"
    content_bundle = "clam"
    expected = "networks/{network_code}/contentBundles/{content_bundle}".format(
        network_code=network_code,
        content_bundle=content_bundle,
    )
    actual = ProposalServiceClient.content_bundle_path(network_code, content_bundle)
    assert expected == actual


def test_parse_content_bundle_path():
    expected = {
        "network_code": "whelk",
        "content_bundle": "octopus",
    }
    path = ProposalServiceClient.content_bundle_path(**expected)

    # Check that the path construction is reversible.
    actual = ProposalServiceClient.parse_content_bundle_path(path)
    assert expected == actual


def test_content_label_path():
    network_code = "oyster"
    content_label = "nudibranch"
    expected = "networks/{network_code}/contentLabels/{content_label}".format(
        network_code=network_code,
        content_label=content_label,
    )
    actual = ProposalServiceClient.content_label_path(network_code, content_label)
    assert expected == actual


def test_parse_content_label_path():
    expected = {
        "network_code": "cuttlefish",
        "content_label": "mussel",
    }
    path = ProposalServiceClient.content_label_path(**expected)

    # Check that the path construction is reversible.
    actual = ProposalServiceClient.parse_content_label_path(path)
    assert expected == actual


def test_custom_field_path():
    network_code = "winkle"
    custom_field = "nautilus"
    expected = "networks/{network_code}/customFields/{custom_field}".format(
        network_code=network_code,
        custom_field=custom_field,
    )
    actual = ProposalServiceClient.custom_field_path(network_code, custom_field)
    assert expected == actual


def test_parse_custom_field_path():
    expected = {
        "network_code": "scallop",
        "custom_field": "abalone",
    }
    path = ProposalServiceClient.custom_field_path(**expected)

    # Check that the path construction is reversible.
    actual = ProposalServiceClient.parse_custom_field_path(path)
    assert expected == actual


def test_custom_targeting_key_path():
    network_code = "squid"
    custom_targeting_key = "clam"
    expected = (
        "networks/{network_code}/customTargetingKeys/{custom_targeting_key}".format(
            network_code=network_code,
            custom_targeting_key=custom_targeting_key,
        )
    )
    actual = ProposalServiceClient.custom_targeting_key_path(
        network_code, custom_targeting_key
    )
    assert expected == actual


def test_parse_custom_targeting_key_path():
    expected = {
        "network_code": "whelk",
        "custom_targeting_key": "octopus",
    }
    path = ProposalServiceClient.custom_targeting_key_path(**expected)

    # Check that the path construction is reversible.
    actual = ProposalServiceClient.parse_custom_targeting_key_path(path)
    assert expected == actual


def test_custom_targeting_value_path():
    network_code = "oyster"
    custom_targeting_value = "nudibranch"
    expected = (
        "networks/{network_code}/customTargetingValues/{custom_targeting_value}".format(
            network_code=network_code,
            custom_targeting_value=custom_targeting_value,
        )
    )
    actual = ProposalServiceClient.custom_targeting_value_path(
        network_code, custom_targeting_value
    )
    assert expected == actual


def test_parse_custom_targeting_value_path():
    expected = {
        "network_code": "cuttlefish",
        "custom_targeting_value": "mussel",
    }
    path = ProposalServiceClient.custom_targeting_value_path(**expected)

    # Check that the path construction is reversible.
    actual = ProposalServiceClient.parse_custom_targeting_value_path(path)
    assert expected == actual


def test_device_capability_path():
    network_code = "winkle"
    device_capability = "nautilus"
    expected = "networks/{network_code}/deviceCapabilities/{device_capability}".format(
        network_code=network_code,
        device_capability=device_capability,
    )
    actual = ProposalServiceClient.device_capability_path(
        network_code, device_capability
    )
    assert expected == actual


def test_parse_device_capability_path():
    expected = {
        "network_code": "scallop",
        "device_capability": "abalone",
    }
    path = ProposalServiceClient.device_capability_path(**expected)

    # Check that the path construction is reversible.
    actual = ProposalServiceClient.parse_device_capability_path(path)
    assert expected == actual


def test_device_category_path():
    network_code = "squid"
    device_category = "clam"
    expected = "networks/{network_code}/deviceCategories/{device_category}".format(
        network_code=network_code,
        device_category=device_category,
    )
    actual = ProposalServiceClient.device_category_path(network_code, device_category)
    assert expected == actual


def test_parse_device_category_path():
    expected = {
        "network_code": "whelk",
        "device_category": "octopus",
    }
    path = ProposalServiceClient.device_category_path(**expected)

    # Check that the path construction is reversible.
    actual = ProposalServiceClient.parse_device_category_path(path)
    assert expected == actual


def test_device_manufacturer_path():
    network_code = "oyster"
    device_manufacturer = "nudibranch"
    expected = (
        "networks/{network_code}/deviceManufacturers/{device_manufacturer}".format(
            network_code=network_code,
            device_manufacturer=device_manufacturer,
        )
    )
    actual = ProposalServiceClient.device_manufacturer_path(
        network_code, device_manufacturer
    )
    assert expected == actual


def test_parse_device_manufacturer_path():
    expected = {
        "network_code": "cuttlefish",
        "device_manufacturer": "mussel",
    }
    path = ProposalServiceClient.device_manufacturer_path(**expected)

    # Check that the path construction is reversible.
    actual = ProposalServiceClient.parse_device_manufacturer_path(path)
    assert expected == actual


def test_geo_target_path():
    network_code = "winkle"
    geo_target = "nautilus"
    expected = "networks/{network_code}/geoTargets/{geo_target}".format(
        network_code=network_code,
        geo_target=geo_target,
    )
    actual = ProposalServiceClient.geo_target_path(network_code, geo_target)
    assert expected == actual


def test_parse_geo_target_path():
    expected = {
        "network_code": "scallop",
        "geo_target": "abalone",
    }
    path = ProposalServiceClient.geo_target_path(**expected)

    # Check that the path construction is reversible.
    actual = ProposalServiceClient.parse_geo_target_path(path)
    assert expected == actual


def test_inventory_url_path():
    network_code = "squid"
    inventory_url = "clam"
    expected = "networks/{network_code}/inventoryUrls/{inventory_url}".format(
        network_code=network_code,
        inventory_url=inventory_url,
    )
    actual = ProposalServiceClient.inventory_url_path(network_code, inventory_url)
    assert expected == actual


def test_parse_inventory_url_path():
    expected = {
        "network_code": "whelk",
        "inventory_url": "octopus",
    }
    path = ProposalServiceClient.inventory_url_path(**expected)

    # Check that the path construction is reversible.
    actual = ProposalServiceClient.parse_inventory_url_path(path)
    assert expected == actual


def test_label_path():
    network_code = "oyster"
    label = "nudibranch"
    expected = "networks/{network_code}/labels/{label}".format(
        network_code=network_code,
        label=label,
    )
    actual = ProposalServiceClient.label_path(network_code, label)
    assert expected == actual


def test_parse_label_path():
    expected = {
        "network_code": "cuttlefish",
        "label": "mussel",
    }
    path = ProposalServiceClient.label_path(**expected)

    # Check that the path construction is reversible.
    actual = ProposalServiceClient.parse_label_path(path)
    assert expected == actual


def test_mobile_carrier_path():
    network_code = "winkle"
    mobile_carrier = "nautilus"
    expected = "networks/{network_code}/mobileCarriers/{mobile_carrier}".format(
        network_code=network_code,
        mobile_carrier=mobile_carrier,
    )
    actual = ProposalServiceClient.mobile_carrier_path(network_code, mobile_carrier)
    assert expected == actual


def test_parse_mobile_carrier_path():
    expected = {
        "network_code": "scallop",
        "mobile_carrier": "abalone",
    }
    path = ProposalServiceClient.mobile_carrier_path(**expected)

    # Check that the path construction is reversible.
    actual = ProposalServiceClient.parse_mobile_carrier_path(path)
    assert expected == actual


def test_mobile_device_path():
    network_code = "squid"
    mobile_device = "clam"
    expected = "networks/{network_code}/mobileDevices/{mobile_device}".format(
        network_code=network_code,
        mobile_device=mobile_device,
    )
    actual = ProposalServiceClient.mobile_device_path(network_code, mobile_device)
    assert expected == actual


def test_parse_mobile_device_path():
    expected = {
        "network_code": "whelk",
        "mobile_device": "octopus",
    }
    path = ProposalServiceClient.mobile_device_path(**expected)

    # Check that the path construction is reversible.
    actual = ProposalServiceClient.parse_mobile_device_path(path)
    assert expected == actual


def test_mobile_device_submodel_path():
    network_code = "oyster"
    mobile_device_submodel = "nudibranch"
    expected = (
        "networks/{network_code}/mobileDeviceSubmodels/{mobile_device_submodel}".format(
            network_code=network_code,
            mobile_device_submodel=mobile_device_submodel,
        )
    )
    actual = ProposalServiceClient.mobile_device_submodel_path(
        network_code, mobile_device_submodel
    )
    assert expected == actual


def test_parse_mobile_device_submodel_path():
    expected = {
        "network_code": "cuttlefish",
        "mobile_device_submodel": "mussel",
    }
    path = ProposalServiceClient.mobile_device_submodel_path(**expected)

    # Check that the path construction is reversible.
    actual = ProposalServiceClient.parse_mobile_device_submodel_path(path)
    assert expected == actual


def test_network_path():
    network_code = "winkle"
    expected = "networks/{network_code}".format(
        network_code=network_code,
    )
    actual = ProposalServiceClient.network_path(network_code)
    assert expected == actual


def test_parse_network_path():
    expected = {
        "network_code": "nautilus",
    }
    path = ProposalServiceClient.network_path(**expected)

    # Check that the path construction is reversible.
    actual = ProposalServiceClient.parse_network_path(path)
    assert expected == actual


def test_operating_system_path():
    network_code = "scallop"
    operating_system = "abalone"
    expected = "networks/{network_code}/operatingSystems/{operating_system}".format(
        network_code=network_code,
        operating_system=operating_system,
    )
    actual = ProposalServiceClient.operating_system_path(network_code, operating_system)
    assert expected == actual


def test_parse_operating_system_path():
    expected = {
        "network_code": "squid",
        "operating_system": "clam",
    }
    path = ProposalServiceClient.operating_system_path(**expected)

    # Check that the path construction is reversible.
    actual = ProposalServiceClient.parse_operating_system_path(path)
    assert expected == actual


def test_operating_system_version_path():
    network_code = "whelk"
    operating_system_version = "octopus"
    expected = "networks/{network_code}/operatingSystemVersions/{operating_system_version}".format(
        network_code=network_code,
        operating_system_version=operating_system_version,
    )
    actual = ProposalServiceClient.operating_system_version_path(
        network_code, operating_system_version
    )
    assert expected == actual


def test_parse_operating_system_version_path():
    expected = {
        "network_code": "oyster",
        "operating_system_version": "nudibranch",
    }
    path = ProposalServiceClient.operating_system_version_path(**expected)

    # Check that the path construction is reversible.
    actual = ProposalServiceClient.parse_operating_system_version_path(path)
    assert expected == actual


def test_order_path():
    network_code = "cuttlefish"
    order = "mussel"
    expected = "networks/{network_code}/orders/{order}".format(
        network_code=network_code,
        order=order,
    )
    actual = ProposalServiceClient.order_path(network_code, order)
    assert expected == actual


def test_parse_order_path():
    expected = {
        "network_code": "winkle",
        "order": "nautilus",
    }
    path = ProposalServiceClient.order_path(**expected)

    # Check that the path construction is reversible.
    actual = ProposalServiceClient.parse_order_path(path)
    assert expected == actual


def test_placement_path():
    network_code = "scallop"
    placement = "abalone"
    expected = "networks/{network_code}/placements/{placement}".format(
        network_code=network_code,
        placement=placement,
    )
    actual = ProposalServiceClient.placement_path(network_code, placement)
    assert expected == actual


def test_parse_placement_path():
    expected = {
        "network_code": "squid",
        "placement": "clam",
    }
    path = ProposalServiceClient.placement_path(**expected)

    # Check that the path construction is reversible.
    actual = ProposalServiceClient.parse_placement_path(path)
    assert expected == actual


def test_proposal_path():
    network_code = "whelk"
    proposal = "octopus"
    expected = "networks/{network_code}/proposals/{proposal}".format(
        network_code=network_code,
        proposal=proposal,
    )
    actual = ProposalServiceClient.proposal_path(network_code, proposal)
    assert expected == actual


def test_parse_proposal_path():
    expected = {
        "network_code": "oyster",
        "proposal": "nudibranch",
    }
    path = ProposalServiceClient.proposal_path(**expected)

    # Check that the path construction is reversible.
    actual = ProposalServiceClient.parse_proposal_path(path)
    assert expected == actual


def test_taxonomy_category_path():
    network_code = "cuttlefish"
    taxonomy_category = "mussel"
    expected = "networks/{network_code}/taxonomyCategories/{taxonomy_category}".format(
        network_code=network_code,
        taxonomy_category=taxonomy_category,
    )
    actual = ProposalServiceClient.taxonomy_category_path(
        network_code, taxonomy_category
    )
    assert expected == actual


def test_parse_taxonomy_category_path():
    expected = {
        "network_code": "winkle",
        "taxonomy_category": "nautilus",
    }
    path = ProposalServiceClient.taxonomy_category_path(**expected)

    # Check that the path construction is reversible.
    actual = ProposalServiceClient.parse_taxonomy_category_path(path)
    assert expected == actual


def test_team_path():
    network_code = "scallop"
    team = "abalone"
    expected = "networks/{network_code}/teams/{team}".format(
        network_code=network_code,
        team=team,
    )
    actual = ProposalServiceClient.team_path(network_code, team)
    assert expected == actual


def test_parse_team_path():
    expected = {
        "network_code": "squid",
        "team": "clam",
    }
    path = ProposalServiceClient.team_path(**expected)

    # Check that the path construction is reversible.
    actual = ProposalServiceClient.parse_team_path(path)
    assert expected == actual


def test_user_path():
    network_code = "whelk"
    user = "octopus"
    expected = "networks/{network_code}/users/{user}".format(
        network_code=network_code,
        user=user,
    )
    actual = ProposalServiceClient.user_path(network_code, user)
    assert expected == actual


def test_parse_user_path():
    expected = {
        "network_code": "oyster",
        "user": "nudibranch",
    }
    path = ProposalServiceClient.user_path(**expected)

    # Check that the path construction is reversible.
    actual = ProposalServiceClient.parse_user_path(path)
    assert expected == actual


def test_common_billing_account_path():
    billing_account = "cuttlefish"
    expected = "billingAccounts/{billing_account}".format(
        billing_account=billing_account,
    )
    actual = ProposalServiceClient.common_billing_account_path(billing_account)
    assert expected == actual


def test_parse_common_billing_account_path():
    expected = {
        "billing_account": "mussel",
    }
    path = ProposalServiceClient.common_billing_account_path(**expected)

    # Check that the path construction is reversible.
    actual = ProposalServiceClient.parse_common_billing_account_path(path)
    assert expected == actual


def test_common_folder_path():
    folder = "winkle"
    expected = "folders/{folder}".format(
        folder=folder,
    )
    actual = ProposalServiceClient.common_folder_path(folder)
    assert expected == actual


def test_parse_common_folder_path():
    expected = {
        "folder": "nautilus",
    }
    path = ProposalServiceClient.common_folder_path(**expected)

    # Check that the path construction is reversible.
    actual = ProposalServiceClient.parse_common_folder_path(path)
    assert expected == actual


def test_common_organization_path():
    organization = "scallop"
    expected = "organizations/{organization}".format(
        organization=organization,
    )
    actual = ProposalServiceClient.common_organization_path(organization)
    assert expected == actual


def test_parse_common_organization_path():
    expected = {
        "organization": "abalone",
    }
    path = ProposalServiceClient.common_organization_path(**expected)

    # Check that the path construction is reversible.
    actual = ProposalServiceClient.parse_common_organization_path(path)
    assert expected == actual


def test_common_project_path():
    project = "squid"
    expected = "projects/{project}".format(
        project=project,
    )
    actual = ProposalServiceClient.common_project_path(project)
    assert expected == actual


def test_parse_common_project_path():
    expected = {
        "project": "clam",
    }
    path = ProposalServiceClient.common_project_path(**expected)

    # Check that the path construction is reversible.
    actual = ProposalServiceClient.parse_common_project_path(path)
    assert expected == actual


def test_common_location_path():
    project = "whelk"
    location = "octopus"
    expected = "projects/{project}/locations/{location}".format(
        project=project,
        location=location,
    )
    actual = ProposalServiceClient.common_location_path(project, location)
    assert expected == actual


def test_parse_common_location_path():
    expected = {
        "project": "oyster",
        "location": "nudibranch",
    }
    path = ProposalServiceClient.common_location_path(**expected)

    # Check that the path construction is reversible.
    actual = ProposalServiceClient.parse_common_location_path(path)
    assert expected == actual


def test_client_with_default_client_info():
    client_info = gapic_v1.client_info.ClientInfo()

    with mock.patch.object(
        transports.ProposalServiceTransport, "_prep_wrapped_messages"
    ) as prep:
        client = ProposalServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

    with mock.patch.object(
        transports.ProposalServiceTransport, "_prep_wrapped_messages"
    ) as prep:
        transport_class = ProposalServiceClient.get_transport_class()
        transport = transport_class(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)


def test_transport_close_rest():
    client = ProposalServiceClient(
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
        client = ProposalServiceClient(
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
        (ProposalServiceClient, transports.ProposalServiceRestTransport),
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
