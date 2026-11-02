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
import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.recaptchaenterprise.v1",
    manifest={
        "ChallengeType",
        "CreateAssessmentRequest",
        "TransactionEvent",
        "PhoneAuthenticationEvent",
        "AnnotateAssessmentRequest",
        "AnnotateAssessmentResponse",
        "EndpointVerificationInfo",
        "AccountVerificationInfo",
        "PrivatePasswordLeakVerification",
        "Assessment",
        "Event",
        "TransactionData",
        "UserInfo",
        "UserId",
        "RiskAnalysis",
        "Bot",
        "TokenProperties",
        "FraudPreventionAssessment",
        "FraudSignals",
        "SmsTollFraudVerdict",
        "PhoneFraudAssessment",
        "AccountDefenderAssessment",
        "CreateKeyRequest",
        "ListKeysRequest",
        "ListKeysResponse",
        "RetrieveLegacySecretKeyRequest",
        "GetKeyRequest",
        "UpdateKeyRequest",
        "DeleteKeyRequest",
        "CreateFirewallPolicyRequest",
        "ListFirewallPoliciesRequest",
        "ListFirewallPoliciesResponse",
        "GetFirewallPolicyRequest",
        "UpdateFirewallPolicyRequest",
        "DeleteFirewallPolicyRequest",
        "ReorderFirewallPoliciesRequest",
        "ReorderFirewallPoliciesResponse",
        "MigrateKeyRequest",
        "GetMetricsRequest",
        "Metrics",
        "RetrieveLegacySecretKeyResponse",
        "Key",
        "TestingOptions",
        "WebKeySettings",
        "AndroidKeySettings",
        "IOSKeySettings",
        "ExpressKeySettings",
        "UniversalKeySettings",
        "AppleDeveloperId",
        "ScoreDistribution",
        "ScoreMetrics",
        "ChallengeMetrics",
        "FirewallPolicyAssessment",
        "FirewallAction",
        "FirewallPolicy",
        "ListRelatedAccountGroupMembershipsRequest",
        "ListRelatedAccountGroupMembershipsResponse",
        "ListRelatedAccountGroupsRequest",
        "ListRelatedAccountGroupsResponse",
        "SearchRelatedAccountGroupMembershipsRequest",
        "SearchRelatedAccountGroupMembershipsResponse",
        "AddIpOverrideRequest",
        "AddIpOverrideResponse",
        "RemoveIpOverrideRequest",
        "RemoveIpOverrideResponse",
        "ListIpOverridesRequest",
        "ListIpOverridesResponse",
        "RelatedAccountGroupMembership",
        "RelatedAccountGroup",
        "WafSettings",
        "AssessmentEnvironment",
        "PolicyEvaluation",
        "ChallengeRuleEvaluation",
        "IpOverrideData",
        "GetPolicyRequest",
        "UpdatePolicyRequest",
        "Policy",
        "ChallengeRuleGroup",
        "ChallengeRule",
        "ClientSettings",
        "ProtectedEndpointGroup",
        "ProtectedEndpoint",
    },
)


class ChallengeType(proto.Enum):
    r"""Enum of challenge types for Universal, ``POLICY_BASED_CHALLENGE``
    and ``INVISIBLE`` keys. Ensure that applications can handle values
    not explicitly listed.

    Values:
        CHALLENGE_TYPE_UNSPECIFIED (0):
            Default unspecified type.
        CHALLENGE_TYPE_VISUAL (1):
            A visual challenge.
        CHALLENGE_TYPE_AUDIO (2):
            An audio challenge.
    """

    CHALLENGE_TYPE_UNSPECIFIED = 0
    CHALLENGE_TYPE_VISUAL = 1
    CHALLENGE_TYPE_AUDIO = 2


