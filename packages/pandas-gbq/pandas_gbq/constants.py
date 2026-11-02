# Copyright (c) 2024 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import google.api_core.exceptions

# BigQuery uses powers of 2 in calculating data sizes. See:
# https://cloud.google.com/bigquery/pricing#data The documentation uses
# GiB rather than GB to disambiguate from the alternative base 10 units.
# https://en.wikipedia.org/wiki/Byte#Multiple-byte_units
BYTES_IN_KIB = 1024
BYTES_IN_MIB = 1024 * BYTES_IN_KIB
BYTES_IN_GIB = 1024 * BYTES_IN_MIB
BYTES_TO_RECOMMEND_BIGFRAMES = BYTES_IN_GIB

HTTP_ERRORS = (
    google.api_core.exceptions.ClientError,
    google.api_core.exceptions.GoogleAPIError,
)
