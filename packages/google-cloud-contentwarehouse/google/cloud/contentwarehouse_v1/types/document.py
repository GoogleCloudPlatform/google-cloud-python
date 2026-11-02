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
import google.type.datetime_pb2 as datetime_pb2  # type: ignore
import proto  # type: ignore
from google.cloud.documentai_v1.types import document as gcd_document

__protobuf__ = proto.module(
    package="google.cloud.contentwarehouse.v1",
    manifest={
        "RawDocumentFileType",
        "ContentCategory",
        "Document",
        "DocumentReference",
        "Property",
        "IntegerArray",
        "FloatArray",
        "TextArray",
        "EnumArray",
        "DateTimeArray",
        "TimestampArray",
        "TimestampValue",
        "PropertyArray",
        "MapProperty",
        "Value",
        "EnumValue",
    },
)


class RawDocumentFileType(proto.Enum):
    r"""When a raw document is supplied, this indicates the file
    format

    Values:
        RAW_DOCUMENT_FILE_TYPE_UNSPECIFIED (0):
            No raw document specified or it is
            non-parsable
        RAW_DOCUMENT_FILE_TYPE_PDF (1):
            Adobe PDF format
        RAW_DOCUMENT_FILE_TYPE_DOCX (2):
            Microsoft Word format
        RAW_DOCUMENT_FILE_TYPE_XLSX (3):
            Microsoft Excel format
        RAW_DOCUMENT_FILE_TYPE_PPTX (4):
            Microsoft Powerpoint format
        RAW_DOCUMENT_FILE_TYPE_TEXT (5):
            UTF-8 encoded text format
        RAW_DOCUMENT_FILE_TYPE_TIFF (6):
            TIFF or TIF image file format
    """

    RAW_DOCUMENT_FILE_TYPE_UNSPECIFIED = 0
    RAW_DOCUMENT_FILE_TYPE_PDF = 1
    RAW_DOCUMENT_FILE_TYPE_DOCX = 2
    RAW_DOCUMENT_FILE_TYPE_XLSX = 3
    RAW_DOCUMENT_FILE_TYPE_PPTX = 4
    RAW_DOCUMENT_FILE_TYPE_TEXT = 5
    RAW_DOCUMENT_FILE_TYPE_TIFF = 6


class ContentCategory(proto.Enum):
    r"""When a raw document or structured content is supplied, this
    stores the content category.

    Values:
        CONTENT_CATEGORY_UNSPECIFIED (0):
            No category is specified.
        CONTENT_CATEGORY_IMAGE (1):
            Content is of image type.
        CONTENT_CATEGORY_AUDIO (2):
            Content is of audio type.
        CONTENT_CATEGORY_VIDEO (3):
            Content is of video type.
    """

    CONTENT_CATEGORY_UNSPECIFIED = 0
    CONTENT_CATEGORY_IMAGE = 1
    CONTENT_CATEGORY_AUDIO = 2
    CONTENT_CATEGORY_VIDEO = 3


