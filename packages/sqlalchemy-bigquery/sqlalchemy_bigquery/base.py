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

"""Integration between SQLAlchemy and BigQuery."""

import datetime
import operator
import random
import re
import uuid
from decimal import Decimal

import google.api_core.exceptions
import packaging.version
import sqlalchemy
import sqlalchemy.sql.expression
import sqlalchemy.sql.functions
import sqlalchemy.sql.sqltypes
import sqlalchemy.sql.type_api
import sqlalchemy_bigquery_vendored.sqlalchemy.postgresql.base as vendored_postgresql
from google import auth
from google.api_core.exceptions import NotFound
from google.cloud.bigquery import ConnectionProperty, QueryJobConfig, dbapi
from google.cloud.bigquery.table import (
    RangePartitioning,
    TableReference,
    TimePartitioning,
)
from sqlalchemy import util
from sqlalchemy.engine.base import Engine
from sqlalchemy.engine.default import DefaultDialect, DefaultExecutionContext
from sqlalchemy.exc import NoSuchColumnError, NoSuchTableError
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql import elements, selectable
from sqlalchemy.sql.compiler import (
    DDLCompiler,
    GenericTypeCompiler,
    IdentifierPreparer,
    SQLCompiler,
)
from sqlalchemy.sql.schema import Column, Table
from sqlalchemy.sql.selectable import CTE
from sqlalchemy.sql.sqltypes import Integer, NullType, Numeric, String

from . import _helpers, _types
from .parse_url import parse_url

# Illegal characters is intended to be all characters that are not explicitly
# allowed as part of the flexible column names.
# https://cloud.google.com/bigquery/docs/schemas#flexible-column-names
FIELD_ILLEGAL_CHARACTERS = re.compile(r'[!"$()*,./;?@[\\\]^{}~\n]+', re.ASCII)

TABLE_VALUED_ALIAS_ALIASES = "bigquery_table_valued_alias_aliases"


def assert_(cond, message="Assertion failed"):  # pragma: NO COVER
    if not cond:
        raise AssertionError(message)


class BigQueryIdentifierPreparer(IdentifierPreparer):
    """
    Set containing everything
    https://github.com/dropbox/PyHive/blob/master/pyhive/sqlalchemy_presto.py
    """

    def __init__(self, dialect):
        super(BigQueryIdentifierPreparer, self).__init__(
            dialect,
            initial_quote="`",
        )

    def quote_column(self, value):
        """
        Quote a column.
        Fields are quoted separately from the record name.
        """

        parts = value.split(".")
        return ".".join(self.quote_identifier(x) for x in parts)

    def quote(self, ident, force=None, column=False):
        """
        Conditionally quote an identifier.
        """

        force = getattr(ident, "quote", None)
        if force is None or force:
            return self.quote_column(ident) if column else self.quote_identifier(ident)
        else:
            return ident

    def format_label(self, label, name=None):
        name = name or label.name

        # Fields must start with a letter or underscore
        if not name[0].isalpha() and name[0] != "_":
            name = "_" + name

        # Fields must contain only letters, numbers, and underscores
        name = FIELD_ILLEGAL_CHARACTERS.sub("_", name)

        result = self.quote(name)
        return result


class BigQueryExecutionContext(DefaultExecutionContext):
    def create_cursor(self):
        # Set arraysize
        c = super(BigQueryExecutionContext, self).create_cursor()
        if self.dialect.arraysize:
            c.arraysize = self.dialect.arraysize
        return c

    def get_insert_default(self, column):  # pragma: NO COVER
        # Only used by compliance tests
        if isinstance(column.type, Integer):
            return random.randint(-9223372036854775808, 9223372036854775808)  # 1<<63
        elif isinstance(column.type, String):
            return str(uuid.uuid4())

    __remove_type_from_empty_in = _helpers.substitute_string_re_method(
        r"""
        \sIN\sUNNEST\(\[\s               # ' IN UNNEST([ '
        (
        (?:NULL|\(NULL(?:,\sNULL)+\))\)  # '(NULL)' or '((NULL, NULL, ...))'
        \s(?:AND|OR)\s\(1\s!?=\s1        # ' and 1 != 1' or ' or 1 = 1'
        )
        (?:[:][A-Z0-9]+)?                # Maybe ':TYPE' (e.g. ':INT64')
        \s\]\)                           # Close: ' ])'
        """,
        flags=re.IGNORECASE | re.VERBOSE,
        repl=r" IN(\1)",
    )

    @_helpers.substitute_re_method(
        r"""
        \sIN\sUNNEST\(\[\s       # ' IN UNNEST([ '
        (                        # Placeholders. See below.
        %\([^)]+_\d+\)s          # Placeholder '%(foo_1)s'
        (?:,\s                   # 0 or more placeholders
        %\([^)]+_\d+\)s
        )*
        )?
        :([A-Z0-9]+)             # Type ':TYPE' (e.g. ':INT64')
        \s\]\)                   # Close: ' ])'
        """,
        flags=re.IGNORECASE | re.VERBOSE,
    )
    def __distribute_types_to_expanded_placeholders(self, m):  # pragma: NO COVER
        # If we have an in parameter, it sometimes gets expaned to 0 or more
        # parameters and we need to move the type marker to each
        # parameter.
        # (The way SQLAlchemy handles this is a bit awkward for our
        # purposes.)

        # In the placeholder part of the regex above, the `_\d+
        # suffixes refect that when an array parameter is expanded,
        # numeric suffixes are added.  For example, a placeholder like
        # `%(foo)s` gets expaneded to `%(foo_0)s, `%(foo_1)s, ...`.

        # Coverage: despite our best efforts, never recognized this segment of code as being tested.
        placeholders, type_ = m.groups()
        if placeholders:
            placeholders = placeholders.replace(")", f":{type_})")
        else:
            placeholders = ""
        return f" IN UNNEST([ {placeholders} ])"

    def pre_exec(self):
        self.statement = self.__distribute_types_to_expanded_placeholders(
            self.__remove_type_from_empty_in(self.statement)
        )


