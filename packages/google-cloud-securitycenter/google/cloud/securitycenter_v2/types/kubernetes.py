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

from google.cloud.securitycenter_v2.types import container, label

__protobuf__ = proto.module(
    package="google.cloud.securitycenter.v2",
    manifest={
        "Kubernetes",
    },
)


class Kubernetes(proto.Message):
    r"""Kubernetes-related attributes.

    Attributes:
        pods (MutableSequence[google.cloud.securitycenter_v2.types.Kubernetes.Pod]):
            Kubernetes
            `Pods <https://cloud.google.com/kubernetes-engine/docs/concepts/pod>`__
            associated with the finding. This field contains Pod records
            for each container that is owned by a Pod.
        nodes (MutableSequence[google.cloud.securitycenter_v2.types.Kubernetes.Node]):
            Provides Kubernetes
            `node <https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#nodes>`__
            information.
        node_pools (MutableSequence[google.cloud.securitycenter_v2.types.Kubernetes.NodePool]):
            GKE `node
            pools <https://cloud.google.com/kubernetes-engine/docs/concepts/node-pools>`__
            associated with the finding. This field contains node pool
            information for each node, when it is available.
        roles (MutableSequence[google.cloud.securitycenter_v2.types.Kubernetes.Role]):
            Provides Kubernetes role information for findings that
            involve `Roles or
            ClusterRoles <https://cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control>`__.
        bindings (MutableSequence[google.cloud.securitycenter_v2.types.Kubernetes.Binding]):
            Provides Kubernetes role binding information for findings
            that involve `RoleBindings or
            ClusterRoleBindings <https://cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control>`__.
        access_reviews (MutableSequence[google.cloud.securitycenter_v2.types.Kubernetes.AccessReview]):
            Provides information on any Kubernetes access
            reviews (privilege checks) relevant to the
            finding.
        objects (MutableSequence[google.cloud.securitycenter_v2.types.Kubernetes.Object]):
            Kubernetes objects related to the finding.
    """

    class Pod(proto.Message):
        r"""A Kubernetes Pod.

        Attributes:
            ns (str):
                Kubernetes Pod namespace.
            name (str):
                Kubernetes Pod name.
            labels (MutableSequence[google.cloud.securitycenter_v2.types.Label]):
                Pod labels.  For Kubernetes containers, these
                are applied to the container.
            containers (MutableSequence[google.cloud.securitycenter_v2.types.Container]):
                Pod containers associated with this finding,
                if any.
        """

        ns: str = proto.Field(
            proto.STRING,
            number=1,
        )
        name: str = proto.Field(
            proto.STRING,
            number=2,
        )
        labels: MutableSequence[label.Label] = proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message=label.Label,
        )
        containers: MutableSequence[container.Container] = proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message=container.Container,
        )

    class Node(proto.Message):
        r"""Kubernetes nodes associated with the finding.

        Attributes:
            name (str):
                `Full resource
                name <https://google.aip.dev/122#full-resource-names>`__ of
                the Compute Engine VM running the cluster node.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class NodePool(proto.Message):
        r"""Provides GKE node pool information.

        Attributes:
            name (str):
                Kubernetes node pool name.
            nodes (MutableSequence[google.cloud.securitycenter_v2.types.Kubernetes.Node]):
                Nodes associated with the finding.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        nodes: MutableSequence["Kubernetes.Node"] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="Kubernetes.Node",
        )

    class Role(proto.Message):
        r"""Kubernetes Role or ClusterRole.

        Attributes:
            kind (google.cloud.securitycenter_v2.types.Kubernetes.Role.Kind):
                Role type.
            ns (str):
                Role namespace.
            name (str):
                Role name.
        """

        class Kind(proto.Enum):
            r"""Types of Kubernetes roles.

            Values:
                KIND_UNSPECIFIED (0):
                    Role type is not specified.
                ROLE (1):
                    Kubernetes Role.
                CLUSTER_ROLE (2):
                    Kubernetes ClusterRole.
            """

            KIND_UNSPECIFIED = 0
            ROLE = 1
            CLUSTER_ROLE = 2

        kind: "Kubernetes.Role.Kind" = proto.Field(
            proto.ENUM,
            number=1,
            enum="Kubernetes.Role.Kind",
        )
        ns: str = proto.Field(
            proto.STRING,
            number=2,
        )
        name: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class Binding(proto.Message):
        r"""Represents a Kubernetes RoleBinding or ClusterRoleBinding.

        Attributes:
            ns (str):
                Namespace for the binding.
            name (str):
                Name for the binding.
            role (google.cloud.securitycenter_v2.types.Kubernetes.Role):
                The Role or ClusterRole referenced by the
                binding.
            subjects (MutableSequence[google.cloud.securitycenter_v2.types.Kubernetes.Subject]):
                Represents one or more subjects that are
                bound to the role. Not always available for
                PATCH requests.
        """

        ns: str = proto.Field(
            proto.STRING,
            number=1,
        )
        name: str = proto.Field(
            proto.STRING,
            number=2,
        )
        role: "Kubernetes.Role" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="Kubernetes.Role",
        )
        subjects: MutableSequence["Kubernetes.Subject"] = proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message="Kubernetes.Subject",
        )

    class Subject(proto.Message):
        r"""Represents a Kubernetes subject.

        Attributes:
            kind (google.cloud.securitycenter_v2.types.Kubernetes.Subject.AuthType):
                Authentication type for the subject.
            ns (str):
                Namespace for the subject.
            name (str):
                Name for the subject.
        """

        class AuthType(proto.Enum):
            r"""Auth types that can be used for the subject's kind field.

            Values:
                AUTH_TYPE_UNSPECIFIED (0):
                    Authentication is not specified.
                USER (1):
                    User with valid certificate.
                SERVICEACCOUNT (2):
                    Users managed by Kubernetes API with
                    credentials stored as secrets.
                GROUP (3):
                    Collection of users.
            """

            AUTH_TYPE_UNSPECIFIED = 0
            USER = 1
            SERVICEACCOUNT = 2
            GROUP = 3

        kind: "Kubernetes.Subject.AuthType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="Kubernetes.Subject.AuthType",
        )
        ns: str = proto.Field(
            proto.STRING,
            number=2,
        )
        name: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class AccessReview(proto.Message):
        r"""Conveys information about a Kubernetes access review (such as one
        returned by a
        ```kubectl auth can-i`` <https://kubernetes.io/docs/reference/access-authn-authz/authorization/#checking-api-access>`__
        command) that was involved in a finding.

        Attributes:
            group (str):
                The API group of the resource. "\*" means all.
            ns (str):
                Namespace of the action being requested.
                Currently, there is no distinction between no
                namespace and all namespaces.  Both are
                represented by "" (empty).
            name (str):
                The name of the resource being requested.
                Empty means all.
            resource (str):
                The optional resource type requested. "\*" means all.
            subresource (str):
                The optional subresource type.
            verb (str):
                A Kubernetes resource API verb, like get, list, watch,
                create, update, delete, proxy. "\*" means all.
            version (str):
                The API version of the resource. "\*" means all.
        """

        group: str = proto.Field(
            proto.STRING,
            number=1,
        )
        ns: str = proto.Field(
            proto.STRING,
            number=2,
        )
        name: str = proto.Field(
            proto.STRING,
            number=3,
        )
        resource: str = proto.Field(
            proto.STRING,
            number=4,
        )
        subresource: str = proto.Field(
            proto.STRING,
            number=5,
        )
        verb: str = proto.Field(
            proto.STRING,
            number=6,
        )
        version: str = proto.Field(
            proto.STRING,
            number=7,
        )

    class Object(proto.Message):
        r"""Kubernetes object related to the finding, uniquely identified
        by GKNN. Used if the object Kind is not one of Pod, Node,
        NodePool, Binding, or AccessReview.

        Attributes:
            group (str):
                Kubernetes object group, such as
                "policy.k8s.io/v1".
            kind (str):
                Kubernetes object kind, such as "Namespace".
            ns (str):
                Kubernetes object namespace. Must be a valid
                DNS label. Named "ns" to avoid collision with
                C++ namespace keyword. For details see
                https://kubernetes.io/docs/tasks/administer-cluster/namespaces/.
            name (str):
                Kubernetes object name. For details see
                https://kubernetes.io/docs/concepts/overview/working-with-objects/names/.
            containers (MutableSequence[google.cloud.securitycenter_v2.types.Container]):
                Pod containers associated with this finding,
                if any.
        """

        group: str = proto.Field(
            proto.STRING,
            number=1,
        )
        kind: str = proto.Field(
            proto.STRING,
            number=2,
        )
        ns: str = proto.Field(
            proto.STRING,
            number=3,
        )
        name: str = proto.Field(
            proto.STRING,
            number=4,
        )
        containers: MutableSequence[container.Container] = proto.RepeatedField(
            proto.MESSAGE,
            number=5,
            message=container.Container,
        )

    pods: MutableSequence[Pod] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=Pod,
    )
    nodes: MutableSequence[Node] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=Node,
    )
    node_pools: MutableSequence[NodePool] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=NodePool,
    )
    roles: MutableSequence[Role] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=Role,
    )
    bindings: MutableSequence[Binding] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=Binding,
    )
    access_reviews: MutableSequence[AccessReview] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=AccessReview,
    )
    objects: MutableSequence[Object] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message=Object,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
