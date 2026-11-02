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

import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.wrappers_pb2 as wrappers_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.iap.v1",
    manifest={
        "ListTunnelDestGroupsRequest",
        "ListTunnelDestGroupsResponse",
        "CreateTunnelDestGroupRequest",
        "GetTunnelDestGroupRequest",
        "DeleteTunnelDestGroupRequest",
        "UpdateTunnelDestGroupRequest",
        "TunnelDestGroup",
        "GetIapSettingsRequest",
        "UpdateIapSettingsRequest",
        "IapSettings",
        "AccessSettings",
        "GcipSettings",
        "CorsSettings",
        "OAuthSettings",
        "WorkforceIdentitySettings",
        "OAuth2",
        "ReauthSettings",
        "AllowedDomainsSettings",
        "ApplicationSettings",
        "CsmSettings",
        "AccessDeniedPageSettings",
        "AttributePropagationSettings",
        "ValidateIapAttributeExpressionRequest",
        "ValidateIapAttributeExpressionResponse",
        "ListBrandsRequest",
        "ListBrandsResponse",
        "CreateBrandRequest",
        "GetBrandRequest",
        "ListIdentityAwareProxyClientsRequest",
        "ListIdentityAwareProxyClientsResponse",
        "CreateIdentityAwareProxyClientRequest",
        "GetIdentityAwareProxyClientRequest",
        "ResetIdentityAwareProxyClientSecretRequest",
        "DeleteIdentityAwareProxyClientRequest",
        "Brand",
        "IdentityAwareProxyClient",
    },
)


