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

__protobuf__ = proto.module(
    package="google.cloud.securitycenter.v2",
    manifest={
        "AttackPath",
    },
)


class AttackPath(proto.Message):
    r"""A path that an attacker could take to reach an exposed
    resource.

    Attributes:
        name (str):
            The attack path name, for example,
            ``organizations/12/simulations/34/valuedResources/56/attackPaths/78``
        path_nodes (MutableSequence[google.cloud.securitycenter_v2.types.AttackPath.AttackPathNode]):
            A list of nodes that exist in this attack
            path.
        edges (MutableSequence[google.cloud.securitycenter_v2.types.AttackPath.AttackPathEdge]):
            A list of the edges between nodes in this
            attack path.
    """

    class AttackPathNode(proto.Message):
        r"""Represents one point that an attacker passes through in this
        attack path.

        Attributes:
            resource (str):
                The name of the resource at this point in the attack path.
                The format of the name follows the Cloud Asset Inventory
                `resource name
                format <https://cloud.google.com/asset-inventory/docs/resource-name-format>`__
            resource_type (str):
                The `supported resource
                type <https://cloud.google.com/asset-inventory/docs/supported-asset-types>`__
            display_name (str):
                Human-readable name of this resource.
            associated_findings (MutableSequence[google.cloud.securitycenter_v2.types.AttackPath.AttackPathNode.PathNodeAssociatedFinding]):
                The findings associated with this node in the
                attack path.
            uuid (str):
                Unique id of the attack path node.
            attack_steps (MutableSequence[google.cloud.securitycenter_v2.types.AttackPath.AttackPathNode.AttackStepNode]):
                A list of attack step nodes that exist in
                this attack path node.
        """

        class NodeType(proto.Enum):
            r"""The type of the incoming attack step node.

            Values:
                NODE_TYPE_UNSPECIFIED (0):
                    Type not specified
                NODE_TYPE_AND (1):
                    Incoming edge joined with AND
                NODE_TYPE_OR (2):
                    Incoming edge joined with OR
                NODE_TYPE_DEFENSE (3):
                    Incoming edge is defense
                NODE_TYPE_ATTACKER (4):
                    Incoming edge is attacker
            """

            NODE_TYPE_UNSPECIFIED = 0
            NODE_TYPE_AND = 1
            NODE_TYPE_OR = 2
            NODE_TYPE_DEFENSE = 3
            NODE_TYPE_ATTACKER = 4

        class PathNodeAssociatedFinding(proto.Message):
            r"""A finding that is associated with this node in the attack
            path.

            Attributes:
                canonical_finding (str):
                    Canonical name of the associated findings. Example:
                    ``organizations/123/sources/456/findings/789``
                finding_category (str):
                    The additional taxonomy group within findings
                    from a given source.
                name (str):
                    Full resource name of the finding.
            """

            canonical_finding: str = proto.Field(
                proto.STRING,
                number=1,
            )
            finding_category: str = proto.Field(
                proto.STRING,
                number=2,
            )
            name: str = proto.Field(
                proto.STRING,
                number=3,
            )

        class AttackStepNode(proto.Message):
            r"""Detailed steps the attack can take between path nodes.

            Attributes:
                uuid (str):
                    Unique ID for one Node
                type_ (google.cloud.securitycenter_v2.types.AttackPath.AttackPathNode.NodeType):
                    Attack step type. Can be either AND, OR or
                    DEFENSE
                display_name (str):
                    User friendly name of the attack step
                labels (MutableMapping[str, str]):
                    Attack step labels for metadata
                description (str):
                    Attack step description
            """

            uuid: str = proto.Field(
                proto.STRING,
                number=1,
            )
            type_: "AttackPath.AttackPathNode.NodeType" = proto.Field(
                proto.ENUM,
                number=2,
                enum="AttackPath.AttackPathNode.NodeType",
            )
            display_name: str = proto.Field(
                proto.STRING,
                number=3,
            )
            labels: MutableMapping[str, str] = proto.MapField(
                proto.STRING,
                proto.STRING,
                number=4,
            )
            description: str = proto.Field(
                proto.STRING,
                number=5,
            )

        resource: str = proto.Field(
            proto.STRING,
            number=1,
        )
        resource_type: str = proto.Field(
            proto.STRING,
            number=2,
        )
        display_name: str = proto.Field(
            proto.STRING,
            number=3,
        )
        associated_findings: MutableSequence[
            "AttackPath.AttackPathNode.PathNodeAssociatedFinding"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message="AttackPath.AttackPathNode.PathNodeAssociatedFinding",
        )
        uuid: str = proto.Field(
            proto.STRING,
            number=5,
        )
        attack_steps: MutableSequence["AttackPath.AttackPathNode.AttackStepNode"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=6,
                message="AttackPath.AttackPathNode.AttackStepNode",
            )
        )

    class AttackPathEdge(proto.Message):
        r"""Represents a connection between a source node and a
        destination node in this attack path.

        Attributes:
            source (str):
                The attack node uuid of the source node.
            destination (str):
                The attack node uuid of the destination node.
        """

        source: str = proto.Field(
            proto.STRING,
            number=1,
        )
        destination: str = proto.Field(
            proto.STRING,
            number=2,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    path_nodes: MutableSequence[AttackPathNode] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=AttackPathNode,
    )
    edges: MutableSequence[AttackPathEdge] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=AttackPathEdge,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
