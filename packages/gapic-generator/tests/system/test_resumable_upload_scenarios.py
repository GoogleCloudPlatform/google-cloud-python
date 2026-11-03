# Copyright 2026 Google LLC
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

"""System tests for GAPIC Resumable Upload protocol scenarios against gapic-showcase.

Covers both `ResumableUploadSession` and end-to-end `ResumableUploadServiceClient` /
`ResumableUploadServiceAsyncClient` across default `grpc`/`grpc_asyncio` and
`rest`/`rest_asyncio` transports:
- Section 2.2 Chunk Granularity Suite (`chunk_granularity`)
- Section 2.3 Error Recovery Suite (`non_fatal_error_on_chunk_upload`: Category 1
  transient retries, Category 2 protocol recovery at offset 0 / chunk 2 /
  finalizing chunk, and repeated no-header failures until global deadline exceeded)
- Section 2.4 Error on Start Suite (`non_fatal_error_on_start` &
  `fatal_error_on_start`: 503 retry, 400 rejection, retry exhaustion, fatal
  403/404 immediate failure, and sequential session isolation)
"""

import datetime
import io
import json
import os
import time
from typing import List
import uuid
import pytest

from google.auth import credentials as ga_credentials
from google.api_core import exceptions as core_exceptions
from google.api_core import retry as retries
from google.api_core.resumable_transfer import (
    ProgressState,
    ResumableUploadConfig,
    ResumableUploadSession,
    UploadProgress,
)
from google.showcase import (
    ResumableUploadServiceClient,
    UploadMediaRequest,
    UploadMediaResponse,
)

from conftest import (
    HAS_ASYNC_REST_RESUMABLE_UPLOAD_TRANSPORT,
    make_resumable_upload,
)

if os.environ.get("GAPIC_PYTHON_ASYNC", "true") == "true":
    from conftest import async_anonymous_credentials
    from google.showcase import ResumableUploadServiceAsyncClient


SHOWCASE_API_ENDPOINT = "http://localhost:7469"

FAST_RETRY = retries.Retry(initial=0.05, maximum=0.2, multiplier=1.5, timeout=5.0)
FAST_STREAMING_RETRY = retries.StreamingRetry(
    initial=0.05, maximum=0.2, multiplier=1.5, timeout=5.0
)
FAST_ASYNC_RETRY = retries.AsyncRetry(
    initial=0.05, maximum=0.2, multiplier=1.5, timeout=5.0
)
FAST_ASYNC_STREAMING_RETRY = retries.AsyncStreamingRetry(
    initial=0.05, maximum=0.2, multiplier=1.5, timeout=5.0
)


def test_resumable_upload_scenario_non_fatal_start_error(intercepted_resumable_upload_rest):
    client, _ = intercepted_resumable_upload_rest
    initial_url = f"{client.transport._host}/resumable/upload/v1beta1/media/upload"
    request_body = '{"name": "retry_start_upload.txt"}'
    stream = io.BytesIO(b"Hello world!")

    # Injects 503 error on start attempt, which gets automatically retried
    scenario_headers = [
        ("X-Goog-Test-Scenario", "non_fatal_error_on_start"),
        (
            "X-Goog-Test-Scenario-Config",
            json.dumps({"client_uuid": str(uuid.uuid4()), "error_code": 503, "failure_count": 1}),
        ),
    ]

    response = make_resumable_upload(
        transport=client.transport._session,
        request_body=request_body,
        stream=stream,
        upload_url=initial_url,
        chunk_size=256,
        headers=scenario_headers,
    )
    assert isinstance(response, bytes)
    final_response = UploadMediaResponse.from_json(response)
    assert final_response.name == "retry_start_upload.txt"
    assert final_response.size == len(stream.getvalue())


def test_resumable_upload_scenario_fatal_start_error(intercepted_resumable_upload_rest):
    client, _ = intercepted_resumable_upload_rest
    initial_url = f"{client.transport._host}/resumable/upload/v1beta1/media/upload"
    request_body = '{"name": "fatal_start_upload.txt"}'
    stream = io.BytesIO(b"Hello fatal error!")

    # Injects 403 Forbidden error on start attempt (Category 3 unretriable error)
    scenario_headers = [
        ("X-Goog-Test-Scenario", "fatal_error_on_start"),
        ("X-Goog-Test-Scenario-Config", '{"error_code":403}'),
    ]

    with pytest.raises(core_exceptions.Forbidden):
        make_resumable_upload(
            transport=client.transport._session,
            request_body=request_body,
            stream=stream,
            upload_url=initial_url,
            headers=scenario_headers,
        )


@pytest.mark.skip(reason="https://github.com/googleapis/gapic-showcase/issues/1685")
def test_resumable_upload_scenario_missing_status_header_start_retry(intercepted_resumable_upload_rest):
    client, _ = intercepted_resumable_upload_rest
    initial_url = f"{client.transport._host}/resumable/upload/v1beta1/media/upload"
    request_body = '{"name": "missing_status_header_upload.txt"}'
    stream = io.BytesIO(b"Retrying on missing status header!")

    # Intercept first start response and strip X-Goog-Upload-Status header to test Category 1 retry
    original_send = client.transport._session.send
    attempt_count = [0]

    def intercepting_send(request, **kwargs):
        resp = original_send(request, **kwargs)
        if request.headers.get("X-Goog-Upload-Command") == "start":
            attempt_count[0] += 1
            if attempt_count[0] == 1:
                # Strip X-Goog-Upload-Status on first attempt
                resp.headers.pop("X-Goog-Upload-Status", None)
                resp.headers.pop("x-goog-upload-status", None)
        return resp

    client.transport._session.send = intercepting_send
    try:
        response = make_resumable_upload(
            transport=client.transport._session,
            request_body=request_body,
            stream=stream,
            upload_url=initial_url,
        )
        assert isinstance(response, bytes)
        assert attempt_count[0] >= 2  # Verified that start was retried upon missing status header
        final_response = UploadMediaResponse.from_json(response)
        assert final_response.name == "missing_status_header_upload.txt"
        assert final_response.size == len(stream.getvalue())
    finally:
        client.transport._session.send = original_send


def test_resumable_upload_scenario_non_fatal_chunk_error(intercepted_resumable_upload_rest):
    client, _ = intercepted_resumable_upload_rest
    initial_url = f"{client.transport._host}/resumable/upload/v1beta1/media/upload"
    request_body = '{"name": "recovered_chunk_upload.txt"}'
    stream = io.BytesIO(b"A" * 1024)

    # Injects 503 error on first chunk attempt, which ResumableUploadSession recovers via in-memory buffer
    scenario_headers = [
        ("X-Goog-Test-Scenario", "non_fatal_error_on_chunk_upload"),
        ("X-Goog-Test-Scenario-Config", '{"error_code":503,"failure_count":1,"after_offset":0}'),
    ]

    response = make_resumable_upload(
        transport=client.transport._session,
        request_body=request_body,
        stream=stream,
        upload_url=initial_url,
        chunk_size=512,
        headers=scenario_headers,
    )
    assert isinstance(response, bytes)
    final_response = UploadMediaResponse.from_json(response)
    assert final_response.name == "recovered_chunk_upload.txt"
    assert final_response.size == len(stream.getvalue())


def test_resumable_upload_partial_commit_recovery(intercepted_resumable_upload_rest):
    client, _ = intercepted_resumable_upload_rest
    initial_url = f"{client.transport._host}/resumable/upload/v1beta1/media/upload"
    request_body = '{"name": "partial_commit_upload.txt"}'
    data = b"0123456789" * 50
    stream = io.BytesIO(data)

    # Injects 503 error after server commits only 100 bytes of the chunk
    scenario_headers = [
        ("X-Goog-Test-Scenario", "partial_commit_on_chunk_upload"),
        ("X-Goog-Test-Scenario-Config", '{"error_code":503,"failure_count":1,"after_offset":0,"partial_bytes":100}'),
    ]

    response = make_resumable_upload(
        transport=client.transport._session,
        request_body=request_body,
        stream=stream,
        upload_url=initial_url,
        chunk_size=256,
        headers=scenario_headers,
    )
    assert isinstance(response, bytes)
    final_response = UploadMediaResponse.from_json(response)
    assert final_response.name == "partial_commit_upload.txt"
    assert final_response.size == len(data)


