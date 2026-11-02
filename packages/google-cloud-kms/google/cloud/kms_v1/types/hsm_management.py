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

import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.kms.v1",
    manifest={
        "SingleTenantHsmInstance",
        "SingleTenantHsmInstanceProposal",
        "Challenge",
        "ChallengeReply",
        "ListSingleTenantHsmInstancesRequest",
        "ListSingleTenantHsmInstancesResponse",
        "GetSingleTenantHsmInstanceRequest",
        "CreateSingleTenantHsmInstanceRequest",
        "CreateSingleTenantHsmInstanceMetadata",
        "CreateSingleTenantHsmInstanceProposalRequest",
        "CreateSingleTenantHsmInstanceProposalMetadata",
        "GetSingleTenantHsmInstanceProposalRequest",
        "ApproveSingleTenantHsmInstanceProposalRequest",
        "ApproveSingleTenantHsmInstanceProposalResponse",
        "ExecuteSingleTenantHsmInstanceProposalRequest",
        "ExecuteSingleTenantHsmInstanceProposalResponse",
        "ExecuteSingleTenantHsmInstanceProposalMetadata",
        "ListSingleTenantHsmInstanceProposalsRequest",
        "ListSingleTenantHsmInstanceProposalsResponse",
        "DeleteSingleTenantHsmInstanceProposalRequest",
    },
)


