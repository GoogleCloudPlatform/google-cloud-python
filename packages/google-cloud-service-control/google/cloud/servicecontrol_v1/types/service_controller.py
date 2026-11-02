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

from google.cloud.servicecontrol_v1.types import check_error
from google.cloud.servicecontrol_v1.types import operation as gas_operation

__protobuf__ = proto.module(
    package="google.api.servicecontrol.v1",
    manifest={
        "CheckRequest",
        "CheckResponse",
        "ReportRequest",
        "ReportResponse",
    },
)


class CheckRequest(proto.Message):
    r"""Request message for the Check method.

    Attributes:
        service_name (str):
            The service name as specified in its service configuration.
            For example, ``"pubsub.googleapis.com"``.

            See
            `google.api.Service <https://cloud.google.com/service-management/reference/rpc/google.api#google.api.Service>`__
            for the definition of a service name.
        operation (google.cloud.servicecontrol_v1.types.Operation):
            The operation to be checked.
        service_config_id (str):
            Specifies which version of service
            configuration should be used to process the
            request.

            If unspecified or no matching version can be
            found, the latest one will be used.
    """

    service_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    operation: gas_operation.Operation = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gas_operation.Operation,
    )
    service_config_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class CheckResponse(proto.Message):
    r"""Response message for the Check method.

    Attributes:
        operation_id (str):
            The same operation_id value used in the
            [CheckRequest][google.api.servicecontrol.v1.CheckRequest].
            Used for logging and diagnostics purposes.
        check_errors (MutableSequence[google.cloud.servicecontrol_v1.types.CheckError]):
            Indicate the decision of the check.

            If no check errors are present, the service
            should process the operation. Otherwise the
            service should use the list of errors to
            determine the appropriate action.
        service_config_id (str):
            The actual config id used to process the
            request.
        service_rollout_id (str):
            The current service rollout id used to
            process the request.
        check_info (google.cloud.servicecontrol_v1.types.CheckResponse.CheckInfo):
            Feedback data returned from the server during
            processing a Check request.
    """

    class CheckInfo(proto.Message):
        r"""Contains additional information about the check operation.

        Attributes:
            unused_arguments (MutableSequence[str]):
                A list of fields and label keys that are
                ignored by the server. The client doesn't need
                to send them for following requests to improve
                performance and allow better aggregation.
            consumer_info (google.cloud.servicecontrol_v1.types.CheckResponse.ConsumerInfo):
                Consumer info of this check.
            api_key_uid (str):
                The unique id of the api key in the format of
                "apikey:<UID>". This field will be populated
                when the consumer passed to Service Control is
                an API key and all the API key related
                validations are successful.
        """

        unused_arguments: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        consumer_info: "CheckResponse.ConsumerInfo" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="CheckResponse.ConsumerInfo",
        )
        api_key_uid: str = proto.Field(
            proto.STRING,
            number=5,
        )

    class ConsumerInfo(proto.Message):
        r"""``ConsumerInfo`` provides information about the consumer.

        Attributes:
            project_number (int):
                The Google cloud project number, e.g.
                1234567890. A value of 0 indicates no project
                    number is found.

                NOTE: This field is deprecated after we support
                flexible consumer id. New code should not depend
                on this field anymore.
            type_ (google.cloud.servicecontrol_v1.types.CheckResponse.ConsumerInfo.ConsumerType):
                The type of the consumer which should have been defined in
                `Google Resource
                Manager <https://cloud.google.com/resource-manager/>`__.
            consumer_number (int):
                The consumer identity number, can be Google
                cloud project number, folder number or
                organization number e.g. 1234567890. A value of
                0 indicates no consumer number is found.
        """

        class ConsumerType(proto.Enum):
            r"""The type of the consumer as defined in `Google Resource
            Manager <https://cloud.google.com/resource-manager/>`__.

            Values:
                CONSUMER_TYPE_UNSPECIFIED (0):
                    This is never used.
                PROJECT (1):
                    The consumer is a Google Cloud Project.
                FOLDER (2):
                    The consumer is a Google Cloud Folder.
                ORGANIZATION (3):
                    The consumer is a Google Cloud Organization.
                SERVICE_SPECIFIC (4):
                    Service-specific resource container which is
                    defined by the service producer to offer their
                    users the ability to manage service control
                    functionalities at a finer level of granularity
                    than the PROJECT.
            """

            CONSUMER_TYPE_UNSPECIFIED = 0
            PROJECT = 1
            FOLDER = 2
            ORGANIZATION = 3
            SERVICE_SPECIFIC = 4

        project_number: int = proto.Field(
            proto.INT64,
            number=1,
        )
        type_: "CheckResponse.ConsumerInfo.ConsumerType" = proto.Field(
            proto.ENUM,
            number=2,
            enum="CheckResponse.ConsumerInfo.ConsumerType",
        )
        consumer_number: int = proto.Field(
            proto.INT64,
            number=3,
        )

    operation_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    check_errors: MutableSequence[check_error.CheckError] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=check_error.CheckError,
    )
    service_config_id: str = proto.Field(
        proto.STRING,
        number=5,
    )
    service_rollout_id: str = proto.Field(
        proto.STRING,
        number=11,
    )
    check_info: CheckInfo = proto.Field(
        proto.MESSAGE,
        number=6,
        message=CheckInfo,
    )


