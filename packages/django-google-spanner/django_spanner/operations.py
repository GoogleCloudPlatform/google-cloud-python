# Copyright 2020 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

import os
import re
from base64 import b64decode
from datetime import datetime, time
from uuid import UUID

from django.conf import settings
from django.db.backends.base.operations import BaseDatabaseOperations
from django.db.utils import DatabaseError, OperationalError
from django.utils import timezone
from django.utils.duration import duration_microseconds
from django.utils.regex_helper import _lazy_re_compile
from google.cloud.spanner_dbapi.parse_utils import (
    DateStr,
    TimestampStr,
    escape_name,
)


class DatabaseOperations(BaseDatabaseOperations):
    """A Spanner-specific version of Django database operations."""

    # EXTRACT and TRUNC date parts cannot be passed as query parameters in SQL.
    # Following the practice of other Django database backends (PostgreSQL,
    # MySQL, Oracle), validate lookup types with an identifier regex to prevent
    # SQL injection while allowing custom user-registered lookups.
    extract_trunc_lookup_pattern = _lazy_re_compile(r"^[a-zA-Z_]+$")

    # Cloud Spanner only supports INT64, so all integer fields can hold
    # 64-bit values.
    integer_field_ranges = {
        "SmallIntegerField": (-9223372036854775808, 9223372036854775807),
        "IntegerField": (-9223372036854775808, 9223372036854775807),
        "BigIntegerField": (-9223372036854775808, 9223372036854775807),
        "PositiveBigIntegerField": (0, 9223372036854775807),
        "PositiveSmallIntegerField": (0, 9223372036854775807),
        "PositiveIntegerField": (0, 9223372036854775807),
        "SmallAutoField": (-9223372036854775808, 9223372036854775807),
        "AutoField": (-9223372036854775808, 9223372036854775807),
        "BigAutoField": (-9223372036854775808, 9223372036854775807),
    }

    cast_data_types = {"CharField": "STRING", "TextField": "STRING"}
    cast_char_field_without_max_length = "STRING"
    compiler_module = "django_spanner.compiler"

    def returning_columns(self, fields):
        if not fields:
            return "", ()
        columns = [
            self.quote_name(getattr(field, "column", str(field))) for field in fields
        ]
        return "THEN RETURN %s" % ", ".join(columns), ()

    # In Django <= 5.2, this method was named return_insert_columns
    return_insert_columns = returning_columns

    # Django's lookup names that require a different name in Spanner's
    # EXTRACT() function.
    # https://cloud.google.com/spanner/docs/functions-and-operators#extract
    extract_names = {
        "iso_year": "isoyear",
        "week": "isoweek",
        "week_day": "dayofweek",
    }

    # TODO: Consider changing the hardcoded output to a linked value.
    def max_name_length(self):
        """Get the maximum length of Spanner table and column names.

        See also: https://cloud.google.com/spanner/quotas#tables

        :rtype: int
        :returns: Maximum length of the name of the table.
        """
        return 128

    def quote_name(self, name):
        """
        Return a quoted version of the given table or column name. Also,
        applies backticks to the name that either contain '-' or ' ', or is a
        Cloud Spanner's reserved keyword.

        Spanner says "column name not valid" if spaces or hyphens are present
        (although according to the documantation, any character should be
        allowed in quoted identifiers). Replace problematic characters when
        running the Django tests to prevent crashes. (Don't modify names in
        normal operation to prevent the possibility of colliding with another
        column.)

        See: https://github.com/googleapis/python-spanner-django/issues/204

        :type name: str
        :param name: The Quota name.

        :rtype: :class:`str`
        :returns: Name escaped if it has to be escaped.
        """
        if os.environ.get("RUNNING_SPANNER_BACKEND_TESTS") == "1":
            name = name.replace(" ", "_").replace("-", "_")
        return escape_name(name)

    def bulk_batch_size(self, fields, objs):
        """
        Override the base class method. Returns the maximum number of objects
        that can be batched in a single query.

        :type fields: list
        :param fields: List of fields to be inserted.

        :type objs: list
        :param objs: List of objects to be inserted.

        :rtype: int
        :returns: The maximum number of objects (row counts).
        """
        max_params = self.connection.features.max_query_params
        if not fields:
            return max_params
        return max_params // len(fields)

    def bulk_insert_sql(self, fields, placeholder_rows):
        """
        A helper method that stitches multiple values into a single SQL
        record.

        :type fields: list
        :param fields: Currently not used.

        :type placeholder_rows: list
        :param placeholder_rows: Data "rows" containing values to combine.

        :rtype: str
        :returns: A SQL statement (a `VALUES` command).
        """
        placeholder_rows_sql = (", ".join(row) for row in placeholder_rows)
        values_sql = ", ".join("(%s)" % sql for sql in placeholder_rows_sql)
        return "VALUES " + values_sql

    def sql_flush(self, style, tables, reset_sequences=False, allow_cascade=False):
        """
        Override the base class method. Returns a list of SQL statements
        required to remove all data from the given database tables (without
        actually removing the tables themselves).

        :type style: :class:`~django.core.management.color.Style`
        :param style: (Currently not used) An object as returned by either
                      color_style() or no_style().

        :type tables: list
        :param tables: A collection of Cloud Spanner Tables

        :type reset_sequences: bool
        :param reset_sequences: (Optional) Currently not used.

        :type allow_cascade: bool
        :param allow_cascade: (Optional) Currently not used.

        :rtype: list
        :returns: A list of SQL statements required to remove all data from
        the given database tables.
        """
        # Cloud Spanner doesn't support TRUNCATE so DELETE instead.
        # A dummy WHERE clause is required.
        if tables:
            delete_sql = "%s %s %%s WHERE 1=1" % (
                style.SQL_KEYWORD("DELETE"),
                style.SQL_KEYWORD("FROM"),
            )
            return [
                delete_sql % style.SQL_FIELD(self.quote_name(table)) for table in tables
            ]
        else:
            return []

    def execute_sql_flush(self, sql_list):
        """Execute a list of SQL statements to flush the database.

        Cloud Spanner doesn't support disabling foreign key checks, so we use a
        retry mechanism to handle deletion order. We try to delete from all tables;
        if some fail due to foreign key constraints, we retry them in subsequent
        passes. As long as we make progress (delete at least one table) in each
        pass, we continue.
        """
        if not sql_list:
            return

        # Ensure we are in autocommit mode or commit explicitly if needed
        was_autocommit = self.connection.get_autocommit()
        if not was_autocommit:
            self.connection.set_autocommit(True)

        try:
            with self.connection.cursor() as cursor:
                # We might need several passes if there is a deep dependency chain
                remaining_sql = list(sql_list)

                # Safety valve: 10 passes should be enough for any reasonable schema depth
                max_passes = 10
                pass_count = 0

                while remaining_sql:
                    pass_count += 1
                    failed_sql = []
                    progress = False
                    last_exception = None

                    if pass_count > max_passes:
                        # We are stuck in a cycle or too deep
                        if last_exception:
                            raise last_exception
                        raise DatabaseError(
                            "Max passes reached in execute_sql_flush without clearing all tables."
                        )

                    for sql in remaining_sql:
                        try:
                            cursor.execute(sql)
                            progress = True
                        except Exception as e:
                            # We catch Exception because Spanner might raise various errors
                            # (Aborted, FailedPrecondition, IntegrityError, etc.)
                            failed_sql.append(sql)
                            last_exception = e

                    # If no progress and still have failed SQL, we are stuck
                    if not progress and failed_sql:
                        raise last_exception

                    remaining_sql = failed_sql

        finally:
            if not was_autocommit:
                self.connection.set_autocommit(False)

    def adapt_datefield_value(self, value):
        """Cast date argument into Spanner DB API DateStr format.

        :type value: object
        :param value: A date argument.

        :rtype: :class:`~google.cloud.spanner_dbapi.types.DateStr`
        :returns: Formatted Date.
        """
        if value is None:
            return None
        return DateStr(str(value))

    def adapt_datetimefield_value(self, value):
        """Reformat time argument into Cloud Spanner.

        :type value: object
        :param value: A time argument.

        :rtype: :class:`~google.cloud.spanner_dbapi.types.TimestampStr`
        :returns: Formatted Time.
        """
        if value is None:
            return None
        # Expression values are adapted by the database.
        if hasattr(value, "resolve_expression"):
            return value
        # Cloud Spanner doesn't support tz-aware datetimes
        if timezone.is_aware(value):
            if settings.USE_TZ:
                value = timezone.make_naive(value, self.connection.timezone)
            else:
                raise ValueError(
                    "The Cloud Spanner backend does not support "
                    "timezone-aware datetimes when USE_TZ is False."
                )
        return TimestampStr(value.isoformat(timespec="microseconds") + "Z")

    def adapt_timefield_value(self, value):
        """
        Transform a time value to an object compatible with what is expected
        by the backend driver for time columns.

        :type value: `datetime.datetime`
        :param value: A time field value.

        :rtype: :class:`~google.cloud.spanner_dbapi.types.TimestampStr`
        :returns: Formatted Time.
        """
        if value is None:
            return None
        # Expression values are adapted by the database.
        if hasattr(value, "resolve_expression"):
            return value
        # Column is TIMESTAMP, so prefix a dummy date to the datetime.time.
        return TimestampStr(
            "0001-01-01T" + value.isoformat(timespec="microseconds") + "Z"
        )

    def get_db_converters(self, expression):
        """Get a list of functions needed to convert field data.

        :type expression: :class:`django.db.models.expressions.BaseExpression`
        :param expression: A query expression to convert.

        :rtype: list
        :returns: Converter functions to apply to Spanner field values.
        """
        converters = super().get_db_converters(expression)
        internal_type = expression.output_field.get_internal_type()
        if internal_type == "DateTimeField":
            converters.append(self.convert_datetimefield_value)
        elif internal_type == "TimeField":
            converters.append(self.convert_timefield_value)
        elif internal_type == "BinaryField":
            converters.append(self.convert_binaryfield_value)
        elif internal_type == "UUIDField":
            converters.append(self.convert_uuidfield_value)
        return converters

    def convert_binaryfield_value(self, value, expression, connection):
        """Convert Spanner BinaryField value for Django.

        :type value: bytes
        :param value: A base64-encoded binary field value.

        :type expression: :class:`django.db.models.expressions.BaseExpression`
        :param expression: A query expression.

        :type connection: :class:`~google.cloud.cpanner_dbapi.connection.Connection`
        :param connection: Reference to a Spanner database connection.

        :rtype: bytes
        :returns: A base64 encoded bytes.
        """
        if value is None:
            return value
        # Cloud Spanner stores bytes base64 encoded.
        return b64decode(value)

    def convert_datetimefield_value(self, value, expression, connection):
        """Convert Spanner DateTimeField value for Django.

        :type value: `DatetimeWithNanoseconds`
        :param value: A datetime field value.

        :type expression: :class:`django.db.models.expressions.BaseExpression`
        :param expression: A query expression.

        :type connection: :class:`~google.cloud.cpanner_dbapi.connection.Connection`
        :param connection: Reference to a Spanner database connection.

        :rtype: datetime
        :returns: A TZ-aware datetime.
        """
        if value is None:
            return value
        # Cloud Spanner returns the
        # google.api_core.datetime_helpers.DatetimeWithNanoseconds subclass
        # of datetime with tzinfo=UTC (which should be replaced with the
        # connection's timezone). Django doesn't support nanoseconds so that
        # part is ignored.
        dt = datetime(
            value.year,
            value.month,
            value.day,
            value.hour,
            value.minute,
            value.second,
            value.microsecond,
        )
        return (
            timezone.make_aware(dt, self.connection.timezone) if settings.USE_TZ else dt
        )

    def convert_timefield_value(self, value, expression, connection):
        """Convert Spanner TimeField value for Django.

        :type value: :class:`~google.api_core.datetime_helpers.DatetimeWithNanoseconds`
        :param value: A datetime/time field.

        :type expression: :class:`django.db.models.expressions.BaseExpression`
        :param expression: A query expression.

        :type connection: :class:`~google.cloud.cpanner_dbapi.connection.Connection`
        :param connection: Reference to a Spanner database connection.

        :rtype: :class:`datetime.time`
        :returns: A converted datetime.
        """
        if value is None:
            return value
        # Convert DatetimeWithNanoseconds to time.
        return time(value.hour, value.minute, value.second, value.microsecond)

    def convert_uuidfield_value(self, value, expression, connection):
        """Convert a UUID field to Cloud Spanner.

        :type value: str
        :param value: A UUID-valued str.

        :type expression: :class:`django.db.models.expressions.BaseExpression`
        :param expression: A query expression.

        :type connection: :class:`~google.cloud.cpanner_dbapi.connection.Connection`
        :param connection: Reference to a Spanner database connection.

        :rtype: :class:`uuid.UUID`
        :returns: A converted UUID.
        """
        if value is not None:
            value = UUID(value)
        return value

    def _prepare_tzname_delta(self, tzname):
        if not tzname or tzname == "UTC":
            return "UTC"
        # Only parse pure offset representations (e.g. +05:30, -08:00, UTC+5).
        # Named timezones (including Etc/GMT+5, Etc/GMT-10) should be passed as-is to Spanner.
        if tzname.startswith(("UTC+", "UTC-")):
            tzname = tzname[3:]
        elif not tzname.startswith(("+", "-")):
            return tzname
        # Spanner does not support seconds in timezone offsets (e.g. +05:30:00, -05:00:00).
        if len(tzname) in (8, 9) and tzname.endswith(":00"):
            return tzname[:-3]
        return tzname

    def _get_timezone_param(self, tzname):
        """Determine the timezone parameter according to Django USE_TZ settings.

        - When USE_TZ is True: use the application's timezone; if none is provided,
          return None so Cloud Spanner uses the database default timezone.
        - When USE_TZ is False: default to 'UTC' so naive timestamps (stored on the
          UTC timeline) are evaluated without server timezone drift, unless an explicit
          timezone is supplied.
        """
        if settings.USE_TZ:
            return self._prepare_tzname_delta(tzname) if tzname else None
        return self._prepare_tzname_delta(tzname) if tzname else "UTC"

    def _validate_lookup_type(self, lookup_type):
        if not isinstance(
            lookup_type, str
        ) or not self.extract_trunc_lookup_pattern.fullmatch(lookup_type):
            raise ValueError(f"Invalid lookup type: {lookup_type!r}")

    # Django's test_trunc_lookup_name_sql_injection catches only (DataError, OperationalError),
    # unlike test_extract_lookup_name_sql_injection which also catches ValueError.
    # OperationalError is raised here to satisfy Django's trunc exception contract.
    def _validate_trunc_lookup_type(self, lookup_type):
        if not isinstance(
            lookup_type, str
        ) or not self.extract_trunc_lookup_pattern.fullmatch(lookup_type):
            raise OperationalError(f"Invalid trunc lookup type: {lookup_type!r}")

    def date_extract_sql(self, lookup_type, field_name, params=None):
        """Extract date from the lookup.

        :type lookup_type: str
        :param lookup_type: A type of the lookup.

        :type field_name: str
        :param field_name: The name of the field.

        :type params: list(str)
        :param params: list of query params.

        :rtype: str
        :returns: A SQL statement for extracting.
        """
        lookup_type = self.extract_names.get(lookup_type, lookup_type)
        self._validate_lookup_type(lookup_type)
        params = () if params is None else tuple(params)
        sql = f"EXTRACT({lookup_type} FROM {field_name})"
        return sql, params

    def datetime_extract_sql(self, lookup_type, field_name, params, tzname):
        """Extract datetime from the lookup.

        :type lookup_type: str
        :param lookup_type: A type of the lookup.

        :type field_name: str
        :param field_name: The name of the field.

        :type tzname: str
        :param tzname: The time zone name. If using of time zone is not
                       allowed in settings default will be UTC.

        :rtype: str
        :returns: A SQL statement for extracting.
        """
        lookup_type = self.extract_names.get(lookup_type, lookup_type)
        self._validate_lookup_type(lookup_type)
        params = () if params is None else tuple(params)
        tzname_param = self._get_timezone_param(tzname)
        if tzname_param:
            return (
                f"EXTRACT({lookup_type} FROM {field_name} AT TIME ZONE %s)",
                (*params, tzname_param),
            )
        return f"EXTRACT({lookup_type} FROM {field_name})", params

    def time_extract_sql(self, lookup_type, field_name, params=None):
        """Extract time from the lookup.

        :type lookup_type: str
        :param lookup_type: A type of the lookup.

        :type field_name: str
        :param field_name: The name of the field.

        :type params: list(str)
        :param params: list of query params.

        :rtype: str
        :returns: A SQL statement for extracting.
        """
        lookup_type = self.extract_names.get(lookup_type, lookup_type)
        self._validate_lookup_type(lookup_type)
        params = () if params is None else tuple(params)
        # Time is stored as TIMESTAMP with UTC time zone.
        sql = f"EXTRACT({lookup_type} FROM {field_name} AT TIME ZONE %s)"
        return sql, (*params, "UTC")

    def date_trunc_sql(self, lookup_type, field_name, params, tzname=None):
        """Truncate date in the lookup.

        :type lookup_type: str
        :param lookup_type: A type of the lookup.

        :type field_name: str
        :param field_name: The name of the field.

        :type params: list(str)
        :param params: list of query params.

        :type tzname: str
        :param tzname: The name of the timezone. This is ignored because
        Spanner does not support Timezone conversion in DATE_TRUNC function.

        :rtype: str
        :returns: A SQL statement for truncating.
        """
        self._validate_trunc_lookup_type(lookup_type)
        params = () if params is None else tuple(params)
        # https://cloud.google.com/spanner/docs/functions-and-operators#date_trunc
        if lookup_type == "week":
            # Spanner truncates to Sunday but Django expects Monday. First,
            # subtract a day so that a Sunday will be truncated to the previous
            # week...
            field_name = f"DATE_SUB(CAST({field_name} AS DATE), INTERVAL 1 DAY)"
        sql = f"DATE_TRUNC(CAST({field_name} AS DATE), {lookup_type})"
        if lookup_type == "week":
            # ...then add a day to get from Sunday to Monday.
            sql = f"DATE_ADD(CAST({sql} AS DATE), INTERVAL 1 DAY)"
        return sql, params

    def datetime_trunc_sql(self, lookup_type, field_name, params, tzname=None):
        """Truncate datetime in the lookup.

        :type lookup_type: str
        :param lookup_type: A type of the lookup.

        :type field_name: str
        :param field_name: The name of the field.

        :type params: list(str)
        :param params: list of query params.

        :type tzname: str
        :param tzname: The name of the timezone.

        :rtype: str
        :returns: A SQL statement for truncating.
        """
        # https://cloud.google.com/spanner/docs/functions-and-operators#timestamp_trunc
        self._validate_trunc_lookup_type(lookup_type)
        params = () if params is None else tuple(params)
        if lookup_type == "week":
            # Spanner truncates to Sunday but Django expects Monday. First,
            # subtract a day so that a Sunday will be truncated to the previous
            # week...
            field_name = f"TIMESTAMP_SUB({field_name}, INTERVAL 1 DAY)"
        tzname_param = self._get_timezone_param(tzname)
        if tzname_param:
            sql = f"TIMESTAMP_TRUNC({field_name}, {lookup_type}, %s)"
            params = (*params, tzname_param)
        else:
            sql = f"TIMESTAMP_TRUNC({field_name}, {lookup_type})"
        if lookup_type == "week":
            # ...then add a day to get from Sunday to Monday.
            sql = f"TIMESTAMP_ADD({sql}, INTERVAL 1 DAY)"
        return sql, params

    def time_trunc_sql(self, lookup_type, field_name, params, tzname=None):
        """Truncate time in the lookup.

        :type lookup_type: str
        :param lookup_type: A type of the lookup.

        :type field_name: str
        :param field_name: The name of the field.

        :type params: list(str)
        :param params: list of query params.

        :type tzname: str
        :param tzname: The name of the timezone.

        :rtype: str
        :returns: A SQL statement for truncating.
        """
        # https://cloud.google.com/spanner/docs/functions-and-operators#timestamp_trunc
        self._validate_trunc_lookup_type(lookup_type)
        params = () if params is None else tuple(params)
        # Time is stored as TIMESTAMP with UTC time zone.
        tzname = tzname if settings.USE_TZ and tzname else "UTC"
        tzname_param = self._prepare_tzname_delta(tzname)
        return (
            f"TIMESTAMP_TRUNC({field_name}, {lookup_type}, %s)",
            (*params, tzname_param),
        )

    def datetime_cast_date_sql(self, field_name, params, tzname):
        """Cast date in the lookup.

        :type field_name: str
        :param field_name: The name of the field.

        :type params: list(str)
        :param params: list of query params.

        :type tzname: str
        :param tzname: The time zone name.

        :rtype: str
        :returns: A SQL statement for casting.
        """
        # https://cloud.google.com/spanner/docs/functions-and-operators#date
        params = () if params is None else tuple(params)
        tzname_param = self._get_timezone_param(tzname)
        if tzname_param:
            return f"DATE({field_name}, %s)", (*params, tzname_param)
        return f"DATE({field_name})", params

    def datetime_cast_time_sql(self, field_name, params, tzname):
        """Cast time in the lookup.

        :type field_name: str
        :param field_name: The name of the field.

        :type params: list(str)
        :param params: list of query params.

        :type tzname: str
        :param tzname: The time zone name.

        :rtype: str
        :returns: A SQL statement for casting.
        """
        params = () if params is None else tuple(params)
        tzname_param = self._get_timezone_param(tzname)
        if tzname_param:
            return (
                f"TIMESTAMP(FORMAT_TIMESTAMP('1970-01-01 %H:%M:%E9S', {field_name}, %s), 'UTC')",
                (*params, tzname_param),
            )
        return (
            f"TIMESTAMP(FORMAT_TIMESTAMP('1970-01-01 %H:%M:%E9S', {field_name}), 'UTC')",
            params,
        )

    def date_interval_sql(self, timedelta):
        """Get a date interval in microseconds.

        :type timedelta: datetime
        :param timedelta: A time delta for the interval.

        :rtype: str
        :returns: A SQL statement.
        """
        return "INTERVAL %s MICROSECOND" % duration_microseconds(timedelta)

    def format_for_duration_arithmetic(self, sql):
        """Do nothing since formatting is handled in the custom function.

        :type sql: str
        :param sql: A SQL statement.

        :rtype: str
        :return: A SQL statement.
        """
        return "INTERVAL %s MICROSECOND" % sql

    def combine_expression(self, connector, sub_expressions):
        """Recurrently combine expressions into single one using connector.

        :type connector: str
        :param connector: A type of connector operation.

        :type sub_expressions: list
        :param sub_expressions: A list of expressions to combine.

        :rtype: str
        :return: A SQL statement for combining.
        """
        if connector == "%%":
            return "MOD(%s)" % ", ".join(sub_expressions)
        elif connector == "^":
            return "POWER(%s)" % ", ".join(sub_expressions)
        elif connector == "#":
            # Connector '#' represents Bit Xor in django.
            # Spanner represents the same fuction with '^' symbol.
            return super().combine_expression("^", sub_expressions)
        elif connector == ">>":
            lhs, rhs = sub_expressions
            # Use an alternate computation because Cloud Sapnner's '>>'
            # operator does not do sign bit extension with a signed type (i.e.
            # produces different results for negative numbers than what
            # Django's tests expect). Cast float result as INT64 to allow
            # assigning to both INT64 and FLOAT64 columns (otherwise the FLOAT
            # result couldn't be assigned to INT64 columns).
            return "CAST(FLOOR(%(lhs)s / POW(2, %(rhs)s)) AS INT64)" % {
                "lhs": lhs,
                "rhs": rhs,
            }
        return super().combine_expression(connector, sub_expressions)

    def combine_duration_expression(self, connector, sub_expressions):
        """Combine duration expressions into single one using connector.

        :type connector: str
        :param connector: A type of connector operation.

        :type sub_expressions: list
        :param sub_expressions: A list of expressions to combine.

        :raises: :class:`~django.db.utils.DatabaseError`

        :rtype: str
        :return: A SQL statement for combining.
        """
        if connector == "+":
            return "TIMESTAMP_ADD(" + ", ".join(sub_expressions) + ")"
        elif connector == "-":
            return "TIMESTAMP_SUB(" + ", ".join(sub_expressions) + ")"
        else:
            raise DatabaseError("Invalid connector for timedelta: %s." % connector)

    def lookup_cast(self, lookup_type, internal_type=None):
        """
        Cast text lookups to string to allow things like  filter(x__contains=4).

        :type lookup_type: str
        :param lookup_type: A type of the lookup.

        :type internal_type: str
        :param internal_type: (Optional)

        :rtype: str
        :return: A SQL statement.
        """
        # Cast text lookups to string to allow things like
        # filter(x__contains=4)
        if lookup_type in (
            "contains",
            "icontains",
            "startswith",
            "istartswith",
            "endswith",
            "iendswith",
            "regex",
            "iregex",
            "iexact",
        ):
            return "CAST(%s AS STRING)"
        return "%s"

    def prep_for_like_query(self, x):
        """Lookups that use this method use REGEXP_CONTAINS instead of LIKE.

        :type x: str
        :param x: A query to prepare.

        :rtype: str
        :returns: A prepared query.
        """
        return re.escape(str(x))

    prep_for_iexact_query = prep_for_like_query

    def no_limit_value(self):
        """The largest INT64: (2**63) - 1

        :rtype: int
        :returns: The largest INT64.
        """
        return 9223372036854775807

    def _get_limit_offset_params(self, low_mark, high_mark):
        limit, offset = super()._get_limit_offset_params(low_mark, high_mark)
        if offset and limit == self.connection.ops.no_limit_value():
            # Subtract offset from the limit to avoid an INT64 overflow error
            # from Cloud Spanner.
            limit -= offset
        return limit, offset

    def savepoint_create_sql(self, sid):
        """
        Return the SQL for creating a savepoint.
        """
        return "SELECT 1"

    def savepoint_commit_sql(self, sid):
        """
        Return the SQL for committing a savepoint.
        """
        return "SELECT 1"

    def savepoint_rollback_sql(self, sid):
        """
        Return the SQL for rolling back to a savepoint.
        """
        return "SELECT 1"
