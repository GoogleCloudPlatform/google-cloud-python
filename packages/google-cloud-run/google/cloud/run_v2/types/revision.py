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

import google.api.launch_stage_pb2 as launch_stage_pb2  # type: ignore
import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.run_v2.types import condition, k8s_min, status, vendor_settings

__protobuf__ = proto.module(
    package="google.cloud.run.v2",
    manifest={
        "GetRevisionRequest",
        "ListRevisionsRequest",
        "ListRevisionsResponse",
        "DeleteRevisionRequest",
        "Revision",
    },
)


class GetRevisionRequest(proto.Message):
    r"""Request message for obtaining a Revision by its full name.

    Attributes:
        name (str):
            Required. The full name of the Revision.
            Format:

            projects/{project}/locations/{location}/services/{service}/revisions/{revision}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListRevisionsRequest(proto.Message):
    r"""Request message for retrieving a list of Revisions.

    Attributes:
        parent (str):
            Required. The Service from which the
            Revisions should be listed. To list all
            Revisions across Services, use "-" instead of
            Service name. Format:

            projects/{project}/locations/{location}/services/{service}
        page_size (int):
            Maximum number of revisions to return in this
            call.
        page_token (str):
            A page token received from a previous call to
            ListRevisions. All other parameters must match.
        show_deleted (bool):
            If true, returns deleted (but unexpired)
            resources along with active ones.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    show_deleted: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class ListRevisionsResponse(proto.Message):
    r"""Response message containing a list of Revisions.

    Attributes:
        revisions (MutableSequence[google.cloud.run_v2.types.Revision]):
            The resulting list of Revisions.
        next_page_token (str):
            A token indicating there are more items than page_size. Use
            it in the next ListRevisions request to continue.
    """

    @property
    def raw_page(self):
        return self

    revisions: MutableSequence["Revision"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Revision",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteRevisionRequest(proto.Message):
    r"""Request message for deleting a retired Revision.
    Revision lifecycle is usually managed by making changes to the
    parent Service. Only retired revisions can be deleted with this
    API.

    Attributes:
        name (str):
            Required. The name of the Revision to delete.
            Format:

            projects/{project}/locations/{location}/services/{service}/revisions/{revision}
        validate_only (bool):
            Indicates that the request should be
            validated without actually deleting any
            resources.
        etag (str):
            A system-generated fingerprint for this
            version of the resource. This may be used to
            detect modification conflict during updates.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=3,
    )


class Revision(proto.Message):
    r"""A Revision is an immutable snapshot of code and
    configuration.  A Revision references a container image.
    Revisions are only created by updates to its parent Service.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. The unique name of this
            Revision.
        uid (str):
            Output only. Server assigned unique
            identifier for the Revision. The value is a
            UUID4 string and guaranteed to remain unchanged
            until the resource is deleted.
        generation (int):
            Output only. A number that monotonically
            increases every time the user modifies the
            desired state.
        labels (MutableMapping[str, str]):
            Output only. Unstructured key value map that
            can be used to organize and categorize objects.
            User-provided labels are shared with Google's
            billing system, so they can be used to filter,
            or break down billing charges by team,
            component, environment, state, etc. For more
            information, visit
            https://cloud.google.com/resource-manager/docs/creating-managing-labels
            or
            https://cloud.google.com/run/docs/configuring/labels.
        annotations (MutableMapping[str, str]):
            Output only. Unstructured key value map that
            may be set by external tools to store and
            arbitrary metadata. They are not queryable and
            should be preserved when modifying objects.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last-modified time.
        delete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. For a deleted resource, the
            deletion time. It is only populated as a
            response to a Delete request.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. For a deleted resource, the time
            after which it will be permamently deleted. It
            is only populated as a response to a Delete
            request.
        launch_stage (google.api.launch_stage_pb2.LaunchStage):
            The least stable launch stage needed to create this
            resource, as defined by `Google Cloud Platform Launch
            Stages <https://cloud.google.com/terms/launch-stages>`__.
            Cloud Run supports ``ALPHA``, ``BETA``, and ``GA``.

            Note that this value might not be what was used as input.
            For example, if ALPHA was provided as input in the parent
            resource, but only BETA and GA-level features are were, this
            field will be BETA.
        service (str):
            Output only. The name of the parent service.
        scaling (google.cloud.run_v2.types.RevisionScaling):
            Scaling settings for this revision.
        vpc_access (google.cloud.run_v2.types.VpcAccess):
            VPC Access configuration for this Revision.
            For more information, visit
            https://cloud.google.com/run/docs/configuring/connecting-vpc.
        max_instance_request_concurrency (int):
            Sets the maximum number of requests that each
            serving instance can receive.
        timeout (google.protobuf.duration_pb2.Duration):
            Max allowed time for an instance to respond
            to a request.
        service_account (str):
            Email address of the IAM service account
            associated with the revision of the service. The
            service account represents the identity of the
            running revision, and determines what
            permissions the revision has.
        containers (MutableSequence[google.cloud.run_v2.types.Container]):
            Holds the single container that defines the
            unit of execution for this Revision.
        volumes (MutableSequence[google.cloud.run_v2.types.Volume]):
            A list of Volumes to make available to
            containers.
        execution_environment (google.cloud.run_v2.types.ExecutionEnvironment):
            The execution environment being used to host
            this Revision.
        encryption_key (str):
            A reference to a customer managed encryption
            key (CMEK) to use to encrypt this container
            image. For more information, go to
            https://cloud.google.com/run/docs/securing/using-cmek
        service_mesh (google.cloud.run_v2.types.ServiceMesh):
            Enables service mesh connectivity.
        encryption_key_revocation_action (google.cloud.run_v2.types.EncryptionKeyRevocationAction):
            The action to take if the encryption key is
            revoked.
        encryption_key_shutdown_duration (google.protobuf.duration_pb2.Duration):
            If encryption_key_revocation_action is SHUTDOWN, the
            duration before shutting down all instances. The minimum
            increment is 1 hour.
        reconciling (bool):
            Output only. Indicates whether the resource's reconciliation
            is still in progress. See comments in
            ``Service.reconciling`` for additional information on
            reconciliation process in Cloud Run.
        conditions (MutableSequence[google.cloud.run_v2.types.Condition]):
            Output only. The Condition of this Revision,
            containing its readiness status, and detailed
            error information in case it did not reach a
            serving state.
        observed_generation (int):
            Output only. The generation of this Revision currently
            serving traffic. See comments in ``reconciling`` for
            additional information on reconciliation process in Cloud
            Run.
        log_uri (str):
            Output only. The Google Console URI to obtain
            logs for the Revision.
        satisfies_pzs (bool):
            Output only. Reserved for future use.
        session_affinity (bool):
            Enable session affinity.
        scaling_status (google.cloud.run_v2.types.RevisionScalingStatus):
            Output only. The current effective scaling
            settings for the revision.
        node_selector (google.cloud.run_v2.types.NodeSelector):
            The node selector for the revision.
        gpu_zonal_redundancy_disabled (bool):
            Optional. Output only. True if GPU zonal
            redundancy is disabled on this revision.

            This field is a member of `oneof`_ ``_gpu_zonal_redundancy_disabled``.
        creator (str):
            Output only. Email address of the
            authenticated creator.
        etag (str):
            Output only. A system-generated fingerprint
            for this version of the resource. May be used to
            detect modification conflict during updates.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    generation: int = proto.Field(
        proto.INT64,
        number=3,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    delete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    launch_stage: launch_stage_pb2.LaunchStage = proto.Field(
        proto.ENUM,
        number=10,
        enum=launch_stage_pb2.LaunchStage,
    )
    service: str = proto.Field(
        proto.STRING,
        number=11,
    )
    scaling: vendor_settings.RevisionScaling = proto.Field(
        proto.MESSAGE,
        number=12,
        message=vendor_settings.RevisionScaling,
    )
    vpc_access: vendor_settings.VpcAccess = proto.Field(
        proto.MESSAGE,
        number=13,
        message=vendor_settings.VpcAccess,
    )
    max_instance_request_concurrency: int = proto.Field(
        proto.INT32,
        number=34,
    )
    timeout: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=15,
        message=duration_pb2.Duration,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=16,
    )
    containers: MutableSequence[k8s_min.Container] = proto.RepeatedField(
        proto.MESSAGE,
        number=17,
        message=k8s_min.Container,
    )
    volumes: MutableSequence[k8s_min.Volume] = proto.RepeatedField(
        proto.MESSAGE,
        number=18,
        message=k8s_min.Volume,
    )
    execution_environment: vendor_settings.ExecutionEnvironment = proto.Field(
        proto.ENUM,
        number=20,
        enum=vendor_settings.ExecutionEnvironment,
    )
    encryption_key: str = proto.Field(
        proto.STRING,
        number=21,
    )
    service_mesh: vendor_settings.ServiceMesh = proto.Field(
        proto.MESSAGE,
        number=22,
        message=vendor_settings.ServiceMesh,
    )
    encryption_key_revocation_action: vendor_settings.EncryptionKeyRevocationAction = (
        proto.Field(
            proto.ENUM,
            number=23,
            enum=vendor_settings.EncryptionKeyRevocationAction,
        )
    )
    encryption_key_shutdown_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=24,
        message=duration_pb2.Duration,
    )
    reconciling: bool = proto.Field(
        proto.BOOL,
        number=30,
    )
    conditions: MutableSequence[condition.Condition] = proto.RepeatedField(
        proto.MESSAGE,
        number=31,
        message=condition.Condition,
    )
    observed_generation: int = proto.Field(
        proto.INT64,
        number=32,
    )
    log_uri: str = proto.Field(
        proto.STRING,
        number=33,
    )
    satisfies_pzs: bool = proto.Field(
        proto.BOOL,
        number=37,
    )
    session_affinity: bool = proto.Field(
        proto.BOOL,
        number=38,
    )
    scaling_status: status.RevisionScalingStatus = proto.Field(
        proto.MESSAGE,
        number=39,
        message=status.RevisionScalingStatus,
    )
    node_selector: vendor_settings.NodeSelector = proto.Field(
        proto.MESSAGE,
        number=40,
        message=vendor_settings.NodeSelector,
    )
    gpu_zonal_redundancy_disabled: bool = proto.Field(
        proto.BOOL,
        number=48,
        optional=True,
    )
    creator: str = proto.Field(
        proto.STRING,
        number=49,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=99,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
