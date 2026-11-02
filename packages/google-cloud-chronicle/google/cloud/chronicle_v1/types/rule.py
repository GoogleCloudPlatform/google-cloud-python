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

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.type.interval_pb2 as interval_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.chronicle.v1",
    manifest={
        "RunFrequency",
        "RuleType",
        "RuleView",
        "Rule",
        "RuleDeployment",
        "Retrohunt",
        "CreateRuleRequest",
        "GetRuleRequest",
        "ListRulesRequest",
        "ListRulesResponse",
        "UpdateRuleRequest",
        "DeleteRuleRequest",
        "VerifyRuleTextRequest",
        "VerifyRuleTextResponse",
        "ListRuleRevisionsRequest",
        "ListRuleRevisionsResponse",
        "CreateRetrohuntRequest",
        "GetRetrohuntRequest",
        "ListRetrohuntsRequest",
        "ListRetrohuntsResponse",
        "GetRuleDeploymentRequest",
        "ListRuleDeploymentsRequest",
        "ListRuleDeploymentsResponse",
        "UpdateRuleDeploymentRequest",
        "CompilationPosition",
        "CompilationDiagnostic",
        "Severity",
        "RetrohuntMetadata",
        "InputsUsed",
    },
)


class RunFrequency(proto.Enum):
    r"""RunFrequency indicates the run frequency at which a YARA-L 2
    rule will run if enabled.

    Values:
        RUN_FREQUENCY_UNSPECIFIED (0):
            The run frequency is unspecified/unknown.
        LIVE (1):
            Executes in real time.
        HOURLY (2):
            Executes once per hour.
        DAILY (3):
            Executes once per day.
    """

    RUN_FREQUENCY_UNSPECIFIED = 0
    LIVE = 1
    HOURLY = 2
    DAILY = 3


class RuleType(proto.Enum):
    r"""RuleType indicates the YARA-L rule type of user-created and
    Google Cloud Threat Intelligence (GCTI) authored rules.

    Values:
        RULE_TYPE_UNSPECIFIED (0):
            The rule type is unspecified/unknown.
        SINGLE_EVENT (1):
            Rule checks for the existence of a single
            event.
        MULTI_EVENT (2):
            Rule checks for correlation between multiple
            events
    """

    RULE_TYPE_UNSPECIFIED = 0
    SINGLE_EVENT = 1
    MULTI_EVENT = 2


class RuleView(proto.Enum):
    r"""RuleView indicates the scope of fields to populate when
    returning the Rule resource.

    Values:
        RULE_VIEW_UNSPECIFIED (0):
            The default/unset value.
            The API will default to the BASIC view for
            ListRules/ListRuleRevisions. The API will
            default to the FULL view for GetRule.
        BASIC (1):
            Include basic metadata about the rule, but not the full
            contents. Returned fields include: revision_id,
            revision_create_time, display_name, author, severity, type,
            allowed_run_frequency, near_real_time_live_rule_eligible,
            etag, and scope. This is the default value for ListRules and
            ListRuleRevisions.
        FULL (2):
            Include all fields.
            This is the default value for GetRule.
        REVISION_METADATA_ONLY (3):
            Include basic metadata about the rule's revision only.
            Returned fields include: revision_id and
            revision_create_time.
    """

    RULE_VIEW_UNSPECIFIED = 0
    BASIC = 1
    FULL = 2
    REVISION_METADATA_ONLY = 3


