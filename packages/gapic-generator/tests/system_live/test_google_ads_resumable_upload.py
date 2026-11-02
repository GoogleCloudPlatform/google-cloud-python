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

"""Live Google Ads acceptance tests for GAPIC Resumable Upload client libraries.

Exercises `YouTubeVideoUploadServiceClient` and
`YouTubeVideoUploadServiceAsyncClient` (with `grpc`/`grpc_asyncio` and
`rest`/`rest_asyncio` transports) against `https://googleads.googleapis.com`
using two-tier service account impersonation.

To run the live Google Ads acceptance suite:
    GOOGLE_ADS_DEVELOPER_TOKEN="<developer-token>" \\
    GOOGLE_ADS_LOGIN_CUSTOMER_ID="<login-customer-id>" \\
    GOOGLE_ADS_CUSTOMER_ID="<customer-id>" \\
    GOOGLE_ADS_TARGET_SERVICE_ACCOUNT="<target-sa>@<project>.iam.gserviceaccount.com" \\
    GOOGLE_ADS_SOURCE_SERVICE_ACCOUNT="<source-sa>@<project>.iam.gserviceaccount.com" \\
    GOOGLE_ADS_VIDEO_PATH="~/Downloads/video.mp4" \\
    nox -s system-3.14
"""

from datetime import datetime, timedelta, timezone
import io
import os
from pathlib import Path
import re
from typing import List, Optional, Sequence, Tuple

import pytest
import requests

import google.auth
from google.auth import credentials as ga_credentials
from google.auth import impersonated_credentials
import google.auth.transport.requests
from google.oauth2 import service_account
from google.api_core import exceptions as core_exceptions
from google.api_core.resumable_transfer import (
    ProgressState,
    ResumableUploadConfig,
    UploadProgress,
)


class _ClientPauseError(Exception):
    """Client-side exception raised inside progress loop to simulate user pause."""

    def __init__(self, message: str, upload_url: str, chunk_size: int) -> None:
        """Initialize the pause exception with resumable session state.

        Args:
            message: Human-readable reason for pausing the upload.
            upload_url: Resumable session URI used to resume the upload.
            chunk_size: Active chunk size in bytes for the upload session.
        """
        super().__init__(message)
        self.upload_url = upload_url
        self.chunk_size = chunk_size


# =============================================================================
# Live Google Ads (YouTubeVideoUploadService) Acceptance Tests
# =============================================================================


ADWORDS_SCOPE = "https://www.googleapis.com/auth/adwords"
SOURCE_SCOPES = (
    "https://www.googleapis.com/auth/iam",
    "https://www.googleapis.com/auth/cloud-platform",
)
VIDEO_TITLE_PREFIX = "gapic-generator-resumable-upload-"
VIDEO_TITLE_TIMESTAMP_FMT = "%Y%m%dT%H%M%SZ"
STALE_UPLOAD_MAX_AGE = timedelta(hours=2)

from google.ads.googleads_v23.services.services.you_tube_video_upload_service import (
    YouTubeVideoUploadServiceAsyncClient,
    YouTubeVideoUploadServiceClient,
)


def _generate_video_title() -> str:
    """Generate a test video title tagged with the suite prefix and UTC timestamp.

    Returns:
        Formatted video title string containing `VIDEO_TITLE_PREFIX` and the
        current UTC timestamp (`%Y%m%dT%H%M%SZ`).
    """
    ts = datetime.now(timezone.utc).strftime(VIDEO_TITLE_TIMESTAMP_FMT)
    return f"{VIDEO_TITLE_PREFIX}{ts}"


