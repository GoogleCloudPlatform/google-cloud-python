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
    package="google.shopping.merchant.issueresolution.v1",
    manifest={
        "Severity",
        "ContentOption",
        "UserInputActionRenderingOption",
        "RenderAccountIssuesResponse",
        "RenderAccountIssuesRequest",
        "RenderIssuesRequestPayload",
        "RenderProductIssuesResponse",
        "RenderProductIssuesRequest",
        "RenderedIssue",
        "Impact",
        "Breakdown",
        "Action",
        "BuiltInSimpleAction",
        "BuiltInUserInputAction",
        "ActionFlow",
        "InputField",
        "TextWithTooltip",
        "Callout",
        "ExternalAction",
        "TriggerActionRequest",
        "TriggerActionPayload",
        "TriggerActionResponse",
        "ActionInput",
        "InputValue",
    },
)


class Severity(proto.Enum):
    r"""Enum specifying the severity of the issue.

    Values:
        SEVERITY_UNSPECIFIED (0):
            Default value. Will never be provided by the
            API.
        ERROR (1):
            Causes either an account suspension or an
            item disapproval. Errors should be resolved as
            soon as possible to ensure items are eligible to
            appear in results again.
        WARNING (2):
            Warnings can negatively impact the
            performance of ads and can lead to item or
            account suspensions in the future unless the
            issue is resolved.
        INFO (3):
            Infos are suggested optimizations to increase
            data quality. Resolving these issues is
            recommended, but not required.
    """

    SEVERITY_UNSPECIFIED = 0
    ERROR = 1
    WARNING = 2
    INFO = 3


class ContentOption(proto.Enum):
    r"""Enum specifying how is the content returned.

    Values:
        CONTENT_OPTION_UNSPECIFIED (0):
            Default value. Will never be provided by the
            API.
        PRE_RENDERED_HTML (1):
            Returns the detail of the issue as a
            pre-rendered HTML text.
    """

    CONTENT_OPTION_UNSPECIFIED = 0
    PRE_RENDERED_HTML = 1


class UserInputActionRenderingOption(proto.Enum):
    r"""Enum specifying how actions with user input forms, such as
    requesting re-review, are handled.

    Values:
        USER_INPUT_ACTION_RENDERING_OPTION_UNSPECIFIED (0):
            Default value. Will never be provided by the
            API.
        REDIRECT_TO_MERCHANT_CENTER (1):
            Actions that require user input are represented only as
            links that points the business to Merchant Center where they
            can request the action. Provides easier to implement
            alternative to ``BUILT_IN_USER_INPUT_ACTIONS``.
        BUILT_IN_USER_INPUT_ACTIONS (2):
            Returns content and input form definition for each complex
            action. Your application needs to display this content and
            input form to the business before they can request
            processing of the action. To start the action, your
            application needs to call the ``triggeraction`` method.
    """

    USER_INPUT_ACTION_RENDERING_OPTION_UNSPECIFIED = 0
    REDIRECT_TO_MERCHANT_CENTER = 1
    BUILT_IN_USER_INPUT_ACTIONS = 2


class RenderAccountIssuesResponse(proto.Message):
    r"""Response containing an issue resolution content and actions
    for listed account issues.

    Attributes:
        rendered_issues (MutableSequence[google.shopping.merchant_issueresolution_v1.types.RenderedIssue]):
            List of account issues for a given account.

            This list can be shown with compressed, expandable items. In
            the compressed form, the title and impact should be shown
            for each issue. Once the issue is expanded, the detailed
            [content][google.shopping.merchant.issueresolution.v1.RenderedIssue.prerendered_content]
            and available
            [actions][google.shopping.merchant.issueresolution.v1.RenderedIssue.actions]
            should be rendered.
    """

    rendered_issues: MutableSequence["RenderedIssue"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="RenderedIssue",
    )