class Rule(proto.Message):
    r"""The Rule resource represents a user-created rule.
    NEXT TAG: 21

    Attributes:
        name (str):
            Identifier. Full resource name for the rule. Format:
            ``projects/{project}/locations/{location}/instances/{instance}/rules/{rule}``
        revision_id (str):
            Output only. The revision ID of the rule. A new revision is
            created whenever the rule text is changed in any way.
            Format: ``v_{10 digits}_{9 digits}`` Populated in
            REVISION_METADATA_ONLY view and FULL view.
        display_name (str):
            Output only. Display name of the rule.
            Populated in BASIC view and FULL view.
        text (str):
            The YARA-L content of the rule.
            Populated in FULL view.
        author (str):
            Output only. The author of the rule.
            Extracted from the meta section of text.
            Populated in BASIC view and FULL view.
        severity (google.cloud.chronicle_v1.types.Severity):
            Output only. The severity of the rule as
            specified in the meta section of text. Populated
            in BASIC view and FULL view.
        metadata (MutableMapping[str, str]):
            Output only. Additional metadata specified in
            the meta section of text. Populated in FULL
            view.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp of when the rule
            was created. Populated in FULL view.
        revision_create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp of when the rule revision was
            created. Populated in FULL, REVISION_METADATA_ONLY views.
        compilation_state (google.cloud.chronicle_v1.types.Rule.CompilationState):
            Output only. The current compilation state of
            the rule. Populated in FULL view.
        type_ (google.cloud.chronicle_v1.types.RuleType):
            Output only. User-facing type of the rule.
            Extracted from the events section of rule text.
            Populated in BASIC view and FULL view.
        reference_lists (MutableSequence[str]):
            Output only. Resource names of the reference
            lists used in this rule. Populated in FULL view.
        allowed_run_frequencies (MutableSequence[google.cloud.chronicle_v1.types.RunFrequency]):
            Output only. The run frequencies that are
            allowed for the rule. Populated in BASIC view
            and FULL view.
        etag (str):
            The etag for this rule.
            If this is provided on update, the request will
            succeed if and only if it matches the
            server-computed value, and will fail with an
            ABORTED error otherwise.
            Populated in BASIC view and FULL view.
        scope (str):
            Resource name of the DataAccessScope bound to this rule.
            Populated in BASIC view and FULL view. If reference lists
            are used in the rule, validations will be performed against
            this scope to ensure that the reference lists are compatible
            with both the user's and the rule's scopes. The scope should
            be in the format:
            ``projects/{project}/locations/{location}/instances/{instance}/dataAccessScopes/{scope}``.
        compilation_diagnostics (MutableSequence[google.cloud.chronicle_v1.types.CompilationDiagnostic]):
            Output only. A list of a rule's corresponding
            compilation diagnostic messages such as
            compilation errors and compilation warnings.
            Populated in FULL view.
        near_real_time_live_rule_eligible (bool):
            Output only. Indicate the rule can run in
            near real time live rule. If this is true, the
            rule uses the near real time live rule when the
            run frequency is set to LIVE.
        inputs_used (google.cloud.chronicle_v1.types.InputsUsed):
            Output only. The set of inputs used in the rule. For
            example, if the rule uses $e.principal.hostname, then the
            uses_udm field will be true.
    """

    class CompilationState(proto.Enum):
        r"""The current compilation state of the rule.

        Values:
            COMPILATION_STATE_UNSPECIFIED (0):
                The compilation state is unspecified/unknown.
            SUCCEEDED (1):
                The Rule can successfully compile.
            FAILED (2):
                The Rule cannot successfully compile.
                This is possible if a backwards-incompatible
                change was made to the compiler.
        """

        COMPILATION_STATE_UNSPECIFIED = 0
        SUCCEEDED = 1
        FAILED = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    revision_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    text: str = proto.Field(
        proto.STRING,
        number=4,
    )
    author: str = proto.Field(
        proto.STRING,
        number=5,
    )
    severity: "Severity" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="Severity",
    )
    metadata: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    revision_create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    compilation_state: CompilationState = proto.Field(
        proto.ENUM,
        number=10,
        enum=CompilationState,
    )
    type_: "RuleType" = proto.Field(
        proto.ENUM,
        number=12,
        enum="RuleType",
    )
    reference_lists: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=13,
    )
    allowed_run_frequencies: MutableSequence["RunFrequency"] = proto.RepeatedField(
        proto.ENUM,
        number=14,
        enum="RunFrequency",
    )
    etag: str = proto.Field(
        proto.STRING,
        number=15,
    )
    scope: str = proto.Field(
        proto.STRING,
        number=16,
    )
    compilation_diagnostics: MutableSequence["CompilationDiagnostic"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=17,
            message="CompilationDiagnostic",
        )
    )
    near_real_time_live_rule_eligible: bool = proto.Field(
        proto.BOOL,
        number=18,
    )
    inputs_used: "InputsUsed" = proto.Field(
        proto.MESSAGE,
        number=20,
        message="InputsUsed",
    )


