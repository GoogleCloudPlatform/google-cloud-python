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

from google.cloud.firestore_v1 import pipeline_stages as stages
from google.cloud.firestore_v1.pipeline_expressions import Field
from tests.unit.v1._test_helpers import make_client


def _make_pipeline(*args, client=mock.Mock()):
    from google.cloud.firestore_v1.pipeline import Pipeline

    return Pipeline._create_with_stages(client, *args)


def test_ctor():
    from google.cloud.firestore_v1.pipeline import Pipeline

    client = object()
    instance = Pipeline(client)
    assert instance._client == client
    assert len(instance.stages) == 0


def test_create():
    from google.cloud.firestore_v1.pipeline import Pipeline

    client = object()
    stages = [object() for i in range(10)]
    instance = Pipeline._create_with_stages(client, *stages)
    assert instance._client == client
    assert len(instance.stages) == 10
    assert instance.stages[0] == stages[0]
    assert instance.stages[-1] == stages[-1]


def test_pipeline_repr_empty():
    ppl = _make_pipeline()
    repr_str = repr(ppl)
    assert repr_str == "Pipeline()"


def test_pipeline_repr_single_stage():
    stage = mock.Mock()
    stage.__repr__ = lambda x: "SingleStage"
    ppl = _make_pipeline(stage)
    repr_str = repr(ppl)
    assert repr_str == "Pipeline(SingleStage)"


def test_pipeline_repr_multiple_stage():
    stage_1 = stages.Collection("path")
    stage_2 = stages.RawStage("second", 2)
    stage_3 = stages.RawStage("third", 3)
    ppl = _make_pipeline(stage_1, stage_2, stage_3)
    repr_str = repr(ppl)
    assert repr_str == (
        "Pipeline(\n"
        "  Collection(path='/path'),\n"
        "  RawStage(name='second'),\n"
        "  RawStage(name='third')\n"
        ")"
    )


def test_pipeline_repr_long():
    num_stages = 100
    stage_list = [stages.RawStage("custom", i) for i in range(num_stages)]
    ppl = _make_pipeline(*stage_list)
    repr_str = repr(ppl)
    assert repr_str.count("RawStage") == num_stages
    assert repr_str.count("\n") == num_stages + 1


def test_pipeline__to_pb():
    from google.cloud.firestore_v1.types.pipeline import StructuredPipeline

    stage_1 = stages.RawStage("first")
    stage_2 = stages.RawStage("second")
    ppl = _make_pipeline(stage_1, stage_2)
    pb = ppl._to_pb()
    assert isinstance(pb, StructuredPipeline)
    assert pb.pipeline.stages[0] == stage_1._to_pb()
    assert pb.pipeline.stages[1] == stage_2._to_pb()


def test_pipeline__to_pb_with_options():
    from google.cloud.firestore_v1.types.document import Value
    from google.cloud.firestore_v1.types.pipeline import StructuredPipeline

    ppl = _make_pipeline()
    options = {"option_1": Value(integer_value=1)}
    pb = ppl._to_pb(**options)
    assert isinstance(pb, StructuredPipeline)
    assert pb.options["option_1"].integer_value == 1


def test_pipeline_append():
    """append should create a new pipeline with the additional stage"""

    stage_1 = stages.RawStage("first")
    ppl_1 = _make_pipeline(stage_1, client=object())
    stage_2 = stages.RawStage("second")
    ppl_2 = ppl_1._append(stage_2)
    assert ppl_1 != ppl_2
    assert len(ppl_1.stages) == 1
    assert len(ppl_2.stages) == 2
    assert ppl_2.stages[0] == stage_1
    assert ppl_2.stages[1] == stage_2
    assert ppl_1._client == ppl_2._client
    assert isinstance(ppl_2, type(ppl_1))


