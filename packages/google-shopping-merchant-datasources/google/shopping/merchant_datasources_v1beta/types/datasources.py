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

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import proto  # type: ignore

from google.shopping.merchant_datasources_v1beta.types import (
    datasourcetypes,
    fileinputs,
)

__protobuf__ = proto.module(
    package="google.shopping.merchant.datasources.v1beta",
    manifest={
        "DataSource",
        "GetDataSourceRequest",
        "ListDataSourcesRequest",
        "ListDataSourcesResponse",
        "CreateDataSourceRequest",
        "UpdateDataSourceRequest",
        "FetchDataSourceRequest",
        "DeleteDataSourceRequest",
    },
)


class DataSource(proto.Message):
    r"""The `data
    source <https://support.google.com/merchants/answer/7439058>`__ for
    the Merchant Center account.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        primary_product_data_source (google.shopping.merchant_datasources_v1beta.types.PrimaryProductDataSource):
            The `primary data
            source <https://support.google.com/merchants/answer/7439058>`__
            for local and online products.

            This field is a member of `oneof`_ ``Type``.
        supplemental_product_data_source (google.shopping.merchant_datasources_v1beta.types.SupplementalProductDataSource):
            The `supplemental data
            source <https://support.google.com/merchants/answer/7439058>`__
            for local and online products.

            This field is a member of `oneof`_ ``Type``.
        local_inventory_data_source (google.shopping.merchant_datasources_v1beta.types.LocalInventoryDataSource):
            The `local
            inventory <https://support.google.com/merchants/answer/7023001>`__
            data source.

            This field is a member of `oneof`_ ``Type``.
        regional_inventory_data_source (google.shopping.merchant_datasources_v1beta.types.RegionalInventoryDataSource):
            The `regional
            inventory <https://support.google.com/merchants/answer/7439058>`__
            data source.

            This field is a member of `oneof`_ ``Type``.
        promotion_data_source (google.shopping.merchant_datasources_v1beta.types.PromotionDataSource):
            The
            `promotion <https://support.google.com/merchants/answer/2906014>`__
            data source.

            This field is a member of `oneof`_ ``Type``.
        product_review_data_source (google.shopping.merchant_datasources_v1beta.types.ProductReviewDataSource):
            The `product
            review <https://support.google.com/merchants/answer/7045996>`__
            data source.

            This field is a member of `oneof`_ ``Type``.
        merchant_review_data_source (google.shopping.merchant_datasources_v1beta.types.MerchantReviewDataSource):
            The `merchant
            review <https://support.google.com/merchants/answer/7045996>`__
            data source.

            This field is a member of `oneof`_ ``Type``.
        name (str):
            Identifier. The name of the data source. Format:
            ``{datasource.name=accounts/{account}/dataSources/{datasource}}``
        data_source_id (int):
            Output only. The data source id.
        display_name (str):
            Required. The displayed data source name in
            the Merchant Center UI.
        input (google.shopping.merchant_datasources_v1beta.types.DataSource.Input):
            Output only. Determines the type of input to
            the data source. Based on the input some
            settings might not work. Only generic data
            sources can be created through the API.
        file_input (google.shopping.merchant_datasources_v1beta.types.FileInput):
            Optional. The field is used only when data is
            managed through a file.
    """

    class Input(proto.Enum):
        r"""Determines the type of input to the data source. Based on the
        input some settings might not be supported.

        Values:
            INPUT_UNSPECIFIED (0):
                Input unspecified.
            API (1):
                Represents data sources for which the data is
                primarily provided through the API.
            FILE (2):
                Represents data sources for which the data is
                primarily provided through file input. Data can
                still be provided through the API.
            UI (3):
                The data source for products added directly
                in Merchant Center.
                This type of data source can not be created or
                updated through this API, only by Merchant
                Center UI.

                This type of data source is read only.
            AUTOFEED (4):
                This is also known as `Automated
                feeds <https://support.google.com/merchants/answer/12158480>`__
                used to automatically build your product data. This type of
                data source can be enabled or disabled through the Accounts
                bundle.
        """

        INPUT_UNSPECIFIED = 0
        API = 1
        FILE = 2
        UI = 3
        AUTOFEED = 4

    primary_product_data_source: datasourcetypes.PrimaryProductDataSource = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="Type",
        message=datasourcetypes.PrimaryProductDataSource,
    )
    supplemental_product_data_source: datasourcetypes.SupplementalProductDataSource = (
        proto.Field(
            proto.MESSAGE,
            number=5,
            oneof="Type",
            message=datasourcetypes.SupplementalProductDataSource,
        )
    )
    local_inventory_data_source: datasourcetypes.LocalInventoryDataSource = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="Type",
        message=datasourcetypes.LocalInventoryDataSource,
    )
    regional_inventory_data_source: datasourcetypes.RegionalInventoryDataSource = (
        proto.Field(
            proto.MESSAGE,
            number=7,
            oneof="Type",
            message=datasourcetypes.RegionalInventoryDataSource,
        )
    )
    promotion_data_source: datasourcetypes.PromotionDataSource = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="Type",
        message=datasourcetypes.PromotionDataSource,
    )
    product_review_data_source: datasourcetypes.ProductReviewDataSource = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="Type",
        message=datasourcetypes.ProductReviewDataSource,
    )
    merchant_review_data_source: datasourcetypes.MerchantReviewDataSource = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="Type",
        message=datasourcetypes.MerchantReviewDataSource,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_source_id: int = proto.Field(
        proto.INT64,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    input: Input = proto.Field(
        proto.ENUM,
        number=10,
        enum=Input,
    )
    file_input: fileinputs.FileInput = proto.Field(
        proto.MESSAGE,
        number=11,
        message=fileinputs.FileInput,
    )


class GetDataSourceRequest(proto.Message):
    r"""Request message for the GetDataSource method.

    Attributes:
        name (str):
            Required. The name of the data source to retrieve. Format:
            ``accounts/{account}/dataSources/{datasource}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListDataSourcesRequest(proto.Message):
    r"""Request message for the ListDataSources method.

    Attributes:
        parent (str):
            Required. The account to list data sources for. Format:
            ``accounts/{account}``
        page_size (int):
            Optional. The maximum number of data sources
            to return. The service may return fewer than
            this value. The maximum value is 1000; values
            above 1000 will be coerced to 1000. If
            unspecified, the maximum number of data sources
            will be returned.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListDataSources`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListDataSources`` must match the call that provided the
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


class ListDataSourcesResponse(proto.Message):
    r"""Response message for the ListDataSources method.

    Attributes:
        data_sources (MutableSequence[google.shopping.merchant_datasources_v1beta.types.DataSource]):
            The data sources from the specified account.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    data_sources: MutableSequence["DataSource"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DataSource",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateDataSourceRequest(proto.Message):
    r"""Request message for the CreateDataSource method.

    Attributes:
        parent (str):
            Required. The account where this data source will be
            created. Format: ``accounts/{account}``
        data_source (google.shopping.merchant_datasources_v1beta.types.DataSource):
            Required. The data source to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_source: "DataSource" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DataSource",
    )


class UpdateDataSourceRequest(proto.Message):
    r"""Request message for the UpdateDataSource method.

    Attributes:
        data_source (google.shopping.merchant_datasources_v1beta.types.DataSource):
            Required. The data source resource to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of data source fields to be updated.

            Fields specified in the update mask without a value
            specified in the body will be deleted from the data source.

            Providing special "\*" value for full data source
            replacement is not supported.
    """

    data_source: "DataSource" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="DataSource",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class FetchDataSourceRequest(proto.Message):
    r"""Request message for the FetchDataSource method.

    Attributes:
        name (str):
            Required. The name of the data source resource to fetch.
            Format: ``accounts/{account}/dataSources/{datasource}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteDataSourceRequest(proto.Message):
    r"""Request message for the DeleteDataSource method.

    Attributes:
        name (str):
            Required. The name of the data source to delete. Format:
            ``accounts/{account}/dataSources/{datasource}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