class RenderAccountIssuesRequest(proto.Message):
    r"""Request to provide issue resolution content and actions for
    business's account issues.

    Attributes:
        name (str):
            Required. The account to fetch issues for. Format:
            ``accounts/{account}``
        language_code (str):
            Optional. The `IETF
            BCP-47 <https://tools.ietf.org/html/bcp47>`__ language code
            used to localize issue resolution content. If not set, the
            result will be in default language ``en-US``.
        time_zone (str):
            Optional. The `IANA <https://www.iana.org/time-zones>`__
            timezone used to localize times in an issue resolution
            content. For example 'America/Los_Angeles'. If not set,
            results will use as a default UTC.
        payload (google.shopping.merchant_issueresolution_v1.types.RenderIssuesRequestPayload):
            Optional. The payload for configuring how the
            content should be rendered.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=2,
    )
    time_zone: str = proto.Field(
        proto.STRING,
        number=3,
    )
    payload: "RenderIssuesRequestPayload" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="RenderIssuesRequestPayload",
    )


class RenderIssuesRequestPayload(proto.Message):
    r"""The payload for configuring how the content should be
    rendered.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        content_option (google.shopping.merchant_issueresolution_v1.types.ContentOption):
            Optional. How the detailed content should be
            returned. Default option is to return the
            content as a pre-rendered HTML text.

            This field is a member of `oneof`_ ``_content_option``.
        user_input_action_option (google.shopping.merchant_issueresolution_v1.types.UserInputActionRenderingOption):
            Optional. How actions with user input form
            should be handled. If not provided, actions will
            be returned as links that points the business to
            Merchant Center where they can request the
            action.

            This field is a member of `oneof`_ ``_user_input_action_option``.
    """

    content_option: "ContentOption" = proto.Field(
        proto.ENUM,
        number=1,
        optional=True,
        enum="ContentOption",
    )
    user_input_action_option: "UserInputActionRenderingOption" = proto.Field(
        proto.ENUM,
        number=2,
        optional=True,
        enum="UserInputActionRenderingOption",
    )


class RenderProductIssuesResponse(proto.Message):
    r"""Response containing an issue resolution content and actions
    for listed product issues.

    Attributes:
        rendered_issues (MutableSequence[google.shopping.merchant_issueresolution_v1.types.RenderedIssue]):
            List of issues for a given product.

            This list can be shown with compressed, expandable items. In
            the compressed form, the
            [title][google.shopping.merchant.issueresolution.v1.RenderedIssue.title]
            and
            [impact][google.shopping.merchant.issueresolution.v1.RenderedIssue.impact]
            should be shown for each issue. Once the issue is expanded,
            the detailed
            [content][google.shopping.merchant.issueresolution.v1.RenderedIssue.prerendered_content]
            and available
            [actions][google.shopping.merchant.issueresolution.v1.RenderedIssue.actions]
            should be rendered.
    """

    rendered_issues: MutableSequence["RenderedIssue"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="RenderedIssue",
    )


class RenderProductIssuesRequest(proto.Message):
    r"""Request to provide an issue resolution content and actions
    for product issues of business's product.

    Attributes:
        name (str):
            Required. The name of the product to fetch issues for.
            Format: ``accounts/{account}/products/{product}``
        language_code (str):
            Optional. The `IETF
            BCP-47 <https://tools.ietf.org/html/bcp47>`__ language code
            used to localize an issue resolution content. If not set,
            the result will be in default language ``en-US``.
        time_zone (str):
            Optional. The `IANA <https://www.iana.org/time-zones>`__
            timezone used to localize times in an issue resolution
            content. For example 'America/Los_Angeles'. If not set,
            results will use as a default UTC.
        payload (google.shopping.merchant_issueresolution_v1.types.RenderIssuesRequestPayload):
            Optional. The payload for configuring how the
            content should be rendered.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=2,
    )
    time_zone: str = proto.Field(
        proto.STRING,
        number=3,
    )
    payload: "RenderIssuesRequestPayload" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="RenderIssuesRequestPayload",
    )