class ListTunnelDestGroupsRequest(proto.Message):
    r"""The request to ListTunnelDestGroups.

    Attributes:
        parent (str):
            Required. Google Cloud Project ID and location. In the
            following format:
            ``projects/{project_number/id}/iap_tunnel/locations/{location}``.
            A ``-`` can be used for the location to group across all
            locations.
        page_size (int):
            The maximum number of groups to return. The
            service might return fewer than this value.
            If unspecified, at most 100 groups are returned.
            The maximum value is 1000; values above 1000 are
            coerced to 1000.
        page_token (str):
            A page token, received from a previous
            ``ListTunnelDestGroups`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListTunnelDestGroups`` must match the call that provided
            the page token.
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


class ListTunnelDestGroupsResponse(proto.Message):
    r"""The response from ListTunnelDestGroups.

    Attributes:
        tunnel_dest_groups (MutableSequence[google.cloud.iap_v1.types.TunnelDestGroup]):
            TunnelDestGroup existing in the project.
        next_page_token (str):
            A token that you can send as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    tunnel_dest_groups: MutableSequence["TunnelDestGroup"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="TunnelDestGroup",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateTunnelDestGroupRequest(proto.Message):
    r"""The request to CreateTunnelDestGroup.

    Attributes:
        parent (str):
            Required. Google Cloud Project ID and location. In the
            following format:
            ``projects/{project_number/id}/iap_tunnel/locations/{location}``.
        tunnel_dest_group (google.cloud.iap_v1.types.TunnelDestGroup):
            Required. The TunnelDestGroup to create.
        tunnel_dest_group_id (str):
            Required. The ID to use for the TunnelDestGroup, which
            becomes the final component of the resource name.

            This value must be 4-63 characters, and valid characters are
            ``[a-z]-``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    tunnel_dest_group: "TunnelDestGroup" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="TunnelDestGroup",
    )
    tunnel_dest_group_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GetTunnelDestGroupRequest(proto.Message):
    r"""The request to GetTunnelDestGroup.

    Attributes:
        name (str):
            Required. Name of the TunnelDestGroup to be fetched. In the
            following format:
            ``projects/{project_number/id}/iap_tunnel/locations/{location}/destGroups/{dest_group}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteTunnelDestGroupRequest(proto.Message):
    r"""The request to DeleteTunnelDestGroup.

    Attributes:
        name (str):
            Required. Name of the TunnelDestGroup to delete. In the
            following format:
            ``projects/{project_number/id}/iap_tunnel/locations/{location}/destGroups/{dest_group}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateTunnelDestGroupRequest(proto.Message):
    r"""The request to UpdateTunnelDestGroup.

    Attributes:
        tunnel_dest_group (google.cloud.iap_v1.types.TunnelDestGroup):
            Required. The new values for the
            TunnelDestGroup.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            A field mask that specifies which IAP
            settings to update. If omitted, then all of the
            settings are updated. See
            https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask
    """

    tunnel_dest_group: "TunnelDestGroup" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="TunnelDestGroup",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class TunnelDestGroup(proto.Message):
    r"""A TunnelDestGroup.

    Attributes:
        name (str):
            Identifier. Identifier for the
            TunnelDestGroup. Must be unique within the
            project and contain only lower case letters
            (a-z) and dashes (-).
        cidrs (MutableSequence[str]):
            Optional. Unordered list. List of CIDRs that
            this group applies to.
        fqdns (MutableSequence[str]):
            Optional. Unordered list. List of FQDNs that
            this group applies to.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cidrs: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    fqdns: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetIapSettingsRequest(proto.Message):
    r"""The request sent to GetIapSettings.

    Attributes:
        name (str):
            Required. The resource name for which to retrieve the
            settings. Authorization: Requires the ``getSettings``
            permission for the associated resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateIapSettingsRequest(proto.Message):
    r"""The request sent to UpdateIapSettings.

    Attributes:
        iap_settings (google.cloud.iap_v1.types.IapSettings):
            Required. The new values for the IAP settings to be updated.
            Authorization: Requires the ``updateSettings`` permission
            for the associated resource.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The field mask specifying which IAP settings should be
            updated. If omitted, then all of the settings are updated.
            See
            https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask.

            Note: All IAP reauth settings must always be set together,
            using the field mask:
            ``iapSettings.accessSettings.reauthSettings``.
    """

    iap_settings: "IapSettings" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="IapSettings",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class IapSettings(proto.Message):
    r"""The IAP configurable settings.

    Attributes:
        name (str):
            Required. The resource name of the IAP
            protected resource.
        access_settings (google.cloud.iap_v1.types.AccessSettings):
            Optional. Top level wrapper for all access
            related setting in IAP
        application_settings (google.cloud.iap_v1.types.ApplicationSettings):
            Optional. Top level wrapper for all
            application related settings in IAP
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    access_settings: "AccessSettings" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="AccessSettings",
    )
    application_settings: "ApplicationSettings" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="ApplicationSettings",
    )


class AccessSettings(proto.Message):
    r"""Access related settings for IAP protected apps.

    Attributes:
        gcip_settings (google.cloud.iap_v1.types.GcipSettings):
            Optional. GCIP claims and endpoint
            configurations for 3p identity providers.
        cors_settings (google.cloud.iap_v1.types.CorsSettings):
            Optional. Configuration to allow cross-origin
            requests via IAP.
        oauth_settings (google.cloud.iap_v1.types.OAuthSettings):
            Optional. Settings to configure IAP's OAuth
            behavior.
        reauth_settings (google.cloud.iap_v1.types.ReauthSettings):
            Optional. Settings to configure
            reauthentication policies in IAP.
        allowed_domains_settings (google.cloud.iap_v1.types.AllowedDomainsSettings):
            Optional. Settings to configure and enable
            allowed domains.
        workforce_identity_settings (google.cloud.iap_v1.types.WorkforceIdentitySettings):
            Optional. Settings to configure the workforce
            identity federation, including workforce pools
            and OAuth 2.0 settings.
        identity_sources (MutableSequence[google.cloud.iap_v1.types.AccessSettings.IdentitySource]):
            Optional. Identity sources that IAP can use
            to authenticate the end user. Only one identity
            source can be configured.
    """

    class IdentitySource(proto.Enum):
        r"""Types of identity source supported by IAP.

        Values:
            IDENTITY_SOURCE_UNSPECIFIED (0):
                IdentitySource Unspecified.
                When selected, IAP relies on which identity
                settings are fully configured to redirect the
                traffic to. The precedence order is
                WorkforceIdentitySettings > GcipSettings. If
                none is set, default to use Google identity.
            WORKFORCE_IDENTITY_FEDERATION (3):
                Use external identities set up on Google
                Cloud Workforce Identity Federation.
        """

        IDENTITY_SOURCE_UNSPECIFIED = 0
        WORKFORCE_IDENTITY_FEDERATION = 3

    gcip_settings: "GcipSettings" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="GcipSettings",
    )
    cors_settings: "CorsSettings" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="CorsSettings",
    )
    oauth_settings: "OAuthSettings" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="OAuthSettings",
    )
    reauth_settings: "ReauthSettings" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="ReauthSettings",
    )
    allowed_domains_settings: "AllowedDomainsSettings" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="AllowedDomainsSettings",
    )
    workforce_identity_settings: "WorkforceIdentitySettings" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="WorkforceIdentitySettings",
    )
    identity_sources: MutableSequence[IdentitySource] = proto.RepeatedField(
        proto.ENUM,
        number=10,
        enum=IdentitySource,
    )


