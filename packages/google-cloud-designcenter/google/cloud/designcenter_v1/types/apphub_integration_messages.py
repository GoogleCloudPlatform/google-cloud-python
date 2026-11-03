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

from google.cloud.designcenter_v1.types import apphub_integration

__protobuf__ = proto.module(
    package="google.cloud.designcenter.v1",
    manifest={
        "RegisterAppHubApplicationResourcesRequest",
        "RegisterAppHubApplicationResourcesResponse",
        "DeployedResourceResponse",
    },
)


class RegisterAppHubApplicationResourcesRequest(proto.Message):
    r"""Request message for RegisterAppHubApplicationResources
    method.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        tfstate_content (str):
            Optional. The Terraform state (tfstate) content as a raw
            string. For large state files exceeding 10MB, use the
            'tfstate_signed_gcs_uri' field instead.

            This field is a member of `oneof`_ ``tfstate_source``.
        tfstate_signed_gcs_uri (str):
            Optional. A securely signed Cloud Storage URI
            pointing to the tfstate file. The URI must be
            signed to grant the service temporary read
            access to the state file. Application Design
            Center imposes a limit on the maximum size of
            the state file accessed via this URI.

            This field is a member of `oneof`_ ``tfstate_source``.
        parent (str):
            Required. The parent location.
            Format: projects/{project}/locations/{location}
        apphub_application (str):
            Required. The name of the AppHub Application.
            Format:

            projects/{project}/locations/{location}/applications/{application}
    """

    tfstate_content: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="tfstate_source",
    )
    tfstate_signed_gcs_uri: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="tfstate_source",
    )
    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    apphub_application: str = proto.Field(
        proto.STRING,
        number=4,
    )


class RegisterAppHubApplicationResourcesResponse(proto.Message):
    r"""Response message for RegisterAppHubApplicationResources
    method.

    Attributes:
        response (google.cloud.designcenter_v1.types.DeployedResourceResponse):
            The response for the registration of deployed
            resources of a given AppHub application.
    """

    response: "DeployedResourceResponse" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="DeployedResourceResponse",
    )


class DeployedResourceResponse(proto.Message):
    r"""Common response message for the resource registration
    methods.

    Attributes:
        apphub_application (str):
            The App Hub application name.
        registered_resources (MutableSequence[str]):
            The list of successfully registered GCP
            resources.
        unregistered_resources (MutableSequence[google.cloud.designcenter_v1.types.UnregisteredResource]):
            The list of unregistered GCP resources with
            error details.
    """

    apphub_application: str = proto.Field(
        proto.STRING,
        number=1,
    )
    registered_resources: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    unregistered_resources: MutableSequence[apphub_integration.UnregisteredResource] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message=apphub_integration.UnregisteredResource,
        )
    )


__all__ = tuple(sorted(__protobuf__.manifest))