class BigQueryCompiler(vendored_postgresql.PGCompiler, SQLCompiler):
    compound_keywords = SQLCompiler.compound_keywords.copy()
    compound_keywords[selectable.CompoundSelect.UNION] = "UNION DISTINCT"
    compound_keywords[selectable.CompoundSelect.UNION_ALL] = "UNION ALL"
    compound_keywords[selectable.CompoundSelect.EXCEPT] = "EXCEPT DISTINCT"
    compound_keywords[selectable.CompoundSelect.INTERSECT] = "INTERSECT DISTINCT"

    def __init__(self, dialect, statement, *args, **kwargs):
        if isinstance(statement, Column):
            kwargs["compile_kwargs"] = util.immutabledict({"include_table": False})
        super(BigQueryCompiler, self).__init__(dialect, statement, *args, **kwargs)

    def visit_insert(self, insert_stmt, asfrom=False, **kw):
        # The (internal) documentation for `inline` is confusing, but
        # having `inline` be true prevents us from generating default
        # primary-key values when we're doing executemany, which seem broken.

        # We can probably do this in the constructor, but I want to
        # make sure this only affects insert, because I'm paranoid. :)

        self.inline = False

        return super(BigQueryCompiler, self).visit_insert(
            insert_stmt, asfrom=False, **kw
        )

    def visit_json_getitem_op_binary(self, binary, operator_, **kw):
        left = self.process(binary.left, **kw)
        return f"{left}.{binary.right.value}"

    def visit_table_valued_alias(self, element, **kw):
        # When using table-valued functions, like UNNEST, BigQuery requires a
        # FROM for any table referenced in the function, including expressions
        # in function arguments.
        #
        # For example, given SQLAlchemy code:
        #
        #   print(
        #      select(func.unnest(foo.c.objects).alias('foo_objects').column)
        #      .compile(engine))
        #
        # Left to it's own devices, SQLAlchemy would outout:
        #
        #   SELECT `foo_objects`
        #   FROM unnest(`foo`.`objects`) AS `foo_objects`
        #
        # But BigQuery diesn't understand the `foo` reference unless
        # we add as reference to `foo` in the FROM:
        #
        #   SELECT foo_objects
        #   FROM `foo`, UNNEST(`foo`.`objects`) as foo_objects
        #
        # This is tricky because:
        # 1. We have to find the table references.
        # 2. We can't know practically if there's already a FROM for a table.
        #
        # We leverage visit_column to find a table reference.  Whenever we find
        # one, we create an alias for it, so as not to conflict with an existing
        # reference if one is present.
        #
        # This requires communicating between this function and visit_column.
        # We do this by sticking a dictionary in the keyword arguments.
        # This dictionary:
        # a. Tells visit_column that it's an a table-valued alias expresssion, and
        # b. Gives it a place to record the aliases it creates.
        #
        # This function creates aliases in the FROM list for any aliases recorded
        # by visit_column.

        kw[TABLE_VALUED_ALIAS_ALIASES] = {}
        ret = super().visit_table_valued_alias(element, **kw)
        aliases = kw.pop(TABLE_VALUED_ALIAS_ALIASES)
        if aliases:
            aliases = ", ".join(
                f"{self.preparer.quote(tablename)} {self.preparer.quote(alias)}"
                for tablename, alias in aliases.items()
            )
            ret = f"{aliases}, {ret}"
        return ret

    def _known_tables(self):
        known_tables = set()

        for from_ in self.compile_state.froms:
            if isinstance(from_, Table):
                known_tables.add(from_.name)
            elif isinstance(from_, CTE):
                known_tables.add(from_.name)
                for column in from_.original.selected_columns:
                    table = getattr(column, "table", None)
                    if table is not None:
                        known_tables.add(table.name)

        # If we have the table in the `from` of our parent, do not add the alias
        # as this will add the table twice and cause an implicit JOIN for that
        # table on itself
        asfrom_froms = self.stack[-1].get("asfrom_froms", [])
        for from_ in asfrom_froms:
            if isinstance(from_, Table):
                known_tables.add(from_.name)

        return known_tables

    def visit_column(
        self,
        column,
        add_to_result_map=None,
        include_table=True,
        result_map_targets=(),
        **kwargs,
    ):
        name = orig_name = column.name
        if name is None:
            name = self._fallback_column_name(column)

        is_literal = column.is_literal
        if not is_literal and isinstance(name, elements._truncated_label):
            name = self._truncated_identifier("colident", name)

        if add_to_result_map is not None:
            targets = (column, name, column.key) + result_map_targets
            if getattr(column, "_tq_label", None):
                # _tq_label was added in SQLAlchemy 1.4
                targets += (column._tq_label,)

            add_to_result_map(name, orig_name, targets, column.type)

        if is_literal:
            name = self.escape_literal_column(name)
        else:
            name = self.preparer.quote(name, column=True)
        table = column.table
        if table is None or not include_table or not table.named_with_column:
            return name
        else:
            tablename = table.name
            if isinstance(tablename, elements._truncated_label):
                tablename = self._truncated_identifier("alias", tablename)
            elif TABLE_VALUED_ALIAS_ALIASES in kwargs:
                if tablename not in self._known_tables():
                    aliases = kwargs[TABLE_VALUED_ALIAS_ALIASES]
                    if tablename not in aliases:
                        aliases[tablename] = self.anon_map[
                            f"{TABLE_VALUED_ALIAS_ALIASES} {tablename}"
                        ]
                    tablename = aliases[tablename]

            return self.preparer.quote(tablename) + "." + name

    def visit_label(self, *args, within_group_by=False, **kwargs):
        # Use labels in GROUP BY clause.
        #
        # Flag set in the group_by_clause method. Works around missing
        # equivalent to supports_simple_order_by_label for group by.
        if within_group_by:
            column_label = args[0]
            sql_keywords = {"GROUPING SETS", "ROLLUP", "CUBE"}
            label_str = column_label.compile(dialect=self.dialect).string
            if not any(keyword in label_str for keyword in sql_keywords):
                kwargs["render_label_as_label"] = column_label

        return super(BigQueryCompiler, self).visit_label(*args, **kwargs)

    def group_by_clause(self, select, **kw):
        return super(BigQueryCompiler, self).group_by_clause(
            select, **kw, within_group_by=True
        )

    ############################################################################
    # Handle parameters in in

    # Due to details in the way sqlalchemy arranges the compilation we
    # expect the bind parameter as an array and unnest it.

    # As it happens, bigquery can handle arrays directly, but there's
    # no way to tell sqlalchemy that, so it works harder than
    # necessary and makes us do the same.

    __sqlalchemy_version_info = packaging.version.parse(sqlalchemy.__version__)

    __expanding_text = "POSTCOMPILE"

    # https://github.com/sqlalchemy/sqlalchemy/commit/f79df12bd6d99b8f6f09d4bf07722638c4b4c159
    __expanding_conflict = (
        "" if __sqlalchemy_version_info < packaging.version.parse("1.4.27") else "__"
    )

    __in_expanding_bind = _helpers.substitute_string_re_method(
        rf"""
        \sIN\s\(                     # ' IN ('
        (
        {__expanding_conflict}\[     # Expanding placeholder
        {__expanding_text}           #   e.g. [EXPANDING_foo_1]
        _[^\]]+                      #
        \]
        (:[A-Z0-9]+)?                # type marker (e.g. ':INT64'
        )
        \)$                          # close w ending )
        """,
        flags=re.IGNORECASE | re.VERBOSE,
        repl=r" IN UNNEST([ \1 ])",
    )

    def visit_in_op_binary(self, binary, operator_, **kw):
        return self.__in_expanding_bind(
            self._generate_generic_binary(binary, " IN ", **kw)
        )

    def visit_not_in_op_binary(self, binary, operator, **kw):
        return (
            "("
            + self.__in_expanding_bind(
                self._generate_generic_binary(binary, " NOT IN ", **kw)
            )
            + ")"
        )

    ############################################################################

    ############################################################################
    # Correct for differences in the way that SQLAlchemy escape % and _ (/)
    # and BigQuery does (\\).

    @staticmethod
    def _maybe_reescape(binary):
        binary = binary._clone()
        escape = binary.modifiers.pop("escape", None)
        if escape and escape != "\\":
            binary.right.value = escape.join(
                v.replace(escape, "\\")
                for v in binary.right.value.split(escape + escape)
            )
        return binary

    def visit_contains_op_binary(self, binary, operator, **kw):
        return super(BigQueryCompiler, self).visit_contains_op_binary(
            self._maybe_reescape(binary), operator, **kw
        )

    def visit_not_contains_op_binary(self, binary, operator, **kw):
        return super(BigQueryCompiler, self).visit_not_contains_op_binary(
            self._maybe_reescape(binary), operator, **kw
        )

    def visit_startswith_op_binary(self, binary, operator, **kw):
        return super(BigQueryCompiler, self).visit_startswith_op_binary(
            self._maybe_reescape(binary), operator, **kw
        )

    def visit_not_startswith_op_binary(self, binary, operator, **kw):
        return super(BigQueryCompiler, self).visit_not_startswith_op_binary(
            self._maybe_reescape(binary), operator, **kw
        )

    def visit_endswith_op_binary(self, binary, operator, **kw):
        return super(BigQueryCompiler, self).visit_endswith_op_binary(
            self._maybe_reescape(binary), operator, **kw
        )

    def visit_not_endswith_op_binary(self, binary, operator, **kw):
        return super(BigQueryCompiler, self).visit_not_endswith_op_binary(
            self._maybe_reescape(binary), operator, **kw
        )

    ############################################################################

    __placeholder = re.compile(r"%\(([^\]:]+)(:[^\]:]+)?\)s$").match

    __expanded_param = re.compile(
        rf"\({__expanding_conflict}\[" rf"{__expanding_text}" rf"_[^\]]+\]\)$"
    ).match

    __remove_type_parameter = _helpers.substitute_string_re_method(
        r"""
        (STRING|BYTES|NUMERIC|BIGNUMERIC)  # Base type
        \(                                 # Dimensions e.g. '(42)', '(4, 2)':
        \s*\d+\s*                          # First dimension
        (?:,\s*\d+\s*)*                    # Remaining dimensions
        \)
        """,
        repl=r"\1",
        flags=re.VERBOSE | re.IGNORECASE,
    )

    def visit_bindparam(
        self,
        bindparam,
        within_columns_clause=False,
        literal_binds=False,
        skip_bind_expression=False,
        **kwargs,
    ):
        type_ = bindparam.type
        unnest = False
        if (
            bindparam.expanding
            and not isinstance(type_, NullType)
            and not literal_binds
        ):
            # Normally, when performing an IN operation, like:
            #
            #  foo IN (some_sequence)
            #
            # SQAlchemy passes `foo` as a parameter and unpacks
            # `some_sequence` and passes each element as a parameter.
            # This mechanism is refered to as "expanding".  It's
            # inefficient and can't handle large arrays. (It's also
            # very complicated, but that's not the issue we care about
            # here. :) ) BigQuery lets us use arrays directly in this
            # context, we just need to call UNNEST on an array when
            # it's used in IN.
            #
            # So, if we get an `expanding` flag, and if we have a known type
            # (and don't have literal binds, which are implemented in-line in
            # in the SQL), we turn off expanding and we set an unnest flag
            # so that we add an UNNEST() call (below).
            #
            # The NullType/known-type check has to do with some extreme
            # edge cases having to do with empty in-lists that get special
            # hijinks from SQLAlchemy that we don't want to disturb. :)
            #
            # Note that we do *not* want to overwrite the "real" bindparam
            # here, because then we can't do a recompile later (e.g., first
            # print the statment, then execute it).  See issue #357.
            #
            # Coverage: despite our best efforts, never recognized this segment of code as being tested.
            if getattr(bindparam, "expand_op", None) is not None:  # pragma: NO COVER
                assert bindparam.expand_op.__name__.endswith("in_op")  # in in
                bindparam = bindparam._clone(maintain_key=True)
                bindparam.expanding = False
                unnest = True

        param = super(BigQueryCompiler, self).visit_bindparam(
            bindparam,
            within_columns_clause,
            literal_binds,
            skip_bind_expression,
            **kwargs,
        )

        if literal_binds or isinstance(type_, NullType):
            return param

        if (
            isinstance(type_, Numeric)
            and (type_.precision is None or type_.scale is None)
            and isinstance(bindparam.value, Decimal)
        ):
            t = bindparam.value.as_tuple()

            if type_.precision is None:
                type_.precision = len(t.digits)

            if type_.scale is None and t.exponent < 0:
                type_.scale = -t.exponent

        bq_type = self.dialect.type_compiler.process(type_)
        bq_type = self.__remove_type_parameter(bq_type)

        assert_(param != "%s", f"Unexpected param: {param}")

        if bindparam.expanding:  # pragma: NO COVER
            assert_(self.__expanded_param(param), f"Unexpected param: {param}")
            if self.__sqlalchemy_version_info < packaging.version.parse("1.4.27"):
                param = param.replace(")", f":{bq_type})")

        else:
            m = self.__placeholder(param)
            if m:
                name, type_ = m.groups()
                assert_(type_ is None)
                param = f"%({name}:{bq_type})s"

        if unnest:
            param = f"UNNEST({param})"

        return param

    def visit_getitem_binary(self, binary, operator_, **kw):
        left = self.process(binary.left, **kw)
        right = self.process(binary.right, **kw)
        return f"{left}[OFFSET({right})]"

    def _get_regexp_args(self, binary, kw):
        string = self.process(binary.left, **kw)
        pattern = self.process(binary.right, **kw)
        return string, pattern

    def visit_regexp_match_op_binary(self, binary, operator, **kw):
        string, pattern = self._get_regexp_args(binary, kw)
        return "REGEXP_CONTAINS(%s, %s)" % (string, pattern)

    def visit_not_regexp_match_op_binary(self, binary, operator, **kw):
        return "NOT %s" % self.visit_regexp_match_op_binary(binary, operator, **kw)

    def visit_mod_binary(self, binary, operator, **kw):
        return f"MOD({self.process(binary.left, **kw)}, {self.process(binary.right, **kw)})"


