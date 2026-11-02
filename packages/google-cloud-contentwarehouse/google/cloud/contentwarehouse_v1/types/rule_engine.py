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

import google.iam.v1.policy_pb2 as policy_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.contentwarehouse.v1",
    manifest={
        "RuleSet",
        "Rule",
        "Action",
        "AccessControlAction",
        "DataValidationAction",
        "DataUpdateAction",
        "AddToFolderAction",
        "RemoveFromFolderAction",
        "PublishAction",
        "DeleteDocumentAction",
        "RuleEngineOutput",
        "RuleEvaluatorOutput",
        "InvalidRule",
        "ActionExecutorOutput",
        "RuleActionsPair",
        "ActionOutput",
    },
)


class RuleSet(proto.Message):
    r"""Represents a set of rules from a single customer.

    Attributes:
        name (str):
            The resource name of the rule set. Managed internally.
            Format:
            projects/{project_number}/locations/{location}/ruleSet/{rule_set_id}.

            The name is ignored when creating a rule set.
        description (str):
            Short description of the rule-set.
        source (str):
            Source of the rules i.e., customer name.
        rules (MutableSequence[google.cloud.contentwarehouse_v1.types.Rule]):
            List of rules given by the customer.
    """

    name: str = proto.Field(
        proto.STRING,
        number=6,
    )
    description: str = proto.Field(
        proto.STRING,
        number=1,
    )
    source: str = proto.Field(
        proto.STRING,
        number=2,
    )
    rules: MutableSequence["Rule"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="Rule",
    )


class Rule(proto.Message):
    r"""Represents the rule for a content warehouse trigger.

    Attributes:
        description (str):
            Short description of the rule and its
            context.
        rule_id (str):
            ID of the rule. It has to be unique across
            all the examples. This is managed internally.
        trigger_type (google.cloud.contentwarehouse_v1.types.Rule.TriggerType):
            Identifies the trigger type for running the
            policy.
        condition (str):
            Represents the conditional expression to be evaluated.
            Expression should evaluate to a boolean result. When the
            condition is true actions are executed. Example: user_role =
            "hsbc_role_1" AND doc.salary > 20000
        actions (MutableSequence[google.cloud.contentwarehouse_v1.types.Action]):
            List of actions that are executed when the
            rule is satisfied.
    """

    class TriggerType(proto.Enum):
        r"""The trigger types for actions.

        Values:
            UNKNOWN (0):
                Trigger for unknown action.
            ON_CREATE (1):
                Trigger for create document action.
            ON_UPDATE (4):
                Trigger for update document action.
            ON_CREATE_LINK (7):
                Trigger for create link action.
            ON_DELETE_LINK (8):
                Trigger for delete link action.
        """

        UNKNOWN = 0
        ON_CREATE = 1
        ON_UPDATE = 4
        ON_CREATE_LINK = 7
        ON_DELETE_LINK = 8

    description: str = proto.Field(
        proto.STRING,
        number=1,
    )
    rule_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    trigger_type: TriggerType = proto.Field(
        proto.ENUM,
        number=3,
        enum=TriggerType,
    )
    condition: str = proto.Field(
        proto.STRING,
        number=4,
    )
    actions: MutableSequence["Action"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="Action",
    )


class Action(proto.Message):
    r"""Represents the action triggered by Rule Engine when the rule
    is true.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        action_id (str):
            ID of the action. Managed internally.
        access_control (google.cloud.contentwarehouse_v1.types.AccessControlAction):
            Action triggering access control operations.

            This field is a member of `oneof`_ ``action``.
        data_validation (google.cloud.contentwarehouse_v1.types.DataValidationAction):
            Action triggering data validation operations.

            This field is a member of `oneof`_ ``action``.
        data_update (google.cloud.contentwarehouse_v1.types.DataUpdateAction):
            Action triggering data update operations.

            This field is a member of `oneof`_ ``action``.
        add_to_folder (google.cloud.contentwarehouse_v1.types.AddToFolderAction):
            Action triggering create document link
            operation.

            This field is a member of `oneof`_ ``action``.
        publish_to_pub_sub (google.cloud.contentwarehouse_v1.types.PublishAction):
            Action publish to Pub/Sub operation.

            This field is a member of `oneof`_ ``action``.
        remove_from_folder_action (google.cloud.contentwarehouse_v1.types.RemoveFromFolderAction):
            Action removing a document from a folder.

            This field is a member of `oneof`_ ``action``.
        delete_document_action (google.cloud.contentwarehouse_v1.types.DeleteDocumentAction):
            Action deleting the document.

            This field is a member of `oneof`_ ``action``.
    """

    action_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    access_control: "AccessControlAction" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="action",
        message="AccessControlAction",
    )
    data_validation: "DataValidationAction" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="action",
        message="DataValidationAction",
    )
    data_update: "DataUpdateAction" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="action",
        message="DataUpdateAction",
    )
    add_to_folder: "AddToFolderAction" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="action",
        message="AddToFolderAction",
    )
    publish_to_pub_sub: "PublishAction" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="action",
        message="PublishAction",
    )
    remove_from_folder_action: "RemoveFromFolderAction" = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="action",
        message="RemoveFromFolderAction",
    )
    delete_document_action: "DeleteDocumentAction" = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="action",
        message="DeleteDocumentAction",
    )


