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

__protobuf__ = proto.module(
    package="google.cloud.webrisk.v1",
    manifest={
        "ThreatType",
        "CompressionType",
        "ComputeThreatListDiffRequest",
        "ComputeThreatListDiffResponse",
        "SearchUrisRequest",
        "SearchUrisResponse",
        "SearchHashesRequest",
        "SearchHashesResponse",
        "ThreatEntryAdditions",
        "ThreatEntryRemovals",
        "RawIndices",
        "RawHashes",
        "RiceDeltaEncoding",
        "Submission",
        "ThreatInfo",
        "ThreatDiscovery",
        "CreateSubmissionRequest",
        "SubmitUriRequest",
        "SubmitUriMetadata",
    },
)


class ThreatType(proto.Enum):
    r"""The type of threat. This maps directly to the threat list a
    threat may belong to.

    Values:
        THREAT_TYPE_UNSPECIFIED (0):
            No entries should match this threat type.
            This threat type is unused.
        MALWARE (1):
            Malware targeting any platform.
        SOCIAL_ENGINEERING (2):
            Social engineering targeting any platform.
        UNWANTED_SOFTWARE (3):
            Unwanted software targeting any platform.
        SOCIAL_ENGINEERING_EXTENDED_COVERAGE (4):
            A list of extended coverage social
            engineering URIs targeting any platform.
    """

    THREAT_TYPE_UNSPECIFIED = 0
    MALWARE = 1
    SOCIAL_ENGINEERING = 2
    UNWANTED_SOFTWARE = 3
    SOCIAL_ENGINEERING_EXTENDED_COVERAGE = 4


class CompressionType(proto.Enum):
    r"""The ways in which threat entry sets can be compressed.

    Values:
        COMPRESSION_TYPE_UNSPECIFIED (0):
            Unknown.
        RAW (1):
            Raw, uncompressed data.
        RICE (2):
            Rice-Golomb encoded data.
    """

    COMPRESSION_TYPE_UNSPECIFIED = 0
    RAW = 1
    RICE = 2


class ComputeThreatListDiffRequest(proto.Message):
    r"""Describes an API diff request.

    Attributes:
        threat_type (google.cloud.webrisk_v1.types.ThreatType):
            Required. The threat list to update. Only a
            single ThreatType should be specified per
            request. If you want to handle multiple
            ThreatTypes, you must make one request per
            ThreatType.
        version_token (bytes):
            The current version token of the client for
            the requested list (the client version that was
            received from the last successful diff). If the
            client does not have a version token (this is
            the first time calling ComputeThreatListDiff),
            this may be left empty and a full database
            snapshot will be returned.
        constraints (google.cloud.webrisk_v1.types.ComputeThreatListDiffRequest.Constraints):
            Required. The constraints associated with
            this request.
    """

    class Constraints(proto.Message):
        r"""The constraints for this diff.

        Attributes:
            max_diff_entries (int):
                The maximum size in number of entries. The diff will not
                contain more entries than this value. This should be a power
                of 2 between 2\ **10 and 2**\ 20. If zero, no diff size
                limit is set.
            max_database_entries (int):
                Sets the maximum number of entries that the client is
                willing to have in the local database. This should be a
                power of 2 between 2\ **10 and 2**\ 20. If zero, no database
                size limit is set.
            supported_compressions (MutableSequence[google.cloud.webrisk_v1.types.CompressionType]):
                The compression types supported by the
                client.
        """

        max_diff_entries: int = proto.Field(
            proto.INT32,
            number=1,
        )
        max_database_entries: int = proto.Field(
            proto.INT32,
            number=2,
        )
        supported_compressions: MutableSequence["CompressionType"] = (
            proto.RepeatedField(
                proto.ENUM,
                number=3,
                enum="CompressionType",
            )
        )

    threat_type: "ThreatType" = proto.Field(
        proto.ENUM,
        number=1,
        enum="ThreatType",
    )
    version_token: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )
    constraints: Constraints = proto.Field(
        proto.MESSAGE,
        number=3,
        message=Constraints,
    )


