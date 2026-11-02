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
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.orchestration.airflow.service.v1beta1",
    manifest={
        "CreateEnvironmentRequest",
        "GetEnvironmentRequest",
        "ListEnvironmentsRequest",
        "ListEnvironmentsResponse",
        "DeleteEnvironmentRequest",
        "UpdateEnvironmentRequest",
        "RestartWebServerRequest",
        "ExecuteAirflowCommandRequest",
        "ExecuteAirflowCommandResponse",
        "StopAirflowCommandRequest",
        "StopAirflowCommandResponse",
        "PollAirflowCommandRequest",
        "PollAirflowCommandResponse",
        "CreateUserWorkloadsSecretRequest",
        "GetUserWorkloadsSecretRequest",
        "ListUserWorkloadsSecretsRequest",
        "UpdateUserWorkloadsSecretRequest",
        "DeleteUserWorkloadsSecretRequest",
        "CreateUserWorkloadsConfigMapRequest",
        "GetUserWorkloadsConfigMapRequest",
        "ListUserWorkloadsConfigMapsRequest",
        "UpdateUserWorkloadsConfigMapRequest",
        "DeleteUserWorkloadsConfigMapRequest",
        "UserWorkloadsSecret",
        "ListUserWorkloadsSecretsResponse",
        "UserWorkloadsConfigMap",
        "ListUserWorkloadsConfigMapsResponse",
        "ListWorkloadsRequest",
        "ListWorkloadsResponse",
        "SaveSnapshotRequest",
        "SaveSnapshotResponse",
        "LoadSnapshotRequest",
        "LoadSnapshotResponse",
        "DatabaseFailoverRequest",
        "DatabaseFailoverResponse",
        "FetchDatabasePropertiesRequest",
        "FetchDatabasePropertiesResponse",
        "EnvironmentConfig",
        "WebServerNetworkAccessControl",
        "SoftwareConfig",
        "IPAllocationPolicy",
        "NodeConfig",
        "PrivateClusterConfig",
        "NetworkingConfig",
        "PrivateEnvironmentConfig",
        "DatabaseConfig",
        "WebServerConfig",
        "EncryptionConfig",
        "MaintenanceWindow",
        "WorkloadsConfig",
        "DataRetentionConfig",
        "TaskLogsRetentionConfig",
        "AirflowMetadataRetentionPolicyConfig",
        "StorageConfig",
        "RecoveryConfig",
        "ScheduledSnapshotsConfig",
        "MasterAuthorizedNetworksConfig",
        "CloudDataLineageIntegration",
        "Environment",
        "CheckUpgradeRequest",
        "CheckUpgradeResponse",
    },
)


class CreateEnvironmentRequest(proto.Message):
    r"""Create a new environment.

    Attributes:
        parent (str):
            The parent must be of the form
            "projects/{projectId}/locations/{locationId}".
        environment (google.cloud.orchestration.airflow.service_v1beta1.types.Environment):
            The environment to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    environment: "Environment" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Environment",
    )


class GetEnvironmentRequest(proto.Message):
    r"""Get an environment.

    Attributes:
        name (str):
            The resource name of the environment to get,
            in the form:
            "projects/{projectId}/locations/{locationId}/environments/{environmentId}".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListEnvironmentsRequest(proto.Message):
    r"""List environments in a project and location.

    Attributes:
        parent (str):
            List environments in the given project and
            location, in the form:
            "projects/{projectId}/locations/{locationId}".
        page_size (int):
            The maximum number of environments to return.
        page_token (str):
            The next_page_token value returned from a previous List
            request, if any.
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


class ListEnvironmentsResponse(proto.Message):
    r"""The environments in a project and location.

    Attributes:
        environments (MutableSequence[google.cloud.orchestration.airflow.service_v1beta1.types.Environment]):
            The list of environments returned by a
            ListEnvironmentsRequest.
        next_page_token (str):
            The page token used to query for the next
            page if one exists.
    """

    @property
    def raw_page(self):
        return self

    environments: MutableSequence["Environment"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Environment",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteEnvironmentRequest(proto.Message):
    r"""Delete an environment.

    Attributes:
        name (str):
            The environment to delete, in the form:

            "projects/{projectId}/locations/{locationId}/environments/{environmentId}".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateEnvironmentRequest(proto.Message):
    r"""Update an environment.

    Attributes:
        name (str):
            The relative resource name of the environment
            to update, in the form:
            "projects/{projectId}/locations/{locationId}/environments/{environmentId}".
        environment (google.cloud.orchestration.airflow.service_v1beta1.types.Environment):
            A patch environment. Fields specified by the ``updateMask``
            will be copied from the patch environment into the
            environment under update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. A comma-separated list of paths, relative to
            ``Environment``, of fields to update. For example, to set
            the version of scikit-learn to install in the environment to
            0.19.0 and to remove an existing installation of argparse,
            the ``updateMask`` parameter would include the following two
            ``paths`` values:
            "config.softwareConfig.pypiPackages.scikit-learn" and
            "config.softwareConfig.pypiPackages.argparse". The included
            patch environment would specify the scikit-learn version as
            follows:

            ::

                {
                  "config":{
                    "softwareConfig":{
                      "pypiPackages":{
                        "scikit-learn":"==0.19.0"
                      }
                    }
                  }
                }

            Note that in the above example, any existing PyPI packages
            other than scikit-learn and argparse will be unaffected.

            Only one update type may be included in a single request's
            ``updateMask``. For example, one cannot update both the PyPI
            packages and labels in the same request. However, it is
            possible to update multiple members of a map field
            simultaneously in the same request. For example, to set the
            labels "label1" and "label2" while clearing "label3"
            (assuming it already exists), one can provide the paths
            "labels.label1", "labels.label2", and "labels.label3" and
            populate the patch environment as follows:

            ::

                {
                  "labels":{
                    "label1":"new-label1-value"
                    "label2":"new-label2-value"
                  }
                }

            Note that in the above example, any existing labels that are
            not included in the ``updateMask`` will be unaffected.

            It is also possible to replace an entire map field by
            providing the map field's path in the ``updateMask``. The
            new value of the field will be that which is provided in the
            patch environment. For example, to delete all pre-existing
            user-specified PyPI packages and install botocore at version
            1.7.14, the ``updateMask`` would contain the path
            "config.softwareConfig.pypiPackages", and the patch
            environment would be the following:

            ::

                {
                  "config":{
                    "softwareConfig":{
                      "pypiPackages":{
                        "botocore":"==1.7.14"
                      }
                    }
                  }
                }

            **Note:** Only the following fields can be updated:

            - ``config.softwareConfig.pypiPackages``

              - Replace all custom custom PyPI packages. If a
                replacement package map is not included in
                ``environment``, all custom PyPI packages are cleared.
                It is an error to provide both this mask and a mask
                specifying an individual package.

            - ``config.softwareConfig.pypiPackages.``\ packagename

              - Update the custom PyPI package *packagename*, preserving
                other packages. To delete the package, include it in
                ``updateMask``, and omit the mapping for it in
                ``environment.config.softwareConfig.pypiPackages``. It
                is an error to provide both a mask of this form and the
                ``config.softwareConfig.pypiPackages`` mask.

            - ``labels``

              - Replace all environment labels. If a replacement labels
                map is not included in ``environment``, all labels are
                cleared. It is an error to provide both this mask and a
                mask specifying one or more individual labels.

            - ``labels.``\ labelName

              - Set the label named *labelName*, while preserving other
                labels. To delete the label, include it in
                ``updateMask`` and omit its mapping in
                ``environment.labels``. It is an error to provide both a
                mask of this form and the ``labels`` mask.

            - ``config.nodeCount``

              - Horizontally scale the number of nodes in the
                environment. An integer greater than or equal to 3 must
                be provided in the ``config.nodeCount`` field. Supported
                for Cloud Composer environments in versions
                composer-1.\ *.*-airflow-*.*.\*.

            - ``config.webServerNetworkAccessControl``

              - Replace the environment's current
                WebServerNetworkAccessControl.

            - ``config.softwareConfig.airflowConfigOverrides``

              - Replace all Apache Airflow config overrides. If a
                replacement config overrides map is not included in
                ``environment``, all config overrides are cleared. It is
                an error to provide both this mask and a mask specifying
                one or more individual config overrides.

            - ``config.softwareConfig.airflowConfigOverrides.``\ section-name

              - Override the Apache Airflow config property *name* in
                the section named *section*, preserving other
                properties. To delete the property override, include it
                in ``updateMask`` and omit its mapping in
                ``environment.config.softwareConfig.airflowConfigOverrides``.
                It is an error to provide both a mask of this form and
                the ``config.softwareConfig.airflowConfigOverrides``
                mask.

            - ``config.softwareConfig.envVariables``

              - Replace all environment variables. If a replacement
                environment variable map is not included in
                ``environment``, all custom environment variables are
                cleared.

            - ``config.softwareConfig.imageVersion``

              - Upgrade the version of the environment in-place. Refer
                to ``SoftwareConfig.image_version`` for information on
                how to format the new image version. Additionally, the
                new image version cannot effect a version downgrade, and
                must match the current image version's Composer and
                Airflow major versions. Consult the `Cloud Composer
                version
                list </composer/docs/concepts/versioning/composer-versions>`__
                for valid values.

            - ``config.softwareConfig.schedulerCount``

              - Horizontally scale the number of schedulers in Airflow.
                A positive integer not greater than the number of nodes
                must be provided in the
                ``config.softwareConfig.schedulerCount`` field.
                Supported for Cloud Composer environments in versions
                composer-1.\ *.*-airflow-2.\ *.*.

            - ``config.softwareConfig.cloudDataLineageIntegration``

              - Configuration for Cloud Data Lineage integration.

            - ``config.databaseConfig.machineType``

              - Cloud SQL machine type used by Airflow database. It has
                to be one of: db-n1-standard-2, db-n1-standard-4,
                db-n1-standard-8 or db-n1-standard-16. Supported for
                Cloud Composer environments in versions
                composer-1.\ *.*-airflow-*.*.\*.

            - ``config.webServerConfig.machineType``

              - Machine type on which Airflow web server is running. It
                has to be one of: composer-n1-webserver-2,
                composer-n1-webserver-4 or composer-n1-webserver-8.
                Supported for Cloud Composer environments in versions
                composer-1.\ *.*-airflow-*.*.\*.

            - ``config.maintenanceWindow``

              - Maintenance window during which Cloud Composer
                components may be under maintenance.

            - ``config.workloadsConfig``

              - The workloads configuration settings for the GKE cluster
                associated with the Cloud Composer environment.
                Supported for Cloud Composer environments in versions
                composer-2.\ *.*-airflow-*.*.\* and newer.

            - ``config.environmentSize``

              - The size of the Cloud Composer environment. Supported
                for Cloud Composer environments in versions
                composer-2.\ *.*-airflow-*.*.\* and newer.
    """

    name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    environment: "Environment" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Environment",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=3,
        message=field_mask_pb2.FieldMask,
    )