class AccessControlAction(proto.Message):
    r"""Represents the action responsible for access control list
    management operations.

    Attributes:
        operation_type (google.cloud.contentwarehouse_v1.types.AccessControlAction.OperationType):
            Identifies the type of operation.
        policy (google.iam.v1.policy_pb2.Policy):
            Represents the new policy from which bindings
            are added, removed or replaced based on the type
            of the operation. the policy is limited to a few
            10s of KB.
    """

    class OperationType(proto.Enum):
        r"""Type of ACL modification operation.

        Values:
            UNKNOWN (0):
                The unknown operation type.
            ADD_POLICY_BINDING (1):
                Adds newly given policy bindings in the
                existing bindings list.
            REMOVE_POLICY_BINDING (2):
                Removes newly given policy bindings from the
                existing bindings list.
            REPLACE_POLICY_BINDING (3):
                Replaces existing policy bindings with the
                given policy binding list
        """

        UNKNOWN = 0
        ADD_POLICY_BINDING = 1
        REMOVE_POLICY_BINDING = 2
        REPLACE_POLICY_BINDING = 3

    operation_type: OperationType = proto.Field(
        proto.ENUM,
        number=1,
        enum=OperationType,
    )
    policy: policy_pb2.Policy = proto.Field(
        proto.MESSAGE,
        number=2,
        message=policy_pb2.Policy,
    )


class DataValidationAction(proto.Message):
    r"""Represents the action responsible for data validation
    operations.

    Attributes:
        conditions (MutableMapping[str, str]):
            Map of (K, V) -> (field, string condition to
            be evaluated on the field) E.g., ("age", "age >
            18  && age < 60") entry triggers validation of
            field age with the given condition. Map entries
            will be ANDed during validation.
    """

    conditions: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=1,
    )


class DataUpdateAction(proto.Message):
    r"""Represents the action responsible for properties update
    operations.

    Attributes:
        entries (MutableMapping[str, str]):
            Map of (K, V) -> (valid name of the field,
            new value of the field) E.g., ("age", "60")
            entry triggers update of field age with a value
            of 60. If the field is not present then new
            entry is added. During update action execution,
            value strings will be casted to appropriate
            types.
    """

    entries: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=1,
    )


class AddToFolderAction(proto.Message):
    r"""Represents the action responsible for adding document under a
    folder.

    Attributes:
        folders (MutableSequence[str]):
            Names of the folder under which new document is to be added.
            Format:
            projects/{project_number}/locations/{location}/documents/{document_id}.
    """

    folders: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class RemoveFromFolderAction(proto.Message):
    r"""Represents the action responsible for remove a document from
    a specific folder.

    Attributes:
        condition (str):
            Condition of the action to be executed.
        folder (str):
            Name of the folder under which new document is to be added.
            Format:
            projects/{project_number}/locations/{location}/documents/{document_id}.
    """

    condition: str = proto.Field(
        proto.STRING,
        number=1,
    )
    folder: str = proto.Field(
        proto.STRING,
        number=2,
    )


