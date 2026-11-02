# Copyright (c) 2017 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import pandas_gbq

# Select a few KB worth of data, to time downloading small result sets.
df = pandas_gbq.read_gbq(
    "SELECT * FROM `bigquery-public-data.utility_us.country_code_iso`",
    dialect="standard",
)