class ComputeThreatListDiffResponse(proto.Message):
    r"""

    Attributes:
        response_type (google.cloud.webrisk_v1.types.ComputeThreatListDiffResponse.ResponseType):
            The type of response. This may indicate that
            an action must be taken by the client when the
            response is received.
        additions (google.cloud.webrisk_v1.types.ThreatEntryAdditions):
            A set of entries to add to a local threat
            type's list.
        removals (google.cloud.webrisk_v1.types.ThreatEntryRemovals):
            A set of entries to remove from a local
            threat type's list. This field may be empty.
        new_version_token (bytes):
            The new opaque client version token. This should be retained
            by the client and passed into the next call of
            ComputeThreatListDiff as 'version_token'. A separate version
            token should be stored and used for each threatList.
        checksum (google.cloud.webrisk_v1.types.ComputeThreatListDiffResponse.Checksum):
            The expected SHA256 hash of the client state;
            that is, of the sorted list of all hashes
            present in the database after applying the
            provided diff. If the client state doesn't match
            the expected state, the client must discard this
            diff and retry later.
        recommended_next_diff (google.protobuf.timestamp_pb2.Timestamp):
            The soonest the client should wait before
            issuing any diff request. Querying sooner is
            unlikely to produce a meaningful diff. Waiting
            longer is acceptable considering the use case.
            If this field is not set clients may update as
            soon as they want.
    """

    class ResponseType(proto.Enum):
        r"""The type of response sent to the client.

        Values:
            RESPONSE_TYPE_UNSPECIFIED (0):
                Unknown.
            DIFF (1):
                Partial updates are applied to the client's
                existing local database.
            RESET (2):
                Full updates resets the client's entire local
                database. This means that either the client had
                no state, was seriously out-of-date, or the
                client is believed to be corrupt.
        """

        RESPONSE_TYPE_UNSPECIFIED = 0
        DIFF = 1
        RESET = 2

    class Checksum(proto.Message):
        r"""The expected state of a client's local database.

        Attributes:
            sha256 (bytes):
                The SHA256 hash of the client state; that is,
                of the sorted list of all hashes present in the
                database.
        """

        sha256: bytes = proto.Field(
            proto.BYTES,
            number=1,
        )

    response_type: ResponseType = proto.Field(
        proto.ENUM,
        number=4,
        enum=ResponseType,
    )
    additions: "ThreatEntryAdditions" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="ThreatEntryAdditions",
    )
    removals: "ThreatEntryRemovals" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="ThreatEntryRemovals",
    )
    new_version_token: bytes = proto.Field(
        proto.BYTES,
        number=7,
    )
    checksum: Checksum = proto.Field(
        proto.MESSAGE,
        number=8,
        message=Checksum,
    )
    recommended_next_diff: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


