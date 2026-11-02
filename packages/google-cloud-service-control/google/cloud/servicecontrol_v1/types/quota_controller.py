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

import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.servicecontrol_v1.types import metric_value

__protobuf__ = proto.module(
    package="google.api.servicecontrol.v1",
    manifest={
        "AllocateQuotaRequest",
        "QuotaOperation",
        "AllocateQuotaResponse",
        "QuotaError",
    },
)


class AllocateQuotaRequest(proto.Message):
    r"""Request message for the AllocateQuota method.

    Attributes:
        service_name (str):
            Name of the service as specified in the service
            configuration. For example, ``"pubsub.googleapis.com"``.

            See [google.api.Service][google.api.Service] for the
            definition of a service name.
        allocate_operation (google.cloud.servicecontrol_v1.types.QuotaOperation):
            Operation that describes the quota
            allocation.
        service_config_id (str):
            Specifies which version of service
            configuration should be used to process the
            request. If unspecified or no matching version
            can be found, the latest one will be used.
    """

    service_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    allocate_operation: "QuotaOperation" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="QuotaOperation",
    )
    service_config_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class QuotaOperation(proto.Message):
    r"""Represents information regarding a quota operation.

    Attributes:
        operation_id (str):
            Identity of the operation. For Allocation Quota, this is
            expected to be unique within the scope of the service that
            generated the operation, and guarantees idempotency in case
            of retries.

            In order to ensure best performance and latency in the Quota
            backends, operation_ids are optimally associated with time,
            so that related operations can be accessed fast in storage.
            For this reason, the recommended token for services that
            intend to operate at a high QPS is Unix time in nanos + UUID
        method_name (str):
            Fully qualified name of the API method for which this quota
            operation is requested. This name is used for matching quota
            rules or metric rules and billing status rules defined in
            service configuration.

            This field should not be set if any of the following is
            true: (1) the quota operation is performed on non-API
            resources. (2) quota_metrics is set because the caller is
            doing quota override.

            Example of an RPC method name:
            google.example.library.v1.LibraryService.CreateShelf
        consumer_id (str):
            Identity of the consumer for whom this quota operation is
            being performed.

            This can be in one of the following formats:
            project:<project_id>, project_number:<project_number>,
            api_key:<api_key>.
        labels (MutableMapping[str, str]):
            Labels describing the operation.
        quota_metrics (MutableSequence[google.cloud.servicecontrol_v1.types.MetricValueSet]):
            Represents information about this operation. Each
            MetricValueSet corresponds to a metric defined in the
            service configuration. The data type used in the
            MetricValueSet must agree with the data type specified in
            the metric definition.

            Within a single operation, it is not allowed to have more
            than one MetricValue instances that have the same metric
            names and identical label value combinations. If a request
            has such duplicated MetricValue instances, the entire
            request is rejected with an invalid argument error.

            This field is mutually exclusive with method_name.
        quota_mode (google.cloud.servicecontrol_v1.types.QuotaOperation.QuotaMode):
            Quota mode for this operation.
    """

    class QuotaMode(proto.Enum):
        r"""Supported quota modes.

        Values:
            UNSPECIFIED (0):
                Guard against implicit default. Must not be
                used.
            NORMAL (1):
                For AllocateQuota request, allocates quota
                for the amount specified in the service
                configuration or specified using the quota
                metrics. If the amount is higher than the
                available quota, allocation error will be
                returned and no quota will be allocated.
                If multiple quotas are part of the request, and
                one fails, none of the quotas are allocated or
                released.
            BEST_EFFORT (2):
                The operation allocates quota for the amount specified in
                the service configuration or specified using the quota
                metrics. If the amount is higher than the available quota,
                request does not fail but all available quota will be
                allocated. For rate quota, BEST_EFFORT will continue to
                deduct from other groups even if one does not have enough
                quota. For allocation, it will find the minimum available
                amount across all groups and deduct that amount from all the
                affected groups.
            CHECK_ONLY (3):
                For AllocateQuota request, only checks if
                there is enough quota available and does not
                change the available quota. No lock is placed on
                the available quota either.
            QUERY_ONLY (4):
                Unimplemented. When used in
                AllocateQuotaRequest, this returns the effective
                quota limit(s) in the response, and no quota
                check will be performed. Not supported for other
                requests, and even for AllocateQuotaRequest,
                this is currently supported only for allowlisted
                services.
            ADJUST_ONLY (5):
                The operation allocates quota for the amount
                specified in the service configuration or
                specified using the quota metrics. If the
                requested amount is higher than the available
                quota, request does not fail and remaining quota
                would become negative (going over the limit).
                Not supported for Rate Quota.
        """

        UNSPECIFIED = 0
        NORMAL = 1
        BEST_EFFORT = 2
        CHECK_ONLY = 3
        QUERY_ONLY = 4
        ADJUST_ONLY = 5

    operation_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    method_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    consumer_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    quota_metrics: MutableSequence[metric_value.MetricValueSet] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=metric_value.MetricValueSet,
    )
    quota_mode: QuotaMode = proto.Field(
        proto.ENUM,
        number=6,
        enum=QuotaMode,
    )


