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

import google.iam.v1.resource_policy_member_pb2 as resource_policy_member_pb2  # type: ignore
import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.secretmanager.v1",
    manifest={
        "Secret",
        "SecretVersion",
        "Replication",
        "CustomerManagedEncryption",
        "ReplicationStatus",
        "CustomerManagedEncryptionStatus",
        "Topic",
        "Rotation",
        "SecretPayload",
    },
)


class Secret(proto.Message):
    r"""A [Secret][google.cloud.secretmanager.v1.Secret] is a logical secret
    whose value and versions can be accessed.

    A [Secret][google.cloud.secretmanager.v1.Secret] is made up of zero
    or more
    [SecretVersions][google.cloud.secretmanager.v1.SecretVersion] that
    represent the secret data.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. The resource name of the
            [Secret][google.cloud.secretmanager.v1.Secret] in the format
            ``projects/*/secrets/*``.
        replication (google.cloud.secretmanager_v1.types.Replication):
            Optional. Immutable. The replication policy of the secret
            data attached to the
            [Secret][google.cloud.secretmanager.v1.Secret].

            The replication policy cannot be changed after the Secret
            has been created.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the
            [Secret][google.cloud.secretmanager.v1.Secret] was created.
        labels (MutableMapping[str, str]):
            The labels assigned to this Secret.

            Label keys must be between 1 and 63 characters long, have a
            UTF-8 encoding of maximum 128 bytes, and must conform to the
            following PCRE regular expression:
            ``[\p{Ll}\p{Lo}][\p{Ll}\p{Lo}\p{N}_-]{0,62}``

            Label values must be between 0 and 63 characters long, have
            a UTF-8 encoding of maximum 128 bytes, and must conform to
            the following PCRE regular expression:
            ``[\p{Ll}\p{Lo}\p{N}_-]{0,63}``

            No more than 64 labels can be assigned to a given resource.
        topics (MutableSequence[google.cloud.secretmanager_v1.types.Topic]):
            Optional. A list of up to 10 Pub/Sub topics
            to which messages are published when control
            plane operations are called on the secret or its
            versions.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. Timestamp in UTC when the
            [Secret][google.cloud.secretmanager.v1.Secret] is scheduled
            to expire. This is always provided on output, regardless of
            what was sent on input.

            This field is a member of `oneof`_ ``expiration``.
        ttl (google.protobuf.duration_pb2.Duration):
            Input only. The TTL for the
            [Secret][google.cloud.secretmanager.v1.Secret].

            This field is a member of `oneof`_ ``expiration``.
        etag (str):
            Optional. Etag of the currently stored
            [Secret][google.cloud.secretmanager.v1.Secret].
        rotation (google.cloud.secretmanager_v1.types.Rotation):
            Optional. Rotation policy attached to the
            [Secret][google.cloud.secretmanager.v1.Secret]. May be
            excluded if there is no rotation policy.
        version_aliases (MutableMapping[str, int]):
            Optional. Mapping from version alias to version name.

            A version alias is a string with a maximum length of 63
            characters and can contain uppercase and lowercase letters,
            numerals, and the hyphen (``-``) and underscore ('\_')
            characters. An alias string must start with a letter and
            cannot be the string 'latest' or 'NEW'. No more than 50
            aliases can be assigned to a given secret.

            Version-Alias pairs will be viewable via GetSecret and
            modifiable via UpdateSecret. Access by alias is only be
            supported on GetSecretVersion and AccessSecretVersion.
        annotations (MutableMapping[str, str]):
            Optional. Custom metadata about the secret.

            Annotations are distinct from various forms of labels.
            Annotations exist to allow client tools to store their own
            state information without requiring a database.

            Annotation keys must be between 1 and 63 characters long,
            have a UTF-8 encoding of maximum 128 bytes, begin and end
            with an alphanumeric character ([a-z0-9A-Z]), and may have
            dashes (-), underscores (\_), dots (.), and alphanumerics in
            between these symbols.

            The total size of annotation keys and values must be less
            than 16KiB.
        version_destroy_ttl (google.protobuf.duration_pb2.Duration):
            Optional. Secret Version TTL after
            destruction request
            This is a part of the Delayed secret version
            destroy feature. For secret with TTL>0, version
            destruction doesn't happen immediately on
            calling destroy instead the version goes to a
            disabled state and destruction happens after the
            TTL expires.
        customer_managed_encryption (google.cloud.secretmanager_v1.types.CustomerManagedEncryption):
            Optional. The customer-managed encryption configuration of
            the regionalized secrets. If no configuration is provided,
            Google-managed default encryption is used.

            Updates to the
            [Secret][google.cloud.secretmanager.v1.Secret] encryption
            configuration only apply to
            [SecretVersions][google.cloud.secretmanager.v1.SecretVersion]
            added afterwards. They do not apply retroactively to
            existing
            [SecretVersions][google.cloud.secretmanager.v1.SecretVersion].
        tags (MutableMapping[str, str]):
            Optional. Input only. Immutable. Mapping of
            Tag keys/values directly bound to this resource.
            For example:

              "123/environment": "production",
              "123/costCenter": "marketing"

            Tags are used to organize and group resources.

            Tags can be used to control policy evaluation
            for the resource.
        secret_type (google.cloud.secretmanager_v1.types.Secret.SecretType):
            Optional. Immutable. This defines the type of the secret.
            Enforces certain structural requirements on the
            [SecretVersions][google.cloud.secretmanager.v1.SecretVersion].
            For secret of type UNSPECIFIED, the SecretVersions can be of
            any type.
        policy_member (google.iam.v1.resource_policy_member_pb2.ResourcePolicyMember):
            Output only. Defines the policy member for
            the secret. This will be used to check if the
            caller has the permission to perform certain
            operations on the typed secret.
    """

    class SecretType(proto.Enum):
        r"""This defines the various values of the type of secret can be.

        Values:
            SECRET_TYPE_UNSPECIFIED (0):
                Applicable to all secrets which do not have
                any restriction on the SecretVersions.
            CLOUD_SQL_DB_CREDENTIALS (1):
                Applicable to secrets which are used for the
                managed rotation feature for Cloud SQL Single
                User.
            ACCESS_KEY (2):
                Applicable to secrets where the payload
                contains an access key.
            CERTIFICATE (3):
                Applicable to secrets where the payload
                contains a certificate.
            OTHER_DB_CREDENTIALS (4):
                Applicable to secrets where the payload
                contains database credentials.
            OTHER (50):
                Applicable to secrets whose type doesn't
                belong to any of the above defined types.
        """

        SECRET_TYPE_UNSPECIFIED = 0
        CLOUD_SQL_DB_CREDENTIALS = 1
        ACCESS_KEY = 2
        CERTIFICATE = 3
        OTHER_DB_CREDENTIALS = 4
        OTHER = 50

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    replication: "Replication" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Replication",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    topics: MutableSequence["Topic"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="Topic",
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
    etag: str = proto.Field(
        proto.STRING,
        number=8,
    )
    rotation: "Rotation" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="Rotation",
    )
    version_aliases: MutableMapping[str, int] = proto.MapField(
        proto.STRING,
        proto.INT64,
        number=11,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=13,
    )
    version_destroy_ttl: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=14,
        message=duration_pb2.Duration,
    )
    customer_managed_encryption: "CustomerManagedEncryption" = proto.Field(
        proto.MESSAGE,
        number=15,
        message="CustomerManagedEncryption",
    )
    tags: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=16,
    )
    secret_type: SecretType = proto.Field(
        proto.ENUM,
        number=17,
        enum=SecretType,
    )
    policy_member: resource_policy_member_pb2.ResourcePolicyMember = proto.Field(
        proto.MESSAGE,
        number=18,
        message=resource_policy_member_pb2.ResourcePolicyMember,
    )