class SearchUrisRequest(proto.Message):
    r"""Request to check URI entries against threatLists.

    Attributes:
        uri (str):
            Required. The URI to be checked for matches.
        threat_types (MutableSequence[google.cloud.webrisk_v1.types.ThreatType]):
            Required. The ThreatLists to search in.
            Multiple ThreatLists may be specified.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    threat_types: MutableSequence["ThreatType"] = proto.RepeatedField(
        proto.ENUM,
        number=2,
        enum="ThreatType",
    )


class SearchUrisResponse(proto.Message):
    r"""

    Attributes:
        threat (google.cloud.webrisk_v1.types.SearchUrisResponse.ThreatUri):
            The threat list matches. This might be empty
            if the URI is on no list.
    """

    class ThreatUri(proto.Message):
        r"""Contains threat information on a matching uri.

        Attributes:
            threat_types (MutableSequence[google.cloud.webrisk_v1.types.ThreatType]):
                The ThreatList this threat belongs to.
            expire_time (google.protobuf.timestamp_pb2.Timestamp):
                The cache lifetime for the returned match.
                Clients must not cache this response past this
                timestamp to avoid false positives.
        """

        threat_types: MutableSequence["ThreatType"] = proto.RepeatedField(
            proto.ENUM,
            number=1,
            enum="ThreatType",
        )
        expire_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=2,
            message=timestamp_pb2.Timestamp,
        )

    threat: ThreatUri = proto.Field(
        proto.MESSAGE,
        number=1,
        message=ThreatUri,
    )


class SearchHashesRequest(proto.Message):
    r"""Request to return full hashes matched by the provided hash
    prefixes.

    Attributes:
        hash_prefix (bytes):
            A hash prefix, consisting of the most
            significant 4-32 bytes of a SHA256 hash. For
            JSON requests, this field is base64-encoded.
            Note that if this parameter is provided by a
            URI, it must be encoded using the web safe
            base64 variant (RFC 4648).
        threat_types (MutableSequence[google.cloud.webrisk_v1.types.ThreatType]):
            Required. The ThreatLists to search in.
            Multiple ThreatLists may be specified.
    """

    hash_prefix: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )
    threat_types: MutableSequence["ThreatType"] = proto.RepeatedField(
        proto.ENUM,
        number=2,
        enum="ThreatType",
    )


class SearchHashesResponse(proto.Message):
    r"""

    Attributes:
        threats (MutableSequence[google.cloud.webrisk_v1.types.SearchHashesResponse.ThreatHash]):
            The full hashes that matched the requested
            prefixes. The hash will be populated in the key.
        negative_expire_time (google.protobuf.timestamp_pb2.Timestamp):
            For requested entities that did not match the
            threat list, how long to cache the response
            until.
    """

    class ThreatHash(proto.Message):
        r"""Contains threat information on a matching hash.

        Attributes:
            threat_types (MutableSequence[google.cloud.webrisk_v1.types.ThreatType]):
                The ThreatList this threat belongs to.
                This must contain at least one entry.
            hash_ (bytes):
                A 32 byte SHA256 hash. This field is in
                binary format. For JSON requests, hashes are
                base64-encoded.
            expire_time (google.protobuf.timestamp_pb2.Timestamp):
                The cache lifetime for the returned match.
                Clients must not cache this response past this
                timestamp to avoid false positives.
        """

        threat_types: MutableSequence["ThreatType"] = proto.RepeatedField(
            proto.ENUM,
            number=1,
            enum="ThreatType",
        )
        hash_: bytes = proto.Field(
            proto.BYTES,
            number=2,
        )
        expire_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=3,
            message=timestamp_pb2.Timestamp,
        )

    threats: MutableSequence[ThreatHash] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=ThreatHash,
    )
    negative_expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


class ThreatEntryAdditions(proto.Message):
    r"""Contains the set of entries to add to a local database.
    May contain a combination of compressed and raw data in a single
    response.

    Attributes:
        raw_hashes (MutableSequence[google.cloud.webrisk_v1.types.RawHashes]):
            The raw SHA256-formatted entries.
            Repeated to allow returning sets of hashes with
            different prefix sizes.
        rice_hashes (google.cloud.webrisk_v1.types.RiceDeltaEncoding):
            The encoded 4-byte prefixes of SHA256-formatted entries,
            using a Golomb-Rice encoding. The hashes are converted to
            uint32, sorted in ascending order, then delta encoded and
            stored as encoded_data.
    """

    raw_hashes: MutableSequence["RawHashes"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="RawHashes",
    )
    rice_hashes: "RiceDeltaEncoding" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="RiceDeltaEncoding",
    )


class ThreatEntryRemovals(proto.Message):
    r"""Contains the set of entries to remove from a local database.

    Attributes:
        raw_indices (google.cloud.webrisk_v1.types.RawIndices):
            The raw removal indices for a local list.
        rice_indices (google.cloud.webrisk_v1.types.RiceDeltaEncoding):
            The encoded local, lexicographically-sorted list indices,
            using a Golomb-Rice encoding. Used for sending compressed
            removal indices. The removal indices (uint32) are sorted in
            ascending order, then delta encoded and stored as
            encoded_data.
    """

    raw_indices: "RawIndices" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="RawIndices",
    )
    rice_indices: "RiceDeltaEncoding" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="RiceDeltaEncoding",
    )


class RawIndices(proto.Message):
    r"""A set of raw indices to remove from a local list.

    Attributes:
        indices (MutableSequence[int]):
            The indices to remove from a
            lexicographically-sorted local list.
    """

    indices: MutableSequence[int] = proto.RepeatedField(
        proto.INT32,
        number=1,
    )


class RawHashes(proto.Message):
    r"""The uncompressed threat entries in hash format.
    Hashes can be anywhere from 4 to 32 bytes in size. A large
    majority are 4 bytes, but some hashes are lengthened if they
    collide with the hash of a popular URI.

    Used for sending ThreatEntryAdditons to clients that do not
    support compression, or when sending non-4-byte hashes to
    clients that do support compression.

    Attributes:
        prefix_size (int):
            The number of bytes for each prefix encoded
            below.  This field can be anywhere from 4
            (shortest prefix) to 32 (full SHA256 hash). In
            practice this is almost always 4, except in
            exceptional circumstances.
        raw_hashes (bytes):
            The hashes, in binary format, concatenated
            into one long string. Hashes are sorted in
            lexicographic order. For JSON API users, hashes
            are base64-encoded.
    """

    prefix_size: int = proto.Field(
        proto.INT32,
        number=1,
    )
    raw_hashes: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )


class RiceDeltaEncoding(proto.Message):
    r"""The Rice-Golomb encoded data. Used for sending compressed
    4-byte hashes or compressed removal indices.

    Attributes:
        first_value (int):
            The offset of the first entry in the encoded
            data, or, if only a single integer was encoded,
            that single integer's value. If the field is
            empty or missing, assume zero.
        rice_parameter (int):
            The Golomb-Rice parameter, which is a number between 2 and
            28. This field is missing (that is, zero) if ``num_entries``
            is zero.
        entry_count (int):
            The number of entries that are delta encoded in the encoded
            data. If only a single integer was encoded, this will be
            zero and the single value will be stored in ``first_value``.
        encoded_data (bytes):
            The encoded deltas that are encoded using the
            Golomb-Rice coder.
    """

    first_value: int = proto.Field(
        proto.INT64,
        number=1,
    )
    rice_parameter: int = proto.Field(
        proto.INT32,
        number=2,
    )
    entry_count: int = proto.Field(
        proto.INT32,
        number=3,
    )
    encoded_data: bytes = proto.Field(
        proto.BYTES,
        number=4,
    )


class Submission(proto.Message):
    r"""Wraps a URI that might be displaying malicious content.

    Attributes:
        uri (str):
            Required. The URI that is being reported for
            malicious content to be analyzed.
        threat_types (MutableSequence[google.cloud.webrisk_v1.types.ThreatType]):
            Output only. ThreatTypes found to be
            associated with the submitted URI after
            reviewing it. This might be empty if the URI was
            not added to any list.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    threat_types: MutableSequence["ThreatType"] = proto.RepeatedField(
        proto.ENUM,
        number=2,
        enum="ThreatType",
    )