class CreateAssessmentRequest(proto.Message):
    r"""The create assessment request message.

    Attributes:
        parent (str):
            Required. The name of the project in which the assessment is
            created, in the format ``projects/{project}``.
        assessment (google.cloud.recaptchaenterprise_v1.types.Assessment):
            Required. The assessment details.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    assessment: "Assessment" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Assessment",
    )


class TransactionEvent(proto.Message):
    r"""Describes an event in the lifecycle of a payment transaction.

    Attributes:
        event_type (google.cloud.recaptchaenterprise_v1.types.TransactionEvent.TransactionEventType):
            Optional. The type of this transaction event.
        reason (str):
            Optional. The reason or standardized code
            that corresponds with this transaction event, if
            one exists. For example, a CHARGEBACK event with
            code 6005.
        value (float):
            Optional. The value that corresponds with
            this transaction event, if one exists. For
            example, a refund event where $5.00 was
            refunded. Currency is obtained from the original
            transaction data.
        event_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. Timestamp when this transaction
            event occurred; otherwise assumed to be the time
            of the API call.
    """

    class TransactionEventType(proto.Enum):
        r"""Enum that represents an event in the payment transaction
        lifecycle. Ensure that applications can handle values not
        explicitly listed.

        Values:
            TRANSACTION_EVENT_TYPE_UNSPECIFIED (0):
                Default, unspecified event type.
            MERCHANT_APPROVE (1):
                Indicates that the transaction is approved by the merchant.
                The accompanying reasons can include terms such as
                'INHOUSE', 'ACCERTIFY', 'CYBERSOURCE', or 'MANUAL_REVIEW'.
            MERCHANT_DENY (2):
                Indicates that the transaction is denied and concluded due
                to risks detected by the merchant. The accompanying reasons
                can include terms such as 'INHOUSE', 'ACCERTIFY',
                'CYBERSOURCE', or 'MANUAL_REVIEW'.
            MANUAL_REVIEW (3):
                Indicates that the transaction is being
                evaluated by a human, due to suspicion or risk.
            AUTHORIZATION (4):
                Indicates that the authorization attempt with
                the card issuer succeeded.
            AUTHORIZATION_DECLINE (5):
                Indicates that the authorization attempt with
                the card issuer failed. The accompanying reasons
                can include Visa's '54' indicating that the card
                is expired, or '82' indicating that the CVV is
                incorrect.
            PAYMENT_CAPTURE (6):
                Indicates that the transaction is completed
                because the funds were settled.
            PAYMENT_CAPTURE_DECLINE (7):
                Indicates that the transaction could not be
                completed because the funds were not settled.
            CANCEL (8):
                Indicates that the transaction has been canceled. Specify
                the reason for the cancellation. For example,
                'INSUFFICIENT_INVENTORY'.
            CHARGEBACK_INQUIRY (9):
                Indicates that the merchant has received a
                chargeback inquiry due to fraud for the
                transaction, requesting additional information
                before a fraud chargeback is officially issued
                and a formal chargeback notification is sent.
            CHARGEBACK_ALERT (10):
                Indicates that the merchant has received a
                chargeback alert due to fraud for the
                transaction. The process of resolving the
                dispute without involving the payment network is
                started.
            FRAUD_NOTIFICATION (11):
                Indicates that a fraud notification is issued for the
                transaction, sent by the payment instrument's issuing bank
                because the transaction appears to be fraudulent. We
                recommend including TC40 or SAFE data in the ``reason``
                field for this event type. For partial chargebacks, we
                recommend that you include an amount in the ``value`` field.
            CHARGEBACK (12):
                Indicates that the merchant is informed by the payment
                network that the transaction has entered the chargeback
                process due to fraud. Reason code examples include
                Discover's '6005' and '6041'. For partial chargebacks, we
                recommend that you include an amount in the ``value`` field.
            CHARGEBACK_REPRESENTMENT (13):
                Indicates that the transaction has entered the chargeback
                process due to fraud, and that the merchant has chosen to
                enter representment. Reason examples include Discover's
                '6005' and '6041'. For partial chargebacks, we recommend
                that you include an amount in the ``value`` field.
            CHARGEBACK_REVERSE (14):
                Indicates that the transaction has had a fraud chargeback
                which was illegitimate and was reversed as a result. For
                partial chargebacks, we recommend that you include an amount
                in the ``value`` field.
            REFUND_REQUEST (15):
                Indicates that the merchant has received a refund for a
                completed transaction. For partial refunds, we recommend
                that you include an amount in the ``value`` field. Reason
                example: 'TAX_EXEMPT' (partial refund of exempt tax)
            REFUND_DECLINE (16):
                Indicates that the merchant has received a refund request
                for this transaction, but that they have declined it. For
                partial refunds, we recommend that you include an amount in
                the ``value`` field. Reason example: 'TAX_EXEMPT' (partial
                refund of exempt tax)
            REFUND (17):
                Indicates that the completed transaction was refunded by the
                merchant. For partial refunds, we recommend that you include
                an amount in the ``value`` field. Reason example:
                'TAX_EXEMPT' (partial refund of exempt tax)
            REFUND_REVERSE (18):
                Indicates that the completed transaction was refunded by the
                merchant, and that this refund was reversed. For partial
                refunds, we recommend that you include an amount in the
                ``value`` field.
        """

        TRANSACTION_EVENT_TYPE_UNSPECIFIED = 0
        MERCHANT_APPROVE = 1
        MERCHANT_DENY = 2
        MANUAL_REVIEW = 3
        AUTHORIZATION = 4
        AUTHORIZATION_DECLINE = 5
        PAYMENT_CAPTURE = 6
        PAYMENT_CAPTURE_DECLINE = 7
        CANCEL = 8
        CHARGEBACK_INQUIRY = 9
        CHARGEBACK_ALERT = 10
        FRAUD_NOTIFICATION = 11
        CHARGEBACK = 12
        CHARGEBACK_REPRESENTMENT = 13
        CHARGEBACK_REVERSE = 14
        REFUND_REQUEST = 15
        REFUND_DECLINE = 16
        REFUND = 17
        REFUND_REVERSE = 18

    event_type: TransactionEventType = proto.Field(
        proto.ENUM,
        number=1,
        enum=TransactionEventType,
    )
    reason: str = proto.Field(
        proto.STRING,
        number=2,
    )
    value: float = proto.Field(
        proto.DOUBLE,
        number=3,
    )
    event_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


class PhoneAuthenticationEvent(proto.Message):
    r"""Details on a phone authentication event

    Attributes:
        phone_number (str):
            Required. Phone number in E.164 format for
            which a multi-factor authentication challenge
            was initiated, succeeded, or failed.
        event_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The time at which the multi-factor
            authentication event (challenge or verification)
            occurred.
    """

    phone_number: str = proto.Field(
        proto.STRING,
        number=1,
    )
    event_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


class AnnotateAssessmentRequest(proto.Message):
    r"""The request message to annotate an Assessment.

    Attributes:
        name (str):
            Required. The resource name of the Assessment, in the format
            ``projects/{project}/assessments/{assessment}``.
        annotation (google.cloud.recaptchaenterprise_v1.types.AnnotateAssessmentRequest.Annotation):
            Optional. The annotation that is assigned to
            the Event. This field can be left empty to
            provide reasons that apply to an event without
            concluding whether the event is legitimate or
            fraudulent.
        reasons (MutableSequence[google.cloud.recaptchaenterprise_v1.types.AnnotateAssessmentRequest.Reason]):
            Optional. Reasons for the annotation that are
            assigned to the event.
        account_id (str):
            Optional. A stable account identifier to apply to the
            assessment. This is an alternative to setting ``account_id``
            in ``CreateAssessment``, for example when a stable account
            identifier is not yet known in the initial request.
        hashed_account_id (bytes):
            Optional. A stable hashed account identifier to apply to the
            assessment. This is an alternative to setting
            ``hashed_account_id`` in ``CreateAssessment``, for example
            when a stable account identifier is not yet known in the
            initial request.
        transaction_event (google.cloud.recaptchaenterprise_v1.types.TransactionEvent):
            Optional. If the assessment is part of a
            payment transaction, provide details on payment
            lifecycle events that occur in the transaction.
        phone_authentication_event (google.cloud.recaptchaenterprise_v1.types.PhoneAuthenticationEvent):
            Optional. If using an external multi-factor
            authentication provider, provide phone
            authentication details for fraud detection
            purposes.
    """

    class Annotation(proto.Enum):
        r"""Enum that represents the types of annotations.

        Values:
            ANNOTATION_UNSPECIFIED (0):
                Default unspecified type.
            LEGITIMATE (1):
                Provides information that the event turned
                out to be legitimate.
            FRAUDULENT (2):
                Provides information that the event turned
                out to be fraudulent.
            PASSWORD_CORRECT (3):
                Provides information that the event was related to a login
                event in which the user typed the correct password.
                Deprecated, prefer indicating CORRECT_PASSWORD through the
                reasons field instead.
            PASSWORD_INCORRECT (4):
                Provides information that the event was related to a login
                event in which the user typed the incorrect password.
                Deprecated, prefer indicating INCORRECT_PASSWORD through the
                reasons field instead.
        """

        ANNOTATION_UNSPECIFIED = 0
        LEGITIMATE = 1
        FRAUDULENT = 2
        PASSWORD_CORRECT = 3
        PASSWORD_INCORRECT = 4

    class Reason(proto.Enum):
        r"""Enum that represents potential reasons for annotating an
        assessment.

        Values:
            REASON_UNSPECIFIED (0):
                Unspecified reason. Do not use.
            CHARGEBACK (1):
                Indicates that the transaction had a chargeback issued with
                no other details. When possible, specify the type by using
                CHARGEBACK_FRAUD or CHARGEBACK_DISPUTE instead.
            CHARGEBACK_FRAUD (8):
                Indicates that the transaction had a
                chargeback issued related to an alleged
                unauthorized transaction from the cardholder's
                perspective (for example, the card number was
                stolen).
            CHARGEBACK_DISPUTE (9):
                Indicates that the transaction had a
                chargeback issued related to the cardholder
                having provided their card details but allegedly
                not being satisfied with the purchase (for
                example, misrepresentation, attempted
                cancellation).
            REFUND (10):
                Indicates that the completed payment
                transaction was refunded by the seller.
            REFUND_FRAUD (11):
                Indicates that the completed payment
                transaction was determined to be fraudulent by
                the seller, and was cancelled and refunded as a
                result.
            TRANSACTION_ACCEPTED (12):
                Indicates that the payment transaction was
                accepted, and the user was charged.
            TRANSACTION_DECLINED (13):
                Indicates that the payment transaction was
                declined, for example due to invalid card
                details.
            PAYMENT_HEURISTICS (2):
                Indicates the transaction associated with the
                assessment is suspected of being fraudulent
                based on the payment method, billing details,
                shipping address or other transaction
                information.
            INITIATED_TWO_FACTOR (7):
                Indicates that the user was served a 2FA challenge. An old
                assessment with ``ENUM_VALUES.INITIATED_TWO_FACTOR`` reason
                that has not been overwritten with ``PASSED_TWO_FACTOR`` is
                treated as an abandoned 2FA flow. This is equivalent to
                ``FAILED_TWO_FACTOR``.
            PASSED_TWO_FACTOR (3):
                Indicates that the user passed a 2FA
                challenge.
            FAILED_TWO_FACTOR (4):
                Indicates that the user failed a 2FA
                challenge.
            CORRECT_PASSWORD (5):
                Indicates the user provided the correct
                password.
            INCORRECT_PASSWORD (6):
                Indicates the user provided an incorrect
                password.
            SOCIAL_SPAM (14):
                Indicates that the user sent unwanted and
                abusive messages to other users of the platform,
                such as spam, scams, phishing, or social
                engineering.
        """

        REASON_UNSPECIFIED = 0
        CHARGEBACK = 1
        CHARGEBACK_FRAUD = 8
        CHARGEBACK_DISPUTE = 9
        REFUND = 10
        REFUND_FRAUD = 11
        TRANSACTION_ACCEPTED = 12
        TRANSACTION_DECLINED = 13
        PAYMENT_HEURISTICS = 2
        INITIATED_TWO_FACTOR = 7
        PASSED_TWO_FACTOR = 3
        FAILED_TWO_FACTOR = 4
        CORRECT_PASSWORD = 5
        INCORRECT_PASSWORD = 6
        SOCIAL_SPAM = 14

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    annotation: Annotation = proto.Field(
        proto.ENUM,
        number=2,
        enum=Annotation,
    )
    reasons: MutableSequence[Reason] = proto.RepeatedField(
        proto.ENUM,
        number=3,
        enum=Reason,
    )
    account_id: str = proto.Field(
        proto.STRING,
        number=7,
    )
    hashed_account_id: bytes = proto.Field(
        proto.BYTES,
        number=4,
    )
    transaction_event: "TransactionEvent" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="TransactionEvent",
    )
    phone_authentication_event: "PhoneAuthenticationEvent" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="PhoneAuthenticationEvent",
    )


class AnnotateAssessmentResponse(proto.Message):
    r"""Empty response for AnnotateAssessment."""


class EndpointVerificationInfo(proto.Message):
    r"""Information about a verification endpoint that can be used
    for 2FA.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        email_address (str):
            Email address for which to trigger a
            verification request.

            This field is a member of `oneof`_ ``endpoint``.
        phone_number (str):
            Phone number for which to trigger a
            verification request. Should be given in E.164
            format.

            This field is a member of `oneof`_ ``endpoint``.
        request_token (str):
            Output only. Token to provide to the client
            to trigger endpoint verification. It must be
            used within 15 minutes.
        last_verification_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp of the last successful
            verification for the endpoint, if any.
    """

    email_address: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="endpoint",
    )
    phone_number: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="endpoint",
    )
    request_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    last_verification_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


class AccountVerificationInfo(proto.Message):
    r"""Information about account verification, used for identity
    verification.

    Attributes:
        endpoints (MutableSequence[google.cloud.recaptchaenterprise_v1.types.EndpointVerificationInfo]):
            Optional. Endpoints that can be used for
            identity verification.
        language_code (str):
            Optional. Language code preference for the
            verification message, set as a IETF BCP 47
            language code.
        latest_verification_result (google.cloud.recaptchaenterprise_v1.types.AccountVerificationInfo.Result):
            Output only. Result of the latest account
            verification challenge.
        username (str):
            Username of the account that is being verified. Deprecated.
            Customers should now provide the ``account_id`` field in
            ``event.user_info``.
    """

    class Result(proto.Enum):
        r"""Result of the account verification as contained in the
        verdict token issued at the end of the verification flow. Ensure
        that applications can handle values not explicitly listed.

        Values:
            RESULT_UNSPECIFIED (0):
                No information about the latest account
                verification.
            SUCCESS_USER_VERIFIED (1):
                The user was successfully verified. This
                means the account verification challenge was
                successfully completed.
            ERROR_USER_NOT_VERIFIED (2):
                The user failed the verification challenge.
            ERROR_SITE_ONBOARDING_INCOMPLETE (3):
                The site is not properly onboarded to use the
                account verification feature.
            ERROR_RECIPIENT_NOT_ALLOWED (4):
                The recipient is not allowed for account
                verification. This can occur during integration
                but should not occur in production.
            ERROR_RECIPIENT_ABUSE_LIMIT_EXHAUSTED (5):
                The recipient has already been sent too many
                verification codes in a short amount of time.
            ERROR_CRITICAL_INTERNAL (6):
                The verification flow could not be completed
                due to a critical internal error.
            ERROR_CUSTOMER_QUOTA_EXHAUSTED (7):
                The client has exceeded their two factor
                request quota for this period of time.
            ERROR_VERIFICATION_BYPASSED (8):
                The request cannot be processed at the time
                because of an incident. This bypass can be
                restricted to a problematic destination email
                domain, a customer, or could affect the entire
                service.
            ERROR_VERDICT_MISMATCH (9):
                The request parameters do not match with the
                token provided and cannot be processed.
        """

        RESULT_UNSPECIFIED = 0
        SUCCESS_USER_VERIFIED = 1
        ERROR_USER_NOT_VERIFIED = 2
        ERROR_SITE_ONBOARDING_INCOMPLETE = 3
        ERROR_RECIPIENT_NOT_ALLOWED = 4
        ERROR_RECIPIENT_ABUSE_LIMIT_EXHAUSTED = 5
        ERROR_CRITICAL_INTERNAL = 6
        ERROR_CUSTOMER_QUOTA_EXHAUSTED = 7
        ERROR_VERIFICATION_BYPASSED = 8
        ERROR_VERDICT_MISMATCH = 9

    endpoints: MutableSequence["EndpointVerificationInfo"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="EndpointVerificationInfo",
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=3,
    )
    latest_verification_result: Result = proto.Field(
        proto.ENUM,
        number=7,
        enum=Result,
    )
    username: str = proto.Field(
        proto.STRING,
        number=2,
    )


class PrivatePasswordLeakVerification(proto.Message):
    r"""Private password leak verification info.

    Attributes:
        lookup_hash_prefix (bytes):
            Required. Exactly 26-bit prefix of the
            SHA-256 hash of the canonicalized username. It
            is used to look up password leaks associated
            with that hash prefix.
        encrypted_user_credentials_hash (bytes):
            Optional. Encrypted Scrypt hash of the canonicalized
            username+password. It is re-encrypted by the server and
            returned through ``reencrypted_user_credentials_hash``.
        encrypted_leak_match_prefixes (MutableSequence[bytes]):
            Output only. List of prefixes of the encrypted potential
            password leaks that matched the given parameters. They must
            be compared with the client-side decryption prefix of
            ``reencrypted_user_credentials_hash``
        reencrypted_user_credentials_hash (bytes):
            Output only. Corresponds to the re-encryption of the
            ``encrypted_user_credentials_hash`` field. It is used to
            match potential password leaks within
            ``encrypted_leak_match_prefixes``.
    """

    lookup_hash_prefix: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )
    encrypted_user_credentials_hash: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )
    encrypted_leak_match_prefixes: MutableSequence[bytes] = proto.RepeatedField(
        proto.BYTES,
        number=3,
    )
    reencrypted_user_credentials_hash: bytes = proto.Field(
        proto.BYTES,
        number=4,
    )


class Assessment(proto.Message):
    r"""A reCAPTCHA Enterprise assessment resource.

    Attributes:
        name (str):
            Output only. Identifier. The resource name for the
            Assessment in the format
            ``projects/{project}/assessments/{assessment}``.
        event (google.cloud.recaptchaenterprise_v1.types.Event):
            Optional. The event being assessed.
        risk_analysis (google.cloud.recaptchaenterprise_v1.types.RiskAnalysis):
            Output only. The risk analysis result for the
            event being assessed.
        token_properties (google.cloud.recaptchaenterprise_v1.types.TokenProperties):
            Output only. Properties of the provided event
            token.
        account_verification (google.cloud.recaptchaenterprise_v1.types.AccountVerificationInfo):
            Optional. Account verification information
            for identity verification. The assessment event
            must include a token and site key to use this
            feature.
        account_defender_assessment (google.cloud.recaptchaenterprise_v1.types.AccountDefenderAssessment):
            Output only. Assessment returned by Account
            defense when an account identifier is provided.
        private_password_leak_verification (google.cloud.recaptchaenterprise_v1.types.PrivatePasswordLeakVerification):
            Optional. The private password leak
            verification field contains the parameters that
            are used to to check for leaks privately without
            sharing user credentials.
        firewall_policy_assessment (google.cloud.recaptchaenterprise_v1.types.FirewallPolicyAssessment):
            Output only. Assessment returned when firewall policies
            belonging to the project are evaluated using the field
            firewall_policy_evaluation.
        fraud_prevention_assessment (google.cloud.recaptchaenterprise_v1.types.FraudPreventionAssessment):
            Output only. Assessment returned by Fraud
            Prevention when TransactionData is provided.
        fraud_signals (google.cloud.recaptchaenterprise_v1.types.FraudSignals):
            Output only. Fraud Signals specific to the
            users involved in a payment transaction.
        phone_fraud_assessment (google.cloud.recaptchaenterprise_v1.types.PhoneFraudAssessment):
            Output only. Assessment returned when a site key, a token,
            and a phone number as ``user_id`` are provided. SMS defense
            needs to be enabled.
        assessment_environment (google.cloud.recaptchaenterprise_v1.types.AssessmentEnvironment):
            Optional. The environment creating the
            assessment. This describes your environment (the
            system invoking CreateAssessment), NOT the
            environment of your user.
        policy_evaluation (google.cloud.recaptchaenterprise_v1.types.PolicyEvaluation):
            Output only. Provides information about the
            policy evaluation for this assessment.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    event: "Event" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Event",
    )
    risk_analysis: "RiskAnalysis" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="RiskAnalysis",
    )
    token_properties: "TokenProperties" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="TokenProperties",
    )
    account_verification: "AccountVerificationInfo" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="AccountVerificationInfo",
    )
    account_defender_assessment: "AccountDefenderAssessment" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="AccountDefenderAssessment",
    )
    private_password_leak_verification: "PrivatePasswordLeakVerification" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="PrivatePasswordLeakVerification",
    )
    firewall_policy_assessment: "FirewallPolicyAssessment" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="FirewallPolicyAssessment",
    )
    fraud_prevention_assessment: "FraudPreventionAssessment" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="FraudPreventionAssessment",
    )
    fraud_signals: "FraudSignals" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="FraudSignals",
    )
    phone_fraud_assessment: "PhoneFraudAssessment" = proto.Field(
        proto.MESSAGE,
        number=12,
        message="PhoneFraudAssessment",
    )
    assessment_environment: "AssessmentEnvironment" = proto.Field(
        proto.MESSAGE,
        number=14,
        message="AssessmentEnvironment",
    )
    policy_evaluation: "PolicyEvaluation" = proto.Field(
        proto.MESSAGE,
        number=16,
        message="PolicyEvaluation",
    )


class Event(proto.Message):
    r"""The event being assessed.

    Attributes:
        token (str):
            Optional. The user response token provided by
            the reCAPTCHA Enterprise client-side integration
            on your site.
        site_key (str):
            Optional. The site key that was used to
            invoke reCAPTCHA Enterprise on your site and
            generate the token.
        user_agent (str):
            Optional. The user agent present in the
            request from the user's device related to this
            event.
        user_ip_address (str):
            Optional. The IP address in the request from
            the user's device related to this event.
        expected_action (str):
            Optional. The expected action for this type
            of event. This should be the same action
            provided at token generation time on client-side
            platforms already integrated with recaptcha
            enterprise. Required for Universal keys.
        hashed_account_id (bytes):
            Optional. Deprecated: use ``user_info.account_id`` instead.
            Unique stable hashed user identifier for the request. The
            identifier must be hashed using hmac-sha256 with stable
            secret.
        express (bool):
            Optional. Flag for a reCAPTCHA express request for an
            assessment without a token. If enabled, ``site_key`` must
            reference an Express site key.
        requested_uri (str):
            Optional. The URI resource the user requested
            that triggered an assessment.
        waf_token_assessment (bool):
            Optional. Flag for running Web Application
            Firewall (WAF) token assessment. If enabled, the
            token must be specified, and have been created
            by a WAF-enabled key.
        ja3 (str):
            Optional. JA3 fingerprint for SSL clients. To
            learn how to compute this fingerprint, please
            refer to https://github.com/salesforce/ja3.
        ja4 (str):
            Optional. JA4 fingerprint for SSL clients. To
            learn how to compute this fingerprint, please
            refer to https://github.com/FoxIO-LLC/ja4.
        headers (MutableSequence[str]):
            Optional. HTTP header information about the
            request.
        firewall_policy_evaluation (bool):
            Optional. Flag for enabling firewall policy
            config assessment. If this flag is enabled, the
            firewall policy is evaluated and a suggested
            firewall action is returned in the response.
        transaction_data (google.cloud.recaptchaenterprise_v1.types.TransactionData):
            Optional. Data describing a payment
            transaction to be assessed. Sending this data
            enables reCAPTCHA Enterprise Fraud Prevention
            and the FraudPreventionAssessment component in
            the response.
        user_info (google.cloud.recaptchaenterprise_v1.types.UserInfo):
            Optional. Information about the user that
            generates this event, when they can be
            identified. They are often identified through
            the use of an account for logged-in requests or
            login/registration requests, or by providing
            user identifiers for guest actions like
            checkout.
        fraud_prevention (google.cloud.recaptchaenterprise_v1.types.Event.FraudPrevention):
            Optional. The Fraud Prevention setting for
            this assessment.
    """

    class FraudPrevention(proto.Enum):
        r"""Setting that controls Fraud Prevention assessments.
        Ensure that applications can handle values not explicitly
        listed.

        Values:
            FRAUD_PREVENTION_UNSPECIFIED (0):
                Default, unspecified setting.
                ``fraud_prevention_assessment`` is returned if
                ``transaction_data`` is present in ``Event`` and Fraud
                Prevention is enabled in the Google Cloud console.
            ENABLED (1):
                Enable Fraud Prevention for this assessment,
                if Fraud Prevention is enabled in the Google
                Cloud console.
            DISABLED (2):
                Disable Fraud Prevention for this assessment,
                regardless of the Google Cloud console settings.
        """

        FRAUD_PREVENTION_UNSPECIFIED = 0
        ENABLED = 1
        DISABLED = 2

    token: str = proto.Field(
        proto.STRING,
        number=1,
    )
    site_key: str = proto.Field(
        proto.STRING,
        number=2,
    )
    user_agent: str = proto.Field(
        proto.STRING,
        number=3,
    )
    user_ip_address: str = proto.Field(
        proto.STRING,
        number=4,
    )
    expected_action: str = proto.Field(
        proto.STRING,
        number=5,
    )
    hashed_account_id: bytes = proto.Field(
        proto.BYTES,
        number=6,
    )
    express: bool = proto.Field(
        proto.BOOL,
        number=14,
    )
    requested_uri: str = proto.Field(
        proto.STRING,
        number=8,
    )
    waf_token_assessment: bool = proto.Field(
        proto.BOOL,
        number=9,
    )
    ja3: str = proto.Field(
        proto.STRING,
        number=10,
    )
    ja4: str = proto.Field(
        proto.STRING,
        number=18,
    )
    headers: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=11,
    )
    firewall_policy_evaluation: bool = proto.Field(
        proto.BOOL,
        number=12,
    )
    transaction_data: "TransactionData" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="TransactionData",
    )
    user_info: "UserInfo" = proto.Field(
        proto.MESSAGE,
        number=15,
        message="UserInfo",
    )
    fraud_prevention: FraudPrevention = proto.Field(
        proto.ENUM,
        number=17,
        enum=FraudPrevention,
    )


