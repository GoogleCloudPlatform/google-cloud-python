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
import google.protobuf.wrappers_pb2 as wrappers_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.shopping.merchant.accounts.v1beta",
    manifest={
        "GetRegionRequest",
        "CreateRegionRequest",
        "UpdateRegionRequest",
        "DeleteRegionRequest",
        "ListRegionsRequest",
        "ListRegionsResponse",
        "Region",
    },
)


class GetRegionRequest(proto.Message):
    r"""Request message for the ``GetRegion`` method.

    Attributes:
        name (str):
            Required. The name of the region to retrieve. Format:
            ``accounts/{account}/regions/{region}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateRegionRequest(proto.Message):
    r"""Request message for the ``CreateRegion`` method.

    Attributes:
        parent (str):
            Required. The account to create a region for. Format:
            ``accounts/{account}``
        region_id (str):
            Required. The identifier for the region,
            unique over all regions of the same account.
        region (google.shopping.merchant_accounts_v1beta.types.Region):
            Required. The region to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    region_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    region: "Region" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Region",
    )


class UpdateRegionRequest(proto.Message):
    r"""Request message for the ``UpdateRegion`` method.

    Attributes:
        region (google.shopping.merchant_accounts_v1beta.types.Region):
            Required. The updated region.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The comma-separated field mask indicating the
            fields to update. Example:
            ``"displayName,postalCodeArea.regionCode"``.
    """

    region: "Region" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Region",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteRegionRequest(proto.Message):
    r"""Request message for the ``DeleteRegion`` method.

    Attributes:
        name (str):
            Required. The name of the region to delete. Format:
            ``accounts/{account}/regions/{region}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListRegionsRequest(proto.Message):
    r"""Request message for the ``ListRegions`` method.

    Attributes:
        parent (str):
            Required. The account to list regions for. Format:
            ``accounts/{account}``
        page_size (int):
            Optional. The maximum number of regions to
            return. The service may return fewer than this
            value. If unspecified, at most 50 regions will
            be returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListRegions`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListRegions`` must match the call that provided the page
            token.
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


class ListRegionsResponse(proto.Message):
    r"""Response message for the ``ListRegions`` method.

    Attributes:
        regions (MutableSequence[google.shopping.merchant_accounts_v1beta.types.Region]):
            The regions from the specified merchant.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    regions: MutableSequence["Region"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Region",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class Region(proto.Message):
    r"""Represents a geographic region that you can use as a target with
    both the ``RegionalInventory`` and ``ShippingSettings`` services.
    You can define regions as collections of either postal codes or, in
    some countries, using predefined geotargets. For more information,
    see `Set up
    regions <https://support.google.com/merchants/answer/7410946#zippy=%2Ccreate-a-new-region>`__
    for more information.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the region. Format:
            ``accounts/{account}/regions/{region}``
        display_name (str):
            Optional. The display name of the region.

            This field is a member of `oneof`_ ``_display_name``.
        postal_code_area (google.shopping.merchant_accounts_v1beta.types.Region.PostalCodeArea):
            Optional. A list of postal codes that defines
            the region area.
        geotarget_area (google.shopping.merchant_accounts_v1beta.types.Region.GeoTargetArea):
            Optional. A list of geotargets that defines
            the region area.
        regional_inventory_eligible (google.protobuf.wrappers_pb2.BoolValue):
            Output only. Indicates if the region is
            eligible for use in the Regional Inventory
            configuration.
        shipping_eligible (google.protobuf.wrappers_pb2.BoolValue):
            Output only. Indicates if the region is
            eligible for use in the Shipping Services
            configuration.
    """

    class PostalCodeArea(proto.Message):
        r"""A list of postal codes that defines the region area. Note: All
        regions defined using postal codes are accessible through the
        account's ``ShippingSettings.postalCodeGroups`` resource.

        Attributes:
            region_code (str):
                Required. `CLDR territory
                code <http://www.unicode.org/repos/cldr/tags/latest/common/main/en.xml>`__
                or the country the postal code group applies to.
            postal_codes (MutableSequence[google.shopping.merchant_accounts_v1beta.types.Region.PostalCodeArea.PostalCodeRange]):
                Required. A range of postal codes.
        """

        class PostalCodeRange(proto.Message):
            r"""A range of postal codes that defines the region area.

            Attributes:
                begin (str):
                    Required. A postal code or a pattern of the form prefix\*
                    denoting the inclusive lower bound of the range defining the
                    area. Examples values: ``94108``, ``9410*``, ``9*``.
                end (str):
                    Optional. A postal code or a pattern of the form ``prefix*``
                    denoting the inclusive upper bound of the range defining the
                    area. It must have the same length as postalCodeRangeBegin:
                    if postalCodeRangeBegin is a postal code then
                    postalCodeRangeEnd must be a postal code too; if
                    postalCodeRangeBegin is a pattern then postalCodeRangeEnd
                    must be a pattern with the same prefix length. Optional: if
                    not set, then the area is defined as being all the postal
                    codes matching postalCodeRangeBegin.
            """

            begin: str = proto.Field(
                proto.STRING,
                number=1,
            )
            end: str = proto.Field(
                proto.STRING,
                number=2,
            )

        region_code: str = proto.Field(
            proto.STRING,
            number=1,
        )
        postal_codes: MutableSequence["Region.PostalCodeArea.PostalCodeRange"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="Region.PostalCodeArea.PostalCodeRange",
            )
        )

    class GeoTargetArea(proto.Message):
        r"""A list of geotargets that defines the region area.

        Attributes:
            geotarget_criteria_ids (MutableSequence[int]):
                Required. A non-empty list of `location
                IDs <https://developers.google.com/adwords/api/docs/appendix/geotargeting>`__.
                They must all be of the same location type (for example,
                state).
        """

        geotarget_criteria_ids: MutableSequence[int] = proto.RepeatedField(
            proto.INT64,
            number=1,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    postal_code_area: PostalCodeArea = proto.Field(
        proto.MESSAGE,
        number=3,
        message=PostalCodeArea,
    )
    geotarget_area: GeoTargetArea = proto.Field(
        proto.MESSAGE,
        number=4,
        message=GeoTargetArea,
    )
    regional_inventory_eligible: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=5,
        message=wrappers_pb2.BoolValue,
    )
    shipping_eligible: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=6,
        message=wrappers_pb2.BoolValue,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