def test_resumable_upload_chunk_granularity_alignment(intercepted_resumable_upload_rest):
    client, _ = intercepted_resumable_upload_rest
    initial_url = f"{client.transport._host}/resumable/upload/v1beta1/media/upload"
    request_body = '{"name": "granularity_upload.txt"}'
    data = b"X" * 1000
    stream = io.BytesIO(data)

    # Server enforces 256 byte chunk granularity
    scenario_headers = [
        ("X-Goog-Test-Scenario", "chunk_granularity"),
    ]

    response = make_resumable_upload(
        transport=client.transport._session,
        request_body=request_body,
        stream=stream,
        upload_url=initial_url,
        chunk_size=300,  # Request unaligned chunk size (300) -> state machine aligns up to 512
        headers=scenario_headers,
    )
    assert isinstance(response, bytes)
    final_response = UploadMediaResponse.from_json(response)
    assert final_response.name == "granularity_upload.txt"
    assert final_response.size == len(data)


def test_chunk_granularity_alignment_1mb(intercepted_resumable_upload_rest):
    """Chunk Granularity Suite Case 1: 1 MB upload with unaligned chunk_size=300_000."""
    client, _ = intercepted_resumable_upload_rest
    initial_url = f"{client.transport._host}/resumable/upload/v1beta1/media/upload"
    total_size = 1_000_000
    payload = b"G" * total_size
    stream = io.BytesIO(payload)

    config = ResumableUploadConfig(
        chunk_size=300_000,
        headers=[
            ("X-Goog-Test-Scenario", "chunk_granularity"),
            ("Content-Type", "application/json"),
        ],
    )
    session = ResumableUploadSession(
        upload_url=initial_url,
        config=config,
        transport=client.transport._session,
        response_type=UploadMediaResponse,
    )

    progress_records = list(
        session.iter_upload(
            stream,
            request_body='{"name": "granularity_1mb.bin"}',
            size=total_size,
            timeout=5.0,
        )
    )

    assert session.chunk_size == 300_032
    assert isinstance(session.response, UploadMediaResponse)
    assert session.response.size == total_size

    phases = [p.state for p in progress_records]
    offsets = [p.bytes_uploaded for p in progress_records]
    assert phases == [
        ProgressState.STARTED,
        ProgressState.UPLOADING,
        ProgressState.UPLOADING,
        ProgressState.UPLOADING,
        ProgressState.FINALIZED,
    ]
    assert offsets == [0, 300_032, 600_064, 900_096, 1_000_000]


def test_cat1_error_retried(intercepted_resumable_upload_rest):
    """Error Recovery Suite Case 1: 503 transient error on chunk 1 at offset 0."""
    client, _ = intercepted_resumable_upload_rest
    initial_url = f"{client.transport._host}/resumable/upload/v1beta1/media/upload"
    chunk_size = 262_144
    total_size = 3 * chunk_size  # 786_432
    payload = b"C" * total_size
    stream = io.BytesIO(payload)

    scenario_headers = [
        ("X-Goog-Test-Scenario", "non_fatal_error_on_chunk_upload"),
        (
            "X-Goog-Test-Scenario-Config",
            '{"error_code":503,"failure_count":1,"after_offset":0}',
        ),
        ("Content-Type", "application/json"),
    ]
    config = ResumableUploadConfig(chunk_size=chunk_size, headers=scenario_headers)
    session = ResumableUploadSession(
        upload_url=initial_url,
        config=config,
        transport=client.transport._session,
        response_type=UploadMediaResponse,
    )

    progress_records = list(
        session.iter_upload(
            stream,
            request_body='{"name": "cat1_503.bin"}',
            size=total_size,
            retry=FAST_STREAMING_RETRY,
        )
    )

    assert isinstance(session.response, UploadMediaResponse)
    assert session.response.size == total_size
    assert progress_records[-1].state == ProgressState.FINALIZED
    assert progress_records[-1].bytes_uploaded == total_size


def test_simple_cat2_error_recovery(intercepted_resumable_upload_rest):
    """Error Recovery Suite Case 2: Category 2 error recovery at offset 0."""
    client, _ = intercepted_resumable_upload_rest
    initial_url = f"{client.transport._host}/resumable/upload/v1beta1/media/upload"
    chunk_size = 262_144
    total_size = 3 * chunk_size  # 786_432
    payload = b"D" * total_size
    stream = io.BytesIO(payload)

    scenario_headers = [
        ("X-Goog-Test-Scenario", "non_fatal_error_on_chunk_upload"),
        (
            "X-Goog-Test-Scenario-Config",
            '{"error_code":412,"failure_count":1,"after_offset":0}',
        ),
        ("Content-Type", "application/json"),
    ]
    config = ResumableUploadConfig(chunk_size=chunk_size, headers=scenario_headers)
    session = ResumableUploadSession(
        upload_url=initial_url,
        config=config,
        transport=client.transport._session,
        response_type=UploadMediaResponse,
    )

    progress_records = list(
        session.iter_upload(
            stream,
            request_body='{"name": "cat2_offset_0.bin"}',
            size=total_size,
            retry=FAST_STREAMING_RETRY,
        )
    )

    assert isinstance(session.response, UploadMediaResponse)
    assert session.response.size == total_size

    phases = [p.state for p in progress_records]
    offsets = [p.bytes_uploaded for p in progress_records]
    assert phases == [
        ProgressState.STARTED,
        ProgressState.RECOVERING,
        ProgressState.OFFSET_RECEIVED,
        ProgressState.UPLOADING,
        ProgressState.UPLOADING,
        ProgressState.FINALIZED,
    ]
    assert offsets == [0, 0, 0, 262_144, 524_288, 786_432]


def test_two_consecutive_cat2_recoveries_on_chunk_2(intercepted_resumable_upload_rest):
    """Error Recovery Suite Case 3: Two consecutive Category 2 recoveries on chunk 2."""
    client, _ = intercepted_resumable_upload_rest
    initial_url = f"{client.transport._host}/resumable/upload/v1beta1/media/upload"
    chunk_size = 262_144
    total_size = 3 * chunk_size  # 786_432
    payload = b"E" * total_size
    stream = io.BytesIO(payload)

    scenario_headers = [
        ("X-Goog-Test-Scenario", "non_fatal_error_on_chunk_upload"),
        (
            "X-Goog-Test-Scenario-Config",
            '{"error_code":412,"failure_count":2,"after_offset":262144}',
        ),
        ("Content-Type", "application/json"),
    ]
    config = ResumableUploadConfig(chunk_size=chunk_size, headers=scenario_headers)
    session = ResumableUploadSession(
        upload_url=initial_url,
        config=config,
        transport=client.transport._session,
        response_type=UploadMediaResponse,
    )

    progress_records = list(
        session.iter_upload(
            stream,
            request_body='{"name": "cat2_two_on_chunk_2.bin"}',
            size=total_size,
            retry=FAST_STREAMING_RETRY,
        )
    )

    assert isinstance(session.response, UploadMediaResponse)
    assert session.response.size == total_size

    phases = [p.state for p in progress_records]
    offsets = [p.bytes_uploaded for p in progress_records]
    assert phases == [
        ProgressState.STARTED,
        ProgressState.UPLOADING,
        ProgressState.RECOVERING,
        ProgressState.OFFSET_RECEIVED,
        ProgressState.RECOVERING,
        ProgressState.OFFSET_RECEIVED,
        ProgressState.UPLOADING,
        ProgressState.FINALIZED,
    ]
    assert offsets == [0, 262_144, 262_144, 262_144, 262_144, 262_144, 524_288, 786_432]


