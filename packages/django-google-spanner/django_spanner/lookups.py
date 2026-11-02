# Copyright 2020 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

from django.db.models.lookups import (
    Contains,
    EndsWith,
    Exact,
    GreaterThan,
    GreaterThanOrEqual,
    IContains,
    IEndsWith,
    IExact,
    IRegex,
    IStartsWith,
    LessThan,
    LessThanOrEqual,
    Regex,
    StartsWith,
)


def contains(self, compiler, connection):
    """A method to extend Django Contains and IContains classes.

    :type self: :class:`~django.db.models.lookups.Contains` or
                :class:`~django.db.models.lookups.IContains`
    :param self: the instance of the class that owns this method.

    :type compiler: :class:`~django_spanner.compiler.SQLCompilerst`
    :param compiler: The query compiler responsible for generating the query.
                     Must have a compile method, returning a (sql, [params])
                     tuple. Calling compiler(value) will return a quoted
                     `value`.

    :type connection: :class:`~google.cloud.spanner_dbapi.connection.Connection`
    :param connection: The Spanner database connection used for the current
                       query.

    :rtype: tuple[str, str]
    :returns: A tuple of the SQL request and parameters.
    """
    lhs_sql, lhs_params = self.process_lhs(compiler, connection)
    rhs_sql, rhs_params = self.process_rhs(compiler, connection)
    params = list(lhs_params)
    params.extend(rhs_params)
    is_icontains = self.lookup_name.startswith("i")
    if self.rhs_is_direct_value() and rhs_params and not self.bilateral_transforms:
        rhs_sql = self.get_rhs_op(connection, rhs_sql)
        rhs_idx = len(lhs_params)
        # Chop the leading and trailing percent signs that Django adds to the
        # param since this isn't a LIKE query as Django expects.
        params[rhs_idx] = params[rhs_idx][1:-1]
        # Add the case insensitive flag for icontains.
        if is_icontains:
            params[rhs_idx] = "(?i)" + params[rhs_idx]
        # rhs_sql is REGEXP_CONTAINS(%s, %%s), and lhs_sql is the column name.
        return rhs_sql % lhs_sql, tuple(params)
    else:
        # rhs_sql is the expression/column to use as the base of the regular
        # expression.
        if is_icontains:
            rhs_sql = "CONCAT('(?i)', " + rhs_sql + ")"
        return (
            "REGEXP_CONTAINS(%s, %s)"
            % (lhs_sql, connection.pattern_esc.format(rhs_sql)),
            tuple(params),
        )


def iexact(self, compiler, connection):
    """A method to extend Django IExact class. Case-insensitive exact match.
    If the value provided for comparison is None, it will be interpreted as
    an SQL NULL.

    :type self: :class:`~django.db.models.lookups.IExact`
    :param self: the instance of the class that owns this method.

    :type compiler: :class:`~django_spanner.compiler.SQLCompilerst`
    :param compiler: The query compiler responsible for generating the query.
                     Must have a compile method, returning a (sql, [params])
                     tuple. Calling compiler(value) will return a quoted
                     `value`.

    :type connection: :class:`~google.cloud.spanner_dbapi.connection.Connection`
    :param connection: The Spanner database connection used for the current
                       query.

    :rtype: tuple[str, str]
    :returns: A tuple of the SQL request and parameters.
    """
    lhs_sql, lhs_params = self.process_lhs(compiler, connection)
    rhs_sql, rhs_params = self.process_rhs(compiler, connection)
    params = list(lhs_params)
    params.extend(rhs_params)
    rhs_sql = self.get_rhs_op(connection, rhs_sql)
    # Wrap the parameter in ^ and $ to restrict the regex to an exact match.
    if self.rhs_is_direct_value() and rhs_params and not self.bilateral_transforms:
        rhs_idx = len(lhs_params)
        params[rhs_idx] = "^(?i)%s$" % params[rhs_idx]
    else:
        # lhs_sql is the expression/column to use as the regular expression.
        # Use concat to make the value case-insensitive.
        lhs_sql = "CONCAT('^(?i)', " + lhs_sql + ", '$')"
        if not self.rhs_is_direct_value():
            # If rhs is not a direct value
            if not params:
                # if params is not present, then we have only 1 formatable
                # argument in rhs_sql.
                rhs_sql = rhs_sql.replace("%%s", "%s")
            else:
                # If params is present and rhs_sql is to be replaced as well.
                # Example: model_fields.test_uuid.TestQuerying.test_iexact.
                rhs_sql = rhs_sql.replace("%%s", "__PLACEHOLDER_FOR_LHS_SQL__")
                rhs_sql = rhs_sql.replace("%s", "%%s")
                rhs_sql = rhs_sql.replace("__PLACEHOLDER_FOR_LHS_SQL__", "%s")
    # rhs_sql is REGEXP_CONTAINS(%s, %%s), and lhs_sql is the column name.
    return rhs_sql % lhs_sql, tuple(params)


