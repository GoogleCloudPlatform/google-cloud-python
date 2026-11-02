# Copyright 2015 Google LLC
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

import math
import types
from unittest import mock

import pytest

from google.api_core import page_iterator


def test__do_nothing_page_start():
    assert page_iterator._do_nothing_page_start(None, None, None) is None


class TestPage(object):
    def test_constructor(self):
        parent = mock.sentinel.parent
        item_to_value = mock.sentinel.item_to_value

        page = page_iterator.Page(parent, (1, 2, 3), item_to_value)

        assert page.num_items == 3
        assert page.remaining == 3
        assert page._parent is parent
        assert page._item_to_value is item_to_value
        assert page.raw_page is None

    def test___iter__(self):
        page = page_iterator.Page(None, (), None, None)
        assert iter(page) is page

    def test_iterator_calls_parent_item_to_value(self):
        parent = mock.sentinel.parent

        item_to_value = mock.Mock(
            side_effect=lambda iterator, value: value, spec=["__call__"]
        )

        page = page_iterator.Page(parent, (10, 11, 12), item_to_value)
        page._remaining = 100

        assert item_to_value.call_count == 0
        assert page.remaining == 100

        assert next(page) == 10
        assert item_to_value.call_count == 1
        item_to_value.assert_called_with(parent, 10)
        assert page.remaining == 99

        assert next(page) == 11
        assert item_to_value.call_count == 2
        item_to_value.assert_called_with(parent, 11)
        assert page.remaining == 98

        assert next(page) == 12
        assert item_to_value.call_count == 3
        item_to_value.assert_called_with(parent, 12)
        assert page.remaining == 97

    def test_raw_page(self):
        parent = mock.sentinel.parent
        item_to_value = mock.sentinel.item_to_value

        raw_page = mock.sentinel.raw_page

        page = page_iterator.Page(parent, (1, 2, 3), item_to_value, raw_page=raw_page)
        assert page.raw_page is raw_page

        with pytest.raises(AttributeError):
            page.raw_page = None


class PageIteratorImpl(page_iterator.Iterator):
    def _next_page(self):
        return mock.create_autospec(page_iterator.Page, instance=True)


class TestIterator(object):
    def test_constructor(self):
        client = mock.sentinel.client
        item_to_value = mock.sentinel.item_to_value
        token = "ab13nceor03"
        max_results = 1337

        iterator = PageIteratorImpl(
            client, item_to_value, page_token=token, max_results=max_results
        )

        assert not iterator._started
        assert iterator.client is client
        assert iterator.item_to_value == item_to_value
        assert iterator.max_results == max_results
        # Changing attributes.
        assert iterator.page_number == 0
        assert iterator.next_page_token == token
        assert iterator.num_results == 0

    def test_next(self):
        iterator = PageIteratorImpl(None, None)
        page_1 = page_iterator.Page(
            iterator, ("item 1.1", "item 1.2"), page_iterator._item_to_value_identity
        )
        page_2 = page_iterator.Page(
            iterator, ("item 2.1",), page_iterator._item_to_value_identity
        )
        iterator._next_page = mock.Mock(side_effect=[page_1, page_2, None])

        result = next(iterator)
        assert result == "item 1.1"
        result = next(iterator)
        assert result == "item 1.2"
        result = next(iterator)
        assert result == "item 2.1"

        with pytest.raises(StopIteration):
            next(iterator)

    def test_pages_property_starts(self):
        iterator = PageIteratorImpl(None, None)

        assert not iterator._started

        assert isinstance(iterator.pages, types.GeneratorType)

        assert iterator._started

    def test_pages_property_restart(self):
        iterator = PageIteratorImpl(None, None)

        assert iterator.pages

        # Make sure we cannot restart.
        with pytest.raises(ValueError):
            assert iterator.pages

    def test__page_iter_increment(self):
        iterator = PageIteratorImpl(None, None)
        page = page_iterator.Page(
            iterator, ("item",), page_iterator._item_to_value_identity
        )
        iterator._next_page = mock.Mock(side_effect=[page, None])

        assert iterator.num_results == 0

        page_iter = iterator._page_iter(increment=True)
        next(page_iter)

        assert iterator.num_results == 1

    def test__page_iter_no_increment(self):
        iterator = PageIteratorImpl(None, None)

        assert iterator.num_results == 0

        page_iter = iterator._page_iter(increment=False)
        next(page_iter)

        # results should still be 0 after fetching a page.
        assert iterator.num_results == 0

    def test__items_iter(self):
        # Items to be returned.
        item1 = 17
        item2 = 100
        item3 = 211

        # Make pages from mock responses
        parent = mock.sentinel.parent
        page1 = page_iterator.Page(
            parent, (item1, item2), page_iterator._item_to_value_identity
        )
        page2 = page_iterator.Page(
            parent, (item3,), page_iterator._item_to_value_identity
        )

        iterator = PageIteratorImpl(None, None)
        iterator._next_page = mock.Mock(side_effect=[page1, page2, None])

        items_iter = iterator._items_iter()

        assert isinstance(items_iter, types.GeneratorType)

        # Consume items and check the state of the iterator.
        assert iterator.num_results == 0

        assert next(items_iter) == item1
        assert iterator.num_results == 1

        assert next(items_iter) == item2
        assert iterator.num_results == 2

        assert next(items_iter) == item3
        assert iterator.num_results == 3

        with pytest.raises(StopIteration):
            next(items_iter)

    def test___iter__(self):
        iterator = PageIteratorImpl(None, None)
        iterator._next_page = mock.Mock(side_effect=[(1, 2), (3,), None])

        assert not iterator._started

        result = list(iterator)

        assert result == [1, 2, 3]
        assert iterator._started

    def test___iter__restart(self):
        iterator = PageIteratorImpl(None, None)

        iter(iterator)

        # Make sure we cannot restart.
        with pytest.raises(ValueError):
            iter(iterator)

    def test___iter___restart_after_page(self):
        iterator = PageIteratorImpl(None, None)

        assert iterator.pages

        # Make sure we cannot restart after starting the page iterator
        with pytest.raises(ValueError):
            iter(iterator)


