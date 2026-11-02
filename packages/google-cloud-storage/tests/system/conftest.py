# Copyright 2021 Google LLC
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

import contextlib
import os

# MUST set env var before any google-cloud-storage imports occur
os.environ["ENABLE_GCS_PYTHON_CLIENT_OTEL_TRACES"] = "true"

# Import OpenTelemetry modules safely at top
try:
    from opentelemetry import trace as trace_api
    from opentelemetry.sdk.trace import TracerProvider, export
    from opentelemetry.sdk.trace.export.in_memory_span_exporter import (
        InMemorySpanExporter,
    )
except ImportError:
    trace_api = None

import pytest  # noqa: E402
from google.api_core import exceptions  # noqa: E402
from google.api_core.client_options import ClientOptions  # noqa: E402

from google.cloud import kms  # noqa: E402
from google.cloud.storage._helpers import _base64_md5hash  # noqa: E402
from google.cloud.storage.retry import DEFAULT_RETRY  # noqa: E402

from . import _helpers  # noqa: E402

PREPROD_JSON_HOST = "https://storage-preprod-test-unified.googleusercontent.com"
RUN_SYSTEM_TESTS_ON_PREPROD = os.getenv("RUN_SYSTEM_TESTS_ON_PREPROD") == "True"

if trace_api is not None:
    _global_exporter = InMemorySpanExporter()
    _provider = TracerProvider()
    _provider.add_span_processor(export.SimpleSpanProcessor(_global_exporter))

    # Option to also export telemetry to Google Cloud Trace Console
    # (for testing in GCE VM)
    if os.environ.get("ENABLE_GCP_TRACE_EXPORTER", "").lower() in (
        "1",
        "true",
        "yes",
        "on",
    ):
        try:
            from opentelemetry.exporter.cloud_trace import CloudTraceSpanExporter

            _provider.add_span_processor(
                export.BatchSpanProcessor(CloudTraceSpanExporter())
            )
        except ImportError:
            import warnings

            warnings.warn(
                "ENABLE_GCP_TRACE_EXPORTER is enabled, but "
                "opentelemetry-exporter-cloud-trace is not installed.",
                UserWarning,
            )

    trace_api.set_tracer_provider(_provider)
else:
    _global_exporter = None

dirname = os.path.realpath(os.path.dirname(__file__))
data_dirname = os.path.abspath(os.path.join(dirname, "..", "data"))
_filenames = [
    ("logo", "CloudPlatform_128px_Retina.png"),
    ("big", "five-point-one-mb-file.zip"),
    ("simple", "simple.txt"),
    ("big_9MiB", "random_9_MiB_file"),
]
_file_data = {
    key: {"path": os.path.join(data_dirname, file_name)}
    for key, file_name in _filenames
}

_listable_filenames = ["CloudLogo1", "CloudLogo2", "CloudLogo3", "CloudLogo4"]
_hierarchy_filenames = [
    "file01.txt",
    "parent/",
    "parent/file11.txt",
    "parent/child/file21.txt",
    "parent/child/file22.txt",
    "parent/child/grand/file31.txt",
    "parent/child/other/file32.txt",
]

ebh_bucket_iteration = 0

_key_name_format = "projects/{}/locations/{}/keyRings/{}/cryptoKeys/{}"

keyring_name = "gcs-test"
default_key_name = "gcs-test"
alt_key_name = "gcs-test-alternate"


def _kms_key_name(client, bucket, key_name):
    return _key_name_format.format(
        client.project,
        bucket.location.lower(),
        keyring_name,
        key_name,
    )


@pytest.fixture(scope="session")
def run_system_tests_on_preprod():
    return os.getenv("RUN_SYSTEM_TESTS_ON_PREPROD") == "True"


@pytest.fixture(scope="session")
def storage_client(run_system_tests_on_preprod):
    from google.cloud.storage import Client

    client = Client(
        client_options=ClientOptions(api_endpoint=PREPROD_JSON_HOST)
        if run_system_tests_on_preprod
        else None
    )
    with contextlib.closing(client):
        yield client


@pytest.fixture(scope="session")
def user_project():
    if _helpers.user_project is None:
        pytest.skip("USER_PROJECT not set in environment.")
    return _helpers.user_project


@pytest.fixture(scope="session")
def no_mtls():
    if _helpers.testing_mtls:
        pytest.skip("Test incompatible with mTLS.")


@pytest.fixture(scope="session")
def service_account(storage_client):
    from google.oauth2.service_account import Credentials

    if not isinstance(storage_client._credentials, Credentials):
        pytest.skip("These tests require a service account credential")
    return storage_client._credentials


@pytest.fixture(scope="session")
def shared_bucket_name():
    return _helpers.unique_name("gcp-systest")


