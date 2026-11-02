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

import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.run_v2.types import k8s_min, vendor_settings

__protobuf__ = proto.module(
    package="google.cloud.run.v2",
    manifest={
        "WorkerPoolRevisionTemplate",
    },
)


class WorkerPoolRevisionTemplate(proto.Message):
    r"""WorkerPoolRevisionTemplate describes the data a worker pool
    revision should have when created from a template.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        revision (str):
            Optional. The unique name for the revision.
            If this field is omitted, it will be
            automatically generated based on the WorkerPool
            name.
        labels (MutableMapping[str, str]):
            Optional. Unstructured key value map that can be used to
            organize and categorize objects. User-provided labels are
            shared with Google's billing system, so they can be used to
            filter, or break down billing charges by team, component,
            environment, state, etc. For more information, visit
            https://cloud.google.com/resource-manager/docs/creating-managing-labels
            or https://cloud.google.com/run/docs/configuring/labels.

            Cloud Run API v2 does not support labels with
            ``run.googleapis.com``, ``cloud.googleapis.com``,
            ``serving.knative.dev``, or ``autoscaling.knative.dev``
            namespaces, and they will be rejected. All system labels in
            v1 now have a corresponding field in v2
            WorkerPoolRevisionTemplate.
        annotations (MutableMapping[str, str]):
            Optional. Unstructured key value map that may be set by
            external tools to store and arbitrary metadata. They are not
            queryable and should be preserved when modifying objects.

            Cloud Run API v2 does not support annotations with
            ``run.googleapis.com``, ``cloud.googleapis.com``,
            ``serving.knative.dev``, or ``autoscaling.knative.dev``
            namespaces, and they will be rejected. All system
            annotations in v1 now have a corresponding field in v2
            WorkerPoolRevisionTemplate.

            This field follows Kubernetes annotations' namespacing,
            limits, and rules.
        vpc_access (google.cloud.run_v2.types.VpcAccess):
            Optional. VPC Access configuration to use for
            this Revision. For more information, visit
            https://cloud.google.com/run/docs/configuring/connecting-vpc.
        service_account (str):
            Optional. Email address of the IAM service
            account associated with the revision of the
            service. The service account represents the
            identity of the running revision, and determines
            what permissions the revision has. If not
            provided, the revision will use the project's
            default service account.
        containers (MutableSequence[google.cloud.run_v2.types.Container]):
            Holds list of the containers that defines the
            unit of execution for this Revision.
        volumes (MutableSequence[google.cloud.run_v2.types.Volume]):
            Optional. A list of Volumes to make available
            to containers.
        encryption_key (str):
            A reference to a customer managed encryption
            key (CMEK) to use to encrypt this container
            image. For more information, go to
            https://cloud.google.com/run/docs/securing/using-cmek
        service_mesh (google.cloud.run_v2.types.ServiceMesh):
            Optional. Enables service mesh connectivity.
        encryption_key_revocation_action (google.cloud.run_v2.types.EncryptionKeyRevocationAction):
            Optional. The action to take if the
            encryption key is revoked.
        encryption_key_shutdown_duration (google.protobuf.duration_pb2.Duration):
            Optional. If encryption_key_revocation_action is SHUTDOWN,
            the duration before shutting down all instances. The minimum
            increment is 1 hour.
        node_selector (google.cloud.run_v2.types.NodeSelector):
            Optional. The node selector for the revision
            template.
        gpu_zonal_redundancy_disabled (bool):
            Optional. True if GPU zonal redundancy is
            disabled on this worker pool.

            This field is a member of `oneof`_ ``_gpu_zonal_redundancy_disabled``.
    """

    revision: str = proto.Field(
        proto.STRING,
        number=1,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )
    vpc_access: vendor_settings.VpcAccess = proto.Field(
        proto.MESSAGE,
        number=4,
        message=vendor_settings.VpcAccess,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=5,
    )
    containers: MutableSequence[k8s_min.Container] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=k8s_min.Container,
    )
    volumes: MutableSequence[k8s_min.Volume] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message=k8s_min.Volume,
    )
    encryption_key: str = proto.Field(
        proto.STRING,
        number=8,
    )
    service_mesh: vendor_settings.ServiceMesh = proto.Field(
        proto.MESSAGE,
        number=9,
        message=vendor_settings.ServiceMesh,
    )
    encryption_key_revocation_action: vendor_settings.EncryptionKeyRevocationAction = (
        proto.Field(
            proto.ENUM,
            number=10,
            enum=vendor_settings.EncryptionKeyRevocationAction,
        )
    )
    encryption_key_shutdown_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=11,
        message=duration_pb2.Duration,
    )
    node_selector: vendor_settings.NodeSelector = proto.Field(
        proto.MESSAGE,
        number=13,
        message=vendor_settings.NodeSelector,
    )
    gpu_zonal_redundancy_disabled: bool = proto.Field(
        proto.BOOL,
        number=16,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