class GcipSettings(proto.Message):
    r"""Allows customers to configure tenant IDs for a Cloud Identity
    Platform (GCIP) instance for each application.

    Attributes:
        tenant_ids (MutableSequence[str]):
            Optional. GCIP tenant IDs that are linked to the IAP
            resource. ``tenant_ids`` could be a string beginning with a
            number character to indicate authenticating with GCIP tenant
            flow, or in the format of ``_<ProjectNumber>`` to indicate
            authenticating with GCIP agent flow. If agent flow is used,
            ``tenant_ids`` should only contain one single element, while
            for tenant flow, ``tenant_ids`` can contain multiple
            elements.
        login_page_uri (google.protobuf.wrappers_pb2.StringValue):
            Login page URI associated with the GCIP
            tenants. Typically, all resources within the
            same project share the same login page, though
            it could be overridden at the sub resource
            level.
    """

    tenant_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    login_page_uri: wrappers_pb2.StringValue = proto.Field(
        proto.MESSAGE,
        number=2,
        message=wrappers_pb2.StringValue,
    )


class CorsSettings(proto.Message):
    r"""Allows customers to configure HTTP request paths that'll allow HTTP
    ``OPTIONS`` call to bypass authentication and authorization.

    Attributes:
        allow_http_options (google.protobuf.wrappers_pb2.BoolValue):
            Configuration to allow HTTP ``OPTIONS`` calls to skip
            authentication and authorization. If undefined, IAP will not
            apply any special logic to ``OPTIONS`` requests.
    """

    allow_http_options: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=1,
        message=wrappers_pb2.BoolValue,
    )


class OAuthSettings(proto.Message):
    r"""Configuration for OAuth login&consent flow behavior as well
    as for OAuth Credentials.

    Attributes:
        login_hint (google.protobuf.wrappers_pb2.StringValue):
            Domain hint to send as hd=? parameter in
            OAuth request flow. Enables redirect to primary
            IDP by skipping Google's login screen.
            https://developers.google.com/identity/protocols/OpenIDConnect#hd-param
            Note: IAP does not verify that the id token's hd
            claim matches this value since access behavior
            is managed by IAM policies.
        client_id (google.protobuf.wrappers_pb2.StringValue):
            Optional. OAuth 2.0 client ID used in the
            OAuth flow. This allows for client sharing. The
            risks of client sharing are outlined here:

            https://cloud.google.com/iap/docs/sharing-oauth-clients#risks.
        client_secret (google.protobuf.wrappers_pb2.StringValue):
            Optional. Input only. OAuth secret paired
            with client ID.
        client_secret_sha256 (google.protobuf.wrappers_pb2.StringValue):
            Output only. OAuth secret SHA256 paired with
            client ID.
        programmatic_clients (MutableSequence[str]):
            Optional. List of client ids allowed to use
            IAP programmatically.
    """

    login_hint: wrappers_pb2.StringValue = proto.Field(
        proto.MESSAGE,
        number=2,
        message=wrappers_pb2.StringValue,
    )
    client_id: wrappers_pb2.StringValue = proto.Field(
        proto.MESSAGE,
        number=3,
        message=wrappers_pb2.StringValue,
    )
    client_secret: wrappers_pb2.StringValue = proto.Field(
        proto.MESSAGE,
        number=4,
        message=wrappers_pb2.StringValue,
    )
    client_secret_sha256: wrappers_pb2.StringValue = proto.Field(
        proto.MESSAGE,
        number=6,
        message=wrappers_pb2.StringValue,
    )
    programmatic_clients: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )


