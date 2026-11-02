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

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.managedidentities_v1.types import resource

__protobuf__ = proto.module(
    package="google.cloud.managedidentities.v1",
    manifest={
        "OpMetadata",
        "CreateMicrosoftAdDomainRequest",
        "ResetAdminPasswordRequest",
        "ResetAdminPasswordResponse",
        "ListDomainsRequest",
        "ListDomainsResponse",
        "GetDomainRequest",
        "UpdateDomainRequest",
        "DeleteDomainRequest",
        "AttachTrustRequest",
        "ReconfigureTrustRequest",
        "DetachTrustRequest",
        "ValidateTrustRequest",
    },
)


class OpMetadata(proto.Message):
    r"""Represents the metadata of the long-running operation.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        target (str):
            Output only. Server-defined resource path for
            the target of the operation.
        verb (str):
            Output only. Name of the verb executed by the
            operation.
        requested_cancellation (bool):
            Output only. Identifies whether the user has requested
            cancellation of the operation. Operations that have
            successfully been cancelled have [Operation.error][] value
            with a [google.rpc.Status.code][google.rpc.Status.code] of
            1, corresponding to ``Code.CANCELLED``.
        api_version (str):
            Output only. API version used to start the
            operation.
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    target: str = proto.Field(
        proto.STRING,
        number=3,
    )
    verb: str = proto.Field(
        proto.STRING,
        number=4,
    )
    requested_cancellation: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    api_version: str = proto.Field(
        proto.STRING,
        number=6,
    )


class CreateMicrosoftAdDomainRequest(proto.Message):
    r"""Request message for
    [CreateMicrosoftAdDomain][google.cloud.managedidentities.v1.CreateMicrosoftAdDomain]

    Attributes:
        parent (str):
            Required. The resource project name and location using the
            form: ``projects/{project_id}/locations/global``
        domain_name (str):
            Required. The fully qualified domain name. e.g.
            mydomain.myorganization.com, with the following
            restrictions:

            - Must contain only lowercase letters, numbers, periods and
              hyphens.
            - Must start with a letter.
            - Must contain between 2-64 characters.
            - Must end with a number or a letter.
            - Must not start with period.
            - First segement length (mydomain form example above)
              shouldn't exceed 15 chars.
            - The last segment cannot be fully numeric.
            - Must be unique within the customer project.
        domain (google.cloud.managedidentities_v1.types.Domain):
            Required. A Managed Identity domain resource.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    domain_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    domain: resource.Domain = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resource.Domain,
    )


class ResetAdminPasswordRequest(proto.Message):
    r"""Request message for
    [ResetAdminPassword][google.cloud.managedidentities.v1.ResetAdminPassword]

    Attributes:
        name (str):
            Required. The domain resource name using the form:
            ``projects/{project_id}/locations/global/domains/{domain_name}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ResetAdminPasswordResponse(proto.Message):
    r"""Response message for
    [ResetAdminPassword][google.cloud.managedidentities.v1.ResetAdminPassword]

    Attributes:
        password (str):
            A random password. See
            [admin][google.cloud.managedidentities.v1.Domain.admin] for
            more information.
    """

    password: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListDomainsRequest(proto.Message):
    r"""Request message for
    [ListDomains][google.cloud.managedidentities.v1.ListDomains]

    Attributes:
        parent (str):
            Required. The resource name of the domain location using the
            form: ``projects/{project_id}/locations/global``
        page_size (int):
            Optional. The maximum number of items to return. If not
            specified, a default value of 1000 will be used. Regardless
            of the page_size value, the response may include a partial
            list. Callers should rely on a response's
            [next_page_token][google.cloud.managedidentities.v1.ListDomainsResponse.next_page_token]
            to determine if there are additional results to list.
        page_token (str):
            Optional. The ``next_page_token`` value returned from a
            previous ListDomainsRequest request, if any.
        filter (str):
            Optional. A filter specifying constraints of a list
            operation. For example,
            ``Domain.fqdn="mydomain.myorginization"``.
        order_by (str):
            Optional. Specifies the ordering of results. See `Sorting
            order <https://cloud.google.com/apis/design/design_patterns#sorting_order>`__
            for more information.
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


