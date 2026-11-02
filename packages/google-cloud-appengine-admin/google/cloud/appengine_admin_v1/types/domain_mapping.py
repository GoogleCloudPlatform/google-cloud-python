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

__protobuf__ = proto.module(
    package="google.appengine.v1",
    manifest={
        "DomainMapping",
        "SslSettings",
        "ResourceRecord",
    },
)


class DomainMapping(proto.Message):
    r"""A domain serving an App Engine application.

    Attributes:
        name (str):
            Full path to the ``DomainMapping`` resource in the API.
            Example: ``apps/myapp/domainMapping/example.com``.

            @OutputOnly
        id (str):
            Relative name of the domain serving the application.
            Example: ``example.com``.
        ssl_settings (google.cloud.appengine_admin_v1.types.SslSettings):
            SSL configuration for this domain. If
            unconfigured, this domain will not serve with
            SSL.
        resource_records (MutableSequence[google.cloud.appengine_admin_v1.types.ResourceRecord]):
            The resource records required to configure
            this domain mapping. These records must be added
            to the domain's DNS configuration in order to
            serve the application via this domain mapping.

            @OutputOnly
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    ssl_settings: "SslSettings" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="SslSettings",
    )
    resource_records: MutableSequence["ResourceRecord"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="ResourceRecord",
    )


class SslSettings(proto.Message):
    r"""SSL configuration for a ``DomainMapping`` resource.

    Attributes:
        certificate_id (str):
            ID of the ``AuthorizedCertificate`` resource configuring SSL
            for the application. Clearing this field will remove SSL
            support.

            By default, a managed certificate is automatically created
            for every domain mapping. To omit SSL support or to
            configure SSL manually, specify ``SslManagementType.MANUAL``
            on a ``CREATE`` or ``UPDATE`` request. You must be
            authorized to administer the ``AuthorizedCertificate``
            resource to manually map it to a ``DomainMapping`` resource.
            Example: ``12345``.
        ssl_management_type (google.cloud.appengine_admin_v1.types.SslSettings.SslManagementType):
            SSL management type for this domain. If ``AUTOMATIC``, a
            managed certificate is automatically provisioned. If
            ``MANUAL``, ``certificate_id`` must be manually specified in
            order to configure SSL for this domain.
        pending_managed_certificate_id (str):
            ID of the managed ``AuthorizedCertificate`` resource
            currently being provisioned, if applicable. Until the new
            managed certificate has been successfully provisioned, the
            previous SSL state will be preserved. Once the provisioning
            process completes, the ``certificate_id`` field will reflect
            the new managed certificate and this field will be left
            empty. To remove SSL support while there is still a pending
            managed certificate, clear the ``certificate_id`` field with
            an ``UpdateDomainMappingRequest``.

            @OutputOnly
    """

    class SslManagementType(proto.Enum):
        r"""The SSL management type for this domain.

        Values:
            SSL_MANAGEMENT_TYPE_UNSPECIFIED (0):
                Defaults to ``AUTOMATIC``.
            AUTOMATIC (1):
                SSL support for this domain is configured
                automatically. The mapped SSL certificate will
                be automatically renewed.
            MANUAL (2):
                SSL support for this domain is configured
                manually by the user. Either the domain has no
                SSL support or a user-obtained SSL certificate
                has been explictly mapped to this domain.
        """

        SSL_MANAGEMENT_TYPE_UNSPECIFIED = 0
        AUTOMATIC = 1
        MANUAL = 2

    certificate_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ssl_management_type: SslManagementType = proto.Field(
        proto.ENUM,
        number=3,
        enum=SslManagementType,
    )
    pending_managed_certificate_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ResourceRecord(proto.Message):
    r"""A DNS resource record.

    Attributes:
        name (str):
            Relative name of the object affected by this record. Only
            applicable for ``CNAME`` records. Example: 'www'.
        rrdata (str):
            Data for this record. Values vary by record
            type, as defined in RFC 1035 (section 5) and RFC
            1034 (section 3.6.1).
        type_ (google.cloud.appengine_admin_v1.types.ResourceRecord.RecordType):
            Resource record type. Example: ``AAAA``.
    """

    class RecordType(proto.Enum):
        r"""A resource record type.

        Values:
            RECORD_TYPE_UNSPECIFIED (0):
                An unknown resource record.
            A (1):
                An A resource record. Data is an IPv4
                address.
            AAAA (2):
                An AAAA resource record. Data is an IPv6
                address.
            CNAME (3):
                A CNAME resource record. Data is a domain
                name to be aliased.
        """

        RECORD_TYPE_UNSPECIFIED = 0
        A = 1
        AAAA = 2
        CNAME = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    rrdata: str = proto.Field(
        proto.STRING,
        number=2,
    )
    type_: RecordType = proto.Field(
        proto.ENUM,
        number=3,
        enum=RecordType,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
