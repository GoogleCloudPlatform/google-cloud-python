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
    package="google.cloud.bigquery.dataexchange.v1beta1",
    manifest={
        "DataExchange",
        "DataProvider",
        "Publisher",
        "DestinationDatasetReference",
        "DestinationDataset",
        "Listing",
        "ListDataExchangesRequest",
        "ListDataExchangesResponse",
        "ListOrgDataExchangesRequest",
        "ListOrgDataExchangesResponse",
        "GetDataExchangeRequest",
        "CreateDataExchangeRequest",
        "UpdateDataExchangeRequest",
        "DeleteDataExchangeRequest",
        "ListListingsRequest",
        "ListListingsResponse",
        "GetListingRequest",
        "CreateListingRequest",
        "UpdateListingRequest",
        "DeleteListingRequest",
        "SubscribeListingRequest",
        "SubscribeListingResponse",
    },
)


class DataExchange(proto.Message):
    r"""A data exchange is a container that lets you share data.
    Along with the descriptive information about the data exchange,
    it contains listings that reference shared datasets.

    Attributes:
        name (str):
            Output only. The resource name of the data exchange. e.g.
            ``projects/myproject/locations/US/dataExchanges/123``.
        display_name (str):
            Required. Human-readable display name of the data exchange.
            The display name must contain only Unicode letters, numbers
            (0-9), underscores (\_), dashes (-), spaces ( ), ampersands
            (&) and must not start or end with spaces. Default value is
            an empty string. Max length: 63 bytes.
        description (str):
            Optional. Description of the data exchange.
            The description must not contain Unicode
            non-characters as well as C0 and C1 control
            codes except tabs (HT), new lines (LF), carriage
            returns (CR), and page breaks (FF). Default
            value is an empty string.
            Max length: 2000 bytes.
        primary_contact (str):
            Optional. Email or URL of the primary point
            of contact of the data exchange. Max Length:
            1000 bytes.
        documentation (str):
            Optional. Documentation describing the data
            exchange.
        listing_count (int):
            Output only. Number of listings contained in
            the data exchange.
        icon (bytes):
            Optional. Base64 encoded image representing
            the data exchange. Max Size: 3.0MiB Expected
            image dimensions are 512x512 pixels, however the
            API only performs validation on size of the
            encoded data. Note: For byte fields, the content
            of the fields are base64-encoded (which
            increases the size of the data by 33-36%) when
            using JSON on the wire.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    primary_contact: str = proto.Field(
        proto.STRING,
        number=4,
    )
    documentation: str = proto.Field(
        proto.STRING,
        number=5,
    )
    listing_count: int = proto.Field(
        proto.INT32,
        number=6,
    )
    icon: bytes = proto.Field(
        proto.BYTES,
        number=7,
    )


class DataProvider(proto.Message):
    r"""Contains details of the data provider.

    Attributes:
        name (str):
            Optional. Name of the data provider.
        primary_contact (str):
            Optional. Email or URL of the data provider.
            Max Length: 1000 bytes.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    primary_contact: str = proto.Field(
        proto.STRING,
        number=2,
    )


