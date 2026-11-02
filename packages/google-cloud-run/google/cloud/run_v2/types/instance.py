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

from google.cloud.run_v2.types import (
    condition,
    container_status,
    k8s_min,
    vendor_settings,
)

__protobuf__ = proto.module(
    package="google.cloud.run.v2",
    manifest={
        "CreateInstanceRequest",
        "GetInstanceRequest",
        "DeleteInstanceRequest",
        "ListInstancesRequest",
        "ListInstancesResponse",
        "StopInstanceRequest",
        "StartInstanceRequest",
        "Instance",
    },
)


class CreateInstanceRequest(proto.Message):
    r"""

    Attributes:
        parent (str):

        instance (google.cloud.run_v2.types.Instance):

        instance_id (str):
            Required. The unique identifier for the Instance. It must
            begin with letter, and cannot end with hyphen; must contain
            fewer than 50 characters. The name of the instance becomes
            {parent}/instances/{instance_id}.
        validate_only (bool):
            Optional. Indicates that the request should
            be validated and default values populated,
            without persisting the request or creating any
            resources.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance: "Instance" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Instance",
    )
    instance_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class GetInstanceRequest(proto.Message):
    r"""

    Attributes:
        name (str):

    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteInstanceRequest(proto.Message):
    r"""

    Attributes:
        name (str):

        validate_only (bool):
            Optional. Indicates that the request should
            be validated without actually deleting any
            resources.
        etag (str):
            Optional. A system-generated fingerprint for
            this version of the resource. May be used to
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


class ListInstancesRequest(proto.Message):
    r"""Request message for retrieving a list of Instances.

    Attributes:
        parent (str):
            Required. The location and project to list
            resources on. Format:
            projects/{project}/locations/{location}, where
            {project} can be project id or number.
        page_size (int):
            Optional. Maximum number of Instances to
            return in this call.
        page_token (str):
            Optional. A page token received from a
            previous call to ListInstances. All other
            parameters must match.
        show_deleted (bool):
            Optional. If true, returns deleted (but
            unexpired) resources along with active ones.
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


