# Copyright 2016 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
import json
import logging
import urllib
from unittest import mock

import pytest  # type: ignore

from google.auth import _helpers

# _MOCK_BASE_LOGGER_NAME is the base logger namespace used for testing.
_MOCK_BASE_LOGGER_NAME = "foogle"

# _MOCK_CHILD_LOGGER_NAME is the child logger namespace used for testing.
_MOCK_CHILD_LOGGER_NAME = "foogle.bar"


@pytest.fixture
def logger():
    """Returns a child logger for testing."""
    logger = logging.getLogger(_MOCK_CHILD_LOGGER_NAME)
    logger.level = logging.NOTSET
    logger.handlers = []
    logger.propagate = True
    return logger


@pytest.fixture
def base_logger():
    """Returns a child logger for testing."""
    logger = logging.getLogger(_MOCK_BASE_LOGGER_NAME)
    logger.level = logging.NOTSET
    logger.handlers = []
    logger.propagate = True
    return logger


@pytest.fixture(autouse=True)
def reset_logging_initialized():
    """Resets the global _LOGGING_INITIALIZED variable before each test."""
    original_state = _helpers._LOGGING_INITIALIZED
    _helpers._LOGGING_INITIALIZED = False
    yield
    _helpers._LOGGING_INITIALIZED = original_state


class SourceClass(object):
    def func(self):  # pragma: NO COVER
        """example docstring"""


def test_copy_docstring_success():
    def func():  # pragma: NO COVER
        pass

    _helpers.copy_docstring(SourceClass)(func)

    assert func.__doc__ == SourceClass.func.__doc__


def test_copy_docstring_conflict():
    def func():  # pragma: NO COVER
        """existing docstring"""
        pass

    with pytest.raises(ValueError):
        _helpers.copy_docstring(SourceClass)(func)


def test_copy_docstring_non_existing():
    def func2():  # pragma: NO COVER
        pass

    with pytest.raises(AttributeError):
        _helpers.copy_docstring(SourceClass)(func2)


def test_parse_content_type_plain():
    assert _helpers.parse_content_type("text/html") == "text/html"
    assert _helpers.parse_content_type("application/xml") == "application/xml"
    assert _helpers.parse_content_type("application/json") == "application/json"


def test_parse_content_type_with_parameters():
    content_type_html = "text/html; charset=UTF-8"
    content_type_xml = "application/xml; charset=UTF-16; version=1.0"
    content_type_json = "application/json; charset=UTF-8; indent=2"
    assert _helpers.parse_content_type(content_type_html) == "text/html"
    assert _helpers.parse_content_type(content_type_xml) == "application/xml"
    assert _helpers.parse_content_type(content_type_json) == "application/json"


def test_parse_content_type_missing_or_broken():
    content_type_foo = None
    content_type_bar = ""
    content_type_baz = "1234"
    content_type_qux = " ; charset=UTF-8"
    assert _helpers.parse_content_type(content_type_foo) == "text/plain"
    assert _helpers.parse_content_type(content_type_bar) == "text/plain"
    assert _helpers.parse_content_type(content_type_baz) == "text/plain"
    assert _helpers.parse_content_type(content_type_qux) == "text/plain"


def test_utcnow():
    assert isinstance(_helpers.utcnow(), datetime.datetime)


def test_datetime_to_secs():
    assert _helpers.datetime_to_secs(datetime.datetime(1970, 1, 1)) == 0
    assert _helpers.datetime_to_secs(datetime.datetime(1990, 5, 29)) == 643939200


def test_to_bytes_with_bytes():
    value = b"bytes-val"
    assert _helpers.to_bytes(value) == value


def test_to_bytes_with_unicode():
    value = "string-val"
    encoded_value = b"string-val"
    assert _helpers.to_bytes(value) == encoded_value


def test_to_bytes_with_nonstring_type():
    with pytest.raises(ValueError):
        _helpers.to_bytes(object())


