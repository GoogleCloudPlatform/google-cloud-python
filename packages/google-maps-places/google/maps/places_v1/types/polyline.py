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
    package="google.maps.places.v1",
    manifest={
        "Polyline",
    },
)


class Polyline(proto.Message):
    r"""A route polyline. Only supports an `encoded
    polyline <https://developers.google.com/maps/documentation/utilities/polylinealgorithm>`__,
    which can be passed as a string and includes compression with
    minimal lossiness. This is the Routes API default output.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        encoded_polyline (str):
            An `encoded
            polyline <https://developers.google.com/maps/documentation/utilities/polylinealgorithm>`__,
            as returned by the `Routes API by
            default <https://developers.google.com/maps/documentation/routes/reference/rest/v2/TopLevel/computeRoutes#polylineencoding>`__.
            See the
            `encoder <https://developers.google.com/maps/documentation/utilities/polylineutility>`__
            and
            `decoder <https://developers.google.com/maps/documentation/routes/polylinedecoder>`__
            tools.

            This field is a member of `oneof`_ ``polyline_type``.
    """

    encoded_polyline: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="polyline_type",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
