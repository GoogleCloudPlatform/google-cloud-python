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

import google.api.service_pb2 as service_pb2  # type: ignore
import google.protobuf.any_pb2 as any_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.servicemanagement_v1.types import resources

__protobuf__ = proto.module(
    package="google.api.servicemanagement.v1",
    manifest={
        "ListServicesRequest",
        "ListServicesResponse",
        "GetServiceRequest",
        "CreateServiceRequest",
        "DeleteServiceRequest",
        "UndeleteServiceRequest",
        "UndeleteServiceResponse",
        "GetServiceConfigRequest",
        "ListServiceConfigsRequest",
        "ListServiceConfigsResponse",
        "CreateServiceConfigRequest",
        "SubmitConfigSourceRequest",
        "SubmitConfigSourceResponse",
        "CreateServiceRolloutRequest",
        "ListServiceRolloutsRequest",
        "ListServiceRolloutsResponse",
        "GetServiceRolloutRequest",
        "EnableServiceResponse",
        "GenerateConfigReportRequest",
        "GenerateConfigReportResponse",
    },
)


class ListServicesRequest(proto.Message):
    r"""Request message for ``ListServices`` method.

    Attributes:
        producer_project_id (str):
            Include services produced by the specified
            project.
        page_size (int):
            The max number of items to include in the
            response list. Page size is 50 if not specified.
            Maximum value is 500.
        page_token (str):
            Token identifying which result to start with;
            returned by a previous list call.
        consumer_id (str):
            Include services consumed by the specified consumer.

            The Google Service Management implementation accepts the
            following forms:

            - project:<project_id>
    """

    producer_project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=5,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=6,
    )
    consumer_id: str = proto.Field(
        proto.STRING,
        number=7,
    )


class ListServicesResponse(proto.Message):
    r"""Response message for ``ListServices`` method.

    Attributes:
        services (MutableSequence[google.cloud.servicemanagement_v1.types.ManagedService]):
            The returned services will only have the name
            field set.
        next_page_token (str):
            Token that can be passed to ``ListServices`` to resume a
            paginated query.
    """

    @property
    def raw_page(self):
        return self

    services: MutableSequence[resources.ManagedService] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.ManagedService,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetServiceRequest(proto.Message):
    r"""Request message for ``GetService`` method.

    Attributes:
        service_name (str):
            Required. The name of the service. See the
            ``ServiceManager`` overview for naming requirements. For
            example: ``example.googleapis.com``.
    """

    service_name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateServiceRequest(proto.Message):
    r"""Request message for CreateService method.

    Attributes:
        service (google.cloud.servicemanagement_v1.types.ManagedService):
            Required. Initial values for the service
            resource.
    """

    service: resources.ManagedService = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.ManagedService,
    )


class DeleteServiceRequest(proto.Message):
    r"""Request message for DeleteService method.

    Attributes:
        service_name (str):
            Required. The name of the service. See the
            `overview <https://cloud.google.com/service-management/overview>`__
            for naming requirements. For example:
            ``example.googleapis.com``.
    """

    service_name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UndeleteServiceRequest(proto.Message):
    r"""Request message for UndeleteService method.

    Attributes:
        service_name (str):
            Required. The name of the service. See the
            `overview <https://cloud.google.com/service-management/overview>`__
            for naming requirements. For example:
            ``example.googleapis.com``.
    """

    service_name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UndeleteServiceResponse(proto.Message):
    r"""Response message for UndeleteService method.

    Attributes:
        service (google.cloud.servicemanagement_v1.types.ManagedService):
            Revived service resource.
    """

    service: resources.ManagedService = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.ManagedService,
    )


