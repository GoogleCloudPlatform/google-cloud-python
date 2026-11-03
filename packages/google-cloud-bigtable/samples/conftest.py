# Copyright 2026 Google LLC
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

import atexit
import os
import signal
import uuid
from typing import Optional
from unittest import mock

import pytest
from google.api_core import exceptions, retry

from google.cloud import bigtable_admin
from google.cloud.bigtable.data._async import client as async_client
from google.cloud.bigtable.data._sync_autogen import client as sync_client
from tests.system.utils import clear_stale_instances

_CREATED_INSTANCE_NAME: Optional[str] = None


def _cleanup_temp_instance() -> None:
    """Deletes the temporary Bigtable instance if one was created for this session."""
    global _CREATED_INSTANCE_NAME
    instance_name = _CREATED_INSTANCE_NAME
    if not instance_name:
        return
    _CREATED_INSTANCE_NAME = None

    print(f"\nDeleting temporary sample test instance: {instance_name}")
    client = bigtable_admin.BigtableInstanceAdminClient()
    retry_delete = retry.Retry(
        predicate=retry.if_exception_type(
            exceptions.TooManyRequests,
            exceptions.ServiceUnavailable,
        )
    )
    try:
        client.delete_instance(name=instance_name, retry=retry_delete)
        print(f"Deleted temporary sample test instance: {instance_name}")
    except exceptions.NotFound:
        pass
    except Exception as exc:
        print(f"Failed to delete temporary instance {instance_name}: {exc}")


def _sigterm_handler(signum, frame) -> None:
    _cleanup_temp_instance()
    raise SystemExit(128 + signum)


def pytest_configure(config) -> None:
    """Creates a temporary Bigtable instance if BIGTABLE_INSTANCE is not set."""
    global _CREATED_INSTANCE_NAME

    # Disable client-side metrics export during sample tests to avoid
    # per-snippet MetricServiceClient initialization and background export threads.
    async_client.BigtableMetricsExporter = mock.MagicMock
    async_client.GoogleCloudMetricsHandler = mock.MagicMock
    sync_client.BigtableMetricsExporter = mock.MagicMock
    sync_client.GoogleCloudMetricsHandler = mock.MagicMock

    if getattr(config.option, "help", False) or getattr(
        config.option, "collectonly", False
    ):
        return

    project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
    if not project_id:
        raise pytest.UsageError(
            "GOOGLE_CLOUD_PROJECT environment variable must be set to run sample tests."
        )

    if os.environ.get("BIGTABLE_INSTANCE"):
        return

    clear_stale_instances(
        project_id,
        prefix=(
            "bt-samples-",
            "metric-scale-test-",
            "instanceadmin-",
            "instance-admin-",
        ),
        older_than_days=1,
    )

    instance_id = f"bt-samples-{uuid.uuid4().hex[:8]}"
    client = bigtable_admin.BigtableInstanceAdminClient()
    project_path = client.common_project_path(project_id)
    instance_name = client.instance_path(project_id, instance_id)

    _CREATED_INSTANCE_NAME = instance_name
    atexit.register(_cleanup_temp_instance)
    signal.signal(signal.SIGTERM, _sigterm_handler)

    print(f"\nCreating temporary sample test instance: {instance_name}")
    try:
        operation = client.create_instance(
            parent=project_path,
            instance_id=instance_id,
            instance=bigtable_admin.Instance(
                display_name=instance_id,
                type_=bigtable_admin.Instance.Type.PRODUCTION,
            ),
            clusters={
                f"{instance_id}-c1": bigtable_admin.Cluster(
                    location=client.common_location_path(project_id, "us-central1-b"),
                    serve_nodes=1,
                    default_storage_type=bigtable_admin.StorageType.SSD,
                )
            },
        )
        operation.result(timeout=240)
        os.environ["BIGTABLE_INSTANCE"] = instance_id
        print(f"Created temporary sample test instance: {instance_id}")
    except Exception:
        _cleanup_temp_instance()
        raise


def pytest_sessionfinish(session, exitstatus) -> None:
    """Deletes the temporary Bigtable instance as soon as the test session finishes."""
    _cleanup_temp_instance()


def pytest_unconfigure(config) -> None:
    """Fallback hook to ensure the temporary Bigtable instance is deleted."""
    _cleanup_temp_instance()
