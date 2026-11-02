# Copyright (c) 2021 The sqlalchemy-bigquery Authors
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
This module is used by the compliance tests to control which tests are run

based on database capabilities.
"""

import sqlalchemy.testing.exclusions
import sqlalchemy.testing.requirements

supported = sqlalchemy.testing.exclusions.open
unsupported = sqlalchemy.testing.exclusions.closed


class Requirements(sqlalchemy.testing.requirements.SuiteRequirements):
    @property
    def index_reflection(self):
        return unsupported()

    @property
    def indexes_with_ascdesc(self):
        """target database supports CREATE INDEX with per-column ASC/DESC."""
        return unsupported()

    @property
    def unique_constraint_reflection(self):
        """target dialect supports reflection of unique constraints"""
        return unsupported()

    @property
    def autoincrement_insert(self):
        """target platform generates new surrogate integer primary key values
        when insert() is executed, excluding the pk column."""
        return unsupported()

    @property
    def primary_key_constraint_reflection(self):
        return unsupported()

    @property
    def foreign_keys(self):
        """Target database must support foreign keys."""

        return unsupported()

    @property
    def foreign_key_constraint_reflection(self):
        return unsupported()

    @property
    def on_update_cascade(self):
        """target database must support ON UPDATE..CASCADE behavior in
        foreign keys."""

        return unsupported()

    @property
    def named_constraints(self):
        """target database must support names for constraints."""

        return unsupported()

    @property
    def temp_table_reflection(self):
        return unsupported()

    @property
    def temporary_tables(self):
        """target database supports temporary tables"""
        return unsupported()  # Temporary tables require use of scripts.

    @property
    def duplicate_key_raises_integrity_error(self):
        """target dialect raises IntegrityError when reporting an INSERT
        with a primary key violation.  (hint: it should)

        """
        return unsupported()

    @property
    def precision_numerics_many_significant_digits(self):
        """target backend supports values with many digits on both sides,
        such as 319438950232418390.273596, 87673.594069654243

        """
        return supported()

    @property
    def date_coerces_from_datetime(self):
        """target dialect accepts a datetime object as the target
        of a date column."""

        # BigQuery doesn't allow saving a datetime in a date:
        # `TYPE_DATE`, Invalid date: '2012-10-15T12:57:18'

        return unsupported()

    @property
    def window_functions(self):
        """Target database must support window functions."""
        return supported()  # There are no tests for this. <shrug>

    @property
    def ctes(self):
        """Target database supports CTEs"""

        return supported()

    @property
    def views(self):
        """Target database must support VIEWs."""

        return supported()

    @property
    def schemas(self):
        """Target database must support external schemas, and have one
        named 'test_schema'."""

        return unsupported()

    @property
    def array_type(self):
        """Target database must support array_type"""
        return supported()

    @property
    def implicit_default_schema(self):
        """target system has a strong concept of 'default' schema that can
        be referred to implicitly.

        basically, PostgreSQL.

        """
        return supported()

    @property
    def comment_reflection(self):
        return supported()  # Well, probably not, but we'll try. :)

    @property
    def unicode_ddl(self):
        """Target driver must support some degree of non-ascii symbol
        names.

        However:

        Must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_)

        https://cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#column_name_and_column_schema
        """
        return unsupported()

    @property
    def datetime_literals(self):
        """target dialect supports rendering of a date, time, or datetime as a
        literal string, e.g. via the TypeEngine.literal_processor() method.

        """

        return supported()

    @property
    def timestamp_microseconds(self):
        """target dialect supports representation of Python
        datetime.datetime() with microsecond objects but only
        if TIMESTAMP is used."""
        return supported()

    @property
    def datetime_historic(self):
        """target dialect supports representation of Python
        datetime.datetime() objects with historic (pre 1970) values."""

        return supported()

    @property
    def date_historic(self):
        """target dialect supports representation of Python
        datetime.datetime() objects with historic (pre 1970) values."""

        return supported()

    @property
    def precision_numerics_enotation_small(self):
        """target backend supports Decimal() objects using E notation
        to represent very small values."""
        return supported()

    @property
    def precision_numerics_enotation_large(self):
        """target backend supports Decimal() objects using E notation
        to represent very large values."""
        return supported()

    @property
    def update_from(self):
        """Target must support UPDATE..FROM syntax"""
        return supported()

    @property
    def order_by_label_with_expression(self):
        """target backend supports ORDER BY a column label within an
        expression.

        Basically this::

            select data as foo from test order by foo || 'bar'

        Lots of databases including PostgreSQL don't support this,
        so this is off by default.

        """
        return supported()

    @property
    def sql_expression_limit_offset(self):
        """target database can render LIMIT and/or OFFSET with a complete
        SQL expression, such as one that uses the addition operator.
        parameter
        """
        return unsupported()


class WithSchemas(Requirements):
    """
    Option to run without schema tests

    because the `test_schema` name can't be overridden.
    """

    @property
    def schemas(self):
        return supported()