class RuleDeployment(proto.Message):
    r"""The RuleDeployment resource represents the deployment state
    of a Rule.

    Attributes:
        name (str):
            Required. The resource name of the rule deployment. Note
            that RuleDeployment is a child of the overall Rule, not any
            individual revision, so the resource ID segment for the Rule
            resource must not reference a specific revision. Format:
            ``projects/{project}/locations/{location}/instances/{instance}/rules/{rule}/deployment``
        enabled (bool):
            Whether the rule is currently deployed
            continuously against incoming data.
        alerting (bool):
            Whether detections resulting from this
            deployment should be considered alerts.
        archived (bool):
            The archive state of the rule deployment. Cannot be set to
            true unless enabled is set to false. If set to true,
            alerting will automatically be set to false. If currently
            set to true, enabled, alerting, and run_frequency cannot be
            updated.
        archive_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the rule
            deployment archive state was last set to true.
            If the rule deployment's current archive state
            is not set to true, the field will be empty.
        run_frequency (google.cloud.chronicle_v1.types.RunFrequency):
            The run frequency of the rule deployment.
        execution_state (google.cloud.chronicle_v1.types.RuleDeployment.ExecutionState):
            Output only. The execution state of the rule
            deployment.
        producer_rules (MutableSequence[str]):
            Output only. The names of the associated/chained producer
            rules. Rules are considered producers for this rule if this
            rule explicitly filters on their ruleid. Format:
            ``projects/{project}/locations/{location}/instances/{instance}/rules/{rule}``
        consumer_rules (MutableSequence[str]):
            Output only. The names of the associated/chained consumer
            rules. Rules are considered consumers of this rule if their
            rule text explicitly filters on this rule's ruleid. Format:
            ``projects/{project}/locations/{location}/instances/{instance}/rules/{rule}``
        last_alert_status_change_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the rule
            deployment alert state was lastly changed. This
            is filled regardless of the current alert state.
            E.g. if the current alert status is false, this
            timestamp will be the timestamp when the alert
            status was changed to false.
    """

    class ExecutionState(proto.Enum):
        r"""The possible execution states the rule deployment can be in.

        Values:
            EXECUTION_STATE_UNSPECIFIED (0):
                Unspecified or unknown execution state.
            DEFAULT (1):
                Default execution state.
            LIMITED (2):
                Rules in limited state may not have their
                executions guaranteed.
            PAUSED (3):
                Paused rules are not executed at all.
        """

        EXECUTION_STATE_UNSPECIFIED = 0
        DEFAULT = 1
        LIMITED = 2
        PAUSED = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    enabled: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    alerting: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    archived: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    archive_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    run_frequency: "RunFrequency" = proto.Field(
        proto.ENUM,
        number=6,
        enum="RunFrequency",
    )
    execution_state: ExecutionState = proto.Field(
        proto.ENUM,
        number=7,
        enum=ExecutionState,
    )
    producer_rules: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    consumer_rules: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=9,
    )
    last_alert_status_change_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )


class Retrohunt(proto.Message):
    r"""Retrohunt is an execution of a Rule over a time range in the
    past.

    Attributes:
        name (str):
            The resource name of the retrohunt. Retrohunt is the child
            of a rule revision. {rule} in the format below is structured
            as {rule_id@revision_id}. Format:
            ``projects/{project}/locations/{location}/instances/{instance}/rules/{rule}/retrohunts/{retrohunt}``
        process_interval (google.type.interval_pb2.Interval):
            Required. The start and end time of the event
            time range this retrohunt processes.
        execution_interval (google.type.interval_pb2.Interval):
            Output only. The start and end time of the
            retrohunt execution. If the retrohunt is not yet
            finished, the end time of the interval will not
            be populated.
        state (google.cloud.chronicle_v1.types.Retrohunt.State):
            Output only. The state of the retrohunt.
        progress_percentage (float):
            Output only. Percent progress of the
            retrohunt towards completion, from 0.00 to
            100.00.
    """

    class State(proto.Enum):
        r"""The possible states a retrohunt can be in.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified or unknown retrohunt state.
            RUNNING (1):
                Running state.
            DONE (2):
                Done state.
            CANCELLED (3):
                Cancelled state.
            FAILED (4):
                Failed state.
        """

        STATE_UNSPECIFIED = 0
        RUNNING = 1
        DONE = 2
        CANCELLED = 3
        FAILED = 4

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    process_interval: interval_pb2.Interval = proto.Field(
        proto.MESSAGE,
        number=2,
        message=interval_pb2.Interval,
    )
    execution_interval: interval_pb2.Interval = proto.Field(
        proto.MESSAGE,
        number=3,
        message=interval_pb2.Interval,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )
    progress_percentage: float = proto.Field(
        proto.FLOAT,
        number=5,
    )