class BigQueryTypeCompiler(GenericTypeCompiler):
    def visit_INTEGER(self, type_, **kw):
        return "INT64"

    visit_BIGINT = visit_SMALLINT = visit_INTEGER

    def visit_BOOLEAN(self, type_, **kw):
        return "BOOL"

    def visit_FLOAT(self, type_, **kw):
        return "FLOAT64"

    visit_REAL = visit_DOUBLE = visit_DOUBLE_PRECISION = visit_FLOAT

    def visit_STRING(self, type_, **kw):
        if (type_.length is not None) and isinstance(
            kw.get("type_expression"), Column
        ):  # column def
            return f"STRING({type_.length})"
        return "STRING"

    visit_CHAR = visit_NCHAR = visit_STRING
    visit_VARCHAR = visit_NVARCHAR = visit_TEXT = visit_STRING

    def visit_ARRAY(self, type_, **kw):
        return "ARRAY<{}>".format(self.process(type_.item_type, **kw))

    def visit_BINARY(self, type_, **kw):
        if type_.length is not None:
            return f"BYTES({type_.length})"
        return "BYTES"

    visit_VARBINARY = visit_BLOB = visit_BINARY

    def visit_JSON(self, type_, **kw):
        return "JSON"

    def visit_NUMERIC(self, type_, **kw):
        if (type_.precision is not None) and isinstance(
            kw.get("type_expression"), Column
        ):  # column def
            if type_.scale is not None:
                suffix = f"({type_.precision}, {type_.scale})"
            else:
                suffix = f"({type_.precision})"
        else:
            suffix = ""

        return (
            "BIGNUMERIC"
            if (type_.precision is not None and type_.precision > 38)
            or (type_.scale is not None and type_.scale > 9)
            else "NUMERIC"
        ) + suffix

    visit_DECIMAL = visit_NUMERIC


