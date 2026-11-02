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
import proto  # type: ignore

from google.cloud.discoveryengine_v1beta.types import logging

__protobuf__ = proto.module(
    package="google.cloud.discoveryengine.v1beta",
    manifest={
        "Project",
    },
)


class Project(proto.Message):
    r"""Metadata and configurations for a Google Cloud project in the
    service.

    Attributes:
        name (str):
            Output only. Full resource name of the project, for example
            ``projects/{project}``. Note that when making requests,
            project number and project id are both acceptable, but the
            server will always respond in project number.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when this project
            is created.
        provision_completion_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when this project
            is successfully provisioned. Empty value means
            this project is still provisioning and is not
            ready for use.
        service_terms_map (MutableMapping[str, google.cloud.discoveryengine_v1beta.types.Project.ServiceTerms]):
            Output only. A map of terms of services. The key is the
            ``id`` of
            [ServiceTerms][google.cloud.discoveryengine.v1beta.Project.ServiceTerms].
        customer_provided_config (google.cloud.discoveryengine_v1beta.types.Project.CustomerProvidedConfig):
            Optional. Customer provided configurations.
        configurable_billing_status (google.cloud.discoveryengine_v1beta.types.Project.ConfigurableBillingStatus):
            Output only. The current status of the
            project's configurable billing.
    """

    class ServiceTerms(proto.Message):
        r"""Metadata about the terms of service.

        Attributes:
            id (str):
                The unique identifier of this terms of service. Available
                terms:

                - ``GA_DATA_USE_TERMS``: `Terms for data
                  use <https://cloud.google.com/retail/data-use-terms>`__.
                  When using this as ``id``, the acceptable
                  [version][google.cloud.discoveryengine.v1beta.Project.ServiceTerms.version]
                  to provide is ``2022-11-23``.
            version (str):
                The version string of the terms of service. For acceptable
                values, see the comments for
                [id][google.cloud.discoveryengine.v1beta.Project.ServiceTerms.id]
                above.
            state (google.cloud.discoveryengine_v1beta.types.Project.ServiceTerms.State):
                Whether the project has accepted/rejected the
                service terms or it is still pending.
            accept_time (google.protobuf.timestamp_pb2.Timestamp):
                The last time when the project agreed to the
                terms of service.
            decline_time (google.protobuf.timestamp_pb2.Timestamp):
                The last time when the project declined or
                revoked the agreement to terms of service.
        """

        class State(proto.Enum):
            r"""The agreement states this terms of service.

            Values:
                STATE_UNSPECIFIED (0):
                    The default value of the enum. This value is
                    not actually used.
                TERMS_ACCEPTED (1):
                    The project has given consent to the terms of
                    service.
                TERMS_PENDING (2):
                    The project is pending to review and accept
                    the terms of service.
                TERMS_DECLINED (3):
                    The project has declined or revoked the
                    agreement to terms of service.
            """

            STATE_UNSPECIFIED = 0
            TERMS_ACCEPTED = 1
            TERMS_PENDING = 2
            TERMS_DECLINED = 3

        id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        version: str = proto.Field(
            proto.STRING,
            number=2,
        )
        state: "Project.ServiceTerms.State" = proto.Field(
            proto.ENUM,
            number=4,
            enum="Project.ServiceTerms.State",
        )
        accept_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=5,
            message=timestamp_pb2.Timestamp,
        )
        decline_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=6,
            message=timestamp_pb2.Timestamp,
        )

    class CustomerProvidedConfig(proto.Message):
        r"""Customer provided configurations.

        Attributes:
            notebooklm_config (google.cloud.discoveryengine_v1beta.types.Project.CustomerProvidedConfig.NotebooklmConfig):
                Optional. Configuration for NotebookLM
                settings.
        """

        class NotebooklmConfig(proto.Message):
            r"""Configuration for NotebookLM.

            Attributes:
                model_armor_config (google.cloud.discoveryengine_v1beta.types.Project.CustomerProvidedConfig.NotebooklmConfig.ModelArmorConfig):
                    Model Armor configuration to be used for
                    sanitizing user prompts and LLM responses.
                opt_out_notebook_sharing (bool):
                    Optional. Whether to disable the notebook
                    sharing feature for the project. Default to
                    false if not specified.
                data_protection_policy (google.cloud.discoveryengine_v1beta.types.Project.CustomerProvidedConfig.NotebooklmConfig.DataProtectionPolicy):
                    Optional. Specifies the data protection
                    policy for NotebookLM.
                observability_config (google.cloud.discoveryengine_v1beta.types.ObservabilityConfig):
                    Optional. Observability config for
                    NotebookLM.
            """

            class ModelArmorConfig(proto.Message):
                r"""Configuration for customer defined Model Armor templates to
                be used for sanitizing user prompts and LLM responses.

                Attributes:
                    user_prompt_template (str):
                        Optional. The resource name of the Model Armor Template for
                        sanitizing user prompts. Format:
                        projects/{project}/locations/{location}/templates/{template_id}
                        If not specified, no sanitization will be applied to the
                        user prompt.
                    response_template (str):
                        Optional. The resource name of the Model Armor Template for
                        sanitizing LLM responses. Format:
                        projects/{project}/locations/{location}/templates/{template_id}
                        If not specified, no sanitization will be applied to the LLM
                        response.
                """

                user_prompt_template: str = proto.Field(
                    proto.STRING,
                    number=1,
                )
                response_template: str = proto.Field(
                    proto.STRING,
                    number=2,
                )

            class DataProtectionPolicy(proto.Message):
                r"""Data protection policy config for NotebookLM.

                Attributes:
                    sensitive_data_protection_policy (google.cloud.discoveryengine_v1beta.types.Project.CustomerProvidedConfig.NotebooklmConfig.DataProtectionPolicy.SensitiveDataProtectionPolicy):
                        Optional. The sensitive data protection
                        policy.
                """

                class SensitiveDataProtectionPolicy(proto.Message):
                    r"""Specifies a Sensitive Data Protection
                    (https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)
                    policy.

                    Attributes:
                        policy (str):
                            Optional. The Sensitive Data Protection
                            policy resource name.
                    """

                    policy: str = proto.Field(
                        proto.STRING,
                        number=1,
                    )

                sensitive_data_protection_policy: "Project.CustomerProvidedConfig.NotebooklmConfig.DataProtectionPolicy.SensitiveDataProtectionPolicy" = proto.Field(
                    proto.MESSAGE,
                    number=1,
                    message="Project.CustomerProvidedConfig.NotebooklmConfig.DataProtectionPolicy.SensitiveDataProtectionPolicy",
                )

            model_armor_config: "Project.CustomerProvidedConfig.NotebooklmConfig.ModelArmorConfig" = proto.Field(
                proto.MESSAGE,
                number=1,
                message="Project.CustomerProvidedConfig.NotebooklmConfig.ModelArmorConfig",
            )
            opt_out_notebook_sharing: bool = proto.Field(
                proto.BOOL,
                number=2,
            )
            data_protection_policy: "Project.CustomerProvidedConfig.NotebooklmConfig.DataProtectionPolicy" = proto.Field(
                proto.MESSAGE,
                number=5,
                message="Project.CustomerProvidedConfig.NotebooklmConfig.DataProtectionPolicy",
            )
            observability_config: logging.ObservabilityConfig = proto.Field(
                proto.MESSAGE,
                number=6,
                message=logging.ObservabilityConfig,
            )

        notebooklm_config: "Project.CustomerProvidedConfig.NotebooklmConfig" = (
            proto.Field(
                proto.MESSAGE,
                number=3,
                message="Project.CustomerProvidedConfig.NotebooklmConfig",
            )
        )

    class ConfigurableBillingStatus(proto.Message):
        r"""Represents the currently effective configurable billing parameters.
        These values are derived from the customer's subscription history
        stored internally and reflect the thresholds actively being used for
        billing purposes at the time of the GetProject call. This includes
        the start_time of the subscription and may differ from the values in
        ``customer_provided_config`` due to billing rules (e.g., scale-downs
        taking effect only at the start of a new month). We also include the
        update type to indicate the type of update performed on the
        configurable billing configuration in the UpdateProject operation.

        Attributes:
            effective_search_qpm_threshold (int):
                Optional. The currently effective Search QPM
                threshold in queries per minute. This is the
                threshold against which QPM usage is compared
                for overage calculations.
            effective_indexing_core_threshold (int):
                Optional. The currently effective Indexing
                Core threshold. This is the threshold against
                which Indexing Core usage is compared for
                overage calculations.
            start_time (google.protobuf.timestamp_pb2.Timestamp):
                Optional. The start time of the currently
                active billing subscription.
            terminate_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. The latest terminate effective
                time of search qpm and indexing core
                subscriptions.
            search_qpm_threshold_next_update_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. The earliest next update time for the search
                QPM subscription threshold. This is based on the
                next_update_time returned by the underlying Cloud Billing
                Subscription V3 API. This field is populated only if an
                update QPM subscription threshold request is succeeded.
            indexing_core_threshold_next_update_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. The earliest next update time for the indexing
                core subscription threshold. This is based on the
                next_update_time returned by the underlying Cloud Billing
                Subscription V3 API. This field is populated only if an
                update indexing core subscription threshold request is
                succeeded.
            update_type (google.cloud.discoveryengine_v1beta.types.Project.ConfigurableBillingStatus.UpdateType):
                Output only. The type of update performed in
                this operation. This field is populated in the
                response of UpdateProject.
            agent_search_token_subscription_statuses (MutableSequence[google.cloud.discoveryengine_v1beta.types.Project.ConfigurableBillingStatus.AgentSearchTokenSubscriptionStatus]):
                Output only. Per-model Agent Search TPM
                subscription status.
        """

        class UpdateType(proto.Enum):
            r"""The type of update performed on the configurable billing
            configuration.

            Values:
                UPDATE_TYPE_UNSPECIFIED (0):
                    Unspecified update type.
                CREATE (1):
                    Configurable billing was created/enabled.
                DELETE (2):
                    Configurable billing was deleted/disabled.
                SCALE_UP (3):
                    Subscription was scaled up (thresholds
                    increased).
                SCALE_DOWN (4):
                    Subscription was scaled down (thresholds
                    decreased).
            """

            UPDATE_TYPE_UNSPECIFIED = 0
            CREATE = 1
            DELETE = 2
            SCALE_UP = 3
            SCALE_DOWN = 4

        class AgentSearchTokenSubscriptionStatus(proto.Message):
            r"""Per-model Agent Search TPM subscription status. One entry per active
            ``core_subscription.agent_search_token_subscriptions[*]`` entry in
            the customer-provided config; populated by UpdateProject and
            GetProject.

            The lifecycle scalars on this message (``start_time``,
            ``terminate_time``, ``update_type``,
            ``tpm_threshold_next_update_time``) are per (project, model_version)
            — siblings of the whole-relationship ``start_time`` /
            ``terminate_time`` / ``update_type`` on the enclosing
            ConfigurableBillingStatus, but scoped to this specific Agent Search
            TPM subscription instead of to the overall customer-configurable-
            pricing relationship. This per-instance granularity is intentional:
            the underlying SubV3 storage is per-(project, model_version), so
            each model has its own activation, termination, and deferred-update
            clock; surfacing that on the response gives customers the
            granularity they need to manage per-model commitments independently.
            QPM / IndexingCore differ — their storage is one row per (project,
            location), so their lifecycle is represented only by the whole-
            relationship scalars on ConfigurableBillingStatus.

            Attributes:
                model_version (str):
                    Output only. The Gemini model version this status
                    corresponds to. Matches
                    CoreSubscription.AgentSearchTokenSubscription.model_version
                    (a stable Gemini model version from the Gemini Enterprise
                    Agent Platform model-versions registry; see
                    https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-versions#gemini-models).
                effective_tpm_threshold (int):
                    Output only. The currently effective TPM threshold. Reflects
                    scale-up immediately and scale-down at the next billing
                    cycle, matching ``effective_search_qpm_threshold``
                    semantics.
                tpm_threshold_next_update_time (google.protobuf.timestamp_pb2.Timestamp):
                    Output only. The earliest next update time for the TPM
                    subscription threshold for this (project, model_version).
                    Populated only after a successful update.
                start_time (google.protobuf.timestamp_pb2.Timestamp):
                    Output only. When this (project, model_version) Agent Search
                    TPM subscription was first activated. Set once on first
                    activation of this model version and never moved by
                    subsequent threshold updates; on termination + re-activation
                    a new value is recorded. Does NOT move the
                    whole-relationship ``start_time`` on the enclosing
                    ConfigurableBillingStatus, which continues to represent the
                    first activation of the overall
                    customer-configurable-pricing relationship.
                terminate_time (google.protobuf.timestamp_pb2.Timestamp):
                    Output only. If set, the scheduled effective time at which
                    this (project, model_version) Agent Search TPM subscription
                    will terminate. Populated when the customer removes this
                    entry from
                    ``core_subscription.agent_search_token_subscriptions[*]``.
                    Does NOT move the whole-relationship ``terminate_time`` on
                    the enclosing ConfigurableBillingStatus, which is populated
                    only when the entire customer-configurable-pricing
                    relationship is being torn down.
                update_type (google.cloud.discoveryengine_v1beta.types.Project.ConfigurableBillingStatus.UpdateType):
                    Output only. The type of the most recent update to this
                    (project, model_version) subscription, as performed by the
                    most recent UpdateProject call. ``UPDATE_TYPE_UNSPECIFIED``
                    indicates this model_version was not touched by the most
                    recent UpdateProject (its ``effective_tpm_threshold``
                    reflects an earlier update). The whole-relationship
                    ``update_type`` on the enclosing ConfigurableBillingStatus
                    continues to summarize the direction of the most recent
                    update across all surfaces in the project (QPM,
                    IndexingCore, and Agent Search TPM together).
            """

            model_version: str = proto.Field(
                proto.STRING,
                number=1,
            )
            effective_tpm_threshold: int = proto.Field(
                proto.INT64,
                number=2,
            )
            tpm_threshold_next_update_time: timestamp_pb2.Timestamp = proto.Field(
                proto.MESSAGE,
                number=3,
                message=timestamp_pb2.Timestamp,
            )
            start_time: timestamp_pb2.Timestamp = proto.Field(
                proto.MESSAGE,
                number=4,
                message=timestamp_pb2.Timestamp,
            )
            terminate_time: timestamp_pb2.Timestamp = proto.Field(
                proto.MESSAGE,
                number=5,
                message=timestamp_pb2.Timestamp,
            )
            update_type: "Project.ConfigurableBillingStatus.UpdateType" = proto.Field(
                proto.ENUM,
                number=6,
                enum="Project.ConfigurableBillingStatus.UpdateType",
            )

        effective_search_qpm_threshold: int = proto.Field(
            proto.INT64,
            number=1,
        )
        effective_indexing_core_threshold: int = proto.Field(
            proto.INT64,
            number=2,
        )
        start_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=3,
            message=timestamp_pb2.Timestamp,
        )
        terminate_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=4,
            message=timestamp_pb2.Timestamp,
        )
        search_qpm_threshold_next_update_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=5,
            message=timestamp_pb2.Timestamp,
        )
        indexing_core_threshold_next_update_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=6,
            message=timestamp_pb2.Timestamp,
        )
        update_type: "Project.ConfigurableBillingStatus.UpdateType" = proto.Field(
            proto.ENUM,
            number=7,
            enum="Project.ConfigurableBillingStatus.UpdateType",
        )
        agent_search_token_subscription_statuses: MutableSequence[
            "Project.ConfigurableBillingStatus.AgentSearchTokenSubscriptionStatus"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=8,
            message="Project.ConfigurableBillingStatus.AgentSearchTokenSubscriptionStatus",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    provision_completion_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    service_terms_map: MutableMapping[str, ServiceTerms] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=4,
        message=ServiceTerms,
    )
    customer_provided_config: CustomerProvidedConfig = proto.Field(
        proto.MESSAGE,
        number=6,
        message=CustomerProvidedConfig,
    )
    configurable_billing_status: ConfigurableBillingStatus = proto.Field(
        proto.MESSAGE,
        number=10,
        message=ConfigurableBillingStatus,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