class ListInstancesResponse(proto.Message):
    r"""Response message containing a list of Instances.

    Attributes:
        instances (MutableSequence[google.cloud.run_v2.types.Instance]):
            The resulting list of Instances.
        next_page_token (str):
            A token indicating there are more items than page_size. Use
            it in the next ListInstances request to continue.
    """

    @property
    def raw_page(self):
        return self

    instances: MutableSequence["Instance"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Instance",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class StopInstanceRequest(proto.Message):
    r"""Request message for deleting an Instance.

    Attributes:
        name (str):
            Required. The name of the Instance to stop. Format:
            ``projects/{project}/locations/{location}/instances/{instance}``,
            where ``{project}`` can be project id or number.
        validate_only (bool):
            Optional. Indicates that the request should
            be validated without actually stopping any
            resources.
        etag (str):
            Optional. A system-generated fingerprint for
            this version of the resource. This may be used
            to detect modification conflict during updates.
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


class StartInstanceRequest(proto.Message):
    r"""Request message for starting an Instance.

    Attributes:
        name (str):
            Required. The name of the Instance to stop. Format:
            ``projects/{project}/locations/{location}/instances/{instance}``,
            where ``{project}`` can be project id or number.
        validate_only (bool):
            Optional. Indicates that the request should
            be validated without actually stopping any
            resources.
        etag (str):
            Optional. A system-generated fingerprint for
            this version of the resource. This may be used
            to detect modification conflict during updates.
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


class Instance(proto.Message):
    r"""A Cloud Run Instance represents a single group of containers
    running in a region.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            The fully qualified name of this Instance. In
            CreateInstanceRequest, this field is ignored, and instead
            composed from CreateInstanceRequest.parent and
            CreateInstanceRequest.instance_id.

            Format:
            projects/{project}/locations/{location}/instances/{instance_id}
        description (str):
            User-provided description of the Instance.
            This field currently has a 512-character limit.
        uid (str):
            Output only. Server assigned unique
            identifier for the trigger. The value is a UUID4
            string and guaranteed to remain unchanged until
            the resource is deleted.
        generation (int):
            Output only. A number that monotonically increases every
            time the user modifies the desired state. Please note that
            unlike v1, this is an int64 value. As with most Google APIs,
            its JSON representation will be a ``string`` instead of an
            ``integer``.
        labels (MutableMapping[str, str]):

        annotations (MutableMapping[str, str]):

        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last-modified time.
        delete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The deletion time.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. For a deleted resource, the time
            after which it will be permamently deleted.
        creator (str):
            Output only. Email address of the
            authenticated creator.
        last_modifier (str):
            Output only. Email address of the last
            authenticated modifier.
        client (str):
            Arbitrary identifier for the API client.
        client_version (str):
            Arbitrary version identifier for the API
            client.
        launch_stage (google.api.launch_stage_pb2.LaunchStage):
            The launch stage as defined by `Google Cloud Platform Launch
            Stages <https://cloud.google.com/terms/launch-stages>`__.
            Cloud Run supports ``ALPHA``, ``BETA``, and ``GA``. If no
            value is specified, GA is assumed. Set the launch stage to a
            preview stage on input to allow use of preview features in
            that stage. On read (or output), describes whether the
            resource uses preview features.

            .. raw:: html

                <p>
                 For example, if ALPHA is provided as input, but only BETA and GA-level
                 features are used, this field will be BETA on output.
        binary_authorization (google.cloud.run_v2.types.BinaryAuthorization):
            Settings for the Binary Authorization
            feature.
        vpc_access (google.cloud.run_v2.types.VpcAccess):
            Optional. VPC Access configuration to use for
            this Revision. For more information, visit
            https://cloud.google.com/run/docs/configuring/connecting-vpc.
        service_account (str):

        containers (MutableSequence[google.cloud.run_v2.types.Container]):
            Required. Holds the single container that
            defines the unit of execution for this Instance.
        volumes (MutableSequence[google.cloud.run_v2.types.Volume]):
            A list of Volumes to make available to
            containers.
        encryption_key (str):
            A reference to a customer managed encryption
            key (CMEK) to use to encrypt this container
            image. For more information, go to
            https://cloud.google.com/run/docs/securing/using-cmek
        encryption_key_revocation_action (google.cloud.run_v2.types.EncryptionKeyRevocationAction):
            The action to take if the encryption key is
            revoked.
        encryption_key_shutdown_duration (google.protobuf.duration_pb2.Duration):
            If encryption_key_revocation_action is SHUTDOWN, the
            duration before shutting down all instances. The minimum
            increment is 1 hour.
        node_selector (google.cloud.run_v2.types.NodeSelector):
            Optional. The node selector for the instance.
        gpu_zonal_redundancy_disabled (bool):
            Optional. True if GPU zonal redundancy is
            disabled on this instance.

            This field is a member of `oneof`_ ``_gpu_zonal_redundancy_disabled``.
        ingress (google.cloud.run_v2.types.IngressTraffic):
            Optional. Provides the ingress settings for this Instance.
            On output, returns the currently observed ingress settings,
            or INGRESS_TRAFFIC_UNSPECIFIED if no revision is active.
        invoker_iam_disabled (bool):
            Optional. Disables IAM permission check for
            run.routes.invoke for callers of this Instance. For more
            information, visit
            https://cloud.google.com/run/docs/securing/managing-access#invoker_check.
        iap_enabled (bool):
            Optional. IAP settings on the Instance.
        observed_generation (int):
            Output only. The generation of this Instance currently
            serving traffic. See comments in ``reconciling`` for
            additional information on reconciliation process in Cloud
            Run. Please note that unlike v1, this is an int64 value. As
            with most Google APIs, its JSON representation will be a
            ``string`` instead of an ``integer``.
        log_uri (str):
            Output only. The Google Console URI to obtain
            logs for the Instance.
        terminal_condition (google.cloud.run_v2.types.Condition):
            Output only. The Condition of this Instance, containing its
            readiness status, and detailed error information in case it
            did not reach a serving state. See comments in
            ``reconciling`` for additional information on reconciliation
            process in Cloud Run.
        conditions (MutableSequence[google.cloud.run_v2.types.Condition]):
            Output only. The Conditions of all other associated
            sub-resources. They contain additional diagnostics
            information in case the Instance does not reach its Serving
            state. See comments in ``reconciling`` for additional
            information on reconciliation process in Cloud Run.
        container_statuses (MutableSequence[google.cloud.run_v2.types.ContainerStatus]):
            Output only. Status information for each of
            the specified containers. The status includes
            the resolved digest for specified images.
        satisfies_pzs (bool):
            Output only. Reserved for future use.
        urls (MutableSequence[str]):
            Output only. All URLs serving traffic for
            this Instance.
        reconciling (bool):
            Output only. Returns true if the Instance is currently being
            acted upon by the system to bring it into the desired state.

            When a new Instance is created, or an existing one is
            updated, Cloud Run will asynchronously perform all necessary
            steps to bring the Instance to the desired serving state.
            This process is called reconciliation. While reconciliation
            is in process, ``observed_generation`` will have a transient
            value that might mismatch the intended state. Once
            reconciliation is over (and this field is false), there are
            two possible outcomes: reconciliation succeeded and the
            serving state matches the Instance, or there was an error,
            and reconciliation failed. This state can be found in
            ``terminal_condition.state``.
        etag (str):
            Optional. A system-generated fingerprint for
            this version of the resource. May be used to
            detect modification conflict during updates.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=4,
    )
    generation: int = proto.Field(
        proto.INT64,
        number=5,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    delete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )
    creator: str = proto.Field(
        proto.STRING,
        number=12,
    )
    last_modifier: str = proto.Field(
        proto.STRING,
        number=13,
    )
    client: str = proto.Field(
        proto.STRING,
        number=14,
    )
    client_version: str = proto.Field(
        proto.STRING,
        number=15,
    )
    launch_stage: launch_stage_pb2.LaunchStage = proto.Field(
        proto.ENUM,
        number=16,
        enum=launch_stage_pb2.LaunchStage,
    )
    binary_authorization: vendor_settings.BinaryAuthorization = proto.Field(
        proto.MESSAGE,
        number=17,
        message=vendor_settings.BinaryAuthorization,
    )
    vpc_access: vendor_settings.VpcAccess = proto.Field(
        proto.MESSAGE,
        number=18,
        message=vendor_settings.VpcAccess,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=19,
    )
    containers: MutableSequence[k8s_min.Container] = proto.RepeatedField(
        proto.MESSAGE,
        number=20,
        message=k8s_min.Container,
    )
    volumes: MutableSequence[k8s_min.Volume] = proto.RepeatedField(
        proto.MESSAGE,
        number=21,
        message=k8s_min.Volume,
    )
    encryption_key: str = proto.Field(
        proto.STRING,
        number=22,
    )
    encryption_key_revocation_action: vendor_settings.EncryptionKeyRevocationAction = (
        proto.Field(
            proto.ENUM,
            number=24,
            enum=vendor_settings.EncryptionKeyRevocationAction,
        )
    )
    encryption_key_shutdown_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=25,
        message=duration_pb2.Duration,
    )
    node_selector: vendor_settings.NodeSelector = proto.Field(
        proto.MESSAGE,
        number=26,
        message=vendor_settings.NodeSelector,
    )
    gpu_zonal_redundancy_disabled: bool = proto.Field(
        proto.BOOL,
        number=27,
        optional=True,
    )
    ingress: vendor_settings.IngressTraffic = proto.Field(
        proto.ENUM,
        number=28,
        enum=vendor_settings.IngressTraffic,
    )
    invoker_iam_disabled: bool = proto.Field(
        proto.BOOL,
        number=29,
    )
    iap_enabled: bool = proto.Field(
        proto.BOOL,
        number=30,
    )
    observed_generation: int = proto.Field(
        proto.INT64,
        number=40,
    )
    log_uri: str = proto.Field(
        proto.STRING,
        number=41,
    )
    terminal_condition: condition.Condition = proto.Field(
        proto.MESSAGE,
        number=42,
        message=condition.Condition,
    )
    conditions: MutableSequence[condition.Condition] = proto.RepeatedField(
        proto.MESSAGE,
        number=43,
        message=condition.Condition,
    )
    container_statuses: MutableSequence[container_status.ContainerStatus] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=44,
            message=container_status.ContainerStatus,
        )
    )
    satisfies_pzs: bool = proto.Field(
        proto.BOOL,
        number=46,
    )
    urls: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=45,
    )
    reconciling: bool = proto.Field(
        proto.BOOL,
        number=98,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=99,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
