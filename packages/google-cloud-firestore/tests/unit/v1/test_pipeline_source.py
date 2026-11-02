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

from google.cloud.firestore_v1 import pipeline_stages as stages
from google.cloud.firestore_v1.async_pipeline import AsyncPipeline
from google.cloud.firestore_v1.async_query import AsyncQuery
from google.cloud.firestore_v1.base_document import BaseDocumentReference
from google.cloud.firestore_v1.base_pipeline import SubPipeline
from google.cloud.firestore_v1.pipeline import Pipeline
from google.cloud.firestore_v1.pipeline_source import PipelineSource
from google.cloud.firestore_v1.query import Query
from tests.unit.v1._test_helpers import make_async_client, make_client


class TestPipelineSource:
    _expected_pipeline_type = Pipeline

    def _make_client(self):
        return make_client()

    def _make_query(self):
        return Query(mock.Mock())

    def test_make_from_client(self):
        instance = self._make_client().pipeline()
        assert isinstance(instance, PipelineSource)

    def test_create_pipeline(self):
        instance = self._make_client().pipeline()
        ppl = instance._create_pipeline(None)
        assert isinstance(ppl, self._expected_pipeline_type)

    def test_create_from_mock(self):
        mock_query = mock.Mock()
        expected = object()
        mock_query._build_pipeline.return_value = expected
        instance = self._make_client().pipeline()
        got = instance.create_from(mock_query)
        assert got == expected
        assert mock_query._build_pipeline.call_count == 1
        assert mock_query._build_pipeline.call_args_list[0][0][0] == instance

    def test_create_from_query(self):
        query = self._make_query()
        instance = self._make_client().pipeline()
        ppl = instance.create_from(query)
        assert isinstance(ppl, self._expected_pipeline_type)
        assert len(ppl.stages) == 1

    def test_collection(self):
        instance = self._make_client().pipeline()
        ppl = instance.collection("path")
        assert isinstance(ppl, self._expected_pipeline_type)
        assert len(ppl.stages) == 1
        first_stage = ppl.stages[0]
        assert isinstance(first_stage, stages.Collection)
        assert first_stage.path == "/path"

    def test_collection_w_tuple(self):
        instance = self._make_client().pipeline()
        ppl = instance.collection(("a", "b", "c"))
        assert isinstance(ppl, self._expected_pipeline_type)
        assert len(ppl.stages) == 1
        first_stage = ppl.stages[0]
        assert isinstance(first_stage, stages.Collection)
        assert first_stage.path == "/a/b/c"

    def test_collection_group(self):
        instance = self._make_client().pipeline()
        ppl = instance.collection_group("id")
        assert isinstance(ppl, self._expected_pipeline_type)
        assert len(ppl.stages) == 1
        first_stage = ppl.stages[0]
        assert isinstance(first_stage, stages.CollectionGroup)
        assert first_stage.collection_id == "id"

    def test_database(self):
        instance = self._make_client().pipeline()
        ppl = instance.database()
        assert isinstance(ppl, self._expected_pipeline_type)
        assert len(ppl.stages) == 1
        first_stage = ppl.stages[0]
        assert isinstance(first_stage, stages.Database)

    def test_documents(self):
        instance = self._make_client().pipeline()
        test_documents = [
            BaseDocumentReference("a", "1"),
            BaseDocumentReference("a", "2"),
            BaseDocumentReference("a", "3"),
        ]
        ppl = instance.documents(*test_documents)
        assert isinstance(ppl, self._expected_pipeline_type)
        assert len(ppl.stages) == 1
        first_stage = ppl.stages[0]
        assert isinstance(first_stage, stages.Documents)
        assert len(first_stage.paths) == 3
        assert first_stage.paths[0] == "/a/1"
        assert first_stage.paths[1] == "/a/2"
        assert first_stage.paths[2] == "/a/3"

    def test_literals(self):
        from google.cloud.firestore_v1.pipeline_expressions import Field

        instance = self._make_client().pipeline()
        documents = ({"field": Field.of("a")}, {"name": "joe"})
        ppl = instance.literals(*documents)
        assert isinstance(ppl, self._expected_pipeline_type)
        assert len(ppl.stages) == 1
        first_stage = ppl.stages[0]
        assert isinstance(first_stage, stages.Literals)

    def test_subcollection(self):
        expected_path = "/a/b/c"
        ppl = PipelineSource.subcollection(expected_path)
        assert isinstance(ppl, SubPipeline)
        assert len(ppl.stages) == 1
        first_stage = ppl.stages[0]
        assert isinstance(first_stage, stages.Subcollection)
        assert first_stage.path == expected_path


class TestPipelineSourceWithAsyncClient(TestPipelineSource):
    """
    When an async client is used, it should produce async pipelines
    """

    _expected_pipeline_type = AsyncPipeline

    def _make_client(self):
        return make_async_client()

    def _make_query(self):
        return AsyncQuery(mock.Mock())