def _parse_video_title_timestamp(title: str) -> Optional[datetime]:
    """Extract the UTC creation timestamp from a prefixed test video title.

    Args:
        title: Video title string retrieved from YouTube metadata.

    Returns:
        Timezone-aware UTC `datetime` if `title` starts with
        `VIDEO_TITLE_PREFIX` and ends with a valid timestamp, otherwise `None`.
    """
    if not title.startswith(VIDEO_TITLE_PREFIX):
        return None
    raw_ts = title[len(VIDEO_TITLE_PREFIX) :]
    try:
        return datetime.strptime(raw_ts, VIDEO_TITLE_TIMESTAMP_FMT).replace(
            tzinfo=timezone.utc
        )
    except ValueError:
        return None


def _fetch_youtube_video_title(video_id: str) -> Optional[str]:
    """Resolve the title of an uploaded YouTube video via the public oEmbed endpoint.

    Args:
        video_id: 11-character YouTube video identifier (`you_tube_video_upload.video_id`).

    Returns:
        Video title string if the oEmbed lookup succeeds with HTTP 200,
        otherwise `None`.
    """
    resp = requests.get(
        "https://www.youtube.com/oembed",
        params={
            "url": f"https://www.youtube.com/watch?v={video_id}",
            "format": "json",
        },
        timeout=10,
    )
    if resp.status_code != 200:
        return None
    return resp.json().get("title")


def _load_source_credentials() -> ga_credentials.Credentials:
    """Load default source credentials scoped for IAM impersonation and Cloud Platform.

    Returns:
        Google Auth credentials object loaded via Application Default Credentials.
    """
    creds, _ = google.auth.default(scopes=list(SOURCE_SCOPES))
    return creds


def _load_impersonated_credentials() -> impersonated_credentials.Credentials:
    """Construct impersonated Google Ads credentials for the target service account.

    Returns:
        Impersonated credentials configured for `ADWORDS_SCOPE` targeting
        `GOOGLE_ADS_TARGET_SERVICE_ACCOUNT`.
    """
    target_principal = os.environ.get("GOOGLE_ADS_TARGET_SERVICE_ACCOUNT", "")
    if not target_principal:
        pytest.fail("GOOGLE_ADS_TARGET_SERVICE_ACCOUNT is not set.")
    source_creds = _load_source_credentials()
    return impersonated_credentials.Credentials(
        source_credentials=source_creds,
        target_principal=target_principal,
        target_scopes=[ADWORDS_SCOPE],
        lifetime=3600,
    )


def _google_ads_metadata() -> Sequence[Tuple[str, str]]:
    """Build gRPC/REST request metadata headers for Google Ads API calls.

    Returns:
        Sequence of `(header_name, header_value)` pairs containing
        `developer-token` and `login-customer-id`.
    """
    developer_token = os.environ.get("GOOGLE_ADS_DEVELOPER_TOKEN", "")
    login_customer_id = os.environ.get("GOOGLE_ADS_LOGIN_CUSTOMER_ID", "")
    if not developer_token or not login_customer_id:
        pytest.fail(
            "GOOGLE_ADS_DEVELOPER_TOKEN and GOOGLE_ADS_LOGIN_CUSTOMER_ID are required."
        )
    return (
        ("developer-token", developer_token),
        ("login-customer-id", login_customer_id),
    )


def _google_ads_customer_id() -> str:
    """Read the target Google Ads customer ID from environment configuration.

    Returns:
        Customer ID string read from `GOOGLE_ADS_CUSTOMER_ID` (falling back to
        `GOOGLE_ADS_LOGIN_CUSTOMER_ID`).
    """
    customer_id = os.environ.get(
        "GOOGLE_ADS_CUSTOMER_ID",
        os.environ.get("GOOGLE_ADS_LOGIN_CUSTOMER_ID", ""),
    )
    if not customer_id:
        pytest.fail("GOOGLE_ADS_CUSTOMER_ID is required.")
    return customer_id


def _open_upload_file() -> Tuple[io.BufferedReader, int]:
    """Open the sample video payload file in binary mode and inspect its size.

    Returns:
        Tuple of `(stream, upload_size)` where `stream` is an open binary file
        reader and `upload_size` is the file size in bytes.
    """
    raw_path = os.environ.get("GOOGLE_ADS_VIDEO_PATH", "~/Downloads/video.mp4")
    expanded = Path(os.path.expanduser(raw_path)).resolve()
    if not expanded.is_file():
        pytest.fail(f"Test media file not found at {expanded}")
    f = open(expanded, "rb")
    return f, expanded.stat().st_size


