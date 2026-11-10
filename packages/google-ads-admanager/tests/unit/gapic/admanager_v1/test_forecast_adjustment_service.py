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
import google.type.date_pb2 as date_pb2  # type: ignore
import google.type.dayofweek_pb2 as dayofweek_pb2  # type: ignore
import google.type.interval_pb2 as interval_pb2  # type: ignore
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

from google.ads.admanager_v1.services.forecast_adjustment_service import (
    ForecastAdjustmentServiceClient,
    pagers,
    transports,
)
from google.ads.admanager_v1.types import (
    date_range,
    dayparting_time_zone_enum,
    forecast_adjustment_enums,
    forecast_adjustment_messages,
    forecast_adjustment_service,
    request_platform_enum,
    size,
    size_type_enum,
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

    assert ForecastAdjustmentServiceClient._get_client_cert_source(None, False) is None
    assert (
        ForecastAdjustmentServiceClient._get_client_cert_source(
            mock_provided_cert_source, False
        )
        is None
    )
    assert (
        ForecastAdjustmentServiceClient._get_client_cert_source(
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
                ForecastAdjustmentServiceClient._get_client_cert_source(None, True)
                is mock_default_cert_source
            )
            assert (
                ForecastAdjustmentServiceClient._get_client_cert_source(
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
    client = ForecastAdjustmentServiceClient(credentials=cred)
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
    client = ForecastAdjustmentServiceClient(credentials=cred)
    client._transport._credentials = cred

    error = core_exceptions.GoogleAPICallError("message", details=[])
    error.code = error_code

    client._add_cred_info_for_auth_errors(error)
    assert error.details == []


@pytest.mark.parametrize(
    "client_class,transport_name",
    [
        (ForecastAdjustmentServiceClient, "rest"),
    ],
)
def test_forecast_adjustment_service_client_from_service_account_info(
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
        (transports.ForecastAdjustmentServiceRestTransport, "rest"),
    ],
)
def test_forecast_adjustment_service_client_service_account_always_use_jwt(
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
        (ForecastAdjustmentServiceClient, "rest"),
    ],
)
def test_forecast_adjustment_service_client_from_service_account_file(
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


def test_forecast_adjustment_service_client_get_transport_class():
    transport = ForecastAdjustmentServiceClient.get_transport_class()
    available_transports = [
        transports.ForecastAdjustmentServiceRestTransport,
    ]
    assert transport in available_transports

    transport = ForecastAdjustmentServiceClient.get_transport_class("rest")
    assert transport == transports.ForecastAdjustmentServiceRestTransport


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (
            ForecastAdjustmentServiceClient,
            transports.ForecastAdjustmentServiceRestTransport,
            "rest",
        ),
    ],
)
@mock.patch.object(
    ForecastAdjustmentServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(ForecastAdjustmentServiceClient),
)
def test_forecast_adjustment_service_client_client_options(
    client_class, transport_class, transport_name
):
    # Check that if channel is provided we won't create a new one.
    with mock.patch.object(
        ForecastAdjustmentServiceClient, "get_transport_class"
    ) as gtc:
        transport = transport_class(credentials=ga_credentials.AnonymousCredentials())
        client = client_class(transport=transport)
        gtc.assert_not_called()

    # Check that if channel is provided via str we will create a new one.
    with mock.patch.object(
        ForecastAdjustmentServiceClient, "get_transport_class"
    ) as gtc:
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
            ForecastAdjustmentServiceClient,
            transports.ForecastAdjustmentServiceRestTransport,
            "rest",
            "true",
        ),
        (
            ForecastAdjustmentServiceClient,
            transports.ForecastAdjustmentServiceRestTransport,
            "rest",
            "false",
        ),
    ],
)
@mock.patch.object(
    ForecastAdjustmentServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(ForecastAdjustmentServiceClient),
)
@mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "auto"})
def test_forecast_adjustment_service_client_mtls_env_auto(
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


@pytest.mark.parametrize("client_class", [ForecastAdjustmentServiceClient])
@mock.patch.object(
    ForecastAdjustmentServiceClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(ForecastAdjustmentServiceClient),
)
def test_forecast_adjustment_service_client_get_mtls_endpoint_and_cert_source(
    client_class,
):
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


@pytest.mark.parametrize("client_class", [ForecastAdjustmentServiceClient])
@mock.patch.object(
    ForecastAdjustmentServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(ForecastAdjustmentServiceClient),
)
def test_forecast_adjustment_service_client_client_api_endpoint(client_class):
    mock_client_cert_source = client_cert_source_callback
    api_override = "foo.com"
    default_universe = ForecastAdjustmentServiceClient._DEFAULT_UNIVERSE
    default_endpoint = (
        ForecastAdjustmentServiceClient._DEFAULT_ENDPOINT_TEMPLATE.format(
            UNIVERSE_DOMAIN=default_universe
        )
    )
    mock_universe = "bar.com"
    mock_endpoint = ForecastAdjustmentServiceClient._DEFAULT_ENDPOINT_TEMPLATE.format(
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
            ForecastAdjustmentServiceClient,
            transports.ForecastAdjustmentServiceRestTransport,
            "rest",
        ),
    ],
)
def test_forecast_adjustment_service_client_client_options_scopes(
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
            ForecastAdjustmentServiceClient,
            transports.ForecastAdjustmentServiceRestTransport,
            "rest",
            None,
        ),
    ],
)
def test_forecast_adjustment_service_client_client_options_credentials_file(
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


def test_get_forecast_adjustment_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = ForecastAdjustmentServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.get_forecast_adjustment
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.get_forecast_adjustment
        ] = mock_rpc

        request = {}
        client.get_forecast_adjustment(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_forecast_adjustment(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_forecast_adjustment_rest_required_fields(
    request_type=forecast_adjustment_service.GetForecastAdjustmentRequest,
):
    transport_class = transports.ForecastAdjustmentServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGetForecastAdjustment,
        "_BaseGetForecastAdjustment__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = forecast_adjustment_messages.ForecastAdjustment()
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
            return_value = forecast_adjustment_messages.ForecastAdjustment.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get_forecast_adjustment(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_forecast_adjustment_rest_flattened():
    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = forecast_adjustment_messages.ForecastAdjustment()

        # get arguments that satisfy an http rule for this method
        sample_request = {"name": "networks/sample1/forecastAdjustments/sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = forecast_adjustment_messages.ForecastAdjustment.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get_forecast_adjustment(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{name=networks/*/forecastAdjustments/*}" % client.transport._host,
            args[1],
        )


def test_get_forecast_adjustment_rest_flattened_error(transport: str = "rest"):
    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_forecast_adjustment(
            forecast_adjustment_service.GetForecastAdjustmentRequest(),
            name="name_value",
        )


def test_list_forecast_adjustments_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = ForecastAdjustmentServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.list_forecast_adjustments
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.list_forecast_adjustments
        ] = mock_rpc

        request = {}
        client.list_forecast_adjustments(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_forecast_adjustments(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_forecast_adjustments_rest_required_fields(
    request_type=forecast_adjustment_service.ListForecastAdjustmentsRequest,
):
    transport_class = transports.ForecastAdjustmentServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseListForecastAdjustments,
        "_BaseListForecastAdjustments__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = forecast_adjustment_service.ListForecastAdjustmentsResponse()
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
            return_value = (
                forecast_adjustment_service.ListForecastAdjustmentsResponse.pb(
                    return_value
                )
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_forecast_adjustments(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_forecast_adjustments_rest_flattened():
    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = forecast_adjustment_service.ListForecastAdjustmentsResponse()

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
        return_value = forecast_adjustment_service.ListForecastAdjustmentsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_forecast_adjustments(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/forecastAdjustments" % client.transport._host,
            args[1],
        )


def test_list_forecast_adjustments_rest_flattened_error(transport: str = "rest"):
    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_forecast_adjustments(
            forecast_adjustment_service.ListForecastAdjustmentsRequest(),
            parent="parent_value",
        )


def test_list_forecast_adjustments_rest_pager(transport: str = "rest"):
    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            forecast_adjustment_service.ListForecastAdjustmentsResponse(
                forecast_adjustments=[
                    forecast_adjustment_messages.ForecastAdjustment(),
                    forecast_adjustment_messages.ForecastAdjustment(),
                    forecast_adjustment_messages.ForecastAdjustment(),
                ],
                next_page_token="abc",
            ),
            forecast_adjustment_service.ListForecastAdjustmentsResponse(
                forecast_adjustments=[],
                next_page_token="def",
            ),
            forecast_adjustment_service.ListForecastAdjustmentsResponse(
                forecast_adjustments=[
                    forecast_adjustment_messages.ForecastAdjustment(),
                ],
                next_page_token="ghi",
            ),
            forecast_adjustment_service.ListForecastAdjustmentsResponse(
                forecast_adjustments=[
                    forecast_adjustment_messages.ForecastAdjustment(),
                    forecast_adjustment_messages.ForecastAdjustment(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            forecast_adjustment_service.ListForecastAdjustmentsResponse.to_json(x)
            for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {"parent": "networks/sample1"}

        pager = client.list_forecast_adjustments(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(
            isinstance(i, forecast_adjustment_messages.ForecastAdjustment)
            for i in results
        )

        pages = list(client.list_forecast_adjustments(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_create_forecast_adjustment_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = ForecastAdjustmentServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.create_forecast_adjustment
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.create_forecast_adjustment
        ] = mock_rpc

        request = {}
        client.create_forecast_adjustment(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.create_forecast_adjustment(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_create_forecast_adjustment_rest_required_fields(
    request_type=forecast_adjustment_service.CreateForecastAdjustmentRequest,
):
    transport_class = transports.ForecastAdjustmentServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseCreateForecastAdjustment,
        "_BaseCreateForecastAdjustment__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = forecast_adjustment_messages.ForecastAdjustment()
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
            return_value = forecast_adjustment_messages.ForecastAdjustment.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.create_forecast_adjustment(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_create_forecast_adjustment_rest_flattened():
    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = forecast_adjustment_messages.ForecastAdjustment()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "networks/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            forecast_adjustment=forecast_adjustment_messages.ForecastAdjustment(
                daily_volume_settings=forecast_adjustment_messages.DailyVolumeSettings(
                    ad_opportunity_counts=[2300]
                )
            ),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = forecast_adjustment_messages.ForecastAdjustment.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.create_forecast_adjustment(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/forecastAdjustments" % client.transport._host,
            args[1],
        )


def test_create_forecast_adjustment_rest_flattened_error(transport: str = "rest"):
    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_forecast_adjustment(
            forecast_adjustment_service.CreateForecastAdjustmentRequest(),
            parent="parent_value",
            forecast_adjustment=forecast_adjustment_messages.ForecastAdjustment(
                daily_volume_settings=forecast_adjustment_messages.DailyVolumeSettings(
                    ad_opportunity_counts=[2300]
                )
            ),
        )


def test_batch_create_forecast_adjustments_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = ForecastAdjustmentServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_create_forecast_adjustments
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.batch_create_forecast_adjustments
        ] = mock_rpc

        request = {}
        client.batch_create_forecast_adjustments(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_create_forecast_adjustments(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_create_forecast_adjustments_rest_required_fields(
    request_type=forecast_adjustment_service.BatchCreateForecastAdjustmentsRequest,
):
    transport_class = transports.ForecastAdjustmentServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseBatchCreateForecastAdjustments,
        "_BaseBatchCreateForecastAdjustments__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = forecast_adjustment_service.BatchCreateForecastAdjustmentsResponse()
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
            return_value = (
                forecast_adjustment_service.BatchCreateForecastAdjustmentsResponse.pb(
                    return_value
                )
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.batch_create_forecast_adjustments(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_create_forecast_adjustments_rest_flattened():
    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = (
            forecast_adjustment_service.BatchCreateForecastAdjustmentsResponse()
        )

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "networks/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            requests=[
                forecast_adjustment_service.CreateForecastAdjustmentRequest(
                    parent="parent_value"
                )
            ],
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = (
            forecast_adjustment_service.BatchCreateForecastAdjustmentsResponse.pb(
                return_value
            )
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.batch_create_forecast_adjustments(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/forecastAdjustments:batchCreate"
            % client.transport._host,
            args[1],
        )


def test_batch_create_forecast_adjustments_rest_flattened_error(
    transport: str = "rest",
):
    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_create_forecast_adjustments(
            forecast_adjustment_service.BatchCreateForecastAdjustmentsRequest(),
            parent="parent_value",
            requests=[
                forecast_adjustment_service.CreateForecastAdjustmentRequest(
                    parent="parent_value"
                )
            ],
        )


def test_batch_activate_forecast_adjustments_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = ForecastAdjustmentServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_activate_forecast_adjustments
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.batch_activate_forecast_adjustments
        ] = mock_rpc

        request = {}
        client.batch_activate_forecast_adjustments(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_activate_forecast_adjustments(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_activate_forecast_adjustments_rest_required_fields(
    request_type=forecast_adjustment_service.BatchActivateForecastAdjustmentsRequest,
):
    transport_class = transports.ForecastAdjustmentServiceRestTransport

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
        transport_class._BaseBatchActivateForecastAdjustments,
        "_BaseBatchActivateForecastAdjustments__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = (
        forecast_adjustment_service.BatchActivateForecastAdjustmentsResponse()
    )
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
            return_value = (
                forecast_adjustment_service.BatchActivateForecastAdjustmentsResponse.pb(
                    return_value
                )
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.batch_activate_forecast_adjustments(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_activate_forecast_adjustments_rest_flattened():
    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = (
            forecast_adjustment_service.BatchActivateForecastAdjustmentsResponse()
        )

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
        return_value = (
            forecast_adjustment_service.BatchActivateForecastAdjustmentsResponse.pb(
                return_value
            )
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.batch_activate_forecast_adjustments(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/forecastAdjustments:batchActivate"
            % client.transport._host,
            args[1],
        )


def test_batch_activate_forecast_adjustments_rest_flattened_error(
    transport: str = "rest",
):
    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_activate_forecast_adjustments(
            forecast_adjustment_service.BatchActivateForecastAdjustmentsRequest(),
            parent="parent_value",
            names=["names_value"],
        )


def test_batch_deactivate_forecast_adjustments_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = ForecastAdjustmentServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_deactivate_forecast_adjustments
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.batch_deactivate_forecast_adjustments
        ] = mock_rpc

        request = {}
        client.batch_deactivate_forecast_adjustments(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_deactivate_forecast_adjustments(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_deactivate_forecast_adjustments_rest_required_fields(
    request_type=forecast_adjustment_service.BatchDeactivateForecastAdjustmentsRequest,
):
    transport_class = transports.ForecastAdjustmentServiceRestTransport

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
        transport_class._BaseBatchDeactivateForecastAdjustments,
        "_BaseBatchDeactivateForecastAdjustments__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = (
        forecast_adjustment_service.BatchDeactivateForecastAdjustmentsResponse()
    )
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
            return_value = forecast_adjustment_service.BatchDeactivateForecastAdjustmentsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.batch_deactivate_forecast_adjustments(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_deactivate_forecast_adjustments_rest_flattened():
    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = (
            forecast_adjustment_service.BatchDeactivateForecastAdjustmentsResponse()
        )

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
        return_value = (
            forecast_adjustment_service.BatchDeactivateForecastAdjustmentsResponse.pb(
                return_value
            )
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.batch_deactivate_forecast_adjustments(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/forecastAdjustments:batchDeactivate"
            % client.transport._host,
            args[1],
        )


def test_batch_deactivate_forecast_adjustments_rest_flattened_error(
    transport: str = "rest",
):
    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_deactivate_forecast_adjustments(
            forecast_adjustment_service.BatchDeactivateForecastAdjustmentsRequest(),
            parent="parent_value",
            names=["names_value"],
        )


def test_update_forecast_adjustment_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = ForecastAdjustmentServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.update_forecast_adjustment
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.update_forecast_adjustment
        ] = mock_rpc

        request = {}
        client.update_forecast_adjustment(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.update_forecast_adjustment(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_update_forecast_adjustment_rest_required_fields(
    request_type=forecast_adjustment_service.UpdateForecastAdjustmentRequest,
):
    transport_class = transports.ForecastAdjustmentServiceRestTransport

    request_init = {}
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseUpdateForecastAdjustment,
        "_BaseUpdateForecastAdjustment__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = forecast_adjustment_messages.ForecastAdjustment()
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
            return_value = forecast_adjustment_messages.ForecastAdjustment.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.update_forecast_adjustment(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_update_forecast_adjustment_rest_flattened():
    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = forecast_adjustment_messages.ForecastAdjustment()

        # get arguments that satisfy an http rule for this method
        sample_request = {
            "forecast_adjustment": {
                "name": "networks/sample1/forecastAdjustments/sample2"
            }
        }

        # get truthy value for each flattened field
        mock_args = dict(
            forecast_adjustment=forecast_adjustment_messages.ForecastAdjustment(
                daily_volume_settings=forecast_adjustment_messages.DailyVolumeSettings(
                    ad_opportunity_counts=[2300]
                )
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = forecast_adjustment_messages.ForecastAdjustment.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.update_forecast_adjustment(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{forecast_adjustment.name=networks/*/forecastAdjustments/*}"
            % client.transport._host,
            args[1],
        )


def test_update_forecast_adjustment_rest_flattened_error(transport: str = "rest"):
    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_forecast_adjustment(
            forecast_adjustment_service.UpdateForecastAdjustmentRequest(),
            forecast_adjustment=forecast_adjustment_messages.ForecastAdjustment(
                daily_volume_settings=forecast_adjustment_messages.DailyVolumeSettings(
                    ad_opportunity_counts=[2300]
                )
            ),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


def test_batch_update_forecast_adjustments_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = ForecastAdjustmentServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_update_forecast_adjustments
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.batch_update_forecast_adjustments
        ] = mock_rpc

        request = {}
        client.batch_update_forecast_adjustments(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_update_forecast_adjustments(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_update_forecast_adjustments_rest_required_fields(
    request_type=forecast_adjustment_service.BatchUpdateForecastAdjustmentsRequest,
):
    transport_class = transports.ForecastAdjustmentServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseBatchUpdateForecastAdjustments,
        "_BaseBatchUpdateForecastAdjustments__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = forecast_adjustment_service.BatchUpdateForecastAdjustmentsResponse()
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
            return_value = (
                forecast_adjustment_service.BatchUpdateForecastAdjustmentsResponse.pb(
                    return_value
                )
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.batch_update_forecast_adjustments(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_update_forecast_adjustments_rest_flattened():
    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = (
            forecast_adjustment_service.BatchUpdateForecastAdjustmentsResponse()
        )

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "networks/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            requests=[
                forecast_adjustment_service.UpdateForecastAdjustmentRequest(
                    forecast_adjustment=forecast_adjustment_messages.ForecastAdjustment(
                        daily_volume_settings=forecast_adjustment_messages.DailyVolumeSettings(
                            ad_opportunity_counts=[2300]
                        )
                    )
                )
            ],
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = (
            forecast_adjustment_service.BatchUpdateForecastAdjustmentsResponse.pb(
                return_value
            )
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.batch_update_forecast_adjustments(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/forecastAdjustments:batchUpdate"
            % client.transport._host,
            args[1],
        )


def test_batch_update_forecast_adjustments_rest_flattened_error(
    transport: str = "rest",
):
    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_update_forecast_adjustments(
            forecast_adjustment_service.BatchUpdateForecastAdjustmentsRequest(),
            parent="parent_value",
            requests=[
                forecast_adjustment_service.UpdateForecastAdjustmentRequest(
                    forecast_adjustment=forecast_adjustment_messages.ForecastAdjustment(
                        daily_volume_settings=forecast_adjustment_messages.DailyVolumeSettings(
                            ad_opportunity_counts=[2300]
                        )
                    )
                )
            ],
        )


def test_calculate_daily_ad_opportunity_counts_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = ForecastAdjustmentServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.calculate_daily_ad_opportunity_counts
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.calculate_daily_ad_opportunity_counts
        ] = mock_rpc

        request = {}
        client.calculate_daily_ad_opportunity_counts(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.calculate_daily_ad_opportunity_counts(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_calculate_daily_ad_opportunity_counts_rest_required_fields(
    request_type=forecast_adjustment_service.CalculateDailyAdOpportunityCountsRequest,
):
    transport_class = transports.ForecastAdjustmentServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseCalculateDailyAdOpportunityCounts,
        "_BaseCalculateDailyAdOpportunityCounts__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = (
        forecast_adjustment_service.CalculateDailyAdOpportunityCountsResponse()
    )
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
            return_value = forecast_adjustment_service.CalculateDailyAdOpportunityCountsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.calculate_daily_ad_opportunity_counts(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_calculate_daily_ad_opportunity_counts_rest_flattened():
    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = (
            forecast_adjustment_service.CalculateDailyAdOpportunityCountsResponse()
        )

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "networks/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            forecast_adjustment=forecast_adjustment_messages.ForecastAdjustment(
                daily_volume_settings=forecast_adjustment_messages.DailyVolumeSettings(
                    ad_opportunity_counts=[2300]
                )
            ),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = (
            forecast_adjustment_service.CalculateDailyAdOpportunityCountsResponse.pb(
                return_value
            )
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.calculate_daily_ad_opportunity_counts(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/forecastAdjustments:calculateDailyAdOpportunityCounts"
            % client.transport._host,
            args[1],
        )


def test_calculate_daily_ad_opportunity_counts_rest_flattened_error(
    transport: str = "rest",
):
    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.calculate_daily_ad_opportunity_counts(
            forecast_adjustment_service.CalculateDailyAdOpportunityCountsRequest(),
            parent="parent_value",
            forecast_adjustment=forecast_adjustment_messages.ForecastAdjustment(
                daily_volume_settings=forecast_adjustment_messages.DailyVolumeSettings(
                    ad_opportunity_counts=[2300]
                )
            ),
        )


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.ForecastAdjustmentServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = ForecastAdjustmentServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport=transport,
        )

    # It is an error to provide a credentials file and a transport instance.
    transport = transports.ForecastAdjustmentServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = ForecastAdjustmentServiceClient(
            client_options={"credentials_file": "credentials.json"},
            transport=transport,
        )

    # It is an error to provide an api_key and a transport instance.
    transport = transports.ForecastAdjustmentServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = ForecastAdjustmentServiceClient(
            client_options=options,
            transport=transport,
        )

    # It is an error to provide an api_key and a credential.
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = ForecastAdjustmentServiceClient(
            client_options=options, credentials=ga_credentials.AnonymousCredentials()
        )

    # It is an error to provide scopes and a transport instance.
    transport = transports.ForecastAdjustmentServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = ForecastAdjustmentServiceClient(
            client_options={"scopes": ["1", "2"]},
            transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.ForecastAdjustmentServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    client = ForecastAdjustmentServiceClient(transport=transport)
    assert client.transport is transport


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.ForecastAdjustmentServiceRestTransport,
    ],
)
def test_transport_adc(transport_class):
    # Test default credentials are used if not provided.
    with mock.patch.object(google.auth, "default") as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class()
        adc.assert_called_once()


def test_transport_kind_rest():
    transport = ForecastAdjustmentServiceClient.get_transport_class("rest")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "rest"


def test_get_forecast_adjustment_rest_bad_request(
    request_type=forecast_adjustment_service.GetForecastAdjustmentRequest,
):
    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"name": "networks/sample1/forecastAdjustments/sample2"}
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
        client.get_forecast_adjustment(request)


@pytest.mark.parametrize(
    "request_type",
    [
        forecast_adjustment_service.GetForecastAdjustmentRequest,
        dict,
    ],
)
def test_get_forecast_adjustment_rest_call_success(request_type):
    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "networks/sample1/forecastAdjustments/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = forecast_adjustment_messages.ForecastAdjustment(
            name="name_value",
            traffic_forecast_segment="traffic_forecast_segment_value",
            display_name="display_name_value",
            status=forecast_adjustment_enums.ForecastAdjustmentStatusEnum.ForecastAdjustmentStatus.ACTIVE,
            volume_type=forecast_adjustment_enums.ForecastAdjustmentVolumeTypeEnum.ForecastAdjustmentVolumeType.DAILY_VOLUME,
            allow_adjusting_forecast_above_recommended_limit=True,
            calculated_daily_ad_opportunity_counts=[4063],
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = forecast_adjustment_messages.ForecastAdjustment.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_forecast_adjustment(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, forecast_adjustment_messages.ForecastAdjustment)
    assert response.name == "name_value"
    assert response.traffic_forecast_segment == "traffic_forecast_segment_value"
    assert response.display_name == "display_name_value"
    assert (
        response.status
        == forecast_adjustment_enums.ForecastAdjustmentStatusEnum.ForecastAdjustmentStatus.ACTIVE
    )
    assert (
        response.volume_type
        == forecast_adjustment_enums.ForecastAdjustmentVolumeTypeEnum.ForecastAdjustmentVolumeType.DAILY_VOLUME
    )
    assert response.allow_adjusting_forecast_above_recommended_limit is True
    assert response.calculated_daily_ad_opportunity_counts == [4063]


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_forecast_adjustment_rest_interceptors(null_interceptor):
    transport = transports.ForecastAdjustmentServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.ForecastAdjustmentServiceRestInterceptor(),
    )
    client = ForecastAdjustmentServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.ForecastAdjustmentServiceRestInterceptor,
            "post_get_forecast_adjustment",
        ) as post,
        mock.patch.object(
            transports.ForecastAdjustmentServiceRestInterceptor,
            "post_get_forecast_adjustment_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.ForecastAdjustmentServiceRestInterceptor,
            "pre_get_forecast_adjustment",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = forecast_adjustment_service.GetForecastAdjustmentRequest.pb(
            forecast_adjustment_service.GetForecastAdjustmentRequest()
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
        return_value = forecast_adjustment_messages.ForecastAdjustment.to_json(
            forecast_adjustment_messages.ForecastAdjustment()
        )
        req.return_value.content = return_value

        request = forecast_adjustment_service.GetForecastAdjustmentRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = forecast_adjustment_messages.ForecastAdjustment()
        post_with_metadata.return_value = (
            forecast_adjustment_messages.ForecastAdjustment(),
            metadata,
        )

        client.get_forecast_adjustment(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_forecast_adjustments_rest_bad_request(
    request_type=forecast_adjustment_service.ListForecastAdjustmentsRequest,
):
    client = ForecastAdjustmentServiceClient(
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
        client.list_forecast_adjustments(request)


@pytest.mark.parametrize(
    "request_type",
    [
        forecast_adjustment_service.ListForecastAdjustmentsRequest,
        dict,
    ],
)
def test_list_forecast_adjustments_rest_call_success(request_type):
    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = forecast_adjustment_service.ListForecastAdjustmentsResponse(
            next_page_token="next_page_token_value",
            total_size=1086,
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = forecast_adjustment_service.ListForecastAdjustmentsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_forecast_adjustments(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListForecastAdjustmentsPager)
    assert response.next_page_token == "next_page_token_value"
    assert response.total_size == 1086


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_forecast_adjustments_rest_interceptors(null_interceptor):
    transport = transports.ForecastAdjustmentServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.ForecastAdjustmentServiceRestInterceptor(),
    )
    client = ForecastAdjustmentServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.ForecastAdjustmentServiceRestInterceptor,
            "post_list_forecast_adjustments",
        ) as post,
        mock.patch.object(
            transports.ForecastAdjustmentServiceRestInterceptor,
            "post_list_forecast_adjustments_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.ForecastAdjustmentServiceRestInterceptor,
            "pre_list_forecast_adjustments",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = forecast_adjustment_service.ListForecastAdjustmentsRequest.pb(
            forecast_adjustment_service.ListForecastAdjustmentsRequest()
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
            forecast_adjustment_service.ListForecastAdjustmentsResponse.to_json(
                forecast_adjustment_service.ListForecastAdjustmentsResponse()
            )
        )
        req.return_value.content = return_value

        request = forecast_adjustment_service.ListForecastAdjustmentsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = (
            forecast_adjustment_service.ListForecastAdjustmentsResponse()
        )
        post_with_metadata.return_value = (
            forecast_adjustment_service.ListForecastAdjustmentsResponse(),
            metadata,
        )

        client.list_forecast_adjustments(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_create_forecast_adjustment_rest_bad_request(
    request_type=forecast_adjustment_service.CreateForecastAdjustmentRequest,
):
    client = ForecastAdjustmentServiceClient(
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
        client.create_forecast_adjustment(request)


@pytest.mark.parametrize(
    "request_type",
    [
        forecast_adjustment_service.CreateForecastAdjustmentRequest,
        dict,
    ],
)
def test_create_forecast_adjustment_rest_call_success(request_type):
    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request_init["forecast_adjustment"] = {
        "daily_volume_settings": {"ad_opportunity_counts": [2301, 2302]},
        "total_volume_settings": {"ad_opportunity_count": 2185},
        "historical_basis_volume_settings": {
            "use_parent_traffic_forecast_segment_targeting": True,
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
                    "targeted_inventory_sizes": [
                        {"width": 544, "height": 633, "size_type": 1}
                    ],
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
                    "targeted_range": [
                        {"start_time": {"seconds": 751, "nanos": 543}, "end_time": {}}
                    ]
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
            "historical_date_range": {
                "start_date": {"year": 433, "month": 550, "day": 318},
                "end_date": {},
            },
            "multiplier_milli_percent": 2573,
        },
        "name": "name_value",
        "traffic_forecast_segment": "traffic_forecast_segment_value",
        "display_name": "display_name_value",
        "date_range": {},
        "status": 1,
        "volume_type": 1,
        "allow_adjusting_forecast_above_recommended_limit": True,
        "calculated_daily_ad_opportunity_counts": [4064, 4065],
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = (
        forecast_adjustment_service.CreateForecastAdjustmentRequest.meta.fields[
            "forecast_adjustment"
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
    for field, value in request_init["forecast_adjustment"].items():  # pragma: NO COVER
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
                for i in range(0, len(request_init["forecast_adjustment"][field])):
                    del request_init["forecast_adjustment"][field][i][subfield]
            else:
                del request_init["forecast_adjustment"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = forecast_adjustment_messages.ForecastAdjustment(
            name="name_value",
            traffic_forecast_segment="traffic_forecast_segment_value",
            display_name="display_name_value",
            status=forecast_adjustment_enums.ForecastAdjustmentStatusEnum.ForecastAdjustmentStatus.ACTIVE,
            volume_type=forecast_adjustment_enums.ForecastAdjustmentVolumeTypeEnum.ForecastAdjustmentVolumeType.DAILY_VOLUME,
            allow_adjusting_forecast_above_recommended_limit=True,
            calculated_daily_ad_opportunity_counts=[4063],
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = forecast_adjustment_messages.ForecastAdjustment.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.create_forecast_adjustment(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, forecast_adjustment_messages.ForecastAdjustment)
    assert response.name == "name_value"
    assert response.traffic_forecast_segment == "traffic_forecast_segment_value"
    assert response.display_name == "display_name_value"
    assert (
        response.status
        == forecast_adjustment_enums.ForecastAdjustmentStatusEnum.ForecastAdjustmentStatus.ACTIVE
    )
    assert (
        response.volume_type
        == forecast_adjustment_enums.ForecastAdjustmentVolumeTypeEnum.ForecastAdjustmentVolumeType.DAILY_VOLUME
    )
    assert response.allow_adjusting_forecast_above_recommended_limit is True
    assert response.calculated_daily_ad_opportunity_counts == [4063]


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_create_forecast_adjustment_rest_interceptors(null_interceptor):
    transport = transports.ForecastAdjustmentServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.ForecastAdjustmentServiceRestInterceptor(),
    )
    client = ForecastAdjustmentServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.ForecastAdjustmentServiceRestInterceptor,
            "post_create_forecast_adjustment",
        ) as post,
        mock.patch.object(
            transports.ForecastAdjustmentServiceRestInterceptor,
            "post_create_forecast_adjustment_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.ForecastAdjustmentServiceRestInterceptor,
            "pre_create_forecast_adjustment",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = forecast_adjustment_service.CreateForecastAdjustmentRequest.pb(
            forecast_adjustment_service.CreateForecastAdjustmentRequest()
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
        return_value = forecast_adjustment_messages.ForecastAdjustment.to_json(
            forecast_adjustment_messages.ForecastAdjustment()
        )
        req.return_value.content = return_value

        request = forecast_adjustment_service.CreateForecastAdjustmentRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = forecast_adjustment_messages.ForecastAdjustment()
        post_with_metadata.return_value = (
            forecast_adjustment_messages.ForecastAdjustment(),
            metadata,
        )

        client.create_forecast_adjustment(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_create_forecast_adjustments_rest_bad_request(
    request_type=forecast_adjustment_service.BatchCreateForecastAdjustmentsRequest,
):
    client = ForecastAdjustmentServiceClient(
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
        client.batch_create_forecast_adjustments(request)


@pytest.mark.parametrize(
    "request_type",
    [
        forecast_adjustment_service.BatchCreateForecastAdjustmentsRequest,
        dict,
    ],
)
def test_batch_create_forecast_adjustments_rest_call_success(request_type):
    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = (
            forecast_adjustment_service.BatchCreateForecastAdjustmentsResponse()
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = (
            forecast_adjustment_service.BatchCreateForecastAdjustmentsResponse.pb(
                return_value
            )
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.batch_create_forecast_adjustments(request)

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, forecast_adjustment_service.BatchCreateForecastAdjustmentsResponse
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_create_forecast_adjustments_rest_interceptors(null_interceptor):
    transport = transports.ForecastAdjustmentServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.ForecastAdjustmentServiceRestInterceptor(),
    )
    client = ForecastAdjustmentServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.ForecastAdjustmentServiceRestInterceptor,
            "post_batch_create_forecast_adjustments",
        ) as post,
        mock.patch.object(
            transports.ForecastAdjustmentServiceRestInterceptor,
            "post_batch_create_forecast_adjustments_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.ForecastAdjustmentServiceRestInterceptor,
            "pre_batch_create_forecast_adjustments",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = (
            forecast_adjustment_service.BatchCreateForecastAdjustmentsRequest.pb(
                forecast_adjustment_service.BatchCreateForecastAdjustmentsRequest()
            )
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
            forecast_adjustment_service.BatchCreateForecastAdjustmentsResponse.to_json(
                forecast_adjustment_service.BatchCreateForecastAdjustmentsResponse()
            )
        )
        req.return_value.content = return_value

        request = forecast_adjustment_service.BatchCreateForecastAdjustmentsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = (
            forecast_adjustment_service.BatchCreateForecastAdjustmentsResponse()
        )
        post_with_metadata.return_value = (
            forecast_adjustment_service.BatchCreateForecastAdjustmentsResponse(),
            metadata,
        )

        client.batch_create_forecast_adjustments(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_activate_forecast_adjustments_rest_bad_request(
    request_type=forecast_adjustment_service.BatchActivateForecastAdjustmentsRequest,
):
    client = ForecastAdjustmentServiceClient(
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
        client.batch_activate_forecast_adjustments(request)


@pytest.mark.parametrize(
    "request_type",
    [
        forecast_adjustment_service.BatchActivateForecastAdjustmentsRequest,
        dict,
    ],
)
def test_batch_activate_forecast_adjustments_rest_call_success(request_type):
    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = (
            forecast_adjustment_service.BatchActivateForecastAdjustmentsResponse()
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = (
            forecast_adjustment_service.BatchActivateForecastAdjustmentsResponse.pb(
                return_value
            )
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.batch_activate_forecast_adjustments(request)

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, forecast_adjustment_service.BatchActivateForecastAdjustmentsResponse
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_activate_forecast_adjustments_rest_interceptors(null_interceptor):
    transport = transports.ForecastAdjustmentServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.ForecastAdjustmentServiceRestInterceptor(),
    )
    client = ForecastAdjustmentServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.ForecastAdjustmentServiceRestInterceptor,
            "post_batch_activate_forecast_adjustments",
        ) as post,
        mock.patch.object(
            transports.ForecastAdjustmentServiceRestInterceptor,
            "post_batch_activate_forecast_adjustments_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.ForecastAdjustmentServiceRestInterceptor,
            "pre_batch_activate_forecast_adjustments",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = (
            forecast_adjustment_service.BatchActivateForecastAdjustmentsRequest.pb(
                forecast_adjustment_service.BatchActivateForecastAdjustmentsRequest()
            )
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
        return_value = forecast_adjustment_service.BatchActivateForecastAdjustmentsResponse.to_json(
            forecast_adjustment_service.BatchActivateForecastAdjustmentsResponse()
        )
        req.return_value.content = return_value

        request = forecast_adjustment_service.BatchActivateForecastAdjustmentsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = (
            forecast_adjustment_service.BatchActivateForecastAdjustmentsResponse()
        )
        post_with_metadata.return_value = (
            forecast_adjustment_service.BatchActivateForecastAdjustmentsResponse(),
            metadata,
        )

        client.batch_activate_forecast_adjustments(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_deactivate_forecast_adjustments_rest_bad_request(
    request_type=forecast_adjustment_service.BatchDeactivateForecastAdjustmentsRequest,
):
    client = ForecastAdjustmentServiceClient(
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
        client.batch_deactivate_forecast_adjustments(request)


@pytest.mark.parametrize(
    "request_type",
    [
        forecast_adjustment_service.BatchDeactivateForecastAdjustmentsRequest,
        dict,
    ],
)
def test_batch_deactivate_forecast_adjustments_rest_call_success(request_type):
    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = (
            forecast_adjustment_service.BatchDeactivateForecastAdjustmentsResponse()
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = (
            forecast_adjustment_service.BatchDeactivateForecastAdjustmentsResponse.pb(
                return_value
            )
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.batch_deactivate_forecast_adjustments(request)

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, forecast_adjustment_service.BatchDeactivateForecastAdjustmentsResponse
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_deactivate_forecast_adjustments_rest_interceptors(null_interceptor):
    transport = transports.ForecastAdjustmentServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.ForecastAdjustmentServiceRestInterceptor(),
    )
    client = ForecastAdjustmentServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.ForecastAdjustmentServiceRestInterceptor,
            "post_batch_deactivate_forecast_adjustments",
        ) as post,
        mock.patch.object(
            transports.ForecastAdjustmentServiceRestInterceptor,
            "post_batch_deactivate_forecast_adjustments_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.ForecastAdjustmentServiceRestInterceptor,
            "pre_batch_deactivate_forecast_adjustments",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = (
            forecast_adjustment_service.BatchDeactivateForecastAdjustmentsRequest.pb(
                forecast_adjustment_service.BatchDeactivateForecastAdjustmentsRequest()
            )
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
        return_value = forecast_adjustment_service.BatchDeactivateForecastAdjustmentsResponse.to_json(
            forecast_adjustment_service.BatchDeactivateForecastAdjustmentsResponse()
        )
        req.return_value.content = return_value

        request = (
            forecast_adjustment_service.BatchDeactivateForecastAdjustmentsRequest()
        )
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = (
            forecast_adjustment_service.BatchDeactivateForecastAdjustmentsResponse()
        )
        post_with_metadata.return_value = (
            forecast_adjustment_service.BatchDeactivateForecastAdjustmentsResponse(),
            metadata,
        )

        client.batch_deactivate_forecast_adjustments(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_update_forecast_adjustment_rest_bad_request(
    request_type=forecast_adjustment_service.UpdateForecastAdjustmentRequest,
):
    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {
        "forecast_adjustment": {"name": "networks/sample1/forecastAdjustments/sample2"}
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
        client.update_forecast_adjustment(request)


@pytest.mark.parametrize(
    "request_type",
    [
        forecast_adjustment_service.UpdateForecastAdjustmentRequest,
        dict,
    ],
)
def test_update_forecast_adjustment_rest_call_success(request_type):
    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {
        "forecast_adjustment": {"name": "networks/sample1/forecastAdjustments/sample2"}
    }
    request_init["forecast_adjustment"] = {
        "daily_volume_settings": {"ad_opportunity_counts": [2301, 2302]},
        "total_volume_settings": {"ad_opportunity_count": 2185},
        "historical_basis_volume_settings": {
            "use_parent_traffic_forecast_segment_targeting": True,
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
                    "targeted_inventory_sizes": [
                        {"width": 544, "height": 633, "size_type": 1}
                    ],
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
                    "targeted_range": [
                        {"start_time": {"seconds": 751, "nanos": 543}, "end_time": {}}
                    ]
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
            "historical_date_range": {
                "start_date": {"year": 433, "month": 550, "day": 318},
                "end_date": {},
            },
            "multiplier_milli_percent": 2573,
        },
        "name": "networks/sample1/forecastAdjustments/sample2",
        "traffic_forecast_segment": "traffic_forecast_segment_value",
        "display_name": "display_name_value",
        "date_range": {},
        "status": 1,
        "volume_type": 1,
        "allow_adjusting_forecast_above_recommended_limit": True,
        "calculated_daily_ad_opportunity_counts": [4064, 4065],
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = (
        forecast_adjustment_service.UpdateForecastAdjustmentRequest.meta.fields[
            "forecast_adjustment"
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
    for field, value in request_init["forecast_adjustment"].items():  # pragma: NO COVER
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
                for i in range(0, len(request_init["forecast_adjustment"][field])):
                    del request_init["forecast_adjustment"][field][i][subfield]
            else:
                del request_init["forecast_adjustment"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = forecast_adjustment_messages.ForecastAdjustment(
            name="name_value",
            traffic_forecast_segment="traffic_forecast_segment_value",
            display_name="display_name_value",
            status=forecast_adjustment_enums.ForecastAdjustmentStatusEnum.ForecastAdjustmentStatus.ACTIVE,
            volume_type=forecast_adjustment_enums.ForecastAdjustmentVolumeTypeEnum.ForecastAdjustmentVolumeType.DAILY_VOLUME,
            allow_adjusting_forecast_above_recommended_limit=True,
            calculated_daily_ad_opportunity_counts=[4063],
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = forecast_adjustment_messages.ForecastAdjustment.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.update_forecast_adjustment(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, forecast_adjustment_messages.ForecastAdjustment)
    assert response.name == "name_value"
    assert response.traffic_forecast_segment == "traffic_forecast_segment_value"
    assert response.display_name == "display_name_value"
    assert (
        response.status
        == forecast_adjustment_enums.ForecastAdjustmentStatusEnum.ForecastAdjustmentStatus.ACTIVE
    )
    assert (
        response.volume_type
        == forecast_adjustment_enums.ForecastAdjustmentVolumeTypeEnum.ForecastAdjustmentVolumeType.DAILY_VOLUME
    )
    assert response.allow_adjusting_forecast_above_recommended_limit is True
    assert response.calculated_daily_ad_opportunity_counts == [4063]


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_update_forecast_adjustment_rest_interceptors(null_interceptor):
    transport = transports.ForecastAdjustmentServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.ForecastAdjustmentServiceRestInterceptor(),
    )
    client = ForecastAdjustmentServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.ForecastAdjustmentServiceRestInterceptor,
            "post_update_forecast_adjustment",
        ) as post,
        mock.patch.object(
            transports.ForecastAdjustmentServiceRestInterceptor,
            "post_update_forecast_adjustment_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.ForecastAdjustmentServiceRestInterceptor,
            "pre_update_forecast_adjustment",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = forecast_adjustment_service.UpdateForecastAdjustmentRequest.pb(
            forecast_adjustment_service.UpdateForecastAdjustmentRequest()
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
        return_value = forecast_adjustment_messages.ForecastAdjustment.to_json(
            forecast_adjustment_messages.ForecastAdjustment()
        )
        req.return_value.content = return_value

        request = forecast_adjustment_service.UpdateForecastAdjustmentRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = forecast_adjustment_messages.ForecastAdjustment()
        post_with_metadata.return_value = (
            forecast_adjustment_messages.ForecastAdjustment(),
            metadata,
        )

        client.update_forecast_adjustment(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_update_forecast_adjustments_rest_bad_request(
    request_type=forecast_adjustment_service.BatchUpdateForecastAdjustmentsRequest,
):
    client = ForecastAdjustmentServiceClient(
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
        client.batch_update_forecast_adjustments(request)


@pytest.mark.parametrize(
    "request_type",
    [
        forecast_adjustment_service.BatchUpdateForecastAdjustmentsRequest,
        dict,
    ],
)
def test_batch_update_forecast_adjustments_rest_call_success(request_type):
    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = (
            forecast_adjustment_service.BatchUpdateForecastAdjustmentsResponse()
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = (
            forecast_adjustment_service.BatchUpdateForecastAdjustmentsResponse.pb(
                return_value
            )
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.batch_update_forecast_adjustments(request)

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, forecast_adjustment_service.BatchUpdateForecastAdjustmentsResponse
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_update_forecast_adjustments_rest_interceptors(null_interceptor):
    transport = transports.ForecastAdjustmentServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.ForecastAdjustmentServiceRestInterceptor(),
    )
    client = ForecastAdjustmentServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.ForecastAdjustmentServiceRestInterceptor,
            "post_batch_update_forecast_adjustments",
        ) as post,
        mock.patch.object(
            transports.ForecastAdjustmentServiceRestInterceptor,
            "post_batch_update_forecast_adjustments_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.ForecastAdjustmentServiceRestInterceptor,
            "pre_batch_update_forecast_adjustments",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = (
            forecast_adjustment_service.BatchUpdateForecastAdjustmentsRequest.pb(
                forecast_adjustment_service.BatchUpdateForecastAdjustmentsRequest()
            )
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
            forecast_adjustment_service.BatchUpdateForecastAdjustmentsResponse.to_json(
                forecast_adjustment_service.BatchUpdateForecastAdjustmentsResponse()
            )
        )
        req.return_value.content = return_value

        request = forecast_adjustment_service.BatchUpdateForecastAdjustmentsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = (
            forecast_adjustment_service.BatchUpdateForecastAdjustmentsResponse()
        )
        post_with_metadata.return_value = (
            forecast_adjustment_service.BatchUpdateForecastAdjustmentsResponse(),
            metadata,
        )

        client.batch_update_forecast_adjustments(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_calculate_daily_ad_opportunity_counts_rest_bad_request(
    request_type=forecast_adjustment_service.CalculateDailyAdOpportunityCountsRequest,
):
    client = ForecastAdjustmentServiceClient(
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
        client.calculate_daily_ad_opportunity_counts(request)


@pytest.mark.parametrize(
    "request_type",
    [
        forecast_adjustment_service.CalculateDailyAdOpportunityCountsRequest,
        dict,
    ],
)
def test_calculate_daily_ad_opportunity_counts_rest_call_success(request_type):
    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = (
            forecast_adjustment_service.CalculateDailyAdOpportunityCountsResponse()
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = (
            forecast_adjustment_service.CalculateDailyAdOpportunityCountsResponse.pb(
                return_value
            )
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.calculate_daily_ad_opportunity_counts(request)

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, forecast_adjustment_service.CalculateDailyAdOpportunityCountsResponse
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_calculate_daily_ad_opportunity_counts_rest_interceptors(null_interceptor):
    transport = transports.ForecastAdjustmentServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.ForecastAdjustmentServiceRestInterceptor(),
    )
    client = ForecastAdjustmentServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.ForecastAdjustmentServiceRestInterceptor,
            "post_calculate_daily_ad_opportunity_counts",
        ) as post,
        mock.patch.object(
            transports.ForecastAdjustmentServiceRestInterceptor,
            "post_calculate_daily_ad_opportunity_counts_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.ForecastAdjustmentServiceRestInterceptor,
            "pre_calculate_daily_ad_opportunity_counts",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = (
            forecast_adjustment_service.CalculateDailyAdOpportunityCountsRequest.pb(
                forecast_adjustment_service.CalculateDailyAdOpportunityCountsRequest()
            )
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
        return_value = forecast_adjustment_service.CalculateDailyAdOpportunityCountsResponse.to_json(
            forecast_adjustment_service.CalculateDailyAdOpportunityCountsResponse()
        )
        req.return_value.content = return_value

        request = forecast_adjustment_service.CalculateDailyAdOpportunityCountsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = (
            forecast_adjustment_service.CalculateDailyAdOpportunityCountsResponse()
        )
        post_with_metadata.return_value = (
            forecast_adjustment_service.CalculateDailyAdOpportunityCountsResponse(),
            metadata,
        )

        client.calculate_daily_ad_opportunity_counts(
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
    client = ForecastAdjustmentServiceClient(
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
    client = ForecastAdjustmentServiceClient(
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
    client = ForecastAdjustmentServiceClient(
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
    client = ForecastAdjustmentServiceClient(
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
    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_forecast_adjustment_empty_call_rest():
    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.get_forecast_adjustment), "__call__"
    ) as call:
        client.get_forecast_adjustment(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = forecast_adjustment_service.GetForecastAdjustmentRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_forecast_adjustments_empty_call_rest():
    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.list_forecast_adjustments), "__call__"
    ) as call:
        client.list_forecast_adjustments(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = forecast_adjustment_service.ListForecastAdjustmentsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_forecast_adjustment_empty_call_rest():
    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.create_forecast_adjustment), "__call__"
    ) as call:
        client.create_forecast_adjustment(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = forecast_adjustment_service.CreateForecastAdjustmentRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_create_forecast_adjustments_empty_call_rest():
    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_create_forecast_adjustments), "__call__"
    ) as call:
        client.batch_create_forecast_adjustments(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = (
            forecast_adjustment_service.BatchCreateForecastAdjustmentsRequest()
        )
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_activate_forecast_adjustments_empty_call_rest():
    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_activate_forecast_adjustments), "__call__"
    ) as call:
        client.batch_activate_forecast_adjustments(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = (
            forecast_adjustment_service.BatchActivateForecastAdjustmentsRequest()
        )
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_deactivate_forecast_adjustments_empty_call_rest():
    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_deactivate_forecast_adjustments), "__call__"
    ) as call:
        client.batch_deactivate_forecast_adjustments(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = (
            forecast_adjustment_service.BatchDeactivateForecastAdjustmentsRequest()
        )
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_forecast_adjustment_empty_call_rest():
    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.update_forecast_adjustment), "__call__"
    ) as call:
        client.update_forecast_adjustment(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = forecast_adjustment_service.UpdateForecastAdjustmentRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_update_forecast_adjustments_empty_call_rest():
    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_update_forecast_adjustments), "__call__"
    ) as call:
        client.batch_update_forecast_adjustments(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = (
            forecast_adjustment_service.BatchUpdateForecastAdjustmentsRequest()
        )
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_calculate_daily_ad_opportunity_counts_empty_call_rest():
    client = ForecastAdjustmentServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.calculate_daily_ad_opportunity_counts), "__call__"
    ) as call:
        client.calculate_daily_ad_opportunity_counts(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = (
            forecast_adjustment_service.CalculateDailyAdOpportunityCountsRequest()
        )
        assert args[0] == request_msg


def test_forecast_adjustment_service_base_transport_error():
    # Passing both a credentials object and credentials_file should raise an error
    with pytest.raises(core_exceptions.DuplicateCredentialArgs):
        transport = transports.ForecastAdjustmentServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            credentials_file="credentials.json",
        )


def test_forecast_adjustment_service_base_transport():
    # Instantiate the base transport.
    with mock.patch(
        "google.ads.admanager_v1.services.forecast_adjustment_service.transports.ForecastAdjustmentServiceTransport.__init__"
    ) as Transport:
        Transport.return_value = None
        transport = transports.ForecastAdjustmentServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        "get_forecast_adjustment",
        "list_forecast_adjustments",
        "create_forecast_adjustment",
        "batch_create_forecast_adjustments",
        "batch_activate_forecast_adjustments",
        "batch_deactivate_forecast_adjustments",
        "update_forecast_adjustment",
        "batch_update_forecast_adjustments",
        "calculate_daily_ad_opportunity_counts",
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


def test_forecast_adjustment_service_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with (
        mock.patch.object(
            google.auth, "load_credentials_from_file", autospec=True
        ) as load_creds,
        mock.patch(
            "google.ads.admanager_v1.services.forecast_adjustment_service.transports.ForecastAdjustmentServiceTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        load_creds.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.ForecastAdjustmentServiceTransport(
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


def test_forecast_adjustment_service_base_transport_with_adc():
    # Test the default credentials are used if credentials and credentials_file are None.
    with (
        mock.patch.object(google.auth, "default", autospec=True) as adc,
        mock.patch(
            "google.ads.admanager_v1.services.forecast_adjustment_service.transports.ForecastAdjustmentServiceTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.ForecastAdjustmentServiceTransport()
        adc.assert_called_once()


def test_forecast_adjustment_service_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        ForecastAdjustmentServiceClient()
        adc.assert_called_once_with(
            scopes=None,
            default_scopes=(
                "https://www.googleapis.com/auth/admanager",
                "https://www.googleapis.com/auth/admanager.readonly",
            ),
            quota_project_id=None,
        )


def test_forecast_adjustment_service_http_transport_client_cert_source_for_mtls():
    cred = ga_credentials.AnonymousCredentials()
    with mock.patch(
        "google.auth.transport.requests.AuthorizedSession.configure_mtls_channel"
    ) as mock_configure_mtls_channel:
        transports.ForecastAdjustmentServiceRestTransport(
            credentials=cred, client_cert_source_for_mtls=client_cert_source_callback
        )
        mock_configure_mtls_channel.assert_called_once_with(client_cert_source_callback)


@pytest.mark.parametrize(
    "transport_name",
    [
        "rest",
    ],
)
def test_forecast_adjustment_service_host_no_port(transport_name):
    client = ForecastAdjustmentServiceClient(
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
def test_forecast_adjustment_service_host_with_port(transport_name):
    client = ForecastAdjustmentServiceClient(
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
def test_forecast_adjustment_service_client_transport_session_collision(transport_name):
    creds1 = ga_credentials.AnonymousCredentials()
    creds2 = ga_credentials.AnonymousCredentials()
    client1 = ForecastAdjustmentServiceClient(
        credentials=creds1,
        transport=transport_name,
    )
    client2 = ForecastAdjustmentServiceClient(
        credentials=creds2,
        transport=transport_name,
    )
    session1 = client1.transport.get_forecast_adjustment._session
    session2 = client2.transport.get_forecast_adjustment._session
    assert session1 != session2
    session1 = client1.transport.list_forecast_adjustments._session
    session2 = client2.transport.list_forecast_adjustments._session
    assert session1 != session2
    session1 = client1.transport.create_forecast_adjustment._session
    session2 = client2.transport.create_forecast_adjustment._session
    assert session1 != session2
    session1 = client1.transport.batch_create_forecast_adjustments._session
    session2 = client2.transport.batch_create_forecast_adjustments._session
    assert session1 != session2
    session1 = client1.transport.batch_activate_forecast_adjustments._session
    session2 = client2.transport.batch_activate_forecast_adjustments._session
    assert session1 != session2
    session1 = client1.transport.batch_deactivate_forecast_adjustments._session
    session2 = client2.transport.batch_deactivate_forecast_adjustments._session
    assert session1 != session2
    session1 = client1.transport.update_forecast_adjustment._session
    session2 = client2.transport.update_forecast_adjustment._session
    assert session1 != session2
    session1 = client1.transport.batch_update_forecast_adjustments._session
    session2 = client2.transport.batch_update_forecast_adjustments._session
    assert session1 != session2
    session1 = client1.transport.calculate_daily_ad_opportunity_counts._session
    session2 = client2.transport.calculate_daily_ad_opportunity_counts._session
    assert session1 != session2


def test_ad_category_path():
    network_code = "squid"
    ad_category = "clam"
    expected = "networks/{network_code}/adCategories/{ad_category}".format(
        network_code=network_code,
        ad_category=ad_category,
    )
    actual = ForecastAdjustmentServiceClient.ad_category_path(network_code, ad_category)
    assert expected == actual


def test_parse_ad_category_path():
    expected = {
        "network_code": "whelk",
        "ad_category": "octopus",
    }
    path = ForecastAdjustmentServiceClient.ad_category_path(**expected)

    # Check that the path construction is reversible.
    actual = ForecastAdjustmentServiceClient.parse_ad_category_path(path)
    assert expected == actual


def test_ad_spot_path():
    network_code = "oyster"
    ad_spot = "nudibranch"
    expected = "networks/{network_code}/adSpots/{ad_spot}".format(
        network_code=network_code,
        ad_spot=ad_spot,
    )
    actual = ForecastAdjustmentServiceClient.ad_spot_path(network_code, ad_spot)
    assert expected == actual


def test_parse_ad_spot_path():
    expected = {
        "network_code": "cuttlefish",
        "ad_spot": "mussel",
    }
    path = ForecastAdjustmentServiceClient.ad_spot_path(**expected)

    # Check that the path construction is reversible.
    actual = ForecastAdjustmentServiceClient.parse_ad_spot_path(path)
    assert expected == actual


def test_ad_unit_path():
    network_code = "winkle"
    ad_unit = "nautilus"
    expected = "networks/{network_code}/adUnits/{ad_unit}".format(
        network_code=network_code,
        ad_unit=ad_unit,
    )
    actual = ForecastAdjustmentServiceClient.ad_unit_path(network_code, ad_unit)
    assert expected == actual


def test_parse_ad_unit_path():
    expected = {
        "network_code": "scallop",
        "ad_unit": "abalone",
    }
    path = ForecastAdjustmentServiceClient.ad_unit_path(**expected)

    # Check that the path construction is reversible.
    actual = ForecastAdjustmentServiceClient.parse_ad_unit_path(path)
    assert expected == actual


def test_application_path():
    network_code = "squid"
    application = "clam"
    expected = "networks/{network_code}/applications/{application}".format(
        network_code=network_code,
        application=application,
    )
    actual = ForecastAdjustmentServiceClient.application_path(network_code, application)
    assert expected == actual


def test_parse_application_path():
    expected = {
        "network_code": "whelk",
        "application": "octopus",
    }
    path = ForecastAdjustmentServiceClient.application_path(**expected)

    # Check that the path construction is reversible.
    actual = ForecastAdjustmentServiceClient.parse_application_path(path)
    assert expected == actual


def test_audience_segment_path():
    network_code = "oyster"
    audience_segment = "nudibranch"
    expected = "networks/{network_code}/audienceSegments/{audience_segment}".format(
        network_code=network_code,
        audience_segment=audience_segment,
    )
    actual = ForecastAdjustmentServiceClient.audience_segment_path(
        network_code, audience_segment
    )
    assert expected == actual


def test_parse_audience_segment_path():
    expected = {
        "network_code": "cuttlefish",
        "audience_segment": "mussel",
    }
    path = ForecastAdjustmentServiceClient.audience_segment_path(**expected)

    # Check that the path construction is reversible.
    actual = ForecastAdjustmentServiceClient.parse_audience_segment_path(path)
    assert expected == actual


def test_bandwidth_group_path():
    network_code = "winkle"
    bandwidth_group = "nautilus"
    expected = "networks/{network_code}/bandwidthGroups/{bandwidth_group}".format(
        network_code=network_code,
        bandwidth_group=bandwidth_group,
    )
    actual = ForecastAdjustmentServiceClient.bandwidth_group_path(
        network_code, bandwidth_group
    )
    assert expected == actual


def test_parse_bandwidth_group_path():
    expected = {
        "network_code": "scallop",
        "bandwidth_group": "abalone",
    }
    path = ForecastAdjustmentServiceClient.bandwidth_group_path(**expected)

    # Check that the path construction is reversible.
    actual = ForecastAdjustmentServiceClient.parse_bandwidth_group_path(path)
    assert expected == actual


def test_browser_path():
    network_code = "squid"
    browser = "clam"
    expected = "networks/{network_code}/browsers/{browser}".format(
        network_code=network_code,
        browser=browser,
    )
    actual = ForecastAdjustmentServiceClient.browser_path(network_code, browser)
    assert expected == actual


def test_parse_browser_path():
    expected = {
        "network_code": "whelk",
        "browser": "octopus",
    }
    path = ForecastAdjustmentServiceClient.browser_path(**expected)

    # Check that the path construction is reversible.
    actual = ForecastAdjustmentServiceClient.parse_browser_path(path)
    assert expected == actual


def test_browser_language_path():
    network_code = "oyster"
    browser_language = "nudibranch"
    expected = "networks/{network_code}/browserLanguages/{browser_language}".format(
        network_code=network_code,
        browser_language=browser_language,
    )
    actual = ForecastAdjustmentServiceClient.browser_language_path(
        network_code, browser_language
    )
    assert expected == actual


def test_parse_browser_language_path():
    expected = {
        "network_code": "cuttlefish",
        "browser_language": "mussel",
    }
    path = ForecastAdjustmentServiceClient.browser_language_path(**expected)

    # Check that the path construction is reversible.
    actual = ForecastAdjustmentServiceClient.parse_browser_language_path(path)
    assert expected == actual


def test_cms_metadata_value_path():
    network_code = "winkle"
    cms_metadata_value = "nautilus"
    expected = "networks/{network_code}/cmsMetadataValues/{cms_metadata_value}".format(
        network_code=network_code,
        cms_metadata_value=cms_metadata_value,
    )
    actual = ForecastAdjustmentServiceClient.cms_metadata_value_path(
        network_code, cms_metadata_value
    )
    assert expected == actual


def test_parse_cms_metadata_value_path():
    expected = {
        "network_code": "scallop",
        "cms_metadata_value": "abalone",
    }
    path = ForecastAdjustmentServiceClient.cms_metadata_value_path(**expected)

    # Check that the path construction is reversible.
    actual = ForecastAdjustmentServiceClient.parse_cms_metadata_value_path(path)
    assert expected == actual


def test_content_path():
    network_code = "squid"
    content = "clam"
    expected = "networks/{network_code}/content/{content}".format(
        network_code=network_code,
        content=content,
    )
    actual = ForecastAdjustmentServiceClient.content_path(network_code, content)
    assert expected == actual


def test_parse_content_path():
    expected = {
        "network_code": "whelk",
        "content": "octopus",
    }
    path = ForecastAdjustmentServiceClient.content_path(**expected)

    # Check that the path construction is reversible.
    actual = ForecastAdjustmentServiceClient.parse_content_path(path)
    assert expected == actual


def test_content_bundle_path():
    network_code = "oyster"
    content_bundle = "nudibranch"
    expected = "networks/{network_code}/contentBundles/{content_bundle}".format(
        network_code=network_code,
        content_bundle=content_bundle,
    )
    actual = ForecastAdjustmentServiceClient.content_bundle_path(
        network_code, content_bundle
    )
    assert expected == actual


def test_parse_content_bundle_path():
    expected = {
        "network_code": "cuttlefish",
        "content_bundle": "mussel",
    }
    path = ForecastAdjustmentServiceClient.content_bundle_path(**expected)

    # Check that the path construction is reversible.
    actual = ForecastAdjustmentServiceClient.parse_content_bundle_path(path)
    assert expected == actual


def test_content_label_path():
    network_code = "winkle"
    content_label = "nautilus"
    expected = "networks/{network_code}/contentLabels/{content_label}".format(
        network_code=network_code,
        content_label=content_label,
    )
    actual = ForecastAdjustmentServiceClient.content_label_path(
        network_code, content_label
    )
    assert expected == actual


def test_parse_content_label_path():
    expected = {
        "network_code": "scallop",
        "content_label": "abalone",
    }
    path = ForecastAdjustmentServiceClient.content_label_path(**expected)

    # Check that the path construction is reversible.
    actual = ForecastAdjustmentServiceClient.parse_content_label_path(path)
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
    actual = ForecastAdjustmentServiceClient.custom_targeting_key_path(
        network_code, custom_targeting_key
    )
    assert expected == actual


def test_parse_custom_targeting_key_path():
    expected = {
        "network_code": "whelk",
        "custom_targeting_key": "octopus",
    }
    path = ForecastAdjustmentServiceClient.custom_targeting_key_path(**expected)

    # Check that the path construction is reversible.
    actual = ForecastAdjustmentServiceClient.parse_custom_targeting_key_path(path)
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
    actual = ForecastAdjustmentServiceClient.custom_targeting_value_path(
        network_code, custom_targeting_value
    )
    assert expected == actual


def test_parse_custom_targeting_value_path():
    expected = {
        "network_code": "cuttlefish",
        "custom_targeting_value": "mussel",
    }
    path = ForecastAdjustmentServiceClient.custom_targeting_value_path(**expected)

    # Check that the path construction is reversible.
    actual = ForecastAdjustmentServiceClient.parse_custom_targeting_value_path(path)
    assert expected == actual


def test_device_capability_path():
    network_code = "winkle"
    device_capability = "nautilus"
    expected = "networks/{network_code}/deviceCapabilities/{device_capability}".format(
        network_code=network_code,
        device_capability=device_capability,
    )
    actual = ForecastAdjustmentServiceClient.device_capability_path(
        network_code, device_capability
    )
    assert expected == actual


def test_parse_device_capability_path():
    expected = {
        "network_code": "scallop",
        "device_capability": "abalone",
    }
    path = ForecastAdjustmentServiceClient.device_capability_path(**expected)

    # Check that the path construction is reversible.
    actual = ForecastAdjustmentServiceClient.parse_device_capability_path(path)
    assert expected == actual


def test_device_category_path():
    network_code = "squid"
    device_category = "clam"
    expected = "networks/{network_code}/deviceCategories/{device_category}".format(
        network_code=network_code,
        device_category=device_category,
    )
    actual = ForecastAdjustmentServiceClient.device_category_path(
        network_code, device_category
    )
    assert expected == actual


def test_parse_device_category_path():
    expected = {
        "network_code": "whelk",
        "device_category": "octopus",
    }
    path = ForecastAdjustmentServiceClient.device_category_path(**expected)

    # Check that the path construction is reversible.
    actual = ForecastAdjustmentServiceClient.parse_device_category_path(path)
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
    actual = ForecastAdjustmentServiceClient.device_manufacturer_path(
        network_code, device_manufacturer
    )
    assert expected == actual


def test_parse_device_manufacturer_path():
    expected = {
        "network_code": "cuttlefish",
        "device_manufacturer": "mussel",
    }
    path = ForecastAdjustmentServiceClient.device_manufacturer_path(**expected)

    # Check that the path construction is reversible.
    actual = ForecastAdjustmentServiceClient.parse_device_manufacturer_path(path)
    assert expected == actual


def test_forecast_adjustment_path():
    network_code = "winkle"
    forecast_adjustment = "nautilus"
    expected = (
        "networks/{network_code}/forecastAdjustments/{forecast_adjustment}".format(
            network_code=network_code,
            forecast_adjustment=forecast_adjustment,
        )
    )
    actual = ForecastAdjustmentServiceClient.forecast_adjustment_path(
        network_code, forecast_adjustment
    )
    assert expected == actual


def test_parse_forecast_adjustment_path():
    expected = {
        "network_code": "scallop",
        "forecast_adjustment": "abalone",
    }
    path = ForecastAdjustmentServiceClient.forecast_adjustment_path(**expected)

    # Check that the path construction is reversible.
    actual = ForecastAdjustmentServiceClient.parse_forecast_adjustment_path(path)
    assert expected == actual


def test_geo_target_path():
    network_code = "squid"
    geo_target = "clam"
    expected = "networks/{network_code}/geoTargets/{geo_target}".format(
        network_code=network_code,
        geo_target=geo_target,
    )
    actual = ForecastAdjustmentServiceClient.geo_target_path(network_code, geo_target)
    assert expected == actual


def test_parse_geo_target_path():
    expected = {
        "network_code": "whelk",
        "geo_target": "octopus",
    }
    path = ForecastAdjustmentServiceClient.geo_target_path(**expected)

    # Check that the path construction is reversible.
    actual = ForecastAdjustmentServiceClient.parse_geo_target_path(path)
    assert expected == actual


def test_inventory_url_path():
    network_code = "oyster"
    inventory_url = "nudibranch"
    expected = "networks/{network_code}/inventoryUrls/{inventory_url}".format(
        network_code=network_code,
        inventory_url=inventory_url,
    )
    actual = ForecastAdjustmentServiceClient.inventory_url_path(
        network_code, inventory_url
    )
    assert expected == actual


def test_parse_inventory_url_path():
    expected = {
        "network_code": "cuttlefish",
        "inventory_url": "mussel",
    }
    path = ForecastAdjustmentServiceClient.inventory_url_path(**expected)

    # Check that the path construction is reversible.
    actual = ForecastAdjustmentServiceClient.parse_inventory_url_path(path)
    assert expected == actual


def test_mobile_carrier_path():
    network_code = "winkle"
    mobile_carrier = "nautilus"
    expected = "networks/{network_code}/mobileCarriers/{mobile_carrier}".format(
        network_code=network_code,
        mobile_carrier=mobile_carrier,
    )
    actual = ForecastAdjustmentServiceClient.mobile_carrier_path(
        network_code, mobile_carrier
    )
    assert expected == actual


def test_parse_mobile_carrier_path():
    expected = {
        "network_code": "scallop",
        "mobile_carrier": "abalone",
    }
    path = ForecastAdjustmentServiceClient.mobile_carrier_path(**expected)

    # Check that the path construction is reversible.
    actual = ForecastAdjustmentServiceClient.parse_mobile_carrier_path(path)
    assert expected == actual


def test_mobile_device_path():
    network_code = "squid"
    mobile_device = "clam"
    expected = "networks/{network_code}/mobileDevices/{mobile_device}".format(
        network_code=network_code,
        mobile_device=mobile_device,
    )
    actual = ForecastAdjustmentServiceClient.mobile_device_path(
        network_code, mobile_device
    )
    assert expected == actual


def test_parse_mobile_device_path():
    expected = {
        "network_code": "whelk",
        "mobile_device": "octopus",
    }
    path = ForecastAdjustmentServiceClient.mobile_device_path(**expected)

    # Check that the path construction is reversible.
    actual = ForecastAdjustmentServiceClient.parse_mobile_device_path(path)
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
    actual = ForecastAdjustmentServiceClient.mobile_device_submodel_path(
        network_code, mobile_device_submodel
    )
    assert expected == actual


def test_parse_mobile_device_submodel_path():
    expected = {
        "network_code": "cuttlefish",
        "mobile_device_submodel": "mussel",
    }
    path = ForecastAdjustmentServiceClient.mobile_device_submodel_path(**expected)

    # Check that the path construction is reversible.
    actual = ForecastAdjustmentServiceClient.parse_mobile_device_submodel_path(path)
    assert expected == actual


def test_network_path():
    network_code = "winkle"
    expected = "networks/{network_code}".format(
        network_code=network_code,
    )
    actual = ForecastAdjustmentServiceClient.network_path(network_code)
    assert expected == actual


def test_parse_network_path():
    expected = {
        "network_code": "nautilus",
    }
    path = ForecastAdjustmentServiceClient.network_path(**expected)

    # Check that the path construction is reversible.
    actual = ForecastAdjustmentServiceClient.parse_network_path(path)
    assert expected == actual


def test_operating_system_path():
    network_code = "scallop"
    operating_system = "abalone"
    expected = "networks/{network_code}/operatingSystems/{operating_system}".format(
        network_code=network_code,
        operating_system=operating_system,
    )
    actual = ForecastAdjustmentServiceClient.operating_system_path(
        network_code, operating_system
    )
    assert expected == actual


def test_parse_operating_system_path():
    expected = {
        "network_code": "squid",
        "operating_system": "clam",
    }
    path = ForecastAdjustmentServiceClient.operating_system_path(**expected)

    # Check that the path construction is reversible.
    actual = ForecastAdjustmentServiceClient.parse_operating_system_path(path)
    assert expected == actual


def test_operating_system_version_path():
    network_code = "whelk"
    operating_system_version = "octopus"
    expected = "networks/{network_code}/operatingSystemVersions/{operating_system_version}".format(
        network_code=network_code,
        operating_system_version=operating_system_version,
    )
    actual = ForecastAdjustmentServiceClient.operating_system_version_path(
        network_code, operating_system_version
    )
    assert expected == actual


def test_parse_operating_system_version_path():
    expected = {
        "network_code": "oyster",
        "operating_system_version": "nudibranch",
    }
    path = ForecastAdjustmentServiceClient.operating_system_version_path(**expected)

    # Check that the path construction is reversible.
    actual = ForecastAdjustmentServiceClient.parse_operating_system_version_path(path)
    assert expected == actual


def test_placement_path():
    network_code = "cuttlefish"
    placement = "mussel"
    expected = "networks/{network_code}/placements/{placement}".format(
        network_code=network_code,
        placement=placement,
    )
    actual = ForecastAdjustmentServiceClient.placement_path(network_code, placement)
    assert expected == actual


def test_parse_placement_path():
    expected = {
        "network_code": "winkle",
        "placement": "nautilus",
    }
    path = ForecastAdjustmentServiceClient.placement_path(**expected)

    # Check that the path construction is reversible.
    actual = ForecastAdjustmentServiceClient.parse_placement_path(path)
    assert expected == actual


def test_taxonomy_category_path():
    network_code = "scallop"
    taxonomy_category = "abalone"
    expected = "networks/{network_code}/taxonomyCategories/{taxonomy_category}".format(
        network_code=network_code,
        taxonomy_category=taxonomy_category,
    )
    actual = ForecastAdjustmentServiceClient.taxonomy_category_path(
        network_code, taxonomy_category
    )
    assert expected == actual


def test_parse_taxonomy_category_path():
    expected = {
        "network_code": "squid",
        "taxonomy_category": "clam",
    }
    path = ForecastAdjustmentServiceClient.taxonomy_category_path(**expected)

    # Check that the path construction is reversible.
    actual = ForecastAdjustmentServiceClient.parse_taxonomy_category_path(path)
    assert expected == actual


def test_traffic_forecast_segment_path():
    network_code = "whelk"
    traffic_forecast_segment = "octopus"
    expected = "networks/{network_code}/trafficForecastSegments/{traffic_forecast_segment}".format(
        network_code=network_code,
        traffic_forecast_segment=traffic_forecast_segment,
    )
    actual = ForecastAdjustmentServiceClient.traffic_forecast_segment_path(
        network_code, traffic_forecast_segment
    )
    assert expected == actual


def test_parse_traffic_forecast_segment_path():
    expected = {
        "network_code": "oyster",
        "traffic_forecast_segment": "nudibranch",
    }
    path = ForecastAdjustmentServiceClient.traffic_forecast_segment_path(**expected)

    # Check that the path construction is reversible.
    actual = ForecastAdjustmentServiceClient.parse_traffic_forecast_segment_path(path)
    assert expected == actual


def test_common_billing_account_path():
    billing_account = "cuttlefish"
    expected = "billingAccounts/{billing_account}".format(
        billing_account=billing_account,
    )
    actual = ForecastAdjustmentServiceClient.common_billing_account_path(
        billing_account
    )
    assert expected == actual


def test_parse_common_billing_account_path():
    expected = {
        "billing_account": "mussel",
    }
    path = ForecastAdjustmentServiceClient.common_billing_account_path(**expected)

    # Check that the path construction is reversible.
    actual = ForecastAdjustmentServiceClient.parse_common_billing_account_path(path)
    assert expected == actual


def test_common_folder_path():
    folder = "winkle"
    expected = "folders/{folder}".format(
        folder=folder,
    )
    actual = ForecastAdjustmentServiceClient.common_folder_path(folder)
    assert expected == actual


def test_parse_common_folder_path():
    expected = {
        "folder": "nautilus",
    }
    path = ForecastAdjustmentServiceClient.common_folder_path(**expected)

    # Check that the path construction is reversible.
    actual = ForecastAdjustmentServiceClient.parse_common_folder_path(path)
    assert expected == actual


def test_common_organization_path():
    organization = "scallop"
    expected = "organizations/{organization}".format(
        organization=organization,
    )
    actual = ForecastAdjustmentServiceClient.common_organization_path(organization)
    assert expected == actual


def test_parse_common_organization_path():
    expected = {
        "organization": "abalone",
    }
    path = ForecastAdjustmentServiceClient.common_organization_path(**expected)

    # Check that the path construction is reversible.
    actual = ForecastAdjustmentServiceClient.parse_common_organization_path(path)
    assert expected == actual


def test_common_project_path():
    project = "squid"
    expected = "projects/{project}".format(
        project=project,
    )
    actual = ForecastAdjustmentServiceClient.common_project_path(project)
    assert expected == actual


def test_parse_common_project_path():
    expected = {
        "project": "clam",
    }
    path = ForecastAdjustmentServiceClient.common_project_path(**expected)

    # Check that the path construction is reversible.
    actual = ForecastAdjustmentServiceClient.parse_common_project_path(path)
    assert expected == actual


def test_common_location_path():
    project = "whelk"
    location = "octopus"
    expected = "projects/{project}/locations/{location}".format(
        project=project,
        location=location,
    )
    actual = ForecastAdjustmentServiceClient.common_location_path(project, location)
    assert expected == actual


def test_parse_common_location_path():
    expected = {
        "project": "oyster",
        "location": "nudibranch",
    }
    path = ForecastAdjustmentServiceClient.common_location_path(**expected)

    # Check that the path construction is reversible.
    actual = ForecastAdjustmentServiceClient.parse_common_location_path(path)
    assert expected == actual


def test_client_with_default_client_info():
    client_info = gapic_v1.client_info.ClientInfo()

    with mock.patch.object(
        transports.ForecastAdjustmentServiceTransport, "_prep_wrapped_messages"
    ) as prep:
        client = ForecastAdjustmentServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

    with mock.patch.object(
        transports.ForecastAdjustmentServiceTransport, "_prep_wrapped_messages"
    ) as prep:
        transport_class = ForecastAdjustmentServiceClient.get_transport_class()
        transport = transport_class(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)


def test_transport_close_rest():
    client = ForecastAdjustmentServiceClient(
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
        client = ForecastAdjustmentServiceClient(
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
        (
            ForecastAdjustmentServiceClient,
            transports.ForecastAdjustmentServiceRestTransport,
        ),
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
