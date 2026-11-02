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

from google.cloud.securitycenter_v1p1beta1.types import asset as gcs_asset
from google.cloud.securitycenter_v1p1beta1.types import finding as gcs_finding
from google.cloud.securitycenter_v1p1beta1.types import folder
from google.cloud.securitycenter_v1p1beta1.types import (
    notification_config as gcs_notification_config,
)
from google.cloud.securitycenter_v1p1beta1.types import (
    organization_settings as gcs_organization_settings,
)
from google.cloud.securitycenter_v1p1beta1.types import (
    security_marks as gcs_security_marks,
)
from google.cloud.securitycenter_v1p1beta1.types import source as gcs_source

__protobuf__ = proto.module(
    package="google.cloud.securitycenter.v1p1beta1",
    manifest={
        "CreateFindingRequest",
        "CreateNotificationConfigRequest",
        "CreateSourceRequest",
        "DeleteNotificationConfigRequest",
        "GetNotificationConfigRequest",
        "GetOrganizationSettingsRequest",
        "GetSourceRequest",
        "GroupAssetsRequest",
        "GroupAssetsResponse",
        "GroupFindingsRequest",
        "GroupFindingsResponse",
        "GroupResult",
        "ListNotificationConfigsRequest",
        "ListNotificationConfigsResponse",
        "ListSourcesRequest",
        "ListSourcesResponse",
        "ListAssetsRequest",
        "ListAssetsResponse",
        "ListFindingsRequest",
        "ListFindingsResponse",
        "SetFindingStateRequest",
        "RunAssetDiscoveryRequest",
        "UpdateFindingRequest",
        "UpdateNotificationConfigRequest",
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
            client within the parent scope.
        finding (google.cloud.securitycenter_v1p1beta1.types.Finding):
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


class CreateNotificationConfigRequest(proto.Message):
    r"""Request message for creating a notification config.

    Attributes:
        parent (str):
            Required. Resource name of the new notification config's
            parent. Its format is "organizations/[organization_id]".
        config_id (str):
            Required. Unique identifier provided by the
            client within the parent scope. It must be
            between 1 and 128 characters, and contains
            alphanumeric characters, underscores or hyphens
            only.
        notification_config (google.cloud.securitycenter_v1p1beta1.types.NotificationConfig):
            Required. The notification config being
            created. The name and the service account will
            be ignored as they are both output only fields
            on this resource.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    config_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    notification_config: gcs_notification_config.NotificationConfig = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcs_notification_config.NotificationConfig,
    )


class CreateSourceRequest(proto.Message):
    r"""Request message for creating a source.

    Attributes:
        parent (str):
            Required. Resource name of the new source's parent. Its
            format should be "organizations/[organization_id]".
        source (google.cloud.securitycenter_v1p1beta1.types.Source):
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


class DeleteNotificationConfigRequest(proto.Message):
    r"""Request message for deleting a notification config.

    Attributes:
        name (str):
            Required. Name of the notification config to delete. Its
            format is
            "organizations/[organization_id]/notificationConfigs/[config_id]".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetNotificationConfigRequest(proto.Message):
    r"""Request message for getting a notification config.

    Attributes:
        name (str):
            Required. Name of the notification config to get. Its format
            is
            "organizations/[organization_id]/notificationConfigs/[config_id]".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
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
            "organizations/[organization_id], folders/[folder_id], or
            projects/[project_id]".
        filter (str):
            Expression that defines the filter to apply across assets.
            The expression is a list of zero or more restrictions
            combined via logical operators ``AND`` and ``OR``.
            Parentheses are supported, and ``OR`` has higher precedence
            than ``AND``.

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

            The following field and operator combinations are supported:

            - name: ``=``

            - update_time: ``=``, ``>``, ``<``, ``>=``, ``<=``

              Usage: This should be milliseconds since epoch or an
              RFC3339 string. Examples:
              ``update_time = "2019-06-10T16:07:18-07:00"``
              ``update_time = 1560208038000``

            - create_time: ``=``, ``>``, ``<``, ``>=``, ``<=``

              Usage: This should be milliseconds since epoch or an
              RFC3339 string. Examples:
              ``create_time = "2019-06-10T16:07:18-07:00"``
              ``create_time = 1560208038000``

            - iam_policy.policy_blob: ``=``, ``:``

            - resource_properties: ``=``, ``:``, ``>``, ``<``, ``>=``,
              ``<=``

            - security_marks.marks: ``=``, ``:``

            - security_center_properties.resource_name: ``=``, ``:``

            - security_center_properties.resource_name_display_name:
              ``=``, ``:``

            - security_center_properties.resource_type: ``=``, ``:``

            - security_center_properties.resource_parent: ``=``, ``:``

            - security_center_properties.resource_parent_display_name:
              ``=``, ``:``

            - security_center_properties.resource_project: ``=``, ``:``

            - security_center_properties.resource_project_display_name:
              ``=``, ``:``

            - security_center_properties.resource_owners: ``=``, ``:``

            For example, ``resource_properties.size = 100`` is a valid
            filter string.

            Use a partial match on the empty string to filter based on a
            property existing: ``resource_properties.my_property : ""``

            Use a negated partial match on the empty string to filter
            based on a property not existing:
            ``-resource_properties.my_property : ""``
        group_by (str):
            Required. Expression that defines what assets fields to use
            for grouping. The string value should follow SQL syntax:
            comma separated list of fields. For example:
            "security_center_properties.resource_project,security_center_properties.project".

            The following fields are supported when compare_duration is
            not set:

            - security_center_properties.resource_project
            - security_center_properties.resource_project_display_name
            - security_center_properties.resource_type
            - security_center_properties.resource_parent
            - security_center_properties.resource_parent_display_name

            The following fields are supported when compare_duration is
            set:

            - security_center_properties.resource_type
            - security_center_properties.resource_project_display_name
            - security_center_properties.resource_parent_display_name
        compare_duration (google.protobuf.duration_pb2.Duration):
            When compare_duration is set, the GroupResult's
            "state_change" property is updated to indicate whether the
            asset was added, removed, or remained present during the
            compare_duration period of time that precedes the read_time.
            This is the time between (read_time - compare_duration) and
            read_time.

            The state change value is derived based on the presence of
            the asset at the two points in time. Intermediate state
            changes between the two times don't affect the result. For
            example, the results aren't affected if the asset is removed
            and re-created again.

            Possible "state_change" values when compare_duration is
            specified:

            - "ADDED": indicates that the asset was not present at the
              start of compare_duration, but present at reference_time.
            - "REMOVED": indicates that the asset was present at the
              start of compare_duration, but not present at
              reference_time.
            - "ACTIVE": indicates that the asset was present at both the
              start and the end of the time period defined by
              compare_duration and reference_time.

            If compare_duration is not specified, then the only possible
            state_change is "UNUSED", which will be the state_change set
            for all assets present at read_time.

            If this field is set then ``state_change`` must be a
            specified field in ``group_by``.
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
        group_by_results (MutableSequence[google.cloud.securitycenter_v1p1beta1.types.GroupResult]):
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
        total_size (int):
            The total number of results matching the
            query.
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
    total_size: int = proto.Field(
        proto.INT32,
        number=4,
    )


class GroupFindingsRequest(proto.Message):
    r"""Request message for grouping by findings.

    Attributes:
        parent (str):
            Required. Name of the source to groupBy. Its format is
            "organizations/[organization_id]/sources/[source_id]",
            folders/[folder_id]/sources/[source_id], or
            projects/[project_id]/sources/[source_id]. To groupBy across
            all sources provide a source_id of ``-``. For example:
            organizations/{organization_id}/sources/-,
            folders/{folder_id}/sources/-, or
            projects/{project_id}/sources/-
        filter (str):
            Expression that defines the filter to apply across findings.
            The expression is a list of one or more restrictions
            combined via logical operators ``AND`` and ``OR``.
            Parentheses are supported, and ``OR`` has higher precedence
            than ``AND``.

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

            The following field and operator combinations are supported:

            - name: ``=``

            - parent: ``=``, ``:``

            - resource_name: ``=``, ``:``

            - state: ``=``, ``:``

            - category: ``=``, ``:``

            - external_uri: ``=``, ``:``

            - event_time: ``=``, ``>``, ``<``, ``>=``, ``<=``

            - severity: ``=``, ``:``

              Usage: This should be milliseconds since epoch or an
              RFC3339 string. Examples:
              ``event_time = "2019-06-10T16:07:18-07:00"``
              ``event_time = 1560208038000``

            - security_marks.marks: ``=``, ``:``

            - source_properties: ``=``, ``:``, ``>``, ``<``, ``>=``,
              ``<=``

            For example, ``source_properties.size = 100`` is a valid
            filter string.

            Use a partial match on the empty string to filter based on a
            property existing: ``source_properties.my_property : ""``

            Use a negated partial match on the empty string to filter
            based on a property not existing:
            ``-source_properties.my_property : ""``
        group_by (str):
            Required. Expression that defines what assets fields to use
            for grouping (including ``state_change``). The string value
            should follow SQL syntax: comma separated list of fields.
            For example: "parent,resource_name".

            The following fields are supported:

            - resource_name
            - category
            - state
            - parent
            - severity

            The following fields are supported when compare_duration is
            set:

            - state_change
        read_time (google.protobuf.timestamp_pb2.Timestamp):
            Time used as a reference point when filtering
            findings. The filter is limited to findings
            existing at the supplied time and their values
            are those at that specific time. Absence of this
            field will default to the API's version of NOW.
        compare_duration (google.protobuf.duration_pb2.Duration):
            When compare_duration is set, the GroupResult's
            "state_change" attribute is updated to indicate whether the
            finding had its state changed, the finding's state remained
            unchanged, or if the finding was added during the
            compare_duration period of time that precedes the read_time.
            This is the time between (read_time - compare_duration) and
            read_time.

            The state_change value is derived based on the presence and
            state of the finding at the two points in time. Intermediate
            state changes between the two times don't affect the result.
            For example, the results aren't affected if the finding is
            made inactive and then active again.

            Possible "state_change" values when compare_duration is
            specified:

            - "CHANGED": indicates that the finding was present and
              matched the given filter at the start of compare_duration,
              but changed its state at read_time.
            - "UNCHANGED": indicates that the finding was present and
              matched the given filter at the start of compare_duration
              and did not change state at read_time.
            - "ADDED": indicates that the finding did not match the
              given filter or was not present at the start of
              compare_duration, but was present at read_time.
            - "REMOVED": indicates that the finding was present and
              matched the filter at the start of compare_duration, but
              did not match the filter at read_time.

            If compare_duration is not specified, then the only possible
            state_change is "UNUSED", which will be the state_change set
            for all findings present at read_time.

            If this field is set then ``state_change`` must be a
            specified field in ``group_by``.
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
    compare_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=5,
        message=duration_pb2.Duration,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=7,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=8,
    )


class GroupFindingsResponse(proto.Message):
    r"""Response message for group by findings.

    Attributes:
        group_by_results (MutableSequence[google.cloud.securitycenter_v1p1beta1.types.GroupResult]):
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
        total_size (int):
            The total number of results matching the
            query.
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
    total_size: int = proto.Field(
        proto.INT32,
        number=4,
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


class ListNotificationConfigsRequest(proto.Message):
    r"""Request message for listing notification configs.

    Attributes:
        parent (str):
            Required. Name of the organization to list notification
            configs. Its format is "organizations/[organization_id]".
        page_token (str):
            The value returned by the last
            ``ListNotificationConfigsResponse``; indicates that this is
            a continuation of a prior ``ListNotificationConfigs`` call,
            and that the system should return the next page of data.
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
        number=3,
    )


class ListNotificationConfigsResponse(proto.Message):
    r"""Response message for listing notification configs.

    Attributes:
        notification_configs (MutableSequence[google.cloud.securitycenter_v1p1beta1.types.NotificationConfig]):
            Notification configs belonging to the
            requested parent.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results.
    """

    @property
    def raw_page(self):
        return self

    notification_configs: MutableSequence[
        gcs_notification_config.NotificationConfig
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcs_notification_config.NotificationConfig,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListSourcesRequest(proto.Message):
    r"""Request message for listing sources.

    Attributes:
        parent (str):
            Required. Resource name of the parent of sources to list.
            Its format should be "organizations/[organization_id],
            folders/[folder_id], or projects/[project_id]".
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
        sources (MutableSequence[google.cloud.securitycenter_v1p1beta1.types.Source]):
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
            Its format is "organizations/[organization_id],
            folders/[folder_id], or projects/[project_id]".
        filter (str):
            Expression that defines the filter to apply across assets.
            The expression is a list of zero or more restrictions
            combined via logical operators ``AND`` and ``OR``.
            Parentheses are supported, and ``OR`` has higher precedence
            than ``AND``.

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

            The following are the allowed field and operator
            combinations:

            - name: ``=``

            - update_time: ``=``, ``>``, ``<``, ``>=``, ``<=``

              Usage: This should be milliseconds since epoch or an
              RFC3339 string. Examples:
              ``update_time = "2019-06-10T16:07:18-07:00"``
              ``update_time = 1560208038000``

            - create_time: ``=``, ``>``, ``<``, ``>=``, ``<=``

              Usage: This should be milliseconds since epoch or an
              RFC3339 string. Examples:
              ``create_time = "2019-06-10T16:07:18-07:00"``
              ``create_time = 1560208038000``

            - iam_policy.policy_blob: ``=``, ``:``

            - resource_properties: ``=``, ``:``, ``>``, ``<``, ``>=``,
              ``<=``

            - security_marks.marks: ``=``, ``:``

            - security_center_properties.resource_name: ``=``, ``:``

            - security_center_properties.resource_display_name: ``=``,
              ``:``

            - security_center_properties.resource_type: ``=``, ``:``

            - security_center_properties.resource_parent: ``=``, ``:``

            - security_center_properties.resource_parent_display_name:
              ``=``, ``:``

            - security_center_properties.resource_project: ``=``, ``:``

            - security_center_properties.resource_project_display_name:
              ``=``, ``:``

            - security_center_properties.resource_owners: ``=``, ``:``

            For example, ``resource_properties.size = 100`` is a valid
            filter string.

            Use a partial match on the empty string to filter based on a
            property existing: ``resource_properties.my_property : ""``

            Use a negated partial match on the empty string to filter
            based on a property not existing:
            ``-resource_properties.my_property : ""``
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

            The following fields are supported: name update_time
            resource_properties security_marks.marks
            security_center_properties.resource_name
            security_center_properties.resource_display_name
            security_center_properties.resource_parent
            security_center_properties.resource_parent_display_name
            security_center_properties.resource_project
            security_center_properties.resource_project_display_name
            security_center_properties.resource_type
        read_time (google.protobuf.timestamp_pb2.Timestamp):
            Time used as a reference point when filtering
            assets. The filter is limited to assets existing
            at the supplied time and their values are those
            at that specific time. Absence of this field
            will default to the API's version of NOW.
        compare_duration (google.protobuf.duration_pb2.Duration):
            When compare_duration is set, the ListAssetsResult's
            "state_change" attribute is updated to indicate whether the
            asset was added, removed, or remained present during the
            compare_duration period of time that precedes the read_time.
            This is the time between (read_time - compare_duration) and
            read_time.

            The state_change value is derived based on the presence of
            the asset at the two points in time. Intermediate state
            changes between the two times don't affect the result. For
            example, the results aren't affected if the asset is removed
            and re-created again.

            Possible "state_change" values when compare_duration is
            specified:

            - "ADDED": indicates that the asset was not present at the
              start of compare_duration, but present at read_time.
            - "REMOVED": indicates that the asset was present at the
              start of compare_duration, but not present at read_time.
            - "ACTIVE": indicates that the asset was present at both the
              start and the end of the time period defined by
              compare_duration and read_time.

            If compare_duration is not specified, then the only possible
            state_change is "UNUSED", which will be the state_change set
            for all assets present at read_time.
        field_mask (google.protobuf.field_mask_pb2.FieldMask):
            A field mask to specify the ListAssetsResult
            fields to be listed in the response.
            An empty field mask will list all fields.
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
        list_assets_results (MutableSequence[google.cloud.securitycenter_v1p1beta1.types.ListAssetsResponse.ListAssetsResult]):
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
            asset (google.cloud.securitycenter_v1p1beta1.types.Asset):
                Asset matching the search request.
            state_change (google.cloud.securitycenter_v1p1beta1.types.ListAssetsResponse.ListAssetsResult.StateChange):
                State change of the asset between the points
                in time.
        """

        class StateChange(proto.Enum):
            r"""The change in state of the asset.

            When querying across two points in time this describes the change
            between the two points: ADDED, REMOVED, or ACTIVE. If there was no
            compare_duration supplied in the request the state change will be:
            UNUSED

            Values:
                UNUSED (0):
                    State change is unused, this is the canonical
                    default for this enum.
                ADDED (1):
                    Asset was added between the points in time.
                REMOVED (2):
                    Asset was removed between the points in time.
                ACTIVE (3):
                    Asset was present at both point(s) in time.
            """

            UNUSED = 0
            ADDED = 1
            REMOVED = 2
            ACTIVE = 3

        asset: gcs_asset.Asset = proto.Field(
            proto.MESSAGE,
            number=1,
            message=gcs_asset.Asset,
        )
        state_change: "ListAssetsResponse.ListAssetsResult.StateChange" = proto.Field(
            proto.ENUM,
            number=2,
            enum="ListAssetsResponse.ListAssetsResult.StateChange",
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
            "organizations/[organization_id]/sources/[source_id],
            folders/[folder_id]/sources/[source_id], or
            projects/[project_id]/sources/[source_id]". To list across
            all sources provide a source_id of ``-``. For example:
            organizations/{organization_id}/sources/-,
            folders/{folder_id}/sources/- or
            projects/{projects_id}/sources/-
        filter (str):
            Expression that defines the filter to apply across findings.
            The expression is a list of one or more restrictions
            combined via logical operators ``AND`` and ``OR``.
            Parentheses are supported, and ``OR`` has higher precedence
            than ``AND``.

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

            The following field and operator combinations are supported:

            - name: ``=``

            - parent: ``=``, ``:``

            - resource_name: ``=``, ``:``

            - state: ``=``, ``:``

            - category: ``=``, ``:``

            - external_uri: ``=``, ``:``

            - event_time: ``=``, ``>``, ``<``, ``>=``, ``<=``

            - severity: ``=``, ``:``

              Usage: This should be milliseconds since epoch or an
              RFC3339 string. Examples:
              ``event_time = "2019-06-10T16:07:18-07:00"``
              ``event_time = 1560208038000``

            security_marks.marks: ``=``, ``:`` source_properties: ``=``,
            ``:``, ``>``, ``<``, ``>=``, ``<=``

            For example, ``source_properties.size = 100`` is a valid
            filter string.

            Use a partial match on the empty string to filter based on a
            property existing: ``source_properties.my_property : ""``

            Use a negated partial match on the empty string to filter
            based on a property not existing:
            ``-source_properties.my_property : ""``
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

            The following fields are supported: name parent state
            category resource_name event_time source_properties
            security_marks.marks
        read_time (google.protobuf.timestamp_pb2.Timestamp):
            Time used as a reference point when filtering
            findings. The filter is limited to findings
            existing at the supplied time and their values
            are those at that specific time. Absence of this
            field will default to the API's version of NOW.
        compare_duration (google.protobuf.duration_pb2.Duration):
            When compare_duration is set, the ListFindingsResult's
            "state_change" attribute is updated to indicate whether the
            finding had its state changed, the finding's state remained
            unchanged, or if the finding was added in any state during
            the compare_duration period of time that precedes the
            read_time. This is the time between (read_time -
            compare_duration) and read_time.

            The state_change value is derived based on the presence and
            state of the finding at the two points in time. Intermediate
            state changes between the two times don't affect the result.
            For example, the results aren't affected if the finding is
            made inactive and then active again.

            Possible "state_change" values when compare_duration is
            specified:

            - "CHANGED": indicates that the finding was present and
              matched the given filter at the start of compare_duration,
              but changed its state at read_time.
            - "UNCHANGED": indicates that the finding was present and
              matched the given filter at the start of compare_duration
              and did not change state at read_time.
            - "ADDED": indicates that the finding did not match the
              given filter or was not present at the start of
              compare_duration, but was present at read_time.
            - "REMOVED": indicates that the finding was present and
              matched the filter at the start of compare_duration, but
              did not match the filter at read_time.

            If compare_duration is not specified, then the only possible
            state_change is "UNUSED", which will be the state_change set
            for all findings present at read_time.
        field_mask (google.protobuf.field_mask_pb2.FieldMask):
            A field mask to specify the Finding fields to
            be listed in the response. An empty field mask
            will list all fields.
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


class ListFindingsResponse(proto.Message):
    r"""Response message for listing findings.

    Attributes:
        list_findings_results (MutableSequence[google.cloud.securitycenter_v1p1beta1.types.ListFindingsResponse.ListFindingsResult]):
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

    class ListFindingsResult(proto.Message):
        r"""Result containing the Finding and its StateChange.

        Attributes:
            finding (google.cloud.securitycenter_v1p1beta1.types.Finding):
                Finding matching the search request.
            state_change (google.cloud.securitycenter_v1p1beta1.types.ListFindingsResponse.ListFindingsResult.StateChange):
                State change of the finding between the
                points in time.
            resource (google.cloud.securitycenter_v1p1beta1.types.ListFindingsResponse.ListFindingsResult.Resource):
                Output only. Resource that is associated with
                this finding.
        """

        class StateChange(proto.Enum):
            r"""The change in state of the finding.

            When querying across two points in time this describes the change in
            the finding between the two points: CHANGED, UNCHANGED, ADDED, or
            REMOVED. Findings can not be deleted, so REMOVED implies that the
            finding at timestamp does not match the filter specified, but it did
            at timestamp - compare_duration. If there was no compare_duration
            supplied in the request the state change will be: UNUSED

            Values:
                UNUSED (0):
                    State change is unused, this is the canonical
                    default for this enum.
                CHANGED (1):
                    The finding has changed state in some way
                    between the points in time and existed at both
                    points.
                UNCHANGED (2):
                    The finding has not changed state between the
                    points in time and existed at both points.
                ADDED (3):
                    The finding was created between the points in
                    time.
                REMOVED (4):
                    The finding at timestamp does not match the filter
                    specified, but it did at timestamp - compare_duration.
            """

            UNUSED = 0
            CHANGED = 1
            UNCHANGED = 2
            ADDED = 3
            REMOVED = 4

        class Resource(proto.Message):
            r"""Information related to the Google Cloud resource that is
            associated with this finding.

            Attributes:
                name (str):
                    The full resource name of the resource. See:
                    https://cloud.google.com/apis/design/resource_names#full_resource_name
                project_name (str):
                    The full resource name of project that the
                    resource belongs to.
                project_display_name (str):
                    The human readable name of project that the
                    resource belongs to.
                parent_name (str):
                    The full resource name of resource's parent.
                parent_display_name (str):
                    The human readable name of resource's parent.
                folders (MutableSequence[google.cloud.securitycenter_v1p1beta1.types.Folder]):
                    Contains a Folder message for each folder in
                    the assets ancestry. The first folder is the
                    deepest nested folder, and the last folder is
                    the folder directly under the Organization.
            """

            name: str = proto.Field(
                proto.STRING,
                number=1,
            )
            project_name: str = proto.Field(
                proto.STRING,
                number=2,
            )
            project_display_name: str = proto.Field(
                proto.STRING,
                number=3,
            )
            parent_name: str = proto.Field(
                proto.STRING,
                number=4,
            )
            parent_display_name: str = proto.Field(
                proto.STRING,
                number=5,
            )
            folders: MutableSequence[folder.Folder] = proto.RepeatedField(
                proto.MESSAGE,
                number=10,
                message=folder.Folder,
            )

        finding: gcs_finding.Finding = proto.Field(
            proto.MESSAGE,
            number=1,
            message=gcs_finding.Finding,
        )
        state_change: "ListFindingsResponse.ListFindingsResult.StateChange" = (
            proto.Field(
                proto.ENUM,
                number=2,
                enum="ListFindingsResponse.ListFindingsResult.StateChange",
            )
        )
        resource: "ListFindingsResponse.ListFindingsResult.Resource" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="ListFindingsResponse.ListFindingsResult.Resource",
        )

    @property
    def raw_page(self):
        return self

    list_findings_results: MutableSequence[ListFindingsResult] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=ListFindingsResult,
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
        state (google.cloud.securitycenter_v1p1beta1.types.Finding.State):
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
        finding (google.cloud.securitycenter_v1p1beta1.types.Finding):
            Required. The finding resource to update or create if it
            does not already exist. parent, security_marks, and
            update_time will be ignored.

            In the case of creation, the finding id portion of the name
            must be alphanumeric and less than or equal to 32 characters
            and greater than 0 characters in length.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The FieldMask to use when updating the finding resource.
            This field should not be specified when creating a finding.

            When updating a finding, an empty mask is treated as
            updating all mutable fields and replacing source_properties.
            Individual source_properties can be added/updated by using
            "source_properties." in the field mask.
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


class UpdateNotificationConfigRequest(proto.Message):
    r"""Request message for updating a notification config.

    Attributes:
        notification_config (google.cloud.securitycenter_v1p1beta1.types.NotificationConfig):
            Required. The notification config to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The FieldMask to use when updating the
            notification config.
            If empty all mutable fields will be updated.
    """

    notification_config: gcs_notification_config.NotificationConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcs_notification_config.NotificationConfig,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class UpdateOrganizationSettingsRequest(proto.Message):
    r"""Request message for updating an organization's settings.

    Attributes:
        organization_settings (google.cloud.securitycenter_v1p1beta1.types.OrganizationSettings):
            Required. The organization settings resource
            to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The FieldMask to use when updating the
            settings resource.
            If empty all mutable fields will be updated.
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
        source (google.cloud.securitycenter_v1p1beta1.types.Source):
            Required. The source resource to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The FieldMask to use when updating the source
            resource.
            If empty all mutable fields will be updated.
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
        security_marks (google.cloud.securitycenter_v1p1beta1.types.SecurityMarks):
            Required. The security marks resource to
            update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The FieldMask to use when updating the security marks
            resource.

            The field mask must not contain duplicate fields. If empty
            or set to "marks", all marks will be replaced. Individual
            marks can be updated using "marks.<mark_key>".
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            The time at which the updated SecurityMarks
            take effect. If not set uses current server
            time.  Updates will be applied to the
            SecurityMarks that are active immediately
            preceding this time.
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
