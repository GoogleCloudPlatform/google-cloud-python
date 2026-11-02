# Copyright (c) 2017 The sqlalchemy-bigquery Authors
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
SQLAlchemy dialect for Google BigQuery
"""

import sys
import warnings

from ._types import (
    ARRAY,
    BIGNUMERIC,
    BOOL,
    BOOLEAN,
    BYTES,
    DATE,
    DATETIME,
    FLOAT,
    FLOAT64,
    INT64,
    INTEGER,
    NUMERIC,
    RECORD,
    STRING,
    STRUCT,
    TIME,
    TIMESTAMP,
)
from .base import BigQueryDialect, dialect
from .version import __version__

# Now that support for Python 3.7, 3.8 and 3.9 has been removed, we don't expect the
# following check to succeed. The warning is only included for robustness.
if sys.version_info < (3, 10):  # pragma: NO COVER
    warnings.warn(
        "The python-bigquery-sqlalchemy library no longer supports Python 3.7, "
        "3.8 and 3.9. "
        f"Your Python version is {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}. We "
        "recommend that you update soon to ensure ongoing support. For "
        "more details, see: [Google Cloud Client Libraries Supported Python Versions policy](https://cloud.google.com/python/docs/supported-python-versions)",
        FutureWarning,
    )


__all__ = [
    "__version__",
    "dialect",
    "ARRAY",
    "BIGNUMERIC",
    "BigQueryDialect",
    "BOOL",
    "BOOLEAN",
    "BYTES",
    "DATE",
    "DATETIME",
    "FLOAT",
    "FLOAT64",
    "INT64",
    "INTEGER",
    "NUMERIC",
    "RECORD",
    "STRING",
    "STRUCT",
    "TIME",
    "TIMESTAMP",
]

try:
    from .geography import GEOGRAPHY, WKB, WKT  # noqa
except ImportError:  # pragma: NO COVER
    pass
else:
    __all__.extend(["GEOGRAPHY", "WKB", "WKT"])

try:
    import pybigquery  # noqa
except ImportError:
    pass
else:  # pragma: NO COVER
    import warnings

    warnings.warn(
        "Obsolete pybigquery is installed, which is likely to\n"
        "interfere with sqlalchemy_bigquery.\n"
        "pybigquery should be uninstalled.",
        stacklevel=2,
    )
