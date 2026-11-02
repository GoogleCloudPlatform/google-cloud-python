# Copyright 2016 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

import google.auth
from google.auth.exceptions import RefreshError
import google.oauth2.credentials

EXPECT_PROJECT_ID = os.getenv("EXPECT_PROJECT_ID")
CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "")


def test_application_default_credentials(verify_refresh):
    credentials, project_id = google.auth.default()

    if EXPECT_PROJECT_ID is not None:
        assert project_id is not None

    try:
        verify_refresh(credentials)
    except RefreshError as e:
        # allow expired credentials for explicit_authorized_user tests
        # TODO: https://github.com/googleapis/google-auth-library-python/issues/1882
        is_user_credentials = isinstance(
            credentials, google.oauth2.credentials.Credentials
        )
        if not is_user_credentials and not CREDENTIALS.endswith("authorized_user.json"):
            raise

        error_message = str(e)
        if (
            "Token has been expired or revoked" not in error_message
            and "invalid_grant" not in error_message
            and "invalid_client" not in error_message
        ):
            raise
