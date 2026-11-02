# -*- coding: utf-8 -*-
#
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

import pytest


@pytest.fixture
def target_class():
    from google.cloud.bigquery import ModelReference

    return ModelReference


def test_from_api_repr(target_class):
    resource = {
        "projectId": "my-project",
        "datasetId": "my_dataset",
        "modelId": "my_model",
    }
    got = target_class.from_api_repr(resource)
    assert got.project == "my-project"
    assert got.dataset_id == "my_dataset"
    assert got.model_id == "my_model"
    assert got.path == "/projects/my-project/datasets/my_dataset/models/my_model"


def test_from_api_repr_w_unknown_fields(target_class):
    resource = {
        "projectId": "my-project",
        "datasetId": "my_dataset",
        "modelId": "my_model",
        "thisFieldIsNotInTheProto": "just ignore me",
    }
    got = target_class.from_api_repr(resource)
    assert got.project == "my-project"
    assert got.dataset_id == "my_dataset"
    assert got.model_id == "my_model"
    assert got._properties is resource


def test_to_api_repr(target_class):
    ref = target_class.from_string("my-project.my_dataset.my_model")
    got = ref.to_api_repr()
    assert got == {
        "projectId": "my-project",
        "datasetId": "my_dataset",
        "modelId": "my_model",
    }


def test_from_string(target_class):
    got = target_class.from_string("string-project.string_dataset.string_model")
    assert got.project == "string-project"
    assert got.dataset_id == "string_dataset"
    assert got.model_id == "string_model"
    assert got.path == (
        "/projects/string-project/datasets/string_dataset/models/string_model"
    )


def test_from_string_legacy_string(target_class):
    with pytest.raises(ValueError):
        target_class.from_string("string-project:string_dataset.string_model")


def test_from_string_not_fully_qualified(target_class):
    with pytest.raises(ValueError):
        target_class.from_string("string_model")

    with pytest.raises(ValueError):
        target_class.from_string("string_dataset.string_model")

    with pytest.raises(ValueError):
        target_class.from_string("a.b.c.d")


def test_from_string_with_default_project(target_class):
    got = target_class.from_string(
        "string_dataset.string_model", default_project="default-project"
    )
    assert got.project == "default-project"
    assert got.dataset_id == "string_dataset"
    assert got.model_id == "string_model"


def test_from_string_ignores_default_project(target_class):
    got = target_class.from_string(
        "string-project.string_dataset.string_model", default_project="default-project"
    )
    assert got.project == "string-project"
    assert got.dataset_id == "string_dataset"
    assert got.model_id == "string_model"


def test_eq(target_class):
    model = target_class.from_string("my-proj.my_dset.my_model")
    model_too = target_class.from_string("my-proj.my_dset.my_model")
    assert model == model_too
    assert not (model != model_too)

    other_model = target_class.from_string("my-proj.my_dset.my_model2")
    assert not (model == other_model)
    assert model != other_model

    notamodel = object()
    assert not (model == notamodel)
    assert model != notamodel


def test_hash(target_class):
    model = target_class.from_string("my-proj.my_dset.my_model")
    model2 = target_class.from_string("my-proj.my_dset.model2")
    got = {model: "hello", model2: "world"}
    assert got[model] == "hello"
    assert got[model2] == "world"

    model_too = target_class.from_string("my-proj.my_dset.my_model")
    assert got[model_too] == "hello"


def test_repr(target_class):
    model = target_class.from_string("my-proj.my_dset.my_model")
    got = repr(model)
    assert (
        got
        == "ModelReference(project_id='my-proj', dataset_id='my_dset', model_id='my_model')"
    )
