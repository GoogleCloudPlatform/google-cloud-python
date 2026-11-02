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
    package="google.cloud.datalabeling.v1beta1",
    manifest={
        "AnnotationSpecSet",
        "AnnotationSpec",
    },
)


class AnnotationSpecSet(proto.Message):
    r"""An AnnotationSpecSet is a collection of label definitions.
    For example, in image classification tasks, you define a set of
    possible labels for images as an AnnotationSpecSet. An
    AnnotationSpecSet is immutable upon creation.

    Attributes:
        name (str):
            Output only. The AnnotationSpecSet resource name in the
            following format:

            "projects/{project_id}/annotationSpecSets/{annotation_spec_set_id}".
        display_name (str):
            Required. The display name for
            AnnotationSpecSet that you define when you
            create it. Maximum of 64 characters.
        description (str):
            Optional. User-provided description of the
            annotation specification set. The description
            can be up to 10,000 characters long.
        annotation_specs (MutableSequence[google.cloud.datalabeling_v1beta1.types.AnnotationSpec]):
            Required. The array of AnnotationSpecs that
            you define when you create the
            AnnotationSpecSet. These are the possible labels
            for the labeling task.
        blocking_resources (MutableSequence[str]):
            Output only. The names of any related
            resources that are blocking changes to the
            annotation spec set.
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
    annotation_specs: MutableSequence["AnnotationSpec"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="AnnotationSpec",
    )
    blocking_resources: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )


class AnnotationSpec(proto.Message):
    r"""Container of information related to one possible annotation that can
    be used in a labeling task. For example, an image classification
    task where images are labeled as ``dog`` or ``cat`` must reference
    an AnnotationSpec for ``dog`` and an AnnotationSpec for ``cat``.

    Attributes:
        display_name (str):
            Required. The display name of the
            AnnotationSpec. Maximum of 64 characters.
        description (str):
            Optional. User-provided description of the
            annotation specification. The description can be
            up to 10,000 characters long.
    """

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