class WorkforceIdentitySettings(proto.Message):
    r"""WorkforceIdentitySettings allows customers to configure
    workforce pools and OAuth 2.0 settings to gate their
    applications using a third-party IdP with access control.

    Attributes:
        workforce_pools (MutableSequence[str]):
            The workforce pool resources. Only one
            workforce pool is accepted.
        oauth2 (google.cloud.iap_v1.types.OAuth2):
            OAuth 2.0 settings for IAP to perform OIDC
            flow with workforce identity federation
            services.
    """

    workforce_pools: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    oauth2: "OAuth2" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="OAuth2",
    )


class OAuth2(proto.Message):
    r"""The OAuth 2.0 Settings

    Attributes:
        client_id (str):
            The OAuth 2.0 client ID registered in the
            workforce identity federation OAuth 2.0 Server.
        client_secret (str):
            Input only. The OAuth 2.0 client secret
            created while registering the client ID.
        client_secret_sha256 (str):
            Output only. SHA256 hash value for the client
            secret. This field is returned by IAP when the
            settings are retrieved.
    """

    client_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    client_secret: str = proto.Field(
        proto.STRING,
        number=2,
    )
    client_secret_sha256: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ReauthSettings(proto.Message):
    r"""Configuration for IAP reauthentication policies.

    Attributes:
        method (google.cloud.iap_v1.types.ReauthSettings.Method):
            Optional. Reauth method requested.
        max_age (google.protobuf.duration_pb2.Duration):
            Optional. Reauth session lifetime, how long
            before a user has to reauthenticate again.
        policy_type (google.cloud.iap_v1.types.ReauthSettings.PolicyType):
            Optional. How IAP determines the effective
            policy in cases of hierarchical policies.
            Policies are merged from higher in the hierarchy
            to lower in the hierarchy.
    """

    class Method(proto.Enum):
        r"""Types of reauthentication methods supported by IAP.

        Values:
            METHOD_UNSPECIFIED (0):
                Reauthentication disabled.
            LOGIN (1):
                Prompts the user to log in again.
            PASSWORD (2):
                No description available.
            SECURE_KEY (3):
                User must use their secure key 2nd factor
                device.
            ENROLLED_SECOND_FACTORS (4):
                User can use any enabled 2nd factor.
        """

        METHOD_UNSPECIFIED = 0
        LOGIN = 1
        PASSWORD = 2
        SECURE_KEY = 3
        ENROLLED_SECOND_FACTORS = 4

    class PolicyType(proto.Enum):
        r"""Type of policy in the case of hierarchical policies.

        Values:
            POLICY_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            MINIMUM (1):
                This policy acts as a minimum to other
                policies, lower in the hierarchy. Effective
                policy may only be the same or stricter.
            DEFAULT (2):
                This policy acts as a default if no other
                reauth policy is set.
        """

        POLICY_TYPE_UNSPECIFIED = 0
        MINIMUM = 1
        DEFAULT = 2

    method: Method = proto.Field(
        proto.ENUM,
        number=1,
        enum=Method,
    )
    max_age: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )
    policy_type: PolicyType = proto.Field(
        proto.ENUM,
        number=3,
        enum=PolicyType,
    )


