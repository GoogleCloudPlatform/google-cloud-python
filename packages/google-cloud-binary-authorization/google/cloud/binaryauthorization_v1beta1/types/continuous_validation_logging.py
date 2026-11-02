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

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.binaryauthorization.v1beta1",
    manifest={
        "ContinuousValidationEvent",
    },
)


class ContinuousValidationEvent(proto.Message):
    r"""Represents an auditing event from Continuous Validation.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        pod_event (google.cloud.binaryauthorization_v1beta1.types.ContinuousValidationEvent.ContinuousValidationPodEvent):
            Pod event.

            This field is a member of `oneof`_ ``event_type``.
        config_error_event (google.cloud.binaryauthorization_v1beta1.types.ContinuousValidationEvent.ConfigErrorEvent):
            Config error event.

            This field is a member of `oneof`_ ``event_type``.
    """

    class ContinuousValidationPodEvent(proto.Message):
        r"""An auditing event for one Pod.

        Attributes:
            pod_namespace (str):
                The k8s namespace of the Pod.
            pod (str):
                The name of the Pod.
            policy_name (str):
                The name of the policy.
            deploy_time (google.protobuf.timestamp_pb2.Timestamp):
                Deploy time of the Pod from k8s.
            end_time (google.protobuf.timestamp_pb2.Timestamp):
                Termination time of the Pod from k8s, or
                nothing if still running.
            verdict (google.cloud.binaryauthorization_v1beta1.types.ContinuousValidationEvent.ContinuousValidationPodEvent.PolicyConformanceVerdict):
                Auditing verdict for this Pod.
            images (MutableSequence[google.cloud.binaryauthorization_v1beta1.types.ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails]):
                List of images with auditing details.
        """

        class PolicyConformanceVerdict(proto.Enum):
            r"""Audit time policy conformance verdict.

            Values:
                POLICY_CONFORMANCE_VERDICT_UNSPECIFIED (0):
                    We should always have a verdict. This is an
                    error.
                VIOLATES_POLICY (1):
                    The pod violates the policy.
            """

            POLICY_CONFORMANCE_VERDICT_UNSPECIFIED = 0
            VIOLATES_POLICY = 1

        class ImageDetails(proto.Message):
            r"""Container image with auditing details.

            Attributes:
                image (str):
                    The name of the image.
                container_name (str):
                    The name of the container.
                container_type (google.cloud.binaryauthorization_v1beta1.types.ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.ContainerType):
                    The container type that this image belongs
                    to.
                result (google.cloud.binaryauthorization_v1beta1.types.ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.AuditResult):
                    The result of the audit for this image.
                description (str):
                    Description of the above result.
                check_results (MutableSequence[google.cloud.binaryauthorization_v1beta1.types.ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.CheckResult]):
                    List of check results.
            """

            class ContainerType(proto.Enum):
                r"""The container type.

                Values:
                    CONTAINER_TYPE_UNSPECIFIED (0):
                        The container type should always be
                        specified. This is an error.
                    CONTAINER (1):
                        A regular deployment.
                    INIT_CONTAINER (2):
                        Init container defined as specified at
                        https://kubernetes.io/docs/concepts/workloads/pods/init-containers/
                    EPHEMERAL_CONTAINER (3):
                        Ephemeral container defined as specified at
                        https://kubernetes.io/docs/concepts/workloads/pods/ephemeral-containers/
                """

                CONTAINER_TYPE_UNSPECIFIED = 0
                CONTAINER = 1
                INIT_CONTAINER = 2
                EPHEMERAL_CONTAINER = 3

            class AuditResult(proto.Enum):
                r"""Result of the audit.

                Values:
                    AUDIT_RESULT_UNSPECIFIED (0):
                        Unspecified result. This is an error.
                    ALLOW (1):
                        Image is allowed.
                    DENY (2):
                        Image is denied.
                """

                AUDIT_RESULT_UNSPECIFIED = 0
                ALLOW = 1
                DENY = 2

            class CheckResult(proto.Message):
                r"""

                Attributes:
                    check_set_index (str):
                        The index of the check set.
                    check_set_name (str):
                        The name of the check set.
                    check_set_scope (google.cloud.binaryauthorization_v1beta1.types.ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.CheckResult.CheckSetScope):
                        The scope of the check set.
                    check_index (str):
                        The index of the check.
                    check_name (str):
                        The name of the check.
                    check_type (str):
                        The type of the check.
                    verdict (google.cloud.binaryauthorization_v1beta1.types.ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.CheckResult.CheckVerdict):
                        The verdict of this check.
                    explanation (str):
                        User-friendly explanation of this check
                        result.
                """

                class CheckVerdict(proto.Enum):
                    r"""Result of evaluating one check.

                    Values:
                        CHECK_VERDICT_UNSPECIFIED (0):
                            We should always have a verdict. This is an
                            error.
                        NON_CONFORMANT (1):
                            The check was successfully evaluated and the
                            image did not satisfy the check.
                    """

                    CHECK_VERDICT_UNSPECIFIED = 0
                    NON_CONFORMANT = 1

                class CheckSetScope(proto.Message):
                    r"""A scope specifier for check sets.

                    This message has `oneof`_ fields (mutually exclusive fields).
                    For each oneof, at most one member field can be set at the same time.
                    Setting any member of the oneof automatically clears all other
                    members.

                    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

                    Attributes:
                        kubernetes_service_account (str):
                            Matches a single Kubernetes service account, e.g.
                            'my-namespace:my-service-account'.
                            ``kubernetes_service_account`` scope is always more specific
                            than ``kubernetes_namespace`` scope for the same namespace.

                            This field is a member of `oneof`_ ``scope``.
                        kubernetes_namespace (str):
                            Matches all Kubernetes service accounts in the provided
                            namespace, unless a more specific
                            ``kubernetes_service_account`` scope already matched.

                            This field is a member of `oneof`_ ``scope``.
                    """

                    kubernetes_service_account: str = proto.Field(
                        proto.STRING,
                        number=1,
                        oneof="scope",
                    )
                    kubernetes_namespace: str = proto.Field(
                        proto.STRING,
                        number=2,
                        oneof="scope",
                    )

                check_set_index: str = proto.Field(
                    proto.STRING,
                    number=1,
                )
                check_set_name: str = proto.Field(
                    proto.STRING,
                    number=2,
                )
                check_set_scope: "ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.CheckResult.CheckSetScope" = proto.Field(
                    proto.MESSAGE,
                    number=3,
                    message="ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.CheckResult.CheckSetScope",
                )
                check_index: str = proto.Field(
                    proto.STRING,
                    number=4,
                )
                check_name: str = proto.Field(
                    proto.STRING,
                    number=5,
                )
                check_type: str = proto.Field(
                    proto.STRING,
                    number=6,
                )
                verdict: "ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.CheckResult.CheckVerdict" = proto.Field(
                    proto.ENUM,
                    number=7,
                    enum="ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.CheckResult.CheckVerdict",
                )
                explanation: str = proto.Field(
                    proto.STRING,
                    number=8,
                )

            image: str = proto.Field(
                proto.STRING,
                number=1,
            )
            container_name: str = proto.Field(
                proto.STRING,
                number=5,
            )
            container_type: "ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.ContainerType" = proto.Field(
                proto.ENUM,
                number=6,
                enum="ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.ContainerType",
            )
            result: "ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.AuditResult" = proto.Field(
                proto.ENUM,
                number=2,
                enum="ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.AuditResult",
            )
            description: str = proto.Field(
                proto.STRING,
                number=3,
            )
            check_results: MutableSequence[
                "ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.CheckResult"
            ] = proto.RepeatedField(
                proto.MESSAGE,
                number=4,
                message="ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails.CheckResult",
            )

        pod_namespace: str = proto.Field(
            proto.STRING,
            number=7,
        )
        pod: str = proto.Field(
            proto.STRING,
            number=1,
        )
        policy_name: str = proto.Field(
            proto.STRING,
            number=8,
        )
        deploy_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=2,
            message=timestamp_pb2.Timestamp,
        )
        end_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=3,
            message=timestamp_pb2.Timestamp,
        )
        verdict: "ContinuousValidationEvent.ContinuousValidationPodEvent.PolicyConformanceVerdict" = proto.Field(
            proto.ENUM,
            number=4,
            enum="ContinuousValidationEvent.ContinuousValidationPodEvent.PolicyConformanceVerdict",
        )
        images: MutableSequence[
            "ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=5,
            message="ContinuousValidationEvent.ContinuousValidationPodEvent.ImageDetails",
        )

    class ConfigErrorEvent(proto.Message):
        r"""An event describing a user-actionable configuration issue
        that prevents CV from auditing.

        Attributes:
            description (str):
                A description of the issue.
        """

        description: str = proto.Field(
            proto.STRING,
            number=1,
        )

    pod_event: ContinuousValidationPodEvent = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="event_type",
        message=ContinuousValidationPodEvent,
    )
    config_error_event: ConfigErrorEvent = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="event_type",
        message=ConfigErrorEvent,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
