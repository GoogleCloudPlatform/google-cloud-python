# Live Google Ads Acceptance Tests (`tests/system_live/`)

This directory contains live acceptance tests ([`test_google_ads_resumable_upload.py`](test_google_ads_resumable_upload.py)) that exercise end-to-end resumable uploads and mid-stream session resumptions against the generated Google Ads `YouTubeVideoUploadService` GAPIC client (`https://googleads.googleapis.com`) across `grpc`, `rest`, `grpc_asyncio`, and `rest_asyncio` transports.

These tests are isolated in `tests/system_live/` (without `tests/system/conftest.py`) so Showcase system test runs (`tests/system/`) never depend on external credentials or live API endpoints.

---

## 1. Configure Credentials and Environment Variables

The acceptance suite uses two-tier service account impersonation (`google.auth.impersonated_credentials.Credentials`):

1. **Source Service Account (`GOOGLE_APPLICATION_CREDENTIALS` / `GOOGLE_ADS_SOURCE_SERVICE_ACCOUNT`)**:
   - Service account JSON key with `roles/iam.serviceAccountTokenCreator` permission on the target service account (and `iamcredentials.googleapis.com` enabled on its project).
2. **Target Service Account (`GOOGLE_ADS_TARGET_SERVICE_ACCOUNT`)**:
   - Service account granted access to the Google Ads Manager / Customer account (`GOOGLE_ADS_LOGIN_CUSTOMER_ID` / `GOOGLE_ADS_CUSTOMER_ID`) with `googleads.googleapis.com` enabled on its project.
3. **Sample Video Payload (`GOOGLE_ADS_VIDEO_PATH`)**:
   - Local `.mp4` file (defaults to `~/Downloads/video.mp4` if unset; should be > 512 KiB to exercise multi-chunk progress and resumption).

Export the required environment variables in the active shell:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/source-service-account-key.json"
export GOOGLE_ADS_SOURCE_SERVICE_ACCOUNT="<source-sa>@<project>.iam.gserviceaccount.com"
export GOOGLE_ADS_TARGET_SERVICE_ACCOUNT="<target-sa>@<project>.iam.gserviceaccount.com"
export GOOGLE_ADS_DEVELOPER_TOKEN="<developer-token>"
export GOOGLE_ADS_LOGIN_CUSTOMER_ID="<login-customer-id>"
export GOOGLE_ADS_CUSTOMER_ID="<customer-id>"
export GOOGLE_ADS_VIDEO_PATH="${HOME}/Downloads/video.mp4"
```

---

## 2. Run the Live Acceptance Tests

From `packages/gapic-generator`, run the [`system`](../../noxfile.py) `nox` session (which sparse-clones `googleapis`, generates and installs the Google Ads GAPIC library via `protoc`, and runs `pytest` against `tests/system_live`):

```bash
cd packages/gapic-generator
nox -s system-3.14
```
