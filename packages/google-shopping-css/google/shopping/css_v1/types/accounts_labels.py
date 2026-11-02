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
    package="google.shopping.css.v1",
    manifest={
        "AccountLabel",
        "ListAccountLabelsRequest",
        "ListAccountLabelsResponse",
        "CreateAccountLabelRequest",
        "UpdateAccountLabelRequest",
        "DeleteAccountLabelRequest",
    },
)


class AccountLabel(proto.Message):
    r"""Label assigned by CSS domain or CSS group to one of its
    sub-accounts.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the label.
            Format: accounts/{account}/labels/{label}
        label_id (int):
            Output only. The ID of the label.
        account_id (int):
            Output only. The ID of account this label
            belongs to.
        display_name (str):
            The display name of this label.

            This field is a member of `oneof`_ ``_display_name``.
        description (str):
            The description of this label.

            This field is a member of `oneof`_ ``_description``.
        label_type (google.shopping.css_v1.types.AccountLabel.LabelType):
            Output only. The type of this label.
    """

    class LabelType(proto.Enum):
        r"""The label type.

        Values:
            LABEL_TYPE_UNSPECIFIED (0):
                Unknown label type.
            MANUAL (1):
                Indicates that the label was created
                manually.
            AUTOMATIC (2):
                Indicates that the label was created
                automatically by CSS Center.
        """

        LABEL_TYPE_UNSPECIFIED = 0
        MANUAL = 1
        AUTOMATIC = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    label_id: int = proto.Field(
        proto.INT64,
        number=2,
    )
    account_id: int = proto.Field(
        proto.INT64,
        number=3,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    description: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    label_type: LabelType = proto.Field(
        proto.ENUM,
        number=6,
        enum=LabelType,
    )


class ListAccountLabelsRequest(proto.Message):
    r"""Request message for the ``ListAccountLabels`` method.

    Attributes:
        parent (str):
            Required. The parent account.
            Format: accounts/{account}
        page_size (int):
            The maximum number of labels to return. The
            service may return fewer than this value.
            If unspecified, at most 50 labels will be
            returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            A page token, received from a previous ``ListAccountLabels``
            call. Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListAccountLabels`` must match the call that provided the
            page token.
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


class ListAccountLabelsResponse(proto.Message):
    r"""Response message for the ``ListAccountLabels`` method.

    Attributes:
        account_labels (MutableSequence[google.shopping.css_v1.types.AccountLabel]):
            The labels from the specified account.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    account_labels: MutableSequence["AccountLabel"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AccountLabel",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateAccountLabelRequest(proto.Message):
    r"""Request message for the 'CreateAccountLanel' method.

    Attributes:
        parent (str):
            Required. The parent account.
            Format: accounts/{account}
        account_label (google.shopping.css_v1.types.AccountLabel):
            Required. The label to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    account_label: "AccountLabel" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="AccountLabel",
    )


class UpdateAccountLabelRequest(proto.Message):
    r"""Request message for the ``UpdateAccountLabel`` method.

    Attributes:
        account_label (google.shopping.css_v1.types.AccountLabel):
            Required. The updated label. All fields must
            be provided.
    """

    account_label: "AccountLabel" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="AccountLabel",
    )


class DeleteAccountLabelRequest(proto.Message):
    r"""Request message for the 'DeleteAccountLabel' method.

    Attributes:
        name (str):
            Required. The name of the label to delete.
            Format:  accounts/{account}/labels/{label}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