def _try_remove_upload(
    client: YouTubeVideoUploadServiceClient,
    customer_id: str,
    resource_name: str,
    metadata: Sequence[Tuple[str, str]],
) -> None:
    """Attempt best-effort removal of a newly uploaded YouTube video resource.

    Immediately after upload completion (`ProgressState.FINALIZED`), the video
    remains in `UPLOADED` state while YouTube processes the media stream, during
    which `RemoveYouTubeVideoUpload` returns `INVALID_ARGUMENT` (`NOT_FOUND`).
    Any upload still processing at teardown is removed by `_cleanup_stale_test_videos`
    once processed and older than `STALE_UPLOAD_MAX_AGE`.

    Args:
        client: Synchronous `YouTubeVideoUploadServiceClient` instance.
        customer_id: Google Ads customer ID owning the upload resource.
        resource_name: Resource name (`customers/{id}/youTubeVideoUploads/{id}`).
        metadata: Request metadata headers (`developer-token`, `login-customer-id`).
    """
    try:
        client.remove_you_tube_video_upload(
            request={
                "customer_id": customer_id,
                "resource_names": [resource_name],
            },
            metadata=metadata,
        )
    except core_exceptions.GoogleAPICallError:
        pass


async def _async_try_remove_upload(
    client: YouTubeVideoUploadServiceAsyncClient,
    customer_id: str,
    resource_name: str,
    metadata: Sequence[Tuple[str, str]],
) -> None:
    """Attempt best-effort async removal of a newly uploaded YouTube video resource.

    Args:
        client: Asynchronous `YouTubeVideoUploadServiceAsyncClient` instance.
        customer_id: Google Ads customer ID owning the upload resource.
        resource_name: Resource name (`customers/{id}/youTubeVideoUploads/{id}`).
        metadata: Request metadata headers (`developer-token`, `login-customer-id`).
    """
    try:
        await client.remove_you_tube_video_upload(
            request={
                "customer_id": customer_id,
                "resource_names": [resource_name],
            },
            metadata=metadata,
        )
    except core_exceptions.GoogleAPICallError:
        pass


@pytest.fixture(scope="session", autouse=True)
def _cleanup_stale_test_videos():
    """Query processed YouTube video uploads and remove test resources older than 2 hours.

    Queries `you_tube_video_upload` resources in `PROCESSED` state via
    `googleAds:search`, inspects video titles via YouTube oEmbed to identify
    test resources created with `VIDEO_TITLE_PREFIX`, and removes any resource
    whose embedded timestamp exceeds `STALE_UPLOAD_MAX_AGE`.
    """
    creds = _load_impersonated_credentials()
    customer_id = _google_ads_customer_id()
    metadata = _google_ads_metadata()
    developer_token = dict(metadata)["developer-token"]
    login_customer_id = dict(metadata)["login-customer-id"]

    creds.refresh(google.auth.transport.requests.Request())
    headers = {
        "Authorization": f"Bearer {creds.token}",
        "developer-token": developer_token,
        "login-customer-id": login_customer_id,
    }
    search_url = (
        f"https://googleads.googleapis.com/v23/customers/{customer_id}/googleAds:search"
    )
    resp = requests.post(
        search_url,
        headers=headers,
        json={
            "query": (
                "SELECT you_tube_video_upload.resource_name, "
                "you_tube_video_upload.video_id "
                "FROM you_tube_video_upload "
                "WHERE you_tube_video_upload.state = 'PROCESSED'"
            )
        },
        timeout=30,
    )
    if resp.status_code != 200:
        return

    now = datetime.now(timezone.utc)
    stale_resource_names: List[str] = []
    for row in resp.json().get("results", []):
        upload = row.get("youTubeVideoUpload", {})
        video_id = upload.get("videoId")
        resource_name = upload.get("resourceName")
        if not video_id or not resource_name:
            continue
        title = _fetch_youtube_video_title(video_id)
        if not title:
            continue
        created_at = _parse_video_title_timestamp(title)
        if created_at is not None and (now - created_at) > STALE_UPLOAD_MAX_AGE:
            stale_resource_names.append(resource_name)

    if stale_resource_names:
        client = YouTubeVideoUploadServiceClient(credentials=creds)
        for resource_name in stale_resource_names:
            _try_remove_upload(client, customer_id, resource_name, metadata)