class AllowedDomainsSettings(proto.Message):
    r"""Configuration for IAP allowed domains. Lets you to restrict
    access to an app and allow access to only the domains that you
    list.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        enable (bool):
            Optional. Configuration for customers to opt
            in for the feature.

            This field is a member of `oneof`_ ``_enable``.
        domains (MutableSequence[str]):
            Optional. List of trusted domains.
    """

    enable: bool = proto.Field(
        proto.BOOL,
        number=1,
        optional=True,
    )
    domains: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class ApplicationSettings(proto.Message):
    r"""Wrapper over application specific settings for IAP.

    Attributes:
        csm_settings (google.cloud.iap_v1.types.CsmSettings):
            Optional. Settings to configure IAP's
            behavior for a service mesh.
        access_denied_page_settings (google.cloud.iap_v1.types.AccessDeniedPageSettings):
            Optional. Customization for Access Denied
            page.
        cookie_domain (google.protobuf.wrappers_pb2.StringValue):
            The Domain value to set for cookies generated
            by IAP. This value is not validated by the API,
            but will be ignored at runtime if invalid.
        attribute_propagation_settings (google.cloud.iap_v1.types.AttributePropagationSettings):
            Optional. Settings to configure attribute
            propagation.
    """

    csm_settings: "CsmSettings" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="CsmSettings",
    )
    access_denied_page_settings: "AccessDeniedPageSettings" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="AccessDeniedPageSettings",
    )
    cookie_domain: wrappers_pb2.StringValue = proto.Field(
        proto.MESSAGE,
        number=3,
        message=wrappers_pb2.StringValue,
    )
    attribute_propagation_settings: "AttributePropagationSettings" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="AttributePropagationSettings",
    )


class CsmSettings(proto.Message):
    r"""Configuration for RCToken generated for service mesh
    workloads protected by IAP. RCToken are IAP generated JWTs that
    can be verified at the application. The RCToken is primarily
    used for service mesh deployments, and can be scoped to a single
    mesh by configuring the audience field accordingly.

    Attributes:
        rctoken_aud (google.protobuf.wrappers_pb2.StringValue):
            Audience claim set in the generated RCToken.
            This value is not validated by IAP.
    """

    rctoken_aud: wrappers_pb2.StringValue = proto.Field(
        proto.MESSAGE,
        number=1,
        message=wrappers_pb2.StringValue,
    )


class AccessDeniedPageSettings(proto.Message):
    r"""Custom content configuration for access denied page.
    IAP allows customers to define a custom URI to use as the error
    page when access is denied to users. If IAP prevents access to
    this page, the default IAP error page will be displayed instead.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        access_denied_page_uri (google.protobuf.wrappers_pb2.StringValue):
            The URI to be redirected to when access is
            denied.
        generate_troubleshooting_uri (google.protobuf.wrappers_pb2.BoolValue):
            Whether to generate a troubleshooting URL on
            access denied events to this application.
        remediation_token_generation_enabled (google.protobuf.wrappers_pb2.BoolValue):
            Whether to generate remediation token on
            access denied events to this application.

            This field is a member of `oneof`_ ``_remediation_token_generation_enabled``.
    """

    access_denied_page_uri: wrappers_pb2.StringValue = proto.Field(
        proto.MESSAGE,
        number=1,
        message=wrappers_pb2.StringValue,
    )
    generate_troubleshooting_uri: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=2,
        message=wrappers_pb2.BoolValue,
    )
    remediation_token_generation_enabled: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=3,
        optional=True,
        message=wrappers_pb2.BoolValue,
    )


