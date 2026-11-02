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
    package="google.cloud.discoveryengine.v1beta",
    manifest={
        "ProvisionProjectRequest",
        "ProvisionProjectMetadata",
    },
)


class ProvisionProjectRequest(proto.Message):
    r"""Request for
    [ProjectService.ProvisionProject][google.cloud.discoveryengine.v1beta.ProjectService.ProvisionProject]
    method.

    Attributes:
        name (str):
            Required. Full resource name of a
            [Project][google.cloud.discoveryengine.v1beta.Project], such
            as ``projects/{project_id_or_number}``.
        accept_data_use_terms (bool):
            Required. Set to ``true`` to specify that caller has read
            and would like to give consent to the `Terms for data
            use <https://cloud.google.com/retail/data-use-terms>`__.
        data_use_terms_version (str):
            Required. The version of the `Terms for data
            use <https://cloud.google.com/retail/data-use-terms>`__ that
            caller has read and would like to give consent to.

            Acceptable version is ``2022-11-23``, and this may change
            over time.
        saas_params (google.cloud.discoveryengine_v1beta.types.ProvisionProjectRequest.SaasParams):
            Optional. Parameters for Agentspace.
    """

    class SaasParams(proto.Message):
        r"""Parameters for Agentspace.

        Attributes:
            accept_biz_qos (bool):
                Optional. Set to ``true`` to specify that caller has read
                and would like to give consent to the [Terms for Agent Space
                quality of service].
            is_biz (bool):
                Optional. Indicates if the current request is
                for Biz edition (= true) or not
                (= false).
        """

        accept_biz_qos: bool = proto.Field(
            proto.BOOL,
            number=1,
        )
        is_biz: bool = proto.Field(
            proto.BOOL,
            number=2,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    accept_data_use_terms: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    data_use_terms_version: str = proto.Field(
        proto.STRING,
        number=3,
    )
    saas_params: SaasParams = proto.Field(
        proto.MESSAGE,
        number=4,
        message=SaasParams,
    )


class ProvisionProjectMetadata(proto.Message):
    r"""Metadata associated with a project provision operation."""


__all__ = tuple(sorted(__protobuf__.manifest))
