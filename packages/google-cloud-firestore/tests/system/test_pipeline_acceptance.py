# Copyright 2025 Google LLC
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
"""
This file loads and executes yaml-encoded test cases from pipeline_e2e.yaml
"""

from __future__ import annotations

import datetime
import os
import re
from typing import Any

import pytest
import yaml
from google.protobuf.json_format import MessageToDict
from test__helpers import FIRESTORE_EMULATOR, FIRESTORE_ENTERPRISE_DB, system_test_lock

from google.cloud.firestore import AsyncClient, Client, GeoPoint
from google.cloud.firestore_v1 import pipeline_expressions
from google.cloud.firestore_v1 import pipeline_expressions as expr
from google.cloud.firestore_v1 import pipeline_stages as stages
from google.cloud.firestore_v1.vector import Vector

FIRESTORE_PROJECT = os.environ.get("GCLOUD_PROJECT")

pytestmark = pytest.mark.skipif(
    condition=FIRESTORE_EMULATOR,
    reason="Pipeline tests are currently not supported by emulator",
)

test_dir_name = os.path.dirname(__file__)

id_format = lambda x: f"{x.get('file_name', '')}: {x.get('description', '')}"  # noqa: E731


def yaml_loader(field="tests", dir_name="pipeline_e2e", attach_file_name=True):
    """
    Helper to load test cases or data from yaml file
    """
    combined_yaml = None
    for file_name in os.listdir(f"{test_dir_name}/{dir_name}"):
        if not file_name.endswith(".yaml"):
            continue
        with open(f"{test_dir_name}/{dir_name}/{file_name}") as f:
            new_yaml = yaml.safe_load(f)
            assert new_yaml is not None, f"found empty yaml in {file_name}"
            extracted = new_yaml.get(field, None)
            # attach file_name field
            if attach_file_name:
                if isinstance(extracted, list):
                    for item in extracted:
                        item["file_name"] = file_name
                elif isinstance(extracted, dict):
                    extracted["file_name"] = file_name
            # aggregate files
            if not combined_yaml:
                combined_yaml = extracted
            elif isinstance(combined_yaml, dict) and extracted:
                combined_yaml.update(extracted)
            elif isinstance(combined_yaml, list) and extracted:
                combined_yaml.extend(extracted)

    # Validate test keys
    allowed_keys = {
        "description",
        "pipeline",
        "assert_proto",
        "assert_error",
        "assert_results",
        "assert_count",
        "assert_results_approximate",
        "assert_end_state",
        "file_name",
    }
    if field == "tests" and isinstance(combined_yaml, list):
        for item in combined_yaml:
            if isinstance(item, dict):
                for key in item:
                    if key not in allowed_keys:
                        raise ValueError(
                            f"Unrecognized key '{key}' in test '{item.get('description', 'Unknown')}' in file '{item.get('file_name', 'Unknown')}'"
                        )

    return combined_yaml


@pytest.mark.parametrize(
    "test_dict",
    [t for t in yaml_loader() if "assert_proto" in t],
    ids=id_format,
)
def test_pipeline_parse_proto(test_dict, client):
    """
    Finds assert_proto statements in yaml, and compares generated proto against expected value
    """
    expected_proto = test_dict.get("assert_proto", None)
    pipeline = parse_pipeline(client, test_dict["pipeline"])
    # check if proto matches as expected
    if expected_proto:
        got_proto = MessageToDict(pipeline._to_pb()._pb)
        assert yaml.dump(expected_proto) == yaml.dump(got_proto)


@pytest.mark.parametrize(
    "test_dict",
    [t for t in yaml_loader() if "assert_error" in t],
    ids=id_format,
)
def test_pipeline_expected_errors(test_dict, client):
    """
    Finds assert_error statements in yaml, and ensures the pipeline raises the expected error
    """
    error_regex = test_dict["assert_error"]

    with pytest.raises(Exception) as err:
        pipeline = parse_pipeline(client, test_dict["pipeline"])
        pipeline.execute()
    found_error = str(err.value)
    match = re.search(error_regex, found_error)
    assert match, f"error '{found_error}' does not match '{error_regex}'"