class AttributePropagationSettings(proto.Message):
    r"""Configuration for propagating attributes to applications
    protected by IAP.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        expression (str):
            Optional. Raw string CEL expression. Must return a list of
            attributes. A maximum of 45 attributes can be selected.
            Expressions can select different attribute types from
            ``attributes``: ``attributes.saml_attributes``,
            ``attributes.iap_attributes``. The following functions are
            supported:

            - filter ``<list>.filter(<iter_var>, <predicate>)``: Returns
              a subset of ``<list>`` where ``<predicate>`` is true for
              every item.

            - in ``<var> in <list>``: Returns true if ``<list>``
              contains ``<var>``.

            - selectByName ``<list>.selectByName(<string>)``: Returns
              the attribute in ``<list>`` with the given ``<string>``
              name, otherwise returns empty.

            - emitAs ``<attribute>.emitAs(<string>)``: Sets the
              ``<attribute>`` name field to the given ``<string>`` for
              propagation in selected output credentials.

            - strict ``<attribute>.strict()``: Ignores the
              ``x-goog-iap-attr-`` prefix for the provided
              ``<attribute>`` when propagating with the ``HEADER``
              output credential, such as request headers.

            - append ``<target_list>.append(<attribute>)`` OR
              ``<target_list>.append(<list>)``: Appends the provided
              ``<attribute>`` or ``<list>`` to the end of
              ``<target_list>``.

            Example expression:
            ``attributes.saml_attributes.filter(x, x.name in ['test']).append(attributes.iap_attributes.selectByName('exact').emitAs('custom').strict())``

            This field is a member of `oneof`_ ``_expression``.
        output_credentials (MutableSequence[google.cloud.iap_v1.types.AttributePropagationSettings.OutputCredentials]):
            Optional. Which output credentials attributes
            selected by the CEL expression should be
            propagated in. All attributes will be fully
            duplicated in each selected output credential.
        enable (bool):
            Optional. Whether the provided attribute
            propagation settings should be evaluated on user
            requests. If set to true, attributes returned
            from the expression will be propagated in the
            set output credentials.

            This field is a member of `oneof`_ ``_enable``.
    """

    class OutputCredentials(proto.Enum):
        r"""Supported output credentials for attribute propagation. Each
        output credential maps to a "field" in the response. For
        example, selecting JWT will propagate all attributes in the IAP
        JWT, header in the headers, etc.

        Values:
            OUTPUT_CREDENTIALS_UNSPECIFIED (0):
                An output credential is required.
            HEADER (1):
                Propagate attributes in the headers with
                "x-goog-iap-attr-" prefix.
            JWT (2):
                Propagate attributes in the JWT of the form:
                ``"additional_claims": { "my_attribute": ["value1", "value2"] }``
            RCTOKEN (3):
                Propagate attributes in the RCToken of the form:
                ``"additional_claims": { "my_attribute": ["value1", "value2"] }``
        """

        OUTPUT_CREDENTIALS_UNSPECIFIED = 0
        HEADER = 1
        JWT = 2
        RCTOKEN = 3

    expression: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    output_credentials: MutableSequence[OutputCredentials] = proto.RepeatedField(
        proto.ENUM,
        number=2,
        enum=OutputCredentials,
    )
    enable: bool = proto.Field(
        proto.BOOL,
        number=3,
        optional=True,
    )


class ValidateIapAttributeExpressionRequest(proto.Message):
    r"""Request sent to IAP Expression Linter endpoint.

    Attributes:
        name (str):
            Required. The resource name of the IAP
            protected resource.
        expression (str):
            Required. User input string expression. Should be of the
            form
            ``attributes.saml_attributes.filter(attribute, attribute.name in ['{attribute_name}', '{attribute_name}'])``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    expression: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ValidateIapAttributeExpressionResponse(proto.Message):
    r"""IAP Expression Linter endpoint returns empty response body."""


class ListBrandsRequest(proto.Message):
    r"""The request sent to ListBrands.

    Attributes:
        parent (str):
            Required. GCP Project number/id. In the following format:
            projects/{project_number/id}.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListBrandsResponse(proto.Message):
    r"""Response message for ListBrands.

    Attributes:
        brands (MutableSequence[google.cloud.iap_v1.types.Brand]):
            Brands existing in the project.
    """

    brands: MutableSequence["Brand"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Brand",
    )