class TransactionData(proto.Message):
    r"""Transaction data associated with a payment protected by
    reCAPTCHA Enterprise.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        transaction_id (str):
            Unique identifier for the transaction. This
            custom identifier can be used to reference this
            transaction in the future, for example, labeling
            a refund or chargeback event. Two attempts at
            the same transaction should use the same
            transaction id.

            This field is a member of `oneof`_ ``_transaction_id``.
        payment_method (str):
            Optional. The payment method for the transaction. The
            allowed values are:

            - credit-card
            - debit-card
            - gift-card
            - processor-{name} (If a third-party is used, for example,
              processor-paypal)
            - custom-{name} (If an alternative method is used, for
              example, custom-crypto)
        card_bin (str):
            Optional. The Bank Identification Number -
            generally the first 6 or 8 digits of the card.
        card_last_four (str):
            Optional. The last four digits of the card.
        currency_code (str):
            Optional. The currency code in ISO-4217
            format.
        value (float):
            Optional. The decimal value of the
            transaction in the specified currency.
        shipping_value (float):
            Optional. The value of shipping in the
            specified currency. 0 for free or no shipping.
        shipping_address (google.cloud.recaptchaenterprise_v1.types.TransactionData.Address):
            Optional. Destination address if this
            transaction involves shipping a physical item.
        billing_address (google.cloud.recaptchaenterprise_v1.types.TransactionData.Address):
            Optional. Address associated with the payment
            method when applicable.
        user (google.cloud.recaptchaenterprise_v1.types.TransactionData.User):
            Optional. Information about the user
            paying/initiating the transaction.
        merchants (MutableSequence[google.cloud.recaptchaenterprise_v1.types.TransactionData.User]):
            Optional. Information about the user or users
            fulfilling the transaction.
        items (MutableSequence[google.cloud.recaptchaenterprise_v1.types.TransactionData.Item]):
            Optional. Items purchased in this
            transaction.
        gateway_info (google.cloud.recaptchaenterprise_v1.types.TransactionData.GatewayInfo):
            Optional. Information about the payment
            gateway's response to the transaction.
    """

    class Address(proto.Message):
        r"""Structured address format for billing and shipping addresses.

        Attributes:
            recipient (str):
                Optional. The recipient name, potentially
                including information such as "care of".
            address (MutableSequence[str]):
                Optional. The first lines of the address. The
                first line generally contains the street name
                and number, and further lines may include
                information such as an apartment number.
            locality (str):
                Optional. The town/city of the address.
            administrative_area (str):
                Optional. The state, province, or otherwise
                administrative area of the address.
            region_code (str):
                Optional. The CLDR country/region of the
                address.
            postal_code (str):
                Optional. The postal or ZIP code of the
                address.
        """

        recipient: str = proto.Field(
            proto.STRING,
            number=1,
        )
        address: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )
        locality: str = proto.Field(
            proto.STRING,
            number=3,
        )
        administrative_area: str = proto.Field(
            proto.STRING,
            number=4,
        )
        region_code: str = proto.Field(
            proto.STRING,
            number=5,
        )
        postal_code: str = proto.Field(
            proto.STRING,
            number=6,
        )

    class User(proto.Message):
        r"""Details about a user's account involved in the transaction.

        Attributes:
            account_id (str):
                Optional. Unique account identifier for this user. If using
                Account defense, this should match the hashed_account_id
                field. Otherwise, a unique and persistent identifier for
                this account.
            creation_ms (int):
                Optional. The epoch milliseconds of the
                user's account creation.
            email (str):
                Optional. The email address of the user.
            email_verified (bool):
                Optional. Whether the email has been verified
                to be accessible by the user (OTP or similar).
            phone_number (str):
                Optional. The phone number of the user, with
                country code.
            phone_verified (bool):
                Optional. Whether the phone number has been
                verified to be accessible by the user (OTP or
                similar).
        """

        account_id: str = proto.Field(
            proto.STRING,
            number=6,
        )
        creation_ms: int = proto.Field(
            proto.INT64,
            number=1,
        )
        email: str = proto.Field(
            proto.STRING,
            number=2,
        )
        email_verified: bool = proto.Field(
            proto.BOOL,
            number=3,
        )
        phone_number: str = proto.Field(
            proto.STRING,
            number=4,
        )
        phone_verified: bool = proto.Field(
            proto.BOOL,
            number=5,
        )

    class Item(proto.Message):
        r"""Line items being purchased in this transaction.

        Attributes:
            name (str):
                Optional. The full name of the item.
            value (float):
                Optional. The value per item that the user is
                paying, in the transaction currency, after
                discounts.
            quantity (int):
                Optional. The quantity of this item that is
                being purchased.
            merchant_account_id (str):
                Optional. When a merchant is specified, its corresponding
                account_id. Necessary to populate marketplace-style
                transactions.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        value: float = proto.Field(
            proto.DOUBLE,
            number=2,
        )
        quantity: int = proto.Field(
            proto.INT64,
            number=3,
        )
        merchant_account_id: str = proto.Field(
            proto.STRING,
            number=4,
        )

    class GatewayInfo(proto.Message):
        r"""Details about the transaction from the gateway.

        Attributes:
            name (str):
                Optional. Name of the gateway service (for
                example, stripe, square, paypal).
            gateway_response_code (str):
                Optional. Gateway response code describing
                the state of the transaction.
            avs_response_code (str):
                Optional. AVS response code from the gateway
                (available only when reCAPTCHA Enterprise is
                called after authorization).
            cvv_response_code (str):
                Optional. CVV response code from the gateway
                (available only when reCAPTCHA Enterprise is
                called after authorization).
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        gateway_response_code: str = proto.Field(
            proto.STRING,
            number=2,
        )
        avs_response_code: str = proto.Field(
            proto.STRING,
            number=3,
        )
        cvv_response_code: str = proto.Field(
            proto.STRING,
            number=4,
        )

    transaction_id: str = proto.Field(
        proto.STRING,
        number=11,
        optional=True,
    )
    payment_method: str = proto.Field(
        proto.STRING,
        number=1,
    )
    card_bin: str = proto.Field(
        proto.STRING,
        number=2,
    )
    card_last_four: str = proto.Field(
        proto.STRING,
        number=3,
    )
    currency_code: str = proto.Field(
        proto.STRING,
        number=4,
    )
    value: float = proto.Field(
        proto.DOUBLE,
        number=5,
    )
    shipping_value: float = proto.Field(
        proto.DOUBLE,
        number=12,
    )
    shipping_address: Address = proto.Field(
        proto.MESSAGE,
        number=6,
        message=Address,
    )
    billing_address: Address = proto.Field(
        proto.MESSAGE,
        number=7,
        message=Address,
    )
    user: User = proto.Field(
        proto.MESSAGE,
        number=8,
        message=User,
    )
    merchants: MutableSequence[User] = proto.RepeatedField(
        proto.MESSAGE,
        number=13,
        message=User,
    )
    items: MutableSequence[Item] = proto.RepeatedField(
        proto.MESSAGE,
        number=14,
        message=Item,
    )
    gateway_info: GatewayInfo = proto.Field(
        proto.MESSAGE,
        number=10,
        message=GatewayInfo,
    )


class UserInfo(proto.Message):
    r"""User information associated with a request protected by
    reCAPTCHA Enterprise.

    Attributes:
        create_account_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. Creation time for this account
            associated with this user. Leave blank for non
            logged-in actions, guest checkout, or when there
            is no account associated with the current user.
        account_id (str):
            Optional. For logged-in requests or
            login/registration requests, the unique account
            identifier associated with this user. You can
            use the username if it is stable (meaning it is
            the same for every request associated with the
            same user), or any stable user ID of your
            choice. Leave blank for non logged-in actions or
            guest checkout.
        user_ids (MutableSequence[google.cloud.recaptchaenterprise_v1.types.UserId]):
            Optional. Identifiers associated with this
            user or request.
    """

    create_account_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    account_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    user_ids: MutableSequence["UserId"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="UserId",
    )


class UserId(proto.Message):
    r"""An identifier associated with a user.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        email (str):
            Optional. An email address.

            This field is a member of `oneof`_ ``id_oneof``.
        phone_number (str):
            Optional. A phone number. Should use the
            E.164 format.

            This field is a member of `oneof`_ ``id_oneof``.
        username (str):
            Optional. A unique username, if different from all the other
            identifiers and ``account_id`` that are provided. Can be a
            unique login handle or display name for a user.

            This field is a member of `oneof`_ ``id_oneof``.
    """

    email: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="id_oneof",
    )
    phone_number: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="id_oneof",
    )
    username: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="id_oneof",
    )


class RiskAnalysis(proto.Message):
    r"""Risk analysis result for an event.

    Attributes:
        score (float):
            Output only. Legitimate event score from 0.0
            to 1.0. (1.0 means very likely legitimate
            traffic while 0.0 means very likely
            non-legitimate traffic).
        reasons (MutableSequence[google.cloud.recaptchaenterprise_v1.types.RiskAnalysis.ClassificationReason]):
            Output only. Reasons contributing to the risk
            analysis verdict.
        extended_verdict_reasons (MutableSequence[str]):
            Output only. Additional reasons contributing
            to the risk analysis verdict. These reasons are
            available to Enterprise tier projects only.
            Contact sales for more information.
            The set of reasons is subject to change.
        last_challenge_type (google.cloud.recaptchaenterprise_v1.types.ChallengeType):
            Output only. Type of the last challenge presented to the
            user for Universal, ``POLICY_BASED_CHALLENGE`` and
            ``INVISIBLE`` keys. The field is only set when a challenge
            was presented to the user.
        challenge (google.cloud.recaptchaenterprise_v1.types.RiskAnalysis.Challenge):
            Output only. Challenge information for Universal,
            ``POLICY_BASED_CHALLENGE`` and ``INVISIBLE`` keys.
        verified_bots (MutableSequence[google.cloud.recaptchaenterprise_v1.types.Bot]):
            Output only. Bots with identities that have
            been verified by reCAPTCHA and detected in the
            event.
    """

    class ClassificationReason(proto.Enum):
        r"""Reasons contributing to the risk analysis verdict.
        Ensure that applications can handle values not explicitly
        listed.

        Values:
            CLASSIFICATION_REASON_UNSPECIFIED (0):
                Default unspecified type.
            AUTOMATION (1):
                Interactions matched the behavior of an
                automated agent.
            UNEXPECTED_ENVIRONMENT (2):
                The event originated from an illegitimate
                environment.
            TOO_MUCH_TRAFFIC (3):
                Traffic volume from the event source is
                higher than normal.
            UNEXPECTED_USAGE_PATTERNS (4):
                Interactions with the site were significantly
                different than expected patterns.
            LOW_CONFIDENCE_SCORE (5):
                Too little traffic has been received from
                this site thus far to generate quality risk
                analysis.
            SUSPECTED_CARDING (6):
                Deprecated: Use
                [FraudPreventionAssessment.transaction_risk][google.cloud.recaptchaenterprise.v1.FraudPreventionAssessment.transaction_risk]
                and
                [FraudPreventionAssessment.RiskReason.Reason.EXCESSIVE_ENUMERATION_PATTERN][google.cloud.recaptchaenterprise.v1.FraudPreventionAssessment.RiskReason.Reason.EXCESSIVE_ENUMERATION_PATTERN]
                instead.
            SUSPECTED_CHARGEBACK (7):
                Deprecated: Use
                [FraudPreventionAssessment.transaction_risk][google.cloud.recaptchaenterprise.v1.FraudPreventionAssessment.transaction_risk]
                and
                [FraudPreventionAssessment.RiskReason.Reason.ASSOCIATED_WITH_FRAUD_CLUSTER][google.cloud.recaptchaenterprise.v1.FraudPreventionAssessment.RiskReason.Reason.ASSOCIATED_WITH_FRAUD_CLUSTER]
                instead.
        """

        CLASSIFICATION_REASON_UNSPECIFIED = 0
        AUTOMATION = 1
        UNEXPECTED_ENVIRONMENT = 2
        TOO_MUCH_TRAFFIC = 3
        UNEXPECTED_USAGE_PATTERNS = 4
        LOW_CONFIDENCE_SCORE = 5
        SUSPECTED_CARDING = 6
        SUSPECTED_CHARGEBACK = 7

    class Challenge(proto.Enum):
        r"""Challenge information for Universal, ``POLICY_BASED_CHALLENGE`` and
        ``INVISIBLE`` keys. Ensure that applications can handle values not
        explicitly listed.

        Values:
            CHALLENGE_UNSPECIFIED (0):
                Default unspecified type.
            NOCAPTCHA (1):
                No challenge was presented for solving.
            PASSED (2):
                A solution was submitted that was correct.
            FAILED (3):
                A solution was submitted that was incorrect
                or otherwise deemed suspicious.
        """

        CHALLENGE_UNSPECIFIED = 0
        NOCAPTCHA = 1
        PASSED = 2
        FAILED = 3

    score: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    reasons: MutableSequence[ClassificationReason] = proto.RepeatedField(
        proto.ENUM,
        number=2,
        enum=ClassificationReason,
    )
    extended_verdict_reasons: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    last_challenge_type: "ChallengeType" = proto.Field(
        proto.ENUM,
        number=6,
        enum="ChallengeType",
    )
    challenge: Challenge = proto.Field(
        proto.ENUM,
        number=4,
        enum=Challenge,
    )
    verified_bots: MutableSequence["Bot"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="Bot",
    )