class BigQueryDDLCompiler(DDLCompiler):
    option_datatype_mapping = {
        "friendly_name": str,
        "expiration_timestamp": datetime.datetime,
        "require_partition_filter": bool,
        "default_rounding_mode": str,
    }

    # BigQuery has no support for foreign keys.
    def visit_foreign_key_constraint(self, constraint, **kw):
        return None

    # BigQuery has no support for primary keys.
    def visit_primary_key_constraint(self, constraint, **kw):
        return None

    # BigQuery has no support for unique constraints.
    def visit_unique_constraint(self, constraint, **kw):
        return None

    def get_column_specification(self, column, **kwargs):
        colspec = super(BigQueryDDLCompiler, self).get_column_specification(
            column, **kwargs
        )
        if column.comment is not None:
            colspec = "{} OPTIONS(description={})".format(
                colspec, process_string_literal(column.comment)
            )
        return colspec

    def post_create_table(self, table):
        """
        Constructs additional SQL clauses for table creation in BigQuery.

        This function processes the BigQuery dialect-specific options and generates SQL clauses for partitioning,
        clustering, and other table options.

        Args:
            table (Table): The SQLAlchemy Table object for which the SQL is being generated.

        Returns:
            str: A string composed of SQL clauses for time partitioning, clustering, and other BigQuery specific
                options, each separated by a newline. Returns an empty string if no such options are specified.

        Raises:
            TypeError: If the time_partitioning option is not a `TimePartitioning` object or if the clustering_fields option is not a list.
            NoSuchColumnError: If any field specified in clustering_fields does not exist in the table.
        """

        bq_opts = table.dialect_options["bigquery"]

        options = {}
        clauses = []

        if (
            bq_opts.get("time_partitioning") is not None
            and bq_opts.get("range_partitioning") is not None
        ):
            raise ValueError(
                "biquery_time_partitioning and bigquery_range_partitioning"
                " dialect options are mutually exclusive."
            )

        if (time_partitioning := bq_opts.get("time_partitioning")) is not None:
            self._raise_for_type(
                "time_partitioning",
                time_partitioning,
                TimePartitioning,
            )

            if time_partitioning.expiration_ms:
                _24hours = 1000 * 60 * 60 * 24
                options["partition_expiration_days"] = (
                    time_partitioning.expiration_ms / _24hours
                )

            partition_by_clause = self._process_time_partitioning(
                table,
                time_partitioning,
            )

            clauses.append(partition_by_clause)

        if (range_partitioning := bq_opts.get("range_partitioning")) is not None:
            self._raise_for_type(
                "range_partitioning",
                range_partitioning,
                RangePartitioning,
            )

            partition_by_clause = self._process_range_partitioning(
                table,
                range_partitioning,
            )

            clauses.append(partition_by_clause)

        if (clustering_fields := bq_opts.get("clustering_fields")) is not None:
            self._raise_for_type("clustering_fields", clustering_fields, list)

            for field in clustering_fields:
                if field not in table.c:
                    raise NoSuchColumnError(field)

            clauses.append(f"CLUSTER BY {', '.join(clustering_fields)}")

        if ("description" in bq_opts) or table.comment:
            description = bq_opts.get("description", table.comment)
            self._validate_option_value_type("description", description)
            options["description"] = description

        for option in self.option_datatype_mapping:
            if option in bq_opts:
                options[option] = bq_opts.get(option)

        if options:
            individual_option_statements = [
                "{}={}".format(k, self._process_option_value(v))
                for (k, v) in options.items()
                if self._validate_option_value_type(k, v)
            ]
            clauses.append(f"OPTIONS({', '.join(individual_option_statements)})")

        return " " + "\n".join(clauses)

    def visit_set_table_comment(self, create, **kw):
        table_name = self.preparer.format_table(create.element)
        description = self.sql_compiler.render_literal_value(
            create.element.comment, sqlalchemy.sql.sqltypes.String()
        )
        return f"ALTER TABLE {table_name} SET OPTIONS(description={description})"

    def visit_drop_table_comment(self, drop, **kw):
        table_name = self.preparer.format_table(drop.element)
        return f"ALTER TABLE {table_name} SET OPTIONS(description=null)"

    def _validate_option_value_type(self, option: str, value):
        """
        Validates the type of the given option value against the expected data type.

        Args:
            option (str): The name of the option to be validated.
            value: The value of the dialect option whose type is to be checked. The type of this parameter
                is dynamic and is verified against the expected type in `self.option_datatype_mapping`.

        Returns:
            bool: True if the type of the value matches the expected type, or if the option is not found in
                `self.option_datatype_mapping`.

        Raises:
            TypeError: If the type of the provided value does not match the expected type as defined in
                `self.option_datatype_mapping`.
        """
        if option in self.option_datatype_mapping:
            self._raise_for_type(
                option,
                value,
                self.option_datatype_mapping[option],
            )

        return True

    def _raise_for_type(self, option, value, expected_type):
        if type(value) is not expected_type:
            raise TypeError(
                f"bigquery_{option} dialect option accepts only {expected_type},"
                f" provided {repr(value)}"
            )

    def _process_time_partitioning(
        self,
        table: Table,
        time_partitioning: TimePartitioning,
    ):
        """
        Generates a SQL 'PARTITION BY' clause for partitioning a table,

        Args:
        - table (Table): The SQLAlchemy table object representing the BigQuery
            table to be partitioned.
        - time_partitioning (TimePartitioning): The time partitioning details,
            including the field to be used for partitioning.

        Returns:
        - str: A SQL 'PARTITION BY' clause.

        Example:
        - Given a table with an 'event_timestamp' and setting time_partitioning.type
        as DAY and by setting 'time_partitioning.field' as 'event_timestamp', the
        function returns:
        "PARTITION BY TIMESTAMP_TRUNC(event_timestamp, DAY)".

        Current inputs allowed by BQ and covered by this function include:
        * _PARTITIONDATE
        * DATETIME_TRUNC(<datetime_column>, DAY/HOUR/MONTH/YEAR)
        * TIMESTAMP_TRUNC(<timestamp_column>, DAY/HOUR/MONTH/YEAR)
        * DATE_TRUNC(<date_column>, MONTH/YEAR)

        Additional options allowed by BQ but not explicitly covered by this
        function include:
        * DATE(_PARTITIONTIME)
        * DATE(<timestamp_column>)
        * DATE(<datetime_column>)
        * DATE column
        """

        sqltypes = {
            "_PARTITIONDATE": ("_PARTITIONDATE", None),
            "TIMESTAMP": ("TIMESTAMP_TRUNC", {"DAY", "HOUR", "MONTH", "YEAR"}),
            "DATETIME": ("DATETIME_TRUNC", {"DAY", "HOUR", "MONTH", "YEAR"}),
            "DATE": ("DATE_TRUNC", {"MONTH", "YEAR"}),
        }

        # Extract field (i.e <column_name> or _PARTITIONDATE)
        # AND extract the name of the column_type (i.e. "TIMESTAMP", "DATE",
        # "DATETIME", "_PARTITIONDATE")
        if time_partitioning.field is not None:
            field = time_partitioning.field
            column_type = table.columns[field].type.__visit_name__.upper()

        else:
            field = "_PARTITIONDATE"
            column_type = "_PARTITIONDATE"

        # Extract time_partitioning.type_ (DAY, HOUR, MONTH, YEAR)
        # i.e. generates one partition per type (1/DAY, 1/HOUR)
        # NOTE: if time_partitioning.type_ == None, it gets
        # immediately overwritten by python-bigquery to a default of DAY.
        partitioning_period = time_partitioning.type_

        # Extract the truncation_function (i.e. DATE_TRUNC)
        # and the set of allowable partition_periods
        # that can be used in that function
        trunc_fn, allowed_partitions = sqltypes[column_type]

        # Create output:
        # Special Case: _PARTITIONDATE does NOT use a function or partitioning_period
        if trunc_fn == "_PARTITIONDATE":
            return f"PARTITION BY {field}"

        # Special Case: BigQuery will not accept DAY as partitioning_period for
        # DATE_TRUNC.
        # However, the default argument in python-bigquery for TimePartioning
        # is DAY. This case overwrites that to avoid making a breaking change in
        # python-bigquery.
        # https://github.com/googleapis/python-bigquery/blob/a4d9534a900f13ae7355904cda05097d781f27e3/google/cloud/bigquery/table.py#L2916
        if trunc_fn == "DATE_TRUNC" and partitioning_period == "DAY":
            raise ValueError(
                "The TimePartitioning.type_ must be one of: "
                f"{allowed_partitions}, received {partitioning_period}."
                "NOTE: the `default` value for TimePartioning.type_ as set in "
                "python-bigquery is 'DAY', if you wish to use 'DATE_TRUNC' "
                "ensure that you overwrite the default TimePartitioning.type_. "
            )

        # Generic Case
        if partitioning_period not in allowed_partitions:
            raise ValueError(
                "The TimePartitioning.type_ must be one of: "
                f"{allowed_partitions}, received {partitioning_period}."
            )

        return f"PARTITION BY {trunc_fn}({field}, {partitioning_period})"

    def _process_range_partitioning(
        self, table: Table, range_partitioning: RangePartitioning
    ):
        """
        Generates a SQL 'PARTITION BY' clause for partitioning a table by a range of integers.

        Args:
        - table (Table): The SQLAlchemy table object representing the BigQuery table to be partitioned.
        - range_partitioning (RangePartitioning): The RangePartitioning object containing the
        partitioning field, range start, range end, and interval.

        Returns:
        - str: A SQL string for range partitioning using RANGE_BUCKET and GENERATE_ARRAY functions.

        Raises:
        - AttributeError: If the partitioning field is not defined.
        - ValueError: If the partitioning field (i.e. column) data type is not an integer.
        - TypeError: If the partitioning range start/end values are not integers.

        Example:
            "PARTITION BY RANGE_BUCKET(zipcode, GENERATE_ARRAY(0, 100000, 10))"
        """
        if range_partitioning.field is None:
            raise AttributeError(
                "bigquery_range_partitioning expects field to be defined"
            )

        if not isinstance(
            table.columns[range_partitioning.field].type,
            sqlalchemy.sql.sqltypes.INT,
        ):
            raise ValueError(
                "bigquery_range_partitioning expects field (i.e. column) data type to be INTEGER"
            )

        range_ = range_partitioning.range_

        if not isinstance(range_.start, int):
            raise TypeError(
                "bigquery_range_partitioning expects range_.start to be an int,"
                f" provided {repr(range_.start)}"
            )

        if not isinstance(range_.end, int):
            raise TypeError(
                "bigquery_range_partitioning expects range_.end to be an int,"
                f" provided {repr(range_.end)}"
            )

        default_interval = 1

        return f"PARTITION BY RANGE_BUCKET({range_partitioning.field}, GENERATE_ARRAY({range_.start}, {range_.end}, {range_.interval or default_interval}))"

    def _process_option_value(self, value):
        """
        Transforms the given option value into a literal representation suitable for SQL queries in BigQuery.

        Args:
            value: The value to be transformed.

        Returns:
            The processed value in a format suitable for inclusion in a SQL query.

        Raises:
            NotImplementedError: When there is no transformation registered for a data type.
        """
        option_casting = {
            # Mapping from option type to its casting method
            str: lambda x: process_string_literal(x),
            int: lambda x: x,
            float: lambda x: x,
            bool: lambda x: "true" if x else "false",
            datetime.datetime: lambda x: BQTimestamp.process_timestamp_literal(x),
        }

        if (option_cast := option_casting.get(type(value))) is not None:
            return option_cast(value)

        raise NotImplementedError(f"No transformation registered for {repr(value)}")


