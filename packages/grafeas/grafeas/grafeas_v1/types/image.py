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
    package="grafeas.v1",
    manifest={
        "Layer",
        "Fingerprint",
        "ImageNote",
        "ImageOccurrence",
    },
)


class Layer(proto.Message):
    r"""Layer holds metadata specific to a layer of a Docker image.

    Attributes:
        directive (str):
            Required. The recovered Dockerfile directive
            used to construct this layer. See
            https://docs.docker.com/engine/reference/builder/
            for more information.
        arguments (str):
            The recovered arguments to the Dockerfile
            directive.
    """

    directive: str = proto.Field(
        proto.STRING,
        number=1,
    )
    arguments: str = proto.Field(
        proto.STRING,
        number=2,
    )


class Fingerprint(proto.Message):
    r"""A set of properties that uniquely identify a given Docker
    image.

    Attributes:
        v1_name (str):
            Required. The layer ID of the final layer in
            the Docker image's v1 representation.
        v2_blob (MutableSequence[str]):
            Required. The ordered list of v2 blobs that
            represent a given image.
        v2_name (str):
            Output only. The name of the image's v2 blobs computed via:
            [bottom] := v2_blob[bottom] [N] := sha256(v2_blob[N] + " " +
            v2_name[N+1]) Only the name of the final blob is kept.
    """

    v1_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    v2_blob: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    v2_name: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ImageNote(proto.Message):
    r"""Basis describes the base image portion (Note) of the DockerImage
    relationship. Linked occurrences are derived from this or an
    equivalent image via: FROM <Basis.resource_url> Or an equivalent
    reference, e.g., a tag of the resource_url.

    Attributes:
        resource_url (str):
            Required. Immutable. The resource_url for the resource
            representing the basis of associated occurrence images.
        fingerprint (grafeas.grafeas_v1.types.Fingerprint):
            Required. Immutable. The fingerprint of the
            base image.
    """

    resource_url: str = proto.Field(
        proto.STRING,
        number=1,
    )
    fingerprint: "Fingerprint" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Fingerprint",
    )


class ImageOccurrence(proto.Message):
    r"""Details of the derived image portion of the DockerImage
    relationship. This image would be produced from a Dockerfile
    with FROM <DockerImage.Basis in attached Note>.

    Attributes:
        fingerprint (grafeas.grafeas_v1.types.Fingerprint):
            Required. The fingerprint of the derived
            image.
        distance (int):
            Output only. The number of layers by which
            this image differs from the associated image
            basis.
        layer_info (MutableSequence[grafeas.grafeas_v1.types.Layer]):
            This contains layer-specific metadata, if populated it has
            length "distance" and is ordered with [distance] being the
            layer immediately following the base image and [1] being the
            final layer.
        base_resource_url (str):
            Output only. This contains the base image URL
            for the derived image occurrence.
    """

    fingerprint: "Fingerprint" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Fingerprint",
    )
    distance: int = proto.Field(
        proto.INT32,
        number=2,
    )
    layer_info: MutableSequence["Layer"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="Layer",
    )
    base_resource_url: str = proto.Field(
        proto.STRING,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
