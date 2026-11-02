# Copyright 2025 Google LLC All rights reserved.
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
# limitations under the License

import mock
import pytest
from google.protobuf.timestamp_pb2 import Timestamp

from google.cloud.firestore_v1._helpers import encode_value
from google.cloud.firestore_v1.pipeline_expressions import Constant
from google.cloud.firestore_v1.pipeline_result import (
    AsyncPipelineStream,
    PipelineResult,
    PipelineSnapshot,
    PipelineStream,
)
from google.cloud.firestore_v1.query_profile import (
    PipelineExplainOptions,
    QueryExplainError,
)
from google.cloud.firestore_v1.types.document import Document
from google.cloud.firestore_v1.types.firestore import ExecutePipelineResponse

_mock_stream_responses = [
    ExecutePipelineResponse(
        results=[Document(name="projects/p/databases/d/documents/c/d1", fields={})],
        execution_time=Timestamp(seconds=1, nanos=2),
        explain_stats={"data": {}},
    ),
    ExecutePipelineResponse(
        results=[Document(name="projects/p/databases/d/documents/c/d2", fields={})],
        execution_time=Timestamp(seconds=3, nanos=4),
    ),
]


class TestPipelineResult:
    def _make_one(self, *args, **kwargs):
        if not args:
            # use defaults if not passed
            args = [mock.Mock(), {}]
        return PipelineResult(*args, **kwargs)

    def test_ref(self):
        expected = object()
        instance = self._make_one(ref=expected)
        assert instance.ref == expected
        # should be None if not set
        assert self._make_one().ref is None

    def test_id(self):
        ref = mock.Mock()
        ref.id = "test"
        instance = self._make_one(ref=ref)
        assert instance.id == "test"
        # should be None if not set
        assert self._make_one().id is None

    def test_create_time(self):
        expected = object()
        instance = self._make_one(create_time=expected)
        assert instance.create_time == expected
        # should be None if not set
        assert self._make_one().create_time is None

    def test_update_time(self):
        expected = object()
        instance = self._make_one(update_time=expected)
        assert instance.update_time == expected
        # should be None if not set
        assert self._make_one().update_time is None

    def test_exection_time(self):
        expected = object()
        instance = self._make_one(execution_time=expected)
        assert instance.execution_time == expected
        # should raise if not set
        with pytest.raises(ValueError) as e:
            self._make_one().execution_time
            assert "execution_time" in e

    @pytest.mark.parametrize(
        "first,second,result",
        [
            ((object(), {}), (object(), {}), True),
            ((object(), {1: 1}), (object(), {1: 1}), True),
            ((object(), {1: 1}), (object(), {2: 2}), False),
            ((object(), {}, "ref"), (object(), {}, "ref"), True),
            ((object(), {}, "ref"), (object(), {}, "diff"), False),
            ((object(), {1: 1}, "ref"), (object(), {1: 1}, "ref"), True),
            ((object(), {1: 1}, "ref"), (object(), {2: 2}, "ref"), False),
            ((object(), {1: 1}, "ref"), (object(), {1: 1}, "diff"), False),
            (
                (object(), {1: 1}, "ref", 1, 2, 3),
                (object(), {1: 1}, "ref", 4, 5, 6),
                True,
            ),
        ],
    )
    def test_eq(self, first, second, result):
        first_obj = self._make_one(*first)
        second_obj = self._make_one(*second)
        assert (first_obj == second_obj) is result

    def test_eq_wrong_type(self):
        instance = self._make_one()
        result = instance == object()
        assert result is False

    def test_data(self):
        from google.cloud.firestore_v1.types.document import Value

        client = mock.Mock()
        data = {"str": Value(string_value="hello world"), "int": Value(integer_value=5)}
        instance = self._make_one(client, data)
        got = instance.data()
        assert len(got) == 2
        assert got["str"] == "hello world"
        assert got["int"] == 5

    def test_data_none(self):
        client = object()
        data = None
        instance = self._make_one(client, data)
        assert instance.data() is None

    def test_data_call(self):
        """
        ensure decode_dict is called on .data
        """
        client = object()
        data = {"hello": "world"}
        instance = self._make_one(client, data)
        with mock.patch(
            "google.cloud.firestore_v1._helpers.decode_dict"
        ) as decode_mock:
            got = instance.data()
            decode_mock.assert_called_once_with(data, client)
            assert got == decode_mock.return_value

    def test_get(self):
        from google.cloud.firestore_v1.types.document import Value

        client = object()
        data = {"key": Value(string_value="hello world")}
        instance = self._make_one(client, data)
        got = instance.get("key")
        assert got == "hello world"

    def test_get_nested(self):
        from google.cloud.firestore_v1.types.document import Value

        client = object()
        data = {"first": {"second": Value(string_value="hello world")}}
        instance = self._make_one(client, data)
        got = instance.get("first.second")
        assert got == "hello world"

    def test_get_field_path(self):
        from google.cloud.firestore_v1.field_path import FieldPath
        from google.cloud.firestore_v1.types.document import Value

        client = object()
        data = {"first": {"second": Value(string_value="hello world")}}
        path = FieldPath.from_string("first.second")
        instance = self._make_one(client, data)
        got = instance.get(path)
        assert got == "hello world"

    def test_get_failure(self):
        """
        test calling get on value not in data
        """
        client = object()
        data = {}
        instance = self._make_one(client, data)
        with pytest.raises(KeyError):
            instance.get("key")

    def test_get_call(self):
        """
        ensure decode_value is called on .get()
        """
        client = object()
        data = {"key": "value"}
        instance = self._make_one(client, data)
        with mock.patch(
            "google.cloud.firestore_v1._helpers.decode_value"
        ) as decode_mock:
            got = instance.get("key")
            decode_mock.assert_called_once_with("value", client)
            assert got == decode_mock.return_value