class RenderedIssue(proto.Message):
    r"""An issue affecting specific business or their product.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        prerendered_content (str):
            Details of the issue as a pre-rendered HTML. HTML elements
            contain CSS classes that can be used to customize the style
            of the content.

            Always sanitize the HTML before embedding it directly to
            your application. The sanitizer needs to allow basic HTML
            tags, such as: ``div``, ``span``, ``p``, ``a``, ``ul``,
            ``li``, ``table``, ``tr``, ``td``. For example, you can use
            `DOMPurify <https://www.npmjs.com/package/dompurify>`__.

            CSS classes:

            - ``issue-detail`` - top level container for the detail of
              the issue
            - ``callout-banners`` - section of the ``issue-detail`` with
              callout banners
            - ``callout-banner`` - single callout banner, inside
              ``callout-banners``
            - ``callout-banner-info`` - callout with important
              information (default)
            - ``callout-banner-warning`` - callout with a warning
            - ``callout-banner-error`` - callout informing about an
              error (most severe)
            - ``issue-content`` - section of the ``issue-detail``,
              contains multiple ``content-element``
            - ``content-element`` - content element such as a list, link
              or paragraph, inside ``issue-content``
            - ``root-causes`` - unordered list with items describing
              root causes of the issue, inside ``issue-content``
            - ``root-causes-intro`` - intro text before the
              ``root-causes`` list, inside ``issue-content``
            - ``segment`` - section of the text, ``span`` inside
              paragraph
            - ``segment-attribute`` - section of the text that
              represents a product attribute, for example 'image_link'
            - ``segment-literal`` - section of the text that contains a
              special value, for example '0-1000 kg'
            - ``segment-bold`` - section of the text that should be
              rendered as bold
            - ``segment-italic`` - section of the text that should be
              rendered as italic
            - ``tooltip`` - used on paragraphs that should be rendered
              with a tooltip. A section of the text in such a paragraph
              will have a class ``tooltip-text`` and is intended to be
              shown in a mouse over dialog. If the style is not used,
              the ``tooltip-text`` section would be shown on a new line,
              after the main part of the text.
            - ``tooltip-text`` - marks a section of the text within a
              ``tooltip``, that is intended to be shown in a mouse over
              dialog.
            - ``tooltip-icon`` - marks a section of the text within a
              ``tooltip``, that can be replaced with a tooltip icon, for
              example '?' or 'i'. By default, this section contains a
              ``br`` tag, that is separating the main text and the
              tooltip text when the style is not used.
            - ``tooltip-style-question`` - the tooltip shows helpful
              information, can use the '?' as an icon.
            - ``tooltip-style-info`` - the tooltip adds additional
              information fitting to the context, can use the 'i' as an
              icon.
            - ``content-moderation`` - marks the paragraph that explains
              how the issue was identified.
            - ``new-element`` - Present for new elements added to the
              pre-rendered content in the future. To make sure that a
              new content element does not break your style, you can
              hide everything with this class.

            This field is a member of `oneof`_ ``content``.
        prerendered_out_of_court_dispute_settlement (str):
            Pre-rendered HTML that contains a link to the external
            location where the ODS can be requested and instructions for
            how to request it. HTML elements contain CSS classes that
            can be used to customize the style of this snippet.

            Always sanitize the HTML before embedding it directly to
            your application. The sanitizer needs to allow basic HTML
            tags, such as: ``div``, ``span``, ``p``, ``a``, ``ul``,
            ``li``, ``table``, ``tr``, ``td``. For example, you can use
            `DOMPurify <https://www.npmjs.com/package/dompurify>`__.

            CSS classes:

            - ``ods-section``\ \* - wrapper around the out-of-court
              dispute resolution section
            - ``ods-description``\ \* - intro text for the out-of-court
              dispute resolution. It may contain multiple segments and a
              link.
            - ``ods-param``\ \* - wrapper around the header-value pair
              for parameters that the business may need to provide
              during the ODS process.
            - ``ods-routing-id``\ \* - ods param for the Routing ID.
            - ``ods-reference-id``\ \* - ods param for the Routing ID.
            - ``ods-param-header``\ \* - header for the ODS parameter
            - ``ods-param-value``\ \* - value of the ODS parameter. This
              value should be rendered in a way that it is easy for the
              user to identify and copy.
            - ``segment`` - section of the text, ``span`` inside
              paragraph
            - ``segment-attribute`` - section of the text that
              represents a product attribute, for example 'image_link'
            - ``segment-literal`` - section of the text that contains a
              special value, for example '0-1000 kg'
            - ``segment-bold`` - section of the text that should be
              rendered as bold
            - ``segment-italic`` - section of the text that should be
              rendered as italic
            - ``tooltip`` - used on paragraphs that should be rendered
              with a tooltip. A section of the text in such a paragraph
              will have a class ``tooltip-text`` and is intended to be
              shown in a mouse over dialog. If the style is not used,
              the ``tooltip-text`` section would be shown on a new line,
              after the main part of the text.
            - ``tooltip-text`` - marks a section of the text within a
              ``tooltip``, that is intended to be shown in a mouse over
              dialog.
            - ``tooltip-icon`` - marks a section of the text within a
              ``tooltip``, that can be replaced with a tooltip icon, for
              example '?' or 'i'. By default, this section contains a
              ``br`` tag, that is separating the main text and the
              tooltip text when the style is not used.
            - ``tooltip-style-question`` - the tooltip shows helpful
              information, can use the '?' as an icon.
            - ``tooltip-style-info`` - the tooltip adds additional
              information fitting to the context, can use the 'i' as an
              icon.

            This field is a member of `oneof`_ ``out_of_court_dispute_settlement``.
        title (str):
            Title of the issue.
        impact (google.shopping.merchant_issueresolution_v1.types.Impact):
            Clarifies the severity of the issue.

            The [summarizing
            message][google.shopping.merchant.issueresolution.v1.Impact.message],
            if present, should be shown right under the title for each
            issue. It helps business to quickly understand the impact of
            the issue.

            The detailed
            [breakdown][google.shopping.merchant.issueresolution.v1.Impact.breakdowns]
            helps the business to fully understand the impact of the
            issue. It can be rendered as dialog that opens when the
            business mouse over the summarized impact statement.

            Issues with different
            [severity][google.shopping.merchant.issueresolution.v1.Impact.severity]
            can be styled differently. They may use a different color or
            icon to signal the difference between ``ERROR``, ``WARNING``
            and ``INFO``.
        actions (MutableSequence[google.shopping.merchant_issueresolution_v1.types.Action]):
            A list of actionable steps that can be
            executed to solve the issue. An example is
            requesting a re-review or providing arguments
            when business disagrees with the issue.

            Actions that are supported in (your) third-party
            application can be rendered as buttons and
            should be available to the business when they
            expand the issue.
    """

    prerendered_content: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="content",
    )
    prerendered_out_of_court_dispute_settlement: str = proto.Field(
        proto.STRING,
        number=5,
        oneof="out_of_court_dispute_settlement",
    )
    title: str = proto.Field(
        proto.STRING,
        number=1,
    )
    impact: "Impact" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Impact",
    )
    actions: MutableSequence["Action"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="Action",
    )


class Impact(proto.Message):
    r"""Overall impact of the issue.

    Attributes:
        message (str):
            Optional. Message summarizing the overall
            impact of the issue. If present, it should be
            rendered to the business. For example:
            "Disapproves 90k offers in 25 countries".
        severity (google.shopping.merchant_issueresolution_v1.types.Severity):
            The severity of the issue.
        breakdowns (MutableSequence[google.shopping.merchant_issueresolution_v1.types.Breakdown]):
            Detailed impact breakdown. Explains the types
            of restriction the issue has in different
            shopping destinations and territory. If present,
            it should be rendered to the business. Can be
            shown as a mouse over dropdown or a dialog. Each
            breakdown item represents a group of regions
            with the same impact details.
    """

    message: str = proto.Field(
        proto.STRING,
        number=1,
    )
    severity: "Severity" = proto.Field(
        proto.ENUM,
        number=2,
        enum="Severity",
    )
    breakdowns: MutableSequence["Breakdown"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="Breakdown",
    )


