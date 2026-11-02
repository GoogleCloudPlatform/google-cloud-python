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
    package="google.cloud.dataplex.v1",
    manifest={
        "ResourceAccessSpec",
        "DataAccessSpec",
    },
)


class ResourceAccessSpec(proto.Message):
    r"""ResourceAccessSpec holds the access control configuration to
    be enforced on the resources, for example, Cloud Storage bucket,
    BigQuery dataset, BigQuery table.

    Attributes:
        readers (MutableSequence[str]):
            Optional. The format of strings follows the
            pattern followed by IAM in the bindings.
            user:{email}, serviceAccount:{email}
            group:{email}. The set of principals to be
            granted reader role on the resource.
        writers (MutableSequence[str]):
            Optional. The set of principals to be granted
            writer role on the resource.
        owners (MutableSequence[str]):
            Optional. The set of principals to be granted
            owner role on the resource.
    """

    readers: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    writers: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    owners: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class DataAccessSpec(proto.Message):
    r"""DataAccessSpec holds the access control configuration to be
    enforced on data stored within resources (eg: rows, columns in
    BigQuery Tables). When associated with data, the data is only
    accessible to principals explicitly granted access through the
    DataAccessSpec. Principals with access to the containing
    resource are not implicitly granted access.

    Attributes:
        readers (MutableSequence[str]):
            Optional. The format of strings follows the
            pattern followed by IAM in the bindings.
            user:{email}, serviceAccount:{email}
            group:{email}. The set of principals to be
            granted reader role on data stored within
            resources.
    """

    readers: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
