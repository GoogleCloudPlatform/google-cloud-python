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

import os
import pytest


def test_crud_with_request(identity):
    count = len(identity.list_users().users)
    user = identity.create_user(
        request={
            "user": {
                "display_name": "Guido van Rossum",
                "email": "guido@guido.fake",
            }
        }
    )
    try:
        assert user.display_name == "Guido van Rossum"
        assert user.email == "guido@guido.fake"
        assert len(identity.list_users().users) == count + 1
        assert identity.get_user({"name": user.name}).display_name == "Guido van Rossum"
    finally:
        identity.delete_user({"name": user.name})


def test_crud_flattened(identity):
    count = len(identity.list_users().users)
    user = identity.create_user(
        display_name="Monty Python",
        email="monty@python.org",
    )
    try:
        assert user.display_name == "Monty Python"
        assert user.email == "monty@python.org"
        assert len(identity.list_users().users) == count + 1
        assert identity.get_user(name=user.name).display_name == "Monty Python"
    finally:
        identity.delete_user(name=user.name)


def test_path_methods(identity):
    expected = "users/bdfl"
    actual = identity.user_path("bdfl")

    assert expected == actual


def test_nonslash_resource(messaging):
    expected = "users/bdfl/profile/blurbs/legacy/apocalyptic~city"
    actual = messaging.blurb_path("bdfl", "apocalyptic", "city")

    assert expected == actual


def test_path_parsing(messaging):
    expected = {"room": "tiki"}
    actual = messaging.parse_room_path(messaging.room_path("tiki"))

    assert expected == actual

    expected = {
        "user": "bdfl",
        "legacy_user": "apocalyptic",
        "blurb": "city",
    }
    actual = messaging.parse_blurb_path(
        messaging.blurb_path("bdfl", "apocalyptic", "city")
    )
    assert expected == actual


if os.environ.get("GAPIC_PYTHON_ASYNC", "true") == "true":

    @pytest.mark.asyncio
    async def test_crud_with_request_async(async_identity):
        pager = await async_identity.list_users()
        count = len(pager.users)
        user = await async_identity.create_user(
            request={
                "user": {
                    "display_name": "Guido van Rossum",
                    "email": "guido@guido.fake",
                }
            }
        )
        try:
            assert user.display_name == "Guido van Rossum"
            assert user.email == "guido@guido.fake"
            pager = await async_identity.list_users()
            assert len(pager.users) == count + 1
            assert (
                await async_identity.get_user({"name": user.name})
            ).display_name == "Guido van Rossum"
        finally:
            await async_identity.delete_user({"name": user.name})

    @pytest.mark.asyncio
    async def test_crud_flattened_async(async_identity):
        count = len((await async_identity.list_users()).users)
        user = await async_identity.create_user(
            display_name="Monty Python",
            email="monty@python.org",
        )
        try:
            assert user.display_name == "Monty Python"
            assert user.email == "monty@python.org"
            assert len((await async_identity.list_users()).users) == count + 1
            assert (
                await async_identity.get_user(name=user.name)
            ).display_name == "Monty Python"
        finally:
            await async_identity.delete_user(name=user.name)

    def test_path_methods_async(async_identity):
        expected = "users/bdfl"
        actual = async_identity.user_path("bdfl")
        assert expected == actual
