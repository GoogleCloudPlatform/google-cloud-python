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
import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.securitycenter_v1beta1.types import asset as gcs_asset
from google.cloud.securitycenter_v1beta1.types import finding as gcs_finding
from google.cloud.securitycenter_v1beta1.types import (
    organization_settings as gcs_organization_settings,
)
from google.cloud.securitycenter_v1beta1.types import (
    security_marks as gcs_security_marks,
)
from google.cloud.securitycenter_v1beta1.types import source as gcs_source

__protobuf__ = proto.module(
    package="google.cloud.securitycenter.v1beta1",
    manifest={
        "CreateFindingRequest",
        "CreateSourceRequest",
        "GetOrganizationSettingsRequest",
        "GetSourceRequest",
        "GroupAssetsRequest",
        "GroupAssetsResponse",
        "GroupFindingsRequest",
        "GroupFindingsResponse",
        "GroupResult",
        "ListSourcesRequest",
        "ListSourcesResponse",
        "ListAssetsRequest",
        "ListAssetsResponse",
        "ListFindingsRequest",
        "ListFindingsResponse",
        "SetFindingStateRequest",
        "RunAssetDiscoveryRequest",
        "UpdateFindingRequest",
        "UpdateOrganizationSettingsRequest",
        "UpdateSourceRequest",
        "UpdateSecurityMarksRequest",
    },
)


class CreateFindingRequest(proto.Message):
    r"""Request message for creating a finding.

    Attributes:
        parent (str):
            Required. Resource name of the new finding's parent. Its
            format should be
            "organizations/[organization_id]/sources/[source_id]".
        finding_id (str):
            Required. Unique identifier provided by the
            client within the parent scope. It must be
            alphanumeric and less than or equal to 32
            characters and greater than 0 characters in
            length.
        finding (google.cloud.securitycenter_v1beta1.types.Finding):
            Required. The Finding being created. The name and
            security_marks will be ignored as they are both output only
            fields on this resource.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    finding_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    finding: gcs_finding.Finding = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcs_finding.Finding,
    )


class CreateSourceRequest(proto.Message):
    r"""Request message for creating a source.

    Attributes:
        parent (str):
            Required. Resource name of the new source's parent. Its
            format should be "organizations/[organization_id]".
        source (google.cloud.securitycenter_v1beta1.types.Source):
            Required. The Source being created, only the display_name
            and description will be used. All other fields will be
            ignored.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    source: gcs_source.Source = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcs_source.Source,
    )