class Bot(proto.Message):
    r"""Bot information and metadata.

    Attributes:
        name (str):
            Optional. Enumerated string value that indicates the
            identity of the bot, formatted in kebab-case. Current
            example values include the following:

            - google-agent - AI_AGENT
            - browser-base - AI_AGENT
            - chat-gpt - AI_AGENT
            - aws-bedrock - AI_AGENT
            - cybaa-bot - AI_AGENT
            - cloudflare - AI_AGENT
            - payhawk - AI_AGENT
            - duck-duck-go - SEARCH_INDEXER
            - mediaboard - CONTENT_SCRAPER
            - marker-io - AI_AGENT
            - broadcom - AI_AGENT
            - anchor-browser - AI_AGENT
            - shopify - AI_AGENT
            - stackscope - CONTENT_SCRAPER
            - manus - AI_AGENT
            - kernel-sh - AI_AGENT
            - zvelo - SEARCH_INDEXER

            Ensure that your applications can handle identifier values
            not explicitly listed here. Deprecated values might take
            some time to stop showing up in responses. New values can be
            pushed so this list should be taken as non exhaustive.
        bot_type (google.cloud.recaptchaenterprise_v1.types.Bot.BotType):
            Optional. Enumerated field representing the
            type of bot.
    """

    class BotType(proto.Enum):
        r"""Types of bots.
        Ensure that applications can handle values not explicitly
        listed.

        Values:
            BOT_TYPE_UNSPECIFIED (0):
                Default unspecified type.
            AI_AGENT (1):
                Software program that interacts with a site
                and performs tasks autonomously.
            CONTENT_SCRAPER (2):
                Software that extracts specific data from
                sites for use.
            SEARCH_INDEXER (3):
                Software that crawls sites and stores content
                for the purpose of efficient retrieval, likely
                as part of a search engine.
        """

        BOT_TYPE_UNSPECIFIED = 0
        AI_AGENT = 1
        CONTENT_SCRAPER = 2
        SEARCH_INDEXER = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    bot_type: BotType = proto.Field(
        proto.ENUM,
        number=2,
        enum=BotType,
    )


class TokenProperties(proto.Message):
    r"""Properties of the provided event token.

    Attributes:
        valid (bool):
            Output only. Indicates whether the provided user response
            token is valid. If ``false``, the token is invalid, either
            because the user failed the challenge or for a reason
            provided in the ``invalid_reason`` field.
        invalid_reason (google.cloud.recaptchaenterprise_v1.types.TokenProperties.InvalidReason):
            Output only. Reason associated with the
            response when valid = false.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp corresponding to
            the generation of the token.
        hostname (str):
            Output only. The hostname of the page on
            which the token was generated (Web keys only).
        android_package_name (str):
            Output only. The name of the Android package
            with which the token was generated (Android keys
            only).
        ios_bundle_id (str):
            Output only. The ID of the iOS bundle with
            which the token was generated (iOS keys only).
        action (str):
            Output only. Action name provided at token
            generation.
    """

    class InvalidReason(proto.Enum):
        r"""Enum that represents the types of invalid token reasons.
        Ensure that applications can handle values not explicitly
        listed.

        Values:
            INVALID_REASON_UNSPECIFIED (0):
                Default unspecified type.
            UNKNOWN_INVALID_REASON (1):
                If the failure reason was not accounted for.
            MALFORMED (2):
                The provided user verification token was
                malformed.
            EXPIRED (3):
                The user verification token had expired.
            DUPE (4):
                The user verification had already been seen.
            MISSING (5):
                The user verification token was not present.
            BROWSER_ERROR (6):
                A retriable error (such as network failure)
                occurred on the browser. Could easily be
                simulated by an attacker.
            UNEXPECTED_ACTION (7):
                The action provided at token generation was different than
                the ``expected_action`` in the assessment request. The
                comparison is case-insensitive. This reason can only be
                returned if all of the following are true:

                - your ``site_key`` has the POLICY_BASED_CHALLENGE
                  integration type
                - you set an action score threshold higher than 0.0
                - you provided a non-empty ``expected_action``
            KEY_MISMATCH (8):
                The key used to generate the token does not match the
                ``site_key``.
            DOMAIN_MISMATCH (9):
                The domain of the page on which the token was generated does
                not match the ``allowed_domains`` configured in the
                ``site_key``.
        """

        INVALID_REASON_UNSPECIFIED = 0
        UNKNOWN_INVALID_REASON = 1
        MALFORMED = 2
        EXPIRED = 3
        DUPE = 4
        MISSING = 5
        BROWSER_ERROR = 6
        UNEXPECTED_ACTION = 7
        KEY_MISMATCH = 8
        DOMAIN_MISMATCH = 9

    valid: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    invalid_reason: InvalidReason = proto.Field(
        proto.ENUM,
        number=2,
        enum=InvalidReason,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    hostname: str = proto.Field(
        proto.STRING,
        number=4,
    )
    android_package_name: str = proto.Field(
        proto.STRING,
        number=8,
    )
    ios_bundle_id: str = proto.Field(
        proto.STRING,
        number=9,
    )
    action: str = proto.Field(
        proto.STRING,
        number=5,
    )


class FraudPreventionAssessment(proto.Message):
    r"""Assessment for Fraud Prevention.

    Attributes:
        transaction_risk (float):
            Output only. Probability of this transaction
            being fraudulent. Summarizes the combined risk
            of attack vectors below. Values are from 0.0
            (lowest) to 1.0 (highest).
        risk_reasons (MutableSequence[google.cloud.recaptchaenterprise_v1.types.FraudPreventionAssessment.RiskReason]):
            Output only. Reasons why the transaction is
            probably fraudulent and received a high
            transaction risk score.
        stolen_instrument_verdict (google.cloud.recaptchaenterprise_v1.types.FraudPreventionAssessment.StolenInstrumentVerdict):
            Output only. Assessment of this transaction
            for risk of a stolen instrument.
        card_testing_verdict (google.cloud.recaptchaenterprise_v1.types.FraudPreventionAssessment.CardTestingVerdict):
            Output only. Assessment of this transaction
            for risk of being part of a card testing attack.
        behavioral_trust_verdict (google.cloud.recaptchaenterprise_v1.types.FraudPreventionAssessment.BehavioralTrustVerdict):
            Output only. Assessment of this transaction
            for behavioral trust.
    """

    class RiskReason(proto.Message):
        r"""Risk reasons applicable to the Fraud Prevention assessment.

        Attributes:
            reason (google.cloud.recaptchaenterprise_v1.types.FraudPreventionAssessment.RiskReason.Reason):
                Output only. Risk reasons applicable to the
                Fraud Prevention assessment.
        """

        class Reason(proto.Enum):
            r"""Risk reasons applicable to the Fraud Prevention assessment.
            New risk reasons will be added over time.

            Values:
                REASON_UNSPECIFIED (0):
                    Default unspecified type.
                HIGH_TRANSACTION_VELOCITY (1):
                    A suspiciously high number of recent
                    transactions have used identifiers present in
                    this transaction.
                EXCESSIVE_ENUMERATION_PATTERN (2):
                    User is cycling through a suspiciously large
                    number of identifiers, suggesting enumeration or
                    validation attacks within a potential fraud
                    network.
                SHORT_IDENTITY_HISTORY (3):
                    User has a short history or no history in the
                    reCAPTCHA network, suggesting the possibility of
                    synthetic identity generation.
                GEOLOCATION_DISCREPANCY (4):
                    Identifiers used in this transaction
                    originate from an unusual or conflicting set of
                    geolocations.
                ASSOCIATED_WITH_FRAUD_CLUSTER (5):
                    This transaction is linked to a cluster of
                    known fraudulent activity.
            """

            REASON_UNSPECIFIED = 0
            HIGH_TRANSACTION_VELOCITY = 1
            EXCESSIVE_ENUMERATION_PATTERN = 2
            SHORT_IDENTITY_HISTORY = 3
            GEOLOCATION_DISCREPANCY = 4
            ASSOCIATED_WITH_FRAUD_CLUSTER = 5

        reason: "FraudPreventionAssessment.RiskReason.Reason" = proto.Field(
            proto.ENUM,
            number=1,
            enum="FraudPreventionAssessment.RiskReason.Reason",
        )

    class StolenInstrumentVerdict(proto.Message):
        r"""Information about stolen instrument fraud, where the user is
        not the legitimate owner of the instrument being used for the
        purchase.

        Attributes:
            risk (float):
                Output only. Probability of this transaction
                being executed with a stolen instrument. Values
                are from 0.0 (lowest) to 1.0 (highest).
        """

        risk: float = proto.Field(
            proto.FLOAT,
            number=1,
        )

    class CardTestingVerdict(proto.Message):
        r"""Information about card testing fraud, where an adversary is
        testing fraudulently obtained cards or brute forcing their
        details.

        Attributes:
            risk (float):
                Output only. Probability of this transaction
                attempt being part of a card testing attack.
                Values are from 0.0 (lowest) to 1.0 (highest).
        """

        risk: float = proto.Field(
            proto.FLOAT,
            number=1,
        )

    class BehavioralTrustVerdict(proto.Message):
        r"""Information about behavioral trust of the transaction.

        Attributes:
            trust (float):
                Output only. Probability of this transaction
                attempt being executed in a behaviorally
                trustworthy way. Values are from 0.0 (lowest) to
                1.0 (highest).
        """

        trust: float = proto.Field(
            proto.FLOAT,
            number=1,
        )

    transaction_risk: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    risk_reasons: MutableSequence[RiskReason] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=RiskReason,
    )
    stolen_instrument_verdict: StolenInstrumentVerdict = proto.Field(
        proto.MESSAGE,
        number=2,
        message=StolenInstrumentVerdict,
    )
    card_testing_verdict: CardTestingVerdict = proto.Field(
        proto.MESSAGE,
        number=3,
        message=CardTestingVerdict,
    )
    behavioral_trust_verdict: BehavioralTrustVerdict = proto.Field(
        proto.MESSAGE,
        number=4,
        message=BehavioralTrustVerdict,
    )


class FraudSignals(proto.Message):
    r"""Fraud signals describing users and cards involved in the
    transaction.

    Attributes:
        user_signals (google.cloud.recaptchaenterprise_v1.types.FraudSignals.UserSignals):
            Output only. Signals describing the end user
            in this transaction.
        card_signals (google.cloud.recaptchaenterprise_v1.types.FraudSignals.CardSignals):
            Output only. Signals describing the payment
            card or cards used in this transaction.
    """

    class UserSignals(proto.Message):
        r"""Signals describing the user involved in this transaction.

        Attributes:
            active_days_lower_bound (int):
                Output only. This user (based on email,
                phone, and other identifiers) has been seen on
                the internet for at least this number of days.
            synthetic_risk (float):
                Output only. Likelihood (from 0.0 to 1.0)
                this user includes synthetic components in their
                identity, such as a randomly generated email
                address, temporary phone number, or fake
                shipping address.
        """

        active_days_lower_bound: int = proto.Field(
            proto.INT32,
            number=1,
        )
        synthetic_risk: float = proto.Field(
            proto.FLOAT,
            number=2,
        )

    class CardSignals(proto.Message):
        r"""Signals describing the payment card used in this transaction.

        Attributes:
            card_labels (MutableSequence[google.cloud.recaptchaenterprise_v1.types.FraudSignals.CardSignals.CardLabel]):
                Output only. The labels for the payment card
                in this transaction.
        """

        class CardLabel(proto.Enum):
            r"""Risk labels describing the card being assessed, such as its
            funding mechanism.
            Ensure that applications can handle values not explicitly
            listed.

            Values:
                CARD_LABEL_UNSPECIFIED (0):
                    No label specified.
                PREPAID (1):
                    This card has been detected as prepaid.
                VIRTUAL (2):
                    This card has been detected as virtual, such
                    as a card number generated for a single
                    transaction or merchant.
                UNEXPECTED_LOCATION (3):
                    This card has been detected as being used in
                    an unexpected geographic location.
            """

            CARD_LABEL_UNSPECIFIED = 0
            PREPAID = 1
            VIRTUAL = 2
            UNEXPECTED_LOCATION = 3

        card_labels: MutableSequence["FraudSignals.CardSignals.CardLabel"] = (
            proto.RepeatedField(
                proto.ENUM,
                number=1,
                enum="FraudSignals.CardSignals.CardLabel",
            )
        )

    user_signals: UserSignals = proto.Field(
        proto.MESSAGE,
        number=1,
        message=UserSignals,
    )
    card_signals: CardSignals = proto.Field(
        proto.MESSAGE,
        number=2,
        message=CardSignals,
    )


