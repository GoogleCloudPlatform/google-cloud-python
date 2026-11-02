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
        "Program",
        "GetProgramRequest",
        "ListProgramsRequest",
        "ListProgramsResponse",
        "EnableProgramRequest",
        "DisableProgramRequest",
    },
)


class Program(proto.Message):
    r"""Defines participation in a given program for the specified account.

    Programs provide a mechanism for adding functionality to merchant
    accounts. A typical example of this is the `Free product
    listings <https://support.google.com/merchants/topic/9240261?ref_topic=7257954,7259405,&sjid=796648681813264022-EU>`__
    program, which enables products from a merchant's store to be shown
    across Google for free.

    Attributes:
        name (str):
            Identifier. The resource name of the program. Format:
            ``accounts/{account}/programs/{program}``
        documentation_uri (str):
            Output only. The URL of a Merchant Center
            help page describing the program.
        state (google.shopping.merchant_accounts_v1beta.types.Program.State):
            Output only. The participation state of the
            account in the program.
        active_region_codes (MutableSequence[str]):
            Output only. The regions in which the account is actively
            participating in the program. Active regions are defined as
            those where all program requirements affecting the regions
            have been met.

            Region codes are defined by
            `CLDR <https://cldr.unicode.org/>`__. This is either a
            country where the program applies specifically to that
            country or ``001`` when the program applies globally.
        unmet_requirements (MutableSequence[google.shopping.merchant_accounts_v1beta.types.Program.Requirement]):
            Output only. The requirements that the
            account has not yet satisfied that are affecting
            participation in the program.
    """

    class State(proto.Enum):
        r"""Possible program participation states for the account.

        Values:
            STATE_UNSPECIFIED (0):
                Default value. This value is unused.
            NOT_ELIGIBLE (1):
                The account is not eligible to participate in
                the program.
            ELIGIBLE (2):
                The account is eligible to participate in the
                program.
            ENABLED (3):
                The program is enabled for the account.
        """

        STATE_UNSPECIFIED = 0
        NOT_ELIGIBLE = 1
        ELIGIBLE = 2
        ENABLED = 3

    class Requirement(proto.Message):
        r"""Defines a requirement specified for participation in the
        program.

        Attributes:
            title (str):
                Output only. Name of the requirement.
            documentation_uri (str):
                Output only. The URL of a help page
                describing the requirement.
            affected_region_codes (MutableSequence[str]):
                Output only. The regions that are currently affected by this
                requirement not being met.

                Region codes are defined by
                `CLDR <https://cldr.unicode.org/>`__. This is either a
                country where the program applies specifically to that
                country or ``001`` when the program applies globally.
        """

        title: str = proto.Field(
            proto.STRING,
            number=1,
        )
        documentation_uri: str = proto.Field(
            proto.STRING,
            number=2,
        )
        affected_region_codes: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=3,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    documentation_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )
    active_region_codes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    unmet_requirements: MutableSequence[Requirement] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=Requirement,
    )


class GetProgramRequest(proto.Message):
    r"""Request message for the GetProgram method.

    Attributes:
        name (str):
            Required. The name of the program to retrieve. Format:
            ``accounts/{account}/programs/{program}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListProgramsRequest(proto.Message):
    r"""Request message for the ListPrograms method.

    Attributes:
        parent (str):
            Required. The name of the account for which to retrieve all
            programs. Format: ``accounts/{account}``
        page_size (int):
            Optional. The maximum number of programs to
            return in a single response. If unspecified (or
            0), a default size of 1000 is used. The maximum
            value is 1000; values above 1000 will be coerced
            to 1000.
        page_token (str):
            Optional. A continuation token, received from a previous
            ``ListPrograms`` call. Provide this to retrieve the next
            page.
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


class ListProgramsResponse(proto.Message):
    r"""Response message for the ListPrograms method.

    Attributes:
        programs (MutableSequence[google.shopping.merchant_accounts_v1beta.types.Program]):
            The programs for the given account.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    programs: MutableSequence["Program"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Program",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class EnableProgramRequest(proto.Message):
    r"""Request message for the EnableProgram method.

    Attributes:
        name (str):
            Required. The name of the program for which to enable
            participation for the given account. Format:
            ``accounts/{account}/programs/{program}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DisableProgramRequest(proto.Message):
    r"""Request message for the DisableProgram method.

    Attributes:
        name (str):
            Required. The name of the program for which to disable
            participation for the given account. Format:
            ``accounts/{account}/programs/{program}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
