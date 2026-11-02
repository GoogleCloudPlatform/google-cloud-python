# Copyright 2020 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

from django.core.exceptions import EmptyResultSet
from django.db.models.sql.compiler import (
    SQLAggregateCompiler as BaseSQLAggregateCompiler,
)
from django.db.models.sql.compiler import (
    SQLCompiler as BaseSQLCompiler,
)
from django.db.models.sql.compiler import (
    SQLDeleteCompiler as BaseSQLDeleteCompiler,
)
from django.db.models.sql.compiler import (
    SQLInsertCompiler as BaseSQLInsertCompiler,
)
from django.db.models.sql.compiler import (
    SQLUpdateCompiler as BaseSQLUpdateCompiler,
)
from django.db.utils import DatabaseError


class SQLCompiler(BaseSQLCompiler):
    """
    A variation of the Django SQL compiler, adjusted for Spanner-specific
    functionality.
    """

    def get_combinator_sql(self, combinator, all):
        """Override the native Django method.

        Copied from the base class except for:
            combinator_sql += ' ALL' if all else ' DISTINCT'
        Cloud Spanner requires ALL or DISTINCT.

        :type combinator: str
        :param combinator: A type of the combinator for the operation.

        :type all: bool
        :param all: Bool option for the SQL statement.

        :rtype: tuple
        :returns: A tuple containing SQL statement(s) with some additional
                  parameters.
        """
        # This method copies the complete code of this overridden method from
        # Django core and modify it for Spanner by adding one line
        features = self.connection.features
        compilers = [
            query.get_compiler(self.using, self.connection, self.elide_empty)
            for query in self.query.combined_queries
        ]
        if not features.supports_slicing_ordering_in_compound:
            for compiler in compilers:
                if compiler.query.is_sliced:
                    raise DatabaseError(
                        "LIMIT/OFFSET not allowed in subqueries of compound statements."
                    )
                if compiler.get_order_by():
                    raise DatabaseError(
                        "ORDER BY not allowed in subqueries of compound statements."
                    )
        elif self.query.is_sliced and combinator == "union":
            for compiler in compilers:
                # A sliced union cannot have its parts elided as some of them
                # might be sliced as well and in the event where only a single
                # part produces a non-empty resultset it might be impossible to
                # generate valid SQL.
                compiler.elide_empty = False
        parts = ()
        for compiler in compilers:
            try:
                # If the columns list is limited, then all combined queries
                # must have the same columns list. Set the selects defined on
                # the query on all combined queries, if not already set.
                if not compiler.query.values_select and self.query.values_select:
                    compiler.query = compiler.query.clone()
                    compiler.query.set_values(
                        (
                            *self.query.extra_select,
                            *self.query.values_select,
                            *self.query.annotation_select,
                        )
                    )
                part_sql, part_args = compiler.as_sql(with_col_aliases=True)
                if compiler.query.combinator:
                    # Wrap in a subquery if wrapping in parentheses isn't
                    # supported.
                    if not features.supports_parentheses_in_compound:
                        part_sql = "SELECT * FROM ({})".format(part_sql)
                    # Add parentheses when combining with compound query if not
                    # already added for all compound queries.
                    elif (
                        self.query.subquery
                        or not features.supports_slicing_ordering_in_compound
                    ):
                        part_sql = "({})".format(part_sql)
                elif (
                    self.query.subquery
                    and features.supports_slicing_ordering_in_compound
                ):
                    part_sql = "({})".format(part_sql)
                parts += ((part_sql, part_args),)
            except EmptyResultSet:
                # Omit the empty queryset with UNION and with DIFFERENCE if the
                # first queryset is nonempty.
                if combinator == "union" or (combinator == "difference" and parts):
                    continue
                raise
        if not parts:
            raise EmptyResultSet
        combinator_sql = self.connection.ops.set_operators[combinator]
        # This is the only line that is changed from the Django core
        # implementation of this method
        combinator_sql += " ALL" if all else " DISTINCT"
        braces = "{}"
        if not self.query.subquery and features.supports_slicing_ordering_in_compound:
            braces = "({})"
        sql_parts, args_parts = zip(
            *((braces.format(sql), args) for sql, args in parts)
        )
        result = [" {} ".format(combinator_sql).join(sql_parts)]
        params = []
        for part in args_parts:
            params.extend(part)
        return result, params


class SQLInsertCompiler(BaseSQLInsertCompiler, SQLCompiler):
    """A wrapper class for compatibility with Django specifications."""

    pass


class SQLDeleteCompiler(BaseSQLDeleteCompiler, SQLCompiler):
    """A wrapper class for compatibility with Django specifications."""

    pass


class SQLUpdateCompiler(BaseSQLUpdateCompiler, SQLCompiler):
    """A wrapper class for compatibility with Django specifications."""

    pass


class SQLAggregateCompiler(BaseSQLAggregateCompiler, SQLCompiler):
    """A wrapper class for compatibility with Django specifications."""

    pass
