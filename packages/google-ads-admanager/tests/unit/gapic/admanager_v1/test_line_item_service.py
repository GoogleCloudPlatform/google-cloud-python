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
import google.type.money_pb2 as money_pb2  # type: ignore
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

from google.ads.admanager_v1.services.line_item_service import (
    LineItemServiceClient,
    pagers,
    transports,
)
from google.ads.admanager_v1.types import (
    applied_label,
    brand_lift_partner_enum,
    child_content_eligibility_enum,
    creative_placeholder,
    creative_targeting,
    custom_field_value,
    custom_pacing_curve,
    custom_pacing_goal_unit_enum,
    delivery_enums,
    delivery_indicator,
    discount_type_enum,
    environment_type_enum,
    exclusion_scope_enum,
    frequency_cap,
    goal,
    goal_enums,
    grp_provider_enum,
    grp_settings,
    grp_target_gender_enum,
    line_item_allowed_format_enum,
    line_item_deal_info,
    line_item_delivery_forecast_source_enum,
    line_item_discount,
    line_item_enums,
    line_item_messages,
    line_item_service,
    line_item_stats,
    nielsen_ctv_pacing_enum,
    pacing_device_categorization_enum,
    reach_partner_enum,
    request_platform_enum,
    size,
    size_type_enum,
    skippable_ad_type_enum,
    targeted_video_bumper_type_enum,
    targeting,
    third_party_measurement_settings,
    time_unit_enum,
    video_position_enum,
    viewability_partner_enum,
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

    assert LineItemServiceClient._get_client_cert_source(None, False) is None
    assert (
        LineItemServiceClient._get_client_cert_source(mock_provided_cert_source, False)
        is None
    )
    assert (
        LineItemServiceClient._get_client_cert_source(mock_provided_cert_source, True)
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
                LineItemServiceClient._get_client_cert_source(None, True)
                is mock_default_cert_source
            )
            assert (
                LineItemServiceClient._get_client_cert_source(
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
    client = LineItemServiceClient(credentials=cred)
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
    client = LineItemServiceClient(credentials=cred)
    client._transport._credentials = cred

    error = core_exceptions.GoogleAPICallError("message", details=[])
    error.code = error_code

    client._add_cred_info_for_auth_errors(error)
    assert error.details == []


@pytest.mark.parametrize(
    "client_class,transport_name",
    [
        (LineItemServiceClient, "rest"),
    ],
)
def test_line_item_service_client_from_service_account_info(
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
        (transports.LineItemServiceRestTransport, "rest"),
    ],
)
def test_line_item_service_client_service_account_always_use_jwt(
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
        (LineItemServiceClient, "rest"),
    ],
)
def test_line_item_service_client_from_service_account_file(
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


def test_line_item_service_client_get_transport_class():
    transport = LineItemServiceClient.get_transport_class()
    available_transports = [
        transports.LineItemServiceRestTransport,
    ]
    assert transport in available_transports

    transport = LineItemServiceClient.get_transport_class("rest")
    assert transport == transports.LineItemServiceRestTransport


@pytest.mark.parametrize(
    "client_class,transport_class,transport_name",
    [
        (LineItemServiceClient, transports.LineItemServiceRestTransport, "rest"),
    ],
)
@mock.patch.object(
    LineItemServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(LineItemServiceClient),
)
def test_line_item_service_client_client_options(
    client_class, transport_class, transport_name
):
    # Check that if channel is provided we won't create a new one.
    with mock.patch.object(LineItemServiceClient, "get_transport_class") as gtc:
        transport = transport_class(credentials=ga_credentials.AnonymousCredentials())
        client = client_class(transport=transport)
        gtc.assert_not_called()

    # Check that if channel is provided via str we will create a new one.
    with mock.patch.object(LineItemServiceClient, "get_transport_class") as gtc:
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
            LineItemServiceClient,
            transports.LineItemServiceRestTransport,
            "rest",
            "true",
        ),
        (
            LineItemServiceClient,
            transports.LineItemServiceRestTransport,
            "rest",
            "false",
        ),
    ],
)
@mock.patch.object(
    LineItemServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(LineItemServiceClient),
)
@mock.patch.dict(os.environ, {"GOOGLE_API_USE_MTLS_ENDPOINT": "auto"})
def test_line_item_service_client_mtls_env_auto(
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


@pytest.mark.parametrize("client_class", [LineItemServiceClient])
@mock.patch.object(
    LineItemServiceClient,
    "DEFAULT_ENDPOINT",
    modify_default_endpoint(LineItemServiceClient),
)
def test_line_item_service_client_get_mtls_endpoint_and_cert_source(client_class):
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


@pytest.mark.parametrize("client_class", [LineItemServiceClient])
@mock.patch.object(
    LineItemServiceClient,
    "_DEFAULT_ENDPOINT_TEMPLATE",
    modify_default_endpoint_template(LineItemServiceClient),
)
def test_line_item_service_client_client_api_endpoint(client_class):
    mock_client_cert_source = client_cert_source_callback
    api_override = "foo.com"
    default_universe = LineItemServiceClient._DEFAULT_UNIVERSE
    default_endpoint = LineItemServiceClient._DEFAULT_ENDPOINT_TEMPLATE.format(
        UNIVERSE_DOMAIN=default_universe
    )
    mock_universe = "bar.com"
    mock_endpoint = LineItemServiceClient._DEFAULT_ENDPOINT_TEMPLATE.format(
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
        (LineItemServiceClient, transports.LineItemServiceRestTransport, "rest"),
    ],
)
def test_line_item_service_client_client_options_scopes(
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
        (LineItemServiceClient, transports.LineItemServiceRestTransport, "rest", None),
    ],
)
def test_line_item_service_client_client_options_credentials_file(
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


def test_get_line_item_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = LineItemServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.get_line_item in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.get_line_item] = mock_rpc

        request = {}
        client.get_line_item(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.get_line_item(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_get_line_item_rest_required_fields(
    request_type=line_item_service.GetLineItemRequest,
):
    transport_class = transports.LineItemServiceRestTransport

    request_init = {}
    request_init["name"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseGetLineItem,
        "_BaseGetLineItem__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = line_item_messages.LineItem()
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
            return_value = line_item_messages.LineItem.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.get_line_item(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_get_line_item_rest_flattened():
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = line_item_messages.LineItem()

        # get arguments that satisfy an http rule for this method
        sample_request = {"name": "networks/sample1/lineItems/sample2"}

        # get truthy value for each flattened field
        mock_args = dict(
            name="name_value",
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = line_item_messages.LineItem.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.get_line_item(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{name=networks/*/lineItems/*}" % client.transport._host, args[1]
        )


def test_get_line_item_rest_flattened_error(transport: str = "rest"):
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.get_line_item(
            line_item_service.GetLineItemRequest(),
            name="name_value",
        )


def test_list_line_items_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = LineItemServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.list_line_items in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.list_line_items] = mock_rpc

        request = {}
        client.list_line_items(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.list_line_items(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_list_line_items_rest_required_fields(
    request_type=line_item_service.ListLineItemsRequest,
):
    transport_class = transports.LineItemServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseListLineItems,
        "_BaseListLineItems__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = line_item_service.ListLineItemsResponse()
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
            return_value = line_item_service.ListLineItemsResponse.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.list_line_items(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_list_line_items_rest_flattened():
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = line_item_service.ListLineItemsResponse()

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
        return_value = line_item_service.ListLineItemsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.list_line_items(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/lineItems" % client.transport._host, args[1]
        )


def test_list_line_items_rest_flattened_error(transport: str = "rest"):
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.list_line_items(
            line_item_service.ListLineItemsRequest(),
            parent="parent_value",
        )


def test_list_line_items_rest_pager(transport: str = "rest"):
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(Session, "request") as req:
        # TODO(kbandes): remove this mock unless there's a good reason for it.
        # with mock.patch.object(path_template, 'transcode') as transcode:
        # Set the response as a series of pages
        response = (
            line_item_service.ListLineItemsResponse(
                line_items=[
                    line_item_messages.LineItem(),
                    line_item_messages.LineItem(),
                    line_item_messages.LineItem(),
                ],
                next_page_token="abc",
            ),
            line_item_service.ListLineItemsResponse(
                line_items=[],
                next_page_token="def",
            ),
            line_item_service.ListLineItemsResponse(
                line_items=[
                    line_item_messages.LineItem(),
                ],
                next_page_token="ghi",
            ),
            line_item_service.ListLineItemsResponse(
                line_items=[
                    line_item_messages.LineItem(),
                    line_item_messages.LineItem(),
                ],
            ),
        )
        # Two responses for two calls
        response = response + response

        # Wrap the values into proper Response objs
        response = tuple(
            line_item_service.ListLineItemsResponse.to_json(x) for x in response
        )
        return_values = tuple(Response() for i in response)
        for return_val, response_val in zip(return_values, response):
            return_val._content = response_val.encode("UTF-8")
            return_val.status_code = 200
        req.side_effect = return_values

        sample_request = {"parent": "networks/sample1"}

        pager = client.list_line_items(request=sample_request)

        assert pager.next_page_token == "abc"
        assert str(pager).startswith(f"{pager.__class__.__name__}<")

        results = list(pager)
        assert len(results) == 6
        assert all(isinstance(i, line_item_messages.LineItem) for i in results)

        pages = list(client.list_line_items(request=sample_request).pages)
        for page_, token in zip(pages, ["abc", "def", "ghi", ""]):
            assert page_.raw_page.next_page_token == token


def test_create_line_item_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = LineItemServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.create_line_item in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.create_line_item] = (
            mock_rpc
        )

        request = {}
        client.create_line_item(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.create_line_item(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_create_line_item_rest_required_fields(
    request_type=line_item_service.CreateLineItemRequest,
):
    transport_class = transports.LineItemServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseCreateLineItem,
        "_BaseCreateLineItem__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = line_item_messages.LineItem()
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
            return_value = line_item_messages.LineItem.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.create_line_item(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_create_line_item_rest_flattened():
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = line_item_messages.LineItem()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "networks/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            line_item=line_item_messages.LineItem(name="name_value"),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = line_item_messages.LineItem.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.create_line_item(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/lineItems" % client.transport._host, args[1]
        )


def test_create_line_item_rest_flattened_error(transport: str = "rest"):
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.create_line_item(
            line_item_service.CreateLineItemRequest(),
            parent="parent_value",
            line_item=line_item_messages.LineItem(name="name_value"),
        )


def test_batch_create_line_items_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = LineItemServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_create_line_items
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.batch_create_line_items
        ] = mock_rpc

        request = {}
        client.batch_create_line_items(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_create_line_items(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_create_line_items_rest_required_fields(
    request_type=line_item_service.BatchCreateLineItemsRequest,
):
    transport_class = transports.LineItemServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseBatchCreateLineItems,
        "_BaseBatchCreateLineItems__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = line_item_service.BatchCreateLineItemsResponse()
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
            return_value = line_item_service.BatchCreateLineItemsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.batch_create_line_items(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_create_line_items_rest_flattened():
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = line_item_service.BatchCreateLineItemsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "networks/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            requests=[line_item_service.CreateLineItemRequest(parent="parent_value")],
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = line_item_service.BatchCreateLineItemsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.batch_create_line_items(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/lineItems:batchCreate" % client.transport._host,
            args[1],
        )


def test_batch_create_line_items_rest_flattened_error(transport: str = "rest"):
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_create_line_items(
            line_item_service.BatchCreateLineItemsRequest(),
            parent="parent_value",
            requests=[line_item_service.CreateLineItemRequest(parent="parent_value")],
        )


def test_update_line_item_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = LineItemServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert client._transport.update_line_item in client._transport._wrapped_methods

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.update_line_item] = (
            mock_rpc
        )

        request = {}
        client.update_line_item(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.update_line_item(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_update_line_item_rest_required_fields(
    request_type=line_item_service.UpdateLineItemRequest,
):
    transport_class = transports.LineItemServiceRestTransport

    request_init = {}
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseUpdateLineItem,
        "_BaseUpdateLineItem__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = line_item_messages.LineItem()
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
            return_value = line_item_messages.LineItem.pb(return_value)
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.update_line_item(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_update_line_item_rest_flattened():
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = line_item_messages.LineItem()

        # get arguments that satisfy an http rule for this method
        sample_request = {"line_item": {"name": "networks/sample1/lineItems/sample2"}}

        # get truthy value for each flattened field
        mock_args = dict(
            line_item=line_item_messages.LineItem(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = line_item_messages.LineItem.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.update_line_item(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{line_item.name=networks/*/lineItems/*}" % client.transport._host,
            args[1],
        )


def test_update_line_item_rest_flattened_error(transport: str = "rest"):
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.update_line_item(
            line_item_service.UpdateLineItemRequest(),
            line_item=line_item_messages.LineItem(name="name_value"),
            update_mask=field_mask_pb2.FieldMask(paths=["paths_value"]),
        )


def test_batch_update_line_items_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = LineItemServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_update_line_items
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.batch_update_line_items
        ] = mock_rpc

        request = {}
        client.batch_update_line_items(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_update_line_items(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_update_line_items_rest_required_fields(
    request_type=line_item_service.BatchUpdateLineItemsRequest,
):
    transport_class = transports.LineItemServiceRestTransport

    request_init = {}
    request_init["parent"] = ""
    request = request_type(**request_init)
    pb_request = request_type.pb(request)
    jsonified_request = json.loads(
        json_format.MessageToJson(pb_request, use_integers_for_enums=False)
    )

    # verify fields with default values are dropped

    default_values = getattr(
        transport_class._BaseBatchUpdateLineItems,
        "_BaseBatchUpdateLineItems__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = line_item_service.BatchUpdateLineItemsResponse()
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
            return_value = line_item_service.BatchUpdateLineItemsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.batch_update_line_items(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_update_line_items_rest_flattened():
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = line_item_service.BatchUpdateLineItemsResponse()

        # get arguments that satisfy an http rule for this method
        sample_request = {"parent": "networks/sample1"}

        # get truthy value for each flattened field
        mock_args = dict(
            parent="parent_value",
            requests=[
                line_item_service.UpdateLineItemRequest(
                    line_item=line_item_messages.LineItem(name="name_value")
                )
            ],
        )
        mock_args.update(sample_request)

        # Wrap the value into a proper Response obj
        response_value = Response()
        response_value.status_code = 200
        # Convert return value to protobuf type
        return_value = line_item_service.BatchUpdateLineItemsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.batch_update_line_items(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/lineItems:batchUpdate" % client.transport._host,
            args[1],
        )


def test_batch_update_line_items_rest_flattened_error(transport: str = "rest"):
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_update_line_items(
            line_item_service.BatchUpdateLineItemsRequest(),
            parent="parent_value",
            requests=[
                line_item_service.UpdateLineItemRequest(
                    line_item=line_item_messages.LineItem(name="name_value")
                )
            ],
        )


def test_batch_activate_line_items_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = LineItemServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_activate_line_items
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.batch_activate_line_items
        ] = mock_rpc

        request = {}
        client.batch_activate_line_items(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_activate_line_items(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_activate_line_items_rest_required_fields(
    request_type=line_item_service.BatchActivateLineItemsRequest,
):
    transport_class = transports.LineItemServiceRestTransport

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
        transport_class._BaseBatchActivateLineItems,
        "_BaseBatchActivateLineItems__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = line_item_service.BatchActivateLineItemsResponse()
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
            return_value = line_item_service.BatchActivateLineItemsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.batch_activate_line_items(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_activate_line_items_rest_flattened():
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = line_item_service.BatchActivateLineItemsResponse()

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
        return_value = line_item_service.BatchActivateLineItemsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.batch_activate_line_items(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/lineItems:batchActivate"
            % client.transport._host,
            args[1],
        )


def test_batch_activate_line_items_rest_flattened_error(transport: str = "rest"):
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_activate_line_items(
            line_item_service.BatchActivateLineItemsRequest(),
            parent="parent_value",
            names=["names_value"],
        )


def test_batch_pause_line_items_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = LineItemServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_pause_line_items
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[client._transport.batch_pause_line_items] = (
            mock_rpc
        )

        request = {}
        client.batch_pause_line_items(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_pause_line_items(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_pause_line_items_rest_required_fields(
    request_type=line_item_service.BatchPauseLineItemsRequest,
):
    transport_class = transports.LineItemServiceRestTransport

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
        transport_class._BaseBatchPauseLineItems,
        "_BaseBatchPauseLineItems__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = line_item_service.BatchPauseLineItemsResponse()
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
            return_value = line_item_service.BatchPauseLineItemsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.batch_pause_line_items(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_pause_line_items_rest_flattened():
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = line_item_service.BatchPauseLineItemsResponse()

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
        return_value = line_item_service.BatchPauseLineItemsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.batch_pause_line_items(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/lineItems:batchPause" % client.transport._host,
            args[1],
        )


def test_batch_pause_line_items_rest_flattened_error(transport: str = "rest"):
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_pause_line_items(
            line_item_service.BatchPauseLineItemsRequest(),
            parent="parent_value",
            names=["names_value"],
        )


def test_batch_resume_line_items_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = LineItemServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_resume_line_items
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.batch_resume_line_items
        ] = mock_rpc

        request = {}
        client.batch_resume_line_items(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_resume_line_items(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_resume_line_items_rest_required_fields(
    request_type=line_item_service.BatchResumeLineItemsRequest,
):
    transport_class = transports.LineItemServiceRestTransport

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
        transport_class._BaseBatchResumeLineItems,
        "_BaseBatchResumeLineItems__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = line_item_service.BatchResumeLineItemsResponse()
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
            return_value = line_item_service.BatchResumeLineItemsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.batch_resume_line_items(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_resume_line_items_rest_flattened():
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = line_item_service.BatchResumeLineItemsResponse()

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
        return_value = line_item_service.BatchResumeLineItemsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.batch_resume_line_items(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/lineItems:batchResume" % client.transport._host,
            args[1],
        )


def test_batch_resume_line_items_rest_flattened_error(transport: str = "rest"):
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_resume_line_items(
            line_item_service.BatchResumeLineItemsRequest(),
            parent="parent_value",
            names=["names_value"],
        )


def test_batch_resume_and_overbook_line_items_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = LineItemServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_resume_and_overbook_line_items
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.batch_resume_and_overbook_line_items
        ] = mock_rpc

        request = {}
        client.batch_resume_and_overbook_line_items(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_resume_and_overbook_line_items(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_resume_and_overbook_line_items_rest_required_fields(
    request_type=line_item_service.BatchResumeAndOverbookLineItemsRequest,
):
    transport_class = transports.LineItemServiceRestTransport

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
        transport_class._BaseBatchResumeAndOverbookLineItems,
        "_BaseBatchResumeAndOverbookLineItems__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = line_item_service.BatchResumeAndOverbookLineItemsResponse()
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
            return_value = line_item_service.BatchResumeAndOverbookLineItemsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.batch_resume_and_overbook_line_items(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_resume_and_overbook_line_items_rest_flattened():
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = line_item_service.BatchResumeAndOverbookLineItemsResponse()

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
        return_value = line_item_service.BatchResumeAndOverbookLineItemsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.batch_resume_and_overbook_line_items(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/lineItems:batchResumeAndOverbook"
            % client.transport._host,
            args[1],
        )


def test_batch_resume_and_overbook_line_items_rest_flattened_error(
    transport: str = "rest",
):
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_resume_and_overbook_line_items(
            line_item_service.BatchResumeAndOverbookLineItemsRequest(),
            parent="parent_value",
            names=["names_value"],
        )


def test_batch_delete_line_items_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = LineItemServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_delete_line_items
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.batch_delete_line_items
        ] = mock_rpc

        request = {}
        client.batch_delete_line_items(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_delete_line_items(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_delete_line_items_rest_required_fields(
    request_type=line_item_service.BatchDeleteLineItemsRequest,
):
    transport_class = transports.LineItemServiceRestTransport

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
        transport_class._BaseBatchDeleteLineItems,
        "_BaseBatchDeleteLineItems__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = LineItemServiceClient(
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

            response = client.batch_delete_line_items(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_delete_line_items_rest_flattened():
    client = LineItemServiceClient(
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

        client.batch_delete_line_items(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/lineItems:batchDelete" % client.transport._host,
            args[1],
        )


def test_batch_delete_line_items_rest_flattened_error(transport: str = "rest"):
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_delete_line_items(
            line_item_service.BatchDeleteLineItemsRequest(),
            parent="parent_value",
            names=["names_value"],
        )


def test_batch_reserve_line_items_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = LineItemServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_reserve_line_items
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.batch_reserve_line_items
        ] = mock_rpc

        request = {}
        client.batch_reserve_line_items(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_reserve_line_items(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_reserve_line_items_rest_required_fields(
    request_type=line_item_service.BatchReserveLineItemsRequest,
):
    transport_class = transports.LineItemServiceRestTransport

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
        transport_class._BaseBatchReserveLineItems,
        "_BaseBatchReserveLineItems__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = line_item_service.BatchReserveLineItemsResponse()
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
            return_value = line_item_service.BatchReserveLineItemsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.batch_reserve_line_items(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_reserve_line_items_rest_flattened():
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = line_item_service.BatchReserveLineItemsResponse()

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
        return_value = line_item_service.BatchReserveLineItemsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.batch_reserve_line_items(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/lineItems:batchReserve" % client.transport._host,
            args[1],
        )


def test_batch_reserve_line_items_rest_flattened_error(transport: str = "rest"):
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_reserve_line_items(
            line_item_service.BatchReserveLineItemsRequest(),
            parent="parent_value",
            names=["names_value"],
        )


def test_batch_reserve_and_overbook_line_items_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = LineItemServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_reserve_and_overbook_line_items
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.batch_reserve_and_overbook_line_items
        ] = mock_rpc

        request = {}
        client.batch_reserve_and_overbook_line_items(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_reserve_and_overbook_line_items(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_reserve_and_overbook_line_items_rest_required_fields(
    request_type=line_item_service.BatchReserveAndOverbookLineItemsRequest,
):
    transport_class = transports.LineItemServiceRestTransport

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
        transport_class._BaseBatchReserveAndOverbookLineItems,
        "_BaseBatchReserveAndOverbookLineItems__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = line_item_service.BatchReserveAndOverbookLineItemsResponse()
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
                line_item_service.BatchReserveAndOverbookLineItemsResponse.pb(
                    return_value
                )
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.batch_reserve_and_overbook_line_items(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_reserve_and_overbook_line_items_rest_flattened():
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = line_item_service.BatchReserveAndOverbookLineItemsResponse()

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
        return_value = line_item_service.BatchReserveAndOverbookLineItemsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.batch_reserve_and_overbook_line_items(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/lineItems:batchReserveAndOverbook"
            % client.transport._host,
            args[1],
        )


def test_batch_reserve_and_overbook_line_items_rest_flattened_error(
    transport: str = "rest",
):
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_reserve_and_overbook_line_items(
            line_item_service.BatchReserveAndOverbookLineItemsRequest(),
            parent="parent_value",
            names=["names_value"],
        )


def test_batch_release_line_items_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = LineItemServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_release_line_items
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.batch_release_line_items
        ] = mock_rpc

        request = {}
        client.batch_release_line_items(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_release_line_items(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_release_line_items_rest_required_fields(
    request_type=line_item_service.BatchReleaseLineItemsRequest,
):
    transport_class = transports.LineItemServiceRestTransport

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
        transport_class._BaseBatchReleaseLineItems,
        "_BaseBatchReleaseLineItems__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = line_item_service.BatchReleaseLineItemsResponse()
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
            return_value = line_item_service.BatchReleaseLineItemsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.batch_release_line_items(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_release_line_items_rest_flattened():
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = line_item_service.BatchReleaseLineItemsResponse()

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
        return_value = line_item_service.BatchReleaseLineItemsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.batch_release_line_items(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/lineItems:batchRelease" % client.transport._host,
            args[1],
        )


def test_batch_release_line_items_rest_flattened_error(transport: str = "rest"):
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_release_line_items(
            line_item_service.BatchReleaseLineItemsRequest(),
            parent="parent_value",
            names=["names_value"],
        )


def test_batch_archive_line_items_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = LineItemServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_archive_line_items
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.batch_archive_line_items
        ] = mock_rpc

        request = {}
        client.batch_archive_line_items(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_archive_line_items(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_archive_line_items_rest_required_fields(
    request_type=line_item_service.BatchArchiveLineItemsRequest,
):
    transport_class = transports.LineItemServiceRestTransport

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
        transport_class._BaseBatchArchiveLineItems,
        "_BaseBatchArchiveLineItems__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = line_item_service.BatchArchiveLineItemsResponse()
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
            return_value = line_item_service.BatchArchiveLineItemsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.batch_archive_line_items(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_archive_line_items_rest_flattened():
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = line_item_service.BatchArchiveLineItemsResponse()

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
        return_value = line_item_service.BatchArchiveLineItemsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.batch_archive_line_items(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/lineItems:batchArchive" % client.transport._host,
            args[1],
        )


def test_batch_archive_line_items_rest_flattened_error(transport: str = "rest"):
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_archive_line_items(
            line_item_service.BatchArchiveLineItemsRequest(),
            parent="parent_value",
            names=["names_value"],
        )


def test_batch_unarchive_line_items_rest_use_cached_wrapped_rpc():
    # Clients should use _prep_wrapped_messages to create cached wrapped rpcs,
    # instead of constructing them on each call
    with mock.patch("google.api_core.gapic_v1.method.wrap_method") as wrapper_fn:
        client = LineItemServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport="rest",
        )

        # Should wrap all calls on client creation
        assert wrapper_fn.call_count > 0
        wrapper_fn.reset_mock()

        # Ensure method has been cached
        assert (
            client._transport.batch_unarchive_line_items
            in client._transport._wrapped_methods
        )

        # Replace cached wrapped function with mock
        mock_rpc = mock.Mock()
        mock_rpc.return_value.name = (
            "foo"  # operation_request.operation in compute client(s) expect a string.
        )
        client._transport._wrapped_methods[
            client._transport.batch_unarchive_line_items
        ] = mock_rpc

        request = {}
        client.batch_unarchive_line_items(request)

        # Establish that the underlying gRPC stub method was called.
        assert mock_rpc.call_count == 1

        client.batch_unarchive_line_items(request)

        # Establish that a new wrapper was not created for this call
        assert wrapper_fn.call_count == 0
        assert mock_rpc.call_count == 2


def test_batch_unarchive_line_items_rest_required_fields(
    request_type=line_item_service.BatchUnarchiveLineItemsRequest,
):
    transport_class = transports.LineItemServiceRestTransport

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
        transport_class._BaseBatchUnarchiveLineItems,
        "_BaseBatchUnarchiveLineItems__REQUIRED_FIELDS_DEFAULT_VALUES",
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

    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )
    request = request_type(**request_init)

    # Designate an appropriate value for the returned response.
    return_value = line_item_service.BatchUnarchiveLineItemsResponse()
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
            return_value = line_item_service.BatchUnarchiveLineItemsResponse.pb(
                return_value
            )
            json_return_value = json_format.MessageToJson(return_value)

            response_value._content = json_return_value.encode("UTF-8")
            req.return_value = response_value
            req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

            response = client.batch_unarchive_line_items(request)

            expected_params = [("$alt", "json;enum-encoding=int")]
            actual_params = req.call_args.kwargs["params"]
            assert sorted(expected_params) == sorted(actual_params)


def test_batch_unarchive_line_items_rest_flattened():
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = line_item_service.BatchUnarchiveLineItemsResponse()

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
        return_value = line_item_service.BatchUnarchiveLineItemsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value._content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}

        client.batch_unarchive_line_items(**mock_args)

        # Establish that the underlying call was made with the expected
        # request object values.
        assert len(req.mock_calls) == 1
        _, args, _ = req.mock_calls[0]
        assert path_template.validate(
            "%s/v1/{parent=networks/*}/lineItems:batchUnarchive"
            % client.transport._host,
            args[1],
        )


def test_batch_unarchive_line_items_rest_flattened_error(transport: str = "rest"):
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport=transport,
    )

    # Attempting to call a method with both a request object and flattened
    # fields is an error.
    with pytest.raises(ValueError):
        client.batch_unarchive_line_items(
            line_item_service.BatchUnarchiveLineItemsRequest(),
            parent="parent_value",
            names=["names_value"],
        )


def test_credentials_transport_error():
    # It is an error to provide credentials and a transport instance.
    transport = transports.LineItemServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = LineItemServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            transport=transport,
        )

    # It is an error to provide a credentials file and a transport instance.
    transport = transports.LineItemServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = LineItemServiceClient(
            client_options={"credentials_file": "credentials.json"},
            transport=transport,
        )

    # It is an error to provide an api_key and a transport instance.
    transport = transports.LineItemServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = LineItemServiceClient(
            client_options=options,
            transport=transport,
        )

    # It is an error to provide an api_key and a credential.
    options = client_options.ClientOptions()
    options.api_key = "api_key"
    with pytest.raises(ValueError):
        client = LineItemServiceClient(
            client_options=options, credentials=ga_credentials.AnonymousCredentials()
        )

    # It is an error to provide scopes and a transport instance.
    transport = transports.LineItemServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    with pytest.raises(ValueError):
        client = LineItemServiceClient(
            client_options={"scopes": ["1", "2"]},
            transport=transport,
        )


def test_transport_instance():
    # A client may be instantiated with a custom transport instance.
    transport = transports.LineItemServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
    )
    client = LineItemServiceClient(transport=transport)
    assert client.transport is transport


@pytest.mark.parametrize(
    "transport_class",
    [
        transports.LineItemServiceRestTransport,
    ],
)
def test_transport_adc(transport_class):
    # Test default credentials are used if not provided.
    with mock.patch.object(google.auth, "default") as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport_class()
        adc.assert_called_once()


def test_transport_kind_rest():
    transport = LineItemServiceClient.get_transport_class("rest")(
        credentials=ga_credentials.AnonymousCredentials()
    )
    assert transport.kind == "rest"


def test_get_line_item_rest_bad_request(
    request_type=line_item_service.GetLineItemRequest,
):
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"name": "networks/sample1/lineItems/sample2"}
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
        client.get_line_item(request)


@pytest.mark.parametrize(
    "request_type",
    [
        line_item_service.GetLineItemRequest,
        dict,
    ],
)
def test_get_line_item_rest_call_success(request_type):
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"name": "networks/sample1/lineItems/sample2"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = line_item_messages.LineItem(
            name="name_value",
            order="order_value",
            display_name="display_name_value",
            external_line_item_id="external_line_item_id_value",
            order_display_name="order_display_name_value",
            auto_extension_days=2053,
            end_time_unlimited=True,
            creative_rotation_type=delivery_enums.CreativeRotationTypeEnum.CreativeRotationType.EVENLY,
            delivery_rate_type=delivery_enums.LineItemDeliveryRateTypeEnum.LineItemDeliveryRateType.AS_FAST_AS_POSSIBLE,
            delivery_forecast_source=line_item_delivery_forecast_source_enum.LineItemDeliveryForecastSourceEnum.LineItemDeliveryForecastSource.CUSTOM_PACING_CURVE,
            roadblocking_type=delivery_enums.RoadblockingTypeEnum.RoadblockingType.ALL_ROADBLOCK,
            skippable_ad_type=skippable_ad_type_enum.SkippableAdTypeEnum.SkippableAdType.ANY,
            line_item_type=line_item_enums.LineItemTypeEnum.LineItemType.SPONSORSHIP,
            priority=898,
            cost_type=line_item_enums.LineItemCostTypeEnum.LineItemCostType.CPA,
            contracted_units_bought=2465,
            environment_type=environment_type_enum.EnvironmentTypeEnum.EnvironmentType.BROWSER,
            companion_delivery_option=delivery_enums.CompanionDeliveryOptionEnum.CompanionDeliveryOption.OPTIONAL,
            allow_overbook=True,
            skip_inventory_check=True,
            skip_cross_selling_rule_warning_checks=True,
            reserve_on_creation=True,
            status=line_item_enums.LineItemComputedStatusEnum.LineItemComputedStatus.CANCELED,
            reservation_status=line_item_enums.LineItemReservationStatusEnum.LineItemReservationStatus.RESERVED,
            archived=True,
            web_property_code="web_property_code_value",
            same_advertiser_exception_enabled=True,
            update_source="update_source_value",
            notes="notes_value",
            competitive_constraint_scope=exclusion_scope_enum.ExclusionScopeEnum.ExclusionScope.PAGE,
            missing_creatives=True,
            youtube_kids_restricted=True,
            viewability_provider_companies=["viewability_provider_companies_value"],
            child_content_eligibility=child_content_eligibility_enum.ChildContentEligibilityEnum.ChildContentEligibility.ALLOWED,
            custom_vast_extension="custom_vast_extension_value",
            sponsorship_exclusivity_enabled=True,
            repeated_creative_serving_enabled=True,
            allowed_formats=[
                line_item_allowed_format_enum.LineItemAllowedFormatEnum.LineItemAllowedFormat.AUDIO
            ],
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = line_item_messages.LineItem.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.get_line_item(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, line_item_messages.LineItem)
    assert response.name == "name_value"
    assert response.order == "order_value"
    assert response.display_name == "display_name_value"
    assert response.external_line_item_id == "external_line_item_id_value"
    assert response.order_display_name == "order_display_name_value"
    assert response.auto_extension_days == 2053
    assert response.end_time_unlimited is True
    assert (
        response.creative_rotation_type
        == delivery_enums.CreativeRotationTypeEnum.CreativeRotationType.EVENLY
    )
    assert (
        response.delivery_rate_type
        == delivery_enums.LineItemDeliveryRateTypeEnum.LineItemDeliveryRateType.AS_FAST_AS_POSSIBLE
    )
    assert (
        response.delivery_forecast_source
        == line_item_delivery_forecast_source_enum.LineItemDeliveryForecastSourceEnum.LineItemDeliveryForecastSource.CUSTOM_PACING_CURVE
    )
    assert (
        response.roadblocking_type
        == delivery_enums.RoadblockingTypeEnum.RoadblockingType.ALL_ROADBLOCK
    )
    assert (
        response.skippable_ad_type
        == skippable_ad_type_enum.SkippableAdTypeEnum.SkippableAdType.ANY
    )
    assert (
        response.line_item_type
        == line_item_enums.LineItemTypeEnum.LineItemType.SPONSORSHIP
    )
    assert response.priority == 898
    assert (
        response.cost_type == line_item_enums.LineItemCostTypeEnum.LineItemCostType.CPA
    )
    assert response.contracted_units_bought == 2465
    assert (
        response.environment_type
        == environment_type_enum.EnvironmentTypeEnum.EnvironmentType.BROWSER
    )
    assert (
        response.companion_delivery_option
        == delivery_enums.CompanionDeliveryOptionEnum.CompanionDeliveryOption.OPTIONAL
    )
    assert response.allow_overbook is True
    assert response.skip_inventory_check is True
    assert response.skip_cross_selling_rule_warning_checks is True
    assert response.reserve_on_creation is True
    assert (
        response.status
        == line_item_enums.LineItemComputedStatusEnum.LineItemComputedStatus.CANCELED
    )
    assert (
        response.reservation_status
        == line_item_enums.LineItemReservationStatusEnum.LineItemReservationStatus.RESERVED
    )
    assert response.archived is True
    assert response.web_property_code == "web_property_code_value"
    assert response.same_advertiser_exception_enabled is True
    assert response.update_source == "update_source_value"
    assert response.notes == "notes_value"
    assert (
        response.competitive_constraint_scope
        == exclusion_scope_enum.ExclusionScopeEnum.ExclusionScope.PAGE
    )
    assert response.missing_creatives is True
    assert response.youtube_kids_restricted is True
    assert response.viewability_provider_companies == [
        "viewability_provider_companies_value"
    ]
    assert (
        response.child_content_eligibility
        == child_content_eligibility_enum.ChildContentEligibilityEnum.ChildContentEligibility.ALLOWED
    )
    assert response.custom_vast_extension == "custom_vast_extension_value"
    assert response.sponsorship_exclusivity_enabled is True
    assert response.repeated_creative_serving_enabled is True
    assert response.allowed_formats == [
        line_item_allowed_format_enum.LineItemAllowedFormatEnum.LineItemAllowedFormat.AUDIO
    ]


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_get_line_item_rest_interceptors(null_interceptor):
    transport = transports.LineItemServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.LineItemServiceRestInterceptor(),
    )
    client = LineItemServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor, "post_get_line_item"
        ) as post,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor,
            "post_get_line_item_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor, "pre_get_line_item"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = line_item_service.GetLineItemRequest.pb(
            line_item_service.GetLineItemRequest()
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
        return_value = line_item_messages.LineItem.to_json(
            line_item_messages.LineItem()
        )
        req.return_value.content = return_value

        request = line_item_service.GetLineItemRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = line_item_messages.LineItem()
        post_with_metadata.return_value = line_item_messages.LineItem(), metadata

        client.get_line_item(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_list_line_items_rest_bad_request(
    request_type=line_item_service.ListLineItemsRequest,
):
    client = LineItemServiceClient(
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
        client.list_line_items(request)


@pytest.mark.parametrize(
    "request_type",
    [
        line_item_service.ListLineItemsRequest,
        dict,
    ],
)
def test_list_line_items_rest_call_success(request_type):
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = line_item_service.ListLineItemsResponse(
            next_page_token="next_page_token_value",
            total_size=1086,
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = line_item_service.ListLineItemsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.list_line_items(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, pagers.ListLineItemsPager)
    assert response.next_page_token == "next_page_token_value"
    assert response.total_size == 1086


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_list_line_items_rest_interceptors(null_interceptor):
    transport = transports.LineItemServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.LineItemServiceRestInterceptor(),
    )
    client = LineItemServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor, "post_list_line_items"
        ) as post,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor,
            "post_list_line_items_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor, "pre_list_line_items"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = line_item_service.ListLineItemsRequest.pb(
            line_item_service.ListLineItemsRequest()
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
        return_value = line_item_service.ListLineItemsResponse.to_json(
            line_item_service.ListLineItemsResponse()
        )
        req.return_value.content = return_value

        request = line_item_service.ListLineItemsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = line_item_service.ListLineItemsResponse()
        post_with_metadata.return_value = (
            line_item_service.ListLineItemsResponse(),
            metadata,
        )

        client.list_line_items(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_create_line_item_rest_bad_request(
    request_type=line_item_service.CreateLineItemRequest,
):
    client = LineItemServiceClient(
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
        client.create_line_item(request)


@pytest.mark.parametrize(
    "request_type",
    [
        line_item_service.CreateLineItemRequest,
        dict,
    ],
)
def test_create_line_item_rest_call_success(request_type):
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request_init["line_item"] = {
        "name": "name_value",
        "order": "order_value",
        "display_name": "display_name_value",
        "external_line_item_id": "external_line_item_id_value",
        "order_display_name": "order_display_name_value",
        "start_time": {"seconds": 751, "nanos": 543},
        "target_end_time": {},
        "end_time": {},
        "auto_extension_days": 2053,
        "end_time_unlimited": True,
        "creative_rotation_type": 1,
        "delivery_rate_type": 3,
        "delivery_forecast_source": 1,
        "custom_pacing_curve": {
            "custom_pacing_goal_unit": 1,
            "custom_pacing_goals": [
                {"start_time": {}, "use_line_item_start_time": True, "amount": 660}
            ],
        },
        "roadblocking_type": 1,
        "skippable_ad_type": 1,
        "frequency_caps": [
            {"max_impressions": 1633, "time_amount": 1186, "time_unit": 1}
        ],
        "line_item_type": 12,
        "priority": 898,
        "rate": {"currency_code": "currency_code_value", "units": 563, "nanos": 543},
        "value_cpm": {},
        "cost_type": 1,
        "discount": {"discount_type": 1, "discount": 0.873},
        "contracted_units_bought": 2465,
        "creative_placeholders": [
            {
                "size": {"width": 544, "height": 633, "size_type": 1},
                "companions": [{"size": {}}],
                "expected_creative_count": 2444,
                "applied_labels": [{"label": "label_value", "negated": True}],
                "amp_only": True,
                "creative_targeting_display_name": "creative_targeting_display_name_value",
            }
        ],
        "environment_type": 1,
        "companion_delivery_option": 1,
        "allow_overbook": True,
        "skip_inventory_check": True,
        "skip_cross_selling_rule_warning_checks": True,
        "reserve_on_creation": True,
        "stats": {
            "impressions_delivered": 2255,
            "clicks_delivered": 1676,
            "video_completions_delivered": 2870,
            "video_starts_delivered": 2346,
            "viewable_impressions_delivered": 3197,
            "delivery_data": [1374, 1375],
        },
        "delivery_indicator": {
            "expected_delivery_percentage": 0.2962,
            "actual_delivery_percentage": 0.2746,
        },
        "budget": {},
        "status": 1,
        "reservation_status": 1,
        "archived": True,
        "web_property_code": "web_property_code_value",
        "applied_labels": {},
        "effective_applied_labels": {},
        "same_advertiser_exception_enabled": True,
        "update_source": "update_source_value",
        "notes": "notes_value",
        "competitive_constraint_scope": 1,
        "update_time": {},
        "create_time": {},
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
        "missing_creatives": True,
        "third_party_measurement_settings": {
            "viewability_partner": 1,
            "viewability_client_id": "viewability_client_id_value",
            "viewability_reporting_id": "viewability_reporting_id_value",
            "publisher_viewability_partner": 1,
            "publisher_viewability_client_id": "publisher_viewability_client_id_value",
            "publisher_viewability_reporting_id": "publisher_viewability_reporting_id_value",
            "brand_lift_partner": 1,
            "brand_lift_client_id": "brand_lift_client_id_value",
            "brand_lift_reporting_id": "brand_lift_reporting_id_value",
            "reach_partner": 1,
            "reach_client_id": "reach_client_id_value",
            "reach_reporting_id": "reach_reporting_id_value",
            "publisher_reach_partner": 1,
            "publisher_reach_client_id": "publisher_reach_client_id_value",
            "publisher_reach_reporting_id": "publisher_reach_reporting_id_value",
        },
        "youtube_kids_restricted": True,
        "max_video_creative_duration": {"seconds": 751, "nanos": 543},
        "goal": {"goal_type": 1, "unit_type": 1, "units": 563},
        "secondary_goals": {},
        "grp_settings": {
            "min_target_age": 1462,
            "max_target_age": 1464,
            "target_gender": 1,
            "provider": 1,
            "in_target_ratio_estimate_milli_percent": 4028,
            "nielsen_ctv_pacing_type": 1,
            "pacing_device_categorization_type": 1,
            "apply_true_coview": True,
        },
        "deal_info": {"external_deal_id": 1668},
        "viewability_provider_companies": [
            "viewability_provider_companies_value1",
            "viewability_provider_companies_value2",
        ],
        "child_content_eligibility": 1,
        "custom_vast_extension": "custom_vast_extension_value",
        "sponsorship_exclusivity_enabled": True,
        "repeated_creative_serving_enabled": True,
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
        "creative_targetings": [
            {
                "creative_targeting_display_name": "creative_targeting_display_name_value",
                "targeting": {},
            }
        ],
        "allowed_formats": [1],
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = line_item_service.CreateLineItemRequest.meta.fields["line_item"]

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
    for field, value in request_init["line_item"].items():  # pragma: NO COVER
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
                for i in range(0, len(request_init["line_item"][field])):
                    del request_init["line_item"][field][i][subfield]
            else:
                del request_init["line_item"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = line_item_messages.LineItem(
            name="name_value",
            order="order_value",
            display_name="display_name_value",
            external_line_item_id="external_line_item_id_value",
            order_display_name="order_display_name_value",
            auto_extension_days=2053,
            end_time_unlimited=True,
            creative_rotation_type=delivery_enums.CreativeRotationTypeEnum.CreativeRotationType.EVENLY,
            delivery_rate_type=delivery_enums.LineItemDeliveryRateTypeEnum.LineItemDeliveryRateType.AS_FAST_AS_POSSIBLE,
            delivery_forecast_source=line_item_delivery_forecast_source_enum.LineItemDeliveryForecastSourceEnum.LineItemDeliveryForecastSource.CUSTOM_PACING_CURVE,
            roadblocking_type=delivery_enums.RoadblockingTypeEnum.RoadblockingType.ALL_ROADBLOCK,
            skippable_ad_type=skippable_ad_type_enum.SkippableAdTypeEnum.SkippableAdType.ANY,
            line_item_type=line_item_enums.LineItemTypeEnum.LineItemType.SPONSORSHIP,
            priority=898,
            cost_type=line_item_enums.LineItemCostTypeEnum.LineItemCostType.CPA,
            contracted_units_bought=2465,
            environment_type=environment_type_enum.EnvironmentTypeEnum.EnvironmentType.BROWSER,
            companion_delivery_option=delivery_enums.CompanionDeliveryOptionEnum.CompanionDeliveryOption.OPTIONAL,
            allow_overbook=True,
            skip_inventory_check=True,
            skip_cross_selling_rule_warning_checks=True,
            reserve_on_creation=True,
            status=line_item_enums.LineItemComputedStatusEnum.LineItemComputedStatus.CANCELED,
            reservation_status=line_item_enums.LineItemReservationStatusEnum.LineItemReservationStatus.RESERVED,
            archived=True,
            web_property_code="web_property_code_value",
            same_advertiser_exception_enabled=True,
            update_source="update_source_value",
            notes="notes_value",
            competitive_constraint_scope=exclusion_scope_enum.ExclusionScopeEnum.ExclusionScope.PAGE,
            missing_creatives=True,
            youtube_kids_restricted=True,
            viewability_provider_companies=["viewability_provider_companies_value"],
            child_content_eligibility=child_content_eligibility_enum.ChildContentEligibilityEnum.ChildContentEligibility.ALLOWED,
            custom_vast_extension="custom_vast_extension_value",
            sponsorship_exclusivity_enabled=True,
            repeated_creative_serving_enabled=True,
            allowed_formats=[
                line_item_allowed_format_enum.LineItemAllowedFormatEnum.LineItemAllowedFormat.AUDIO
            ],
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = line_item_messages.LineItem.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.create_line_item(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, line_item_messages.LineItem)
    assert response.name == "name_value"
    assert response.order == "order_value"
    assert response.display_name == "display_name_value"
    assert response.external_line_item_id == "external_line_item_id_value"
    assert response.order_display_name == "order_display_name_value"
    assert response.auto_extension_days == 2053
    assert response.end_time_unlimited is True
    assert (
        response.creative_rotation_type
        == delivery_enums.CreativeRotationTypeEnum.CreativeRotationType.EVENLY
    )
    assert (
        response.delivery_rate_type
        == delivery_enums.LineItemDeliveryRateTypeEnum.LineItemDeliveryRateType.AS_FAST_AS_POSSIBLE
    )
    assert (
        response.delivery_forecast_source
        == line_item_delivery_forecast_source_enum.LineItemDeliveryForecastSourceEnum.LineItemDeliveryForecastSource.CUSTOM_PACING_CURVE
    )
    assert (
        response.roadblocking_type
        == delivery_enums.RoadblockingTypeEnum.RoadblockingType.ALL_ROADBLOCK
    )
    assert (
        response.skippable_ad_type
        == skippable_ad_type_enum.SkippableAdTypeEnum.SkippableAdType.ANY
    )
    assert (
        response.line_item_type
        == line_item_enums.LineItemTypeEnum.LineItemType.SPONSORSHIP
    )
    assert response.priority == 898
    assert (
        response.cost_type == line_item_enums.LineItemCostTypeEnum.LineItemCostType.CPA
    )
    assert response.contracted_units_bought == 2465
    assert (
        response.environment_type
        == environment_type_enum.EnvironmentTypeEnum.EnvironmentType.BROWSER
    )
    assert (
        response.companion_delivery_option
        == delivery_enums.CompanionDeliveryOptionEnum.CompanionDeliveryOption.OPTIONAL
    )
    assert response.allow_overbook is True
    assert response.skip_inventory_check is True
    assert response.skip_cross_selling_rule_warning_checks is True
    assert response.reserve_on_creation is True
    assert (
        response.status
        == line_item_enums.LineItemComputedStatusEnum.LineItemComputedStatus.CANCELED
    )
    assert (
        response.reservation_status
        == line_item_enums.LineItemReservationStatusEnum.LineItemReservationStatus.RESERVED
    )
    assert response.archived is True
    assert response.web_property_code == "web_property_code_value"
    assert response.same_advertiser_exception_enabled is True
    assert response.update_source == "update_source_value"
    assert response.notes == "notes_value"
    assert (
        response.competitive_constraint_scope
        == exclusion_scope_enum.ExclusionScopeEnum.ExclusionScope.PAGE
    )
    assert response.missing_creatives is True
    assert response.youtube_kids_restricted is True
    assert response.viewability_provider_companies == [
        "viewability_provider_companies_value"
    ]
    assert (
        response.child_content_eligibility
        == child_content_eligibility_enum.ChildContentEligibilityEnum.ChildContentEligibility.ALLOWED
    )
    assert response.custom_vast_extension == "custom_vast_extension_value"
    assert response.sponsorship_exclusivity_enabled is True
    assert response.repeated_creative_serving_enabled is True
    assert response.allowed_formats == [
        line_item_allowed_format_enum.LineItemAllowedFormatEnum.LineItemAllowedFormat.AUDIO
    ]


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_create_line_item_rest_interceptors(null_interceptor):
    transport = transports.LineItemServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.LineItemServiceRestInterceptor(),
    )
    client = LineItemServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor, "post_create_line_item"
        ) as post,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor,
            "post_create_line_item_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor, "pre_create_line_item"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = line_item_service.CreateLineItemRequest.pb(
            line_item_service.CreateLineItemRequest()
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
        return_value = line_item_messages.LineItem.to_json(
            line_item_messages.LineItem()
        )
        req.return_value.content = return_value

        request = line_item_service.CreateLineItemRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = line_item_messages.LineItem()
        post_with_metadata.return_value = line_item_messages.LineItem(), metadata

        client.create_line_item(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_create_line_items_rest_bad_request(
    request_type=line_item_service.BatchCreateLineItemsRequest,
):
    client = LineItemServiceClient(
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
        client.batch_create_line_items(request)


@pytest.mark.parametrize(
    "request_type",
    [
        line_item_service.BatchCreateLineItemsRequest,
        dict,
    ],
)
def test_batch_create_line_items_rest_call_success(request_type):
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = line_item_service.BatchCreateLineItemsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = line_item_service.BatchCreateLineItemsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.batch_create_line_items(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, line_item_service.BatchCreateLineItemsResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_create_line_items_rest_interceptors(null_interceptor):
    transport = transports.LineItemServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.LineItemServiceRestInterceptor(),
    )
    client = LineItemServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor, "post_batch_create_line_items"
        ) as post,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor,
            "post_batch_create_line_items_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor, "pre_batch_create_line_items"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = line_item_service.BatchCreateLineItemsRequest.pb(
            line_item_service.BatchCreateLineItemsRequest()
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
        return_value = line_item_service.BatchCreateLineItemsResponse.to_json(
            line_item_service.BatchCreateLineItemsResponse()
        )
        req.return_value.content = return_value

        request = line_item_service.BatchCreateLineItemsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = line_item_service.BatchCreateLineItemsResponse()
        post_with_metadata.return_value = (
            line_item_service.BatchCreateLineItemsResponse(),
            metadata,
        )

        client.batch_create_line_items(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_update_line_item_rest_bad_request(
    request_type=line_item_service.UpdateLineItemRequest,
):
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    # send a request that will satisfy transcoding
    request_init = {"line_item": {"name": "networks/sample1/lineItems/sample2"}}
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
        client.update_line_item(request)


@pytest.mark.parametrize(
    "request_type",
    [
        line_item_service.UpdateLineItemRequest,
        dict,
    ],
)
def test_update_line_item_rest_call_success(request_type):
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"line_item": {"name": "networks/sample1/lineItems/sample2"}}
    request_init["line_item"] = {
        "name": "networks/sample1/lineItems/sample2",
        "order": "order_value",
        "display_name": "display_name_value",
        "external_line_item_id": "external_line_item_id_value",
        "order_display_name": "order_display_name_value",
        "start_time": {"seconds": 751, "nanos": 543},
        "target_end_time": {},
        "end_time": {},
        "auto_extension_days": 2053,
        "end_time_unlimited": True,
        "creative_rotation_type": 1,
        "delivery_rate_type": 3,
        "delivery_forecast_source": 1,
        "custom_pacing_curve": {
            "custom_pacing_goal_unit": 1,
            "custom_pacing_goals": [
                {"start_time": {}, "use_line_item_start_time": True, "amount": 660}
            ],
        },
        "roadblocking_type": 1,
        "skippable_ad_type": 1,
        "frequency_caps": [
            {"max_impressions": 1633, "time_amount": 1186, "time_unit": 1}
        ],
        "line_item_type": 12,
        "priority": 898,
        "rate": {"currency_code": "currency_code_value", "units": 563, "nanos": 543},
        "value_cpm": {},
        "cost_type": 1,
        "discount": {"discount_type": 1, "discount": 0.873},
        "contracted_units_bought": 2465,
        "creative_placeholders": [
            {
                "size": {"width": 544, "height": 633, "size_type": 1},
                "companions": [{"size": {}}],
                "expected_creative_count": 2444,
                "applied_labels": [{"label": "label_value", "negated": True}],
                "amp_only": True,
                "creative_targeting_display_name": "creative_targeting_display_name_value",
            }
        ],
        "environment_type": 1,
        "companion_delivery_option": 1,
        "allow_overbook": True,
        "skip_inventory_check": True,
        "skip_cross_selling_rule_warning_checks": True,
        "reserve_on_creation": True,
        "stats": {
            "impressions_delivered": 2255,
            "clicks_delivered": 1676,
            "video_completions_delivered": 2870,
            "video_starts_delivered": 2346,
            "viewable_impressions_delivered": 3197,
            "delivery_data": [1374, 1375],
        },
        "delivery_indicator": {
            "expected_delivery_percentage": 0.2962,
            "actual_delivery_percentage": 0.2746,
        },
        "budget": {},
        "status": 1,
        "reservation_status": 1,
        "archived": True,
        "web_property_code": "web_property_code_value",
        "applied_labels": {},
        "effective_applied_labels": {},
        "same_advertiser_exception_enabled": True,
        "update_source": "update_source_value",
        "notes": "notes_value",
        "competitive_constraint_scope": 1,
        "update_time": {},
        "create_time": {},
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
        "missing_creatives": True,
        "third_party_measurement_settings": {
            "viewability_partner": 1,
            "viewability_client_id": "viewability_client_id_value",
            "viewability_reporting_id": "viewability_reporting_id_value",
            "publisher_viewability_partner": 1,
            "publisher_viewability_client_id": "publisher_viewability_client_id_value",
            "publisher_viewability_reporting_id": "publisher_viewability_reporting_id_value",
            "brand_lift_partner": 1,
            "brand_lift_client_id": "brand_lift_client_id_value",
            "brand_lift_reporting_id": "brand_lift_reporting_id_value",
            "reach_partner": 1,
            "reach_client_id": "reach_client_id_value",
            "reach_reporting_id": "reach_reporting_id_value",
            "publisher_reach_partner": 1,
            "publisher_reach_client_id": "publisher_reach_client_id_value",
            "publisher_reach_reporting_id": "publisher_reach_reporting_id_value",
        },
        "youtube_kids_restricted": True,
        "max_video_creative_duration": {"seconds": 751, "nanos": 543},
        "goal": {"goal_type": 1, "unit_type": 1, "units": 563},
        "secondary_goals": {},
        "grp_settings": {
            "min_target_age": 1462,
            "max_target_age": 1464,
            "target_gender": 1,
            "provider": 1,
            "in_target_ratio_estimate_milli_percent": 4028,
            "nielsen_ctv_pacing_type": 1,
            "pacing_device_categorization_type": 1,
            "apply_true_coview": True,
        },
        "deal_info": {"external_deal_id": 1668},
        "viewability_provider_companies": [
            "viewability_provider_companies_value1",
            "viewability_provider_companies_value2",
        ],
        "child_content_eligibility": 1,
        "custom_vast_extension": "custom_vast_extension_value",
        "sponsorship_exclusivity_enabled": True,
        "repeated_creative_serving_enabled": True,
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
        "creative_targetings": [
            {
                "creative_targeting_display_name": "creative_targeting_display_name_value",
                "targeting": {},
            }
        ],
        "allowed_formats": [1],
    }
    # The version of a generated dependency at test runtime may differ from the version used during generation.
    # Delete any fields which are not present in the current runtime dependency
    # See https://github.com/googleapis/gapic-generator-python/issues/1748

    # Determine if the message type is proto-plus or protobuf
    test_field = line_item_service.UpdateLineItemRequest.meta.fields["line_item"]

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
    for field, value in request_init["line_item"].items():  # pragma: NO COVER
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
                for i in range(0, len(request_init["line_item"][field])):
                    del request_init["line_item"][field][i][subfield]
            else:
                del request_init["line_item"][field][subfield]
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = line_item_messages.LineItem(
            name="name_value",
            order="order_value",
            display_name="display_name_value",
            external_line_item_id="external_line_item_id_value",
            order_display_name="order_display_name_value",
            auto_extension_days=2053,
            end_time_unlimited=True,
            creative_rotation_type=delivery_enums.CreativeRotationTypeEnum.CreativeRotationType.EVENLY,
            delivery_rate_type=delivery_enums.LineItemDeliveryRateTypeEnum.LineItemDeliveryRateType.AS_FAST_AS_POSSIBLE,
            delivery_forecast_source=line_item_delivery_forecast_source_enum.LineItemDeliveryForecastSourceEnum.LineItemDeliveryForecastSource.CUSTOM_PACING_CURVE,
            roadblocking_type=delivery_enums.RoadblockingTypeEnum.RoadblockingType.ALL_ROADBLOCK,
            skippable_ad_type=skippable_ad_type_enum.SkippableAdTypeEnum.SkippableAdType.ANY,
            line_item_type=line_item_enums.LineItemTypeEnum.LineItemType.SPONSORSHIP,
            priority=898,
            cost_type=line_item_enums.LineItemCostTypeEnum.LineItemCostType.CPA,
            contracted_units_bought=2465,
            environment_type=environment_type_enum.EnvironmentTypeEnum.EnvironmentType.BROWSER,
            companion_delivery_option=delivery_enums.CompanionDeliveryOptionEnum.CompanionDeliveryOption.OPTIONAL,
            allow_overbook=True,
            skip_inventory_check=True,
            skip_cross_selling_rule_warning_checks=True,
            reserve_on_creation=True,
            status=line_item_enums.LineItemComputedStatusEnum.LineItemComputedStatus.CANCELED,
            reservation_status=line_item_enums.LineItemReservationStatusEnum.LineItemReservationStatus.RESERVED,
            archived=True,
            web_property_code="web_property_code_value",
            same_advertiser_exception_enabled=True,
            update_source="update_source_value",
            notes="notes_value",
            competitive_constraint_scope=exclusion_scope_enum.ExclusionScopeEnum.ExclusionScope.PAGE,
            missing_creatives=True,
            youtube_kids_restricted=True,
            viewability_provider_companies=["viewability_provider_companies_value"],
            child_content_eligibility=child_content_eligibility_enum.ChildContentEligibilityEnum.ChildContentEligibility.ALLOWED,
            custom_vast_extension="custom_vast_extension_value",
            sponsorship_exclusivity_enabled=True,
            repeated_creative_serving_enabled=True,
            allowed_formats=[
                line_item_allowed_format_enum.LineItemAllowedFormatEnum.LineItemAllowedFormat.AUDIO
            ],
        )

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = line_item_messages.LineItem.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.update_line_item(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, line_item_messages.LineItem)
    assert response.name == "name_value"
    assert response.order == "order_value"
    assert response.display_name == "display_name_value"
    assert response.external_line_item_id == "external_line_item_id_value"
    assert response.order_display_name == "order_display_name_value"
    assert response.auto_extension_days == 2053
    assert response.end_time_unlimited is True
    assert (
        response.creative_rotation_type
        == delivery_enums.CreativeRotationTypeEnum.CreativeRotationType.EVENLY
    )
    assert (
        response.delivery_rate_type
        == delivery_enums.LineItemDeliveryRateTypeEnum.LineItemDeliveryRateType.AS_FAST_AS_POSSIBLE
    )
    assert (
        response.delivery_forecast_source
        == line_item_delivery_forecast_source_enum.LineItemDeliveryForecastSourceEnum.LineItemDeliveryForecastSource.CUSTOM_PACING_CURVE
    )
    assert (
        response.roadblocking_type
        == delivery_enums.RoadblockingTypeEnum.RoadblockingType.ALL_ROADBLOCK
    )
    assert (
        response.skippable_ad_type
        == skippable_ad_type_enum.SkippableAdTypeEnum.SkippableAdType.ANY
    )
    assert (
        response.line_item_type
        == line_item_enums.LineItemTypeEnum.LineItemType.SPONSORSHIP
    )
    assert response.priority == 898
    assert (
        response.cost_type == line_item_enums.LineItemCostTypeEnum.LineItemCostType.CPA
    )
    assert response.contracted_units_bought == 2465
    assert (
        response.environment_type
        == environment_type_enum.EnvironmentTypeEnum.EnvironmentType.BROWSER
    )
    assert (
        response.companion_delivery_option
        == delivery_enums.CompanionDeliveryOptionEnum.CompanionDeliveryOption.OPTIONAL
    )
    assert response.allow_overbook is True
    assert response.skip_inventory_check is True
    assert response.skip_cross_selling_rule_warning_checks is True
    assert response.reserve_on_creation is True
    assert (
        response.status
        == line_item_enums.LineItemComputedStatusEnum.LineItemComputedStatus.CANCELED
    )
    assert (
        response.reservation_status
        == line_item_enums.LineItemReservationStatusEnum.LineItemReservationStatus.RESERVED
    )
    assert response.archived is True
    assert response.web_property_code == "web_property_code_value"
    assert response.same_advertiser_exception_enabled is True
    assert response.update_source == "update_source_value"
    assert response.notes == "notes_value"
    assert (
        response.competitive_constraint_scope
        == exclusion_scope_enum.ExclusionScopeEnum.ExclusionScope.PAGE
    )
    assert response.missing_creatives is True
    assert response.youtube_kids_restricted is True
    assert response.viewability_provider_companies == [
        "viewability_provider_companies_value"
    ]
    assert (
        response.child_content_eligibility
        == child_content_eligibility_enum.ChildContentEligibilityEnum.ChildContentEligibility.ALLOWED
    )
    assert response.custom_vast_extension == "custom_vast_extension_value"
    assert response.sponsorship_exclusivity_enabled is True
    assert response.repeated_creative_serving_enabled is True
    assert response.allowed_formats == [
        line_item_allowed_format_enum.LineItemAllowedFormatEnum.LineItemAllowedFormat.AUDIO
    ]


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_update_line_item_rest_interceptors(null_interceptor):
    transport = transports.LineItemServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.LineItemServiceRestInterceptor(),
    )
    client = LineItemServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor, "post_update_line_item"
        ) as post,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor,
            "post_update_line_item_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor, "pre_update_line_item"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = line_item_service.UpdateLineItemRequest.pb(
            line_item_service.UpdateLineItemRequest()
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
        return_value = line_item_messages.LineItem.to_json(
            line_item_messages.LineItem()
        )
        req.return_value.content = return_value

        request = line_item_service.UpdateLineItemRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = line_item_messages.LineItem()
        post_with_metadata.return_value = line_item_messages.LineItem(), metadata

        client.update_line_item(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_update_line_items_rest_bad_request(
    request_type=line_item_service.BatchUpdateLineItemsRequest,
):
    client = LineItemServiceClient(
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
        client.batch_update_line_items(request)


@pytest.mark.parametrize(
    "request_type",
    [
        line_item_service.BatchUpdateLineItemsRequest,
        dict,
    ],
)
def test_batch_update_line_items_rest_call_success(request_type):
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = line_item_service.BatchUpdateLineItemsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = line_item_service.BatchUpdateLineItemsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.batch_update_line_items(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, line_item_service.BatchUpdateLineItemsResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_update_line_items_rest_interceptors(null_interceptor):
    transport = transports.LineItemServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.LineItemServiceRestInterceptor(),
    )
    client = LineItemServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor, "post_batch_update_line_items"
        ) as post,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor,
            "post_batch_update_line_items_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor, "pre_batch_update_line_items"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = line_item_service.BatchUpdateLineItemsRequest.pb(
            line_item_service.BatchUpdateLineItemsRequest()
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
        return_value = line_item_service.BatchUpdateLineItemsResponse.to_json(
            line_item_service.BatchUpdateLineItemsResponse()
        )
        req.return_value.content = return_value

        request = line_item_service.BatchUpdateLineItemsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = line_item_service.BatchUpdateLineItemsResponse()
        post_with_metadata.return_value = (
            line_item_service.BatchUpdateLineItemsResponse(),
            metadata,
        )

        client.batch_update_line_items(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_activate_line_items_rest_bad_request(
    request_type=line_item_service.BatchActivateLineItemsRequest,
):
    client = LineItemServiceClient(
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
        client.batch_activate_line_items(request)


@pytest.mark.parametrize(
    "request_type",
    [
        line_item_service.BatchActivateLineItemsRequest,
        dict,
    ],
)
def test_batch_activate_line_items_rest_call_success(request_type):
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = line_item_service.BatchActivateLineItemsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = line_item_service.BatchActivateLineItemsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.batch_activate_line_items(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, line_item_service.BatchActivateLineItemsResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_activate_line_items_rest_interceptors(null_interceptor):
    transport = transports.LineItemServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.LineItemServiceRestInterceptor(),
    )
    client = LineItemServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor, "post_batch_activate_line_items"
        ) as post,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor,
            "post_batch_activate_line_items_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor, "pre_batch_activate_line_items"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = line_item_service.BatchActivateLineItemsRequest.pb(
            line_item_service.BatchActivateLineItemsRequest()
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
        return_value = line_item_service.BatchActivateLineItemsResponse.to_json(
            line_item_service.BatchActivateLineItemsResponse()
        )
        req.return_value.content = return_value

        request = line_item_service.BatchActivateLineItemsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = line_item_service.BatchActivateLineItemsResponse()
        post_with_metadata.return_value = (
            line_item_service.BatchActivateLineItemsResponse(),
            metadata,
        )

        client.batch_activate_line_items(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_pause_line_items_rest_bad_request(
    request_type=line_item_service.BatchPauseLineItemsRequest,
):
    client = LineItemServiceClient(
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
        client.batch_pause_line_items(request)


@pytest.mark.parametrize(
    "request_type",
    [
        line_item_service.BatchPauseLineItemsRequest,
        dict,
    ],
)
def test_batch_pause_line_items_rest_call_success(request_type):
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = line_item_service.BatchPauseLineItemsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = line_item_service.BatchPauseLineItemsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.batch_pause_line_items(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, line_item_service.BatchPauseLineItemsResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_pause_line_items_rest_interceptors(null_interceptor):
    transport = transports.LineItemServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.LineItemServiceRestInterceptor(),
    )
    client = LineItemServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor, "post_batch_pause_line_items"
        ) as post,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor,
            "post_batch_pause_line_items_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor, "pre_batch_pause_line_items"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = line_item_service.BatchPauseLineItemsRequest.pb(
            line_item_service.BatchPauseLineItemsRequest()
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
        return_value = line_item_service.BatchPauseLineItemsResponse.to_json(
            line_item_service.BatchPauseLineItemsResponse()
        )
        req.return_value.content = return_value

        request = line_item_service.BatchPauseLineItemsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = line_item_service.BatchPauseLineItemsResponse()
        post_with_metadata.return_value = (
            line_item_service.BatchPauseLineItemsResponse(),
            metadata,
        )

        client.batch_pause_line_items(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_resume_line_items_rest_bad_request(
    request_type=line_item_service.BatchResumeLineItemsRequest,
):
    client = LineItemServiceClient(
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
        client.batch_resume_line_items(request)


@pytest.mark.parametrize(
    "request_type",
    [
        line_item_service.BatchResumeLineItemsRequest,
        dict,
    ],
)
def test_batch_resume_line_items_rest_call_success(request_type):
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = line_item_service.BatchResumeLineItemsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = line_item_service.BatchResumeLineItemsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.batch_resume_line_items(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, line_item_service.BatchResumeLineItemsResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_resume_line_items_rest_interceptors(null_interceptor):
    transport = transports.LineItemServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.LineItemServiceRestInterceptor(),
    )
    client = LineItemServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor, "post_batch_resume_line_items"
        ) as post,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor,
            "post_batch_resume_line_items_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor, "pre_batch_resume_line_items"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = line_item_service.BatchResumeLineItemsRequest.pb(
            line_item_service.BatchResumeLineItemsRequest()
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
        return_value = line_item_service.BatchResumeLineItemsResponse.to_json(
            line_item_service.BatchResumeLineItemsResponse()
        )
        req.return_value.content = return_value

        request = line_item_service.BatchResumeLineItemsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = line_item_service.BatchResumeLineItemsResponse()
        post_with_metadata.return_value = (
            line_item_service.BatchResumeLineItemsResponse(),
            metadata,
        )

        client.batch_resume_line_items(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_resume_and_overbook_line_items_rest_bad_request(
    request_type=line_item_service.BatchResumeAndOverbookLineItemsRequest,
):
    client = LineItemServiceClient(
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
        client.batch_resume_and_overbook_line_items(request)


@pytest.mark.parametrize(
    "request_type",
    [
        line_item_service.BatchResumeAndOverbookLineItemsRequest,
        dict,
    ],
)
def test_batch_resume_and_overbook_line_items_rest_call_success(request_type):
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = line_item_service.BatchResumeAndOverbookLineItemsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = line_item_service.BatchResumeAndOverbookLineItemsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.batch_resume_and_overbook_line_items(request)

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, line_item_service.BatchResumeAndOverbookLineItemsResponse
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_resume_and_overbook_line_items_rest_interceptors(null_interceptor):
    transport = transports.LineItemServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.LineItemServiceRestInterceptor(),
    )
    client = LineItemServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor,
            "post_batch_resume_and_overbook_line_items",
        ) as post,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor,
            "post_batch_resume_and_overbook_line_items_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor,
            "pre_batch_resume_and_overbook_line_items",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = line_item_service.BatchResumeAndOverbookLineItemsRequest.pb(
            line_item_service.BatchResumeAndOverbookLineItemsRequest()
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
            line_item_service.BatchResumeAndOverbookLineItemsResponse.to_json(
                line_item_service.BatchResumeAndOverbookLineItemsResponse()
            )
        )
        req.return_value.content = return_value

        request = line_item_service.BatchResumeAndOverbookLineItemsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = line_item_service.BatchResumeAndOverbookLineItemsResponse()
        post_with_metadata.return_value = (
            line_item_service.BatchResumeAndOverbookLineItemsResponse(),
            metadata,
        )

        client.batch_resume_and_overbook_line_items(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_delete_line_items_rest_bad_request(
    request_type=line_item_service.BatchDeleteLineItemsRequest,
):
    client = LineItemServiceClient(
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
        client.batch_delete_line_items(request)


@pytest.mark.parametrize(
    "request_type",
    [
        line_item_service.BatchDeleteLineItemsRequest,
        dict,
    ],
)
def test_batch_delete_line_items_rest_call_success(request_type):
    client = LineItemServiceClient(
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
        response = client.batch_delete_line_items(request)

    # Establish that the response is the type that we expect.
    assert response is None


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_delete_line_items_rest_interceptors(null_interceptor):
    transport = transports.LineItemServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.LineItemServiceRestInterceptor(),
    )
    client = LineItemServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor, "pre_batch_delete_line_items"
        ) as pre,
    ):
        pre.assert_not_called()
        pb_message = line_item_service.BatchDeleteLineItemsRequest.pb(
            line_item_service.BatchDeleteLineItemsRequest()
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

        request = line_item_service.BatchDeleteLineItemsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata

        client.batch_delete_line_items(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()


def test_batch_reserve_line_items_rest_bad_request(
    request_type=line_item_service.BatchReserveLineItemsRequest,
):
    client = LineItemServiceClient(
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
        client.batch_reserve_line_items(request)


@pytest.mark.parametrize(
    "request_type",
    [
        line_item_service.BatchReserveLineItemsRequest,
        dict,
    ],
)
def test_batch_reserve_line_items_rest_call_success(request_type):
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = line_item_service.BatchReserveLineItemsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = line_item_service.BatchReserveLineItemsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.batch_reserve_line_items(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, line_item_service.BatchReserveLineItemsResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_reserve_line_items_rest_interceptors(null_interceptor):
    transport = transports.LineItemServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.LineItemServiceRestInterceptor(),
    )
    client = LineItemServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor, "post_batch_reserve_line_items"
        ) as post,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor,
            "post_batch_reserve_line_items_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor, "pre_batch_reserve_line_items"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = line_item_service.BatchReserveLineItemsRequest.pb(
            line_item_service.BatchReserveLineItemsRequest()
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
        return_value = line_item_service.BatchReserveLineItemsResponse.to_json(
            line_item_service.BatchReserveLineItemsResponse()
        )
        req.return_value.content = return_value

        request = line_item_service.BatchReserveLineItemsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = line_item_service.BatchReserveLineItemsResponse()
        post_with_metadata.return_value = (
            line_item_service.BatchReserveLineItemsResponse(),
            metadata,
        )

        client.batch_reserve_line_items(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_reserve_and_overbook_line_items_rest_bad_request(
    request_type=line_item_service.BatchReserveAndOverbookLineItemsRequest,
):
    client = LineItemServiceClient(
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
        client.batch_reserve_and_overbook_line_items(request)


@pytest.mark.parametrize(
    "request_type",
    [
        line_item_service.BatchReserveAndOverbookLineItemsRequest,
        dict,
    ],
)
def test_batch_reserve_and_overbook_line_items_rest_call_success(request_type):
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = line_item_service.BatchReserveAndOverbookLineItemsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = line_item_service.BatchReserveAndOverbookLineItemsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.batch_reserve_and_overbook_line_items(request)

    # Establish that the response is the type that we expect.
    assert isinstance(
        response, line_item_service.BatchReserveAndOverbookLineItemsResponse
    )


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_reserve_and_overbook_line_items_rest_interceptors(null_interceptor):
    transport = transports.LineItemServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.LineItemServiceRestInterceptor(),
    )
    client = LineItemServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor,
            "post_batch_reserve_and_overbook_line_items",
        ) as post,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor,
            "post_batch_reserve_and_overbook_line_items_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor,
            "pre_batch_reserve_and_overbook_line_items",
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = line_item_service.BatchReserveAndOverbookLineItemsRequest.pb(
            line_item_service.BatchReserveAndOverbookLineItemsRequest()
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
            line_item_service.BatchReserveAndOverbookLineItemsResponse.to_json(
                line_item_service.BatchReserveAndOverbookLineItemsResponse()
            )
        )
        req.return_value.content = return_value

        request = line_item_service.BatchReserveAndOverbookLineItemsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = line_item_service.BatchReserveAndOverbookLineItemsResponse()
        post_with_metadata.return_value = (
            line_item_service.BatchReserveAndOverbookLineItemsResponse(),
            metadata,
        )

        client.batch_reserve_and_overbook_line_items(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_release_line_items_rest_bad_request(
    request_type=line_item_service.BatchReleaseLineItemsRequest,
):
    client = LineItemServiceClient(
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
        client.batch_release_line_items(request)


@pytest.mark.parametrize(
    "request_type",
    [
        line_item_service.BatchReleaseLineItemsRequest,
        dict,
    ],
)
def test_batch_release_line_items_rest_call_success(request_type):
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = line_item_service.BatchReleaseLineItemsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = line_item_service.BatchReleaseLineItemsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.batch_release_line_items(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, line_item_service.BatchReleaseLineItemsResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_release_line_items_rest_interceptors(null_interceptor):
    transport = transports.LineItemServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.LineItemServiceRestInterceptor(),
    )
    client = LineItemServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor, "post_batch_release_line_items"
        ) as post,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor,
            "post_batch_release_line_items_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor, "pre_batch_release_line_items"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = line_item_service.BatchReleaseLineItemsRequest.pb(
            line_item_service.BatchReleaseLineItemsRequest()
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
        return_value = line_item_service.BatchReleaseLineItemsResponse.to_json(
            line_item_service.BatchReleaseLineItemsResponse()
        )
        req.return_value.content = return_value

        request = line_item_service.BatchReleaseLineItemsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = line_item_service.BatchReleaseLineItemsResponse()
        post_with_metadata.return_value = (
            line_item_service.BatchReleaseLineItemsResponse(),
            metadata,
        )

        client.batch_release_line_items(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_archive_line_items_rest_bad_request(
    request_type=line_item_service.BatchArchiveLineItemsRequest,
):
    client = LineItemServiceClient(
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
        client.batch_archive_line_items(request)


@pytest.mark.parametrize(
    "request_type",
    [
        line_item_service.BatchArchiveLineItemsRequest,
        dict,
    ],
)
def test_batch_archive_line_items_rest_call_success(request_type):
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = line_item_service.BatchArchiveLineItemsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = line_item_service.BatchArchiveLineItemsResponse.pb(return_value)
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.batch_archive_line_items(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, line_item_service.BatchArchiveLineItemsResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_archive_line_items_rest_interceptors(null_interceptor):
    transport = transports.LineItemServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.LineItemServiceRestInterceptor(),
    )
    client = LineItemServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor, "post_batch_archive_line_items"
        ) as post,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor,
            "post_batch_archive_line_items_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor, "pre_batch_archive_line_items"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = line_item_service.BatchArchiveLineItemsRequest.pb(
            line_item_service.BatchArchiveLineItemsRequest()
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
        return_value = line_item_service.BatchArchiveLineItemsResponse.to_json(
            line_item_service.BatchArchiveLineItemsResponse()
        )
        req.return_value.content = return_value

        request = line_item_service.BatchArchiveLineItemsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = line_item_service.BatchArchiveLineItemsResponse()
        post_with_metadata.return_value = (
            line_item_service.BatchArchiveLineItemsResponse(),
            metadata,
        )

        client.batch_archive_line_items(
            request,
            metadata=[
                ("key", "val"),
                ("cephalopod", "squid"),
            ],
        )

        pre.assert_called_once()
        post.assert_called_once()
        post_with_metadata.assert_called_once()


def test_batch_unarchive_line_items_rest_bad_request(
    request_type=line_item_service.BatchUnarchiveLineItemsRequest,
):
    client = LineItemServiceClient(
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
        client.batch_unarchive_line_items(request)


@pytest.mark.parametrize(
    "request_type",
    [
        line_item_service.BatchUnarchiveLineItemsRequest,
        dict,
    ],
)
def test_batch_unarchive_line_items_rest_call_success(request_type):
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )

    # send a request that will satisfy transcoding
    request_init = {"parent": "networks/sample1"}
    request = request_type(**request_init)

    # Mock the http request call within the method and fake a response.
    with mock.patch.object(type(client.transport._session), "request") as req:
        # Designate an appropriate value for the returned response.
        return_value = line_item_service.BatchUnarchiveLineItemsResponse()

        # Wrap the value into a proper Response obj
        response_value = mock.Mock()
        response_value.status_code = 200

        # Convert return value to protobuf type
        return_value = line_item_service.BatchUnarchiveLineItemsResponse.pb(
            return_value
        )
        json_return_value = json_format.MessageToJson(return_value)
        response_value.content = json_return_value.encode("UTF-8")
        req.return_value = response_value
        req.return_value.headers = {"header-1": "value-1", "header-2": "value-2"}
        response = client.batch_unarchive_line_items(request)

    # Establish that the response is the type that we expect.
    assert isinstance(response, line_item_service.BatchUnarchiveLineItemsResponse)


@pytest.mark.parametrize("null_interceptor", [True, False])
def test_batch_unarchive_line_items_rest_interceptors(null_interceptor):
    transport = transports.LineItemServiceRestTransport(
        credentials=ga_credentials.AnonymousCredentials(),
        interceptor=None
        if null_interceptor
        else transports.LineItemServiceRestInterceptor(),
    )
    client = LineItemServiceClient(transport=transport)

    with (
        mock.patch.object(type(client.transport._session), "request") as req,
        mock.patch.object(path_template, "transcode") as transcode,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor, "post_batch_unarchive_line_items"
        ) as post,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor,
            "post_batch_unarchive_line_items_with_metadata",
        ) as post_with_metadata,
        mock.patch.object(
            transports.LineItemServiceRestInterceptor, "pre_batch_unarchive_line_items"
        ) as pre,
    ):
        pre.assert_not_called()
        post.assert_not_called()
        post_with_metadata.assert_not_called()
        pb_message = line_item_service.BatchUnarchiveLineItemsRequest.pb(
            line_item_service.BatchUnarchiveLineItemsRequest()
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
        return_value = line_item_service.BatchUnarchiveLineItemsResponse.to_json(
            line_item_service.BatchUnarchiveLineItemsResponse()
        )
        req.return_value.content = return_value

        request = line_item_service.BatchUnarchiveLineItemsRequest()
        metadata = [
            ("key", "val"),
            ("cephalopod", "squid"),
        ]
        pre.return_value = request, metadata
        post.return_value = line_item_service.BatchUnarchiveLineItemsResponse()
        post_with_metadata.return_value = (
            line_item_service.BatchUnarchiveLineItemsResponse(),
            metadata,
        )

        client.batch_unarchive_line_items(
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
    client = LineItemServiceClient(
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
    client = LineItemServiceClient(
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
    client = LineItemServiceClient(
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
    client = LineItemServiceClient(
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
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(), transport="rest"
    )
    assert client is not None


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_get_line_item_empty_call_rest():
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.get_line_item), "__call__") as call:
        client.get_line_item(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = line_item_service.GetLineItemRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_list_line_items_empty_call_rest():
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.list_line_items), "__call__") as call:
        client.list_line_items(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = line_item_service.ListLineItemsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_create_line_item_empty_call_rest():
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.create_line_item), "__call__") as call:
        client.create_line_item(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = line_item_service.CreateLineItemRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_create_line_items_empty_call_rest():
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_create_line_items), "__call__"
    ) as call:
        client.batch_create_line_items(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = line_item_service.BatchCreateLineItemsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_update_line_item_empty_call_rest():
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(type(client.transport.update_line_item), "__call__") as call:
        client.update_line_item(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = line_item_service.UpdateLineItemRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_update_line_items_empty_call_rest():
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_update_line_items), "__call__"
    ) as call:
        client.batch_update_line_items(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = line_item_service.BatchUpdateLineItemsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_activate_line_items_empty_call_rest():
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_activate_line_items), "__call__"
    ) as call:
        client.batch_activate_line_items(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = line_item_service.BatchActivateLineItemsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_pause_line_items_empty_call_rest():
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_pause_line_items), "__call__"
    ) as call:
        client.batch_pause_line_items(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = line_item_service.BatchPauseLineItemsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_resume_line_items_empty_call_rest():
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_resume_line_items), "__call__"
    ) as call:
        client.batch_resume_line_items(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = line_item_service.BatchResumeLineItemsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_resume_and_overbook_line_items_empty_call_rest():
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_resume_and_overbook_line_items), "__call__"
    ) as call:
        client.batch_resume_and_overbook_line_items(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = line_item_service.BatchResumeAndOverbookLineItemsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_delete_line_items_empty_call_rest():
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_delete_line_items), "__call__"
    ) as call:
        client.batch_delete_line_items(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = line_item_service.BatchDeleteLineItemsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_reserve_line_items_empty_call_rest():
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_reserve_line_items), "__call__"
    ) as call:
        client.batch_reserve_line_items(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = line_item_service.BatchReserveLineItemsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_reserve_and_overbook_line_items_empty_call_rest():
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_reserve_and_overbook_line_items), "__call__"
    ) as call:
        client.batch_reserve_and_overbook_line_items(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = line_item_service.BatchReserveAndOverbookLineItemsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_release_line_items_empty_call_rest():
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_release_line_items), "__call__"
    ) as call:
        client.batch_release_line_items(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = line_item_service.BatchReleaseLineItemsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_archive_line_items_empty_call_rest():
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_archive_line_items), "__call__"
    ) as call:
        client.batch_archive_line_items(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = line_item_service.BatchArchiveLineItemsRequest()
        assert args[0] == request_msg


# This test is a coverage failsafe to make sure that totally empty calls,
# i.e. request == None and no flattened fields passed, work.
def test_batch_unarchive_line_items_empty_call_rest():
    client = LineItemServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        transport="rest",
    )

    # Mock the actual call, and fake the request.
    with mock.patch.object(
        type(client.transport.batch_unarchive_line_items), "__call__"
    ) as call:
        client.batch_unarchive_line_items(request=None)

        # Establish that the underlying stub method was called.
        call.assert_called()
        _, args, _ = call.mock_calls[0]
        request_msg = line_item_service.BatchUnarchiveLineItemsRequest()
        assert args[0] == request_msg


def test_line_item_service_base_transport_error():
    # Passing both a credentials object and credentials_file should raise an error
    with pytest.raises(core_exceptions.DuplicateCredentialArgs):
        transport = transports.LineItemServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
            credentials_file="credentials.json",
        )


def test_line_item_service_base_transport():
    # Instantiate the base transport.
    with mock.patch(
        "google.ads.admanager_v1.services.line_item_service.transports.LineItemServiceTransport.__init__"
    ) as Transport:
        Transport.return_value = None
        transport = transports.LineItemServiceTransport(
            credentials=ga_credentials.AnonymousCredentials(),
        )

    # Every method on the transport should just blindly
    # raise NotImplementedError.
    methods = (
        "get_line_item",
        "list_line_items",
        "create_line_item",
        "batch_create_line_items",
        "update_line_item",
        "batch_update_line_items",
        "batch_activate_line_items",
        "batch_pause_line_items",
        "batch_resume_line_items",
        "batch_resume_and_overbook_line_items",
        "batch_delete_line_items",
        "batch_reserve_line_items",
        "batch_reserve_and_overbook_line_items",
        "batch_release_line_items",
        "batch_archive_line_items",
        "batch_unarchive_line_items",
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


def test_line_item_service_base_transport_with_credentials_file():
    # Instantiate the base transport with a credentials file
    with (
        mock.patch.object(
            google.auth, "load_credentials_from_file", autospec=True
        ) as load_creds,
        mock.patch(
            "google.ads.admanager_v1.services.line_item_service.transports.LineItemServiceTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        load_creds.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.LineItemServiceTransport(
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


def test_line_item_service_base_transport_with_adc():
    # Test the default credentials are used if credentials and credentials_file are None.
    with (
        mock.patch.object(google.auth, "default", autospec=True) as adc,
        mock.patch(
            "google.ads.admanager_v1.services.line_item_service.transports.LineItemServiceTransport._prep_wrapped_messages"
        ) as Transport,
    ):
        Transport.return_value = None
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        transport = transports.LineItemServiceTransport()
        adc.assert_called_once()


def test_line_item_service_auth_adc():
    # If no credentials are provided, we should use ADC credentials.
    with mock.patch.object(google.auth, "default", autospec=True) as adc:
        adc.return_value = (ga_credentials.AnonymousCredentials(), None)
        LineItemServiceClient()
        adc.assert_called_once_with(
            scopes=None,
            default_scopes=(
                "https://www.googleapis.com/auth/admanager",
                "https://www.googleapis.com/auth/admanager.readonly",
            ),
            quota_project_id=None,
        )


def test_line_item_service_http_transport_client_cert_source_for_mtls():
    cred = ga_credentials.AnonymousCredentials()
    with mock.patch(
        "google.auth.transport.requests.AuthorizedSession.configure_mtls_channel"
    ) as mock_configure_mtls_channel:
        transports.LineItemServiceRestTransport(
            credentials=cred, client_cert_source_for_mtls=client_cert_source_callback
        )
        mock_configure_mtls_channel.assert_called_once_with(client_cert_source_callback)


@pytest.mark.parametrize(
    "transport_name",
    [
        "rest",
    ],
)
def test_line_item_service_host_no_port(transport_name):
    client = LineItemServiceClient(
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
def test_line_item_service_host_with_port(transport_name):
    client = LineItemServiceClient(
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
def test_line_item_service_client_transport_session_collision(transport_name):
    creds1 = ga_credentials.AnonymousCredentials()
    creds2 = ga_credentials.AnonymousCredentials()
    client1 = LineItemServiceClient(
        credentials=creds1,
        transport=transport_name,
    )
    client2 = LineItemServiceClient(
        credentials=creds2,
        transport=transport_name,
    )
    session1 = client1.transport.get_line_item._session
    session2 = client2.transport.get_line_item._session
    assert session1 != session2
    session1 = client1.transport.list_line_items._session
    session2 = client2.transport.list_line_items._session
    assert session1 != session2
    session1 = client1.transport.create_line_item._session
    session2 = client2.transport.create_line_item._session
    assert session1 != session2
    session1 = client1.transport.batch_create_line_items._session
    session2 = client2.transport.batch_create_line_items._session
    assert session1 != session2
    session1 = client1.transport.update_line_item._session
    session2 = client2.transport.update_line_item._session
    assert session1 != session2
    session1 = client1.transport.batch_update_line_items._session
    session2 = client2.transport.batch_update_line_items._session
    assert session1 != session2
    session1 = client1.transport.batch_activate_line_items._session
    session2 = client2.transport.batch_activate_line_items._session
    assert session1 != session2
    session1 = client1.transport.batch_pause_line_items._session
    session2 = client2.transport.batch_pause_line_items._session
    assert session1 != session2
    session1 = client1.transport.batch_resume_line_items._session
    session2 = client2.transport.batch_resume_line_items._session
    assert session1 != session2
    session1 = client1.transport.batch_resume_and_overbook_line_items._session
    session2 = client2.transport.batch_resume_and_overbook_line_items._session
    assert session1 != session2
    session1 = client1.transport.batch_delete_line_items._session
    session2 = client2.transport.batch_delete_line_items._session
    assert session1 != session2
    session1 = client1.transport.batch_reserve_line_items._session
    session2 = client2.transport.batch_reserve_line_items._session
    assert session1 != session2
    session1 = client1.transport.batch_reserve_and_overbook_line_items._session
    session2 = client2.transport.batch_reserve_and_overbook_line_items._session
    assert session1 != session2
    session1 = client1.transport.batch_release_line_items._session
    session2 = client2.transport.batch_release_line_items._session
    assert session1 != session2
    session1 = client1.transport.batch_archive_line_items._session
    session2 = client2.transport.batch_archive_line_items._session
    assert session1 != session2
    session1 = client1.transport.batch_unarchive_line_items._session
    session2 = client2.transport.batch_unarchive_line_items._session
    assert session1 != session2


def test_ad_unit_path():
    network_code = "squid"
    ad_unit = "clam"
    expected = "networks/{network_code}/adUnits/{ad_unit}".format(
        network_code=network_code,
        ad_unit=ad_unit,
    )
    actual = LineItemServiceClient.ad_unit_path(network_code, ad_unit)
    assert expected == actual


def test_parse_ad_unit_path():
    expected = {
        "network_code": "whelk",
        "ad_unit": "octopus",
    }
    path = LineItemServiceClient.ad_unit_path(**expected)

    # Check that the path construction is reversible.
    actual = LineItemServiceClient.parse_ad_unit_path(path)
    assert expected == actual


def test_application_path():
    network_code = "oyster"
    application = "nudibranch"
    expected = "networks/{network_code}/applications/{application}".format(
        network_code=network_code,
        application=application,
    )
    actual = LineItemServiceClient.application_path(network_code, application)
    assert expected == actual


def test_parse_application_path():
    expected = {
        "network_code": "cuttlefish",
        "application": "mussel",
    }
    path = LineItemServiceClient.application_path(**expected)

    # Check that the path construction is reversible.
    actual = LineItemServiceClient.parse_application_path(path)
    assert expected == actual


def test_audience_segment_path():
    network_code = "winkle"
    audience_segment = "nautilus"
    expected = "networks/{network_code}/audienceSegments/{audience_segment}".format(
        network_code=network_code,
        audience_segment=audience_segment,
    )
    actual = LineItemServiceClient.audience_segment_path(network_code, audience_segment)
    assert expected == actual


def test_parse_audience_segment_path():
    expected = {
        "network_code": "scallop",
        "audience_segment": "abalone",
    }
    path = LineItemServiceClient.audience_segment_path(**expected)

    # Check that the path construction is reversible.
    actual = LineItemServiceClient.parse_audience_segment_path(path)
    assert expected == actual


def test_bandwidth_group_path():
    network_code = "squid"
    bandwidth_group = "clam"
    expected = "networks/{network_code}/bandwidthGroups/{bandwidth_group}".format(
        network_code=network_code,
        bandwidth_group=bandwidth_group,
    )
    actual = LineItemServiceClient.bandwidth_group_path(network_code, bandwidth_group)
    assert expected == actual


def test_parse_bandwidth_group_path():
    expected = {
        "network_code": "whelk",
        "bandwidth_group": "octopus",
    }
    path = LineItemServiceClient.bandwidth_group_path(**expected)

    # Check that the path construction is reversible.
    actual = LineItemServiceClient.parse_bandwidth_group_path(path)
    assert expected == actual


def test_browser_path():
    network_code = "oyster"
    browser = "nudibranch"
    expected = "networks/{network_code}/browsers/{browser}".format(
        network_code=network_code,
        browser=browser,
    )
    actual = LineItemServiceClient.browser_path(network_code, browser)
    assert expected == actual


def test_parse_browser_path():
    expected = {
        "network_code": "cuttlefish",
        "browser": "mussel",
    }
    path = LineItemServiceClient.browser_path(**expected)

    # Check that the path construction is reversible.
    actual = LineItemServiceClient.parse_browser_path(path)
    assert expected == actual


def test_browser_language_path():
    network_code = "winkle"
    browser_language = "nautilus"
    expected = "networks/{network_code}/browserLanguages/{browser_language}".format(
        network_code=network_code,
        browser_language=browser_language,
    )
    actual = LineItemServiceClient.browser_language_path(network_code, browser_language)
    assert expected == actual


def test_parse_browser_language_path():
    expected = {
        "network_code": "scallop",
        "browser_language": "abalone",
    }
    path = LineItemServiceClient.browser_language_path(**expected)

    # Check that the path construction is reversible.
    actual = LineItemServiceClient.parse_browser_language_path(path)
    assert expected == actual


def test_cms_metadata_value_path():
    network_code = "squid"
    cms_metadata_value = "clam"
    expected = "networks/{network_code}/cmsMetadataValues/{cms_metadata_value}".format(
        network_code=network_code,
        cms_metadata_value=cms_metadata_value,
    )
    actual = LineItemServiceClient.cms_metadata_value_path(
        network_code, cms_metadata_value
    )
    assert expected == actual


def test_parse_cms_metadata_value_path():
    expected = {
        "network_code": "whelk",
        "cms_metadata_value": "octopus",
    }
    path = LineItemServiceClient.cms_metadata_value_path(**expected)

    # Check that the path construction is reversible.
    actual = LineItemServiceClient.parse_cms_metadata_value_path(path)
    assert expected == actual


def test_company_path():
    network_code = "oyster"
    company = "nudibranch"
    expected = "networks/{network_code}/companies/{company}".format(
        network_code=network_code,
        company=company,
    )
    actual = LineItemServiceClient.company_path(network_code, company)
    assert expected == actual


def test_parse_company_path():
    expected = {
        "network_code": "cuttlefish",
        "company": "mussel",
    }
    path = LineItemServiceClient.company_path(**expected)

    # Check that the path construction is reversible.
    actual = LineItemServiceClient.parse_company_path(path)
    assert expected == actual


def test_content_path():
    network_code = "winkle"
    content = "nautilus"
    expected = "networks/{network_code}/content/{content}".format(
        network_code=network_code,
        content=content,
    )
    actual = LineItemServiceClient.content_path(network_code, content)
    assert expected == actual


def test_parse_content_path():
    expected = {
        "network_code": "scallop",
        "content": "abalone",
    }
    path = LineItemServiceClient.content_path(**expected)

    # Check that the path construction is reversible.
    actual = LineItemServiceClient.parse_content_path(path)
    assert expected == actual


def test_content_bundle_path():
    network_code = "squid"
    content_bundle = "clam"
    expected = "networks/{network_code}/contentBundles/{content_bundle}".format(
        network_code=network_code,
        content_bundle=content_bundle,
    )
    actual = LineItemServiceClient.content_bundle_path(network_code, content_bundle)
    assert expected == actual


def test_parse_content_bundle_path():
    expected = {
        "network_code": "whelk",
        "content_bundle": "octopus",
    }
    path = LineItemServiceClient.content_bundle_path(**expected)

    # Check that the path construction is reversible.
    actual = LineItemServiceClient.parse_content_bundle_path(path)
    assert expected == actual


def test_custom_field_path():
    network_code = "oyster"
    custom_field = "nudibranch"
    expected = "networks/{network_code}/customFields/{custom_field}".format(
        network_code=network_code,
        custom_field=custom_field,
    )
    actual = LineItemServiceClient.custom_field_path(network_code, custom_field)
    assert expected == actual


def test_parse_custom_field_path():
    expected = {
        "network_code": "cuttlefish",
        "custom_field": "mussel",
    }
    path = LineItemServiceClient.custom_field_path(**expected)

    # Check that the path construction is reversible.
    actual = LineItemServiceClient.parse_custom_field_path(path)
    assert expected == actual


def test_custom_targeting_key_path():
    network_code = "winkle"
    custom_targeting_key = "nautilus"
    expected = (
        "networks/{network_code}/customTargetingKeys/{custom_targeting_key}".format(
            network_code=network_code,
            custom_targeting_key=custom_targeting_key,
        )
    )
    actual = LineItemServiceClient.custom_targeting_key_path(
        network_code, custom_targeting_key
    )
    assert expected == actual


def test_parse_custom_targeting_key_path():
    expected = {
        "network_code": "scallop",
        "custom_targeting_key": "abalone",
    }
    path = LineItemServiceClient.custom_targeting_key_path(**expected)

    # Check that the path construction is reversible.
    actual = LineItemServiceClient.parse_custom_targeting_key_path(path)
    assert expected == actual


def test_custom_targeting_value_path():
    network_code = "squid"
    custom_targeting_value = "clam"
    expected = (
        "networks/{network_code}/customTargetingValues/{custom_targeting_value}".format(
            network_code=network_code,
            custom_targeting_value=custom_targeting_value,
        )
    )
    actual = LineItemServiceClient.custom_targeting_value_path(
        network_code, custom_targeting_value
    )
    assert expected == actual


def test_parse_custom_targeting_value_path():
    expected = {
        "network_code": "whelk",
        "custom_targeting_value": "octopus",
    }
    path = LineItemServiceClient.custom_targeting_value_path(**expected)

    # Check that the path construction is reversible.
    actual = LineItemServiceClient.parse_custom_targeting_value_path(path)
    assert expected == actual


def test_device_capability_path():
    network_code = "oyster"
    device_capability = "nudibranch"
    expected = "networks/{network_code}/deviceCapabilities/{device_capability}".format(
        network_code=network_code,
        device_capability=device_capability,
    )
    actual = LineItemServiceClient.device_capability_path(
        network_code, device_capability
    )
    assert expected == actual


def test_parse_device_capability_path():
    expected = {
        "network_code": "cuttlefish",
        "device_capability": "mussel",
    }
    path = LineItemServiceClient.device_capability_path(**expected)

    # Check that the path construction is reversible.
    actual = LineItemServiceClient.parse_device_capability_path(path)
    assert expected == actual


def test_device_category_path():
    network_code = "winkle"
    device_category = "nautilus"
    expected = "networks/{network_code}/deviceCategories/{device_category}".format(
        network_code=network_code,
        device_category=device_category,
    )
    actual = LineItemServiceClient.device_category_path(network_code, device_category)
    assert expected == actual


def test_parse_device_category_path():
    expected = {
        "network_code": "scallop",
        "device_category": "abalone",
    }
    path = LineItemServiceClient.device_category_path(**expected)

    # Check that the path construction is reversible.
    actual = LineItemServiceClient.parse_device_category_path(path)
    assert expected == actual


def test_device_manufacturer_path():
    network_code = "squid"
    device_manufacturer = "clam"
    expected = (
        "networks/{network_code}/deviceManufacturers/{device_manufacturer}".format(
            network_code=network_code,
            device_manufacturer=device_manufacturer,
        )
    )
    actual = LineItemServiceClient.device_manufacturer_path(
        network_code, device_manufacturer
    )
    assert expected == actual


def test_parse_device_manufacturer_path():
    expected = {
        "network_code": "whelk",
        "device_manufacturer": "octopus",
    }
    path = LineItemServiceClient.device_manufacturer_path(**expected)

    # Check that the path construction is reversible.
    actual = LineItemServiceClient.parse_device_manufacturer_path(path)
    assert expected == actual


def test_geo_target_path():
    network_code = "oyster"
    geo_target = "nudibranch"
    expected = "networks/{network_code}/geoTargets/{geo_target}".format(
        network_code=network_code,
        geo_target=geo_target,
    )
    actual = LineItemServiceClient.geo_target_path(network_code, geo_target)
    assert expected == actual


def test_parse_geo_target_path():
    expected = {
        "network_code": "cuttlefish",
        "geo_target": "mussel",
    }
    path = LineItemServiceClient.geo_target_path(**expected)

    # Check that the path construction is reversible.
    actual = LineItemServiceClient.parse_geo_target_path(path)
    assert expected == actual


def test_label_path():
    network_code = "winkle"
    label = "nautilus"
    expected = "networks/{network_code}/labels/{label}".format(
        network_code=network_code,
        label=label,
    )
    actual = LineItemServiceClient.label_path(network_code, label)
    assert expected == actual


def test_parse_label_path():
    expected = {
        "network_code": "scallop",
        "label": "abalone",
    }
    path = LineItemServiceClient.label_path(**expected)

    # Check that the path construction is reversible.
    actual = LineItemServiceClient.parse_label_path(path)
    assert expected == actual


def test_line_item_path():
    network_code = "squid"
    line_item = "clam"
    expected = "networks/{network_code}/lineItems/{line_item}".format(
        network_code=network_code,
        line_item=line_item,
    )
    actual = LineItemServiceClient.line_item_path(network_code, line_item)
    assert expected == actual


def test_parse_line_item_path():
    expected = {
        "network_code": "whelk",
        "line_item": "octopus",
    }
    path = LineItemServiceClient.line_item_path(**expected)

    # Check that the path construction is reversible.
    actual = LineItemServiceClient.parse_line_item_path(path)
    assert expected == actual


def test_mobile_carrier_path():
    network_code = "oyster"
    mobile_carrier = "nudibranch"
    expected = "networks/{network_code}/mobileCarriers/{mobile_carrier}".format(
        network_code=network_code,
        mobile_carrier=mobile_carrier,
    )
    actual = LineItemServiceClient.mobile_carrier_path(network_code, mobile_carrier)
    assert expected == actual


def test_parse_mobile_carrier_path():
    expected = {
        "network_code": "cuttlefish",
        "mobile_carrier": "mussel",
    }
    path = LineItemServiceClient.mobile_carrier_path(**expected)

    # Check that the path construction is reversible.
    actual = LineItemServiceClient.parse_mobile_carrier_path(path)
    assert expected == actual


def test_mobile_device_path():
    network_code = "winkle"
    mobile_device = "nautilus"
    expected = "networks/{network_code}/mobileDevices/{mobile_device}".format(
        network_code=network_code,
        mobile_device=mobile_device,
    )
    actual = LineItemServiceClient.mobile_device_path(network_code, mobile_device)
    assert expected == actual


def test_parse_mobile_device_path():
    expected = {
        "network_code": "scallop",
        "mobile_device": "abalone",
    }
    path = LineItemServiceClient.mobile_device_path(**expected)

    # Check that the path construction is reversible.
    actual = LineItemServiceClient.parse_mobile_device_path(path)
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
    actual = LineItemServiceClient.mobile_device_submodel_path(
        network_code, mobile_device_submodel
    )
    assert expected == actual


def test_parse_mobile_device_submodel_path():
    expected = {
        "network_code": "whelk",
        "mobile_device_submodel": "octopus",
    }
    path = LineItemServiceClient.mobile_device_submodel_path(**expected)

    # Check that the path construction is reversible.
    actual = LineItemServiceClient.parse_mobile_device_submodel_path(path)
    assert expected == actual


def test_network_path():
    network_code = "oyster"
    expected = "networks/{network_code}".format(
        network_code=network_code,
    )
    actual = LineItemServiceClient.network_path(network_code)
    assert expected == actual


def test_parse_network_path():
    expected = {
        "network_code": "nudibranch",
    }
    path = LineItemServiceClient.network_path(**expected)

    # Check that the path construction is reversible.
    actual = LineItemServiceClient.parse_network_path(path)
    assert expected == actual


def test_operating_system_path():
    network_code = "cuttlefish"
    operating_system = "mussel"
    expected = "networks/{network_code}/operatingSystems/{operating_system}".format(
        network_code=network_code,
        operating_system=operating_system,
    )
    actual = LineItemServiceClient.operating_system_path(network_code, operating_system)
    assert expected == actual


def test_parse_operating_system_path():
    expected = {
        "network_code": "winkle",
        "operating_system": "nautilus",
    }
    path = LineItemServiceClient.operating_system_path(**expected)

    # Check that the path construction is reversible.
    actual = LineItemServiceClient.parse_operating_system_path(path)
    assert expected == actual


def test_operating_system_version_path():
    network_code = "scallop"
    operating_system_version = "abalone"
    expected = "networks/{network_code}/operatingSystemVersions/{operating_system_version}".format(
        network_code=network_code,
        operating_system_version=operating_system_version,
    )
    actual = LineItemServiceClient.operating_system_version_path(
        network_code, operating_system_version
    )
    assert expected == actual


def test_parse_operating_system_version_path():
    expected = {
        "network_code": "squid",
        "operating_system_version": "clam",
    }
    path = LineItemServiceClient.operating_system_version_path(**expected)

    # Check that the path construction is reversible.
    actual = LineItemServiceClient.parse_operating_system_version_path(path)
    assert expected == actual


def test_order_path():
    network_code = "whelk"
    order = "octopus"
    expected = "networks/{network_code}/orders/{order}".format(
        network_code=network_code,
        order=order,
    )
    actual = LineItemServiceClient.order_path(network_code, order)
    assert expected == actual


def test_parse_order_path():
    expected = {
        "network_code": "oyster",
        "order": "nudibranch",
    }
    path = LineItemServiceClient.order_path(**expected)

    # Check that the path construction is reversible.
    actual = LineItemServiceClient.parse_order_path(path)
    assert expected == actual


def test_placement_path():
    network_code = "cuttlefish"
    placement = "mussel"
    expected = "networks/{network_code}/placements/{placement}".format(
        network_code=network_code,
        placement=placement,
    )
    actual = LineItemServiceClient.placement_path(network_code, placement)
    assert expected == actual


def test_parse_placement_path():
    expected = {
        "network_code": "winkle",
        "placement": "nautilus",
    }
    path = LineItemServiceClient.placement_path(**expected)

    # Check that the path construction is reversible.
    actual = LineItemServiceClient.parse_placement_path(path)
    assert expected == actual


def test_common_billing_account_path():
    billing_account = "scallop"
    expected = "billingAccounts/{billing_account}".format(
        billing_account=billing_account,
    )
    actual = LineItemServiceClient.common_billing_account_path(billing_account)
    assert expected == actual


def test_parse_common_billing_account_path():
    expected = {
        "billing_account": "abalone",
    }
    path = LineItemServiceClient.common_billing_account_path(**expected)

    # Check that the path construction is reversible.
    actual = LineItemServiceClient.parse_common_billing_account_path(path)
    assert expected == actual


def test_common_folder_path():
    folder = "squid"
    expected = "folders/{folder}".format(
        folder=folder,
    )
    actual = LineItemServiceClient.common_folder_path(folder)
    assert expected == actual


def test_parse_common_folder_path():
    expected = {
        "folder": "clam",
    }
    path = LineItemServiceClient.common_folder_path(**expected)

    # Check that the path construction is reversible.
    actual = LineItemServiceClient.parse_common_folder_path(path)
    assert expected == actual


def test_common_organization_path():
    organization = "whelk"
    expected = "organizations/{organization}".format(
        organization=organization,
    )
    actual = LineItemServiceClient.common_organization_path(organization)
    assert expected == actual


def test_parse_common_organization_path():
    expected = {
        "organization": "octopus",
    }
    path = LineItemServiceClient.common_organization_path(**expected)

    # Check that the path construction is reversible.
    actual = LineItemServiceClient.parse_common_organization_path(path)
    assert expected == actual


def test_common_project_path():
    project = "oyster"
    expected = "projects/{project}".format(
        project=project,
    )
    actual = LineItemServiceClient.common_project_path(project)
    assert expected == actual


def test_parse_common_project_path():
    expected = {
        "project": "nudibranch",
    }
    path = LineItemServiceClient.common_project_path(**expected)

    # Check that the path construction is reversible.
    actual = LineItemServiceClient.parse_common_project_path(path)
    assert expected == actual


def test_common_location_path():
    project = "cuttlefish"
    location = "mussel"
    expected = "projects/{project}/locations/{location}".format(
        project=project,
        location=location,
    )
    actual = LineItemServiceClient.common_location_path(project, location)
    assert expected == actual


def test_parse_common_location_path():
    expected = {
        "project": "winkle",
        "location": "nautilus",
    }
    path = LineItemServiceClient.common_location_path(**expected)

    # Check that the path construction is reversible.
    actual = LineItemServiceClient.parse_common_location_path(path)
    assert expected == actual


def test_client_with_default_client_info():
    client_info = gapic_v1.client_info.ClientInfo()

    with mock.patch.object(
        transports.LineItemServiceTransport, "_prep_wrapped_messages"
    ) as prep:
        client = LineItemServiceClient(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)

    with mock.patch.object(
        transports.LineItemServiceTransport, "_prep_wrapped_messages"
    ) as prep:
        transport_class = LineItemServiceClient.get_transport_class()
        transport = transport_class(
            credentials=ga_credentials.AnonymousCredentials(),
            client_info=client_info,
        )
        prep.assert_called_once_with(client_info)


def test_transport_close_rest():
    client = LineItemServiceClient(
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
        client = LineItemServiceClient(
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
        (LineItemServiceClient, transports.LineItemServiceRestTransport),
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