def test_from_bytes_with_unicode():
    value = "bytes-val"
    assert _helpers.from_bytes(value) == value


def test_from_bytes_with_bytes():
    value = b"string-val"
    decoded_value = "string-val"
    assert _helpers.from_bytes(value) == decoded_value


def test_from_bytes_with_nonstring_type():
    with pytest.raises(ValueError):
        _helpers.from_bytes(object())


def _assert_query(url, expected):
    parts = urllib.parse.urlsplit(url)
    query = urllib.parse.parse_qs(parts.query)
    assert query == expected


def test_update_query_params_no_params():
    uri = "http://www.google.com"
    updated = _helpers.update_query(uri, {"a": "b"})
    assert updated == uri + "?a=b"


def test_update_query_existing_params():
    uri = "http://www.google.com?x=y"
    updated = _helpers.update_query(uri, {"a": "b", "c": "d&"})
    _assert_query(updated, {"x": ["y"], "a": ["b"], "c": ["d&"]})


def test_update_query_replace_param():
    base_uri = "http://www.google.com"
    uri = base_uri + "?x=a"
    updated = _helpers.update_query(uri, {"x": "b", "y": "c"})
    _assert_query(updated, {"x": ["b"], "y": ["c"]})


def test_update_query_remove_param():
    base_uri = "http://www.google.com"
    uri = base_uri + "?x=a"
    updated = _helpers.update_query(uri, {"y": "c"}, remove=["x"])
    _assert_query(updated, {"y": ["c"]})


def test_scopes_to_string():
    cases = [
        ("", ()),
        ("", []),
        ("", ("",)),
        ("", [""]),
        ("a", ("a",)),
        ("b", ["b"]),
        ("a b", ["a", "b"]),
        ("a b", ("a", "b")),
        ("a b", (s for s in ["a", "b"])),
    ]
    for expected, case in cases:
        assert _helpers.scopes_to_string(case) == expected


def test_string_to_scopes():
    cases = [("", []), ("a", ["a"]), ("a b c d e f", ["a", "b", "c", "d", "e", "f"])]

    for case, expected in cases:
        assert _helpers.string_to_scopes(case) == expected


def test_padded_urlsafe_b64decode():
    cases = [
        ("YQ==", b"a"),
        ("YQ", b"a"),
        ("YWE=", b"aa"),
        ("YWE", b"aa"),
        ("YWFhYQ==", b"aaaa"),
        ("YWFhYQ", b"aaaa"),
        ("YWFhYWE=", b"aaaaa"),
        ("YWFhYWE", b"aaaaa"),
    ]

    for case, expected in cases:
        assert _helpers.padded_urlsafe_b64decode(case) == expected


def test_unpadded_urlsafe_b64encode():
    cases = [(b"", b""), (b"a", b"YQ"), (b"aa", b"YWE"), (b"aaa", b"YWFh")]

    for case, expected in cases:
        assert _helpers.unpadded_urlsafe_b64encode(case) == expected


def test_hash_sensitive_info_basic():
    test_data = {
        "expires_in": 3599,
        "access_token": "access-123",
        "scope": "https://www.googleapis.com/auth/test-api",
        "token_type": "Bearer",
    }
    hashed_data = _helpers._hash_sensitive_info(test_data)
    assert hashed_data["expires_in"] == 3599
    assert hashed_data["scope"] == "https://www.googleapis.com/auth/test-api"
    assert hashed_data["access_token"].startswith("hashed_access_token-")
    assert hashed_data["token_type"] == "Bearer"


def test_hash_sensitive_info_multiple_sensitive():
    test_data = {
        "access_token": "some_long_token",
        "id_token": "1234-5678-9012-3456",
        "expires_in": 3599,
        "token_type": "Bearer",
    }
    hashed_data = _helpers._hash_sensitive_info(test_data)
    assert hashed_data["expires_in"] == 3599
    assert hashed_data["token_type"] == "Bearer"
    assert hashed_data["access_token"].startswith("hashed_access_token-")
    assert hashed_data["id_token"].startswith("hashed_id_token-")


