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

__protobuf__ = proto.module(
    package="google.shopping.merchant.productstudio.v1alpha",
    manifest={
        "GenerateProductTextSuggestionsRequest",
        "GenerateProductTextSuggestionsResponse",
        "TitleExample",
        "ProductTextGenerationMetadata",
        "Image",
        "ProductInfo",
        "OutputSpec",
        "ProductTextGenerationSuggestion",
    },
)


class GenerateProductTextSuggestionsRequest(proto.Message):
    r"""Request message for the GenerateProductTextSuggestions
    method.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. The name of the account to generate
            text suggestions for. This acts as a container
            for the request and does not affect the
            generation itself, as this is a stateless API.
            Format: accounts/{account}
        product_info (google.shopping.merchant_productstudio_v1alpha.types.ProductInfo):
            Required. Available information about the
            product. Used to inform the genAI models.
        output_spec (google.shopping.merchant_productstudio_v1alpha.types.OutputSpec):
            Optional. Configuration parameters that
            directly influence what content is generated,
            and how that content is rendered in the final
            response.

            This field is a member of `oneof`_ ``_output_spec``.
        title_examples (MutableSequence[google.shopping.merchant_productstudio_v1alpha.types.TitleExample]):
            Optional. Provide some hand-crafted examples
            of title improvements that are unique to your
            use case. This is a general tool that handles
            multiple product categories, but your brand
            identity may require custom functionality. Feel
            free to specify that here.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    product_info: "ProductInfo" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ProductInfo",
    )
    output_spec: "OutputSpec" = proto.Field(
        proto.MESSAGE,
        number=3,
        optional=True,
        message="OutputSpec",
    )
    title_examples: MutableSequence["TitleExample"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="TitleExample",
    )


class GenerateProductTextSuggestionsResponse(proto.Message):
    r"""Response message for the GenerateProductTextSuggestions
    method.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        title (google.shopping.merchant_productstudio_v1alpha.types.ProductTextGenerationSuggestion):
            Generated title suggestion.

            This field is a member of `oneof`_ ``_title``.
        description (google.shopping.merchant_productstudio_v1alpha.types.ProductTextGenerationSuggestion):
            Generated description suggestion.

            This field is a member of `oneof`_ ``_description``.
        attributes (MutableMapping[str, str]):
            Any other generated attributes.
        metadata (google.shopping.merchant_productstudio_v1alpha.types.ProductTextGenerationMetadata):
            Additional info that clients may want to
            audit surrounding the generation.

            This field is a member of `oneof`_ ``_metadata``.
    """

    title: "ProductTextGenerationSuggestion" = proto.Field(
        proto.MESSAGE,
        number=1,
        optional=True,
        message="ProductTextGenerationSuggestion",
    )
    description: "ProductTextGenerationSuggestion" = proto.Field(
        proto.MESSAGE,
        number=2,
        optional=True,
        message="ProductTextGenerationSuggestion",
    )
    attributes: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )
    metadata: "ProductTextGenerationMetadata" = proto.Field(
        proto.MESSAGE,
        number=4,
        optional=True,
        message="ProductTextGenerationMetadata",
    )


class TitleExample(proto.Message):
    r"""A hand-crafted example of a product title improvement. These
    examples are provided to the AI to improve its quality and guide
    it towards required outputs.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        product_info (MutableMapping[str, str]):
            Required. A map containing all existing
            product information. For example: {"title":
            "dress", "description": "A red dress", "brand":
            "Dresses4All"} Any information that you might
            use to populate your product feed.
        category (str):
            Required. The product's category. This helps
            the AI understand when certain examples are more
            relevant than others.

            This field is a member of `oneof`_ ``_category``.
        title_format (str):
            Required. The attributes or approximate attributes that make
            up the title. For example, title "Google GShoe M"
            title_format can be "brand \| product \| size".

            This field is a member of `oneof`_ ``_title_format``.
        final_product_info (MutableMapping[str, str]):
            Required. A map in the same format as product_info but with
            all improvements included. For example, {"brand":
            "Dresses4All", "product": "dress", "color": "red", ...}. The
            order of attributes in this map may be used to guide the
            order in which they appear in the final generated title. For
            instance, the above will become: Dresses4All dress \| red
    """

    product_info: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=1,
    )
    category: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    title_format: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    final_product_info: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )


class ProductTextGenerationMetadata(proto.Message):
    r"""Wrapper data type for any metadata associated with text
    generation.

    Attributes:
        metadata (google.protobuf.struct_pb2.Struct):
            Metadata is a pretty loose concept. The data
            is modeled as a map here to indicate that there
            is no guaranteed structure to the output past a
            simple K:V association.
            The first use-case is to track words
            added/removed/changed in generations.
    """

    metadata: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=1,
        message=struct_pb2.Struct,
    )


class Image(proto.Message):
    r"""Product image represented as bytes directly or a URI.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        uri (str):
            Generally web-requestable URI.

            This field is a member of `oneof`_ ``image``.
        data (bytes):
            Raw bytes for the image.

            This field is a member of `oneof`_ ``image``.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="image",
    )
    data: bytes = proto.Field(
        proto.BYTES,
        number=2,
        oneof="image",
    )


