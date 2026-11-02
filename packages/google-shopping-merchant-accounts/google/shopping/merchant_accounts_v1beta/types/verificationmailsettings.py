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
    package="google.shopping.merchant.accounts.v1beta",
    manifest={
        "VerificationMailSettings",
    },
)


class VerificationMailSettings(proto.Message):
    r"""Settings related to the verification email that is sent after
    adding a user.

    Attributes:
        verification_mail_mode (google.shopping.merchant_accounts_v1beta.types.VerificationMailSettings.VerificationMailMode):
            Optional. Mode of the verification mail. If not set, the
            default is ``SEND_VERIFICATION_MAIL``.
    """

    class VerificationMailMode(proto.Enum):
        r"""The different configuration options for sending a
        verification email when adding a user.

        Values:
            VERIFICATION_MAIL_MODE_UNSPECIFIED (0):
                Default first member of every enum. Do not
                use.
            SEND_VERIFICATION_MAIL (1):
                An invitation email is sent to the user added
                shortly after.
            SUPPRESS_VERIFICATION_MAIL (2):
                No invitation email is sent. This can be
                useful if the user is expected to accept the
                invitation through the API without needing
                another notification.
        """

        VERIFICATION_MAIL_MODE_UNSPECIFIED = 0
        SEND_VERIFICATION_MAIL = 1
        SUPPRESS_VERIFICATION_MAIL = 2

    verification_mail_mode: VerificationMailMode = proto.Field(
        proto.ENUM,
        number=1,
        enum=VerificationMailMode,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
