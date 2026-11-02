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
    package="google.cloud.notebooks.v1",
    manifest={
        "ExecutionTemplate",
        "Execution",
    },
)


class ExecutionTemplate(proto.Message):
    r"""The description a notebook execution workload.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        scale_tier (google.cloud.notebooks_v1.types.ExecutionTemplate.ScaleTier):
            Required. Scale tier of the hardware used for
            notebook execution. DEPRECATED Will be
            discontinued. As right now only CUSTOM is
            supported.
        master_type (str):
            Specifies the type of virtual machine to use for your
            training job's master worker. You must specify this field
            when ``scaleTier`` is set to ``CUSTOM``.

            You can use certain Compute Engine machine types directly in
            this field. The following types are supported:

            - ``n1-standard-4``
            - ``n1-standard-8``
            - ``n1-standard-16``
            - ``n1-standard-32``
            - ``n1-standard-64``
            - ``n1-standard-96``
            - ``n1-highmem-2``
            - ``n1-highmem-4``
            - ``n1-highmem-8``
            - ``n1-highmem-16``
            - ``n1-highmem-32``
            - ``n1-highmem-64``
            - ``n1-highmem-96``
            - ``n1-highcpu-16``
            - ``n1-highcpu-32``
            - ``n1-highcpu-64``
            - ``n1-highcpu-96``

            Alternatively, you can use the following legacy machine
            types:

            - ``standard``
            - ``large_model``
            - ``complex_model_s``
            - ``complex_model_m``
            - ``complex_model_l``
            - ``standard_gpu``
            - ``complex_model_m_gpu``
            - ``complex_model_l_gpu``
            - ``standard_p100``
            - ``complex_model_m_p100``
            - ``standard_v100``
            - ``large_model_v100``
            - ``complex_model_m_v100``
            - ``complex_model_l_v100``

            Finally, if you want to use a TPU for training, specify
            ``cloud_tpu`` in this field. Learn more about the `special
            configuration options for training with
            TPU <https://cloud.google.com/ai-platform/training/docs/using-tpus#configuring_a_custom_tpu_machine>`__.
        accelerator_config (google.cloud.notebooks_v1.types.ExecutionTemplate.SchedulerAcceleratorConfig):
            Configuration (count and accelerator type)
            for hardware running notebook execution.
        labels (MutableMapping[str, str]):
            Labels for execution.
            If execution is scheduled, a field included will
            be 'nbs-scheduled'. Otherwise, it is an
            immediate execution, and an included field will
            be 'nbs-immediate'. Use fields to efficiently
            index between various types of executions.
        input_notebook_file (str):
            Path to the notebook file to execute. Must be in a Google
            Cloud Storage bucket. Format:
            ``gs://{bucket_name}/{folder}/{notebook_file_name}`` Ex:
            ``gs://notebook_user/scheduled_notebooks/sentiment_notebook.ipynb``
        container_image_uri (str):
            Container Image URI to a DLVM
            Example:
            'gcr.io/deeplearning-platform-release/base-cu100'
            More examples can be found at:

            https://cloud.google.com/ai-platform/deep-learning-containers/docs/choosing-container
        output_notebook_folder (str):
            Path to the notebook folder to write to. Must be in a Google
            Cloud Storage bucket path. Format:
            ``gs://{bucket_name}/{folder}`` Ex:
            ``gs://notebook_user/scheduled_notebooks``
        params_yaml_file (str):
            Parameters to be overridden in the notebook during
            execution. Ref
            https://papermill.readthedocs.io/en/latest/usage-parameterize.html
            on how to specifying parameters in the input notebook and
            pass them here in an YAML file. Ex:
            ``gs://notebook_user/scheduled_notebooks/sentiment_notebook_params.yaml``
        parameters (str):
            Parameters used within the 'input_notebook_file' notebook.
        service_account (str):
            The email address of a service account to use when running
            the execution. You must have the
            ``iam.serviceAccounts.actAs`` permission for the specified
            service account.
        job_type (google.cloud.notebooks_v1.types.ExecutionTemplate.JobType):
            The type of Job to be used on this execution.
        dataproc_parameters (google.cloud.notebooks_v1.types.ExecutionTemplate.DataprocParameters):
            Parameters used in Dataproc JobType
            executions.

            This field is a member of `oneof`_ ``job_parameters``.
        vertex_ai_parameters (google.cloud.notebooks_v1.types.ExecutionTemplate.VertexAIParameters):
            Parameters used in Vertex AI JobType
            executions.

            This field is a member of `oneof`_ ``job_parameters``.
        kernel_spec (str):
            Name of the kernel spec to use. This must be
            specified if the kernel spec name on the
            execution target does not match the name in the
            input notebook file.
        tensorboard (str):
            The name of a Vertex AI [Tensorboard] resource to which this
            execution will upload Tensorboard logs. Format:
            ``projects/{project}/locations/{location}/tensorboards/{tensorboard}``
    """

    class ScaleTier(proto.Enum):
        r"""Required. Specifies the machine types, the number of replicas
        for workers and parameter servers.

        Values:
            SCALE_TIER_UNSPECIFIED (0):
                Unspecified Scale Tier.
            BASIC (1):
                A single worker instance. This tier is
                suitable for learning how to use Cloud ML, and
                for experimenting with new models using small
                datasets.
            STANDARD_1 (2):
                Many workers and a few parameter servers.
            PREMIUM_1 (3):
                A large number of workers with many parameter
                servers.
            BASIC_GPU (4):
                A single worker instance with a K80 GPU.
            BASIC_TPU (5):
                A single worker instance with a Cloud TPU.
            CUSTOM (6):
                The CUSTOM tier is not a set tier, but rather enables you to
                use your own cluster specification. When you use this tier,
                set values to configure your processing cluster according to
                these guidelines:

                - You *must* set ``ExecutionTemplate.masterType`` to specify
                  the type of machine to use for your master node. This is
                  the only required setting.
        """

        SCALE_TIER_UNSPECIFIED = 0
        BASIC = 1
        STANDARD_1 = 2
        PREMIUM_1 = 3
        BASIC_GPU = 4
        BASIC_TPU = 5
        CUSTOM = 6

    class SchedulerAcceleratorType(proto.Enum):
        r"""Hardware accelerator types for AI Platform Training jobs.

        Values:
            SCHEDULER_ACCELERATOR_TYPE_UNSPECIFIED (0):
                Unspecified accelerator type. Default to no
                GPU.
            NVIDIA_TESLA_K80 (1):
                Nvidia Tesla K80 GPU.
            NVIDIA_TESLA_P100 (2):
                Nvidia Tesla P100 GPU.
            NVIDIA_TESLA_V100 (3):
                Nvidia Tesla V100 GPU.
            NVIDIA_TESLA_P4 (4):
                Nvidia Tesla P4 GPU.
            NVIDIA_TESLA_T4 (5):
                Nvidia Tesla T4 GPU.
            NVIDIA_TESLA_A100 (10):
                Nvidia Tesla A100 GPU.
            TPU_V2 (6):
                TPU v2.
            TPU_V3 (7):
                TPU v3.
        """

        SCHEDULER_ACCELERATOR_TYPE_UNSPECIFIED = 0
        NVIDIA_TESLA_K80 = 1
        NVIDIA_TESLA_P100 = 2
        NVIDIA_TESLA_V100 = 3
        NVIDIA_TESLA_P4 = 4
        NVIDIA_TESLA_T4 = 5
        NVIDIA_TESLA_A100 = 10
        TPU_V2 = 6
        TPU_V3 = 7

    class JobType(proto.Enum):
        r"""The backend used for this execution.

        Values:
            JOB_TYPE_UNSPECIFIED (0):
                No type specified.
            VERTEX_AI (1):
                Custom Job in ``aiplatform.googleapis.com``. Default value
                for an execution.
            DATAPROC (2):
                Run execution on a cluster with Dataproc as a
                job.
                https://cloud.google.com/dataproc/docs/reference/rest/v1/projects.regions.jobs
        """

        JOB_TYPE_UNSPECIFIED = 0
        VERTEX_AI = 1
        DATAPROC = 2

    class SchedulerAcceleratorConfig(proto.Message):
        r"""Definition of a hardware accelerator. Note that not all combinations
        of ``type`` and ``core_count`` are valid. Check `GPUs on Compute
        Engine <https://cloud.google.com/compute/docs/gpus>`__ to find a
        valid combination. TPUs are not supported.

        Attributes:
            type_ (google.cloud.notebooks_v1.types.ExecutionTemplate.SchedulerAcceleratorType):
                Type of this accelerator.
            core_count (int):
                Count of cores of this accelerator.
        """

        type_: "ExecutionTemplate.SchedulerAcceleratorType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="ExecutionTemplate.SchedulerAcceleratorType",
        )
        core_count: int = proto.Field(
            proto.INT64,
            number=2,
        )

    class DataprocParameters(proto.Message):
        r"""Parameters used in Dataproc JobType executions.

        Attributes:
            cluster (str):
                URI for cluster used to run Dataproc execution. Format:
                ``projects/{PROJECT_ID}/regions/{REGION}/clusters/{CLUSTER_NAME}``
        """

        cluster: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class VertexAIParameters(proto.Message):
        r"""Parameters used in Vertex AI JobType executions.

        Attributes:
            network (str):
                The full name of the Compute Engine
                `network <https://cloud.google.com/compute/docs/networks-and-firewalls#networks>`__
                to which the Job should be peered. For example,
                ``projects/12345/global/networks/myVPC``.
                `Format <https://cloud.google.com/compute/docs/reference/rest/v1/networks/insert>`__
                is of the form
                ``projects/{project}/global/networks/{network}``. Where
                ``{project}`` is a project number, as in ``12345``, and
                ``{network}`` is a network name.

                Private services access must already be configured for the
                network. If left unspecified, the job is not peered with any
                network.
            env (MutableMapping[str, str]):
                Environment variables. At most 100 environment variables can
                be specified and unique. Example:
                ``GCP_BUCKET=gs://my-bucket/samples/``
        """

        network: str = proto.Field(
            proto.STRING,
            number=1,
        )
        env: MutableMapping[str, str] = proto.MapField(
            proto.STRING,
            proto.STRING,
            number=2,
        )

    scale_tier: ScaleTier = proto.Field(
        proto.ENUM,
        number=1,
        enum=ScaleTier,
    )
    master_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    accelerator_config: SchedulerAcceleratorConfig = proto.Field(
        proto.MESSAGE,
        number=3,
        message=SchedulerAcceleratorConfig,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    input_notebook_file: str = proto.Field(
        proto.STRING,
        number=5,
    )
    container_image_uri: str = proto.Field(
        proto.STRING,
        number=6,
    )
    output_notebook_folder: str = proto.Field(
        proto.STRING,
        number=7,
    )
    params_yaml_file: str = proto.Field(
        proto.STRING,
        number=8,
    )
    parameters: str = proto.Field(
        proto.STRING,
        number=9,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=10,
    )
    job_type: JobType = proto.Field(
        proto.ENUM,
        number=11,
        enum=JobType,
    )
    dataproc_parameters: DataprocParameters = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="job_parameters",
        message=DataprocParameters,
    )
    vertex_ai_parameters: VertexAIParameters = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="job_parameters",
        message=VertexAIParameters,
    )
    kernel_spec: str = proto.Field(
        proto.STRING,
        number=14,
    )
    tensorboard: str = proto.Field(
        proto.STRING,
        number=15,
    )