class GetServiceConfigRequest(proto.Message):
    r"""Request message for GetServiceConfig method.

    Attributes:
        service_name (str):
            Required. The name of the service. See the
            `overview <https://cloud.google.com/service-management/overview>`__
            for naming requirements. For example:
            ``example.googleapis.com``.
        config_id (str):
            Required. The id of the service configuration resource.

            This field must be specified for the server to return all
            fields, including ``SourceInfo``.
        view (google.cloud.servicemanagement_v1.types.GetServiceConfigRequest.ConfigView):
            Specifies which parts of the Service Config
            should be returned in the response.
    """

    class ConfigView(proto.Enum):
        r"""

        Values:
            BASIC (0):
                Server response includes all fields except
                SourceInfo.
            FULL (1):
                Server response includes all fields including
                SourceInfo. SourceFiles are of type
                'google.api.servicemanagement.v1.ConfigFile' and
                are only available for configs created using the
                SubmitConfigSource method.
        """

        BASIC = 0
        FULL = 1

    service_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    config_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    view: ConfigView = proto.Field(
        proto.ENUM,
        number=3,
        enum=ConfigView,
    )


class ListServiceConfigsRequest(proto.Message):
    r"""Request message for ListServiceConfigs method.

    Attributes:
        service_name (str):
            Required. The name of the service. See the
            `overview <https://cloud.google.com/service-management/overview>`__
            for naming requirements. For example:
            ``example.googleapis.com``.
        page_token (str):
            The token of the page to retrieve.
        page_size (int):
            The max number of items to include in the
            response list. Page size is 50 if not specified.
            Maximum value is 100.
    """

    service_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class ListServiceConfigsResponse(proto.Message):
    r"""Response message for ListServiceConfigs method.

    Attributes:
        service_configs (MutableSequence[google.api.service_pb2.Service]):
            The list of service configuration resources.
        next_page_token (str):
            The token of the next page of results.
    """

    @property
    def raw_page(self):
        return self

    service_configs: MutableSequence[service_pb2.Service] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=service_pb2.Service,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateServiceConfigRequest(proto.Message):
    r"""Request message for CreateServiceConfig method.

    Attributes:
        service_name (str):
            Required. The name of the service. See the
            `overview <https://cloud.google.com/service-management/overview>`__
            for naming requirements. For example:
            ``example.googleapis.com``.
        service_config (google.api.service_pb2.Service):
            Required. The service configuration resource.
    """

    service_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    service_config: service_pb2.Service = proto.Field(
        proto.MESSAGE,
        number=2,
        message=service_pb2.Service,
    )


class SubmitConfigSourceRequest(proto.Message):
    r"""Request message for SubmitConfigSource method.

    Attributes:
        service_name (str):
            Required. The name of the service. See the
            `overview <https://cloud.google.com/service-management/overview>`__
            for naming requirements. For example:
            ``example.googleapis.com``.
        config_source (google.cloud.servicemanagement_v1.types.ConfigSource):
            Required. The source configuration for the
            service.
        validate_only (bool):
            Optional. If set, this will result in the generation of a
            ``google.api.Service`` configuration based on the
            ``ConfigSource`` provided, but the generated config and the
            sources will NOT be persisted.
    """

    service_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    config_source: resources.ConfigSource = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.ConfigSource,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class SubmitConfigSourceResponse(proto.Message):
    r"""Response message for SubmitConfigSource method.

    Attributes:
        service_config (google.api.service_pb2.Service):
            The generated service configuration.
    """

    service_config: service_pb2.Service = proto.Field(
        proto.MESSAGE,
        number=1,
        message=service_pb2.Service,
    )


class CreateServiceRolloutRequest(proto.Message):
    r"""Request message for 'CreateServiceRollout'

    Attributes:
        service_name (str):
            Required. The name of the service. See the
            `overview <https://cloud.google.com/service-management/overview>`__
            for naming requirements. For example:
            ``example.googleapis.com``.
        rollout (google.cloud.servicemanagement_v1.types.Rollout):
            Required. The rollout resource. The ``service_name`` field
            is output only.
    """

    service_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    rollout: resources.Rollout = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.Rollout,
    )


