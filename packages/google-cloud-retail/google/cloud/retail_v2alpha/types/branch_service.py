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
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import proto  # type: ignore

from google.cloud.retail_v2alpha.types import branch

__protobuf__ = proto.module(
    package="google.cloud.retail.v2alpha",
    manifest={
        "ListBranchesRequest",
        "ListBranchesResponse",
        "GetBranchRequest",
    },
)


class ListBranchesRequest(proto.Message):
    r"""Request for
    [BranchService.ListBranches][google.cloud.retail.v2alpha.BranchService.ListBranches]
    method.

    Attributes:
        parent (str):
            Required. The parent catalog resource name.
        view (google.cloud.retail_v2alpha.types.BranchView):
            The view to apply to the returned
            [Branch][google.cloud.retail.v2alpha.Branch]. Defaults to
            [Branch.BranchView.BASIC] if unspecified. See documentation
            of fields of [Branch][google.cloud.retail.v2alpha.Branch] to
            find what fields are excluded from BASIC view.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: branch.BranchView = proto.Field(
        proto.ENUM,
        number=2,
        enum=branch.BranchView,
    )


class ListBranchesResponse(proto.Message):
    r"""Response for
    [BranchService.ListBranches][google.cloud.retail.v2alpha.BranchService.ListBranches]
    method.

    Attributes:
        branches (MutableSequence[google.cloud.retail_v2alpha.types.Branch]):
            The Branches.
    """

    branches: MutableSequence[branch.Branch] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=branch.Branch,
    )


class GetBranchRequest(proto.Message):
    r"""Request for
    [BranchService.GetBranch][google.cloud.retail.v2alpha.BranchService.GetBranch]
    method.

    Attributes:
        name (str):
            Required. The name of the branch to retrieve. Format:
            ``projects/*/locations/global/catalogs/default_catalog/branches/some_branch_id``.

            "default_branch" can be used as a special branch_id, it
            returns the default branch that has been set for the
            catalog.
        view (google.cloud.retail_v2alpha.types.BranchView):
            The view to apply to the returned
            [Branch][google.cloud.retail.v2alpha.Branch]. Defaults to
            [Branch.BranchView.BASIC] if unspecified. See documentation
            of fields of [Branch][google.cloud.retail.v2alpha.Branch] to
            find what fields are excluded from BASIC view.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: branch.BranchView = proto.Field(
        proto.ENUM,
        number=2,
        enum=branch.BranchView,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