class SecretVersion(proto.Message):
    r"""A secret version resource in the Secret Manager API.

    Attributes:
        name (str):
            Output only. The resource name of the
            [SecretVersion][google.cloud.secretmanager.v1.SecretVersion]
            in the format ``projects/*/secrets/*/versions/*``.

            [SecretVersion][google.cloud.secretmanager.v1.SecretVersion]
            IDs in a [Secret][google.cloud.secretmanager.v1.Secret]
            start at 1 and are incremented for each subsequent version
            of the secret.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the
            [SecretVersion][google.cloud.secretmanager.v1.SecretVersion]
            was created.
        destroy_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time this
            [SecretVersion][google.cloud.secretmanager.v1.SecretVersion]
            was destroyed. Only present if
            [state][google.cloud.secretmanager.v1.SecretVersion.state]
            is
            [DESTROYED][google.cloud.secretmanager.v1.SecretVersion.State.DESTROYED].
        state (google.cloud.secretmanager_v1.types.SecretVersion.State):
            Output only. The current state of the
            [SecretVersion][google.cloud.secretmanager.v1.SecretVersion].
        replication_status (google.cloud.secretmanager_v1.types.ReplicationStatus):
            The replication status of the
            [SecretVersion][google.cloud.secretmanager.v1.SecretVersion].
        etag (str):
            Output only. Etag of the currently stored
            [SecretVersion][google.cloud.secretmanager.v1.SecretVersion].
        client_specified_payload_checksum (bool):
            Output only. True if payload checksum specified in
            [SecretPayload][google.cloud.secretmanager.v1.SecretPayload]
            object has been received by
            [SecretManagerService][google.cloud.secretmanager.v1.SecretManagerService]
            on
            [SecretManagerService.AddSecretVersion][google.cloud.secretmanager.v1.SecretManagerService.AddSecretVersion].
        scheduled_destroy_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. Output only. Scheduled destroy time for secret
            version. This is a part of the Delayed secret version
            destroy feature. For a Secret with a valid version destroy
            TTL, when a secert version is destroyed, version is moved to
            disabled state and it is scheduled for destruction Version
            is destroyed only after the scheduled_destroy_time.
        customer_managed_encryption (google.cloud.secretmanager_v1.types.CustomerManagedEncryptionStatus):
            Output only. The customer-managed encryption status of the
            [SecretVersion][google.cloud.secretmanager.v1.SecretVersion].
            Only populated if customer-managed encryption is used and
            [Secret][google.cloud.secretmanager.v1.Secret] is a
            regionalized secret.
    """

    class State(proto.Enum):
        r"""The state of a
        [SecretVersion][google.cloud.secretmanager.v1.SecretVersion],
        indicating if it can be accessed.

        Values:
            STATE_UNSPECIFIED (0):
                Not specified. This value is unused and
                invalid.
            ENABLED (1):
                The
                [SecretVersion][google.cloud.secretmanager.v1.SecretVersion]
                may be accessed.
            DISABLED (2):
                The
                [SecretVersion][google.cloud.secretmanager.v1.SecretVersion]
                may not be accessed, but the secret data is still available
                and can be placed back into the
                [ENABLED][google.cloud.secretmanager.v1.SecretVersion.State.ENABLED]
                state.
            DESTROYED (3):
                The
                [SecretVersion][google.cloud.secretmanager.v1.SecretVersion]
                is destroyed and the secret data is no longer stored. A
                version may not leave this state once entered.
        """

        STATE_UNSPECIFIED = 0
        ENABLED = 1
        DISABLED = 2
        DESTROYED = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    destroy_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )
    replication_status: "ReplicationStatus" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="ReplicationStatus",
    )
    etag: str = proto.Field(
        proto.STRING,
        number=6,
    )
    client_specified_payload_checksum: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    scheduled_destroy_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    customer_managed_encryption: "CustomerManagedEncryptionStatus" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="CustomerManagedEncryptionStatus",
    )