@pytest.fixture(scope="session")
def shared_bucket(storage_client, shared_bucket_name):
    bucket = storage_client.bucket(shared_bucket_name)
    bucket.versioning_enabled = True
    # Create the bucket only if it doesn't yet exist.
    try:
        storage_client.get_bucket(bucket)
    except exceptions.NotFound:
        _helpers.retry_429_503(bucket.create)()

    yield bucket

    _helpers.delete_bucket(bucket)


@pytest.fixture(scope="session")
def listable_bucket_name():
    return _helpers.unique_name("gcp-systest-listable")


@pytest.fixture(scope="session")
def listable_bucket(storage_client, listable_bucket_name, file_data):
    bucket = storage_client.bucket(listable_bucket_name)
    # Create the bucket only if it doesn't yet exist.
    try:
        storage_client.get_bucket(bucket)
    except exceptions.NotFound:
        _helpers.retry_429_503(bucket.create)()

    info = file_data["logo"]
    source_blob = bucket.blob(_listable_filenames[0])
    source_blob.upload_from_filename(info["path"], retry=DEFAULT_RETRY)

    for filename in _listable_filenames[1:]:
        _helpers.retry_bad_copy(bucket.copy_blob)(
            source_blob,
            bucket,
            filename,
        )

    yield bucket

    _helpers.delete_bucket(bucket)


@pytest.fixture(scope="session")
def listable_filenames():
    return _listable_filenames


@pytest.fixture(scope="session")
def hierarchy_bucket_name():
    return _helpers.unique_name("gcp-systest-hierarchy")


@pytest.fixture(scope="session")
def hierarchy_bucket(storage_client, hierarchy_bucket_name, file_data):
    bucket = storage_client.bucket(hierarchy_bucket_name)
    # Create the hierarchy bucket only if it doesn't yet exist.
    try:
        storage_client.get_bucket(bucket)
    except exceptions.NotFound:
        _helpers.retry_429_503(bucket.create)()

    simple_path = _file_data["simple"]["path"]
    for filename in _hierarchy_filenames:
        blob = bucket.blob(filename)
        blob.upload_from_filename(simple_path, retry=DEFAULT_RETRY)

    yield bucket

    _helpers.delete_bucket(bucket)


@pytest.fixture(scope="session")
def hierarchy_filenames():
    return _hierarchy_filenames


@pytest.fixture(scope="session")
def signing_bucket_name():
    return _helpers.unique_name("gcp-systest-signing")


@pytest.fixture(scope="session")
def signing_bucket(storage_client, signing_bucket_name):
    bucket = storage_client.bucket(signing_bucket_name)
    # Create the bucket only if it doesn't yet exist.
    try:
        storage_client.get_bucket(bucket)
    except exceptions.NotFound:
        _helpers.retry_429_503(bucket.create)()

    blob = bucket.blob("README.txt")
    blob.upload_from_string(_helpers.signing_blob_content)

    yield bucket

    _helpers.delete_bucket(bucket)


@pytest.fixture(scope="function")
def default_ebh_bucket_name():
    # Keep track of how many ebh buckets have been created so we can get a
    # clean one each rerun. "unique_name" is unique per test iteration, not
    # per test rerun.
    global ebh_bucket_iteration
    ebh_bucket_iteration += 1
    return _helpers.unique_name("gcp-systest-default-ebh") + "-{}".format(
        ebh_bucket_iteration
    )


# ebh_bucket/name are not scope=session because the bucket is modified in test.
@pytest.fixture(scope="function")
def default_ebh_bucket(storage_client, default_ebh_bucket_name):
    bucket = storage_client.bucket(default_ebh_bucket_name)
    bucket.default_event_based_hold = True
    # Create the bucket only if it doesn't yet exist.
    try:
        storage_client.get_bucket(bucket)
    except exceptions.NotFound:
        _helpers.retry_429_503(bucket.create)()

    yield bucket

    _helpers.delete_bucket(bucket)


@pytest.fixture(scope="function")
def buckets_to_delete():
    buckets_to_delete = []

    yield buckets_to_delete

    for bucket in buckets_to_delete:
        _helpers.delete_bucket(bucket)


@pytest.fixture(scope="function")
def blobs_to_delete():
    blobs_to_delete = []

    yield blobs_to_delete

    for blob in blobs_to_delete:
        _helpers.delete_blob(blob)


@pytest.fixture(scope="session")
def file_data():
    for file_data in _file_data.values():
        with open(file_data["path"], "rb") as file_obj:
            file_data["hash"] = _base64_md5hash(file_obj)

    return _file_data


@pytest.fixture(scope="function")
def kms_bucket_name():
    return _helpers.unique_name("gcp-systest-kms")


@pytest.fixture(scope="function")
def kms_bucket(storage_client, kms_bucket_name, no_mtls):
    bucket = _helpers.retry_429_503(storage_client.create_bucket)(kms_bucket_name)

    yield bucket

    _helpers.delete_bucket(bucket)