class ThreatInfo(proto.Message):
    r"""Context about the submission including the type of abuse
    found on the URI and supporting details.

    Attributes:
        abuse_type (google.cloud.webrisk_v1.types.ThreatInfo.AbuseType):
            The type of abuse.
        threat_confidence (google.cloud.webrisk_v1.types.ThreatInfo.Confidence):
            Confidence that the URI is unsafe.
        threat_justification (google.cloud.webrisk_v1.types.ThreatInfo.ThreatJustification):
            Context about why the URI is unsafe.
    """

    class AbuseType(proto.Enum):
        r"""The abuse type found on the URI.

        Values:
            ABUSE_TYPE_UNSPECIFIED (0):
                Default.
            MALWARE (1):
                The URI contains malware.
            SOCIAL_ENGINEERING (2):
                The URI contains social engineering.
            UNWANTED_SOFTWARE (3):
                The URI contains unwanted software.
        """

        ABUSE_TYPE_UNSPECIFIED = 0
        MALWARE = 1
        SOCIAL_ENGINEERING = 2
        UNWANTED_SOFTWARE = 3

    class Confidence(proto.Message):
        r"""Confidence that a URI is unsafe.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            score (float):
                A decimal representation of confidence in the
                range of 0 to 1 where 0 indicates no confidence
                and 1 indicates complete confidence.

                This field is a member of `oneof`_ ``value``.
            level (google.cloud.webrisk_v1.types.ThreatInfo.Confidence.ConfidenceLevel):
                Enum representation of confidence.

                This field is a member of `oneof`_ ``value``.
        """

        class ConfidenceLevel(proto.Enum):
            r"""Enum representation of confidence.

            Values:
                CONFIDENCE_LEVEL_UNSPECIFIED (0):
                    Default.
                LOW (1):
                    Less than 60% confidence that the URI is
                    unsafe.
                MEDIUM (2):
                    Between 60% and 80% confidence that the URI
                    is unsafe.
                HIGH (3):
                    Greater than 80% confidence that the URI is
                    unsafe.
            """

            CONFIDENCE_LEVEL_UNSPECIFIED = 0
            LOW = 1
            MEDIUM = 2
            HIGH = 3

        score: float = proto.Field(
            proto.FLOAT,
            number=1,
            oneof="value",
        )
        level: "ThreatInfo.Confidence.ConfidenceLevel" = proto.Field(
            proto.ENUM,
            number=2,
            oneof="value",
            enum="ThreatInfo.Confidence.ConfidenceLevel",
        )

    class ThreatJustification(proto.Message):
        r"""Context about why the URI is unsafe.

        Attributes:
            labels (MutableSequence[google.cloud.webrisk_v1.types.ThreatInfo.ThreatJustification.JustificationLabel]):
                Labels associated with this URI that explain
                how it was classified.
            comments (MutableSequence[str]):
                Free-form context on why this URI is unsafe.
        """

        class JustificationLabel(proto.Enum):
            r"""Labels that explain how the URI was classified.

            Values:
                JUSTIFICATION_LABEL_UNSPECIFIED (0):
                    Default.
                MANUAL_VERIFICATION (1):
                    The submitter manually verified that the
                    submission is unsafe.
                USER_REPORT (2):
                    The submitter received the submission from an
                    end user.
                AUTOMATED_REPORT (3):
                    The submitter received the submission from an
                    automated system.
            """

            JUSTIFICATION_LABEL_UNSPECIFIED = 0
            MANUAL_VERIFICATION = 1
            USER_REPORT = 2
            AUTOMATED_REPORT = 3

        labels: MutableSequence["ThreatInfo.ThreatJustification.JustificationLabel"] = (
            proto.RepeatedField(
                proto.ENUM,
                number=1,
                enum="ThreatInfo.ThreatJustification.JustificationLabel",
            )
        )
        comments: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )

    abuse_type: AbuseType = proto.Field(
        proto.ENUM,
        number=1,
        enum=AbuseType,
    )
    threat_confidence: Confidence = proto.Field(
        proto.MESSAGE,
        number=2,
        message=Confidence,
    )
    threat_justification: ThreatJustification = proto.Field(
        proto.MESSAGE,
        number=3,
        message=ThreatJustification,
    )