class TestHTTPIterator(object):
    def test_constructor(self):
        client = mock.sentinel.client
        path = "/foo"
        iterator = page_iterator.HTTPIterator(
            client, mock.sentinel.api_request, path, mock.sentinel.item_to_value
        )

        assert not iterator._started
        assert iterator.client is client
        assert iterator.path == path
        assert iterator.item_to_value is mock.sentinel.item_to_value
        assert iterator._items_key == "items"
        assert iterator.max_results is None
        assert iterator.extra_params == {}
        assert iterator._page_start == page_iterator._do_nothing_page_start
        # Changing attributes.
        assert iterator.page_number == 0
        assert iterator.next_page_token is None
        assert iterator.num_results == 0
        assert iterator._page_size is None

    def test_constructor_w_extra_param_collision(self):
        extra_params = {"pageToken": "val"}

        with pytest.raises(ValueError):
            page_iterator.HTTPIterator(
                mock.sentinel.client,
                mock.sentinel.api_request,
                mock.sentinel.path,
                mock.sentinel.item_to_value,
                extra_params=extra_params,
            )

    def test_iterate(self):
        path = "/foo"
        item1 = {"name": "1"}
        item2 = {"name": "2"}
        api_request = mock.Mock(return_value={"items": [item1, item2]})
        iterator = page_iterator.HTTPIterator(
            mock.sentinel.client,
            api_request,
            path=path,
            item_to_value=page_iterator._item_to_value_identity,
        )

        assert iterator.num_results == 0

        items_iter = iter(iterator)

        val1 = next(items_iter)
        assert val1 == item1
        assert iterator.num_results == 1

        val2 = next(items_iter)
        assert val2 == item2
        assert iterator.num_results == 2

        with pytest.raises(StopIteration):
            next(items_iter)

        api_request.assert_called_once_with(method="GET", path=path, query_params={})

    def test__has_next_page_new(self):
        iterator = page_iterator.HTTPIterator(
            mock.sentinel.client,
            mock.sentinel.api_request,
            mock.sentinel.path,
            mock.sentinel.item_to_value,
        )

        # The iterator should *always* indicate that it has a next page
        # when created so that it can fetch the initial page.
        assert iterator._has_next_page()

    def test__has_next_page_without_token(self):
        iterator = page_iterator.HTTPIterator(
            mock.sentinel.client,
            mock.sentinel.api_request,
            mock.sentinel.path,
            mock.sentinel.item_to_value,
        )

        iterator.page_number = 1

        # The iterator should not indicate that it has a new page if the
        # initial page has been requested and there's no page token.
        assert not iterator._has_next_page()

    def test__has_next_page_w_number_w_token(self):
        iterator = page_iterator.HTTPIterator(
            mock.sentinel.client,
            mock.sentinel.api_request,
            mock.sentinel.path,
            mock.sentinel.item_to_value,
        )

        iterator.page_number = 1
        iterator.next_page_token = mock.sentinel.token

        # The iterator should indicate that it has a new page if the
        # initial page has been requested and there's is a page token.
        assert iterator._has_next_page()

    def test__has_next_page_w_max_results_not_done(self):
        iterator = page_iterator.HTTPIterator(
            mock.sentinel.client,
            mock.sentinel.api_request,
            mock.sentinel.path,
            mock.sentinel.item_to_value,
            max_results=3,
            page_token=mock.sentinel.token,
        )

        iterator.page_number = 1

        # The iterator should indicate that it has a new page if there
        # is a page token and it has not consumed more than max_results.
        assert iterator.num_results < iterator.max_results
        assert iterator._has_next_page()

    def test__has_next_page_w_max_results_done(self):
        iterator = page_iterator.HTTPIterator(
            mock.sentinel.client,
            mock.sentinel.api_request,
            mock.sentinel.path,
            mock.sentinel.item_to_value,
            max_results=3,
            page_token=mock.sentinel.token,
        )

        iterator.page_number = 1
        iterator.num_results = 3

        # The iterator should not indicate that it has a new page if there
        # if it has consumed more than max_results.
        assert iterator.num_results == iterator.max_results
        assert not iterator._has_next_page()

    def test__get_query_params_no_token(self):
        iterator = page_iterator.HTTPIterator(
            mock.sentinel.client,
            mock.sentinel.api_request,
            mock.sentinel.path,
            mock.sentinel.item_to_value,
        )

        assert iterator._get_query_params() == {}

    def test__get_query_params_w_token(self):
        iterator = page_iterator.HTTPIterator(
            mock.sentinel.client,
            mock.sentinel.api_request,
            mock.sentinel.path,
            mock.sentinel.item_to_value,
        )
        iterator.next_page_token = "token"

        assert iterator._get_query_params() == {"pageToken": iterator.next_page_token}

    def test__get_query_params_w_max_results(self):
        max_results = 3
        iterator = page_iterator.HTTPIterator(
            mock.sentinel.client,
            mock.sentinel.api_request,
            mock.sentinel.path,
            mock.sentinel.item_to_value,
            max_results=max_results,
        )

        iterator.num_results = 1
        local_max = max_results - iterator.num_results

        assert iterator._get_query_params() == {"maxResults": local_max}

    def test__get_query_params_extra_params(self):
        extra_params = {"key": "val"}
        iterator = page_iterator.HTTPIterator(
            mock.sentinel.client,
            mock.sentinel.api_request,
            mock.sentinel.path,
            mock.sentinel.item_to_value,
            extra_params=extra_params,
        )

        assert iterator._get_query_params() == extra_params

    def test__get_next_page_response_with_post(self):
        path = "/foo"
        page_response = {"items": ["one", "two"]}
        api_request = mock.Mock(return_value=page_response)
        iterator = page_iterator.HTTPIterator(
            mock.sentinel.client,
            api_request,
            path=path,
            item_to_value=page_iterator._item_to_value_identity,
        )
        iterator._HTTP_METHOD = "POST"

        response = iterator._get_next_page_response()

        assert response == page_response

        api_request.assert_called_once_with(method="POST", path=path, data={})

    def test__get_next_page_bad_http_method(self):
        iterator = page_iterator.HTTPIterator(
            mock.sentinel.client,
            mock.sentinel.api_request,
            mock.sentinel.path,
            mock.sentinel.item_to_value,
        )
        iterator._HTTP_METHOD = "NOT-A-VERB"

        with pytest.raises(ValueError):
            iterator._get_next_page_response()

    @pytest.mark.parametrize(
        "page_size,max_results,pages",
        [(3, None, False), (3, 8, False), (3, None, True), (3, 8, True)],
    )
    def test_page_size_items(self, page_size, max_results, pages):
        path = "/foo"
        NITEMS = 10

        n = [0]  # blast you python 2!

        def api_request(*args, **kw):
            assert not args
            query_params = dict(
                maxResults=(
                    page_size
                    if max_results is None
                    else min(page_size, max_results - n[0])
                )
            )
            if n[0]:
                query_params.update(pageToken="test")
            assert kw == {"method": "GET", "path": "/foo", "query_params": query_params}
            n_items = min(kw["query_params"]["maxResults"], NITEMS - n[0])
            items = [dict(name=str(i + n[0])) for i in range(n_items)]
            n[0] += n_items
            result = dict(items=items)
            if n[0] < NITEMS:
                result.update(nextPageToken="test")
            return result

        iterator = page_iterator.HTTPIterator(
            mock.sentinel.client,
            api_request,
            path=path,
            item_to_value=page_iterator._item_to_value_identity,
            page_size=page_size,
            max_results=max_results,
        )

        assert iterator.num_results == 0

        n_results = max_results if max_results is not None else NITEMS
        if pages:
            items_iter = iter(iterator.pages)
            npages = int(math.ceil(float(n_results) / page_size))
            for ipage in range(npages):
                assert list(next(items_iter)) == [
                    dict(name=str(i))
                    for i in range(
                        ipage * page_size,
                        min((ipage + 1) * page_size, n_results),
                    )
                ]
        else:
            items_iter = iter(iterator)
            for i in range(n_results):
                assert next(items_iter) == dict(name=str(i))
                assert iterator.num_results == i + 1

        with pytest.raises(StopIteration):
            next(items_iter)


