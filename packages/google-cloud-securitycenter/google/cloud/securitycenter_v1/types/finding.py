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
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.securitycenter_v1.types import access as gcs_access
from google.cloud.securitycenter_v1.types import agent as gcs_agent
from google.cloud.securitycenter_v1.types import agent_anomaly as gcs_agent_anomaly
from google.cloud.securitycenter_v1.types import (
    agent_session,
    compliance,
    connection,
    contact_details,
    container,
    external_system,
    file,
    group_membership,
    iam_binding,
    load_balancer,
    log_entry,
    org_policy,
    process,
)
from google.cloud.securitycenter_v1.types import application as gcs_application
from google.cloud.securitycenter_v1.types import attack_exposure as gcs_attack_exposure
from google.cloud.securitycenter_v1.types import (
    backup_disaster_recovery as gcs_backup_disaster_recovery,
)
from google.cloud.securitycenter_v1.types import chokepoint as gcs_chokepoint
from google.cloud.securitycenter_v1.types import cloud_armor as gcs_cloud_armor
from google.cloud.securitycenter_v1.types import (
    cloud_dlp_data_profile as gcs_cloud_dlp_data_profile,
)
from google.cloud.securitycenter_v1.types import (
    cloud_dlp_inspection as gcs_cloud_dlp_inspection,
)
from google.cloud.securitycenter_v1.types import database as gcs_database
from google.cloud.securitycenter_v1.types import exfiltration as gcs_exfiltration
from google.cloud.securitycenter_v1.types import (
    external_exposure as gcs_external_exposure,
)
from google.cloud.securitycenter_v1.types import indicator as gcs_indicator
from google.cloud.securitycenter_v1.types import kernel_rootkit as gcs_kernel_rootkit
from google.cloud.securitycenter_v1.types import kubernetes as gcs_kubernetes
from google.cloud.securitycenter_v1.types import mitre_attack as gcs_mitre_attack
from google.cloud.securitycenter_v1.types import notebook as gcs_notebook
from google.cloud.securitycenter_v1.types import security_marks as gcs_security_marks
from google.cloud.securitycenter_v1.types import (
    security_posture as gcs_security_posture,
)
from google.cloud.securitycenter_v1.types import (
    toxic_combination as gcs_toxic_combination,
)
from google.cloud.securitycenter_v1.types import vulnerability as gcs_vulnerability

__protobuf__ = proto.module(
    package="google.cloud.securitycenter.v1",
    manifest={
        "Finding",
    },
)


