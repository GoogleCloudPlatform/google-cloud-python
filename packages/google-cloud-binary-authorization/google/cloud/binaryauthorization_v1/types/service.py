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

import grafeas.grafeas_v1.types  # type: ignore
import proto  # type: ignore

from google.cloud.binaryauthorization_v1.types import resources

__protobuf__ = proto.module(
    package="google.cloud.binaryauthorization.v1",
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
        "ValidateAttestationOccurrenceRequest",
        "ValidateAttestationOccurrenceResponse",
    },
)


class GetPolicyRequest(proto.Message):
    r"""Request message for
    [BinauthzManagementServiceV1.GetPolicy][google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.GetPolicy].

    Attributes:
        name (str):
            Required. The resource name of the
            [policy][google.cloud.binaryauthorization.v1.Policy] to
            retrieve, in the format ``projects/*/policy``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdatePolicyRequest(proto.Message):
    r"""Request message for
    [BinauthzManagementServiceV1.UpdatePolicy][google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.UpdatePolicy].

    Attributes:
        policy (google.cloud.binaryauthorization_v1.types.Policy):
            Required. A new or updated
            [policy][google.cloud.binaryauthorization.v1.Policy] value.
            The service will overwrite the [policy
            name][google.cloud.binaryauthorization.v1.Policy.name] field
            with the resource name in the request URL, in the format
            ``projects/*/policy``.
    """

    policy: resources.Policy = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.Policy,
    )


class CreateAttestorRequest(proto.Message):
    r"""Request message for
    [BinauthzManagementServiceV1.CreateAttestor][google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.CreateAttestor].

    Attributes:
        parent (str):
            Required. The parent of this
            [attestor][google.cloud.binaryauthorization.v1.Attestor].
        attestor_id (str):
            Required. The
            [attestors][google.cloud.binaryauthorization.v1.Attestor]
            ID.
        attestor (google.cloud.binaryauthorization_v1.types.Attestor):
            Required. The initial
            [attestor][google.cloud.binaryauthorization.v1.Attestor]
            value. The service will overwrite the [attestor
            name][google.cloud.binaryauthorization.v1.Attestor.name]
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
    r"""Request message for
    [BinauthzManagementServiceV1.GetAttestor][google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.GetAttestor].

    Attributes:
        name (str):
            Required. The name of the
            [attestor][google.cloud.binaryauthorization.v1.Attestor] to
            retrieve, in the format ``projects/*/attestors/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateAttestorRequest(proto.Message):
    r"""Request message for
    [BinauthzManagementServiceV1.UpdateAttestor][google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.UpdateAttestor].

    Attributes:
        attestor (google.cloud.binaryauthorization_v1.types.Attestor):
            Required. The updated
            [attestor][google.cloud.binaryauthorization.v1.Attestor]
            value. The service will overwrite the [attestor
            name][google.cloud.binaryauthorization.v1.Attestor.name]
            field with the resource name in the request URL, in the
            format ``projects/*/attestors/*``.
    """

    attestor: resources.Attestor = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.Attestor,
    )


class ListAttestorsRequest(proto.Message):
    r"""Request message for
    [BinauthzManagementServiceV1.ListAttestors][google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.ListAttestors].

    Attributes:
        parent (str):
            Required. The resource name of the project associated with
            the
            [attestors][google.cloud.binaryauthorization.v1.Attestor],
            in the format ``projects/*``.
        page_size (int):
            Requested page size. The server may return
            fewer results than requested. If unspecified,
            the server will pick an appropriate default.
        page_token (str):
            A token identifying a page of results the server should
            return. Typically, this is the value of
            [ListAttestorsResponse.next_page_token][google.cloud.binaryauthorization.v1.ListAttestorsResponse.next_page_token]
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
    r"""Response message for
    [BinauthzManagementServiceV1.ListAttestors][google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.ListAttestors].

    Attributes:
        attestors (MutableSequence[google.cloud.binaryauthorization_v1.types.Attestor]):
            The list of
            [attestors][google.cloud.binaryauthorization.v1.Attestor].
        next_page_token (str):
            A token to retrieve the next page of results. Pass this
            value in the
            [ListAttestorsRequest.page_token][google.cloud.binaryauthorization.v1.ListAttestorsRequest.page_token]
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
    r"""Request message for
    [BinauthzManagementServiceV1.DeleteAttestor][google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.DeleteAttestor].

    Attributes:
        name (str):
            Required. The name of the
            [attestors][google.cloud.binaryauthorization.v1.Attestor] to
            delete, in the format ``projects/*/attestors/*``.
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


class ValidateAttestationOccurrenceRequest(proto.Message):
    r"""Request message for
    [ValidationHelperV1.ValidateAttestationOccurrence][google.cloud.binaryauthorization.v1.ValidationHelperV1.ValidateAttestationOccurrence].

    Attributes:
        attestor (str):
            Required. The resource name of the
            [Attestor][google.cloud.binaryauthorization.v1.Attestor] of
            the [occurrence][grafeas.v1.Occurrence], in the format
            ``projects/*/attestors/*``.
        attestation (grafeas.grafeas_v1.types.AttestationOccurrence):
            Required. An
            [AttestationOccurrence][grafeas.v1.AttestationOccurrence] to
            be checked that it can be verified by the ``Attestor``. It
            does not have to be an existing entity in Container
            Analysis. It must otherwise be a valid
            ``AttestationOccurrence``.
        occurrence_note (str):
            Required. The resource name of the [Note][grafeas.v1.Note]
            to which the containing [Occurrence][grafeas.v1.Occurrence]
            is associated.
        occurrence_resource_uri (str):
            Required. The URI of the artifact (e.g. container image)
            that is the subject of the containing
            [Occurrence][grafeas.v1.Occurrence].
    """

    attestor: str = proto.Field(
        proto.STRING,
        number=1,
    )
    attestation: grafeas.grafeas_v1.types.AttestationOccurrence = proto.Field(
        proto.MESSAGE,
        number=2,
        message=grafeas.grafeas_v1.types.AttestationOccurrence,
    )
    occurrence_note: str = proto.Field(
        proto.STRING,
        number=3,
    )
    occurrence_resource_uri: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ValidateAttestationOccurrenceResponse(proto.Message):
    r"""Response message for
    [ValidationHelperV1.ValidateAttestationOccurrence][google.cloud.binaryauthorization.v1.ValidationHelperV1.ValidateAttestationOccurrence].

    Attributes:
        result (google.cloud.binaryauthorization_v1.types.ValidateAttestationOccurrenceResponse.Result):
            The result of the Attestation validation.
        denial_reason (str):
            The reason for denial if the Attestation
            couldn't be validated.
    """

    class Result(proto.Enum):
        r"""The enum returned in the ``result`` field.

        Values:
            RESULT_UNSPECIFIED (0):
                Unspecified.
            VERIFIED (1):
                The Attestation was able to verified by the
                Attestor.
            ATTESTATION_NOT_VERIFIABLE (2):
                The Attestation was not able to verified by
                the Attestor.
        """

        RESULT_UNSPECIFIED = 0
        VERIFIED = 1
        ATTESTATION_NOT_VERIFIABLE = 2

    result: Result = proto.Field(
        proto.ENUM,
        number=1,
        enum=Result,
    )
    denial_reason: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
