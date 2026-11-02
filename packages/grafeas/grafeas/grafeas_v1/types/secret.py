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

import google.protobuf.any_pb2 as any_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from grafeas.grafeas_v1.types import common

__protobuf__ = proto.module(
    package="grafeas.v1",
    manifest={
        "SecretKind",
        "SecretNote",
        "SecretOccurrence",
        "SecretLocation",
        "SecretStatus",
    },
)


class SecretKind(proto.Enum):
    r"""Kind of secret.

    Values:
        SECRET_KIND_UNSPECIFIED (0):
            Unspecified
        SECRET_KIND_UNKNOWN (1):
            The secret kind is unknown.
        SECRET_KIND_GCP_SERVICE_ACCOUNT_KEY (2):
            A Google Cloud service account key per:

            https://cloud.google.com/iam/docs/creating-managing-service-account-keys
        SECRET_KIND_GCP_API_KEY (3):
            A Google Cloud API key per:

            https://cloud.google.com/docs/authentication/api-keys
        SECRET_KIND_GCP_OAUTH2_CLIENT_CREDENTIALS (4):
            A Google Cloud OAuth2 client credentials per:
            https://developers.google.com/identity/protocols/oauth2
        SECRET_KIND_GCP_OAUTH2_ACCESS_TOKEN (5):
            A Google Cloud OAuth2 access token per:

            https://cloud.google.com/docs/authentication/token-types#access
        SECRET_KIND_ANTHROPIC_ADMIN_API_KEY (6):
            An Anthropic Admin API key.
        SECRET_KIND_ANTHROPIC_API_KEY (7):
            An Anthropic API key.
        SECRET_KIND_AZURE_ACCESS_TOKEN (8):
            An Azure access token.
        SECRET_KIND_AZURE_IDENTITY_TOKEN (9):
            An Azure Identity Platform ID token.
        SECRET_KIND_DOCKER_HUB_PERSONAL_ACCESS_TOKEN (10):
            A Docker Hub personal access token.
        SECRET_KIND_GITHUB_APP_REFRESH_TOKEN (11):
            A GitHub App refresh token.
        SECRET_KIND_GITHUB_APP_SERVER_TO_SERVER_TOKEN (12):
            A GitHub App server-to-server token.
        SECRET_KIND_GITHUB_APP_USER_TO_SERVER_TOKEN (13):
            A GitHub App user-to-server token.
        SECRET_KIND_GITHUB_CLASSIC_PERSONAL_ACCESS_TOKEN (14):
            A GitHub personal access token (classic).
        SECRET_KIND_GITHUB_FINE_GRAINED_PERSONAL_ACCESS_TOKEN (15):
            A GitHub fine-grained personal access token.
        SECRET_KIND_GITHUB_OAUTH_TOKEN (16):
            A GitHub OAuth token.
        SECRET_KIND_HUGGINGFACE_API_KEY (17):
            A Hugging Face API key.
        SECRET_KIND_OPENAI_API_KEY (18):
            An OpenAI API key.
        SECRET_KIND_PERPLEXITY_API_KEY (19):
            A Perplexity API key.
        SECRET_KIND_STRIPE_SECRET_KEY (20):
            A Stripe secret key.
        SECRET_KIND_STRIPE_RESTRICTED_KEY (21):
            A Stripe restricted key.
        SECRET_KIND_STRIPE_WEBHOOK_SECRET (22):
            A Stripe webhook secret.
    """

    SECRET_KIND_UNSPECIFIED = 0
    SECRET_KIND_UNKNOWN = 1
    SECRET_KIND_GCP_SERVICE_ACCOUNT_KEY = 2
    SECRET_KIND_GCP_API_KEY = 3
    SECRET_KIND_GCP_OAUTH2_CLIENT_CREDENTIALS = 4
    SECRET_KIND_GCP_OAUTH2_ACCESS_TOKEN = 5
    SECRET_KIND_ANTHROPIC_ADMIN_API_KEY = 6
    SECRET_KIND_ANTHROPIC_API_KEY = 7
    SECRET_KIND_AZURE_ACCESS_TOKEN = 8
    SECRET_KIND_AZURE_IDENTITY_TOKEN = 9
    SECRET_KIND_DOCKER_HUB_PERSONAL_ACCESS_TOKEN = 10
    SECRET_KIND_GITHUB_APP_REFRESH_TOKEN = 11
    SECRET_KIND_GITHUB_APP_SERVER_TO_SERVER_TOKEN = 12
    SECRET_KIND_GITHUB_APP_USER_TO_SERVER_TOKEN = 13
    SECRET_KIND_GITHUB_CLASSIC_PERSONAL_ACCESS_TOKEN = 14
    SECRET_KIND_GITHUB_FINE_GRAINED_PERSONAL_ACCESS_TOKEN = 15
    SECRET_KIND_GITHUB_OAUTH_TOKEN = 16
    SECRET_KIND_HUGGINGFACE_API_KEY = 17
    SECRET_KIND_OPENAI_API_KEY = 18
    SECRET_KIND_PERPLEXITY_API_KEY = 19
    SECRET_KIND_STRIPE_SECRET_KEY = 20
    SECRET_KIND_STRIPE_RESTRICTED_KEY = 21
    SECRET_KIND_STRIPE_WEBHOOK_SECRET = 22


class SecretNote(proto.Message):
    r"""The note representing a secret."""


class SecretOccurrence(proto.Message):
    r"""The occurrence provides details of a secret.

    Attributes:
        kind (grafeas.grafeas_v1.types.SecretKind):
            Type of secret.
        locations (MutableSequence[grafeas.grafeas_v1.types.SecretLocation]):
            Locations where the secret is detected.
        statuses (MutableSequence[grafeas.grafeas_v1.types.SecretStatus]):
            Status of the secret.
        data (google.protobuf.any_pb2.Any):
            Scan result of the secret.
        digest (grafeas.grafeas_v1.types.Digest):
            Hash value, typically a digest for the secret
            data, that allows unique identification of a
            specific secret.
    """

    kind: "SecretKind" = proto.Field(
        proto.ENUM,
        number=1,
        enum="SecretKind",
    )
    locations: MutableSequence["SecretLocation"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="SecretLocation",
    )
    statuses: MutableSequence["SecretStatus"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="SecretStatus",
    )
    data: any_pb2.Any = proto.Field(
        proto.MESSAGE,
        number=4,
        message=any_pb2.Any,
    )
    digest: common.Digest = proto.Field(
        proto.MESSAGE,
        number=5,
        message=common.Digest,
    )


class SecretLocation(proto.Message):
    r"""The location of the secret.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        file_location (grafeas.grafeas_v1.types.FileLocation):
            The secret is found from a file.

            This field is a member of `oneof`_ ``location``.
    """

    file_location: common.FileLocation = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="location",
        message=common.FileLocation,
    )


class SecretStatus(proto.Message):
    r"""The status of the secret with a timestamp.

    Attributes:
        status (grafeas.grafeas_v1.types.SecretStatus.Status):
            The status of the secret.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the secret status was last updated.
        message (str):
            Optional message about the status code.
    """

    class Status(proto.Enum):
        r"""The status of the secret.

        Values:
            STATUS_UNSPECIFIED (0):
                Unspecified
            UNKNOWN (1):
                The status of the secret is unknown.
            VALID (2):
                The secret is valid.
            INVALID (3):
                The secret is invalid.
        """

        STATUS_UNSPECIFIED = 0
        UNKNOWN = 1
        VALID = 2
        INVALID = 3

    status: Status = proto.Field(
        proto.ENUM,
        number=1,
        enum=Status,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    message: str = proto.Field(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
