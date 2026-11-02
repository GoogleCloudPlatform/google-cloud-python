# Copyright 2024 Google LLC
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

from google.api_core import exceptions


def test_get_operation(echo):
    with pytest.raises(exceptions.NotFound):
        echo.get_operation({"name": "operations/**"})


def test_list_operations(echo):
    response = echo.list_operations({"name": "operations/name"})
    assert response.operations[0].name == "a/pending/thing"


def test_delete_operation(echo):
    response = echo.delete_operation({"name": "operations/name"})
    assert response is None


def test_cancel_operation(echo):
    response = echo.cancel_operation({"name": "operations/name"})
    assert response is None


def test_set_iam_policy(echo):
    policy = echo.set_iam_policy(
        {"resource": "users/user", "policy": {"version": 20240919}}
    )
    assert policy.version == 20240919


def test_get_iam_policy(echo):
    # First we need to set a policy, before we can get it
    echo.set_iam_policy({"resource": "users/user", "policy": {"version": 20240920}})
    policy = echo.get_iam_policy(
        {
            "resource": "users/user",
        }
    )
    assert policy.version == 20240920


def test_test_iam_permissions(echo):
    # First we need to set a policy, before we can call test_iam_permissions
    echo.set_iam_policy({"resource": "users/user", "policy": {"version": 20240920}})
    response = echo.test_iam_permissions(
        {"resource": "users/user", "permissions": ["test_some_permission"]}
    )
    assert response.permissions == ["test_some_permission"]


def test_get_location(echo):
    response = echo.get_location(
        {
            "name": "projects/some_project/locations/some_location",
        }
    )
    assert response.name == "projects/some_project/locations/some_location"


def test_list_locations(echo):
    response = echo.list_locations(
        {
            "name": "projects/some_project",
        }
    )
    assert response.locations[0].name == "projects/some_project/locations/us-north"


if os.environ.get("GAPIC_PYTHON_ASYNC", "true") == "true":

    @pytest.mark.asyncio
    async def test_get_operation_async(async_echo):
        with pytest.raises(exceptions.NotFound):
            await async_echo.get_operation({"name": "operations/**"})

    @pytest.mark.asyncio
    async def test_list_operations_async(async_echo):
        response = await async_echo.list_operations({"name": "operations/name"})
        assert response.operations[0].name == "a/pending/thing"

    @pytest.mark.asyncio
    async def test_delete_operation_async(async_echo):
        await async_echo.delete_operation({"name": "operations/name"})

    @pytest.mark.asyncio
    async def test_cancel_operation_async(async_echo):
        await async_echo.cancel_operation({"name": "operations/name"})

    @pytest.mark.asyncio
    async def test_set_iam_policy_async(async_echo):
        policy = await async_echo.set_iam_policy(
            {"resource": "users/user", "policy": {"version": 20240919}}
        )
        assert policy.version == 20240919

    @pytest.mark.asyncio
    async def test_get_iam_policy_async(async_echo):
        # First we need to set a policy, before we can get it
        await async_echo.set_iam_policy(
            {"resource": "users/user", "policy": {"version": 20240920}}
        )
        policy = await async_echo.get_iam_policy(
            {
                "resource": "users/user",
            }
        )
        assert policy.version == 20240920

    @pytest.mark.asyncio
    async def test_test_iam_permissions_async(async_echo):
        # First we need to set a policy, before we can get it
        await async_echo.set_iam_policy(
            {"resource": "users/user", "policy": {"version": 20240920}}
        )

        response = await async_echo.test_iam_permissions(
            {"resource": "users/user", "permissions": ["test_some_permission"]}
        )
        assert response.permissions == ["test_some_permission"]

    @pytest.mark.asyncio
    async def test_get_location_async(async_echo):
        response = await async_echo.get_location(
            {
                "name": "projects/some_project/locations/some_location",
            }
        )
        assert response.name == "projects/some_project/locations/some_location"

    @pytest.mark.asyncio
    async def test_list_locations_async(async_echo):
        response = await async_echo.list_locations(
            {
                "name": "projects/some_project",
            }
        )
        assert response.locations[0].name == "projects/some_project/locations/us-north"