def test_pipeline_stream_empty():
    """
    test stream pipeline with mocked empty response
    """
    from google.cloud.firestore_v1.types import (
        ExecutePipelineRequest,
        ExecutePipelineResponse,
    )

    client = mock.Mock()
    client.project = "A"
    client._database = "B"
    mock_rpc = client._firestore_api.execute_pipeline
    mock_rpc.return_value = [ExecutePipelineResponse()]
    ppl_1 = _make_pipeline(stages.RawStage("s"), client=client)

    results = list(ppl_1.stream())
    assert results == []
    assert mock_rpc.call_count == 1
    request = mock_rpc.call_args[0][0]
    assert isinstance(request, ExecutePipelineRequest)
    assert request.structured_pipeline == ppl_1._to_pb()
    assert request.database == "projects/A/databases/B"


def test_pipeline_stream_no_doc_ref():
    """
    test stream pipeline with no doc ref
    """
    from google.cloud.firestore_v1.pipeline_result import PipelineResult
    from google.cloud.firestore_v1.types import (
        Document,
        ExecutePipelineRequest,
        ExecutePipelineResponse,
    )

    client = mock.Mock()
    client.project = "A"
    client._database = "B"
    mock_rpc = client._firestore_api.execute_pipeline
    mock_rpc.return_value = [
        ExecutePipelineResponse(results=[Document()], execution_time={"seconds": 9})
    ]
    ppl_1 = _make_pipeline(stages.RawStage("s"), client=client)

    results = list(ppl_1.stream())
    assert len(results) == 1
    assert mock_rpc.call_count == 1
    request = mock_rpc.call_args[0][0]
    assert isinstance(request, ExecutePipelineRequest)
    assert request.structured_pipeline == ppl_1._to_pb()
    assert request.database == "projects/A/databases/B"

    response = results[0]
    assert isinstance(response, PipelineResult)
    assert response.ref is None
    assert response.id is None
    assert response.create_time is None
    assert response.update_time is None
    assert response.execution_time.seconds == 9
    assert response.data() == {}


def test_pipeline_stream_populated():
    """
    test stream pipeline with fully populated doc ref
    """
    from google.cloud.firestore_v1.document import DocumentReference
    from google.cloud.firestore_v1.pipeline_result import PipelineResult
    from google.cloud.firestore_v1.types import (
        Document,
        ExecutePipelineRequest,
        ExecutePipelineResponse,
        Value,
    )

    real_client = make_client()
    client = mock.Mock()
    client.project = "A"
    client._database = "B"
    client.document = real_client.document
    mock_rpc = client._firestore_api.execute_pipeline

    mock_rpc.return_value = [
        ExecutePipelineResponse(
            results=[
                Document(
                    name="test/my_doc",
                    create_time={"seconds": 1},
                    update_time={"seconds": 2},
                    fields={"key": Value(string_value="str_val")},
                )
            ],
            execution_time={"seconds": 9},
        )
    ]
    ppl_1 = _make_pipeline(client=client)

    results = list(ppl_1.stream())
    assert len(results) == 1
    assert mock_rpc.call_count == 1
    request = mock_rpc.call_args[0][0]
    assert isinstance(request, ExecutePipelineRequest)
    assert request.structured_pipeline == ppl_1._to_pb()
    assert request.database == "projects/A/databases/B"
    assert request.transaction == b""

    response = results[0]
    assert isinstance(response, PipelineResult)
    assert isinstance(response.ref, DocumentReference)
    assert response.ref.path == "test/my_doc"
    assert response.id == "my_doc"
    assert response.create_time.seconds == 1
    assert response.update_time.seconds == 2
    assert response.execution_time.seconds == 9
    assert response.data() == {"key": "str_val"}


