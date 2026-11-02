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
    package="google.cloud.securitycenter.v1",
    manifest={
        "Access",
        "ServiceAccountDelegationInfo",
        "Geolocation",
    },
)


class Access(proto.Message):
    r"""Represents an access event.

    Attributes:
        principal_email (str):
            Associated email, such as "foo@google.com".

            The email address of the authenticated user or a service
            account acting on behalf of a third party principal making
            the request. For third party identity callers, the
            ``principal_subject`` field is populated instead of this
            field. For privacy reasons, the principal email address is
            sometimes redacted. For more information, see `Caller
            identities in audit
            logs <https://cloud.google.com/logging/docs/audit#user-id>`__.
        caller_ip (str):
            Caller's IP address, such as "1.1.1.1".
        caller_ip_geo (google.cloud.securitycenter_v1.types.Geolocation):
            The caller IP's geolocation, which identifies
            where the call came from.
        user_agent_family (str):
            Type of user agent associated with the
            finding. For example, an operating system shell
            or an embedded or standalone application.
        user_agent (str):
            The caller's user agent string associated
            with the finding.
        service_name (str):
            This is the API service that the service
            account made a call to, e.g.
            "iam.googleapis.com".
        method_name (str):
            The method that the service account called,
            e.g. "SetIamPolicy".
        principal_subject (str):
            A string that represents the principal_subject that is
            associated with the identity. Unlike ``principal_email``,
            ``principal_subject`` supports principals that aren't
            associated with email addresses, such as third party
            principals. For most identities, the format is
            ``principal://iam.googleapis.com/{identity pool name}/subject/{subject}``.
            Some GKE identities, such as GKE_WORKLOAD, FREEFORM, and
            GKE_HUB_WORKLOAD, still use the legacy format
            ``serviceAccount:{identity pool name}[{subject}]``.
        service_account_key_name (str):
            The name of the service account key that was used to create
            or exchange credentials when authenticating the service
            account that made the request. This is a scheme-less URI
            full resource name. For example:

            "//iam.googleapis.com/projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}/keys/{key}".
        service_account_delegation_info (MutableSequence[google.cloud.securitycenter_v1.types.ServiceAccountDelegationInfo]):
            The identity delegation history of an authenticated service
            account that made the request. The
            ``serviceAccountDelegationInfo[]`` object contains
            information about the real authorities that try to access
            Google Cloud resources by delegating on a service account.
            When multiple authorities are present, they are guaranteed
            to be sorted based on the original ordering of the identity
            delegation events.
        user_name (str):
            A string that represents a username. The
            username provided depends on the type of the
            finding and is likely not an IAM principal. For
            example, this can be a system username if the
            finding is related to a virtual machine, or it
            can be an application login username.
    """

    principal_email: str = proto.Field(
        proto.STRING,
        number=1,
    )
    caller_ip: str = proto.Field(
        proto.STRING,
        number=2,
    )
    caller_ip_geo: "Geolocation" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Geolocation",
    )
    user_agent_family: str = proto.Field(
        proto.STRING,
        number=4,
    )
    user_agent: str = proto.Field(
        proto.STRING,
        number=12,
    )
    service_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    method_name: str = proto.Field(
        proto.STRING,
        number=6,
    )
    principal_subject: str = proto.Field(
        proto.STRING,
        number=7,
    )
    service_account_key_name: str = proto.Field(
        proto.STRING,
        number=8,
    )
    service_account_delegation_info: MutableSequence["ServiceAccountDelegationInfo"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=9,
            message="ServiceAccountDelegationInfo",
        )
    )
    user_name: str = proto.Field(
        proto.STRING,
        number=11,
    )


class ServiceAccountDelegationInfo(proto.Message):
    r"""Identity delegation history of an authenticated service
    account.

    Attributes:
        principal_email (str):
            The email address of a Google account.
        principal_subject (str):
            A string representing the principal_subject associated with
            the identity. As compared to ``principal_email``, supports
            principals that aren't associated with email addresses, such
            as third party principals. For most identities, the format
            will be
            ``principal://iam.googleapis.com/{identity pool name}/subjects/{subject}``
            except for some GKE identities (GKE_WORKLOAD, FREEFORM,
            GKE_HUB_WORKLOAD) that are still in the legacy format
            ``serviceAccount:{identity pool name}[{subject}]``
    """

    principal_email: str = proto.Field(
        proto.STRING,
        number=1,
    )
    principal_subject: str = proto.Field(
        proto.STRING,
        number=2,
    )


class Geolocation(proto.Message):
    r"""Represents a geographical location for a given access.

    Attributes:
        region_code (str):
            A CLDR.
    """

    region_code: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
