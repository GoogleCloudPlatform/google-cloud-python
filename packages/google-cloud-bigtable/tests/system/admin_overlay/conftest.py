import os
import uuid

import google.auth
import pytest

INSTANCE_PREFIX = "admin-overlay-instance"
BACKUP_PREFIX = "admin-overlay-backup"
ROW_PREFIX = "test-row"

DEFAULT_CLUSTER_LOCATIONS = ["us-east1-b"]
REPLICATION_CLUSTER_LOCATIONS = ["us-east1-b", "us-west1-b"]
TEST_TABLE_NAME = "system-test-table"
TEST_BACKUP_TABLE_NAME = "system-test-backup-table"
TEST_COLUMMN_FAMILY_NAME = "test-column"
TEST_COLUMN_NAME = "value"
NUM_ROWS = 500
INITIAL_CELL_VALUE = "Hello"
NEW_CELL_VALUE = "World"


@pytest.fixture(scope="session")
def admin_overlay_project_id():
    project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
    if not project_id:
        _, project_id = google.auth.default()
    return project_id


def generate_unique_suffix(name):
    """
    Generates a unique suffix for the name.

    Uses UUID4 because using time.time doesn't guarantee
    uniqueness when the time is frozen in containers.
    """
    return f"{name}-{uuid.uuid4().hex[:7]}"