def test_cat2_failure_on_finalizing_chunk(intercepted_resumable_upload_rest):
    """Error Recovery Suite Case 4: Category 2 failure on the finalizing chunk."""
    client, _ = intercepted_resumable_upload_rest
    initial_url = f"{client.transport._host}/resumable/upload/v1beta1/media/upload"
    chunk_size = 262_144
    total_size = 3 * chunk_size - 100  # 786_332
    payload = b"F" * total_size
    stream = io.BytesIO(payload)

    scenario_headers = [
        ("X-Goog-Test-Scenario", "non_fatal_error_on_chunk_upload"),
        (
            "X-Goog-Test-Scenario-Config",
            '{"error_code":412,"failure_count":1,"after_offset":524288}',
        ),
        ("Content-Type", "application/json"),
    ]
    config = ResumableUploadConfig(chunk_size=chunk_size, headers=scenario_headers)
    session = ResumableUploadSession(
        upload_url=initial_url,
        config=config,
        transport=client.transport._session,
        response_type=UploadMediaResponse,
    )

    progress_records = list(
        session.iter_upload(
            stream,
            request_body='{"name": "cat2_finalizing_chunk.bin"}',
            size=total_size,
            retry=FAST_STREAMING_RETRY,
        )
    )

    assert isinstance(session.response, UploadMediaResponse)
    assert session.response.size == total_size

    phases = [p.state for p in progress_records]
    offsets = [p.bytes_uploaded for p in progress_records]
    assert phases == [
        ProgressState.STARTED,
        ProgressState.UPLOADING,
        ProgressState.UPLOADING,
        ProgressState.RECOVERING,
        ProgressState.OFFSET_RECEIVED,
        ProgressState.FINALIZED,
    ]
    assert offsets == [0, 262_144, 524_288, 524_288, 524_288, 786_332]


def test_no_headers_failure_recovers_until_deadline_exceeded(intercepted_resumable_upload_rest):
    """Error Recovery Suite Case 5: Repeated no-header failures until global deadline exceeded."""
    client, _ = intercepted_resumable_upload_rest
    initial_url = f"{client.transport._host}/resumable/upload/v1beta1/media/upload"
    chunk_size = 262_144
    payload = b"T" * chunk_size
    stream = io.BytesIO(payload)

    scenario_headers = [
        ("X-Goog-Test-Scenario", "non_fatal_error_on_chunk_upload"),
        (
            "X-Goog-Test-Scenario-Config",
            '{"failure_count":0,"action_after_failures":"terminate"}',
        ),
        ("Content-Type", "application/json"),
    ]
    deadline = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=1.0)
    config = ResumableUploadConfig(
        chunk_size=chunk_size,
        deadline=deadline,
        headers=scenario_headers,
    )
    session = ResumableUploadSession(
        upload_url=initial_url,
        config=config,
        transport=client.transport._session,
        response_type=UploadMediaResponse,
    )

    progress_records = []
    with pytest.raises((core_exceptions.DeadlineExceeded, core_exceptions.RetryError)):
        for progress in session.iter_upload(
            stream,
            request_body='{"name": "terminate_until_deadline.bin"}',
            size=chunk_size,
            retry=FAST_STREAMING_RETRY,
        ):
            progress_records.append(progress)

    recovering_count = sum(1 for p in progress_records if p.state == ProgressState.RECOVERING)
    assert recovering_count >= 1


def test_non_fatal_error_on_start_503(intercepted_resumable_upload_rest):
    """Error on Start Suite Case 1: Single 503 on start with fast retry."""
    client, _ = intercepted_resumable_upload_rest
    initial_url = f"{client.transport._host}/resumable/upload/v1beta1/media/upload"
    payload = b"s" * 100
    stream = io.BytesIO(payload)

    scenario_headers = [
        ("X-Goog-Test-Scenario", "non_fatal_error_on_start"),
        (
            "X-Goog-Test-Scenario-Config",
            json.dumps(
                {"client_uuid": str(uuid.uuid4()), "error_code": 503, "failure_count": 1}
            ),
        ),
        ("Content-Type", "application/json"),
    ]
    config = ResumableUploadConfig(headers=scenario_headers)
    session = ResumableUploadSession(
        upload_url=initial_url,
        config=config,
        transport=client.transport._session,
        response_type=UploadMediaResponse,
        start_retry=FAST_RETRY,
    )

    progress_records = list(
        session.iter_upload(stream, request_body='{"name": "start_503.bin"}', size=100)
    )

    assert isinstance(session.response, UploadMediaResponse)
    assert session.response.size == 100
    phases = [p.state for p in progress_records]
    assert phases.count(ProgressState.STARTED) == 1
    assert phases[-1] == ProgressState.FINALIZED


def test_upload_rejection_400_on_start(intercepted_resumable_upload_rest):
    """Test Case 2: Protocol-level 400 Bad Request rejection during session initiation."""
    client, _ = intercepted_resumable_upload_rest
    initial_url = f"{client.transport._host}/resumable/upload/v1beta1/media/upload"
    payload = b"r" * 100
    stream = io.BytesIO(payload)

    # Invalid JSON in X-Goog-Test-Scenario-Config or injected 400 on start
    scenario_headers = [
        ("X-Goog-Test-Scenario", "non_fatal_error_on_start"),
        (
            "X-Goog-Test-Scenario-Config",
            json.dumps(
                {"client_uuid": str(uuid.uuid4()), "error_code": 400, "failure_count": 1}
            ),
        ),
        ("Content-Type", "application/json"),
    ]
    config = ResumableUploadConfig(headers=scenario_headers)
    session = ResumableUploadSession(
        upload_url=initial_url,
        config=config,
        transport=client.transport._session,
        response_type=UploadMediaResponse,
    )

    with pytest.raises(core_exceptions.BadRequest) as exc_info:
        session.upload(stream, request_body="{}", size=100)

    assert exc_info.value.code == 400


def test_retry_exhaustion_on_start_times_out(intercepted_resumable_upload_rest):
    """Error on Start Suite Case 3: Repeated 503 on start until session deadline expires."""
    client, _ = intercepted_resumable_upload_rest
    initial_url = f"{client.transport._host}/resumable/upload/v1beta1/media/upload"
    payload = b"t" * 100
    stream = io.BytesIO(payload)

    scenario_headers = [
        ("X-Goog-Test-Scenario", "non_fatal_error_on_start"),
        (
            "X-Goog-Test-Scenario-Config",
            json.dumps(
                {
                    "client_uuid": str(uuid.uuid4()),
                    "error_code": 503,
                    "failure_count": 10_000,
                }
            ),
        ),
        ("Content-Type", "application/json"),
    ]
    deadline = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=2.0)
    config = ResumableUploadConfig(headers=scenario_headers, deadline=deadline)
    session = ResumableUploadSession(
        upload_url=initial_url,
        config=config,
        transport=client.transport._session,
        response_type=UploadMediaResponse,
        start_retry=retries.Retry(initial=0.2, maximum=0.5, multiplier=1.5, timeout=2.0),
    )

    progress_records = []
    t_start = time.monotonic()
    with pytest.raises((core_exceptions.GoogleAPICallError, core_exceptions.RetryError)):
        for progress in session.iter_upload(
            stream, request_body='{"name": "start_exhaustion.bin"}', size=100
        ):
            progress_records.append(progress)
    elapsed = time.monotonic() - t_start

    assert elapsed >= 1.5
    phases = [p.state for p in progress_records]
    assert ProgressState.UPLOADING not in phases


@pytest.mark.parametrize(
    "status_code,expected_exc",
    [
        (403, core_exceptions.Forbidden),
        (404, core_exceptions.NotFound),
    ],
)
def test_fatal_error_on_start_raises_immediately(
    intercepted_resumable_upload_rest, status_code, expected_exc
):
    """Error on Start Suite Case 4: Fatal 403 and 404 on start fail immediately without retry."""
    client, _ = intercepted_resumable_upload_rest
    initial_url = f"{client.transport._host}/resumable/upload/v1beta1/media/upload"
    payload = b"f" * 100
    stream = io.BytesIO(payload)

    scenario_headers = [
        ("X-Goog-Test-Scenario", "fatal_error_on_start"),
        ("X-Goog-Test-Scenario-Config", json.dumps({"error_code": status_code})),
        ("Content-Type", "application/json"),
    ]
    config = ResumableUploadConfig(headers=scenario_headers)
    session = ResumableUploadSession(
        upload_url=initial_url,
        config=config,
        transport=client.transport._session,
        response_type=UploadMediaResponse,
    )

    progress_records = []
    t_start = time.monotonic()
    with pytest.raises(expected_exc) as exc_info:
        for progress in session.iter_upload(
            stream, request_body='{"name": "fatal_start.bin"}', size=100
        ):
            progress_records.append(progress)
    elapsed = time.monotonic() - t_start

    assert exc_info.value.code == status_code
    assert elapsed < 0.5
    phases = [p.state for p in progress_records]
    assert ProgressState.UPLOADING not in phases


