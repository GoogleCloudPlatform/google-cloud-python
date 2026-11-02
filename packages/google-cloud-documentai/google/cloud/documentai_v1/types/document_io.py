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

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.documentai.v1",
    manifest={
        "RawDocument",
        "GcsDocument",
        "GcsDocuments",
        "GcsPrefix",
        "BatchDocumentsInputConfig",
        "DocumentOutputConfig",
        "OcrConfig",
    },
)


class RawDocument(proto.Message):
    r"""Payload message of raw document content (bytes).

    Attributes:
        content (bytes):
            Inline document content.
        mime_type (str):
            An IANA MIME type (RFC6838) indicating the nature and format
            of the
            [content][google.cloud.documentai.v1.RawDocument.content].
        display_name (str):
            The display name of the document, it supports all Unicode
            characters except the following: ``*``, ``?``, ``[``, ``]``,
            ``%``, ``{``, ``}``,\ ``'``, ``\"``, ``,`` ``~``, ``=`` and
            ``:`` are reserved. If not specified, a default ID is
            generated.
    """

    content: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )
    mime_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GcsDocument(proto.Message):
    r"""Specifies a document stored on Cloud Storage.

    Attributes:
        gcs_uri (str):
            The Cloud Storage object uri.
        mime_type (str):
            An IANA MIME type (RFC6838) of the content.
    """

    gcs_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    mime_type: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GcsDocuments(proto.Message):
    r"""Specifies a set of documents on Cloud Storage.

    Attributes:
        documents (MutableSequence[google.cloud.documentai_v1.types.GcsDocument]):
            The list of documents.
    """

    documents: MutableSequence["GcsDocument"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="GcsDocument",
    )


class GcsPrefix(proto.Message):
    r"""Specifies all documents on Cloud Storage with a common
    prefix.

    Attributes:
        gcs_uri_prefix (str):
            The URI prefix.
    """

    gcs_uri_prefix: str = proto.Field(
        proto.STRING,
        number=1,
    )


class BatchDocumentsInputConfig(proto.Message):
    r"""The common config to specify a set of documents used as
    input.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_prefix (google.cloud.documentai_v1.types.GcsPrefix):
            The set of documents that match the specified Cloud Storage
            ``gcs_prefix``.

            This field is a member of `oneof`_ ``source``.
        gcs_documents (google.cloud.documentai_v1.types.GcsDocuments):
            The set of documents individually specified
            on Cloud Storage.

            This field is a member of `oneof`_ ``source``.
    """

    gcs_prefix: "GcsPrefix" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="source",
        message="GcsPrefix",
    )
    gcs_documents: "GcsDocuments" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="source",
        message="GcsDocuments",
    )


class DocumentOutputConfig(proto.Message):
    r"""Config that controls the output of documents. All documents
    will be written as a JSON file.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_output_config (google.cloud.documentai_v1.types.DocumentOutputConfig.GcsOutputConfig):
            Output config to write the results to Cloud
            Storage.

            This field is a member of `oneof`_ ``destination``.
    """

    class GcsOutputConfig(proto.Message):
        r"""The configuration used when outputting documents.

        Attributes:
            gcs_uri (str):
                The Cloud Storage uri (a directory) of the
                output.
            field_mask (google.protobuf.field_mask_pb2.FieldMask):
                Specifies which fields to include in the output documents.
                Only supports top level document and pages field so it must
                be in the form of ``{document_field_name}`` or
                ``pages.{page_field_name}``.
            sharding_config (google.cloud.documentai_v1.types.DocumentOutputConfig.GcsOutputConfig.ShardingConfig):
                Specifies the sharding config for the output
                document.
        """

        class ShardingConfig(proto.Message):
            r"""The sharding config for the output document.

            Attributes:
                pages_per_shard (int):
                    The number of pages per shard.
                pages_overlap (int):
                    The number of overlapping pages between
                    consecutive shards.
            """

            pages_per_shard: int = proto.Field(
                proto.INT32,
                number=1,
            )
            pages_overlap: int = proto.Field(
                proto.INT32,
                number=2,
            )

        gcs_uri: str = proto.Field(
            proto.STRING,
            number=1,
        )
        field_mask: field_mask_pb2.FieldMask = proto.Field(
            proto.MESSAGE,
            number=2,
            message=field_mask_pb2.FieldMask,
        )
        sharding_config: "DocumentOutputConfig.GcsOutputConfig.ShardingConfig" = (
            proto.Field(
                proto.MESSAGE,
                number=3,
                message="DocumentOutputConfig.GcsOutputConfig.ShardingConfig",
            )
        )

    gcs_output_config: GcsOutputConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="destination",
        message=GcsOutputConfig,
    )


