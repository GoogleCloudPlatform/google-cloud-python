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
    package="google.cloud.locationfinder.v1",
    manifest={
        "CloudLocation",
        "ListCloudLocationsRequest",
        "ListCloudLocationsResponse",
        "GetCloudLocationRequest",
        "SearchCloudLocationsRequest",
        "SearchCloudLocationsResponse",
    },
)


class CloudLocation(proto.Message):
    r"""Represents resource cloud locations.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. Name of the cloud location. Unique name of the
            cloud location including project and location using the
            form:
            ``projects/{project_id}/locations/{location}/cloudLocations/{cloud_location}``
        containing_cloud_location (str):
            Output only. The containing cloud location in
            the strict nesting hierarchy. For example, the
            containing cloud location of a zone is a region.
        display_name (str):
            Optional. The human-readable name of the
            cloud location. Example: us-east-2, us-east1.
        cloud_provider (google.cloud.locationfinder_v1.types.CloudLocation.CloudProvider):
            Optional. The provider of the cloud location.
            Values can be Google Cloud or third-party
            providers, including AWS, Azure, or Oracle Cloud
            Infrastructure.
        territory_code (str):
            Optional. The two-letter ISO 3166-1 alpha-2
            code of the cloud location. Examples: US, JP,
            KR.
        cloud_location_type (google.cloud.locationfinder_v1.types.CloudLocation.CloudLocationType):
            Optional. The type of the cloud location.
        carbon_free_energy_percentage (float):
            Optional. The carbon free energy percentage
            of the cloud location. This represents the
            average percentage of time customers'
            application will be running on carbon-free
            energy. See
            https://cloud.google.com/sustainability/region-carbon
            for more details. There is a difference between
            default value 0 and unset value. 0 means the
            carbon free energy percentage is 0%, while unset
            value means the carbon footprint data is not
            available.

            This field is a member of `oneof`_ ``_carbon_free_energy_percentage``.
    """

    class CloudProvider(proto.Enum):
        r"""The type of the cloud provider. This enum lists all possible
        providers of cloud locations.

        Values:
            CLOUD_PROVIDER_UNSPECIFIED (0):
                Unspecified type.
            CLOUD_PROVIDER_GCP (1):
                Cloud provider type for Google Cloud.
            CLOUD_PROVIDER_AWS (2):
                Cloud provider type for AWS.
            CLOUD_PROVIDER_AZURE (3):
                Cloud provider type for Azure.
            CLOUD_PROVIDER_OCI (4):
                Cloud provider type for OCI.
        """

        CLOUD_PROVIDER_UNSPECIFIED = 0
        CLOUD_PROVIDER_GCP = 1
        CLOUD_PROVIDER_AWS = 2
        CLOUD_PROVIDER_AZURE = 3
        CLOUD_PROVIDER_OCI = 4

    class CloudLocationType(proto.Enum):
        r"""The type of the cloud location. This enum lists all possible
        categories of cloud locations.

        Values:
            CLOUD_LOCATION_TYPE_UNSPECIFIED (0):
                Unspecified type.
            CLOUD_LOCATION_TYPE_REGION (1):
                CloudLocation type for region.
            CLOUD_LOCATION_TYPE_ZONE (2):
                CloudLocation type for zone.
            CLOUD_LOCATION_TYPE_REGION_EXTENSION (3):
                CloudLocation type for region extension.
            CLOUD_LOCATION_TYPE_GDCC_ZONE (4):
                CloudLocation type for Google Distributed
                Cloud Connected Zone.
        """

        CLOUD_LOCATION_TYPE_UNSPECIFIED = 0
        CLOUD_LOCATION_TYPE_REGION = 1
        CLOUD_LOCATION_TYPE_ZONE = 2
        CLOUD_LOCATION_TYPE_REGION_EXTENSION = 3
        CLOUD_LOCATION_TYPE_GDCC_ZONE = 4

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    containing_cloud_location: str = proto.Field(
        proto.STRING,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    cloud_provider: CloudProvider = proto.Field(
        proto.ENUM,
        number=4,
        enum=CloudProvider,
    )
    territory_code: str = proto.Field(
        proto.STRING,
        number=5,
    )
    cloud_location_type: CloudLocationType = proto.Field(
        proto.ENUM,
        number=6,
        enum=CloudLocationType,
    )
    carbon_free_energy_percentage: float = proto.Field(
        proto.FLOAT,
        number=7,
        optional=True,
    )


class ListCloudLocationsRequest(proto.Message):
    r"""Message for requesting list of cloud locations..

    Attributes:
        parent (str):
            Required. The parent, which owns this
            collection of cloud locations. Format:
            projects/{project}/locations/{location}
        page_size (int):
            Optional. The maximum number of cloud
            locations to return per page. The service might
            return fewer cloud locations than this value. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return. Provide page
            token returned by a previous
            'ListCloudLocations' call to retrieve the next
            page of results. When paginating, all other
            parameters provided to 'ListCloudLocations' must
            match the call that provided the page token.
        filter (str):
            Optional. A filter expression that filters resources listed
            in the response. The expression is in the form of
            field=value. For example,
            'cloud_location_type=CLOUD_LOCATION_TYPE_REGION'. Multiple
            filter queries are space-separated. For example,
            'cloud_location_type=CLOUD_LOCATION_TYPE_REGION
            territory_code="US"' By default, each expression is an AND
            expression. However, you can include AND and OR expressions
            explicitly.
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


class ListCloudLocationsResponse(proto.Message):
    r"""Message for response to listing cloud locations.

    Attributes:
        cloud_locations (MutableSequence[google.cloud.locationfinder_v1.types.CloudLocation]):
            Output only. List of cloud locations.
        next_page_token (str):
            Output only. The continuation token, used to page through
            large result sets. Provide this value in a subsequent
            request as page_token in subsequent requests to retrieve the
            next page. If this field is not present, there are no
            subsequent results.
    """

    @property
    def raw_page(self):
        return self

    cloud_locations: MutableSequence["CloudLocation"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="CloudLocation",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetCloudLocationRequest(proto.Message):
    r"""Message for getting a cloud location.

    Attributes:
        name (str):
            Required. Name of the resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SearchCloudLocationsRequest(proto.Message):
    r"""Message for searching cloud locations from a given source
    location.

    Attributes:
        parent (str):
            Required. The parent, which owns this
            collection of cloud locations. Format:
            projects/{project}/locations/{location}
        source_cloud_location (str):
            Required. The source cloud location to search
            from. Example search can be searching nearby
            cloud locations from the source cloud location
            by latency.
        page_size (int):
            Optional. The maximum number of cloud
            locations to return. The service might return
            fewer cloud locations than this value. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return. Provide Page
            token returned by a previous
            'ListCloudLocations' call to retrieve the next
            page of results. When paginating, all other
            parameters provided to 'ListCloudLocations' must
            match the call that provided the page token.
        query (str):
            Optional. The query string in search query
            syntax. While filter is used to filter the
            search results by attributes, query is used to
            specify the search requirements.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    source_cloud_location: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )
    query: str = proto.Field(
        proto.STRING,
        number=6,
    )


class SearchCloudLocationsResponse(proto.Message):
    r"""Message for response to searching cloud locations.

    Attributes:
        cloud_locations (MutableSequence[google.cloud.locationfinder_v1.types.CloudLocation]):
            Output only. List of cloud locations.
        next_page_token (str):
            Output only. The continuation token, used to page through
            large result sets. Provide this value in a subsequent
            request as page_token in subsequent requests to retrieve the
            next page. If this field is not present, there are no
            subsequent results.
    """

    @property
    def raw_page(self):
        return self

    cloud_locations: MutableSequence["CloudLocation"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="CloudLocation",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