class TestGoogleAdsLiveAcceptance:
    """Live acceptance tests against Google Ads YouTubeVideoUploadService."""

    @pytest.fixture(autouse=True)
    def _disable_mtls(self, monkeypatch):
        """Disable mTLS client certificates for test execution.

        Args:
            monkeypatch: Pytest `MonkeyPatch` fixture for setting environment variables.
        """
        monkeypatch.setenv("GOOGLE_API_USE_CLIENT_CERTIFICATE", "false")

    def test_adc_source_credentials_are_service_account(self):
        """Verify ADC source credentials load as a service account matching configuration."""
        creds = _load_source_credentials()
        assert isinstance(creds, service_account.Credentials)
        expected_source_sa = os.environ.get("GOOGLE_ADS_SOURCE_SERVICE_ACCOUNT")
        if expected_source_sa:
            assert creds.service_account_email == expected_source_sa

    def test_impersonated_credentials_fetch_access_token(self):
        """Verify target service account impersonation mints a valid bearer access token."""
        creds = _load_impersonated_credentials()
        creds.refresh(google.auth.transport.requests.Request())
        headers = {}
        creds.apply(headers)

        assert creds.token is not None
        assert len(creds.token) > 0
        auth_header = headers.get("authorization") or headers.get("Authorization")
        assert auth_header is not None
        assert auth_header.startswith("Bearer ")
        assert creds.expiry is not None
        now_utc = datetime.now(timezone.utc).replace(tzinfo=None)
        assert creds.expiry > now_utc

    @pytest.mark.parametrize("transport", ["grpc", "rest"])
    def test_upload_with_impersonated_credentials(self, transport: str):
        """Verify complete synchronous resumable video upload and resource cleanup.

        Args:
            transport: Client transport name (`"grpc"` or `"rest"`).
        """
        client = YouTubeVideoUploadServiceClient(
            credentials=_load_impersonated_credentials(),
            transport=transport,
        )
        customer_id = _google_ads_customer_id()
        metadata = _google_ads_metadata()
        stream, upload_size = _open_upload_file()
        response = None
        try:
            upload_session = client.create_you_tube_video_upload(
                request={
                    "customer_id": customer_id,
                    "you_tube_video_upload": {
                        "video_title": _generate_video_title(),
                        "video_description": "Testing defaults",
                        "video_privacy": "UNLISTED",
                    },
                },
                metadata=metadata,
            )
            progress_records: List[UploadProgress] = []
            for progress in upload_session.iter_upload(
                stream, size=upload_size, content_type="video/mp4"
            ):
                progress_records.append(progress)

            response = upload_session.response
            assert response is not None
            assert re.match(
                r"^customers/\d+/youTubeVideoUploads/\d+$",
                response.resource_name,
            )
            assert len(progress_records) >= 2
            assert progress_records[0].state == ProgressState.STARTED
            assert progress_records[-1].state == ProgressState.FINALIZED
            assert progress_records[-1].bytes_uploaded == upload_size
        finally:
            stream.close()
            if response is not None and response.resource_name:
                _try_remove_upload(
                    client, customer_id, response.resource_name, metadata
                )

    @pytest.mark.parametrize("transport", ["grpc", "rest"])
    def test_golden_user_style_resume_seekable(self, transport: str):
        """Verify synchronous mid-stream interruption, session resumption, and cleanup.

        Args:
            transport: Client transport name (`"grpc"` or `"rest"`).
        """
        client = YouTubeVideoUploadServiceClient(
            credentials=_load_impersonated_credentials(),
            transport=transport,
        )
        customer_id = _google_ads_customer_id()
        metadata = _google_ads_metadata()
        stream, upload_size = _open_upload_file()
        chunk_size = 512 * 1024  # 512 KiB
        request_payload = {
            "customer_id": customer_id,
            "you_tube_video_upload": {
                "video_title": _generate_video_title(),
                "video_description": "Testing defaults",
                "video_privacy": "UNLISTED",
            },
        }
        response = None
        try:
            session1 = client.create_you_tube_video_upload(
                request=request_payload,
                config=ResumableUploadConfig(chunk_size=chunk_size),
                metadata=metadata,
            )
            with pytest.raises(_ClientPauseError) as exc_info:
                for progress in session1.iter_upload(
                    stream, size=upload_size, content_type="video/mp4"
                ):
                    if (
                        progress.state == ProgressState.UPLOADING
                        and progress.bytes_uploaded >= chunk_size
                    ):
                        raise _ClientPauseError(
                            "User paused upload",
                            upload_url=progress.upload_url,
                            chunk_size=session1.chunk_size,
                        )

            saved_url = exc_info.value.upload_url
            saved_chunk_size = exc_info.value.chunk_size
            assert saved_url
            assert saved_chunk_size >= chunk_size
            assert session1.bytes_uploaded >= chunk_size

            stream.seek(0)
            session2 = client.create_you_tube_video_upload(
                request=request_payload,
                metadata=metadata,
            )
            progress_records_2: List[UploadProgress] = []
            for progress in session2.iter_resume(
                saved_url,
                stream,
                size=upload_size,
                chunk_size=saved_chunk_size,
            ):
                progress_records_2.append(progress)

            response = session2.response
            assert response is not None
            assert re.match(
                r"^customers/\d+/youTubeVideoUploads/\d+$",
                response.resource_name,
            )
            assert len(progress_records_2) >= 2
            assert progress_records_2[0].state == ProgressState.OFFSET_RECEIVED
            assert progress_records_2[0].bytes_uploaded >= chunk_size
            assert progress_records_2[-1].state == ProgressState.FINALIZED
            assert progress_records_2[-1].bytes_uploaded == upload_size
        finally:
            stream.close()
            if response is not None and response.resource_name:
                _try_remove_upload(
                    client, customer_id, response.resource_name, metadata
                )

    if os.environ.get("GAPIC_PYTHON_ASYNC", "true") == "true":

        @pytest.mark.asyncio
        @pytest.mark.parametrize("transport", ["grpc_asyncio", "rest_asyncio"])
        async def test_async_upload_with_impersonated_credentials(
            self, transport: str
        ):
            """Verify complete asynchronous resumable video upload and resource cleanup.

            Args:
                transport: Async client transport name (`"grpc_asyncio"` or `"rest_asyncio"`).
            """
            if (
                transport == "rest_asyncio"
                and "rest_asyncio"
                not in YouTubeVideoUploadServiceClient._transport_registry
            ):
                pytest.fail(
                    "rest_asyncio transport is not registered when rest_async_io_enabled is False."
                )
            client = YouTubeVideoUploadServiceAsyncClient(
                credentials=_load_impersonated_credentials(),
                transport=transport,
            )
            customer_id = _google_ads_customer_id()
            metadata = _google_ads_metadata()
            stream, upload_size = _open_upload_file()
            response = None
            try:
                upload_session = await client.create_you_tube_video_upload(
                    request={
                        "customer_id": customer_id,
                        "you_tube_video_upload": {
                            "video_title": _generate_video_title(),
                            "video_description": "Testing defaults",
                            "video_privacy": "UNLISTED",
                        },
                    },
                    metadata=metadata,
                )
                progress_records: List[UploadProgress] = []
                async for progress in upload_session.upload(
                    stream, size=upload_size, content_type="video/mp4"
                ):
                    progress_records.append(progress)

                response = upload_session.response
                assert response is not None
                assert re.match(
                    r"^customers/\d+/youTubeVideoUploads/\d+$",
                    response.resource_name,
                )
                assert len(progress_records) >= 2
                assert progress_records[0].state == ProgressState.STARTED
                assert progress_records[-1].state == ProgressState.FINALIZED
                assert progress_records[-1].bytes_uploaded == upload_size
            finally:
                stream.close()
                if response is not None and response.resource_name:
                    await _async_try_remove_upload(
                        client, customer_id, response.resource_name, metadata
                    )

        @pytest.mark.asyncio
        @pytest.mark.parametrize("transport", ["grpc_asyncio", "rest_asyncio"])
        async def test_async_golden_user_style_resume_seekable(self, transport: str):
            """Verify asynchronous mid-stream interruption, session resumption, and cleanup.

            Args:
                transport: Async client transport name (`"grpc_asyncio"` or `"rest_asyncio"`).
            """
            if (
                transport == "rest_asyncio"
                and "rest_asyncio"
                not in YouTubeVideoUploadServiceClient._transport_registry
            ):
                pytest.fail(
                    "rest_asyncio transport is not registered when rest_async_io_enabled is False."
                )
            client = YouTubeVideoUploadServiceAsyncClient(
                credentials=_load_impersonated_credentials(),
                transport=transport,
            )
            customer_id = _google_ads_customer_id()
            metadata = _google_ads_metadata()
            stream, upload_size = _open_upload_file()
            chunk_size = 512 * 1024  # 512 KiB
            request_payload = {
                "customer_id": customer_id,
                "you_tube_video_upload": {
                    "video_title": _generate_video_title(),
                    "video_description": "Testing defaults",
                    "video_privacy": "UNLISTED",
                },
            }
            response = None
            try:
                session1 = await client.create_you_tube_video_upload(
                    request=request_payload,
                    config=ResumableUploadConfig(chunk_size=chunk_size),
                    metadata=metadata,
                )
                with pytest.raises(_ClientPauseError) as exc_info:
                    async for progress in session1.upload(
                        stream, size=upload_size, content_type="video/mp4"
                    ):
                        if (
                            progress.state == ProgressState.UPLOADING
                            and progress.bytes_uploaded >= chunk_size
                        ):
                            raise _ClientPauseError(
                                "User paused upload",
                                upload_url=progress.upload_url,
                                chunk_size=session1.chunk_size,
                            )

                saved_url = exc_info.value.upload_url
                saved_chunk_size = exc_info.value.chunk_size
                assert saved_url
                assert saved_chunk_size >= chunk_size
                assert session1.bytes_uploaded >= chunk_size

                stream.seek(0)
                session2 = await client.create_you_tube_video_upload(
                    request=request_payload,
                    metadata=metadata,
                )
                progress_records_2: List[UploadProgress] = []
                async for progress in session2.resume(
                    saved_url,
                    stream,
                    size=upload_size,
                    chunk_size=saved_chunk_size,
                ):
                    progress_records_2.append(progress)

                response = session2.response
                assert response is not None
                assert re.match(
                    r"^customers/\d+/youTubeVideoUploads/\d+$",
                    response.resource_name,
                )
                assert len(progress_records_2) >= 2
                assert progress_records_2[0].state == ProgressState.OFFSET_RECEIVED
                assert progress_records_2[0].bytes_uploaded >= chunk_size
                assert progress_records_2[-1].state == ProgressState.FINALIZED
                assert progress_records_2[-1].bytes_uploaded == upload_size
            finally:
                stream.close()
                if response is not None and response.resource_name:
                    await _async_try_remove_upload(
                        client, customer_id, response.resource_name, metadata
                    )
