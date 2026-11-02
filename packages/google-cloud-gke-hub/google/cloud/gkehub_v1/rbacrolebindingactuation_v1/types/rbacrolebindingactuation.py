# -*- coding: utf-8 -*-
# Copyright 2025 Google LLC
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

__protobuf__ = proto.module(
    package="google.cloud.gkehub.rbacrolebindingactuation.v1",
    manifest={
        "FeatureSpec",
        "FeatureState",
    },
)


class FeatureSpec(proto.Message):
    r"""**RBAC RoleBinding Actuation**: The Hub-wide input for the
    RBACRoleBindingActuation feature.

    Attributes:
        allowed_custom_roles (MutableSequence[str]):
            The list of allowed custom roles
            (ClusterRoles). If a ClusterRole is not part of
            this list, it cannot be used in a Scope
            RBACRoleBinding. If a ClusterRole in this list
            is in use, it cannot be removed from the list.
    """

    allowed_custom_roles: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class FeatureState(proto.Message):
    r"""**RBAC RoleBinding Actuation**: An empty state left as an example
    Hub-wide Feature state.

    """


__all__ = tuple(sorted(__protobuf__.manifest))