class Replication(proto.Message):
    r"""A policy that defines the replication and encryption
    configuration of data.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        automatic (google.cloud.secretmanager_v1.types.Replication.Automatic):
            The [Secret][google.cloud.secretmanager.v1.Secret] will
            automatically be replicated without any restrictions.

            This field is a member of `oneof`_ ``replication``.
        user_managed (google.cloud.secretmanager_v1.types.Replication.UserManaged):
            The [Secret][google.cloud.secretmanager.v1.Secret] will only
            be replicated into the locations specified.

            This field is a member of `oneof`_ ``replication``.
    """

    class Automatic(proto.Message):
        r"""A replication policy that replicates the
        [Secret][google.cloud.secretmanager.v1.Secret] payload without any
        restrictions.

        Attributes:
            customer_managed_encryption (google.cloud.secretmanager_v1.types.CustomerManagedEncryption):
                Optional. The customer-managed encryption configuration of
                the [Secret][google.cloud.secretmanager.v1.Secret]. If no
                configuration is provided, Google-managed default encryption
                is used.

                Updates to the
                [Secret][google.cloud.secretmanager.v1.Secret] encryption
                configuration only apply to
                [SecretVersions][google.cloud.secretmanager.v1.SecretVersion]
                added afterwards. They do not apply retroactively to
                existing
                [SecretVersions][google.cloud.secretmanager.v1.SecretVersion].
        """

        customer_managed_encryption: "CustomerManagedEncryption" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="CustomerManagedEncryption",
        )

    class UserManaged(proto.Message):
        r"""A replication policy that replicates the
        [Secret][google.cloud.secretmanager.v1.Secret] payload into the
        locations specified in
        [Replication.UserManaged.replicas][google.cloud.secretmanager.v1.Replication.UserManaged.replicas]

        Attributes:
            replicas (MutableSequence[google.cloud.secretmanager_v1.types.Replication.UserManaged.Replica]):
                Required. The list of Replicas for this
                [Secret][google.cloud.secretmanager.v1.Secret].

                Cannot be empty.
        """

        class Replica(proto.Message):
            r"""Represents a Replica for this
            [Secret][google.cloud.secretmanager.v1.Secret].

            Attributes:
                location (str):
                    The canonical IDs of the location to replicate data. For
                    example: ``"us-east1"``.
                customer_managed_encryption (google.cloud.secretmanager_v1.types.CustomerManagedEncryption):
                    Optional. The customer-managed encryption configuration of
                    the [User-Managed Replica][Replication.UserManaged.Replica].
                    If no configuration is provided, Google-managed default
                    encryption is used.

                    Updates to the
                    [Secret][google.cloud.secretmanager.v1.Secret] encryption
                    configuration only apply to
                    [SecretVersions][google.cloud.secretmanager.v1.SecretVersion]
                    added afterwards. They do not apply retroactively to
                    existing
                    [SecretVersions][google.cloud.secretmanager.v1.SecretVersion].
            """

            location: str = proto.Field(
                proto.STRING,
                number=1,
            )
            customer_managed_encryption: "CustomerManagedEncryption" = proto.Field(
                proto.MESSAGE,
                number=2,
                message="CustomerManagedEncryption",
            )

        replicas: MutableSequence["Replication.UserManaged.Replica"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message="Replication.UserManaged.Replica",
            )
        )

    automatic: Automatic = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="replication",
        message=Automatic,
    )
    user_managed: UserManaged = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="replication",
        message=UserManaged,
    )


