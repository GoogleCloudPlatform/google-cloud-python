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
    package="grafeas.v1",
    manifest={
        "CVSSVersion",
        "CVSSv3",
        "CVSS",
    },
)


class CVSSVersion(proto.Enum):
    r"""CVSS Version.

    Values:
        CVSS_VERSION_UNSPECIFIED (0):
            Unspecified.
        CVSS_VERSION_2 (1):
            CVSS v2.
        CVSS_VERSION_3 (2):
            CVSS v3.
        CVSS_VERSION_4 (3):
            CVSS v4.
    """

    CVSS_VERSION_UNSPECIFIED = 0
    CVSS_VERSION_2 = 1
    CVSS_VERSION_3 = 2
    CVSS_VERSION_4 = 3


class CVSSv3(proto.Message):
    r"""Common Vulnerability Scoring System version 3.
    For details, see
    https://www.first.org/cvss/specification-document

    Attributes:
        base_score (float):
            The base score is a function of the base
            metric scores.
        exploitability_score (float):

        impact_score (float):

        attack_vector (grafeas.grafeas_v1.types.CVSSv3.AttackVector):
            Base Metrics
            Represents the intrinsic characteristics of a
            vulnerability that are constant over time and
            across user environments.
        attack_complexity (grafeas.grafeas_v1.types.CVSSv3.AttackComplexity):

        privileges_required (grafeas.grafeas_v1.types.CVSSv3.PrivilegesRequired):

        user_interaction (grafeas.grafeas_v1.types.CVSSv3.UserInteraction):

        scope (grafeas.grafeas_v1.types.CVSSv3.Scope):

        confidentiality_impact (grafeas.grafeas_v1.types.CVSSv3.Impact):

        integrity_impact (grafeas.grafeas_v1.types.CVSSv3.Impact):

        availability_impact (grafeas.grafeas_v1.types.CVSSv3.Impact):

    """

    class AttackVector(proto.Enum):
        r"""

        Values:
            ATTACK_VECTOR_UNSPECIFIED (0):
                No description available.
            ATTACK_VECTOR_NETWORK (1):
                No description available.
            ATTACK_VECTOR_ADJACENT (2):
                No description available.
            ATTACK_VECTOR_LOCAL (3):
                No description available.
            ATTACK_VECTOR_PHYSICAL (4):
                No description available.
        """

        ATTACK_VECTOR_UNSPECIFIED = 0
        ATTACK_VECTOR_NETWORK = 1
        ATTACK_VECTOR_ADJACENT = 2
        ATTACK_VECTOR_LOCAL = 3
        ATTACK_VECTOR_PHYSICAL = 4

    class AttackComplexity(proto.Enum):
        r"""

        Values:
            ATTACK_COMPLEXITY_UNSPECIFIED (0):
                No description available.
            ATTACK_COMPLEXITY_LOW (1):
                No description available.
            ATTACK_COMPLEXITY_HIGH (2):
                No description available.
        """

        ATTACK_COMPLEXITY_UNSPECIFIED = 0
        ATTACK_COMPLEXITY_LOW = 1
        ATTACK_COMPLEXITY_HIGH = 2

    class PrivilegesRequired(proto.Enum):
        r"""

        Values:
            PRIVILEGES_REQUIRED_UNSPECIFIED (0):
                No description available.
            PRIVILEGES_REQUIRED_NONE (1):
                No description available.
            PRIVILEGES_REQUIRED_LOW (2):
                No description available.
            PRIVILEGES_REQUIRED_HIGH (3):
                No description available.
        """

        PRIVILEGES_REQUIRED_UNSPECIFIED = 0
        PRIVILEGES_REQUIRED_NONE = 1
        PRIVILEGES_REQUIRED_LOW = 2
        PRIVILEGES_REQUIRED_HIGH = 3

    class UserInteraction(proto.Enum):
        r"""

        Values:
            USER_INTERACTION_UNSPECIFIED (0):
                No description available.
            USER_INTERACTION_NONE (1):
                No description available.
            USER_INTERACTION_REQUIRED (2):
                No description available.
        """

        USER_INTERACTION_UNSPECIFIED = 0
        USER_INTERACTION_NONE = 1
        USER_INTERACTION_REQUIRED = 2

    class Scope(proto.Enum):
        r"""

        Values:
            SCOPE_UNSPECIFIED (0):
                No description available.
            SCOPE_UNCHANGED (1):
                No description available.
            SCOPE_CHANGED (2):
                No description available.
        """

        SCOPE_UNSPECIFIED = 0
        SCOPE_UNCHANGED = 1
        SCOPE_CHANGED = 2

    class Impact(proto.Enum):
        r"""

        Values:
            IMPACT_UNSPECIFIED (0):
                No description available.
            IMPACT_HIGH (1):
                No description available.
            IMPACT_LOW (2):
                No description available.
            IMPACT_NONE (3):
                No description available.
        """

        IMPACT_UNSPECIFIED = 0
        IMPACT_HIGH = 1
        IMPACT_LOW = 2
        IMPACT_NONE = 3

    base_score: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    exploitability_score: float = proto.Field(
        proto.FLOAT,
        number=2,
    )
    impact_score: float = proto.Field(
        proto.FLOAT,
        number=3,
    )
    attack_vector: AttackVector = proto.Field(
        proto.ENUM,
        number=5,
        enum=AttackVector,
    )
    attack_complexity: AttackComplexity = proto.Field(
        proto.ENUM,
        number=6,
        enum=AttackComplexity,
    )
    privileges_required: PrivilegesRequired = proto.Field(
        proto.ENUM,
        number=7,
        enum=PrivilegesRequired,
    )
    user_interaction: UserInteraction = proto.Field(
        proto.ENUM,
        number=8,
        enum=UserInteraction,
    )
    scope: Scope = proto.Field(
        proto.ENUM,
        number=9,
        enum=Scope,
    )
    confidentiality_impact: Impact = proto.Field(
        proto.ENUM,
        number=10,
        enum=Impact,
    )
    integrity_impact: Impact = proto.Field(
        proto.ENUM,
        number=11,
        enum=Impact,
    )
    availability_impact: Impact = proto.Field(
        proto.ENUM,
        number=12,
        enum=Impact,
    )