def test_sequential_runs_session_isolation(intercepted_resumable_upload_rest):
    """Error on Start Suite Case 5: Sequential runs with distinct client_uuid values."""
    client, _ = intercepted_resumable_upload_rest
    initial_url = f"{client.transport._host}/resumable/upload/v1beta1/media/upload"
    payload = b"i" * 100

    for run_idx in range(2):
        scenario_headers = [
            ("X-Goog-Test-Scenario", "non_fatal_error_on_start"),
            (
                "X-Goog-Test-Scenario-Config",
                json.dumps(
                    {
                        "client_uuid": str(uuid.uuid4()),
                        "error_code": 503,
                        "failure_count": 1,
                    }
                ),
            ),
            ("Content-Type", "application/json"),
        ]
        config = ResumableUploadConfig(headers=scenario_headers)
        session = ResumableUploadSession(
            upload_url=initial_url,
            config=config,
            transport=client.transport._session,
            response_type=UploadMediaResponse,
            start_retry=FAST_RETRY,
        )
        resp = session.upload(
            io.BytesIO(payload),
            request_body=f'{{"name": "isolated_run_{run_idx}.bin"}}',
            size=100,
        )
        assert isinstance(resp, UploadMediaResponse)
        assert resp.name == f"isolated_run_{run_idx}.bin"
        assert resp.size == 100


def test_non_fatal_error_on_query_recovery(intercepted_resumable_upload_rest):
    """Query retry scenario: transient 503 on query during session recovery."""
    client, _ = intercepted_resumable_upload_rest
    initial_url = f"{client.transport._host}/resumable/upload/v1beta1/media/upload"
    chunk_size = 262_144
    total_size = 2 * chunk_size  # 524_288
    payload = b"Q" * total_size
    stream = io.BytesIO(payload)

    scenario_headers = [
        ("X-Goog-Test-Scenario", "non_fatal_error_on_query"),
        (
            "X-Goog-Test-Scenario-Config",
            json.dumps({"error_code": 503, "failure_count": 1}),
        ),
        ("Content-Type", "application/json"),
    ]
    config = ResumableUploadConfig(chunk_size=chunk_size, headers=scenario_headers)
    session = ResumableUploadSession(
        upload_url=initial_url,
        config=config,
        transport=client.transport._session,
        response_type=UploadMediaResponse,
    )
    session._initiate(
        transport=client.transport._session,
        request_body='{"name": "query_retry.bin"}',
        size=total_size,
    )
    session._transmit_chunk(client.transport._session, stream, total_size)
    assert session.bytes_uploaded == chunk_size

    # Trigger recovery during _transmit_all_chunks; first query returns 503, second succeeds
    session._needs_recovery = True
    progress_records = list(
        session._transmit_all_chunks(
            client.transport._session,
            stream,
            total_size,
            retry=FAST_STREAMING_RETRY,
        )
    )

    assert isinstance(session.response, UploadMediaResponse)
    assert session.response.name == "query_retry.bin"
    assert session.response.size == total_size
    phases = [p.state for p in progress_records]
    assert ProgressState.RECOVERING in phases
    assert ProgressState.OFFSET_RECEIVED in phases
    assert phases[-1] == ProgressState.FINALIZED


def test_client_upload_media_passes_start_retry(intercepted_resumable_upload_rest):
    """Verify that `retry` passed to `client.upload_media` is forwarded as `start_retry`."""
    client, _ = intercepted_resumable_upload_rest
    payload = b"s" * 100
    stream = io.BytesIO(payload)

    # Injects a single 409 Conflict on start, which is not retried by the default
    # start retry policy unless the custom `retry` passed to `client.upload_media`
    # reaches `ResumableUploadSession(start_retry=...)`.
    scenario_headers = [
        ("X-Goog-Test-Scenario", "non_fatal_error_on_start"),
        (
            "X-Goog-Test-Scenario-Config",
            json.dumps(
                {"client_uuid": str(uuid.uuid4()), "error_code": 409, "failure_count": 1}
            ),
        ),
    ]
    retried_errors = []
    custom_retry = retries.Retry(
        predicate=retries.if_exception_type(core_exceptions.Conflict),
        initial=0.05,
        maximum=0.2,
        multiplier=1.5,
        timeout=5.0,
        on_error=retried_errors.append,
    )

    session = client.upload_media(
        request=UploadMediaRequest(name="client_start_retry.bin"),
        config=ResumableUploadConfig(headers=scenario_headers),
        retry=custom_retry,
    )
    response = session.upload(stream=stream, size=len(payload))

    assert len(retried_errors) == 1
    assert isinstance(retried_errors[0], core_exceptions.Conflict)
    assert isinstance(response, UploadMediaResponse)
    assert response.name == "client_start_retry.bin"
    assert response.size == len(payload)


if os.environ.get("GAPIC_PYTHON_ASYNC", "true") == "true":

    @pytest.mark.asyncio
    async def test_async_client_upload_media_passes_start_retry(
        intercepted_resumable_upload_rest_async,
    ):
        """Verify that `retry` passed to `async_client.upload_media` is forwarded as `start_retry`."""
        client, _ = intercepted_resumable_upload_rest_async
        payload = b"s" * 100
        stream = io.BytesIO(payload)

        scenario_headers = [
            ("X-Goog-Test-Scenario", "non_fatal_error_on_start"),
            (
                "X-Goog-Test-Scenario-Config",
                json.dumps(
                    {
                        "client_uuid": str(uuid.uuid4()),
                        "error_code": 409,
                        "failure_count": 1,
                    }
                ),
            ),
        ]
        retried_errors = []
        custom_retry = retries.AsyncRetry(
            predicate=retries.if_exception_type(core_exceptions.Conflict),
            initial=0.05,
            maximum=0.2,
            multiplier=1.5,
            timeout=5.0,
            on_error=retried_errors.append,
        )

        session = await client.upload_media(
            request=UploadMediaRequest(name="async_client_start_retry.bin"),
            config=ResumableUploadConfig(headers=scenario_headers),
            retry=custom_retry,
        )
        response = await session.upload(stream=stream, size=len(payload))

        assert len(retried_errors) == 1
        assert isinstance(retried_errors[0], core_exceptions.Conflict)
        assert isinstance(response, UploadMediaResponse)
        assert response.name == "async_client_start_retry.bin"
        assert response.size == len(payload)


# =============================================================================
# End-to-End Showcase Client Scenario Suites (gRPC & REST)
# =============================================================================


def _create_sync_client(transport, monkeypatch):
    monkeypatch.setenv("GOOGLE_API_USE_CLIENT_CERTIFICATE", "false")
    return ResumableUploadServiceClient(
        credentials=ga_credentials.AnonymousCredentials(),
        client_options={"api_endpoint": SHOWCASE_API_ENDPOINT},
        transport=transport,
    )


# -----------------------------------------------------------------------------
# 2.2 Chunk Granularity Suite (End-to-End Client across gRPC & REST)
# -----------------------------------------------------------------------------


