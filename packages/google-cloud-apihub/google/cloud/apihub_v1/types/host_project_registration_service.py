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
    package="google.cloud.apihub.v1",
    manifest={
        "CreateHostProjectRegistrationRequest",
        "GetHostProjectRegistrationRequest",
        "ListHostProjectRegistrationsRequest",
        "ListHostProjectRegistrationsResponse",
        "HostProjectRegistration",
    },
)


class CreateHostProjectRegistrationRequest(proto.Message):
    r"""The
    [CreateHostProjectRegistration][google.cloud.apihub.v1.HostProjectRegistrationService.CreateHostProjectRegistration]
    method's request.

    Attributes:
        parent (str):
            Required. The parent resource for the host project. Format:
            ``projects/{project}/locations/{location}``
        host_project_registration_id (str):
            Required. The ID to use for the Host Project Registration,
            which will become the final component of the host project
            registration's resource name. The ID must be the same as the
            Google cloud project specified in the
            host_project_registration.gcp_project field.
        host_project_registration (google.cloud.apihub_v1.types.HostProjectRegistration):
            Required. The host project registration to
            register.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    host_project_registration_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    host_project_registration: "HostProjectRegistration" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="HostProjectRegistration",
    )


class GetHostProjectRegistrationRequest(proto.Message):
    r"""The
    [GetHostProjectRegistration][google.cloud.apihub.v1.HostProjectRegistrationService.GetHostProjectRegistration]
    method's request.

    Attributes:
        name (str):
            Required. Host project registration resource name.
            projects/{project}/locations/{location}/hostProjectRegistrations/{host_project_registration_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListHostProjectRegistrationsRequest(proto.Message):
    r"""The
    [ListHostProjectRegistrations][google.cloud.apihub.v1.HostProjectRegistrationService.ListHostProjectRegistrations]
    method's request.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of host
            projects. Format: ``projects/*/locations/*``
        page_size (int):
            Optional. The maximum number of host project
            registrations to return. The service may return
            fewer than this value. If unspecified, at most
            50 host project registrations will be returned.
            The maximum value is 1000; values above 1000
            will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListHostProjectRegistrations`` call. Provide this to
            retrieve the subsequent page.

            When paginating, all other parameters (except page_size)
            provided to ``ListHostProjectRegistrations`` must match the
            call that provided the page token.
        filter (str):
            Optional. An expression that filters the list of
            HostProjectRegistrations.

            A filter expression consists of a field name, a comparison
            operator, and a value for filtering. The value must be a
            string. All standard operators as documented at
            https://google.aip.dev/160 are supported.

            The following fields in the ``HostProjectRegistration`` are
            eligible for filtering:

            - ``name`` - The name of the HostProjectRegistration.
            - ``create_time`` - The time at which the
              HostProjectRegistration was created. The value should be
              in the (RFC3339)[https://tools.ietf.org/html/rfc3339]
              format.
            - ``gcp_project`` - The Google cloud project associated with
              the HostProjectRegistration.
        order_by (str):
            Optional. Hint for how to order the results.
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
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListHostProjectRegistrationsResponse(proto.Message):
    r"""The
    [ListHostProjectRegistrations][google.cloud.apihub.v1.HostProjectRegistrationService.ListHostProjectRegistrations]
    method's response.

    Attributes:
        host_project_registrations (MutableSequence[google.cloud.apihub_v1.types.HostProjectRegistration]):
            The list of host project registrations.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    host_project_registrations: MutableSequence["HostProjectRegistration"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="HostProjectRegistration",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class HostProjectRegistration(proto.Message):
    r"""Host project registration refers to the registration of a
    Google cloud project with Api Hub as a host project. This is the
    project where Api Hub is provisioned. It acts as the consumer
    project for the Api Hub instance provisioned. Multiple runtime
    projects can be attached to the host project and these
    attachments define the scope of Api Hub.

    Attributes:
        name (str):
            Identifier. The name of the host project registration.
            Format:
            "projects/{project}/locations/{location}/hostProjectRegistrations/{host_project_registration}".
        gcp_project (str):
            Required. Immutable. Google cloud project
            name in the format: "projects/abc" or
            "projects/123". As input, project name with
            either project id or number are accepted. As
            output, this field will contain project number.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the host
            project registration was created.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    gcp_project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