class Publisher(proto.Message):
    r"""Contains details of the listing publisher.

    Attributes:
        name (str):
            Optional. Name of the listing publisher.
        primary_contact (str):
            Optional. Email or URL of the listing
            publisher. Max Length: 1000 bytes.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    primary_contact: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DestinationDatasetReference(proto.Message):
    r"""Contains the reference that identifies a destination bigquery
    dataset.

    Attributes:
        dataset_id (str):
            Required. A unique ID for this dataset, without the project
            name. The ID must contain only letters (a-z, A-Z), numbers
            (0-9), or underscores (\_). The maximum length is 1,024
            characters.
        project_id (str):
            Required. The ID of the project containing
            this dataset.
    """

    dataset_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DestinationDataset(proto.Message):
    r"""Defines the destination bigquery dataset.

    Attributes:
        dataset_reference (google.cloud.bigquery_data_exchange_v1beta1.types.DestinationDatasetReference):
            Required. A reference that identifies the
            destination dataset.
        friendly_name (google.protobuf.wrappers_pb2.StringValue):
            Optional. A descriptive name for the dataset.
        description (google.protobuf.wrappers_pb2.StringValue):
            Optional. A user-friendly description of the
            dataset.
        labels (MutableMapping[str, str]):
            Optional. The labels associated with this
            dataset. You can use these to organize and group
            your datasets. You can set this property when
            inserting or updating a dataset. See
            https://cloud.google.com/resource-manager/docs/creating-managing-labels
            for more information.
        location (str):
            Required. The geographic location where the
            dataset should reside. See
            https://cloud.google.com/bigquery/docs/locations
            for supported locations.
    """

    dataset_reference: "DestinationDatasetReference" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="DestinationDatasetReference",
    )
    friendly_name: wrappers_pb2.StringValue = proto.Field(
        proto.MESSAGE,
        number=2,
        message=wrappers_pb2.StringValue,
    )
    description: wrappers_pb2.StringValue = proto.Field(
        proto.MESSAGE,
        number=3,
        message=wrappers_pb2.StringValue,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    location: str = proto.Field(
        proto.STRING,
        number=5,
    )


class Listing(proto.Message):
    r"""A listing is what gets published into a data exchange that a
    subscriber can subscribe to. It contains a reference to the data
    source along with descriptive information that will help
    subscribers find and subscribe the data.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        bigquery_dataset (google.cloud.bigquery_data_exchange_v1beta1.types.Listing.BigQueryDatasetSource):
            Required. Shared dataset i.e. BigQuery
            dataset source.

            This field is a member of `oneof`_ ``source``.
        name (str):
            Output only. The resource name of the listing. e.g.
            ``projects/myproject/locations/US/dataExchanges/123/listings/456``
        display_name (str):
            Required. Human-readable display name of the listing. The
            display name must contain only Unicode letters, numbers
            (0-9), underscores (\_), dashes (-), spaces ( ), ampersands
            (&) and can't start or end with spaces. Default value is an
            empty string. Max length: 63 bytes.
        description (str):
            Optional. Short description of the listing.
            The description must not contain Unicode
            non-characters and C0 and C1 control codes
            except tabs (HT), new lines (LF), carriage
            returns (CR), and page breaks (FF). Default
            value is an empty string.
            Max length: 2000 bytes.
        primary_contact (str):
            Optional. Email or URL of the primary point
            of contact of the listing. Max Length: 1000
            bytes.
        documentation (str):
            Optional. Documentation describing the
            listing.
        state (google.cloud.bigquery_data_exchange_v1beta1.types.Listing.State):
            Output only. Current state of the listing.
        icon (bytes):
            Optional. Base64 encoded image representing
            the listing. Max Size: 3.0MiB Expected image
            dimensions are 512x512 pixels, however the API
            only performs validation on size of the encoded
            data. Note: For byte fields, the contents of the
            field are base64-encoded (which increases the
            size of the data by 33-36%) when using JSON on
            the wire.
        data_provider (google.cloud.bigquery_data_exchange_v1beta1.types.DataProvider):
            Optional. Details of the data provider who
            owns the source data.
        categories (MutableSequence[google.cloud.bigquery_data_exchange_v1beta1.types.Listing.Category]):
            Optional. Categories of the listing. Up to
            two categories are allowed.
        publisher (google.cloud.bigquery_data_exchange_v1beta1.types.Publisher):
            Optional. Details of the publisher who owns
            the listing and who can share the source data.
        request_access (str):
            Optional. Email or URL of the request access
            of the listing. Subscribers can use this
            reference to request access. Max Length: 1000
            bytes.
    """

    class State(proto.Enum):
        r"""State of the listing.

        Values:
            STATE_UNSPECIFIED (0):
                Default value. This value is unused.
            ACTIVE (1):
                Subscribable state. Users with
                dataexchange.listings.subscribe permission can
                subscribe to this listing.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1

    class Category(proto.Enum):
        r"""Listing categories.

        Values:
            CATEGORY_UNSPECIFIED (0):
                No description available.
            CATEGORY_OTHERS (1):
                No description available.
            CATEGORY_ADVERTISING_AND_MARKETING (2):
                No description available.
            CATEGORY_COMMERCE (3):
                No description available.
            CATEGORY_CLIMATE_AND_ENVIRONMENT (4):
                No description available.
            CATEGORY_DEMOGRAPHICS (5):
                No description available.
            CATEGORY_ECONOMICS (6):
                No description available.
            CATEGORY_EDUCATION (7):
                No description available.
            CATEGORY_ENERGY (8):
                No description available.
            CATEGORY_FINANCIAL (9):
                No description available.
            CATEGORY_GAMING (10):
                No description available.
            CATEGORY_GEOSPATIAL (11):
                No description available.
            CATEGORY_HEALTHCARE_AND_LIFE_SCIENCE (12):
                No description available.
            CATEGORY_MEDIA (13):
                No description available.
            CATEGORY_PUBLIC_SECTOR (14):
                No description available.
            CATEGORY_RETAIL (15):
                No description available.
            CATEGORY_SPORTS (16):
                No description available.
            CATEGORY_SCIENCE_AND_RESEARCH (17):
                No description available.
            CATEGORY_TRANSPORTATION_AND_LOGISTICS (18):
                No description available.
            CATEGORY_TRAVEL_AND_TOURISM (19):
                No description available.
        """

        CATEGORY_UNSPECIFIED = 0
        CATEGORY_OTHERS = 1
        CATEGORY_ADVERTISING_AND_MARKETING = 2
        CATEGORY_COMMERCE = 3
        CATEGORY_CLIMATE_AND_ENVIRONMENT = 4
        CATEGORY_DEMOGRAPHICS = 5
        CATEGORY_ECONOMICS = 6
        CATEGORY_EDUCATION = 7
        CATEGORY_ENERGY = 8
        CATEGORY_FINANCIAL = 9
        CATEGORY_GAMING = 10
        CATEGORY_GEOSPATIAL = 11
        CATEGORY_HEALTHCARE_AND_LIFE_SCIENCE = 12
        CATEGORY_MEDIA = 13
        CATEGORY_PUBLIC_SECTOR = 14
        CATEGORY_RETAIL = 15
        CATEGORY_SPORTS = 16
        CATEGORY_SCIENCE_AND_RESEARCH = 17
        CATEGORY_TRANSPORTATION_AND_LOGISTICS = 18
        CATEGORY_TRAVEL_AND_TOURISM = 19

    class BigQueryDatasetSource(proto.Message):
        r"""A reference to a shared dataset. It is an existing BigQuery dataset
        with a collection of objects such as tables and views that you want
        to share with subscribers. When subscriber's subscribe to a listing,
        Analytics Hub creates a linked dataset in the subscriber's project.
        A Linked dataset is an opaque, read-only BigQuery dataset that
        serves as a *symbolic link* to a shared dataset.

        Attributes:
            dataset (str):
                Resource name of the dataset source for this listing. e.g.
                ``projects/myproject/datasets/123``
        """

        dataset: str = proto.Field(
            proto.STRING,
            number=1,
        )

    bigquery_dataset: BigQueryDatasetSource = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="source",
        message=BigQueryDatasetSource,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    primary_contact: str = proto.Field(
        proto.STRING,
        number=4,
    )
    documentation: str = proto.Field(
        proto.STRING,
        number=5,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=7,
        enum=State,
    )
    icon: bytes = proto.Field(
        proto.BYTES,
        number=8,
    )
    data_provider: "DataProvider" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="DataProvider",
    )
    categories: MutableSequence[Category] = proto.RepeatedField(
        proto.ENUM,
        number=10,
        enum=Category,
    )
    publisher: "Publisher" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="Publisher",
    )
    request_access: str = proto.Field(
        proto.STRING,
        number=12,
    )