class CVSS(proto.Message):
    r"""Common Vulnerability Scoring System.
    For details, see
    https://www.first.org/cvss/specification-document This is a
    message we will try to use for storing various versions of CVSS
    rather than making a separate proto for storing a specific
    version.

    Attributes:
        base_score (float):
            The base score is a function of the base
            metric scores.
        exploitability_score (float):

        impact_score (float):

        attack_vector (grafeas.grafeas_v1.types.CVSS.AttackVector):
            Attack Vector (AV). Defined in CVSS v2, v3,
            v4.
        attack_complexity (grafeas.grafeas_v1.types.CVSS.AttackComplexity):
            Attack Complexity (AC). Defined in CVSS v2,
            v3, v4.
        authentication (grafeas.grafeas_v1.types.CVSS.Authentication):
            Authentication (Au). Defined in CVSS v2.
        privileges_required (grafeas.grafeas_v1.types.CVSS.PrivilegesRequired):
            Privileges Required (PR). Defined in CVSS v3,
            v4.
        user_interaction (grafeas.grafeas_v1.types.CVSS.UserInteraction):
            User Interaction (UI). Defined in CVSS v3,
            v4.
        scope (grafeas.grafeas_v1.types.CVSS.Scope):
            Scope (S). Defined in CVSS v3.
        confidentiality_impact (grafeas.grafeas_v1.types.CVSS.Impact):
            Confidentiality Impact (C). Defined in CVSS
            v2, v3.
        integrity_impact (grafeas.grafeas_v1.types.CVSS.Impact):
            Integrity Impact (I). Defined in CVSS v2, v3.
        availability_impact (grafeas.grafeas_v1.types.CVSS.Impact):
            Availability Impact (A). Defined in CVSS v2,
            v3.
        attack_requirements (grafeas.grafeas_v1.types.CVSS.AttackRequirements):
            Attack Requirements (AT). Defined in CVSS v4.
        vulnerable_system_confidentiality_impact (grafeas.grafeas_v1.types.CVSS.Impact):
            Vulnerable System Confidentiality Impact
            (VC). Defined in CVSS v4.
        vulnerable_system_integrity_impact (grafeas.grafeas_v1.types.CVSS.Impact):
            Vulnerable System Integrity Impact (VI).
            Defined in CVSS v4.
        vulnerable_system_availability_impact (grafeas.grafeas_v1.types.CVSS.Impact):
            Vulnerable System Availability Impact (VA).
            Defined in CVSS v4.
        subsequent_system_confidentiality_impact (grafeas.grafeas_v1.types.CVSS.Impact):
            Subsequent System Confidentiality Impact
            (SC). Defined in CVSS v4.
        subsequent_system_integrity_impact (grafeas.grafeas_v1.types.CVSS.Impact):
            Subsequent System Integrity Impact (SI).
            Defined in CVSS v4.
        subsequent_system_availability_impact (grafeas.grafeas_v1.types.CVSS.Impact):
            Subsequent System Availability Impact (SA).
            Defined in CVSS v4.
        exploit_maturity (grafeas.grafeas_v1.types.CVSS.ExploitMaturity):
            Exploit Maturity (E). Defined in CVSS v4.
    """

    class AttackVector(proto.Enum):
        r"""Attack Vector.

        Values:
            ATTACK_VECTOR_UNSPECIFIED (0):
                Unspecified.
            ATTACK_VECTOR_NETWORK (1):
                Attack Vector: Network (AV:N). Defined in
                CVSS v2, v3, v4.
            ATTACK_VECTOR_ADJACENT (2):
                Attack Vector: Adjacent (AV:A). Defined in
                CVSS v2, v3, v4.
            ATTACK_VECTOR_LOCAL (3):
                Attack Vector: Local (AV:L). Defined in CVSS
                v2, v3, v4.
            ATTACK_VECTOR_PHYSICAL (4):
                Attack Vector: Physical (AV:P). Defined in
                CVSS v3, v4.
        """

        ATTACK_VECTOR_UNSPECIFIED = 0
        ATTACK_VECTOR_NETWORK = 1
        ATTACK_VECTOR_ADJACENT = 2
        ATTACK_VECTOR_LOCAL = 3
        ATTACK_VECTOR_PHYSICAL = 4

    class AttackComplexity(proto.Enum):
        r"""Attack Complexity.

        Values:
            ATTACK_COMPLEXITY_UNSPECIFIED (0):
                Unspecified.
            ATTACK_COMPLEXITY_LOW (1):
                Low attack complexity (AC:L). Defined in CVSS
                v2, v3, v4.
            ATTACK_COMPLEXITY_HIGH (2):
                High attack complexity (AC:H). Defined in
                CVSS v2, v3, v4.
            ATTACK_COMPLEXITY_MEDIUM (3):
                Medium attack complexity (AC:M). Defined in
                CVSS v2.
        """

        ATTACK_COMPLEXITY_UNSPECIFIED = 0
        ATTACK_COMPLEXITY_LOW = 1
        ATTACK_COMPLEXITY_HIGH = 2
        ATTACK_COMPLEXITY_MEDIUM = 3

    class Authentication(proto.Enum):
        r"""Authentication.

        Values:
            AUTHENTICATION_UNSPECIFIED (0):
                Unspecified.
            AUTHENTICATION_MULTIPLE (1):
                Multiple authentication required (Au:M).
                Defined in CVSS v2.
            AUTHENTICATION_SINGLE (2):
                Single authentication required (Au:S).
                Defined in CVSS v2.
            AUTHENTICATION_NONE (3):
                No authentication required (Au:N). Defined in
                CVSS v2.
        """

        AUTHENTICATION_UNSPECIFIED = 0
        AUTHENTICATION_MULTIPLE = 1
        AUTHENTICATION_SINGLE = 2
        AUTHENTICATION_NONE = 3

    class PrivilegesRequired(proto.Enum):
        r"""Privileges Required.

        Values:
            PRIVILEGES_REQUIRED_UNSPECIFIED (0):
                Unspecified.
            PRIVILEGES_REQUIRED_NONE (1):
                No privileges required (PR:N). Defined in
                CVSS v3, v4.
            PRIVILEGES_REQUIRED_LOW (2):
                Low privileges required (PR:L). Defined in
                CVSS v3, v4.
            PRIVILEGES_REQUIRED_HIGH (3):
                High privileges required (PR:H). Defined in
                CVSS v3, v4.
        """

        PRIVILEGES_REQUIRED_UNSPECIFIED = 0
        PRIVILEGES_REQUIRED_NONE = 1
        PRIVILEGES_REQUIRED_LOW = 2
        PRIVILEGES_REQUIRED_HIGH = 3

    class UserInteraction(proto.Enum):
        r"""User Interaction.

        Values:
            USER_INTERACTION_UNSPECIFIED (0):
                Unspecified.
            USER_INTERACTION_NONE (1):
                No user interaction required (UI:N). Defined
                in CVSS v3, v4.
            USER_INTERACTION_REQUIRED (2):
                User interaction required (UI:R). Defined in
                CVSS v3.
            USER_INTERACTION_PASSIVE (3):
                Passive user interaction required (UI:P).
                Defined in CVSS v4.
            USER_INTERACTION_ACTIVE (4):
                Active user interaction required (UI:A).
                Defined in CVSS v4.
        """

        USER_INTERACTION_UNSPECIFIED = 0
        USER_INTERACTION_NONE = 1
        USER_INTERACTION_REQUIRED = 2
        USER_INTERACTION_PASSIVE = 3
        USER_INTERACTION_ACTIVE = 4

    class Scope(proto.Enum):
        r"""Scope.

        Values:
            SCOPE_UNSPECIFIED (0):
                Unspecified.
            SCOPE_UNCHANGED (1):
                Scope: Unchanged (S:U). Defined in CVSS v3.
            SCOPE_CHANGED (2):
                Scope: Changed (S:C). Defined in CVSS v3.
        """

        SCOPE_UNSPECIFIED = 0
        SCOPE_UNCHANGED = 1
        SCOPE_CHANGED = 2

    class Impact(proto.Enum):
        r"""Impact.

        Values:
            IMPACT_UNSPECIFIED (0):
                Unspecified.
            IMPACT_HIGH (1):
                High impact (H). Defined in CVSS v3, v4.
            IMPACT_LOW (2):
                Low impact (L). Defined in CVSS v3, v4.
            IMPACT_NONE (3):
                No impact (N). Defined in CVSS v2, v3, v4.
            IMPACT_PARTIAL (4):
                Partial impact (P). Defined in CVSS v2.
            IMPACT_COMPLETE (5):
                Complete impact (C). Defined in CVSS v2.
        """

        IMPACT_UNSPECIFIED = 0
        IMPACT_HIGH = 1
        IMPACT_LOW = 2
        IMPACT_NONE = 3
        IMPACT_PARTIAL = 4
        IMPACT_COMPLETE = 5

    class AttackRequirements(proto.Enum):
        r"""Attack Requirements.

        Values:
            ATTACK_REQUIREMENTS_UNSPECIFIED (0):
                Unspecified.
            ATTACK_REQUIREMENTS_NONE (1):
                No attack requirements (AT:N). Defined in
                CVSS v4.
            ATTACK_REQUIREMENTS_PRESENT (2):
                Attack requirements: Present (AT:P). Defined
                in CVSS v4.
        """

        ATTACK_REQUIREMENTS_UNSPECIFIED = 0
        ATTACK_REQUIREMENTS_NONE = 1
        ATTACK_REQUIREMENTS_PRESENT = 2

    class ExploitMaturity(proto.Enum):
        r"""Exploit Maturity (E). Defined in CVSS v4.

        Values:
            EXPLOIT_MATURITY_UNSPECIFIED (0):
                Unspecified.
            EXPLOIT_MATURITY_NOT_DEFINED (1):
                Exploit maturity: Not defined (E:X). Defined
                in CVSS v4.
            EXPLOIT_MATURITY_ATTACKED (2):
                Exploit maturity: Attacked (E:A). Defined in
                CVSS v4.
            EXPLOIT_MATURITY_POC (3):
                Exploit maturity: Proof-of-concept (E:P).
                Defined in CVSS v4.
            EXPLOIT_MATURITY_UNREPORTED (4):
                Exploit maturity: Unreported (E:U). Defined
                in CVSS v4.
        """

        EXPLOIT_MATURITY_UNSPECIFIED = 0
        EXPLOIT_MATURITY_NOT_DEFINED = 1
        EXPLOIT_MATURITY_ATTACKED = 2
        EXPLOIT_MATURITY_POC = 3
        EXPLOIT_MATURITY_UNREPORTED = 4

    base_score: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    exploitability_score: float = proto.Field(
        proto.FLOAT,
        number=2,
    )
    impact_score: float = proto.Field(
        proto.FLOAT,
        number=3,
    )
    attack_vector: AttackVector = proto.Field(
        proto.ENUM,
        number=4,
        enum=AttackVector,
    )
    attack_complexity: AttackComplexity = proto.Field(
        proto.ENUM,
        number=5,
        enum=AttackComplexity,
    )
    authentication: Authentication = proto.Field(
        proto.ENUM,
        number=6,
        enum=Authentication,
    )
    privileges_required: PrivilegesRequired = proto.Field(
        proto.ENUM,
        number=7,
        enum=PrivilegesRequired,
    )
    user_interaction: UserInteraction = proto.Field(
        proto.ENUM,
        number=8,
        enum=UserInteraction,
    )
    scope: Scope = proto.Field(
        proto.ENUM,
        number=9,
        enum=Scope,
    )
    confidentiality_impact: Impact = proto.Field(
        proto.ENUM,
        number=10,
        enum=Impact,
    )
    integrity_impact: Impact = proto.Field(
        proto.ENUM,
        number=11,
        enum=Impact,
    )
    availability_impact: Impact = proto.Field(
        proto.ENUM,
        number=12,
        enum=Impact,
    )
    attack_requirements: AttackRequirements = proto.Field(
        proto.ENUM,
        number=13,
        enum=AttackRequirements,
    )
    vulnerable_system_confidentiality_impact: Impact = proto.Field(
        proto.ENUM,
        number=14,
        enum=Impact,
    )
    vulnerable_system_integrity_impact: Impact = proto.Field(
        proto.ENUM,
        number=15,
        enum=Impact,
    )
    vulnerable_system_availability_impact: Impact = proto.Field(
        proto.ENUM,
        number=16,
        enum=Impact,
    )
    subsequent_system_confidentiality_impact: Impact = proto.Field(
        proto.ENUM,
        number=17,
        enum=Impact,
    )
    subsequent_system_integrity_impact: Impact = proto.Field(
        proto.ENUM,
        number=18,
        enum=Impact,
    )
    subsequent_system_availability_impact: Impact = proto.Field(
        proto.ENUM,
        number=19,
        enum=Impact,
    )
    exploit_maturity: ExploitMaturity = proto.Field(
        proto.ENUM,
        number=20,
        enum=ExploitMaturity,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