def regex(self, compiler, connection):
    """A method to extend Django Regex and IRegex classes.

    :type self: :class:`~django.db.models.lookups.Regex` or
                :class:`~django.db.models.lookups.IRegex`
    :param self: the instance of the class that owns this method.

    :type compiler: :class:`~django_spanner.compiler.SQLCompilerst`
    :param compiler: The query compiler responsible for generating the query.
                     Must have a compile method, returning a (sql, [params])
                     tuple. Calling compiler(value) will return a quoted
                     `value`.

    :type connection: :class:`~google.cloud.spanner_dbapi.connection.Connection`
    :param connection: The Spanner database connection used for the current
                       query.

    :rtype: tuple[str, str]
    :returns: A tuple of the SQL request and parameters.
    """
    lhs_sql, lhs_params = self.process_lhs(compiler, connection)
    rhs_sql, rhs_params = self.process_rhs(compiler, connection)
    params = list(lhs_params)
    params.extend(rhs_params)
    is_iregex = self.lookup_name.startswith("i")
    if self.rhs_is_direct_value() and rhs_params and not self.bilateral_transforms:
        rhs_sql = self.get_rhs_op(connection, rhs_sql)
        rhs_idx = len(lhs_params)
        if is_iregex:
            params[rhs_idx] = "(?i)%s" % params[rhs_idx]
        else:
            params[rhs_idx] = str(params[rhs_idx])
        # rhs_sql is REGEXP_CONTAINS(%s, %%s), and lhs_sql is the column name.
        return rhs_sql % lhs_sql, tuple(params)
    else:
        # rhs_sql is the expression/column to use as the base of the regular
        # expression.
        if is_iregex:
            rhs_sql = "CONCAT('(?i)', " + rhs_sql + ")"
        return "REGEXP_CONTAINS(%s, %s)" % (lhs_sql, rhs_sql), tuple(params)


