# Copyright 2019 Google LLC
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

import os
import pytest
from google import showcase


def test_pagination(echo):
    text = "The hail in Wales falls mainly on the snails."
    results = [
        i
        for i in echo.paged_expand(
            {
                "content": text,
                "page_size": 3,
            }
        )
    ]
    assert len(results) == 9
    assert results == [showcase.EchoResponse(content=i) for i in text.split(" ")]


def test_pagination_pages(echo):
    text = "The hail in Wales falls mainly on the snails."
    page_results = list(
        echo.paged_expand(
            {
                "content": text,
                "page_size": 3,
            }
        ).pages
    )

    assert len(page_results) == 3
    assert not page_results[-1].next_page_token

    # The monolithic surface uses a wrapper type that needs an explicit property
    # for a 'raw_page': we need to duplicate that interface, even though the
    # architecture is different.
    assert page_results[0].raw_page is page_results[0]

    results = [r for p in page_results for r in p.responses]
    assert results == [showcase.EchoResponse(content=i) for i in text.split(" ")]


if os.environ.get("GAPIC_PYTHON_ASYNC", "true") == "true":

    @pytest.mark.asyncio
    async def test_pagination_async(async_echo):
        text = "The hail in Wales falls mainly on the snails."
        results = []
        async for i in await async_echo.paged_expand(
            {
                "content": text,
                "page_size": 3,
            }
        ):
            results.append(i)

        assert len(results) == 9
        assert results == [showcase.EchoResponse(content=i) for i in text.split(" ")]

    @pytest.mark.asyncio
    async def test_pagination_pages_async(async_echo):
        text = "The hail in Wales falls mainly on the snails."
        page_results = []
        async for page in (
            await async_echo.paged_expand(
                {
                    "content": text,
                    "page_size": 3,
                }
            )
        ).pages:
            page_results.append(page)

        assert len(page_results) == 3
        assert not page_results[-1].next_page_token

        # The monolithic surface uses a wrapper type that needs an explicit property
        # for a 'raw_page': we need to duplicate that interface, even though the
        # architecture is different.
        assert page_results[0].raw_page is page_results[0]

        results = [r for p in page_results for r in p.responses]
        assert results == [showcase.EchoResponse(content=i) for i in text.split(" ")]