def _assert_pipeline_results(
    got_results, expected_results, expected_approximate_results, expected_count
):
    if expected_results:
        assert got_results == expected_results
    if expected_approximate_results is not None:
        tolerance = 1e-4
        if (
            isinstance(expected_approximate_results, dict)
            and "data" in expected_approximate_results
        ):
            if (
                "config" in expected_approximate_results
                and "absolute_tolerance" in expected_approximate_results["config"]
            ):
                tolerance = expected_approximate_results["config"]["absolute_tolerance"]
            expected_approximate_results = expected_approximate_results["data"]

        assert len(got_results) == len(expected_approximate_results), (
            "got unexpected result count"
        )
        for idx in range(len(got_results)):
            expected = expected_approximate_results[idx]
            assert got_results[idx] == pytest.approx(expected, abs=tolerance)
    if expected_count is not None:
        assert len(got_results) == expected_count


@pytest.mark.parametrize(
    "test_dict",
    [
        t
        for t in yaml_loader()
        if "assert_results" in t
        or "assert_count" in t
        or "assert_results_approximate" in t
        or "assert_end_state" in t
    ],
    ids=id_format,
)
def test_pipeline_results(test_dict, client):
    """
    Ensure pipeline returns expected results
    """
    expected_results = _parse_yaml_types(test_dict.get("assert_results", None))
    expected_approximate_results = _parse_yaml_types(
        test_dict.get("assert_results_approximate", None)
    )
    expected_count = test_dict.get("assert_count", None)
    expected_end_state = _parse_yaml_types(test_dict.get("assert_end_state", {}))
    pipeline = parse_pipeline(client, test_dict["pipeline"])
    # check if server responds as expected
    got_results = [snapshot.data() for snapshot in pipeline.stream()]
    _assert_pipeline_results(
        got_results, expected_results, expected_approximate_results, expected_count
    )
    if expected_end_state:
        for doc_path, expected_content in expected_end_state.items():
            doc_ref = client.document(doc_path)
            snapshot = doc_ref.get()
            if expected_content is None:
                assert not snapshot.exists, (
                    f"Expected {doc_path} to be absent, but it exists"
                )
            else:
                assert snapshot.exists, (
                    f"Expected {doc_path} to exist, but it was absent"
                )
                assert snapshot.to_dict() == expected_content


@pytest.mark.parametrize(
    "test_dict",
    [t for t in yaml_loader() if "assert_error" in t],
    ids=id_format,
)
@pytest.mark.asyncio
async def test_pipeline_expected_errors_async(test_dict, async_client):
    """
    Finds assert_error statements in yaml, and ensures the pipeline raises the expected error
    """
    error_regex = test_dict["assert_error"]
    with pytest.raises(Exception) as err:
        pipeline = parse_pipeline(async_client, test_dict["pipeline"])
        await pipeline.execute()
    found_error = str(err.value)
    match = re.search(error_regex, found_error)
    assert match, f"error '{found_error}' does not match '{error_regex}'"