@pytest.mark.parametrize("transport", ["grpc", "rest"])
def test_client_chunk_granularity_alignment(transport, monkeypatch):
    """Chunk Granularity Suite Case 1: 1 MB upload with unaligned chunk_size=300_000."""
    client = _create_sync_client(transport, monkeypatch)
    total_size = 1_000_000
    stream = io.BytesIO(b"G" * total_size)

    upload_session = client.upload_media(
        request=UploadMediaRequest(name="granularity_1mb.bin"),
        config=ResumableUploadConfig(
            chunk_size=300_000,
            headers=[("X-Goog-Test-Scenario", "chunk_granularity")],
        ),
    )
    progress_records = list(
        upload_session.iter_upload(stream, size=total_size, timeout=5.0)
    )

    assert upload_session.chunk_size == 300_032
    assert isinstance(upload_session.response, UploadMediaResponse)
    assert upload_session.response.size == total_size
    assert [p.state for p in progress_records] == [
        ProgressState.STARTED,
        ProgressState.UPLOADING,
        ProgressState.UPLOADING,
        ProgressState.UPLOADING,
        ProgressState.FINALIZED,
    ]
    assert [p.bytes_uploaded for p in progress_records] == [
        0,
        300_032,
        600_064,
        900_096,
        1_000_000,
    ]


# -----------------------------------------------------------------------------
# 2.3 Error Recovery Suite (End-to-End Client across gRPC & REST)
# -----------------------------------------------------------------------------


@pytest.mark.parametrize("transport", ["grpc", "rest"])
def test_client_cat1_error_retried_transparently(transport, monkeypatch):
    """Error Recovery Suite Case 1: 503 transient error on chunk 1 at offset 0."""
    client = _create_sync_client(transport, monkeypatch)
    chunk_size = 262_144
    total_size = 3 * chunk_size  # 786_432
    stream = io.BytesIO(b"C" * total_size)

    scenario_headers = [
        ("X-Goog-Test-Scenario", "non_fatal_error_on_chunk_upload"),
        (
            "X-Goog-Test-Scenario-Config",
            '{"error_code":503,"failure_count":1,"after_offset":0}',
        ),
    ]
    upload_session = client.upload_media(
        request=UploadMediaRequest(name="cat1_503.bin"),
        config=ResumableUploadConfig(
            chunk_size=chunk_size, headers=scenario_headers
        ),
    )
    progress_records = list(
        upload_session.iter_upload(
            stream, size=total_size, retry=FAST_STREAMING_RETRY
        )
    )

    assert isinstance(upload_session.response, UploadMediaResponse)
    assert upload_session.response.size == total_size
    assert progress_records[-1].state == ProgressState.FINALIZED
    assert progress_records[-1].bytes_uploaded == total_size


@pytest.mark.parametrize("transport", ["grpc", "rest"])
def test_client_simple_cat2_error_recovery(transport, monkeypatch):
    """Error Recovery Suite Case 2: Category 2 error recovery at offset 0."""
    client = _create_sync_client(transport, monkeypatch)
    chunk_size = 262_144
    total_size = 3 * chunk_size  # 786_432
    stream = io.BytesIO(b"D" * total_size)

    scenario_headers = [
        ("X-Goog-Test-Scenario", "non_fatal_error_on_chunk_upload"),
        (
            "X-Goog-Test-Scenario-Config",
            '{"error_code":412,"failure_count":1,"after_offset":0}',
        ),
    ]
    upload_session = client.upload_media(
        request=UploadMediaRequest(name="cat2_offset_0.bin"),
        config=ResumableUploadConfig(
            chunk_size=chunk_size, headers=scenario_headers
        ),
    )
    progress_records = list(
        upload_session.iter_upload(
            stream, size=total_size, retry=FAST_STREAMING_RETRY
        )
    )

    assert isinstance(upload_session.response, UploadMediaResponse)
    assert upload_session.response.size == total_size
    assert [p.state for p in progress_records] == [
        ProgressState.STARTED,
        ProgressState.RECOVERING,
        ProgressState.OFFSET_RECEIVED,
        ProgressState.UPLOADING,
        ProgressState.UPLOADING,
        ProgressState.FINALIZED,
    ]
    assert [p.bytes_uploaded for p in progress_records] == [
        0,
        0,
        0,
        262_144,
        524_288,
        786_432,
    ]


@pytest.mark.parametrize("transport", ["grpc", "rest"])
def test_client_two_consecutive_cat2_recoveries_on_chunk_2(
    transport, monkeypatch
):
    """Error Recovery Suite Case 3: Two consecutive Category 2 recoveries on chunk 2."""
    client = _create_sync_client(transport, monkeypatch)
    chunk_size = 262_144
    total_size = 3 * chunk_size  # 786_432
    stream = io.BytesIO(b"E" * total_size)

    scenario_headers = [
        ("X-Goog-Test-Scenario", "non_fatal_error_on_chunk_upload"),
        (
            "X-Goog-Test-Scenario-Config",
            '{"error_code":412,"failure_count":2,"after_offset":262144}',
        ),
    ]
    upload_session = client.upload_media(
        request=UploadMediaRequest(name="cat2_two_on_chunk_2.bin"),
        config=ResumableUploadConfig(
            chunk_size=chunk_size, headers=scenario_headers
        ),
    )
    progress_records = list(
        upload_session.iter_upload(
            stream, size=total_size, retry=FAST_STREAMING_RETRY
        )
    )

    assert isinstance(upload_session.response, UploadMediaResponse)
    assert upload_session.response.size == total_size
    assert [p.state for p in progress_records] == [
        ProgressState.STARTED,
        ProgressState.UPLOADING,
        ProgressState.RECOVERING,
        ProgressState.OFFSET_RECEIVED,
        ProgressState.RECOVERING,
        ProgressState.OFFSET_RECEIVED,
        ProgressState.UPLOADING,
        ProgressState.FINALIZED,
    ]
    assert [p.bytes_uploaded for p in progress_records] == [
        0,
        262_144,
        262_144,
        262_144,
        262_144,
        262_144,
        524_288,
        786_432,
    ]


@pytest.mark.parametrize("transport", ["grpc", "rest"])
def test_client_cat2_failure_on_finalizing_chunk(transport, monkeypatch):
    """Error Recovery Suite Case 4: Category 2 failure on the finalizing chunk."""
    client = _create_sync_client(transport, monkeypatch)
    chunk_size = 262_144
    total_size = 3 * chunk_size - 100  # 786_332
    stream = io.BytesIO(b"F" * total_size)

    scenario_headers = [
        ("X-Goog-Test-Scenario", "non_fatal_error_on_chunk_upload"),
        (
            "X-Goog-Test-Scenario-Config",
            '{"error_code":412,"failure_count":1,"after_offset":524288}',
        ),
    ]
    upload_session = client.upload_media(
        request=UploadMediaRequest(name="cat2_finalizing_chunk.bin"),
        config=ResumableUploadConfig(
            chunk_size=chunk_size, headers=scenario_headers
        ),
    )
    progress_records = list(
        upload_session.iter_upload(
            stream, size=total_size, retry=FAST_STREAMING_RETRY
        )
    )

    assert isinstance(upload_session.response, UploadMediaResponse)
    assert upload_session.response.size == total_size
    assert [p.state for p in progress_records] == [
        ProgressState.STARTED,
        ProgressState.UPLOADING,
        ProgressState.UPLOADING,
        ProgressState.RECOVERING,
        ProgressState.OFFSET_RECEIVED,
        ProgressState.FINALIZED,
    ]
    assert [p.bytes_uploaded for p in progress_records] == [
        0,
        262_144,
        524_288,
        524_288,
        524_288,
        786_332,
    ]


@pytest.mark.parametrize("transport", ["grpc", "rest"])
def test_client_no_headers_failure_recovers_until_deadline_exceeded(
    transport, monkeypatch
):
    """Error Recovery Suite Case 5: Repeated no-header failures until global deadline exceeded."""
    client = _create_sync_client(transport, monkeypatch)
    chunk_size = 262_144
    stream = io.BytesIO(b"T" * chunk_size)

    scenario_headers = [
        ("X-Goog-Test-Scenario", "non_fatal_error_on_chunk_upload"),
        (
            "X-Goog-Test-Scenario-Config",
            '{"failure_count":0,"action_after_failures":"terminate"}',
        ),
    ]
    deadline = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
        seconds=1.0
    )
    upload_session = client.upload_media(
        request=UploadMediaRequest(name="terminate_until_deadline.bin"),
        config=ResumableUploadConfig(
            chunk_size=chunk_size,
            deadline=deadline,
            headers=scenario_headers,
        ),
    )

    progress_records: List[UploadProgress] = []
    with pytest.raises(
        (core_exceptions.DeadlineExceeded, core_exceptions.RetryError)
    ):
        for progress in upload_session.iter_upload(
            stream, size=chunk_size, retry=FAST_STREAMING_RETRY
        ):
            progress_records.append(progress)

    recovering_count = sum(
        1 for p in progress_records if p.state == ProgressState.RECOVERING
    )
    assert recovering_count >= 1


