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

import re

import pytest

from google.api_core.gapic_v1.requests import setup_request_id

# --- Mock Request Helper Classes ---


class MockRequest:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class MockProtoRequest:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def HasField(self, key):
        return hasattr(self, key)


class MockProtoPlusRequest:
    def __init__(self, **kwargs):
        self._pb = MockProtoRequest(**kwargs)
        for k, v in kwargs.items():
            setattr(self, k, v)


class MockValueErrorRequest:
    def HasField(self, key):
        raise ValueError("Mismatched field")


class MockProtoPlusValueErrorRequest:
    def __init__(self, **kwargs):
        self._pb = MockValueErrorRequest()
        for k, v in kwargs.items():
            setattr(self, k, v)


# --- Parameterized Test ---

UUID_REGEX = r"[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}"


@pytest.mark.parametrize(
    "request_obj, is_proto3_optional, expected",
    [
        # MockRequest cases
        (MockRequest(), True, "uuid"),
        (MockRequest(request_id="already_set"), True, "already_set"),
        (MockRequest(request_id=""), True, ""),
        (MockRequest(request_id=""), False, "uuid"),
        (MockRequest(request_id="already_set"), False, "already_set"),
        # MockProtoRequest cases
        (MockProtoRequest(), True, "uuid"),
        (MockProtoRequest(request_id="already_set"), True, "already_set"),
        (MockProtoRequest(request_id=""), True, ""),
        # MockProtoPlusRequest cases
        (MockProtoPlusRequest(), True, "uuid"),
        (MockProtoPlusRequest(request_id="already_set"), True, "already_set"),
        (MockProtoPlusRequest(request_id=""), True, ""),
        # ValueError case
        (MockValueErrorRequest(), True, "uuid"),
        (MockProtoPlusValueErrorRequest(), True, "uuid"),
        # Dict cases
        ({}, True, "uuid"),
        ({"request_id": None}, True, "uuid"),
        ({"request_id": "already_set"}, True, "already_set"),
        ({"request_id": ""}, True, ""),
        ({"request_id": ""}, False, "uuid"),
        ({"request_id": None}, False, "uuid"),
        ({"request_id": "already_set"}, False, "already_set"),
        # None case
        (None, True, "none"),
    ],
    ids=[
        "proto3_optional_not_in_request",
        "proto3_optional_already_in_request",
        "proto3_optional_explicit_empty",
        "non_proto3_optional_empty",
        "non_proto3_optional_already_set",
        "proto3_optional_not_in_request_proto",
        "proto3_optional_already_in_request_proto",
        "proto3_optional_explicit_empty_proto",
        "proto3_optional_not_in_request_proto_plus",
        "proto3_optional_already_in_request_proto_plus",
        "proto3_optional_explicit_empty_proto_plus",
        "value_error_fallback",
        "proto3_optional_value_error_fallback_proto_plus",
        "dict_proto3_optional_not_in_request",
        "dict_proto3_optional_value_none",
        "dict_proto3_optional_already_in_request",
        "dict_proto3_optional_explicit_empty",
        "dict_non_proto3_optional_empty",
        "dict_non_proto3_optional_value_none",
        "dict_non_proto3_optional_already_set",
        "none_request",
    ],
)
def test_setup_request_id(request_obj, is_proto3_optional, expected):
    # Act
    setup_request_id(request_obj, "request_id", is_proto3_optional)

    # Assert
    if expected == "none":
        assert request_obj is None
        return

    # Extract the resulting value depending on container type
    value = (
        request_obj["request_id"]
        if isinstance(request_obj, dict)
        else request_obj.request_id
    )

    if expected == "uuid":
        assert re.fullmatch(UUID_REGEX, value)
    else:
        assert value == expected


def test_setup_request_id_assertion_strictness(mocker):
    # Mock uuid.uuid4 to return a UUID with trailing characters
    mock_uuid = mocker.patch("uuid.uuid4")
    mock_uuid.return_value.__str__.return_value = (
        "12345678-1234-4123-8123-123456789012-extra"
    )

    # We expect test_setup_request_id to fail (raise AssertionError) because the UUID is invalid.
    # If test_setup_request_id uses re.fullmatch, it will fail (raise AssertionError), so pytest.raises passes.
    # If test_setup_request_id uses re.match, it will NOT fail, so pytest.raises fails!
    with pytest.raises(AssertionError):
        test_setup_request_id(MockRequest(), is_proto3_optional=True, expected="uuid")