class TestGRPCIterator(object):
    def test_constructor(self):
        client = mock.sentinel.client
        items_field = "items"
        iterator = page_iterator.GRPCIterator(
            client, mock.sentinel.method, mock.sentinel.request, items_field
        )

        assert not iterator._started
        assert iterator.client is client
        assert iterator.max_results is None
        assert iterator.item_to_value is page_iterator._item_to_value_identity
        assert iterator._method == mock.sentinel.method
        assert iterator._request == mock.sentinel.request
        assert iterator._items_field == items_field
        assert (
            iterator._request_token_field
            == page_iterator.GRPCIterator._DEFAULT_REQUEST_TOKEN_FIELD
        )
        assert (
            iterator._response_token_field
            == page_iterator.GRPCIterator._DEFAULT_RESPONSE_TOKEN_FIELD
        )
        # Changing attributes.
        assert iterator.page_number == 0
        assert iterator.next_page_token is None
        assert iterator.num_results == 0

    def test_constructor_options(self):
        client = mock.sentinel.client
        items_field = "items"
        request_field = "request"
        response_field = "response"
        iterator = page_iterator.GRPCIterator(
            client,
            mock.sentinel.method,
            mock.sentinel.request,
            items_field,
            item_to_value=mock.sentinel.item_to_value,
            request_token_field=request_field,
            response_token_field=response_field,
            max_results=42,
        )

        assert iterator.client is client
        assert iterator.max_results == 42
        assert iterator.item_to_value is mock.sentinel.item_to_value
        assert iterator._method == mock.sentinel.method
        assert iterator._request == mock.sentinel.request
        assert iterator._items_field == items_field
        assert iterator._request_token_field == request_field
        assert iterator._response_token_field == response_field

    def test_iterate(self):
        request = mock.Mock(spec=["page_token"], page_token=None)
        response1 = mock.Mock(items=["a", "b"], next_page_token="1")
        response2 = mock.Mock(items=["c"], next_page_token="2")
        response3 = mock.Mock(items=["d"], next_page_token="")
        method = mock.Mock(side_effect=[response1, response2, response3])
        iterator = page_iterator.GRPCIterator(
            mock.sentinel.client, method, request, "items"
        )

        assert iterator.num_results == 0

        items = list(iterator)
        assert items == ["a", "b", "c", "d"]

        method.assert_called_with(request)
        assert method.call_count == 3
        assert request.page_token == "2"

    def test_iterate_with_max_results(self):
        request = mock.Mock(spec=["page_token"], page_token=None)
        response1 = mock.Mock(items=["a", "b"], next_page_token="1")
        response2 = mock.Mock(items=["c"], next_page_token="2")
        response3 = mock.Mock(items=["d"], next_page_token="")
        method = mock.Mock(side_effect=[response1, response2, response3])
        iterator = page_iterator.GRPCIterator(
            mock.sentinel.client, method, request, "items", max_results=3
        )

        assert iterator.num_results == 0

        items = list(iterator)

        assert items == ["a", "b", "c"]
        assert iterator.num_results == 3

        method.assert_called_with(request)
        assert method.call_count == 2
        assert request.page_token == "1"


