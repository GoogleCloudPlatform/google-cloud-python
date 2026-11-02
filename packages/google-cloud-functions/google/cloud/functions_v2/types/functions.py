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

import google.protobuf.any_pb2 as any_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.type.date_pb2 as date_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.functions.v2",
    manifest={
        "OperationType",
        "Environment",
        "Function",
        "StateMessage",
        "StorageSource",
        "RepoSource",
        "Source",
        "SourceProvenance",
        "BuildConfig",
        "ServiceConfig",
        "SecretEnvVar",
        "SecretVolume",
        "EventTrigger",
        "EventFilter",
        "GetFunctionRequest",
        "ListFunctionsRequest",
        "ListFunctionsResponse",
        "CreateFunctionRequest",
        "UpdateFunctionRequest",
        "DeleteFunctionRequest",
        "GenerateUploadUrlRequest",
        "GenerateUploadUrlResponse",
        "GenerateDownloadUrlRequest",
        "GenerateDownloadUrlResponse",
        "ListRuntimesRequest",
        "ListRuntimesResponse",
        "AutomaticUpdatePolicy",
        "OnDeployUpdatePolicy",
        "OperationMetadata",
        "LocationMetadata",
        "Stage",
    },
)


class OperationType(proto.Enum):
    r"""The type of the long running operation.

    Values:
        OPERATIONTYPE_UNSPECIFIED (0):
            Unspecified
        CREATE_FUNCTION (1):
            CreateFunction
        UPDATE_FUNCTION (2):
            UpdateFunction
        DELETE_FUNCTION (3):
            DeleteFunction
    """

    OPERATIONTYPE_UNSPECIFIED = 0
    CREATE_FUNCTION = 1
    UPDATE_FUNCTION = 2
    DELETE_FUNCTION = 3


class Environment(proto.Enum):
    r"""The environment the function is hosted on.

    Values:
        ENVIRONMENT_UNSPECIFIED (0):
            Unspecified
        GEN_1 (1):
            Gen 1
        GEN_2 (2):
            Gen 2
    """

    ENVIRONMENT_UNSPECIFIED = 0
    GEN_1 = 1
    GEN_2 = 2


