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
import google.protobuf.wrappers_pb2 as wrappers_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.api.cloudquotas.v1",
    manifest={
        "QuotaSafetyCheck",
        "QuotaInfo",
        "QuotaIncreaseEligibility",
        "QuotaPreference",
        "QuotaConfig",
        "DimensionsInfo",
        "QuotaDetails",
        "RolloutInfo",
    },
)


class QuotaSafetyCheck(proto.Enum):
    r"""Enumerations of quota safety checks.

    Values:
        QUOTA_SAFETY_CHECK_UNSPECIFIED (0):
            Unspecified quota safety check.
        QUOTA_DECREASE_BELOW_USAGE (1):
            Validates that a quota mutation would not
            cause the consumer's effective limit to be lower
            than the consumer's quota usage.
        QUOTA_DECREASE_PERCENTAGE_TOO_HIGH (2):
            Validates that a quota mutation would not
            cause the consumer's effective limit to decrease
            by more than 10 percent.
    """

    QUOTA_SAFETY_CHECK_UNSPECIFIED = 0
    QUOTA_DECREASE_BELOW_USAGE = 1
    QUOTA_DECREASE_PERCENTAGE_TOO_HIGH = 2


class QuotaInfo(proto.Message):
    r"""QuotaInfo represents information about a particular quota for
    a given project, folder or organization.

    Attributes:
        name (str):
            Resource name of this QuotaInfo. The ID component following
            "locations/" must be "global". For example,
            ``projects/123/locations/global/services/compute.googleapis.com/quotaInfos/CpusPerProjectPerRegion``
        quota_id (str):
            The id of the quota, which is unique within the service. For
            example, ``CpusPerProjectPerRegion``
        metric (str):
            The metric of the quota. It specifies the resources
            consumption the quota is defined for. For example,
            ``compute.googleapis.com/cpus``
        service (str):
            The name of the service in which the quota is defined. For
            example, ``compute.googleapis.com``
        is_precise (bool):
            Whether this is a precise quota. A precise
            quota is tracked with absolute precision. In
            contrast, an imprecise quota is not tracked with
            precision.
        refresh_interval (str):
            The reset time interval for the quota.
            Refresh interval applies to rate quota only.
            For example, "minute" for per minute, "day" for
            per day, or "10 seconds" for every 10 seconds.
        container_type (google.cloud.cloudquotas_v1.types.QuotaInfo.ContainerType):
            The container type of the QuotaInfo.
        dimensions (MutableSequence[str]):
            The dimensions the quota is defined on.
        metric_display_name (str):
            The display name of the quota metric
        quota_display_name (str):
            The display name of the quota.
        metric_unit (str):
            The unit in which the metric value is
            reported, e.g., "MByte".
        quota_increase_eligibility (google.cloud.cloudquotas_v1.types.QuotaIncreaseEligibility):
            Whether it is eligible to request a higher
            quota value for this quota.
        is_fixed (bool):
            Whether the quota value is fixed or
            adjustable
        dimensions_infos (MutableSequence[google.cloud.cloudquotas_v1.types.DimensionsInfo]):
            The collection of dimensions info ordered by
            their dimensions from more specific ones to less
            specific ones.
        is_concurrent (bool):
            Whether the quota is a concurrent quota.
            Concurrent quotas are enforced on the total
            number of concurrent operations in flight at any
            given time.
        service_request_quota_uri (str):
            URI to the page where users can request more
            quota for the cloud service—for example,
            https://console.cloud.google.com/iam-admin/quotas.
    """

    class ContainerType(proto.Enum):
        r"""The enumeration of the types of a cloud resource container.

        Values:
            CONTAINER_TYPE_UNSPECIFIED (0):
                Unspecified container type.
            PROJECT (1):
                consumer project
            FOLDER (2):
                folder
            ORGANIZATION (3):
                organization
        """

        CONTAINER_TYPE_UNSPECIFIED = 0
        PROJECT = 1
        FOLDER = 2
        ORGANIZATION = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    quota_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    metric: str = proto.Field(
        proto.STRING,
        number=3,
    )
    service: str = proto.Field(
        proto.STRING,
        number=4,
    )
    is_precise: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    refresh_interval: str = proto.Field(
        proto.STRING,
        number=6,
    )
    container_type: ContainerType = proto.Field(
        proto.ENUM,
        number=7,
        enum=ContainerType,
    )
    dimensions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    metric_display_name: str = proto.Field(
        proto.STRING,
        number=9,
    )
    quota_display_name: str = proto.Field(
        proto.STRING,
        number=10,
    )
    metric_unit: str = proto.Field(
        proto.STRING,
        number=11,
    )
    quota_increase_eligibility: "QuotaIncreaseEligibility" = proto.Field(
        proto.MESSAGE,
        number=12,
        message="QuotaIncreaseEligibility",
    )
    is_fixed: bool = proto.Field(
        proto.BOOL,
        number=13,
    )
    dimensions_infos: MutableSequence["DimensionsInfo"] = proto.RepeatedField(
        proto.MESSAGE,
        number=14,
        message="DimensionsInfo",
    )
    is_concurrent: bool = proto.Field(
        proto.BOOL,
        number=15,
    )
    service_request_quota_uri: str = proto.Field(
        proto.STRING,
        number=17,
    )


