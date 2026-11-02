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

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.retail.v2alpha",
    manifest={
        "MerchantCenterAccountLink",
        "CreateMerchantCenterAccountLinkMetadata",
    },
)


class MerchantCenterAccountLink(proto.Message):
    r"""Represents a link between a Merchant Center account and a
    branch. After a link is established, products from the linked
    Merchant Center account are streamed to the linked branch.

    Attributes:
        name (str):
            Output only. Immutable. Full resource name of the Merchant
            Center Account Link, such as
            ``projects/*/locations/global/catalogs/default_catalog/merchantCenterAccountLinks/merchant_center_account_link``.
        id (str):
            Output only. Immutable.
            [MerchantCenterAccountLink][google.cloud.retail.v2alpha.MerchantCenterAccountLink]
            identifier, which is the final component of
            [name][google.cloud.retail.v2alpha.MerchantCenterAccountLink.name].
            This field is auto generated and follows the convention:
            ``BranchId_MerchantCenterAccountId``.
            ``projects/*/locations/global/catalogs/default_catalog/merchantCenterAccountLinks/id_1``.
        merchant_center_account_id (int):
            Required. The linked `Merchant center account
            id <https://developers.google.com/shopping-content/guides/accountstatuses>`__.
            The account must be a standalone account or a sub-account of
            a MCA.
        branch_id (str):
            Required. The branch ID (e.g. 0/1/2) within the catalog that
            products from merchant_center_account_id are streamed to.
            When updating this field, an empty value will use the
            currently configured default branch. However, changing the
            default branch later on won't change the linked branch here.

            A single branch ID can only have one linked Merchant Center
            account ID.
        feed_label (str):
            The FeedLabel used to perform filtering. Note: this replaces
            `region_id <https://developers.google.com/shopping-content/reference/rest/v2.1/products#Product.FIELDS.feed_label>`__.

            Example value: ``US``. Example value: ``FeedLabel1``.
        language_code (str):
            Language of the title/description and other string
            attributes. Use language tags defined by `BCP
            47 <https://www.rfc-editor.org/rfc/bcp/bcp47.txt>`__. ISO
            639-1.

            This specifies the language of offers in Merchant Center
            that will be accepted. If empty, no language filtering will
            be performed.

            Example value: ``en``.
        feed_filters (MutableSequence[google.cloud.retail_v2alpha.types.MerchantCenterAccountLink.MerchantCenterFeedFilter]):
            Criteria for the Merchant Center feeds to be
            ingested via the link. All offers will be
            ingested if the list is empty. Otherwise the
            offers will be ingested from selected feeds.
        state (google.cloud.retail_v2alpha.types.MerchantCenterAccountLink.State):
            Output only. Represents the state of the
            link.
        project_id (str):
            Output only. Google Cloud project ID.
        source (str):
            Optional. An optional arbitrary string that
            could be used as a tag for tracking link source.
    """

    class State(proto.Enum):
        r"""The state of the link.

        Values:
            STATE_UNSPECIFIED (0):
                Default value.
            PENDING (1):
                Link is created and LRO is not complete.
            ACTIVE (2):
                Link is active.
            FAILED (3):
                Link creation failed.
        """

        STATE_UNSPECIFIED = 0
        PENDING = 1
        ACTIVE = 2
        FAILED = 3

    class MerchantCenterFeedFilter(proto.Message):
        r"""Merchant Center Feed filter criterion.

        Attributes:
            primary_feed_id (int):
                Merchant Center primary feed ID. Deprecated: use
                data_source_id instead.
            data_source_id (int):
                AFM data source ID.
            primary_feed_name (str):
                Merchant Center primary feed name. The name
                is used for the display purposes only.
        """

        primary_feed_id: int = proto.Field(
            proto.INT64,
            number=1,
        )
        data_source_id: int = proto.Field(
            proto.INT64,
            number=3,
        )
        primary_feed_name: str = proto.Field(
            proto.STRING,
            number=2,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    id: str = proto.Field(
        proto.STRING,
        number=8,
    )
    merchant_center_account_id: int = proto.Field(
        proto.INT64,
        number=2,
    )
    branch_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    feed_label: str = proto.Field(
        proto.STRING,
        number=4,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=5,
    )
    feed_filters: MutableSequence[MerchantCenterFeedFilter] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=MerchantCenterFeedFilter,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=7,
        enum=State,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=9,
    )
    source: str = proto.Field(
        proto.STRING,
        number=10,
    )


class CreateMerchantCenterAccountLinkMetadata(proto.Message):
    r"""Common metadata related to the progress of the operations.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Operation create time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Operation last update time. If the operation
            is done, this is also the finish time.
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
