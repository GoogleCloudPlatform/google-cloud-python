# Copyright 2021 Google LLC
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

import datetime
import logging
import random
import time
from typing import List
from unittest.mock import patch

import proto
import pytest
import requests
from google.api import http_pb2, httpbody_pb2

from google.api_core import rest_streaming

from ..helpers import Composer, EchoResponse, Song, parse_responses

__protobuf__ = proto.module(package=__name__)
SEED = int(time.time())
logging.info(f"Starting sync rest streaming tests with random seed: {SEED}")
random.seed(SEED)


class ResponseMock(requests.Response):
    class _ResponseItr:
        def __init__(self, _response_bytes: bytes, random_split=False):
            self._responses_bytes = _response_bytes
            self._i = 0
            self._random_split = random_split

        def __next__(self):
            if self._i == len(self._responses_bytes):
                raise StopIteration
            if self._random_split:
                n = random.randint(1, len(self._responses_bytes[self._i :]))
            else:
                n = 1
            x = self._responses_bytes[self._i : self._i + n]
            self._i += n
            return x.decode("utf-8")

    def __init__(
        self,
        responses: List[proto.Message],
        response_cls,
        random_split=False,
    ):
        super().__init__()
        self._responses = responses
        self._random_split = random_split
        self._response_message_cls = response_cls

    def _parse_responses(self):
        return parse_responses(self._response_message_cls, self._responses)

    def close(self):
        raise NotImplementedError()

    def iter_content(self, *args, **kwargs):
        return self._ResponseItr(
            self._parse_responses(),
            random_split=self._random_split,
        )


@pytest.mark.parametrize(
    "random_split,resp_message_is_proto_plus",
    [(False, True), (False, False)],
)
def test_next_simple(random_split, resp_message_is_proto_plus):
    if resp_message_is_proto_plus:
        response_type = EchoResponse
        responses = [EchoResponse(content="hello world"), EchoResponse(content="yes")]
    else:
        response_type = httpbody_pb2.HttpBody
        responses = [
            httpbody_pb2.HttpBody(content_type="hello world"),
            httpbody_pb2.HttpBody(content_type="yes"),
        ]

    resp = ResponseMock(
        responses=responses, random_split=random_split, response_cls=response_type
    )
    itr = rest_streaming.ResponseIterator(resp, response_type)
    assert list(itr) == responses


@pytest.mark.parametrize(
    "random_split,resp_message_is_proto_plus",
    [
        (True, True),
        (False, True),
        (True, False),
        (False, False),
    ],
)
def test_next_nested(random_split, resp_message_is_proto_plus):
    if resp_message_is_proto_plus:
        response_type = Song
        responses = [
            Song(title="some song", composer=Composer(given_name="some name")),
            Song(title="another song", date_added=datetime.datetime(2021, 12, 17)),
        ]
    else:
        # Although `http_pb2.HttpRule`` is used in the response, any response message
        # can be used which meets this criteria for the test of having a nested field.
        response_type = http_pb2.HttpRule
        responses = [
            http_pb2.HttpRule(
                selector="some selector",
                custom=http_pb2.CustomHttpPattern(kind="some kind"),
            ),
            http_pb2.HttpRule(
                selector="another selector",
                custom=http_pb2.CustomHttpPattern(path="some path"),
            ),
        ]
    resp = ResponseMock(
        responses=responses, random_split=random_split, response_cls=response_type
    )
    itr = rest_streaming.ResponseIterator(resp, response_type)
    assert list(itr) == responses


@pytest.mark.parametrize(
    "random_split,resp_message_is_proto_plus",
    [
        (True, True),
        (False, True),
        (True, False),
        (False, False),
    ],
)
def test_next_stress(random_split, resp_message_is_proto_plus):
    n = 50
    if resp_message_is_proto_plus:
        response_type = Song
        responses = [
            Song(title="title_%d" % i, composer=Composer(given_name="name_%d" % i))
            for i in range(n)
        ]
    else:
        response_type = http_pb2.HttpRule
        responses = [
            http_pb2.HttpRule(
                selector="selector_%d" % i,
                custom=http_pb2.CustomHttpPattern(path="path_%d" % i),
            )
            for i in range(n)
        ]
    resp = ResponseMock(
        responses=responses, random_split=random_split, response_cls=response_type
    )
    itr = rest_streaming.ResponseIterator(resp, response_type)
    assert list(itr) == responses


