# Copyright 2015 Google LLC
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

"""Mocks used to emulate gRPC generated objects."""

import mock


class _FakeStub(object):
    """Acts as a gPRC stub."""

    def __init__(self, *results):
        self.results = results
        self.method_calls = []


def _make_credentials():
    import google.auth.credentials

    from google.cloud.bigtable_v2 import BigtableClient

    class _CredentialsWithScopesAndQuotaProject(
        google.auth.credentials.Scoped,
        google.auth.credentials.CredentialsWithQuotaProject,
        google.auth.credentials.Credentials,
    ):
        pass

    credentials = mock.Mock(spec=_CredentialsWithScopesAndQuotaProject)

    # Needed to mock universe domain and quota project for new data client tests
    credentials_with_scopes = mock.Mock(spec=_CredentialsWithScopesAndQuotaProject)
    credentials_with_scopes.universe_domain = BigtableClient._DEFAULT_UNIVERSE
    credentials_with_scopes.with_quota_project.return_value = credentials_with_scopes
    credentials.with_scopes.return_value = credentials_with_scopes

    return credentials