class Document(proto.Message):
    r"""Defines the structure for content warehouse document proto.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            The resource name of the document. Format:
            projects/{project_number}/locations/{location}/documents/{document_id}.

            The name is ignored when creating a document.
        reference_id (str):
            The reference ID set by customers. Must be
            unique per project and location.
        display_name (str):
            Required. Display name of the document given
            by the user. This name will be displayed in the
            UI. Customer can populate this field with the
            name of the document. This differs from the
            'title' field as 'title' is optional and stores
            the top heading in the document.
        title (str):
            Title that describes the document.
            This can be the top heading or text that
            describes the document.
        display_uri (str):
            Uri to display the document, for example, in
            the UI.
        document_schema_name (str):
            The Document schema name. Format:
            projects/{project_number}/locations/{location}/documentSchemas/{document_schema_id}.
        plain_text (str):
            Other document format, such as PPTX, XLXS

            This field is a member of `oneof`_ ``structured_content``.
        cloud_ai_document (google.cloud.documentai_v1.types.Document):
            Document AI format to save the structured
            content, including OCR.

            This field is a member of `oneof`_ ``structured_content``.
        structured_content_uri (str):
            A path linked to structured content file.
        raw_document_path (str):
            Raw document file in Cloud Storage path.

            This field is a member of `oneof`_ ``raw_document``.
        inline_raw_document (bytes):
            Raw document content.

            This field is a member of `oneof`_ ``raw_document``.
        properties (MutableSequence[google.cloud.contentwarehouse_v1.types.Property]):
            List of values that are user supplied
            metadata.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the document is
            last updated.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the document is
            created.
        raw_document_file_type (google.cloud.contentwarehouse_v1.types.RawDocumentFileType):
            This is used when DocAI was not used to load the document
            and parsing/ extracting is needed for the
            inline_raw_document. For example, if inline_raw_document is
            the byte representation of a PDF file, then this should be
            set to: RAW_DOCUMENT_FILE_TYPE_PDF.
        async_enabled (bool):
            If true, makes the document visible to
            asynchronous policies and rules.
        content_category (google.cloud.contentwarehouse_v1.types.ContentCategory):
            Indicates the category (image, audio, video
            etc.) of the original content.
        text_extraction_disabled (bool):
            If true, text extraction will not be
            performed.
        text_extraction_enabled (bool):
            If true, text extraction will be performed.
        creator (str):
            The user who creates the document.
        updater (str):
            The user who lastly updates the document.
        disposition_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. If linked to a Collection with
            RetentionPolicy, the date when the document
            becomes mutable.
        legal_hold (bool):
            Output only. Indicates if the document has a
            legal hold on it.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    reference_id: str = proto.Field(
        proto.STRING,
        number=11,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    title: str = proto.Field(
        proto.STRING,
        number=18,
    )
    display_uri: str = proto.Field(
        proto.STRING,
        number=17,
    )
    document_schema_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    plain_text: str = proto.Field(
        proto.STRING,
        number=15,
        oneof="structured_content",
    )
    cloud_ai_document: gcd_document.Document = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="structured_content",
        message=gcd_document.Document,
    )
    structured_content_uri: str = proto.Field(
        proto.STRING,
        number=16,
    )
    raw_document_path: str = proto.Field(
        proto.STRING,
        number=5,
        oneof="raw_document",
    )
    inline_raw_document: bytes = proto.Field(
        proto.BYTES,
        number=6,
        oneof="raw_document",
    )
    properties: MutableSequence["Property"] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="Property",
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    raw_document_file_type: "RawDocumentFileType" = proto.Field(
        proto.ENUM,
        number=10,
        enum="RawDocumentFileType",
    )
    async_enabled: bool = proto.Field(
        proto.BOOL,
        number=12,
    )
    content_category: "ContentCategory" = proto.Field(
        proto.ENUM,
        number=20,
        enum="ContentCategory",
    )
    text_extraction_disabled: bool = proto.Field(
        proto.BOOL,
        number=19,
    )
    text_extraction_enabled: bool = proto.Field(
        proto.BOOL,
        number=21,
    )
    creator: str = proto.Field(
        proto.STRING,
        number=13,
    )
    updater: str = proto.Field(
        proto.STRING,
        number=14,
    )
    disposition_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=22,
        message=timestamp_pb2.Timestamp,
    )
    legal_hold: bool = proto.Field(
        proto.BOOL,
        number=23,
    )


class DocumentReference(proto.Message):
    r"""References to the documents.

    Attributes:
        document_name (str):
            Required. Name of the referenced document.
        display_name (str):
            display_name of the referenced document; this name does not
            need to be consistent to the display_name in the Document
            proto, depending on the ACL constraint.
        snippet (str):
            Stores the subset of the referenced
            document's content. This is useful to allow user
            peek the information of the referenced document.
        document_is_folder (bool):
            The document type of the document being
            referenced.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the document is
            last updated.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the document is
            created.
        delete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the document is
            deleted.
        document_is_retention_folder (bool):
            Document is a folder with retention policy.
        document_is_legal_hold_folder (bool):
            Document is a folder with legal hold.
    """

    document_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    snippet: str = proto.Field(
        proto.STRING,
        number=3,
    )
    document_is_folder: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    delete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    document_is_retention_folder: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    document_is_legal_hold_folder: bool = proto.Field(
        proto.BOOL,
        number=9,
    )


class Property(proto.Message):
    r"""Property of a document.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. Must match the name of a
            PropertyDefinition in the DocumentSchema.
        integer_values (google.cloud.contentwarehouse_v1.types.IntegerArray):
            Integer property values.

            This field is a member of `oneof`_ ``values``.
        float_values (google.cloud.contentwarehouse_v1.types.FloatArray):
            Float property values.

            This field is a member of `oneof`_ ``values``.
        text_values (google.cloud.contentwarehouse_v1.types.TextArray):
            String/text property values.

            This field is a member of `oneof`_ ``values``.
        enum_values (google.cloud.contentwarehouse_v1.types.EnumArray):
            Enum property values.

            This field is a member of `oneof`_ ``values``.
        property_values (google.cloud.contentwarehouse_v1.types.PropertyArray):
            Nested structured data property values.

            This field is a member of `oneof`_ ``values``.
        date_time_values (google.cloud.contentwarehouse_v1.types.DateTimeArray):
            Date time property values.
            It is not supported by CMEK compliant
            deployment.

            This field is a member of `oneof`_ ``values``.
        map_property (google.cloud.contentwarehouse_v1.types.MapProperty):
            Map property values.

            This field is a member of `oneof`_ ``values``.
        timestamp_values (google.cloud.contentwarehouse_v1.types.TimestampArray):
            Timestamp property values.
            It is not supported by CMEK compliant
            deployment.

            This field is a member of `oneof`_ ``values``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    integer_values: "IntegerArray" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="values",
        message="IntegerArray",
    )
    float_values: "FloatArray" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="values",
        message="FloatArray",
    )
    text_values: "TextArray" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="values",
        message="TextArray",
    )
    enum_values: "EnumArray" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="values",
        message="EnumArray",
    )
    property_values: "PropertyArray" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="values",
        message="PropertyArray",
    )
    date_time_values: "DateTimeArray" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="values",
        message="DateTimeArray",
    )
    map_property: "MapProperty" = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="values",
        message="MapProperty",
    )
    timestamp_values: "TimestampArray" = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="values",
        message="TimestampArray",
    )


