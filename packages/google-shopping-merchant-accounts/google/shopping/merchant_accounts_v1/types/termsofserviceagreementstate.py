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

import google.type.date_pb2 as date_pb2  # type: ignore
import proto  # type: ignore

from google.shopping.merchant_accounts_v1.types import termsofservicekind

__protobuf__ = proto.module(
    package="google.shopping.merchant.accounts.v1",
    manifest={
        "TermsOfServiceAgreementState",
        "Accepted",
        "Required",
        "GetTermsOfServiceAgreementStateRequest",
        "RetrieveForApplicationTermsOfServiceAgreementStateRequest",
    },
)


class TermsOfServiceAgreementState(proto.Message):
    r"""This resource represents the agreement state for a given account and
    terms of service kind. The state is as follows:

    - If the business has accepted a terms of service,
      [``accepted``][google.shopping.merchant.accounts.v1.Accepted] will
      be populated, otherwise it will be empty
    - If the business must sign a terms of service,
      [``required``][google.shopping.merchant.accounts.v1.Required] will
      be populated, otherwise it will be empty.

    Note that both ``required`` and ``accepted`` can be present. In this
    case the ``accepted`` terms of services will have an expiration date
    set in the
    [``valid_until``][google.shopping.merchant.accounts.v1.Accepted.valid_until]
    field. The ``required`` terms of services need to be accepted before
    ``valid_until`` in order for the account to continue having a valid
    agreement. When accepting new terms of services we expect
    third-party providers to display the text associated with the given
    terms of service agreement (the url to the file containing the text
    is added in the Required message below as
    [``tos_file_uri``][google.shopping.merchant.accounts.v1.Required.tos_file_uri]).
    The actual acceptance of the terms of service is done by calling
    accept on the
    [``TermsOfService``][google.shopping.merchant.accounts.v1.Accepted.terms_of_service]
    resource. ``valid_until`` field.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the terms of service
            version. Format:
            ``accounts/{account}/termsOfServiceAgreementState/{identifier}``
            The identifier format is:
            ``{[TermsOfServiceKind][google.shopping.merchant.accounts.v1.TermsOfServiceKind]}-{country}``
            For example, an identifier could be: ``MERCHANT_CENTER-EU``
            or ``MERCHANT_CENTER-US``.
        region_code (str):
            Required. Region code as defined by
            https://cldr.unicode.org/. This is the country
            the current state applies to.
        terms_of_service_kind (google.shopping.merchant_accounts_v1.types.TermsOfServiceKind):
            Required. Terms of Service kind associated
            with the particular version.
        accepted (google.shopping.merchant_accounts_v1.types.Accepted):
            Optional. The accepted terms of service of this kind and for
            the associated region_code

            This field is a member of `oneof`_ ``_accepted``.
        required (google.shopping.merchant_accounts_v1.types.Required):
            Optional. The required terms of service

            This field is a member of `oneof`_ ``_required``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    region_code: str = proto.Field(
        proto.STRING,
        number=2,
    )
    terms_of_service_kind: termsofservicekind.TermsOfServiceKind = proto.Field(
        proto.ENUM,
        number=3,
        enum=termsofservicekind.TermsOfServiceKind,
    )
    accepted: "Accepted" = proto.Field(
        proto.MESSAGE,
        number=4,
        optional=True,
        message="Accepted",
    )
    required: "Required" = proto.Field(
        proto.MESSAGE,
        number=5,
        optional=True,
        message="Required",
    )


class Accepted(proto.Message):
    r"""Describes the `accepted terms of
    service <https://developers.google.com/merchant/api/guides/accounts/create-and-configure#accept_the_merchant_center_terms_of_service>`__.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        terms_of_service (str):
            Required. The accepted
            [termsOfService][google.shopping.merchant.accounts.v1.TermsOfService].
        accepted_by (str):
            Required. The account where the acceptance
            was recorded. This can be the account itself or,
            in the case of subaccounts, the advanced
            account.
        valid_until (google.type.date_pb2.Date):
            Optional. When set, it states that the accepted
            ``TermsOfService`` is only valid until the end of this date
            (in UTC). A new one must be accepted before then. The
            information of the required ``TermsOfService`` is found in
            the ``Required`` message.

            This field is a member of `oneof`_ ``_valid_until``.
    """

    terms_of_service: str = proto.Field(
        proto.STRING,
        number=1,
    )
    accepted_by: str = proto.Field(
        proto.STRING,
        number=2,
    )
    valid_until: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=3,
        optional=True,
        message=date_pb2.Date,
    )


class Required(proto.Message):
    r"""Describes the terms of service which are required to be
    accepted.

    Attributes:
        terms_of_service (str):
            Required. The ``TermsOfService`` that need to be accepted.
        tos_file_uri (str):
            Required. Full URL to the terms of service file. This field
            is the same as ``TermsOfService.file_uri``, it is added here
            for convenience only.
    """

    terms_of_service: str = proto.Field(
        proto.STRING,
        number=1,
    )
    tos_file_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetTermsOfServiceAgreementStateRequest(proto.Message):
    r"""Request message for the ``GetTermsOfServiceAgreementState`` method.

    Attributes:
        name (str):
            Required. The resource name of the terms of service version.
            Format:
            ``accounts/{account}/termsOfServiceAgreementStates/{identifier}``
            The identifier format is: ``{TermsOfServiceKind}-{country}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class RetrieveForApplicationTermsOfServiceAgreementStateRequest(proto.Message):
    r"""Request message for the
    ``RetrieveForApplicationTermsOfServiceAgreementState`` method.

    Attributes:
        parent (str):
            Required. The account for which to get a
            TermsOfServiceAgreementState Format: ``accounts/{account}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
