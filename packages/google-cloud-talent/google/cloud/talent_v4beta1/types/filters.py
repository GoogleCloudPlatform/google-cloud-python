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

import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.type.latlng_pb2 as latlng_pb2  # type: ignore
import google.type.timeofday_pb2 as timeofday_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.talent_v4beta1.types import common

__protobuf__ = proto.module(
    package="google.cloud.talent.v4beta1",
    manifest={
        "JobQuery",
        "LocationFilter",
        "CompensationFilter",
        "CommuteFilter",
    },
)


class JobQuery(proto.Message):
    r"""The query required to perform a search query.

    Attributes:
        query (str):
            The query string that matches against the job
            title, description, and location fields.

            The maximum number of allowed characters is 255.
        query_language_code (str):
            The language code of
            [query][google.cloud.talent.v4beta1.JobQuery.query]. For
            example, "en-US". This field helps to better interpret the
            query.

            If a value isn't specified, the query language code is
            automatically detected, which may not be accurate.

            Language code should be in BCP-47 format, such as "en-US" or
            "sr-Latn". For more information, see `Tags for Identifying
            Languages <https://tools.ietf.org/html/bcp47>`__.
        companies (MutableSequence[str]):
            This filter specifies the company entities to search
            against.

            If a value isn't specified, jobs are searched for against
            all companies.

            If multiple values are specified, jobs are searched against
            the companies specified.

            The format is
            "projects/{project_id}/tenants/{tenant_id}/companies/{company_id}".
            For example, "projects/foo/tenants/bar/companies/baz".

            If tenant id is unspecified, the default tenant is used. For
            example, "projects/foo/companies/bar".

            At most 20 company filters are allowed.
        location_filters (MutableSequence[google.cloud.talent_v4beta1.types.LocationFilter]):
            The location filter specifies geo-regions containing the
            jobs to search against. See
            [LocationFilter][google.cloud.talent.v4beta1.LocationFilter]
            for more information.

            If a location value isn't specified, jobs fitting the other
            search criteria are retrieved regardless of where they're
            located.

            If multiple values are specified, jobs are retrieved from
            any of the specified locations. If different values are
            specified for the
            [LocationFilter.distance_in_miles][google.cloud.talent.v4beta1.LocationFilter.distance_in_miles]
            parameter, the maximum provided distance is used for all
            locations.

            At most 5 location filters are allowed.
        job_categories (MutableSequence[google.cloud.talent_v4beta1.types.JobCategory]):
            The category filter specifies the categories of jobs to
            search against. See
            [JobCategory][google.cloud.talent.v4beta1.JobCategory] for
            more information.

            If a value isn't specified, jobs from any category are
            searched against.

            If multiple values are specified, jobs from any of the
            specified categories are searched against.
        commute_filter (google.cloud.talent_v4beta1.types.CommuteFilter):
            Allows filtering jobs by commute time with different travel
            methods (for example, driving or public transit).

            Note: This only works when you specify a
            [CommuteMethod][google.cloud.talent.v4beta1.CommuteMethod].
            In this case,
            [location_filters][google.cloud.talent.v4beta1.JobQuery.location_filters]
            is ignored.

            Currently we don't support sorting by commute time.
        company_display_names (MutableSequence[str]):
            This filter specifies the company
            [Company.display_name][google.cloud.talent.v4beta1.Company.display_name]
            of the jobs to search against. The company name must match
            the value exactly.

            Alternatively, the value being searched for can be wrapped
            in different match operators. ``SUBSTRING_MATCH([value])``
            The company name must contain a case insensitive substring
            match of the value. Using this function may increase
            latency.

            Sample Value: ``SUBSTRING_MATCH(google)``

            ``MULTI_WORD_TOKEN_MATCH([value])`` The value will be
            treated as a multi word token and the company name must
            contain a case insensitive match of the value. Using this
            function may increase latency.

            Sample Value: ``MULTI_WORD_TOKEN_MATCH(google)``

            If a value isn't specified, jobs within the search results
            are associated with any company.

            If multiple values are specified, jobs within the search
            results may be associated with any of the specified
            companies.

            At most 20 company display name filters are allowed.
        compensation_filter (google.cloud.talent_v4beta1.types.CompensationFilter):
            This search filter is applied only to
            [Job.compensation_info][google.cloud.talent.v4beta1.Job.compensation_info].
            For example, if the filter is specified as "Hourly job with
            per-hour compensation > $15", only jobs meeting these
            criteria are searched. If a filter isn't defined, all open
            jobs are searched.
        custom_attribute_filter (str):
            This filter specifies a structured syntax to match against
            the
            [Job.custom_attributes][google.cloud.talent.v4beta1.Job.custom_attributes]
            marked as ``filterable``.

            The syntax for this expression is a subset of SQL syntax.

            Supported operators are: ``=``, ``!=``, ``<``, ``<=``,
            ``>``, and ``>=`` where the left of the operator is a custom
            field key and the right of the operator is a number or a
            quoted string. You must escape backslash (\\) and quote (")
            characters.

            Supported functions are ``LOWER([field_name])`` to perform a
            case insensitive match and ``EMPTY([field_name])`` to filter
            on the existence of a key.

            Boolean expressions (AND/OR/NOT) are supported up to 3
            levels of nesting (for example, "((A AND B AND C) OR NOT D)
            AND E"), a maximum of 100 comparisons or functions are
            allowed in the expression. The expression must be < 10000
            bytes in length.

            Sample Query:
            ``(LOWER(driving_license)="class \"a\"" OR EMPTY(driving_license)) AND driving_years > 10``
        disable_spell_check (bool):
            This flag controls the spell-check feature.
            If false, the service attempts to correct a
            misspelled query, for example, "enginee" is
            corrected to "engineer".

            Defaults to false: a spell check is performed.
        employment_types (MutableSequence[google.cloud.talent_v4beta1.types.EmploymentType]):
            The employment type filter specifies the employment type of
            jobs to search against, such as
            [EmploymentType.FULL_TIME][google.cloud.talent.v4beta1.EmploymentType.FULL_TIME].

            If a value isn't specified, jobs in the search results
            includes any employment type.

            If multiple values are specified, jobs in the search results
            include any of the specified employment types.
        language_codes (MutableSequence[str]):
            This filter specifies the locale of jobs to search against,
            for example, "en-US".

            If a value isn't specified, the search results can contain
            jobs in any locale.

            Language codes should be in BCP-47 format, such as "en-US"
            or "sr-Latn". For more information, see `Tags for
            Identifying
            Languages <https://tools.ietf.org/html/bcp47>`__.

            At most 10 language code filters are allowed.
        publish_time_range (google.cloud.talent_v4beta1.types.TimestampRange):
            Jobs published within a range specified by
            this filter are searched against.
        excluded_jobs (MutableSequence[str]):
            This filter specifies a list of job names to
            be excluded during search.
            At most 400 excluded job names are allowed.
    """

    query: str = proto.Field(
        proto.STRING,
        number=1,
    )
    query_language_code: str = proto.Field(
        proto.STRING,
        number=14,
    )
    companies: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    location_filters: MutableSequence["LocationFilter"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="LocationFilter",
    )
    job_categories: MutableSequence[common.JobCategory] = proto.RepeatedField(
        proto.ENUM,
        number=4,
        enum=common.JobCategory,
    )
    commute_filter: "CommuteFilter" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="CommuteFilter",
    )
    company_display_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    compensation_filter: "CompensationFilter" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="CompensationFilter",
    )
    custom_attribute_filter: str = proto.Field(
        proto.STRING,
        number=8,
    )
    disable_spell_check: bool = proto.Field(
        proto.BOOL,
        number=9,
    )
    employment_types: MutableSequence[common.EmploymentType] = proto.RepeatedField(
        proto.ENUM,
        number=10,
        enum=common.EmploymentType,
    )
    language_codes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=11,
    )
    publish_time_range: common.TimestampRange = proto.Field(
        proto.MESSAGE,
        number=12,
        message=common.TimestampRange,
    )
    excluded_jobs: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=13,
    )