class ProductInfo(proto.Message):
    r"""Available information about the product. Used to inform the
    genAI models.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        product_attributes (MutableMapping[str, str]):
            Required. A mapping of all available product
            attributes. This may include title, description,
            brand, gender, color, size, etc.
        product_image (google.shopping.merchant_productstudio_v1alpha.types.Image):
            Optional. Image associated with the product.

            This field is a member of `oneof`_ ``_product_image``.
    """

    product_attributes: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=1,
    )
    product_image: "Image" = proto.Field(
        proto.MESSAGE,
        number=2,
        optional=True,
        message="Image",
    )


class OutputSpec(proto.Message):
    r"""Configuration parameters that directly influence what content
    is generated, and how that content is rendered in the final
    response.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        workflow_id (str):
            Optional. The workflow to execute for the provided product
            data. Workflows may populate the response's title,
            description, or both. Currently supported workflow_ids are:
            "title", "description", and "tide".

            This field is a member of `oneof`_ ``_workflow_id``.
        tone (str):
            Optional. The tone of the output generated
            text. Supported tones are: "playful", "formal",
            "persuasive", and "conversational".

            This field is a member of `oneof`_ ``_tone``.
        editorial_changes (str):
            Optional. Any editorial changes for the
            generated product data. For example, replace
            Small with "S", do not modify color if already
            present.

            This field is a member of `oneof`_ ``_editorial_changes``.
        target_language (str):
            Optional. The language for output
            titles/descriptions. For example. 'German',
            'es', 'FR'. Default is 'en'.

            This field is a member of `oneof`_ ``_target_language``.
        attribute_order (MutableSequence[str]):
            Optional. The order that generated attributes should be
            placed in the generated title. Eg., if the attribute order
            is ["brand", "product", "size"], the generated title will
            have brand first, followed by the product name, and then
            size information after that.
        attribute_separator (str):
            Optional. Character used to separate attributes in the
            generated title. For example, '\|', '-', ','.

            This field is a member of `oneof`_ ``_attribute_separator``.
    """

    workflow_id: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    tone: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    editorial_changes: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    target_language: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    attribute_order: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    attribute_separator: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )


class ProductTextGenerationSuggestion(proto.Message):
    r"""Text generated for a product, optionally including its
    quality score.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        text (str):
            The text generated

            This field is a member of `oneof`_ ``_text``.
        score (float):
            The quality score associated with the
            generation. Heuristic implemented according to
            the feedgen team's implementation styles.

            This field is a member of `oneof`_ ``_score``.
        change_summary (str):
            A brief summarization of all the changes that
            have been made.

            This field is a member of `oneof`_ ``_change_summary``.
    """

    text: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    score: float = proto.Field(
        proto.FLOAT,
        number=2,
        optional=True,
    )
    change_summary: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