class RestartWebServerRequest(proto.Message):
    r"""Restart Airflow web server.

    Attributes:
        name (str):
            The resource name of the environment to
            restart the web server for, in the form:

            "projects/{projectId}/locations/{locationId}/environments/{environmentId}".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ExecuteAirflowCommandRequest(proto.Message):
    r"""Execute Airflow Command request.

    Attributes:
        environment (str):
            The resource name of the environment in the
            form:
            "projects/{projectId}/locations/{locationId}/environments/{environmentId}".
        command (str):
            Airflow command.
        subcommand (str):
            Airflow subcommand.
        parameters (MutableSequence[str]):
            Parameters for the Airflow command/subcommand as an array of
            arguments. It may contain positional arguments like
            ``["my-dag-id"]``, key-value parameters like
            ``["--foo=bar"]`` or ``["--foo","bar"]``, or other flags
            like ``["-f"]``.
    """

    environment: str = proto.Field(
        proto.STRING,
        number=1,
    )
    command: str = proto.Field(
        proto.STRING,
        number=2,
    )
    subcommand: str = proto.Field(
        proto.STRING,
        number=3,
    )
    parameters: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )


class ExecuteAirflowCommandResponse(proto.Message):
    r"""Response to ExecuteAirflowCommandRequest.

    Attributes:
        execution_id (str):
            The unique ID of the command execution for
            polling.
        pod (str):
            The name of the pod where the command is
            executed.
        pod_namespace (str):
            The namespace of the pod where the command is
            executed.
        error (str):
            Error message. Empty if there was no error.
    """

    execution_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    pod: str = proto.Field(
        proto.STRING,
        number=2,
    )
    pod_namespace: str = proto.Field(
        proto.STRING,
        number=3,
    )
    error: str = proto.Field(
        proto.STRING,
        number=4,
    )


class StopAirflowCommandRequest(proto.Message):
    r"""Stop Airflow Command request.

    Attributes:
        environment (str):
            The resource name of the environment in the
            form:
            "projects/{projectId}/locations/{locationId}/environments/{environmentId}".
        execution_id (str):
            The unique ID of the command execution.
        pod (str):
            The name of the pod where the command is
            executed.
        pod_namespace (str):
            The namespace of the pod where the command is
            executed.
        force (bool):
            If true, the execution is terminated
            forcefully (SIGKILL). If false, the execution is
            stopped gracefully, giving it time for cleanup.
    """

    environment: str = proto.Field(
        proto.STRING,
        number=1,
    )
    execution_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    pod: str = proto.Field(
        proto.STRING,
        number=3,
    )
    pod_namespace: str = proto.Field(
        proto.STRING,
        number=4,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class StopAirflowCommandResponse(proto.Message):
    r"""Response to StopAirflowCommandRequest.

    Attributes:
        is_done (bool):
            Whether the execution is still running.
        output (MutableSequence[str]):
            Output message from stopping execution
            request.
    """

    is_done: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    output: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class PollAirflowCommandRequest(proto.Message):
    r"""Poll Airflow Command request.

    Attributes:
        environment (str):
            The resource name of the environment in the
            form:
            "projects/{projectId}/locations/{locationId}/environments/{environmentId}".
        execution_id (str):
            The unique ID of the command execution.
        pod (str):
            The name of the pod where the command is
            executed.
        pod_namespace (str):
            The namespace of the pod where the command is
            executed.
        next_line_number (int):
            Line number from which new logs should be
            fetched.
    """

    environment: str = proto.Field(
        proto.STRING,
        number=1,
    )
    execution_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    pod: str = proto.Field(
        proto.STRING,
        number=3,
    )
    pod_namespace: str = proto.Field(
        proto.STRING,
        number=4,
    )
    next_line_number: int = proto.Field(
        proto.INT32,
        number=5,
    )


class PollAirflowCommandResponse(proto.Message):
    r"""Response to PollAirflowCommandRequest.

    Attributes:
        output (MutableSequence[google.cloud.orchestration.airflow.service_v1beta1.types.PollAirflowCommandResponse.Line]):
            Output from the command execution. It may not
            contain the full output and the caller may need
            to poll for more lines.
        output_end (bool):
            Whether the command execution has finished
            and there is no more output.
        exit_info (google.cloud.orchestration.airflow.service_v1beta1.types.PollAirflowCommandResponse.ExitInfo):
            The result exit status of the command.
    """

    class Line(proto.Message):
        r"""Contains information about a single line from logs.

        Attributes:
            line_number (int):
                Number of the line.
            content (str):
                Text content of the log line.
        """

        line_number: int = proto.Field(
            proto.INT32,
            number=1,
        )
        content: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class ExitInfo(proto.Message):
        r"""Information about how a command ended.

        Attributes:
            exit_code (int):
                The exit code from the command execution.
            error (str):
                Error message. Empty if there was no error.
        """

        exit_code: int = proto.Field(
            proto.INT32,
            number=1,
        )
        error: str = proto.Field(
            proto.STRING,
            number=2,
        )

    output: MutableSequence[Line] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=Line,
    )
    output_end: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    exit_info: ExitInfo = proto.Field(
        proto.MESSAGE,
        number=3,
        message=ExitInfo,
    )


class CreateUserWorkloadsSecretRequest(proto.Message):
    r"""Create user workloads Secret request.

    Attributes:
        parent (str):
            Required. The environment name to create a
            Secret for, in the form:
            "projects/{projectId}/locations/{locationId}/environments/{environmentId}".
        user_workloads_secret (google.cloud.orchestration.airflow.service_v1beta1.types.UserWorkloadsSecret):
            Required. User workloads Secret to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    user_workloads_secret: "UserWorkloadsSecret" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="UserWorkloadsSecret",
    )


class GetUserWorkloadsSecretRequest(proto.Message):
    r"""Get user workloads Secret request.

    Attributes:
        name (str):
            Required. The resource name of the Secret to
            get, in the form:
            "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsSecrets/{userWorkloadsSecretId}".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListUserWorkloadsSecretsRequest(proto.Message):
    r"""List user workloads Secrets request.

    Attributes:
        parent (str):
            Required. List Secrets in the given
            environment, in the form:
            "projects/{projectId}/locations/{locationId}/environments/{environmentId}".
        page_size (int):
            Optional. The maximum number of Secrets to
            return.
        page_token (str):
            Optional. The next_page_token value returned from a previous
            List request, if any.
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


class UpdateUserWorkloadsSecretRequest(proto.Message):
    r"""Update user workloads Secret request.

    Attributes:
        user_workloads_secret (google.cloud.orchestration.airflow.service_v1beta1.types.UserWorkloadsSecret):
            Optional. User workloads Secret to override.
    """

    user_workloads_secret: "UserWorkloadsSecret" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="UserWorkloadsSecret",
    )


class DeleteUserWorkloadsSecretRequest(proto.Message):
    r"""Delete user workloads Secret request.

    Attributes:
        name (str):
            Required. The Secret to delete, in the form:
            "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsSecrets/{userWorkloadsSecretId}".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateUserWorkloadsConfigMapRequest(proto.Message):
    r"""Create user workloads ConfigMap request.

    Attributes:
        parent (str):
            Required. The environment name to create a
            ConfigMap for, in the form:
            "projects/{projectId}/locations/{locationId}/environments/{environmentId}".
        user_workloads_config_map (google.cloud.orchestration.airflow.service_v1beta1.types.UserWorkloadsConfigMap):
            Required. User workloads ConfigMap to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    user_workloads_config_map: "UserWorkloadsConfigMap" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="UserWorkloadsConfigMap",
    )


class GetUserWorkloadsConfigMapRequest(proto.Message):
    r"""Get user workloads ConfigMap request.

    Attributes:
        name (str):
            Required. The resource name of the ConfigMap
            to get, in the form:
            "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsConfigMaps/{userWorkloadsConfigMapId}".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListUserWorkloadsConfigMapsRequest(proto.Message):
    r"""List user workloads ConfigMaps request.

    Attributes:
        parent (str):
            Required. List ConfigMaps in the given
            environment, in the form:
            "projects/{projectId}/locations/{locationId}/environments/{environmentId}".
        page_size (int):
            Optional. The maximum number of ConfigMaps to
            return.
        page_token (str):
            Optional. The next_page_token value returned from a previous
            List request, if any.
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


class UpdateUserWorkloadsConfigMapRequest(proto.Message):
    r"""Update user workloads ConfigMap request.

    Attributes:
        user_workloads_config_map (google.cloud.orchestration.airflow.service_v1beta1.types.UserWorkloadsConfigMap):
            Optional. User workloads ConfigMap to
            override.
    """

    user_workloads_config_map: "UserWorkloadsConfigMap" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="UserWorkloadsConfigMap",
    )


class DeleteUserWorkloadsConfigMapRequest(proto.Message):
    r"""Delete user workloads ConfigMap request.

    Attributes:
        name (str):
            Required. The ConfigMap to delete, in the
            form:
            "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsConfigMaps/{userWorkloadsConfigMapId}".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UserWorkloadsSecret(proto.Message):
    r"""User workloads Secret used by Airflow tasks that run with
    Kubernetes executor or KubernetesPodOperator.

    Attributes:
        name (str):
            Identifier. The resource name of the Secret,
            in the form:
            "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsSecrets/{userWorkloadsSecretId}".
        data (MutableMapping[str, str]):
            Optional. The "data" field of Kubernetes
            Secret, organized in key-value pairs, which can
            contain sensitive values such as a password, a
            token, or a key. The values for all keys have to
            be base64-encoded strings. For details see:
            https://kubernetes.io/docs/concepts/configuration/secret/

            Example:

            {
              "example": "ZXhhbXBsZV92YWx1ZQ==",
              "another-example":
            "YW5vdGhlcl9leGFtcGxlX3ZhbHVl" }
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )


class ListUserWorkloadsSecretsResponse(proto.Message):
    r"""The user workloads Secrets for a given environment.

    Attributes:
        user_workloads_secrets (MutableSequence[google.cloud.orchestration.airflow.service_v1beta1.types.UserWorkloadsSecret]):
            The list of Secrets returned by a
            ListUserWorkloadsSecretsRequest.
        next_page_token (str):
            The page token used to query for the next
            page if one exists.
    """

    @property
    def raw_page(self):
        return self

    user_workloads_secrets: MutableSequence["UserWorkloadsSecret"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="UserWorkloadsSecret",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UserWorkloadsConfigMap(proto.Message):
    r"""User workloads ConfigMap used by Airflow tasks that run with
    Kubernetes executor or KubernetesPodOperator.

    Attributes:
        name (str):
            Identifier. The resource name of the
            ConfigMap, in the form:
            "projects/{projectId}/locations/{locationId}/environments/{environmentId}/userWorkloadsConfigMaps/{userWorkloadsConfigMapId}".
        data (MutableMapping[str, str]):
            Optional. The "data" field of Kubernetes ConfigMap,
            organized in key-value pairs. For details see:
            https://kubernetes.io/docs/concepts/configuration/configmap/

            Example:

            { "example_key": "example_value", "another_key":
            "another_value" }
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )


class ListUserWorkloadsConfigMapsResponse(proto.Message):
    r"""The user workloads ConfigMaps for a given environment.

    Attributes:
        user_workloads_config_maps (MutableSequence[google.cloud.orchestration.airflow.service_v1beta1.types.UserWorkloadsConfigMap]):
            The list of ConfigMaps returned by a
            ListUserWorkloadsConfigMapsRequest.
        next_page_token (str):
            The page token used to query for the next
            page if one exists.
    """

    @property
    def raw_page(self):
        return self

    user_workloads_config_maps: MutableSequence["UserWorkloadsConfigMap"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="UserWorkloadsConfigMap",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListWorkloadsRequest(proto.Message):
    r"""Request for listing workloads in a Cloud Composer
    environment.

    Attributes:
        parent (str):
            Required. The environment name to get
            workloads for, in the form:
            "projects/{projectId}/locations/{locationId}/environments/{environmentId}".
        page_size (int):
            Optional. The maximum number of environments
            to return.
        page_token (str):
            Optional. The next_page_token value returned from a previous
            List request, if any.
        filter (str):
            Optional. The list filter. Currently only supports equality
            on the type field. The value of a field specified in the
            filter expression must be one ComposerWorkloadType enum
            option. It's possible to get multiple types using "OR"
            operator, e.g.: "type=SCHEDULER OR type=CELERY_WORKER". If
            not specified, all items are returned.
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


class ListWorkloadsResponse(proto.Message):
    r"""Response to ListWorkloadsRequest.

    Attributes:
        workloads (MutableSequence[google.cloud.orchestration.airflow.service_v1beta1.types.ListWorkloadsResponse.ComposerWorkload]):
            The list of environment workloads.
        next_page_token (str):
            The page token used to query for the next
            page if one exists.
    """

    class ComposerWorkloadType(proto.Enum):
        r"""Supported workload types.

        Values:
            COMPOSER_WORKLOAD_TYPE_UNSPECIFIED (0):
                Not able to determine the type of the
                workload.
            CELERY_WORKER (1):
                Celery worker.
            KUBERNETES_WORKER (2):
                Kubernetes worker.
            KUBERNETES_OPERATOR_POD (3):
                Workload created by Kubernetes Pod Operator.
            SCHEDULER (4):
                Airflow scheduler.
            DAG_PROCESSOR (5):
                Airflow Dag processor.
            TRIGGERER (6):
                Airflow triggerer.
            WEB_SERVER (7):
                Airflow web server UI.
            REDIS (8):
                Redis.
        """

        COMPOSER_WORKLOAD_TYPE_UNSPECIFIED = 0
        CELERY_WORKER = 1
        KUBERNETES_WORKER = 2
        KUBERNETES_OPERATOR_POD = 3
        SCHEDULER = 4
        DAG_PROCESSOR = 5
        TRIGGERER = 6
        WEB_SERVER = 7
        REDIS = 8

    class ComposerWorkloadState(proto.Enum):
        r"""Workload states.

        Values:
            COMPOSER_WORKLOAD_STATE_UNSPECIFIED (0):
                Not able to determine the status of the
                workload.
            PENDING (1):
                Workload is in pending state and has not yet
                started.
            OK (2):
                Workload is running fine.
            WARNING (3):
                Workload is running but there are some
                non-critical problems.
            ERROR (4):
                Workload is not running due to an error.
            SUCCEEDED (5):
                Workload has finished execution with success.
            FAILED (6):
                Workload has finished execution with failure.
        """

        COMPOSER_WORKLOAD_STATE_UNSPECIFIED = 0
        PENDING = 1
        OK = 2
        WARNING = 3
        ERROR = 4
        SUCCEEDED = 5
        FAILED = 6

    class ComposerWorkload(proto.Message):
        r"""Information about a single workload.

        Attributes:
            name (str):
                Name of a workload.
            type_ (google.cloud.orchestration.airflow.service_v1beta1.types.ListWorkloadsResponse.ComposerWorkloadType):
                Type of a workload.
            status (google.cloud.orchestration.airflow.service_v1beta1.types.ListWorkloadsResponse.ComposerWorkloadStatus):
                Output only. Status of a workload.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        type_: "ListWorkloadsResponse.ComposerWorkloadType" = proto.Field(
            proto.ENUM,
            number=2,
            enum="ListWorkloadsResponse.ComposerWorkloadType",
        )
        status: "ListWorkloadsResponse.ComposerWorkloadStatus" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="ListWorkloadsResponse.ComposerWorkloadStatus",
        )

    class ComposerWorkloadStatus(proto.Message):
        r"""Workload status.

        Attributes:
            state (google.cloud.orchestration.airflow.service_v1beta1.types.ListWorkloadsResponse.ComposerWorkloadState):
                Output only. Workload state.
            status_message (str):
                Output only. Text to provide more descriptive
                status.
            detailed_status_message (str):
                Output only. Detailed message of the status.
        """

        state: "ListWorkloadsResponse.ComposerWorkloadState" = proto.Field(
            proto.ENUM,
            number=1,
            enum="ListWorkloadsResponse.ComposerWorkloadState",
        )
        status_message: str = proto.Field(
            proto.STRING,
            number=2,
        )
        detailed_status_message: str = proto.Field(
            proto.STRING,
            number=3,
        )

    @property
    def raw_page(self):
        return self

    workloads: MutableSequence[ComposerWorkload] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=ComposerWorkload,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SaveSnapshotRequest(proto.Message):
    r"""Request to create a snapshot of a Cloud Composer environment.

    Attributes:
        environment (str):
            The resource name of the source environment
            in the form:
            "projects/{projectId}/locations/{locationId}/environments/{environmentId}".
        snapshot_location (str):
            Location in a Cloud Storage where the
            snapshot is going to be stored, e.g.:
            "gs://my-bucket/snapshots".
    """

    environment: str = proto.Field(
        proto.STRING,
        number=1,
    )
    snapshot_location: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SaveSnapshotResponse(proto.Message):
    r"""Response to SaveSnapshotRequest.

    Attributes:
        snapshot_path (str):
            The fully-resolved Cloud Storage path of the created
            snapshot, e.g.:
            "gs://my-bucket/snapshots/project_location_environment_timestamp".
            This field is populated only if the snapshot creation was
            successful.
    """

    snapshot_path: str = proto.Field(
        proto.STRING,
        number=1,
    )


class LoadSnapshotRequest(proto.Message):
    r"""Request to load a snapshot into a Cloud Composer environment.

    Attributes:
        environment (str):
            The resource name of the target environment
            in the form:
            "projects/{projectId}/locations/{locationId}/environments/{environmentId}".
        snapshot_path (str):
            A Cloud Storage path to a snapshot to load, e.g.:
            "gs://my-bucket/snapshots/project_location_environment_timestamp".
        skip_pypi_packages_installation (bool):
            Whether or not to skip installing Pypi
            packages when loading the environment's state.
        skip_environment_variables_setting (bool):
            Whether or not to skip setting environment
            variables when loading the environment's state.
        skip_airflow_overrides_setting (bool):
            Whether or not to skip setting Airflow
            overrides when loading the environment's state.
        skip_gcs_data_copying (bool):
            Whether or not to skip copying Cloud Storage
            data when loading the environment's state.
    """

    environment: str = proto.Field(
        proto.STRING,
        number=1,
    )
    snapshot_path: str = proto.Field(
        proto.STRING,
        number=2,
    )
    skip_pypi_packages_installation: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    skip_environment_variables_setting: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    skip_airflow_overrides_setting: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    skip_gcs_data_copying: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


class LoadSnapshotResponse(proto.Message):
    r"""Response to LoadSnapshotRequest."""


class DatabaseFailoverRequest(proto.Message):
    r"""Request to trigger database failover (only for highly
    resilient environments).

    Attributes:
        environment (str):
            Target environment:

            "projects/{projectId}/locations/{locationId}/environments/{environmentId}".
    """

    environment: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DatabaseFailoverResponse(proto.Message):
    r"""Response for DatabaseFailoverRequest."""


class FetchDatabasePropertiesRequest(proto.Message):
    r"""Request to fetch properties of environment's database.

    Attributes:
        environment (str):
            Required. The resource name of the
            environment, in the form:
            "projects/{projectId}/locations/{locationId}/environments/{environmentId}".
    """

    environment: str = proto.Field(
        proto.STRING,
        number=1,
    )


class FetchDatabasePropertiesResponse(proto.Message):
    r"""Response for FetchDatabasePropertiesRequest.

    Attributes:
        primary_gce_zone (str):
            The Compute Engine zone that the instance is
            currently serving from.
        secondary_gce_zone (str):
            The Compute Engine zone that the failover
            instance is currently serving from for a
            regional Cloud SQL instance.
        is_failover_replica_available (bool):
            The availability status of the failover
            replica. A false status indicates that the
            failover replica is out of sync. The primary
            instance can only fail over to the failover
            replica when the status is true.
    """

    primary_gce_zone: str = proto.Field(
        proto.STRING,
        number=1,
    )
    secondary_gce_zone: str = proto.Field(
        proto.STRING,
        number=2,
    )
    is_failover_replica_available: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class EnvironmentConfig(proto.Message):
    r"""Configuration information for an environment.

    Attributes:
        gke_cluster (str):
            Output only. The Kubernetes Engine cluster
            used to run this environment.
        dag_gcs_prefix (str):
            Output only. The Cloud Storage prefix of the
            DAGs for this environment. Although Cloud
            Storage objects reside in a flat namespace, a
            hierarchical file tree can be simulated using
            "/"-delimited object name prefixes. DAG objects
            for this environment reside in a simulated
            directory with the given prefix.
        node_count (int):
            The number of nodes in the Kubernetes Engine cluster that
            will be used to run this environment.

            This field is supported for Cloud Composer environments in
            versions composer-1.\ *.*-airflow-*.*.\*.
        software_config (google.cloud.orchestration.airflow.service_v1beta1.types.SoftwareConfig):
            Optional. The configuration settings for
            software inside the environment.
        node_config (google.cloud.orchestration.airflow.service_v1beta1.types.NodeConfig):
            Optional. The configuration used for the
            Kubernetes Engine cluster.
        private_environment_config (google.cloud.orchestration.airflow.service_v1beta1.types.PrivateEnvironmentConfig):
            Optional. The configuration used for the
            Private IP Cloud Composer environment.
        web_server_network_access_control (google.cloud.orchestration.airflow.service_v1beta1.types.WebServerNetworkAccessControl):
            Optional. The network-level access control
            policy for the Airflow web server. If
            unspecified, no network-level access
            restrictions will be applied.
        database_config (google.cloud.orchestration.airflow.service_v1beta1.types.DatabaseConfig):
            Optional. The configuration settings for
            Cloud SQL instance used internally by Apache
            Airflow software.
        web_server_config (google.cloud.orchestration.airflow.service_v1beta1.types.WebServerConfig):
            Optional. The configuration settings for the Airflow web
            server App Engine instance.

            This field is supported for Cloud Composer environments in
            versions composer-1.\ *.*-airflow-*.*.\*.
        airflow_uri (str):
            Output only. The URI of the Apache Airflow Web UI hosted
            within this environment (see `Airflow web
            interface </composer/docs/how-to/accessing/airflow-web-interface>`__).
        airflow_byoid_uri (str):
            Output only. The 'bring your own identity' variant of the
            URI of the Apache Airflow Web UI hosted within this
            environment, to be accessed with external identities using
            workforce identity federation (see `Access environments with
            workforce identity
            federation </composer/docs/composer-2/access-environments-with-workforce-identity-federation>`__).
        encryption_config (google.cloud.orchestration.airflow.service_v1beta1.types.EncryptionConfig):
            Optional. The encryption options for the
            Cloud Composer environment and its dependencies.
            Cannot be updated.
        maintenance_window (google.cloud.orchestration.airflow.service_v1beta1.types.MaintenanceWindow):
            Optional. The maintenance window is the
            period when Cloud Composer components may
            undergo maintenance. It is defined so that
            maintenance is not executed during peak hours or
            critical time periods.

            The system will not be under maintenance for
            every occurrence of this window, but when
            maintenance is planned, it will be scheduled
            during the window.

            The maintenance window period must encompass at
            least 12 hours per week. This may be split into
            multiple chunks, each with a size of at least 4
            hours.

            If this value is omitted, the default value for
            maintenance window is applied. By default,
            maintenance windows are from 00:00:00 to
            04:00:00 (GMT) on Friday, Saturday, and Sunday
            every week.
        workloads_config (google.cloud.orchestration.airflow.service_v1beta1.types.WorkloadsConfig):
            Optional. The workloads configuration settings for the GKE
            cluster associated with the Cloud Composer environment. The
            GKE cluster runs Airflow scheduler, web server and workers
            workloads.

            This field is supported for Cloud Composer environments in
            versions composer-2.\ *.*-airflow-*.*.\* and newer.
        environment_size (google.cloud.orchestration.airflow.service_v1beta1.types.EnvironmentConfig.EnvironmentSize):
            Optional. The size of the Cloud Composer environment.

            This field is supported for Cloud Composer environments in
            versions composer-2.\ *.*-airflow-*.*.\* and newer.
        master_authorized_networks_config (google.cloud.orchestration.airflow.service_v1beta1.types.MasterAuthorizedNetworksConfig):
            Optional. The configuration options for GKE
            cluster master authorized networks. By default
            master authorized networks feature is:

            - in case of private environment: enabled with
              no external networks allowlisted.
            - in case of public environment: disabled.
        recovery_config (google.cloud.orchestration.airflow.service_v1beta1.types.RecoveryConfig):
            Optional. The Recovery settings configuration of an
            environment.

            This field is supported for Cloud Composer environments in
            versions composer-2.\ *.*-airflow-*.*.\* and newer.
        data_retention_config (google.cloud.orchestration.airflow.service_v1beta1.types.DataRetentionConfig):
            Optional. The configuration setting for
            Airflow database data retention mechanism.
        resilience_mode (google.cloud.orchestration.airflow.service_v1beta1.types.EnvironmentConfig.ResilienceMode):
            Optional. Resilience mode of the Cloud Composer Environment.

            This field is supported for Cloud Composer environments in
            versions composer-2.2.0-airflow-*.*.\* and newer.
    """

    class EnvironmentSize(proto.Enum):
        r"""The size of the Cloud Composer environment.

        Values:
            ENVIRONMENT_SIZE_UNSPECIFIED (0):
                The size of the environment is unspecified.
            ENVIRONMENT_SIZE_SMALL (1):
                The environment size is small.
            ENVIRONMENT_SIZE_MEDIUM (2):
                The environment size is medium.
            ENVIRONMENT_SIZE_LARGE (3):
                The environment size is large.
        """

        ENVIRONMENT_SIZE_UNSPECIFIED = 0
        ENVIRONMENT_SIZE_SMALL = 1
        ENVIRONMENT_SIZE_MEDIUM = 2
        ENVIRONMENT_SIZE_LARGE = 3

    class ResilienceMode(proto.Enum):
        r"""Resilience mode of the Cloud Composer Environment.

        Values:
            RESILIENCE_MODE_UNSPECIFIED (0):
                Default mode doesn't change environment
                parameters.
            HIGH_RESILIENCE (1):
                Enabled High Resilience mode, including Cloud
                SQL HA.
        """

        RESILIENCE_MODE_UNSPECIFIED = 0
        HIGH_RESILIENCE = 1

    gke_cluster: str = proto.Field(
        proto.STRING,
        number=1,
    )
    dag_gcs_prefix: str = proto.Field(
        proto.STRING,
        number=2,
    )
    node_count: int = proto.Field(
        proto.INT32,
        number=3,
    )
    software_config: "SoftwareConfig" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="SoftwareConfig",
    )
    node_config: "NodeConfig" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="NodeConfig",
    )
    private_environment_config: "PrivateEnvironmentConfig" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="PrivateEnvironmentConfig",
    )
    web_server_network_access_control: "WebServerNetworkAccessControl" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="WebServerNetworkAccessControl",
    )
    database_config: "DatabaseConfig" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="DatabaseConfig",
    )
    web_server_config: "WebServerConfig" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="WebServerConfig",
    )
    airflow_uri: str = proto.Field(
        proto.STRING,
        number=6,
    )
    airflow_byoid_uri: str = proto.Field(
        proto.STRING,
        number=21,
    )
    encryption_config: "EncryptionConfig" = proto.Field(
        proto.MESSAGE,
        number=12,
        message="EncryptionConfig",
    )
    maintenance_window: "MaintenanceWindow" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="MaintenanceWindow",
    )
    workloads_config: "WorkloadsConfig" = proto.Field(
        proto.MESSAGE,
        number=15,
        message="WorkloadsConfig",
    )
    environment_size: EnvironmentSize = proto.Field(
        proto.ENUM,
        number=16,
        enum=EnvironmentSize,
    )
    master_authorized_networks_config: "MasterAuthorizedNetworksConfig" = proto.Field(
        proto.MESSAGE,
        number=17,
        message="MasterAuthorizedNetworksConfig",
    )
    recovery_config: "RecoveryConfig" = proto.Field(
        proto.MESSAGE,
        number=18,
        message="RecoveryConfig",
    )
    data_retention_config: "DataRetentionConfig" = proto.Field(
        proto.MESSAGE,
        number=19,
        message="DataRetentionConfig",
    )
    resilience_mode: ResilienceMode = proto.Field(
        proto.ENUM,
        number=20,
        enum=ResilienceMode,
    )


class WebServerNetworkAccessControl(proto.Message):
    r"""Network-level access control policy for the Airflow web
    server.

    Attributes:
        allowed_ip_ranges (MutableSequence[google.cloud.orchestration.airflow.service_v1beta1.types.WebServerNetworkAccessControl.AllowedIpRange]):
            A collection of allowed IP ranges with
            descriptions.
    """

    class AllowedIpRange(proto.Message):
        r"""Allowed IP range with user-provided description.

        Attributes:
            value (str):
                IP address or range, defined using CIDR notation, of
                requests that this rule applies to. Examples:
                ``192.168.1.1`` or ``192.168.0.0/16`` or ``2001:db8::/32``
                or ``2001:0db8:0000:0042:0000:8a2e:0370:7334``.

                IP range prefixes should be properly truncated. For example,
                ``1.2.3.4/24`` should be truncated to ``1.2.3.0/24``.
                Similarly, for IPv6, ``2001:db8::1/32`` should be truncated
                to ``2001:db8::/32``.
            description (str):
                Optional. User-provided description. It must
                contain at most 300 characters.
        """

        value: str = proto.Field(
            proto.STRING,
            number=1,
        )
        description: str = proto.Field(
            proto.STRING,
            number=2,
        )

    allowed_ip_ranges: MutableSequence[AllowedIpRange] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=AllowedIpRange,
    )


class SoftwareConfig(proto.Message):
    r"""Specifies the selection and configuration of software inside
    the environment.

    Attributes:
        image_version (str):
            Optional. The version of the software running in the
            environment. This encapsulates both the version of Cloud
            Composer functionality and the version of Apache Airflow. It
            must match the regular expression
            ``composer-([0-9]+(\.[0-9]+\.[0-9]+(-preview\.[0-9]+)?)?|latest)-airflow-([0-9]+(\.[0-9]+(\.[0-9]+)?)?)``.
            When used as input, the server also checks if the provided
            version is supported and denies the request for an
            unsupported version.

            The Cloud Composer portion of the image version is a full
            `semantic version <https://semver.org>`__, or an alias in
            the form of major version number or ``latest``. When an
            alias is provided, the server replaces it with the current
            Cloud Composer version that satisfies the alias.

            The Apache Airflow portion of the image version is a full
            semantic version that points to one of the supported Apache
            Airflow versions, or an alias in the form of only major or
            major.minor versions specified. When an alias is provided,
            the server replaces it with the latest Apache Airflow
            version that satisfies the alias and is supported in the
            given Cloud Composer version.

            In all cases, the resolved image version is stored in the
            same field.

            See also `version
            list </composer/docs/concepts/versioning/composer-versions>`__
            and `versioning
            overview </composer/docs/concepts/versioning/composer-versioning-overview>`__.
        airflow_config_overrides (MutableMapping[str, str]):
            Optional. Apache Airflow configuration properties to
            override.

            Property keys contain the section and property names,
            separated by a hyphen, for example
            "core-dags_are_paused_at_creation". Section names must not
            contain hyphens ("-"), opening square brackets ("["), or
            closing square brackets ("]"). The property name must not be
            empty and must not contain an equals sign ("=") or semicolon
            (";"). Section and property names must not contain a period
            ("."). Apache Airflow configuration property names must be
            written in
            `snake_case <https://en.wikipedia.org/wiki/Snake_case>`__.
            Property values can contain any character, and can be
            written in any lower/upper case format.

            Certain Apache Airflow configuration property values are
            `blocked </composer/docs/concepts/airflow-configurations>`__,
            and cannot be overridden.
        pypi_packages (MutableMapping[str, str]):
            Optional. Custom Python Package Index (PyPI) packages to be
            installed in the environment.

            Keys refer to the lowercase package name such as "numpy" and
            values are the lowercase extras and version specifier such
            as "==1.12.0", "[devel,gcp_api]", or "[devel]>=1.8.2,
            <1.9.2". To specify a package without pinning it to a
            version specifier, use the empty string as the value.
        env_variables (MutableMapping[str, str]):
            Optional. Additional environment variables to provide to the
            Apache Airflow scheduler, worker, and webserver processes.

            Environment variable names must match the regular expression
            ``[a-zA-Z_][a-zA-Z0-9_]*``. They cannot specify Apache
            Airflow software configuration overrides (they cannot match
            the regular expression ``AIRFLOW__[A-Z0-9_]+__[A-Z0-9_]+``),
            and they cannot match any of the following reserved names:

            - ``AIRFLOW_HOME``
            - ``C_FORCE_ROOT``
            - ``CONTAINER_NAME``
            - ``DAGS_FOLDER``
            - ``GCP_PROJECT``
            - ``GCS_BUCKET``
            - ``GKE_CLUSTER_NAME``
            - ``SQL_DATABASE``
            - ``SQL_INSTANCE``
            - ``SQL_PASSWORD``
            - ``SQL_PROJECT``
            - ``SQL_REGION``
            - ``SQL_USER``
        python_version (str):
            Optional. The major version of Python used to run the Apache
            Airflow scheduler, worker, and webserver processes.

            Can be set to '2' or '3'. If not specified, the default is
            '3'. Cannot be updated.

            This field is only supported for Cloud Composer environments
            in versions composer-1.\ *.*-airflow-*.*.\*. Environments in
            newer versions always use Python major version 3.
        scheduler_count (int):
            Optional. The number of schedulers for Airflow.

            This field is supported for Cloud Composer environments in
            versions composer-1.\ *.*-airflow-2.\ *.*.
        cloud_data_lineage_integration (google.cloud.orchestration.airflow.service_v1beta1.types.CloudDataLineageIntegration):
            Optional. The configuration for Cloud Data
            Lineage integration.
        web_server_plugins_mode (google.cloud.orchestration.airflow.service_v1beta1.types.SoftwareConfig.WebServerPluginsMode):
            Optional. Whether or not the web server uses custom plugins.
            If unspecified, the field defaults to ``PLUGINS_ENABLED``.

            This field is supported for Cloud Composer environments in
            versions composer-3-airflow-*.*.\ *-build.* and newer.
    """

    class WebServerPluginsMode(proto.Enum):
        r"""Web server plugins mode of the Cloud Composer environment.

        Values:
            WEB_SERVER_PLUGINS_MODE_UNSPECIFIED (0):
                Default mode.
            PLUGINS_DISABLED (1):
                Web server plugins are not supported.
            PLUGINS_ENABLED (2):
                Web server plugins are supported.
        """

        WEB_SERVER_PLUGINS_MODE_UNSPECIFIED = 0
        PLUGINS_DISABLED = 1
        PLUGINS_ENABLED = 2

    image_version: str = proto.Field(
        proto.STRING,
        number=1,
    )
    airflow_config_overrides: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )
    pypi_packages: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )
    env_variables: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    python_version: str = proto.Field(
        proto.STRING,
        number=6,
    )
    scheduler_count: int = proto.Field(
        proto.INT32,
        number=7,
    )
    cloud_data_lineage_integration: "CloudDataLineageIntegration" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="CloudDataLineageIntegration",
    )
    web_server_plugins_mode: WebServerPluginsMode = proto.Field(
        proto.ENUM,
        number=10,
        enum=WebServerPluginsMode,
    )


class IPAllocationPolicy(proto.Message):
    r"""Configuration for controlling how IPs are allocated in the
    GKE cluster.

    Attributes:
        use_ip_aliases (bool):
            Optional. Whether or not to enable Alias IPs in the GKE
            cluster. If ``true``, a VPC-native cluster is created.

            This field is only supported for Cloud Composer environments
            in versions composer-1.\ *.*-airflow-*.*.\*. Environments in
            newer versions always use VPC-native GKE clusters.
        cluster_secondary_range_name (str):
            Optional. The name of the cluster's secondary range used to
            allocate IP addresses to pods. Specify either
            ``cluster_secondary_range_name`` or
            ``cluster_ipv4_cidr_block`` but not both.

            For Cloud Composer environments in versions
            composer-1.\ *.*-airflow-*.*.\*, this field is applicable
            only when ``use_ip_aliases`` is true.
        services_secondary_range_name (str):
            Optional. The name of the services' secondary range used to
            allocate IP addresses to the cluster. Specify either
            ``services_secondary_range_name`` or
            ``services_ipv4_cidr_block`` but not both.

            For Cloud Composer environments in versions
            composer-1.\ *.*-airflow-*.*.\*, this field is applicable
            only when ``use_ip_aliases`` is true.
        cluster_ipv4_cidr_block (str):
            Optional. The IP address range used to allocate IP addresses
            to pods in the cluster.

            For Cloud Composer environments in versions
            composer-1.\ *.*-airflow-*.*.\*, this field is applicable
            only when ``use_ip_aliases`` is true.

            Set to blank to have GKE choose a range with the default
            size.

            Set to /netmask (e.g. ``/14``) to have GKE choose a range
            with a specific netmask.

            Set to a
            `CIDR <https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing>`__
            notation (e.g. ``10.96.0.0/14``) from the RFC-1918 private
            networks (e.g. ``10.0.0.0/8``, ``172.16.0.0/12``,
            ``192.168.0.0/16``) to pick a specific range to use. Specify
            ``cluster_secondary_range_name`` or
            ``cluster_ipv4_cidr_block`` but not both.
        services_ipv4_cidr_block (str):
            Optional. The IP address range of the services IP addresses
            in this cluster.

            For Cloud Composer environments in versions
            composer-1.\ *.*-airflow-*.*.\*, this field is applicable
            only when ``use_ip_aliases`` is true.

            Set to blank to have GKE choose a range with the default
            size.

            Set to /netmask (e.g. ``/14``) to have GKE choose a range
            with a specific netmask.

            Set to a
            `CIDR <https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing>`__
            notation (e.g. ``10.96.0.0/14``) from the RFC-1918 private
            networks (e.g. ``10.0.0.0/8``, ``172.16.0.0/12``,
            ``192.168.0.0/16``) to pick a specific range to use. Specify
            ``services_secondary_range_name`` or
            ``services_ipv4_cidr_block`` but not both.
    """

    use_ip_aliases: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    cluster_secondary_range_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    services_secondary_range_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    cluster_ipv4_cidr_block: str = proto.Field(
        proto.STRING,
        number=4,
    )
    services_ipv4_cidr_block: str = proto.Field(
        proto.STRING,
        number=5,
    )


class NodeConfig(proto.Message):
    r"""The configuration information for the Kubernetes Engine nodes
    running the Apache Airflow software.

    Attributes:
        location (str):
            Optional. The Compute Engine
            `zone </compute/docs/regions-zones>`__ in which to deploy
            the VMs used to run the Apache Airflow software, specified
            as a `relative resource
            name </apis/design/resource_names#relative_resource_name>`__.
            For example: "projects/{projectId}/zones/{zoneId}".

            This ``location`` must belong to the enclosing environment's
            project and location. If both this field and
            ``nodeConfig.machineType`` are specified,
            ``nodeConfig.machineType`` must belong to this ``location``;
            if both are unspecified, the service will pick a zone in the
            Compute Engine region corresponding to the Cloud Composer
            location, and propagate that choice to both fields. If only
            one field (``location`` or ``nodeConfig.machineType``) is
            specified, the location information from the specified field
            will be propagated to the unspecified field.

            This field is supported for Cloud Composer environments in
            versions composer-1.\ *.*-airflow-*.*.\*.
        machine_type (str):
            Optional. The Compute Engine `machine
            type </compute/docs/machine-types>`__ used for cluster
            instances, specified as a `relative resource
            name </apis/design/resource_names#relative_resource_name>`__.
            For example:
            "projects/{projectId}/zones/{zoneId}/machineTypes/{machineTypeId}".

            The ``machineType`` must belong to the enclosing
            environment's project and location. If both this field and
            ``nodeConfig.location`` are specified, this ``machineType``
            must belong to the ``nodeConfig.location``; if both are
            unspecified, the service will pick a zone in the Compute
            Engine region corresponding to the Cloud Composer location,
            and propagate that choice to both fields. If exactly one of
            this field and ``nodeConfig.location`` is specified, the
            location information from the specified field will be
            propagated to the unspecified field.

            The ``machineTypeId`` must not be a `shared-core machine
            type </compute/docs/machine-types#sharedcore>`__.

            If this field is unspecified, the ``machineTypeId`` defaults
            to "n1-standard-1".

            This field is supported for Cloud Composer environments in
            versions composer-1.\ *.*-airflow-*.*.\*.
        network (str):
            Optional. The Compute Engine network to be used for machine
            communications, specified as a `relative resource
            name </apis/design/resource_names#relative_resource_name>`__.
            For example:
            "projects/{projectId}/global/networks/{networkId}".

            If unspecified, the default network in the environment's
            project is used. If a `Custom Subnet
            Network </vpc/docs/vpc#vpc_networks_and_subnets>`__ is
            provided, ``nodeConfig.subnetwork`` must also be provided.
            For `Shared VPC </vpc/docs/shared-vpc>`__ subnetwork
            requirements, see ``nodeConfig.subnetwork``.
        subnetwork (str):
            Optional. The Compute Engine subnetwork to be used for
            machine communications, specified as a `relative resource
            name </apis/design/resource_names#relative_resource_name>`__.
            For example:
            "projects/{projectId}/regions/{regionId}/subnetworks/{subnetworkId}"

            If a subnetwork is provided, ``nodeConfig.network`` must
            also be provided, and the subnetwork must belong to the
            enclosing environment's project and location.
        disk_size_gb (int):
            Optional. The disk size in GB used for node VMs. Minimum
            size is 30GB. If unspecified, defaults to 100GB. Cannot be
            updated.

            This field is supported for Cloud Composer environments in
            versions composer-1.\ *.*-airflow-*.*.\*.
        oauth_scopes (MutableSequence[str]):
            Optional. The set of Google API scopes to be made available
            on all node VMs. If ``oauth_scopes`` is empty, defaults to
            ["https://www.googleapis.com/auth/cloud-platform"]. Cannot
            be updated.

            This field is supported for Cloud Composer environments in
            versions composer-1.\ *.*-airflow-*.*.\*.
        service_account (str):
            Optional. The Google Cloud Platform Service
            Account to be used by the workloads. If a
            service account is not specified, the "default"
            Compute Engine service account is used. Cannot
            be updated.
        tags (MutableSequence[str]):
            Optional. The list of instance tags applied to all node VMs.
            Tags are used to identify valid sources or targets for
            network firewalls. Each tag within the list must comply with
            `RFC1035 <https://www.ietf.org/rfc/rfc1035.txt>`__. Cannot
            be updated.
        ip_allocation_policy (google.cloud.orchestration.airflow.service_v1beta1.types.IPAllocationPolicy):
            Optional. The IPAllocationPolicy fields for
            the GKE cluster.
        max_pods_per_node (int):
            Optional. The maximum number of pods per node in the Cloud
            Composer GKE cluster. The value must be between 8 and 110
            and it can be set only if the environment is VPC-native. The
            default value is 32. Values of this field will be propagated
            both to the ``default-pool`` node pool of the newly created
            GKE cluster, and to the default "Maximum Pods per Node"
            value which is used for newly created node pools if their
            value is not explicitly set during node pool creation. For
            more information, see [Optimizing IP address allocation]
            (https://cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr).
            Cannot be updated.

            This field is supported for Cloud Composer environments in
            versions composer-1.\ *.*-airflow-*.*.\*.
        enable_ip_masq_agent (bool):
            Optional. Deploys 'ip-masq-agent' daemon set
            in the GKE cluster and defines
            nonMasqueradeCIDRs equals to pod IP range so IP
            masquerading is used for all destination
            addresses, except between pods traffic.

            See:

            https://cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent
        composer_network_attachment (str):
            Optional. Network Attachment that Cloud Composer environment
            is connected to, which provides connectivity with a user's
            VPC network. Takes precedence over network and subnetwork
            settings. If not provided, but network and subnetwork are
            defined during environment, it will be provisioned. If not
            provided and network and subnetwork are also empty, then
            connectivity to user's VPC network is disabled. Network
            attachment must be provided in format
            projects/{project}/regions/{region}/networkAttachments/{networkAttachment}.

            This field is supported for Cloud Composer environments in
            versions composer-3-airflow-*.*.\ *-build.* and newer.
        composer_internal_ipv4_cidr_block (str):
            Optional. The IP range in CIDR notation to use internally by
            Cloud Composer. IP addresses are not reserved - and the same
            range can be used by multiple Cloud Composer environments.
            In case of overlap, IPs from this range will not be
            accessible in the user's VPC network. Cannot be updated. If
            not specified, the default value of '100.64.128.0/20' is
            used.

            This field is supported for Cloud Composer environments in
            versions composer-3-airflow-*.*.\ *-build.* and newer.
    """

    location: str = proto.Field(
        proto.STRING,
        number=1,
    )
    machine_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    network: str = proto.Field(
        proto.STRING,
        number=3,
    )
    subnetwork: str = proto.Field(
        proto.STRING,
        number=4,
    )
    disk_size_gb: int = proto.Field(
        proto.INT32,
        number=5,
    )
    oauth_scopes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=7,
    )
    tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    ip_allocation_policy: "IPAllocationPolicy" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="IPAllocationPolicy",
    )
    max_pods_per_node: int = proto.Field(
        proto.INT32,
        number=10,
    )
    enable_ip_masq_agent: bool = proto.Field(
        proto.BOOL,
        number=11,
    )
    composer_network_attachment: str = proto.Field(
        proto.STRING,
        number=12,
    )
    composer_internal_ipv4_cidr_block: str = proto.Field(
        proto.STRING,
        number=13,
    )


class PrivateClusterConfig(proto.Message):
    r"""Configuration options for the private GKE cluster in a Cloud
    Composer environment.

    Attributes:
        enable_private_endpoint (bool):
            Optional. If ``true``, access to the public endpoint of the
            GKE cluster is denied.
        master_ipv4_cidr_block (str):
            Optional. The CIDR block from which IPv4
            range for GKE master will be reserved. If left
            blank, the default value of '172.16.0.0/23' is
            used.
        master_ipv4_reserved_range (str):
            Output only. The IP range in CIDR notation to
            use for the hosted master network. This range is
            used for assigning internal IP addresses to the
            cluster master or set of masters and to the
            internal load balancer virtual IP. This range
            must not overlap with any other ranges in use
            within the cluster's network.
    """

    enable_private_endpoint: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    master_ipv4_cidr_block: str = proto.Field(
        proto.STRING,
        number=2,
    )
    master_ipv4_reserved_range: str = proto.Field(
        proto.STRING,
        number=3,
    )


class NetworkingConfig(proto.Message):
    r"""Configuration options for networking connections in the
    Composer 2 environment.

    Attributes:
        connection_type (google.cloud.orchestration.airflow.service_v1beta1.types.NetworkingConfig.ConnectionType):
            Optional. Indicates the user requested
            specific connection type between Tenant and
            Customer projects. You cannot set networking
            connection type in public IP environment.
    """

    class ConnectionType(proto.Enum):
        r"""Represents connection type between Composer environment in
        Customer Project and the corresponding Tenant project, from a
        predefined list of available connection modes.

        Values:
            CONNECTION_TYPE_UNSPECIFIED (0):
                No specific connection type was requested, so
                the environment uses the default value
                corresponding to the rest of its configuration.
            VPC_PEERING (1):
                Requests the use of VPC peerings for
                connecting the Customer and Tenant projects.
            PRIVATE_SERVICE_CONNECT (2):
                Requests the use of Private Service Connect
                for connecting the Customer and Tenant projects.
        """

        CONNECTION_TYPE_UNSPECIFIED = 0
        VPC_PEERING = 1
        PRIVATE_SERVICE_CONNECT = 2

    connection_type: ConnectionType = proto.Field(
        proto.ENUM,
        number=1,
        enum=ConnectionType,
    )


class PrivateEnvironmentConfig(proto.Message):
    r"""The configuration information for configuring a Private IP
    Cloud Composer environment.

    Attributes:
        enable_private_environment (bool):
            Optional. If ``true``, a Private IP Cloud Composer
            environment is created. If this field is set to true,
            ``IPAllocationPolicy.use_ip_aliases`` must be set to true
            for Cloud Composer environments in versions
            composer-1.\ *.*-airflow-*.*.\*.
        enable_private_builds_only (bool):
            Optional. If ``true``, builds performed during operations
            that install Python packages have only private connectivity
            to Google services (including Artifact Registry) and VPC
            network (if either ``NodeConfig.network`` and
            ``NodeConfig.subnetwork`` fields or
            ``NodeConfig.composer_network_attachment`` field are
            specified). If ``false``, the builds also have access to the
            internet.

            This field is supported for Cloud Composer environments in
            versions composer-3-airflow-*.*.\ *-build.* and newer.
        private_cluster_config (google.cloud.orchestration.airflow.service_v1beta1.types.PrivateClusterConfig):
            Optional. Configuration for the private GKE
            cluster for a Private IP Cloud Composer
            environment.
        web_server_ipv4_cidr_block (str):
            Optional. The CIDR block from which IP range for web server
            will be reserved. Needs to be disjoint from
            private_cluster_config.master_ipv4_cidr_block and
            cloud_sql_ipv4_cidr_block.

            This field is supported for Cloud Composer environments in
            versions composer-1.\ *.*-airflow-*.*.\*.
        cloud_sql_ipv4_cidr_block (str):
            Optional. The CIDR block from which IP range in tenant
            project will be reserved for Cloud SQL. Needs to be disjoint
            from web_server_ipv4_cidr_block
        web_server_ipv4_reserved_range (str):
            Output only. The IP range reserved for the tenant project's
            App Engine VMs.

            This field is supported for Cloud Composer environments in
            versions composer-1.\ *.*-airflow-*.*.\*.
        cloud_composer_network_ipv4_cidr_block (str):
            Optional. The CIDR block from which IP range for Cloud
            Composer Network in tenant project will be reserved. Needs
            to be disjoint from
            private_cluster_config.master_ipv4_cidr_block and
            cloud_sql_ipv4_cidr_block.

            This field is supported for Cloud Composer environments in
            versions composer-2.\ *.*-airflow-*.*.\* and newer.
        cloud_composer_network_ipv4_reserved_range (str):
            Output only. The IP range reserved for the tenant project's
            Cloud Composer network.

            This field is supported for Cloud Composer environments in
            versions composer-2.\ *.*-airflow-*.*.\* and newer.
        enable_privately_used_public_ips (bool):
            Optional. When enabled, IPs from public (non-RFC1918) ranges
            can be used for
            ``IPAllocationPolicy.cluster_ipv4_cidr_block`` and
            ``IPAllocationPolicy.service_ipv4_cidr_block``.
        cloud_composer_connection_subnetwork (str):
            Optional. When specified, the environment
            will use Private Service Connect instead of VPC
            peerings to connect to Cloud SQL in the Tenant
            Project, and the PSC endpoint in the Customer
            Project will use an IP address from this
            subnetwork.
        networking_config (google.cloud.orchestration.airflow.service_v1beta1.types.NetworkingConfig):
            Optional. Configuration for the network
            connections configuration in the environment.
    """

    enable_private_environment: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    enable_private_builds_only: bool = proto.Field(
        proto.BOOL,
        number=11,
    )
    private_cluster_config: "PrivateClusterConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="PrivateClusterConfig",
    )
    web_server_ipv4_cidr_block: str = proto.Field(
        proto.STRING,
        number=3,
    )
    cloud_sql_ipv4_cidr_block: str = proto.Field(
        proto.STRING,
        number=4,
    )
    web_server_ipv4_reserved_range: str = proto.Field(
        proto.STRING,
        number=5,
    )
    cloud_composer_network_ipv4_cidr_block: str = proto.Field(
        proto.STRING,
        number=7,
    )
    cloud_composer_network_ipv4_reserved_range: str = proto.Field(
        proto.STRING,
        number=8,
    )
    enable_privately_used_public_ips: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    cloud_composer_connection_subnetwork: str = proto.Field(
        proto.STRING,
        number=9,
    )
    networking_config: "NetworkingConfig" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="NetworkingConfig",
    )


class DatabaseConfig(proto.Message):
    r"""The configuration of Cloud SQL instance that is used by the
    Apache Airflow software.

    Attributes:
        machine_type (str):
            Optional. Cloud SQL machine type used by Airflow database.
            It has to be one of: db-n1-standard-2, db-n1-standard-4,
            db-n1-standard-8 or db-n1-standard-16. If not specified,
            db-n1-standard-2 will be used. Supported for Cloud Composer
            environments in versions composer-1.\ *.*-airflow-*.*.\*.
        zone (str):
            Optional. The Compute Engine zone where the Airflow database
            is created. If zone is provided, it must be in the region
            selected for the environment. If zone is not provided, a
            zone is automatically selected. The zone can only be set
            during environment creation. Supported for Cloud Composer
            environments in versions composer-2.\ *.*-airflow-*.*.\*.
    """

    machine_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    zone: str = proto.Field(
        proto.STRING,
        number=2,
    )


class WebServerConfig(proto.Message):
    r"""The configuration settings for the Airflow web server App Engine
    instance. Supported for Cloud Composer environments in versions
    composer-1.\ *.*-airflow-*.*.\*.

    Attributes:
        machine_type (str):
            Optional. Machine type on which Airflow web
            server is running. It has to be one of:
            composer-n1-webserver-2, composer-n1-webserver-4
            or composer-n1-webserver-8.
            If not specified, composer-n1-webserver-2 will
            be used. Value custom is returned only in
            response, if Airflow web server parameters were
            manually changed to a non-standard values.
    """

    machine_type: str = proto.Field(
        proto.STRING,
        number=1,
    )


class EncryptionConfig(proto.Message):
    r"""The encryption options for the Cloud Composer environment and its
    dependencies. Supported for Cloud Composer environments in versions
    composer-1.\ *.*-airflow-*.*.\*.

    Attributes:
        kms_key_name (str):
            Optional. Customer-managed Encryption Key
            available through Google's Key Management
            Service. Cannot be updated. If not specified,
            Google-managed key will be used.
    """

    kms_key_name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class MaintenanceWindow(proto.Message):
    r"""The configuration settings for Cloud Composer maintenance window.
    The following example:

    ::

          {
            "startTime":"2019-08-01T01:00:00Z"
            "endTime":"2019-08-01T07:00:00Z"
            "recurrence":"FREQ=WEEKLY;BYDAY=TU,WE"
          }

    would define a maintenance window between 01 and 07 hours UTC during
    each Tuesday and Wednesday.

    Attributes:
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Required. Start time of the first recurrence
            of the maintenance window.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Required. Maintenance window end time. It is used only to
            calculate the duration of the maintenance window. The value
            for end_time must be in the future, relative to
            ``start_time``.
        recurrence (str):
            Required. Maintenance window recurrence. Format is a subset
            of `RFC-5545 <https://tools.ietf.org/html/rfc5545>`__
            ``RRULE``. The only allowed values for ``FREQ`` field are
            ``FREQ=DAILY`` and ``FREQ=WEEKLY;BYDAY=...`` Example values:
            ``FREQ=WEEKLY;BYDAY=TU,WE``, ``FREQ=DAILY``.
    """

    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    recurrence: str = proto.Field(
        proto.STRING,
        number=3,
    )


class WorkloadsConfig(proto.Message):
    r"""The Kubernetes workloads configuration for GKE cluster associated
    with the Cloud Composer environment. Supported for Cloud Composer
    environments in versions composer-2.\ *.*-airflow-*.*.\* and newer.

    Attributes:
        scheduler (google.cloud.orchestration.airflow.service_v1beta1.types.WorkloadsConfig.SchedulerResource):
            Optional. Resources used by Airflow
            schedulers.
        web_server (google.cloud.orchestration.airflow.service_v1beta1.types.WorkloadsConfig.WebServerResource):
            Optional. Resources used by Airflow web
            server.
        worker (google.cloud.orchestration.airflow.service_v1beta1.types.WorkloadsConfig.WorkerResource):
            Optional. Resources used by Airflow workers.
        triggerer (google.cloud.orchestration.airflow.service_v1beta1.types.WorkloadsConfig.TriggererResource):
            Optional. Resources used by Airflow
            triggerers.
        dag_processor (google.cloud.orchestration.airflow.service_v1beta1.types.WorkloadsConfig.DagProcessorResource):
            Optional. Resources used by Airflow DAG processors.

            This field is supported for Cloud Composer environments in
            versions composer-3-airflow-*.*.\ *-build.* and newer.
    """

    class SchedulerResource(proto.Message):
        r"""Configuration for resources used by Airflow schedulers.

        Attributes:
            cpu (float):
                Optional. CPU request and limit for a single
                Airflow scheduler replica.
            memory_gb (float):
                Optional. Memory (GB) request and limit for a
                single Airflow scheduler replica.
            storage_gb (float):
                Optional. Storage (GB) request and limit for
                a single Airflow scheduler replica.
            count (int):
                Optional. The number of schedulers.
        """

        cpu: float = proto.Field(
            proto.FLOAT,
            number=1,
        )
        memory_gb: float = proto.Field(
            proto.FLOAT,
            number=2,
        )
        storage_gb: float = proto.Field(
            proto.FLOAT,
            number=3,
        )
        count: int = proto.Field(
            proto.INT32,
            number=4,
        )

    class WebServerResource(proto.Message):
        r"""Configuration for resources used by Airflow web server.

        Attributes:
            cpu (float):
                Optional. CPU request and limit for Airflow
                web server.
            memory_gb (float):
                Optional. Memory (GB) request and limit for
                Airflow web server.
            storage_gb (float):
                Optional. Storage (GB) request and limit for
                Airflow web server.
        """

        cpu: float = proto.Field(
            proto.FLOAT,
            number=1,
        )
        memory_gb: float = proto.Field(
            proto.FLOAT,
            number=2,
        )
        storage_gb: float = proto.Field(
            proto.FLOAT,
            number=3,
        )

    class WorkerResource(proto.Message):
        r"""Configuration for resources used by Airflow workers.

        Attributes:
            cpu (float):
                Optional. CPU request and limit for a single
                Airflow worker replica.
            memory_gb (float):
                Optional. Memory (GB) request and limit for a
                single Airflow worker replica.
            storage_gb (float):
                Optional. Storage (GB) request and limit for
                a single Airflow worker replica.
            min_count (int):
                Optional. Minimum number of workers for
                autoscaling.
            max_count (int):
                Optional. Maximum number of workers for
                autoscaling.
        """

        cpu: float = proto.Field(
            proto.FLOAT,
            number=1,
        )
        memory_gb: float = proto.Field(
            proto.FLOAT,
            number=2,
        )
        storage_gb: float = proto.Field(
            proto.FLOAT,
            number=3,
        )
        min_count: int = proto.Field(
            proto.INT32,
            number=4,
        )
        max_count: int = proto.Field(
            proto.INT32,
            number=5,
        )

    class TriggererResource(proto.Message):
        r"""Configuration for resources used by Airflow triggerers.

        Attributes:
            count (int):
                Optional. The number of triggerers.
            cpu (float):
                Optional. CPU request and limit for a single
                Airflow triggerer replica.
            memory_gb (float):
                Optional. Memory (GB) request and limit for a
                single Airflow triggerer replica.
        """

        count: int = proto.Field(
            proto.INT32,
            number=1,
        )
        cpu: float = proto.Field(
            proto.FLOAT,
            number=2,
        )
        memory_gb: float = proto.Field(
            proto.FLOAT,
            number=3,
        )

    class DagProcessorResource(proto.Message):
        r"""Configuration for resources used by Airflow DAG processors.

        This field is supported for Cloud Composer environments in versions
        composer-3-airflow-*.*.\ *-build.* and newer.

        Attributes:
            cpu (float):
                Optional. CPU request and limit for a single
                Airflow DAG processor replica.
            memory_gb (float):
                Optional. Memory (GB) request and limit for a
                single Airflow DAG processor replica.
            storage_gb (float):
                Optional. Storage (GB) request and limit for
                a single Airflow DAG processor replica.
            count (int):
                Optional. The number of DAG processors. If
                not provided or set to 0, a single DAG processor
                instance will be created.
        """

        cpu: float = proto.Field(
            proto.FLOAT,
            number=1,
        )
        memory_gb: float = proto.Field(
            proto.FLOAT,
            number=2,
        )
        storage_gb: float = proto.Field(
            proto.FLOAT,
            number=3,
        )
        count: int = proto.Field(
            proto.INT32,
            number=4,
        )

    scheduler: SchedulerResource = proto.Field(
        proto.MESSAGE,
        number=1,
        message=SchedulerResource,
    )
    web_server: WebServerResource = proto.Field(
        proto.MESSAGE,
        number=2,
        message=WebServerResource,
    )
    worker: WorkerResource = proto.Field(
        proto.MESSAGE,
        number=3,
        message=WorkerResource,
    )
    triggerer: TriggererResource = proto.Field(
        proto.MESSAGE,
        number=4,
        message=TriggererResource,
    )
    dag_processor: DagProcessorResource = proto.Field(
        proto.MESSAGE,
        number=5,
        message=DagProcessorResource,
    )


class DataRetentionConfig(proto.Message):
    r"""The configuration setting for Airflow database data retention
    mechanism.

    Attributes:
        airflow_database_retention_days (int):
            Optional. The number of days describing for
            how long to store event-based records in airflow
            database. If the retention mechanism is enabled
            this value must be a positive integer otherwise,
            value should be set to 0.
        task_logs_retention_config (google.cloud.orchestration.airflow.service_v1beta1.types.TaskLogsRetentionConfig):
            Optional. The configuration settings for task
            logs retention
        airflow_metadata_retention_config (google.cloud.orchestration.airflow.service_v1beta1.types.AirflowMetadataRetentionPolicyConfig):
            Optional. The retention policy for airflow
            metadata database.
    """

    airflow_database_retention_days: int = proto.Field(
        proto.INT32,
        number=1,
    )
    task_logs_retention_config: "TaskLogsRetentionConfig" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="TaskLogsRetentionConfig",
    )
    airflow_metadata_retention_config: "AirflowMetadataRetentionPolicyConfig" = (
        proto.Field(
            proto.MESSAGE,
            number=5,
            message="AirflowMetadataRetentionPolicyConfig",
        )
    )


class TaskLogsRetentionConfig(proto.Message):
    r"""The configuration setting for Task Logs.

    Attributes:
        storage_mode (google.cloud.orchestration.airflow.service_v1beta1.types.TaskLogsRetentionConfig.TaskLogsStorageMode):
            Optional. The mode of storage for Airflow
            workers task logs.
    """

    class TaskLogsStorageMode(proto.Enum):
        r"""The definition of task_logs_storage_mode.

        Values:
            TASK_LOGS_STORAGE_MODE_UNSPECIFIED (0):
                This configuration is not specified by the
                user.
            CLOUD_LOGGING_AND_CLOUD_STORAGE (1):
                Store task logs in Cloud Logging and in the
                environment's Cloud Storage bucket.
            CLOUD_LOGGING_ONLY (2):
                Store task logs in Cloud Logging only.
        """

        TASK_LOGS_STORAGE_MODE_UNSPECIFIED = 0
        CLOUD_LOGGING_AND_CLOUD_STORAGE = 1
        CLOUD_LOGGING_ONLY = 2

    storage_mode: TaskLogsStorageMode = proto.Field(
        proto.ENUM,
        number=2,
        enum=TaskLogsStorageMode,
    )


class AirflowMetadataRetentionPolicyConfig(proto.Message):
    r"""The policy for airflow metadata database retention.

    Attributes:
        retention_mode (google.cloud.orchestration.airflow.service_v1beta1.types.AirflowMetadataRetentionPolicyConfig.RetentionMode):
            Optional. Retention can be either enabled or
            disabled.
        retention_days (int):
            Optional. How many days data should be
            retained for.
    """

    class RetentionMode(proto.Enum):
        r"""Describes retention policy.

        Values:
            RETENTION_MODE_UNSPECIFIED (0):
                Default mode doesn't change environment
                parameters.
            RETENTION_MODE_ENABLED (1):
                Retention policy is enabled.
            RETENTION_MODE_DISABLED (2):
                Retention policy is disabled.
        """

        RETENTION_MODE_UNSPECIFIED = 0
        RETENTION_MODE_ENABLED = 1
        RETENTION_MODE_DISABLED = 2

    retention_mode: RetentionMode = proto.Field(
        proto.ENUM,
        number=1,
        enum=RetentionMode,
    )
    retention_days: int = proto.Field(
        proto.INT32,
        number=2,
    )


class StorageConfig(proto.Message):
    r"""The configuration for data storage in the environment.

    Attributes:
        bucket (str):
            Optional. The name of the Cloud Storage bucket used by the
            environment. No ``gs://`` prefix.
    """

    bucket: str = proto.Field(
        proto.STRING,
        number=1,
    )


class RecoveryConfig(proto.Message):
    r"""The Recovery settings of an environment.

    Attributes:
        scheduled_snapshots_config (google.cloud.orchestration.airflow.service_v1beta1.types.ScheduledSnapshotsConfig):
            Optional. The configuration for scheduled
            snapshot creation mechanism.
    """

    scheduled_snapshots_config: "ScheduledSnapshotsConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ScheduledSnapshotsConfig",
    )


class ScheduledSnapshotsConfig(proto.Message):
    r"""The configuration for scheduled snapshot creation mechanism.

    Attributes:
        enabled (bool):
            Optional. Whether scheduled snapshots
            creation is enabled.
        snapshot_location (str):
            Optional. The Cloud Storage location for
            storing automatically created snapshots.
        snapshot_creation_schedule (str):
            Optional. The cron expression representing
            the time when snapshots creation mechanism runs.
            This field is subject to additional validation
            around frequency of execution.
        time_zone (str):
            Optional. Time zone that sets the context to interpret
            snapshot_creation_schedule.
    """

    enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    snapshot_location: str = proto.Field(
        proto.STRING,
        number=6,
    )
    snapshot_creation_schedule: str = proto.Field(
        proto.STRING,
        number=3,
    )
    time_zone: str = proto.Field(
        proto.STRING,
        number=5,
    )


class MasterAuthorizedNetworksConfig(proto.Message):
    r"""Configuration options for the master authorized networks
    feature. Enabled master authorized networks will disallow all
    external traffic to access Kubernetes master through HTTPS
    except traffic from the given CIDR blocks, Google Compute Engine
    Public IPs and Google Prod IPs.

    Attributes:
        enabled (bool):
            Optional. Whether or not master authorized
            networks feature is enabled.
        cidr_blocks (MutableSequence[google.cloud.orchestration.airflow.service_v1beta1.types.MasterAuthorizedNetworksConfig.CidrBlock]):
            Up to 50 external networks that could access
            Kubernetes master through HTTPS.
    """

    class CidrBlock(proto.Message):
        r"""CIDR block with an optional name.

        Attributes:
            display_name (str):
                User-defined name that identifies the CIDR
                block.
            cidr_block (str):
                CIDR block that must be specified in CIDR
                notation.
        """

        display_name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        cidr_block: str = proto.Field(
            proto.STRING,
            number=2,
        )

    enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    cidr_blocks: MutableSequence[CidrBlock] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=CidrBlock,
    )


class CloudDataLineageIntegration(proto.Message):
    r"""Configuration for Cloud Data Lineage integration.

    Attributes:
        enabled (bool):
            Optional. Whether or not Cloud Data Lineage
            integration is enabled.
    """

    enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class Environment(proto.Message):
    r"""An environment for running orchestration tasks.

    Attributes:
        name (str):
            Identifier. The resource name of the
            environment, in the form:
            "projects/{projectId}/locations/{locationId}/environments/{environmentId}"

            EnvironmentId must start with a lowercase letter
            followed by up to 63 lowercase letters, numbers,
            or hyphens, and cannot end with a hyphen.
        config (google.cloud.orchestration.airflow.service_v1beta1.types.EnvironmentConfig):
            Optional. Configuration parameters for this
            environment.
        uuid (str):
            Output only. The UUID (Universally Unique
            IDentifier) associated with this environment.
            This value is generated when the environment is
            created.
        state (google.cloud.orchestration.airflow.service_v1beta1.types.Environment.State):
            The current state of the environment.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which this
            environment was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which this
            environment was last modified.
        labels (MutableMapping[str, str]):
            Optional. User-defined labels for this environment. The
            labels map can contain no more than 64 entries. Entries of
            the labels map are UTF8 strings that comply with the
            following restrictions:

            - Keys must conform to regexp:
              [\\p{Ll}\\p{Lo}][\\p{Ll}\\p{Lo}\\p{N}\_-]{0,62}
            - Values must conform to regexp:
              [\\p{Ll}\\p{Lo}\\p{N}\_-]{0,63}
            - Both keys and values are additionally constrained to be <=
              128 bytes in size.
        satisfies_pzs (bool):
            Output only. Reserved for future use.
        satisfies_pzi (bool):
            Output only. Reserved for future use.
        storage_config (google.cloud.orchestration.airflow.service_v1beta1.types.StorageConfig):
            Optional. Storage configuration for this
            environment.
    """

    class State(proto.Enum):
        r"""State of the environment.

        Values:
            STATE_UNSPECIFIED (0):
                The state of the environment is unknown.
            CREATING (1):
                The environment is in the process of being
                created.
            RUNNING (2):
                The environment is currently running and
                healthy. It is ready for use.
            UPDATING (3):
                The environment is being updated. It remains
                usable but cannot receive additional update
                requests or be deleted at this time.
            DELETING (4):
                The environment is undergoing deletion. It
                cannot be used.
            ERROR (5):
                The environment has encountered an error and
                cannot be used.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        RUNNING = 2
        UPDATING = 3
        DELETING = 4
        ERROR = 5

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    config: "EnvironmentConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="EnvironmentConfig",
    )
    uuid: str = proto.Field(
        proto.STRING,
        number=3,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    satisfies_pzs: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    satisfies_pzi: bool = proto.Field(
        proto.BOOL,
        number=10,
    )
    storage_config: "StorageConfig" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="StorageConfig",
    )


class CheckUpgradeRequest(proto.Message):
    r"""Request to check whether image upgrade will succeed.

    Attributes:
        environment (str):
            The resource name of the environment to check
            upgrade for, in the form:

            "projects/{projectId}/locations/{locationId}/environments/{environmentId}".
        image_version (str):
            The version of the software running in the environment. This
            encapsulates both the version of Cloud Composer
            functionality and the version of Apache Airflow. It must
            match the regular expression
            ``composer-([0-9]+(\.[0-9]+\.[0-9]+(-preview\.[0-9]+)?)?|latest)-airflow-([0-9]+(\.[0-9]+(\.[0-9]+)?)?)``.
            When used as input, the server also checks if the provided
            version is supported and denies the request for an
            unsupported version.

            The Cloud Composer portion of the image version is a full
            `semantic version <https://semver.org>`__, or an alias in
            the form of major version number or ``latest``. When an
            alias is provided, the server replaces it with the current
            Cloud Composer version that satisfies the alias.

            The Apache Airflow portion of the image version is a full
            semantic version that points to one of the supported Apache
            Airflow versions, or an alias in the form of only major or
            major.minor versions specified. When an alias is provided,
            the server replaces it with the latest Apache Airflow
            version that satisfies the alias and is supported in the
            given Cloud Composer version.

            In all cases, the resolved image version is stored in the
            same field.

            See also `version
            list </composer/docs/concepts/versioning/composer-versions>`__
            and `versioning
            overview </composer/docs/concepts/versioning/composer-versioning-overview>`__.
    """

    environment: str = proto.Field(
        proto.STRING,
        number=1,
    )
    image_version: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CheckUpgradeResponse(proto.Message):
    r"""Message containing information about the result of an upgrade
    check operation.

    Attributes:
        build_log_uri (str):
            Output only. Url for a docker build log of an
            upgraded image.
        contains_pypi_modules_conflict (google.cloud.orchestration.airflow.service_v1beta1.types.CheckUpgradeResponse.ConflictResult):
            Output only. Whether build has succeeded or
            failed on modules conflicts.
        pypi_conflict_build_log_extract (str):
            Output only. Extract from a docker image
            build log containing information about pypi
            modules conflicts.
        image_version (str):
            Composer image for which the build was
            happening.
        pypi_dependencies (MutableMapping[str, str]):
            Pypi dependencies specified in the
            environment configuration, at the time when the
            build was triggered.
    """

    class ConflictResult(proto.Enum):
        r"""Whether there were python modules conflict during image
        build.

        Values:
            CONFLICT_RESULT_UNSPECIFIED (0):
                It is unknown whether build had conflicts or
                not.
            CONFLICT (1):
                There were python packages conflicts.
            NO_CONFLICT (2):
                There were no python packages conflicts.
        """

        CONFLICT_RESULT_UNSPECIFIED = 0
        CONFLICT = 1
        NO_CONFLICT = 2

    build_log_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    contains_pypi_modules_conflict: ConflictResult = proto.Field(
        proto.ENUM,
        number=4,
        enum=ConflictResult,
    )
    pypi_conflict_build_log_extract: str = proto.Field(
        proto.STRING,
        number=3,
    )
    image_version: str = proto.Field(
        proto.STRING,
        number=5,
    )
    pypi_dependencies: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