class SmsTollFraudVerdict(proto.Message):
    r"""Information about SMS toll fraud.

    Attributes:
        risk (float):
            Output only. Probability of an SMS event
            being fraudulent. Values are from 0.0 (lowest)
            to 1.0 (highest).
        reasons (MutableSequence[google.cloud.recaptchaenterprise_v1.types.SmsTollFraudVerdict.SmsTollFraudReason]):
            Output only. Reasons contributing to the SMS
            toll fraud verdict.
    """

    class SmsTollFraudReason(proto.Enum):
        r"""Reasons contributing to the SMS toll fraud verdict.
        Ensure that applications can handle values not explicitly
        listed.

        Values:
            SMS_TOLL_FRAUD_REASON_UNSPECIFIED (0):
                Default unspecified reason
            INVALID_PHONE_NUMBER (1):
                The provided phone number was invalid
        """

        SMS_TOLL_FRAUD_REASON_UNSPECIFIED = 0
        INVALID_PHONE_NUMBER = 1

    risk: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    reasons: MutableSequence[SmsTollFraudReason] = proto.RepeatedField(
        proto.ENUM,
        number=2,
        enum=SmsTollFraudReason,
    )


class PhoneFraudAssessment(proto.Message):
    r"""Assessment for Phone Fraud

    Attributes:
        sms_toll_fraud_verdict (google.cloud.recaptchaenterprise_v1.types.SmsTollFraudVerdict):
            Output only. Assessment of this phone event
            for risk of SMS toll fraud.
    """

    sms_toll_fraud_verdict: "SmsTollFraudVerdict" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="SmsTollFraudVerdict",
    )


class AccountDefenderAssessment(proto.Message):
    r"""Account defense risk assessment.

    Attributes:
        labels (MutableSequence[google.cloud.recaptchaenterprise_v1.types.AccountDefenderAssessment.AccountDefenderLabel]):
            Output only. Labels for this request.
        account_takeover_verdict (google.cloud.recaptchaenterprise_v1.types.AccountDefenderAssessment.AccountTakeoverVerdict):
            Output only. Account takeover risk assessment
            for this request.
    """

    class AccountDefenderLabel(proto.Enum):
        r"""Labels returned by Account defense for this request.
        Ensure that applications can handle values not explicitly
        listed.

        Values:
            ACCOUNT_DEFENDER_LABEL_UNSPECIFIED (0):
                Default unspecified type.
            PROFILE_MATCH (1):
                The request matches a trusted profile
                associated with this account.
            SUSPICIOUS_LOGIN_ACTIVITY (2):
                The request is potentially a suspicious login
                event and must be further verified either
                through multi-factor authentication or another
                system.
            SUSPICIOUS_ACCOUNT_CREATION (3):
                The request matched a profile that previously
                had suspicious account creation behavior. This
                can mean that this is a fake account.
            RELATED_ACCOUNTS_NUMBER_HIGH (4):
                The account in the request has a high number
                of related accounts. It does not necessarily
                imply that the account is bad but can require
                further investigation.
        """

        ACCOUNT_DEFENDER_LABEL_UNSPECIFIED = 0
        PROFILE_MATCH = 1
        SUSPICIOUS_LOGIN_ACTIVITY = 2
        SUSPICIOUS_ACCOUNT_CREATION = 3
        RELATED_ACCOUNTS_NUMBER_HIGH = 4

    class AccountTakeoverVerdict(proto.Message):
        r"""Account takeover risk assessment.

        Attributes:
            risk (float):
                Output only. Account takeover attempt
                probability. Values are from 0.0 (lowest risk)
                to 1.0 (highest risk).
            risk_reasons (MutableSequence[google.cloud.recaptchaenterprise_v1.types.AccountDefenderAssessment.AccountRiskReason]):
                Output only. Unordered list. Reasons why the
                request appears risky. Risk reasons can be
                returned even if the risk is low, as trustworthy
                requests can still have some risk signals.
            trust_reasons (MutableSequence[google.cloud.recaptchaenterprise_v1.types.AccountDefenderAssessment.AccountTrustReason]):
                Output only. Unordered list. Reasons why the
                request appears trustworthy. Trust reasons can
                be returned even if the risk is high, as risky
                requests can still have some trust signals.
        """

        risk: float = proto.Field(
            proto.FLOAT,
            number=1,
        )
        risk_reasons: MutableSequence["AccountDefenderAssessment.AccountRiskReason"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=4,
                message="AccountDefenderAssessment.AccountRiskReason",
            )
        )
        trust_reasons: MutableSequence[
            "AccountDefenderAssessment.AccountTrustReason"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=5,
            message="AccountDefenderAssessment.AccountTrustReason",
        )

    class AccountRiskReason(proto.Message):
        r"""Risk explainability reasons for Account defense.

        Attributes:
            reason (google.cloud.recaptchaenterprise_v1.types.AccountDefenderAssessment.AccountRiskReason.RiskReason):
                Output only. A risk reason associated with
                this request.
        """

        class RiskReason(proto.Enum):
            r"""Risk explainability reasons for Account defense.
            Ensure that applications can handle values not explicitly
            listed.

            Values:
                RISK_REASON_UNSPECIFIED (0):
                    Default unspecified type.
                CLIENT_HISTORICAL_BOT_ACTIVITY (1):
                    The client has been observed sending bot-like
                    traffic to this site in the past. This reason
                    incorporates historical reputation and indicates
                    that the client is known to use bots, even if
                    the current request is being made by a human.
                ACCOUNT_IN_LARGE_RELATED_GROUP (2):
                    The account is part of a large group of
                    related accounts, indicating that it may be part
                    of a fraudulent network. Related accounts are
                    identified based on having similar traffic
                    patterns and request characteristics.
                CLIENT_ACCESSED_MANY_ACCOUNTS (3):
                    The client has been observed accessing many
                    accounts on this site.
                DISPOSABLE_EMAIL_DOMAIN (4):
                    This email domain is a suspected provider of
                    disposable email addresses.
            """

            RISK_REASON_UNSPECIFIED = 0
            CLIENT_HISTORICAL_BOT_ACTIVITY = 1
            ACCOUNT_IN_LARGE_RELATED_GROUP = 2
            CLIENT_ACCESSED_MANY_ACCOUNTS = 3
            DISPOSABLE_EMAIL_DOMAIN = 4

        reason: "AccountDefenderAssessment.AccountRiskReason.RiskReason" = proto.Field(
            proto.ENUM,
            number=1,
            enum="AccountDefenderAssessment.AccountRiskReason.RiskReason",
        )

    class AccountTrustReason(proto.Message):
        r"""Trust explainability reasons for Account defense.

        Attributes:
            reason (google.cloud.recaptchaenterprise_v1.types.AccountDefenderAssessment.AccountTrustReason.TrustReason):
                Output only. A trust reason associated with
                this request.
        """

        class TrustReason(proto.Enum):
            r"""Trust explainability reasons for Account defense.
            Ensure that applications can handle values not explicitly
            listed.

            Values:
                TRUST_REASON_UNSPECIFIED (0):
                    Default unspecified type.
                PROFILE_MATCH (1):
                    The request matches a trusted profile associated with this
                    account. Equivalent to
                    ``AccountDefenderLabel.PROFILE_MATCH``.
                ACCOUNT_HISTORY_REPUTABLE (2):
                    The account's historical activity is
                    reputable. It is unlikely that the account has
                    been compromised in the past.
                IDENTITY_GLOBAL_ACTIVITY_REPUTABLE (3):
                    The identity shows a global pattern of reputable activity
                    based on ``userInfo`` and associated identifiers.
                IDENTITY_HISTORY_REPUTABLE (4):
                    The identity shows a long-standing history of reputable
                    activity based on ``userInfo`` and associated identifiers.
            """

            TRUST_REASON_UNSPECIFIED = 0
            PROFILE_MATCH = 1
            ACCOUNT_HISTORY_REPUTABLE = 2
            IDENTITY_GLOBAL_ACTIVITY_REPUTABLE = 3
            IDENTITY_HISTORY_REPUTABLE = 4

        reason: "AccountDefenderAssessment.AccountTrustReason.TrustReason" = (
            proto.Field(
                proto.ENUM,
                number=1,
                enum="AccountDefenderAssessment.AccountTrustReason.TrustReason",
            )
        )

    labels: MutableSequence[AccountDefenderLabel] = proto.RepeatedField(
        proto.ENUM,
        number=1,
        enum=AccountDefenderLabel,
    )
    account_takeover_verdict: AccountTakeoverVerdict = proto.Field(
        proto.MESSAGE,
        number=4,
        message=AccountTakeoverVerdict,
    )


class CreateKeyRequest(proto.Message):
    r"""The create key request message.

    Attributes:
        parent (str):
            Required. The name of the project in which the key is
            created, in the format ``projects/{project}``.
        key (google.cloud.recaptchaenterprise_v1.types.Key):
            Required. Information to create a reCAPTCHA
            Enterprise key.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    key: "Key" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Key",
    )


class ListKeysRequest(proto.Message):
    r"""The list keys request message.

    Attributes:
        parent (str):
            Required. The name of the project that contains the keys
            that is listed, in the format ``projects/{project}``.
        page_size (int):
            Optional. The maximum number of keys to
            return. Default is 10. Max limit is 1000.
        page_token (str):
            Optional. The next_page_token value returned from a
            previous. ListKeysRequest, if any.
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


