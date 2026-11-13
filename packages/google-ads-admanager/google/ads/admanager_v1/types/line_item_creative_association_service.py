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

from google.ads.admanager_v1.types import line_item_creative_association_messages

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "GetLineItemCreativeAssociationRequest",
        "ListLineItemCreativeAssociationsRequest",
        "ListLineItemCreativeAssociationsResponse",
        "CreateLineItemCreativeAssociationRequest",
        "BatchCreateLineItemCreativeAssociationsRequest",
        "BatchCreateLineItemCreativeAssociationsResponse",
        "UpdateLineItemCreativeAssociationRequest",
        "BatchUpdateLineItemCreativeAssociationsRequest",
        "BatchUpdateLineItemCreativeAssociationsResponse",
        "BatchActivateLineItemCreativeAssociationsRequest",
        "BatchActivateLineItemCreativeAssociationsResponse",
        "BatchDeactivateLineItemCreativeAssociationsRequest",
        "BatchDeactivateLineItemCreativeAssociationsResponse",
        "BatchDeleteLineItemCreativeAssociationsRequest",
        "PreviewLineItemCreativeAssociationRequest",
        "PreviewLineItemCreativeAssociationResponse",
    },
)


class GetLineItemCreativeAssociationRequest(proto.Message):
    r"""Request object for ``GetLineItemCreativeAssociation`` method.

    Attributes:
        name (str):
            Required. The resource name of the
            LineItemCreativeAssociation. Format:
            ``networks/{network_code}/lineItems/{line_item_id}/creatives/{creative_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListLineItemCreativeAssociationsRequest(proto.Message):
    r"""Request object for ``ListLineItemCreativeAssociations`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            LineItemCreativeAssociations. This request supports using
            the "-" character as a wildcard for resources that span
            across multiple LineItem parents. Format:
            ``networks/{network_code}/lineItems/{line_item_id}`` Format:
            ``networks/{network_code}/lineItems/-``
        page_size (int):
            Optional. The maximum number of
            ``LineItemCreativeAssociations`` to return. The service may
            return fewer than this value. If unspecified, at most 50
            ``LineItemCreativeAssociations`` will be returned. The
            maximum value is 1000; values greater than 1000 will be
            coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListLineItemCreativeAssociations`` call. Provide this to
            retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListLineItemCreativeAssociations`` must match the call
            that provided the page token.
        filter (str):
            Optional. Expression to filter the response. See syntax
            details at
            https://developers.google.com/ad-manager/api/beta/filters

            Syntax summary: double-quoted ``"..."`` (never ``'...'``)
            strings and RFC 3339 timestamps, full resource names on
            reference fields (for example,
            ``order = "networks/123/orders/456"``, not ``*Id`` or bare
            IDs), prefix or suffix ``*`` wildcards with ``=``
            (``displayName = "foo*"``), ``:`` for substring or
            repeated-field matching, unquoted enums and booleans,
            uppercase ``AND``/``OR``/``NOT``, and standalone
            ``IN(field, SET(v1, v2))`` (not ``field IN (...)``).

            **Filterable fields:**

            - ``creative``
            - ``creativeSet``
            - ``destinationUrl``
            - ``endTime``
            - ``lineItem``
            - ``manualCreativeRotationWeight``
            - ``name``
            - ``sequentialCreativeRotationIndex``
            - ``startTime``
            - ``status``
            - ``targetingDisplayName``
            - ``updateTime``
        order_by (str):
            Optional. Expression to specify sorting
            order. See syntax details at
            https://developers.google.com/ad-manager/api/beta/filters#order
        skip (int):
            Optional. Number of individual resources to
            skip while paginating.
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
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )
    skip: int = proto.Field(
        proto.INT32,
        number=6,
    )


class ListLineItemCreativeAssociationsResponse(proto.Message):
    r"""Response object for ``ListLineItemCreativeAssociationsRequest``
    containing matching ``LineItemCreativeAssociation`` objects.

    Attributes:
        line_item_creative_associations (MutableSequence[google.ads.admanager_v1.types.LineItemCreativeAssociation]):
            The ``LineItemCreativeAssociation`` objects from the
            specified network.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        total_size (int):
            Total number of ``LineItemCreativeAssociation`` objects. If
            a filter was included in the request, this reflects the
            total number after the filtering is applied.

            ``total_size`` won't be calculated in the response unless it
            has been included in a response field mask. The response
            field mask can be provided to the method by using the URL
            parameter ``$fields`` or ``fields``, or by using the
            HTTP/gRPC header ``X-Goog-FieldMask``.

            For more information, see
            https://developers.google.com/ad-manager/api/beta/field-masks
    """

    @property
    def raw_page(self):
        return self

    line_item_creative_associations: MutableSequence[
        line_item_creative_association_messages.LineItemCreativeAssociation
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=line_item_creative_association_messages.LineItemCreativeAssociation,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class CreateLineItemCreativeAssociationRequest(proto.Message):
    r"""Request object for ``CreateLineItemCreativeAssociation`` method.

    Attributes:
        parent (str):
            Required. The parent resource where this
            ``LineItemCreativeAssociation`` will be created. Format:
            ``networks/{network_code}/lineItems/{line_item_id}``
        line_item_creative_association (google.ads.admanager_v1.types.LineItemCreativeAssociation):
            Required. The ``LineItemCreativeAssociation`` to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    line_item_creative_association: line_item_creative_association_messages.LineItemCreativeAssociation = proto.Field(
        proto.MESSAGE,
        number=2,
        message=line_item_creative_association_messages.LineItemCreativeAssociation,
    )


class BatchCreateLineItemCreativeAssociationsRequest(proto.Message):
    r"""Request object for ``BatchCreateLineItemCreativeAssociations``
    method.

    Attributes:
        parent (str):
            Required. The parent resource where
            ``LineItemCreativeAssociations`` will be created. This
            request supports using the "-" character as a wildcard for
            resources that span across multiple LineItem parents.
            Format: ``networks/{network_code}/lineItems/{line_item_id}``
            Format: ``networks/{network_code}/lineItems/-``
        requests (MutableSequence[google.ads.admanager_v1.types.CreateLineItemCreativeAssociationRequest]):
            Required. The ``LineItemCreativeAssociation`` objects to
            create. A maximum of 100 objects can be created in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreateLineItemCreativeAssociationRequest"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="CreateLineItemCreativeAssociationRequest",
        )
    )


class BatchCreateLineItemCreativeAssociationsResponse(proto.Message):
    r"""Response object for ``BatchCreateLineItemCreativeAssociations``
    method.

    Attributes:
        line_item_creative_associations (MutableSequence[google.ads.admanager_v1.types.LineItemCreativeAssociation]):
            The ``LineItemCreativeAssociation`` objects created.
    """

    line_item_creative_associations: MutableSequence[
        line_item_creative_association_messages.LineItemCreativeAssociation
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=line_item_creative_association_messages.LineItemCreativeAssociation,
    )


class UpdateLineItemCreativeAssociationRequest(proto.Message):
    r"""Request object for ``UpdateLineItemCreativeAssociation`` method.

    Attributes:
        line_item_creative_association (google.ads.admanager_v1.types.LineItemCreativeAssociation):
            Required. The ``LineItemCreativeAssociation`` to update.
            Format:
            ``networks/{network_code}/lineItems/{line_item_id}/creatives/{creative_id}``
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    line_item_creative_association: line_item_creative_association_messages.LineItemCreativeAssociation = proto.Field(
        proto.MESSAGE,
        number=1,
        message=line_item_creative_association_messages.LineItemCreativeAssociation,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class BatchUpdateLineItemCreativeAssociationsRequest(proto.Message):
    r"""Request object for ``BatchUpdateLineItemCreativeAssociations``
    method.

    Attributes:
        parent (str):
            Required. The parent resource where
            ``LineItemCreativeAssociations`` will be updated. This
            request supports using the "-" character as a wildcard for
            resources that span across multiple LineItem parents.
            Format: ``networks/{network_code}/lineItems/{line_item_id}``
            Format: ``networks/{network_code}/lineItems/-``
        requests (MutableSequence[google.ads.admanager_v1.types.UpdateLineItemCreativeAssociationRequest]):
            Required. The ``LineItemCreativeAssociation`` objects to
            update. A maximum of 100 objects can be updated in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["UpdateLineItemCreativeAssociationRequest"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="UpdateLineItemCreativeAssociationRequest",
        )
    )


class BatchUpdateLineItemCreativeAssociationsResponse(proto.Message):
    r"""Response object for ``BatchUpdateLineItemCreativeAssociations``
    method.

    Attributes:
        line_item_creative_associations (MutableSequence[google.ads.admanager_v1.types.LineItemCreativeAssociation]):
            The ``LineItemCreativeAssociation`` objects updated.
    """

    line_item_creative_associations: MutableSequence[
        line_item_creative_association_messages.LineItemCreativeAssociation
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=line_item_creative_association_messages.LineItemCreativeAssociation,
    )


class BatchActivateLineItemCreativeAssociationsRequest(proto.Message):
    r"""Request message for ``BatchActivateLineItemCreativeAssociations``
    method.

    Attributes:
        parent (str):
            Required. The parent resource where
            ``LineItemCreativeAssociations`` will be activated. This
            request supports using the "-" character as a wildcard for
            resources that span across multiple LineItem parents.
            Format: ``networks/{network_code}/lineItems/{line_item_id}``
            Format: ``networks/{network_code}/lineItems/-``
        names (MutableSequence[str]):
            Required. The names of the ``LineItemCreativeAssociation``
            objects to activate. A maximum of 1000 objects can be
            activated in a batch. Format:
            ``networks/{network_code}/lineItems/{line_item_id}/creatives/{creative_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchActivateLineItemCreativeAssociationsResponse(proto.Message):
    r"""Response object for ``BatchActivateLineItemCreativeAssociations``
    method.

    """


class BatchDeactivateLineItemCreativeAssociationsRequest(proto.Message):
    r"""Request message for ``BatchDeactivateLineItemCreativeAssociations``
    method.

    Attributes:
        parent (str):
            Required. The parent resource where
            ``LineItemCreativeAssociations`` will be deactivated. This
            request supports using the "-" character as a wildcard for
            resources that span across multiple LineItem parents.
            Format: ``networks/{network_code}/lineItems/{line_item_id}``
            Format: ``networks/{network_code}/lineItems/-``
        names (MutableSequence[str]):
            Required. The names of the ``LineItemCreativeAssociation``
            objects to deactivate. A maximum of 1000 objects can be
            deactivated in a batch. Format:
            ``networks/{network_code}/lineItems/{line_item_id}/creatives/{creative_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchDeactivateLineItemCreativeAssociationsResponse(proto.Message):
    r"""Response object for ``BatchDeactivateLineItemCreativeAssociations``
    method.

    """


class BatchDeleteLineItemCreativeAssociationsRequest(proto.Message):
    r"""Request message for ``BatchDeleteLineItemCreativeAssociations``
    method.

    Attributes:
        parent (str):
            Required. The parent resource where
            ``LineItemCreativeAssociations`` will be deleted. This
            request supports using the "-" character as a wildcard for
            resources that span across multiple LineItem parents.
            Format: ``networks/{network_code}/lineItems/{line_item_id}``
            Format: ``networks/{network_code}/lineItems/-``
        names (MutableSequence[str]):
            Required. The names of the ``LineItemCreativeAssociation``
            objects to delete. A maximum of 1000 objects can be deleted
            in a batch. Format:
            ``networks/{network_code}/lineItems/{line_item_id}/creatives/{creative_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class PreviewLineItemCreativeAssociationRequest(proto.Message):
    r"""Request message for ``PreviewLineItemCreativeAssociation`` method.

    Attributes:
        name (str):
            Required. The name of the ``LineItemCreativeAssociation``
            object to preview. Format:
            ``networks/{network_code}/lineItems/{line_item_id}/creatives/{creative_id}``
        site_url (str):
            Required. The URL of the site that the
            creative should be previewed in
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    site_url: str = proto.Field(
        proto.STRING,
        number=2,
    )


class PreviewLineItemCreativeAssociationResponse(proto.Message):
    r"""Response object for ``PreviewLineItemCreativeAssociation`` method.

    Attributes:
        previews (MutableSequence[google.ads.admanager_v1.types.PreviewLineItemCreativeAssociationResponse.Preview]):
            On-site previews of the ``LineItemCreativeAssociation``. It
            has only one element for non-native previews and one preview
            url per ``NativeStyle`` associated.
    """

    class PreviewType(proto.Enum):
        r"""Represents preview types.

        Values:
            PREVIEW_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            STANDARD (1):
                Standard preview type.
            NATIVE (2):
                ``NativeStyle`` preview type.
        """

        PREVIEW_TYPE_UNSPECIFIED = 0
        STANDARD = 1
        NATIVE = 2

    class Preview(proto.Message):
        r"""Represents the ``Creative`` and its corresponding preview URL. \*/

        Attributes:
            preview_type (google.ads.admanager_v1.types.PreviewLineItemCreativeAssociationResponse.PreviewType):
                Represents the type of preview.
            on_site_preview_url (str):
                The URL for previewing this creative.
            native_style (str):
                The resource names of the ``NativeStyle`` for the preview.
                Only relevant when PreviewType is NATIVE. Format:
                ``networks/{network_code}/nativeStyles/{native_style_id}``
        """

        preview_type: "PreviewLineItemCreativeAssociationResponse.PreviewType" = (
            proto.Field(
                proto.ENUM,
                number=1,
                enum="PreviewLineItemCreativeAssociationResponse.PreviewType",
            )
        )
        on_site_preview_url: str = proto.Field(
            proto.STRING,
            number=2,
        )
        native_style: str = proto.Field(
            proto.STRING,
            number=3,
        )

    previews: MutableSequence[Preview] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=Preview,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