class ReportRequest(proto.Message):
    r"""Request message for the Report method.

    Attributes:
        service_name (str):
            The service name as specified in its service configuration.
            For example, ``"pubsub.googleapis.com"``.

            See
            `google.api.Service <https://cloud.google.com/service-management/reference/rpc/google.api#google.api.Service>`__
            for the definition of a service name.
        operations (MutableSequence[google.cloud.servicecontrol_v1.types.Operation]):
            Operations to be reported.

            Typically the service should report one operation per
            request. Putting multiple operations into a single request
            is allowed, but should be used only when multiple operations
            are natually available at the time of the report.

            There is no limit on the number of operations in the same
            ReportRequest, however the ReportRequest size should be no
            larger than 1MB. See
            [ReportResponse.report_errors][google.api.servicecontrol.v1.ReportResponse.report_errors]
            for partial failure behavior.
        service_config_id (str):
            Specifies which version of service config
            should be used to process the request.

            If unspecified or no matching version can be
            found, the latest one will be used.
    """

    service_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    operations: MutableSequence[gas_operation.Operation] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=gas_operation.Operation,
    )
    service_config_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ReportResponse(proto.Message):
    r"""Response message for the Report method.

    Attributes:
        report_errors (MutableSequence[google.cloud.servicecontrol_v1.types.ReportResponse.ReportError]):
            Partial failures, one for each ``Operation`` in the request
            that failed processing. There are three possible
            combinations of the RPC status:

            1. The combination of a successful RPC status and an empty
               ``report_errors`` list indicates a complete success where
               all ``Operations`` in the request are processed
               successfully.
            2. The combination of a successful RPC status and a
               non-empty ``report_errors`` list indicates a partial
               success where some ``Operations`` in the request
               succeeded. Each ``Operation`` that failed processing has
               a corresponding item in this list.
            3. A failed RPC status indicates a general non-deterministic
               failure. When this happens, it's impossible to know which
               of the 'Operations' in the request succeeded or failed.
        service_config_id (str):
            The actual config id used to process the
            request.
        service_rollout_id (str):
            The current service rollout id used to
            process the request.
    """

    class ReportError(proto.Message):
        r"""Represents the processing error of one
        [Operation][google.api.servicecontrol.v1.Operation] in the request.

        Attributes:
            operation_id (str):
                The
                [Operation.operation_id][google.api.servicecontrol.v1.Operation.operation_id]
                value from the request.
            status (google.rpc.status_pb2.Status):
                Details of the error when processing the
                [Operation][google.api.servicecontrol.v1.Operation].
        """

        operation_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        status: status_pb2.Status = proto.Field(
            proto.MESSAGE,
            number=2,
            message=status_pb2.Status,
        )

    report_errors: MutableSequence[ReportError] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=ReportError,
    )
    service_config_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    service_rollout_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