def process_string_literal(value):
    return repr(value.replace("%", "%%"))


class BQString(String):
    def literal_processor(self, dialect):
        return process_string_literal


class BQBinary(sqlalchemy.sql.sqltypes._Binary):
    @staticmethod
    def __process_bytes_literal(value):
        return repr(value.replace(b"%", b"%%"))

    def literal_processor(self, dialect):
        return self.__process_bytes_literal


class BQClassTaggedStr(sqlalchemy.sql.type_api.TypeEngine):
    """Type that can get literals via str"""

    @staticmethod
    def process_literal_as_class_tagged_str(value):
        return f"{value.__class__.__name__.upper()} {repr(str(value))}"

    def literal_processor(self, dialect):
        return self.process_literal_as_class_tagged_str


class BQTimestamp(sqlalchemy.sql.type_api.TypeEngine):
    """Type that can get literals via str"""

    @staticmethod
    def process_timestamp_literal(value):
        return f"TIMESTAMP {process_string_literal(str(value))}"

    def literal_processor(self, dialect):
        return self.process_timestamp_literal


class BQArray(sqlalchemy.sql.sqltypes.ARRAY):
    def literal_processor(self, dialect):
        item_processor = self.item_type._cached_literal_processor(dialect)
        if not item_processor:
            raise NotImplementedError(
                f"Don't know how to literal-quote values of type {self.item_type}"
            )

        def process_array_literal(value):
            return "[" + ", ".join(item_processor(v) for v in value) + "]"

        return process_array_literal