def test_hash_sensitive_info_none_value():
    test_data = {"username": "user3", "secret": None, "normal_data": "abc"}
    hashed_data = _helpers._hash_sensitive_info(test_data)
    assert hashed_data["secret"] is None
    assert hashed_data["normal_data"] == "abc"


def test_hash_sensitive_info_non_string_value():
    test_data = {"username": "user4", "access_token": 12345, "normal_data": "def"}
    hashed_data = _helpers._hash_sensitive_info(test_data)
    assert hashed_data["access_token"].startswith("hashed_access_token-")
    assert hashed_data["normal_data"] == "def"


def test_hash_sensitive_info_list_value():
    test_data = [
        {"name": "Alice", "access_token": "12345"},
        {"name": "Bob", "client_id": "1141"},
    ]
    hashed_data = _helpers._hash_sensitive_info(test_data)
    assert hashed_data[0]["access_token"].startswith("hashed_access_token-")
    assert hashed_data[1]["client_id"].startswith("hashed_client_id-")


def test_hash_sensitive_info_nested_list_value():
    test_data = [{"names": ["Alice", "Bob"], "tokens": [{"access_token": "1234"}]}]
    hashed_data = _helpers._hash_sensitive_info(test_data)
    assert hashed_data[0]["tokens"][0]["access_token"].startswith(
        "hashed_access_token-"
    )


def test_hash_sensitive_info_int_value():
    test_data = 123
    hashed_data = _helpers._hash_sensitive_info(test_data)
    assert hashed_data == "<class 'int'>"


def test_hash_sensitive_info_bool_value():
    test_data = True
    hashed_data = _helpers._hash_sensitive_info(test_data)
    assert hashed_data == "<class 'bool'>"


def test_hash_sensitive_info_byte_value():
    test_data = b"1243"
    hashed_data = _helpers._hash_sensitive_info(test_data)
    assert hashed_data == "<class 'bytes'>"


def test_hash_sensitive_info_empty_dict():
    test_data = {}
    hashed_data = _helpers._hash_sensitive_info(test_data)
    assert hashed_data == {}


def test_hash_value_consistent_hashing():
    value = "test_value"
    field_name = "test_field"
    hash1 = _helpers._hash_value(value, field_name)
    hash2 = _helpers._hash_value(value, field_name)
    assert hash1 == hash2


def test_hash_value_different_hashing():
    value1 = "test_value1"
    value2 = "test_value2"
    field_name = "test_field"
    hash1 = _helpers._hash_value(value1, field_name)
    hash2 = _helpers._hash_value(value2, field_name)
    assert hash1 != hash2


def test_hash_value_none():
    assert _helpers._hash_value(None, "test") is None


def test_logger_configured_default(logger):
    assert not _helpers._logger_configured(logger)


def test_logger_configured_with_handler(logger):
    mock_handler = logging.NullHandler()
    logger.addHandler(mock_handler)
    assert _helpers._logger_configured(logger)

    # Cleanup
    logger.removeHandler(mock_handler)


def test_logger_configured_with_custom_level(logger):
    original_level = logger.level
    logger.level = logging.INFO
    assert _helpers._logger_configured(logger)

    # Cleanup
    logging.level = original_level


def test_logger_configured_with_propagate(logger):
    original_propagate = logger.propagate
    logger.propagate = False
    assert _helpers._logger_configured(logger)

    # Cleanup
    logger.propagate = original_propagate


def test_is_logging_enabled_with_no_level_set(logger, base_logger):
    with mock.patch("google.auth._helpers._BASE_LOGGER_NAME", "foogle"):
        assert _helpers.is_logging_enabled(logger) is False