# -----------------------------------------------------------------------------
# 2.4 Error on Start Suite (End-to-End Client across gRPC & REST)
# -----------------------------------------------------------------------------


@pytest.mark.parametrize("transport", ["grpc", "rest"])
def test_client_non_fatal_error_on_start_503(transport, monkeypatch):
    """Error on Start Suite Case 1: Single 503 on start with fast retry."""
    client = _create_sync_client(transport, monkeypatch)
    stream = io.BytesIO(b"s" * 100)

    scenario_headers = [
        ("X-Goog-Test-Scenario", "non_fatal_error_on_start"),
        (
            "X-Goog-Test-Scenario-Config",
            json.dumps(
                {
                    "client_uuid": str(uuid.uuid4()),
                    "error_code": 503,
                    "failure_count": 1,
                }
            ),
        ),
    ]
    upload_session = client.upload_media(
        request=UploadMediaRequest(name="start_503.bin"),
        config=ResumableUploadConfig(headers=scenario_headers),
        retry=FAST_RETRY,
    )
    progress_records = list(upload_session.iter_upload(stream, size=100))

    assert isinstance(upload_session.response, UploadMediaResponse)
    assert upload_session.response.size == 100
    phases = [p.state for p in progress_records]
    assert phases.count(ProgressState.STARTED) == 1
    assert phases[-1] == ProgressState.FINALIZED


@pytest.mark.parametrize("transport", ["grpc", "rest"])
def test_client_upload_rejection_400_on_start(transport, monkeypatch):
    """Error on Start Suite Case 2: Protocol-level 400 Bad Request rejection on start."""
    client = _create_sync_client(transport, monkeypatch)
    stream = io.BytesIO(b"r" * 100)

    scenario_headers = [
        ("X-Goog-Test-Scenario", "non_fatal_error_on_start"),
        (
            "X-Goog-Test-Scenario-Config",
            json.dumps(
                {
                    "client_uuid": str(uuid.uuid4()),
                    "error_code": 400,
                    "failure_count": 1,
                }
            ),
        ),
    ]
    upload_session = client.upload_media(
        request=UploadMediaRequest(name="reject_400.bin"),
        config=ResumableUploadConfig(headers=scenario_headers),
    )
    with pytest.raises(core_exceptions.BadRequest) as exc_info:
        upload_session.upload(stream, size=100)

    assert exc_info.value.code == 400


@pytest.mark.parametrize("transport", ["grpc", "rest"])
def test_client_retry_exhaustion_on_start_times_out(transport, monkeypatch):
    """Error on Start Suite Case 3: Repeated 503 on start until session deadline expires."""
    client = _create_sync_client(transport, monkeypatch)
    stream = io.BytesIO(b"t" * 100)

    scenario_headers = [
        ("X-Goog-Test-Scenario", "non_fatal_error_on_start"),
        (
            "X-Goog-Test-Scenario-Config",
            json.dumps(
                {
                    "client_uuid": str(uuid.uuid4()),
                    "error_code": 503,
                    "failure_count": 10_000,
                }
            ),
        ),
    ]
    deadline = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
        seconds=2.0
    )
    upload_session = client.upload_media(
        request=UploadMediaRequest(name="start_exhaustion.bin"),
        config=ResumableUploadConfig(
            headers=scenario_headers, deadline=deadline
        ),
        retry=retries.Retry(
            initial=0.2, maximum=0.5, multiplier=1.5, timeout=2.0
        ),
    )

    progress_records: List[UploadProgress] = []
    t_start = time.monotonic()
    with pytest.raises(
        (core_exceptions.GoogleAPICallError, core_exceptions.RetryError)
    ):
        for progress in upload_session.iter_upload(stream, size=100):
            progress_records.append(progress)
    elapsed = time.monotonic() - t_start

    assert elapsed >= 1.5
    phases = [p.state for p in progress_records]
    assert ProgressState.UPLOADING not in phases


@pytest.mark.parametrize("transport", ["grpc", "rest"])
@pytest.mark.parametrize(
    "status_code,expected_exc",
    [
        (403, core_exceptions.Forbidden),
        (404, core_exceptions.NotFound),
    ],
)
def test_client_fatal_error_on_start_raises_immediately(
    transport, status_code, expected_exc, monkeypatch
):
    """Error on Start Suite Case 4: Fatal 403 and 404 on start fail immediately without retry."""
    client = _create_sync_client(transport, monkeypatch)
    stream = io.BytesIO(b"f" * 100)

    scenario_headers = [
        ("X-Goog-Test-Scenario", "fatal_error_on_start"),
        (
            "X-Goog-Test-Scenario-Config",
            json.dumps({"error_code": status_code}),
        ),
    ]
    upload_session = client.upload_media(
        request=UploadMediaRequest(name="fatal_start.bin"),
        config=ResumableUploadConfig(headers=scenario_headers),
    )

    progress_records: List[UploadProgress] = []
    t_start = time.monotonic()
    with pytest.raises(expected_exc) as exc_info:
        for progress in upload_session.iter_upload(stream, size=100):
            progress_records.append(progress)
    elapsed = time.monotonic() - t_start

    assert exc_info.value.code == status_code
    assert elapsed < 0.5
    phases = [p.state for p in progress_records]
    assert ProgressState.UPLOADING not in phases


@pytest.mark.parametrize("transport", ["grpc", "rest"])
def test_client_sequential_runs_session_isolation(transport, monkeypatch):
    """Error on Start Suite Case 5: Sequential runs with distinct client_uuid values."""
    client = _create_sync_client(transport, monkeypatch)
    payload = b"i" * 100

    for run_idx in range(2):
        scenario_headers = [
            ("X-Goog-Test-Scenario", "non_fatal_error_on_start"),
            (
                "X-Goog-Test-Scenario-Config",
                json.dumps(
                    {
                        "client_uuid": str(uuid.uuid4()),
                        "error_code": 503,
                        "failure_count": 1,
                    }
                ),
            ),
        ]
        upload_session = client.upload_media(
            request=UploadMediaRequest(name=f"isolated_run_{run_idx}.bin"),
            config=ResumableUploadConfig(headers=scenario_headers),
            retry=FAST_RETRY,
        )
        resp = upload_session.upload(io.BytesIO(payload), size=100)
        assert isinstance(resp, UploadMediaResponse)
        assert resp.name == f"isolated_run_{run_idx}.bin"
        assert resp.size == 100


