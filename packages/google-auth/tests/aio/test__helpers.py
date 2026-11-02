# Copyright 2025 Google LLC
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

import json
import logging

import pytest  # type: ignore

from google.auth.aio import _helpers

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


@pytest.mark.asyncio
async def test_response_log_debug_enabled(logger, caplog, base_logger):
    caplog.set_level(logging.DEBUG, logger=_MOCK_CHILD_LOGGER_NAME)
    await _helpers.response_log_async(logger, {"payload": None})
    assert len(caplog.records) == 1
    record = caplog.records[0]
    assert record.message == "Response received..."
    assert record.httpResponse == "<class 'NoneType'>"


@pytest.mark.asyncio
async def test_response_log_debug_disabled(logger, caplog, base_logger):
    caplog.set_level(logging.INFO, logger=_MOCK_CHILD_LOGGER_NAME)
    await _helpers.response_log_async(logger, "another_response")
    assert "Response received..." not in caplog.text


@pytest.mark.asyncio
async def test_response_log_debug_enabled_response_json(logger, caplog, base_logger):
    response = None
    caplog.set_level(logging.DEBUG, logger=_MOCK_CHILD_LOGGER_NAME)
    await _helpers.response_log_async(logger, response)
    assert len(caplog.records) == 1
    record = caplog.records[0]
    assert record.message == "Response received..."
    assert record.httpResponse == "<class 'NoneType'>"


@pytest.mark.asyncio
async def test_parse_response_async_json_valid():
    class MockResponse:
        async def json(self):
            return {"data": "test"}

    response = MockResponse()
    expected = {"data": "test"}
    assert await _helpers._parse_response_async(response) == expected


@pytest.mark.asyncio
async def test_parse_response_async_json_invalid():
    class MockResponse:
        def json(self):
            raise json.JSONDecodeError("msg", "doc", 0)

    response = MockResponse()
    assert await _helpers._parse_response_async(response) is None


@pytest.mark.asyncio
async def test_parse_response_async_no_json_method():
    response = "plain text"
    assert await _helpers._parse_response_async(response) is None


@pytest.mark.asyncio
async def test_parse_response_async_none():
    assert await _helpers._parse_response_async(None) is None