@pytest.fixture(scope="function")
def kms_key_name(storage_client, kms_bucket):
    return _kms_key_name(storage_client, kms_bucket, default_key_name)


@pytest.fixture(scope="function")
def alt_kms_key_name(storage_client, kms_bucket):
    return _kms_key_name(storage_client, kms_bucket, alt_key_name)


@pytest.fixture(scope="session")
def kms_client():
    return kms.KeyManagementServiceClient()


@pytest.fixture(scope="function")
def keyring(storage_client, kms_bucket, kms_client):
    project = storage_client.project
    location = kms_bucket.location.lower()
    purpose = kms.enums.CryptoKey.CryptoKeyPurpose.ENCRYPT_DECRYPT

    # If the keyring doesn't exist create it.
    keyring_path = kms_client.key_ring_path(project, location, keyring_name)

    try:
        kms_client.get_key_ring(keyring_path)
    except exceptions.NotFound:
        parent = kms_client.location_path(project, location)
        kms_client.create_key_ring(parent, keyring_name, {})

        # Mark this service account as an owner of the new keyring
        service_account_email = storage_client.get_service_account_email()
        policy = {
            "bindings": [
                {
                    "role": "roles/cloudkms.cryptoKeyEncrypterDecrypter",
                    "members": ["serviceAccount:" + service_account_email],
                }
            ]
        }
        kms_client.set_iam_policy(keyring_path, policy)

    # Populate the keyring with the keys we use in the tests
    key_names = [
        "gcs-test",
        "gcs-test-alternate",
        "explicit-kms-key-name",
        "default-kms-key-name",
        "override-default-kms-key-name",
        "alt-default-kms-key-name",
    ]
    for key_name in key_names:
        key_path = kms_client.crypto_key_path(project, location, keyring_name, key_name)
        try:
            kms_client.get_crypto_key(key_path)
        except exceptions.NotFound:
            key = {"purpose": purpose}
            kms_client.create_crypto_key(keyring_path, key_name, key)


@pytest.fixture(scope="function")
def test_universe_domain():
    if _helpers.test_universe_domain is None:
        pytest.skip("TEST_UNIVERSE_DOMAIN not set in environment.")
    return _helpers.test_universe_domain


@pytest.fixture(scope="function")
def test_universe_project_id():
    if _helpers.test_universe_project_id is None:
        pytest.skip("TEST_UNIVERSE_PROJECT_ID not set in environment.")
    return _helpers.test_universe_project_id


@pytest.fixture(scope="function")
def test_universe_location():
    if _helpers.test_universe_location is None:
        pytest.skip("TEST_UNIVERSE_LOCATION not set in environment.")
    return _helpers.test_universe_location


@pytest.fixture(scope="function")
def test_universe_domain_credential():
    if _helpers.test_universe_domain_credential is None:
        pytest.skip("TEST_UNIVERSE_DOMAIN_CREDENTIAL not set in environment.")
    return _helpers.test_universe_domain_credential


@pytest.fixture(scope="function")
def universe_domain_credential(test_universe_domain_credential):
    from google.oauth2 import service_account

    return service_account.Credentials.from_service_account_file(
        test_universe_domain_credential
    )


@pytest.fixture(scope="function")
def universe_domain_client(
    test_universe_domain, test_universe_project_id, universe_domain_credential
):
    from google.cloud.storage import Client

    client_options = {"universe_domain": test_universe_domain}
    ud_storage_client = Client(
        project=test_universe_project_id,
        credentials=universe_domain_credential,
        client_options=client_options,
    )
    with contextlib.closing(ud_storage_client):
        yield ud_storage_client


@pytest.fixture(scope="function")
def universe_domain_bucket(universe_domain_client, test_universe_location):
    bucket_name = _helpers.unique_name("gcp-systest-ud")
    bucket = universe_domain_client.create_bucket(
        bucket_name, location=test_universe_location
    )

    blob = bucket.blob("README.txt")
    blob.upload_from_string(_helpers.signing_blob_content)

    yield bucket

    _helpers.delete_bucket(bucket)


@pytest.fixture(scope="function")
def universe_domain_iam_client(
    test_universe_domain, test_universe_project_id, universe_domain_credential
):
    from google.cloud import iam_credentials_v1

    client_options = {"universe_domain": test_universe_domain}
    iam_client = iam_credentials_v1.IAMCredentialsClient(
        credentials=universe_domain_credential,
        client_options=client_options,
    )

    return iam_client


@pytest.fixture(scope="function")
def exporter():
    if _global_exporter is None:
        pytest.fail("OpenTelemetry is not installed or failed to initialize.")
    _global_exporter.clear()
    return _global_exporter
