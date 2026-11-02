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

import google.api.distribution_pb2 as distribution_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.api.servicecontrol.v1",
    manifest={
        "Distribution",
    },
)


class Distribution(proto.Message):
    r"""Distribution represents a frequency distribution of double-valued
    sample points. It contains the size of the population of sample
    points plus additional optional information:

    - the arithmetic mean of the samples
    - the minimum and maximum of the samples
    - the sum-squared-deviation of the samples, used to compute variance
    - a histogram of the values of the sample points

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        count (int):
            The total number of samples in the
            distribution. Must be >= 0.
        mean (float):
            The arithmetic mean of the samples in the distribution. If
            ``count`` is zero then this field must be zero.
        minimum (float):
            The minimum of the population of values. Ignored if
            ``count`` is zero.
        maximum (float):
            The maximum of the population of values. Ignored if
            ``count`` is zero.
        sum_of_squared_deviation (float):
            The sum of squared deviations from the mean:
            Sum[i=1..count]((x_i - mean)^2) where each x_i is a sample
            values. If ``count`` is zero then this field must be zero,
            otherwise validation of the request fails.
        bucket_counts (MutableSequence[int]):
            The number of samples in each histogram bucket.
            ``bucket_counts`` are optional. If present, they must sum to
            the ``count`` value.

            The buckets are defined below in ``bucket_option``. There
            are N buckets. ``bucket_counts[0]`` is the number of samples
            in the underflow bucket. ``bucket_counts[1]`` to
            ``bucket_counts[N-1]`` are the numbers of samples in each of
            the finite buckets. And ``bucket_counts[N]`` is the number
            of samples in the overflow bucket. See the comments of
            ``bucket_option`` below for more details.

            Any suffix of trailing zeros may be omitted.
        linear_buckets (google.cloud.servicecontrol_v1.types.Distribution.LinearBuckets):
            Buckets with constant width.

            This field is a member of `oneof`_ ``bucket_option``.
        exponential_buckets (google.cloud.servicecontrol_v1.types.Distribution.ExponentialBuckets):
            Buckets with exponentially growing width.

            This field is a member of `oneof`_ ``bucket_option``.
        explicit_buckets (google.cloud.servicecontrol_v1.types.Distribution.ExplicitBuckets):
            Buckets with arbitrary user-provided width.

            This field is a member of `oneof`_ ``bucket_option``.
        exemplars (MutableSequence[google.api.distribution_pb2.Exemplar]):
            Example points. Must be in increasing order of ``value``
            field.
    """

    class LinearBuckets(proto.Message):
        r"""Describing buckets with constant width.

        Attributes:
            num_finite_buckets (int):
                The number of finite buckets. With the underflow and
                overflow buckets, the total number of buckets is
                ``num_finite_buckets`` + 2. See comments on
                ``bucket_options`` for details.
            width (float):
                The i'th linear bucket covers the interval [offset + (i-1)
                \* width, offset + i \* width) where i ranges from 1 to
                num_finite_buckets, inclusive. Must be strictly positive.
            offset (float):
                The i'th linear bucket covers the interval [offset + (i-1)
                \* width, offset + i \* width) where i ranges from 1 to
                num_finite_buckets, inclusive.
        """

        num_finite_buckets: int = proto.Field(
            proto.INT32,
            number=1,
        )
        width: float = proto.Field(
            proto.DOUBLE,
            number=2,
        )
        offset: float = proto.Field(
            proto.DOUBLE,
            number=3,
        )

    class ExponentialBuckets(proto.Message):
        r"""Describing buckets with exponentially growing width.

        Attributes:
            num_finite_buckets (int):
                The number of finite buckets. With the underflow and
                overflow buckets, the total number of buckets is
                ``num_finite_buckets`` + 2. See comments on
                ``bucket_options`` for details.
            growth_factor (float):
                The i'th exponential bucket covers the interval [scale \*
                growth_factor^(i-1), scale \* growth_factor^i) where i
                ranges from 1 to num_finite_buckets inclusive. Must be
                larger than 1.0.
            scale (float):
                The i'th exponential bucket covers the interval [scale \*
                growth_factor^(i-1), scale \* growth_factor^i) where i
                ranges from 1 to num_finite_buckets inclusive. Must be > 0.
        """

        num_finite_buckets: int = proto.Field(
            proto.INT32,
            number=1,
        )
        growth_factor: float = proto.Field(
            proto.DOUBLE,
            number=2,
        )
        scale: float = proto.Field(
            proto.DOUBLE,
            number=3,
        )

    class ExplicitBuckets(proto.Message):
        r"""Describing buckets with arbitrary user-provided width.

        Attributes:
            bounds (MutableSequence[float]):
                'bound' is a list of strictly increasing boundaries between
                buckets. Note that a list of length N-1 defines N buckets
                because of fenceposting. See comments on ``bucket_options``
                for details.

                The i'th finite bucket covers the interval [bound[i-1],
                bound[i]) where i ranges from 1 to bound_size() - 1. Note
                that there are no finite buckets at all if 'bound' only
                contains a single element; in that special case the single
                bound defines the boundary between the underflow and
                overflow buckets.

                bucket number lower bound upper bound i == 0 (underflow)
                -inf bound[i] 0 < i < bound_size() bound[i-1] bound[i] i ==
                bound_size() (overflow) bound[i-1] +inf
        """

        bounds: MutableSequence[float] = proto.RepeatedField(
            proto.DOUBLE,
            number=1,
        )

    count: int = proto.Field(
        proto.INT64,
        number=1,
    )
    mean: float = proto.Field(
        proto.DOUBLE,
        number=2,
    )
    minimum: float = proto.Field(
        proto.DOUBLE,
        number=3,
    )
    maximum: float = proto.Field(
        proto.DOUBLE,
        number=4,
    )
    sum_of_squared_deviation: float = proto.Field(
        proto.DOUBLE,
        number=5,
    )
    bucket_counts: MutableSequence[int] = proto.RepeatedField(
        proto.INT64,
        number=6,
    )
    linear_buckets: LinearBuckets = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="bucket_option",
        message=LinearBuckets,
    )
    exponential_buckets: ExponentialBuckets = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="bucket_option",
        message=ExponentialBuckets,
    )
    explicit_buckets: ExplicitBuckets = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="bucket_option",
        message=ExplicitBuckets,
    )
    exemplars: MutableSequence[distribution_pb2.Distribution.Exemplar] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=10,
            message=distribution_pb2.Distribution.Exemplar,
        )
    )


__all__ = tuple(sorted(__protobuf__.manifest))
