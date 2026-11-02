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

import google.api.launch_stage_pb2 as launch_stage_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.documentai.v1",
    manifest={
        "ProcessorType",
    },
)


class ProcessorType(proto.Message):
    r"""A processor type is responsible for performing a certain
    document understanding task on a certain type of document.

    Attributes:
        name (str):
            The resource name of the processor type. Format:
            ``projects/{project}/processorTypes/{processor_type}``
        type_ (str):
            The processor type, such as: ``OCR_PROCESSOR``,
            ``INVOICE_PROCESSOR``.
        category (str):
            The processor category, used by UI to group
            processor types.
        available_locations (MutableSequence[google.cloud.documentai_v1.types.ProcessorType.LocationInfo]):
            The locations in which this processor is
            available.
        allow_creation (bool):
            Whether the processor type allows creation.
            If true, users can create a processor of this
            processor type. Otherwise, users need to request
            access.
        launch_stage (google.api.launch_stage_pb2.LaunchStage):
            Launch stage of the processor type
        sample_document_uris (MutableSequence[str]):
            A set of Cloud Storage URIs of sample
            documents for this processor.
    """

    class LocationInfo(proto.Message):
        r"""The location information about where the processor is
        available.

        Attributes:
            location_id (str):
                The location ID. For supported locations, refer to `regional
                and multi-regional support </document-ai/docs/regions>`__.
        """

        location_id: str = proto.Field(
            proto.STRING,
            number=1,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=2,
    )
    category: str = proto.Field(
        proto.STRING,
        number=3,
    )
    available_locations: MutableSequence[LocationInfo] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=LocationInfo,
    )
    allow_creation: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    launch_stage: launch_stage_pb2.LaunchStage = proto.Field(
        proto.ENUM,
        number=8,
        enum=launch_stage_pb2.LaunchStage,
    )
    sample_document_uris: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=9,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
