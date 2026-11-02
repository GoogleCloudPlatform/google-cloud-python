# Copyright (c) 2017 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import logging
import sys
import warnings

from pandas_gbq import arrow
from pandas_gbq import version as pandas_gbq_version
from pandas_gbq.contexts import Context, context
from pandas_gbq.core.sample import sample

from .gbq import read_gbq, to_gbq  # noqa

if sys.version_info < (3, 10):
    warnings.warn(
        "pandas-gbq no longer supports Python versions older than 3.10. "
        f"Your Python version is {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}. "
        "Please update to Python 3.10 or newer to ensure ongoing support. For more details, "
        "see: https://cloud.google.com/python/docs/supported-python-versions",
        FutureWarning,
    )

logger = logging.Logger(__name__)

__version__ = pandas_gbq_version.__version__

__all__ = [
    "__version__",
    "to_gbq",
    "read_gbq",
    "Context",
    "context",
    "sample",
    "arrow",
]