class Execution(proto.Message):
    r"""The definition of a single executed notebook.

    Attributes:
        execution_template (google.cloud.notebooks_v1.types.ExecutionTemplate):
            execute metadata including name, hardware
            spec, region, labels, etc.
        name (str):
            Output only. The resource name of the execute. Format:
            ``projects/{project_id}/locations/{location}/executions/{execution_id}``
        display_name (str):
            Output only. Name used for UI purposes. Name can only
            contain alphanumeric characters and underscores '\_'.
        description (str):
            A brief description of this execution.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time the Execution was
            instantiated.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time the Execution was last
            updated.
        state (google.cloud.notebooks_v1.types.Execution.State):
            Output only. State of the underlying AI
            Platform job.
        output_notebook_file (str):
            Output notebook file generated by this
            execution
        job_uri (str):
            Output only. The URI of the external job used
            to execute the notebook.
    """

    class State(proto.Enum):
        r"""Enum description of the state of the underlying AIP job.

        Values:
            STATE_UNSPECIFIED (0):
                The job state is unspecified.
            QUEUED (1):
                The job has been just created and processing
                has not yet begun.
            PREPARING (2):
                The service is preparing to execution the
                job.
            RUNNING (3):
                The job is in progress.
            SUCCEEDED (4):
                The job completed successfully.
            FAILED (5):
                The job failed. ``error_message`` should contain the details
                of the failure.
            CANCELLING (6):
                The job is being cancelled. ``error_message`` should
                describe the reason for the cancellation.
            CANCELLED (7):
                The job has been cancelled. ``error_message`` should
                describe the reason for the cancellation.
            EXPIRED (9):
                The job has become expired (relevant to
                Vertex AI jobs)
                https://cloud.google.com/vertex-ai/docs/reference/rest/v1/JobState
            INITIALIZING (10):
                The Execution is being created.
        """

        STATE_UNSPECIFIED = 0
        QUEUED = 1
        PREPARING = 2
        RUNNING = 3
        SUCCEEDED = 4
        FAILED = 5
        CANCELLING = 6
        CANCELLED = 7
        EXPIRED = 9
        INITIALIZING = 10

    execution_template: "ExecutionTemplate" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ExecutionTemplate",
    )
    name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
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
    state: State = proto.Field(
        proto.ENUM,
        number=7,
        enum=State,
    )
    output_notebook_file: str = proto.Field(
        proto.STRING,
        number=8,
    )
    job_uri: str = proto.Field(
        proto.STRING,
        number=9,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