def startswith_endswith(self, compiler, connection):
    """A method to extend Django StartsWith, IStartsWith, EndsWith, and
    IEndsWith classes.

    :type self: :class:`~django.db.models.lookups.StartsWith` or
                :class:`~django.db.models.lookups.IStartsWith` or
                :class:`~django.db.models.lookups.EndsWith` or
                :class:`~django.db.models.lookups.IEndsWith`
    :param self: the instance of the class that owns this method.

    :type compiler: :class:`~django_spanner.compiler.SQLCompilerst`
    :param compiler: The query compiler responsible for generating the query.
                     Must have a compile method, returning a (sql, [params])
                     tuple. Calling compiler(value) will return a quoted
                     `value`.

    :type connection: :class:`~google.cloud.spanner_dbapi.connection.Connection`
    :param connection: The Spanner database connection used for the current
                       query.

    :rtype: tuple[str, str]
    :returns: A tuple of the SQL request and parameters.
    """
    lhs_sql, lhs_params = self.process_lhs(compiler, connection)
    rhs_sql, rhs_params = self.process_rhs(compiler, connection)
    params = list(lhs_params)
    params.extend(rhs_params)
    is_startswith = "startswith" in self.lookup_name
    is_endswith = "endswith" in self.lookup_name
    is_insensitive = self.lookup_name.startswith("i")
    # Chop the leading (endswith) or trailing (startswith) percent sign that
    # Django adds to the param since this isn't a LIKE query as Django expects.
    if self.rhs_is_direct_value() and rhs_params and not self.bilateral_transforms:
        rhs_sql = self.get_rhs_op(connection, rhs_sql)
        rhs_idx = len(lhs_params)
        if is_endswith:
            params[rhs_idx] = str(params[rhs_idx][1:]) + "$"
        else:
            params[rhs_idx] = "^" + str(params[rhs_idx][:-1])
        # Add the case insensitive flag for istartswith or iendswith.
        if is_insensitive:
            params[rhs_idx] = "(?i)" + params[rhs_idx]
        # rhs_sql is REGEXP_CONTAINS(%s, %%s), and lhs_sql is the column name.
        return rhs_sql % lhs_sql, tuple(params)
    else:
        # rhs_sql is the expression/column to use as the base of the regular
        # expression.
        sql = "CONCAT('"
        if is_startswith:
            sql += "^"
        if is_insensitive:
            sql += "(?i)"
        sql += "', " + rhs_sql
        if is_endswith:
            sql += ", '$'"
        sql += ")"
        return (
            "REGEXP_CONTAINS(%s, %s)" % (lhs_sql, connection.pattern_esc.format(sql)),
            tuple(params),
        )


def cast_param_to_float(self, compiler, connection):
    """A method to extend Django Exact, GreaterThan, GreaterThanOrEqual,
    LessThan, and LessThanOrEqual classes.

    :type self: :class:`~django.db.models.lookups.Exact` or
                :class:`~django.db.models.lookups.GreaterThan` or
                :class:`~django.db.models.lookups.GreaterThanOrEqual` or
                :class:`~django.db.models.lookups.LessThan` or
                :class:`~django.db.models.lookups.LessThanOrEqual`
    :param self: the instance of the class that owns this method.

    :type compiler: :class:`~django_spanner.compiler.SQLCompilerst`
    :param compiler: The query compiler responsible for generating the query.
                     Must have a compile method, returning a (sql, [params])
                     tuple. Calling compiler(value) will return a quoted
                     `value`.

    :type connection: :class:`~google.cloud.spanner_dbapi.connection.Connection`
    :param connection: The Spanner database connection used for the current
                       query.

    :rtype: tuple[str, str]
    :returns: A tuple of the SQL request and float parameters.
    """
    sql, params = self.as_sql(compiler, connection)
    params = list(params) if params else []
    if params:
        # Cast remote field lookups that must be integer but come in as string.
        if hasattr(self.lhs.output_field, "get_path_info"):
            for i, field in enumerate(
                self.lhs.output_field.get_path_info()[-1].target_fields
            ):
                if field.rel_db_type(connection) == "INT64" and isinstance(
                    params[i], str
                ):
                    params[i] = int(params[i])
    return sql, tuple(params)


def register_lookups():
    """Registers the above methods with the corersponding Django classes."""
    Contains.as_spanner = contains
    IContains.as_spanner = contains
    IExact.as_spanner = iexact
    Regex.as_spanner = regex
    IRegex.as_spanner = regex
    EndsWith.as_spanner = startswith_endswith
    IEndsWith.as_spanner = startswith_endswith
    StartsWith.as_spanner = startswith_endswith
    IStartsWith.as_spanner = startswith_endswith
    Exact.as_spanner = cast_param_to_float
    GreaterThan.as_spanner = cast_param_to_float
    GreaterThanOrEqual.as_spanner = cast_param_to_float
    LessThan.as_spanner = cast_param_to_float
    LessThanOrEqual.as_spanner = cast_param_to_float