class GetOrganizationSettingsRequest(proto.Message):
    r"""Request message for getting organization settings.

    Attributes:
        name (str):
            Required. Name of the organization to get organization
            settings for. Its format is
            "organizations/[organization_id]/organizationSettings".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetSourceRequest(proto.Message):
    r"""Request message for getting a source.

    Attributes:
        name (str):
            Required. Relative resource name of the source. Its format
            is "organizations/[organization_id]/source/[source_id]".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GroupAssetsRequest(proto.Message):
    r"""Request message for grouping by assets.

    Attributes:
        parent (str):
            Required. Name of the organization to groupBy. Its format is
            "organizations/[organization_id]".
        filter (str):
            Expression that defines the filter to apply across assets.
            The expression is a list of zero or more restrictions
            combined via logical operators ``AND`` and ``OR``.
            Parentheses are not supported, and ``OR`` has higher
            precedence than ``AND``.

            Restrictions have the form ``<field> <operator> <value>``
            and may have a ``-`` character in front of them to indicate
            negation. The fields map to those defined in the Asset
            resource. Examples include:

            - name
            - security_center_properties.resource_name
            - resource_properties.a_property
            - security_marks.marks.marka

            The supported operators are:

            - ``=`` for all value types.
            - ``>``, ``<``, ``>=``, ``<=`` for integer values.
            - ``:``, meaning substring matching, for strings.

            The supported value types are:

            - string literals in quotes.
            - integer literals without quotes.
            - boolean literals ``true`` and ``false`` without quotes.

            For example, ``resource_properties.size = 100`` is a valid
            filter string.
        group_by (str):
            Required. Expression that defines what assets fields to use
            for grouping. The string value should follow SQL syntax:
            comma separated list of fields. For example:
            "security_center_properties.resource_project,security_center_properties.project".

            The following fields are supported when compare_duration is
            not set:

            - security_center_properties.resource_project
            - security_center_properties.resource_type
            - security_center_properties.resource_parent

            The following fields are supported when compare_duration is
            set:

            - security_center_properties.resource_type
        compare_duration (google.protobuf.duration_pb2.Duration):
            When compare_duration is set, the Asset's "state" property
            is updated to indicate whether the asset was added, removed,
            or remained present during the compare_duration period of
            time that precedes the read_time. This is the time between
            (read_time - compare_duration) and read_time.

            The state value is derived based on the presence of the
            asset at the two points in time. Intermediate state changes
            between the two times don't affect the result. For example,
            the results aren't affected if the asset is removed and
            re-created again.

            Possible "state" values when compare_duration is specified:

            - "ADDED": indicates that the asset was not present before
              compare_duration, but present at reference_time.
            - "REMOVED": indicates that the asset was present at the
              start of compare_duration, but not present at
              reference_time.
            - "ACTIVE": indicates that the asset was present at both the
              start and the end of the time period defined by
              compare_duration and reference_time.

            This field is ignored if ``state`` is not a field in
            ``group_by``.
        read_time (google.protobuf.timestamp_pb2.Timestamp):
            Time used as a reference point when filtering
            assets. The filter is limited to assets existing
            at the supplied time and their values are those
            at that specific time. Absence of this field
            will default to the API's version of NOW.
        page_token (str):
            The value returned by the last ``GroupAssetsResponse``;
            indicates that this is a continuation of a prior
            ``GroupAssets`` call, and that the system should return the
            next page of data.
        page_size (int):
            The maximum number of results to return in a
            single response. Default is 10, minimum is 1,
            maximum is 1000.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    group_by: str = proto.Field(
        proto.STRING,
        number=3,
    )
    compare_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=4,
        message=duration_pb2.Duration,
    )
    read_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=7,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=8,
    )


class GroupAssetsResponse(proto.Message):
    r"""Response message for grouping by assets.

    Attributes:
        group_by_results (MutableSequence[google.cloud.securitycenter_v1beta1.types.GroupResult]):
            Group results. There exists an element for
            each existing unique combination of
            property/values. The element contains a count
            for the number of times those specific
            property/values appear.
        read_time (google.protobuf.timestamp_pb2.Timestamp):
            Time used for executing the groupBy request.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results.
    """

    @property
    def raw_page(self):
        return self

    group_by_results: MutableSequence["GroupResult"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="GroupResult",
    )
    read_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GroupFindingsRequest(proto.Message):
    r"""Request message for grouping by findings.

    Attributes:
        parent (str):
            Required. Name of the source to groupBy. Its format is
            "organizations/[organization_id]/sources/[source_id]". To
            groupBy across all sources provide a source_id of ``-``. For
            example: organizations/{organization_id}/sources/-
        filter (str):
            Expression that defines the filter to apply across findings.
            The expression is a list of one or more restrictions
            combined via logical operators ``AND`` and ``OR``.
            Parentheses are not supported, and ``OR`` has higher
            precedence than ``AND``.

            Restrictions have the form ``<field> <operator> <value>``
            and may have a ``-`` character in front of them to indicate
            negation. Examples include:

            - name
            - source_properties.a_property
            - security_marks.marks.marka

            The supported operators are:

            - ``=`` for all value types.
            - ``>``, ``<``, ``>=``, ``<=`` for integer values.
            - ``:``, meaning substring matching, for strings.

            The supported value types are:

            - string literals in quotes.
            - integer literals without quotes.
            - boolean literals ``true`` and ``false`` without quotes.

            For example, ``source_properties.size = 100`` is a valid
            filter string.
        group_by (str):
            Required. Expression that defines what assets fields to use
            for grouping (including ``state``). The string value should
            follow SQL syntax: comma separated list of fields. For
            example: "parent,resource_name".

            The following fields are supported:

            - resource_name
            - category
            - state
            - parent
        read_time (google.protobuf.timestamp_pb2.Timestamp):
            Time used as a reference point when filtering
            findings. The filter is limited to findings
            existing at the supplied time and their values
            are those at that specific time. Absence of this
            field will default to the API's version of NOW.
        page_token (str):
            The value returned by the last ``GroupFindingsResponse``;
            indicates that this is a continuation of a prior
            ``GroupFindings`` call, and that the system should return
            the next page of data.
        page_size (int):
            The maximum number of results to return in a
            single response. Default is 10, minimum is 1,
            maximum is 1000.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    group_by: str = proto.Field(
        proto.STRING,
        number=3,
    )
    read_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=5,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=6,
    )