class Breakdown(proto.Message):
    r"""A detailed impact breakdown for a group of regions where the
    impact of the issue on different shopping destinations is the
    same.

    Attributes:
        regions (MutableSequence[google.shopping.merchant_issueresolution_v1.types.Breakdown.Region]):
            Lists of regions. Should be rendered as a
            title for this group of details. The full list
            should be shown to the business. If the list is
            too long, it is recommended to make it
            expandable.
        details (MutableSequence[str]):
            Human readable, localized description of issue's effect on
            different targets. Should be rendered as a list.

            For example:

            - "Products not showing in ads"
            - "Products not showing organically".
    """

    class Region(proto.Message):
        r"""Region with code and localized name.

        Attributes:
            code (str):
                The [CLDR territory code]
                (http://www.unicode.org/repos/cldr/tags/latest/common/main/en.xml)
            name (str):
                The localized name of the region.
                For region with code='001' the value is 'All
                countries' or the equivalent in other languages.
        """

        code: str = proto.Field(
            proto.STRING,
            number=1,
        )
        name: str = proto.Field(
            proto.STRING,
            number=2,
        )

    regions: MutableSequence[Region] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=Region,
    )
    details: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )


class Action(proto.Message):
    r"""An actionable step that can be executed to solve the issue.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        builtin_simple_action (google.shopping.merchant_issueresolution_v1.types.BuiltInSimpleAction):
            Action implemented and performed in (your)
            third-party application. The application should
            point the business to the place, where they can
            access the corresponding functionality or
            provide instructions, if the specific
            functionality is not available.

            This field is a member of `oneof`_ ``action``.
        external_action (google.shopping.merchant_issueresolution_v1.types.ExternalAction):
            Action that is implemented and performed
            outside of (your) third-party application. The
            application needs to redirect the business to
            the external location where they can perform the
            action.

            This field is a member of `oneof`_ ``action``.
        builtin_user_input_action (google.shopping.merchant_issueresolution_v1.types.BuiltInUserInputAction):
            Action implemented and performed in (your)
            third-party application. The application needs
            to show an additional content and input form to
            the business as specified for given action. They
            can trigger the action only when they provided
            all required inputs.

            This field is a member of `oneof`_ ``action``.
        button_label (str):
            Label of the action button.
        is_available (bool):
            Controlling whether the button is active or disabled. The
            value is 'false' when the action was already requested or is
            not available. If the action is not available then a
            [reason][google.shopping.merchant.issueresolution.v1.Action.reasons]
            will be present. If (your) third-party application shows a
            disabled button for action that is not available, then it
            should also show reasons.
        reasons (MutableSequence[google.shopping.merchant_issueresolution_v1.types.Action.Reason]):
            List of reasons why the action is not
            available. The list of reasons is empty if the
            action is available. If there is only one
            reason, it can be displayed next to the disabled
            button. If there are more reasons, all of them
            should be displayed, for example in a pop-up
            dialog.
    """

    class Reason(proto.Message):
        r"""A single reason why the action is not available.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            message (str):
                Messages summarizing the reason, why the
                action is not available. For example: "Review
                requested on Jan 03. Review requests can take a
                few days to complete.".
            detail (str):
                Detailed explanation of the reason. Should be
                displayed as a hint if present.

                This field is a member of `oneof`_ ``_detail``.
            action (google.shopping.merchant_issueresolution_v1.types.Action):
                Optional. An action that needs to be
                performed to solve the problem represented by
                this reason. This action will always be
                available. Should be rendered as a link or
                button next to the summarizing message.

                For example, the review may be available only
                once the business configure all required
                attributes. In such a situation this action can
                be a link to the form, where they can fill the
                missing attribute to unblock the main action.

                This field is a member of `oneof`_ ``_action``.
        """

        message: str = proto.Field(
            proto.STRING,
            number=1,
        )
        detail: str = proto.Field(
            proto.STRING,
            number=2,
            optional=True,
        )
        action: "Action" = proto.Field(
            proto.MESSAGE,
            number=3,
            optional=True,
            message="Action",
        )

    builtin_simple_action: "BuiltInSimpleAction" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="action",
        message="BuiltInSimpleAction",
    )
    external_action: "ExternalAction" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="action",
        message="ExternalAction",
    )
    builtin_user_input_action: "BuiltInUserInputAction" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="action",
        message="BuiltInUserInputAction",
    )
    button_label: str = proto.Field(
        proto.STRING,
        number=4,
    )
    is_available: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    reasons: MutableSequence[Reason] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=Reason,
    )