class ListKeysResponse(proto.Message):
    r"""Response to request to list keys in a project.

    Attributes:
        keys (MutableSequence[google.cloud.recaptchaenterprise_v1.types.Key]):
            Key details.
        next_page_token (str):
            Token to retrieve the next page of results.
            It is set to empty if no keys remain in results.
    """

    @property
    def raw_page(self):
        return self

    keys: MutableSequence["Key"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Key",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class RetrieveLegacySecretKeyRequest(proto.Message):
    r"""The retrieve legacy secret key request message.

    Attributes:
        key (str):
            Required. The public key name linked to the requested secret
            key in the format ``projects/{project}/keys/{key}``.
    """

    key: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetKeyRequest(proto.Message):
    r"""The get key request message.

    Attributes:
        name (str):
            Required. The name of the requested key, in the format
            ``projects/{project}/keys/{key}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateKeyRequest(proto.Message):
    r"""The update key request message.

    Attributes:
        key (google.cloud.recaptchaenterprise_v1.types.Key):
            Required. The key to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The mask to control which fields of
            the key get updated. If the mask is not present,
            all fields are updated.
    """

    key: "Key" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Key",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteKeyRequest(proto.Message):
    r"""The delete key request message.

    Attributes:
        name (str):
            Required. The name of the key to be deleted, in the format
            ``projects/{project}/keys/{key}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateFirewallPolicyRequest(proto.Message):
    r"""The create firewall policy request message.

    Attributes:
        parent (str):
            Required. The name of the project this policy applies to, in
            the format ``projects/{project}``.
        firewall_policy (google.cloud.recaptchaenterprise_v1.types.FirewallPolicy):
            Required. Information to create the policy.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    firewall_policy: "FirewallPolicy" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="FirewallPolicy",
    )


class ListFirewallPoliciesRequest(proto.Message):
    r"""The list firewall policies request message.

    Attributes:
        parent (str):
            Required. The name of the project to list the policies for,
            in the format ``projects/{project}``.
        page_size (int):
            Optional. The maximum number of policies to
            return. Default is 10. Max limit is 1000.
        page_token (str):
            Optional. The next_page_token value returned from a
            previous. ListFirewallPoliciesRequest, if any.
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


class ListFirewallPoliciesResponse(proto.Message):
    r"""Response to request to list firewall policies belonging to a
    project.

    Attributes:
        firewall_policies (MutableSequence[google.cloud.recaptchaenterprise_v1.types.FirewallPolicy]):
            Policy details.
        next_page_token (str):
            Token to retrieve the next page of results.
            It is set to empty if no policies remain in
            results.
    """

    @property
    def raw_page(self):
        return self

    firewall_policies: MutableSequence["FirewallPolicy"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="FirewallPolicy",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetFirewallPolicyRequest(proto.Message):
    r"""The get firewall policy request message.

    Attributes:
        name (str):
            Required. The name of the requested policy, in the format
            ``projects/{project}/firewallpolicies/{firewallpolicy}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateFirewallPolicyRequest(proto.Message):
    r"""The update firewall policy request message.

    Attributes:
        firewall_policy (google.cloud.recaptchaenterprise_v1.types.FirewallPolicy):
            Required. The policy to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The mask to control which fields of
            the policy get updated. If the mask is not
            present, all fields are updated.
    """

    firewall_policy: "FirewallPolicy" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="FirewallPolicy",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteFirewallPolicyRequest(proto.Message):
    r"""The delete firewall policy request message.

    Attributes:
        name (str):
            Required. The name of the policy to be deleted, in the
            format
            ``projects/{project}/firewallpolicies/{firewallpolicy}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ReorderFirewallPoliciesRequest(proto.Message):
    r"""The reorder firewall policies request message.

    Attributes:
        parent (str):
            Required. The name of the project to list the policies for,
            in the format ``projects/{project}``.
        names (MutableSequence[str]):
            Required. A list containing all policy names, in the new
            order. Each name is in the format
            ``projects/{project}/firewallpolicies/{firewallpolicy}``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class ReorderFirewallPoliciesResponse(proto.Message):
    r"""The reorder firewall policies response message."""


class MigrateKeyRequest(proto.Message):
    r"""The migrate key request message.

    Attributes:
        name (str):
            Required. The name of the key to be migrated, in the format
            ``projects/{project}/keys/{key}``.
        skip_billing_check (bool):
            Optional. If true, skips the billing check. A reCAPTCHA
            Enterprise key or migrated key behaves differently than a
            reCAPTCHA (non-Enterprise version) key when you reach a
            quota limit (see
            https://docs.cloud.google.com/recaptcha/quotas#quota_limit).
            To avoid any disruption of your usage, we check that a
            billing account is present. If your usage of reCAPTCHA is
            under the free quota, you can safely skip the billing check
            and proceed with the migration. See
            https://cloud.google.com/recaptcha/docs/billing-information.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    skip_billing_check: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class GetMetricsRequest(proto.Message):
    r"""The get metrics request message.

    Attributes:
        name (str):
            Required. The name of the requested metrics, in the format
            ``projects/{project}/keys/{key}/metrics``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Metrics(proto.Message):
    r"""Metrics for a single Key.

    Attributes:
        name (str):
            Output only. Identifier. The name of the metrics, in the
            format ``projects/{project}/keys/{key}/metrics``.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Inclusive start time aligned to a day in the
            America/Los_Angeles (Pacific) timezone.
        score_metrics (MutableSequence[google.cloud.recaptchaenterprise_v1.types.ScoreMetrics]):
            Metrics are continuous and in order by dates,
            and in the granularity of day. All Key types
            should have score-based data.
        challenge_metrics (MutableSequence[google.cloud.recaptchaenterprise_v1.types.ChallengeMetrics]):
            Metrics are continuous and in order by dates,
            and in the granularity of day. Only
            challenge-based keys (CHECKBOX, INVISIBLE) have
            challenge-based data.
    """

    name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    score_metrics: MutableSequence["ScoreMetrics"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="ScoreMetrics",
    )
    challenge_metrics: MutableSequence["ChallengeMetrics"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="ChallengeMetrics",
    )


class RetrieveLegacySecretKeyResponse(proto.Message):
    r"""Secret key is used only in legacy reCAPTCHA. It must be used
    in a 3rd party integration with legacy reCAPTCHA.

    Attributes:
        legacy_secret_key (str):
            The secret key (also known as shared secret)
            authorizes communication between your
            application backend and the reCAPTCHA Enterprise
            server to create an assessment.
            The secret key needs to be kept safe for
            security purposes.
    """

    legacy_secret_key: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Key(proto.Message):
    r"""A key used to identify and configure applications (web and/or
    mobile) that use reCAPTCHA Enterprise.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name for the Key in the format
            ``projects/{project}/keys/{key}``.
        display_name (str):
            Required. Human-readable display name of this
            key. Modifiable by user.
        web_settings (google.cloud.recaptchaenterprise_v1.types.WebKeySettings):
            Settings for keys that can be used by
            websites.

            This field is a member of `oneof`_ ``platform_settings``.
        android_settings (google.cloud.recaptchaenterprise_v1.types.AndroidKeySettings):
            Settings for keys that can be used by Android
            apps.

            This field is a member of `oneof`_ ``platform_settings``.
        ios_settings (google.cloud.recaptchaenterprise_v1.types.IOSKeySettings):
            Settings for keys that can be used by iOS
            apps.

            This field is a member of `oneof`_ ``platform_settings``.
        express_settings (google.cloud.recaptchaenterprise_v1.types.ExpressKeySettings):
            Settings for keys that can be used by
            reCAPTCHA Express.

            This field is a member of `oneof`_ ``platform_settings``.
        universal_settings (google.cloud.recaptchaenterprise_v1.types.UniversalKeySettings):
            Settings for keys that are configured through
            their Policy.

            This field is a member of `oneof`_ ``platform_settings``.
        labels (MutableMapping[str, str]):
            Optional. See [Creating and managing labels]
            (https://cloud.google.com/recaptcha/docs/labels).
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp corresponding to
            the creation of this key.
        testing_options (google.cloud.recaptchaenterprise_v1.types.TestingOptions):
            Optional. Options for user acceptance
            testing.
        waf_settings (google.cloud.recaptchaenterprise_v1.types.WafSettings):
            Optional. Settings for Web Application
            Firewall (WAF).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    web_settings: "WebKeySettings" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="platform_settings",
        message="WebKeySettings",
    )
    android_settings: "AndroidKeySettings" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="platform_settings",
        message="AndroidKeySettings",
    )
    ios_settings: "IOSKeySettings" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="platform_settings",
        message="IOSKeySettings",
    )
    express_settings: "ExpressKeySettings" = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="platform_settings",
        message="ExpressKeySettings",
    )
    universal_settings: "UniversalKeySettings" = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="platform_settings",
        message="UniversalKeySettings",
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    testing_options: "TestingOptions" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="TestingOptions",
    )
    waf_settings: "WafSettings" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="WafSettings",
    )


class TestingOptions(proto.Message):
    r"""Options for user acceptance testing.

    Attributes:
        testing_score (float):
            Optional. All assessments for this Key return
            this score. Must be between 0 (likely not
            legitimate) and 1 (likely legitimate) inclusive.
        testing_challenge (google.cloud.recaptchaenterprise_v1.types.TestingOptions.TestingChallenge):
            Optional. For challenge-based keys only
            (CHECKBOX, INVISIBLE), all challenge requests
            for this site return nocaptcha if NOCAPTCHA, or
            an unsolvable challenge if CHALLENGE.
    """

    class TestingChallenge(proto.Enum):
        r"""Enum that represents the challenge option for challenge-based
        (for example, CHECKBOX and INVISIBLE) testing keys. Ensure that
        applications can handle values not explicitly listed.

        Values:
            TESTING_CHALLENGE_UNSPECIFIED (0):
                Perform the normal risk analysis and return
                either nocaptcha or a challenge depending on
                risk and trust factors.
            NOCAPTCHA (1):
                Challenge requests for this key always return
                a nocaptcha, which does not require a solution.
            UNSOLVABLE_CHALLENGE (2):
                Challenge requests for this key always return
                an unsolvable challenge.
        """

        TESTING_CHALLENGE_UNSPECIFIED = 0
        NOCAPTCHA = 1
        UNSOLVABLE_CHALLENGE = 2

    testing_score: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    testing_challenge: TestingChallenge = proto.Field(
        proto.ENUM,
        number=2,
        enum=TestingChallenge,
    )


class WebKeySettings(proto.Message):
    r"""Settings specific to keys that can be used by websites.

    Attributes:
        allow_all_domains (bool):
            Optional. If set to true, it means allowed_domains are not
            enforced.
        allowed_domains (MutableSequence[str]):
            Optional. Domains or subdomains of websites allowed to use
            the key. All subdomains of an allowed domain are
            automatically allowed. A valid domain requires a host and
            must not include any path, port, query or fragment.
            Examples: 'example.com' or 'subdomain.example.com' Each key
            supports a maximum of 250 domains. To use a key on more
            domains, set ``allow_all_domains`` to true. When this is
            set, you are responsible for validating the hostname by
            checking the ``token_properties.hostname`` field in each
            assessment response against your list of allowed domains.
        allow_amp_traffic (bool):
            Optional. If set to true, the key can be used
            on AMP (Accelerated Mobile Pages) websites. This
            is supported only for the SCORE integration
            type.
        integration_type (google.cloud.recaptchaenterprise_v1.types.WebKeySettings.IntegrationType):
            Required. Describes how this key is
            integrated with the website.
        challenge_security_preference (google.cloud.recaptchaenterprise_v1.types.WebKeySettings.ChallengeSecurityPreference):
            Optional. Settings for the frequency and difficulty at which
            this key triggers captcha challenges. This should only be
            specified for ``IntegrationType`` CHECKBOX, INVISIBLE or
            POLICY_BASED_CHALLENGE.
        challenge_settings (google.cloud.recaptchaenterprise_v1.types.WebKeySettings.ChallengeSettings):
            Optional. Challenge settings.
    """

    class IntegrationType(proto.Enum):
        r"""Enum that represents the integration types for web keys.
        Ensure that applications can handle values not explicitly
        listed.

        Values:
            INTEGRATION_TYPE_UNSPECIFIED (0):
                Default type that indicates this enum hasn't
                been specified. This is not a valid
                IntegrationType, one of the other types must be
                specified instead.
            SCORE (1):
                Only used to produce scores. It doesn't
                display the "I'm not a robot" checkbox and never
                shows captcha challenges.
            CHECKBOX (2):
                Displays the "I'm not a robot" checkbox and
                may show captcha challenges after it is checked.
            INVISIBLE (3):
                Doesn't display the "I'm not a robot"
                checkbox, but may show captcha challenges after
                risk analysis.
            POLICY_BASED_CHALLENGE (5):
                Displays a visual challenge or not depending
                on the user risk analysis score.
        """

        INTEGRATION_TYPE_UNSPECIFIED = 0
        SCORE = 1
        CHECKBOX = 2
        INVISIBLE = 3
        POLICY_BASED_CHALLENGE = 5

    class ChallengeSecurityPreference(proto.Enum):
        r"""Enum that represents the possible challenge frequency and
        difficulty configurations for a web key.
        Ensure that applications can handle values not explicitly
        listed.

        Values:
            CHALLENGE_SECURITY_PREFERENCE_UNSPECIFIED (0):
                Default type that indicates this enum hasn't
                been specified.
            USABILITY (1):
                Key tends to show fewer and easier
                challenges.
            BALANCE (2):
                Key tends to show balanced (in amount and
                difficulty) challenges.
            SECURITY (3):
                Key tends to show more and harder challenges.
        """

        CHALLENGE_SECURITY_PREFERENCE_UNSPECIFIED = 0
        USABILITY = 1
        BALANCE = 2
        SECURITY = 3

    class ActionSettings(proto.Message):
        r"""Per-action challenge settings.

        Attributes:
            score_threshold (float):
                Required. A challenge is triggered if the
                end-user score is below that threshold. Value
                must be between 0 and 1 (inclusive).
        """

        score_threshold: float = proto.Field(
            proto.FLOAT,
            number=1,
        )

    class ChallengeSettings(proto.Message):
        r"""Settings for POLICY_BASED_CHALLENGE keys to control when a challenge
        is triggered.

        Attributes:
            default_settings (google.cloud.recaptchaenterprise_v1.types.WebKeySettings.ActionSettings):
                Required. Defines when a challenge is triggered (unless the
                default threshold is overridden for the given action, see
                ``action_settings``).
            action_settings (MutableMapping[str, google.cloud.recaptchaenterprise_v1.types.WebKeySettings.ActionSettings]):
                Optional. The action to score threshold map. The action name
                should be the same as the action name passed in the
                ``data-action`` attribute (see
                https://cloud.google.com/recaptcha/docs/actions-website).
                Action names are case-insensitive. There is a maximum of 100
                action settings. An action name has a maximum length of 100.
        """

        default_settings: "WebKeySettings.ActionSettings" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="WebKeySettings.ActionSettings",
        )
        action_settings: MutableMapping[str, "WebKeySettings.ActionSettings"] = (
            proto.MapField(
                proto.STRING,
                proto.MESSAGE,
                number=2,
                message="WebKeySettings.ActionSettings",
            )
        )

    allow_all_domains: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    allowed_domains: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    allow_amp_traffic: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    integration_type: IntegrationType = proto.Field(
        proto.ENUM,
        number=4,
        enum=IntegrationType,
    )
    challenge_security_preference: ChallengeSecurityPreference = proto.Field(
        proto.ENUM,
        number=5,
        enum=ChallengeSecurityPreference,
    )
    challenge_settings: ChallengeSettings = proto.Field(
        proto.MESSAGE,
        number=6,
        message=ChallengeSettings,
    )


class AndroidKeySettings(proto.Message):
    r"""Settings specific to keys that can be used by Android apps.

    Attributes:
        allow_all_package_names (bool):
            Optional. If set to true, allowed_package_names are not
            enforced.
        allowed_package_names (MutableSequence[str]):
            Optional. Android package names of apps allowed to use the
            key. Example: 'com.companyname.appname' Each key supports a
            maximum of 250 package names. To use a key on more apps, set
            ``allow_all_package_names`` to true. When this is set, you
            are responsible for validating the package name by checking
            the ``token_properties.android_package_name`` field in each
            assessment response against your list of allowed package
            names.
        support_non_google_app_store_distribution (bool):
            Optional. Set to true for keys that are used
            in an Android application that is available for
            download in app stores in addition to the Google
            Play Store.
    """

    allow_all_package_names: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    allowed_package_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    support_non_google_app_store_distribution: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class IOSKeySettings(proto.Message):
    r"""Settings specific to keys that can be used by iOS apps.

    Attributes:
        allow_all_bundle_ids (bool):
            Optional. If set to true, allowed_bundle_ids are not
            enforced.
        allowed_bundle_ids (MutableSequence[str]):
            Optional. iOS bundle IDs of apps allowed to use the key.
            Example: 'com.companyname.productname.appname' Each key
            supports a maximum of 250 bundle IDs. To use a key on more
            apps, set ``allow_all_bundle_ids`` to true. When this is
            set, you are responsible for validating the bundle id by
            checking the ``token_properties.ios_bundle_id`` field in
            each assessment response against your list of allowed bundle
            IDs.
        apple_developer_id (google.cloud.recaptchaenterprise_v1.types.AppleDeveloperId):
            Optional. Apple Developer account details for
            the app that is protected by the reCAPTCHA Key.
            reCAPTCHA leverages platform-specific checks
            like Apple App Attest and Apple DeviceCheck to
            protect your app from abuse. Providing these
            fields allows reCAPTCHA to get a better
            assessment of the integrity of your app.
    """

    allow_all_bundle_ids: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    allowed_bundle_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    apple_developer_id: "AppleDeveloperId" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="AppleDeveloperId",
    )


class ExpressKeySettings(proto.Message):
    r"""Settings specific to keys that can be used for reCAPTCHA
    Express.

    """


class UniversalKeySettings(proto.Message):
    r"""Settings for keys that are configured through their Policy."""