@pytest.mark.parametrize(
    "test_dict",
    [
        t
        for t in yaml_loader()
        if "assert_results" in t
        or "assert_count" in t
        or "assert_results_approximate" in t
        or "assert_end_state" in t
    ],
    ids=id_format,
)
@pytest.mark.asyncio
async def test_pipeline_results_async(test_dict, async_client):
    """
    Ensure pipeline returns expected results
    """
    expected_results = _parse_yaml_types(test_dict.get("assert_results", None))
    expected_approximate_results = _parse_yaml_types(
        test_dict.get("assert_results_approximate", None)
    )
    expected_count = test_dict.get("assert_count", None)
    expected_end_state = _parse_yaml_types(test_dict.get("assert_end_state", {}))
    pipeline = parse_pipeline(async_client, test_dict["pipeline"])
    # check if server responds as expected
    got_results = [snapshot.data() async for snapshot in pipeline.stream()]
    _assert_pipeline_results(
        got_results, expected_results, expected_approximate_results, expected_count
    )
    if expected_end_state:
        for doc_path, expected_content in expected_end_state.items():
            doc_ref = async_client.document(doc_path)
            snapshot = await doc_ref.get()
            if expected_content is None:
                assert not snapshot.exists, (
                    f"Expected {doc_path} to be absent, but it exists"
                )
            else:
                assert snapshot.exists, (
                    f"Expected {doc_path} to exist, but it was absent"
                )
                assert snapshot.to_dict() == expected_content


#################################################################################
# Helpers & Fixtures
#################################################################################


def parse_pipeline(client, pipeline: list[dict[str, Any], str]):
    """
    parse a yaml list of pipeline stages into firestore._pipeline_stages.Stage classes
    """
    result_list = []
    for stage in pipeline:
        # stage will be either a map of the stage_name and its args, or just the stage_name itself
        stage_name: str = stage if isinstance(stage, str) else list(stage.keys())[0]
        stage_cls: type[stages.Stage] = getattr(stages, stage_name)
        # find arguments if given
        if isinstance(stage, dict):
            stage_yaml_args = stage[stage_name]
            if stage_yaml_args is None:
                stage_obj = stage_cls()
            else:
                stage_obj = _apply_yaml_args_to_callable(
                    stage_cls, client, stage_yaml_args
                )
        else:
            # yaml has no arguments
            stage_obj = stage_cls()
        result_list.append(stage_obj)
    return client._pipeline_cls._create_with_stages(client, *result_list)


def _parse_expressions(client, yaml_element: Any):
    """
    Turn yaml objects into pipeline expressions or native python object arguments
    """
    if isinstance(yaml_element, list):
        return [_parse_expressions(client, v) for v in yaml_element]
    elif isinstance(yaml_element, dict):
        if len(yaml_element) == 1 and _is_expr_string(next(iter(yaml_element))):
            # build pipeline expressions if possible
            cls_str = next(iter(yaml_element))
            callable_obj = None
            if "." in cls_str:
                cls_name, method_name = cls_str.split(".")
                cls = getattr(pipeline_expressions, cls_name)
                callable_obj = getattr(cls, method_name)
            else:
                callable_obj = getattr(pipeline_expressions, cls_str)
            yaml_args = yaml_element[cls_str]
            return _apply_yaml_args_to_callable(callable_obj, client, yaml_args)
        elif len(yaml_element) == 1 and _is_stage_string(next(iter(yaml_element))):
            # build pipeline stage if possible (eg, for SampleOptions)
            cls_str = next(iter(yaml_element))
            cls = getattr(stages, cls_str)
            yaml_args = yaml_element[cls_str]
            return _apply_yaml_args_to_callable(cls, client, yaml_args)
        elif len(yaml_element) == 1 and list(yaml_element)[0] == "Pipeline":
            # find Pipeline objects for Union expressions
            other_ppl = yaml_element["Pipeline"]
            return parse_pipeline(client, other_ppl)
        elif (
            len(yaml_element) == 1
            and list(yaml_element)[0] == "Pipeline.to_array_expression"
        ):
            other_ppl = yaml_element["Pipeline.to_array_expression"]
            return parse_pipeline(client, other_ppl).to_array_expression()
        elif (
            len(yaml_element) == 1
            and list(yaml_element)[0] == "Pipeline.to_scalar_expression"
        ):
            other_ppl = yaml_element["Pipeline.to_scalar_expression"]
            return parse_pipeline(client, other_ppl).to_scalar_expression()
        else:
            # otherwise, return dict
            return {
                _parse_expressions(client, k): _parse_expressions(client, v)
                for k, v in yaml_element.items()
            }
    elif _is_expr_string(yaml_element):
        return getattr(pipeline_expressions, yaml_element)()
    elif yaml_element == "NaN":
        return float(yaml_element)
    else:
        return yaml_element