class BuiltInSimpleAction(proto.Message):
    r"""Action that is implemented and performed in (your)
    third-party application. Represents various functionality that
    is expected to be available to business and will help them with
    resolving the issue. The application should point the business
    to the place, where they can access the corresponding
    functionality. If the functionality is not supported, it is
    recommended to explain the situation to the business and provide
    them with instructions how to solve the issue.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        type_ (google.shopping.merchant_issueresolution_v1.types.BuiltInSimpleAction.BuiltInSimpleActionType):
            The type of action that represents a
            functionality that is expected to be available
            in third-party application.
        attribute_code (str):
            The attribute that needs to be updated. Present when the
            [type][google.shopping.merchant.issueresolution.v1.BuiltInSimpleAction.type]
            is ``EDIT_ITEM_ATTRIBUTE``.

            This field contains a code for attribute, represented in
            snake_case. You can find a list of product's attributes,
            with their codes
            `here <https://support.google.com/merchants/answer/7052112>`__.

            This field is a member of `oneof`_ ``_attribute_code``.
        additional_content (google.shopping.merchant_issueresolution_v1.types.BuiltInSimpleAction.AdditionalContent):
            Long text from an external source that should be available
            to the business. Present when the
            [type][google.shopping.merchant.issueresolution.v1.BuiltInSimpleAction.type]
            is ``SHOW_ADDITIONAL_CONTENT``.

            This field is a member of `oneof`_ ``_additional_content``.
    """

    class BuiltInSimpleActionType(proto.Enum):
        r"""Enum specifying the type of action in third-party
        application.

        Values:
            BUILT_IN_SIMPLE_ACTION_TYPE_UNSPECIFIED (0):
                Default value. Will never be provided by the
                API.
            VERIFY_PHONE (1):
                Redirect the business to the part of your
                application where they can verify their phone.
            CLAIM_WEBSITE (2):
                Redirect the business to the part of your
                application where they can claim their website.
            ADD_PRODUCTS (3):
                Redirect the business to the part of your
                application where they can add products.
            ADD_CONTACT_INFO (4):
                Open a form where the business can edit their
                contact information.
            LINK_ADS_ACCOUNT (5):
                Redirect the business to the part of your
                application where they can link ads account.
            ADD_BUSINESS_REGISTRATION_NUMBER (6):
                Open a form where the business can add their
                business registration number.
            EDIT_ITEM_ATTRIBUTE (7):
                Open a form where the business can edit an attribute. The
                attribute that needs to be updated is specified in
                [attribute_code][google.shopping.merchant.issueresolution.v1.BuiltInSimpleAction.attribute_code]
                field of the action.
            FIX_ACCOUNT_ISSUE (8):
                Redirect the business from the product issues
                to the diagnostic page with their account issues
                in your application.

                This action will be returned only for product
                issues that are caused by an account issue and
                thus the business should resolve the problem on
                the account level.
            SHOW_ADDITIONAL_CONTENT (9):
                Show [additional
                content][google.shopping.merchant.issueresolution.v1.BuiltInSimpleAction.additional_content]
                to the business.

                This action will be used for example to deliver a
                justification from national authority.
        """

        BUILT_IN_SIMPLE_ACTION_TYPE_UNSPECIFIED = 0
        VERIFY_PHONE = 1
        CLAIM_WEBSITE = 2
        ADD_PRODUCTS = 3
        ADD_CONTACT_INFO = 4
        LINK_ADS_ACCOUNT = 5
        ADD_BUSINESS_REGISTRATION_NUMBER = 6
        EDIT_ITEM_ATTRIBUTE = 7
        FIX_ACCOUNT_ISSUE = 8
        SHOW_ADDITIONAL_CONTENT = 9

    class AdditionalContent(proto.Message):
        r"""Long text from external source.

        Attributes:
            title (str):
                Title of the additional content;
            paragraphs (MutableSequence[str]):
                Long text organized into paragraphs.
        """

        title: str = proto.Field(
            proto.STRING,
            number=1,
        )
        paragraphs: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )

    type_: BuiltInSimpleActionType = proto.Field(
        proto.ENUM,
        number=1,
        enum=BuiltInSimpleActionType,
    )
    attribute_code: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    additional_content: AdditionalContent = proto.Field(
        proto.MESSAGE,
        number=3,
        optional=True,
        message=AdditionalContent,
    )


class BuiltInUserInputAction(proto.Message):
    r"""Action that is implemented and performed in (your) third-party
    application. The application needs to show an additional content and
    input form to the business. They can start the action only when they
    provided all required inputs. The application will request
    processing of the action by calling the `triggeraction
    method <https://developers.google.com/merchant/api/reference/rest/issueresolution_v1/issueresolution/triggeraction>`__.

    Attributes:
        action_context (str):
            Contains the action's context that must be included as part
            of the
            [TriggerActionPayload.action_context][google.shopping.merchant.issueresolution.v1.TriggerActionPayload.action_context]
            in
            [TriggerActionRequest.payload][google.shopping.merchant.issueresolution.v1.TriggerActionRequest.payload]
            to call the ``triggeraction`` method. The content should be
            treated as opaque and must not be modified.
        flows (MutableSequence[google.shopping.merchant_issueresolution_v1.types.ActionFlow]):
            Actions may provide multiple different flows.
            Business selects one that fits best to their
            intent. Selecting the flow is the first step in
            user's interaction with the action. It affects
            what input fields will be available and required
            and also how the request will be processed.
    """

    action_context: str = proto.Field(
        proto.STRING,
        number=1,
    )
    flows: MutableSequence["ActionFlow"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="ActionFlow",
    )