class ListServiceRolloutsRequest(proto.Message):
    r"""Request message for 'ListServiceRollouts'

    Attributes:
        service_name (str):
            Required. The name of the service. See the
            `overview <https://cloud.google.com/service-management/overview>`__
            for naming requirements. For example:
            ``example.googleapis.com``.
        page_token (str):
            The token of the page to retrieve.
        page_size (int):
            The max number of items to include in the
            response list. Page size is 50 if not specified.
            Maximum value is 100.
        filter (str):
            Required. Use ``filter`` to return subset of rollouts. The
            following filters are supported:

            -- By [status]
            [google.api.servicemanagement.v1.Rollout.RolloutStatus]. For
            example, ``filter='status=SUCCESS'``

            -- By [strategy]
            [google.api.servicemanagement.v1.Rollout.strategy]. For
            example, ``filter='strategy=TrafficPercentStrategy'``
    """

    service_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListServiceRolloutsResponse(proto.Message):
    r"""Response message for ListServiceRollouts method.

    Attributes:
        rollouts (MutableSequence[google.cloud.servicemanagement_v1.types.Rollout]):
            The list of rollout resources.
        next_page_token (str):
            The token of the next page of results.
    """

    @property
    def raw_page(self):
        return self

    rollouts: MutableSequence[resources.Rollout] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Rollout,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetServiceRolloutRequest(proto.Message):
    r"""Request message for GetServiceRollout method.

    Attributes:
        service_name (str):
            Required. The name of the service. See the
            `overview <https://cloud.google.com/service-management/overview>`__
            for naming requirements. For example:
            ``example.googleapis.com``.
        rollout_id (str):
            Required. The id of the rollout resource.
    """

    service_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    rollout_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class EnableServiceResponse(proto.Message):
    r"""Operation payload for EnableService method."""


class GenerateConfigReportRequest(proto.Message):
    r"""Request message for GenerateConfigReport method.

    Attributes:
        new_config (google.protobuf.any_pb2.Any):
            Required. Service configuration for which we want to
            generate the report. For this version of API, the supported
            types are
            [google.api.servicemanagement.v1.ConfigRef][google.api.servicemanagement.v1.ConfigRef],
            [google.api.servicemanagement.v1.ConfigSource][google.api.servicemanagement.v1.ConfigSource],
            and [google.api.Service][google.api.Service]
        old_config (google.protobuf.any_pb2.Any):
            Optional. Service configuration against which the comparison
            will be done. For this version of API, the supported types
            are
            [google.api.servicemanagement.v1.ConfigRef][google.api.servicemanagement.v1.ConfigRef],
            [google.api.servicemanagement.v1.ConfigSource][google.api.servicemanagement.v1.ConfigSource],
            and [google.api.Service][google.api.Service]
    """

    new_config: any_pb2.Any = proto.Field(
        proto.MESSAGE,
        number=1,
        message=any_pb2.Any,
    )
    old_config: any_pb2.Any = proto.Field(
        proto.MESSAGE,
        number=2,
        message=any_pb2.Any,
    )


class GenerateConfigReportResponse(proto.Message):
    r"""Response message for GenerateConfigReport method.

    Attributes:
        service_name (str):
            Name of the service this report belongs to.
        id (str):
            ID of the service configuration this report
            belongs to.
        change_reports (MutableSequence[google.cloud.servicemanagement_v1.types.ChangeReport]):
            list of ChangeReport, each corresponding to
            comparison between two service configurations.
        diagnostics (MutableSequence[google.cloud.servicemanagement_v1.types.Diagnostic]):
            Errors / Linter warnings associated with the
            service definition this report
            belongs to.
    """

    service_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    change_reports: MutableSequence[resources.ChangeReport] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=resources.ChangeReport,
    )
    diagnostics: MutableSequence[resources.Diagnostic] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=resources.Diagnostic,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