class LocationFilter(proto.Message):
    r"""Geographic region of the search.

    Attributes:
        address (str):
            The address name, such as "Mountain View" or
            "Bay Area".
        region_code (str):
            CLDR region code of the country/region. This field may be
            used in two ways:

            1) If telecommute preference is not set, this field is used
               address ambiguity of the user-input address. For example,
               "Liverpool" may refer to "Liverpool, NY, US" or
               "Liverpool, UK". This region code biases the address
               resolution toward a specific country or territory. If
               this field is not set, address resolution is biased
               toward the United States by default.

            2) If telecommute preference is set to TELECOMMUTE_ALLOWED,
               the telecommute location filter will be limited to the
               region specified in this field. If this field is not set,
               the telecommute job locations will not be

            See
            https://unicode-org.github.io/cldr-staging/charts/latest/supplemental/territory_information.html
            for details. Example: "CH" for Switzerland.
        lat_lng (google.type.latlng_pb2.LatLng):
            The latitude and longitude of the geographic center to
            search from. This field is ignored if ``address`` is
            provided.
        distance_in_miles (float):
            The distance_in_miles is applied when the location being
            searched for is identified as a city or smaller. This field
            is ignored if the location being searched for is a state or
            larger.
        telecommute_preference (google.cloud.talent_v4beta1.types.LocationFilter.TelecommutePreference):
            Allows the client to return jobs without a set location,
            specifically, telecommuting jobs (telecommuting is
            considered by the service as a special location).
            [Job.posting_region][google.cloud.talent.v4beta1.Job.posting_region]
            indicates if a job permits telecommuting. If this field is
            set to
            [TelecommutePreference.TELECOMMUTE_ALLOWED][google.cloud.talent.v4beta1.LocationFilter.TelecommutePreference.TELECOMMUTE_ALLOWED],
            telecommuting jobs are searched, and
            [address][google.cloud.talent.v4beta1.LocationFilter.address]
            and
            [lat_lng][google.cloud.talent.v4beta1.LocationFilter.lat_lng]
            are ignored. If not set or set to
            [TelecommutePreference.TELECOMMUTE_EXCLUDED][google.cloud.talent.v4beta1.LocationFilter.TelecommutePreference.TELECOMMUTE_EXCLUDED],
            the telecommute status of the jobs is ignored. Jobs that
            have
            [PostingRegion.TELECOMMUTE][google.cloud.talent.v4beta1.PostingRegion.TELECOMMUTE]
            and have additional
            [Job.addresses][google.cloud.talent.v4beta1.Job.addresses]
            may still be matched based on other location filters using
            [address][google.cloud.talent.v4beta1.LocationFilter.address]
            or [latlng][].

            This filter can be used by itself to search exclusively for
            telecommuting jobs, or it can be combined with another
            location filter to search for a combination of job
            locations, such as "Mountain View" or "telecommuting" jobs.
            However, when used in combination with other location
            filters, telecommuting jobs can be treated as less relevant
            than other jobs in the search response.

            This field is only used for job search requests.
        negated (bool):
            Whether to apply negation to the filter so
            profiles matching the filter are excluded.
    """

    class TelecommutePreference(proto.Enum):
        r"""Specify whether to include telecommute jobs.

        Values:
            TELECOMMUTE_PREFERENCE_UNSPECIFIED (0):
                Default value if the telecommute preference
                isn't specified.
            TELECOMMUTE_EXCLUDED (1):
                Deprecated: Ignore telecommute status of jobs. Use
                TELECOMMUTE_JOBS_EXCLUDED if want to exclude telecommute
                jobs.
            TELECOMMUTE_ALLOWED (2):
                Allow telecommute jobs.
            TELECOMMUTE_JOBS_EXCLUDED (3):
                Exclude telecommute jobs.
        """

        TELECOMMUTE_PREFERENCE_UNSPECIFIED = 0
        TELECOMMUTE_EXCLUDED = 1
        TELECOMMUTE_ALLOWED = 2
        TELECOMMUTE_JOBS_EXCLUDED = 3

    address: str = proto.Field(
        proto.STRING,
        number=1,
    )
    region_code: str = proto.Field(
        proto.STRING,
        number=2,
    )
    lat_lng: latlng_pb2.LatLng = proto.Field(
        proto.MESSAGE,
        number=3,
        message=latlng_pb2.LatLng,
    )
    distance_in_miles: float = proto.Field(
        proto.DOUBLE,
        number=4,
    )
    telecommute_preference: TelecommutePreference = proto.Field(
        proto.ENUM,
        number=5,
        enum=TelecommutePreference,
    )
    negated: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


