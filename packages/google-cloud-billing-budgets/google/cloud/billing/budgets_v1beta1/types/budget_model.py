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

import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.type.date_pb2 as date_pb2  # type: ignore
import google.type.money_pb2 as money_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.billing.budgets.v1beta1",
    manifest={
        "CalendarPeriod",
        "Budget",
        "BudgetAmount",
        "LastPeriodAmount",
        "ThresholdRule",
        "AllUpdatesRule",
        "Filter",
        "CustomPeriod",
    },
)


class CalendarPeriod(proto.Enum):
    r"""A ``CalendarPeriod`` represents the abstract concept of a time
    period that has a canonical start. Grammatically, "the start of the
    current ``CalendarPeriod``". All calendar times begin at 12 AM US
    and Canadian Pacific Time (UTC-8).

    Values:
        CALENDAR_PERIOD_UNSPECIFIED (0):
            Calendar period is unset. This is the default
            if the budget is for a custom time period
            (CustomPeriod).
        MONTH (1):
            A month. Month starts on the first day of
            each month, such as January 1, February 1, March
            1, and so on.
        QUARTER (2):
            A quarter. Quarters start on dates January 1,
            April 1, July 1, and October 1 of each year.
        YEAR (3):
            A year. Year starts on January 1.
    """

    CALENDAR_PERIOD_UNSPECIFIED = 0
    MONTH = 1
    QUARTER = 2
    YEAR = 3