class AppleDeveloperId(proto.Message):
    r"""Contains fields that are required to perform Apple-specific
    integrity checks.

    Attributes:
        private_key (str):
            Required. Input only. A private key
            (downloaded as a text file with a .p8 file
            extension) generated for your Apple Developer
            account. Ensure that Apple DeviceCheck is
            enabled for the private key.
        key_id (str):
            Required. The Apple developer key ID
            (10-character string).
        team_id (str):
            Required. The Apple team ID (10-character
            string) owning the provisioning profile used to
            build your application.
    """

    private_key: str = proto.Field(
        proto.STRING,
        number=1,
    )
    key_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    team_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ScoreDistribution(proto.Message):
    r"""Score distribution.

    Attributes:
        score_buckets (MutableMapping[int, int]):
            Map key is score value multiplied by 100. The scores are
            discrete values between [0, 1]. The maximum number of
            buckets is on order of a few dozen, but typically much lower
            (ie. 10).
    """

    score_buckets: MutableMapping[int, int] = proto.MapField(
        proto.INT32,
        proto.INT64,
        number=1,
    )


class ScoreMetrics(proto.Message):
    r"""Metrics related to scoring.

    Attributes:
        overall_metrics (google.cloud.recaptchaenterprise_v1.types.ScoreDistribution):
            Aggregated score metrics for all traffic.
        action_metrics (MutableMapping[str, google.cloud.recaptchaenterprise_v1.types.ScoreDistribution]):
            Action-based metrics. The map key is the
            action name which specified by the site owners
            at time of the "execute" client-side call.
    """

    overall_metrics: "ScoreDistribution" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ScoreDistribution",
    )
    action_metrics: MutableMapping[str, "ScoreDistribution"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=2,
        message="ScoreDistribution",
    )


class ChallengeMetrics(proto.Message):
    r"""Metrics related to challenges.

    Attributes:
        pageload_count (int):
            Count of reCAPTCHA checkboxes or badges
            rendered. This is mostly equivalent to a count
            of pageloads for pages that include reCAPTCHA.
        nocaptcha_count (int):
            Count of nocaptchas (successful verification
            without a challenge) issued.
        failed_count (int):
            Count of submitted challenge solutions that
            were incorrect or otherwise deemed suspicious
            such that a subsequent challenge was triggered.
        passed_count (int):
            Count of nocaptchas (successful verification
            without a challenge) plus submitted challenge
            solutions that were correct and resulted in
            verification.
    """

    pageload_count: int = proto.Field(
        proto.INT64,
        number=1,
    )
    nocaptcha_count: int = proto.Field(
        proto.INT64,
        number=2,
    )
    failed_count: int = proto.Field(
        proto.INT64,
        number=3,
    )
    passed_count: int = proto.Field(
        proto.INT64,
        number=4,
    )


class FirewallPolicyAssessment(proto.Message):
    r"""Policy config assessment.

    Attributes:
        error (google.rpc.status_pb2.Status):
            Output only. If the processing of a policy config fails, an
            error is populated and the firewall_policy is left empty.
        firewall_policy (google.cloud.recaptchaenterprise_v1.types.FirewallPolicy):
            Output only. The policy that matched the
            request. If more than one policy may match, this
            is the first match. If no policy matches the
            incoming request, the policy field is left
            empty.
    """

    error: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=5,
        message=status_pb2.Status,
    )
    firewall_policy: "FirewallPolicy" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="FirewallPolicy",
    )


class FirewallAction(proto.Message):
    r"""An individual action. Each action represents what to do if a
    policy matches.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        allow (google.cloud.recaptchaenterprise_v1.types.FirewallAction.AllowAction):
            The user request did not match any policy and
            should be allowed access to the requested
            resource.

            This field is a member of `oneof`_ ``firewall_action_oneof``.
        block (google.cloud.recaptchaenterprise_v1.types.FirewallAction.BlockAction):
            This action denies access to a given page.
            The user gets an HTTP error code.

            This field is a member of `oneof`_ ``firewall_action_oneof``.
        include_recaptcha_script (google.cloud.recaptchaenterprise_v1.types.FirewallAction.IncludeRecaptchaScriptAction):
            This action injects reCAPTCHA JavaScript code
            into the HTML page returned by the site backend.

            This field is a member of `oneof`_ ``firewall_action_oneof``.
        redirect (google.cloud.recaptchaenterprise_v1.types.FirewallAction.RedirectAction):
            This action redirects the request to a
            reCAPTCHA interstitial to attach a token.

            This field is a member of `oneof`_ ``firewall_action_oneof``.
        substitute (google.cloud.recaptchaenterprise_v1.types.FirewallAction.SubstituteAction):
            This action transparently serves a different
            page to an offending user.

            This field is a member of `oneof`_ ``firewall_action_oneof``.
        set_header (google.cloud.recaptchaenterprise_v1.types.FirewallAction.SetHeaderAction):
            This action sets a custom header but allow
            the request to continue to the customer backend.

            This field is a member of `oneof`_ ``firewall_action_oneof``.
    """

    class AllowAction(proto.Message):
        r"""An allow action continues processing a request unimpeded."""

    class BlockAction(proto.Message):
        r"""A block action serves an HTTP error code a prevents the
        request from hitting the backend.

        """

    class IncludeRecaptchaScriptAction(proto.Message):
        r"""An include reCAPTCHA script action involves injecting
        reCAPTCHA JavaScript code into the HTML returned by the site
        backend. This reCAPTCHA script is tasked with collecting user
        signals on the requested web page, issuing tokens as a cookie
        within the site domain, and enabling their utilization in
        subsequent page requests.

        """

    class RedirectAction(proto.Message):
        r"""A redirect action returns a 307 (temporary redirect)
        response, pointing the user to a reCAPTCHA interstitial page to
        attach a token.

        """

    class SubstituteAction(proto.Message):
        r"""A substitute action transparently serves a different page
        than the one requested.

        Attributes:
            path (str):
                Optional. The address to redirect to. The
                target is a relative path in the current host.
                Example: "/blog/404.html".
        """

        path: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class SetHeaderAction(proto.Message):
        r"""A set header action sets a header and forwards the request to
        the backend. This can be used to trigger custom protection
        implemented on the backend.

        Attributes:
            key (str):
                Optional. The header key to set in the
                request to the backend server.
            value (str):
                Optional. The header value to set in the
                request to the backend server.
        """

        key: str = proto.Field(
            proto.STRING,
            number=1,
        )
        value: str = proto.Field(
            proto.STRING,
            number=2,
        )

    allow: AllowAction = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="firewall_action_oneof",
        message=AllowAction,
    )
    block: BlockAction = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="firewall_action_oneof",
        message=BlockAction,
    )
    include_recaptcha_script: IncludeRecaptchaScriptAction = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="firewall_action_oneof",
        message=IncludeRecaptchaScriptAction,
    )
    redirect: RedirectAction = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="firewall_action_oneof",
        message=RedirectAction,
    )
    substitute: SubstituteAction = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="firewall_action_oneof",
        message=SubstituteAction,
    )
    set_header: SetHeaderAction = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="firewall_action_oneof",
        message=SetHeaderAction,
    )


class FirewallPolicy(proto.Message):
    r"""A FirewallPolicy represents a single matching pattern and
    resulting actions to take.

    Attributes:
        name (str):
            Identifier. The resource name for the FirewallPolicy in the
            format
            ``projects/{project}/firewallpolicies/{firewallpolicy}``.
        description (str):
            Optional. A description of what this policy
            aims to achieve, for convenience purposes. The
            description can at most include 256 UTF-8
            characters.
        path (str):
            Optional. The path for which this policy applies, specified
            as a glob pattern. For more information on glob, see the
            `manual
            page <https://man7.org/linux/man-pages/man7/glob.7.html>`__.
            A path has a max length of 200 characters.
        condition (str):
            Optional. A CEL (Common Expression Language) conditional
            expression that specifies if this policy applies to an
            incoming user request. If this condition evaluates to true
            and the requested path matched the path pattern, the
            associated actions should be executed by the caller. The
            condition string is checked for CEL syntax correctness on
            creation. For more information, see the `CEL
            spec <https://github.com/google/cel-spec>`__ and its
            `language
            definition <https://github.com/google/cel-spec/blob/master/doc/langdef.md>`__.
            A condition has a max length of 500 characters.
        actions (MutableSequence[google.cloud.recaptchaenterprise_v1.types.FirewallAction]):
            Optional. The actions that the caller should take regarding
            user access. There should be at most one terminal action. A
            terminal action is any action that forces a response, such
            as ``AllowAction``, ``BlockAction`` or ``SubstituteAction``.
            Zero or more non-terminal actions such as ``SetHeader``
            might be specified. A single policy can contain up to 16
            actions.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    path: str = proto.Field(
        proto.STRING,
        number=4,
    )
    condition: str = proto.Field(
        proto.STRING,
        number=5,
    )
    actions: MutableSequence["FirewallAction"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="FirewallAction",
    )


class ListRelatedAccountGroupMembershipsRequest(proto.Message):
    r"""The request message to list memberships in a related account
    group.

    Attributes:
        parent (str):
            Required. The resource name for the related account group in
            the format
            ``projects/{project}/relatedaccountgroups/{relatedaccountgroup}``.
        page_size (int):
            Optional. The maximum number of accounts to
            return. The service might return fewer than this
            value. If unspecified, at most 50 accounts are
            returned. The maximum value is 1000; values
            above 1000 are coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListRelatedAccountGroupMemberships`` call.

            When paginating, all other parameters provided to
            ``ListRelatedAccountGroupMemberships`` must match the call
            that provided the page token.
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


class ListRelatedAccountGroupMembershipsResponse(proto.Message):
    r"""The response to a ``ListRelatedAccountGroupMemberships`` call.

    Attributes:
        related_account_group_memberships (MutableSequence[google.cloud.recaptchaenterprise_v1.types.RelatedAccountGroupMembership]):
            The memberships listed by the query.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    related_account_group_memberships: MutableSequence[
        "RelatedAccountGroupMembership"
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="RelatedAccountGroupMembership",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListRelatedAccountGroupsRequest(proto.Message):
    r"""The request message to list related account groups.

    Attributes:
        parent (str):
            Required. The name of the project to list related account
            groups from, in the format ``projects/{project}``.
        page_size (int):
            Optional. The maximum number of groups to
            return. The service might return fewer than this
            value. If unspecified, at most 50 groups are
            returned. The maximum value is 1000; values
            above 1000 are coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListRelatedAccountGroups`` call. Provide this to retrieve
            the subsequent page.

            When paginating, all other parameters provided to
            ``ListRelatedAccountGroups`` must match the call that
            provided the page token.
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


class ListRelatedAccountGroupsResponse(proto.Message):
    r"""The response to a ``ListRelatedAccountGroups`` call.

    Attributes:
        related_account_groups (MutableSequence[google.cloud.recaptchaenterprise_v1.types.RelatedAccountGroup]):
            The groups of related accounts listed by the
            query.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    related_account_groups: MutableSequence["RelatedAccountGroup"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="RelatedAccountGroup",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SearchRelatedAccountGroupMembershipsRequest(proto.Message):
    r"""The request message to search related account group
    memberships.

    Attributes:
        project (str):
            Required. The name of the project to search related account
            group memberships from. Specify the project name in the
            following format: ``projects/{project}``.
        account_id (str):
            Optional. The unique stable account identifier used to
            search connections. The identifier should correspond to an
            ``account_id`` provided in a previous ``CreateAssessment``
            or ``AnnotateAssessment`` call. Either hashed_account_id or
            account_id must be set, but not both.
        hashed_account_id (bytes):
            Optional. Deprecated: use ``account_id`` instead. The unique
            stable hashed account identifier used to search connections.
            The identifier should correspond to a ``hashed_account_id``
            provided in a previous ``CreateAssessment`` or
            ``AnnotateAssessment`` call. Either hashed_account_id or
            account_id must be set, but not both.
        page_size (int):
            Optional. The maximum number of groups to
            return. The service might return fewer than this
            value. If unspecified, at most 50 groups are
            returned. The maximum value is 1000; values
            above 1000 are coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``SearchRelatedAccountGroupMemberships`` call. Provide this
            to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``SearchRelatedAccountGroupMemberships`` must match the call
            that provided the page token.
    """

    project: str = proto.Field(
        proto.STRING,
        number=1,
    )
    account_id: str = proto.Field(
        proto.STRING,
        number=5,
    )
    hashed_account_id: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class SearchRelatedAccountGroupMembershipsResponse(proto.Message):
    r"""The response to a ``SearchRelatedAccountGroupMemberships`` call.

    Attributes:
        related_account_group_memberships (MutableSequence[google.cloud.recaptchaenterprise_v1.types.RelatedAccountGroupMembership]):
            The queried memberships.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    related_account_group_memberships: MutableSequence[
        "RelatedAccountGroupMembership"
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="RelatedAccountGroupMembership",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AddIpOverrideRequest(proto.Message):
    r"""The AddIpOverride request message.

    Attributes:
        name (str):
            Required. The name of the key to which the IP override is
            added, in the format ``projects/{project}/keys/{key}``.
        ip_override_data (google.cloud.recaptchaenterprise_v1.types.IpOverrideData):
            Required. IP override added to the key.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ip_override_data: "IpOverrideData" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="IpOverrideData",
    )


class AddIpOverrideResponse(proto.Message):
    r"""Response for AddIpOverride."""


class RemoveIpOverrideRequest(proto.Message):
    r"""The RemoveIpOverride request message.

    Attributes:
        name (str):
            Required. The name of the key from which the IP override is
            removed, in the format ``projects/{project}/keys/{key}``.
        ip_override_data (google.cloud.recaptchaenterprise_v1.types.IpOverrideData):
            Required. IP override to be removed from the
            key.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ip_override_data: "IpOverrideData" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="IpOverrideData",
    )


class RemoveIpOverrideResponse(proto.Message):
    r"""Response for RemoveIpOverride."""


