# Copyright 2018 Google Inc.
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

import os
import random
import time
import warnings

import backoff
import pytest
from google.api_core import exceptions

from google.cloud import bigtable

from . import instanceadmin

PROJECT = os.environ["GOOGLE_CLOUD_PROJECT"]
INSTANCE_ID_FORMAT = "instanceadmin-{:03}-{}"
CLUSTER_ID_FORMAT = "instanceadmin-{:03}"
ID_RANGE = 1000

INSTANCE = INSTANCE_ID_FORMAT.format(random.randrange(ID_RANGE), int(time.time()))
CLUSTER1 = CLUSTER_ID_FORMAT.format(random.randrange(ID_RANGE))
CLUSTER2 = CLUSTER_ID_FORMAT.format(random.randrange(ID_RANGE))


@pytest.fixture(scope="module", autouse=True)
def preclean():
    """In case any test instances weren't cleared out in a previous run.

    Deletes any test instances that were created over an hour ago. Newer instances may
    be being used by a concurrent test run.
    """
    client = bigtable.Client(project=PROJECT, admin=True)
    for instance in client.list_instances()[0]:
        if instance.instance_id.startswith("instanceadmin-"):
            timestamp = instance.instance_id.split("-")[-1]
            timestamp = int(timestamp)
            if time.time() - timestamp > 3600:
                warnings.warn(
                    f"Deleting leftover test instance: {instance.instance_id}"
                )
                instance.delete()


@pytest.fixture
def dispose_of():
    instances = []

    def disposal(instance):
        instances.append(instance)

    yield disposal

    client = bigtable.Client(project=PROJECT, admin=True)
    for instance_id in instances:
        instance = client.instance(instance_id)
        if instance.exists():
            instance.delete()


def test_run_instance_operations(capsys, dispose_of):
    dispose_of(INSTANCE)

    instanceadmin.run_instance_operations(PROJECT, INSTANCE, CLUSTER1)
    out = capsys.readouterr().out
    assert f"Instance {INSTANCE} does not exist." in out
    assert "Creating an instance" in out
    assert f"Created instance: {INSTANCE}" in out
    assert "Listing instances" in out
    assert f"\n{INSTANCE}\n" in out
    assert f"Name of instance: {INSTANCE}" in out
    assert "Labels: {'prod-label': 'prod-label'}" in out
    assert "Listing clusters..." in out
    assert f"\n{CLUSTER1}\n" in out

    instanceadmin.run_instance_operations(PROJECT, INSTANCE, CLUSTER1)
    out = capsys.readouterr().out
    assert f"Instance {INSTANCE} already exists." in out
    assert "Listing instances" in out
    assert f"\n{INSTANCE}\n" in out
    assert f"Name of instance: {INSTANCE}" in out
    assert "Labels: {'prod-label': 'prod-label'}" in out
    assert "Listing clusters..." in out
    assert f"\n{CLUSTER1}\n" in out


def test_delete_instance(capsys, dispose_of):
    from concurrent.futures import TimeoutError

    @backoff.on_exception(backoff.expo, TimeoutError)
    def _set_up_instance():
        dispose_of(INSTANCE)

        # Can't delete it, it doesn't exist
        instanceadmin.delete_instance(PROJECT, INSTANCE)
        out = capsys.readouterr().out
        assert "Deleting instance" in out
        assert f"Instance {INSTANCE} does not exist" in out

        # Ok, create it then
        instanceadmin.run_instance_operations(PROJECT, INSTANCE, CLUSTER1)
        capsys.readouterr()  # throw away output

    _set_up_instance()

    # Now delete it
    instanceadmin.delete_instance(PROJECT, INSTANCE)
    out = capsys.readouterr().out
    assert "Deleting instance" in out
    assert f"Deleted instance: {INSTANCE}" in out


def test_add_and_delete_cluster(capsys, dispose_of):
    from concurrent.futures import TimeoutError

    @backoff.on_exception(backoff.expo, TimeoutError)
    def _set_up_instance():
        dispose_of(INSTANCE)

        # This won't work, because the instance isn't created yet
        instanceadmin.add_cluster(PROJECT, INSTANCE, CLUSTER2)
        out = capsys.readouterr().out
        assert f"Instance {INSTANCE} does not exist" in out

        # Get the instance created
        instanceadmin.run_instance_operations(PROJECT, INSTANCE, CLUSTER1)
        capsys.readouterr()  # throw away output

    _set_up_instance()

    # Add a cluster to that instance
    # Avoid failing for "instance is currently being changed" by
    # applying an exponential backoff
    backoff_503 = backoff.on_exception(backoff.expo, exceptions.ServiceUnavailable)

    backoff_503(instanceadmin.add_cluster)(PROJECT, INSTANCE, CLUSTER2)
    out = capsys.readouterr().out
    assert f"Adding cluster to instance {INSTANCE}" in out
    assert "Listing clusters..." in out
    assert f"\n{CLUSTER1}\n" in out
    assert f"Cluster created: {CLUSTER2}" in out

    # Try to add the same cluster again, won't work
    instanceadmin.add_cluster(PROJECT, INSTANCE, CLUSTER2)
    out = capsys.readouterr().out
    assert "Listing clusters..." in out
    assert f"\n{CLUSTER1}\n" in out
    assert f"\n{CLUSTER2}\n" in out
    assert f"Cluster not created, as {CLUSTER2} already exists."

    # Now delete it
    instanceadmin.delete_cluster(PROJECT, INSTANCE, CLUSTER2)
    out = capsys.readouterr().out
    assert "Deleting cluster" in out
    assert f"Cluster deleted: {CLUSTER2}" in out

    # Verify deletion
    instanceadmin.run_instance_operations(PROJECT, INSTANCE, CLUSTER1)
    out = capsys.readouterr().out
    assert "Listing clusters..." in out
    assert f"\n{CLUSTER1}\n" in out
    assert f"\n{CLUSTER2}\n" not in out

    # Try deleting it again, for fun (and coverage)
    instanceadmin.delete_cluster(PROJECT, INSTANCE, CLUSTER2)
    out = capsys.readouterr().out
    assert "Deleting cluster" in out
    assert f"Cluster {CLUSTER2} does not exist" in out
