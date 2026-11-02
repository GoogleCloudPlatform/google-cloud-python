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

from google.cloud.service_usage_v1.types import resources

__protobuf__ = proto.module(
    package="google.api.serviceusage.v1",
    manifest={
        "EnableServiceRequest",
        "EnableServiceResponse",
        "DisableServiceRequest",
        "DisableServiceResponse",
        "GetServiceRequest",
        "ListServicesRequest",
        "ListServicesResponse",
        "BatchEnableServicesRequest",
        "BatchEnableServicesResponse",
        "BatchGetServicesRequest",
        "BatchGetServicesResponse",
    },
)


class EnableServiceRequest(proto.Message):
    r"""Request message for the ``EnableService`` method.

    Attributes:
        name (str):
            Name of the consumer and service to enable the service on.

            The ``EnableService`` and ``DisableService`` methods
            currently only support projects.

            Enabling a service requires that the service is public or is
            shared with the user enabling the service.

            An example name would be:
            ``projects/123/services/serviceusage.googleapis.com`` where
            ``123`` is the project number.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class EnableServiceResponse(proto.Message):
    r"""Response message for the ``EnableService`` method. This response
    message is assigned to the ``response`` field of the returned
    Operation when that operation is done.

    Attributes:
        service (google.cloud.service_usage_v1.types.Service):
            The new state of the service after enabling.
    """

    service: resources.Service = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.Service,
    )


class DisableServiceRequest(proto.Message):
    r"""Request message for the ``DisableService`` method.

    Attributes:
        name (str):
            Name of the consumer and service to disable the service on.

            The enable and disable methods currently only support
            projects.

            An example name would be:
            ``projects/123/services/serviceusage.googleapis.com`` where
            ``123`` is the project number.
        disable_dependent_services (bool):
            Indicates if services that are enabled and
            which depend on this service should also be
            disabled. If not set, an error will be generated
            if any enabled services depend on the service to
            be disabled. When set, the service, and any
            enabled services that depend on it, will be
            disabled together.
        check_if_service_has_usage (google.cloud.service_usage_v1.types.DisableServiceRequest.CheckIfServiceHasUsage):
            Defines the behavior for checking service
            usage when disabling a service.
    """

    class CheckIfServiceHasUsage(proto.Enum):
        r"""Enum to determine if service usage should be checked when
        disabling a service.

        Values:
            CHECK_IF_SERVICE_HAS_USAGE_UNSPECIFIED (0):
                When unset, the default behavior is used,
                which is SKIP.
            SKIP (1):
                If set, skip checking service usage when
                disabling a service.
            CHECK (2):
                If set, service usage is checked when disabling the service.
                If a service, or its dependents, has usage in the last 30
                days, the request returns a FAILED_PRECONDITION error.
        """

        CHECK_IF_SERVICE_HAS_USAGE_UNSPECIFIED = 0
        SKIP = 1
        CHECK = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    disable_dependent_services: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    check_if_service_has_usage: CheckIfServiceHasUsage = proto.Field(
        proto.ENUM,
        number=3,
        enum=CheckIfServiceHasUsage,
    )


class DisableServiceResponse(proto.Message):
    r"""Response message for the ``DisableService`` method. This response
    message is assigned to the ``response`` field of the returned
    Operation when that operation is done.

    Attributes:
        service (google.cloud.service_usage_v1.types.Service):
            The new state of the service after disabling.
    """

    service: resources.Service = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.Service,
    )


class GetServiceRequest(proto.Message):
    r"""Request message for the ``GetService`` method.

    Attributes:
        name (str):
            Name of the consumer and service to get the
            ``ConsumerState`` for.

            An example name would be:
            ``projects/123/services/serviceusage.googleapis.com`` where
            ``123`` is the project number.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListServicesRequest(proto.Message):
    r"""Request message for the ``ListServices`` method.

    Attributes:
        parent (str):
            Parent to search for services on.

            An example name would be: ``projects/123`` where ``123`` is
            the project number.
        page_size (int):
            Requested size of the next page of data.
            Requested page size cannot exceed 200.
            If not set, the default page size is 50.
        page_token (str):
            Token identifying which result to start with,
            which is returned by a previous list call.
        filter (str):
            Only list services that conform to the given filter. The
            allowed filter strings are ``state:ENABLED`` and
            ``state:DISABLED``.
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
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListServicesResponse(proto.Message):
    r"""Response message for the ``ListServices`` method.

    Attributes:
        services (MutableSequence[google.cloud.service_usage_v1.types.Service]):
            The available services for the requested
            project.
        next_page_token (str):
            Token that can be passed to ``ListServices`` to resume a
            paginated query.
    """

    @property
    def raw_page(self):
        return self

    services: MutableSequence[resources.Service] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Service,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class BatchEnableServicesRequest(proto.Message):
    r"""Request message for the ``BatchEnableServices`` method.

    Attributes:
        parent (str):
            Parent to enable services on.

            An example name would be: ``projects/123`` where ``123`` is
            the project number.

            The ``BatchEnableServices`` method currently only supports
            projects.
        service_ids (MutableSequence[str]):
            The identifiers of the services to enable on
            the project.
            A valid identifier would be:

            serviceusage.googleapis.com

            Enabling services requires that each service is
            public or is shared with the user enabling the
            service.

            A single request can enable a maximum of 20
            services at a time. If more than 20 services are
            specified, the request will fail, and no state
            changes will occur.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    service_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchEnableServicesResponse(proto.Message):
    r"""Response message for the ``BatchEnableServices`` method. This
    response message is assigned to the ``response`` field of the
    returned Operation when that operation is done.

    Attributes:
        services (MutableSequence[google.cloud.service_usage_v1.types.Service]):
            The new state of the services after enabling.
        failures (MutableSequence[google.cloud.service_usage_v1.types.BatchEnableServicesResponse.EnableFailure]):
            If allow_partial_success is true, and one or more services
            could not be enabled, this field contains the details about
            each failure.
    """

    class EnableFailure(proto.Message):
        r"""Provides error messages for the failing services.

        Attributes:
            service_id (str):
                The service id of a service that could not be
                enabled.
            error_message (str):
                An error message describing why the service
                could not be enabled.
        """

        service_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        error_message: str = proto.Field(
            proto.STRING,
            number=2,
        )

    services: MutableSequence[resources.Service] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Service,
    )
    failures: MutableSequence[EnableFailure] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=EnableFailure,
    )


class BatchGetServicesRequest(proto.Message):
    r"""Request message for the ``BatchGetServices`` method.

    Attributes:
        parent (str):
            Parent to retrieve services from. If this is set, the parent
            of all of the services specified in ``names`` must match
            this field. An example name would be: ``projects/123`` where
            ``123`` is the project number. The ``BatchGetServices``
            method currently only supports projects.
        names (MutableSequence[str]):
            Names of the services to retrieve.

            An example name would be:
            ``projects/123/services/serviceusage.googleapis.com`` where
            ``123`` is the project number. A single request can get a
            maximum of 30 services at a time.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchGetServicesResponse(proto.Message):
    r"""Response message for the ``BatchGetServices`` method.

    Attributes:
        services (MutableSequence[google.cloud.service_usage_v1.types.Service]):
            The requested Service states.
    """

    services: MutableSequence[resources.Service] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Service,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
