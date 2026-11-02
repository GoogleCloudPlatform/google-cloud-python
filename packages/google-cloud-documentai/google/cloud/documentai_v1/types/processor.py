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

from google.cloud.documentai_v1.types import document_schema as gcd_document_schema
from google.cloud.documentai_v1.types import evaluation

__protobuf__ = proto.module(
    package="google.cloud.documentai.v1",
    manifest={
        "ProcessorVersion",
        "ProcessorVersionAlias",
        "Processor",
    },
)


class ProcessorVersion(proto.Message):
    r"""A processor version is an implementation of a processor. Each
    processor can have multiple versions, pretrained by Google
    internally or uptrained by the customer. A processor can only
    have one default version at a time. Its document-processing
    behavior is defined by that version.

    Attributes:
        name (str):
            Identifier. The resource name of the processor version.
            Format:
            ``projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processor_version}``
        display_name (str):
            The display name of the processor version.
        document_schema (google.cloud.documentai_v1.types.DocumentSchema):
            Output only. The schema of the processor
            version. Describes the output.
        state (google.cloud.documentai_v1.types.ProcessorVersion.State):
            Output only. The state of the processor
            version.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the processor version
            was created.
        latest_evaluation (google.cloud.documentai_v1.types.EvaluationReference):
            Output only. The most recently invoked
            evaluation for the processor version.
        kms_key_name (str):
            Output only. The KMS key name used for
            encryption.
        kms_key_version_name (str):
            Output only. The KMS key version with which
            data is encrypted.
        google_managed (bool):
            Output only. Denotes that this ``ProcessorVersion`` is
            managed by Google.
        deprecation_info (google.cloud.documentai_v1.types.ProcessorVersion.DeprecationInfo):
            Output only. If set, information about the
            eventual deprecation of this version.
        model_type (google.cloud.documentai_v1.types.ProcessorVersion.ModelType):
            Output only. The model type of this processor
            version.
        satisfies_pzs (bool):
            Output only. Reserved for future use.
        satisfies_pzi (bool):
            Output only. Reserved for future use.
        gen_ai_model_info (google.cloud.documentai_v1.types.ProcessorVersion.GenAiModelInfo):
            Output only. Information about Generative AI
            model-based processor versions.
    """

    class State(proto.Enum):
        r"""The possible states of the processor version.

        Values:
            STATE_UNSPECIFIED (0):
                The processor version is in an unspecified
                state.
            DEPLOYED (1):
                The processor version is deployed and can be
                used for processing.
            DEPLOYING (2):
                The processor version is being deployed.
            UNDEPLOYED (3):
                The processor version is not deployed and
                cannot be used for processing.
            UNDEPLOYING (4):
                The processor version is being undeployed.
            CREATING (5):
                The processor version is being created.
            DELETING (6):
                The processor version is being deleted.
            FAILED (7):
                The processor version failed and is in an
                indeterminate state.
            IMPORTING (8):
                The processor version is being imported.
        """

        STATE_UNSPECIFIED = 0
        DEPLOYED = 1
        DEPLOYING = 2
        UNDEPLOYED = 3
        UNDEPLOYING = 4
        CREATING = 5
        DELETING = 6
        FAILED = 7
        IMPORTING = 8

    class ModelType(proto.Enum):
        r"""The possible model types of the processor version.

        Values:
            MODEL_TYPE_UNSPECIFIED (0):
                The processor version has unspecified model
                type.
            MODEL_TYPE_GENERATIVE (1):
                The processor version has generative model
                type.
            MODEL_TYPE_CUSTOM (2):
                The processor version has custom model type.
        """

        MODEL_TYPE_UNSPECIFIED = 0
        MODEL_TYPE_GENERATIVE = 1
        MODEL_TYPE_CUSTOM = 2

    class DeprecationInfo(proto.Message):
        r"""Information about the upcoming deprecation of this processor
        version.

        Attributes:
            deprecation_time (google.protobuf.timestamp_pb2.Timestamp):
                The time at which this processor version will
                be deprecated.
            replacement_processor_version (str):
                If set, the processor version that will be
                used as a replacement.
        """

        deprecation_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=1,
            message=timestamp_pb2.Timestamp,
        )
        replacement_processor_version: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class GenAiModelInfo(proto.Message):
        r"""Information about Generative AI model-based processor
        versions.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            foundation_gen_ai_model_info (google.cloud.documentai_v1.types.ProcessorVersion.GenAiModelInfo.FoundationGenAiModelInfo):
                Information for a pretrained Google-managed
                foundation model.

                This field is a member of `oneof`_ ``model_info``.
            custom_gen_ai_model_info (google.cloud.documentai_v1.types.ProcessorVersion.GenAiModelInfo.CustomGenAiModelInfo):
                Information for a custom Generative AI model
                created by the user.

                This field is a member of `oneof`_ ``model_info``.
        """

        class FoundationGenAiModelInfo(proto.Message):
            r"""Information for a pretrained Google-managed foundation model.

            Attributes:
                finetuning_allowed (bool):
                    Whether finetuning is allowed for this base
                    processor version.
                min_train_labeled_documents (int):
                    The minimum number of labeled documents in
                    the training dataset required for finetuning.
            """

            finetuning_allowed: bool = proto.Field(
                proto.BOOL,
                number=1,
            )
            min_train_labeled_documents: int = proto.Field(
                proto.INT32,
                number=2,
            )

        class CustomGenAiModelInfo(proto.Message):
            r"""Information for a custom Generative AI model created by the user.
            These are created with ``Create New Version`` in either the
            ``Call foundation model`` or ``Fine tuning`` tabs.

            Attributes:
                custom_model_type (google.cloud.documentai_v1.types.ProcessorVersion.GenAiModelInfo.CustomGenAiModelInfo.CustomModelType):
                    The type of custom model created by the user.
                base_processor_version_id (str):
                    The base processor version ID for the custom
                    model.
            """

            class CustomModelType(proto.Enum):
                r"""The type of custom model created by the user.

                Values:
                    CUSTOM_MODEL_TYPE_UNSPECIFIED (0):
                        The model type is unspecified.
                    VERSIONED_FOUNDATION (1):
                        The model is a versioned foundation model.
                    FINE_TUNED (2):
                        The model is a finetuned foundation model.
                """

                CUSTOM_MODEL_TYPE_UNSPECIFIED = 0
                VERSIONED_FOUNDATION = 1
                FINE_TUNED = 2

            custom_model_type: "ProcessorVersion.GenAiModelInfo.CustomGenAiModelInfo.CustomModelType" = proto.Field(
                proto.ENUM,
                number=1,
                enum="ProcessorVersion.GenAiModelInfo.CustomGenAiModelInfo.CustomModelType",
            )
            base_processor_version_id: str = proto.Field(
                proto.STRING,
                number=2,
            )

        foundation_gen_ai_model_info: "ProcessorVersion.GenAiModelInfo.FoundationGenAiModelInfo" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="model_info",
            message="ProcessorVersion.GenAiModelInfo.FoundationGenAiModelInfo",
        )
        custom_gen_ai_model_info: "ProcessorVersion.GenAiModelInfo.CustomGenAiModelInfo" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="model_info",
            message="ProcessorVersion.GenAiModelInfo.CustomGenAiModelInfo",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    document_schema: gcd_document_schema.DocumentSchema = proto.Field(
        proto.MESSAGE,
        number=12,
        message=gcd_document_schema.DocumentSchema,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=6,
        enum=State,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    latest_evaluation: evaluation.EvaluationReference = proto.Field(
        proto.MESSAGE,
        number=8,
        message=evaluation.EvaluationReference,
    )
    kms_key_name: str = proto.Field(
        proto.STRING,
        number=9,
    )
    kms_key_version_name: str = proto.Field(
        proto.STRING,
        number=10,
    )
    google_managed: bool = proto.Field(
        proto.BOOL,
        number=11,
    )
    deprecation_info: DeprecationInfo = proto.Field(
        proto.MESSAGE,
        number=13,
        message=DeprecationInfo,
    )
    model_type: ModelType = proto.Field(
        proto.ENUM,
        number=15,
        enum=ModelType,
    )
    satisfies_pzs: bool = proto.Field(
        proto.BOOL,
        number=16,
    )
    satisfies_pzi: bool = proto.Field(
        proto.BOOL,
        number=17,
    )
    gen_ai_model_info: GenAiModelInfo = proto.Field(
        proto.MESSAGE,
        number=18,
        message=GenAiModelInfo,
    )


class ProcessorVersionAlias(proto.Message):
    r"""Contains the alias and the aliased resource name of processor
    version.

    Attributes:
        alias (str):
            The alias in the form of ``processor_version`` resource
            name.
        processor_version (str):
            The resource name of aliased processor
            version.
    """

    alias: str = proto.Field(
        proto.STRING,
        number=1,
    )
    processor_version: str = proto.Field(
        proto.STRING,
        number=2,
    )


class Processor(proto.Message):
    r"""The first-class citizen for Document AI. Each processor
    defines how to extract structural information from a document.

    Attributes:
        name (str):
            Output only. Immutable. The resource name of the processor.
            Format:
            ``projects/{project}/locations/{location}/processors/{processor}``
        type_ (str):
            The processor type, such as: ``OCR_PROCESSOR``,
            ``INVOICE_PROCESSOR``. To get a list of processor types, see
            [FetchProcessorTypes][google.cloud.documentai.v1.DocumentProcessorService.FetchProcessorTypes].
        display_name (str):
            The display name of the processor.
        state (google.cloud.documentai_v1.types.Processor.State):
            Output only. The state of the processor.
        default_processor_version (str):
            The default processor version.
        processor_version_aliases (MutableSequence[google.cloud.documentai_v1.types.ProcessorVersionAlias]):
            Output only. The processor version aliases.
        process_endpoint (str):
            Output only. Immutable. The http endpoint
            that can be called to invoke processing.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the processor was
            created.
        kms_key_name (str):
            The `KMS
            key <https://cloud.google.com/security-key-management>`__
            used for encryption and decryption in CMEK scenarios.
        satisfies_pzs (bool):
            Output only. Reserved for future use.
        satisfies_pzi (bool):
            Output only. Reserved for future use.
    """

    class State(proto.Enum):
        r"""The possible states of the processor.

        Values:
            STATE_UNSPECIFIED (0):
                The processor is in an unspecified state.
            ENABLED (1):
                The processor is enabled, i.e., has an
                enabled version which can currently serve
                processing requests and all the feature
                dependencies have been successfully initialized.
            DISABLED (2):
                The processor is disabled.
            ENABLING (3):
                The processor is being enabled, will become ``ENABLED`` if
                successful.
            DISABLING (4):
                The processor is being disabled, will become ``DISABLED`` if
                successful.
            CREATING (5):
                The processor is being created, will become either
                ``ENABLED`` (for successful creation) or ``FAILED`` (for
                failed ones). Once a processor is in this state, it can then
                be used for document processing, but the feature
                dependencies of the processor might not be fully created
                yet.
            FAILED (6):
                The processor failed during creation or
                initialization of feature dependencies. The user
                should delete the processor and recreate one as
                all the functionalities of the processor are
                disabled.
            DELETING (7):
                The processor is being deleted, will be
                removed if successful.
        """

        STATE_UNSPECIFIED = 0
        ENABLED = 1
        DISABLED = 2
        ENABLING = 3
        DISABLING = 4
        CREATING = 5
        FAILED = 6
        DELETING = 7

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )
    default_processor_version: str = proto.Field(
        proto.STRING,
        number=9,
    )
    processor_version_aliases: MutableSequence["ProcessorVersionAlias"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=10,
            message="ProcessorVersionAlias",
        )
    )
    process_endpoint: str = proto.Field(
        proto.STRING,
        number=6,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    kms_key_name: str = proto.Field(
        proto.STRING,
        number=8,
    )
    satisfies_pzs: bool = proto.Field(
        proto.BOOL,
        number=12,
    )
    satisfies_pzi: bool = proto.Field(
        proto.BOOL,
        number=13,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