class CustomerManagedEncryption(proto.Message):
    r"""Configuration for encrypting secret payloads using
    customer-managed encryption keys (CMEK).

    Attributes:
        kms_key_name (str):
            Required. The resource name of the Cloud KMS CryptoKey used
            to encrypt secret payloads.

            For secrets using the
            [UserManaged][google.cloud.secretmanager.v1.Replication.UserManaged]
            replication policy type, Cloud KMS CryptoKeys must reside in
            the same location as the [replica
            location][Secret.UserManaged.Replica.location].

            For secrets using the
            [Automatic][google.cloud.secretmanager.v1.Replication.Automatic]
            replication policy type, Cloud KMS CryptoKeys must reside in
            ``global``.

            The expected format is
            ``projects/*/locations/*/keyRings/*/cryptoKeys/*``.
    """

    kms_key_name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ReplicationStatus(proto.Message):
    r"""The replication status of a
    [SecretVersion][google.cloud.secretmanager.v1.SecretVersion].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        automatic (google.cloud.secretmanager_v1.types.ReplicationStatus.AutomaticStatus):
            Describes the replication status of a
            [SecretVersion][google.cloud.secretmanager.v1.SecretVersion]
            with automatic replication.

            Only populated if the parent
            [Secret][google.cloud.secretmanager.v1.Secret] has an
            automatic replication policy.

            This field is a member of `oneof`_ ``replication_status``.
        user_managed (google.cloud.secretmanager_v1.types.ReplicationStatus.UserManagedStatus):
            Describes the replication status of a
            [SecretVersion][google.cloud.secretmanager.v1.SecretVersion]
            with user-managed replication.

            Only populated if the parent
            [Secret][google.cloud.secretmanager.v1.Secret] has a
            user-managed replication policy.

            This field is a member of `oneof`_ ``replication_status``.
    """

    class AutomaticStatus(proto.Message):
        r"""The replication status of a
        [SecretVersion][google.cloud.secretmanager.v1.SecretVersion] using
        automatic replication.

        Only populated if the parent
        [Secret][google.cloud.secretmanager.v1.Secret] has an automatic
        replication policy.

        Attributes:
            customer_managed_encryption (google.cloud.secretmanager_v1.types.CustomerManagedEncryptionStatus):
                Output only. The customer-managed encryption status of the
                [SecretVersion][google.cloud.secretmanager.v1.SecretVersion].
                Only populated if customer-managed encryption is used.
        """

        customer_managed_encryption: "CustomerManagedEncryptionStatus" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="CustomerManagedEncryptionStatus",
        )

    class UserManagedStatus(proto.Message):
        r"""The replication status of a
        [SecretVersion][google.cloud.secretmanager.v1.SecretVersion] using
        user-managed replication.

        Only populated if the parent
        [Secret][google.cloud.secretmanager.v1.Secret] has a user-managed
        replication policy.

        Attributes:
            replicas (MutableSequence[google.cloud.secretmanager_v1.types.ReplicationStatus.UserManagedStatus.ReplicaStatus]):
                Output only. The list of replica statuses for the
                [SecretVersion][google.cloud.secretmanager.v1.SecretVersion].
        """

        class ReplicaStatus(proto.Message):
            r"""Describes the status of a user-managed replica for the
            [SecretVersion][google.cloud.secretmanager.v1.SecretVersion].

            Attributes:
                location (str):
                    Output only. The canonical ID of the replica location. For
                    example: ``"us-east1"``.
                customer_managed_encryption (google.cloud.secretmanager_v1.types.CustomerManagedEncryptionStatus):
                    Output only. The customer-managed encryption status of the
                    [SecretVersion][google.cloud.secretmanager.v1.SecretVersion].
                    Only populated if customer-managed encryption is used.
            """

            location: str = proto.Field(
                proto.STRING,
                number=1,
            )
            customer_managed_encryption: "CustomerManagedEncryptionStatus" = (
                proto.Field(
                    proto.MESSAGE,
                    number=2,
                    message="CustomerManagedEncryptionStatus",
                )
            )

        replicas: MutableSequence[
            "ReplicationStatus.UserManagedStatus.ReplicaStatus"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="ReplicationStatus.UserManagedStatus.ReplicaStatus",
        )

    automatic: AutomaticStatus = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="replication_status",
        message=AutomaticStatus,
    )
    user_managed: UserManagedStatus = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="replication_status",
        message=UserManagedStatus,
    )


