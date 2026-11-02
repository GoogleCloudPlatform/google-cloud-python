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
    package="google.maps.routing.v2",
    manifest={
        "PolylineQuality",
        "PolylineEncoding",
        "Polyline",
    },
)


class PolylineQuality(proto.Enum):
    r"""A set of values that specify the quality of the polyline.

    Values:
        POLYLINE_QUALITY_UNSPECIFIED (0):
            No polyline quality preference specified. Defaults to
            ``OVERVIEW``.
        HIGH_QUALITY (1):
            Specifies a high-quality polyline - which is composed using
            more points than ``OVERVIEW``, at the cost of increased
            response size. Use this value when you need more precision.
        OVERVIEW (2):
            Specifies an overview polyline - which is composed using a
            small number of points. Use this value when displaying an
            overview of the route. Using this option has a lower request
            latency compared to using the ``HIGH_QUALITY`` option.
    """

    POLYLINE_QUALITY_UNSPECIFIED = 0
    HIGH_QUALITY = 1
    OVERVIEW = 2


class PolylineEncoding(proto.Enum):
    r"""Specifies the preferred type of polyline to be returned.

    Values:
        POLYLINE_ENCODING_UNSPECIFIED (0):
            No polyline type preference specified. Defaults to
            ``ENCODED_POLYLINE``.
        ENCODED_POLYLINE (1):
            Specifies a polyline encoded using the `polyline encoding
            algorithm </maps/documentation/utilities/polylinealgorithm>`__.
        GEO_JSON_LINESTRING (2):
            Specifies a polyline using the `GeoJSON LineString
            format <https://tools.ietf.org/html/rfc7946#section-3.1.4>`__
    """

    POLYLINE_ENCODING_UNSPECIFIED = 0
    ENCODED_POLYLINE = 1
    GEO_JSON_LINESTRING = 2


class Polyline(proto.Message):
    r"""Encapsulates an encoded polyline.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        encoded_polyline (str):
            The string encoding of the polyline using the `polyline
            encoding
            algorithm <https://developers.google.com/maps/documentation/utilities/polylinealgorithm>`__

            This field is a member of `oneof`_ ``polyline_type``.
        geo_json_linestring (google.protobuf.struct_pb2.Struct):
            Specifies a polyline using the `GeoJSON LineString
            format <https://tools.ietf.org/html/rfc7946#section-3.1.4>`__.

            This field is a member of `oneof`_ ``polyline_type``.
    """

    encoded_polyline: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="polyline_type",
    )
    geo_json_linestring: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="polyline_type",
        message=struct_pb2.Struct,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