class ActionFlow(proto.Message):
    r"""Flow that can be selected for an action. When a business
    selects a flow, application should open a dialog with more
    information and input form.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        id (str):
            Not for display but need to be sent back for
            the selected action flow.
        label (str):
            Text value describing the intent for the
            action flow. It can be used as an input label if
            business needs to pick one of multiple flows.
            For example:

            "I disagree with the issue".
        inputs (MutableSequence[google.shopping.merchant_issueresolution_v1.types.InputField]):
            A list of input fields.
        dialog_title (str):
            Title of the request dialog. For example:
            "Before you request a review".
        dialog_message (google.shopping.merchant_issueresolution_v1.types.TextWithTooltip):
            Message displayed in the request dialog. For
            example: "Make sure you've fixed all your
            country-specific issues. If not, you may have to
            wait 7 days to request another review". There
            may be an more information to be shown in a
            tooltip.

            This field is a member of `oneof`_ ``_dialog_message``.
        dialog_callout (google.shopping.merchant_issueresolution_v1.types.Callout):
            Important message to be highlighted in the
            request dialog. For example: "You can only
            request a review for disagreeing with this issue
            once. If it's not approved, you'll need to fix
            the issue and wait a few days before you can
            request another review.".

            This field is a member of `oneof`_ ``_dialog_callout``.
        dialog_button_label (str):
            Label for the button to trigger the action
            from the action dialog. For example: "Request
            review".
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    label: str = proto.Field(
        proto.STRING,
        number=2,
    )
    inputs: MutableSequence["InputField"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="InputField",
    )
    dialog_title: str = proto.Field(
        proto.STRING,
        number=4,
    )
    dialog_message: "TextWithTooltip" = proto.Field(
        proto.MESSAGE,
        number=7,
        optional=True,
        message="TextWithTooltip",
    )
    dialog_callout: "Callout" = proto.Field(
        proto.MESSAGE,
        number=8,
        optional=True,
        message="Callout",
    )
    dialog_button_label: str = proto.Field(
        proto.STRING,
        number=9,
    )


class InputField(proto.Message):
    r"""Input field that needs to be available to the business. If
    the field is marked as required, then a value needs to be
    provided for a successful processing of the request.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        text_input (google.shopping.merchant_issueresolution_v1.types.InputField.TextInput):
            Input field to provide text information. Corresponds to the
            `html input
            type=text <https://www.w3.org/TR/2012/WD-html-markup-20121025/input.text.html#input.text>`__
            or `html
            textarea <https://www.w3.org/TR/2012/WD-html-markup-20121025/textarea.html#textarea>`__.

            This field is a member of `oneof`_ ``value_input``.
        choice_input (google.shopping.merchant_issueresolution_v1.types.InputField.ChoiceInput):
            Input field to select one of the offered choices.
            Corresponds to the `html input
            type=radio <https://www.w3.org/TR/2012/WD-html-markup-20121025/input.radio.html#input.radio>`__.

            This field is a member of `oneof`_ ``value_input``.
        checkbox_input (google.shopping.merchant_issueresolution_v1.types.InputField.CheckboxInput):
            Input field to provide a boolean value. Corresponds to the
            `html input
            type=checkbox <https://www.w3.org/TR/2012/WD-html-markup-20121025/input.checkbox.html#input.checkbox>`__.

            This field is a member of `oneof`_ ``value_input``.
        id (str):
            Not for display but need to be sent back for
            the given input field.
        label (google.shopping.merchant_issueresolution_v1.types.TextWithTooltip):
            Input field label. There may be more
            information to be shown in a tooltip.
        required (bool):
            Whether the field is required. The action
            button needs to stay disabled till values for
            all required fields are provided.
    """

    class TextInput(proto.Message):
        r"""Text input allows the business to provide a text value.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            type_ (google.shopping.merchant_issueresolution_v1.types.InputField.TextInput.TextInputType):
                Type of the text input
            additional_info (google.shopping.merchant_issueresolution_v1.types.TextWithTooltip):
                Additional info regarding the field to be
                displayed to the business. For example, warning
                to not include personal identifiable
                information. There may be more information to be
                shown in a tooltip.

                This field is a member of `oneof`_ ``_additional_info``.
            format_info (str):
                Information about the required format. If
                present, it should be shown close to the input
                field to help the business to provide a correct
                value. For example: "VAT numbers should be in a
                format similar to SK9999999999".

                This field is a member of `oneof`_ ``_format_info``.
            aria_label (str):
                Text to be used as the
                `aria-label <https://www.w3.org/TR/WCAG20-TECHS/ARIA14.html>`__
                for the input.

                This field is a member of `oneof`_ ``_aria_label``.
        """

        class TextInputType(proto.Enum):
            r"""Enum specifying the type of the text input and how it should
            be rendered.

            Values:
                TEXT_INPUT_TYPE_UNSPECIFIED (0):
                    Default value. Will never be provided by the
                    API.
                GENERIC_SHORT_TEXT (1):
                    Used when a short text is expected. The field can be
                    rendered as a `text
                    field <https://www.w3.org/TR/2012/WD-html-markup-20121025/input.text.html#input.text>`__.
                GENERIC_LONG_TEXT (2):
                    Used when a longer text is expected. The field should be
                    rendered as a
                    `textarea <https://www.w3.org/TR/2012/WD-html-markup-20121025/textarea.html#textarea>`__.
            """

            TEXT_INPUT_TYPE_UNSPECIFIED = 0
            GENERIC_SHORT_TEXT = 1
            GENERIC_LONG_TEXT = 2

        type_: "InputField.TextInput.TextInputType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="InputField.TextInput.TextInputType",
        )
        additional_info: "TextWithTooltip" = proto.Field(
            proto.MESSAGE,
            number=2,
            optional=True,
            message="TextWithTooltip",
        )
        format_info: str = proto.Field(
            proto.STRING,
            number=3,
            optional=True,
        )
        aria_label: str = proto.Field(
            proto.STRING,
            number=4,
            optional=True,
        )

    class ChoiceInput(proto.Message):
        r"""Choice input allows the business to select one of the offered
        choices. Some choices may be linked to additional input fields
        that should be displayed under or next to the choice option. The
        value for the additional input field needs to be provided only
        when the specific choice is selected by the the business. For
        example, additional input field can be hidden or disabled until
        the business selects the specific choice.

        Attributes:
            options (MutableSequence[google.shopping.merchant_issueresolution_v1.types.InputField.ChoiceInput.ChoiceInputOption]):
                A list of choices. Only one option can be
                selected.
        """

        class ChoiceInputOption(proto.Message):
            r"""A choice that the business can select.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                id (str):
                    Not for display but need to be sent back for
                    the selected choice option.
                label (google.shopping.merchant_issueresolution_v1.types.TextWithTooltip):
                    Short description of the choice option. There
                    may be more information to be shown as a
                    tooltip.
                additional_input (google.shopping.merchant_issueresolution_v1.types.InputField):
                    Input that should be displayed when this option is selected.
                    The additional input will not contain a ``ChoiceInput``.

                    This field is a member of `oneof`_ ``_additional_input``.
            """

            id: str = proto.Field(
                proto.STRING,
                number=1,
            )
            label: "TextWithTooltip" = proto.Field(
                proto.MESSAGE,
                number=2,
                message="TextWithTooltip",
            )
            additional_input: "InputField" = proto.Field(
                proto.MESSAGE,
                number=3,
                optional=True,
                message="InputField",
            )

        options: MutableSequence["InputField.ChoiceInput.ChoiceInputOption"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message="InputField.ChoiceInput.ChoiceInputOption",
            )
        )

    class CheckboxInput(proto.Message):
        r"""Checkbox input allows the business to provide a boolean value.
        Corresponds to the `html input
        type=checkbox <https://www.w3.org/TR/2012/WD-html-markup-20121025/input.checkbox.html#input.checkbox>`__.

        If the business checks the box, the input value for the field is
        ``true``, otherwise it is ``false``.

        This type of input is often used as a confirmation that the business
        completed required steps before they are allowed to start the
        action. In such a case, the input field is marked as
        [required][google.shopping.merchant.issueresolution.v1.InputField.required]
        and the button to trigger the action should stay disabled until the
        business checks the box.

        """

    text_input: TextInput = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="value_input",
        message=TextInput,
    )
    choice_input: ChoiceInput = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="value_input",
        message=ChoiceInput,
    )
    checkbox_input: CheckboxInput = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="value_input",
        message=CheckboxInput,
    )
    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    label: "TextWithTooltip" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="TextWithTooltip",
    )
    required: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class TextWithTooltip(proto.Message):
    r"""Block of text that may contain a tooltip with more
    information.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        simple_value (str):
            Value of the message as a simple text.

            This field is a member of `oneof`_ ``value``.
        simple_tooltip_value (str):
            Value of the tooltip as a simple text.

            This field is a member of `oneof`_ ``tooltip_value``.
        tooltip_icon_style (google.shopping.merchant_issueresolution_v1.types.TextWithTooltip.TooltipIconStyle):
            The suggested type of an icon for tooltip, if
            a tooltip is present.
    """

    class TooltipIconStyle(proto.Enum):
        r"""Enum specifying the type of an icon that is being used to
        display a corresponding tooltip in the Merchant Center.

        Values:
            TOOLTIP_ICON_STYLE_UNSPECIFIED (0):
                Default value. Will never be provided by the
                API.
            INFO (1):
                Used when the tooltip adds additional
                information to the context, the 'i' can be used
                as an icon.
            QUESTION (2):
                Used when the tooltip shows helpful
                information, the '?' can be used as an icon.
        """

        TOOLTIP_ICON_STYLE_UNSPECIFIED = 0
        INFO = 1
        QUESTION = 2

    simple_value: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="value",
    )
    simple_tooltip_value: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="tooltip_value",
    )
    tooltip_icon_style: TooltipIconStyle = proto.Field(
        proto.ENUM,
        number=3,
        enum=TooltipIconStyle,
    )


class Callout(proto.Message):
    r"""An important message that should be highlighted. Usually
    displayed as a banner.

    Attributes:
        style_hint (google.shopping.merchant_issueresolution_v1.types.Callout.CalloutStyleHint):
            Can be used to render messages with different
            severity in different styles. Snippets off all
            types contain important information that should
            be displayed to the business.
        full_message (google.shopping.merchant_issueresolution_v1.types.TextWithTooltip):
            A full message that needs to be shown to the
            business.
    """

    class CalloutStyleHint(proto.Enum):
        r"""Enum specifying the suggested style, how the message should
        be rendered.

        Values:
            CALLOUT_STYLE_HINT_UNSPECIFIED (0):
                Default value. Will never be provided by the
                API.
            ERROR (1):
                The most important type of information
                highlighting problems, like an unsuccessful
                outcome of previously requested actions.
            WARNING (2):
                Information warning about pending problems,
                risks or deadlines.
            INFO (3):
                Default severity for important information
                like pending status of previously requested
                action or cooldown for re-review.
        """

        CALLOUT_STYLE_HINT_UNSPECIFIED = 0
        ERROR = 1
        WARNING = 2
        INFO = 3

    style_hint: CalloutStyleHint = proto.Field(
        proto.ENUM,
        number=1,
        enum=CalloutStyleHint,
    )
    full_message: "TextWithTooltip" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="TextWithTooltip",
    )


class ExternalAction(proto.Message):
    r"""Action that is implemented and performed outside of the
    third-party application. It should redirect the business to the
    provided URL of an external system where they can perform the
    action. For example to request a review in the Merchant Center.

    Attributes:
        type_ (google.shopping.merchant_issueresolution_v1.types.ExternalAction.ExternalActionType):
            The type of external action.
        uri (str):
            URL to external system, for example Merchant
            Center, where the business can perform the
            action.
    """

    class ExternalActionType(proto.Enum):
        r"""Enum specifying the type of action that requires to redirect
        the business to an external location.

        Values:
            EXTERNAL_ACTION_TYPE_UNSPECIFIED (0):
                Default value. Will never be provided by the
                API.
            REVIEW_PRODUCT_ISSUE_IN_MERCHANT_CENTER (1):
                Redirect to Merchant Center where the
                business can request a review for issue related
                to their product.
            REVIEW_ACCOUNT_ISSUE_IN_MERCHANT_CENTER (2):
                Redirect to Merchant Center where the
                business can request a review for issue related
                to their account.
            LEGAL_APPEAL_IN_HELP_CENTER (3):
                Redirect to the form in Help Center where the
                business can request a legal appeal for the
                issue.
            VERIFY_IDENTITY_IN_MERCHANT_CENTER (4):
                Redirect to Merchant Center where the
                business can perform identity verification.
        """

        EXTERNAL_ACTION_TYPE_UNSPECIFIED = 0
        REVIEW_PRODUCT_ISSUE_IN_MERCHANT_CENTER = 1
        REVIEW_ACCOUNT_ISSUE_IN_MERCHANT_CENTER = 2
        LEGAL_APPEAL_IN_HELP_CENTER = 3
        VERIFY_IDENTITY_IN_MERCHANT_CENTER = 4

    type_: ExternalActionType = proto.Field(
        proto.ENUM,
        number=1,
        enum=ExternalActionType,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=2,
    )


class TriggerActionRequest(proto.Message):
    r"""Request to start the selected action

    Attributes:
        name (str):
            Required. The business's account that is triggering the
            action. Format: ``accounts/{account}``
        payload (google.shopping.merchant_issueresolution_v1.types.TriggerActionPayload):
            Required. The payload for the triggered
            action.
        language_code (str):
            Optional. Language code `IETF BCP 47
            syntax <https://tools.ietf.org/html/bcp47>`__ used to
            localize the response. If not set, the result will be in
            default language ``en-US``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    payload: "TriggerActionPayload" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="TriggerActionPayload",
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=3,
    )