class CustomerManagedEncryptionStatus(proto.Message):
    r"""Describes the status of customer-managed encryption.

    Attributes:
        kms_key_version_name (str):
            Required. The resource name of the Cloud KMS
            CryptoKeyVersion used to encrypt the secret payload, in the
            following format:
            ``projects/*/locations/*/keyRings/*/cryptoKeys/*/versions/*``.
    """

    kms_key_version_name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Topic(proto.Message):
    r"""A Pub/Sub topic which Secret Manager will publish to when
    control plane events occur on this secret.

    Attributes:
        name (str):
            Identifier. The resource name of the Pub/Sub topic that will
            be published to, in the following format:
            ``projects/*/topics/*``. For publication to succeed, the
            Secret Manager service agent must have the
            ``pubsub.topic.publish`` permission on the topic. The
            Pub/Sub Publisher role (``roles/pubsub.publisher``) includes
            this permission.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Rotation(proto.Message):
    r"""The rotation time and period for a
    [Secret][google.cloud.secretmanager.v1.Secret]. At
    next_rotation_time, Secret Manager will send a Pub/Sub notification
    to the topics configured on the Secret.
    [Secret.topics][google.cloud.secretmanager.v1.Secret.topics] must be
    set to configure rotation.

    Attributes:
        next_rotation_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. Timestamp in UTC at which the
            [Secret][google.cloud.secretmanager.v1.Secret] is scheduled
            to rotate. Cannot be set to less than 300s (5 min) in the
            future and at most 3153600000s (100 years).

            [next_rotation_time][google.cloud.secretmanager.v1.Rotation.next_rotation_time]
            MUST be set if
            [rotation_period][google.cloud.secretmanager.v1.Rotation.rotation_period]
            is set.
        rotation_period (google.protobuf.duration_pb2.Duration):
            Input only. The Duration between rotation notifications.
            Must be in seconds and at least 3600s (1h) and at most
            3153600000s (100 years).

            If
            [rotation_period][google.cloud.secretmanager.v1.Rotation.rotation_period]
            is set,
            [next_rotation_time][google.cloud.secretmanager.v1.Rotation.next_rotation_time]
            must be set.
            [next_rotation_time][google.cloud.secretmanager.v1.Rotation.next_rotation_time]
            will be advanced by this period when the service
            automatically sends rotation notifications.
        managed_rotation_status (google.cloud.secretmanager_v1.types.Rotation.ManagedRotationStatus):
            Output only. The current status of the
            managed rotation. This field is only applicable
            to Typed Secrets. This field is set by the
            service and cannot be set by the user.
    """

    class ManagedRotationStatus(proto.Message):
        r"""Represents the status of a managed rotation.

        This is applicable only to Typed Secrets. It indicates whether
        the rotation is active and any errors that may have occurred
        during the asynchronous managed rotation.

        Attributes:
            state (google.cloud.secretmanager_v1.types.Rotation.ManagedRotationStatus.State):
                Output only. Indicates whether the Managed
                Rotation is active or not.
            error (google.rpc.status_pb2.Status):
                Output only. Displays customer-facing issues
                that occurred during an asynchronous managed
                rotation. For example, if there are some
                permission errors.
        """

        class State(proto.Enum):
            r"""This defines the various states in which the managed rotation
            can be.

            Values:
                STATE_UNSPECIFIED (0):
                    Not specified. This value is unused and
                    invalid.
                ACTIVE (1):
                    Indicates that the Managed rotation is
                    ACTIVE.
                INACTIVE (2):
                    Indicates that the Managed rotation is
                    INACTIVE.
            """

            STATE_UNSPECIFIED = 0
            ACTIVE = 1
            INACTIVE = 2

        state: "Rotation.ManagedRotationStatus.State" = proto.Field(
            proto.ENUM,
            number=1,
            enum="Rotation.ManagedRotationStatus.State",
        )
        error: status_pb2.Status = proto.Field(
            proto.MESSAGE,
            number=2,
            message=status_pb2.Status,
        )

    next_rotation_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    rotation_period: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )
    managed_rotation_status: ManagedRotationStatus = proto.Field(
        proto.MESSAGE,
        number=3,
        message=ManagedRotationStatus,
    )


class SecretPayload(proto.Message):
    r"""A secret payload resource in the Secret Manager API. This contains
    the sensitive secret payload that is associated with a
    [SecretVersion][google.cloud.secretmanager.v1.SecretVersion].


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        data (bytes):
            The secret data. Must be no larger than
            64KiB.
        data_crc32c (int):
            Optional. If specified,
            [SecretManagerService][google.cloud.secretmanager.v1.SecretManagerService]
            will verify the integrity of the received
            [data][google.cloud.secretmanager.v1.SecretPayload.data] on
            [SecretManagerService.AddSecretVersion][google.cloud.secretmanager.v1.SecretManagerService.AddSecretVersion]
            calls using the crc32c checksum and store it to include in
            future
            [SecretManagerService.AccessSecretVersion][google.cloud.secretmanager.v1.SecretManagerService.AccessSecretVersion]
            responses. If a checksum is not provided in the
            [SecretManagerService.AddSecretVersion][google.cloud.secretmanager.v1.SecretManagerService.AddSecretVersion]
            request, the
            [SecretManagerService][google.cloud.secretmanager.v1.SecretManagerService]
            will generate and store one for you.

            The CRC32C value is encoded as a Int64 for compatibility,
            and can be safely downconverted to uint32 in languages that
            support this type.
            https://cloud.google.com/apis/design/design_patterns#integer_types

            This field is a member of `oneof`_ ``_data_crc32c``.
    """

    data: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )
    data_crc32c: int = proto.Field(
        proto.INT64,
        number=2,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
