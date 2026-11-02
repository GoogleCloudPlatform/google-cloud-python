# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import os
import pytest
import threading
from google import showcase


# `_METADATA` will be sent as part of the request, and the
# showcase server will echo it (since it has key 'showcase-trailer') as trailing
# metadata.
_METADATA = (("showcase-trailer", "hello world"),)


def test_unary_stream(echo):
    content = "The hail in Wales falls mainly on the snails."
    responses = echo.expand(
        {
            "content": content,
        },
        metadata=_METADATA,
    )

    # Consume the response and ensure it matches what we expect.
    # with pytest.raises(exceptions.NotFound) as exc:
    for ground_truth, response in zip(content.split(" "), responses):
        assert response.content == ground_truth
    assert ground_truth == "snails."
    if isinstance(echo.transport, type(echo).get_transport_class("grpc")):
        response_metadata = [
            (metadata.key, metadata.value) for metadata in responses.trailing_metadata()
        ]
        assert _METADATA[0] in response_metadata
    else:
        showcase_header = f"X-Showcase-Request-{_METADATA[0][0]}"
        assert showcase_header in responses._response.headers
        assert responses._response.headers[showcase_header] == _METADATA[0][1]


def test_stream_unary(echo):
    if isinstance(echo.transport, type(echo).get_transport_class("rest")):
        # (TODO: dovs) Temporarily disabling rest
        return

    requests = []
    requests.append(showcase.EchoRequest(content="hello"))
    requests.append(showcase.EchoRequest(content="world!"))
    response = echo.collect(iter(requests))
    assert response.content == "hello world!"


def test_stream_unary_passing_dict(echo):
    if isinstance(echo.transport, type(echo).get_transport_class("rest")):
        # (TODO: dovs) Temporarily disabling rest
        return

    requests = [{"content": "hello"}, {"content": "world!"}]
    response = echo.collect(iter(requests))
    assert response.content == "hello world!"


def test_stream_stream(echo):
    if isinstance(echo.transport, type(echo).get_transport_class("rest")):
        # (TODO: dovs) Temporarily disabling rest
        return

    requests = []
    requests.append(showcase.EchoRequest(content="hello"))
    requests.append(showcase.EchoRequest(content="world!"))
    responses = echo.chat(iter(requests), metadata=_METADATA)

    contents = []
    for response in responses:
        contents.append(response.content)
    assert contents == ["hello", "world!"]

    response_metadata = [
        (metadata.key, metadata.value) for metadata in responses.trailing_metadata()
    ]
    assert _METADATA[0] in response_metadata


def test_stream_stream_passing_dict(echo):
    if isinstance(echo.transport, type(echo).get_transport_class("rest")):
        # (TODO: dovs) Temporarily disabling rest
        return

    requests = [{"content": "hello"}, {"content": "world!"}]
    responses = echo.chat(iter(requests), metadata=_METADATA)

    contents = []
    for response in responses:
        contents.append(response.content)
    assert contents == ["hello", "world!"]

    response_metadata = [
        (metadata.key, metadata.value) for metadata in responses.trailing_metadata()
    ]
    assert _METADATA[0] in response_metadata


