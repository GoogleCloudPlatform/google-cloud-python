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

import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.designcenter_v1.types import parameters as gcd_parameters

__protobuf__ = proto.module(
    package="google.cloud.designcenter.v1",
    manifest={
        "RootModulesMetadata",
        "RootModule",
        "RootModuleDependency",
        "RootInputVariable",
        "RootOutputVariable",
        "TerraformModule",
        "TerraformFile",
    },
)


class RootModulesMetadata(proto.Message):
    r"""Root modules metadata.

    Attributes:
        root_modules (MutableSequence[google.cloud.designcenter_v1.types.RootModule]):
            List of terraform root modules.
    """

    root_modules: MutableSequence["RootModule"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="RootModule",
    )


class RootModule(proto.Message):
    r"""Metadata for a root module.

    Attributes:
        id (str):
            Identifier of the root module. This is the
            directory name of the root module in the
            generated terraform which is also same as the
            corresponding component ID.
        components (MutableSequence[str]):
            List of Application Design Center component
            names associated with this root module. For
            standard app template type components, this list
            will have a single element. For service /
            workload / asset components, this list will
            contain all such component names.
        dependencies (MutableSequence[google.cloud.designcenter_v1.types.RootModuleDependency]):
            Dependencies of this root module. The
            dependency graph of root modules must be
            acyclic.
        input_variables (MutableSequence[google.cloud.designcenter_v1.types.RootInputVariable]):
            List of input variables of this root module.
        output_variables (MutableSequence[google.cloud.designcenter_v1.types.RootOutputVariable]):
            List of output variables of this root module.
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    components: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    dependencies: MutableSequence["RootModuleDependency"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="RootModuleDependency",
    )
    input_variables: MutableSequence["RootInputVariable"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="RootInputVariable",
    )
    output_variables: MutableSequence["RootOutputVariable"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="RootOutputVariable",
    )


class RootModuleDependency(proto.Message):
    r"""Root module dependency.

    Attributes:
        root_module_id (str):
            Identifier of the root module.
        parameters (MutableSequence[google.cloud.designcenter_v1.types.Parameter]):
            Parameters associated with this dependency.
    """

    root_module_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    parameters: MutableSequence[gcd_parameters.Parameter] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=gcd_parameters.Parameter,
    )


class RootInputVariable(proto.Message):
    r"""Input variable of a root module.

    Attributes:
        variable (str):
            Name of the input variable.
        variable_type (str):
            Type of the input variable.
        value (google.protobuf.struct_pb2.Value):
            Value for the input variable.
        default_value (google.protobuf.struct_pb2.Value):
            Default value of the input variable.
        alias (str):
            Alias for the variable name.
    """

    variable: str = proto.Field(
        proto.STRING,
        number=1,
    )
    variable_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    value: struct_pb2.Value = proto.Field(
        proto.MESSAGE,
        number=3,
        message=struct_pb2.Value,
    )
    default_value: struct_pb2.Value = proto.Field(
        proto.MESSAGE,
        number=4,
        message=struct_pb2.Value,
    )
    alias: str = proto.Field(
        proto.STRING,
        number=5,
    )


class RootOutputVariable(proto.Message):
    r"""Output variable of a root module.

    Attributes:
        variable (str):
            Name of the output variable.
    """

    variable: str = proto.Field(
        proto.STRING,
        number=1,
    )


class TerraformModule(proto.Message):
    r"""Represents a Terraform module, which is a collection of Terraform
    files. Eg: { "source": "git::https://github.com/my-org/my-repo",
    "files": [ { "path": "/path/to/file/main.tf", "content": "tf file
    content" } ] }

    Attributes:
        source (str):
            The source of the Terraform module.
        files (MutableSequence[google.cloud.designcenter_v1.types.TerraformFile]):
            The files within the Terraform module.
    """

    source: str = proto.Field(
        proto.STRING,
        number=1,
    )
    files: MutableSequence["TerraformFile"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="TerraformFile",
    )


class TerraformFile(proto.Message):
    r"""Represents a single Terraform file.

    Attributes:
        path (str):
            The path of the Terraform file.
        content (str):
            The content of the Terraform file.
    """

    path: str = proto.Field(
        proto.STRING,
        number=1,
    )
    content: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