class TriggerActionPayload(proto.Message):
    r"""The payload for the triggered action.

    Attributes:
        action_context (str):
            Required. The
            [context][google.shopping.merchant.issueresolution.v1.BuiltInUserInputAction.action_context]
            from the selected action. The value is obtained from
            rendered issues and needs to be sent back to identify the
            [action][google.shopping.merchant.issueresolution.v1.Action.builtin_user_input_action]
            that is being triggered.
        action_input (google.shopping.merchant_issueresolution_v1.types.ActionInput):
            Required. Input provided by the business.
    """

    action_context: str = proto.Field(
        proto.STRING,
        number=1,
    )
    action_input: "ActionInput" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ActionInput",
    )


class TriggerActionResponse(proto.Message):
    r"""Response informing about the started action.

    Attributes:
        message (str):
            The message for the business.
    """

    message: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ActionInput(proto.Message):
    r"""Input provided by the business.

    Attributes:
        action_flow_id (str):
            Required.
            [Id][google.shopping.merchant.issueresolution.v1.ActionFlow.id]
            of the selected action flow.
        input_values (MutableSequence[google.shopping.merchant_issueresolution_v1.types.InputValue]):
            Required. Values for input fields.
    """

    action_flow_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    input_values: MutableSequence["InputValue"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="InputValue",
    )


