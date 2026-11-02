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

from google.shopping.merchant_productstudio_v1alpha.types import productstudio_common

__protobuf__ = proto.module(
    package="google.shopping.merchant.productstudio.v1alpha",
    manifest={
        "GenerateProductImageBackgroundRequest",
        "GenerateProductImageBackgroundResponse",
        "RemoveProductImageBackgroundRequest",
        "RemoveProductImageBackgroundResponse",
        "UpscaleProductImageRequest",
        "UpscaleProductImageResponse",
        "GeneratedImage",
        "OutputImageConfig",
        "GenerateImageBackgroundConfig",
        "RemoveImageBackgroundConfig",
        "RgbColor",
    },
)


class GenerateProductImageBackgroundRequest(proto.Message):
    r"""Request message for the GenerateProductImageBackground
    method.

    Attributes:
        name (str):
            Required. The account for which to generate
            an image. This acts as a container for the
            request and does not affect the generation
            itself. Format: accounts/{account}
        output_config (google.shopping.merchant_productstudio_v1alpha.types.OutputImageConfig):
            Optional. Configuration for how the output
            image should be returned.
        input_image (google.shopping.merchant_productstudio_v1alpha.types.InputImage):
            Required. The input image.
        config (google.shopping.merchant_productstudio_v1alpha.types.GenerateImageBackgroundConfig):
            Required. Configuration parameters for the
            generation of the background.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    output_config: "OutputImageConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="OutputImageConfig",
    )
    input_image: productstudio_common.InputImage = proto.Field(
        proto.MESSAGE,
        number=3,
        message=productstudio_common.InputImage,
    )
    config: "GenerateImageBackgroundConfig" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="GenerateImageBackgroundConfig",
    )


class GenerateProductImageBackgroundResponse(proto.Message):
    r"""Response message for the GenerateProductImageBackground
    method.

    Attributes:
        generated_image (google.shopping.merchant_productstudio_v1alpha.types.GeneratedImage):
            The generated output image.
    """

    generated_image: "GeneratedImage" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="GeneratedImage",
    )


class RemoveProductImageBackgroundRequest(proto.Message):
    r"""Request message for the RemoveProductImageBackground method.

    Attributes:
        name (str):
            Required. The account for which to generate
            an image. This acts as a container for the
            request and does not affect the generation
            itself. Format: accounts/{account}
        output_config (google.shopping.merchant_productstudio_v1alpha.types.OutputImageConfig):
            Optional. Configuration for how the output
            image should be returned.
        input_image (google.shopping.merchant_productstudio_v1alpha.types.InputImage):
            Required. The input image.
        config (google.shopping.merchant_productstudio_v1alpha.types.RemoveImageBackgroundConfig):
            Optional. Configuration parameters for the
            removal of the background.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    output_config: "OutputImageConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="OutputImageConfig",
    )
    input_image: productstudio_common.InputImage = proto.Field(
        proto.MESSAGE,
        number=3,
        message=productstudio_common.InputImage,
    )
    config: "RemoveImageBackgroundConfig" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="RemoveImageBackgroundConfig",
    )


class RemoveProductImageBackgroundResponse(proto.Message):
    r"""Response message for the RemoveProductImageBackground method.

    Attributes:
        generated_image (google.shopping.merchant_productstudio_v1alpha.types.GeneratedImage):
            The generated output image.
    """

    generated_image: "GeneratedImage" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="GeneratedImage",
    )


class UpscaleProductImageRequest(proto.Message):
    r"""Request message for the UpscaleProductImage method.

    Attributes:
        name (str):
            Required. The account for which to generate
            an image. This acts as a container for the
            request and does not affect the generation
            itself. Format: accounts/{account}
        output_config (google.shopping.merchant_productstudio_v1alpha.types.OutputImageConfig):
            Optional. Configuration for how the output
            image should be returned.
        input_image (google.shopping.merchant_productstudio_v1alpha.types.InputImage):
            Required. The input image.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    output_config: "OutputImageConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="OutputImageConfig",
    )
    input_image: productstudio_common.InputImage = proto.Field(
        proto.MESSAGE,
        number=3,
        message=productstudio_common.InputImage,
    )


class UpscaleProductImageResponse(proto.Message):
    r"""Response message for the UpscaleProductImage method.

    Attributes:
        generated_image (google.shopping.merchant_productstudio_v1alpha.types.GeneratedImage):
            The generated output image.
    """

    generated_image: "GeneratedImage" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="GeneratedImage",
    )


class GeneratedImage(proto.Message):
    r"""Represents a generated image object.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        uri (str):
            Generally web-requestable URI of the generated image. This
            is a temporary URI and will expire after 6 months. A URI may
            not be populated immediately after generation. Use get or
            list api using image_id to get the URI.

            This field is a member of `oneof`_ ``image``.
        image_bytes (bytes):
            Raw bytes for the image.

            This field is a member of `oneof`_ ``image``.
        name (str):
            Identifier. The unique key for the image.
        generation_time (google.protobuf.timestamp_pb2.Timestamp):
            The timestamp when the image was generated.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="image",
    )
    image_bytes: bytes = proto.Field(
        proto.BYTES,
        number=3,
        oneof="image",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    generation_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


class OutputImageConfig(proto.Message):
    r"""Configuration for how the output image should be returned.

    Attributes:
        return_image_uri (bool):
            Optional. If true, returns the output images
            as serving uris instead of bytes.
    """

    return_image_uri: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class GenerateImageBackgroundConfig(proto.Message):
    r"""Client provided input configuration for generating the
    background.

    Attributes:
        product_description (str):
            Required. Example: "Hat on a baseball field"
            "Hat" = product description
            Description of product.
        background_description (str):
            Required. Example: "Hat on a baseball field"
            "on a baseball field" = background description
            Description of wanted background.
    """

    product_description: str = proto.Field(
        proto.STRING,
        number=1,
    )
    background_description: str = proto.Field(
        proto.STRING,
        number=2,
    )


class RemoveImageBackgroundConfig(proto.Message):
    r"""Client provided input configuration for removing the
    background.

    Attributes:
        background_color (google.shopping.merchant_productstudio_v1alpha.types.RgbColor):
            Optional. If set, the result of background
            removal will be an RGB image with this given
            color as the background, instead of an RGBA
            4-channel transparent image.
    """

    background_color: "RgbColor" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="RgbColor",
    )


class RgbColor(proto.Message):
    r"""Represents a color in RGB format.

    Attributes:
        red (int):
            Optional. Values in [0, 255].
        green (int):
            Optional. Values in [0, 255].
        blue (int):
            Optional. Values in [0, 255].
    """

    red: int = proto.Field(
        proto.INT32,
        number=1,
    )
    green: int = proto.Field(
        proto.INT32,
        number=2,
    )
    blue: int = proto.Field(
        proto.INT32,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
