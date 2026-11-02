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
    package="google.cloud.datacatalog.v1beta1",
    manifest={
        "IntegratedSystem",
        "ManagingSystem",
    },
)


class IntegratedSystem(proto.Enum):
    r"""This enum describes all the possible systems that Data
    Catalog integrates with.

    Values:
        INTEGRATED_SYSTEM_UNSPECIFIED (0):
            Default unknown system.
        BIGQUERY (1):
            BigQuery.
        CLOUD_PUBSUB (2):
            Cloud Pub/Sub.
    """

    INTEGRATED_SYSTEM_UNSPECIFIED = 0
    BIGQUERY = 1
    CLOUD_PUBSUB = 2


class ManagingSystem(proto.Enum):
    r"""This enum describes all the systems that manage
    Taxonomy and PolicyTag resources in DataCatalog.

    Values:
        MANAGING_SYSTEM_UNSPECIFIED (0):
            Default value
        MANAGING_SYSTEM_DATAPLEX (1):
            Dataplex.
        MANAGING_SYSTEM_OTHER (2):
            Other
    """

    MANAGING_SYSTEM_UNSPECIFIED = 0
    MANAGING_SYSTEM_DATAPLEX = 1
    MANAGING_SYSTEM_OTHER = 2


__all__ = tuple(sorted(__protobuf__.manifest))
