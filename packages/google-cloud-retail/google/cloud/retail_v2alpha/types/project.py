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

from google.cloud.retail_v2alpha.types import common

__protobuf__ = proto.module(
    package="google.cloud.retail.v2alpha",
    manifest={
        "LoggingConfig",
        "Project",
        "AlertConfig",
    },
)


class LoggingConfig(proto.Message):
    r"""Project level logging config to control what level of log
    will be generated and written to Cloud Logging.

    Attributes:
        name (str):
            Required. Immutable. The name of the LoggingConfig singleton
            resource. Format: projects/\*/loggingConfig
        default_log_generation_rule (google.cloud.retail_v2alpha.types.LoggingConfig.LogGenerationRule):
            The log generation rule that applies by default to all
            services supporting log generation. It can be overridden by
            [ServiceLogGenerationRule][google.cloud.retail.v2alpha.LoggingConfig.ServiceLogGenerationRule]
            for service level control.
        service_log_generation_rules (MutableSequence[google.cloud.retail_v2alpha.types.LoggingConfig.ServiceLogGenerationRule]):
            Controls logging configurations more granularly for each
            supported service.

            This overrides the
            [default_log_generation_rule][google.cloud.retail.v2alpha.LoggingConfig.default_log_generation_rule]
            for the services specified. For those not mentioned, they
            will fallback to the default log generation rule.
    """

    class LoggingLevel(proto.Enum):
        r"""The setting to control log generation.

        Values:
            LOGGING_LEVEL_UNSPECIFIED (0):
                Default value. Defaults to ``LOG_FOR_WARNINGS_AND_ABOVE`` if
                unset.
            LOGGING_DISABLED (1):
                No log will be generated and sent to Cloud
                Logging.
            LOG_ERRORS_AND_ABOVE (2):
                Log for operations resulted in fatal error.
            LOG_WARNINGS_AND_ABOVE (3):
                In addition to ``LOG_ERRORS_AND_ABOVE``, also log for
                operations that have soft errors, quality suggestions.
            LOG_ALL (4):
                Log all operations, including successful
                ones.
        """

        LOGGING_LEVEL_UNSPECIFIED = 0
        LOGGING_DISABLED = 1
        LOG_ERRORS_AND_ABOVE = 2
        LOG_WARNINGS_AND_ABOVE = 3
        LOG_ALL = 4

    class LogGenerationRule(proto.Message):
        r"""The logging configurations for services supporting log
        generation.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            logging_level (google.cloud.retail_v2alpha.types.LoggingConfig.LoggingLevel):
                The logging level.

                By default it is set to ``LOG_WARNINGS_AND_ABOVE``.
            info_log_sample_rate (float):
                The log sample rate for INFO level log entries. You can use
                this to reduce the number of entries generated for INFO
                level logs.

                DO NOT set this field if the
                [logging_level][google.cloud.retail.v2alpha.LoggingConfig.LogGenerationRule.logging_level]
                is not
                [LoggingLevel.LOG_ALL][google.cloud.retail.v2alpha.LoggingConfig.LoggingLevel.LOG_ALL].
                Otherwise, an INVALID_ARGUMENT error is returned.

                Sample rate for INFO logs defaults to 1 when unset (generate
                and send all INFO logs to Cloud Logging). Its value must be
                greater than 0 and less than or equal to 1.

                This field is a member of `oneof`_ ``_info_log_sample_rate``.
        """

        logging_level: "LoggingConfig.LoggingLevel" = proto.Field(
            proto.ENUM,
            number=1,
            enum="LoggingConfig.LoggingLevel",
        )
        info_log_sample_rate: float = proto.Field(
            proto.FLOAT,
            number=2,
            optional=True,
        )

    class ServiceLogGenerationRule(proto.Message):
        r"""The granular logging configurations for supported services.

        Attributes:
            service_name (str):
                Required. Supported service names:

                "CatalogService",
                "CompletionService",
                "ControlService",
                "MerchantCenterStreaming",
                "ModelService",
                "PredictionService",
                "ProductService",
                "ServingConfigService",
                "UserEventService",
            log_generation_rule (google.cloud.retail_v2alpha.types.LoggingConfig.LogGenerationRule):
                The log generation rule that applies to this
                service.
        """

        service_name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        log_generation_rule: "LoggingConfig.LogGenerationRule" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="LoggingConfig.LogGenerationRule",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    default_log_generation_rule: LogGenerationRule = proto.Field(
        proto.MESSAGE,
        number=2,
        message=LogGenerationRule,
    )
    service_log_generation_rules: MutableSequence[ServiceLogGenerationRule] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message=ServiceLogGenerationRule,
        )
    )


class Project(proto.Message):
    r"""Metadata that describes a Cloud Retail Project.

    Attributes:
        name (str):
            Output only. Full resource name of the retail project, such
            as ``projects/{project_id_or_number}/retailProject``.
        enrolled_solutions (MutableSequence[google.cloud.retail_v2alpha.types.SolutionType]):
            Output only. Retail API solutions that the
            project has enrolled.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    enrolled_solutions: MutableSequence[common.SolutionType] = proto.RepeatedField(
        proto.ENUM,
        number=2,
        enum=common.SolutionType,
    )


class AlertConfig(proto.Message):
    r"""Project level alert config.

    Attributes:
        name (str):
            Required. Immutable. The name of the AlertConfig singleton
            resource. Format: projects/\*/alertConfig
        alert_policies (MutableSequence[google.cloud.retail_v2alpha.types.AlertConfig.AlertPolicy]):
            Alert policies for a customer. They must be unique by
            [AlertPolicy.alert_group]
    """

    class AlertPolicy(proto.Message):
        r"""Alert policy for a customer.

        Attributes:
            alert_group (str):
                The feature that provides alerting capability. Supported
                value:

                - ``search-data-quality`` for retail search customers.
                - ``conv-data-quality`` for retail conversation customers.
            enroll_status (google.cloud.retail_v2alpha.types.AlertConfig.AlertPolicy.EnrollStatus):
                The enrollment status of a customer.
            recipients (MutableSequence[google.cloud.retail_v2alpha.types.AlertConfig.AlertPolicy.Recipient]):
                Recipients for the alert policy.
                One alert policy should not exceed 20
                recipients.
        """

        class EnrollStatus(proto.Enum):
            r"""The enrollment status enum for alert policy.

            Values:
                ENROLL_STATUS_UNSPECIFIED (0):
                    Default value. Used for customers who have
                    not responded to the alert policy.
                ENROLLED (1):
                    Customer is enrolled in this policy.
                DECLINED (2):
                    Customer declined this policy.
            """

            ENROLL_STATUS_UNSPECIFIED = 0
            ENROLLED = 1
            DECLINED = 2

        class Recipient(proto.Message):
            r"""Recipient contact information.

            Attributes:
                email_address (str):
                    Email address of the recipient.
            """

            email_address: str = proto.Field(
                proto.STRING,
                number=1,
            )

        alert_group: str = proto.Field(
            proto.STRING,
            number=1,
        )
        enroll_status: "AlertConfig.AlertPolicy.EnrollStatus" = proto.Field(
            proto.ENUM,
            number=2,
            enum="AlertConfig.AlertPolicy.EnrollStatus",
        )
        recipients: MutableSequence["AlertConfig.AlertPolicy.Recipient"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=3,
                message="AlertConfig.AlertPolicy.Recipient",
            )
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    alert_policies: MutableSequence[AlertPolicy] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=AlertPolicy,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