def test_pipeline_stream_multiple():
    """
    test stream pipeline with multiple docs and responses
    """
    from google.cloud.firestore_v1.pipeline_result import PipelineResult
    from google.cloud.firestore_v1.types import (
        Document,
        ExecutePipelineRequest,
        ExecutePipelineResponse,
        Value,
    )

    real_client = make_client()
    client = mock.Mock()
    client.project = "A"
    client._database = "B"
    client.document = real_client.document
    mock_rpc = client._firestore_api.execute_pipeline

    mock_rpc.return_value = [
        ExecutePipelineResponse(
            results=[
                Document(fields={"key": Value(integer_value=0)}),
                Document(fields={"key": Value(integer_value=1)}),
            ],
            execution_time={"seconds": 0},
        ),
        ExecutePipelineResponse(
            results=[
                Document(fields={"key": Value(integer_value=2)}),
                Document(fields={"key": Value(integer_value=3)}),
            ],
            execution_time={"seconds": 1},
        ),
    ]
    ppl_1 = _make_pipeline(client=client)

    results = list(ppl_1.stream())
    assert len(results) == 4
    assert mock_rpc.call_count == 1
    request = mock_rpc.call_args[0][0]
    assert isinstance(request, ExecutePipelineRequest)
    assert request.structured_pipeline == ppl_1._to_pb()
    assert request.database == "projects/A/databases/B"

    for idx, response in enumerate(results):
        assert isinstance(response, PipelineResult)
        assert response.data() == {"key": idx}


def test_pipeline_stream_with_transaction():
    """
    test stream pipeline with fully populated doc ref
    """
    from google.cloud.firestore_v1.transaction import Transaction
    from google.cloud.firestore_v1.types import (
        ExecutePipelineRequest,
        ExecutePipelineResponse,
    )

    client = mock.Mock()
    client.project = "A"
    client._database = "B"
    mock_rpc = client._firestore_api.execute_pipeline

    transaction = Transaction(client)
    transaction._id = b"123"

    mock_rpc.return_value = [ExecutePipelineResponse()]
    ppl_1 = _make_pipeline(client=client)

    list(ppl_1.stream(transaction=transaction))
    assert mock_rpc.call_count == 1
    request = mock_rpc.call_args[0][0]
    assert isinstance(request, ExecutePipelineRequest)
    assert request.structured_pipeline == ppl_1._to_pb()
    assert request.database == "projects/A/databases/B"
    assert request.transaction == b"123"


def test_pipeline_stream_with_read_time():
    """
    test stream pipeline with read_time
    """
    import datetime

    from google.cloud.firestore_v1.types import (
        ExecutePipelineRequest,
        ExecutePipelineResponse,
    )

    client = mock.Mock()
    client.project = "A"
    client._database = "B"
    mock_rpc = client._firestore_api.execute_pipeline

    read_time = datetime.datetime.now(tz=datetime.timezone.utc)

    mock_rpc.return_value = [ExecutePipelineResponse()]
    ppl_1 = _make_pipeline(client=client)

    list(ppl_1.stream(read_time=read_time))
    assert mock_rpc.call_count == 1
    request = mock_rpc.call_args[0][0]
    assert isinstance(request, ExecutePipelineRequest)
    assert request.structured_pipeline == ppl_1._to_pb()
    assert request.database == "projects/A/databases/B"
    assert request.read_time == read_time


def test_pipeline_execute_stream_equivalence():
    """
    Pipeline.execute should provide same results from pipeline.stream, as a list
    """
    from google.cloud.firestore_v1.types import Document, ExecutePipelineResponse, Value

    real_client = make_client()
    client = mock.Mock()
    client.project = "A"
    client._database = "B"
    client.document = real_client.document
    mock_rpc = client._firestore_api.execute_pipeline

    mock_rpc.return_value = [
        ExecutePipelineResponse(
            results=[
                Document(
                    name="test/my_doc",
                    fields={"key": Value(string_value="str_val")},
                )
            ],
        )
    ]
    ppl_1 = _make_pipeline(client=client)

    stream_results = list(ppl_1.stream())
    execute_results = ppl_1.execute()
    assert stream_results == execute_results
    assert stream_results[0].data()["key"] == "str_val"
    assert execute_results[0].data()["key"] == "str_val"


