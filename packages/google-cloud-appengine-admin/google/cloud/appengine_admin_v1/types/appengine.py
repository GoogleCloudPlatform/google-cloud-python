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
import proto  # type: ignore

from google.cloud.appengine_admin_v1.types import application as ga_application
from google.cloud.appengine_admin_v1.types import certificate as ga_certificate
from google.cloud.appengine_admin_v1.types import domain, firewall, instance
from google.cloud.appengine_admin_v1.types import domain_mapping as ga_domain_mapping
from google.cloud.appengine_admin_v1.types import service as ga_service
from google.cloud.appengine_admin_v1.types import version as ga_version

__protobuf__ = proto.module(
    package="google.appengine.v1",
    manifest={
        "VersionView",
        "AuthorizedCertificateView",
        "DomainOverrideStrategy",
        "GetApplicationRequest",
        "CreateApplicationRequest",
        "UpdateApplicationRequest",
        "RepairApplicationRequest",
        "ListServicesRequest",
        "ListServicesResponse",
        "GetServiceRequest",
        "UpdateServiceRequest",
        "DeleteServiceRequest",
        "ListVersionsRequest",
        "ListVersionsResponse",
        "GetVersionRequest",
        "CreateVersionRequest",
        "UpdateVersionRequest",
        "DeleteVersionRequest",
        "ListInstancesRequest",
        "ListInstancesResponse",
        "GetInstanceRequest",
        "DeleteInstanceRequest",
        "DebugInstanceRequest",
        "ListIngressRulesRequest",
        "ListIngressRulesResponse",
        "BatchUpdateIngressRulesRequest",
        "BatchUpdateIngressRulesResponse",
        "CreateIngressRuleRequest",
        "GetIngressRuleRequest",
        "UpdateIngressRuleRequest",
        "DeleteIngressRuleRequest",
        "ListAuthorizedDomainsRequest",
        "ListAuthorizedDomainsResponse",
        "ListAuthorizedCertificatesRequest",
        "ListAuthorizedCertificatesResponse",
        "GetAuthorizedCertificateRequest",
        "CreateAuthorizedCertificateRequest",
        "UpdateAuthorizedCertificateRequest",
        "DeleteAuthorizedCertificateRequest",
        "ListDomainMappingsRequest",
        "ListDomainMappingsResponse",
        "GetDomainMappingRequest",
        "CreateDomainMappingRequest",
        "UpdateDomainMappingRequest",
        "DeleteDomainMappingRequest",
    },
)


class VersionView(proto.Enum):
    r"""Fields that should be returned when
    [Version][google.appengine.v1.Version] resources are retrieved.

    Values:
        BASIC (0):
            Basic version information including scaling
            and inbound services, but not detailed
            deployment information.
        FULL (1):
            The information from ``BASIC``, plus detailed information
            about the deployment. This format is required when creating
            resources, but is not returned in ``Get`` or ``List`` by
            default.
    """

    BASIC = 0
    FULL = 1


class AuthorizedCertificateView(proto.Enum):
    r"""Fields that should be returned when an AuthorizedCertificate
    resource is retrieved.

    Values:
        BASIC_CERTIFICATE (0):
            Basic certificate information, including
            applicable domains and expiration date.
        FULL_CERTIFICATE (1):
            The information from ``BASIC_CERTIFICATE``, plus detailed
            information on the domain mappings that have this
            certificate mapped.
    """

    BASIC_CERTIFICATE = 0
    FULL_CERTIFICATE = 1


class DomainOverrideStrategy(proto.Enum):
    r"""Override strategy for mutating an existing mapping.

    Values:
        UNSPECIFIED_DOMAIN_OVERRIDE_STRATEGY (0):
            Strategy unspecified. Defaults to ``STRICT``.
        STRICT (1):
            Overrides not allowed. If a mapping already exists for the
            specified domain, the request will return an ALREADY_EXISTS
            (409).
        OVERRIDE (2):
            Overrides allowed. If a mapping already
            exists for the specified domain, the request
            will overwrite it. Note that this might stop
            another Google product from serving. For
            example, if the domain is mapped to another App
            Engine application, that app will no longer
            serve from that domain.
    """

    UNSPECIFIED_DOMAIN_OVERRIDE_STRATEGY = 0
    STRICT = 1
    OVERRIDE = 2