class Budget(proto.Message):
    r"""A budget is a plan that describes what you expect to spend on
    Cloud projects, plus the rules to execute as spend is tracked
    against that plan, (for example, send an alert when 90% of the
    target spend is met). The budget time period is configurable,
    with options such as month (default), quarter, year, or custom
    time period.

    Attributes:
        name (str):
            Output only. Resource name of the budget. The resource name
            implies the scope of a budget. Values are of the form
            ``billingAccounts/{billingAccountId}/budgets/{budgetId}``.
        display_name (str):
            User data for display name in UI.
            Validation: <= 60 chars.
        budget_filter (google.cloud.billing.budgets_v1beta1.types.Filter):
            Optional. Filters that define which resources
            are used to compute the actual spend against the
            budget amount, such as projects, services, and
            the budget's time period, as well as other
            filters.
        amount (google.cloud.billing.budgets_v1beta1.types.BudgetAmount):
            Required. Budgeted amount.
        threshold_rules (MutableSequence[google.cloud.billing.budgets_v1beta1.types.ThresholdRule]):
            Optional. Rules that trigger alerts (notifications of
            thresholds being crossed) when spend exceeds the specified
            percentages of the budget.

            Optional for ``pubsubTopic`` notifications.

            Required if using email notifications.
        all_updates_rule (google.cloud.billing.budgets_v1beta1.types.AllUpdatesRule):
            Optional. Rules to apply to notifications
            sent based on budget spend and thresholds.
        etag (str):
            Optional. Etag to validate that the object is
            unchanged for a read-modify-write operation.
            An empty etag will cause an update to overwrite
            other changes.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    budget_filter: "Filter" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Filter",
    )
    amount: "BudgetAmount" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="BudgetAmount",
    )
    threshold_rules: MutableSequence["ThresholdRule"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="ThresholdRule",
    )
    all_updates_rule: "AllUpdatesRule" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="AllUpdatesRule",
    )
    etag: str = proto.Field(
        proto.STRING,
        number=7,
    )


class BudgetAmount(proto.Message):
    r"""The budgeted amount for each usage period.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        specified_amount (google.type.money_pb2.Money):
            A specified amount to use as the budget. ``currency_code``
            is optional. If specified when creating a budget, it must
            match the currency of the billing account. If specified when
            updating a budget, it must match the currency_code of the
            existing budget. The ``currency_code`` is provided on
            output.

            This field is a member of `oneof`_ ``budget_amount``.
        last_period_amount (google.cloud.billing.budgets_v1beta1.types.LastPeriodAmount):
            Use the last period's actual spend as the budget for the
            present period. LastPeriodAmount can only be set when the
            budget's time period is a
            [Filter.calendar_period][google.cloud.billing.budgets.v1beta1.Filter.calendar_period].
            It cannot be set in combination with
            [Filter.custom_period][google.cloud.billing.budgets.v1beta1.Filter.custom_period].

            This field is a member of `oneof`_ ``budget_amount``.
    """

    specified_amount: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="budget_amount",
        message=money_pb2.Money,
    )
    last_period_amount: "LastPeriodAmount" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="budget_amount",
        message="LastPeriodAmount",
    )


class LastPeriodAmount(proto.Message):
    r"""Describes a budget amount targeted to the last
    [Filter.calendar_period][google.cloud.billing.budgets.v1beta1.Filter.calendar_period]
    spend. At this time, the amount is automatically 100% of the last
    calendar period's spend; that is, there are no other options yet.
    Future configuration options will be described here (for example,
    configuring a percentage of last period's spend). LastPeriodAmount
    cannot be set for a budget configured with a
    [Filter.custom_period][google.cloud.billing.budgets.v1beta1.Filter.custom_period].

    """


class ThresholdRule(proto.Message):
    r"""ThresholdRule contains the definition of a threshold. Threshold
    rules define the triggering events used to generate a budget
    notification email. When a threshold is crossed (spend exceeds the
    specified percentages of the budget), budget alert emails are sent
    to the email recipients you specify in the
    `NotificationsRule <#notificationsrule>`__.

    Threshold rules also affect the fields included in the `JSON data
    object <https://cloud.google.com/billing/docs/how-to/budgets-programmatic-notifications#notification_format>`__
    sent to a Pub/Sub topic.

    Threshold rules are *required* if using email notifications.

    Threshold rules are *optional* if only setting a ```pubsubTopic``
    NotificationsRule <#NotificationsRule>`__, unless you want your JSON
    data object to include data about the thresholds you set.

    For more information, see `set budget threshold rules and
    actions <https://cloud.google.com/billing/docs/how-to/budgets#budget-actions>`__.

    Attributes:
        threshold_percent (float):
            Required. Send an alert when this threshold
            is exceeded. This is a 1.0-based percentage, so
            0.5 = 50%. Validation: non-negative number.
        spend_basis (google.cloud.billing.budgets_v1beta1.types.ThresholdRule.Basis):
            Optional. The type of basis used to determine if spend has
            passed the threshold. Behavior defaults to CURRENT_SPEND if
            not set.
    """

    class Basis(proto.Enum):
        r"""The type of basis used to determine if spend has passed the
        threshold.

        Values:
            BASIS_UNSPECIFIED (0):
                Unspecified threshold basis.
            CURRENT_SPEND (1):
                Use current spend as the basis for comparison
                against the threshold.
            FORECASTED_SPEND (2):
                Use forecasted spend for the period as the basis for
                comparison against the threshold. FORECASTED_SPEND can only
                be set when the budget's time period is a
                [Filter.calendar_period][google.cloud.billing.budgets.v1beta1.Filter.calendar_period].
                It cannot be set in combination with
                [Filter.custom_period][google.cloud.billing.budgets.v1beta1.Filter.custom_period].
        """

        BASIS_UNSPECIFIED = 0
        CURRENT_SPEND = 1
        FORECASTED_SPEND = 2

    threshold_percent: float = proto.Field(
        proto.DOUBLE,
        number=1,
    )
    spend_basis: Basis = proto.Field(
        proto.ENUM,
        number=2,
        enum=Basis,
    )


class AllUpdatesRule(proto.Message):
    r"""AllUpdatesRule defines notifications that are sent based on
    budget spend and thresholds.

    Attributes:
        pubsub_topic (str):
            Optional. The name of the Pub/Sub topic where budget related
            messages will be published, in the form
            ``projects/{project_id}/topics/{topic_id}``. Updates are
            sent at regular intervals to the topic. The topic needs to
            be created before the budget is created; see
            https://cloud.google.com/billing/docs/how-to/budgets-programmatic-notifications
            for more details. Caller is expected to have
            ``pubsub.topics.setIamPolicy`` permission on the topic when
            it's set for a budget, otherwise, the API call will fail
            with PERMISSION_DENIED. See
            https://cloud.google.com/billing/docs/how-to/budgets-programmatic-notifications#permissions_required_for_this_task
            for more details on Pub/Sub roles and permissions.
        schema_version (str):
            Optional. Required when
            [AllUpdatesRule.pubsub_topic][google.cloud.billing.budgets.v1beta1.AllUpdatesRule.pubsub_topic]
            is set. The schema version of the notification sent to
            [AllUpdatesRule.pubsub_topic][google.cloud.billing.budgets.v1beta1.AllUpdatesRule.pubsub_topic].
            Only "1.0" is accepted. It represents the JSON schema as
            defined in
            https://cloud.google.com/billing/docs/how-to/budgets-programmatic-notifications#notification_format.
        monitoring_notification_channels (MutableSequence[str]):
            Optional. Targets to send notifications to when a threshold
            is exceeded. This is in addition to default recipients who
            have billing account IAM roles. The value is the full REST
            resource name of a monitoring notification channel with the
            form
            ``projects/{project_id}/notificationChannels/{channel_id}``.
            A maximum of 5 channels are allowed. See
            https://cloud.google.com/billing/docs/how-to/budgets-notification-recipients
            for more details.
        disable_default_iam_recipients (bool):
            Optional. When set to true, disables default
            notifications sent when a threshold is exceeded.
            Default notifications are sent to those with
            Billing Account Administrator and Billing
            Account User IAM roles for the target account.
        enable_project_level_recipients (bool):
            Optional. When set to true, and when the budget has a single
            project configured, notifications will be sent to project
            level recipients of that project. This field will be ignored
            if the budget has multiple or no project configured.

            Currently, project level recipients are the users with
            ``Owner`` role on a cloud project.
    """

    pubsub_topic: str = proto.Field(
        proto.STRING,
        number=1,
    )
    schema_version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    monitoring_notification_channels: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    disable_default_iam_recipients: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    enable_project_level_recipients: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class Filter(proto.Message):
    r"""A filter for a budget, limiting the scope of the cost to
    calculate.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        projects (MutableSequence[str]):
            Optional. A set of projects of the form
            ``projects/{project}``, specifying that usage from only this
            set of projects should be included in the budget. If
            omitted, the report will include all usage for the billing
            account, regardless of which project the usage occurred on.
        resource_ancestors (MutableSequence[str]):
            Optional. A set of folder and organization names of the form
            ``folders/{folderId}`` or
            ``organizations/{organizationId}``, specifying that usage
            from only this set of folders and organizations should be
            included in the budget. If omitted, the budget includes all
            usage that the billing account pays for. If the folder or
            organization contains projects that are paid for by a
            different Cloud Billing account, the budget *doesn't* apply
            to those projects.
        credit_types (MutableSequence[str]):
            Optional. If
            [Filter.credit_types_treatment][google.cloud.billing.budgets.v1beta1.Filter.credit_types_treatment]
            is INCLUDE_SPECIFIED_CREDITS, this is a list of credit types
            to be subtracted from gross cost to determine the spend for
            threshold calculations. See `a list of acceptable credit
            type
            values <https://cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#credits-type>`__.

            If
            [Filter.credit_types_treatment][google.cloud.billing.budgets.v1beta1.Filter.credit_types_treatment]
            is **not** INCLUDE_SPECIFIED_CREDITS, this field must be
            empty.
        credit_types_treatment (google.cloud.billing.budgets_v1beta1.types.Filter.CreditTypesTreatment):
            Optional. If not set, default behavior is
            ``INCLUDE_ALL_CREDITS``.
        services (MutableSequence[str]):
            Optional. A set of services of the form
            ``services/{service_id}``, specifying that usage from only
            this set of services should be included in the budget. If
            omitted, the report will include usage for all the services.
            The service names are available through the Catalog API:
            https://cloud.google.com/billing/v1/how-tos/catalog-api.
        subaccounts (MutableSequence[str]):
            Optional. A set of subaccounts of the form
            ``billingAccounts/{account_id}``, specifying that usage from
            only this set of subaccounts should be included in the
            budget. If a subaccount is set to the name of the parent
            account, usage from the parent account will be included. If
            omitted, the report will include usage from the parent
            account and all subaccounts, if they exist.
        labels (MutableMapping[str, google.protobuf.struct_pb2.ListValue]):
            Optional. A single label and value pair specifying that
            usage from only this set of labeled resources should be
            included in the budget. If omitted, the report will include
            all labeled and unlabeled usage.

            An object containing a single ``"key": value`` pair.
            Example: ``{ "name": "wrench" }``.

            *Currently, multiple entries or multiple values per entry
            are not allowed.*
        calendar_period (google.cloud.billing.budgets_v1beta1.types.CalendarPeriod):
            Optional. Specifies to track usage for
            recurring calendar period. For example, assume
            that CalendarPeriod.QUARTER is set. The budget
            will track usage from April 1 to June 30, when
            the current calendar month is April, May, June.
            After that, it will track usage from July 1 to
            September 30 when the current calendar month is
            July, August, September, so on.

            This field is a member of `oneof`_ ``usage_period``.
        custom_period (google.cloud.billing.budgets_v1beta1.types.CustomPeriod):
            Optional. Specifies to track usage from any
            start date (required) to any end date
            (optional). This time period is static, it does
            not recur.

            This field is a member of `oneof`_ ``usage_period``.
    """

    class CreditTypesTreatment(proto.Enum):
        r"""Specifies how credits are applied when determining the spend for
        threshold calculations. Budgets track the total cost minus any
        applicable selected credits. `See the documentation for a list of
        credit
        types <https://cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#credits-type>`__.

        Values:
            CREDIT_TYPES_TREATMENT_UNSPECIFIED (0):
                No description available.
            INCLUDE_ALL_CREDITS (1):
                All types of credit are subtracted from the
                gross cost to determine the spend for threshold
                calculations.
            EXCLUDE_ALL_CREDITS (2):
                All types of credit are added to the net cost
                to determine the spend for threshold
                calculations.
            INCLUDE_SPECIFIED_CREDITS (3):
                `Credit
                types <https://cloud.google.com/billing/docs/how-to/export-data-bigquery-tables#credits-type>`__
                specified in the credit_types field are subtracted from the
                gross cost to determine the spend for threshold
                calculations.
        """

        CREDIT_TYPES_TREATMENT_UNSPECIFIED = 0
        INCLUDE_ALL_CREDITS = 1
        EXCLUDE_ALL_CREDITS = 2
        INCLUDE_SPECIFIED_CREDITS = 3

    projects: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    resource_ancestors: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    credit_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    credit_types_treatment: CreditTypesTreatment = proto.Field(
        proto.ENUM,
        number=4,
        enum=CreditTypesTreatment,
    )
    services: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    subaccounts: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    labels: MutableMapping[str, struct_pb2.ListValue] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=6,
        message=struct_pb2.ListValue,
    )
    calendar_period: "CalendarPeriod" = proto.Field(
        proto.ENUM,
        number=8,
        oneof="usage_period",
        enum="CalendarPeriod",
    )
    custom_period: "CustomPeriod" = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="usage_period",
        message="CustomPeriod",
    )


class CustomPeriod(proto.Message):
    r"""All date times begin at 12 AM US and Canadian Pacific Time
    (UTC-8).

    Attributes:
        start_date (google.type.date_pb2.Date):
            Required. The start date must be after
            January 1, 2017.
        end_date (google.type.date_pb2.Date):
            Optional. The end date of the time period. Budgets with
            elapsed end date won't be processed. If unset, specifies to
            track all usage incurred since the start_date.
    """

    start_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=1,
        message=date_pb2.Date,
    )
    end_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=2,
        message=date_pb2.Date,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