class QuotaIncreaseEligibility(proto.Message):
    r"""Eligibility information regarding requesting increase
    adjustment of a quota.

    Attributes:
        is_eligible (bool):
            Whether a higher quota value can be requested
            for the quota.
        ineligibility_reason (google.cloud.cloudquotas_v1.types.QuotaIncreaseEligibility.IneligibilityReason):
            The reason of why it is ineligible to request increased
            value of the quota. If the is_eligible field is true, it
            defaults to INELIGIBILITY_REASON_UNSPECIFIED.
    """

    class IneligibilityReason(proto.Enum):
        r"""The enumeration of reasons when it is ineligible to request
        increase adjustment.

        Values:
            INELIGIBILITY_REASON_UNSPECIFIED (0):
                Default value when is_eligible is true.
            NO_VALID_BILLING_ACCOUNT (1):
                The container is not linked with a valid
                billing account.
            NOT_SUPPORTED (3):
                Quota increase is not supported for the
                quota.
            NOT_ENOUGH_USAGE_HISTORY (4):
                There is not enough usage history to
                determine the eligibility.
            OTHER (2):
                Other reasons.
        """

        INELIGIBILITY_REASON_UNSPECIFIED = 0
        NO_VALID_BILLING_ACCOUNT = 1
        NOT_SUPPORTED = 3
        NOT_ENOUGH_USAGE_HISTORY = 4
        OTHER = 2

    is_eligible: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    ineligibility_reason: IneligibilityReason = proto.Field(
        proto.ENUM,
        number=2,
        enum=IneligibilityReason,
    )