def test_is_logging_enabled_with_debug_disabled(caplog, logger, base_logger):
    with mock.patch("google.auth._helpers._BASE_LOGGER_NAME", _MOCK_BASE_LOGGER_NAME):
        caplog.set_level(logging.INFO, logger=_MOCK_CHILD_LOGGER_NAME)
        assert _helpers.is_logging_enabled(logger) is False


def test_is_logging_enabled_with_debug_enabled(caplog, logger, base_logger):
    with mock.patch("google.auth._helpers._BASE_LOGGER_NAME", _MOCK_BASE_LOGGER_NAME):
        caplog.set_level(logging.DEBUG, logger=_MOCK_CHILD_LOGGER_NAME)
        assert _helpers.is_logging_enabled(logger)


def test_is_logging_enabled_with_base_logger_configured_with_info(
    caplog, logger, base_logger
):
    with mock.patch("google.auth._helpers._BASE_LOGGER_NAME", _MOCK_BASE_LOGGER_NAME):
        caplog.set_level(logging.INFO, logger=_MOCK_BASE_LOGGER_NAME)

    base_logger = logging.getLogger(_MOCK_BASE_LOGGER_NAME)
    assert not _helpers.is_logging_enabled(base_logger)
    assert not _helpers.is_logging_enabled(logger)


def test_is_logging_enabled_with_base_logger_configured_with_debug(
    caplog, logger, base_logger
):
    with mock.patch("google.auth._helpers._BASE_LOGGER_NAME", _MOCK_BASE_LOGGER_NAME):
        caplog.set_level(logging.DEBUG, logger=_MOCK_BASE_LOGGER_NAME)

    assert _helpers.is_logging_enabled(base_logger)
    assert _helpers.is_logging_enabled(logger)


def test_is_logging_enabled_with_base_logger_info_child_logger_debug(
    caplog, logger, base_logger
):
    with mock.patch("google.auth._helpers._BASE_LOGGER_NAME", _MOCK_BASE_LOGGER_NAME):
        caplog.set_level(logging.INFO, logger=_MOCK_BASE_LOGGER_NAME)
        caplog.set_level(logging.DEBUG, logger=_MOCK_CHILD_LOGGER_NAME)

    assert not _helpers.is_logging_enabled(base_logger)
    assert _helpers.is_logging_enabled(logger)


def test_is_logging_enabled_with_base_logger_debug_child_logger_info(
    caplog, logger, base_logger
):
    with mock.patch("google.auth._helpers._BASE_LOGGER_NAME", _MOCK_BASE_LOGGER_NAME):
        caplog.set_level(logging.DEBUG, logger=_MOCK_BASE_LOGGER_NAME)
        caplog.set_level(logging.INFO, logger=_MOCK_CHILD_LOGGER_NAME)

    assert _helpers.is_logging_enabled(base_logger)
    assert not _helpers.is_logging_enabled(logger)


def test_request_log_debug_enabled(logger, caplog, base_logger):
    caplog.set_level(logging.DEBUG, logger=_MOCK_CHILD_LOGGER_NAME)
    _helpers.request_log(
        logger,
        "GET",
        "http://example.com",
        b'{"key": "value"}',
        {"Authorization": "Bearer token"},
    )
    assert len(caplog.records) == 1
    record = caplog.records[0]
    assert record.message == "Making request..."
    assert record.httpRequest == {
        "method": "GET",
        "url": "http://example.com",
        "body": {"key": "value"},
        "headers": {"Authorization": "Bearer token"},
    }


def test_request_log_plain_text_debug_enabled(logger, caplog, base_logger):
    caplog.set_level(logging.DEBUG, logger=_MOCK_CHILD_LOGGER_NAME)
    _helpers.request_log(
        logger,
        "GET",
        "http://example.com",
        b"This is plain text.",
        {"Authorization": "Bearer token", "Content-Type": "text/plain"},
    )
    assert len(caplog.records) == 1
    record = caplog.records[0]
    assert record.message == "Making request..."
    assert record.httpRequest == {
        "method": "GET",
        "url": "http://example.com",
        "body": "<class 'str'>",
        "headers": {"Authorization": "Bearer token", "Content-Type": "text/plain"},
    }