class ListDomainsResponse(proto.Message):
    r"""Response message for
    [ListDomains][google.cloud.managedidentities.v1.ListDomains]

    Attributes:
        domains (MutableSequence[google.cloud.managedidentities_v1.types.Domain]):
            A list of Managed Identities Service domains
            in the project.
        next_page_token (str):
            A token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
        unreachable (MutableSequence[str]):
            A list of locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    domains: MutableSequence[resource.Domain] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resource.Domain,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetDomainRequest(proto.Message):
    r"""Request message for
    [GetDomain][google.cloud.managedidentities.v1.GetDomain]

    Attributes:
        name (str):
            Required. The domain resource name using the form:
            ``projects/{project_id}/locations/global/domains/{domain_name}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateDomainRequest(proto.Message):
    r"""Request message for
    [UpdateDomain][google.cloud.managedidentities.v1.UpdateDomain]

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Mask of fields to update. At least one path must
            be supplied in this field. The elements of the repeated
            paths field may only include fields from
            [Domain][google.cloud.managedidentities.v1.Domain]:

            - ``labels``
            - ``locations``
            - ``authorized_networks``
        domain (google.cloud.managedidentities_v1.types.Domain):
            Required. Domain message with updated fields. Only supported
            fields specified in update_mask are updated.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    domain: resource.Domain = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resource.Domain,
    )


class DeleteDomainRequest(proto.Message):
    r"""Request message for
    [DeleteDomain][google.cloud.managedidentities.v1.DeleteDomain]

    Attributes:
        name (str):
            Required. The domain resource name using the form:
            ``projects/{project_id}/locations/global/domains/{domain_name}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AttachTrustRequest(proto.Message):
    r"""Request message for
    [AttachTrust][google.cloud.managedidentities.v1.AttachTrust]

    Attributes:
        name (str):
            Required. The resource domain name, project name and
            location using the form:
            ``projects/{project_id}/locations/global/domains/{domain_name}``
        trust (google.cloud.managedidentities_v1.types.Trust):
            Required. The domain trust resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    trust: resource.Trust = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resource.Trust,
    )


class ReconfigureTrustRequest(proto.Message):
    r"""Request message for
    [ReconfigureTrust][google.cloud.managedidentities.v1.ReconfigureTrust]

    Attributes:
        name (str):
            Required. The resource domain name, project name and
            location using the form:
            ``projects/{project_id}/locations/global/domains/{domain_name}``
        target_domain_name (str):
            Required. The fully-qualified target domain
            name which will be in trust with current domain.
        target_dns_ip_addresses (MutableSequence[str]):
            Required. The target DNS server IP addresses
            to resolve the remote domain involved in the
            trust.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    target_domain_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    target_dns_ip_addresses: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class DetachTrustRequest(proto.Message):
    r"""Request message for
    [DetachTrust][google.cloud.managedidentities.v1.DetachTrust]

    Attributes:
        name (str):
            Required. The resource domain name, project name, and
            location using the form:
            ``projects/{project_id}/locations/global/domains/{domain_name}``
        trust (google.cloud.managedidentities_v1.types.Trust):
            Required. The domain trust resource to
            removed.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    trust: resource.Trust = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resource.Trust,
    )


class ValidateTrustRequest(proto.Message):
    r"""Request message for
    [ValidateTrust][google.cloud.managedidentities.v1.ValidateTrust]

    Attributes:
        name (str):
            Required. The resource domain name, project name, and
            location using the form:
            ``projects/{project_id}/locations/global/domains/{domain_name}``
        trust (google.cloud.managedidentities_v1.types.Trust):
            Required. The domain trust to validate trust
            state for.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    trust: resource.Trust = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resource.Trust,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
