# -*- coding: utf-8 -*-
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
#
import google.api_core as api_core

from google.cloud.securesourcemanager_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.securesourcemanager_v1.services.secure_source_manager",
    "google.cloud.securesourcemanager_v1.types.secure_source_manager",
}


from .services.secure_source_manager import (
    SecureSourceManagerAsyncClient,
    SecureSourceManagerClient,
)
from .types.secure_source_manager import (
    BatchCreatePullRequestCommentsRequest,
    BatchCreatePullRequestCommentsResponse,
    BranchRule,
    CloseIssueRequest,
    ClosePullRequestRequest,
    CreateBranchRuleRequest,
    CreateHookRequest,
    CreateInstanceRequest,
    CreateIssueCommentRequest,
    CreateIssueRequest,
    CreatePullRequestCommentRequest,
    CreatePullRequestRequest,
    CreateRepositoryRequest,
    DeleteBranchRuleRequest,
    DeleteHookRequest,
    DeleteInstanceRequest,
    DeleteIssueCommentRequest,
    DeleteIssueRequest,
    DeletePullRequestCommentRequest,
    DeleteRepositoryRequest,
    FetchBlobRequest,
    FetchBlobResponse,
    FetchRefsRequest,
    FetchRefsResponse,
    FetchTreeRequest,
    FetchTreeResponse,
    FileDiff,
    GetBranchRuleRequest,
    GetHookRequest,
    GetInstanceRequest,
    GetIssueCommentRequest,
    GetIssueRequest,
    GetPullRequestCommentRequest,
    GetPullRequestRequest,
    GetRepositoryRequest,
    Hook,
    Instance,
    Issue,
    IssueComment,
    ListBranchRulesRequest,
    ListBranchRulesResponse,
    ListHooksRequest,
    ListHooksResponse,
    ListInstancesRequest,
    ListInstancesResponse,
    ListIssueCommentsRequest,
    ListIssueCommentsResponse,
    ListIssuesRequest,
    ListIssuesResponse,
    ListPullRequestCommentsRequest,
    ListPullRequestCommentsResponse,
    ListPullRequestFileDiffsRequest,
    ListPullRequestFileDiffsResponse,
    ListPullRequestsRequest,
    ListPullRequestsResponse,
    ListRepositoriesRequest,
    ListRepositoriesResponse,
    MergePullRequestRequest,
    OpenIssueRequest,
    OpenPullRequestRequest,
    OperationMetadata,
    PullRequest,
    PullRequestComment,
    Ref,
    Repository,
    ResolvePullRequestCommentsRequest,
    ResolvePullRequestCommentsResponse,
    TreeEntry,
    UnresolvePullRequestCommentsRequest,
    UnresolvePullRequestCommentsResponse,
    UpdateBranchRuleRequest,
    UpdateHookRequest,
    UpdateIssueCommentRequest,
    UpdateIssueRequest,
    UpdatePullRequestCommentRequest,
    UpdatePullRequestRequest,
    UpdateRepositoryRequest,
)

__all__ = (
    "SecureSourceManagerAsyncClient",
    "BatchCreatePullRequestCommentsRequest",
    "BatchCreatePullRequestCommentsResponse",
    "BranchRule",
    "CloseIssueRequest",
    "ClosePullRequestRequest",
    "CreateBranchRuleRequest",
    "CreateHookRequest",
    "CreateInstanceRequest",
    "CreateIssueCommentRequest",
    "CreateIssueRequest",
    "CreatePullRequestCommentRequest",
    "CreatePullRequestRequest",
    "CreateRepositoryRequest",
    "DeleteBranchRuleRequest",
    "DeleteHookRequest",
    "DeleteInstanceRequest",
    "DeleteIssueCommentRequest",
    "DeleteIssueRequest",
    "DeletePullRequestCommentRequest",
    "DeleteRepositoryRequest",
    "FetchBlobRequest",
    "FetchBlobResponse",
    "FetchRefsRequest",
    "FetchRefsResponse",
    "FetchTreeRequest",
    "FetchTreeResponse",
    "FileDiff",
    "GetBranchRuleRequest",
    "GetHookRequest",
    "GetInstanceRequest",
    "GetIssueCommentRequest",
    "GetIssueRequest",
    "GetPullRequestCommentRequest",
    "GetPullRequestRequest",
    "GetRepositoryRequest",
    "Hook",
    "Instance",
    "Issue",
    "IssueComment",
    "ListBranchRulesRequest",
    "ListBranchRulesResponse",
    "ListHooksRequest",
    "ListHooksResponse",
    "ListInstancesRequest",
    "ListInstancesResponse",
    "ListIssueCommentsRequest",
    "ListIssueCommentsResponse",
    "ListIssuesRequest",
    "ListIssuesResponse",
    "ListPullRequestCommentsRequest",
    "ListPullRequestCommentsResponse",
    "ListPullRequestFileDiffsRequest",
    "ListPullRequestFileDiffsResponse",
    "ListPullRequestsRequest",
    "ListPullRequestsResponse",
    "ListRepositoriesRequest",
    "ListRepositoriesResponse",
    "MergePullRequestRequest",
    "OpenIssueRequest",
    "OpenPullRequestRequest",
    "OperationMetadata",
    "PullRequest",
    "PullRequestComment",
    "Ref",
    "Repository",
    "ResolvePullRequestCommentsRequest",
    "ResolvePullRequestCommentsResponse",
    "SecureSourceManagerClient",
    "TreeEntry",
    "UnresolvePullRequestCommentsRequest",
    "UnresolvePullRequestCommentsResponse",
    "UpdateBranchRuleRequest",
    "UpdateHookRequest",
    "UpdateIssueCommentRequest",
    "UpdateIssueRequest",
    "UpdatePullRequestCommentRequest",
    "UpdatePullRequestRequest",
    "UpdateRepositoryRequest",
)

api_core.check_python_version("google.cloud.securesourcemanager_v1")
api_core.check_dependency_versions("google.cloud.securesourcemanager_v1")