class SingleTenantHsmInstance(proto.Message):
    r"""A
    [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]
    represents a single-tenant HSM instance. It can be used for creating
    [CryptoKeys][google.cloud.kms.v1.CryptoKey] with a
    [ProtectionLevel][google.cloud.kms.v1.ProtectionLevel] of
    [HSM_SINGLE_TENANT][CryptoKeyVersion.ProtectionLevel.HSM_SINGLE_TENANT],
    as well as performing cryptographic operations using keys created
    within the
    [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance].

    Attributes:
        name (str):
            Identifier. The resource name for this
            [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]
            in the format
            ``projects/*/locations/*/singleTenantHsmInstances/*``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the
            [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]
            was created.
        state (google.cloud.kms_v1.types.SingleTenantHsmInstance.State):
            Output only. The state of the
            [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance].
        quorum_auth (google.cloud.kms_v1.types.SingleTenantHsmInstance.QuorumAuth):
            Required. The quorum auth configuration for the
            [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance].
        delete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the
            [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]
            was deleted.
        unrefreshed_duration_until_disable (google.protobuf.duration_pb2.Duration):
            Output only. The system-defined duration that
            an instance can remain unrefreshed until it is
            automatically disabled. This will have a value
            of 730 days.
        disable_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the instance will be
            automatically disabled if not refreshed. This field is
            updated upon creation and after each successful refresh
            operation and enable. A [RefreshSingleTenantHsmInstance][]
            operation must be made via a
            [SingleTenantHsmInstanceProposal][google.cloud.kms.v1.SingleTenantHsmInstanceProposal]
            before this time otherwise the
            [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]
            will become disabled.
        key_portability_enabled (bool):
            Optional. Immutable. Indicates whether key portability is
            enabled for the
            [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance].
            This can only be set at creation time. Key portability
            features are disabled by default.
    """

    class State(proto.Enum):
        r"""The set of states of a
        [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance].

        Values:
            STATE_UNSPECIFIED (0):
                Not specified.
            CREATING (1):
                The
                [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]
                is being created.
            PENDING_TWO_FACTOR_AUTH_REGISTRATION (2):
                The
                [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]
                is waiting for 2FA keys to be registered. This can be done
                by calling
                [CreateSingleTenantHsmInstanceProposal][google.cloud.kms.v1.HsmManagement.CreateSingleTenantHsmInstanceProposal]
                with the [RegisterTwoFactorAuthKeys][] operation.
            ACTIVE (3):
                The
                [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]
                is ready to use. A
                [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]
                must be in the
                [ACTIVE][google.cloud.kms.v1.SingleTenantHsmInstance.State.ACTIVE]
                state for all [CryptoKeys][google.cloud.kms.v1.CryptoKey]
                created within the
                [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]
                to be usable.
            DISABLING (4):
                The
                [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]
                is being disabled.
            DISABLED (5):
                The
                [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]
                is disabled.
            DELETING (6):
                The
                [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]
                is being deleted. Requests to the instance will be rejected
                in this state.
            DELETED (7):
                The
                [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]
                has been deleted.
            FAILED (8):
                The
                [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]
                has failed and can not be recovered or used.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        PENDING_TWO_FACTOR_AUTH_REGISTRATION = 2
        ACTIVE = 3
        DISABLING = 4
        DISABLED = 5
        DELETING = 6
        DELETED = 7
        FAILED = 8

    class QuorumAuth(proto.Message):
        r"""Configuration for M of N quorum auth.

        Attributes:
            total_approver_count (int):
                Required. The total number of approvers. This
                is the N value used for M of N quorum auth. Must
                be greater than or equal to 3 and less than or
                equal to 16.
            required_approver_count (int):
                Output only. The required numbers of approvers. The M value
                used for M of N quorum auth. Must be greater than or equal
                to 2 and less than or equal to
                [total_approver_count][google.cloud.kms.v1.SingleTenantHsmInstance.QuorumAuth.total_approver_count]

                -

                  1.
            two_factor_public_key_pems (MutableSequence[str]):
                Output only. The public keys associated with
                the 2FA keys for M of N quorum auth.
        """

        total_approver_count: int = proto.Field(
            proto.INT32,
            number=1,
        )
        required_approver_count: int = proto.Field(
            proto.INT32,
            number=2,
        )
        two_factor_public_key_pems: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=3,
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
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )
    quorum_auth: QuorumAuth = proto.Field(
        proto.MESSAGE,
        number=4,
        message=QuorumAuth,
    )
    delete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    unrefreshed_duration_until_disable: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=6,
        message=duration_pb2.Duration,
    )
    disable_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    key_portability_enabled: bool = proto.Field(
        proto.BOOL,
        number=8,
    )


class SingleTenantHsmInstanceProposal(proto.Message):
    r"""A
    [SingleTenantHsmInstanceProposal][google.cloud.kms.v1.SingleTenantHsmInstanceProposal]
    represents a proposal to perform an operation on a
    [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name for this
            [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]
            in the format
            ``projects/*/locations/*/singleTenantHsmInstances/*/proposals/*``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the
            [SingleTenantHsmInstanceProposal][google.cloud.kms.v1.SingleTenantHsmInstanceProposal]
            was created.
        state (google.cloud.kms_v1.types.SingleTenantHsmInstanceProposal.State):
            Output only. The state of the
            [SingleTenantHsmInstanceProposal][google.cloud.kms.v1.SingleTenantHsmInstanceProposal].
        failure_reason (str):
            Output only. The root cause of the most recent failure. Only
            present if
            [state][google.cloud.kms.v1.SingleTenantHsmInstanceProposal.state]
            is [FAILED][SingleTenantHsmInstanceProposal.FAILED].
        quorum_parameters (google.cloud.kms_v1.types.SingleTenantHsmInstanceProposal.QuorumParameters):
            Output only. The quorum approval parameters for the
            [SingleTenantHsmInstanceProposal][google.cloud.kms.v1.SingleTenantHsmInstanceProposal].

            This field is a member of `oneof`_ ``approval_parameters``.
        required_action_quorum_parameters (google.cloud.kms_v1.types.SingleTenantHsmInstanceProposal.RequiredActionQuorumParameters):
            Output only. Parameters for an approval of a
            [SingleTenantHsmInstanceProposal][google.cloud.kms.v1.SingleTenantHsmInstanceProposal]
            that has both required challenges and a quorum.

            This field is a member of `oneof`_ ``approval_parameters``.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            The time at which the
            [SingleTenantHsmInstanceProposal][google.cloud.kms.v1.SingleTenantHsmInstanceProposal]
            will expire if not approved and executed.

            This field is a member of `oneof`_ ``expiration``.
        ttl (google.protobuf.duration_pb2.Duration):
            Input only. The TTL for the
            [SingleTenantHsmInstanceProposal][google.cloud.kms.v1.SingleTenantHsmInstanceProposal].
            Proposals will expire after this duration.

            This field is a member of `oneof`_ ``expiration``.
        delete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the
            [SingleTenantHsmInstanceProposal][google.cloud.kms.v1.SingleTenantHsmInstanceProposal]
            was deleted.
        purge_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the soft-deleted
            [SingleTenantHsmInstanceProposal][google.cloud.kms.v1.SingleTenantHsmInstanceProposal]
            will be permanently purged. This field is only populated
            when the state is DELETED and will be set a time after
            expiration of the proposal, i.e. >= expire_time or
            (create_time + ttl).
        register_two_factor_auth_keys (google.cloud.kms_v1.types.SingleTenantHsmInstanceProposal.RegisterTwoFactorAuthKeys):
            Register 2FA keys for the
            [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance].
            This operation requires all N Challenges to be signed by 2FA
            keys. The
            [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]
            must be in the
            [PENDING_TWO_FACTOR_AUTH_REGISTRATION][google.cloud.kms.v1.SingleTenantHsmInstance.State.PENDING_TWO_FACTOR_AUTH_REGISTRATION]
            state to perform this operation.

            This field is a member of `oneof`_ ``operation``.
        disable_single_tenant_hsm_instance (google.cloud.kms_v1.types.SingleTenantHsmInstanceProposal.DisableSingleTenantHsmInstance):
            Disable the
            [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance].
            The
            [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]
            must be in the
            [ACTIVE][google.cloud.kms.v1.SingleTenantHsmInstance.State.ACTIVE]
            state to perform this operation.

            This field is a member of `oneof`_ ``operation``.
        enable_single_tenant_hsm_instance (google.cloud.kms_v1.types.SingleTenantHsmInstanceProposal.EnableSingleTenantHsmInstance):
            Enable the
            [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance].
            The
            [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]
            must be in the
            [DISABLED][google.cloud.kms.v1.SingleTenantHsmInstance.State.DISABLED]
            state to perform this operation.

            This field is a member of `oneof`_ ``operation``.
        delete_single_tenant_hsm_instance (google.cloud.kms_v1.types.SingleTenantHsmInstanceProposal.DeleteSingleTenantHsmInstance):
            Delete the
            [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance].
            Deleting a
            [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]
            will make all [CryptoKeys][google.cloud.kms.v1.CryptoKey]
            attached to the
            [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]
            unusable. The
            [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]
            must be in the
            [DISABLED][google.cloud.kms.v1.SingleTenantHsmInstance.State.DISABLED]
            or
            [PENDING_TWO_FACTOR_AUTH_REGISTRATION][google.cloud.kms.v1.SingleTenantHsmInstance.State.PENDING_TWO_FACTOR_AUTH_REGISTRATION]
            state to perform this operation.

            This field is a member of `oneof`_ ``operation``.
        add_quorum_member (google.cloud.kms_v1.types.SingleTenantHsmInstanceProposal.AddQuorumMember):
            Add a quorum member to the
            [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance].
            This will increase the
            [total_approver_count][google.cloud.kms.v1.SingleTenantHsmInstance.QuorumAuth.total_approver_count]
            by 1. The
            [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]
            must be in the
            [ACTIVE][google.cloud.kms.v1.SingleTenantHsmInstance.State.ACTIVE]
            state to perform this operation.

            This field is a member of `oneof`_ ``operation``.
        remove_quorum_member (google.cloud.kms_v1.types.SingleTenantHsmInstanceProposal.RemoveQuorumMember):
            Remove a quorum member from the
            [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance].
            This will reduce
            [total_approver_count][google.cloud.kms.v1.SingleTenantHsmInstance.QuorumAuth.total_approver_count]
            by 1. The
            [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]
            must be in the
            [ACTIVE][google.cloud.kms.v1.SingleTenantHsmInstance.State.ACTIVE]
            state to perform this operation.

            This field is a member of `oneof`_ ``operation``.
        refresh_single_tenant_hsm_instance (google.cloud.kms_v1.types.SingleTenantHsmInstanceProposal.RefreshSingleTenantHsmInstance):
            Refreshes the
            [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance].
            This operation must be performed periodically to keep the
            [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]
            active. This operation must be performed before
            [unrefreshed_duration_until_disable][google.cloud.kms.v1.SingleTenantHsmInstance.unrefreshed_duration_until_disable]
            has passed. The
            [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]
            must be in the
            [ACTIVE][google.cloud.kms.v1.SingleTenantHsmInstance.State.ACTIVE]
            state to perform this operation.

            This field is a member of `oneof`_ ``operation``.
        upgrade_key_trust (google.cloud.kms_v1.types.SingleTenantHsmInstanceProposal.UpgradeKeyTrust):
            Promotes a key with the AES_WRAPPING purpose to a trusted
            wrapping key. The key must be in the
            [ACTIVE][CryptoKeyVersion.CryptoKeyVersionState.ACTIVE]
            state to perform this operation.

            This field is a member of `oneof`_ ``operation``.
    """

    class State(proto.Enum):
        r"""The set of states of a
        [SingleTenantHsmInstanceProposal][google.cloud.kms.v1.SingleTenantHsmInstanceProposal].

        Values:
            STATE_UNSPECIFIED (0):
                Not specified.
            CREATING (1):
                The
                [SingleTenantHsmInstanceProposal][google.cloud.kms.v1.SingleTenantHsmInstanceProposal]
                is being created.
            PENDING (2):
                The
                [SingleTenantHsmInstanceProposal][google.cloud.kms.v1.SingleTenantHsmInstanceProposal]
                is pending approval.
            APPROVED (3):
                The
                [SingleTenantHsmInstanceProposal][google.cloud.kms.v1.SingleTenantHsmInstanceProposal]
                has been approved.
            RUNNING (4):
                The
                [SingleTenantHsmInstanceProposal][google.cloud.kms.v1.SingleTenantHsmInstanceProposal]
                is being executed.
            SUCCEEDED (5):
                The
                [SingleTenantHsmInstanceProposal][google.cloud.kms.v1.SingleTenantHsmInstanceProposal]
                has been executed successfully.
            FAILED (6):
                The
                [SingleTenantHsmInstanceProposal][google.cloud.kms.v1.SingleTenantHsmInstanceProposal]
                has failed.
            DELETED (7):
                The
                [SingleTenantHsmInstanceProposal][google.cloud.kms.v1.SingleTenantHsmInstanceProposal]
                has been deleted and will be purged after the purge_time.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        PENDING = 2
        APPROVED = 3
        RUNNING = 4
        SUCCEEDED = 5
        FAILED = 6
        DELETED = 7

    class QuorumParameters(proto.Message):
        r"""Parameters of quorum approval for the
        [SingleTenantHsmInstanceProposal][google.cloud.kms.v1.SingleTenantHsmInstanceProposal].

        Attributes:
            required_approver_count (int):
                Output only. The required numbers of
                approvers. This is the M value used for M of N
                quorum auth. It is less than the number of
                public keys.
            challenges (MutableSequence[google.cloud.kms_v1.types.Challenge]):
                Output only. The challenges to be signed by
                2FA keys for quorum auth. M of N of these
                challenges are required to be signed to approve
                the operation.
            approved_two_factor_public_key_pems (MutableSequence[str]):
                Output only. The public keys associated with the 2FA keys
                that have already approved the
                [SingleTenantHsmInstanceProposal][google.cloud.kms.v1.SingleTenantHsmInstanceProposal]
                by signing the challenge.
        """

        required_approver_count: int = proto.Field(
            proto.INT32,
            number=1,
        )
        challenges: MutableSequence["Challenge"] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="Challenge",
        )
        approved_two_factor_public_key_pems: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=3,
        )

    class RequiredActionQuorumParameters(proto.Message):
        r"""Parameters for an approval that has both required challenges
        and a quorum.

        Attributes:
            required_challenges (MutableSequence[google.cloud.kms_v1.types.Challenge]):
                Output only. A list of specific challenges
                that must be signed. For some operations, this
                will contain a single challenge.
            required_approver_count (int):
                Output only. The required number of quorum
                approvers. This is the M value used for M of N
                quorum auth. It is less than the number of
                public keys.
            quorum_challenges (MutableSequence[google.cloud.kms_v1.types.Challenge]):
                Output only. The challenges to be signed by
                2FA keys for quorum auth. M of N of these
                challenges are required to be signed to approve
                the operation.
            approved_two_factor_public_key_pems (MutableSequence[str]):
                Output only. The public keys associated with the 2FA keys
                that have already approved the
                [SingleTenantHsmInstanceProposal][google.cloud.kms.v1.SingleTenantHsmInstanceProposal]
                by signing the challenge.
        """

        required_challenges: MutableSequence["Challenge"] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="Challenge",
        )
        required_approver_count: int = proto.Field(
            proto.INT32,
            number=2,
        )
        quorum_challenges: MutableSequence["Challenge"] = proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="Challenge",
        )
        approved_two_factor_public_key_pems: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=4,
        )

    class RegisterTwoFactorAuthKeys(proto.Message):
        r"""Register 2FA keys for the
        [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance].
        This operation requires all Challenges to be signed by 2FA keys. The
        [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]
        must be in the
        [PENDING_TWO_FACTOR_AUTH_REGISTRATION][google.cloud.kms.v1.SingleTenantHsmInstance.State.PENDING_TWO_FACTOR_AUTH_REGISTRATION]
        state to perform this operation.

        Attributes:
            required_approver_count (int):
                Required. The required numbers of approvers to set for the
                [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance].
                This is the M value used for M of N quorum auth. Must be
                greater than or equal to 2 and less than or equal to
                [total_approver_count][google.cloud.kms.v1.SingleTenantHsmInstance.QuorumAuth.total_approver_count]

                -

                  1.
            two_factor_public_key_pems (MutableSequence[str]):
                Required. The public keys associated with the
                2FA keys for M of N quorum auth. Public keys
                must be associated with RSA 2048 keys.
        """

        required_approver_count: int = proto.Field(
            proto.INT32,
            number=1,
        )
        two_factor_public_key_pems: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )

    class DisableSingleTenantHsmInstance(proto.Message):
        r"""Disable the
        [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance].
        The
        [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]
        must be in the
        [ACTIVE][google.cloud.kms.v1.SingleTenantHsmInstance.State.ACTIVE]
        state to perform this operation.

        """

    class EnableSingleTenantHsmInstance(proto.Message):
        r"""Enable the
        [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance].
        The
        [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]
        must be in the
        [DISABLED][google.cloud.kms.v1.SingleTenantHsmInstance.State.DISABLED]
        state to perform this operation.

        """

    class DeleteSingleTenantHsmInstance(proto.Message):
        r"""Delete the
        [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance].
        Deleting a
        [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]
        will make all [CryptoKeys][google.cloud.kms.v1.CryptoKey] attached
        to the
        [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]
        unusable. The
        [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]
        must not be in the
        [DELETING][google.cloud.kms.v1.SingleTenantHsmInstance.State.DELETING]
        or
        [DELETED][google.cloud.kms.v1.SingleTenantHsmInstance.State.DELETED]
        state to perform this operation.

        """

    class AddQuorumMember(proto.Message):
        r"""Add a quorum member to the
        [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance].
        This will increase the
        [total_approver_count][google.cloud.kms.v1.SingleTenantHsmInstance.QuorumAuth.total_approver_count]
        by 1. The
        [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]
        must be in the
        [ACTIVE][google.cloud.kms.v1.SingleTenantHsmInstance.State.ACTIVE]
        state to perform this operation.

        Attributes:
            two_factor_public_key_pem (str):
                Required. The public key associated with the
                2FA key for the new quorum member to add. Public
                keys must be associated with RSA 2048 keys.
        """

        two_factor_public_key_pem: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class RemoveQuorumMember(proto.Message):
        r"""Remove a quorum member from the
        [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance].
        This will reduce
        [total_approver_count][google.cloud.kms.v1.SingleTenantHsmInstance.QuorumAuth.total_approver_count]
        by 1. The
        [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]
        must be in the
        [ACTIVE][google.cloud.kms.v1.SingleTenantHsmInstance.State.ACTIVE]
        state to perform this operation.

        Attributes:
            two_factor_public_key_pem (str):
                Required. The public key associated with the
                2FA key for the quorum member to remove. Public
                keys must be associated with RSA 2048 keys.
        """

        two_factor_public_key_pem: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class RefreshSingleTenantHsmInstance(proto.Message):
        r"""Refreshes the
        [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance].
        This operation must be performed periodically to keep the
        [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]
        active. This operation must be performed before
        [unrefreshed_duration_until_disable][google.cloud.kms.v1.SingleTenantHsmInstance.unrefreshed_duration_until_disable]
        has passed. The
        [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]
        must be in the
        [ACTIVE][google.cloud.kms.v1.SingleTenantHsmInstance.State.ACTIVE]
        state to perform this operation.

        """

    class UpgradeKeyTrust(proto.Message):
        r"""Promotes a key with the AES_WRAPPING purpose to a trusted wrapping
        key. The key must be in the
        [ACTIVE][CryptoKeyVersion.CryptoKeyVersionState.ACTIVE] state to
        perform this operation.

        Attributes:
            name (str):
                Required. The
                [name][google.cloud.kms.v1.CryptoKeyVersion.name] of the
                [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] to
                promote.
            two_factor_public_key_pem (str):
                Required. The public key associated with the
                2FA key that will sign the login nonce for this
                operation.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        two_factor_public_key_pem: str = proto.Field(
            proto.STRING,
            number=2,
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
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )
    failure_reason: str = proto.Field(
        proto.STRING,
        number=4,
    )
    quorum_parameters: QuorumParameters = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="approval_parameters",
        message=QuorumParameters,
    )
    required_action_quorum_parameters: RequiredActionQuorumParameters = proto.Field(
        proto.MESSAGE,
        number=14,
        oneof="approval_parameters",
        message=RequiredActionQuorumParameters,
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="expiration",
        message=timestamp_pb2.Timestamp,
    )
    ttl: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="expiration",
        message=duration_pb2.Duration,
    )
    delete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=15,
        message=timestamp_pb2.Timestamp,
    )
    purge_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=16,
        message=timestamp_pb2.Timestamp,
    )
    register_two_factor_auth_keys: RegisterTwoFactorAuthKeys = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="operation",
        message=RegisterTwoFactorAuthKeys,
    )
    disable_single_tenant_hsm_instance: DisableSingleTenantHsmInstance = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="operation",
        message=DisableSingleTenantHsmInstance,
    )
    enable_single_tenant_hsm_instance: EnableSingleTenantHsmInstance = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="operation",
        message=EnableSingleTenantHsmInstance,
    )
    delete_single_tenant_hsm_instance: DeleteSingleTenantHsmInstance = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="operation",
        message=DeleteSingleTenantHsmInstance,
    )
    add_quorum_member: AddQuorumMember = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="operation",
        message=AddQuorumMember,
    )
    remove_quorum_member: RemoveQuorumMember = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="operation",
        message=RemoveQuorumMember,
    )
    refresh_single_tenant_hsm_instance: RefreshSingleTenantHsmInstance = proto.Field(
        proto.MESSAGE,
        number=17,
        oneof="operation",
        message=RefreshSingleTenantHsmInstance,
    )
    upgrade_key_trust: UpgradeKeyTrust = proto.Field(
        proto.MESSAGE,
        number=18,
        oneof="operation",
        message=UpgradeKeyTrust,
    )


class Challenge(proto.Message):
    r"""A challenge to be signed by a 2FA key.

    Attributes:
        challenge (bytes):
            Output only. The challenge to be signed by
            the 2FA key indicated by the public key.
        public_key_pem (str):
            Output only. The public key associated with
            the 2FA key that should sign the challenge.
    """

    challenge: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )
    public_key_pem: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ChallengeReply(proto.Message):
    r"""A reply to a challenge signed by a 2FA key.

    Attributes:
        signed_challenge (bytes):
            Required. The signed challenge associated
            with the 2FA key. The signature must be
            RSASSA-PKCS1 v1.5 with a SHA256 digest.
        public_key_pem (str):
            Required. The public key associated with the
            2FA key.
    """

    signed_challenge: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )
    public_key_pem: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListSingleTenantHsmInstancesRequest(proto.Message):
    r"""Request message for
    [HsmManagement.ListSingleTenantHsmInstances][google.cloud.kms.v1.HsmManagement.ListSingleTenantHsmInstances].

    Attributes:
        parent (str):
            Required. The resource name of the location associated with
            the
            [SingleTenantHsmInstances][google.cloud.kms.v1.SingleTenantHsmInstance]
            to list, in the format ``projects/*/locations/*``.
        page_size (int):
            Optional. Optional limit on the number of
            [SingleTenantHsmInstances][google.cloud.kms.v1.SingleTenantHsmInstance]
            to include in the response. Further
            [SingleTenantHsmInstances][google.cloud.kms.v1.SingleTenantHsmInstance]
            can subsequently be obtained by including the
            [ListSingleTenantHsmInstancesResponse.next_page_token][google.cloud.kms.v1.ListSingleTenantHsmInstancesResponse.next_page_token]
            in a subsequent request. If unspecified, the server will
            pick an appropriate default.
        page_token (str):
            Optional. Optional pagination token, returned earlier via
            [ListSingleTenantHsmInstancesResponse.next_page_token][google.cloud.kms.v1.ListSingleTenantHsmInstancesResponse.next_page_token].
        filter (str):
            Optional. Only include resources that match the filter in
            the response. For more information, see `Sorting and
            filtering list
            results <https://cloud.google.com/kms/docs/sorting-and-filtering>`__.
        order_by (str):
            Optional. Specify how the results should be sorted. If not
            specified, the results will be sorted in the default order.
            For more information, see `Sorting and filtering list
            results <https://cloud.google.com/kms/docs/sorting-and-filtering>`__.
        show_deleted (bool):
            Optional. If set to true,
            [HsmManagement.ListSingleTenantHsmInstances][google.cloud.kms.v1.HsmManagement.ListSingleTenantHsmInstances]
            will also return
            [SingleTenantHsmInstances][google.cloud.kms.v1.SingleTenantHsmInstance]
            in DELETED state.
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
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )
    show_deleted: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


class ListSingleTenantHsmInstancesResponse(proto.Message):
    r"""Response message for
    [HsmManagement.ListSingleTenantHsmInstances][google.cloud.kms.v1.HsmManagement.ListSingleTenantHsmInstances].

    Attributes:
        single_tenant_hsm_instances (MutableSequence[google.cloud.kms_v1.types.SingleTenantHsmInstance]):
            The list of
            [SingleTenantHsmInstances][google.cloud.kms.v1.SingleTenantHsmInstance].
        next_page_token (str):
            A token to retrieve next page of results. Pass this value in
            [ListSingleTenantHsmInstancesRequest.page_token][google.cloud.kms.v1.ListSingleTenantHsmInstancesRequest.page_token]
            to retrieve the next page of results.
        total_size (int):
            The total number of
            [SingleTenantHsmInstances][google.cloud.kms.v1.SingleTenantHsmInstance]
            that matched the query.

            This field is not populated if
            [ListSingleTenantHsmInstancesRequest.filter][google.cloud.kms.v1.ListSingleTenantHsmInstancesRequest.filter]
            is applied.
    """

    @property
    def raw_page(self):
        return self

    single_tenant_hsm_instances: MutableSequence["SingleTenantHsmInstance"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="SingleTenantHsmInstance",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class GetSingleTenantHsmInstanceRequest(proto.Message):
    r"""Request message for
    [HsmManagement.GetSingleTenantHsmInstance][google.cloud.kms.v1.HsmManagement.GetSingleTenantHsmInstance].

    Attributes:
        name (str):
            Required. The
            [name][google.cloud.kms.v1.SingleTenantHsmInstance.name] of
            the
            [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]
            to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateSingleTenantHsmInstanceRequest(proto.Message):
    r"""Request message for
    [HsmManagement.CreateSingleTenantHsmInstance][google.cloud.kms.v1.HsmManagement.CreateSingleTenantHsmInstance].

    Attributes:
        parent (str):
            Required. The resource name of the location associated with
            the
            [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance],
            in the format ``projects/*/locations/*``.
        single_tenant_hsm_instance_id (str):
            Optional. It must be unique within a location and match the
            regular expression ``[a-zA-Z0-9_-]{1,63}``.
        single_tenant_hsm_instance (google.cloud.kms_v1.types.SingleTenantHsmInstance):
            Required. An
            [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]
            with initial field values.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    single_tenant_hsm_instance_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    single_tenant_hsm_instance: "SingleTenantHsmInstance" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="SingleTenantHsmInstance",
    )


class CreateSingleTenantHsmInstanceMetadata(proto.Message):
    r"""Metadata message for
    [CreateSingleTenantHsmInstance][google.cloud.kms.v1.HsmManagement.CreateSingleTenantHsmInstance]
    long-running operation response.

    """


class CreateSingleTenantHsmInstanceProposalRequest(proto.Message):
    r"""Request message for
    [HsmManagement.CreateSingleTenantHsmInstanceProposal][google.cloud.kms.v1.HsmManagement.CreateSingleTenantHsmInstanceProposal].

    Attributes:
        parent (str):
            Required. The
            [name][google.cloud.kms.v1.SingleTenantHsmInstance.name] of
            the
            [SingleTenantHsmInstance][google.cloud.kms.v1.SingleTenantHsmInstance]
            associated with the
            [SingleTenantHsmInstanceProposals][google.cloud.kms.v1.SingleTenantHsmInstanceProposal].
        single_tenant_hsm_instance_proposal_id (str):
            Optional. It must be unique within a location and match the
            regular expression ``[a-zA-Z0-9_-]{1,63}``.
        single_tenant_hsm_instance_proposal (google.cloud.kms_v1.types.SingleTenantHsmInstanceProposal):
            Required. The
            [SingleTenantHsmInstanceProposal][google.cloud.kms.v1.SingleTenantHsmInstanceProposal]
            to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    single_tenant_hsm_instance_proposal_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    single_tenant_hsm_instance_proposal: "SingleTenantHsmInstanceProposal" = (
        proto.Field(
            proto.MESSAGE,
            number=3,
            message="SingleTenantHsmInstanceProposal",
        )
    )


class CreateSingleTenantHsmInstanceProposalMetadata(proto.Message):
    r"""Metadata message for
    [CreateSingleTenantHsmInstanceProposal][google.cloud.kms.v1.HsmManagement.CreateSingleTenantHsmInstanceProposal]
    long-running operation response.

    """


class GetSingleTenantHsmInstanceProposalRequest(proto.Message):
    r"""Request message for
    [HsmManagement.GetSingleTenantHsmInstanceProposal][google.cloud.kms.v1.HsmManagement.GetSingleTenantHsmInstanceProposal].

    Attributes:
        name (str):
            Required. The
            [name][google.cloud.kms.v1.SingleTenantHsmInstanceProposal.name]
            of the
            [SingleTenantHsmInstanceProposal][google.cloud.kms.v1.SingleTenantHsmInstanceProposal]
            to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ApproveSingleTenantHsmInstanceProposalRequest(proto.Message):
    r"""Request message for
    [HsmManagement.ApproveSingleTenantHsmInstanceProposal][google.cloud.kms.v1.HsmManagement.ApproveSingleTenantHsmInstanceProposal].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. The
            [name][google.cloud.kms.v1.SingleTenantHsmInstanceProposal.name]
            of the
            [SingleTenantHsmInstanceProposal][google.cloud.kms.v1.SingleTenantHsmInstanceProposal]
            to approve.
        quorum_reply (google.cloud.kms_v1.types.ApproveSingleTenantHsmInstanceProposalRequest.QuorumReply):
            Required. The reply to
            [QuorumParameters][google.cloud.kms.v1.SingleTenantHsmInstanceProposal.QuorumParameters]
            for approving the proposal.

            This field is a member of `oneof`_ ``approval_payload``.
        required_action_quorum_reply (google.cloud.kms_v1.types.ApproveSingleTenantHsmInstanceProposalRequest.RequiredActionQuorumReply):
            Required. The reply to
            [RequiredActionQuorumParameters][google.cloud.kms.v1.SingleTenantHsmInstanceProposal.RequiredActionQuorumParameters]
            for approving the proposal.

            This field is a member of `oneof`_ ``approval_payload``.
    """

    class QuorumReply(proto.Message):
        r"""The reply to
        [QuorumParameters][google.cloud.kms.v1.SingleTenantHsmInstanceProposal.QuorumParameters]
        for approving the proposal.

        Attributes:
            challenge_replies (MutableSequence[google.cloud.kms_v1.types.ChallengeReply]):
                Required. The challenge replies to approve the proposal.
                Challenge replies can be sent across multiple requests. The
                proposal will be approved when
                [required_approver_count][google.cloud.kms.v1.SingleTenantHsmInstanceProposal.QuorumParameters.required_approver_count]
                challenge replies are provided.
        """

        challenge_replies: MutableSequence["ChallengeReply"] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="ChallengeReply",
        )

    class RequiredActionQuorumReply(proto.Message):
        r"""The reply to
        [RequiredActionQuorumParameters][google.cloud.kms.v1.SingleTenantHsmInstanceProposal.RequiredActionQuorumParameters]
        for approving the proposal.

        Attributes:
            required_challenge_replies (MutableSequence[google.cloud.kms_v1.types.ChallengeReply]):
                Required. All required challenges must be
                signed for the proposal to be approved. These
                can be sent across multiple requests.
            quorum_challenge_replies (MutableSequence[google.cloud.kms_v1.types.ChallengeReply]):
                Required. Quorum members' signed challenge replies. These
                can be provided across multiple requests. The proposal will
                be approved when
                [required_approver_count][google.cloud.kms.v1.SingleTenantHsmInstanceProposal.RequiredActionQuorumParameters.required_approver_count]
                quorum_challenge_replies are provided and when all
                required_challenge_replies are provided.
        """

        required_challenge_replies: MutableSequence["ChallengeReply"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message="ChallengeReply",
            )
        )
        quorum_challenge_replies: MutableSequence["ChallengeReply"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="ChallengeReply",
            )
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    quorum_reply: QuorumReply = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="approval_payload",
        message=QuorumReply,
    )
    required_action_quorum_reply: RequiredActionQuorumReply = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="approval_payload",
        message=RequiredActionQuorumReply,
    )


class ApproveSingleTenantHsmInstanceProposalResponse(proto.Message):
    r"""Response message for
    [HsmManagement.ApproveSingleTenantHsmInstanceProposal][google.cloud.kms.v1.HsmManagement.ApproveSingleTenantHsmInstanceProposal].

    """


class ExecuteSingleTenantHsmInstanceProposalRequest(proto.Message):
    r"""Request message for
    [HsmManagement.ExecuteSingleTenantHsmInstanceProposal][google.cloud.kms.v1.HsmManagement.ExecuteSingleTenantHsmInstanceProposal].

    Attributes:
        name (str):
            Required. The
            [name][google.cloud.kms.v1.SingleTenantHsmInstanceProposal.name]
            of the
            [SingleTenantHsmInstanceProposal][google.cloud.kms.v1.SingleTenantHsmInstanceProposal]
            to execute.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ExecuteSingleTenantHsmInstanceProposalResponse(proto.Message):
    r"""Response message for
    [HsmManagement.ExecuteSingleTenantHsmInstanceProposal][google.cloud.kms.v1.HsmManagement.ExecuteSingleTenantHsmInstanceProposal].

    """


class ExecuteSingleTenantHsmInstanceProposalMetadata(proto.Message):
    r"""Metadata message for
    [ExecuteSingleTenantHsmInstanceProposal][google.cloud.kms.v1.HsmManagement.ExecuteSingleTenantHsmInstanceProposal]
    long-running operation response.

    """


class ListSingleTenantHsmInstanceProposalsRequest(proto.Message):
    r"""Request message for
    [HsmManagement.ListSingleTenantHsmInstanceProposals][google.cloud.kms.v1.HsmManagement.ListSingleTenantHsmInstanceProposals].

    Attributes:
        parent (str):
            Required. The resource name of the single tenant HSM
            instance associated with the
            [SingleTenantHsmInstanceProposals][google.cloud.kms.v1.SingleTenantHsmInstanceProposal]
            to list, in the format
            ``projects/*/locations/*/singleTenantHsmInstances/*``.
        page_size (int):
            Optional. Optional limit on the number of
            [SingleTenantHsmInstanceProposals][google.cloud.kms.v1.SingleTenantHsmInstanceProposal]
            to include in the response. Further
            [SingleTenantHsmInstanceProposals][google.cloud.kms.v1.SingleTenantHsmInstanceProposal]
            can subsequently be obtained by including the
            [ListSingleTenantHsmInstanceProposalsResponse.next_page_token][google.cloud.kms.v1.ListSingleTenantHsmInstanceProposalsResponse.next_page_token]
            in a subsequent request. If unspecified, the server will
            pick an appropriate default.
        page_token (str):
            Optional. Optional pagination token, returned earlier via
            [ListSingleTenantHsmInstanceProposalsResponse.next_page_token][google.cloud.kms.v1.ListSingleTenantHsmInstanceProposalsResponse.next_page_token].
        filter (str):
            Optional. Only include resources that match the filter in
            the response. For more information, see `Sorting and
            filtering list
            results <https://cloud.google.com/kms/docs/sorting-and-filtering>`__.
        order_by (str):
            Optional. Specify how the results should be sorted. If not
            specified, the results will be sorted in the default order.
            For more information, see `Sorting and filtering list
            results <https://cloud.google.com/kms/docs/sorting-and-filtering>`__.
        show_deleted (bool):
            Optional. If set to true,
            [HsmManagement.ListSingleTenantHsmInstanceProposals][google.cloud.kms.v1.HsmManagement.ListSingleTenantHsmInstanceProposals]
            will also return
            [SingleTenantHsmInstanceProposals][google.cloud.kms.v1.SingleTenantHsmInstanceProposal]
            in DELETED state.
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
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )
    show_deleted: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


class ListSingleTenantHsmInstanceProposalsResponse(proto.Message):
    r"""Response message for
    [HsmManagement.ListSingleTenantHsmInstanceProposals][google.cloud.kms.v1.HsmManagement.ListSingleTenantHsmInstanceProposals].

    Attributes:
        single_tenant_hsm_instance_proposals (MutableSequence[google.cloud.kms_v1.types.SingleTenantHsmInstanceProposal]):
            The list of
            [SingleTenantHsmInstanceProposals][google.cloud.kms.v1.SingleTenantHsmInstanceProposal].
        next_page_token (str):
            A token to retrieve next page of results. Pass this value in
            [ListSingleTenantHsmInstanceProposalsRequest.page_token][google.cloud.kms.v1.ListSingleTenantHsmInstanceProposalsRequest.page_token]
            to retrieve the next page of results.
        total_size (int):
            The total number of
            [SingleTenantHsmInstanceProposals][google.cloud.kms.v1.SingleTenantHsmInstanceProposal]
            that matched the query.

            This field is not populated if
            [ListSingleTenantHsmInstanceProposalsRequest.filter][google.cloud.kms.v1.ListSingleTenantHsmInstanceProposalsRequest.filter]
            is applied.
    """

    @property
    def raw_page(self):
        return self

    single_tenant_hsm_instance_proposals: MutableSequence[
        "SingleTenantHsmInstanceProposal"
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SingleTenantHsmInstanceProposal",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class DeleteSingleTenantHsmInstanceProposalRequest(proto.Message):
    r"""Request message for
    [HsmManagement.DeleteSingleTenantHsmInstanceProposal][google.cloud.kms.v1.HsmManagement.DeleteSingleTenantHsmInstanceProposal].

    Attributes:
        name (str):
            Required. The
            [name][google.cloud.kms.v1.SingleTenantHsmInstanceProposal.name]
            of the
            [SingleTenantHsmInstanceProposal][google.cloud.kms.v1.SingleTenantHsmInstanceProposal]
            to delete.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