class CompensationFilter(proto.Message):
    r"""Filter on job compensation type and amount.

    Attributes:
        type_ (google.cloud.talent_v4beta1.types.CompensationFilter.FilterType):
            Required. Type of filter.
        units (MutableSequence[google.cloud.talent_v4beta1.types.CompensationInfo.CompensationUnit]):
            Required. Specify desired ``base compensation entry's``
            [CompensationInfo.CompensationUnit][google.cloud.talent.v4beta1.CompensationInfo.CompensationUnit].
        range_ (google.cloud.talent_v4beta1.types.CompensationInfo.CompensationRange):
            Compensation range.
        include_jobs_with_unspecified_compensation_range (bool):
            If set to true, jobs with unspecified
            compensation range fields are included.
    """

    class FilterType(proto.Enum):
        r"""Specify the type of filtering.

        Values:
            FILTER_TYPE_UNSPECIFIED (0):
                Filter type unspecified. Position holder,
                INVALID, should never be used.
            UNIT_ONLY (1):
                Filter by ``base compensation entry's`` unit. A job is a
                match if and only if the job contains a base
                CompensationEntry and the base CompensationEntry's unit
                matches provided
                [units][google.cloud.talent.v4beta1.CompensationFilter.units].
                Populate one or more
                [units][google.cloud.talent.v4beta1.CompensationFilter.units].

                See
                [CompensationInfo.CompensationEntry][google.cloud.talent.v4beta1.CompensationInfo.CompensationEntry]
                for definition of base compensation entry.
            UNIT_AND_AMOUNT (2):
                Filter by ``base compensation entry's`` unit and amount /
                range. A job is a match if and only if the job contains a
                base CompensationEntry, and the base entry's unit matches
                provided
                [CompensationUnit][google.cloud.talent.v4beta1.CompensationInfo.CompensationUnit]
                and amount or range overlaps with provided
                [CompensationRange][google.cloud.talent.v4beta1.CompensationInfo.CompensationRange].

                See
                [CompensationInfo.CompensationEntry][google.cloud.talent.v4beta1.CompensationInfo.CompensationEntry]
                for definition of base compensation entry.

                Set exactly one
                [units][google.cloud.talent.v4beta1.CompensationFilter.units]
                and populate
                [range][google.cloud.talent.v4beta1.CompensationFilter.range].
            ANNUALIZED_BASE_AMOUNT (3):
                Filter by annualized base compensation amount and
                ``base compensation entry's`` unit. Populate
                [range][google.cloud.talent.v4beta1.CompensationFilter.range]
                and zero or more
                [units][google.cloud.talent.v4beta1.CompensationFilter.units].
            ANNUALIZED_TOTAL_AMOUNT (4):
                Filter by annualized total compensation amount and
                ``base compensation entry's`` unit . Populate
                [range][google.cloud.talent.v4beta1.CompensationFilter.range]
                and zero or more
                [units][google.cloud.talent.v4beta1.CompensationFilter.units].
        """

        FILTER_TYPE_UNSPECIFIED = 0
        UNIT_ONLY = 1
        UNIT_AND_AMOUNT = 2
        ANNUALIZED_BASE_AMOUNT = 3
        ANNUALIZED_TOTAL_AMOUNT = 4

    type_: FilterType = proto.Field(
        proto.ENUM,
        number=1,
        enum=FilterType,
    )
    units: MutableSequence[common.CompensationInfo.CompensationUnit] = (
        proto.RepeatedField(
            proto.ENUM,
            number=2,
            enum=common.CompensationInfo.CompensationUnit,
        )
    )
    range_: common.CompensationInfo.CompensationRange = proto.Field(
        proto.MESSAGE,
        number=3,
        message=common.CompensationInfo.CompensationRange,
    )
    include_jobs_with_unspecified_compensation_range: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class CommuteFilter(proto.Message):
    r"""Parameters needed for commute search.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        commute_method (google.cloud.talent_v4beta1.types.CommuteMethod):
            Required. The method of transportation to
            calculate the commute time for.
        start_coordinates (google.type.latlng_pb2.LatLng):
            Required. The latitude and longitude of the
            location to calculate the commute time from.
        travel_duration (google.protobuf.duration_pb2.Duration):
            Required. The maximum travel time in seconds. The maximum
            allowed value is ``3600s`` (one hour). Format is ``123s``.
        allow_imprecise_addresses (bool):
            If ``true``, jobs without street level addresses may also be
            returned. For city level addresses, the city center is used.
            For state and coarser level addresses, text matching is
            used. If this field is set to ``false`` or isn't specified,
            only jobs that include street level addresses will be
            returned by commute search.
        road_traffic (google.cloud.talent_v4beta1.types.CommuteFilter.RoadTraffic):
            Specifies the traffic density to use when
            calculating commute time.

            This field is a member of `oneof`_ ``traffic_option``.
        departure_time (google.type.timeofday_pb2.TimeOfDay):
            The departure time used to calculate traffic impact,
            represented as
            [google.type.TimeOfDay][google.type.TimeOfDay] in local time
            zone.

            Currently traffic model is restricted to hour level
            resolution.

            This field is a member of `oneof`_ ``traffic_option``.
    """

    class RoadTraffic(proto.Enum):
        r"""The traffic density to use when calculating commute time.

        Values:
            ROAD_TRAFFIC_UNSPECIFIED (0):
                Road traffic situation isn't specified.
            TRAFFIC_FREE (1):
                Optimal commute time without considering any
                traffic impact.
            BUSY_HOUR (2):
                Commute time calculation takes in account the
                peak traffic impact.
        """

        ROAD_TRAFFIC_UNSPECIFIED = 0
        TRAFFIC_FREE = 1
        BUSY_HOUR = 2

    commute_method: common.CommuteMethod = proto.Field(
        proto.ENUM,
        number=1,
        enum=common.CommuteMethod,
    )
    start_coordinates: latlng_pb2.LatLng = proto.Field(
        proto.MESSAGE,
        number=2,
        message=latlng_pb2.LatLng,
    )
    travel_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=3,
        message=duration_pb2.Duration,
    )
    allow_imprecise_addresses: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    road_traffic: RoadTraffic = proto.Field(
        proto.ENUM,
        number=5,
        oneof="traffic_option",
        enum=RoadTraffic,
    )
    departure_time: timeofday_pb2.TimeOfDay = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="traffic_option",
        message=timeofday_pb2.TimeOfDay,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
