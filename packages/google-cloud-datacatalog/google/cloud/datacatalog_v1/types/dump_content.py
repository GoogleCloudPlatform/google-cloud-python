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

from google.cloud.datacatalog_v1.types import datacatalog, tags

__protobuf__ = proto.module(
    package="google.cloud.datacatalog.v1",
    manifest={
        "TaggedEntry",
        "DumpItem",
    },
)


class TaggedEntry(proto.Message):
    r"""Wrapper containing Entry and information about Tags
    that should and should not be attached to it.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        v1_entry (google.cloud.datacatalog_v1.types.Entry):
            Non-encrypted Data Catalog v1 Entry.

            This field is a member of `oneof`_ ``entry``.
        present_tags (MutableSequence[google.cloud.datacatalog_v1.types.Tag]):
            Optional. Tags that should be ingested into
            the Data Catalog. Caller should populate
            template name, column and fields.
        absent_tags (MutableSequence[google.cloud.datacatalog_v1.types.Tag]):
            Optional. Tags that should be deleted from
            the Data Catalog. Caller should populate
            template name and column only.
    """

    v1_entry: datacatalog.Entry = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="entry",
        message=datacatalog.Entry,
    )
    present_tags: MutableSequence[tags.Tag] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=tags.Tag,
    )
    absent_tags: MutableSequence[tags.Tag] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=tags.Tag,
    )


class DumpItem(proto.Message):
    r"""Wrapper for any item that can be contained in the dump.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        tagged_entry (google.cloud.datacatalog_v1.types.TaggedEntry):
            Entry and its tags.

            This field is a member of `oneof`_ ``item``.
    """

    tagged_entry: "TaggedEntry" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="item",
        message="TaggedEntry",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