class QuotaPreference(proto.Message):
    r"""QuotaPreference represents the preferred quota configuration
    specified for a project, folder or organization. There is only
    one QuotaPreference resource for a quota value targeting a
    unique set of dimensions.

    Attributes:
        name (str):
            Required except in the CREATE requests. The resource name of
            the quota preference. The path that follows ``/locations``
            must be ``/global``. For example:
            ``projects/123/locations/global/quotaPreferences/my-config-for-us-east1``
        dimensions (MutableMapping[str, str]):
            Immutable. The dimensions that this quota preference applies
            to. The key of the map entry is the name of a dimension,
            such as ``region``, ``zone``, ``network_id``, and the value
            of the map entry is the dimension value.

            If a dimension is missing from the map of dimensions, the
            quota preference applies to all the dimension values except
            for those that have other quota preferences configured for
            the specific value.

            Note: QuotaPreferences can only be applied across all values
            of ``user`` and ``resource`` dimension. Do not set values
            for ``user`` or ``resource`` in the dimension map.

            For example: ``{"provider" : "Example Organization"}`` where
            ``provider`` is a service-specific quota dimension and
            ``Example Organization`` is the provider name.
        quota_config (google.cloud.cloudquotas_v1.types.QuotaConfig):
            Required. Preferred quota configuration.
        etag (str):
            Optional. The current etag of the quota
            preference. If an etag is provided on update and
            does not match the current server's etag of the
            quota preference, the request will be blocked
            and an ABORTED error will be returned. See
            https://google.aip.dev/134#etags for more
            details on etags.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create time stamp
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Update time stamp
        service (str):
            Required. The name of the service to which
            the quota preference is applied.
        quota_id (str):
            Required. The id of the quota to which the quota preference
            is applied. A quota name is unique in the service. For
            example, ``CpusPerProjectPerRegion``
        reconciling (bool):
            Output only. Is the quota preference pending
            Google Cloud approval and fulfillment.
        justification (str):
            The reason / justification for this quota
            preference.
        contact_email (str):
            Input only. An email address that can be used to contact the
            user, in case Google Cloud needs more information to make a
            decision before additional quota can be granted.

            When requesting a quota increase, the email address is
            required. When requesting a quota decrease, the email
            address is optional. For example, the email address is
            optional when the ``QuotaConfig.preferred_value`` is smaller
            than the ``QuotaDetails.reset_value``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    dimensions: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )
    quota_config: "QuotaConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="QuotaConfig",
    )
    etag: str = proto.Field(
        proto.STRING,
        number=4,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    service: str = proto.Field(
        proto.STRING,
        number=7,
    )
    quota_id: str = proto.Field(
        proto.STRING,
        number=8,
    )
    reconciling: bool = proto.Field(
        proto.BOOL,
        number=10,
    )
    justification: str = proto.Field(
        proto.STRING,
        number=11,
    )
    contact_email: str = proto.Field(
        proto.STRING,
        number=12,
    )


class QuotaConfig(proto.Message):
    r"""The preferred quota configuration.

    Attributes:
        preferred_value (int):
            Required. The preferred value. Must be
            greater than or equal to -1. If set to -1, it
            means the value is "unlimited".
        state_detail (str):
            Output only. Optional details about the state
            of this quota preference.
        granted_value (google.protobuf.wrappers_pb2.Int64Value):
            Output only. Granted quota value.
        trace_id (str):
            Output only. The trace id that the Google
            Cloud uses to provision the requested quota.
            This trace id may be used by the client to
            contact Cloud support to track the state of a
            quota preference request. The trace id is only
            produced for increase requests and is unique for
            each request. The quota decrease requests do not
            have a trace id.
        annotations (MutableMapping[str, str]):
            Optional. The annotations map for clients to
            store small amounts of arbitrary data. Do not
            put PII or other sensitive information here. See
            https://google.aip.dev/128#annotations
        request_origin (google.cloud.cloudquotas_v1.types.QuotaConfig.Origin):
            Output only. The origin of the quota
            preference request.
    """

    class Origin(proto.Enum):
        r"""The enumeration of the origins of quota preference requests.

        Values:
            ORIGIN_UNSPECIFIED (0):
                The unspecified value.
            CLOUD_CONSOLE (1):
                Created through Cloud Console.
            AUTO_ADJUSTER (2):
                Generated by automatic quota adjustment.
        """

        ORIGIN_UNSPECIFIED = 0
        CLOUD_CONSOLE = 1
        AUTO_ADJUSTER = 2

    preferred_value: int = proto.Field(
        proto.INT64,
        number=1,
    )
    state_detail: str = proto.Field(
        proto.STRING,
        number=2,
    )
    granted_value: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=3,
        message=wrappers_pb2.Int64Value,
    )
    trace_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    request_origin: Origin = proto.Field(
        proto.ENUM,
        number=6,
        enum=Origin,
    )


class DimensionsInfo(proto.Message):
    r"""The detailed quota information such as effective quota value
    for a combination of dimensions.

    Attributes:
        dimensions (MutableMapping[str, str]):
            The map of dimensions in key-value pairs. The key of a map
            entry is "region", "zone", or the name of a service-specific
            dimension, and the value of a map entry is the value of the
            dimension. If a dimension does not appear in the map of
            dimensions, the dimensions info applies to all the dimension
            values except for those that have another DimensionInfo
            instance configured for the specific value. For example:
            ``{"provider" : "Example Organization"}`` where ``provider``
            is a service-specific quota dimension and
            ``Example Organization`` is the provider name.
        details (google.cloud.cloudquotas_v1.types.QuotaDetails):
            Quota details for the specified dimensions.
        applicable_locations (MutableSequence[str]):
            The applicable regions or zones of this dimension. The field
            is set to ['global'] for quotas that are not per region or
            per zone. Otherwise, it will be set to the list of locations
            this dimension info is applicable to.
    """

    dimensions: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=1,
    )
    details: "QuotaDetails" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="QuotaDetails",
    )
    applicable_locations: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class QuotaDetails(proto.Message):
    r"""The quota details for a map of dimensions.

    Attributes:
        value (int):
            The value currently in effect and being
            enforced.
        rollout_info (google.cloud.cloudquotas_v1.types.RolloutInfo):
            Rollout information of this quota.
            This field is present only if the effective
            limit will change due to the ongoing rollout of
            the service config.
    """

    value: int = proto.Field(
        proto.INT64,
        number=1,
    )
    rollout_info: "RolloutInfo" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="RolloutInfo",
    )


class RolloutInfo(proto.Message):
    r"""[Output only] Rollout information of a quota.

    Attributes:
        ongoing_rollout (bool):
            Whether there is an ongoing rollout for a
            quota or not.
    """

    ongoing_rollout: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