class CreateBrandRequest(proto.Message):
    r"""The request sent to CreateBrand.

    Attributes:
        parent (str):
            Required. GCP Project number/id under which the brand is to
            be created. In the following format:
            projects/{project_number/id}.
        brand (google.cloud.iap_v1.types.Brand):
            Required. The brand to be created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    brand: "Brand" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Brand",
    )


class GetBrandRequest(proto.Message):
    r"""The request sent to GetBrand.

    Attributes:
        name (str):
            Required. Name of the brand to be fetched. In the following
            format: projects/{project_number/id}/brands/{brand}.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListIdentityAwareProxyClientsRequest(proto.Message):
    r"""The request sent to ListIdentityAwareProxyClients.

    Attributes:
        parent (str):
            Required. Full brand path. In the following format:
            projects/{project_number/id}/brands/{brand}.
        page_size (int):
            The maximum number of clients to return. The
            service may return fewer than this value.
            If unspecified, at most 100 clients will be
            returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            A page token, received from a previous
            ``ListIdentityAwareProxyClients`` call. Provide this to
            retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListIdentityAwareProxyClients`` must match the call that
            provided the page token.
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


class ListIdentityAwareProxyClientsResponse(proto.Message):
    r"""Response message for ListIdentityAwareProxyClients.

    Attributes:
        identity_aware_proxy_clients (MutableSequence[google.cloud.iap_v1.types.IdentityAwareProxyClient]):
            Clients existing in the brand.
        next_page_token (str):
            A token, which can be send as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    identity_aware_proxy_clients: MutableSequence["IdentityAwareProxyClient"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="IdentityAwareProxyClient",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateIdentityAwareProxyClientRequest(proto.Message):
    r"""The request sent to CreateIdentityAwareProxyClient.

    Attributes:
        parent (str):
            Required. Path to create the client in. In the following
            format: projects/{project_number/id}/brands/{brand}. The
            project must belong to a G Suite account.
        identity_aware_proxy_client (google.cloud.iap_v1.types.IdentityAwareProxyClient):
            Required. Identity Aware Proxy Client to be
            created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    identity_aware_proxy_client: "IdentityAwareProxyClient" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="IdentityAwareProxyClient",
    )


class GetIdentityAwareProxyClientRequest(proto.Message):
    r"""The request sent to GetIdentityAwareProxyClient.

    Attributes:
        name (str):
            Required. Name of the Identity Aware Proxy client to be
            fetched. In the following format:
            projects/{project_number/id}/brands/{brand}/identityAwareProxyClients/{client_id}.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ResetIdentityAwareProxyClientSecretRequest(proto.Message):
    r"""The request sent to ResetIdentityAwareProxyClientSecret.

    Attributes:
        name (str):
            Required. Name of the Identity Aware Proxy client to that
            will have its secret reset. In the following format:
            projects/{project_number/id}/brands/{brand}/identityAwareProxyClients/{client_id}.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteIdentityAwareProxyClientRequest(proto.Message):
    r"""The request sent to DeleteIdentityAwareProxyClient.

    Attributes:
        name (str):
            Required. Name of the Identity Aware Proxy client to be
            deleted. In the following format:
            projects/{project_number/id}/brands/{brand}/identityAwareProxyClients/{client_id}.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Brand(proto.Message):
    r"""OAuth brand data.
    NOTE: Only contains a portion of the data that describes a
    brand.

    Attributes:
        name (str):
            Output only. Identifier of the brand.
            NOTE: GCP project number achieves the same brand
            identification purpose as only one brand per
            project can be created.
        support_email (str):
            Support email displayed on the OAuth consent
            screen.
        application_title (str):
            Application name displayed on OAuth consent
            screen.
        org_internal_only (bool):
            Output only. Whether the brand is only
            intended for usage inside the G Suite
            organization only.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    support_email: str = proto.Field(
        proto.STRING,
        number=2,
    )
    application_title: str = proto.Field(
        proto.STRING,
        number=3,
    )
    org_internal_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class IdentityAwareProxyClient(proto.Message):
    r"""Contains the data that describes an Identity Aware Proxy
    owned client.

    Attributes:
        name (str):
            Output only. Unique identifier of the OAuth
            client.
        secret (str):
            Output only. Client secret of the OAuth
            client.
        display_name (str):
            Human-friendly name given to the OAuth
            client.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    secret: str = proto.Field(
        proto.STRING,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
