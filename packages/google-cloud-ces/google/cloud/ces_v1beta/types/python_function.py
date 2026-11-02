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

from google.cloud.ces_v1beta.types import common

__protobuf__ = proto.module(
    package="google.cloud.ces.v1beta",
    manifest={
        "PythonFunction",
    },
)


class PythonFunction(proto.Message):
    r"""A Python function tool.

    Attributes:
        name (str):
            Optional. The name of the Python function to
            execute. Must match a Python function name
            defined in the python code. Case sensitive. If
            the name is not provided, the first function
            defined in the python code will be used.
        python_code (str):
            Optional. The Python code to execute for the
            tool.
        description (str):
            Output only. The description of the Python
            function, parsed from the python code's
            docstring.
        service_directory_config (google.cloud.ces_v1beta.types.ServiceDirectoryConfig):
            Optional. Service Directory configuration for
            the tool.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    python_code: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    service_directory_config: common.ServiceDirectoryConfig = proto.Field(
        proto.MESSAGE,
        number=4,
        message=common.ServiceDirectoryConfig,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
