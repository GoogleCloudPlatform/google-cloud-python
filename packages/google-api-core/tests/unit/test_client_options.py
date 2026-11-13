# Copyright 2019 Google LLC
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

from re import match

import pytest

from google.api_core import client_options

from ..helpers import warn_deprecated_credentials_file


def get_client_cert():
    return b"cert", b"key"


def get_client_encrypted_cert():
    return "cert_path", "key_path", b"passphrase"


def test_constructor():
    mock_tracer_provider = object()
    with warn_deprecated_credentials_file():
        options = client_options.ClientOptions(
            api_endpoint="foo.googleapis.com",
            client_cert_source=get_client_cert,
            quota_project_id="quote-proj",
            credentials_file="path/to/credentials.json",
            scopes=[
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/cloud-platform.read-only",
            ],
            api_audience="foo2.googleapis.com",
            universe_domain="googleapis.com",
            tracer_provider=mock_tracer_provider,
        )

    assert options.api_endpoint == "foo.googleapis.com"
    assert options.client_cert_source() == (b"cert", b"key")
    assert options.quota_project_id == "quote-proj"
    assert options.credentials_file == "path/to/credentials.json"
    assert options.scopes == [
        "https://www.googleapis.com/auth/cloud-platform",
        "https://www.googleapis.com/auth/cloud-platform.read-only",
    ]
    assert options.api_audience == "foo2.googleapis.com"
    assert options.universe_domain == "googleapis.com"
    assert options.tracer_provider is mock_tracer_provider


def test_constructor_with_encrypted_cert_source():
    options = client_options.ClientOptions(
        api_endpoint="foo.googleapis.com",
        client_encrypted_cert_source=get_client_encrypted_cert,
    )

    assert options.api_endpoint == "foo.googleapis.com"
    assert options.client_encrypted_cert_source() == (
        "cert_path",
        "key_path",
        b"passphrase",
    )


def test_constructor_with_both_cert_sources():
    with pytest.raises(ValueError):
        client_options.ClientOptions(
            api_endpoint="foo.googleapis.com",
            client_cert_source=get_client_cert,
            client_encrypted_cert_source=get_client_encrypted_cert,
        )


def test_constructor_with_api_key():
    options = client_options.ClientOptions(
        api_endpoint="foo.googleapis.com",
        client_cert_source=get_client_cert,
        quota_project_id="quote-proj",
        api_key="api-key",
        scopes=[
            "https://www.googleapis.com/auth/cloud-platform",
            "https://www.googleapis.com/auth/cloud-platform.read-only",
        ],
    )

    assert options.api_endpoint == "foo.googleapis.com"
    assert options.client_cert_source() == (b"cert", b"key")
    assert options.quota_project_id == "quote-proj"
    assert options.api_key == "api-key"
    assert options.scopes == [
        "https://www.googleapis.com/auth/cloud-platform",
        "https://www.googleapis.com/auth/cloud-platform.read-only",
    ]


def test_constructor_with_both_api_key_and_credentials_file():
    with pytest.raises(ValueError):
        with warn_deprecated_credentials_file():
            client_options.ClientOptions(
                api_key="api-key",
                credentials_file="path/to/credentials.json",
            )


def test_from_dict():
    options = client_options.from_dict(
        {
            "api_endpoint": "foo.googleapis.com",
            "universe_domain": "googleapis.com",
            "client_cert_source": get_client_cert,
            "quota_project_id": "quote-proj",
            "credentials_file": "path/to/credentials.json",
            "scopes": [
                "https://www.googleapis.com/auth/cloud-platform",
                "https://www.googleapis.com/auth/cloud-platform.read-only",
            ],
            "api_audience": "foo2.googleapis.com",
        }
    )

    assert options.api_endpoint == "foo.googleapis.com"
    assert options.universe_domain == "googleapis.com"
    assert options.client_cert_source() == (b"cert", b"key")
    assert options.quota_project_id == "quote-proj"
    assert options.credentials_file == "path/to/credentials.json"
    assert options.scopes == [
        "https://www.googleapis.com/auth/cloud-platform",
        "https://www.googleapis.com/auth/cloud-platform.read-only",
    ]
    assert options.api_key is None
    assert options.api_audience == "foo2.googleapis.com"


def test_from_dict_bad_argument():
    with pytest.raises(ValueError):
        client_options.from_dict(
            {
                "api_endpoint": "foo.googleapis.com",
                "bad_arg": "1234",
                "client_cert_source": get_client_cert,
            }
        )


def test_repr():
    expected_keys = set(
        [
            "api_endpoint",
            "universe_domain",
            "client_cert_source",
            "client_encrypted_cert_source",
            "quota_project_id",
            "credentials_file",
            "scopes",
            "api_key",
            "api_audience",
            "tracer_provider",
        ]
    )
    options = client_options.ClientOptions(api_endpoint="foo.googleapis.com")
    options_repr = repr(options)
    options_keys = vars(options).keys()
    assert match(r"ClientOptions:", options_repr)
    assert match(r".*'api_endpoint': 'foo.googleapis.com'.*", options_repr)
    assert options_keys == expected_keys
