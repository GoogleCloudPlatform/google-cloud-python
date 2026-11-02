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
    from google.cloud.bigquery.routine import RoutineReference

    return RoutineReference


def test_from_api_repr(target_class):
    resource = {
        "projectId": "my-project",
        "datasetId": "my_dataset",
        "routineId": "my_routine",
    }
    got = target_class.from_api_repr(resource)
    assert got.project == "my-project"
    assert got.dataset_id == "my_dataset"
    assert got.routine_id == "my_routine"
    assert got.path == "/projects/my-project/datasets/my_dataset/routines/my_routine"


def test_from_api_repr_w_unknown_fields(target_class):
    resource = {
        "projectId": "my-project",
        "datasetId": "my_dataset",
        "routineId": "my_routine",
        "thisFieldIsNotInTheProto": "just ignore me",
    }
    got = target_class.from_api_repr(resource)
    assert got.project == "my-project"
    assert got.dataset_id == "my_dataset"
    assert got.routine_id == "my_routine"
    assert got._properties is resource


def test_to_api_repr(target_class):
    ref = target_class.from_string("my-project.my_dataset.my_routine")
    got = ref.to_api_repr()
    assert got == {
        "projectId": "my-project",
        "datasetId": "my_dataset",
        "routineId": "my_routine",
    }


def test_from_string(target_class):
    got = target_class.from_string("string-project.string_dataset.string_routine")
    assert got.project == "string-project"
    assert got.dataset_id == "string_dataset"
    assert got.routine_id == "string_routine"
    assert got.path == (
        "/projects/string-project/datasets/string_dataset/routines/string_routine"
    )


def test_from_string_legacy_string(target_class):
    with pytest.raises(ValueError):
        target_class.from_string("string-project:string_dataset.string_routine")


def test_from_string_not_fully_qualified(target_class):
    with pytest.raises(ValueError):
        target_class.from_string("string_routine")

    with pytest.raises(ValueError):
        target_class.from_string("string_dataset.string_routine")

    with pytest.raises(ValueError):
        target_class.from_string("a.b.c.d")


def test_from_string_with_default_project(target_class):
    got = target_class.from_string(
        "string_dataset.string_routine", default_project="default-project"
    )
    assert got.project == "default-project"
    assert got.dataset_id == "string_dataset"
    assert got.routine_id == "string_routine"


def test_from_string_ignores_default_project(target_class):
    got = target_class.from_string(
        "string-project.string_dataset.string_routine",
        default_project="default-project",
    )
    assert got.project == "string-project"
    assert got.dataset_id == "string_dataset"
    assert got.routine_id == "string_routine"


def test_eq(target_class):
    routine = target_class.from_string("my-proj.my_dset.my_routine")
    routine_too = target_class.from_string("my-proj.my_dset.my_routine")
    assert routine == routine_too
    assert not (routine != routine_too)

    other_routine = target_class.from_string("my-proj.my_dset.my_routine2")
    assert not (routine == other_routine)
    assert routine != other_routine

    notaroutine = object()
    assert not (routine == notaroutine)
    assert routine != notaroutine


def test_hash(target_class):
    routine = target_class.from_string("my-proj.my_dset.my_routine")
    routine2 = target_class.from_string("my-proj.my_dset.routine2")
    got = {routine: "hello", routine2: "world"}
    assert got[routine] == "hello"
    assert got[routine2] == "world"

    routine_too = target_class.from_string("my-proj.my_dset.my_routine")
    assert got[routine_too] == "hello"


def test_repr(target_class):
    routine = target_class.from_string("my-proj.my_dset.my_routine")
    got = repr(routine)
    assert got == "RoutineReference.from_string('my-proj.my_dset.my_routine')"