class BigQueryDialect(DefaultDialect):
    name = "bigquery"
    driver = "bigquery"
    preparer = BigQueryIdentifierPreparer
    statement_compiler = BigQueryCompiler
    type_compiler = BigQueryTypeCompiler
    ddl_compiler = BigQueryDDLCompiler
    execution_ctx_cls = BigQueryExecutionContext
    cte_follows_insert = True
    supports_alter = False
    supports_comments = True
    inline_comments = True
    supports_pk_autoincrement = False
    supports_default_values = False
    supports_empty_insert = False
    supports_multivalues_insert = True
    supports_statement_cache = False
    supports_unicode_statements = True
    supports_unicode_binds = True
    supports_native_decimal = True
    description_encoding = None
    supports_native_boolean = True
    supports_simple_order_by_label = True
    postfetch_lastrowid = False
    preexecute_autoincrement_sequences = False

    colspecs = {
        String: BQString,
        sqlalchemy.sql.sqltypes._Binary: BQBinary,
        sqlalchemy.sql.sqltypes.Date: BQClassTaggedStr,
        sqlalchemy.sql.sqltypes.DateTime: BQClassTaggedStr,
        sqlalchemy.sql.sqltypes.Time: BQClassTaggedStr,
        sqlalchemy.sql.sqltypes.TIMESTAMP: BQTimestamp,
        sqlalchemy.sql.sqltypes.ARRAY: BQArray,
        sqlalchemy.sql.sqltypes.Enum: sqlalchemy.sql.sqltypes.Enum,
    }

    def __init__(
        self,
        arraysize=5000,
        credentials_path=None,
        billing_project_id=None,
        location=None,
        credentials_info=None,
        credentials_base64=None,
        list_tables_page_size=1000,
        *args,
        **kwargs,
    ):
        super(BigQueryDialect, self).__init__(*args, **kwargs)
        self.arraysize = arraysize
        self.credentials_path = credentials_path
        self.credentials_info = credentials_info
        self.credentials_base64 = credentials_base64
        self.project_id = None
        self.billing_project_id = billing_project_id
        self.location = location
        self.identifier_preparer = self.preparer(self)
        self.dataset_id = None
        self.list_tables_page_size = list_tables_page_size

    @classmethod
    def dbapi(cls):
        """
        Use `import_dbapi()` instead.
        Maintained for backward compatibility.
        """
        return dbapi

    @classmethod
    def import_dbapi(cls):
        return dbapi

    @staticmethod
    def _build_formatted_table_id(table):
        """Build '<dataset_id>.<table_id>' string using given table."""
        return "{}.{}".format(table.reference.dataset_id, table.table_id)

    def create_job_config(self, provided_config: QueryJobConfig):
        project_id = self.project_id
        if self.dataset_id is None and project_id == self.billing_project_id:
            return provided_config
        job_config = provided_config or QueryJobConfig()
        if project_id != self.billing_project_id:
            job_config.connection_properties = [
                ConnectionProperty(key="dataset_project_id", value=project_id)
            ]
        if self.dataset_id:
            if not project_id:
                _, project_id = auth.default()
            job_config.default_dataset = "{}.{}".format(project_id, self.dataset_id)
        return job_config

    def do_execute(self, cursor, statement, parameters, context=None):
        kwargs = {}
        if context is not None and context.execution_options.get("job_config"):
            kwargs["job_config"] = context.execution_options.get("job_config")
        cursor.execute(statement, parameters, **kwargs)

    def create_connect_args(self, url):
        (
            self.project_id,
            location,
            dataset_id,
            arraysize,
            credentials_path,
            credentials_base64,
            provided_job_config,
            list_tables_page_size,
            user_supplied_client,
        ) = parse_url(url)

        self.arraysize = arraysize or self.arraysize
        self.list_tables_page_size = list_tables_page_size or self.list_tables_page_size
        self.location = location or self.location
        self.credentials_path = credentials_path or self.credentials_path
        self.credentials_base64 = credentials_base64 or self.credentials_base64
        self.dataset_id = dataset_id
        self.billing_project_id = self.billing_project_id or self.project_id

        default_query_job_config = self.create_job_config(provided_job_config)

        if user_supplied_client:
            # The user is expected to supply a client with
            # create_engine('...', connect_args={'client': bq_client})
            return ([], {})
        else:
            client = _helpers.create_bigquery_client(
                credentials_path=self.credentials_path,
                credentials_info=self.credentials_info,
                credentials_base64=self.credentials_base64,
                project_id=self.billing_project_id,
                location=self.location,
                default_query_job_config=default_query_job_config,
            )
            # If the user specified `bigquery://` we need to set the project_id
            # from the client
            self.project_id = self.project_id or client.project
            self.billing_project_id = self.billing_project_id or client.project
            return ([], {"client": client})

    def _get_table_or_view_names(self, connection, item_types, schema=None):
        current_schema = schema or self.dataset_id
        get_table_name = (
            self._build_formatted_table_id
            if self.dataset_id is None
            else operator.attrgetter("table_id")
        )

        client = connection.connection._client
        datasets = client.list_datasets(self.project_id)

        result = []
        for dataset in datasets:
            if current_schema is not None and current_schema != dataset.dataset_id:
                continue

            try:
                tables = client.list_tables(
                    dataset.reference, page_size=self.list_tables_page_size
                )
                for table in tables:
                    if table.table_type in item_types:
                        result.append(get_table_name(table))
            except google.api_core.exceptions.NotFound:
                # It's possible that the dataset was deleted between when we
                # fetched the list of datasets and when we try to list the
                # tables from it. See:
                # https://github.com/googleapis/python-bigquery-sqlalchemy/issues/105
                pass
        return result

    @staticmethod
    def _split_table_name(full_table_name):
        # Split full_table_name to get project, dataset and table name
        dataset = None
        table_name = None
        project = None

        table_name_split = full_table_name.split(".")
        if len(table_name_split) == 1:
            table_name = full_table_name
        elif len(table_name_split) == 2:
            dataset, table_name = table_name_split
        elif len(table_name_split) == 3:
            project, dataset, table_name = table_name_split
        else:
            raise ValueError(
                "Did not understand table_name: {}".format(full_table_name)
            )

        return (project, dataset, table_name)

    def _table_reference(
        self, provided_schema_name, provided_table_name, client_project
    ):
        project_id_from_table, dataset_id_from_table, table_id = self._split_table_name(
            provided_table_name
        )
        project_id_from_schema = None
        dataset_id_from_schema = None
        if provided_schema_name is not None:
            provided_schema_name_split = provided_schema_name.split(".")
            if len(provided_schema_name_split) == 1:
                if dataset_id_from_table:
                    project_id_from_schema = provided_schema_name_split[0]
                else:
                    dataset_id_from_schema = provided_schema_name_split[0]
            elif len(provided_schema_name_split) == 2:
                project_id_from_schema = provided_schema_name_split[0]
                dataset_id_from_schema = provided_schema_name_split[1]
            else:
                raise ValueError(
                    "Did not understand schema: {}".format(provided_schema_name)
                )
        if (
            dataset_id_from_schema
            and dataset_id_from_table
            and dataset_id_from_schema != dataset_id_from_table
        ):
            raise ValueError(
                "dataset_id specified in schema and table_name disagree: "
                "got {} in schema, and {} in table_name".format(
                    dataset_id_from_schema, dataset_id_from_table
                )
            )
        if (
            project_id_from_schema
            and project_id_from_table
            and project_id_from_schema != project_id_from_table
        ):
            raise ValueError(
                "project_id specified in schema and table_name disagree: "
                "got {} in schema, and {} in table_name".format(
                    project_id_from_schema, project_id_from_table
                )
            )
        project_id = project_id_from_schema or project_id_from_table or client_project
        dataset_id = dataset_id_from_schema or dataset_id_from_table or self.dataset_id

        table_ref = TableReference.from_string(
            "{}.{}.{}".format(project_id, dataset_id, table_id)
        )
        return table_ref

    def _get_table(self, connection, table_name, schema=None):
        if isinstance(connection, Engine):
            connection = connection.connect()

        client = connection.connection._client

        # table_ref = self._table_reference(schema, table_name, client.project)
        table_ref = self._table_reference(schema, table_name, self.project_id)
        try:
            table = client.get_table(table_ref)
        except NotFound:
            raise NoSuchTableError(table_name)
        return table

    def has_table(self, connection, table_name, schema=None, **kw):
        """Checks whether a table exists in BigQuery.

        Args:
            connection (google.cloud.bigquery.client.Client): The client
                object used to interact with BigQuery.
            table_name (str): The name of the table to check for.
            schema (str, optional): The name of the schema to which the table
                belongs. Defaults to the default schema.
            **kw (dict): Any extra keyword arguments will be ignored.

        Returns:
            bool: True if the table exists, False otherwise.

        """
        try:
            self._get_table(connection, table_name, schema)
            return True
        except NoSuchTableError:
            return False

    def get_columns(self, connection, table_name, schema=None, **kw):
        table = self._get_table(connection, table_name, schema)
        return _types.get_columns(table.schema)

    def get_table_comment(self, connection, table_name, schema=None, **kw):
        table = self._get_table(connection, table_name, schema)
        return {
            "text": table.description,
        }

    def get_foreign_keys(self, connection, table_name, schema=None, **kw):
        # BigQuery has no support for foreign keys.
        return []

    def get_pk_constraint(self, connection, table_name, schema=None, **kw):
        # BigQuery has no support for primary keys.
        return {"constrained_columns": []}

    def get_indexes(self, connection, table_name, schema=None, **kw):
        # BigQuery has no support for indexes.
        return []

    def get_schema_names(self, connection, **kw):
        if isinstance(connection, Engine):
            connection = connection.connect()

        datasets = connection.connection._client.list_datasets(self.project_id)
        return [d.dataset_id for d in datasets]

    def get_table_names(self, connection, schema=None, **kw):
        if isinstance(connection, Engine):
            connection = connection.connect()

        item_types = ["TABLE", "EXTERNAL"]
        return self._get_table_or_view_names(connection, item_types, schema)

    def get_view_names(self, connection, schema=None, **kw):
        if isinstance(connection, Engine):
            connection = connection.connect()

        item_types = ["VIEW", "MATERIALIZED_VIEW"]
        return self._get_table_or_view_names(connection, item_types, schema)

    def do_rollback(self, dbapi_connection):
        # BigQuery has no support for transactions.
        pass

    def get_view_definition(self, connection, view_name, schema=None, **kw):
        if isinstance(connection, Engine):
            connection = connection.connect()
        client = connection.connection._client
        if self.dataset_id:
            view_name = f"{self.dataset_id}.{view_name}"
        view = client.get_table(view_name)
        return view.view_query


