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
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.run_v2.types import (
    condition,
    revision_template,
    traffic_target,
    vendor_settings,
)

__protobuf__ = proto.module(
    package="google.cloud.run.v2",
    manifest={
        "CreateServiceRequest",
        "UpdateServiceRequest",
        "ListServicesRequest",
        "ListServicesResponse",
        "GetServiceRequest",
        "DeleteServiceRequest",
        "Service",
    },
)


class CreateServiceRequest(proto.Message):
    r"""Request message for creating a Service.

    Attributes:
        parent (str):
            Required. The location and project in which
            this service should be created. Format:
            projects/{project}/locations/{location}, where
            {project} can be project id or number. Only
            lowercase characters, digits, and hyphens.
        service (google.cloud.run_v2.types.Service):
            Required. The Service instance to create.
        service_id (str):
            Required. The unique identifier for the Service. It must
            begin with letter, and cannot end with hyphen; must contain
            fewer than 50 characters. The name of the service becomes
            {parent}/services/{service_id}.
        validate_only (bool):
            Indicates that the request should be
            validated and default values populated, without
            persisting the request or creating any
            resources.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    service: "Service" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Service",
    )
    service_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class UpdateServiceRequest(proto.Message):
    r"""Request message for updating a service.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to be updated.
        service (google.cloud.run_v2.types.Service):
            Required. The Service to be updated.
        validate_only (bool):
            Indicates that the request should be
            validated and default values populated, without
            persisting the request or updating any
            resources.
        allow_missing (bool):
            Optional. If set to true, and if the Service
            does not exist, it will create a new one. The
            caller must have 'run.services.create'
            permissions if this is set to true and the
            Service does not exist.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    service: "Service" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Service",
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class ListServicesRequest(proto.Message):
    r"""Request message for retrieving a list of Services.

    Attributes:
        parent (str):
            Required. The location and project to list
            resources on. Location must be a valid Google
            Cloud region, and cannot be the "-" wildcard.
            Format: projects/{project}/locations/{location},
            where {project} can be project id or number.
        page_size (int):
            Maximum number of Services to return in this
            call.
        page_token (str):
            A page token received from a previous call to
            ListServices. All other parameters must match.
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


class ListServicesResponse(proto.Message):
    r"""Response message containing a list of Services.

    Attributes:
        services (MutableSequence[google.cloud.run_v2.types.Service]):
            The resulting list of Services.
        next_page_token (str):
            A token indicating there are more items than page_size. Use
            it in the next ListServices request to continue.
        unreachable (MutableSequence[str]):
            Output only. For global requests, returns the
            list of regions that could not be reached within
            the deadline.
    """

    @property
    def raw_page(self):
        return self

    services: MutableSequence["Service"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Service",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetServiceRequest(proto.Message):
    r"""Request message for obtaining a Service by its full name.

    Attributes:
        name (str):
            Required. The full name of the Service.
            Format:
            projects/{project}/locations/{location}/services/{service},
            where {project} can be project id or number.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteServiceRequest(proto.Message):
    r"""Request message to delete a Service by its full name.

    Attributes:
        name (str):
            Required. The full name of the Service.
            Format:
            projects/{project}/locations/{location}/services/{service},
            where {project} can be project id or number.
        validate_only (bool):
            Indicates that the request should be
            validated without actually deleting any
            resources.
        etag (str):
            A system-generated fingerprint for this
            version of the resource. May be used to detect
            modification conflict during updates.
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


class Service(proto.Message):
    r"""Service acts as a top-level container that manages a set of
    configurations and revision templates which implement a network
    service. Service exists to provide a singular abstraction which
    can be access controlled, reasoned about, and which encapsulates
    software lifecycle decisions such as rollout policy and team
    resource ownership.

    Attributes:
        name (str):
            Identifier. The fully qualified name of this Service. In
            CreateServiceRequest, this field is ignored, and instead
            composed from CreateServiceRequest.parent and
            CreateServiceRequest.service_id.

            Format:
            projects/{project}/locations/{location}/services/{service_id}
        description (str):
            User-provided description of the Service.
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
            Optional. Unstructured key value map that can be used to
            organize and categorize objects. User-provided labels are
            shared with Google's billing system, so they can be used to
            filter, or break down billing charges by team, component,
            environment, state, etc. For more information, visit
            https://cloud.google.com/resource-manager/docs/creating-managing-labels
            or https://cloud.google.com/run/docs/configuring/labels.

            .. raw:: html

                <p>Cloud Run API v2 does not support labels with  `run.googleapis.com`,
                `cloud.googleapis.com`, `serving.knative.dev`, or `autoscaling.knative.dev`
                namespaces, and they will be rejected. All system labels in v1 now have a
                corresponding field in v2 Service.
        annotations (MutableMapping[str, str]):
            Optional. Unstructured key value map that may be set by
            external tools to store and arbitrary metadata. They are not
            queryable and should be preserved when modifying objects.

            .. raw:: html

                <p>Cloud Run API v2 does not support annotations with `run.googleapis.com`,
                `cloud.googleapis.com`, `serving.knative.dev`, or `autoscaling.knative.dev`
                namespaces, and they will be rejected in new resources. All system
                annotations in v1 now have a corresponding field in v2 Service.

            .. raw:: html

                <p>This field follows Kubernetes
                annotations' namespacing, limits, and rules.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last-modified time.
        delete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The deletion time. It is only
            populated as a response to a Delete request.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. For a deleted resource, the time
            after which it will be permanently deleted.
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
        ingress (google.cloud.run_v2.types.IngressTraffic):
            Optional. Provides the ingress settings for this Service. On
            output, returns the currently observed ingress settings, or
            INGRESS_TRAFFIC_UNSPECIFIED if no revision is active.
        launch_stage (google.api.launch_stage_pb2.LaunchStage):
            Optional. The launch stage as defined by `Google Cloud
            Platform Launch
            Stages <https://cloud.google.com/terms/launch-stages>`__.
            Cloud Run supports ``ALPHA``, ``BETA``, and ``GA``. If no
            value is specified, GA is assumed. Set the launch stage to a
            preview stage on input to allow use of preview features in
            that stage. On read (or output), describes whether the
            resource uses preview features.

            For example, if ALPHA is provided as input, but only BETA
            and GA-level features are used, this field will be BETA on
            output.
        binary_authorization (google.cloud.run_v2.types.BinaryAuthorization):
            Optional. Settings for the Binary
            Authorization feature.
        template (google.cloud.run_v2.types.RevisionTemplate):
            Required. The template used to create
            revisions for this Service.
        traffic (MutableSequence[google.cloud.run_v2.types.TrafficTarget]):
            Optional. Specifies how to distribute traffic over a
            collection of Revisions belonging to the Service. If traffic
            is empty or not provided, defaults to 100% traffic to the
            latest ``Ready`` Revision.
        scaling (google.cloud.run_v2.types.ServiceScaling):
            Optional. Specifies service-level scaling
            settings
        invoker_iam_disabled (bool):
            Optional. Disables IAM permission check for
            run.routes.invoke for callers of this service. For more
            information, visit
            https://cloud.google.com/run/docs/securing/managing-access#invoker_check.
        default_uri_disabled (bool):
            Optional. Disables public resolution of the
            default URI of this service.
        urls (MutableSequence[str]):
            Output only. All URLs serving traffic for
            this Service.
        iap_enabled (bool):
            Optional. IAP settings on the Service.
        multi_region_settings (google.cloud.run_v2.types.Service.MultiRegionSettings):
            Optional. Settings for multi-region
            deployment.
        custom_audiences (MutableSequence[str]):
            One or more custom audiences that you want
            this service to support. Specify each custom
            audience as the full URL in a string. The custom
            audiences are encoded in the token and used to
            authenticate requests. For more information, see
            https://cloud.google.com/run/docs/configuring/custom-audiences.
        observed_generation (int):
            Output only. The generation of this Service currently
            serving traffic. See comments in ``reconciling`` for
            additional information on reconciliation process in Cloud
            Run. Please note that unlike v1, this is an int64 value. As
            with most Google APIs, its JSON representation will be a
            ``string`` instead of an ``integer``.
        terminal_condition (google.cloud.run_v2.types.Condition):
            Output only. The Condition of this Service, containing its
            readiness status, and detailed error information in case it
            did not reach a serving state. See comments in
            ``reconciling`` for additional information on reconciliation
            process in Cloud Run.
        conditions (MutableSequence[google.cloud.run_v2.types.Condition]):
            Output only. The Conditions of all other associated
            sub-resources. They contain additional diagnostics
            information in case the Service does not reach its Serving
            state. See comments in ``reconciling`` for additional
            information on reconciliation process in Cloud Run.
        latest_ready_revision (str):
            Output only. Name of the latest revision that is serving
            traffic. See comments in ``reconciling`` for additional
            information on reconciliation process in Cloud Run.
        latest_created_revision (str):
            Output only. Name of the last created revision. See comments
            in ``reconciling`` for additional information on
            reconciliation process in Cloud Run.
        traffic_statuses (MutableSequence[google.cloud.run_v2.types.TrafficTargetStatus]):
            Output only. Detailed status information for corresponding
            traffic targets. See comments in ``reconciling`` for
            additional information on reconciliation process in Cloud
            Run.
        uri (str):
            Output only. The main URI in which this
            Service is serving traffic.
        satisfies_pzs (bool):
            Output only. Reserved for future use.
        threat_detection_enabled (bool):
            Output only. True if Cloud Run Threat
            Detection monitoring is enabled for the parent
            project of this Service.
        build_config (google.cloud.run_v2.types.BuildConfig):
            Optional. Configuration for building a Cloud
            Run function.
        reconciling (bool):
            Output only. Returns true if the Service is currently being
            acted upon by the system to bring it into the desired state.

            When a new Service is created, or an existing one is
            updated, Cloud Run will asynchronously perform all necessary
            steps to bring the Service to the desired serving state.
            This process is called reconciliation. While reconciliation
            is in process, ``observed_generation``,
            ``latest_ready_revision``, ``traffic_statuses``, and ``uri``
            will have transient values that might mismatch the intended
            state: Once reconciliation is over (and this field is
            false), there are two possible outcomes: reconciliation
            succeeded and the serving state matches the Service, or
            there was an error, and reconciliation failed. This state
            can be found in ``terminal_condition.state``.

            If reconciliation succeeded, the following fields will
            match: ``traffic`` and ``traffic_statuses``,
            ``observed_generation`` and ``generation``,
            ``latest_ready_revision`` and ``latest_created_revision``.

            If reconciliation failed, ``traffic_statuses``,
            ``observed_generation``, and ``latest_ready_revision`` will
            have the state of the last serving revision, or empty for
            newly created Services. Additional information on the
            failure can be found in ``terminal_condition`` and
            ``conditions``.
        etag (str):
            Optional. A system-generated fingerprint for
            this version of the resource. May be used to
            detect modification conflict during updates.
    """

    class MultiRegionSettings(proto.Message):
        r"""Settings for multi-region deployment.

        Attributes:
            regions (MutableSequence[str]):
                Required. List of regions to deploy to,
                including primary region.
            multi_region_id (str):
                Optional. System-generated unique id for the
                multi-region Service.
        """

        regions: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        multi_region_id: str = proto.Field(
            proto.STRING,
            number=2,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=3,
    )
    generation: int = proto.Field(
        proto.INT64,
        number=4,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    delete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    creator: str = proto.Field(
        proto.STRING,
        number=11,
    )
    last_modifier: str = proto.Field(
        proto.STRING,
        number=12,
    )
    client: str = proto.Field(
        proto.STRING,
        number=13,
    )
    client_version: str = proto.Field(
        proto.STRING,
        number=14,
    )
    ingress: vendor_settings.IngressTraffic = proto.Field(
        proto.ENUM,
        number=15,
        enum=vendor_settings.IngressTraffic,
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
    template: revision_template.RevisionTemplate = proto.Field(
        proto.MESSAGE,
        number=18,
        message=revision_template.RevisionTemplate,
    )
    traffic: MutableSequence[traffic_target.TrafficTarget] = proto.RepeatedField(
        proto.MESSAGE,
        number=19,
        message=traffic_target.TrafficTarget,
    )
    scaling: vendor_settings.ServiceScaling = proto.Field(
        proto.MESSAGE,
        number=20,
        message=vendor_settings.ServiceScaling,
    )
    invoker_iam_disabled: bool = proto.Field(
        proto.BOOL,
        number=21,
    )
    default_uri_disabled: bool = proto.Field(
        proto.BOOL,
        number=22,
    )
    urls: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=24,
    )
    iap_enabled: bool = proto.Field(
        proto.BOOL,
        number=25,
    )
    multi_region_settings: MultiRegionSettings = proto.Field(
        proto.MESSAGE,
        number=26,
        message=MultiRegionSettings,
    )
    custom_audiences: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=37,
    )
    observed_generation: int = proto.Field(
        proto.INT64,
        number=30,
    )
    terminal_condition: condition.Condition = proto.Field(
        proto.MESSAGE,
        number=31,
        message=condition.Condition,
    )
    conditions: MutableSequence[condition.Condition] = proto.RepeatedField(
        proto.MESSAGE,
        number=32,
        message=condition.Condition,
    )
    latest_ready_revision: str = proto.Field(
        proto.STRING,
        number=33,
    )
    latest_created_revision: str = proto.Field(
        proto.STRING,
        number=34,
    )
    traffic_statuses: MutableSequence[traffic_target.TrafficTargetStatus] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=35,
            message=traffic_target.TrafficTargetStatus,
        )
    )
    uri: str = proto.Field(
        proto.STRING,
        number=36,
    )
    satisfies_pzs: bool = proto.Field(
        proto.BOOL,
        number=38,
    )
    threat_detection_enabled: bool = proto.Field(
        proto.BOOL,
        number=40,
    )
    build_config: vendor_settings.BuildConfig = proto.Field(
        proto.MESSAGE,
        number=41,
        message=vendor_settings.BuildConfig,
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