class ThreatDiscovery(proto.Message):
    r"""Details about how the threat was discovered.

    Attributes:
        platform (google.cloud.webrisk_v1.types.ThreatDiscovery.Platform):
            Platform on which the threat was discovered.
        region_codes (MutableSequence[str]):
            CLDR region code of the countries/regions the
            URI poses a threat ordered from most impact to
            least impact. Example: "US" for United States.
    """

    class Platform(proto.Enum):
        r"""Platform types.

        Values:
            PLATFORM_UNSPECIFIED (0):
                Default.
            ANDROID (1):
                General Android platform.
            IOS (2):
                General iOS platform.
            MACOS (3):
                General macOS platform.
            WINDOWS (4):
                General Windows platform.
        """

        PLATFORM_UNSPECIFIED = 0
        ANDROID = 1
        IOS = 2
        MACOS = 3
        WINDOWS = 4

    platform: Platform = proto.Field(
        proto.ENUM,
        number=1,
        enum=Platform,
    )
    region_codes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class CreateSubmissionRequest(proto.Message):
    r"""Request to send a potentially phishy URI to WebRisk.

    Attributes:
        parent (str):
            Required. The name of the project that is making the
            submission. This string is in the format
            "projects/{project_number}".
        submission (google.cloud.webrisk_v1.types.Submission):
            Required. The submission that contains the
            content of the phishing report.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    submission: "Submission" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Submission",
    )


class SubmitUriRequest(proto.Message):
    r"""Request to send a potentially malicious URI to WebRisk.

    Attributes:
        parent (str):
            Required. The name of the project that is making the
            submission. This string is in the format
            "projects/{project_number}".
        submission (google.cloud.webrisk_v1.types.Submission):
            Required. The submission that contains the
            URI to be scanned.
        threat_info (google.cloud.webrisk_v1.types.ThreatInfo):
            Provides additional information about the
            submission.
        threat_discovery (google.cloud.webrisk_v1.types.ThreatDiscovery):
            Provides additional information about how the
            submission was discovered.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    submission: "Submission" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Submission",
    )
    threat_info: "ThreatInfo" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ThreatInfo",
    )
    threat_discovery: "ThreatDiscovery" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="ThreatDiscovery",
    )


class SubmitUriMetadata(proto.Message):
    r"""Metadata for the Submit URI long-running operation.

    Attributes:
        state (google.cloud.webrisk_v1.types.SubmitUriMetadata.State):
            The state of the operation.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Creation time of the operation.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Latest update time of the operation.
    """

    class State(proto.Enum):
        r"""Enum that represents the state of the long-running operation.

        Values:
            STATE_UNSPECIFIED (0):
                Default unspecified state.
            RUNNING (1):
                The operation is currently running.
            SUCCEEDED (2):
                The operation finished with a success status.
            CANCELLED (3):
                The operation was cancelled.
            FAILED (4):
                The operation finished with a failure status.
            CLOSED (5):
                The operation was closed with no action
                taken.
        """

        STATE_UNSPECIFIED = 0
        RUNNING = 1
        SUCCEEDED = 2
        CANCELLED = 3
        FAILED = 4
        CLOSED = 5

    state: State = proto.Field(
        proto.ENUM,
        number=1,
        enum=State,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