class unnest(sqlalchemy.sql.functions.GenericFunction):
    def __init__(self, *args, **kwargs):
        expr = kwargs.pop("expr", None)
        if expr is not None:
            args = (expr,) + args
        if len(args) != 1:
            raise TypeError("The unnest function requires a single argument.")
        arg = args[0]
        if isinstance(arg, sqlalchemy.sql.expression.ColumnElement):
            if not (
                isinstance(arg.type, sqlalchemy.sql.sqltypes.ARRAY)
                or (
                    hasattr(arg.type, "impl")
                    and isinstance(arg.type.impl, sqlalchemy.sql.sqltypes.ARRAY)
                )
            ):
                raise TypeError("The argument to unnest must have an ARRAY type.")
            self.type = arg.type.item_type
        super().__init__(*args, **kwargs)


dialect = BigQueryDialect

try:
    import alembic  # noqa
except ImportError:  # pragma: NO COVER
    pass
else:
    from alembic.ddl import impl
    from alembic.ddl.base import (
        ColumnName,
        ColumnType,
        alter_column,
        alter_table,
        format_column_name,
        format_type,
    )

    class SqlalchemyBigqueryImpl(impl.DefaultImpl):
        __dialect__ = "bigquery"

    @compiles(ColumnName, "bigquery")
    def visit_column_name(element: ColumnName, compiler: DDLCompiler, **kw) -> str:
        """Replaces the visit_column_name() function in alembic/alembic/ddl/base.py.
        See https://github.com/googleapis/python-bigquery-sqlalchemy/issues/1097"""

        return "%s RENAME COLUMN %s TO %s" % (
            alter_table(compiler, element.table_name, element.schema),
            format_column_name(compiler, element.column_name),
            format_column_name(compiler, element.newname),
        )

    @compiles(ColumnType, "bigquery")
    def visit_column_type(element: ColumnType, compiler: DDLCompiler, **kw) -> str:
        """Replaces the visit_column_type() function in alembic/alembic/ddl/base.py.
        The alembic version ends in TYPE <element type>, but bigquery requires this syntax:
        SET DATA TYPE <element type>"""

        return "%s %s %s" % (
            alter_table(compiler, element.table_name, element.schema),
            alter_column(compiler, element.column_name),
            "SET DATA TYPE %s" % format_type(compiler, element.type_),
        )