class Function(proto.Message):
    r"""Describes a Cloud Function that contains user computation
    executed in response to an event. It encapsulates function and
    trigger configurations.

    Attributes:
        name (str):
            A user-defined name of the function. Function names must be
            unique globally and match pattern
            ``projects/*/locations/*/functions/*``
        description (str):
            User-provided description of a function.
        build_config (google.cloud.functions_v2.types.BuildConfig):
            Describes the Build step of the function that
            builds a container from the given source.
        service_config (google.cloud.functions_v2.types.ServiceConfig):
            Describes the Service being deployed.
            Currently deploys services to Cloud Run (fully
            managed).
        event_trigger (google.cloud.functions_v2.types.EventTrigger):
            An Eventarc trigger managed by Google Cloud
            Functions that fires events in response to a
            condition in another service.
        state (google.cloud.functions_v2.types.Function.State):
            Output only. State of the function.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last update timestamp of a
            Cloud Function.
        labels (MutableMapping[str, str]):
            Labels associated with this Cloud Function.
        state_messages (MutableSequence[google.cloud.functions_v2.types.StateMessage]):
            Output only. State Messages for this Cloud
            Function.
        environment (google.cloud.functions_v2.types.Environment):
            Describe whether the function is 1st Gen or
            2nd Gen.
        url (str):
            Output only. The deployed url for the
            function.
        kms_key_name (str):
            Resource name of a KMS crypto key (managed by the user) used
            to encrypt/decrypt function resources.

            It must match the pattern
            ``projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}``.
        satisfies_pzs (bool):
            Output only. Reserved for future use.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The create timestamp of a Cloud
            Function. This is only applicable to 2nd Gen
            functions.
    """

    class State(proto.Enum):
        r"""Describes the current state of the function.

        Values:
            STATE_UNSPECIFIED (0):
                Not specified. Invalid state.
            ACTIVE (1):
                Function has been successfully deployed and
                is serving.
            FAILED (2):
                Function deployment failed and the function
                is not serving.
            DEPLOYING (3):
                Function is being created or updated.
            DELETING (4):
                Function is being deleted.
            UNKNOWN (5):
                Function deployment failed and the function
                serving state is undefined. The function should
                be updated or deleted to move it out of this
                state.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        FAILED = 2
        DEPLOYING = 3
        DELETING = 4
        UNKNOWN = 5

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    build_config: "BuildConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="BuildConfig",
    )
    service_config: "ServiceConfig" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="ServiceConfig",
    )
    event_trigger: "EventTrigger" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="EventTrigger",
    )
    state: State = proto.Field(
        proto.ENUM,
        number=6,
        enum=State,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=8,
    )
    state_messages: MutableSequence["StateMessage"] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="StateMessage",
    )
    environment: "Environment" = proto.Field(
        proto.ENUM,
        number=10,
        enum="Environment",
    )
    url: str = proto.Field(
        proto.STRING,
        number=14,
    )
    kms_key_name: str = proto.Field(
        proto.STRING,
        number=25,
    )
    satisfies_pzs: bool = proto.Field(
        proto.BOOL,
        number=27,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=28,
        message=timestamp_pb2.Timestamp,
    )


class StateMessage(proto.Message):
    r"""Informational messages about the state of the Cloud Function
    or Operation.

    Attributes:
        severity (google.cloud.functions_v2.types.StateMessage.Severity):
            Severity of the state message.
        type_ (str):
            One-word CamelCase type of the state message.
        message (str):
            The message.
    """

    class Severity(proto.Enum):
        r"""Severity of the state message.

        Values:
            SEVERITY_UNSPECIFIED (0):
                Not specified. Invalid severity.
            ERROR (1):
                ERROR-level severity.
            WARNING (2):
                WARNING-level severity.
            INFO (3):
                INFO-level severity.
        """

        SEVERITY_UNSPECIFIED = 0
        ERROR = 1
        WARNING = 2
        INFO = 3

    severity: Severity = proto.Field(
        proto.ENUM,
        number=1,
        enum=Severity,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=2,
    )
    message: str = proto.Field(
        proto.STRING,
        number=3,
    )


class StorageSource(proto.Message):
    r"""Location of the source in an archive file in Google Cloud
    Storage.

    Attributes:
        bucket (str):
            Google Cloud Storage bucket containing the source (see
            `Bucket Name
            Requirements <https://cloud.google.com/storage/docs/bucket-naming#requirements>`__).
        object_ (str):
            Google Cloud Storage object containing the source.

            This object must be a gzipped archive file (``.tar.gz``)
            containing source to build.
        generation (int):
            Google Cloud Storage generation for the
            object. If the generation is omitted, the latest
            generation will be used.
        source_upload_url (str):
            When the specified storage bucket is a 1st
            gen function uploard url bucket, this field
            should be set as the generated upload url for
            1st gen deployment.
    """

    bucket: str = proto.Field(
        proto.STRING,
        number=1,
    )
    object_: str = proto.Field(
        proto.STRING,
        number=2,
    )
    generation: int = proto.Field(
        proto.INT64,
        number=3,
    )
    source_upload_url: str = proto.Field(
        proto.STRING,
        number=4,
    )


class RepoSource(proto.Message):
    r"""Location of the source in a Google Cloud Source Repository.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        branch_name (str):
            Regex matching branches to build.

            The syntax of the regular expressions accepted
            is the syntax accepted by RE2 and described at
            https://github.com/google/re2/wiki/Syntax

            This field is a member of `oneof`_ ``revision``.
        tag_name (str):
            Regex matching tags to build.

            The syntax of the regular expressions accepted
            is the syntax accepted by RE2 and described at
            https://github.com/google/re2/wiki/Syntax

            This field is a member of `oneof`_ ``revision``.
        commit_sha (str):
            Explicit commit SHA to build.

            This field is a member of `oneof`_ ``revision``.
        project_id (str):
            ID of the project that owns the Cloud Source
            Repository. If omitted, the project ID
            requesting the build is assumed.
        repo_name (str):
            Name of the Cloud Source Repository.
        dir_ (str):
            Directory, relative to the source root, in which to run the
            build.

            This must be a relative path. If a step's ``dir`` is
            specified and is an absolute path, this value is ignored for
            that step's execution. eg. helloworld (no leading slash
            allowed)
        invert_regex (bool):
            Only trigger a build if the revision regex
            does NOT match the revision regex.
    """

    branch_name: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="revision",
    )
    tag_name: str = proto.Field(
        proto.STRING,
        number=4,
        oneof="revision",
    )
    commit_sha: str = proto.Field(
        proto.STRING,
        number=5,
        oneof="revision",
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    repo_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    dir_: str = proto.Field(
        proto.STRING,
        number=6,
    )
    invert_regex: bool = proto.Field(
        proto.BOOL,
        number=7,
    )


class Source(proto.Message):
    r"""The location of the function source code.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        storage_source (google.cloud.functions_v2.types.StorageSource):
            If provided, get the source from this
            location in Google Cloud Storage.

            This field is a member of `oneof`_ ``source``.
        repo_source (google.cloud.functions_v2.types.RepoSource):
            If provided, get the source from this
            location in a Cloud Source Repository.

            This field is a member of `oneof`_ ``source``.
        git_uri (str):
            If provided, get the source from GitHub
            repository. This option is valid only for GCF
            1st Gen function. Example:
            https://github.com/<user>/<repo>/blob/<commit>/<path-to-code>

            This field is a member of `oneof`_ ``source``.
    """

    storage_source: "StorageSource" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="source",
        message="StorageSource",
    )
    repo_source: "RepoSource" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="source",
        message="RepoSource",
    )
    git_uri: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="source",
    )


class SourceProvenance(proto.Message):
    r"""Provenance of the source. Ways to find the original source,
    or verify that some source was used for this build.

    Attributes:
        resolved_storage_source (google.cloud.functions_v2.types.StorageSource):
            A copy of the build's ``source.storage_source``, if exists,
            with any generations resolved.
        resolved_repo_source (google.cloud.functions_v2.types.RepoSource):
            A copy of the build's ``source.repo_source``, if exists,
            with any revisions resolved.
        git_uri (str):
            A copy of the build's ``source.git_uri``, if exists, with
            any commits resolved.
    """

    resolved_storage_source: "StorageSource" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="StorageSource",
    )
    resolved_repo_source: "RepoSource" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="RepoSource",
    )
    git_uri: str = proto.Field(
        proto.STRING,
        number=3,
    )


class BuildConfig(proto.Message):
    r"""Describes the Build step of the function that builds a
    container from the given source.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        automatic_update_policy (google.cloud.functions_v2.types.AutomaticUpdatePolicy):

            This field is a member of `oneof`_ ``runtime_update_policy``.
        on_deploy_update_policy (google.cloud.functions_v2.types.OnDeployUpdatePolicy):

            This field is a member of `oneof`_ ``runtime_update_policy``.
        build (str):
            Output only. The Cloud Build name of the
            latest successful deployment of the function.
        runtime (str):
            The runtime in which to run the function. Required when
            deploying a new function, optional when updating an existing
            function. For a complete list of possible choices, see the
            ```gcloud`` command
            reference <https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime>`__.
        entry_point (str):
            The name of the function (as defined in source code) that
            will be executed. Defaults to the resource name suffix, if
            not specified. For backward compatibility, if function with
            given name is not found, then the system will try to use
            function named "function". For Node.js this is name of a
            function exported by the module specified in
            ``source_location``.
        source (google.cloud.functions_v2.types.Source):
            The location of the function source code.
        source_provenance (google.cloud.functions_v2.types.SourceProvenance):
            Output only. A permanent fixed identifier for
            source.
        worker_pool (str):
            Name of the Cloud Build Custom Worker Pool that should be
            used to build the function. The format of this field is
            ``projects/{project}/locations/{region}/workerPools/{workerPool}``
            where {project} and {region} are the project id and region
            respectively where the worker pool is defined and
            {workerPool} is the short name of the worker pool.

            If the project id is not the same as the function, then the
            Cloud Functions Service Agent
            (service-<project_number>@gcf-admin-robot.iam.gserviceaccount.com)
            must be granted the role Cloud Build Custom Workers Builder
            (roles/cloudbuild.customworkers.builder) in the project.
        environment_variables (MutableMapping[str, str]):
            User-provided build-time environment
            variables for the function
        docker_registry (google.cloud.functions_v2.types.BuildConfig.DockerRegistry):
            Docker Registry to use for this deployment. This
            configuration is only applicable to 1st Gen functions, 2nd
            Gen functions can only use Artifact Registry. Deprecated: As
            of March 2025, ``CONTAINER_REGISTRY`` option is no longer
            available in response to Container Registry's deprecation:
            https://cloud.google.com/artifact-registry/docs/transition/transition-from-gcr
            Please use Artifact Registry instead, which is the default
            choice.

            If unspecified, it defaults to ``ARTIFACT_REGISTRY``. If
            ``docker_repository`` field is specified, this field should
            either be left unspecified or set to ``ARTIFACT_REGISTRY``.
        docker_repository (str):
            Repository in Artifact Registry to which the function docker
            image will be pushed after it is built by Cloud Build. If
            specified by user, it is created and managed by user with a
            customer managed encryption key. Otherwise, GCF will create
            and use a repository named 'gcf-artifacts' for every
            deployed region.

            It must match the pattern
            ``projects/{project}/locations/{location}/repositories/{repository}``.
            Repository format must be 'DOCKER'.
        service_account (str):
            Service account to be used for building the container. The
            format of this field is
            ``projects/{projectId}/serviceAccounts/{serviceAccountEmail}``.
    """

    class DockerRegistry(proto.Enum):
        r"""Docker Registry to use for storing function Docker images.

        Values:
            DOCKER_REGISTRY_UNSPECIFIED (0):
                Unspecified.
            CONTAINER_REGISTRY (1):
                Docker images will be stored in multi-regional Container
                Registry repositories named ``gcf``.
            ARTIFACT_REGISTRY (2):
                Docker images will be stored in regional Artifact Registry
                repositories. By default, GCF will create and use
                repositories named ``gcf-artifacts`` in every region in
                which a function is deployed. But the repository to use can
                also be specified by the user using the
                ``docker_repository`` field.
        """

        DOCKER_REGISTRY_UNSPECIFIED = 0
        CONTAINER_REGISTRY = 1
        ARTIFACT_REGISTRY = 2

    automatic_update_policy: "AutomaticUpdatePolicy" = proto.Field(
        proto.MESSAGE,
        number=40,
        oneof="runtime_update_policy",
        message="AutomaticUpdatePolicy",
    )
    on_deploy_update_policy: "OnDeployUpdatePolicy" = proto.Field(
        proto.MESSAGE,
        number=41,
        oneof="runtime_update_policy",
        message="OnDeployUpdatePolicy",
    )
    build: str = proto.Field(
        proto.STRING,
        number=1,
    )
    runtime: str = proto.Field(
        proto.STRING,
        number=2,
    )
    entry_point: str = proto.Field(
        proto.STRING,
        number=3,
    )
    source: "Source" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="Source",
    )
    source_provenance: "SourceProvenance" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="SourceProvenance",
    )
    worker_pool: str = proto.Field(
        proto.STRING,
        number=5,
    )
    environment_variables: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    docker_registry: DockerRegistry = proto.Field(
        proto.ENUM,
        number=10,
        enum=DockerRegistry,
    )
    docker_repository: str = proto.Field(
        proto.STRING,
        number=7,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=27,
    )


class ServiceConfig(proto.Message):
    r"""Describes the Service being deployed.
    Currently Supported : Cloud Run (fully managed).

    Attributes:
        service (str):
            Output only. Name of the service associated with a Function.
            The format of this field is
            ``projects/{project}/locations/{region}/services/{service}``
        timeout_seconds (int):
            The function execution timeout. Execution is
            considered failed and can be terminated if the
            function is not completed at the end of the
            timeout period. Defaults to 60 seconds.
        available_memory (str):
            The amount of memory available for a
            function. Defaults to 256M. Supported units are
            k, M, G, Mi, Gi. If no unit is supplied the
            value is interpreted as bytes.
            See
            https://github.com/kubernetes/kubernetes/blob/master/staging/src/k8s.io/apimachinery/pkg/api/resource/quantity.go
            a full description.
        available_cpu (str):
            The number of CPUs used in a single container
            instance. Default value is calculated from
            available memory. Supports the same values as
            Cloud Run, see
            https://cloud.google.com/run/docs/reference/rest/v1/Container#resourcerequirements
            Example: "1" indicates 1 vCPU
        environment_variables (MutableMapping[str, str]):
            Environment variables that shall be available
            during function execution.
        max_instance_count (int):
            The limit on the maximum number of function instances that
            may coexist at a given time.

            In some cases, such as rapid traffic surges, Cloud Functions
            may, for a short period of time, create more instances than
            the specified max instances limit. If your function cannot
            tolerate this temporary behavior, you may want to factor in
            a safety margin and set a lower max instances value than
            your function can tolerate.

            See the `Max
            Instances <https://cloud.google.com/functions/docs/max-instances>`__
            Guide for more details.
        min_instance_count (int):
            The limit on the minimum number of function
            instances that may coexist at a given time.

            Function instances are kept in idle state for a
            short period after they finished executing the
            request to reduce cold start time for subsequent
            requests. Setting a minimum instance count will
            ensure that the given number of instances are
            kept running in idle state always. This can help
            with cold start times when jump in incoming
            request count occurs after the idle instance
            would have been stopped in the default case.
        vpc_connector (str):
            The Serverless VPC Access connector that this cloud function
            can connect to. The format of this field is
            ``projects/*/locations/*/connectors/*``.
        vpc_connector_egress_settings (google.cloud.functions_v2.types.ServiceConfig.VpcConnectorEgressSettings):
            The egress settings for the connector,
            controlling what traffic is diverted through it.
        ingress_settings (google.cloud.functions_v2.types.ServiceConfig.IngressSettings):
            The ingress settings for the function,
            controlling what traffic can reach it.
        uri (str):
            Output only. URI of the Service deployed.
        service_account_email (str):
            The email of the service's service account. If empty,
            defaults to
            ``{project_number}-compute@developer.gserviceaccount.com``.
        all_traffic_on_latest_revision (bool):
            Whether 100% of traffic is routed to the
            latest revision. On CreateFunction and
            UpdateFunction, when set to true, the revision
            being deployed will serve 100% of traffic,
            ignoring any traffic split settings, if any. On
            GetFunction, true will be returned if the latest
            revision is serving 100% of traffic.
        secret_environment_variables (MutableSequence[google.cloud.functions_v2.types.SecretEnvVar]):
            Secret environment variables configuration.
        secret_volumes (MutableSequence[google.cloud.functions_v2.types.SecretVolume]):
            Secret volumes configuration.
        revision (str):
            Output only. The name of service revision.
        max_instance_request_concurrency (int):
            Sets the maximum number of concurrent
            requests that each instance can receive.
            Defaults to 1.
        security_level (google.cloud.functions_v2.types.ServiceConfig.SecurityLevel):
            Security level configure whether the function
            only accepts https. This configuration is only
            applicable to 1st Gen functions with Http
            trigger. By default https is optional for 1st
            Gen functions; 2nd Gen functions are https ONLY.
        binary_authorization_policy (str):
            Optional. The binary authorization policy to
            be checked when deploying the Cloud Run service.
    """

    class VpcConnectorEgressSettings(proto.Enum):
        r"""Available egress settings.

        This controls what traffic is diverted through the VPC Access
        Connector resource. By default PRIVATE_RANGES_ONLY will be used.

        Values:
            VPC_CONNECTOR_EGRESS_SETTINGS_UNSPECIFIED (0):
                Unspecified.
            PRIVATE_RANGES_ONLY (1):
                Use the VPC Access Connector only for private
                IP space from RFC1918.
            ALL_TRAFFIC (2):
                Force the use of VPC Access Connector for all
                egress traffic from the function.
        """

        VPC_CONNECTOR_EGRESS_SETTINGS_UNSPECIFIED = 0
        PRIVATE_RANGES_ONLY = 1
        ALL_TRAFFIC = 2

    class IngressSettings(proto.Enum):
        r"""Available ingress settings.

        This controls what traffic can reach the function.

        If unspecified, ALLOW_ALL will be used.

        Values:
            INGRESS_SETTINGS_UNSPECIFIED (0):
                Unspecified.
            ALLOW_ALL (1):
                Allow HTTP traffic from public and private
                sources.
            ALLOW_INTERNAL_ONLY (2):
                Allow HTTP traffic from only private VPC
                sources.
            ALLOW_INTERNAL_AND_GCLB (3):
                Allow HTTP traffic from private VPC sources
                and through GCLB.
        """

        INGRESS_SETTINGS_UNSPECIFIED = 0
        ALLOW_ALL = 1
        ALLOW_INTERNAL_ONLY = 2
        ALLOW_INTERNAL_AND_GCLB = 3

    class SecurityLevel(proto.Enum):
        r"""Available security level settings.

        This enforces security protocol on function URL.

        Security level is only configurable for 1st Gen functions, If
        unspecified, SECURE_OPTIONAL will be used. 2nd Gen functions are
        SECURE_ALWAYS ONLY.

        Values:
            SECURITY_LEVEL_UNSPECIFIED (0):
                Unspecified.
            SECURE_ALWAYS (1):
                Requests for a URL that match this handler
                that do not use HTTPS are automatically
                redirected to the HTTPS URL with the same path.
                Query parameters are reserved for the redirect.
            SECURE_OPTIONAL (2):
                Both HTTP and HTTPS requests with URLs that
                match the handler succeed without redirects. The
                application can examine the request to determine
                which protocol was used and respond accordingly.
        """

        SECURITY_LEVEL_UNSPECIFIED = 0
        SECURE_ALWAYS = 1
        SECURE_OPTIONAL = 2

    service: str = proto.Field(
        proto.STRING,
        number=1,
    )
    timeout_seconds: int = proto.Field(
        proto.INT32,
        number=2,
    )
    available_memory: str = proto.Field(
        proto.STRING,
        number=13,
    )
    available_cpu: str = proto.Field(
        proto.STRING,
        number=22,
    )
    environment_variables: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    max_instance_count: int = proto.Field(
        proto.INT32,
        number=5,
    )
    min_instance_count: int = proto.Field(
        proto.INT32,
        number=12,
    )
    vpc_connector: str = proto.Field(
        proto.STRING,
        number=6,
    )
    vpc_connector_egress_settings: VpcConnectorEgressSettings = proto.Field(
        proto.ENUM,
        number=7,
        enum=VpcConnectorEgressSettings,
    )
    ingress_settings: IngressSettings = proto.Field(
        proto.ENUM,
        number=8,
        enum=IngressSettings,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=9,
    )
    service_account_email: str = proto.Field(
        proto.STRING,
        number=10,
    )
    all_traffic_on_latest_revision: bool = proto.Field(
        proto.BOOL,
        number=16,
    )
    secret_environment_variables: MutableSequence["SecretEnvVar"] = proto.RepeatedField(
        proto.MESSAGE,
        number=17,
        message="SecretEnvVar",
    )
    secret_volumes: MutableSequence["SecretVolume"] = proto.RepeatedField(
        proto.MESSAGE,
        number=19,
        message="SecretVolume",
    )
    revision: str = proto.Field(
        proto.STRING,
        number=18,
    )
    max_instance_request_concurrency: int = proto.Field(
        proto.INT32,
        number=20,
    )
    security_level: SecurityLevel = proto.Field(
        proto.ENUM,
        number=21,
        enum=SecurityLevel,
    )
    binary_authorization_policy: str = proto.Field(
        proto.STRING,
        number=23,
    )


class SecretEnvVar(proto.Message):
    r"""Configuration for a secret environment variable. It has the
    information necessary to fetch the secret value from secret
    manager and expose it as an environment variable.

    Attributes:
        key (str):
            Name of the environment variable.
        project_id (str):
            Project identifier (preferably project number
            but can also be the project ID) of the project
            that contains the secret. If not set, it is
            assumed that the secret is in the same project
            as the function.
        secret (str):
            Name of the secret in secret manager (not the
            full resource name).
        version (str):
            Version of the secret (version number or the
            string 'latest'). It is recommended to use a
            numeric version for secret environment variables
            as any updates to the secret value is not
            reflected until new instances start.
    """

    key: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    secret: str = proto.Field(
        proto.STRING,
        number=3,
    )
    version: str = proto.Field(
        proto.STRING,
        number=4,
    )


class SecretVolume(proto.Message):
    r"""Configuration for a secret volume. It has the information
    necessary to fetch the secret value from secret manager and make
    it available as files mounted at the requested paths within the
    application container.

    Attributes:
        mount_path (str):
            The path within the container to mount the secret volume.
            For example, setting the mount_path as ``/etc/secrets``
            would mount the secret value files under the
            ``/etc/secrets`` directory. This directory will also be
            completely shadowed and unavailable to mount any other
            secrets. Recommended mount path: /etc/secrets
        project_id (str):
            Project identifier (preferably project number
            but can also be the project ID) of the project
            that contains the secret. If not set, it is
            assumed that the secret is in the same project
            as the function.
        secret (str):
            Name of the secret in secret manager (not the
            full resource name).
        versions (MutableSequence[google.cloud.functions_v2.types.SecretVolume.SecretVersion]):
            List of secret versions to mount for this secret. If empty,
            the ``latest`` version of the secret will be made available
            in a file named after the secret under the mount point.
    """

    class SecretVersion(proto.Message):
        r"""Configuration for a single version.

        Attributes:
            version (str):
                Version of the secret (version number or the string
                'latest'). It is preferable to use ``latest`` version with
                secret volumes as secret value changes are reflected
                immediately.
            path (str):
                Relative path of the file under the mount path where the
                secret value for this version will be fetched and made
                available. For example, setting the mount_path as
                '/etc/secrets' and path as ``secret_foo`` would mount the
                secret value file at ``/etc/secrets/secret_foo``.
        """

        version: str = proto.Field(
            proto.STRING,
            number=1,
        )
        path: str = proto.Field(
            proto.STRING,
            number=2,
        )

    mount_path: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    secret: str = proto.Field(
        proto.STRING,
        number=3,
    )
    versions: MutableSequence[SecretVersion] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=SecretVersion,
    )


class EventTrigger(proto.Message):
    r"""Describes EventTrigger, used to request events to be sent
    from another service.

    Attributes:
        trigger (str):
            Output only. The resource name of the Eventarc trigger. The
            format of this field is
            ``projects/{project}/locations/{region}/triggers/{trigger}``.
        trigger_region (str):
            The region that the trigger will be in. The
            trigger will only receive events originating in
            this region. It can be the same region as the
            function, a different region or multi-region, or
            the global region. If not provided, defaults to
            the same region as the function.
        event_type (str):
            Required. The type of event to observe. For example:
            ``google.cloud.audit.log.v1.written`` or
            ``google.cloud.pubsub.topic.v1.messagePublished``.
        event_filters (MutableSequence[google.cloud.functions_v2.types.EventFilter]):
            Criteria used to filter events.
        pubsub_topic (str):
            Optional. The name of a Pub/Sub topic in the same project
            that will be used as the transport topic for the event
            delivery. Format: ``projects/{project}/topics/{topic}``.

            This is only valid for events of type
            ``google.cloud.pubsub.topic.v1.messagePublished``. The topic
            provided here will not be deleted at function deletion.
        service_account_email (str):
            Optional. The email of the trigger's service account. The
            service account must have permission to invoke Cloud Run
            services, the permission is ``run.routes.invoke``. If empty,
            defaults to the Compute Engine default service account:
            ``{project_number}-compute@developer.gserviceaccount.com``.
        retry_policy (google.cloud.functions_v2.types.EventTrigger.RetryPolicy):
            Optional. If unset, then defaults to ignoring
            failures (i.e. not retrying them).
        channel (str):
            Optional. The name of the channel associated with the
            trigger in
            ``projects/{project}/locations/{location}/channels/{channel}``
            format. You must provide a channel to receive events from
            Eventarc SaaS partners.
        service (str):
            Optional. The hostname of the service that 1st Gen function
            should be observed.

            If no string is provided, the default service implementing
            the API will be used. For example,
            ``storage.googleapis.com`` is the default for all event
            types in the ``google.storage`` namespace.

            The field is only applicable to 1st Gen functions.
    """

    class RetryPolicy(proto.Enum):
        r"""Describes the retry policy in case of function's execution
        failure. Retried execution is charged as any other execution.

        Values:
            RETRY_POLICY_UNSPECIFIED (0):
                Not specified.
            RETRY_POLICY_DO_NOT_RETRY (1):
                Do not retry.
            RETRY_POLICY_RETRY (2):
                Retry on any failure, retry up to 7 days with
                an exponential backoff (capped at 10 seconds).
        """

        RETRY_POLICY_UNSPECIFIED = 0
        RETRY_POLICY_DO_NOT_RETRY = 1
        RETRY_POLICY_RETRY = 2

    trigger: str = proto.Field(
        proto.STRING,
        number=1,
    )
    trigger_region: str = proto.Field(
        proto.STRING,
        number=2,
    )
    event_type: str = proto.Field(
        proto.STRING,
        number=3,
    )
    event_filters: MutableSequence["EventFilter"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="EventFilter",
    )
    pubsub_topic: str = proto.Field(
        proto.STRING,
        number=5,
    )
    service_account_email: str = proto.Field(
        proto.STRING,
        number=6,
    )
    retry_policy: RetryPolicy = proto.Field(
        proto.ENUM,
        number=7,
        enum=RetryPolicy,
    )
    channel: str = proto.Field(
        proto.STRING,
        number=8,
    )
    service: str = proto.Field(
        proto.STRING,
        number=9,
    )


class EventFilter(proto.Message):
    r"""Filters events based on exact matches on the CloudEvents
    attributes.

    Attributes:
        attribute (str):
            Required. The name of a CloudEvents
            attribute.
        value (str):
            Required. The value for the attribute.
        operator (str):
            Optional. The operator used for matching the events with the
            value of the filter. If not specified, only events that have
            an exact key-value pair specified in the filter are matched.
            The only allowed value is ``match-path-pattern``.
    """

    attribute: str = proto.Field(
        proto.STRING,
        number=1,
    )
    value: str = proto.Field(
        proto.STRING,
        number=2,
    )
    operator: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GetFunctionRequest(proto.Message):
    r"""Request for the ``GetFunction`` method.

    Attributes:
        name (str):
            Required. The name of the function which
            details should be obtained.
        revision (str):
            Optional. The optional version of the 1st gen
            function whose details should be obtained. The
            version of a 1st gen function is an integer that
            starts from 1 and gets incremented on
            redeployments. GCF may keep historical configs
            for old versions of 1st gen function. This field
            can be specified to fetch the historical
            configs. This field is valid only for GCF 1st
            gen function.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    revision: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListFunctionsRequest(proto.Message):
    r"""Request for the ``ListFunctions`` method.

    Attributes:
        parent (str):
            Required. The project and location from which the function
            should be listed, specified in the format
            ``projects/*/locations/*`` If you want to list functions in
            all locations, use "-" in place of a location. When listing
            functions in all locations, if one or more location(s) are
            unreachable, the response will contain functions from all
            reachable locations along with the names of any unreachable
            locations.
        page_size (int):
            Maximum number of functions to return per call. The largest
            allowed page_size is 1,000, if the page_size is omitted or
            specified as greater than 1,000 then it will be replaced as
            1,000. The size of the list response can be less than
            specified when used with filters.
        page_token (str):
            The value returned by the last ``ListFunctionsResponse``;
            indicates that this is a continuation of a prior
            ``ListFunctions`` call, and that the system should return
            the next page of data.
        filter (str):
            The filter for Functions that match the
            filter expression, following the syntax outlined
            in https://google.aip.dev/160.
        order_by (str):
            The sorting order of the resources returned.
            Value should be a comma separated list of
            fields. The default sorting order is ascending.
            See https://google.aip.dev/132#ordering.
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


class ListFunctionsResponse(proto.Message):
    r"""Response for the ``ListFunctions`` method.

    Attributes:
        functions (MutableSequence[google.cloud.functions_v2.types.Function]):
            The functions that match the request.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached. The
            response does not include any functions from
            these locations.
    """

    @property
    def raw_page(self):
        return self

    functions: MutableSequence["Function"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Function",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class CreateFunctionRequest(proto.Message):
    r"""Request for the ``CreateFunction`` method.

    Attributes:
        parent (str):
            Required. The project and location in which the function
            should be created, specified in the format
            ``projects/*/locations/*``
        function (google.cloud.functions_v2.types.Function):
            Required. Function to be created.
        function_id (str):
            The ID to use for the function, which will become the final
            component of the function's resource name.

            This value should be 4-63 characters, and valid characters
            are /[a-z][0-9]-/.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    function: "Function" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Function",
    )
    function_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class UpdateFunctionRequest(proto.Message):
    r"""Request for the ``UpdateFunction`` method.

    Attributes:
        function (google.cloud.functions_v2.types.Function):
            Required. New version of the function.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to be updated.
            If no field mask is provided, all fields will be
            updated.
    """

    function: "Function" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Function",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteFunctionRequest(proto.Message):
    r"""Request for the ``DeleteFunction`` method.

    Attributes:
        name (str):
            Required. The name of the function which
            should be deleted.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GenerateUploadUrlRequest(proto.Message):
    r"""Request of ``GenerateSourceUploadUrl`` method.

    Attributes:
        parent (str):
            Required. The project and location in which the Google Cloud
            Storage signed URL should be generated, specified in the
            format ``projects/*/locations/*``.
        kms_key_name (str):
            Resource name of a KMS crypto key (managed by the user) used
            to encrypt/decrypt function source code objects in
            intermediate Cloud Storage buckets. When you generate an
            upload url and upload your source code, it gets copied to an
            intermediate Cloud Storage bucket. The source code is then
            copied to a versioned directory in the sources bucket in the
            consumer project during the function deployment.

            It must match the pattern
            ``projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}``.

            The Google Cloud Functions service account
            (service-{project_number}@gcf-admin-robot.iam.gserviceaccount.com)
            must be granted the role 'Cloud KMS CryptoKey
            Encrypter/Decrypter
            (roles/cloudkms.cryptoKeyEncrypterDecrypter)' on the
            Key/KeyRing/Project/Organization (least access preferred).
        environment (google.cloud.functions_v2.types.Environment):
            The function environment the generated upload
            url will be used for. The upload url for 2nd Gen
            functions can also be used for 1st gen
            functions, but not vice versa. If not specified,
            2nd generation-style upload URLs are generated.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    kms_key_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    environment: "Environment" = proto.Field(
        proto.ENUM,
        number=3,
        enum="Environment",
    )


class GenerateUploadUrlResponse(proto.Message):
    r"""Response of ``GenerateSourceUploadUrl`` method.

    Attributes:
        upload_url (str):
            The generated Google Cloud Storage signed URL
            that should be used for a function source code
            upload. The uploaded file should be a zip
            archive which contains a function.
        storage_source (google.cloud.functions_v2.types.StorageSource):
            The location of the source code in the upload bucket.

            Once the archive is uploaded using the ``upload_url`` use
            this field to set the
            ``function.build_config.source.storage_source`` during
            CreateFunction and UpdateFunction.

            Generation defaults to 0, as Cloud Storage provides a new
            generation only upon uploading a new object or version of an
            object.
    """

    upload_url: str = proto.Field(
        proto.STRING,
        number=1,
    )
    storage_source: "StorageSource" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="StorageSource",
    )


class GenerateDownloadUrlRequest(proto.Message):
    r"""Request of ``GenerateDownloadUrl`` method.

    Attributes:
        name (str):
            Required. The name of function for which
            source code Google Cloud Storage signed URL
            should be generated.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GenerateDownloadUrlResponse(proto.Message):
    r"""Response of ``GenerateDownloadUrl`` method.

    Attributes:
        download_url (str):
            The generated Google Cloud Storage signed URL
            that should be used for function source code
            download.
    """

    download_url: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListRuntimesRequest(proto.Message):
    r"""Request for the ``ListRuntimes`` method.

    Attributes:
        parent (str):
            Required. The project and location from which the runtimes
            should be listed, specified in the format
            ``projects/*/locations/*``
        filter (str):
            The filter for Runtimes that match the filter
            expression, following the syntax outlined in
            https://google.aip.dev/160.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListRuntimesResponse(proto.Message):
    r"""Response for the ``ListRuntimes`` method.

    Attributes:
        runtimes (MutableSequence[google.cloud.functions_v2.types.ListRuntimesResponse.Runtime]):
            The runtimes that match the request.
    """

    class RuntimeStage(proto.Enum):
        r"""The various stages that a runtime can be in.

        Values:
            RUNTIME_STAGE_UNSPECIFIED (0):
                Not specified.
            DEVELOPMENT (1):
                The runtime is in development.
            ALPHA (2):
                The runtime is in the Alpha stage.
            BETA (3):
                The runtime is in the Beta stage.
            GA (4):
                The runtime is generally available.
            DEPRECATED (5):
                The runtime is deprecated.
            DECOMMISSIONED (6):
                The runtime is no longer supported.
        """

        RUNTIME_STAGE_UNSPECIFIED = 0
        DEVELOPMENT = 1
        ALPHA = 2
        BETA = 3
        GA = 4
        DEPRECATED = 5
        DECOMMISSIONED = 6

    class Runtime(proto.Message):
        r"""Describes a runtime and any special information (e.g.,
        deprecation status) related to it.

        Attributes:
            name (str):
                The name of the runtime, e.g., 'go113',
                'nodejs12', etc.
            display_name (str):
                The user facing name, eg 'Go 1.13', 'Node.js
                12', etc.
            stage (google.cloud.functions_v2.types.ListRuntimesResponse.RuntimeStage):
                The stage of life this runtime is in, e.g.,
                BETA, GA, etc.
            warnings (MutableSequence[str]):
                Warning messages, e.g., a deprecation
                warning.
            environment (google.cloud.functions_v2.types.Environment):
                The environment for the runtime.
            deprecation_date (google.type.date_pb2.Date):
                Deprecation date for the runtime.
            decommission_date (google.type.date_pb2.Date):
                Decommission date for the runtime.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        display_name: str = proto.Field(
            proto.STRING,
            number=5,
        )
        stage: "ListRuntimesResponse.RuntimeStage" = proto.Field(
            proto.ENUM,
            number=2,
            enum="ListRuntimesResponse.RuntimeStage",
        )
        warnings: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=3,
        )
        environment: "Environment" = proto.Field(
            proto.ENUM,
            number=4,
            enum="Environment",
        )
        deprecation_date: date_pb2.Date = proto.Field(
            proto.MESSAGE,
            number=6,
            message=date_pb2.Date,
        )
        decommission_date: date_pb2.Date = proto.Field(
            proto.MESSAGE,
            number=7,
            message=date_pb2.Date,
        )

    runtimes: MutableSequence[Runtime] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=Runtime,
    )


class AutomaticUpdatePolicy(proto.Message):
    r"""Security patches are applied automatically to the runtime
    without requiring the function to be redeployed.

    """


class OnDeployUpdatePolicy(proto.Message):
    r"""Security patches are only applied when a function is
    redeployed.

    Attributes:
        runtime_version (str):
            Output only. contains the runtime version
            which was used during latest function
            deployment.
    """

    runtime_version: str = proto.Field(
        proto.STRING,
        number=1,
    )


class OperationMetadata(proto.Message):
    r"""Represents the metadata of the long-running operation.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the operation was created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the operation finished running.
        target (str):
            Server-defined resource path for the target
            of the operation.
        verb (str):
            Name of the verb executed by the operation.
        status_detail (str):
            Human-readable status of the operation, if
            any.
        cancel_requested (bool):
            Identifies whether the user has requested cancellation of
            the operation. Operations that have successfully been
            cancelled have
            [google.longrunning.Operation.error][google.longrunning.Operation.error]
            value with a
            [google.rpc.Status.code][google.rpc.Status.code] of 1,
            corresponding to ``Code.CANCELLED``.
        api_version (str):
            API version used to start the operation.
        request_resource (google.protobuf.any_pb2.Any):
            The original request that started the
            operation.
        stages (MutableSequence[google.cloud.functions_v2.types.Stage]):
            Mechanism for reporting in-progress stages
        source_token (str):
            An identifier for Firebase function sources.
            Disclaimer: This field is only supported for
            Firebase function deployments.
        build_name (str):
            The build name of the function for create and
            update operations.
        operation_type (google.cloud.functions_v2.types.OperationType):
            The operation type.
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    target: str = proto.Field(
        proto.STRING,
        number=3,
    )
    verb: str = proto.Field(
        proto.STRING,
        number=4,
    )
    status_detail: str = proto.Field(
        proto.STRING,
        number=5,
    )
    cancel_requested: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    api_version: str = proto.Field(
        proto.STRING,
        number=7,
    )
    request_resource: any_pb2.Any = proto.Field(
        proto.MESSAGE,
        number=8,
        message=any_pb2.Any,
    )
    stages: MutableSequence["Stage"] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="Stage",
    )
    source_token: str = proto.Field(
        proto.STRING,
        number=10,
    )
    build_name: str = proto.Field(
        proto.STRING,
        number=13,
    )
    operation_type: "OperationType" = proto.Field(
        proto.ENUM,
        number=11,
        enum="OperationType",
    )


class LocationMetadata(proto.Message):
    r"""Extra GCF specific location information.

    Attributes:
        environments (MutableSequence[google.cloud.functions_v2.types.Environment]):
            The Cloud Function environments this location
            supports.
    """

    environments: MutableSequence["Environment"] = proto.RepeatedField(
        proto.ENUM,
        number=1,
        enum="Environment",
    )


class Stage(proto.Message):
    r"""Each Stage of the deployment process

    Attributes:
        name (google.cloud.functions_v2.types.Stage.Name):
            Name of the Stage. This will be unique for
            each Stage.
        message (str):
            Message describing the Stage
        state (google.cloud.functions_v2.types.Stage.State):
            Current state of the Stage
        resource (str):
            Resource of the Stage
        resource_uri (str):
            Link to the current Stage resource
        state_messages (MutableSequence[google.cloud.functions_v2.types.StateMessage]):
            State messages from the current Stage.
    """

    class Name(proto.Enum):
        r"""Possible names for a Stage

        Values:
            NAME_UNSPECIFIED (0):
                Not specified. Invalid name.
            ARTIFACT_REGISTRY (1):
                Artifact Registry Stage
            BUILD (2):
                Build Stage
            SERVICE (3):
                Service Stage
            TRIGGER (4):
                Trigger Stage
            SERVICE_ROLLBACK (5):
                Service Rollback Stage
            TRIGGER_ROLLBACK (6):
                Trigger Rollback Stage
        """

        NAME_UNSPECIFIED = 0
        ARTIFACT_REGISTRY = 1
        BUILD = 2
        SERVICE = 3
        TRIGGER = 4
        SERVICE_ROLLBACK = 5
        TRIGGER_ROLLBACK = 6

    class State(proto.Enum):
        r"""Possible states for a Stage

        Values:
            STATE_UNSPECIFIED (0):
                Not specified. Invalid state.
            NOT_STARTED (1):
                Stage has not started.
            IN_PROGRESS (2):
                Stage is in progress.
            COMPLETE (3):
                Stage has completed.
        """

        STATE_UNSPECIFIED = 0
        NOT_STARTED = 1
        IN_PROGRESS = 2
        COMPLETE = 3

    name: Name = proto.Field(
        proto.ENUM,
        number=1,
        enum=Name,
    )
    message: str = proto.Field(
        proto.STRING,
        number=2,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )
    resource: str = proto.Field(
        proto.STRING,
        number=4,
    )
    resource_uri: str = proto.Field(
        proto.STRING,
        number=5,
    )
    state_messages: MutableSequence["StateMessage"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="StateMessage",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
