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
    package="google.cloud.contentwarehouse.v1",
    manifest={
        "SynonymSet",
    },
)


class SynonymSet(proto.Message):
    r"""Represents a list of synonyms for a given context.
    For example a context "sales" could contain:

    Synonym 1: sale, invoice, bill, order
    Synonym 2: money, credit, finance, payment
    Synonym 3: shipping, freight, transport
    Each SynonymSets should be disjoint

    Attributes:
        name (str):
            The resource name of the SynonymSet This is mandatory for
            google.api.resource. Format:
            projects/{project_number}/locations/{location}/synonymSets/{context}.
        context (str):
            This is a freeform field. Example contexts
            can be "sales," "engineering," "real estate,"
            "accounting," etc. The context can be supplied
            during search requests.
        synonyms (MutableSequence[google.cloud.contentwarehouse_v1.types.SynonymSet.Synonym]):
            List of Synonyms for the context.
    """

    class Synonym(proto.Message):
        r"""Represents a list of words given by the customer
        All these words are synonyms of each other.

        Attributes:
            words (MutableSequence[str]):
                For example: sale, invoice, bill, order
        """

        words: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    context: str = proto.Field(
        proto.STRING,
        number=2,
    )
    synonyms: MutableSequence[Synonym] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=Synonym,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
