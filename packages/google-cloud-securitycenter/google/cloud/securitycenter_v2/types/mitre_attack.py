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
    package="google.cloud.securitycenter.v2",
    manifest={
        "MitreAttack",
    },
)


class MitreAttack(proto.Message):
    r"""MITRE ATT&CK tactics and techniques related to this finding.
    See: https://attack.mitre.org

    Attributes:
        primary_tactic (google.cloud.securitycenter_v2.types.MitreAttack.Tactic):
            The MITRE ATT&CK tactic most closely
            represented by this finding, if any.
        primary_techniques (MutableSequence[google.cloud.securitycenter_v2.types.MitreAttack.Technique]):
            The MITRE ATT&CK technique most closely represented by this
            finding, if any. primary_techniques is a repeated field
            because there are multiple levels of MITRE ATT&CK
            techniques. If the technique most closely represented by
            this finding is a sub-technique (e.g.
            ``SCANNING_IP_BLOCKS``), both the sub-technique and its
            parent technique(s) will be listed (e.g.
            ``SCANNING_IP_BLOCKS``, ``ACTIVE_SCANNING``).
        additional_tactics (MutableSequence[google.cloud.securitycenter_v2.types.MitreAttack.Tactic]):
            Additional MITRE ATT&CK tactics related to
            this finding, if any.
        additional_techniques (MutableSequence[google.cloud.securitycenter_v2.types.MitreAttack.Technique]):
            Additional MITRE ATT&CK techniques related to
            this finding, if any, along with any of their
            respective parent techniques.
        version (str):
            The MITRE ATT&CK version referenced by the
            above fields. E.g. "8".
    """

    class Tactic(proto.Enum):
        r"""MITRE ATT&CK tactics that can be referenced by SCC findings.
        See: https://attack.mitre.org/tactics/enterprise/

        Values:
            TACTIC_UNSPECIFIED (0):
                Unspecified value.
            RECONNAISSANCE (1):
                TA0043
            RESOURCE_DEVELOPMENT (2):
                TA0042
            INITIAL_ACCESS (5):
                TA0001
            EXECUTION (3):
                TA0002
            PERSISTENCE (6):
                TA0003
            PRIVILEGE_ESCALATION (8):
                TA0004
            DEFENSE_EVASION (7):
                TA0005
            CREDENTIAL_ACCESS (9):
                TA0006
            DISCOVERY (10):
                TA0007
            LATERAL_MOVEMENT (11):
                TA0008
            COLLECTION (12):
                TA0009
            COMMAND_AND_CONTROL (4):
                TA0011
            EXFILTRATION (13):
                TA0010
            IMPACT (14):
                TA0040
        """

        TACTIC_UNSPECIFIED = 0
        RECONNAISSANCE = 1
        RESOURCE_DEVELOPMENT = 2
        INITIAL_ACCESS = 5
        EXECUTION = 3
        PERSISTENCE = 6
        PRIVILEGE_ESCALATION = 8
        DEFENSE_EVASION = 7
        CREDENTIAL_ACCESS = 9
        DISCOVERY = 10
        LATERAL_MOVEMENT = 11
        COLLECTION = 12
        COMMAND_AND_CONTROL = 4
        EXFILTRATION = 13
        IMPACT = 14

    class Technique(proto.Enum):
        r"""MITRE ATT&CK techniques that can be referenced by Security
        Command Center findings. See:
        https://attack.mitre.org/techniques/enterprise/

        Values:
            TECHNIQUE_UNSPECIFIED (0):
                Unspecified value.
            DATA_OBFUSCATION (70):
                T1001
            DATA_OBFUSCATION_STEGANOGRAPHY (71):
                T1001.002
            OS_CREDENTIAL_DUMPING (114):
                T1003
            OS_CREDENTIAL_DUMPING_PROC_FILESYSTEM (115):
                T1003.007
            OS_CREDENTIAL_DUMPING_ETC_PASSWORD_AND_ETC_SHADOW (122):
                T1003.008
            DATA_FROM_LOCAL_SYSTEM (117):
                T1005
            AUTOMATED_EXFILTRATION (68):
                T1020
            OBFUSCATED_FILES_OR_INFO (72):
                T1027
            STEGANOGRAPHY (73):
                T1027.003
            COMPILE_AFTER_DELIVERY (74):
                T1027.004
            COMMAND_OBFUSCATION (75):
                T1027.010
            SCHEDULED_TRANSFER (120):
                T1029
            SYSTEM_OWNER_USER_DISCOVERY (118):
                T1033
            MASQUERADING (49):
                T1036
            MATCH_LEGITIMATE_NAME_OR_LOCATION (50):
                T1036.005
            BOOT_OR_LOGON_INITIALIZATION_SCRIPTS (37):
                T1037
            STARTUP_ITEMS (38):
                T1037.005
            NETWORK_SERVICE_DISCOVERY (32):
                T1046
            SCHEDULED_TASK_JOB (89):
                T1053
            SCHEDULED_TASK_JOB_CRON (119):
                T1053.003
            CONTAINER_ORCHESTRATION_JOB (90):
                T1053.007
            PROCESS_INJECTION (93):
                T1055
            INPUT_CAPTURE (103):
                T1056
            INPUT_CAPTURE_KEYLOGGING (104):
                T1056.001
            PROCESS_DISCOVERY (56):
                T1057
            COMMAND_AND_SCRIPTING_INTERPRETER (6):
                T1059
            UNIX_SHELL (7):
                T1059.004
            PYTHON (59):
                T1059.006
            EXPLOITATION_FOR_PRIVILEGE_ESCALATION (63):
                T1068
            PERMISSION_GROUPS_DISCOVERY (18):
                T1069
            CLOUD_GROUPS (19):
                T1069.003
            INDICATOR_REMOVAL (123):
                T1070
            INDICATOR_REMOVAL_CLEAR_LINUX_OR_MAC_SYSTEM_LOGS (124):
                T1070.002
            INDICATOR_REMOVAL_CLEAR_COMMAND_HISTORY (125):
                T1070.003
            INDICATOR_REMOVAL_FILE_DELETION (64):
                T1070.004
            INDICATOR_REMOVAL_TIMESTOMP (128):
                T1070.006
            INDICATOR_REMOVAL_CLEAR_MAILBOX_DATA (126):
                T1070.008
            APPLICATION_LAYER_PROTOCOL (45):
                T1071
            DNS (46):
                T1071.004
            SOFTWARE_DEPLOYMENT_TOOLS (47):
                T1072
            VALID_ACCOUNTS (14):
                T1078
            DEFAULT_ACCOUNTS (35):
                T1078.001
            LOCAL_ACCOUNTS (15):
                T1078.003
            CLOUD_ACCOUNTS (16):
                T1078.004
            FILE_AND_DIRECTORY_DISCOVERY (121):
                T1083
            ACCOUNT_DISCOVERY_LOCAL_ACCOUNT (116):
                T1087.001
            PROXY (9):
                T1090
            EXTERNAL_PROXY (10):
                T1090.002
            MULTI_HOP_PROXY (11):
                T1090.003
            ACCOUNT_MANIPULATION (22):
                T1098
            ADDITIONAL_CLOUD_CREDENTIALS (40):
                T1098.001
            ADDITIONAL_CLOUD_ROLES (67):
                T1098.003
            SSH_AUTHORIZED_KEYS (23):
                T1098.004
            ADDITIONAL_CONTAINER_CLUSTER_ROLES (58):
                T1098.006
            MULTI_STAGE_CHANNELS (76):
                T1104
            INGRESS_TOOL_TRANSFER (3):
                T1105
            NATIVE_API (4):
                T1106
            BRUTE_FORCE (44):
                T1110
            AUTOMATED_COLLECTION (94):
                T1119
            SHARED_MODULES (5):
                T1129
            DATA_ENCODING (77):
                T1132
            STANDARD_ENCODING (78):
                T1132.001
            ACCESS_TOKEN_MANIPULATION (33):
                T1134
            TOKEN_IMPERSONATION_OR_THEFT (39):
                T1134.001
            CREATE_ACCOUNT (79):
                T1136
            LOCAL_ACCOUNT (80):
                T1136.001
            DEOBFUSCATE_DECODE_FILES_OR_INFO (95):
                T1140
            EXPLOIT_PUBLIC_FACING_APPLICATION (27):
                T1190
            SUPPLY_CHAIN_COMPROMISE (129):
                T1195
            COMPROMISE_SOFTWARE_DEPENDENCIES_AND_DEVELOPMENT_TOOLS (130):
                T1195.001
            EXPLOITATION_FOR_CLIENT_EXECUTION (134):
                T1203
            USER_EXECUTION (69):
                T1204
            LINUX_AND_MAC_FILE_AND_DIRECTORY_PERMISSIONS_MODIFICATION (135):
                T1222.002
            DOMAIN_POLICY_MODIFICATION (30):
                T1484
            DATA_DESTRUCTION (29):
                T1485
            DATA_ENCRYPTED_FOR_IMPACT (132):
                T1486
            SERVICE_STOP (52):
                T1489
            INHIBIT_SYSTEM_RECOVERY (36):
                T1490
            FIRMWARE_CORRUPTION (81):
                T1495
            RESOURCE_HIJACKING (8):
                T1496
            NETWORK_DENIAL_OF_SERVICE (17):
                T1498
            CLOUD_SERVICE_DISCOVERY (48):
                T1526
            STEAL_APPLICATION_ACCESS_TOKEN (42):
                T1528
            ACCOUNT_ACCESS_REMOVAL (51):
                T1531
            TRANSFER_DATA_TO_CLOUD_ACCOUNT (91):
                T1537
            STEAL_WEB_SESSION_COOKIE (25):
                T1539
            CREATE_OR_MODIFY_SYSTEM_PROCESS (24):
                T1543
            EVENT_TRIGGERED_EXECUTION (65):
                T1546
            BOOT_OR_LOGON_AUTOSTART_EXECUTION (82):
                T1547
            KERNEL_MODULES_AND_EXTENSIONS (83):
                T1547.006
            SHORTCUT_MODIFICATION (127):
                T1547.009
            ABUSE_ELEVATION_CONTROL_MECHANISM (34):
                T1548
            ABUSE_ELEVATION_CONTROL_MECHANISM_SETUID_AND_SETGID (136):
                T1548.001
            ABUSE_ELEVATION_CONTROL_MECHANISM_SUDO_AND_SUDO_CACHING (109):
                T1548.003
            UNSECURED_CREDENTIALS (13):
                T1552
            CREDENTIALS_IN_FILES (105):
                T1552.001
            BASH_HISTORY (96):
                T1552.003
            PRIVATE_KEYS (97):
                T1552.004
            SUBVERT_TRUST_CONTROL (106):
                T1553
            INSTALL_ROOT_CERTIFICATE (107):
                T1553.004
            COMPROMISE_HOST_SOFTWARE_BINARY (84):
                T1554
            CREDENTIALS_FROM_PASSWORD_STORES (98):
                T1555
            MODIFY_AUTHENTICATION_PROCESS (28):
                T1556
            PLUGGABLE_AUTHENTICATION_MODULES (108):
                T1556.003
            MULTI_FACTOR_AUTHENTICATION (137):
                T1556.006
            IMPAIR_DEFENSES (31):
                T1562
            DISABLE_OR_MODIFY_TOOLS (55):
                T1562.001
            INDICATOR_BLOCKING (110):
                T1562.006
            DISABLE_OR_MODIFY_LINUX_AUDIT_SYSTEM (111):
                T1562.012
            HIDE_ARTIFACTS (85):
                T1564
            HIDDEN_FILES_AND_DIRECTORIES (86):
                T1564.001
            HIDDEN_USERS (87):
                T1564.002
            EXFILTRATION_OVER_WEB_SERVICE (20):
                T1567
            EXFILTRATION_TO_CLOUD_STORAGE (21):
                T1567.002
            DYNAMIC_RESOLUTION (12):
                T1568
            LATERAL_TOOL_TRANSFER (41):
                T1570
            HIJACK_EXECUTION_FLOW (112):
                T1574
            HIJACK_EXECUTION_FLOW_DYNAMIC_LINKER_HIJACKING (113):
                T1574.006
            MODIFY_CLOUD_COMPUTE_INFRASTRUCTURE (26):
                T1578
            CREATE_SNAPSHOT (54):
                T1578.001
            CLOUD_INFRASTRUCTURE_DISCOVERY (53):
                T1580
            DEVELOP_CAPABILITIES (99):
                T1587
            DEVELOP_CAPABILITIES_MALWARE (100):
                T1587.001
            OBTAIN_CAPABILITIES (43):
                T1588
            OBTAIN_CAPABILITIES_MALWARE (101):
                T1588.001
            OBTAIN_CAPABILITIES_VULNERABILITIES (133):
                T1588.006
            ACTIVE_SCANNING (1):
                T1595
            SCANNING_IP_BLOCKS (2):
                T1595.001
            STAGE_CAPABILITIES (88):
                T1608
            UPLOAD_MALWARE (102):
                T1608.001
            CONTAINER_ADMINISTRATION_COMMAND (60):
                T1609
            DEPLOY_CONTAINER (66):
                T1610
            ESCAPE_TO_HOST (61):
                T1611
            CONTAINER_AND_RESOURCE_DISCOVERY (57):
                T1613
            REFLECTIVE_CODE_LOADING (92):
                T1620
            STEAL_OR_FORGE_AUTHENTICATION_CERTIFICATES (62):
                T1649
            FINANCIAL_THEFT (131):
                T1657
        """

        TECHNIQUE_UNSPECIFIED = 0
        DATA_OBFUSCATION = 70
        DATA_OBFUSCATION_STEGANOGRAPHY = 71
        OS_CREDENTIAL_DUMPING = 114
        OS_CREDENTIAL_DUMPING_PROC_FILESYSTEM = 115
        OS_CREDENTIAL_DUMPING_ETC_PASSWORD_AND_ETC_SHADOW = 122
        DATA_FROM_LOCAL_SYSTEM = 117
        AUTOMATED_EXFILTRATION = 68
        OBFUSCATED_FILES_OR_INFO = 72
        STEGANOGRAPHY = 73
        COMPILE_AFTER_DELIVERY = 74
        COMMAND_OBFUSCATION = 75
        SCHEDULED_TRANSFER = 120
        SYSTEM_OWNER_USER_DISCOVERY = 118
        MASQUERADING = 49
        MATCH_LEGITIMATE_NAME_OR_LOCATION = 50
        BOOT_OR_LOGON_INITIALIZATION_SCRIPTS = 37
        STARTUP_ITEMS = 38
        NETWORK_SERVICE_DISCOVERY = 32
        SCHEDULED_TASK_JOB = 89
        SCHEDULED_TASK_JOB_CRON = 119
        CONTAINER_ORCHESTRATION_JOB = 90
        PROCESS_INJECTION = 93
        INPUT_CAPTURE = 103
        INPUT_CAPTURE_KEYLOGGING = 104
        PROCESS_DISCOVERY = 56
        COMMAND_AND_SCRIPTING_INTERPRETER = 6
        UNIX_SHELL = 7
        PYTHON = 59
        EXPLOITATION_FOR_PRIVILEGE_ESCALATION = 63
        PERMISSION_GROUPS_DISCOVERY = 18
        CLOUD_GROUPS = 19
        INDICATOR_REMOVAL = 123
        INDICATOR_REMOVAL_CLEAR_LINUX_OR_MAC_SYSTEM_LOGS = 124
        INDICATOR_REMOVAL_CLEAR_COMMAND_HISTORY = 125
        INDICATOR_REMOVAL_FILE_DELETION = 64
        INDICATOR_REMOVAL_TIMESTOMP = 128
        INDICATOR_REMOVAL_CLEAR_MAILBOX_DATA = 126
        APPLICATION_LAYER_PROTOCOL = 45
        DNS = 46
        SOFTWARE_DEPLOYMENT_TOOLS = 47
        VALID_ACCOUNTS = 14
        DEFAULT_ACCOUNTS = 35
        LOCAL_ACCOUNTS = 15
        CLOUD_ACCOUNTS = 16
        FILE_AND_DIRECTORY_DISCOVERY = 121
        ACCOUNT_DISCOVERY_LOCAL_ACCOUNT = 116
        PROXY = 9
        EXTERNAL_PROXY = 10
        MULTI_HOP_PROXY = 11
        ACCOUNT_MANIPULATION = 22
        ADDITIONAL_CLOUD_CREDENTIALS = 40
        ADDITIONAL_CLOUD_ROLES = 67
        SSH_AUTHORIZED_KEYS = 23
        ADDITIONAL_CONTAINER_CLUSTER_ROLES = 58
        MULTI_STAGE_CHANNELS = 76
        INGRESS_TOOL_TRANSFER = 3
        NATIVE_API = 4
        BRUTE_FORCE = 44
        AUTOMATED_COLLECTION = 94
        SHARED_MODULES = 5
        DATA_ENCODING = 77
        STANDARD_ENCODING = 78
        ACCESS_TOKEN_MANIPULATION = 33
        TOKEN_IMPERSONATION_OR_THEFT = 39
        CREATE_ACCOUNT = 79
        LOCAL_ACCOUNT = 80
        DEOBFUSCATE_DECODE_FILES_OR_INFO = 95
        EXPLOIT_PUBLIC_FACING_APPLICATION = 27
        SUPPLY_CHAIN_COMPROMISE = 129
        COMPROMISE_SOFTWARE_DEPENDENCIES_AND_DEVELOPMENT_TOOLS = 130
        EXPLOITATION_FOR_CLIENT_EXECUTION = 134
        USER_EXECUTION = 69
        LINUX_AND_MAC_FILE_AND_DIRECTORY_PERMISSIONS_MODIFICATION = 135
        DOMAIN_POLICY_MODIFICATION = 30
        DATA_DESTRUCTION = 29
        DATA_ENCRYPTED_FOR_IMPACT = 132
        SERVICE_STOP = 52
        INHIBIT_SYSTEM_RECOVERY = 36
        FIRMWARE_CORRUPTION = 81
        RESOURCE_HIJACKING = 8
        NETWORK_DENIAL_OF_SERVICE = 17
        CLOUD_SERVICE_DISCOVERY = 48
        STEAL_APPLICATION_ACCESS_TOKEN = 42
        ACCOUNT_ACCESS_REMOVAL = 51
        TRANSFER_DATA_TO_CLOUD_ACCOUNT = 91
        STEAL_WEB_SESSION_COOKIE = 25
        CREATE_OR_MODIFY_SYSTEM_PROCESS = 24
        EVENT_TRIGGERED_EXECUTION = 65
        BOOT_OR_LOGON_AUTOSTART_EXECUTION = 82
        KERNEL_MODULES_AND_EXTENSIONS = 83
        SHORTCUT_MODIFICATION = 127
        ABUSE_ELEVATION_CONTROL_MECHANISM = 34
        ABUSE_ELEVATION_CONTROL_MECHANISM_SETUID_AND_SETGID = 136
        ABUSE_ELEVATION_CONTROL_MECHANISM_SUDO_AND_SUDO_CACHING = 109
        UNSECURED_CREDENTIALS = 13
        CREDENTIALS_IN_FILES = 105
        BASH_HISTORY = 96
        PRIVATE_KEYS = 97
        SUBVERT_TRUST_CONTROL = 106
        INSTALL_ROOT_CERTIFICATE = 107
        COMPROMISE_HOST_SOFTWARE_BINARY = 84
        CREDENTIALS_FROM_PASSWORD_STORES = 98
        MODIFY_AUTHENTICATION_PROCESS = 28
        PLUGGABLE_AUTHENTICATION_MODULES = 108
        MULTI_FACTOR_AUTHENTICATION = 137
        IMPAIR_DEFENSES = 31
        DISABLE_OR_MODIFY_TOOLS = 55
        INDICATOR_BLOCKING = 110
        DISABLE_OR_MODIFY_LINUX_AUDIT_SYSTEM = 111
        HIDE_ARTIFACTS = 85
        HIDDEN_FILES_AND_DIRECTORIES = 86
        HIDDEN_USERS = 87
        EXFILTRATION_OVER_WEB_SERVICE = 20
        EXFILTRATION_TO_CLOUD_STORAGE = 21
        DYNAMIC_RESOLUTION = 12
        LATERAL_TOOL_TRANSFER = 41
        HIJACK_EXECUTION_FLOW = 112
        HIJACK_EXECUTION_FLOW_DYNAMIC_LINKER_HIJACKING = 113
        MODIFY_CLOUD_COMPUTE_INFRASTRUCTURE = 26
        CREATE_SNAPSHOT = 54
        CLOUD_INFRASTRUCTURE_DISCOVERY = 53
        DEVELOP_CAPABILITIES = 99
        DEVELOP_CAPABILITIES_MALWARE = 100
        OBTAIN_CAPABILITIES = 43
        OBTAIN_CAPABILITIES_MALWARE = 101
        OBTAIN_CAPABILITIES_VULNERABILITIES = 133
        ACTIVE_SCANNING = 1
        SCANNING_IP_BLOCKS = 2
        STAGE_CAPABILITIES = 88
        UPLOAD_MALWARE = 102
        CONTAINER_ADMINISTRATION_COMMAND = 60
        DEPLOY_CONTAINER = 66
        ESCAPE_TO_HOST = 61
        CONTAINER_AND_RESOURCE_DISCOVERY = 57
        REFLECTIVE_CODE_LOADING = 92
        STEAL_OR_FORGE_AUTHENTICATION_CERTIFICATES = 62
        FINANCIAL_THEFT = 131

    primary_tactic: Tactic = proto.Field(
        proto.ENUM,
        number=1,
        enum=Tactic,
    )
    primary_techniques: MutableSequence[Technique] = proto.RepeatedField(
        proto.ENUM,
        number=2,
        enum=Technique,
    )
    additional_tactics: MutableSequence[Tactic] = proto.RepeatedField(
        proto.ENUM,
        number=3,
        enum=Tactic,
    )
    additional_techniques: MutableSequence[Technique] = proto.RepeatedField(
        proto.ENUM,
        number=4,
        enum=Technique,
    )
    version: str = proto.Field(
        proto.STRING,
        number=5,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