class Finding(proto.Message):
    r"""Security Command Center finding.

    A finding is a record of assessment data like security, risk,
    health, or privacy, that is ingested into Security Command
    Center for presentation, notification, analysis, policy testing,
    and enforcement. For example, a cross-site scripting (XSS)
    vulnerability in an App Engine application is a finding.

    Attributes:
        name (str):
            The `relative resource
            name <https://cloud.google.com/apis/design/resource_names#relative_resource_name>`__
            of the finding. Example:
            "organizations/{organization_id}/sources/{source_id}/findings/{finding_id}",
            "folders/{folder_id}/sources/{source_id}/findings/{finding_id}",
            "projects/{project_id}/sources/{source_id}/findings/{finding_id}".
        parent (str):
            The relative resource name of the source the finding belongs
            to. See:
            https://cloud.google.com/apis/design/resource_names#relative_resource_name
            This field is immutable after creation time. For example:
            "organizations/{organization_id}/sources/{source_id}".
        resource_name (str):
            For findings on Google Cloud resources, the full resource
            name of the Google Cloud resource this finding is for. See:
            https://cloud.google.com/apis/design/resource_names#full_resource_name
            When the finding is for a non-Google Cloud resource, the
            resourceName can be a customer or partner defined string.
            This field is immutable after creation time.
        state (google.cloud.securitycenter_v1.types.Finding.State):
            The state of the finding.
        category (str):
            The additional taxonomy group within findings from a given
            source. This field is immutable after creation time.
            Example: "XSS_FLASH_INJECTION".
        external_uri (str):
            The URI that, if available, points to a web
            page outside of Security Command Center where
            additional information about the finding can be
            found. This field is guaranteed to be either
            empty or a well formed URL.
        source_properties (MutableMapping[str, google.protobuf.struct_pb2.Value]):
            Source specific properties. These properties are managed by
            the source that writes the finding. The key names in the
            source_properties map must be between 1 and 255 characters,
            and must start with a letter and contain alphanumeric
            characters or underscores only.
        security_marks (google.cloud.securitycenter_v1.types.SecurityMarks):
            Output only. User specified security marks.
            These marks are entirely managed by the user and
            come from the SecurityMarks resource that
            belongs to the finding.
        event_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the finding was first detected. If
            an existing finding is updated, then this is the
            time the update occurred. For example, if the
            finding represents an open firewall, this
            property captures the time the detector believes
            the firewall became open. The accuracy is
            determined by the detector. If the finding is
            later resolved, then this time reflects when the
            finding was resolved. This must not be set to a
            value greater than the current timestamp.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time at which the finding was created in
            Security Command Center.
        severity (google.cloud.securitycenter_v1.types.Finding.Severity):
            The severity of the finding. This field is
            managed by the source that writes the finding.
        canonical_name (str):
            The canonical name of the finding. It's either
            "organizations/{organization_id}/sources/{source_id}/findings/{finding_id}",
            "folders/{folder_id}/sources/{source_id}/findings/{finding_id}"
            or
            "projects/{project_number}/sources/{source_id}/findings/{finding_id}",
            depending on the closest CRM ancestor of the resource
            associated with the finding.
        mute (google.cloud.securitycenter_v1.types.Finding.Mute):
            Indicates the mute state of a finding (either
            muted, unmuted or undefined). Unlike other
            attributes of a finding, a finding provider
            shouldn't set the value of mute.
        finding_class (google.cloud.securitycenter_v1.types.Finding.FindingClass):
            The class of the finding.
        indicator (google.cloud.securitycenter_v1.types.Indicator):
            Represents what's commonly known as an *indicator of
            compromise* (IoC) in computer forensics. This is an artifact
            observed on a network or in an operating system that, with
            high confidence, indicates a computer intrusion. For more
            information, see `Indicator of
            compromise <https://en.wikipedia.org/wiki/Indicator_of_compromise>`__.
        vulnerability (google.cloud.securitycenter_v1.types.Vulnerability):
            Represents vulnerability-specific fields like
            CVE and CVSS scores. CVE stands for Common
            Vulnerabilities and Exposures
            (https://cve.mitre.org/about/)
        mute_update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The most recent time this
            finding was muted or unmuted.
        external_systems (MutableMapping[str, google.cloud.securitycenter_v1.types.ExternalSystem]):
            Output only. Third party SIEM/SOAR fields
            within SCC, contains external system information
            and external system finding fields.
        mitre_attack (google.cloud.securitycenter_v1.types.MitreAttack):
            MITRE ATT&CK tactics and techniques related
            to this finding. See: https://attack.mitre.org
        access (google.cloud.securitycenter_v1.types.Access):
            Access details associated with the finding,
            such as more information on the caller, which
            method was accessed, and from where.
        connections (MutableSequence[google.cloud.securitycenter_v1.types.Connection]):
            Contains information about the IP connection
            associated with the finding.
        mute_initiator (str):
            Records additional information about the mute operation, for
            example, the `mute
            configuration </security-command-center/docs/how-to-mute-findings>`__
            that muted the finding and the user who muted the finding.
        mute_info (google.cloud.securitycenter_v1.types.Finding.MuteInfo):
            Output only. The mute information regarding
            this finding.
        processes (MutableSequence[google.cloud.securitycenter_v1.types.Process]):
            Represents operating system processes
            associated with the Finding.
        contacts (MutableMapping[str, google.cloud.securitycenter_v1.types.ContactDetails]):
            Output only. Map containing the points of contact for the
            given finding. The key represents the type of contact, while
            the value contains a list of all the contacts that pertain.
            Please refer to:
            https://cloud.google.com/resource-manager/docs/managing-notification-contacts#notification-categories

            ::

                {
                  "security": {
                    "contacts": [
                      {
                        "email": "person1@company.com"
                      },
                      {
                        "email": "person2@company.com"
                      }
                    ]
                  }
                }
        compliances (MutableSequence[google.cloud.securitycenter_v1.types.Compliance]):
            Contains compliance information for security
            standards associated to the finding.
        parent_display_name (str):
            Output only. The human readable display name
            of the finding source such as "Event Threat
            Detection" or "Security Health Analytics".
        description (str):
            Contains more details about the finding.
        exfiltration (google.cloud.securitycenter_v1.types.Exfiltration):
            Represents exfiltrations associated with the
            finding.
        iam_bindings (MutableSequence[google.cloud.securitycenter_v1.types.IamBinding]):
            Represents IAM bindings associated with the
            finding.
        next_steps (str):
            Steps to address the finding.
        module_name (str):
            Unique identifier of the module which
            generated the finding. Example:

            folders/598186756061/securityHealthAnalyticsSettings/customModules/56799441161885
        containers (MutableSequence[google.cloud.securitycenter_v1.types.Container]):
            Containers associated with the finding. This
            field provides information for both Kubernetes
            and non-Kubernetes containers.
        kubernetes (google.cloud.securitycenter_v1.types.Kubernetes):
            Kubernetes resources associated with the
            finding.
        database (google.cloud.securitycenter_v1.types.Database):
            Database associated with the finding.
        attack_exposure (google.cloud.securitycenter_v1.types.AttackExposure):
            The results of an attack path simulation
            relevant to this finding.
        files (MutableSequence[google.cloud.securitycenter_v1.types.File]):
            File associated with the finding.
        cloud_dlp_inspection (google.cloud.securitycenter_v1.types.CloudDlpInspection):
            Cloud Data Loss Prevention (Cloud DLP)
            inspection results that are associated with the
            finding.
        cloud_dlp_data_profile (google.cloud.securitycenter_v1.types.CloudDlpDataProfile):
            Cloud DLP data profile that is associated
            with the finding.
        kernel_rootkit (google.cloud.securitycenter_v1.types.KernelRootkit):
            Signature of the kernel rootkit.
        org_policies (MutableSequence[google.cloud.securitycenter_v1.types.OrgPolicy]):
            Contains information about the org policies
            associated with the finding.
        application (google.cloud.securitycenter_v1.types.Application):
            Represents an application associated with the
            finding.
        backup_disaster_recovery (google.cloud.securitycenter_v1.types.BackupDisasterRecovery):
            Fields related to Backup and DR findings.
        security_posture (google.cloud.securitycenter_v1.types.SecurityPosture):
            The security posture associated with the
            finding.
        log_entries (MutableSequence[google.cloud.securitycenter_v1.types.LogEntry]):
            Log entries that are relevant to the finding.
        load_balancers (MutableSequence[google.cloud.securitycenter_v1.types.LoadBalancer]):
            The load balancers associated with the
            finding.
        cloud_armor (google.cloud.securitycenter_v1.types.CloudArmor):
            Fields related to Cloud Armor findings.
        notebook (google.cloud.securitycenter_v1.types.Notebook):
            Notebook associated with the finding.
        toxic_combination (google.cloud.securitycenter_v1.types.ToxicCombination):
            Contains details about a group of security
            issues that, when the issues occur together,
            represent a greater risk than when the issues
            occur independently. A group of such issues is
            referred to as a toxic combination.
            This field cannot be updated. Its value is
            ignored in all update requests.
        group_memberships (MutableSequence[google.cloud.securitycenter_v1.types.GroupMembership]):
            Contains details about groups of which this
            finding is a member. A group is a collection of
            findings that are related in some way. This
            field cannot be updated. Its value is ignored in
            all update requests.
        chokepoint (google.cloud.securitycenter_v1.types.Chokepoint):
            Contains details about a chokepoint, which is a resource or
            resource group where high-risk attack paths converge, based
            on [attack path simulations]
            (https://cloud.google.com/security-command-center/docs/attack-exposure-learn#attack_path_simulations).
            This field cannot be updated. Its value is ignored in all
            update requests.
        external_exposure (google.cloud.securitycenter_v1.types.ExternalExposure):
            External exposure associated with the
            finding.
        agent (google.cloud.securitycenter_v1.types.Agent):
            Primary Agent that the specified finding was
            flagged for
        agent_sessions (MutableSequence[google.cloud.securitycenter_v1.types.AgentSession]):
            Conversational session(s) where the finding
            occurred.
        agent_anomaly (google.cloud.securitycenter_v1.types.AgentAnomaly):
            Details about behavior anomalies detected in
            AI agents.
    """

    class State(proto.Enum):
        r"""The state of the finding.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified state.
            ACTIVE (1):
                The finding requires attention and has not
                been addressed yet.
            INACTIVE (2):
                The finding has been fixed, triaged as a
                non-issue or otherwise addressed and is no
                longer active.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        INACTIVE = 2

    class Severity(proto.Enum):
        r"""The severity of the finding.

        Values:
            SEVERITY_UNSPECIFIED (0):
                This value is used for findings when a source
                doesn't write a severity value.
            CRITICAL (1):
                Vulnerability:

                A critical vulnerability is easily discoverable
                by an external actor, exploitable, and results
                in the direct ability to execute arbitrary code,
                exfiltrate data, and otherwise gain additional
                access and privileges to cloud resources and
                workloads. Examples include publicly accessible
                unprotected user data and public SSH access with
                weak or no passwords.

                Threat:

                Indicates a threat that is able to access,
                modify, or delete data or execute unauthorized
                code within existing resources.
            HIGH (2):
                Vulnerability:

                A high risk vulnerability can be easily
                discovered and exploited in combination with
                other vulnerabilities in order to gain direct
                access and the ability to execute arbitrary
                code, exfiltrate data, and otherwise gain
                additional access and privileges to cloud
                resources and workloads. An example is a
                database with weak or no passwords that is only
                accessible internally. This database could
                easily be compromised by an actor that had
                access to the internal network.

                Threat:

                Indicates a threat that is able to create new
                computational resources in an environment but
                not able to access data or execute code in
                existing resources.
            MEDIUM (3):
                Vulnerability:

                A medium risk vulnerability could be used by an
                actor to gain access to resources or privileges
                that enable them to eventually (through multiple
                steps or a complex exploit) gain access and the
                ability to execute arbitrary code or exfiltrate
                data. An example is a service account with
                access to more projects than it should have. If
                an actor gains access to the service account,
                they could potentially use that access to
                manipulate a project the service account was not
                intended to.

                Threat:

                Indicates a threat that is able to cause
                operational impact but may not access data or
                execute unauthorized code.
            LOW (4):
                Vulnerability:

                A low risk vulnerability hampers a security
                organization's ability to detect vulnerabilities
                or active threats in their deployment, or
                prevents the root cause investigation of
                security issues. An example is monitoring and
                logs being disabled for resource configurations
                and access.

                Threat:

                Indicates a threat that has obtained minimal
                access to an environment but is not able to
                access data, execute code, or create resources.
        """

        SEVERITY_UNSPECIFIED = 0
        CRITICAL = 1
        HIGH = 2
        MEDIUM = 3
        LOW = 4

    class Mute(proto.Enum):
        r"""Mute state a finding can be in.

        Values:
            MUTE_UNSPECIFIED (0):
                Unspecified.
            MUTED (1):
                Finding has been muted.
            UNMUTED (2):
                Finding has been unmuted.
            UNDEFINED (4):
                Finding has never been muted/unmuted.
        """

        MUTE_UNSPECIFIED = 0
        MUTED = 1
        UNMUTED = 2
        UNDEFINED = 4

    class FindingClass(proto.Enum):
        r"""Represents what kind of Finding it is.

        Values:
            FINDING_CLASS_UNSPECIFIED (0):
                Unspecified finding class.
            THREAT (1):
                Describes unwanted or malicious activity.
            VULNERABILITY (2):
                Describes a potential weakness in software
                that increases risk to Confidentiality &
                Integrity & Availability.
            MISCONFIGURATION (3):
                Describes a potential weakness in cloud
                resource/asset configuration that increases
                risk.
            OBSERVATION (4):
                Describes a security observation that is for
                informational purposes.
            SCC_ERROR (5):
                Describes an error that prevents some SCC
                functionality.
            POSTURE_VIOLATION (6):
                Describes a potential security risk due to a
                change in the security posture.
            TOXIC_COMBINATION (7):
                Describes a group of security issues that,
                when the issues occur together, represent a
                greater risk than when the issues occur
                independently. A group of such issues is
                referred to as a toxic combination.
            SENSITIVE_DATA_RISK (8):
                Describes a potential security risk to data
                assets that contain sensitive data.
            CHOKEPOINT (9):
                Describes a resource or resource group where
                high risk attack paths converge, based on attack
                path simulations (APS).
            EXTERNAL_EXPOSURE (10):
                Describes a potential security risk due to
                the resource being exposed to the internet.
        """

        FINDING_CLASS_UNSPECIFIED = 0
        THREAT = 1
        VULNERABILITY = 2
        MISCONFIGURATION = 3
        OBSERVATION = 4
        SCC_ERROR = 5
        POSTURE_VIOLATION = 6
        TOXIC_COMBINATION = 7
        SENSITIVE_DATA_RISK = 8
        CHOKEPOINT = 9
        EXTERNAL_EXPOSURE = 10

    class MuteInfo(proto.Message):
        r"""Mute information about the finding, including whether the
        finding has a static mute or any matching dynamic mute rules.

        Attributes:
            static_mute (google.cloud.securitycenter_v1.types.Finding.MuteInfo.StaticMute):
                If set, the static mute applied to this
                finding. Static mutes override dynamic mutes. If
                unset, there is no static mute.
            dynamic_mute_records (MutableSequence[google.cloud.securitycenter_v1.types.Finding.MuteInfo.DynamicMuteRecord]):
                The list of dynamic mute rules that currently
                match the finding.
        """

        class StaticMute(proto.Message):
            r"""Information about the static mute state. A static mute state
            overrides any dynamic mute rules that apply to this finding. The
            static mute state can be set by a static mute rule or by muting
            the finding directly.

            Attributes:
                state (google.cloud.securitycenter_v1.types.Finding.Mute):
                    The static mute state. If the value is ``MUTED`` or
                    ``UNMUTED``, then the finding's overall mute state will have
                    the same value.
                apply_time (google.protobuf.timestamp_pb2.Timestamp):
                    When the static mute was applied.
            """

            state: "Finding.Mute" = proto.Field(
                proto.ENUM,
                number=1,
                enum="Finding.Mute",
            )
            apply_time: timestamp_pb2.Timestamp = proto.Field(
                proto.MESSAGE,
                number=2,
                message=timestamp_pb2.Timestamp,
            )

        class DynamicMuteRecord(proto.Message):
            r"""The record of a dynamic mute rule that matches the finding.

            Attributes:
                mute_config (str):
                    The relative resource name of the mute rule, represented by
                    a mute config, that created this record, for example
                    ``organizations/123/muteConfigs/mymuteconfig`` or
                    ``organizations/123/locations/global/muteConfigs/mymuteconfig``.
                match_time (google.protobuf.timestamp_pb2.Timestamp):
                    When the dynamic mute rule first matched the
                    finding.
            """

            mute_config: str = proto.Field(
                proto.STRING,
                number=1,
            )
            match_time: timestamp_pb2.Timestamp = proto.Field(
                proto.MESSAGE,
                number=2,
                message=timestamp_pb2.Timestamp,
            )

        static_mute: "Finding.MuteInfo.StaticMute" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="Finding.MuteInfo.StaticMute",
        )
        dynamic_mute_records: MutableSequence["Finding.MuteInfo.DynamicMuteRecord"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="Finding.MuteInfo.DynamicMuteRecord",
            )
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=2,
    )
    resource_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )
    category: str = proto.Field(
        proto.STRING,
        number=5,
    )
    external_uri: str = proto.Field(
        proto.STRING,
        number=6,
    )
    source_properties: MutableMapping[str, struct_pb2.Value] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=7,
        message=struct_pb2.Value,
    )
    security_marks: gcs_security_marks.SecurityMarks = proto.Field(
        proto.MESSAGE,
        number=8,
        message=gcs_security_marks.SecurityMarks,
    )
    event_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    severity: Severity = proto.Field(
        proto.ENUM,
        number=12,
        enum=Severity,
    )
    canonical_name: str = proto.Field(
        proto.STRING,
        number=14,
    )
    mute: Mute = proto.Field(
        proto.ENUM,
        number=15,
        enum=Mute,
    )
    finding_class: FindingClass = proto.Field(
        proto.ENUM,
        number=17,
        enum=FindingClass,
    )
    indicator: gcs_indicator.Indicator = proto.Field(
        proto.MESSAGE,
        number=18,
        message=gcs_indicator.Indicator,
    )
    vulnerability: gcs_vulnerability.Vulnerability = proto.Field(
        proto.MESSAGE,
        number=20,
        message=gcs_vulnerability.Vulnerability,
    )
    mute_update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=21,
        message=timestamp_pb2.Timestamp,
    )
    external_systems: MutableMapping[str, external_system.ExternalSystem] = (
        proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=22,
            message=external_system.ExternalSystem,
        )
    )
    mitre_attack: gcs_mitre_attack.MitreAttack = proto.Field(
        proto.MESSAGE,
        number=25,
        message=gcs_mitre_attack.MitreAttack,
    )
    access: gcs_access.Access = proto.Field(
        proto.MESSAGE,
        number=26,
        message=gcs_access.Access,
    )
    connections: MutableSequence[connection.Connection] = proto.RepeatedField(
        proto.MESSAGE,
        number=31,
        message=connection.Connection,
    )
    mute_initiator: str = proto.Field(
        proto.STRING,
        number=28,
    )
    mute_info: MuteInfo = proto.Field(
        proto.MESSAGE,
        number=61,
        message=MuteInfo,
    )
    processes: MutableSequence[process.Process] = proto.RepeatedField(
        proto.MESSAGE,
        number=30,
        message=process.Process,
    )
    contacts: MutableMapping[str, contact_details.ContactDetails] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=33,
        message=contact_details.ContactDetails,
    )
    compliances: MutableSequence[compliance.Compliance] = proto.RepeatedField(
        proto.MESSAGE,
        number=34,
        message=compliance.Compliance,
    )
    parent_display_name: str = proto.Field(
        proto.STRING,
        number=36,
    )
    description: str = proto.Field(
        proto.STRING,
        number=37,
    )
    exfiltration: gcs_exfiltration.Exfiltration = proto.Field(
        proto.MESSAGE,
        number=38,
        message=gcs_exfiltration.Exfiltration,
    )
    iam_bindings: MutableSequence[iam_binding.IamBinding] = proto.RepeatedField(
        proto.MESSAGE,
        number=39,
        message=iam_binding.IamBinding,
    )
    next_steps: str = proto.Field(
        proto.STRING,
        number=40,
    )
    module_name: str = proto.Field(
        proto.STRING,
        number=41,
    )
    containers: MutableSequence[container.Container] = proto.RepeatedField(
        proto.MESSAGE,
        number=42,
        message=container.Container,
    )
    kubernetes: gcs_kubernetes.Kubernetes = proto.Field(
        proto.MESSAGE,
        number=43,
        message=gcs_kubernetes.Kubernetes,
    )
    database: gcs_database.Database = proto.Field(
        proto.MESSAGE,
        number=44,
        message=gcs_database.Database,
    )
    attack_exposure: gcs_attack_exposure.AttackExposure = proto.Field(
        proto.MESSAGE,
        number=45,
        message=gcs_attack_exposure.AttackExposure,
    )
    files: MutableSequence[file.File] = proto.RepeatedField(
        proto.MESSAGE,
        number=46,
        message=file.File,
    )
    cloud_dlp_inspection: gcs_cloud_dlp_inspection.CloudDlpInspection = proto.Field(
        proto.MESSAGE,
        number=48,
        message=gcs_cloud_dlp_inspection.CloudDlpInspection,
    )
    cloud_dlp_data_profile: gcs_cloud_dlp_data_profile.CloudDlpDataProfile = (
        proto.Field(
            proto.MESSAGE,
            number=49,
            message=gcs_cloud_dlp_data_profile.CloudDlpDataProfile,
        )
    )
    kernel_rootkit: gcs_kernel_rootkit.KernelRootkit = proto.Field(
        proto.MESSAGE,
        number=50,
        message=gcs_kernel_rootkit.KernelRootkit,
    )
    org_policies: MutableSequence[org_policy.OrgPolicy] = proto.RepeatedField(
        proto.MESSAGE,
        number=51,
        message=org_policy.OrgPolicy,
    )
    application: gcs_application.Application = proto.Field(
        proto.MESSAGE,
        number=53,
        message=gcs_application.Application,
    )
    backup_disaster_recovery: gcs_backup_disaster_recovery.BackupDisasterRecovery = (
        proto.Field(
            proto.MESSAGE,
            number=55,
            message=gcs_backup_disaster_recovery.BackupDisasterRecovery,
        )
    )
    security_posture: gcs_security_posture.SecurityPosture = proto.Field(
        proto.MESSAGE,
        number=56,
        message=gcs_security_posture.SecurityPosture,
    )
    log_entries: MutableSequence[log_entry.LogEntry] = proto.RepeatedField(
        proto.MESSAGE,
        number=57,
        message=log_entry.LogEntry,
    )
    load_balancers: MutableSequence[load_balancer.LoadBalancer] = proto.RepeatedField(
        proto.MESSAGE,
        number=58,
        message=load_balancer.LoadBalancer,
    )
    cloud_armor: gcs_cloud_armor.CloudArmor = proto.Field(
        proto.MESSAGE,
        number=59,
        message=gcs_cloud_armor.CloudArmor,
    )
    notebook: gcs_notebook.Notebook = proto.Field(
        proto.MESSAGE,
        number=63,
        message=gcs_notebook.Notebook,
    )
    toxic_combination: gcs_toxic_combination.ToxicCombination = proto.Field(
        proto.MESSAGE,
        number=64,
        message=gcs_toxic_combination.ToxicCombination,
    )
    group_memberships: MutableSequence[group_membership.GroupMembership] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=65,
            message=group_membership.GroupMembership,
        )
    )
    chokepoint: gcs_chokepoint.Chokepoint = proto.Field(
        proto.MESSAGE,
        number=77,
        message=gcs_chokepoint.Chokepoint,
    )
    external_exposure: gcs_external_exposure.ExternalExposure = proto.Field(
        proto.MESSAGE,
        number=84,
        message=gcs_external_exposure.ExternalExposure,
    )
    agent: gcs_agent.Agent = proto.Field(
        proto.MESSAGE,
        number=88,
        message=gcs_agent.Agent,
    )
    agent_sessions: MutableSequence[agent_session.AgentSession] = proto.RepeatedField(
        proto.MESSAGE,
        number=89,
        message=agent_session.AgentSession,
    )
    agent_anomaly: gcs_agent_anomaly.AgentAnomaly = proto.Field(
        proto.MESSAGE,
        number=90,
        message=gcs_agent_anomaly.AgentAnomaly,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