@pytest.mark.parametrize(
    "random_split,resp_message_is_proto_plus",
    [
        (True, True),
        (False, True),
        (True, False),
        (False, False),
    ],
)
def test_next_escaped_characters_in_string(random_split, resp_message_is_proto_plus):
    if resp_message_is_proto_plus:
        response_type = Song
        composer_with_relateds = Composer()
        relateds = ["Artist A", "Artist B"]
        composer_with_relateds.relateds = relateds

        responses = [
            Song(
                title='ti"tle\nfoo\tbar{}', composer=Composer(given_name="name\n\n\n")
            ),
            Song(
                title='{"this is weird": "totally"}',
                composer=Composer(given_name="\\{}\\"),
            ),
            Song(title='\\{"key": ["value",]}\\', composer=composer_with_relateds),
        ]
    else:
        response_type = http_pb2.Http
        responses = [
            http_pb2.Http(
                rules=[
                    http_pb2.HttpRule(
                        selector='ti"tle\nfoo\tbar{}',
                        custom=http_pb2.CustomHttpPattern(kind="name\n\n\n"),
                    )
                ]
            ),
            http_pb2.Http(
                rules=[
                    http_pb2.HttpRule(
                        selector='{"this is weird": "totally"}',
                        custom=http_pb2.CustomHttpPattern(kind="\\{}\\"),
                    )
                ]
            ),
            http_pb2.Http(
                rules=[
                    http_pb2.HttpRule(
                        selector='\\{"key": ["value",]}\\',
                        custom=http_pb2.CustomHttpPattern(kind="\\{}\\"),
                    )
                ]
            ),
        ]
    resp = ResponseMock(
        responses=responses, random_split=random_split, response_cls=response_type
    )
    itr = rest_streaming.ResponseIterator(resp, response_type)
    assert list(itr) == responses


@pytest.mark.parametrize("response_type", [EchoResponse, httpbody_pb2.HttpBody])
def test_next_not_array(response_type):
    with patch.object(
        ResponseMock, "iter_content", return_value=iter('{"hello": 0}')
    ) as mock_method:
        resp = ResponseMock(responses=[], response_cls=response_type)
        itr = rest_streaming.ResponseIterator(resp, response_type)
        with pytest.raises(ValueError):
            next(itr)
        mock_method.assert_called_once()


@pytest.mark.parametrize("response_type", [EchoResponse, httpbody_pb2.HttpBody])
def test_cancel(response_type):
    with patch.object(ResponseMock, "close", return_value=None) as mock_method:
        resp = ResponseMock(responses=[], response_cls=response_type)
        itr = rest_streaming.ResponseIterator(resp, response_type)
        itr.cancel()
        mock_method.assert_called_once()


@pytest.mark.parametrize(
    "response_type,return_value",
    [
        (EchoResponse, bytes('[{"content": "hello"}, {', "utf-8")),
        (httpbody_pb2.HttpBody, bytes('[{"content_type": "hello"}, {', "utf-8")),
    ],
)
def test_check_buffer(response_type, return_value):
    with patch.object(
        ResponseMock,
        "_parse_responses",
        return_value=return_value,
    ):
        resp = ResponseMock(responses=[], response_cls=response_type)
        itr = rest_streaming.ResponseIterator(resp, response_type)
        with pytest.raises(ValueError):
            next(itr)
            next(itr)


@pytest.mark.parametrize("response_type", [EchoResponse, httpbody_pb2.HttpBody])
def test_next_html(response_type):
    with patch.object(
        ResponseMock, "iter_content", return_value=iter("<!DOCTYPE html><html></html>")
    ) as mock_method:
        resp = ResponseMock(responses=[], response_cls=response_type)
        itr = rest_streaming.ResponseIterator(resp, response_type)
        with pytest.raises(ValueError):
            next(itr)
        mock_method.assert_called_once()


def test_invalid_response_class():
    class SomeClass:
        pass

    resp = ResponseMock(responses=[], response_cls=SomeClass)
    with pytest.raises(
        ValueError,
        match="Response message class must be a subclass of proto.Message or google.protobuf.message.Message",
    ):
        rest_streaming.ResponseIterator(resp, SomeClass)
