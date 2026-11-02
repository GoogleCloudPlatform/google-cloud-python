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
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.talent_v4beta1.types import common, filters, histogram
from google.cloud.talent_v4beta1.types import job as gct_job

__protobuf__ = proto.module(
    package="google.cloud.talent.v4beta1",
    manifest={
        "JobView",
        "CreateJobRequest",
        "GetJobRequest",
        "UpdateJobRequest",
        "DeleteJobRequest",
        "BatchDeleteJobsRequest",
        "ListJobsRequest",
        "ListJobsResponse",
        "SearchJobsRequest",
        "SearchJobsResponse",
        "BatchCreateJobsRequest",
        "BatchUpdateJobsRequest",
        "JobOperationResult",
    },
)


class JobView(proto.Enum):
    r"""An enum that specifies the job attributes that are returned in the
    [MatchingJob.job][google.cloud.talent.v4beta1.SearchJobsResponse.MatchingJob.job]
    or
    [ListJobsResponse.jobs][google.cloud.talent.v4beta1.ListJobsResponse.jobs]
    fields.

    Values:
        JOB_VIEW_UNSPECIFIED (0):
            Default value.
        JOB_VIEW_ID_ONLY (1):
            A ID only view of job, with following attributes:
            [Job.name][google.cloud.talent.v4beta1.Job.name],
            [Job.requisition_id][google.cloud.talent.v4beta1.Job.requisition_id],
            [Job.language_code][google.cloud.talent.v4beta1.Job.language_code].
        JOB_VIEW_MINIMAL (2):
            A minimal view of the job, with the following attributes:
            [Job.name][google.cloud.talent.v4beta1.Job.name],
            [Job.requisition_id][google.cloud.talent.v4beta1.Job.requisition_id],
            [Job.title][google.cloud.talent.v4beta1.Job.title],
            [Job.company][google.cloud.talent.v4beta1.Job.company],
            [Job.DerivedInfo.locations][google.cloud.talent.v4beta1.Job.DerivedInfo.locations],
            [Job.language_code][google.cloud.talent.v4beta1.Job.language_code].
        JOB_VIEW_SMALL (3):
            A small view of the job, with the following attributes in
            the search results:
            [Job.name][google.cloud.talent.v4beta1.Job.name],
            [Job.requisition_id][google.cloud.talent.v4beta1.Job.requisition_id],
            [Job.title][google.cloud.talent.v4beta1.Job.title],
            [Job.company][google.cloud.talent.v4beta1.Job.company],
            [Job.DerivedInfo.locations][google.cloud.talent.v4beta1.Job.DerivedInfo.locations],
            [Job.visibility][google.cloud.talent.v4beta1.Job.visibility],
            [Job.language_code][google.cloud.talent.v4beta1.Job.language_code],
            [Job.description][google.cloud.talent.v4beta1.Job.description].
        JOB_VIEW_FULL (4):
            All available attributes are included in the
            search results.
    """

    JOB_VIEW_UNSPECIFIED = 0
    JOB_VIEW_ID_ONLY = 1
    JOB_VIEW_MINIMAL = 2
    JOB_VIEW_SMALL = 3
    JOB_VIEW_FULL = 4