class InputValue(proto.Message):
    r"""Input provided by the business for input field.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        text_input_value (google.shopping.merchant_issueresolution_v1.types.InputValue.TextInputValue):
            Value for [text
            input][google.shopping.merchant.issueresolution.v1.InputField.TextInput]
            field.

            This field is a member of `oneof`_ ``value``.
        choice_input_value (google.shopping.merchant_issueresolution_v1.types.InputValue.ChoiceInputValue):
            Value for [choice
            input][google.shopping.merchant.issueresolution.v1.InputField.ChoiceInput]
            field.

            This field is a member of `oneof`_ ``value``.
        checkbox_input_value (google.shopping.merchant_issueresolution_v1.types.InputValue.CheckboxInputValue):
            Value for [checkbox
            input][google.shopping.merchant.issueresolution.v1.InputField.CheckboxInput]
            field.

            This field is a member of `oneof`_ ``value``.
        input_field_id (str):
            Required.
            [Id][google.shopping.merchant.issueresolution.v1.InputField.id]
            of the corresponding input field.
    """

    class TextInputValue(proto.Message):
        r"""Value for [text
        input][google.shopping.merchant.issueresolution.v1.InputField.TextInput]
        field.

        Attributes:
            value (str):
                Required. Text provided by the business.
        """

        value: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class ChoiceInputValue(proto.Message):
        r"""Value for [choice
        input][google.shopping.merchant.issueresolution.v1.InputField.ChoiceInput]
        field.

        Attributes:
            choice_input_option_id (str):
                Required. [Id][InputField.ChoiceInput.id] of the option that
                was selected by the business.
        """

        choice_input_option_id: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class CheckboxInputValue(proto.Message):
        r"""Value for [checkbox
        input][google.shopping.merchant.issueresolution.v1.InputField.CheckboxInput]
        field.

        Attributes:
            value (bool):
                Required. True if the business checked the
                box field. False otherwise.
        """

        value: bool = proto.Field(
            proto.BOOL,
            number=1,
        )

    text_input_value: TextInputValue = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="value",
        message=TextInputValue,
    )
    choice_input_value: ChoiceInputValue = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="value",
        message=ChoiceInputValue,
    )
    checkbox_input_value: CheckboxInputValue = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="value",
        message=CheckboxInputValue,
    )
    input_field_id: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
