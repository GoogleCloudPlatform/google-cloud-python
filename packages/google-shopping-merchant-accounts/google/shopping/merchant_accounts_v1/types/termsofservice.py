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

from google.shopping.merchant_accounts_v1.types import (
    termsofserviceagreementstate,
    termsofservicekind,
)

__protobuf__ = proto.module(
    package="google.shopping.merchant.accounts.v1",
    manifest={
        "TermsOfService",
        "GetTermsOfServiceRequest",
        "RetrieveLatestTermsOfServiceRequest",
        "AcceptTermsOfServiceRequest",
        "AcceptTermsOfServiceResponse",
    },
)


class TermsOfService(proto.Message):
    r"""The ``TermsOfService`` message represents a specific version of the
    terms of service that merchants must accept to access certain
    features or services. For more information, see `Terms of
    Service <https://support.google.com/merchants/answer/160173>`__.

    This message is important for the onboarding process, ensuring that
    merchants agree to the necessary legal agreements for using the
    service. Merchants can retrieve the latest terms of service for a
    given ``kind`` and ``region`` through
    ``RetrieveLatestTermsOfService``, and accept them as required
    through ``AcceptTermsOfService``.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the terms of service
            version. Format: ``termsOfService/{version}``
        region_code (str):
            Region code as defined by
            `CLDR <https://cldr.unicode.org/>`__. This is either a
            country where the ToS applies specifically to that country
            or ``001`` when the same ``TermsOfService`` can be signed in
            any country. However note that when signing a ToS that
            applies globally we still expect that a specific country is
            provided (this should be merchant business country or
            program country of participation).
        kind (google.shopping.merchant_accounts_v1.types.TermsOfServiceKind):
            The Kind this terms of service version
            applies to.
        file_uri (str):
            URI for terms of service file that needs to
            be displayed to signing users.

            This field is a member of `oneof`_ ``_file_uri``.
        external (bool):
            Whether this terms of service version is
            external. External terms of service versions can
            only be agreed through external processes and
            not directly by the merchant through UI or API.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    region_code: str = proto.Field(
        proto.STRING,
        number=2,
    )
    kind: termsofservicekind.TermsOfServiceKind = proto.Field(
        proto.ENUM,
        number=3,
        enum=termsofservicekind.TermsOfServiceKind,
    )
    file_uri: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    external: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class GetTermsOfServiceRequest(proto.Message):
    r"""Request message for the ``GetTermsOfService`` method.

    Attributes:
        name (str):
            Required. The resource name of the terms of service version.
            Format: ``termsOfService/{version}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class RetrieveLatestTermsOfServiceRequest(proto.Message):
    r"""Request message for the ``RetrieveLatestTermsOfService`` method.

    Attributes:
        region_code (str):
            Required. Region code as defined by
            `CLDR <https://cldr.unicode.org/>`__. This is either a
            country when the ToS applies specifically to that country or
            001 when it applies globally.
        kind (google.shopping.merchant_accounts_v1.types.TermsOfServiceKind):
            Required. The Kind this terms of service
            version applies to.
    """

    region_code: str = proto.Field(
        proto.STRING,
        number=1,
    )
    kind: termsofservicekind.TermsOfServiceKind = proto.Field(
        proto.ENUM,
        number=2,
        enum=termsofservicekind.TermsOfServiceKind,
    )


class AcceptTermsOfServiceRequest(proto.Message):
    r"""Request message for the ``AcceptTermsOfService`` method.

    Attributes:
        name (str):
            Required. The resource name of the terms of service version.
            Format: ``termsOfService/{version}``
        account (str):
            Required. The account for which to accept the ToS. Format:
            ``accounts/{account}``
        region_code (str):
            Required. Region code as defined by
            `CLDR <https://cldr.unicode.org/>`__. This is either a
            country when the ToS applies specifically to that country or
            001 when it applies globally.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    account: str = proto.Field(
        proto.STRING,
        number=2,
    )
    region_code: str = proto.Field(
        proto.STRING,
        number=3,
    )


class AcceptTermsOfServiceResponse(proto.Message):
    r"""Response message for the ``AcceptTermsOfService`` method.

    Attributes:
        terms_of_service_agreement_state (google.shopping.merchant_accounts_v1.types.TermsOfServiceAgreementState):
            The agreement state after accepting the ToS.
    """

    terms_of_service_agreement_state: termsofserviceagreementstate.TermsOfServiceAgreementState = proto.Field(
        proto.MESSAGE,
        number=1,
        message=termsofserviceagreementstate.TermsOfServiceAgreementState,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
