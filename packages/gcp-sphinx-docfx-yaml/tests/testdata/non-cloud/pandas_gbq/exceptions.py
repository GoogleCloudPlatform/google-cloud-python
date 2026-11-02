# Copyright (c) 2017 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


class GenericGBQException(ValueError):
    """
    Raised when an unrecognized Google API Error occurs.
    """


class AccessDenied(ValueError):
    """
    Raised when invalid credentials are provided, or tokens have expired.
    """


class ConversionError(GenericGBQException):
    """
    Raised when there is a problem converting the DataFrame to a format
    required to upload it to BigQuery.
    """


class InvalidPrivateKeyFormat(ValueError):
    """
    Raised when provided private key has invalid format.
    """


class PerformanceWarning(RuntimeWarning):
    """
    Raised when a performance-related feature is requested, but unsupported.

    Such warnings can occur when dependencies for the requested feature
    aren't up-to-date.
    """
