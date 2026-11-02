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

__protobuf__ = proto.module(
    package="google.analytics.admin.v1alpha",
    manifest={
        "ParameterMutation",
        "EventCreateRule",
        "EventEditRule",
        "MatchingCondition",
    },
)


class ParameterMutation(proto.Message):
    r"""Defines an event parameter to mutate.

    Attributes:
        parameter (str):
            Required. The name of the parameter to mutate. This value
            must:

            - be less than 40 characters.
            - be unique across across all mutations within the rule
            - consist only of letters, digits or \_ (underscores) For
              event edit rules, the name may also be set to 'event_name'
              to modify the event_name in place.
        parameter_value (str):
            Required. The value mutation to perform.

            - Must be less than 100 characters.
            - To specify a constant value for the param, use the value's
              string.
            - To copy value from another parameter, use syntax like
              "[[other_parameter]]" For more details, see this `help
              center
              article <https://support.google.com/analytics/answer/10085872#modify-an-event&zippy=%2Cin-this-article%2Cmodify-parameters>`__.
    """

    parameter: str = proto.Field(
        proto.STRING,
        number=1,
    )
    parameter_value: str = proto.Field(
        proto.STRING,
        number=2,
    )


class EventCreateRule(proto.Message):
    r"""An Event Create Rule defines conditions that will trigger the
    creation of an entirely new event based upon matched criteria of
    a source event. Additional mutations of the parameters from the
    source event can be defined.

    Unlike Event Edit rules, Event Creation Rules have no defined
    order.  They will all be run independently.

    Event Edit and Event Create rules can't be used to modify an
    event created from an Event Create rule.

    Attributes:
        name (str):
            Output only. Resource name for this EventCreateRule
            resource. Format:
            properties/{property}/dataStreams/{data_stream}/eventCreateRules/{event_create_rule}
        destination_event (str):
            Required. The name of the new event to be created.

            This value must:

            - be less than 40 characters
            - consist only of letters, digits or \_ (underscores)
            - start with a letter
        event_conditions (MutableSequence[google.analytics.admin_v1alpha.types.MatchingCondition]):
            Required. Must have at least one condition,
            and can have up to 10 max. Conditions on the
            source event must match for this rule to be
            applied.
        source_copy_parameters (bool):
            If true, the source parameters are copied to
            the new event. If false, or unset, all
            non-internal parameters are not copied from the
            source event. Parameter mutations are applied
            after the parameters have been copied.
        parameter_mutations (MutableSequence[google.analytics.admin_v1alpha.types.ParameterMutation]):
            Parameter mutations define parameter behavior
            on the new event, and are applied in order.
            A maximum of 20 mutations can be applied.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    destination_event: str = proto.Field(
        proto.STRING,
        number=2,
    )
    event_conditions: MutableSequence["MatchingCondition"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="MatchingCondition",
    )
    source_copy_parameters: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    parameter_mutations: MutableSequence["ParameterMutation"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="ParameterMutation",
    )


class EventEditRule(proto.Message):
    r"""An Event Edit Rule defines conditions that will trigger the
    creation of an entirely new event based upon matched criteria of
    a source event. Additional mutations of the parameters from the
    source event can be defined.

    Unlike Event Create rules, Event Edit Rules are applied in their
    defined order.

    Event Edit rules can't be used to modify an event created from
    an Event Create rule.

    Attributes:
        name (str):
            Identifier. Resource name for this EventEditRule resource.
            Format:
            properties/{property}/dataStreams/{data_stream}/eventEditRules/{event_edit_rule}
        display_name (str):
            Required. The display name of this event edit
            rule. Maximum of 255 characters.
        event_conditions (MutableSequence[google.analytics.admin_v1alpha.types.MatchingCondition]):
            Required. Conditions on the source event must
            match for this rule to be applied. Must have at
            least one condition, and can have up to 10 max.
        parameter_mutations (MutableSequence[google.analytics.admin_v1alpha.types.ParameterMutation]):
            Required. Parameter mutations define
            parameter behavior on the new event, and are
            applied in order. A maximum of 20 mutations can
            be applied.
        processing_order (int):
            Output only. The order for which this rule
            will be processed. Rules with an order value
            lower than this will be processed before this
            rule, rules with an order value higher than this
            will be processed after this rule. New event
            edit rules will be assigned an order value at
            the end of the order.

            This value does not apply to event create rules.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    event_conditions: MutableSequence["MatchingCondition"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="MatchingCondition",
    )
    parameter_mutations: MutableSequence["ParameterMutation"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="ParameterMutation",
    )
    processing_order: int = proto.Field(
        proto.INT64,
        number=5,
    )