class ListDataExchangesRequest(proto.Message):
    r"""Message for requesting the list of data exchanges.

    Attributes:
        parent (str):
            Required. The parent resource path of the data exchanges.
            e.g. ``projects/myproject/locations/US``.
        page_size (int):
            The maximum number of results to return in a
            single response page. Leverage the page tokens
            to iterate through the entire collection.
        page_token (str):
            Page token, returned by a previous call, to
            request the next page of results.
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


class ListDataExchangesResponse(proto.Message):
    r"""Message for response to the list of data exchanges.

    Attributes:
        data_exchanges (MutableSequence[google.cloud.bigquery_data_exchange_v1beta1.types.DataExchange]):
            The list of data exchanges.
        next_page_token (str):
            A token to request the next page of results.
    """

    @property
    def raw_page(self):
        return self

    data_exchanges: MutableSequence["DataExchange"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DataExchange",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListOrgDataExchangesRequest(proto.Message):
    r"""Message for requesting the list of data exchanges from
    projects in an organization and location.

    Attributes:
        organization (str):
            Required. The organization resource path of the projects
            containing DataExchanges. e.g.
            ``organizations/myorg/locations/US``.
        page_size (int):
            The maximum number of results to return in a
            single response page. Leverage the page tokens
            to iterate through the entire collection.
        page_token (str):
            Page token, returned by a previous call, to
            request the next page of results.
    """

    organization: str = proto.Field(
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


class ListOrgDataExchangesResponse(proto.Message):
    r"""Message for response to listing data exchanges in an
    organization and location.

    Attributes:
        data_exchanges (MutableSequence[google.cloud.bigquery_data_exchange_v1beta1.types.DataExchange]):
            The list of data exchanges.
        next_page_token (str):
            A token to request the next page of results.
    """

    @property
    def raw_page(self):
        return self

    data_exchanges: MutableSequence["DataExchange"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DataExchange",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetDataExchangeRequest(proto.Message):
    r"""Message for getting a data exchange.

    Attributes:
        name (str):
            Required. The resource name of the data exchange. e.g.
            ``projects/myproject/locations/US/dataExchanges/123``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateDataExchangeRequest(proto.Message):
    r"""Message for creating a data exchange.

    Attributes:
        parent (str):
            Required. The parent resource path of the data exchange.
            e.g. ``projects/myproject/locations/US``.
        data_exchange_id (str):
            Required. The ID of the data exchange. Must contain only
            Unicode letters, numbers (0-9), underscores (\_). Should not
            use characters that require URL-escaping, or characters
            outside of ASCII, spaces. Max length: 100 bytes.
        data_exchange (google.cloud.bigquery_data_exchange_v1beta1.types.DataExchange):
            Required. The data exchange to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_exchange_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    data_exchange: "DataExchange" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="DataExchange",
    )


class UpdateDataExchangeRequest(proto.Message):
    r"""Message for updating a data exchange.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask specifies the fields to update in the
            data exchange resource. The fields specified in the
            ``updateMask`` are relative to the resource and are not a
            full request.
        data_exchange (google.cloud.bigquery_data_exchange_v1beta1.types.DataExchange):
            Required. The data exchange to update.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    data_exchange: "DataExchange" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DataExchange",
    )


