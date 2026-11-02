import contextlib
import datetime
import os
import re
import time

from google.api_core.exceptions import AlreadyExists
from test_utils.system import EmulatorCreds, unique_resource_id

from google.cloud.firestore import SERVER_TIMESTAMP
from google.cloud.firestore_v1.base_client import _FIRESTORE_EMULATOR_HOST

FIRESTORE_CREDS = os.environ.get("FIRESTORE_APPLICATION_CREDENTIALS")
FIRESTORE_PROJECT = os.environ.get("GCLOUD_PROJECT")
RANDOM_ID_REGEX = re.compile("^[a-zA-Z0-9]{20}$")
MISSING_DOCUMENT = "No document to update: "
DOCUMENT_EXISTS = "Document already exists: "
ENTERPRISE_MODE_ERROR = "only allowed on ENTERPRISE mode"
UNIQUE_RESOURCE_ID = unique_resource_id("-")
EMULATOR_CREDS = EmulatorCreds()
FIRESTORE_EMULATOR = os.environ.get(_FIRESTORE_EMULATOR_HOST) is not None
FIRESTORE_OTHER_DB = os.environ.get("SYSTEM_TESTS_DATABASE", "system-tests-named-db")
FIRESTORE_ENTERPRISE_DB = os.environ.get("ENTERPRISE_DATABASE", "enterprise-db-native")

# To eliminate test duplication, we use the default database for the
# core test suites. The named database is ONLY tested explicitly in dedicated
# routing tests to prove path construction works.
TEST_DATABASES = [None]
TEST_DATABASES_W_ENTERPRISE = TEST_DATABASES + [FIRESTORE_ENTERPRISE_DB]


@contextlib.contextmanager
def system_test_lock(client, lock_name="system_test_lock", max_wait_minutes=65):
    """
    Acquires a distributed lock using a Firestore document to prevent concurrent system tests.
    """
    lock_ref = client.collection("system_tests").document(lock_name)
    start_time = time.time()
    max_wait_time = max_wait_minutes * 60

    while time.time() - start_time < max_wait_time:
        try:
            lock_ref.create({"created_at": SERVER_TIMESTAMP})
            break  # Lock acquired
        except AlreadyExists:
            lock_doc = lock_ref.get()
            if lock_doc.exists:
                created_at = lock_doc.to_dict().get("created_at")
                if created_at:
                    now = datetime.datetime.now(datetime.timezone.utc)
                    age = (now - created_at).total_seconds()
                    if age > 3600:
                        print(f"Lock is expired (age: {age}s). Stealing lock.")
                        lock_ref.delete()
                        continue
                    else:
                        print(
                            f"Waiting for {lock_name}. Lock is {age:.0f}s old. Sleeping for 15s..."
                        )
            time.sleep(15)
    else:
        raise TimeoutError(f"Timed out waiting for {lock_name}")

    try:
        yield lock_ref
    finally:
        lock_ref.delete()