class GroupFindingsResponse(proto.Message):
    r"""Response message for group by findings.

    Attributes:
        group_by_results (MutableSequence[google.cloud.securitycenter_v1beta1.types.GroupResult]):
            Group results. There exists an element for
            each existing unique combination of
            property/values. The element contains a count
            for the number of times those specific
            property/values appear.
        read_time (google.protobuf.timestamp_pb2.Timestamp):
            Time used for executing the groupBy request.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results.
    """

    @property
    def raw_page(self):
        return self

    group_by_results: MutableSequence["GroupResult"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="GroupResult",
    )
    read_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GroupResult(proto.Message):
    r"""Result containing the properties and count of a groupBy
    request.

    Attributes:
        properties (MutableMapping[str, google.protobuf.struct_pb2.Value]):
            Properties matching the groupBy fields in the
            request.
        count (int):
            Total count of resources for the given
            properties.
    """

    properties: MutableMapping[str, struct_pb2.Value] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=1,
        message=struct_pb2.Value,
    )
    count: int = proto.Field(
        proto.INT64,
        number=2,
    )


class ListSourcesRequest(proto.Message):
    r"""Request message for listing sources.

    Attributes:
        parent (str):
            Required. Resource name of the parent of sources to list.
            Its format should be "organizations/[organization_id]".
        page_token (str):
            The value returned by the last ``ListSourcesResponse``;
            indicates that this is a continuation of a prior
            ``ListSources`` call, and that the system should return the
            next page of data.
        page_size (int):
            The maximum number of results to return in a
            single response. Default is 10, minimum is 1,
            maximum is 1000.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=7,
    )


class ListSourcesResponse(proto.Message):
    r"""Response message for listing sources.

    Attributes:
        sources (MutableSequence[google.cloud.securitycenter_v1beta1.types.Source]):
            Sources belonging to the requested parent.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results.
    """

    @property
    def raw_page(self):
        return self

    sources: MutableSequence[gcs_source.Source] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcs_source.Source,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListAssetsRequest(proto.Message):
    r"""Request message for listing assets.

    Attributes:
        parent (str):
            Required. Name of the organization assets should belong to.
            Its format is "organizations/[organization_id]".
        filter (str):
            Expression that defines the filter to apply across assets.
            The expression is a list of zero or more restrictions
            combined via logical operators ``AND`` and ``OR``.
            Parentheses are not supported, and ``OR`` has higher
            precedence than ``AND``.

            Restrictions have the form ``<field> <operator> <value>``
            and may have a ``-`` character in front of them to indicate
            negation. The fields map to those defined in the Asset
            resource. Examples include:

            - name
            - security_center_properties.resource_name
            - resource_properties.a_property
            - security_marks.marks.marka

            The supported operators are:

            - ``=`` for all value types.
            - ``>``, ``<``, ``>=``, ``<=`` for integer values.
            - ``:``, meaning substring matching, for strings.

            The supported value types are:

            - string literals in quotes.
            - integer literals without quotes.
            - boolean literals ``true`` and ``false`` without quotes.

            For example, ``resource_properties.size = 100`` is a valid
            filter string.
        order_by (str):
            Expression that defines what fields and order to use for
            sorting. The string value should follow SQL syntax: comma
            separated list of fields. For example:
            "name,resource_properties.a_property". The default sorting
            order is ascending. To specify descending order for a field,
            a suffix " desc" should be appended to the field name. For
            example: "name desc,resource_properties.a_property".
            Redundant space characters in the syntax are insignificant.
            "name desc,resource_properties.a_property" and " name desc ,
            resource_properties.a_property " are equivalent.
        read_time (google.protobuf.timestamp_pb2.Timestamp):
            Time used as a reference point when filtering
            assets. The filter is limited to assets existing
            at the supplied time and their values are those
            at that specific time. Absence of this field
            will default to the API's version of NOW.
        compare_duration (google.protobuf.duration_pb2.Duration):
            When compare_duration is set, the ListAssetResult's "state"
            attribute is updated to indicate whether the asset was
            added, removed, or remained present during the
            compare_duration period of time that precedes the read_time.
            This is the time between (read_time - compare_duration) and
            read_time.

            The state value is derived based on the presence of the
            asset at the two points in time. Intermediate state changes
            between the two times don't affect the result. For example,
            the results aren't affected if the asset is removed and
            re-created again.

            Possible "state" values when compare_duration is specified:

            - "ADDED": indicates that the asset was not present before
              compare_duration, but present at read_time.
            - "REMOVED": indicates that the asset was present at the
              start of compare_duration, but not present at read_time.
            - "ACTIVE": indicates that the asset was present at both the
              start and the end of the time period defined by
              compare_duration and read_time.

            If compare_duration is not specified, then the only possible
            state is "UNUSED", which indicates that the asset is present
            at read_time.
        field_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. A field mask to specify the
            ListAssetsResult fields to be listed in the
            response. An empty field mask will list all
            fields.
        page_token (str):
            The value returned by the last ``ListAssetsResponse``;
            indicates that this is a continuation of a prior
            ``ListAssets`` call, and that the system should return the
            next page of data.
        page_size (int):
            The maximum number of results to return in a
            single response. Default is 10, minimum is 1,
            maximum is 1000.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=3,
    )
    read_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    compare_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=5,
        message=duration_pb2.Duration,
    )
    field_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=7,
        message=field_mask_pb2.FieldMask,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=8,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=9,
    )


