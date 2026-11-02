# Copyright 2021 Google LLC All rights reserved.
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

import pytest
from test_utils import retry

from . import _helpers


@pytest.fixture(scope="function")
def instances_to_delete():
    to_delete = []

    yield to_delete

    for instance in to_delete:
        _helpers.scrub_instance_ignore_not_found(instance)


def test_list_instances(
    no_create_instance,
    spanner_client,
    existing_instances,
    shared_instance,
):
    # Retrieve all instances currently visible in the project.
    instances = list(spanner_client.list_instances())

    # We use the instance name (the full resource path) rather than the object itself.
    # Protobuf objects may fail equality (==) if one has extra metadata populated
    # by the server (like 'edition' or 'backup_schedules') that the other lacks.
    instance_names = {instance.name for instance in instances}

    # In a parallel CI environment, other tests may create instances
    # (like 'multi-region-...') simultaneously.
    # Only verify `shared_instance.name` is in the list of instances.
    assert shared_instance.name in instance_names, (
        f"Expected instance {shared_instance.name} was not found in the "
        f"list of project instances: {instance_names}"
    )


def test_reload_instance(spanner_client, shared_instance_id, shared_instance):
    # Use same arguments as shared_instance_id so we can use 'reload()'
    # on a fresh instance.
    instance = spanner_client.instance(shared_instance_id)

    # Unset metadata before reloading.
    instance.display_name = None

    def _expected_display_name(instance):
        return instance.display_name == shared_instance.display_name

    retry_until = retry.RetryInstanceState(_expected_display_name)

    retry_until(instance.reload)()

    assert instance.display_name == shared_instance.display_name


def test_create_instance(
    if_create_instance,
    spanner_client,
    instance_config,
    instances_to_delete,
    instance_operation_timeout,
):
    alt_instance_id = _helpers.unique_id("new")
    instance = spanner_client.instance(alt_instance_id, instance_config.name)
    operation = instance.create()
    # Make sure this instance gets deleted after the test case.
    instances_to_delete.append(instance)

    # We want to make sure the operation completes.
    operation.result(instance_operation_timeout)  # raises on failure / timeout.

    # Create a new instance instance and make sure it is the same.
    instance_alt = spanner_client.instance(alt_instance_id, instance_config.name)
    instance_alt.reload()

    assert instance == instance_alt
    instance.display_name == instance_alt.display_name


def test_create_instance_with_processing_units(
    if_create_instance,
    spanner_client,
    instance_config,
    instances_to_delete,
    instance_operation_timeout,
):
    alt_instance_id = _helpers.unique_id("wpn")
    processing_units = 5000
    instance = spanner_client.instance(
        instance_id=alt_instance_id,
        configuration_name=instance_config.name,
        processing_units=processing_units,
    )
    operation = instance.create()
    # Make sure this instance gets deleted after the test case.
    instances_to_delete.append(instance)

    # We want to make sure the operation completes.
    operation.result(instance_operation_timeout)  # raises on failure / timeout.

    # Create a new instance instance and make sure it is the same.
    instance_alt = spanner_client.instance(alt_instance_id, instance_config.name)
    instance_alt.reload()

    assert instance == instance_alt
    assert instance.display_name == instance_alt.display_name
    assert instance.processing_units == instance_alt.processing_units


def test_update_instance(
    not_emulator,
    spanner_client,
    shared_instance,
    shared_instance_id,
    instance_operation_timeout,
    not_spanner_omni,
):
    old_display_name = shared_instance.display_name
    new_display_name = "Foo Bar Baz"
    shared_instance.display_name = new_display_name
    operation = shared_instance.update()

    # We want to make sure the operation completes.
    operation.result(instance_operation_timeout)  # raises on failure / timeout.

    # Create a new instance instance and reload it.
    instance_alt = spanner_client.instance(shared_instance_id, None)
    assert instance_alt.display_name != new_display_name

    instance_alt.reload()
    assert instance_alt.display_name == new_display_name

    # Make sure to put the instance back the way it was for the
    # other test cases.
    shared_instance.display_name = old_display_name
    shared_instance.update()