class GetApplicationRequest(proto.Message):
    r"""Request message for ``Applications.GetApplication``.

    Attributes:
        name (str):
            Name of the Application resource to get. Example:
            ``apps/myapp``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateApplicationRequest(proto.Message):
    r"""Request message for ``Applications.CreateApplication``.

    Attributes:
        application (google.cloud.appengine_admin_v1.types.Application):
            Application configuration.
    """

    application: ga_application.Application = proto.Field(
        proto.MESSAGE,
        number=2,
        message=ga_application.Application,
    )


class UpdateApplicationRequest(proto.Message):
    r"""Request message for ``Applications.UpdateApplication``.

    Attributes:
        name (str):
            Name of the Application resource to update. Example:
            ``apps/myapp``.
        application (google.cloud.appengine_admin_v1.types.Application):
            An Application containing the updated
            resource.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Standard field mask for the set of
            fields to be updated.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    application: ga_application.Application = proto.Field(
        proto.MESSAGE,
        number=2,
        message=ga_application.Application,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=3,
        message=field_mask_pb2.FieldMask,
    )


class RepairApplicationRequest(proto.Message):
    r"""Request message for 'Applications.RepairApplication'.

    Attributes:
        name (str):
            Name of the application to repair. Example: ``apps/myapp``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListServicesRequest(proto.Message):
    r"""Request message for ``Services.ListServices``.

    Attributes:
        parent (str):
            Name of the parent Application resource. Example:
            ``apps/myapp``.
        page_size (int):
            Maximum results to return per page.
        page_token (str):
            Continuation token for fetching the next page
            of results.
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


