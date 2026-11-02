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

from google.cloud.datalabeling_v1beta1.types import dataset

__protobuf__ = proto.module(
    package="google.cloud.datalabeling.v1beta1",
    manifest={
        "Instruction",
        "CsvInstruction",
        "PdfInstruction",
    },
)


class Instruction(proto.Message):
    r"""Instruction of how to perform the labeling task for human
    operators. Currently only PDF instruction is supported.

    Attributes:
        name (str):
            Output only. Instruction resource name, format:
            projects/{project_id}/instructions/{instruction_id}
        display_name (str):
            Required. The display name of the
            instruction. Maximum of 64 characters.
        description (str):
            Optional. User-provided description of the
            instruction. The description can be up to 10000
            characters long.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Creation time of instruction.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Last update time of instruction.
        data_type (google.cloud.datalabeling_v1beta1.types.DataType):
            Required. The data type of this instruction.
        csv_instruction (google.cloud.datalabeling_v1beta1.types.CsvInstruction):
            Deprecated: this instruction format is not supported any
            more. Instruction from a CSV file, such as for
            classification task. The CSV file should have exact two
            columns, in the following format:

            - The first column is labeled data, such as an image
              reference, text.
            - The second column is comma separated labels associated
              with data.
        pdf_instruction (google.cloud.datalabeling_v1beta1.types.PdfInstruction):
            Instruction from a PDF document. The PDF
            should be in a Cloud Storage bucket.
        blocking_resources (MutableSequence[str]):
            Output only. The names of any related
            resources that are blocking changes to the
            instruction.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    data_type: dataset.DataType = proto.Field(
        proto.ENUM,
        number=6,
        enum=dataset.DataType,
    )
    csv_instruction: "CsvInstruction" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="CsvInstruction",
    )
    pdf_instruction: "PdfInstruction" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="PdfInstruction",
    )
    blocking_resources: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=10,
    )


class CsvInstruction(proto.Message):
    r"""Deprecated: this instruction format is not supported any
    more. Instruction from a CSV file.

    Attributes:
        gcs_file_uri (str):
            CSV file for the instruction. Only gcs path
            is allowed.
    """

    gcs_file_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )


class PdfInstruction(proto.Message):
    r"""Instruction from a PDF file.

    Attributes:
        gcs_file_uri (str):
            PDF file for the instruction. Only gcs path
            is allowed.
    """

    gcs_file_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