class DeleteDataExchangeRequest(proto.Message):
    r"""Message for deleting a data exchange.

    Attributes:
        name (str):
            Required. The full name of the data exchange resource that
            you want to delete. For example,
            ``projects/myproject/locations/US/dataExchanges/123``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListListingsRequest(proto.Message):
    r"""Message for requesting the list of listings.

    Attributes:
        parent (str):
            Required. The parent resource path of the listing. e.g.
            ``projects/myproject/locations/US/dataExchanges/123``.
        page_size (int):
            The maximum number of results to return in a
            single response page. Leverage the page tokens
            to iterate through the entire collection.
        page_token (str):
            Page token, returned by a previous call, to
            request the next page of results.
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


class ListListingsResponse(proto.Message):
    r"""Message for response to the list of Listings.

    Attributes:
        listings (MutableSequence[google.cloud.bigquery_data_exchange_v1beta1.types.Listing]):
            The list of Listing.
        next_page_token (str):
            A token to request the next page of results.
    """

    @property
    def raw_page(self):
        return self

    listings: MutableSequence["Listing"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Listing",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetListingRequest(proto.Message):
    r"""Message for getting a listing.

    Attributes:
        name (str):
            Required. The resource name of the listing. e.g.
            ``projects/myproject/locations/US/dataExchanges/123/listings/456``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateListingRequest(proto.Message):
    r"""Message for creating a listing.

    Attributes:
        parent (str):
            Required. The parent resource path of the listing. e.g.
            ``projects/myproject/locations/US/dataExchanges/123``.
        listing_id (str):
            Required. The ID of the listing to create. Must contain only
            Unicode letters, numbers (0-9), underscores (\_). Should not
            use characters that require URL-escaping, or characters
            outside of ASCII, spaces. Max length: 100 bytes.
        listing (google.cloud.bigquery_data_exchange_v1beta1.types.Listing):
            Required. The listing to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    listing_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    listing: "Listing" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Listing",
    )


class UpdateListingRequest(proto.Message):
    r"""Message for updating a Listing.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask specifies the fields to update in the
            listing resource. The fields specified in the ``updateMask``
            are relative to the resource and are not a full request.
        listing (google.cloud.bigquery_data_exchange_v1beta1.types.Listing):
            Required. The listing to update.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    listing: "Listing" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Listing",
    )


class DeleteListingRequest(proto.Message):
    r"""Message for deleting a listing.

    Attributes:
        name (str):
            Required. Resource name of the listing to delete. e.g.
            ``projects/myproject/locations/US/dataExchanges/123/listings/456``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SubscribeListingRequest(proto.Message):
    r"""Message for subscribing to a listing.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        destination_dataset (google.cloud.bigquery_data_exchange_v1beta1.types.DestinationDataset):
            BigQuery destination dataset to create for
            the subscriber.

            This field is a member of `oneof`_ ``destination``.
        name (str):
            Required. Resource name of the listing that you want to
            subscribe to. e.g.
            ``projects/myproject/locations/US/dataExchanges/123/listings/456``.
    """

    destination_dataset: "DestinationDataset" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="destination",
        message="DestinationDataset",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SubscribeListingResponse(proto.Message):
    r"""Message for response when you subscribe to a listing."""


__all__ = tuple(sorted(__protobuf__.manifest))