class ListIpOverridesRequest(proto.Message):
    r"""The ListIpOverrides request message.

    Attributes:
        parent (str):
            Required. The parent key for which the IP overrides are
            listed, in the format ``projects/{project}/keys/{key}``.
        page_size (int):
            Optional. The maximum number of overrides to return. Default
            is 10. Max limit is 100. If the number of overrides is less
            than the page_size, all overrides are returned. If the page
            size is more than 100, it is coerced to 100.
        page_token (str):
            Optional. The next_page_token value returned from a previous
            ListIpOverridesRequest, if any.
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


class ListIpOverridesResponse(proto.Message):
    r"""Response for ListIpOverrides.

    Attributes:
        ip_overrides (MutableSequence[google.cloud.recaptchaenterprise_v1.types.IpOverrideData]):
            IP Overrides details.
        next_page_token (str):
            Token to retrieve the next page of results.
            If this field is empty, no keys remain in the
            results.
    """

    @property
    def raw_page(self):
        return self

    ip_overrides: MutableSequence["IpOverrideData"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="IpOverrideData",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class RelatedAccountGroupMembership(proto.Message):
    r"""A membership in a group of related accounts.

    Attributes:
        name (str):
            Required. Identifier. The resource name for this membership
            in the format
            ``projects/{project}/relatedaccountgroups/{relatedaccountgroup}/memberships/{membership}``.
        account_id (str):
            The unique stable account identifier of the member. The
            identifier corresponds to an ``account_id`` provided in a
            previous ``CreateAssessment`` or ``AnnotateAssessment``
            call.
        hashed_account_id (bytes):
            Deprecated: use ``account_id`` instead. The unique stable
            hashed account identifier of the member. The identifier
            corresponds to a ``hashed_account_id`` provided in a
            previous ``CreateAssessment`` or ``AnnotateAssessment``
            call.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    account_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    hashed_account_id: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )


class RelatedAccountGroup(proto.Message):
    r"""A group of related accounts.

    Attributes:
        name (str):
            Required. Identifier. The resource name for the related
            account group in the format
            ``projects/{project}/relatedaccountgroups/{related_account_group}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class WafSettings(proto.Message):
    r"""Settings specific to keys that can be used for WAF (Web
    Application Firewall).

    Attributes:
        waf_service (google.cloud.recaptchaenterprise_v1.types.WafSettings.WafService):
            Required. The Web Application Firewall (WAF)
            service that uses this key.
        waf_feature (google.cloud.recaptchaenterprise_v1.types.WafSettings.WafFeature):
            Required. The Web Application Firewall (WAF)
            feature for which this key is enabled.
    """

    class WafFeature(proto.Enum):
        r"""Supported WAF features. For more information, see
        https://cloud.google.com/recaptcha/docs/usecase#comparison_of_features.
        Ensure that applications can handle values not explicitly listed.

        Values:
            WAF_FEATURE_UNSPECIFIED (0):
                Undefined feature.
            CHALLENGE_PAGE (1):
                Redirects suspicious traffic to reCAPTCHA.
            SESSION_TOKEN (2):
                Use reCAPTCHA session-tokens to protect the
                whole user session on the site's domain.
            ACTION_TOKEN (3):
                Use reCAPTCHA action-tokens to protect user
                actions.
            EXPRESS (5):
                Deprecated: Use ``express_settings`` instead.
        """

        WAF_FEATURE_UNSPECIFIED = 0
        CHALLENGE_PAGE = 1
        SESSION_TOKEN = 2
        ACTION_TOKEN = 3
        EXPRESS = 5

    class WafService(proto.Enum):
        r"""Web Application Firewalls that reCAPTCHA supports.
        Ensure that applications can handle values not explicitly
        listed.

        Values:
            WAF_SERVICE_UNSPECIFIED (0):
                Undefined WAF
            CA (1):
                Cloud Armor
            FASTLY (3):
                Fastly
            CLOUDFLARE (4):
                Cloudflare
            AKAMAI (5):
                Akamai
        """

        WAF_SERVICE_UNSPECIFIED = 0
        CA = 1
        FASTLY = 3
        CLOUDFLARE = 4
        AKAMAI = 5

    waf_service: WafService = proto.Field(
        proto.ENUM,
        number=1,
        enum=WafService,
    )
    waf_feature: WafFeature = proto.Field(
        proto.ENUM,
        number=2,
        enum=WafFeature,
    )


class AssessmentEnvironment(proto.Message):
    r"""The environment creating the assessment. This describes your
    environment (the system invoking CreateAssessment), NOT the
    environment of your user.

    Attributes:
        client (str):
            Optional. Identifies the client module
            initiating the CreateAssessment request. This
            can be the link to the client module's project.
            Examples include:

              -
            "github.com/GoogleCloudPlatform/recaptcha-enterprise-google-tag-manager"
              - "wordpress.org/plugins/recaptcha-something".
        version (str):
            Optional. The version of the client module.
            For example, "1.0.0".
    """

    client: str = proto.Field(
        proto.STRING,
        number=1,
    )
    version: str = proto.Field(
        proto.STRING,
        number=2,
    )


class PolicyEvaluation(proto.Message):
    r"""Information about the policy evaluation.

    Attributes:
        challenge_rule_evaluation (google.cloud.recaptchaenterprise_v1.types.ChallengeRuleEvaluation):
            Output only. Populated if one or more
            Challenge rules were matched. Its presence in
            the assessment indicates that at least one
            challenge rule was matched and determined
            whether a challenge was presented to the user.
    """

    challenge_rule_evaluation: "ChallengeRuleEvaluation" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ChallengeRuleEvaluation",
    )


class ChallengeRuleEvaluation(proto.Message):
    r"""Information about the evaluation of a ``ChallengeRule``."""


class IpOverrideData(proto.Message):
    r"""Information about the IP or IP range override.

    Attributes:
        ip (str):
            Required. The IP address to override (can be
            IPv4, IPv6 or CIDR). The IP override must be a
            valid IPv4 or IPv6 address, or a CIDR range. The
            IP override must be a public IP address.
            Example of IPv4: 168.192.5.6
            Example of IPv6:
            2001:0000:130F:0000:0000:09C0:876A:130B Example
            of IPv4 with CIDR: 168.192.5.0/24
            Example of IPv6 with CIDR: 2001:0DB8:1234::/48
        override_type (google.cloud.recaptchaenterprise_v1.types.IpOverrideData.OverrideType):
            Required. Describes the type of IP override.
    """

    class OverrideType(proto.Enum):
        r"""Enum that represents the type of IP override.
        Ensure that applications can handle values not explicitly
        listed.

        Values:
            OVERRIDE_TYPE_UNSPECIFIED (0):
                Default override type that indicates this
                enum hasn't been specified.
            ALLOW (1):
                Allowlist the IP address; i.e. give a
                ``risk_analysis.score`` of 0.9 for all valid assessments.
        """

        OVERRIDE_TYPE_UNSPECIFIED = 0
        ALLOW = 1

    ip: str = proto.Field(
        proto.STRING,
        number=1,
    )
    override_type: OverrideType = proto.Field(
        proto.ENUM,
        number=3,
        enum=OverrideType,
    )


class GetPolicyRequest(proto.Message):
    r"""The request message to get a policy.

    Attributes:
        name (str):
            Required. The name of the policy to get, in the format
            ``projects/{project}/keys/{key}/policy``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdatePolicyRequest(proto.Message):
    r"""The request message to update a policy.

    Attributes:
        policy (google.cloud.recaptchaenterprise_v1.types.Policy):
            Required. The Policy's name is used to identify the policy
            to update, in the format
            ``projects/{project}/keys/{key}/policy``.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The mask to control which fields of
            the policy get updated. If the mask is not
            present, all fields are updated.
    """

    policy: "Policy" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Policy",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class Policy(proto.Message):
    r"""A complete configuration set containing multiple grouped
    rules defining the behavior of reCAPTCHA for fraud detection and
    prevention.

    Attributes:
        name (str):
            Identifier. Resource name for this policy.
            Format: "projects/{project}/keys/{key}/policy"
            for a policy under a key.
        client_settings (google.cloud.recaptchaenterprise_v1.types.ClientSettings):
            Required. Configuration for clients protected
            by this policy.
        challenge_rule_groups (MutableSequence[google.cloud.recaptchaenterprise_v1.types.ChallengeRuleGroup]):
            Optional. Rules to configure the behavior of
            reCAPTCHA for showing a challenge. Rule groups
            are evaluated in order. Evaluation stops when
            the first matching rule group is found.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    client_settings: "ClientSettings" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="ClientSettings",
    )
    challenge_rule_groups: MutableSequence["ChallengeRuleGroup"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="ChallengeRuleGroup",
    )


class ChallengeRuleGroup(proto.Message):
    r"""A collection of challenge rules that applies to one or more
    actions.

    Attributes:
        actions (MutableSequence[str]):
            Required. Action name provided at token generation. The
            action name is not case-sensitive and can only contain
            alphanumeric characters, slashes, and underscores. If "\*"
            is provided, the rule group applies to all actions. If
            multiple actions are provided, the rule group is applied to
            all of them. This field is required.
        challenge_rules (MutableSequence[google.cloud.recaptchaenterprise_v1.types.ChallengeRule]):
            Required. A list of rules that configure when
            and how reCAPTCHA presents a challenge.
            reCAPTCHA evaluates these rules in order and
            applies the first one that matches.
    """

    actions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    challenge_rules: MutableSequence["ChallengeRule"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="ChallengeRule",
    )


class ChallengeRule(proto.Message):
    r"""A rule to configure the behavior of reCAPTCHA for
    conditionally presenting a challenge.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        condition (str):
            Optional. A CEL condition that must be met for this rule to
            apply. If unspecified, the rule applies unconditionally. The
            following fields can be referenced in the condition:

            - ``score``
            - ``user_ip_address``
            - ``user_asn``
            - ``user_agent``
            - ``verified_bots.name``
            - ``verified_bots.bot_type``

            Examples:

            - ``score < 0.5``
            - ``user_ip_address == "123.45.67.89"``
            - ``user_agent.contains("Chrome")``
            - ``score < 0.5 && user_ip_address == "123.45.67.89"``
        no_challenge (google.cloud.recaptchaenterprise_v1.types.ChallengeRule.NoChallengeOutcome):
            Do not present a challenge to the user.

            This field is a member of `oneof`_ ``outcome``.
        challenge (google.cloud.recaptchaenterprise_v1.types.ChallengeRule.ChallengeOutcome):
            Present a challenge to the user.

            This field is a member of `oneof`_ ``outcome``.
    """

    class NoChallengeOutcome(proto.Message):
        r"""An outcome that indicates that no challenge should be
        presented to the user.

        """

    class ChallengeOutcome(proto.Message):
        r"""An outcome that indicates that a challenge of a specified
        difficulty should be presented to the user.

        Attributes:
            difficulty (google.cloud.recaptchaenterprise_v1.types.WebKeySettings.ChallengeSecurityPreference):
                Optional. The difficulty of the challenge to present to the
                user. If unspecified, ``BALANCE`` is used.
        """

        difficulty: "WebKeySettings.ChallengeSecurityPreference" = proto.Field(
            proto.ENUM,
            number=1,
            enum="WebKeySettings.ChallengeSecurityPreference",
        )

    condition: str = proto.Field(
        proto.STRING,
        number=1,
    )
    no_challenge: NoChallengeOutcome = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="outcome",
        message=NoChallengeOutcome,
    )
    challenge: ChallengeOutcome = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="outcome",
        message=ChallengeOutcome,
    )


class ClientSettings(proto.Message):
    r"""Configuration for clients to protect with reCAPTCHA.

    Attributes:
        allowed_domains (MutableSequence[str]):
            Optional. Domains or subdomains of websites allowed to use
            the policy. All subdomains of an allowed domain are
            automatically allowed. A valid domain requires a host and
            must not include any path, port, query or fragment.
            Examples: 'example.com' or 'subdomain.example.com' Each
            policy supports a maximum of 250 domains. To use a policy on
            more domains, set ``allow_all_domains`` to true. When this
            is set, you are responsible for validating the hostname by
            checking the ``token_properties.hostname`` field in each
            assessment response against your list of allowed domains.
        allow_all_domains (bool):
            Optional. If set to true, it means allowed_domains are not
            enforced.
        protected_endpoint_group (google.cloud.recaptchaenterprise_v1.types.ProtectedEndpointGroup):
            Optional. Configuration for all API endpoints
            to protect with reCAPTCHA. If this field is not
            set, reCAPTCHA will not automatically request
            tokens on any API endpoints.
    """

    allowed_domains: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    allow_all_domains: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    protected_endpoint_group: "ProtectedEndpointGroup" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ProtectedEndpointGroup",
    )


class ProtectedEndpointGroup(proto.Message):
    r"""Configuration for API endpoints to protect with reCAPTCHA.

    Attributes:
        protected_endpoints (MutableSequence[google.cloud.recaptchaenterprise_v1.types.ProtectedEndpoint]):
            Optional. List of API endpoints to
            automatically protect with reCAPTCHA. If any of
            these endpoints is invoked from a page where a
            key bound to this policy is installed, a
            reCAPTCHA token is automatically generated and
            attached to the request. If multiple protected
            endpoints match a given API endpoint, the first
            one in the list is used.
    """

    protected_endpoints: MutableSequence["ProtectedEndpoint"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ProtectedEndpoint",
    )


class ProtectedEndpoint(proto.Message):
    r"""Configuration for an API endpoint to protect with reCAPTCHA.

    Attributes:
        path (str):
            Required. URI path of the API endpoint to protect. Must
            start with '/'. Supports glob characters '*' to match a
            single path segment and '\*\*' to match multiple path
            segments. Standalone root catch-alls ('/*' and '/\*\*') are
            invalid because it can negatively impact performance to
            trigger reCAPTCHA on every single request to your backend.

            Matching is evaluated against the URL path only (domain,
            scheme, and query parameters are ignored).

            Examples:

            - ``/login`` matches ``/login``,
              ``https://example.com/login``, and ``/login?query=1``, but
              not ``/login/step1``.
            - ``/products/*`` matches ``/products/123``, but not
              ``/products/123/456``.
            - ``/content/**`` matches ``/content/articles/2024/01/01``.
        action (str):
            Required. Action name to be used for token
            generation for this endpoint. The action name
            can only contain alphanumeric characters,
            slashes, and underscores.
    """

    path: str = proto.Field(
        proto.STRING,
        number=1,
    )
    action: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
