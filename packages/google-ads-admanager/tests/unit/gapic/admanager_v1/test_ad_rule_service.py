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
import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
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

from google.ads.admanager_v1.services.ad_rule_service import (
    AdRuleServiceClient,
    pagers,
    transports,
)
from google.ads.admanager_v1.types import (
    ad_rule_enums,
    ad_rule_messages,
    ad_rule_service,
    ad_rule_slot_behavior_enum,
    ad_rule_slot_bumper_enum,
    ad_rule_slot_midroll_frequency_type_enum,
    request_platform_enum,
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

    assert AdRuleServiceClient._get_client_cert_source(None, False) is None
    assert (
        AdRuleServiceClient._get_client_cert_source(mock_provided_cert_source, False)
        is None
    )
    assert (
        AdRuleServiceClient._get_client_cert_source(mock_provided_cert_source, True)
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
                AdRuleServiceClient._get_client_cert_source(None, True)
                is mock_default_cert_source
            )
            assert (
                AdRuleServiceClient._get_client_cert_source(
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
    client = AdRuleServiceClient(credentials=cred)
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
    client = AdRuleServiceClient(credentials=cred)
    client._transport._credentials = cred

    error = core_exceptions.GoogleAPICallError("message", details=[])
    error.code = error_code

    client._add_cred_info_for_auth_errors(error)
    assert error.details == []


@pytest.mark.parametrize(
    "client_class,transport_name",
    [
        (AdRuleServiceClient, "rest"),
    ],
)
def test_ad_rule_service_client_from_service_account_info(client_class, transport_name):
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
        (transports.AdRuleServiceRestTransport, "rest"),
    ],
)
def test_ad_rule_service_client_service_account_always_use_jwt(
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
        (AdRuleServiceClient, "rest"),
    ],
)
def test_ad_rule_service_client_from_service_account_file(client_class, transport_name):
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