class CreateRuleRequest(proto.Message):
    r"""Request message for CreateRule method.

    Attributes:
        parent (str):
            Required. The parent resource where this rule will be
            created. Format:
            ``projects/{project}/locations/{location}/instances/{instance}``
        rule (google.cloud.chronicle_v1.types.Rule):
            Required. The rule to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    rule: "Rule" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Rule",
    )


class GetRuleRequest(proto.Message):
    r"""Request message for GetRule method.

    Attributes:
        name (str):
            Required. The name of the rule to retrieve. Format:
            ``projects/{project}/locations/{location}/instances/{instance}/rules/{rule}``
        view (google.cloud.chronicle_v1.types.RuleView):
            The view field indicates the scope of fields
            to populate for the Rule being returned. If
            unspecified, defaults to FULL.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: "RuleView" = proto.Field(
        proto.ENUM,
        number=2,
        enum="RuleView",
    )


class ListRulesRequest(proto.Message):
    r"""Request message for ListRules method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of rules.
            Format:
            ``projects/{project}/locations/{location}/instances/{instance}``
        page_size (int):
            The maximum number of rules to return. The
            service may return fewer than this value. If
            unspecified, at most 100 rules will be returned.
            The maximum value is 1000; values above 1000
            will be coerced to 1000.
        page_token (str):
            A page token, received from a previous ``ListRules`` call.
            Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListRules`` must match the call that provided the page
            token.
        view (google.cloud.chronicle_v1.types.RuleView):
            view indicates the scope of fields to
            populate for the Rule being returned. If
            unspecified, defaults to BASIC.
        filter (str):
            Only the following filters are allowed:
            "reference_lists:{reference_list_name}"
            "data_tables:{data_table_name}"
            "display_name:{display_name}".
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
    view: "RuleView" = proto.Field(
        proto.ENUM,
        number=4,
        enum="RuleView",
    )
    filter: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListRulesResponse(proto.Message):
    r"""Response message for ListRules method.

    Attributes:
        rules (MutableSequence[google.cloud.chronicle_v1.types.Rule]):
            The rules from the specified instance.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    rules: MutableSequence["Rule"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Rule",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateRuleRequest(proto.Message):
    r"""Request message for UpdateRule method.

    Attributes:
        rule (google.cloud.chronicle_v1.types.Rule):
            Required. The rule to update.

            The rule's ``name`` field is used to identify the rule to
            update. Format:
            ``projects/{project}/locations/{location}/instances/{instance}/rules/{rule}``
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to update. If not
            included, all fields with a non-empty value will
            be overwritten.
    """

    rule: "Rule" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Rule",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteRuleRequest(proto.Message):
    r"""Request message for the DeleteRule method.

    Attributes:
        name (str):
            Required. The name of the rule to delete. A rule revision
            timestamp cannot be specified as part of the name, as
            deleting specific revisions is not supported. Format:
            ``projects/{project}/locations/{location}/instances/{instance}/rules/{rule}``
        force (bool):
            Optional. If set to true, any retrohunts and
            any detections associated with the rule will
            also be deleted. If set to false, the call will
            only succeed if the rule has no associated
            retrohunts, including completed retrohunts, and
            no associated detections. Regardless of this
            field's value, the rule deployment associated
            with this rule will also be deleted.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class VerifyRuleTextRequest(proto.Message):
    r"""Request message for VerifyRuleText method.

    Attributes:
        instance (str):
            Required. The name of the parent resource, which is the
            SecOps instance associated with the request. Format:
            ``projects/{project}/locations/{location}/instances/{instance}``
        rule_text (str):
            Required. The rule text to verify as a UTF-8
            string.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    rule_text: str = proto.Field(
        proto.STRING,
        number=2,
    )


class VerifyRuleTextResponse(proto.Message):
    r"""Response message for VerifyRuleText method.

    Attributes:
        success (bool):
            Whether or not the rule text was successfully
            verified.
        compilation_diagnostics (MutableSequence[google.cloud.chronicle_v1.types.CompilationDiagnostic]):
            A list of a rule's corresponding compilation
            diagnostic messages such as compilation errors
            and compilation warnings.
    """

    success: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    compilation_diagnostics: MutableSequence["CompilationDiagnostic"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="CompilationDiagnostic",
        )
    )