class OcrConfig(proto.Message):
    r"""Config for Document OCR.

    Attributes:
        hints (google.cloud.documentai_v1.types.OcrConfig.Hints):
            Hints for the OCR model.
        enable_native_pdf_parsing (bool):
            Enables special handling for PDFs with
            existing text information. Results in better
            text extraction quality in such PDF inputs.
        enable_image_quality_scores (bool):
            Enables intelligent document quality scores
            after OCR. Can help with diagnosing why OCR
            responses are of poor quality for a given input.
            Adds additional latency comparable to regular
            OCR to the process call.
        advanced_ocr_options (MutableSequence[str]):
            A list of advanced OCR options to further fine-tune OCR
            behavior. Current valid values are:

            - ``legacy_layout``: a heuristics layout detection
              algorithm, which serves as an alternative to the current
              ML-based layout detection algorithm. Customers can choose
              the best suitable layout algorithm based on their
              situation.
        enable_symbol (bool):
            Includes symbol level OCR information if set
            to true.
        compute_style_info (bool):
            Turn on font identification model and return font style
            information. Deprecated, use
            [PremiumFeatures.compute_style_info][google.cloud.documentai.v1.OcrConfig.PremiumFeatures.compute_style_info]
            instead.
        disable_character_boxes_detection (bool):
            Turn off character box detector in OCR
            engine. Character box detection is enabled by
            default in OCR 2.0 (and later) processors.
        premium_features (google.cloud.documentai_v1.types.OcrConfig.PremiumFeatures):
            Configurations for premium OCR features.
    """

    class Hints(proto.Message):
        r"""Hints for OCR Engine

        Attributes:
            language_hints (MutableSequence[str]):
                List of BCP-47 language codes to use for OCR.
                In most cases, not specifying it yields the best
                results since it enables automatic language
                detection. For languages based on the Latin
                alphabet, setting hints is not needed. In rare
                cases, when the language of the text in the
                image is known, setting a hint will help get
                better results (although it will be a
                significant hindrance if the hint is wrong).
        """

        language_hints: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )

    class PremiumFeatures(proto.Message):
        r"""Configurations for premium OCR features.

        Attributes:
            enable_selection_mark_detection (bool):
                Turn on selection mark detector in OCR
                engine. Only available in OCR 2.0 (and later)
                processors.
            compute_style_info (bool):
                Turn on font identification model and return
                font style information.
            enable_math_ocr (bool):
                Turn on the model that can extract LaTeX math
                formulas.
        """

        enable_selection_mark_detection: bool = proto.Field(
            proto.BOOL,
            number=3,
        )
        compute_style_info: bool = proto.Field(
            proto.BOOL,
            number=4,
        )
        enable_math_ocr: bool = proto.Field(
            proto.BOOL,
            number=5,
        )

    hints: Hints = proto.Field(
        proto.MESSAGE,
        number=2,
        message=Hints,
    )
    enable_native_pdf_parsing: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    enable_image_quality_scores: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    advanced_ocr_options: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    enable_symbol: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    compute_style_info: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    disable_character_boxes_detection: bool = proto.Field(
        proto.BOOL,
        number=10,
    )
    premium_features: PremiumFeatures = proto.Field(
        proto.MESSAGE,
        number=11,
        message=PremiumFeatures,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