class ListServicesResponse(proto.Message):
    r"""Response message for ``Services.ListServices``.

    Attributes:
        services (MutableSequence[google.cloud.appengine_admin_v1.types.Service]):
            The services belonging to the requested
            application.
        next_page_token (str):
            Continuation token for fetching the next page
            of results.
    """

    @property
    def raw_page(self):
        return self

    services: MutableSequence[ga_service.Service] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=ga_service.Service,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetServiceRequest(proto.Message):
    r"""Request message for ``Services.GetService``.

    Attributes:
        name (str):
            Name of the resource requested. Example:
            ``apps/myapp/services/default``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateServiceRequest(proto.Message):
    r"""Request message for ``Services.UpdateService``.

    Attributes:
        name (str):
            Name of the resource to update. Example:
            ``apps/myapp/services/default``.
        service (google.cloud.appengine_admin_v1.types.Service):
            A Service resource containing the updated
            service. Only fields set in the field mask will
            be updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Standard field mask for the set of
            fields to be updated.
        migrate_traffic (bool):
            Set to ``true`` to gradually shift traffic to one or more
            versions that you specify. By default, traffic is shifted
            immediately. For gradual traffic migration, the target
            versions must be located within instances that are
            configured for both `warmup
            requests <https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#InboundServiceType>`__
            and `automatic
            scaling <https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#AutomaticScaling>`__.
            You must specify the
            ```shardBy`` <https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services#ShardBy>`__
            field in the Service resource. Gradual traffic migration is
            not supported in the App Engine flexible environment. For
            examples, see `Migrating and Splitting
            Traffic <https://cloud.google.com/appengine/docs/admin-api/migrating-splitting-traffic>`__.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    service: ga_service.Service = proto.Field(
        proto.MESSAGE,
        number=2,
        message=ga_service.Service,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=3,
        message=field_mask_pb2.FieldMask,
    )
    migrate_traffic: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class DeleteServiceRequest(proto.Message):
    r"""Request message for ``Services.DeleteService``.

    Attributes:
        name (str):
            Name of the resource requested. Example:
            ``apps/myapp/services/default``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListVersionsRequest(proto.Message):
    r"""Request message for ``Versions.ListVersions``.

    Attributes:
        parent (str):
            Name of the parent Service resource. Example:
            ``apps/myapp/services/default``.
        view (google.cloud.appengine_admin_v1.types.VersionView):
            Controls the set of fields returned in the ``List``
            response.
        page_size (int):
            Maximum results to return per page.
        page_token (str):
            Continuation token for fetching the next page
            of results.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: "VersionView" = proto.Field(
        proto.ENUM,
        number=2,
        enum="VersionView",
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListVersionsResponse(proto.Message):
    r"""Response message for ``Versions.ListVersions``.

    Attributes:
        versions (MutableSequence[google.cloud.appengine_admin_v1.types.Version]):
            The versions belonging to the requested
            service.
        next_page_token (str):
            Continuation token for fetching the next page
            of results.
    """

    @property
    def raw_page(self):
        return self

    versions: MutableSequence[ga_version.Version] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=ga_version.Version,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetVersionRequest(proto.Message):
    r"""Request message for ``Versions.GetVersion``.

    Attributes:
        name (str):
            Name of the resource requested. Example:
            ``apps/myapp/services/default/versions/v1``.
        view (google.cloud.appengine_admin_v1.types.VersionView):
            Controls the set of fields returned in the ``Get`` response.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: "VersionView" = proto.Field(
        proto.ENUM,
        number=2,
        enum="VersionView",
    )


class CreateVersionRequest(proto.Message):
    r"""Request message for ``Versions.CreateVersion``.

    Attributes:
        parent (str):
            Name of the parent resource to create this version under.
            Example: ``apps/myapp/services/default``.
        version (google.cloud.appengine_admin_v1.types.Version):
            Application deployment configuration.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    version: ga_version.Version = proto.Field(
        proto.MESSAGE,
        number=2,
        message=ga_version.Version,
    )


class UpdateVersionRequest(proto.Message):
    r"""Request message for ``Versions.UpdateVersion``.

    Attributes:
        name (str):
            Name of the resource to update. Example:
            ``apps/myapp/services/default/versions/1``.
        version (google.cloud.appengine_admin_v1.types.Version):
            A Version containing the updated resource.
            Only fields set in the field mask will be
            updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Standard field mask for the set of fields to
            be updated.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    version: ga_version.Version = proto.Field(
        proto.MESSAGE,
        number=2,
        message=ga_version.Version,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=3,
        message=field_mask_pb2.FieldMask,
    )


class DeleteVersionRequest(proto.Message):
    r"""Request message for ``Versions.DeleteVersion``.

    Attributes:
        name (str):
            Name of the resource requested. Example:
            ``apps/myapp/services/default/versions/v1``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListInstancesRequest(proto.Message):
    r"""Request message for ``Instances.ListInstances``.

    Attributes:
        parent (str):
            Name of the parent Version resource. Example:
            ``apps/myapp/services/default/versions/v1``.
        page_size (int):
            Maximum results to return per page.
        page_token (str):
            Continuation token for fetching the next page
            of results.
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


class ListInstancesResponse(proto.Message):
    r"""Response message for ``Instances.ListInstances``.

    Attributes:
        instances (MutableSequence[google.cloud.appengine_admin_v1.types.Instance]):
            The instances belonging to the requested
            version.
        next_page_token (str):
            Continuation token for fetching the next page
            of results.
    """

    @property
    def raw_page(self):
        return self

    instances: MutableSequence[instance.Instance] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=instance.Instance,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetInstanceRequest(proto.Message):
    r"""Request message for ``Instances.GetInstance``.

    Attributes:
        name (str):
            Name of the resource requested. Example:
            ``apps/myapp/services/default/versions/v1/instances/instance-1``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteInstanceRequest(proto.Message):
    r"""Request message for ``Instances.DeleteInstance``.

    Attributes:
        name (str):
            Name of the resource requested. Example:
            ``apps/myapp/services/default/versions/v1/instances/instance-1``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DebugInstanceRequest(proto.Message):
    r"""Request message for ``Instances.DebugInstance``.

    Attributes:
        name (str):
            Name of the resource requested. Example:
            ``apps/myapp/services/default/versions/v1/instances/instance-1``.
        ssh_key (str):
            Public SSH key to add to the instance. Examples:

            - ``[USERNAME]:ssh-rsa [KEY_VALUE] [USERNAME]``
            - ``[USERNAME]:ssh-rsa [KEY_VALUE] google-ssh {"userName":"[USERNAME]","expireOn":"[EXPIRE_TIME]"}``

            For more information, see `Adding and Removing SSH
            Keys <https://cloud.google.com/compute/docs/instances/adding-removing-ssh-keys>`__.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ssh_key: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListIngressRulesRequest(proto.Message):
    r"""Request message for ``Firewall.ListIngressRules``.

    Attributes:
        parent (str):
            Name of the Firewall collection to retrieve. Example:
            ``apps/myapp/firewall/ingressRules``.
        page_size (int):
            Maximum results to return per page.
        page_token (str):
            Continuation token for fetching the next page
            of results.
        matching_address (str):
            A valid IP Address. If set, only rules
            matching this address will be returned. The
            first returned rule will be the rule that fires
            on requests from this IP.
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
    matching_address: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListIngressRulesResponse(proto.Message):
    r"""Response message for ``Firewall.ListIngressRules``.

    Attributes:
        ingress_rules (MutableSequence[google.cloud.appengine_admin_v1.types.FirewallRule]):
            The ingress FirewallRules for this
            application.
        next_page_token (str):
            Continuation token for fetching the next page
            of results.
    """

    @property
    def raw_page(self):
        return self

    ingress_rules: MutableSequence[firewall.FirewallRule] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=firewall.FirewallRule,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class BatchUpdateIngressRulesRequest(proto.Message):
    r"""Request message for ``Firewall.BatchUpdateIngressRules``.

    Attributes:
        name (str):
            Name of the Firewall collection to set. Example:
            ``apps/myapp/firewall/ingressRules``.
        ingress_rules (MutableSequence[google.cloud.appengine_admin_v1.types.FirewallRule]):
            A list of FirewallRules to replace the
            existing set.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ingress_rules: MutableSequence[firewall.FirewallRule] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=firewall.FirewallRule,
    )


