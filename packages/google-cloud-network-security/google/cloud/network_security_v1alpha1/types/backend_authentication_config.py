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

__protobuf__ = proto.module(
    package="google.cloud.networksecurity.v1alpha1",
    manifest={
        "BackendAuthenticationConfig",
        "ListBackendAuthenticationConfigsRequest",
        "ListBackendAuthenticationConfigsResponse",
        "GetBackendAuthenticationConfigRequest",
        "CreateBackendAuthenticationConfigRequest",
        "UpdateBackendAuthenticationConfigRequest",
        "DeleteBackendAuthenticationConfigRequest",
    },
)


class BackendAuthenticationConfig(proto.Message):
    r"""BackendAuthenticationConfig message groups the TrustConfig together
    with other settings that control how the load balancer
    authenticates, and expresses its identity to, the backend:

    - ``trustConfig`` is the attached TrustConfig.

    - ``wellKnownRoots`` indicates whether the load balance should trust
      backend server certificates that are issued by public certificate
      authorities, in addition to certificates trusted by the
      TrustConfig.

    - ``clientCertificate`` is a client certificate that the load
      balancer uses to express its identity to the backend, if the
      connection to the backend uses mTLS.

    You can attach the BackendAuthenticationConfig to the load
    balancer's BackendService directly determining how that
    BackendService negotiates TLS.

    Attributes:
        name (str):
            Required. Name of the BackendAuthenticationConfig resource.
            It matches the pattern
            ``projects/*/locations/{location}/backendAuthenticationConfigs/{backend_authentication_config}``
        description (str):
            Optional. Free-text description of the
            resource.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was updated.
        labels (MutableMapping[str, str]):
            Set of label tags associated with the
            resource.
        client_certificate (str):
            Optional. A reference to a
            certificatemanager.googleapis.com.Certificate resource. This
            is a relative resource path following the form
            "projects/{project}/locations/{location}/certificates/{certificate}".

            Used by a BackendService to negotiate mTLS when the backend
            connection uses TLS and the backend requests a client
            certificate. Must have a CLIENT_AUTH scope.
        trust_config (str):
            Optional. A reference to a TrustConfig resource from the
            certificatemanager.googleapis.com namespace. This is a
            relative resource path following the form
            "projects/{project}/locations/{location}/trustConfigs/{trust_config}".

            A BackendService uses the chain of trust represented by this
            TrustConfig, if specified, to validate the server
            certificates presented by the backend. Required unless
            wellKnownRoots is set to PUBLIC_ROOTS.
        well_known_roots (google.cloud.network_security_v1alpha1.types.BackendAuthenticationConfig.WellKnownRoots):
            Well known roots to use for server
            certificate validation.
        etag (str):
            Output only. Etag of the resource.
    """

    class WellKnownRoots(proto.Enum):
        r"""Enum to specify the well known roots to use for server
        certificate validation.

        Values:
            WELL_KNOWN_ROOTS_UNSPECIFIED (0):
                Equivalent to NONE.
            NONE (1):
                The BackendService will only validate server
                certificates against roots specified in
                TrustConfig.
            PUBLIC_ROOTS (2):
                The BackendService uses a set of well-known
                public roots, in addition to any roots specified
                in the trustConfig field, when validating the
                server certificates presented by the backend.
                Validation with these roots is only considered
                when the TlsSettings.sni field in the
                BackendService is set.

                The well-known roots are a set of root CAs
                managed by Google. CAs in this set can be added
                or removed without notice.
        """

        WELL_KNOWN_ROOTS_UNSPECIFIED = 0
        NONE = 1
        PUBLIC_ROOTS = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    client_certificate: str = proto.Field(
        proto.STRING,
        number=6,
    )
    trust_config: str = proto.Field(
        proto.STRING,
        number=7,
    )
    well_known_roots: WellKnownRoots = proto.Field(
        proto.ENUM,
        number=8,
        enum=WellKnownRoots,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=9,
    )


class ListBackendAuthenticationConfigsRequest(proto.Message):
    r"""Request used by the ListBackendAuthenticationConfigs method.

    Attributes:
        parent (str):
            Required. The project and location from which the
            BackendAuthenticationConfigs should be listed, specified in
            the format ``projects/*/locations/{location}``.
        page_size (int):
            Maximum number of
            BackendAuthenticationConfigs to return per call.
        page_token (str):
            The value returned by the last
            ``ListBackendAuthenticationConfigsResponse`` Indicates that
            this is a continuation of a prior
            ``ListBackendAuthenticationConfigs`` call, and that the
            system should return the next page of data.
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


class ListBackendAuthenticationConfigsResponse(proto.Message):
    r"""Response returned by the ListBackendAuthenticationConfigs
    method.

    Attributes:
        backend_authentication_configs (MutableSequence[google.cloud.network_security_v1alpha1.types.BackendAuthenticationConfig]):
            List of BackendAuthenticationConfig
            resources.
        next_page_token (str):
            If there might be more results than those appearing in this
            response, then ``next_page_token`` is included. To get the
            next set of results, call this method again using the value
            of ``next_page_token`` as ``page_token``.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    backend_authentication_configs: MutableSequence["BackendAuthenticationConfig"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="BackendAuthenticationConfig",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetBackendAuthenticationConfigRequest(proto.Message):
    r"""Request used by the GetBackendAuthenticationConfig method.

    Attributes:
        name (str):
            Required. A name of the BackendAuthenticationConfig to get.
            Must be in the format
            ``projects/*/locations/{location}/backendAuthenticationConfigs/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateBackendAuthenticationConfigRequest(proto.Message):
    r"""Request used by the CreateBackendAuthenticationConfig method.

    Attributes:
        parent (str):
            Required. The parent resource of the
            BackendAuthenticationConfig. Must be in the format
            ``projects/*/locations/{location}``.
        backend_authentication_config_id (str):
            Required. Short name of the
            BackendAuthenticationConfig resource to be
            created. This value should be 1-63 characters
            long, containing only letters, numbers, hyphens,
            and underscores, and should not start with a
            number. E.g. "backend-auth-config".
        backend_authentication_config (google.cloud.network_security_v1alpha1.types.BackendAuthenticationConfig):
            Required. BackendAuthenticationConfig
            resource to be created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    backend_authentication_config_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    backend_authentication_config: "BackendAuthenticationConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="BackendAuthenticationConfig",
    )


class UpdateBackendAuthenticationConfigRequest(proto.Message):
    r"""Request used by UpdateBackendAuthenticationConfig method.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the BackendAuthenticationConfig resource by
            the update. The fields specified in the update_mask are
            relative to the resource, not the full request. A field will
            be overwritten if it is in the mask. If the user does not
            provide a mask then all fields will be overwritten.
        backend_authentication_config (google.cloud.network_security_v1alpha1.types.BackendAuthenticationConfig):
            Required. Updated BackendAuthenticationConfig
            resource.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    backend_authentication_config: "BackendAuthenticationConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="BackendAuthenticationConfig",
    )


class DeleteBackendAuthenticationConfigRequest(proto.Message):
    r"""Request used by the DeleteBackendAuthenticationConfig method.

    Attributes:
        name (str):
            Required. A name of the BackendAuthenticationConfig to
            delete. Must be in the format
            ``projects/*/locations/{location}/backendAuthenticationConfigs/*``.
        etag (str):
            Optional. Etag of the resource.
            If this is provided, it must match the server's
            etag.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
