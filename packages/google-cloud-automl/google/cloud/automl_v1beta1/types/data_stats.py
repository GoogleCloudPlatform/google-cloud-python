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
    package="google.cloud.automl.v1beta1",
    manifest={
        "DataStats",
        "Float64Stats",
        "StringStats",
        "TimestampStats",
        "ArrayStats",
        "StructStats",
        "CategoryStats",
        "CorrelationStats",
    },
)


class DataStats(proto.Message):
    r"""The data statistics of a series of values that share the same
    DataType.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        float64_stats (google.cloud.automl_v1beta1.types.Float64Stats):
            The statistics for FLOAT64 DataType.

            This field is a member of `oneof`_ ``stats``.
        string_stats (google.cloud.automl_v1beta1.types.StringStats):
            The statistics for STRING DataType.

            This field is a member of `oneof`_ ``stats``.
        timestamp_stats (google.cloud.automl_v1beta1.types.TimestampStats):
            The statistics for TIMESTAMP DataType.

            This field is a member of `oneof`_ ``stats``.
        array_stats (google.cloud.automl_v1beta1.types.ArrayStats):
            The statistics for ARRAY DataType.

            This field is a member of `oneof`_ ``stats``.
        struct_stats (google.cloud.automl_v1beta1.types.StructStats):
            The statistics for STRUCT DataType.

            This field is a member of `oneof`_ ``stats``.
        category_stats (google.cloud.automl_v1beta1.types.CategoryStats):
            The statistics for CATEGORY DataType.

            This field is a member of `oneof`_ ``stats``.
        distinct_value_count (int):
            The number of distinct values.
        null_value_count (int):
            The number of values that are null.
        valid_value_count (int):
            The number of values that are valid.
    """

    float64_stats: "Float64Stats" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="stats",
        message="Float64Stats",
    )
    string_stats: "StringStats" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="stats",
        message="StringStats",
    )
    timestamp_stats: "TimestampStats" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="stats",
        message="TimestampStats",
    )
    array_stats: "ArrayStats" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="stats",
        message="ArrayStats",
    )
    struct_stats: "StructStats" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="stats",
        message="StructStats",
    )
    category_stats: "CategoryStats" = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="stats",
        message="CategoryStats",
    )
    distinct_value_count: int = proto.Field(
        proto.INT64,
        number=1,
    )
    null_value_count: int = proto.Field(
        proto.INT64,
        number=2,
    )
    valid_value_count: int = proto.Field(
        proto.INT64,
        number=9,
    )


class Float64Stats(proto.Message):
    r"""The data statistics of a series of FLOAT64 values.

    Attributes:
        mean (float):
            The mean of the series.
        standard_deviation (float):
            The standard deviation of the series.
        quantiles (MutableSequence[float]):
            Ordered from 0 to k k-quantile values of the data series of
            n values. The value at index i is, approximately, the
            i*n/k-th smallest value in the series; for i = 0 and i = k
            these are, respectively, the min and max values.
        histogram_buckets (MutableSequence[google.cloud.automl_v1beta1.types.Float64Stats.HistogramBucket]):
            Histogram buckets of the data series. Sorted by the min
            value of the bucket, ascendingly, and the number of the
            buckets is dynamically generated. The buckets are
            non-overlapping and completely cover whole FLOAT64 range
            with min of first bucket being ``"-Infinity"``, and max of
            the last one being ``"Infinity"``.
    """

    class HistogramBucket(proto.Message):
        r"""A bucket of a histogram.

        Attributes:
            min_ (float):
                The minimum value of the bucket, inclusive.
            max_ (float):
                The maximum value of the bucket, exclusive unless max =
                ``"Infinity"``, in which case it's inclusive.
            count (int):
                The number of data values that are in the
                bucket, i.e. are between min and max values.
        """

        min_: float = proto.Field(
            proto.DOUBLE,
            number=1,
        )
        max_: float = proto.Field(
            proto.DOUBLE,
            number=2,
        )
        count: int = proto.Field(
            proto.INT64,
            number=3,
        )

    mean: float = proto.Field(
        proto.DOUBLE,
        number=1,
    )
    standard_deviation: float = proto.Field(
        proto.DOUBLE,
        number=2,
    )
    quantiles: MutableSequence[float] = proto.RepeatedField(
        proto.DOUBLE,
        number=3,
    )
    histogram_buckets: MutableSequence[HistogramBucket] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=HistogramBucket,
    )