class GAXPageIterator(object):
    """Fake object that matches gax.PageIterator"""

    def __init__(self, pages, page_token=None):
        self._pages = iter(pages)
        self.page_token = page_token

    def next(self):
        return next(self._pages)

    __next__ = next


class TestGAXIterator(object):
    def test_constructor(self):
        client = mock.sentinel.client
        token = "zzzyy78kl"
        page_iter = GAXPageIterator((), page_token=token)
        item_to_value = page_iterator._item_to_value_identity
        max_results = 1337
        iterator = page_iterator._GAXIterator(
            client, page_iter, item_to_value, max_results=max_results
        )

        assert not iterator._started
        assert iterator.client is client
        assert iterator.item_to_value is item_to_value
        assert iterator.max_results == max_results
        assert iterator._gax_page_iter is page_iter
        # Changing attributes.
        assert iterator.page_number == 0
        assert iterator.next_page_token == token
        assert iterator.num_results == 0

    def test__next_page(self):
        page_items = (29, 31)
        page_token = "2sde98ds2s0hh"
        page_iter = GAXPageIterator([page_items], page_token=page_token)
        iterator = page_iterator._GAXIterator(
            mock.sentinel.client, page_iter, page_iterator._item_to_value_identity
        )

        page = iterator._next_page()

        assert iterator.next_page_token == page_token
        assert isinstance(page, page_iterator.Page)
        assert list(page) == list(page_items)

        next_page = iterator._next_page()

        assert next_page is None
