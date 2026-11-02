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
    package="google.cloud.contentwarehouse.v1",
    manifest={
        "HistogramQuery",
        "HistogramQueryPropertyNameFilter",
        "HistogramQueryResult",
    },
)


class HistogramQuery(proto.Message):
    r"""The histogram request.

    Attributes:
        histogram_query (str):
            An expression specifies a histogram request against matching
            documents for searches.

            See
            [SearchDocumentsRequest.histogram_queries][google.cloud.contentwarehouse.v1.SearchDocumentsRequest.histogram_queries]
            for details about syntax.
        require_precise_result_size (bool):
            Controls if the histogram query requires the
            return of a precise count. Enable this flag may
            adversely impact performance.

            Defaults to true.
        filters (google.cloud.contentwarehouse_v1.types.HistogramQueryPropertyNameFilter):
            Optional. Filter the result of histogram
            query by the property names. It only works with
            histogram query count('FilterableProperties').
            It is an optional. It will perform histogram on
            all the property names for all the document
            schemas. Setting this field will have a better
            performance.
    """

    histogram_query: str = proto.Field(
        proto.STRING,
        number=1,
    )
    require_precise_result_size: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    filters: "HistogramQueryPropertyNameFilter" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="HistogramQueryPropertyNameFilter",
    )


class HistogramQueryPropertyNameFilter(proto.Message):
    r"""

    Attributes:
        document_schemas (MutableSequence[str]):
            This filter specifies the exact document schema(s)
            [Document.document_schema_name][google.cloud.contentwarehouse.v1.Document.document_schema_name]
            to run histogram query against. It is optional. It will
            perform histogram for property names for all the document
            schemas if it is not set.

            At most 10 document schema names are allowed. Format:
            projects/{project_number}/locations/{location}/documentSchemas/{document_schema_id}.
        property_names (MutableSequence[str]):
            It is optional. It will perform histogram for all the
            property names if it is not set. The properties need to be
            defined with the is_filterable flag set to true and the name
            of the property should be in the format:
            "schemaId.propertyName". The property needs to be defined in
            the schema. Example: the schema id is abc. Then the name of
            property for property MORTGAGE_TYPE will be
            "abc.MORTGAGE_TYPE".
        y_axis (google.cloud.contentwarehouse_v1.types.HistogramQueryPropertyNameFilter.HistogramYAxis):
            By default, the y_axis is HISTOGRAM_YAXIS_DOCUMENT if this
            field is not set.
    """

    class HistogramYAxis(proto.Enum):
        r"""The result of the histogram query count('FilterableProperties')
        using HISTOGRAM_YAXIS_DOCUMENT will be: invoice_id: 2 address: 1
        payment_method: 2 line_item_description: 1

        Values:
            HISTOGRAM_YAXIS_DOCUMENT (0):
                Count the documents per property name.
            HISTOGRAM_YAXIS_PROPERTY (1):
                Count the properties per property name.
        """

        HISTOGRAM_YAXIS_DOCUMENT = 0
        HISTOGRAM_YAXIS_PROPERTY = 1

    document_schemas: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    property_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    y_axis: HistogramYAxis = proto.Field(
        proto.ENUM,
        number=3,
        enum=HistogramYAxis,
    )


class HistogramQueryResult(proto.Message):
    r"""Histogram result that matches
    [HistogramQuery][google.cloud.contentwarehouse.v1.HistogramQuery]
    specified in searches.

    Attributes:
        histogram_query (str):
            Requested histogram expression.
        histogram (MutableMapping[str, int]):
            A map from the values of the facet associated with distinct
            values to the number of matching entries with corresponding
            value.

            The key format is:

            - (for string histogram) string values stored in the field.
    """

    histogram_query: str = proto.Field(
        proto.STRING,
        number=1,
    )
    histogram: MutableMapping[str, int] = proto.MapField(
        proto.STRING,
        proto.INT64,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