class TestPipelineSnapshot:
    def _make_one(self, *args, **kwargs):
        if not args:
            # use defaults if not passed
            args = [[], mock.Mock()]
        return PipelineSnapshot(*args, **kwargs)

    def test_ctor(self):
        in_arr = [1, 2, 3]
        expected_type = object()
        expected_pipeline = mock.Mock()
        expected_transaction = object()
        expected_read_time = 123
        expected_explain_options = object()
        expected_addtl_options = {}
        source = PipelineStream(
            expected_type,
            expected_pipeline,
            expected_transaction,
            expected_read_time,
            expected_explain_options,
            expected_addtl_options,
        )
        instance = self._make_one(in_arr, source)
        assert instance._return_type == expected_type
        assert instance.pipeline == expected_pipeline
        assert instance._client == expected_pipeline._client
        assert instance._additonal_options == expected_addtl_options
        assert instance._explain_options == expected_explain_options
        assert instance._explain_stats is None
        assert instance._started is True
        assert instance.execution_time is None
        assert instance.transaction == expected_transaction
        assert instance._read_time == expected_read_time

    def test_list_methods(self):
        instance = self._make_one(list(range(10)), mock.Mock())
        assert isinstance(instance, list)
        assert len(instance) == 10
        assert instance[0] == 0
        assert instance[-1] == 9

    def test_explain_stats(self):
        instance = self._make_one()
        expected_stats = mock.Mock()
        instance._explain_stats = expected_stats
        assert instance.explain_stats == expected_stats
        # test different failure modes
        instance._explain_stats = None
        instance._explain_options = None
        # fail if explain_stats set without explain_options
        with pytest.raises(QueryExplainError) as e:
            instance.explain_stats
        assert "explain_options not set" in str(e)
        # fail if explain_stats missing
        instance._explain_options = object()
        with pytest.raises(QueryExplainError) as e:
            instance.explain_stats
        assert "explain_stats not found" in str(e)


class SharedStreamTests:
    """
    Shared test logic for PipelineStream and AsyncPipelineStream
    """

    def _make_one(self, *args, **kwargs):
        raise NotImplementedError

    def _mock_init_args(self):
        # return default mocks for all init args
        from google.cloud.firestore_v1.pipeline import Pipeline

        return {
            "return_type": PipelineResult,
            "pipeline": Pipeline(mock.Mock()),
            "transaction": None,
            "read_time": None,
            "explain_options": None,
            "additional_options": {},
        }

    def test_explain_stats(self):
        instance = self._make_one()
        expected_stats = mock.Mock()
        instance._started = True
        instance._explain_stats = expected_stats
        assert instance.explain_stats == expected_stats
        # test different failure modes
        instance._explain_stats = None
        instance._explain_options = None
        # fail if explain_stats set without explain_options
        with pytest.raises(QueryExplainError) as e:
            instance.explain_stats
        assert "explain_options not set" in str(e)
        # fail if explain_stats missing
        instance._explain_options = object()
        with pytest.raises(QueryExplainError) as e:
            instance.explain_stats
        assert "explain_stats not found" in str(e)
        # fail if not started
        instance._started = False
        with pytest.raises(QueryExplainError) as e:
            instance.explain_stats
        assert "not available until query is complete" in str(e)

    @pytest.mark.parametrize(
        "init_kwargs,expected_options",
        [
            (
                {"explain_options": PipelineExplainOptions()},
                {"explain_options": encode_value({"mode": "analyze"})},
            ),
            (
                {"explain_options": PipelineExplainOptions(mode="explain")},
                {"explain_options": encode_value({"mode": "explain"})},
            ),
            (
                {"additional_options": {"explain_options": Constant("custom")}},
                {"explain_options": encode_value("custom")},
            ),
            (
                {"additional_options": {"explain_options": encode_value("custom")}},
                {"explain_options": encode_value("custom")},
            ),
            (
                {
                    "explain_options": PipelineExplainOptions(),
                    "additional_options": {"explain_options": Constant.of("override")},
                },
                {"explain_options": encode_value("override")},
            ),
        ],
    )
    def test_build_request_options(self, init_kwargs, expected_options):
        """
        Certain Arguments to PipelineStream should be passed to `options` field in proto request
        """
        instance = self._make_one(**init_kwargs)
        request = instance._build_request()
        options = dict(request.structured_pipeline.options)
        assert options == expected_options
        assert len(options) == len(expected_options)

    def test_build_request_transaction(self):
        """Ensure transaction is passed down when building request"""
        from google.cloud.firestore_v1.transaction import Transaction

        expected_id = b"expected"
        transaction = Transaction(mock.Mock())
        transaction._id = expected_id
        instance = self._make_one(transaction=transaction)
        request = instance._build_request()
        assert request.transaction == expected_id

    def test_build_request_read_time(self):
        """Ensure readtime is passed down when building request"""
        import datetime

        ts = datetime.datetime.now()
        instance = self._make_one(read_time=ts)
        request = instance._build_request()
        assert request.read_time.timestamp() == ts.timestamp()