class ListRuleRevisionsRequest(proto.Message):
    r"""Request message for ListRuleRevisions method.

    Attributes:
        name (str):
            Required. The name of the rule to list revisions for.
            Format:
            ``projects/{project}/locations/{location}/instances/{instance}/rules/{rule}``
        page_size (int):
            The maximum number of revisions to return per
            page. The service may return fewer than this
            value. If unspecified, at most 100 revisions
            will be returned. The maximum value is 1000;
            values above 1000 will be coerced to 1000.
        page_token (str):
            The page token, received from a previous
            ``ListRuleRevisions`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListRuleRevisions`` must match the call that provided the
            page token.
        view (google.cloud.chronicle_v1.types.RuleView):
            The view field indicates the scope of fields
            to populate for the revision being returned. If
            unspecified, defaults to BASIC.
    """

    name: str = proto.Field(
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
    view: "RuleView" = proto.Field(
        proto.ENUM,
        number=4,
        enum="RuleView",
    )


class ListRuleRevisionsResponse(proto.Message):
    r"""Response message for ListRuleRevisions method.

    Attributes:
        rules (MutableSequence[google.cloud.chronicle_v1.types.Rule]):
            The revisions of the rule.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    rules: MutableSequence["Rule"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Rule",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateRetrohuntRequest(proto.Message):
    r"""Request message for CreateRetrohunt method.

    Attributes:
        parent (str):
            Required. The parent of retrohunt, which is a rule. Format:
            ``projects/{project}/locations/{location}/instances/{instance}/rules/{rule}``
        retrohunt (google.cloud.chronicle_v1.types.Retrohunt):
            Required. The retrohunt to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    retrohunt: "Retrohunt" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Retrohunt",
    )


class GetRetrohuntRequest(proto.Message):
    r"""Request message for GetRetrohunt method.

    Attributes:
        name (str):
            Required. The name of the retrohunt to retrieve. Format:
            ``projects/{project}/locations/{location}/instances/{instance}/rules/{rule}/retrohunts/{retrohunt}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListRetrohuntsRequest(proto.Message):
    r"""Request message for ListRetrohunts method.

    Attributes:
        parent (str):
            Required. The rule that the retrohunts belong to. Format:
            ``projects/{project}/locations/{location}/instances/{instance}/rules/{rule}``
        page_size (int):
            The maximum number of retrohunt to return.
            The service may return fewer than this value. If
            unspecified, at most 100 retrohunts will be
            returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            A page token, received from a previous ``ListRetrohunts``
            call. Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListRetrohunts`` must match the call that provided the
            page token.
        filter (str):
            A filter that can be used to retrieve
            specific rule deployments. The following fields
            are filterable:

            state
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