if os.environ.get("GAPIC_PYTHON_ASYNC", "true") == "true":

    def _create_async_client(transport, monkeypatch):
        monkeypatch.setenv("GOOGLE_API_USE_CLIENT_CERTIFICATE", "false")
        if not HAS_ASYNC_REST_RESUMABLE_UPLOAD_TRANSPORT:
            pytest.skip("Async REST transport not available.")
        if (
            transport == "rest_asyncio"
            and "rest_asyncio"
            not in ResumableUploadServiceClient._transport_registry
        ):
            pytest.skip(
                "rest_asyncio transport is not registered when rest_async_io_enabled is False."
            )
        return ResumableUploadServiceAsyncClient(
            credentials=async_anonymous_credentials(),
            client_options={"api_endpoint": SHOWCASE_API_ENDPOINT},
            transport=transport,
        )

    @pytest.mark.asyncio
    @pytest.mark.parametrize("transport", ["grpc_asyncio", "rest_asyncio"])
    async def test_async_chunk_granularity_alignment(transport, monkeypatch):
        """Async Chunk Granularity Suite Case 1: 1 MB upload with unaligned chunk_size=300_000."""
        client = _create_async_client(transport, monkeypatch)
        total_size = 1_000_000
        stream = io.BytesIO(b"G" * total_size)

        upload_session = await client.upload_media(
            request=UploadMediaRequest(name="async_granularity_1mb.bin"),
            config=ResumableUploadConfig(
                chunk_size=300_000,
                headers=[("X-Goog-Test-Scenario", "chunk_granularity")],
            ),
        )
        progress_records = [
            p
            async for p in upload_session.upload(
                stream, size=total_size, timeout=5.0
            )
        ]

        assert upload_session.chunk_size == 300_032
        assert isinstance(upload_session.response, UploadMediaResponse)
        assert upload_session.response.size == total_size
        assert [p.state for p in progress_records] == [
            ProgressState.STARTED,
            ProgressState.UPLOADING,
            ProgressState.UPLOADING,
            ProgressState.UPLOADING,
            ProgressState.FINALIZED,
        ]
        assert [p.bytes_uploaded for p in progress_records] == [
            0,
            300_032,
            600_064,
            900_096,
            1_000_000,
        ]

    @pytest.mark.asyncio
    @pytest.mark.parametrize("transport", ["grpc_asyncio", "rest_asyncio"])
    async def test_async_cat1_error_retried_transparently(
        transport, monkeypatch
    ):
        """Async Error Recovery Suite Case 1: 503 transient error on chunk 1 at offset 0."""
        client = _create_async_client(transport, monkeypatch)
        chunk_size = 262_144
        total_size = 3 * chunk_size
        stream = io.BytesIO(b"C" * total_size)

        scenario_headers = [
            ("X-Goog-Test-Scenario", "non_fatal_error_on_chunk_upload"),
            (
                "X-Goog-Test-Scenario-Config",
                '{"error_code":503,"failure_count":1,"after_offset":0}',
            ),
        ]
        upload_session = await client.upload_media(
            request=UploadMediaRequest(name="async_cat1_503.bin"),
            config=ResumableUploadConfig(
                chunk_size=chunk_size, headers=scenario_headers
            ),
        )
        progress_records = [
            p
            async for p in upload_session.upload(
                stream, size=total_size, retry=FAST_ASYNC_STREAMING_RETRY
            )
        ]

        assert isinstance(upload_session.response, UploadMediaResponse)
        assert upload_session.response.size == total_size
        assert progress_records[-1].state == ProgressState.FINALIZED
        assert progress_records[-1].bytes_uploaded == total_size

    @pytest.mark.asyncio
    @pytest.mark.parametrize("transport", ["grpc_asyncio", "rest_asyncio"])
    async def test_async_simple_cat2_error_recovery(transport, monkeypatch):
        """Async Error Recovery Suite Case 2: Category 2 error recovery at offset 0."""
        client = _create_async_client(transport, monkeypatch)
        chunk_size = 262_144
        total_size = 3 * chunk_size
        stream = io.BytesIO(b"D" * total_size)

        scenario_headers = [
            ("X-Goog-Test-Scenario", "non_fatal_error_on_chunk_upload"),
            (
                "X-Goog-Test-Scenario-Config",
                '{"error_code":412,"failure_count":1,"after_offset":0}',
            ),
        ]
        upload_session = await client.upload_media(
            request=UploadMediaRequest(name="async_cat2_offset_0.bin"),
            config=ResumableUploadConfig(
                chunk_size=chunk_size, headers=scenario_headers
            ),
        )
        progress_records = [
            p
            async for p in upload_session.upload(
                stream, size=total_size, retry=FAST_ASYNC_STREAMING_RETRY
            )
        ]

        assert isinstance(upload_session.response, UploadMediaResponse)
        assert upload_session.response.size == total_size
        assert [p.state for p in progress_records] == [
            ProgressState.STARTED,
            ProgressState.RECOVERING,
            ProgressState.OFFSET_RECEIVED,
            ProgressState.UPLOADING,
            ProgressState.UPLOADING,
            ProgressState.FINALIZED,
        ]
        assert [p.bytes_uploaded for p in progress_records] == [
            0,
            0,
            0,
            262_144,
            524_288,
            786_432,
        ]

    @pytest.mark.asyncio
    @pytest.mark.parametrize("transport", ["grpc_asyncio", "rest_asyncio"])
    async def test_async_two_consecutive_cat2_recoveries_on_chunk_2(
        transport, monkeypatch
    ):
        """Async Error Recovery Suite Case 3: Two consecutive Category 2 recoveries on chunk 2."""
        client = _create_async_client(transport, monkeypatch)
        chunk_size = 262_144
        total_size = 3 * chunk_size
        stream = io.BytesIO(b"E" * total_size)

        scenario_headers = [
            ("X-Goog-Test-Scenario", "non_fatal_error_on_chunk_upload"),
            (
                "X-Goog-Test-Scenario-Config",
                '{"error_code":412,"failure_count":2,"after_offset":262144}',
            ),
        ]
        upload_session = await client.upload_media(
            request=UploadMediaRequest(name="async_cat2_two_on_chunk_2.bin"),
            config=ResumableUploadConfig(
                chunk_size=chunk_size, headers=scenario_headers
            ),
        )
        progress_records = [
            p
            async for p in upload_session.upload(
                stream, size=total_size, retry=FAST_ASYNC_STREAMING_RETRY
            )
        ]

        assert isinstance(upload_session.response, UploadMediaResponse)
        assert upload_session.response.size == total_size
        assert [p.state for p in progress_records] == [
            ProgressState.STARTED,
            ProgressState.UPLOADING,
            ProgressState.RECOVERING,
            ProgressState.OFFSET_RECEIVED,
            ProgressState.RECOVERING,
            ProgressState.OFFSET_RECEIVED,
            ProgressState.UPLOADING,
            ProgressState.FINALIZED,
        ]
        assert [p.bytes_uploaded for p in progress_records] == [
            0,
            262_144,
            262_144,
            262_144,
            262_144,
            262_144,
            524_288,
            786_432,
        ]

    @pytest.mark.asyncio
    @pytest.mark.parametrize("transport", ["grpc_asyncio", "rest_asyncio"])
    async def test_async_cat2_failure_on_finalizing_chunk(
        transport, monkeypatch
    ):
        """Async Error Recovery Suite Case 4: Category 2 failure on the finalizing chunk."""
        client = _create_async_client(transport, monkeypatch)
        chunk_size = 262_144
        total_size = 3 * chunk_size - 100
        stream = io.BytesIO(b"F" * total_size)

        scenario_headers = [
            ("X-Goog-Test-Scenario", "non_fatal_error_on_chunk_upload"),
            (
                "X-Goog-Test-Scenario-Config",
                '{"error_code":412,"failure_count":1,"after_offset":524288}',
            ),
        ]
        upload_session = await client.upload_media(
            request=UploadMediaRequest(name="async_cat2_finalizing_chunk.bin"),
            config=ResumableUploadConfig(
                chunk_size=chunk_size, headers=scenario_headers
            ),
        )
        progress_records = [
            p
            async for p in upload_session.upload(
                stream, size=total_size, retry=FAST_ASYNC_STREAMING_RETRY
            )
        ]

        assert isinstance(upload_session.response, UploadMediaResponse)
        assert upload_session.response.size == total_size
        assert [p.state for p in progress_records] == [
            ProgressState.STARTED,
            ProgressState.UPLOADING,
            ProgressState.UPLOADING,
            ProgressState.RECOVERING,
            ProgressState.OFFSET_RECEIVED,
            ProgressState.FINALIZED,
        ]
        assert [p.bytes_uploaded for p in progress_records] == [
            0,
            262_144,
            524_288,
            524_288,
            524_288,
            786_332,
        ]

    @pytest.mark.asyncio
    @pytest.mark.parametrize("transport", ["grpc_asyncio", "rest_asyncio"])
    async def test_async_no_headers_failure_recovers_until_deadline_exceeded(
        transport, monkeypatch
    ):
        """Async Error Recovery Suite Case 5: Repeated no-header failures until global deadline exceeded."""
        client = _create_async_client(transport, monkeypatch)
        chunk_size = 262_144
        stream = io.BytesIO(b"T" * chunk_size)

        scenario_headers = [
            ("X-Goog-Test-Scenario", "non_fatal_error_on_chunk_upload"),
            (
                "X-Goog-Test-Scenario-Config",
                '{"failure_count":0,"action_after_failures":"terminate"}',
            ),
        ]
        deadline = datetime.datetime.now(
            datetime.timezone.utc
        ) + datetime.timedelta(seconds=1.0)
        upload_session = await client.upload_media(
            request=UploadMediaRequest(
                name="async_terminate_until_deadline.bin"
            ),
            config=ResumableUploadConfig(
                chunk_size=chunk_size,
                deadline=deadline,
                headers=scenario_headers,
            ),
        )

        progress_records: List[UploadProgress] = []
        with pytest.raises(
            (core_exceptions.DeadlineExceeded, core_exceptions.RetryError)
        ):
            async for progress in upload_session.upload(
                stream, size=chunk_size, retry=FAST_ASYNC_STREAMING_RETRY
            ):
                progress_records.append(progress)

        recovering_count = sum(
            1 for p in progress_records if p.state == ProgressState.RECOVERING
        )
        assert recovering_count >= 1

    @pytest.mark.asyncio
    @pytest.mark.parametrize("transport", ["grpc_asyncio", "rest_asyncio"])
    async def test_async_non_fatal_error_on_start_503(transport, monkeypatch):
        """Async Error on Start Suite Case 1: Single 503 on start with fast retry."""
        client = _create_async_client(transport, monkeypatch)
        stream = io.BytesIO(b"s" * 100)

        scenario_headers = [
            ("X-Goog-Test-Scenario", "non_fatal_error_on_start"),
            (
                "X-Goog-Test-Scenario-Config",
                json.dumps(
                    {
                        "client_uuid": str(uuid.uuid4()),
                        "error_code": 503,
                        "failure_count": 1,
                    }
                ),
            ),
        ]
        upload_session = await client.upload_media(
            request=UploadMediaRequest(name="async_start_503.bin"),
            config=ResumableUploadConfig(headers=scenario_headers),
            retry=FAST_ASYNC_RETRY,
        )
        progress_records = [
            p async for p in upload_session.upload(stream, size=100)
        ]

        assert isinstance(upload_session.response, UploadMediaResponse)
        assert upload_session.response.size == 100
        phases = [p.state for p in progress_records]
        assert phases.count(ProgressState.STARTED) == 1
        assert phases[-1] == ProgressState.FINALIZED

    @pytest.mark.asyncio
    @pytest.mark.parametrize("transport", ["grpc_asyncio", "rest_asyncio"])
    async def test_async_upload_rejection_400_on_start(transport, monkeypatch):
        """Async Error on Start Suite Case 2: Protocol-level 400 Bad Request rejection on start."""
        client = _create_async_client(transport, monkeypatch)
        stream = io.BytesIO(b"r" * 100)

        scenario_headers = [
            ("X-Goog-Test-Scenario", "non_fatal_error_on_start"),
            (
                "X-Goog-Test-Scenario-Config",
                json.dumps(
                    {
                        "client_uuid": str(uuid.uuid4()),
                        "error_code": 400,
                        "failure_count": 1,
                    }
                ),
            ),
        ]
        upload_session = await client.upload_media(
            request=UploadMediaRequest(name="async_reject_400.bin"),
            config=ResumableUploadConfig(headers=scenario_headers),
        )
        with pytest.raises(core_exceptions.BadRequest) as exc_info:
            await upload_session.upload(stream, size=100)

        assert exc_info.value.code == 400

    @pytest.mark.asyncio
    @pytest.mark.parametrize("transport", ["grpc_asyncio", "rest_asyncio"])
    async def test_async_retry_exhaustion_on_start_times_out(
        transport, monkeypatch
    ):
        """Async Error on Start Suite Case 3: Repeated 503 on start until session deadline expires."""
        client = _create_async_client(transport, monkeypatch)
        stream = io.BytesIO(b"t" * 100)

        scenario_headers = [
            ("X-Goog-Test-Scenario", "non_fatal_error_on_start"),
            (
                "X-Goog-Test-Scenario-Config",
                json.dumps(
                    {
                        "client_uuid": str(uuid.uuid4()),
                        "error_code": 503,
                        "failure_count": 10_000,
                    }
                ),
            ),
        ]
        deadline = datetime.datetime.now(
            datetime.timezone.utc
        ) + datetime.timedelta(seconds=2.0)
        upload_session = await client.upload_media(
            request=UploadMediaRequest(name="async_start_exhaustion.bin"),
            config=ResumableUploadConfig(
                headers=scenario_headers, deadline=deadline
            ),
            retry=retries.AsyncRetry(
                initial=0.2, maximum=0.5, multiplier=1.5, timeout=2.0
            ),
        )

        progress_records: List[UploadProgress] = []
        t_start = time.monotonic()
        with pytest.raises(
            (core_exceptions.GoogleAPICallError, core_exceptions.RetryError)
        ):
            async for progress in upload_session.upload(stream, size=100):
                progress_records.append(progress)
        elapsed = time.monotonic() - t_start

        assert elapsed >= 1.5
        phases = [p.state for p in progress_records]
        assert ProgressState.UPLOADING not in phases

    @pytest.mark.asyncio
    @pytest.mark.parametrize("transport", ["grpc_asyncio", "rest_asyncio"])
    @pytest.mark.parametrize(
        "status_code,expected_exc",
        [
            (403, core_exceptions.Forbidden),
            (404, core_exceptions.NotFound),
        ],
    )
    async def test_async_fatal_error_on_start_raises_immediately(
        transport, status_code, expected_exc, monkeypatch
    ):
        """Async Error on Start Suite Case 4: Fatal 403 and 404 on start fail immediately."""
        client = _create_async_client(transport, monkeypatch)
        stream = io.BytesIO(b"f" * 100)

        scenario_headers = [
            ("X-Goog-Test-Scenario", "fatal_error_on_start"),
            (
                "X-Goog-Test-Scenario-Config",
                json.dumps({"error_code": status_code}),
            ),
        ]
        upload_session = await client.upload_media(
            request=UploadMediaRequest(name="async_fatal_start.bin"),
            config=ResumableUploadConfig(headers=scenario_headers),
        )

        progress_records: List[UploadProgress] = []
        t_start = time.monotonic()
        with pytest.raises(expected_exc) as exc_info:
            async for progress in upload_session.upload(stream, size=100):
                progress_records.append(progress)
        elapsed = time.monotonic() - t_start

        assert exc_info.value.code == status_code
        assert elapsed < 0.5
        phases = [p.state for p in progress_records]
        assert ProgressState.UPLOADING not in phases

    @pytest.mark.asyncio
    @pytest.mark.parametrize("transport", ["grpc_asyncio", "rest_asyncio"])
    async def test_async_sequential_runs_session_isolation(
        transport, monkeypatch
    ):
        """Async Error on Start Suite Case 5: Sequential runs with distinct client_uuid values."""
        client = _create_async_client(transport, monkeypatch)
        payload = b"i" * 100

        for run_idx in range(2):
            scenario_headers = [
                ("X-Goog-Test-Scenario", "non_fatal_error_on_start"),
                (
                    "X-Goog-Test-Scenario-Config",
                    json.dumps(
                        {
                            "client_uuid": str(uuid.uuid4()),
                            "error_code": 503,
                            "failure_count": 1,
                        }
                    ),
                ),
            ]
            upload_session = await client.upload_media(
                request=UploadMediaRequest(
                    name=f"async_isolated_run_{run_idx}.bin"
                ),
                config=ResumableUploadConfig(headers=scenario_headers),
                retry=FAST_ASYNC_RETRY,
            )
            resp = await upload_session.upload(io.BytesIO(payload), size=100)
            assert isinstance(resp, UploadMediaResponse)
            assert resp.name == f"async_isolated_run_{run_idx}.bin"
            assert resp.size == 100