class IntegerArray(proto.Message):
    r"""Integer values.

    Attributes:
        values (MutableSequence[int]):
            List of integer values.
    """

    values: MutableSequence[int] = proto.RepeatedField(
        proto.INT32,
        number=1,
    )


class FloatArray(proto.Message):
    r"""Float values.

    Attributes:
        values (MutableSequence[float]):
            List of float values.
    """

    values: MutableSequence[float] = proto.RepeatedField(
        proto.FLOAT,
        number=1,
    )


class TextArray(proto.Message):
    r"""String/text values.

    Attributes:
        values (MutableSequence[str]):
            List of text values.
    """

    values: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class EnumArray(proto.Message):
    r"""Enum values.

    Attributes:
        values (MutableSequence[str]):
            List of enum values.
    """

    values: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class DateTimeArray(proto.Message):
    r"""DateTime values.

    Attributes:
        values (MutableSequence[google.type.datetime_pb2.DateTime]):
            List of datetime values.
            Both OffsetDateTime and ZonedDateTime are
            supported.
    """

    values: MutableSequence[datetime_pb2.DateTime] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=datetime_pb2.DateTime,
    )


class TimestampArray(proto.Message):
    r"""Timestamp values.

    Attributes:
        values (MutableSequence[google.cloud.contentwarehouse_v1.types.TimestampValue]):
            List of timestamp values.
    """

    values: MutableSequence["TimestampValue"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="TimestampValue",
    )


class TimestampValue(proto.Message):
    r"""Timestamp value type.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        timestamp_value (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp value

            This field is a member of `oneof`_ ``value``.
        text_value (str):
            The string must represent a valid instant in UTC and is
            parsed using java.time.format.DateTimeFormatter.ISO_INSTANT.
            e.g. "2013-09-29T18:46:19Z".

            This field is a member of `oneof`_ ``value``.
    """

    timestamp_value: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="value",
        message=timestamp_pb2.Timestamp,
    )
    text_value: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="value",
    )


class PropertyArray(proto.Message):
    r"""Property values.

    Attributes:
        properties (MutableSequence[google.cloud.contentwarehouse_v1.types.Property]):
            List of property values.
    """

    properties: MutableSequence["Property"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Property",
    )


class MapProperty(proto.Message):
    r"""Map property value.
    Represents a structured entries of key value pairs, consisting
    of field names which map to dynamically typed values.

    Attributes:
        fields (MutableMapping[str, google.cloud.contentwarehouse_v1.types.Value]):
            Unordered map of dynamically typed values.
    """

    fields: MutableMapping[str, "Value"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=1,
        message="Value",
    )


class Value(proto.Message):
    r"""``Value`` represents a dynamically typed value which can be either
    be a float, a integer, a string, or a datetime value. A producer of
    value is expected to set one of these variants. Absence of any
    variant indicates an error.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        float_value (float):
            Represents a float value.

            This field is a member of `oneof`_ ``kind``.
        int_value (int):
            Represents a integer value.

            This field is a member of `oneof`_ ``kind``.
        string_value (str):
            Represents a string value.

            This field is a member of `oneof`_ ``kind``.
        enum_value (google.cloud.contentwarehouse_v1.types.EnumValue):
            Represents an enum value.

            This field is a member of `oneof`_ ``kind``.
        datetime_value (google.type.datetime_pb2.DateTime):
            Represents a datetime value.

            This field is a member of `oneof`_ ``kind``.
        timestamp_value (google.cloud.contentwarehouse_v1.types.TimestampValue):
            Represents a timestamp value.

            This field is a member of `oneof`_ ``kind``.
        boolean_value (bool):
            Represents a boolean value.

            This field is a member of `oneof`_ ``kind``.
    """

    float_value: float = proto.Field(
        proto.FLOAT,
        number=1,
        oneof="kind",
    )
    int_value: int = proto.Field(
        proto.INT32,
        number=2,
        oneof="kind",
    )
    string_value: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="kind",
    )
    enum_value: "EnumValue" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="kind",
        message="EnumValue",
    )
    datetime_value: datetime_pb2.DateTime = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="kind",
        message=datetime_pb2.DateTime,
    )
    timestamp_value: "TimestampValue" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="kind",
        message="TimestampValue",
    )
    boolean_value: bool = proto.Field(
        proto.BOOL,
        number=7,
        oneof="kind",
    )


class EnumValue(proto.Message):
    r"""Represents the string value of the enum field.

    Attributes:
        value (str):
            String value of the enum field. This must
            match defined set of enums in document schema
            using EnumTypeOptions.
    """

    value: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