def test_request_log_debug_disabled(logger, caplog, base_logger):
    caplog.set_level(logging.INFO, logger=_MOCK_CHILD_LOGGER_NAME)
    _helpers.request_log(
        logger,
        "POST",
        "https://api.example.com",
        "data",
        {"Content-Type": "application/json"},
    )
    assert "Making request: POST https://api.example.com" not in caplog.text


def test_response_log_debug_enabled(logger, caplog, base_logger):
    caplog.set_level(logging.DEBUG, logger=_MOCK_CHILD_LOGGER_NAME)
    _helpers.response_log(logger, {"payload": None})
    assert len(caplog.records) == 1
    record = caplog.records[0]
    assert record.message == "Response received..."
    assert record.httpResponse == "<class 'NoneType'>"


def test_response_log_debug_disabled(logger, caplog):
    caplog.set_level(logging.INFO, logger=_MOCK_CHILD_LOGGER_NAME)
    _helpers.response_log(logger, "another_response")
    assert "Response received..." not in caplog.text


def test_response_log_base_logger_configured(logger, caplog, base_logger):
    caplog.set_level(logging.DEBUG, logger=_MOCK_BASE_LOGGER_NAME)
    _helpers.response_log(logger, "another_response")
    assert "Response received..." in caplog.text


def test_response_log_debug_enabled_response_list(logger, caplog, base_logger):
    # NOTE: test the response log when response.json() returns a list as per
    #  https://requests.readthedocs.io/en/latest/api/#requests.Response.json.
    class MockResponse:
        def json(self):
            return ["item1", "item2", "item3"]

    response = MockResponse()
    caplog.set_level(logging.DEBUG, logger=_MOCK_CHILD_LOGGER_NAME)
    _helpers.response_log(logger, response)
    assert len(caplog.records) == 1
    record = caplog.records[0]
    assert record.message == "Response received..."
    assert record.httpResponse == ["<class 'str'>", "<class 'str'>", "<class 'str'>"]


def test_parse_request_body_bytes_valid():
    body = b"key1=value1&key2=value2"
    expected = {"key1": "value1", "key2": "value2"}
    assert (
        _helpers._parse_request_body(
            body, content_type="application/x-www-form-urlencoded"
        )
        == expected
    )


def test_parse_request_body_bytes_empty():
    body = b""
    assert _helpers._parse_request_body(body) == ""


def test_parse_request_body_bytes_invalid_encoding():
    body = b"\xff\xfe\xfd"  # Invalid UTF-8 sequence
    assert _helpers._parse_request_body(body) is None


def test_parse_request_body_bytes_malformed_query():
    body = b"key1=value1&key2=value2"  # missing equals
    expected = {"key1": "value1", "key2": "value2"}
    assert (
        _helpers._parse_request_body(
            body, content_type="application/x-www-form-urlencoded"
        )
        == expected
    )


def test_parse_request_body_none():
    assert _helpers._parse_request_body(None) is None


def test_parse_request_body_bytes_no_content_type():
    body = b'{"key": "value"}'
    expected = {"key": "value"}
    assert _helpers._parse_request_body(body) == expected


def test_parse_request_body_bytes_content_type_json():
    body = b'{"key": "value"}'
    expected = {"key": "value"}
    assert (
        _helpers._parse_request_body(body, content_type="application/json") == expected
    )


def test_parse_request_body_content_type_urlencoded():
    body = b"key=value"
    expected = {"key": "value"}
    assert (
        _helpers._parse_request_body(
            body, content_type="application/x-www-form-urlencoded"
        )
        == expected
    )