class PublishAction(proto.Message):
    r"""Represents the action responsible for publishing messages to
    a Pub/Sub topic.

    Attributes:
        topic_id (str):
            The topic id in the Pub/Sub service for which
            messages will be published to.
        messages (MutableSequence[str]):
            Messages to be published.
    """

    topic_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    messages: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class DeleteDocumentAction(proto.Message):
    r"""Represents the action responsible for deleting the document.

    Attributes:
        enable_hard_delete (bool):
            Boolean field to select between hard vs soft
            delete options. Set 'true' for 'hard delete' and
            'false' for 'soft delete'.
    """

    enable_hard_delete: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class RuleEngineOutput(proto.Message):
    r"""Records the output of Rule Engine including rule evaluation
    and actions result.

    Attributes:
        document_name (str):
            Name of the document against which the rules
            and actions were evaluated.
        rule_evaluator_output (google.cloud.contentwarehouse_v1.types.RuleEvaluatorOutput):
            Output from Rule Evaluator containing
            matched, unmatched and invalid rules.
        action_executor_output (google.cloud.contentwarehouse_v1.types.ActionExecutorOutput):
            Output from Action Executor containing rule
            and corresponding actions execution result.
    """

    document_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    rule_evaluator_output: "RuleEvaluatorOutput" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="RuleEvaluatorOutput",
    )
    action_executor_output: "ActionExecutorOutput" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ActionExecutorOutput",
    )


class RuleEvaluatorOutput(proto.Message):
    r"""Represents the output of the Rule Evaluator.

    Attributes:
        triggered_rules (MutableSequence[google.cloud.contentwarehouse_v1.types.Rule]):
            List of rules fetched from database for the
            given request trigger type.
        matched_rules (MutableSequence[google.cloud.contentwarehouse_v1.types.Rule]):
            A subset of triggered rules that are
            evaluated true for a given request.
        invalid_rules (MutableSequence[google.cloud.contentwarehouse_v1.types.InvalidRule]):
            A subset of triggered rules that failed the
            validation check(s) after parsing.
    """

    triggered_rules: MutableSequence["Rule"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Rule",
    )
    matched_rules: MutableSequence["Rule"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Rule",
    )
    invalid_rules: MutableSequence["InvalidRule"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="InvalidRule",
    )


class InvalidRule(proto.Message):
    r"""A triggered rule that failed the validation check(s) after
    parsing.

    Attributes:
        rule (google.cloud.contentwarehouse_v1.types.Rule):
            Triggered rule.
        error (str):
            Validation error on a parsed expression.
    """

    rule: "Rule" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Rule",
    )
    error: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ActionExecutorOutput(proto.Message):
    r"""Represents the output of the Action Executor.

    Attributes:
        rule_actions_pairs (MutableSequence[google.cloud.contentwarehouse_v1.types.RuleActionsPair]):
            List of rule and corresponding actions
            result.
    """

    rule_actions_pairs: MutableSequence["RuleActionsPair"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="RuleActionsPair",
    )


class RuleActionsPair(proto.Message):
    r"""Represents a rule and outputs of associated actions.

    Attributes:
        rule (google.cloud.contentwarehouse_v1.types.Rule):
            Represents the rule.
        action_outputs (MutableSequence[google.cloud.contentwarehouse_v1.types.ActionOutput]):
            Outputs of executing the actions associated
            with the above rule.
    """

    rule: "Rule" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Rule",
    )
    action_outputs: MutableSequence["ActionOutput"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="ActionOutput",
    )


class ActionOutput(proto.Message):
    r"""Represents the result of executing an action.

    Attributes:
        action_id (str):
            ID of the action.
        action_state (google.cloud.contentwarehouse_v1.types.ActionOutput.State):
            State of an action.
        output_message (str):
            Action execution output message.
    """

    class State(proto.Enum):
        r"""Represents execution state of the action.

        Values:
            UNKNOWN (0):
                The unknown state.
            ACTION_SUCCEEDED (1):
                State indicating action executed
                successfully.
            ACTION_FAILED (2):
                State indicating action failed.
            ACTION_TIMED_OUT (3):
                State indicating action timed out.
            ACTION_PENDING (4):
                State indicating action is pending.
        """

        UNKNOWN = 0
        ACTION_SUCCEEDED = 1
        ACTION_FAILED = 2
        ACTION_TIMED_OUT = 3
        ACTION_PENDING = 4

    action_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    action_state: State = proto.Field(
        proto.ENUM,
        number=2,
        enum=State,
    )
    output_message: str = proto.Field(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
