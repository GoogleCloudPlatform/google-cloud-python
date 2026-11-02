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
    package="google.cloud.securitycenter.v1",
    manifest={
        "Exfiltration",
        "ExfilResource",
    },
)


class Exfiltration(proto.Message):
    r"""Exfiltration represents a data exfiltration attempt from one or more
    sources to one or more targets. The ``sources`` attribute lists the
    sources of the exfiltrated data. The ``targets`` attribute lists the
    destinations the data was copied to.

    Attributes:
        sources (MutableSequence[google.cloud.securitycenter_v1.types.ExfilResource]):
            If there are multiple sources, then the data
            is considered "joined" between them. For
            instance, BigQuery can join multiple tables, and
            each table would be considered a source.
        targets (MutableSequence[google.cloud.securitycenter_v1.types.ExfilResource]):
            If there are multiple targets, each target
            would get a complete copy of the "joined" source
            data.
        total_exfiltrated_bytes (int):
            Total exfiltrated bytes processed for the
            entire job.
    """

    sources: MutableSequence["ExfilResource"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ExfilResource",
    )
    targets: MutableSequence["ExfilResource"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="ExfilResource",
    )
    total_exfiltrated_bytes: int = proto.Field(
        proto.INT64,
        number=3,
    )


class ExfilResource(proto.Message):
    r"""Resource where data was exfiltrated from or exfiltrated to.

    Attributes:
        name (str):
            The resource's `full resource
            name <https://cloud.google.com/apis/design/resource_names#full_resource_name>`__.
        components (MutableSequence[str]):
            Subcomponents of the asset that was
            exfiltrated, like URIs used during exfiltration,
            table names, databases, and filenames. For
            example, multiple tables might have been
            exfiltrated from the same Cloud SQL instance, or
            multiple files might have been exfiltrated from
            the same Cloud Storage bucket.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    components: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
