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

from google.cloud.binaryauthorization_v1beta1.types import resources

__protobuf__ = proto.module(
    package="google.cloud.binaryauthorization.v1beta1",
    manifest={
        "GetPolicyRequest",
        "UpdatePolicyRequest",
        "CreateAttestorRequest",
        "GetAttestorRequest",
        "UpdateAttestorRequest",
        "ListAttestorsRequest",
        "ListAttestorsResponse",
        "DeleteAttestorRequest",
        "GetSystemPolicyRequest",
    },
)


class GetPolicyRequest(proto.Message):
    r"""Request message for [BinauthzManagementService.GetPolicy][].

    Attributes:
        name (str):
            Required. The resource name of the
            [policy][google.cloud.binaryauthorization.v1beta1.Policy] to
            retrieve, in the format ``projects/*/policy``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdatePolicyRequest(proto.Message):
    r"""Request message for [BinauthzManagementService.UpdatePolicy][].

    Attributes:
        policy (google.cloud.binaryauthorization_v1beta1.types.Policy):
            Required. A new or updated
            [policy][google.cloud.binaryauthorization.v1beta1.Policy]
            value. The service will overwrite the [policy
            name][google.cloud.binaryauthorization.v1beta1.Policy.name]
            field with the resource name in the request URL, in the
            format ``projects/*/policy``.
    """

    policy: resources.Policy = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.Policy,
    )


class CreateAttestorRequest(proto.Message):
    r"""Request message for [BinauthzManagementService.CreateAttestor][].

    Attributes:
        parent (str):
            Required. The parent of this
            [attestor][google.cloud.binaryauthorization.v1beta1.Attestor].
        attestor_id (str):
            Required. The
            [attestors][google.cloud.binaryauthorization.v1beta1.Attestor]
            ID.
        attestor (google.cloud.binaryauthorization_v1beta1.types.Attestor):
            Required. The initial
            [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]
            value. The service will overwrite the [attestor
            name][google.cloud.binaryauthorization.v1beta1.Attestor.name]
            field with the resource name, in the format
            ``projects/*/attestors/*``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    attestor_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    attestor: resources.Attestor = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.Attestor,
    )


class GetAttestorRequest(proto.Message):
    r"""Request message for [BinauthzManagementService.GetAttestor][].

    Attributes:
        name (str):
            Required. The name of the
            [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]
            to retrieve, in the format ``projects/*/attestors/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateAttestorRequest(proto.Message):
    r"""Request message for [BinauthzManagementService.UpdateAttestor][].

    Attributes:
        attestor (google.cloud.binaryauthorization_v1beta1.types.Attestor):
            Required. The updated
            [attestor][google.cloud.binaryauthorization.v1beta1.Attestor]
            value. The service will overwrite the [attestor
            name][google.cloud.binaryauthorization.v1beta1.Attestor.name]
            field with the resource name in the request URL, in the
            format ``projects/*/attestors/*``.
    """

    attestor: resources.Attestor = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.Attestor,
    )


class ListAttestorsRequest(proto.Message):
    r"""Request message for [BinauthzManagementService.ListAttestors][].

    Attributes:
        parent (str):
            Required. The resource name of the project associated with
            the
            [attestors][google.cloud.binaryauthorization.v1beta1.Attestor],
            in the format ``projects/*``.
        page_size (int):
            Requested page size. The server may return
            fewer results than requested. If unspecified,
            the server will pick an appropriate default.
        page_token (str):
            A token identifying a page of results the server should
            return. Typically, this is the value of
            [ListAttestorsResponse.next_page_token][google.cloud.binaryauthorization.v1beta1.ListAttestorsResponse.next_page_token]
            returned from the previous call to the ``ListAttestors``
            method.
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


class ListAttestorsResponse(proto.Message):
    r"""Response message for [BinauthzManagementService.ListAttestors][].

    Attributes:
        attestors (MutableSequence[google.cloud.binaryauthorization_v1beta1.types.Attestor]):
            The list of
            [attestors][google.cloud.binaryauthorization.v1beta1.Attestor].
        next_page_token (str):
            A token to retrieve the next page of results. Pass this
            value in the
            [ListAttestorsRequest.page_token][google.cloud.binaryauthorization.v1beta1.ListAttestorsRequest.page_token]
            field in the subsequent call to the ``ListAttestors`` method
            to retrieve the next page of results.
    """

    @property
    def raw_page(self):
        return self

    attestors: MutableSequence[resources.Attestor] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Attestor,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteAttestorRequest(proto.Message):
    r"""Request message for [BinauthzManagementService.DeleteAttestor][].

    Attributes:
        name (str):
            Required. The name of the
            [attestors][google.cloud.binaryauthorization.v1beta1.Attestor]
            to delete, in the format ``projects/*/attestors/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetSystemPolicyRequest(proto.Message):
    r"""Request to read the current system policy.

    Attributes:
        name (str):
            Required. The resource name, in the format
            ``locations/*/policy``. Note that the system policy is not
            associated with a project.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