class ListAssetsResponse(proto.Message):
    r"""Response message for listing assets.

    Attributes:
        list_assets_results (MutableSequence[google.cloud.securitycenter_v1beta1.types.ListAssetsResponse.ListAssetsResult]):
            Assets matching the list request.
        read_time (google.protobuf.timestamp_pb2.Timestamp):
            Time used for executing the list request.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results.
        total_size (int):
            The total number of assets matching the
            query.
    """

    class ListAssetsResult(proto.Message):
        r"""Result containing the Asset and its State.

        Attributes:
            asset (google.cloud.securitycenter_v1beta1.types.Asset):
                Asset matching the search request.
            state (google.cloud.securitycenter_v1beta1.types.ListAssetsResponse.ListAssetsResult.State):
                State of the asset.
        """

        class State(proto.Enum):
            r"""State of the asset.

            When querying across two points in time this describes the change
            between the two points: ADDED, REMOVED, or ACTIVE. If there was no
            compare_duration supplied in the request the state should be: UNUSED

            Values:
                STATE_UNSPECIFIED (0):
                    Unspecified state.
                UNUSED (1):
                    Request did not specify use of this field in
                    the result.
                ADDED (2):
                    Asset was added between the points in time.
                REMOVED (3):
                    Asset was removed between the points in time.
                ACTIVE (4):
                    Asset was active at both point(s) in time.
            """

            STATE_UNSPECIFIED = 0
            UNUSED = 1
            ADDED = 2
            REMOVED = 3
            ACTIVE = 4

        asset: gcs_asset.Asset = proto.Field(
            proto.MESSAGE,
            number=1,
            message=gcs_asset.Asset,
        )
        state: "ListAssetsResponse.ListAssetsResult.State" = proto.Field(
            proto.ENUM,
            number=2,
            enum="ListAssetsResponse.ListAssetsResult.State",
        )

    @property
    def raw_page(self):
        return self

    list_assets_results: MutableSequence[ListAssetsResult] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=ListAssetsResult,
    )
    read_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=4,
    )