def _apply_yaml_args_to_callable(callable_obj, client, yaml_args):
    """
    Helper to instantiate a class with yaml arguments. The arguments will be applied
    as positional or keyword arguments, based on type
    """
    parsed = _parse_expressions(client, yaml_args)
    if isinstance(yaml_args, dict) and isinstance(parsed, dict):
        return callable_obj(**parsed)
    elif isinstance(yaml_args, list) and not (
        callable_obj == expr.Constant
        or callable_obj == Vector
        or callable_obj == expr.Array
    ):
        # yaml has an array of arguments. Treat as args
        return callable_obj(*parsed)
    elif yaml_args is None and callable_obj != expr.Constant:
        return callable_obj()
    else:
        # yaml has a single argument
        return callable_obj(parsed)


def _is_expr_string(yaml_str):
    """
    Returns true if a string represents a class in pipeline_expressions
    """
    if isinstance(yaml_str, str) and "." in yaml_str:
        parts = yaml_str.split(".")
        if len(parts) == 2:
            cls_name, method_name = parts
            if hasattr(pipeline_expressions, cls_name):
                cls = getattr(pipeline_expressions, cls_name)
                if hasattr(cls, method_name):
                    return True
    return (
        isinstance(yaml_str, str)
        and yaml_str[0].isupper()
        and hasattr(pipeline_expressions, yaml_str)
    )


def _is_stage_string(yaml_str):
    """
    Returns true if a string represents a class in pipeline_stages
    """
    return (
        isinstance(yaml_str, str)
        and yaml_str[0].isupper()
        and hasattr(stages, yaml_str)
    )


@pytest.fixture(scope="module")
def event_loop():
    """Change event_loop fixture to module level."""
    import asyncio

    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


def _parse_yaml_types(data):
    """helper to convert yaml data to firestore objects when needed"""
    if isinstance(data, dict):
        return {key: _parse_yaml_types(value) for key, value in data.items()}
    if isinstance(data, list):
        # detect vectors
        if len(data) > 0 and all([isinstance(d, float) for d in data]):
            return Vector(data)
        else:
            return [_parse_yaml_types(value) for value in data]
    # detect timestamps
    if isinstance(data, str) and ":" in data and not data.startswith("GEOPOINT("):
        try:
            parsed_datetime = datetime.datetime.fromisoformat(data)
            return parsed_datetime
        except ValueError:
            pass
    if isinstance(data, str) and data.startswith("GEOPOINT("):
        match = re.match(r"GEOPOINT\(([^,]+),\s*([^)]+)\)", data)
        if match:
            return GeoPoint(float(match.group(1)), float(match.group(2)))
    if data == "NaN":
        return float("NaN")
    return data


@pytest.fixture(scope="module")
def client():
    """
    Build a client to use for requests
    """
    client = Client(project=FIRESTORE_PROJECT, database=FIRESTORE_ENTERPRISE_DB)
    data = yaml_loader("data", attach_file_name=False)
    to_delete = []

    with system_test_lock(client, lock_name="pipeline_e2e_lock"):
        try:
            # setup data
            batch = client.batch()
            for collection_name, documents in data.items():
                collection_ref = client.collection(collection_name)
                for document_id, document_data in documents.items():
                    document_ref = collection_ref.document(document_id)
                    to_delete.append(document_ref)
                    batch.set(document_ref, _parse_yaml_types(document_data))
            batch.commit()
            yield client
        finally:
            # clear data
            for document_ref in to_delete:
                document_ref.delete()


@pytest.fixture(scope="module")
def async_client(client):
    """
    Build an async client to use for AsyncPipeline requests
    """
    yield AsyncClient(project=client.project, database=client._database)
