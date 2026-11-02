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
    package="google.cloud.securitycenter.v2",
    manifest={
        "Notebook",
    },
)


class Notebook(proto.Message):
    r"""Represents a Jupyter notebook IPYNB file, such as a `Colab
    Enterprise
    notebook <https://cloud.google.com/colab/docs/introduction>`__ file,
    that is associated with a finding.

    Attributes:
        name (str):
            The name of the notebook.
        service (str):
            The source notebook service, for example,
            "Colab Enterprise".
        last_author (str):
            The user ID of the latest author to modify
            the notebook.
        notebook_update_time (google.protobuf.timestamp_pb2.Timestamp):
            The most recent time the notebook was
            updated.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    service: str = proto.Field(
        proto.STRING,
        number=2,
    )
    last_author: str = proto.Field(
        proto.STRING,
        number=3,
    )
    notebook_update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