class ListRetrohuntsResponse(proto.Message):
    r"""Response message for ListRetrohunts method.

    Attributes:
        retrohunts (MutableSequence[google.cloud.chronicle_v1.types.Retrohunt]):
            The retrohunts from the specified rule.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    retrohunts: MutableSequence["Retrohunt"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Retrohunt",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetRuleDeploymentRequest(proto.Message):
    r"""Request message for GetRuleDeployment.

    Attributes:
        name (str):
            Required. The name of the rule deployment to retrieve.
            Format:
            ``projects/{project}/locations/{location}/instances/{instance}/rules/{rule}/deployment``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListRuleDeploymentsRequest(proto.Message):
    r"""Request message for ListRuleDeployments.

    Attributes:
        parent (str):
            Required. The collection of all parents which own all rule
            deployments. The "-" wildcard token must be used as the rule
            identifier in the resource path. Format:
            ``projects/{project}/locations/{location}/instances/{instance}/rules/-``
        page_size (int):
            The maximum number of rule deployments to
            return. The service may return fewer than this
            value. If unspecified, at most 100 rule
            deployments will be returned. The maximum value
            is 1000; values above 1000 will be coerced to
            1000.
        page_token (str):
            A page token, received from a previous
            ``ListRuleDeployments`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListRuleDeployments`` must match the call that provided
            the page token.
        filter (str):
            A filter that can be used to retrieve
            specific rule deployments. The following fields
            are filterable:

            archived, name
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


class ListRuleDeploymentsResponse(proto.Message):
    r"""Response message for ListRuleDeployments.

    Attributes:
        rule_deployments (MutableSequence[google.cloud.chronicle_v1.types.RuleDeployment]):
            The rule deployments from all rules.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    rule_deployments: MutableSequence["RuleDeployment"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="RuleDeployment",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateRuleDeploymentRequest(proto.Message):
    r"""Request message for UpdateRuleDeployment.

    Attributes:
        rule_deployment (google.cloud.chronicle_v1.types.RuleDeployment):
            Required. The rule deployment to update.

            The rule deployment's ``name`` field is used to identify the
            rule deployment to update. Format:
            ``projects/{project}/locations/{location}/instances/{instance}/rules/{rule}/deployment``
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to update.
    """

    rule_deployment: "RuleDeployment" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="RuleDeployment",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class CompilationPosition(proto.Message):
    r"""CompilationPosition represents the location of a compilation
    diagnostic in rule text.

    Attributes:
        start_line (int):
            Output only. Start line number, beginning at
            1.
        start_column (int):
            Output only. Start column number, beginning
            at 1.
        end_line (int):
            Output only. End line number, beginning at 1.
        end_column (int):
            Output only. End column number, beginning at
            1.
    """

    start_line: int = proto.Field(
        proto.INT32,
        number=1,
    )
    start_column: int = proto.Field(
        proto.INT32,
        number=2,
    )
    end_line: int = proto.Field(
        proto.INT32,
        number=3,
    )
    end_column: int = proto.Field(
        proto.INT32,
        number=4,
    )


class CompilationDiagnostic(proto.Message):
    r"""CompilationDiagnostic represents a compilation diagnostic
    generated during a rule's compilation, such as a compilation
    error or a compilation warning.

    Attributes:
        message (str):
            Output only. The diagnostic message.
        position (google.cloud.chronicle_v1.types.CompilationPosition):
            Output only. The approximate position in the
            rule text associated with the compilation
            diagnostic. Compilation Position may be empty.
        severity (google.cloud.chronicle_v1.types.CompilationDiagnostic.Severity):
            Output only. The severity of a rule's
            compilation diagnostic.
        uri (str):
            Output only. Link to documentation that
            describes a diagnostic in more detail.
    """

    class Severity(proto.Enum):
        r"""The severity level of the compilation diagnostic.

        Values:
            SEVERITY_UNSPECIFIED (0):
                An unspecified severity level.
            WARNING (1):
                A compilation warning.
            ERROR (2):
                A compilation error.
        """

        SEVERITY_UNSPECIFIED = 0
        WARNING = 1
        ERROR = 2

    message: str = proto.Field(
        proto.STRING,
        number=1,
    )
    position: "CompilationPosition" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="CompilationPosition",
    )
    severity: Severity = proto.Field(
        proto.ENUM,
        number=3,
        enum=Severity,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=5,
    )


class Severity(proto.Message):
    r"""Severity represents the severity level of the rule.

    Attributes:
        display_name (str):
            The display name of the severity level.
            Extracted from the meta section of the rule
            text.
    """

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class RetrohuntMetadata(proto.Message):
    r"""Operation Metadata for Retrohunts.

    Attributes:
        retrohunt (str):
            The name of the retrohunt. Format:
            ``projects/{project}/locations/{location}/instances/{instance}/rules/{rule}/retrohunts/{retrohunt}``
        execution_interval (google.type.interval_pb2.Interval):
            The start and end time of the retrohunt
            execution. If the retrohunt is not yet finished,
            the end time of the interval will not be filled.
        progress_percentage (float):
            Percent progress of the retrohunt towards
            completion, from 0.00 to 100.00.
    """

    retrohunt: str = proto.Field(
        proto.STRING,
        number=1,
    )
    execution_interval: interval_pb2.Interval = proto.Field(
        proto.MESSAGE,
        number=2,
        message=interval_pb2.Interval,
    )
    progress_percentage: float = proto.Field(
        proto.FLOAT,
        number=3,
    )


class InputsUsed(proto.Message):
    r"""InputsUsed is a convenience field that tells us which sources
    of events (if any) were used in the rule.
    NEXT TAG: 4

    Attributes:
        uses_udm (bool):
            Optional. Whether the rule queries UDM
            events.
        uses_entity (bool):
            Optional. Whether the rule queries entity
            events.
        uses_detection (bool):
            Optional. Whether the rule queries
            detections.
    """

    uses_udm: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    uses_entity: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    uses_detection: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