def test_ad_rule_service_client_get_transport_class():
    transport = AdRuleServiceClient.get_transport_class()
    available_transports = [
        transports.AdRuleServiceRestTransport,
    ]
    assert transport in available_transports

    transport = AdRuleServiceClient.get_transport_class("rest")
    assert transport == transports.AdRuleServiceRestTransport


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (AdRuleServiceClient, transports.AdRuleServiceRestTransport, "rest"),
    ],
)
@mock.patch.object(
    AdRuleServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(AdRuleServiceClient),
)
def test_ad_rule_service_client_client_options(
    client_class, transport_class, transport_name
):
    # Check that if channel is provided we won't create a new one.
    with mock.patch.object(AdRuleServiceClient, "get_transport_class") as gtc:
        transport = transport_class(credentials=ga_credentials.AnonymousCredentials())
        client = client_class(transport=transport)
        gtc.assert_not_called()

    # Check that if channel is provided via str we will create a new one.
    with mock.patch.object(AdRuleServiceClient, "get_transport_class") as gtc:
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
        (AdRuleServiceClient, transports.AdRuleServiceRestTransport, "rest", "true"),
        (AdRuleServiceClient, transports.AdRuleServiceRestTransport, "rest", "false"),
    ],
)
@mock.patch.object(
    AdRuleServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(AdRuleServiceClient),
)
@mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "auto"})
def test_ad_rule_service_client_mtls_env_auto(
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


@pytest.mark.parametrize("client_class", [AdRuleServiceClient])
@mock.patch.object(
    AdRuleServiceClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(AdRuleServiceClient),
)
def test_ad_rule_service_client_get_mtls_endpoint_and_cert_source(client_class):
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


@pytest.mark.parametrize("client_class", [AdRuleServiceClient])
@mock.patch.object(
    AdRuleServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(AdRuleServiceClient),
)
def test_ad_rule_service_client_client_api_endpoint(client_class):
    mock_client_cert_source = client_cert_source_callback
    api_override = "foo.com"
    default_universe = AdRuleServiceClient._DEFAULT_UNIVERSE
    default_endpoint = AdRuleServiceClient._DEFAULT_ENDPOINT_TEMPLATE.format(
        UNIVERSE_DOMAIN=default_universe
    )
    mock_universe = "bar.com"
    mock_endpoint = AdRuleServiceClient._DEFAULT_ENDPOINT_TEMPLATE.format(
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
        (AdRuleServiceClient, transports.AdRuleServiceRestTransport, "rest"),
    ],
)
def test_ad_rule_service_client_client_options_scopes(
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
        (AdRuleServiceClient, transports.AdRuleServiceRestTransport, "rest", None),
    ],
)
def test_ad_rule_service_client_client_options_credentials_file(
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


def test_get_ad_rule_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = AdRuleServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_ad_rule in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_ad_rule] = mock_rpc

        request = {}
        client.get_ad_rule(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_ad_rule(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_ad_rule_rest_required_fields(
    request_type=ad_rule_service.GetAdRuleRequest,
):
    transport_class = transports.AdRuleServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGetAdRule,
        "_BaseGetAdRule__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = ad_rule_messages.AdRule()
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
            return_value = ad_rule_messages.AdRule.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get_ad_rule(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_ad_rule_rest_flattened():
    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = ad_rule_messages.AdRule()

        # get arguments that satisfy an http rule for this method
        sample_request = {"name": "networks/sample1/adRules/sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = ad_rule_messages.AdRule.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get_ad_rule(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{name=networks/*/adRules/*}" % client.transport._host, args[1]
        )


def test_get_ad_rule_rest_flattened_error(transport: str = "rest"):
    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_ad_rule(
            ad_rule_service.GetAdRuleRequest(),
            name="name_value",
        )


def test_list_ad_rules_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = AdRuleServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_ad_rules in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_ad_rules] = mock_rpc

        request = {}
        client.list_ad_rules(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_ad_rules(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_ad_rules_rest_required_fields(
    request_type=ad_rule_service.ListAdRulesRequest,
):
    transport_class = transports.AdRuleServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseListAdRules,
        "_BaseListAdRules__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = ad_rule_service.ListAdRulesResponse()
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
            return_value = ad_rule_service.ListAdRulesResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_ad_rules(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_ad_rules_rest_flattened():
    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = ad_rule_service.ListAdRulesResponse()

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
        return_value = ad_rule_service.ListAdRulesResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_ad_rules(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/adRules" % client.transport._host, args[1]
        )


def test_list_ad_rules_rest_flattened_error(transport: str = "rest"):
    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_ad_rules(
            ad_rule_service.ListAdRulesRequest(),
            parent="parent_value",
        )


def test_list_ad_rules_rest_pager(transport: str = "rest"):
    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            ad_rule_service.ListAdRulesResponse(
                ad_rules=[
                    ad_rule_messages.AdRule(),
                    ad_rule_messages.AdRule(),
                    ad_rule_messages.AdRule(),
                ],
                next_page_token="abc",
            ),
            ad_rule_service.ListAdRulesResponse(
                ad_rules=[],
                next_page_token="def",
            ),
            ad_rule_service.ListAdRulesResponse(
                ad_rules=[
                    ad_rule_messages.AdRule(),
                ],
                next_page_token="ghi",
            ),
            ad_rule_service.ListAdRulesResponse(
                ad_rules=[
                    ad_rule_messages.AdRule(),
                    ad_rule_messages.AdRule(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            ad_rule_service.ListAdRulesResponse.to_json(x) for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {"parent": "networks/sample1"}

        pager = client.list_ad_rules(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, ad_rule_messages.AdRule) for i in results)

        pages = list(client.list_ad_rules(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_create_ad_rule_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = AdRuleServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.create_ad_rule in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.create_ad_rule] = mock_rpc

        request = {}
        client.create_ad_rule(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.create_ad_rule(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_create_ad_rule_rest_required_fields(
    request_type=ad_rule_service.CreateAdRuleRequest,
):
    transport_class = transports.AdRuleServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseCreateAdRule,
        "_BaseCreateAdRule__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = ad_rule_messages.AdRule()
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
            return_value = ad_rule_messages.AdRule.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.create_ad_rule(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_create_ad_rule_rest_flattened():
    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = ad_rule_messages.AdRule()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "networks/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            ad_rule=ad_rule_messages.AdRule(name="name_value"),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = ad_rule_messages.AdRule.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.create_ad_rule(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/adRules" % client.transport._host, args[1]
        )


def test_create_ad_rule_rest_flattened_error(transport: str = "rest"):
    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_ad_rule(
            ad_rule_service.CreateAdRuleRequest(),
            parent="parent_value",
            ad_rule=ad_rule_messages.AdRule(name="name_value"),
        )


def test_batch_create_ad_rules_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = AdRuleServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_create_ad_rules
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.batch_create_ad_rules] = (
            mock_rpc
        )

        request = {}
        client.batch_create_ad_rules(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_create_ad_rules(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_create_ad_rules_rest_required_fields(
    request_type=ad_rule_service.BatchCreateAdRulesRequest,
):
    transport_class = transports.AdRuleServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseBatchCreateAdRules,
        "_BaseBatchCreateAdRules__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = ad_rule_service.BatchCreateAdRulesResponse()
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
            return_value = ad_rule_service.BatchCreateAdRulesResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.batch_create_ad_rules(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_create_ad_rules_rest_flattened():
    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = ad_rule_service.BatchCreateAdRulesResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "networks/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            requests=[ad_rule_service.CreateAdRuleRequest(parent="parent_value")],
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = ad_rule_service.BatchCreateAdRulesResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.batch_create_ad_rules(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/adRules:batchCreate" % client.transport._host,
            args[1],
        )


def test_batch_create_ad_rules_rest_flattened_error(transport: str = "rest"):
    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_create_ad_rules(
            ad_rule_service.BatchCreateAdRulesRequest(),
            parent="parent_value",
            requests=[ad_rule_service.CreateAdRuleRequest(parent="parent_value")],
        )


def test_update_ad_rule_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = AdRuleServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.update_ad_rule in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.update_ad_rule] = mock_rpc

        request = {}
        client.update_ad_rule(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.update_ad_rule(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_update_ad_rule_rest_required_fields(
    request_type=ad_rule_service.UpdateAdRuleRequest,
):
    transport_class = transports.AdRuleServiceRestTransport

    request_init = {}
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseUpdateAdRule,
        "_BaseUpdateAdRule__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = ad_rule_messages.AdRule()
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
            return_value = ad_rule_messages.AdRule.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.update_ad_rule(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_update_ad_rule_rest_flattened():
    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = ad_rule_messages.AdRule()

        # get arguments that satisfy an http rule for this method
        sample_request = {"ad_rule": {"name": "networks/sample1/adRules/sample2"}}

        # get truthy value for each flattened field
        mock_args = dict(
            ad_rule=ad_rule_messages.AdRule(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = ad_rule_messages.AdRule.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.update_ad_rule(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{ad_rule.name=networks/*/adRules/*}" % client.transport._host,
            args[1],
        )


def test_update_ad_rule_rest_flattened_error(transport: str = "rest"):
    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_ad_rule(
            ad_rule_service.UpdateAdRuleRequest(),
            ad_rule=ad_rule_messages.AdRule(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


def test_batch_update_ad_rules_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = AdRuleServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_update_ad_rules
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.batch_update_ad_rules] = (
            mock_rpc
        )

        request = {}
        client.batch_update_ad_rules(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_update_ad_rules(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_update_ad_rules_rest_required_fields(
    request_type=ad_rule_service.BatchUpdateAdRulesRequest,
):
    transport_class = transports.AdRuleServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseBatchUpdateAdRules,
        "_BaseBatchUpdateAdRules__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = ad_rule_service.BatchUpdateAdRulesResponse()
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
            return_value = ad_rule_service.BatchUpdateAdRulesResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.batch_update_ad_rules(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_update_ad_rules_rest_flattened():
    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = ad_rule_service.BatchUpdateAdRulesResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "networks/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            requests=[
                ad_rule_service.UpdateAdRuleRequest(
                    ad_rule=ad_rule_messages.AdRule(name="name_value")
                )
            ],
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = ad_rule_service.BatchUpdateAdRulesResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.batch_update_ad_rules(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/adRules:batchUpdate" % client.transport._host,
            args[1],
        )


def test_batch_update_ad_rules_rest_flattened_error(transport: str = "rest"):
    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_update_ad_rules(
            ad_rule_service.BatchUpdateAdRulesRequest(),
            parent="parent_value",
            requests=[
                ad_rule_service.UpdateAdRuleRequest(
                    ad_rule=ad_rule_messages.AdRule(name="name_value")
                )
            ],
        )


def test_batch_activate_ad_rules_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = AdRuleServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_activate_ad_rules
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.batch_activate_ad_rules
        ] = mock_rpc

        request = {}
        client.batch_activate_ad_rules(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_activate_ad_rules(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_activate_ad_rules_rest_required_fields(
    request_type=ad_rule_service.BatchActivateAdRulesRequest,
):
    transport_class = transports.AdRuleServiceRestTransport

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
        transport_class._BaseBatchActivateAdRules,
        "_BaseBatchActivateAdRules__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = ad_rule_service.BatchActivateAdRulesResponse()
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
            return_value = ad_rule_service.BatchActivateAdRulesResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.batch_activate_ad_rules(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_activate_ad_rules_rest_flattened():
    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = ad_rule_service.BatchActivateAdRulesResponse()

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
        return_value = ad_rule_service.BatchActivateAdRulesResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.batch_activate_ad_rules(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/adRules:batchActivate" % client.transport._host,
            args[1],
        )


def test_batch_activate_ad_rules_rest_flattened_error(transport: str = "rest"):
    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_activate_ad_rules(
            ad_rule_service.BatchActivateAdRulesRequest(),
            parent="parent_value",
            names=["names_value"],
        )


def test_batch_deactivate_ad_rules_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = AdRuleServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_deactivate_ad_rules
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.batch_deactivate_ad_rules
        ] = mock_rpc

        request = {}
        client.batch_deactivate_ad_rules(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_deactivate_ad_rules(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_deactivate_ad_rules_rest_required_fields(
    request_type=ad_rule_service.BatchDeactivateAdRulesRequest,
):
    transport_class = transports.AdRuleServiceRestTransport

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
        transport_class._BaseBatchDeactivateAdRules,
        "_BaseBatchDeactivateAdRules__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = ad_rule_service.BatchDeactivateAdRulesResponse()
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
            return_value = ad_rule_service.BatchDeactivateAdRulesResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.batch_deactivate_ad_rules(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_deactivate_ad_rules_rest_flattened():
    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = ad_rule_service.BatchDeactivateAdRulesResponse()

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
        return_value = ad_rule_service.BatchDeactivateAdRulesResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.batch_deactivate_ad_rules(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/adRules:batchDeactivate"
            % client.transport._host,
            args[1],
        )


def test_batch_deactivate_ad_rules_rest_flattened_error(transport: str = "rest"):
    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_deactivate_ad_rules(
            ad_rule_service.BatchDeactivateAdRulesRequest(),
            parent="parent_value",
            names=["names_value"],
        )


def test_batch_delete_ad_rules_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = AdRuleServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_delete_ad_rules
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.batch_delete_ad_rules] = (
            mock_rpc
        )

        request = {}
        client.batch_delete_ad_rules(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_delete_ad_rules(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_delete_ad_rules_rest_required_fields(
    request_type=ad_rule_service.BatchDeleteAdRulesRequest,
):
    transport_class = transports.AdRuleServiceRestTransport

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
        transport_class._BaseBatchDeleteAdRules,
        "_BaseBatchDeleteAdRules__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = None
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
            json_return_value = ""

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.batch_delete_ad_rules(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_delete_ad_rules_rest_flattened():
    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = None

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
        json_return_value = ""
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.batch_delete_ad_rules(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/adRules:batchDelete" % client.transport._host,
            args[1],
        )


def test_batch_delete_ad_rules_rest_flattened_error(transport: str = "rest"):
    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_delete_ad_rules(
            ad_rule_service.BatchDeleteAdRulesRequest(),
            parent="parent_value",
            names=["names_value"],
        )


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.AdRuleServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = AdRuleServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport=transport,
        )

    # It is an error to provide a credentials file and a transport instance.
    transport = transports.AdRuleServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = AdRuleServiceClient(
            client_options={"credentials_file": "credentials.json"},
            transport=transport,
        )

    # It is an error to provide an api_key and a transport instance.
    transport = transports.AdRuleServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = AdRuleServiceClient(
            client_options=options,
            transport=transport,
        )

    # It is an error to provide an api_key and a credential.
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = AdRuleServiceClient(
            client_options=options, credentials=ga_credentials.AnonymousCredentials()
        )

    # It is an error to provide scopes and a transport instance.
    transport = transports.AdRuleServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = AdRuleServiceClient(
            client_options={"scopes": ["1", "2"]},
            transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.AdRuleServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    client = AdRuleServiceClient(transport=transport)
    assert client.transport is transport


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.AdRuleServiceRestTransport,
    ],
)
def test_transport_adc(transport_class):
    # Test default credentials are used if not provided.
    with mock.patch.object(google.auth, "default") as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class()
        adc.assert_called_once()


def test_transport_kind_rest():
    transport = AdRuleServiceClient.get_transport_class("rest")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "rest"


def test_get_ad_rule_rest_bad_request(request_type=ad_rule_service.GetAdRuleRequest):
    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"name": "networks/sample1/adRules/sample2"}
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
        client.get_ad_rule(request)


@pytest.mark.parametrize(
    "request_type",
    [
        ad_rule_service.GetAdRuleRequest,
        dict,
    ],
)
def test_get_ad_rule_rest_call_success(request_type):
    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "networks/sample1/adRules/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = ad_rule_messages.AdRule(
            name="name_value",
            display_name="display_name_value",
            priority=898,
            end_time_unlimited=True,
            status=ad_rule_enums.AdRuleStatusEnum.AdRuleStatus.ACTIVE,
            frequency_cap_behavior=ad_rule_enums.AdRuleFrequencyCapBehaviorEnum.AdRuleFrequencyCapBehavior.DEFER,
            max_impressions_per_line_item_per_stream=4269,
            max_impressions_per_line_item_per_pod=3940,
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = ad_rule_messages.AdRule.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_ad_rule(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, ad_rule_messages.AdRule)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert response.priority == 898
    assert response.end_time_unlimited is True
    assert response.status == ad_rule_enums.AdRuleStatusEnum.AdRuleStatus.ACTIVE
    assert (
        response.frequency_cap_behavior
        == ad_rule_enums.AdRuleFrequencyCapBehaviorEnum.AdRuleFrequencyCapBehavior.DEFER
    )
    assert response.max_impressions_per_line_item_per_stream == 4269
    assert response.max_impressions_per_line_item_per_pod == 3940


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_ad_rule_rest_interceptors(null_interceptor):
    transport = transports.AdRuleServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.AdRuleServiceRestInterceptor(),
    )
    client = AdRuleServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.AdRuleServiceRestInterceptor, "post_get_ad_rule"
        ) as post,
        mock.patch.object(
            transports.AdRuleServiceRestInterceptor, "post_get_ad_rule_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.AdRuleServiceRestInterceptor, "pre_get_ad_rule"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = ad_rule_service.GetAdRuleRequest.pb(
            ad_rule_service.GetAdRuleRequest()
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
        return_value = ad_rule_messages.AdRule.to_json(ad_rule_messages.AdRule())
        req.return_value.content = return_value

        request = ad_rule_service.GetAdRuleRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = ad_rule_messages.AdRule()
        post_with_metadata.return_value = ad_rule_messages.AdRule(), metadata

        client.get_ad_rule(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_ad_rules_rest_bad_request(
    request_type=ad_rule_service.ListAdRulesRequest,
):
    client = AdRuleServiceClient(
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
        client.list_ad_rules(request)


@pytest.mark.parametrize(
    "request_type",
    [
        ad_rule_service.ListAdRulesRequest,
        dict,
    ],
)
def test_list_ad_rules_rest_call_success(request_type):
    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = ad_rule_service.ListAdRulesResponse(
            next_page_token="next_page_token_value",
            total_size=1086,
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = ad_rule_service.ListAdRulesResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_ad_rules(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListAdRulesPager)
    assert response.next_page_token == "next_page_token_value"
    assert response.total_size == 1086


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_ad_rules_rest_interceptors(null_interceptor):
    transport = transports.AdRuleServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.AdRuleServiceRestInterceptor(),
    )
    client = AdRuleServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.AdRuleServiceRestInterceptor, "post_list_ad_rules"
        ) as post,
        mock.patch.object(
            transports.AdRuleServiceRestInterceptor, "post_list_ad_rules_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.AdRuleServiceRestInterceptor, "pre_list_ad_rules"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = ad_rule_service.ListAdRulesRequest.pb(
            ad_rule_service.ListAdRulesRequest()
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
        return_value = ad_rule_service.ListAdRulesResponse.to_json(
            ad_rule_service.ListAdRulesResponse()
        )
        req.return_value.content = return_value

        request = ad_rule_service.ListAdRulesRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = ad_rule_service.ListAdRulesResponse()
        post_with_metadata.return_value = (
            ad_rule_service.ListAdRulesResponse(),
            metadata,
        )

        client.list_ad_rules(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_create_ad_rule_rest_bad_request(
    request_type=ad_rule_service.CreateAdRuleRequest,
):
    client = AdRuleServiceClient(
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
        client.create_ad_rule(request)


@pytest.mark.parametrize(
    "request_type",
    [
        ad_rule_service.CreateAdRuleRequest,
        dict,
    ],
)
def test_create_ad_rule_rest_call_success(request_type):
    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request_init["ad_rule"] = {
        "name": "name_value",
        "display_name": "display_name_value",
        "priority": 898,
        "start_time": {"seconds": 751, "nanos": 543},
        "end_time": {},
        "end_time_unlimited": True,
        "status": 1,
        "frequency_cap_behavior": 1,
        "max_impressions_per_line_item_per_stream": 4269,
        "max_impressions_per_line_item_per_pod": 3940,
        "preroll": {
            "slot_behavior": 1,
            "max_video_ad_duration": {"seconds": 751, "nanos": 543},
            "video_midroll_frequency_type": 1,
            "video_midroll_frequency": "video_midroll_frequency_value",
            "bumper": 1,
            "max_bumper_duration": {},
            "max_pod_duration": {},
            "pod_max_ad_count": 1684,
        },
        "midrolls": {},
        "postroll": {},
        "targeting": {
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
            "video_position_targeting": {
                "video_positions": [
                    {
                        "midroll_index": 1386,
                        "reverse_midroll_index": 2245,
                        "pod_position": 1303,
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
        },
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = ad_rule_service.CreateAdRuleRequest.meta.fields["ad_rule"]

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
    for field, value in request_init["ad_rule"].items():  # pragma: NO COVER
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
                for i in range(0, len(request_init["ad_rule"][field])):
                    del request_init["ad_rule"][field][i][subfield]
            else:
                del request_init["ad_rule"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = ad_rule_messages.AdRule(
            name="name_value",
            display_name="display_name_value",
            priority=898,
            end_time_unlimited=True,
            status=ad_rule_enums.AdRuleStatusEnum.AdRuleStatus.ACTIVE,
            frequency_cap_behavior=ad_rule_enums.AdRuleFrequencyCapBehaviorEnum.AdRuleFrequencyCapBehavior.DEFER,
            max_impressions_per_line_item_per_stream=4269,
            max_impressions_per_line_item_per_pod=3940,
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = ad_rule_messages.AdRule.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.create_ad_rule(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, ad_rule_messages.AdRule)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert response.priority == 898
    assert response.end_time_unlimited is True
    assert response.status == ad_rule_enums.AdRuleStatusEnum.AdRuleStatus.ACTIVE
    assert (
        response.frequency_cap_behavior
        == ad_rule_enums.AdRuleFrequencyCapBehaviorEnum.AdRuleFrequencyCapBehavior.DEFER
    )
    assert response.max_impressions_per_line_item_per_stream == 4269
    assert response.max_impressions_per_line_item_per_pod == 3940


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_create_ad_rule_rest_interceptors(null_interceptor):
    transport = transports.AdRuleServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.AdRuleServiceRestInterceptor(),
    )
    client = AdRuleServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.AdRuleServiceRestInterceptor, "post_create_ad_rule"
        ) as post,
        mock.patch.object(
            transports.AdRuleServiceRestInterceptor, "post_create_ad_rule_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.AdRuleServiceRestInterceptor, "pre_create_ad_rule"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = ad_rule_service.CreateAdRuleRequest.pb(
            ad_rule_service.CreateAdRuleRequest()
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
        return_value = ad_rule_messages.AdRule.to_json(ad_rule_messages.AdRule())
        req.return_value.content = return_value

        request = ad_rule_service.CreateAdRuleRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = ad_rule_messages.AdRule()
        post_with_metadata.return_value = ad_rule_messages.AdRule(), metadata

        client.create_ad_rule(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_create_ad_rules_rest_bad_request(
    request_type=ad_rule_service.BatchCreateAdRulesRequest,
):
    client = AdRuleServiceClient(
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
        client.batch_create_ad_rules(request)


@pytest.mark.parametrize(
    "request_type",
    [
        ad_rule_service.BatchCreateAdRulesRequest,
        dict,
    ],
)
def test_batch_create_ad_rules_rest_call_success(request_type):
    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = ad_rule_service.BatchCreateAdRulesResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = ad_rule_service.BatchCreateAdRulesResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.batch_create_ad_rules(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, ad_rule_service.BatchCreateAdRulesResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_create_ad_rules_rest_interceptors(null_interceptor):
    transport = transports.AdRuleServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.AdRuleServiceRestInterceptor(),
    )
    client = AdRuleServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.AdRuleServiceRestInterceptor, "post_batch_create_ad_rules"
        ) as post,
        mock.patch.object(
            transports.AdRuleServiceRestInterceptor,
            "post_batch_create_ad_rules_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.AdRuleServiceRestInterceptor, "pre_batch_create_ad_rules"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = ad_rule_service.BatchCreateAdRulesRequest.pb(
            ad_rule_service.BatchCreateAdRulesRequest()
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
        return_value = ad_rule_service.BatchCreateAdRulesResponse.to_json(
            ad_rule_service.BatchCreateAdRulesResponse()
        )
        req.return_value.content = return_value

        request = ad_rule_service.BatchCreateAdRulesRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = ad_rule_service.BatchCreateAdRulesResponse()
        post_with_metadata.return_value = (
            ad_rule_service.BatchCreateAdRulesResponse(),
            metadata,
        )

        client.batch_create_ad_rules(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_update_ad_rule_rest_bad_request(
    request_type=ad_rule_service.UpdateAdRuleRequest,
):
    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"ad_rule": {"name": "networks/sample1/adRules/sample2"}}
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
        client.update_ad_rule(request)


@pytest.mark.parametrize(
    "request_type",
    [
        ad_rule_service.UpdateAdRuleRequest,
        dict,
    ],
)
def test_update_ad_rule_rest_call_success(request_type):
    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"ad_rule": {"name": "networks/sample1/adRules/sample2"}}
    request_init["ad_rule"] = {
        "name": "networks/sample1/adRules/sample2",
        "display_name": "display_name_value",
        "priority": 898,
        "start_time": {"seconds": 751, "nanos": 543},
        "end_time": {},
        "end_time_unlimited": True,
        "status": 1,
        "frequency_cap_behavior": 1,
        "max_impressions_per_line_item_per_stream": 4269,
        "max_impressions_per_line_item_per_pod": 3940,
        "preroll": {
            "slot_behavior": 1,
            "max_video_ad_duration": {"seconds": 751, "nanos": 543},
            "video_midroll_frequency_type": 1,
            "video_midroll_frequency": "video_midroll_frequency_value",
            "bumper": 1,
            "max_bumper_duration": {},
            "max_pod_duration": {},
            "pod_max_ad_count": 1684,
        },
        "midrolls": {},
        "postroll": {},
        "targeting": {
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
            "video_position_targeting": {
                "video_positions": [
                    {
                        "midroll_index": 1386,
                        "reverse_midroll_index": 2245,
                        "pod_position": 1303,
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
        },
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = ad_rule_service.UpdateAdRuleRequest.meta.fields["ad_rule"]

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
    for field, value in request_init["ad_rule"].items():  # pragma: NO COVER
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
                for i in range(0, len(request_init["ad_rule"][field])):
                    del request_init["ad_rule"][field][i][subfield]
            else:
                del request_init["ad_rule"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = ad_rule_messages.AdRule(
            name="name_value",
            display_name="display_name_value",
            priority=898,
            end_time_unlimited=True,
            status=ad_rule_enums.AdRuleStatusEnum.AdRuleStatus.ACTIVE,
            frequency_cap_behavior=ad_rule_enums.AdRuleFrequencyCapBehaviorEnum.AdRuleFrequencyCapBehavior.DEFER,
            max_impressions_per_line_item_per_stream=4269,
            max_impressions_per_line_item_per_pod=3940,
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = ad_rule_messages.AdRule.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.update_ad_rule(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, ad_rule_messages.AdRule)
    assert response.name == "name_value"
    assert response.display_name == "display_name_value"
    assert response.priority == 898
    assert response.end_time_unlimited is True
    assert response.status == ad_rule_enums.AdRuleStatusEnum.AdRuleStatus.ACTIVE
    assert (
        response.frequency_cap_behavior
        == ad_rule_enums.AdRuleFrequencyCapBehaviorEnum.AdRuleFrequencyCapBehavior.DEFER
    )
    assert response.max_impressions_per_line_item_per_stream == 4269
    assert response.max_impressions_per_line_item_per_pod == 3940


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_update_ad_rule_rest_interceptors(null_interceptor):
    transport = transports.AdRuleServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.AdRuleServiceRestInterceptor(),
    )
    client = AdRuleServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.AdRuleServiceRestInterceptor, "post_update_ad_rule"
        ) as post,
        mock.patch.object(
            transports.AdRuleServiceRestInterceptor, "post_update_ad_rule_with_metadata"
        ) as post_with_metadata,
        mock.patch.object(
            transports.AdRuleServiceRestInterceptor, "pre_update_ad_rule"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = ad_rule_service.UpdateAdRuleRequest.pb(
            ad_rule_service.UpdateAdRuleRequest()
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
        return_value = ad_rule_messages.AdRule.to_json(ad_rule_messages.AdRule())
        req.return_value.content = return_value

        request = ad_rule_service.UpdateAdRuleRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = ad_rule_messages.AdRule()
        post_with_metadata.return_value = ad_rule_messages.AdRule(), metadata

        client.update_ad_rule(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_update_ad_rules_rest_bad_request(
    request_type=ad_rule_service.BatchUpdateAdRulesRequest,
):
    client = AdRuleServiceClient(
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
        client.batch_update_ad_rules(request)


@pytest.mark.parametrize(
    "request_type",
    [
        ad_rule_service.BatchUpdateAdRulesRequest,
        dict,
    ],
)
def test_batch_update_ad_rules_rest_call_success(request_type):
    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = ad_rule_service.BatchUpdateAdRulesResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = ad_rule_service.BatchUpdateAdRulesResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.batch_update_ad_rules(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, ad_rule_service.BatchUpdateAdRulesResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_update_ad_rules_rest_interceptors(null_interceptor):
    transport = transports.AdRuleServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.AdRuleServiceRestInterceptor(),
    )
    client = AdRuleServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.AdRuleServiceRestInterceptor, "post_batch_update_ad_rules"
        ) as post,
        mock.patch.object(
            transports.AdRuleServiceRestInterceptor,
            "post_batch_update_ad_rules_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.AdRuleServiceRestInterceptor, "pre_batch_update_ad_rules"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = ad_rule_service.BatchUpdateAdRulesRequest.pb(
            ad_rule_service.BatchUpdateAdRulesRequest()
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
        return_value = ad_rule_service.BatchUpdateAdRulesResponse.to_json(
            ad_rule_service.BatchUpdateAdRulesResponse()
        )
        req.return_value.content = return_value

        request = ad_rule_service.BatchUpdateAdRulesRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = ad_rule_service.BatchUpdateAdRulesResponse()
        post_with_metadata.return_value = (
            ad_rule_service.BatchUpdateAdRulesResponse(),
            metadata,
        )

        client.batch_update_ad_rules(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_activate_ad_rules_rest_bad_request(
    request_type=ad_rule_service.BatchActivateAdRulesRequest,
):
    client = AdRuleServiceClient(
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
        client.batch_activate_ad_rules(request)


@pytest.mark.parametrize(
    "request_type",
    [
        ad_rule_service.BatchActivateAdRulesRequest,
        dict,
    ],
)
def test_batch_activate_ad_rules_rest_call_success(request_type):
    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = ad_rule_service.BatchActivateAdRulesResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = ad_rule_service.BatchActivateAdRulesResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.batch_activate_ad_rules(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, ad_rule_service.BatchActivateAdRulesResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_activate_ad_rules_rest_interceptors(null_interceptor):
    transport = transports.AdRuleServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.AdRuleServiceRestInterceptor(),
    )
    client = AdRuleServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.AdRuleServiceRestInterceptor, "post_batch_activate_ad_rules"
        ) as post,
        mock.patch.object(
            transports.AdRuleServiceRestInterceptor,
            "post_batch_activate_ad_rules_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.AdRuleServiceRestInterceptor, "pre_batch_activate_ad_rules"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = ad_rule_service.BatchActivateAdRulesRequest.pb(
            ad_rule_service.BatchActivateAdRulesRequest()
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
        return_value = ad_rule_service.BatchActivateAdRulesResponse.to_json(
            ad_rule_service.BatchActivateAdRulesResponse()
        )
        req.return_value.content = return_value

        request = ad_rule_service.BatchActivateAdRulesRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = ad_rule_service.BatchActivateAdRulesResponse()
        post_with_metadata.return_value = (
            ad_rule_service.BatchActivateAdRulesResponse(),
            metadata,
        )

        client.batch_activate_ad_rules(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_deactivate_ad_rules_rest_bad_request(
    request_type=ad_rule_service.BatchDeactivateAdRulesRequest,
):
    client = AdRuleServiceClient(
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
        client.batch_deactivate_ad_rules(request)


@pytest.mark.parametrize(
    "request_type",
    [
        ad_rule_service.BatchDeactivateAdRulesRequest,
        dict,
    ],
)
def test_batch_deactivate_ad_rules_rest_call_success(request_type):
    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = ad_rule_service.BatchDeactivateAdRulesResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = ad_rule_service.BatchDeactivateAdRulesResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.batch_deactivate_ad_rules(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, ad_rule_service.BatchDeactivateAdRulesResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_deactivate_ad_rules_rest_interceptors(null_interceptor):
    transport = transports.AdRuleServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.AdRuleServiceRestInterceptor(),
    )
    client = AdRuleServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.AdRuleServiceRestInterceptor, "post_batch_deactivate_ad_rules"
        ) as post,
        mock.patch.object(
            transports.AdRuleServiceRestInterceptor,
            "post_batch_deactivate_ad_rules_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.AdRuleServiceRestInterceptor, "pre_batch_deactivate_ad_rules"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = ad_rule_service.BatchDeactivateAdRulesRequest.pb(
            ad_rule_service.BatchDeactivateAdRulesRequest()
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
        return_value = ad_rule_service.BatchDeactivateAdRulesResponse.to_json(
            ad_rule_service.BatchDeactivateAdRulesResponse()
        )
        req.return_value.content = return_value

        request = ad_rule_service.BatchDeactivateAdRulesRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = ad_rule_service.BatchDeactivateAdRulesResponse()
        post_with_metadata.return_value = (
            ad_rule_service.BatchDeactivateAdRulesResponse(),
            metadata,
        )

        client.batch_deactivate_ad_rules(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_delete_ad_rules_rest_bad_request(
    request_type=ad_rule_service.BatchDeleteAdRulesRequest,
):
    client = AdRuleServiceClient(
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
        client.batch_delete_ad_rules(request)


@pytest.mark.parametrize(
    "request_type",
    [
        ad_rule_service.BatchDeleteAdRulesRequest,
        dict,
    ],
)
def test_batch_delete_ad_rules_rest_call_success(request_type):
    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = None

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200
        json_return_value = ""
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.batch_delete_ad_rules(request)

    # Establish that the response is the type that we expect.
    assert response is None


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_delete_ad_rules_rest_interceptors(null_interceptor):
    transport = transports.AdRuleServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.AdRuleServiceRestInterceptor(),
    )
    client = AdRuleServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.AdRuleServiceRestInterceptor, "pre_batch_delete_ad_rules"
        ) as pre,
    ):
        pre.assert_not_called()
        pb_message = ad_rule_service.BatchDeleteAdRulesRequest.pb(
            ad_rule_service.BatchDeleteAdRulesRequest()
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

        request = ad_rule_service.BatchDeleteAdRulesRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata

        client.batch_delete_ad_rules(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()


def test_cancel_operation_rest_bad_request(
    request_type=operations_pb2.CancelOperationRequest,
):
    client = AdRuleServiceClient(
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
    client = AdRuleServiceClient(
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
    client = AdRuleServiceClient(
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
    client = AdRuleServiceClient(
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
    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_ad_rule_empty_call_rest():
    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_ad_rule), "__call__") as call:
        client.get_ad_rule(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = ad_rule_service.GetAdRuleRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_ad_rules_empty_call_rest():
    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_ad_rules), "__call__") as call:
        client.list_ad_rules(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = ad_rule_service.ListAdRulesRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_ad_rule_empty_call_rest():
    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.create_ad_rule), "__call__") as call:
        client.create_ad_rule(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = ad_rule_service.CreateAdRuleRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_create_ad_rules_empty_call_rest():
    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_create_ad_rules), "__call__"
    ) as call:
        client.batch_create_ad_rules(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = ad_rule_service.BatchCreateAdRulesRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_ad_rule_empty_call_rest():
    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.update_ad_rule), "__call__") as call:
        client.update_ad_rule(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = ad_rule_service.UpdateAdRuleRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_update_ad_rules_empty_call_rest():
    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_update_ad_rules), "__call__"
    ) as call:
        client.batch_update_ad_rules(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = ad_rule_service.BatchUpdateAdRulesRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_activate_ad_rules_empty_call_rest():
    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_activate_ad_rules), "__call__"
    ) as call:
        client.batch_activate_ad_rules(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = ad_rule_service.BatchActivateAdRulesRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_deactivate_ad_rules_empty_call_rest():
    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_deactivate_ad_rules), "__call__"
    ) as call:
        client.batch_deactivate_ad_rules(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = ad_rule_service.BatchDeactivateAdRulesRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_delete_ad_rules_empty_call_rest():
    client = AdRuleServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_delete_ad_rules), "__call__"
    ) as call:
        client.batch_delete_ad_rules(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = ad_rule_service.BatchDeleteAdRulesRequest()
        assert args[0] == request_msg


def test_ad_rule_service_base_transport_error():
    # Passing both a credentials object and credentials_file should raise an error
    with pytest.raises(core_exceptions.DuplicateCredentialArgs):
        transport = transports.AdRuleServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            credentials_file="credentials.json",
        )


def test_ad_rule_service_base_transport():
    # Instantiate the base transport.
    with mock.patch(
        "google.ads.admanager_v1.services.ad_rule_service.transports.AdRuleServiceTransport.__init__"
    ) as Transport:
        Transport.return_value = None
        transport = transports.AdRuleServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        "get_ad_rule",
        "list_ad_rules",
        "create_ad_rule",
        "batch_create_ad_rules",
        "update_ad_rule",
        "batch_update_ad_rules",
        "batch_activate_ad_rules",
        "batch_deactivate_ad_rules",
        "batch_delete_ad_rules",
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


def test_ad_rule_service_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with (
        mock.patch.object(
            google.auth, "load_credentials_from_file", autospec=True
        ) as load_creds,
        mock.patch(
            "google.ads.admanager_v1.services.ad_rule_service.transports.AdRuleServiceTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        load_creds.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.AdRuleServiceTransport(
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


def test_ad_rule_service_base_transport_with_adc():
    # Test the default credentials are used if credentials and credentials_file are None.
    with (
        mock.patch.object(google.auth, "default", autospec=True) as adc,
        mock.patch(
            "google.ads.admanager_v1.services.ad_rule_service.transports.AdRuleServiceTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.AdRuleServiceTransport()
        adc.assert_called_once()


def test_ad_rule_service_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        AdRuleServiceClient()
        adc.assert_called_once_with(
            scopes=None,
            default_scopes=(
                "https://www.googleapis.com/auth/admanager",
                "https://www.googleapis.com/auth/admanager.readonly",
            ),
            quota_project_id=None,
        )


def test_ad_rule_service_http_transport_client_cert_source_for_mtls():
    cred = ga_credentials.AnonymousCredentials()
    with mock.patch(
        "google.auth.transport.requests.AuthorizedSession.configure_mtls_channel"
    ) as mock_configure_mtls_channel:
        transports.AdRuleServiceRestTransport(
            credentials=cred, client_cert_source_for_mtls=client_cert_source_callback
        )
        mock_configure_mtls_channel.assert_called_once_with(client_cert_source_callback)


@pytest.mark.parametrize(
    "transport_name",
    [
        "rest",
    ],
)
def test_ad_rule_service_host_no_port(transport_name):
    client = AdRuleServiceClient(
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
def test_ad_rule_service_host_with_port(transport_name):
    client = AdRuleServiceClient(
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
def test_ad_rule_service_client_transport_session_collision(transport_name):
    creds1 = ga_credentials.AnonymousCredentials()
    creds2 = ga_credentials.AnonymousCredentials()
    client1 = AdRuleServiceClient(
        credentials=creds1,
        transport=transport_name,
    )
    client2 = AdRuleServiceClient(
        credentials=creds2,
        transport=transport_name,
    )
    session1 = client1.transport.get_ad_rule._session
    session2 = client2.transport.get_ad_rule._session
    assert session1 != session2
    session1 = client1.transport.list_ad_rules._session
    session2 = client2.transport.list_ad_rules._session
    assert session1 != session2
    session1 = client1.transport.create_ad_rule._session
    session2 = client2.transport.create_ad_rule._session
    assert session1 != session2
    session1 = client1.transport.batch_create_ad_rules._session
    session2 = client2.transport.batch_create_ad_rules._session
    assert session1 != session2
    session1 = client1.transport.update_ad_rule._session
    session2 = client2.transport.update_ad_rule._session
    assert session1 != session2
    session1 = client1.transport.batch_update_ad_rules._session
    session2 = client2.transport.batch_update_ad_rules._session
    assert session1 != session2
    session1 = client1.transport.batch_activate_ad_rules._session
    session2 = client2.transport.batch_activate_ad_rules._session
    assert session1 != session2
    session1 = client1.transport.batch_deactivate_ad_rules._session
    session2 = client2.transport.batch_deactivate_ad_rules._session
    assert session1 != session2
    session1 = client1.transport.batch_delete_ad_rules._session
    session2 = client2.transport.batch_delete_ad_rules._session
    assert session1 != session2


def test_ad_rule_path():
    network_code = "squid"
    ad_rule = "clam"
    expected = "networks/{network_code}/adRules/{ad_rule}".format(
        network_code=network_code,
        ad_rule=ad_rule,
    )
    actual = AdRuleServiceClient.ad_rule_path(network_code, ad_rule)
    assert expected == actual


def test_parse_ad_rule_path():
    expected = {
        "network_code": "whelk",
        "ad_rule": "octopus",
    }
    path = AdRuleServiceClient.ad_rule_path(**expected)

    # Check that the path construction is reversible.
    actual = AdRuleServiceClient.parse_ad_rule_path(path)
    assert expected == actual


def test_ad_unit_path():
    network_code = "oyster"
    ad_unit = "nudibranch"
    expected = "networks/{network_code}/adUnits/{ad_unit}".format(
        network_code=network_code,
        ad_unit=ad_unit,
    )
    actual = AdRuleServiceClient.ad_unit_path(network_code, ad_unit)
    assert expected == actual


def test_parse_ad_unit_path():
    expected = {
        "network_code": "cuttlefish",
        "ad_unit": "mussel",
    }
    path = AdRuleServiceClient.ad_unit_path(**expected)

    # Check that the path construction is reversible.
    actual = AdRuleServiceClient.parse_ad_unit_path(path)
    assert expected == actual


def test_application_path():
    network_code = "winkle"
    application = "nautilus"
    expected = "networks/{network_code}/applications/{application}".format(
        network_code=network_code,
        application=application,
    )
    actual = AdRuleServiceClient.application_path(network_code, application)
    assert expected == actual


def test_parse_application_path():
    expected = {
        "network_code": "scallop",
        "application": "abalone",
    }
    path = AdRuleServiceClient.application_path(**expected)

    # Check that the path construction is reversible.
    actual = AdRuleServiceClient.parse_application_path(path)
    assert expected == actual


def test_audience_segment_path():
    network_code = "squid"
    audience_segment = "clam"
    expected = "networks/{network_code}/audienceSegments/{audience_segment}".format(
        network_code=network_code,
        audience_segment=audience_segment,
    )
    actual = AdRuleServiceClient.audience_segment_path(network_code, audience_segment)
    assert expected == actual


def test_parse_audience_segment_path():
    expected = {
        "network_code": "whelk",
        "audience_segment": "octopus",
    }
    path = AdRuleServiceClient.audience_segment_path(**expected)

    # Check that the path construction is reversible.
    actual = AdRuleServiceClient.parse_audience_segment_path(path)
    assert expected == actual


def test_bandwidth_group_path():
    network_code = "oyster"
    bandwidth_group = "nudibranch"
    expected = "networks/{network_code}/bandwidthGroups/{bandwidth_group}".format(
        network_code=network_code,
        bandwidth_group=bandwidth_group,
    )
    actual = AdRuleServiceClient.bandwidth_group_path(network_code, bandwidth_group)
    assert expected == actual


def test_parse_bandwidth_group_path():
    expected = {
        "network_code": "cuttlefish",
        "bandwidth_group": "mussel",
    }
    path = AdRuleServiceClient.bandwidth_group_path(**expected)

    # Check that the path construction is reversible.
    actual = AdRuleServiceClient.parse_bandwidth_group_path(path)
    assert expected == actual


def test_browser_path():
    network_code = "winkle"
    browser = "nautilus"
    expected = "networks/{network_code}/browsers/{browser}".format(
        network_code=network_code,
        browser=browser,
    )
    actual = AdRuleServiceClient.browser_path(network_code, browser)
    assert expected == actual


def test_parse_browser_path():
    expected = {
        "network_code": "scallop",
        "browser": "abalone",
    }
    path = AdRuleServiceClient.browser_path(**expected)

    # Check that the path construction is reversible.
    actual = AdRuleServiceClient.parse_browser_path(path)
    assert expected == actual


def test_browser_language_path():
    network_code = "squid"
    browser_language = "clam"
    expected = "networks/{network_code}/browserLanguages/{browser_language}".format(
        network_code=network_code,
        browser_language=browser_language,
    )
    actual = AdRuleServiceClient.browser_language_path(network_code, browser_language)
    assert expected == actual


def test_parse_browser_language_path():
    expected = {
        "network_code": "whelk",
        "browser_language": "octopus",
    }
    path = AdRuleServiceClient.browser_language_path(**expected)

    # Check that the path construction is reversible.
    actual = AdRuleServiceClient.parse_browser_language_path(path)
    assert expected == actual


def test_cms_metadata_value_path():
    network_code = "oyster"
    cms_metadata_value = "nudibranch"
    expected = "networks/{network_code}/cmsMetadataValues/{cms_metadata_value}".format(
        network_code=network_code,
        cms_metadata_value=cms_metadata_value,
    )
    actual = AdRuleServiceClient.cms_metadata_value_path(
        network_code, cms_metadata_value
    )
    assert expected == actual


def test_parse_cms_metadata_value_path():
    expected = {
        "network_code": "cuttlefish",
        "cms_metadata_value": "mussel",
    }
    path = AdRuleServiceClient.cms_metadata_value_path(**expected)

    # Check that the path construction is reversible.
    actual = AdRuleServiceClient.parse_cms_metadata_value_path(path)
    assert expected == actual


def test_content_path():
    network_code = "winkle"
    content = "nautilus"
    expected = "networks/{network_code}/content/{content}".format(
        network_code=network_code,
        content=content,
    )
    actual = AdRuleServiceClient.content_path(network_code, content)
    assert expected == actual


def test_parse_content_path():
    expected = {
        "network_code": "scallop",
        "content": "abalone",
    }
    path = AdRuleServiceClient.content_path(**expected)

    # Check that the path construction is reversible.
    actual = AdRuleServiceClient.parse_content_path(path)
    assert expected == actual


def test_content_bundle_path():
    network_code = "squid"
    content_bundle = "clam"
    expected = "networks/{network_code}/contentBundles/{content_bundle}".format(
        network_code=network_code,
        content_bundle=content_bundle,
    )
    actual = AdRuleServiceClient.content_bundle_path(network_code, content_bundle)
    assert expected == actual


def test_parse_content_bundle_path():
    expected = {
        "network_code": "whelk",
        "content_bundle": "octopus",
    }
    path = AdRuleServiceClient.content_bundle_path(**expected)

    # Check that the path construction is reversible.
    actual = AdRuleServiceClient.parse_content_bundle_path(path)
    assert expected == actual


def test_custom_targeting_key_path():
    network_code = "oyster"
    custom_targeting_key = "nudibranch"
    expected = (
        "networks/{network_code}/customTargetingKeys/{custom_targeting_key}".format(
            network_code=network_code,
            custom_targeting_key=custom_targeting_key,
        )
    )
    actual = AdRuleServiceClient.custom_targeting_key_path(
        network_code, custom_targeting_key
    )
    assert expected == actual


def test_parse_custom_targeting_key_path():
    expected = {
        "network_code": "cuttlefish",
        "custom_targeting_key": "mussel",
    }
    path = AdRuleServiceClient.custom_targeting_key_path(**expected)

    # Check that the path construction is reversible.
    actual = AdRuleServiceClient.parse_custom_targeting_key_path(path)
    assert expected == actual


def test_custom_targeting_value_path():
    network_code = "winkle"
    custom_targeting_value = "nautilus"
    expected = (
        "networks/{network_code}/customTargetingValues/{custom_targeting_value}".format(
            network_code=network_code,
            custom_targeting_value=custom_targeting_value,
        )
    )
    actual = AdRuleServiceClient.custom_targeting_value_path(
        network_code, custom_targeting_value
    )
    assert expected == actual


def test_parse_custom_targeting_value_path():
    expected = {
        "network_code": "scallop",
        "custom_targeting_value": "abalone",
    }
    path = AdRuleServiceClient.custom_targeting_value_path(**expected)

    # Check that the path construction is reversible.
    actual = AdRuleServiceClient.parse_custom_targeting_value_path(path)
    assert expected == actual


def test_device_capability_path():
    network_code = "squid"
    device_capability = "clam"
    expected = "networks/{network_code}/deviceCapabilities/{device_capability}".format(
        network_code=network_code,
        device_capability=device_capability,
    )
    actual = AdRuleServiceClient.device_capability_path(network_code, device_capability)
    assert expected == actual


def test_parse_device_capability_path():
    expected = {
        "network_code": "whelk",
        "device_capability": "octopus",
    }
    path = AdRuleServiceClient.device_capability_path(**expected)

    # Check that the path construction is reversible.
    actual = AdRuleServiceClient.parse_device_capability_path(path)
    assert expected == actual


def test_device_category_path():
    network_code = "oyster"
    device_category = "nudibranch"
    expected = "networks/{network_code}/deviceCategories/{device_category}".format(
        network_code=network_code,
        device_category=device_category,
    )
    actual = AdRuleServiceClient.device_category_path(network_code, device_category)
    assert expected == actual


def test_parse_device_category_path():
    expected = {
        "network_code": "cuttlefish",
        "device_category": "mussel",
    }
    path = AdRuleServiceClient.device_category_path(**expected)

    # Check that the path construction is reversible.
    actual = AdRuleServiceClient.parse_device_category_path(path)
    assert expected == actual


def test_device_manufacturer_path():
    network_code = "winkle"
    device_manufacturer = "nautilus"
    expected = (
        "networks/{network_code}/deviceManufacturers/{device_manufacturer}".format(
            network_code=network_code,
            device_manufacturer=device_manufacturer,
        )
    )
    actual = AdRuleServiceClient.device_manufacturer_path(
        network_code, device_manufacturer
    )
    assert expected == actual


def test_parse_device_manufacturer_path():
    expected = {
        "network_code": "scallop",
        "device_manufacturer": "abalone",
    }
    path = AdRuleServiceClient.device_manufacturer_path(**expected)

    # Check that the path construction is reversible.
    actual = AdRuleServiceClient.parse_device_manufacturer_path(path)
    assert expected == actual


def test_geo_target_path():
    network_code = "squid"
    geo_target = "clam"
    expected = "networks/{network_code}/geoTargets/{geo_target}".format(
        network_code=network_code,
        geo_target=geo_target,
    )
    actual = AdRuleServiceClient.geo_target_path(network_code, geo_target)
    assert expected == actual


def test_parse_geo_target_path():
    expected = {
        "network_code": "whelk",
        "geo_target": "octopus",
    }
    path = AdRuleServiceClient.geo_target_path(**expected)

    # Check that the path construction is reversible.
    actual = AdRuleServiceClient.parse_geo_target_path(path)
    assert expected == actual


def test_mobile_carrier_path():
    network_code = "oyster"
    mobile_carrier = "nudibranch"
    expected = "networks/{network_code}/mobileCarriers/{mobile_carrier}".format(
        network_code=network_code,
        mobile_carrier=mobile_carrier,
    )
    actual = AdRuleServiceClient.mobile_carrier_path(network_code, mobile_carrier)
    assert expected == actual


def test_parse_mobile_carrier_path():
    expected = {
        "network_code": "cuttlefish",
        "mobile_carrier": "mussel",
    }
    path = AdRuleServiceClient.mobile_carrier_path(**expected)

    # Check that the path construction is reversible.
    actual = AdRuleServiceClient.parse_mobile_carrier_path(path)
    assert expected == actual


def test_mobile_device_path():
    network_code = "winkle"
    mobile_device = "nautilus"
    expected = "networks/{network_code}/mobileDevices/{mobile_device}".format(
        network_code=network_code,
        mobile_device=mobile_device,
    )
    actual = AdRuleServiceClient.mobile_device_path(network_code, mobile_device)
    assert expected == actual


def test_parse_mobile_device_path():
    expected = {
        "network_code": "scallop",
        "mobile_device": "abalone",
    }
    path = AdRuleServiceClient.mobile_device_path(**expected)

    # Check that the path construction is reversible.
    actual = AdRuleServiceClient.parse_mobile_device_path(path)
    assert expected == actual


def test_mobile_device_submodel_path():
    network_code = "squid"
    mobile_device_submodel = "clam"
    expected = (
        "networks/{network_code}/mobileDeviceSubmodels/{mobile_device_submodel}".format(
            network_code=network_code,
            mobile_device_submodel=mobile_device_submodel,
        )
    )
    actual = AdRuleServiceClient.mobile_device_submodel_path(
        network_code, mobile_device_submodel
    )
    assert expected == actual


def test_parse_mobile_device_submodel_path():
    expected = {
        "network_code": "whelk",
        "mobile_device_submodel": "octopus",
    }
    path = AdRuleServiceClient.mobile_device_submodel_path(**expected)

    # Check that the path construction is reversible.
    actual = AdRuleServiceClient.parse_mobile_device_submodel_path(path)
    assert expected == actual


def test_network_path():
    network_code = "oyster"
    expected = "networks/{network_code}".format(
        network_code=network_code,
    )
    actual = AdRuleServiceClient.network_path(network_code)
    assert expected == actual


def test_parse_network_path():
    expected = {
        "network_code": "nudibranch",
    }
    path = AdRuleServiceClient.network_path(**expected)

    # Check that the path construction is reversible.
    actual = AdRuleServiceClient.parse_network_path(path)
    assert expected == actual


def test_operating_system_path():
    network_code = "cuttlefish"
    operating_system = "mussel"
    expected = "networks/{network_code}/operatingSystems/{operating_system}".format(
        network_code=network_code,
        operating_system=operating_system,
    )
    actual = AdRuleServiceClient.operating_system_path(network_code, operating_system)
    assert expected == actual


def test_parse_operating_system_path():
    expected = {
        "network_code": "winkle",
        "operating_system": "nautilus",
    }
    path = AdRuleServiceClient.operating_system_path(**expected)

    # Check that the path construction is reversible.
    actual = AdRuleServiceClient.parse_operating_system_path(path)
    assert expected == actual


def test_operating_system_version_path():
    network_code = "scallop"
    operating_system_version = "abalone"
    expected = "networks/{network_code}/operatingSystemVersions/{operating_system_version}".format(
        network_code=network_code,
        operating_system_version=operating_system_version,
    )
    actual = AdRuleServiceClient.operating_system_version_path(
        network_code, operating_system_version
    )
    assert expected == actual


def test_parse_operating_system_version_path():
    expected = {
        "network_code": "squid",
        "operating_system_version": "clam",
    }
    path = AdRuleServiceClient.operating_system_version_path(**expected)

    # Check that the path construction is reversible.
    actual = AdRuleServiceClient.parse_operating_system_version_path(path)
    assert expected == actual


def test_placement_path():
    network_code = "whelk"
    placement = "octopus"
    expected = "networks/{network_code}/placements/{placement}".format(
        network_code=network_code,
        placement=placement,
    )
    actual = AdRuleServiceClient.placement_path(network_code, placement)
    assert expected == actual


def test_parse_placement_path():
    expected = {
        "network_code": "oyster",
        "placement": "nudibranch",
    }
    path = AdRuleServiceClient.placement_path(**expected)

    # Check that the path construction is reversible.
    actual = AdRuleServiceClient.parse_placement_path(path)
    assert expected == actual


def test_common_billing_account_path():
    billing_account = "cuttlefish"
    expected = "billingAccounts/{billing_account}".format(
        billing_account=billing_account,
    )
    actual = AdRuleServiceClient.common_billing_account_path(billing_account)
    assert expected == actual


def test_parse_common_billing_account_path():
    expected = {
        "billing_account": "mussel",
    }
    path = AdRuleServiceClient.common_billing_account_path(**expected)

    # Check that the path construction is reversible.
    actual = AdRuleServiceClient.parse_common_billing_account_path(path)
    assert expected == actual


def test_common_folder_path():
    folder = "winkle"
    expected = "folders/{folder}".format(
        folder=folder,
    )
    actual = AdRuleServiceClient.common_folder_path(folder)
    assert expected == actual


def test_parse_common_folder_path():
    expected = {
        "folder": "nautilus",
    }
    path = AdRuleServiceClient.common_folder_path(**expected)

    # Check that the path construction is reversible.
    actual = AdRuleServiceClient.parse_common_folder_path(path)
    assert expected == actual


def test_common_organization_path():
    organization = "scallop"
    expected = "organizations/{organization}".format(
        organization=organization,
    )
    actual = AdRuleServiceClient.common_organization_path(organization)
    assert expected == actual


def test_parse_common_organization_path():
    expected = {
        "organization": "abalone",
    }
    path = AdRuleServiceClient.common_organization_path(**expected)

    # Check that the path construction is reversible.
    actual = AdRuleServiceClient.parse_common_organization_path(path)
    assert expected == actual


def test_common_project_path():
    project = "squid"
    expected = "projects/{project}".format(
        project=project,
    )
    actual = AdRuleServiceClient.common_project_path(project)
    assert expected == actual


def test_parse_common_project_path():
    expected = {
        "project": "clam",
    }
    path = AdRuleServiceClient.common_project_path(**expected)

    # Check that the path construction is reversible.
    actual = AdRuleServiceClient.parse_common_project_path(path)
    assert expected == actual


def test_common_location_path():
    project = "whelk"
    location = "octopus"
    expected = "projects/{project}/locations/{location}".format(
        project=project,
        location=location,
    )
    actual = AdRuleServiceClient.common_location_path(project, location)
    assert expected == actual


def test_parse_common_location_path():
    expected = {
        "project": "oyster",
        "location": "nudibranch",
    }
    path = AdRuleServiceClient.common_location_path(**expected)

    # Check that the path construction is reversible.
    actual = AdRuleServiceClient.parse_common_location_path(path)
    assert expected == actual


def test_client_with_default_client_info():
    client_info = gapic_v1.client_info.ClientInfo()

    with mock.patch.object(
        transports.AdRuleServiceTransport, "_prep_wrapped_messages"
    ) as prep:
        client = AdRuleServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

    with mock.patch.object(
        transports.AdRuleServiceTransport, "_prep_wrapped_messages"
    ) as prep:
        transport_class = AdRuleServiceClient.get_transport_class()
        transport = transport_class(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)


def test_transport_close_rest():
    client = AdRuleServiceClient(
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
        client = AdRuleServiceClient(
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
        (AdRuleServiceClient, transports.AdRuleServiceRestTransport),
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