class AllocateQuotaResponse(proto.Message):
    r"""Response message for the AllocateQuota method.

    Attributes:
        operation_id (str):
            The same operation_id value used in the
            AllocateQuotaRequest. Used for logging and diagnostics
            purposes.
        allocate_errors (MutableSequence[google.cloud.servicecontrol_v1.types.QuotaError]):
            Indicates the decision of the allocate.
        quota_metrics (MutableSequence[google.cloud.servicecontrol_v1.types.MetricValueSet]):
            Quota metrics to indicate the result of allocation.
            Depending on the request, one or more of the following
            metrics will be included:

            1. Per quota group or per quota metric incremental usage
               will be specified using the following delta metric :
               "serviceruntime.googleapis.com/api/consumer/quota_used_count"

            2. The quota limit reached condition will be specified using
               the following boolean metric :
               "serviceruntime.googleapis.com/quota/exceeded".
        service_config_id (str):
            ID of the actual config used to process the
            request.
    """

    operation_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    allocate_errors: MutableSequence["QuotaError"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="QuotaError",
    )
    quota_metrics: MutableSequence[metric_value.MetricValueSet] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=metric_value.MetricValueSet,
    )
    service_config_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class QuotaError(proto.Message):
    r"""Represents error information for
    [QuotaOperation][google.api.servicecontrol.v1.QuotaOperation].

    Attributes:
        code (google.cloud.servicecontrol_v1.types.QuotaError.Code):
            Error code.
        subject (str):
            Subject to whom this error applies. See the
            specific enum for more details on this field.
            For example, "clientip:<ip address of client>"
            or "project:<Google developer project id>".
        description (str):
            Free-form text that provides details on the
            cause of the error.
        status (google.rpc.status_pb2.Status):
            Contains additional information about the quota error. If
            available, ``status.code`` will be non zero.
    """

    class Code(proto.Enum):
        r"""Error codes related to project config validations are deprecated
        since the quota controller methods do not perform these validations.
        Instead services have to call the Check method, without
        quota_properties field, to perform these validations before calling
        the quota controller methods. These methods check only for project
        deletion to be wipe out compliant.

        Values:
            UNSPECIFIED (0):
                This is never used.
            RESOURCE_EXHAUSTED (8):
                Quota allocation failed. Same as
                [google.rpc.Code.RESOURCE_EXHAUSTED][google.rpc.Code.RESOURCE_EXHAUSTED].
            BILLING_NOT_ACTIVE (107):
                Consumer cannot access the service because
                the service requires active billing.
            PROJECT_DELETED (108):
                Consumer's project has been marked as deleted
                (soft deletion).
            API_KEY_INVALID (105):
                Specified API key is invalid.
            API_KEY_EXPIRED (112):
                Specified API Key has expired.
        """

        UNSPECIFIED = 0
        RESOURCE_EXHAUSTED = 8
        BILLING_NOT_ACTIVE = 107
        PROJECT_DELETED = 108
        API_KEY_INVALID = 105
        API_KEY_EXPIRED = 112

    code: Code = proto.Field(
        proto.ENUM,
        number=1,
        enum=Code,
    )
    subject: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    status: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=4,
        message=status_pb2.Status,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