@pytest.mark.parametrize(
    "method,args,result_cls",
    [
        ("add_fields", (Field.of("n"),), stages.AddFields),
        ("remove_fields", ("name",), stages.RemoveFields),
        ("remove_fields", (Field.of("n"),), stages.RemoveFields),
        ("select", ("name",), stages.Select),
        ("select", (Field.of("n"),), stages.Select),
        ("where", (Field.of("n").exists(),), stages.Where),
        ("find_nearest", ("name", [0.1], "cosine"), stages.FindNearest),
        (
            "find_nearest",
            ("name", [0.1], "cosine", stages.FindNearestOptions(10)),
            stages.FindNearest,
        ),
        ("replace_with", ("name",), stages.ReplaceWith),
        ("replace_with", (Field.of("n"),), stages.ReplaceWith),
        ("sort", (Field.of("n").descending(),), stages.Sort),
        ("sort", (Field.of("n").descending(), Field.of("m").ascending()), stages.Sort),
        ("search", ("my query",), stages.Search),
        ("search", (stages.SearchOptions(query="my query"),), stages.Search),
        ("sample", (10,), stages.Sample),
        ("sample", (stages.SampleOptions.doc_limit(10),), stages.Sample),
        ("union", (_make_pipeline(),), stages.Union),
        ("unnest", ("field_name",), stages.Unnest),
        ("unnest", ("field_name", "alias"), stages.Unnest),
        ("unnest", (Field.of("n"), Field.of("alias")), stages.Unnest),
        ("unnest", ("n", "a", stages.UnnestOptions("idx")), stages.Unnest),
        ("raw_stage", ("stage_name",), stages.RawStage),
        ("raw_stage", ("stage_name", Field.of("n")), stages.RawStage),
        ("offset", (1,), stages.Offset),
        ("limit", (1,), stages.Limit),
        ("aggregate", (Field.of("n").as_("alias"),), stages.Aggregate),
        ("distinct", ("field_name",), stages.Distinct),
        ("distinct", (Field.of("n"), "second"), stages.Distinct),
    ],
)
def test_pipeline_methods(method, args, result_cls):
    start_ppl = _make_pipeline()
    method_ptr = getattr(start_ppl, method)
    result_ppl = method_ptr(*args)
    assert result_ppl != start_ppl
    assert len(start_ppl.stages) == 0
    assert len(result_ppl.stages) == 1
    assert isinstance(result_ppl.stages[0], result_cls)


def test_pipeline_aggregate_with_groups():
    start_ppl = _make_pipeline()
    result_ppl = start_ppl.aggregate(Field.of("title"), groups=[Field.of("author")])
    assert len(start_ppl.stages) == 0
    assert len(result_ppl.stages) == 1
    assert isinstance(result_ppl.stages[0], stages.Aggregate)
    assert list(result_ppl.stages[0].groups) == [Field.of("author")]
    assert list(result_ppl.stages[0].accumulators) == [Field.of("title")]


def test_pipeline_raw_stage_with_options():
    from google.cloud.firestore_v1.pipeline_stages import RawStage

    start_ppl = _make_pipeline()
    result_ppl = start_ppl.raw_stage(
        "stage_name", Field.of("n"), options={"key": "val"}
    )
    assert len(start_ppl.stages) == 0
    assert len(result_ppl.stages) == 1
    assert isinstance(result_ppl.stages[0], RawStage)
    assert result_ppl.stages[0].options == {"key": "val"}


def test_pipeline_union_relative_error():
    start_ppl = _make_pipeline(client=mock.Mock())
    other_ppl = _make_pipeline(client=None)
    with pytest.raises(
        ValueError, match="Union only supports combining root pipelines"
    ):
        start_ppl.union(other_ppl)


def test_subpipeline_execute_error():
    from google.cloud.firestore_v1.base_pipeline import SubPipeline

    ppl = SubPipeline._create_with_stages(None)
    with pytest.raises(
        RuntimeError, match="This pipeline was created without a database"
    ):
        ppl.execute()


def test_subpipeline_stream_error():
    from google.cloud.firestore_v1.base_pipeline import SubPipeline

    ppl = SubPipeline._create_with_stages(None)
    with pytest.raises(
        RuntimeError, match="This pipeline was created without a database"
    ):
        ppl.stream()