def test_parse_request_body_bytes_content_type_text():
    body = b"This is plain text."
    expected = "This is plain text."
    assert _helpers._parse_request_body(body, content_type="text/plain") == expected


def test_parse_request_body_content_type_invalid():
    body = b'{"key": "value"}'
    assert _helpers._parse_request_body(body, content_type="invalid") is None


def test_parse_request_body_other_type():
    assert _helpers._parse_request_body(123) is None
    assert _helpers._parse_request_body("string") is None


def test_parse_request_body_json_type_error():
    body = b'{"key": "value"}'
    with mock.patch("json.loads", side_effect=TypeError):
        # json.loads should raise a TypeError, and the function should return the
        # original string
        assert _helpers._parse_request_body(body, "application/json") == body.decode(
            "utf-8"
        )


def test_parse_request_body_json_value_error():
    body = b'{"key": "value"}'
    content_type = "application/json"
    with mock.patch("json.loads", side_effect=ValueError):
        # json.loads should raise a ValueError, and the function should return the
        # original string
        assert _helpers._parse_request_body(body, content_type) == body.decode("utf-8")


def test_parse_request_body_json_decode_error():
    body = b'{"key": "value"}'
    content_type = "application/json"
    with mock.patch("json.loads", side_effect=json.JSONDecodeError("msg", "doc", 0)):
        # json.loads should raise a JSONDecodeError, and the function should return the
        # original string
        assert _helpers._parse_request_body(body, content_type) == body.decode("utf-8")


def test_parse_response_json_valid():
    class MockResponse:
        def json(self):
            return {"data": "test"}

    response = MockResponse()
    expected = {"data": "test"}
    assert _helpers._parse_response(response) == expected


def test_parse_response_json_invalid():
    class MockResponse:
        def json(self):
            raise json.JSONDecodeError("msg", "doc", 0)

    response = MockResponse()
    assert _helpers._parse_response(response) is None


def test_parse_response_no_json_method():
    response = "plain text"
    assert _helpers._parse_response(response) is None


def test_parse_response_none():
    assert _helpers._parse_response(None) is None


class TestUtcFromTimestamp:
    """Tests for the utcfromtimestamp utility function."""

    @pytest.mark.parametrize(
        "ts, expected",
        [
            (1704067200.0, datetime.datetime(2024, 1, 1, 0, 0, 0)),
            (0.0, datetime.datetime(1970, 1, 1, 0, 0, 0)),
            (1704067200.500123, datetime.datetime(2024, 1, 1, 0, 0, 0, 500123)),
            (-31536000.0, datetime.datetime(1969, 1, 1, 0, 0, 0)),
            (1000000000.0, datetime.datetime(2001, 9, 9, 1, 46, 40)),
        ],
        ids=[
            "standard_timestamp",
            "unix_epoch",
            "subsecond_precision",
            "negative_timestamp",
            "timezone_independence",
        ],
    )
    def test_success_cases(self, ts, expected):
        """Verify correct UTC conversion and that the result is offset-naive."""
        result = _helpers.utcfromtimestamp(ts)

        # 1. Check the datetime value is correct
        assert result == expected

        # 2. Check it is naive (tzinfo is None) for backward compatibility
        assert result.tzinfo is None

    @pytest.mark.parametrize(
        "invalid_input",
        ["string", None, [123]],
        ids=["type_string", "type_none", "type_list"],
    )
    def test_invalid_types(self, invalid_input):
        """Verify that passing invalid types raises a TypeError."""
        with pytest.raises(TypeError):
            _helpers.utcfromtimestamp(invalid_input)

    def test_out_of_range(self):
        """Test very large timestamps that exceed platform limits."""
        with pytest.raises((OverflowError, OSError, ValueError)):
            # Large enough to fail on most systems (Year 300,000+)
            _helpers.utcfromtimestamp(9999999999999)