class TestPipelineStream(SharedStreamTests):
    def _make_one(self, **kwargs):
        init_kwargs = self._mock_init_args()
        init_kwargs.update(kwargs)
        return PipelineStream(**init_kwargs)

    def test_explain_stats(self):
        instance = self._make_one()
        expected_stats = mock.Mock()
        instance._started = True
        instance._explain_stats = expected_stats
        assert instance.explain_stats == expected_stats
        # test different failure modes
        instance._explain_stats = None
        instance._explain_options = None
        # fail if explain_stats set without explain_options
        with pytest.raises(QueryExplainError) as e:
            instance.explain_stats
        assert "explain_options not set" in str(e)
        # fail if explain_stats missing
        instance._explain_options = object()
        with pytest.raises(QueryExplainError) as e:
            instance.explain_stats
        assert "explain_stats not found" in str(e)
        # fail if not started
        instance._started = False
        with pytest.raises(QueryExplainError) as e:
            instance.explain_stats
        assert "not available until query is complete" in str(e)

    def test_iter(self):
        pipeline = mock.Mock()
        pipeline._client.project = "project-id"
        pipeline._client._database = "database-id"
        pipeline._client.document.side_effect = lambda path: mock.Mock(
            id=path.split("/")[-1]
        )
        pipeline._to_pb.return_value = {}

        instance = self._make_one(pipeline=pipeline)

        instance._client._firestore_api.execute_pipeline.return_value = (
            _mock_stream_responses
        )

        results = list(instance)

        assert len(results) == 2
        assert isinstance(results[0], PipelineResult)
        assert results[0].id == "d1"
        assert isinstance(results[1], PipelineResult)
        assert results[1].id == "d2"

        assert instance.execution_time.seconds == 1
        assert instance.execution_time.nanos == 2

        # expect empty stats
        got_stats = instance.explain_stats.get_raw().data
        assert got_stats.value == b""

        instance._client._firestore_api.execute_pipeline.assert_called_once()

    def test_double_iterate(self):
        instance = self._make_one()
        instance._client._firestore_api.execute_pipeline.return_value = []
        # consume the iterator
        list(instance)
        with pytest.raises(RuntimeError):
            list(instance)


class TestAsyncPipelineStream(SharedStreamTests):
    def _make_one(self, **kwargs):
        init_kwargs = self._mock_init_args()
        init_kwargs.update(kwargs)
        return AsyncPipelineStream(**init_kwargs)

    @pytest.mark.asyncio
    async def test_aiter(self):
        pipeline = mock.Mock()
        pipeline._client.project = "project-id"
        pipeline._client._database = "database-id"
        pipeline._client.document.side_effect = lambda path: mock.Mock(
            id=path.split("/")[-1]
        )
        pipeline._to_pb.return_value = {}

        instance = self._make_one(pipeline=pipeline)

        async def async_gen(items):
            for item in items:
                yield item

        instance._client._firestore_api.execute_pipeline = mock.AsyncMock(
            return_value=async_gen(_mock_stream_responses)
        )

        results = [item async for item in instance]

        assert len(results) == 2
        assert isinstance(results[0], PipelineResult)
        assert results[0].id == "d1"
        assert isinstance(results[1], PipelineResult)
        assert results[1].id == "d2"

        assert instance.execution_time.seconds == 1
        assert instance.execution_time.nanos == 2

        # expect empty stats
        got_stats = instance.explain_stats.get_raw().data
        assert got_stats.value == b""

        instance._client._firestore_api.execute_pipeline.assert_called_once()

    @pytest.mark.asyncio
    async def test_double_iterate(self):
        instance = self._make_one()

        async def async_gen(items):
            for item in items:
                yield item  # pragma: NO COVER

        # mock the api call to avoid real network requests
        instance._client._firestore_api.execute_pipeline = mock.AsyncMock(
            return_value=async_gen([])
        )

        # consume the iterator
        [item async for item in instance]
        # should fail on second attempt
        with pytest.raises(RuntimeError):
            [item async for item in instance]
