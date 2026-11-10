# Copyright 2020 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

import datetime
import math
import re
import uuid
from decimal import Decimal

import django
import sqlparse
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils import timezone
from google.cloud.spanner_dbapi.parse_utils import DateStr, TimestampStr
from google.cloud.spanner_v1 import JsonObject

_RE_CONTROL_CHARS = re.compile(r"[\x00-\x1f\x7f]")
_NAMED_CONTROL_ESCAPES = {"\n": r"\n", "\r": r"\r", "\t": r"\t"}


def check_django_compatability(supported_django_versions):
    """
    Verify that this version of django-spanner is compatible with the installed
    version of Django. For example, django-spanner is compatible
    with Django 5.2.x and 6.0.y
    """
    from . import __version__

    if django.VERSION[:2] not in supported_django_versions:
        raise ImproperlyConfigured(
            "You must use the latest version of django-spanner {A}.{B}.x "
            "with Django {A}.{B}.y (found django-spanner {C}).".format(
                A=django.VERSION[0], B=django.VERSION[1], C=__version__
            )
        )


def add_dummy_where(sql):
    """
    Cloud Spanner requires a WHERE clause on UPDATE and DELETE statements.
    Add a dummy WHERE clause if necessary.

    :type sql: str
    :param sql: A SQL statement.

    :rtype: str
    :returns: A SQL statement with dummy WHERE clause.
    """
    if any(isinstance(token, sqlparse.sql.Where) for token in sqlparse.parse(sql)[0]):
        return sql
    return sql + " WHERE 1=1"


def _escape_control_char(match):
    ch = match.group(0)
    return _NAMED_CONTROL_ESCAPES.get(ch, f"\\x{ord(ch):02x}")


def _escape_googlesql_string(text):
    """Escape backslashes, single quotes, and ASCII control chars for GoogleSQL."""
    escaped = text.replace("\\", "\\\\").replace("'", "\\'")
    return _RE_CONTROL_CHARS.sub(_escape_control_char, escaped)


def quote_ddl_literal(value):
    """Format a Python scalar as an inline Cloud Spanner GoogleSQL DDL literal.

    Cloud Spanner ``UpdateDatabaseDdl`` statements do not accept bind
    parameters, and GoogleSQL string literals escape quotes with backslashes
    rather than SQL-standard doubled single quotes. Naive :class:`datetime.datetime`
    values convert from ``settings.TIME_ZONE`` to UTC when ``settings.USE_TZ``
    is active, matching :meth:`DatabaseOperations.adapt_datetimefield_value`.

    :type value: object
    :param value: Scalar value to inline into a DDL expression (``None``,
                  ``bool``, ``int``, ``float``, ``Decimal``, ``UUID``,
                  ``JsonObject``, ``TimestampStr``, ``DateStr``, ``str``,
                  ``bytes``/``bytearray``/``memoryview``,
                  ``datetime.datetime``, ``datetime.date``, or
                  ``datetime.time``).

    :rtype: str
    :returns: A self-contained GoogleSQL literal token safe to embed inside a
              DDL statement; ``None`` renders as ``"NULL"`` and ``UUID``
              renders as its 32-character hex ``STRING(32)`` literal.

    :raises ValueError: If ``value`` is a non-finite :class:`~decimal.Decimal`
                        (``NaN`` or ``Infinity``), which Spanner ``NUMERIC``
                        rejects.
    :raises TypeError: If ``value`` is not a supported scalar DDL literal type.
    """
    # Check bool before int, TimestampStr/DateStr before str, and datetime
    # before date to preserve subclass specificity in Python's type hierarchy.
    if isinstance(value, bool):
        return "TRUE" if value else "FALSE"
    if value is None:
        return "NULL"
    if isinstance(value, int):
        return f"{int(value):d}"
    if isinstance(value, TimestampStr):
        return f"TIMESTAMP '{_escape_googlesql_string(str(value))}'"
    if isinstance(value, DateStr):
        return f"DATE '{_escape_googlesql_string(str(value))}'"
    if isinstance(value, str):
        return f"'{_escape_googlesql_string(value)}'"
    if isinstance(value, uuid.UUID):
        return f"'{value.hex}'"
    if isinstance(value, JsonObject):
        serialized = value.serialize()
        if serialized is None:
            return "NULL"
        return f"JSON '{_escape_googlesql_string(serialized)}'"
    if isinstance(value, (bytes, bytearray, memoryview)):
        hex_escapes = "".join(f"\\x{byte:02x}" for byte in bytes(value))
        return f"b'{hex_escapes}'"
    if isinstance(value, datetime.datetime):
        if timezone.is_naive(value) and settings.configured and settings.USE_TZ:
            value = timezone.make_aware(value, timezone.get_default_timezone())
        if timezone.is_aware(value):
            value = value.astimezone(datetime.timezone.utc).replace(tzinfo=None)
        return f"TIMESTAMP '{value.isoformat()}Z'"
    if isinstance(value, datetime.date):
        return f"DATE '{value.isoformat()}'"
    if isinstance(value, datetime.time):
        # TimeField maps to Spanner TIMESTAMP prefixed with dummy date 0001-01-01.
        return f"TIMESTAMP '0001-01-01T{value.isoformat(timespec='microseconds')}Z'"
    if isinstance(value, Decimal):
        if not value.is_finite():
            raise ValueError(
                f"Spanner NUMERIC DDL literals must be finite, got {value!r}."
            )
        return f"NUMERIC '{format(value, 'f')}'"
    if isinstance(value, float):
        if math.isnan(value):
            return "CAST('NaN' AS FLOAT64)"
        if math.isinf(value):
            sign = "-" if value < 0 else ""
            return f"CAST('{sign}Infinity' AS FLOAT64)"
        return repr(float(value))
    raise TypeError(
        f"Unsupported Cloud Spanner DDL literal type: {type(value).__name__}."
    )