class CreateJobRequest(proto.Message):
    r"""Create job request.

    Attributes:
        parent (str):
            Required. The resource name of the tenant under which the
            job is created.

            The format is "projects/{project_id}/tenants/{tenant_id}".
            For example, "projects/foo/tenant/bar". If tenant id is
            unspecified a default tenant is created. For example,
            "projects/foo".
        job (google.cloud.talent_v4beta1.types.Job):
            Required. The Job to be created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    job: gct_job.Job = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gct_job.Job,
    )


class GetJobRequest(proto.Message):
    r"""Get job request.

    Attributes:
        name (str):
            Required. The resource name of the job to retrieve.

            The format is
            "projects/{project_id}/tenants/{tenant_id}/jobs/{job_id}".
            For example, "projects/foo/tenants/bar/jobs/baz".

            If tenant id is unspecified, the default tenant is used. For
            example, "projects/foo/jobs/bar".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateJobRequest(proto.Message):
    r"""Update job request.

    Attributes:
        job (google.cloud.talent_v4beta1.types.Job):
            Required. The Job to be updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Strongly recommended for the best service experience.

            If
            [update_mask][google.cloud.talent.v4beta1.UpdateJobRequest.update_mask]
            is provided, only the specified fields in
            [job][google.cloud.talent.v4beta1.UpdateJobRequest.job] are
            updated. Otherwise all the fields are updated.

            A field mask to restrict the fields that are updated. Only
            top level fields of [Job][google.cloud.talent.v4beta1.Job]
            are supported.
    """

    job: gct_job.Job = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gct_job.Job,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteJobRequest(proto.Message):
    r"""Delete job request.

    Attributes:
        name (str):
            Required. The resource name of the job to be deleted.

            The format is
            "projects/{project_id}/tenants/{tenant_id}/jobs/{job_id}".
            For example, "projects/foo/tenants/bar/jobs/baz".

            If tenant id is unspecified, the default tenant is used. For
            example, "projects/foo/jobs/bar".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class BatchDeleteJobsRequest(proto.Message):
    r"""Batch delete jobs request.

    Attributes:
        parent (str):
            Required. The resource name of the tenant under which the
            job is created.

            The format is "projects/{project_id}/tenants/{tenant_id}".
            For example, "projects/foo/tenant/bar". If tenant id is
            unspecified, a default tenant is created. For example,
            "projects/foo".
        filter (str):
            Required. The filter string specifies the jobs to be
            deleted.

            Supported operator: =, AND

            The fields eligible for filtering are:

            - ``companyName`` (Required)
            - ``requisitionId`` (Required)

            Sample Query: companyName = "projects/foo/companies/bar" AND
            requisitionId = "req-1".
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListJobsRequest(proto.Message):
    r"""List jobs request.

    Attributes:
        parent (str):
            Required. The resource name of the tenant under which the
            job is created.

            The format is "projects/{project_id}/tenants/{tenant_id}".
            For example, "projects/foo/tenant/bar". If tenant id is
            unspecified, a default tenant is created. For example,
            "projects/foo".
        filter (str):
            Required. The filter string specifies the jobs to be
            enumerated.

            Supported operator: =, AND

            The fields eligible for filtering are:

            - ``companyName``
            - ``requisitionId``
            - ``status`` Available values: OPEN, EXPIRED, ALL. Defaults
              to OPEN if no value is specified.

            At least one of ``companyName`` and ``requisitionId`` must
            present or an INVALID_ARGUMENT error is thrown.

            Sample Query:

            - companyName = "projects/foo/tenants/bar/companies/baz"
            - companyName = "projects/foo/tenants/bar/companies/baz" AND
              requisitionId = "req-1"
            - companyName = "projects/foo/tenants/bar/companies/baz" AND
              status = "EXPIRED"
            - requisitionId = "req-1"
            - requisitionId = "req-1" AND status = "EXPIRED".
        page_token (str):
            The starting point of a query result.
        page_size (int):
            The maximum number of jobs to be returned per page of
            results.

            If
            [job_view][google.cloud.talent.v4beta1.ListJobsRequest.job_view]
            is set to
            [JobView.JOB_VIEW_ID_ONLY][google.cloud.talent.v4beta1.JobView.JOB_VIEW_ID_ONLY],
            the maximum allowed page size is 1000. Otherwise, the
            maximum allowed page size is 100.

            Default is 100 if empty or a number < 1 is specified.
        job_view (google.cloud.talent_v4beta1.types.JobView):
            The desired job attributes returned for jobs in the search
            response. Defaults to
            [JobView.JOB_VIEW_FULL][google.cloud.talent.v4beta1.JobView.JOB_VIEW_FULL]
            if no value is specified.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=4,
    )
    job_view: "JobView" = proto.Field(
        proto.ENUM,
        number=5,
        enum="JobView",
    )


class ListJobsResponse(proto.Message):
    r"""List jobs response.

    Attributes:
        jobs (MutableSequence[google.cloud.talent_v4beta1.types.Job]):
            The Jobs for a given company.

            The maximum number of items returned is based on
            the limit field provided in the request.
        next_page_token (str):
            A token to retrieve the next page of results.
        metadata (google.cloud.talent_v4beta1.types.ResponseMetadata):
            Additional information for the API
            invocation, such as the request tracking id.
    """

    @property
    def raw_page(self):
        return self

    jobs: MutableSequence[gct_job.Job] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gct_job.Job,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    metadata: common.ResponseMetadata = proto.Field(
        proto.MESSAGE,
        number=3,
        message=common.ResponseMetadata,
    )


class SearchJobsRequest(proto.Message):
    r"""The Request body of the ``SearchJobs`` call.

    Attributes:
        parent (str):
            Required. The resource name of the tenant to search within.

            The format is "projects/{project_id}/tenants/{tenant_id}".
            For example, "projects/foo/tenant/bar". If tenant id is
            unspecified, a default tenant is created. For example,
            "projects/foo".
        search_mode (google.cloud.talent_v4beta1.types.SearchJobsRequest.SearchMode):
            Mode of a search.

            Defaults to
            [SearchMode.JOB_SEARCH][google.cloud.talent.v4beta1.SearchJobsRequest.SearchMode.JOB_SEARCH].
        request_metadata (google.cloud.talent_v4beta1.types.RequestMetadata):
            Required. The meta information collected about the job
            searcher, used to improve the search quality of the service.
            The identifiers (such as ``user_id``) are provided by users,
            and must be unique and consistent.
        job_query (google.cloud.talent_v4beta1.types.JobQuery):
            Query used to search against jobs, such as
            keyword, location filters, etc.
        enable_broadening (bool):
            Controls whether to broaden the search when
            it produces sparse results. Broadened queries
            append results to the end of the matching
            results list.

            Defaults to false.
        require_precise_result_size (bool):
            This field is deprecated.
        histogram_queries (MutableSequence[google.cloud.talent_v4beta1.types.HistogramQuery]):
            An expression specifies a histogram request against matching
            jobs.

            Expression syntax is an aggregation function call with
            histogram facets and other options.

            Available aggregation function calls are:

            - ``count(string_histogram_facet)``: Count the number of
              matching entities, for each distinct attribute value.
            - ``count(numeric_histogram_facet, list of buckets)``: Count
              the number of matching entities within each bucket.

            A maximum of 200 histogram buckets are supported.

            Data types:

            - Histogram facet: facet names with format
              ``[a-zA-Z][a-zA-Z0-9_]+``.
            - String: string like "any string with backslash escape for
              quote(")."
            - Number: whole number and floating point number like 10, -1
              and -0.01.
            - List: list of elements with comma(,) separator surrounded
              by square brackets, for example, [1, 2, 3] and ["one",
              "two", "three"].

            Built-in constants:

            - MIN (minimum number similar to java Double.MIN_VALUE)
            - MAX (maximum number similar to java Double.MAX_VALUE)

            Built-in functions:

            - bucket(start, end[, label]): bucket built-in function
              creates a bucket with range of [start, end). Note that the
              end is exclusive, for example, bucket(1, MAX, "positive
              number") or bucket(1, 10).

            Job histogram facets:

            - company_display_name: histogram by
              [Job.company_display_name][google.cloud.talent.v4beta1.Job.company_display_name].
            - employment_type: histogram by
              [Job.employment_types][google.cloud.talent.v4beta1.Job.employment_types],
              for example, "FULL_TIME", "PART_TIME".
            - company_size (DEPRECATED): histogram by
              [CompanySize][google.cloud.talent.v4beta1.CompanySize],
              for example, "SMALL", "MEDIUM", "BIG".
            - publish_time_in_day: histogram by the
              [Job.posting_publish_time][google.cloud.talent.v4beta1.Job.posting_publish_time]
              in days. Must specify list of numeric buckets in spec.
            - publish_time_in_month: histogram by the
              [Job.posting_publish_time][google.cloud.talent.v4beta1.Job.posting_publish_time]
              in months. Must specify list of numeric buckets in spec.
            - publish_time_in_year: histogram by the
              [Job.posting_publish_time][google.cloud.talent.v4beta1.Job.posting_publish_time]
              in years. Must specify list of numeric buckets in spec.
            - degree_types: histogram by the
              [Job.degree_types][google.cloud.talent.v4beta1.Job.degree_types],
              for example, "Bachelors", "Masters".
            - job_level: histogram by the
              [Job.job_level][google.cloud.talent.v4beta1.Job.job_level],
              for example, "Entry Level".
            - country: histogram by the country code of jobs, for
              example, "US", "FR".
            - admin1: histogram by the admin1 code of jobs, which is a
              global placeholder referring to the state, province, or
              the particular term a country uses to define the
              geographic structure below the country level, for example,
              "CA", "IL".
            - city: histogram by a combination of the "city name, admin1
              code". For example, "Mountain View, CA", "New York, NY".
            - admin1_country: histogram by a combination of the "admin1
              code, country", for example, "CA, US", "IL, US".
            - city_coordinate: histogram by the city center's GPS
              coordinates (latitude and longitude), for example,
              37.4038522,-122.0987765. Since the coordinates of a city
              center can change, customers may need to refresh them
              periodically.
            - locale: histogram by the
              [Job.language_code][google.cloud.talent.v4beta1.Job.language_code],
              for example, "en-US", "fr-FR".
            - language: histogram by the language subtag of the
              [Job.language_code][google.cloud.talent.v4beta1.Job.language_code],
              for example, "en", "fr".
            - category: histogram by the
              [JobCategory][google.cloud.talent.v4beta1.JobCategory],
              for example, "COMPUTER_AND_IT", "HEALTHCARE".
            - base_compensation_unit: histogram by the
              [CompensationInfo.CompensationUnit][google.cloud.talent.v4beta1.CompensationInfo.CompensationUnit]
              of base salary, for example, "WEEKLY", "MONTHLY".
            - base_compensation: histogram by the base salary. Must
              specify list of numeric buckets to group results by.
            - annualized_base_compensation: histogram by the base
              annualized salary. Must specify list of numeric buckets to
              group results by.
            - annualized_total_compensation: histogram by the total
              annualized salary. Must specify list of numeric buckets to
              group results by.
            - string_custom_attribute: histogram by string
              [Job.custom_attributes][google.cloud.talent.v4beta1.Job.custom_attributes].
              Values can be accessed via square bracket notations like
              string_custom_attribute["key1"].
            - numeric_custom_attribute: histogram by numeric
              [Job.custom_attributes][google.cloud.talent.v4beta1.Job.custom_attributes].
              Values can be accessed via square bracket notations like
              numeric_custom_attribute["key1"]. Must specify list of
              numeric buckets to group results by.

            Example expressions:

            - ``count(admin1)``
            - ``count(base_compensation, [bucket(1000, 10000), bucket(10000, 100000), bucket(100000, MAX)])``
            - ``count(string_custom_attribute["some-string-custom-attribute"])``
            - ``count(numeric_custom_attribute["some-numeric-custom-attribute"], [bucket(MIN, 0, "negative"), bucket(0, MAX, "non-negative")])``
        job_view (google.cloud.talent_v4beta1.types.JobView):
            The desired job attributes returned for jobs in the search
            response. Defaults to
            [JobView.JOB_VIEW_SMALL][google.cloud.talent.v4beta1.JobView.JOB_VIEW_SMALL]
            if no value is specified.
        offset (int):
            An integer that specifies the current offset (that is,
            starting result location, amongst the jobs deemed by the API
            as relevant) in search results. This field is only
            considered if
            [page_token][google.cloud.talent.v4beta1.SearchJobsRequest.page_token]
            is unset.

            The maximum allowed value is 5000. Otherwise an error is
            thrown.

            For example, 0 means to return results starting from the
            first matching job, and 10 means to return from the 11th
            job. This can be used for pagination, (for example, pageSize
            = 10 and offset = 10 means to return from the second page).
        page_size (int):
            A limit on the number of jobs returned in the
            search results. Increasing this value above the
            default value of 10 can increase search response
            time. The value can be between 1 and 100.
        page_token (str):
            The token specifying the current offset within search
            results. See
            [SearchJobsResponse.next_page_token][google.cloud.talent.v4beta1.SearchJobsResponse.next_page_token]
            for an explanation of how to obtain the next set of query
            results.
        order_by (str):
            The criteria determining how search results are sorted.
            Default is ``"relevance desc"``.

            Supported options are:

            - ``"relevance desc"``: By relevance descending, as
              determined by the API algorithms. Relevance thresholding
              of query results is only available with this ordering.
            - ``"posting_publish_time desc"``: By
              [Job.posting_publish_time][google.cloud.talent.v4beta1.Job.posting_publish_time]
              descending.
            - ``"posting_update_time desc"``: By
              [Job.posting_update_time][google.cloud.talent.v4beta1.Job.posting_update_time]
              descending.
            - ``"title"``: By
              [Job.title][google.cloud.talent.v4beta1.Job.title]
              ascending.
            - ``"title desc"``: By
              [Job.title][google.cloud.talent.v4beta1.Job.title]
              descending.
            - ``"annualized_base_compensation"``: By job's
              [CompensationInfo.annualized_base_compensation_range][google.cloud.talent.v4beta1.CompensationInfo.annualized_base_compensation_range]
              ascending. Jobs whose annualized base compensation is
              unspecified are put at the end of search results.
            - ``"annualized_base_compensation desc"``: By job's
              [CompensationInfo.annualized_base_compensation_range][google.cloud.talent.v4beta1.CompensationInfo.annualized_base_compensation_range]
              descending. Jobs whose annualized base compensation is
              unspecified are put at the end of search results.
            - ``"annualized_total_compensation"``: By job's
              [CompensationInfo.annualized_total_compensation_range][google.cloud.talent.v4beta1.CompensationInfo.annualized_total_compensation_range]
              ascending. Jobs whose annualized base compensation is
              unspecified are put at the end of search results.
            - ``"annualized_total_compensation desc"``: By job's
              [CompensationInfo.annualized_total_compensation_range][google.cloud.talent.v4beta1.CompensationInfo.annualized_total_compensation_range]
              descending. Jobs whose annualized base compensation is
              unspecified are put at the end of search results.
            - ``"custom_ranking desc"``: By the relevance score adjusted
              to the
              [SearchJobsRequest.CustomRankingInfo.ranking_expression][google.cloud.talent.v4beta1.SearchJobsRequest.CustomRankingInfo.ranking_expression]
              with weight factor assigned by
              [SearchJobsRequest.CustomRankingInfo.importance_level][google.cloud.talent.v4beta1.SearchJobsRequest.CustomRankingInfo.importance_level]
              in descending order.
            - Location sorting: Use the special syntax to order jobs by
              distance: ``"distance_from('Hawaii')"``: Order by distance
              from Hawaii. ``"distance_from(19.89, 155.5)"``: Order by
              distance from a coordinate.
              ``"distance_from('Hawaii'), distance_from('Puerto Rico')"``:
              Order by multiple locations. See details below.
              ``"distance_from('Hawaii'), distance_from(19.89, 155.5)"``:
              Order by multiple locations. See details below. The string
              can have a maximum of 256 characters. When multiple
              distance centers are provided, a job that is close to any
              of the distance centers would have a high rank. When a job
              has multiple locations, the job location closest to one of
              the distance centers will be used. Jobs that don't have
              locations will be ranked at the bottom. Distance is
              calculated with a precision of 11.3 meters (37.4 feet).
              Diversification strategy is still applied unless
              explicitly disabled in
              [diversification_level][google.cloud.talent.v4beta1.SearchJobsRequest.diversification_level].
        diversification_level (google.cloud.talent_v4beta1.types.SearchJobsRequest.DiversificationLevel):
            Controls whether highly similar jobs are returned next to
            each other in the search results. Jobs are identified as
            highly similar based on their titles, job categories, and
            locations. Highly similar results are clustered so that only
            one representative job of the cluster is displayed to the
            job seeker higher up in the results, with the other jobs
            being displayed lower down in the results.

            Defaults to
            [DiversificationLevel.SIMPLE][google.cloud.talent.v4beta1.SearchJobsRequest.DiversificationLevel.SIMPLE]
            if no value is specified.
        custom_ranking_info (google.cloud.talent_v4beta1.types.SearchJobsRequest.CustomRankingInfo):
            Controls over how job documents get ranked on
            top of existing relevance score (determined by
            API algorithm).
        disable_keyword_match (bool):
            This field is deprecated. Please use
            [SearchJobsRequest.keyword_match_mode][google.cloud.talent.v4beta1.SearchJobsRequest.keyword_match_mode]
            going forward.

            To migrate, disable_keyword_match set to false maps to
            [KeywordMatchMode.KEYWORD_MATCH_ALL][google.cloud.talent.v4beta1.SearchJobsRequest.KeywordMatchMode.KEYWORD_MATCH_ALL],
            and disable_keyword_match set to true maps to
            [KeywordMatchMode.KEYWORD_MATCH_DISABLED][google.cloud.talent.v4beta1.SearchJobsRequest.KeywordMatchMode.KEYWORD_MATCH_DISABLED].
            If
            [SearchJobsRequest.keyword_match_mode][google.cloud.talent.v4beta1.SearchJobsRequest.keyword_match_mode]
            is set, this field is ignored.

            Controls whether to disable exact keyword match on
            [Job.title][google.cloud.talent.v4beta1.Job.title],
            [Job.description][google.cloud.talent.v4beta1.Job.description],
            [Job.company_display_name][google.cloud.talent.v4beta1.Job.company_display_name],
            [Job.addresses][google.cloud.talent.v4beta1.Job.addresses],
            [Job.qualifications][google.cloud.talent.v4beta1.Job.qualifications].
            When disable keyword match is turned off, a keyword match
            returns jobs that do not match given category filters when
            there are matching keywords. For example, for the query
            "program manager," a result is returned even if the job
            posting has the title "software developer," which doesn't
            fall into "program manager" ontology, but does have "program
            manager" appearing in its description.

            For queries like "cloud" that don't contain title or
            location specific ontology, jobs with "cloud" keyword
            matches are returned regardless of this flag's value.

            Use
            [Company.keyword_searchable_job_custom_attributes][google.cloud.talent.v4beta1.Company.keyword_searchable_job_custom_attributes]
            if company-specific globally matched custom field/attribute
            string values are needed. Enabling keyword match improves
            recall of subsequent search requests.

            Defaults to false.
        keyword_match_mode (google.cloud.talent_v4beta1.types.SearchJobsRequest.KeywordMatchMode):
            Controls what keyword match options to use.

            Defaults to
            [KeywordMatchMode.KEYWORD_MATCH_ALL][google.cloud.talent.v4beta1.SearchJobsRequest.KeywordMatchMode.KEYWORD_MATCH_ALL]
            if no value is specified.
        relevance_threshold (google.cloud.talent_v4beta1.types.SearchJobsRequest.RelevanceThreshold):
            Optional. The relevance threshold of the
            search results.
            Default to Google defined threshold, leveraging
            a balance of precision and recall to deliver
            both highly accurate results and comprehensive
            coverage of relevant information.
    """

    class SearchMode(proto.Enum):
        r"""A string-represented enumeration of the job search mode. The
        service operate differently for different modes of service.

        Values:
            SEARCH_MODE_UNSPECIFIED (0):
                The mode of the search method isn't specified. The default
                search behavior is identical to JOB_SEARCH search behavior.
            JOB_SEARCH (1):
                The job search matches against all jobs, and
                featured jobs (jobs with promotionValue > 0) are
                not specially handled.
            FEATURED_JOB_SEARCH (2):
                The job search matches only against featured
                jobs (jobs with a promotionValue > 0). This
                method doesn't return any jobs having a
                promotionValue <= 0. The search results order is
                determined by the promotionValue (jobs with a
                higher promotionValue are returned higher up in
                the search results), with relevance being used
                as a tiebreaker.
        """

        SEARCH_MODE_UNSPECIFIED = 0
        JOB_SEARCH = 1
        FEATURED_JOB_SEARCH = 2

    class DiversificationLevel(proto.Enum):
        r"""Controls whether highly similar jobs are returned next to
        each other in the search results. Jobs are identified as highly
        similar based on their titles, job categories, and locations.
        Highly similar results are clustered so that only one
        representative job of the cluster is displayed to the job seeker
        higher up in the results, with the other jobs being displayed
        lower down in the results.

        Values:
            DIVERSIFICATION_LEVEL_UNSPECIFIED (0):
                The diversification level isn't specified.
            DISABLED (1):
                Disables diversification. Jobs that would
                normally be pushed to the last page would not
                have their positions altered. This may result in
                highly similar jobs appearing in sequence in the
                search results.
            SIMPLE (2):
                Default diversifying behavior. The result
                list is ordered so that highly similar results
                are pushed to the end of the last page of search
                results. If you are using pageToken to page
                through the result set, latency might be lower
                but we can't guarantee that all results are
                returned. If you are using page offset, latency
                might be higher but all results are returned.
        """

        DIVERSIFICATION_LEVEL_UNSPECIFIED = 0
        DISABLED = 1
        SIMPLE = 2

    class KeywordMatchMode(proto.Enum):
        r"""Controls what keyword matching behavior the search has. When keyword
        matching is enabled, a keyword match returns jobs that may not match
        given category filters when there are matching keywords. For
        example, for the query "program manager" with KeywordMatchMode set
        to KEYWORD_MATCH_ALL, a job posting with the title "software
        developer," which doesn't fall into "program manager" ontology, and
        "program manager" appearing in its description will be surfaced.

        For queries like "cloud" that don't contain title or location
        specific ontology, jobs with "cloud" keyword matches are returned
        regardless of this enum's value.

        Use
        [Company.keyword_searchable_job_custom_attributes][google.cloud.talent.v4beta1.Company.keyword_searchable_job_custom_attributes]
        if company-specific globally matched custom field/attribute string
        values are needed. Enabling keyword match improves recall of
        subsequent search requests.

        Values:
            KEYWORD_MATCH_MODE_UNSPECIFIED (0):
                The keyword match option isn't specified. Defaults to
                [KeywordMatchMode.KEYWORD_MATCH_ALL][google.cloud.talent.v4beta1.SearchJobsRequest.KeywordMatchMode.KEYWORD_MATCH_ALL]
                behavior.
            KEYWORD_MATCH_DISABLED (1):
                Disables keyword matching.
            KEYWORD_MATCH_ALL (2):
                Enable keyword matching over
                [Job.title][google.cloud.talent.v4beta1.Job.title],
                [Job.description][google.cloud.talent.v4beta1.Job.description],
                [Job.company_display_name][google.cloud.talent.v4beta1.Job.company_display_name],
                [Job.addresses][google.cloud.talent.v4beta1.Job.addresses],
                [Job.qualifications][google.cloud.talent.v4beta1.Job.qualifications],
                and keyword searchable
                [Job.custom_attributes][google.cloud.talent.v4beta1.Job.custom_attributes]
                fields.
            KEYWORD_MATCH_TITLE_ONLY (3):
                Only enable keyword matching over
                [Job.title][google.cloud.talent.v4beta1.Job.title].
        """

        KEYWORD_MATCH_MODE_UNSPECIFIED = 0
        KEYWORD_MATCH_DISABLED = 1
        KEYWORD_MATCH_ALL = 2
        KEYWORD_MATCH_TITLE_ONLY = 3

    class RelevanceThreshold(proto.Enum):
        r"""The relevance threshold of the search results. The higher
        relevance threshold is, the higher relevant results are shown
        and the less number of results are returned.

        Values:
            RELEVANCE_THRESHOLD_UNSPECIFIED (0):
                Default value. In this case, server behavior
                defaults to Google defined threshold.
            LOWEST (1):
                Lowest relevance threshold.
            LOW (2):
                Low relevance threshold.
            MEDIUM (3):
                Medium relevance threshold.
            HIGH (4):
                High relevance threshold.
        """

        RELEVANCE_THRESHOLD_UNSPECIFIED = 0
        LOWEST = 1
        LOW = 2
        MEDIUM = 3
        HIGH = 4

    class CustomRankingInfo(proto.Message):
        r"""Custom ranking information for
        [SearchJobsRequest][google.cloud.talent.v4beta1.SearchJobsRequest].

        Attributes:
            importance_level (google.cloud.talent_v4beta1.types.SearchJobsRequest.CustomRankingInfo.ImportanceLevel):
                Required. Controls over how important the score of
                [CustomRankingInfo.ranking_expression][google.cloud.talent.v4beta1.SearchJobsRequest.CustomRankingInfo.ranking_expression]
                gets applied to job's final ranking position.

                An error is thrown if not specified.
            ranking_expression (str):
                Required. Controls over how job documents get ranked on top
                of existing relevance score (determined by API algorithm). A
                combination of the ranking expression and relevance score is
                used to determine job's final ranking position.

                The syntax for this expression is a subset of Google SQL
                syntax.

                Supported operators are: +, -, \*, /, where the left and
                right side of the operator is either a numeric
                [Job.custom_attributes][google.cloud.talent.v4beta1.Job.custom_attributes]
                key, integer/double value or an expression that can be
                evaluated to a number.

                Parenthesis are supported to adjust calculation precedence.
                The expression must be < 200 characters in length.

                The expression is considered invalid for a job if the
                expression references custom attributes that are not
                populated on the job or if the expression results in a
                divide by zero. If an expression is invalid for a job, that
                job is demoted to the end of the results.

                Sample ranking expression (year + 25) \* 0.25 - (freshness /
                0.5)
        """

        class ImportanceLevel(proto.Enum):
            r"""The importance level for
            [CustomRankingInfo.ranking_expression][google.cloud.talent.v4beta1.SearchJobsRequest.CustomRankingInfo.ranking_expression].

            Values:
                IMPORTANCE_LEVEL_UNSPECIFIED (0):
                    Default value if the importance level isn't
                    specified.
                NONE (1):
                    The given ranking expression is of None
                    importance, existing relevance score (determined
                    by API algorithm) dominates job's final ranking
                    position.
                LOW (2):
                    The given ranking expression is of Low
                    importance in terms of job's final ranking
                    position compared to existing relevance score
                    (determined by API algorithm).
                MILD (3):
                    The given ranking expression is of Mild
                    importance in terms of job's final ranking
                    position compared to existing relevance score
                    (determined by API algorithm).
                MEDIUM (4):
                    The given ranking expression is of Medium
                    importance in terms of job's final ranking
                    position compared to existing relevance score
                    (determined by API algorithm).
                HIGH (5):
                    The given ranking expression is of High
                    importance in terms of job's final ranking
                    position compared to existing relevance score
                    (determined by API algorithm).
                EXTREME (6):
                    The given ranking expression is of Extreme
                    importance, and dominates job's final ranking
                    position with existing relevance score
                    (determined by API algorithm) ignored.
            """

            IMPORTANCE_LEVEL_UNSPECIFIED = 0
            NONE = 1
            LOW = 2
            MILD = 3
            MEDIUM = 4
            HIGH = 5
            EXTREME = 6

        importance_level: "SearchJobsRequest.CustomRankingInfo.ImportanceLevel" = (
            proto.Field(
                proto.ENUM,
                number=1,
                enum="SearchJobsRequest.CustomRankingInfo.ImportanceLevel",
            )
        )
        ranking_expression: str = proto.Field(
            proto.STRING,
            number=2,
        )

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    search_mode: SearchMode = proto.Field(
        proto.ENUM,
        number=2,
        enum=SearchMode,
    )
    request_metadata: common.RequestMetadata = proto.Field(
        proto.MESSAGE,
        number=3,
        message=common.RequestMetadata,
    )
    job_query: filters.JobQuery = proto.Field(
        proto.MESSAGE,
        number=4,
        message=filters.JobQuery,
    )
    enable_broadening: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    require_precise_result_size: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    histogram_queries: MutableSequence[histogram.HistogramQuery] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message=histogram.HistogramQuery,
    )
    job_view: "JobView" = proto.Field(
        proto.ENUM,
        number=8,
        enum="JobView",
    )
    offset: int = proto.Field(
        proto.INT32,
        number=9,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=10,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=11,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=12,
    )
    diversification_level: DiversificationLevel = proto.Field(
        proto.ENUM,
        number=13,
        enum=DiversificationLevel,
    )
    custom_ranking_info: CustomRankingInfo = proto.Field(
        proto.MESSAGE,
        number=14,
        message=CustomRankingInfo,
    )
    disable_keyword_match: bool = proto.Field(
        proto.BOOL,
        number=16,
    )
    keyword_match_mode: KeywordMatchMode = proto.Field(
        proto.ENUM,
        number=18,
        enum=KeywordMatchMode,
    )
    relevance_threshold: RelevanceThreshold = proto.Field(
        proto.ENUM,
        number=19,
        enum=RelevanceThreshold,
    )


class SearchJobsResponse(proto.Message):
    r"""Response for SearchJob method.

    Attributes:
        matching_jobs (MutableSequence[google.cloud.talent_v4beta1.types.SearchJobsResponse.MatchingJob]):
            The Job entities that match the specified
            [SearchJobsRequest][google.cloud.talent.v4beta1.SearchJobsRequest].
        histogram_query_results (MutableSequence[google.cloud.talent_v4beta1.types.HistogramQueryResult]):
            The histogram results that match with specified
            [SearchJobsRequest.histogram_queries][google.cloud.talent.v4beta1.SearchJobsRequest.histogram_queries].
        next_page_token (str):
            The token that specifies the starting
            position of the next page of results. This field
            is empty if there are no more results.
        location_filters (MutableSequence[google.cloud.talent_v4beta1.types.Location]):
            The location filters that the service applied to the
            specified query. If any filters are lat-lng based, the
            [Location.location_type][google.cloud.talent.v4beta1.Location.location_type]
            is
            [Location.LocationType.LOCATION_TYPE_UNSPECIFIED][google.cloud.talent.v4beta1.Location.LocationType.LOCATION_TYPE_UNSPECIFIED].
        estimated_total_size (int):
            An estimation of the number of jobs that match the specified
            query.

            This number isn't guaranteed to be accurate. For accurate
            results, see
            [SearchJobsResponse.total_size][google.cloud.talent.v4beta1.SearchJobsResponse.total_size].
        total_size (int):
            The precise result count with limit 100,000.
        metadata (google.cloud.talent_v4beta1.types.ResponseMetadata):
            Additional information for the API
            invocation, such as the request tracking id.
        broadened_query_jobs_count (int):
            If query broadening is enabled, we may append
            additional results from the broadened query.
            This number indicates how many of the jobs
            returned in the jobs field are from the
            broadened query. These results are always at the
            end of the jobs list. In particular, a value of
            0, or if the field isn't set, all the jobs in
            the jobs list are from the original (without
            broadening) query. If this field is non-zero,
            subsequent requests with offset after this
            result set should contain all broadened results.
        spell_correction (google.cloud.talent_v4beta1.types.SpellingCorrection):
            The spell checking result, and correction.
    """

    class MatchingJob(proto.Message):
        r"""Job entry with metadata inside
        [SearchJobsResponse][google.cloud.talent.v4beta1.SearchJobsResponse].

        Attributes:
            job (google.cloud.talent_v4beta1.types.Job):
                Job resource that matches the specified
                [SearchJobsRequest][google.cloud.talent.v4beta1.SearchJobsRequest].
            job_summary (str):
                A summary of the job with core information
                that's displayed on the search results listing
                page.
            job_title_snippet (str):
                Contains snippets of text from the
                [Job.title][google.cloud.talent.v4beta1.Job.title] field
                most closely matching a search query's keywords, if
                available. The matching query keywords are enclosed in HTML
                bold tags.
            search_text_snippet (str):
                Contains snippets of text from the
                [Job.description][google.cloud.talent.v4beta1.Job.description]
                and similar fields that most closely match a search query's
                keywords, if available. All HTML tags in the original fields
                are stripped when returned in this field, and matching query
                keywords are enclosed in HTML bold tags.
            commute_info (google.cloud.talent_v4beta1.types.SearchJobsResponse.CommuteInfo):
                Commute information which is generated based on specified
                [CommuteFilter][google.cloud.talent.v4beta1.CommuteFilter].
        """

        job: gct_job.Job = proto.Field(
            proto.MESSAGE,
            number=1,
            message=gct_job.Job,
        )
        job_summary: str = proto.Field(
            proto.STRING,
            number=2,
        )
        job_title_snippet: str = proto.Field(
            proto.STRING,
            number=3,
        )
        search_text_snippet: str = proto.Field(
            proto.STRING,
            number=4,
        )
        commute_info: "SearchJobsResponse.CommuteInfo" = proto.Field(
            proto.MESSAGE,
            number=5,
            message="SearchJobsResponse.CommuteInfo",
        )

    class CommuteInfo(proto.Message):
        r"""Commute details related to this job.

        Attributes:
            job_location (google.cloud.talent_v4beta1.types.Location):
                Location used as the destination in the
                commute calculation.
            travel_duration (google.protobuf.duration_pb2.Duration):
                The number of seconds required to travel to
                the job location from the query location. A
                duration of 0 seconds indicates that the job
                isn't reachable within the requested duration,
                but was returned as part of an expanded query.
        """

        job_location: common.Location = proto.Field(
            proto.MESSAGE,
            number=1,
            message=common.Location,
        )
        travel_duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=2,
            message=duration_pb2.Duration,
        )

    @property
    def raw_page(self):
        return self

    matching_jobs: MutableSequence[MatchingJob] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=MatchingJob,
    )
    histogram_query_results: MutableSequence[histogram.HistogramQueryResult] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message=histogram.HistogramQueryResult,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    location_filters: MutableSequence[common.Location] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=common.Location,
    )
    estimated_total_size: int = proto.Field(
        proto.INT32,
        number=5,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=6,
    )
    metadata: common.ResponseMetadata = proto.Field(
        proto.MESSAGE,
        number=7,
        message=common.ResponseMetadata,
    )
    broadened_query_jobs_count: int = proto.Field(
        proto.INT32,
        number=8,
    )
    spell_correction: common.SpellingCorrection = proto.Field(
        proto.MESSAGE,
        number=9,
        message=common.SpellingCorrection,
    )


class BatchCreateJobsRequest(proto.Message):
    r"""Request to create a batch of jobs.

    Attributes:
        parent (str):
            Required. The resource name of the tenant under which the
            job is created.

            The format is "projects/{project_id}/tenants/{tenant_id}".
            For example, "projects/foo/tenant/bar". If tenant id is
            unspecified, a default tenant is created. For example,
            "projects/foo".
        jobs (MutableSequence[google.cloud.talent_v4beta1.types.Job]):
            Required. The jobs to be created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    jobs: MutableSequence[gct_job.Job] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=gct_job.Job,
    )


class BatchUpdateJobsRequest(proto.Message):
    r"""Request to update a batch of jobs.

    Attributes:
        parent (str):
            Required. The resource name of the tenant under which the
            job is created.

            The format is "projects/{project_id}/tenants/{tenant_id}".
            For example, "projects/foo/tenant/bar". If tenant id is
            unspecified, a default tenant is created. For example,
            "projects/foo".
        jobs (MutableSequence[google.cloud.talent_v4beta1.types.Job]):
            Required. The jobs to be updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Strongly recommended for the best service experience. Be
            aware that it will also increase latency when checking the
            status of a batch operation.

            If
            [update_mask][google.cloud.talent.v4beta1.BatchUpdateJobsRequest.update_mask]
            is provided, only the specified fields in
            [Job][google.cloud.talent.v4beta1.Job] are updated.
            Otherwise all the fields are updated.

            A field mask to restrict the fields that are updated. Only
            top level fields of [Job][google.cloud.talent.v4beta1.Job]
            are supported.

            If
            [update_mask][google.cloud.talent.v4beta1.BatchUpdateJobsRequest.update_mask]
            is provided, The [Job][google.cloud.talent.v4beta1.Job]
            inside
            [JobResult][google.cloud.talent.v4beta1.JobOperationResult.JobResult]
            will only contains fields that is updated, plus the Id of
            the Job. Otherwise, [Job][google.cloud.talent.v4beta1.Job]
            will include all fields, which can yield a very large
            response.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    jobs: MutableSequence[gct_job.Job] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=gct_job.Job,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=3,
        message=field_mask_pb2.FieldMask,
    )


class JobOperationResult(proto.Message):
    r"""The result of
    [JobService.BatchCreateJobs][google.cloud.talent.v4beta1.JobService.BatchCreateJobs]
    or
    [JobService.BatchUpdateJobs][google.cloud.talent.v4beta1.JobService.BatchUpdateJobs]
    APIs. It's used to replace
    [google.longrunning.Operation.response][google.longrunning.Operation.response]
    in case of success.

    Attributes:
        job_results (MutableSequence[google.cloud.talent_v4beta1.types.JobOperationResult.JobResult]):
            List of job mutation results from a batch
            mutate operation. It can change until operation
            status is FINISHED, FAILED or CANCELLED.
    """

    class JobResult(proto.Message):
        r"""Mutation result of a job.

        Attributes:
            job (google.cloud.talent_v4beta1.types.Job):
                Here [Job][google.cloud.talent.v4beta1.Job] only contains
                basic information including
                [name][google.cloud.talent.v4beta1.Job.name],
                [company][google.cloud.talent.v4beta1.Job.company],
                [language_code][google.cloud.talent.v4beta1.Job.language_code]
                and
                [requisition_id][google.cloud.talent.v4beta1.Job.requisition_id],
                use getJob method to retrieve detailed information of the
                created/updated job.
            status (google.rpc.status_pb2.Status):
                The status of the job processed. This field is populated if
                the processing of the
                [job][google.cloud.talent.v4beta1.JobOperationResult.JobResult.job]
                fails.
        """

        job: gct_job.Job = proto.Field(
            proto.MESSAGE,
            number=1,
            message=gct_job.Job,
        )
        status: status_pb2.Status = proto.Field(
            proto.MESSAGE,
            number=2,
            message=status_pb2.Status,
        )

    job_results: MutableSequence[JobResult] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=JobResult,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