if os.environ.get("GAPIC_PYTHON_ASYNC", "true") == "true":
    import asyncio

    @pytest.mark.asyncio
    async def test_async_unary_stream_reader(async_echo):
        content = "The hail in Wales falls mainly on the snails."
        stream = await async_echo.expand(
            {
                "content": content,
            },
            metadata=_METADATA,
        )

        # Note: gRPC exposes `read`, REST exposes `__anext__` to read
        # a chunk of response from the stream.
        response_attr = (
            "__anext__" if "rest" in str(async_echo.transport).lower() else "read"
        )

        # Consume the response and ensure it matches what we expect.
        for ground_truth in content.split(" "):
            response = await getattr(stream, response_attr)()
            assert response.content == ground_truth
        assert ground_truth == "snails."

        # Note: trailing metadata is part of a gRPC response.
        if "grpc" in str(async_echo.transport).lower():
            trailing_metadata = await stream.trailing_metadata()
            assert _METADATA[0] in list(trailing_metadata)

    @pytest.mark.asyncio
    async def test_async_unary_stream_async_generator(async_echo):
        content = "The hail in Wales falls mainly on the snails."
        stream = await async_echo.expand(
            {
                "content": content,
            },
            metadata=_METADATA,
        )

        # Consume the response and ensure it matches what we expect.
        tokens = iter(content.split(" "))
        async for response in stream:
            ground_truth = next(tokens)
            assert response.content == ground_truth
        assert ground_truth == "snails."

        # Note: trailing metadata is part of a gRPC response.
        if "grpc" in str(async_echo.transport).lower():
            trailing_metadata = await stream.trailing_metadata()
            assert _METADATA[0] in list(trailing_metadata)

    @pytest.mark.asyncio
    async def test_async_stream_unary_iterable(async_echo):
        # TODO(https://github.com/googleapis/gapic-generator-python/issues/2169): Add test for async rest client-streaming.
        # NOTE: There are currently no plans for supporting async rest client-streaming.
        if "rest" in str(async_echo.transport).lower():
            with pytest.raises(NotImplementedError):
                call = await async_echo.collect()
            return

        requests = []
        requests.append(showcase.EchoRequest(content="hello"))
        requests.append(showcase.EchoRequest(content="world!"))

        call = await async_echo.collect(requests)
        response = await call
        assert response.content == "hello world!"

    @pytest.mark.asyncio
    async def test_async_stream_unary_async_generator(async_echo):
        # TODO(https://github.com/googleapis/gapic-generator-python/issues/2169): Add test for async rest client-streaming.
        # NOTE: There are currently no plans for supporting async rest client-streaming.
        if "rest" in str(async_echo.transport).lower():
            with pytest.raises(NotImplementedError):
                call = await async_echo.collect()
            return

        async def async_generator():
            yield showcase.EchoRequest(content="hello")
            yield showcase.EchoRequest(content="world!")

        call = await async_echo.collect(async_generator())
        response = await call
        assert response.content == "hello world!"

    @pytest.mark.asyncio
    async def test_async_stream_unary_writer(async_echo):
        # TODO(https://github.com/googleapis/gapic-generator-python/issues/2169): Add test for async rest client-streaming.
        # NOTE: There are currently no plans for supporting async rest client-streaming.
        if "rest" in str(async_echo.transport).lower():
            with pytest.raises(NotImplementedError):
                call = await async_echo.collect()
            return
        call = await async_echo.collect()
        await call.write(showcase.EchoRequest(content="hello"))
        await call.write(showcase.EchoRequest(content="world!"))
        await call.done_writing()

        response = await call
        assert response.content == "hello world!"

    @pytest.mark.asyncio
    async def test_async_stream_unary_passing_dict(async_echo):
        # TODO(https://github.com/googleapis/gapic-generator-python/issues/2169): Add test for async rest client-streaming.
        # NOTE: There are currently no plans for supporting async rest client-streaming.
        if "rest" in str(async_echo.transport).lower():
            with pytest.raises(NotImplementedError):
                call = await async_echo.collect()
            return

        requests = [{"content": "hello"}, {"content": "world!"}]
        call = await async_echo.collect(iter(requests))
        response = await call
        assert response.content == "hello world!"

    @pytest.mark.asyncio
    async def test_async_stream_stream_reader_writier(async_echo):
        # TODO(https://github.com/googleapis/gapic-generator-python/issues/2169): Add test for async rest client-streaming.
        # NOTE: There are currently no plans for supporting async rest client-streaming.
        if "rest" in str(async_echo.transport).lower():
            with pytest.raises(NotImplementedError):
                call = await async_echo.chat(metadata=_METADATA)
            return

        call = await async_echo.chat(metadata=_METADATA)
        await call.write(showcase.EchoRequest(content="hello"))
        await call.write(showcase.EchoRequest(content="world!"))
        await call.done_writing()

        contents = [(await call.read()).content, (await call.read()).content]
        assert contents == ["hello", "world!"]

        trailing_metadata = await call.trailing_metadata()
        assert _METADATA[0] in list(trailing_metadata)

    @pytest.mark.asyncio
    async def test_async_stream_stream_async_generator(async_echo):
        # TODO(https://github.com/googleapis/gapic-generator-python/issues/2169): Add test for async rest client-streaming.
        # NOTE: There are currently no plans for supporting async rest client-streaming.
        if "rest" in str(async_echo.transport).lower():
            with pytest.raises(NotImplementedError):
                call = await async_echo.chat(metadata=_METADATA)
            return

        async def async_generator():
            yield showcase.EchoRequest(content="hello")
            yield showcase.EchoRequest(content="world!")

        call = await async_echo.chat(async_generator(), metadata=_METADATA)

        contents = []
        async for response in call:
            contents.append(response.content)
        assert contents == ["hello", "world!"]

        trailing_metadata = await call.trailing_metadata()
        assert _METADATA[0] in list(trailing_metadata)

    @pytest.mark.asyncio
    async def test_async_stream_stream_passing_dict(async_echo):
        # TODO(https://github.com/googleapis/gapic-generator-python/issues/2169): Add test for async rest client-streaming.
        # NOTE: There are currently no plans for supporting async rest client-streaming.
        if "rest" in str(async_echo.transport).lower():
            with pytest.raises(NotImplementedError):
                call = await async_echo.chat(metadata=_METADATA)
            return

        requests = [{"content": "hello"}, {"content": "world!"}]
        call = await async_echo.chat(iter(requests), metadata=_METADATA)

        contents = []
        async for response in call:
            contents.append(response.content)
        assert contents == ["hello", "world!"]

        trailing_metadata = await call.trailing_metadata()
        assert _METADATA[0] in list(trailing_metadata)