class MatchingCondition(proto.Message):
    r"""Defines a condition for when an Event Edit or Event Creation
    rule applies to an event.

    Attributes:
        field (str):
            Required. The name of the field that is compared against for
            the condition. If 'event_name' is specified this condition
            will apply to the name of the event. Otherwise the condition
            will apply to a parameter with the specified name.

            This value cannot contain spaces.
        comparison_type (google.analytics.admin_v1alpha.types.MatchingCondition.ComparisonType):
            Required. The type of comparison to be
            applied to the value.
        value (str):
            Required. The value being compared against
            for this condition.  The runtime implementation
            may perform type coercion of this value to
            evaluate this condition based on the type of the
            parameter value.
        negated (bool):
            Whether or not the result of the comparison should be
            negated. For example, if ``negated`` is true, then 'equals'
            comparisons would function as 'not equals'.
    """

    class ComparisonType(proto.Enum):
        r"""Comparison type for matching condition

        Values:
            COMPARISON_TYPE_UNSPECIFIED (0):
                Unknown
            EQUALS (1):
                Equals, case sensitive
            EQUALS_CASE_INSENSITIVE (2):
                Equals, case insensitive
            CONTAINS (3):
                Contains, case sensitive
            CONTAINS_CASE_INSENSITIVE (4):
                Contains, case insensitive
            STARTS_WITH (5):
                Starts with, case sensitive
            STARTS_WITH_CASE_INSENSITIVE (6):
                Starts with, case insensitive
            ENDS_WITH (7):
                Ends with, case sensitive
            ENDS_WITH_CASE_INSENSITIVE (8):
                Ends with, case insensitive
            GREATER_THAN (9):
                Greater than
            GREATER_THAN_OR_EQUAL (10):
                Greater than or equal
            LESS_THAN (11):
                Less than
            LESS_THAN_OR_EQUAL (12):
                Less than or equal
            REGULAR_EXPRESSION (13):
                regular expression. Only supported for web
                streams.
            REGULAR_EXPRESSION_CASE_INSENSITIVE (14):
                regular expression, case insensitive. Only
                supported for web streams.
        """

        COMPARISON_TYPE_UNSPECIFIED = 0
        EQUALS = 1
        EQUALS_CASE_INSENSITIVE = 2
        CONTAINS = 3
        CONTAINS_CASE_INSENSITIVE = 4
        STARTS_WITH = 5
        STARTS_WITH_CASE_INSENSITIVE = 6
        ENDS_WITH = 7
        ENDS_WITH_CASE_INSENSITIVE = 8
        GREATER_THAN = 9
        GREATER_THAN_OR_EQUAL = 10
        LESS_THAN = 11
        LESS_THAN_OR_EQUAL = 12
        REGULAR_EXPRESSION = 13
        REGULAR_EXPRESSION_CASE_INSENSITIVE = 14

    field: str = proto.Field(
        proto.STRING,
        number=1,
    )
    comparison_type: ComparisonType = proto.Field(
        proto.ENUM,
        number=2,
        enum=ComparisonType,
    )
    value: str = proto.Field(
        proto.STRING,
        number=3,
    )
    negated: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