class StringStats(proto.Message):
    r"""The data statistics of a series of STRING values.

    Attributes:
        top_unigram_stats (MutableSequence[google.cloud.automl_v1beta1.types.StringStats.UnigramStats]):
            The statistics of the top 20 unigrams, ordered by
            [count][google.cloud.automl.v1beta1.StringStats.UnigramStats.count].
    """

    class UnigramStats(proto.Message):
        r"""The statistics of a unigram.

        Attributes:
            value (str):
                The unigram.
            count (int):
                The number of occurrences of this unigram in
                the series.
        """

        value: str = proto.Field(
            proto.STRING,
            number=1,
        )
        count: int = proto.Field(
            proto.INT64,
            number=2,
        )

    top_unigram_stats: MutableSequence[UnigramStats] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=UnigramStats,
    )


class TimestampStats(proto.Message):
    r"""The data statistics of a series of TIMESTAMP values.

    Attributes:
        granular_stats (MutableMapping[str, google.cloud.automl_v1beta1.types.TimestampStats.GranularStats]):
            The string key is the pre-defined granularity. Currently
            supported: hour_of_day, day_of_week, month_of_year.
            Granularities finer that the granularity of timestamp data
            are not populated (e.g. if timestamps are at day
            granularity, then hour_of_day is not populated).
    """

    class GranularStats(proto.Message):
        r"""Stats split by a defined in context granularity.

        Attributes:
            buckets (MutableMapping[int, int]):
                A map from granularity key to example count for that key.
                E.g. for hour_of_day ``13`` means 1pm, or for month_of_year
                ``5`` means May).
        """

        buckets: MutableMapping[int, int] = proto.MapField(
            proto.INT32,
            proto.INT64,
            number=1,
        )

    granular_stats: MutableMapping[str, GranularStats] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=1,
        message=GranularStats,
    )


class ArrayStats(proto.Message):
    r"""The data statistics of a series of ARRAY values.

    Attributes:
        member_stats (google.cloud.automl_v1beta1.types.DataStats):
            Stats of all the values of all arrays, as if
            they were a single long series of data. The type
            depends on the element type of the array.
    """

    member_stats: "DataStats" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DataStats",
    )


class StructStats(proto.Message):
    r"""The data statistics of a series of STRUCT values.

    Attributes:
        field_stats (MutableMapping[str, google.cloud.automl_v1beta1.types.DataStats]):
            Map from a field name of the struct to data
            stats aggregated over series of all data in that
            field across all the structs.
    """

    field_stats: MutableMapping[str, "DataStats"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=1,
        message="DataStats",
    )


class CategoryStats(proto.Message):
    r"""The data statistics of a series of CATEGORY values.

    Attributes:
        top_category_stats (MutableSequence[google.cloud.automl_v1beta1.types.CategoryStats.SingleCategoryStats]):
            The statistics of the top 20 CATEGORY values, ordered by

            [count][google.cloud.automl.v1beta1.CategoryStats.SingleCategoryStats.count].
    """

    class SingleCategoryStats(proto.Message):
        r"""The statistics of a single CATEGORY value.

        Attributes:
            value (str):
                The CATEGORY value.
            count (int):
                The number of occurrences of this value in
                the series.
        """

        value: str = proto.Field(
            proto.STRING,
            number=1,
        )
        count: int = proto.Field(
            proto.INT64,
            number=2,
        )

    top_category_stats: MutableSequence[SingleCategoryStats] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=SingleCategoryStats,
    )


class CorrelationStats(proto.Message):
    r"""A correlation statistics between two series of DataType
    values. The series may have differing DataType-s, but within a
    single series the DataType must be the same.

    Attributes:
        cramers_v (float):
            The correlation value using the Cramer's V
            measure.
    """

    cramers_v: float = proto.Field(
        proto.DOUBLE,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