class ListFindingsRequest(proto.Message):
    r"""Request message for listing findings.

    Attributes:
        parent (str):
            Required. Name of the source the findings belong to. Its
            format is
            "organizations/[organization_id]/sources/[source_id]". To
            list across all sources provide a source_id of ``-``. For
            example: organizations/{organization_id}/sources/-
        filter (str):
            Expression that defines the filter to apply across findings.
            The expression is a list of one or more restrictions
            combined via logical operators ``AND`` and ``OR``.
            Parentheses are not supported, and ``OR`` has higher
            precedence than ``AND``.

            Restrictions have the form ``<field> <operator> <value>``
            and may have a ``-`` character in front of them to indicate
            negation. Examples include:

            - name
            - source_properties.a_property
            - security_marks.marks.marka

            The supported operators are:

            - ``=`` for all value types.
            - ``>``, ``<``, ``>=``, ``<=`` for integer values.
            - ``:``, meaning substring matching, for strings.

            The supported value types are:

            - string literals in quotes.
            - integer literals without quotes.
            - boolean literals ``true`` and ``false`` without quotes.

            For example, ``source_properties.size = 100`` is a valid
            filter string.
        order_by (str):
            Expression that defines what fields and order to use for
            sorting. The string value should follow SQL syntax: comma
            separated list of fields. For example:
            "name,resource_properties.a_property". The default sorting
            order is ascending. To specify descending order for a field,
            a suffix " desc" should be appended to the field name. For
            example: "name desc,source_properties.a_property". Redundant
            space characters in the syntax are insignificant. "name
            desc,source_properties.a_property" and " name desc ,
            source_properties.a_property " are equivalent.
        read_time (google.protobuf.timestamp_pb2.Timestamp):
            Time used as a reference point when filtering
            findings. The filter is limited to findings
            existing at the supplied time and their values
            are those at that specific time. Absence of this
            field will default to the API's version of NOW.
        field_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. A field mask to specify the Finding
            fields to be listed in the response. An empty
            field mask will list all fields.
        page_token (str):
            The value returned by the last ``ListFindingsResponse``;
            indicates that this is a continuation of a prior
            ``ListFindings`` call, and that the system should return the
            next page of data.
        page_size (int):
            The maximum number of results to return in a
            single response. Default is 10, minimum is 1,
            maximum is 1000.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=3,
    )
    read_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    field_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=5,
        message=field_mask_pb2.FieldMask,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=6,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=7,
    )


class ListFindingsResponse(proto.Message):
    r"""Response message for listing findings.

    Attributes:
        findings (MutableSequence[google.cloud.securitycenter_v1beta1.types.Finding]):
            Findings matching the list request.
        read_time (google.protobuf.timestamp_pb2.Timestamp):
            Time used for executing the list request.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results.
        total_size (int):
            The total number of findings matching the
            query.
    """

    @property
    def raw_page(self):
        return self

    findings: MutableSequence[gcs_finding.Finding] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcs_finding.Finding,
    )
    read_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=4,
    )


class SetFindingStateRequest(proto.Message):
    r"""Request message for updating a finding's state.

    Attributes:
        name (str):
            Required. The relative resource name of the finding. See:
            https://cloud.google.com/apis/design/resource_names#relative_resource_name
            Example:
            "organizations/{organization_id}/sources/{source_id}/finding/{finding_id}".
        state (google.cloud.securitycenter_v1beta1.types.Finding.State):
            Required. The desired State of the finding.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Required. The time at which the updated state
            takes effect.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: gcs_finding.Finding.State = proto.Field(
        proto.ENUM,
        number=2,
        enum=gcs_finding.Finding.State,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


class RunAssetDiscoveryRequest(proto.Message):
    r"""Request message for running asset discovery for an
    organization.

    Attributes:
        parent (str):
            Required. Name of the organization to run asset discovery
            for. Its format is "organizations/[organization_id]".
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateFindingRequest(proto.Message):
    r"""Request message for updating or creating a finding.

    Attributes:
        finding (google.cloud.securitycenter_v1beta1.types.Finding):
            Required. The finding resource to update or create if it
            does not already exist. parent, security_marks, and
            update_time will be ignored.

            In the case of creation, the finding id portion of the name
            must alphanumeric and less than or equal to 32 characters
            and greater than 0 characters in length.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The FieldMask to use when updating the
            finding resource. This field should not be
            specified when creating a finding.
    """

    finding: gcs_finding.Finding = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcs_finding.Finding,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class UpdateOrganizationSettingsRequest(proto.Message):
    r"""Request message for updating an organization's settings.

    Attributes:
        organization_settings (google.cloud.securitycenter_v1beta1.types.OrganizationSettings):
            Required. The organization settings resource
            to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The FieldMask to use when updating the
            settings resource.
    """

    organization_settings: gcs_organization_settings.OrganizationSettings = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcs_organization_settings.OrganizationSettings,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class UpdateSourceRequest(proto.Message):
    r"""Request message for updating a source.

    Attributes:
        source (google.cloud.securitycenter_v1beta1.types.Source):
            Required. The source resource to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The FieldMask to use when updating the source
            resource.
    """

    source: gcs_source.Source = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcs_source.Source,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class UpdateSecurityMarksRequest(proto.Message):
    r"""Request message for updating a SecurityMarks resource.

    Attributes:
        security_marks (google.cloud.securitycenter_v1beta1.types.SecurityMarks):
            Required. The security marks resource to
            update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The FieldMask to use when updating the
            security marks resource.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            The time at which the updated SecurityMarks
            take effect.
    """

    security_marks: gcs_security_marks.SecurityMarks = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcs_security_marks.SecurityMarks,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