class BatchUpdateIngressRulesResponse(proto.Message):
    r"""Response message for ``Firewall.UpdateAllIngressRules``.

    Attributes:
        ingress_rules (MutableSequence[google.cloud.appengine_admin_v1.types.FirewallRule]):
            The full list of ingress FirewallRules for
            this application.
    """

    ingress_rules: MutableSequence[firewall.FirewallRule] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=firewall.FirewallRule,
    )


class CreateIngressRuleRequest(proto.Message):
    r"""Request message for ``Firewall.CreateIngressRule``.

    Attributes:
        parent (str):
            Name of the parent Firewall collection in which to create a
            new rule. Example: ``apps/myapp/firewall/ingressRules``.
        rule (google.cloud.appengine_admin_v1.types.FirewallRule):
            A FirewallRule containing the new resource.

            The user may optionally provide a position at
            which the new rule will be placed. The positions
            define a sequential list starting at 1. If a
            rule already exists at the given position, rules
            greater than the provided position will be moved
            forward by one.

            If no position is provided, the server will
            place the rule as the second to last rule in the
            sequence before the required default allow-all
            or deny-all rule.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    rule: firewall.FirewallRule = proto.Field(
        proto.MESSAGE,
        number=2,
        message=firewall.FirewallRule,
    )


class GetIngressRuleRequest(proto.Message):
    r"""Request message for ``Firewall.GetIngressRule``.

    Attributes:
        name (str):
            Name of the Firewall resource to retrieve. Example:
            ``apps/myapp/firewall/ingressRules/100``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateIngressRuleRequest(proto.Message):
    r"""Request message for ``Firewall.UpdateIngressRule``.

    Attributes:
        name (str):
            Name of the Firewall resource to update. Example:
            ``apps/myapp/firewall/ingressRules/100``.
        rule (google.cloud.appengine_admin_v1.types.FirewallRule):
            A FirewallRule containing the updated
            resource
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Standard field mask for the set of fields to
            be updated.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    rule: firewall.FirewallRule = proto.Field(
        proto.MESSAGE,
        number=2,
        message=firewall.FirewallRule,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=3,
        message=field_mask_pb2.FieldMask,
    )


class DeleteIngressRuleRequest(proto.Message):
    r"""Request message for ``Firewall.DeleteIngressRule``.

    Attributes:
        name (str):
            Name of the Firewall resource to delete. Example:
            ``apps/myapp/firewall/ingressRules/100``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListAuthorizedDomainsRequest(proto.Message):
    r"""Request message for ``AuthorizedDomains.ListAuthorizedDomains``.

    Attributes:
        parent (str):
            Name of the parent Application resource. Example:
            ``apps/myapp``.
        page_size (int):
            Maximum results to return per page.
        page_token (str):
            Continuation token for fetching the next page
            of results.
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


class ListAuthorizedDomainsResponse(proto.Message):
    r"""Response message for ``AuthorizedDomains.ListAuthorizedDomains``.

    Attributes:
        domains (MutableSequence[google.cloud.appengine_admin_v1.types.AuthorizedDomain]):
            The authorized domains belonging to the user.
        next_page_token (str):
            Continuation token for fetching the next page
            of results.
    """

    @property
    def raw_page(self):
        return self

    domains: MutableSequence[domain.AuthorizedDomain] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=domain.AuthorizedDomain,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListAuthorizedCertificatesRequest(proto.Message):
    r"""Request message for
    ``AuthorizedCertificates.ListAuthorizedCertificates``.

    Attributes:
        parent (str):
            Name of the parent ``Application`` resource. Example:
            ``apps/myapp``.
        view (google.cloud.appengine_admin_v1.types.AuthorizedCertificateView):
            Controls the set of fields returned in the ``LIST``
            response.
        page_size (int):
            Maximum results to return per page.
        page_token (str):
            Continuation token for fetching the next page
            of results.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: "AuthorizedCertificateView" = proto.Field(
        proto.ENUM,
        number=4,
        enum="AuthorizedCertificateView",
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListAuthorizedCertificatesResponse(proto.Message):
    r"""Response message for
    ``AuthorizedCertificates.ListAuthorizedCertificates``.

    Attributes:
        certificates (MutableSequence[google.cloud.appengine_admin_v1.types.AuthorizedCertificate]):
            The SSL certificates the user is authorized
            to administer.
        next_page_token (str):
            Continuation token for fetching the next page
            of results.
    """

    @property
    def raw_page(self):
        return self

    certificates: MutableSequence[ga_certificate.AuthorizedCertificate] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=ga_certificate.AuthorizedCertificate,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetAuthorizedCertificateRequest(proto.Message):
    r"""Request message for
    ``AuthorizedCertificates.GetAuthorizedCertificate``.

    Attributes:
        name (str):
            Name of the resource requested. Example:
            ``apps/myapp/authorizedCertificates/12345``.
        view (google.cloud.appengine_admin_v1.types.AuthorizedCertificateView):
            Controls the set of fields returned in the ``GET`` response.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: "AuthorizedCertificateView" = proto.Field(
        proto.ENUM,
        number=2,
        enum="AuthorizedCertificateView",
    )


class CreateAuthorizedCertificateRequest(proto.Message):
    r"""Request message for
    ``AuthorizedCertificates.CreateAuthorizedCertificate``.

    Attributes:
        parent (str):
            Name of the parent ``Application`` resource. Example:
            ``apps/myapp``.
        certificate (google.cloud.appengine_admin_v1.types.AuthorizedCertificate):
            SSL certificate data.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    certificate: ga_certificate.AuthorizedCertificate = proto.Field(
        proto.MESSAGE,
        number=2,
        message=ga_certificate.AuthorizedCertificate,
    )


class UpdateAuthorizedCertificateRequest(proto.Message):
    r"""Request message for
    ``AuthorizedCertificates.UpdateAuthorizedCertificate``.

    Attributes:
        name (str):
            Name of the resource to update. Example:
            ``apps/myapp/authorizedCertificates/12345``.
        certificate (google.cloud.appengine_admin_v1.types.AuthorizedCertificate):
            An ``AuthorizedCertificate`` containing the updated
            resource. Only fields set in the field mask will be updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Standard field mask for the set of fields to be updated.
            Updates are only supported on the ``certificate_raw_data``
            and ``display_name`` fields.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    certificate: ga_certificate.AuthorizedCertificate = proto.Field(
        proto.MESSAGE,
        number=2,
        message=ga_certificate.AuthorizedCertificate,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=3,
        message=field_mask_pb2.FieldMask,
    )


class DeleteAuthorizedCertificateRequest(proto.Message):
    r"""Request message for
    ``AuthorizedCertificates.DeleteAuthorizedCertificate``.

    Attributes:
        name (str):
            Name of the resource to delete. Example:
            ``apps/myapp/authorizedCertificates/12345``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListDomainMappingsRequest(proto.Message):
    r"""Request message for ``DomainMappings.ListDomainMappings``.

    Attributes:
        parent (str):
            Name of the parent Application resource. Example:
            ``apps/myapp``.
        page_size (int):
            Maximum results to return per page.
        page_token (str):
            Continuation token for fetching the next page
            of results.
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


class ListDomainMappingsResponse(proto.Message):
    r"""Response message for ``DomainMappings.ListDomainMappings``.

    Attributes:
        domain_mappings (MutableSequence[google.cloud.appengine_admin_v1.types.DomainMapping]):
            The domain mappings for the application.
        next_page_token (str):
            Continuation token for fetching the next page
            of results.
    """

    @property
    def raw_page(self):
        return self

    domain_mappings: MutableSequence[ga_domain_mapping.DomainMapping] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=ga_domain_mapping.DomainMapping,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetDomainMappingRequest(proto.Message):
    r"""Request message for ``DomainMappings.GetDomainMapping``.

    Attributes:
        name (str):
            Name of the resource requested. Example:
            ``apps/myapp/domainMappings/example.com``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateDomainMappingRequest(proto.Message):
    r"""Request message for ``DomainMappings.CreateDomainMapping``.

    Attributes:
        parent (str):
            Name of the parent Application resource. Example:
            ``apps/myapp``.
        domain_mapping (google.cloud.appengine_admin_v1.types.DomainMapping):
            Domain mapping configuration.
        override_strategy (google.cloud.appengine_admin_v1.types.DomainOverrideStrategy):
            Whether the domain creation should override
            any existing mappings for this domain. By
            default, overrides are rejected.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    domain_mapping: ga_domain_mapping.DomainMapping = proto.Field(
        proto.MESSAGE,
        number=2,
        message=ga_domain_mapping.DomainMapping,
    )
    override_strategy: "DomainOverrideStrategy" = proto.Field(
        proto.ENUM,
        number=4,
        enum="DomainOverrideStrategy",
    )


class UpdateDomainMappingRequest(proto.Message):
    r"""Request message for ``DomainMappings.UpdateDomainMapping``.

    Attributes:
        name (str):
            Name of the resource to update. Example:
            ``apps/myapp/domainMappings/example.com``.
        domain_mapping (google.cloud.appengine_admin_v1.types.DomainMapping):
            A domain mapping containing the updated
            resource. Only fields set in the field mask will
            be updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Standard field mask for the set of
            fields to be updated.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    domain_mapping: ga_domain_mapping.DomainMapping = proto.Field(
        proto.MESSAGE,
        number=2,
        message=ga_domain_mapping.DomainMapping,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=3,
        message=field_mask_pb2.FieldMask,
    )


class DeleteDomainMappingRequest(proto.Message):
    r"""Request message for ``DomainMappings.DeleteDomainMapping``.

    Attributes:
        name (str):
            Name of the resource to delete. Example:
            ``apps/myapp/domainMappings/example.com``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
