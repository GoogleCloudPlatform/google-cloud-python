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
    package="google.cloud.geminidataanalytics.v1",
    manifest={
        "Credentials",
        "OAuthCredentials",
    },
)


class Credentials(proto.Message):
    r"""Represents different forms of credential specification.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        oauth (google.cloud.geminidataanalytics_v1.types.OAuthCredentials):
            OAuth credentials.

            This field is a member of `oneof`_ ``kind``.
    """

    oauth: "OAuthCredentials" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="kind",
        message="OAuthCredentials",
    )


class OAuthCredentials(proto.Message):
    r"""Represents OAuth credentials.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        secret (google.cloud.geminidataanalytics_v1.types.OAuthCredentials.SecretBased):
            Secret-based OAuth credentials.

            This field is a member of `oneof`_ ``kind``.
        token (google.cloud.geminidataanalytics_v1.types.OAuthCredentials.TokenBased):
            Token-based OAuth credentials.

            This field is a member of `oneof`_ ``kind``.
    """

    class SecretBased(proto.Message):
        r"""The name of the secret containing the access token.
        Represents secret-based OAuth credentials.

        Attributes:
            client_id (str):
                Required. An OAuth client ID.
            client_secret (str):
                Required. An OAuth client secret.
        """

        client_id: str = proto.Field(
            proto.STRING,
            number=2,
        )
        client_secret: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class TokenBased(proto.Message):
        r"""Read more about Looker access tokens here:

        https://developers.looker.com/api/advanced-usage/looker-api-oauth

        Attributes:
            access_token (str):
                Required. The name of the secret containing
                the access token.
        """

        access_token: str = proto.Field(
            proto.STRING,
            number=1,
        )

    secret: SecretBased = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="kind",
        message=SecretBased,
    )
    token: TokenBased = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="kind",
        message=TokenBased,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
