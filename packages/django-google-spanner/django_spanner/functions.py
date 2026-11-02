# Copyright 2020 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

"""Various math helper functions."""

import math

from django.db.models.expressions import Func, Value
from django.db.models.functions import (
    Cast,
    Chr,
    ConcatPair,
    Cot,
    Degrees,
    JSONArray,
    Left,
    Log,
    Ord,
    Pi,
    Radians,
    Right,
    StrIndex,
    Substr,
)


class IfNull(Func):
    """Represent SQL `IFNULL` function."""

    function = "IFNULL"
    arity = 2


def cast(self, compiler, connection, **extra_context):
    """
    A method to extend Django Cast class. Cast SQL query for given
    parameters.

    :type self: :class:`~django.db.models.functions.Cast`
    :param self: the instance of the class that owns this method.

    :type compiler: :class:`~django_spanner.compiler.SQLCompilerst`
    :param compiler: The query compiler responsible for generating the query.
                     Must have a compile method, returning a (sql, [params])
                     tuple. Calling compiler(value) will return a quoted
                     `value`.

    :type connection: :class:`~google.cloud.spanner_dbapi.connection.Connection`
    :param connection: The Spanner database connection used for the current
                       query.

    :rtype: tuple(str, list)
    :returns: A tuple where `str` is a string containing ordered SQL parameters
              to be replaced with the elements of the `list`.
    """
    # Account for a field's max_length using SUBSTR.
    max_length = getattr(self.output_field, "max_length", None)
    if max_length is not None:
        template = "SUBSTR(" + self.template + ", 0, %s)" % max_length
    else:
        template = self.template
    return self.as_sql(compiler, connection, template=template, **extra_context)


def chr_(self, compiler, connection, **extra_context):
    """
    A method to extend Django Chr class. Returns a SQL query where the code
    points are displayed as a string.

    :type self: :class:`~django.db.models.functions.Chr`
    :param self: the instance of the class that owns this method.

    :type compiler: :class:`~django_spanner.compiler.SQLCompilerst`
    :param compiler: The query compiler responsible for generating the query.
                     Must have a compile method, returning a (sql, [params])
                     tuple. Calling compiler(value) will return a quoted
                     `value`.

    :type connection: :class:`~google.cloud.spanner_dbapi.connection.Connection`
    :param connection: The Spanner database connection used for the current
                       query.

    :rtype: tuple(str, list)
    :returns: A tuple where `str` is a string containing ordered SQL parameters
              to be replaced with the elements of the `list`.
    """
    return self.as_sql(
        compiler,
        connection,
        template="CODE_POINTS_TO_STRING([%(expressions)s])",
        **extra_context,
    )


def concatpair(self, compiler, connection, **extra_context):
    """
    A method to extend Django ConcatPair class. Concatenates a SQL query
    into the sequence of :class:`IfNull` objects.

    :type self: :class:`~django.db.models.functions.ConcatPair`
    :param self: the instance of the class that owns this method.

    :type compiler: :class:`~django_spanner.compiler.SQLCompilerst`
    :param compiler: The query compiler responsible for generating the query.
                     Must have a compile method, returning a (sql, [params])
                     tuple. Calling compiler(value) will return a quoted
                     `value`.

    :type connection: :class:`~google.cloud.spanner_dbapi.connection.Connection`
    :param connection: The Spanner database connection used for the current
                       query.

    :rtype: tuple(str, list)
    :returns: A tuple where `str` is a string containing ordered SQL parameters
              to be replaced with the elements of the `list`.
    """
    # Spanner's CONCAT function returns null if any of its arguments are null.
    # Prevent that by converting null arguments to an empty string.
    clone = self.copy()
    clone.set_source_expressions(
        IfNull(e, Value("")) for e in self.get_source_expressions()
    )
    return clone.as_sql(compiler, connection, **extra_context)


def cot(self, compiler, connection, **extra_context):
    """
    A method to extend Django Cot class. Returns a SQL query of calculated
    trigonometric cotangent function.

    :type self: :class:`~django.db.models.functions.Cot`
    :param self: the instance of the class that owns this method.

    :type compiler: :class:`~django_spanner.compiler.SQLCompilerst`
    :param compiler: The query compiler responsible for generating the query.
                     Must have a compile method, returning a (sql, [params])
                     tuple. Calling compiler(value) will return a quoted
                     `value`.

    :type connection: :class:`~google.cloud.spanner_dbapi.connection.Connection`
    :param connection: The Spanner database connection used for the current
                       query.

    :rtype: tuple(str, list)
    :returns: A tuple where `str` is a string containing ordered SQL parameters
              to be replaced with the elements of the `list`.
    """
    return self.as_sql(
        compiler, connection, template="(1 / TAN(%(expressions)s))", **extra_context
    )


def degrees(self, compiler, connection, **extra_context):
    """
    A method to extend Django Degress class. Returns a SQL query of the
    angle converted to degrees.

    :type self: :class:`~django.db.models.functions.Degrees`
    :param self: the instance of the class that owns this method.

    :type compiler: :class:`~django_spanner.compiler.SQLCompilerst`
    :param compiler: The query compiler responsible for generating the query.
                     Must have a compile method, returning a (sql, [params])
                     tuple. Calling compiler(value) will return a quoted
                     `value`.

    :type connection: :class:`~google.cloud.spanner_dbapi.connection.Connection`
    :param connection: The Spanner database connection used for the current
                       query.

    :rtype: tuple(str, list)
    :returns: A tuple where `str` is a string containing ordered SQL parameters
              to be replaced with the elements of the `list`.
    """
    return self.as_sql(
        compiler,
        connection,
        template="((%%(expressions)s) * 180 / %s)" % math.pi,
        **extra_context,
    )


def json_array(self, compiler, connection, **extra_context):
    """
    A method to extend Django JSONArray class. Returns a SQL query that
    generates a JSON array.

    :type self: :class:`~django.db.models.functions.JSONArray`
    :param self: the instance of the class that owns this method.

    :type compiler: :class:`~django_spanner.compiler.SQLCompilerst`
    :param compiler: The query compiler responsible for generating the query.
                     Must have a compile method, returning a (sql, [params])
                     tuple. Calling compiler(value) will return a quoted
                     `value`.

    :type connection: :class:`~google.cloud.spanner_dbapi.connection.Connection`
    :param connection: The Spanner database connection used for the current
                       query.

    :rtype: tuple(str, list)
    :returns: A tuple where `str` is a string containing ordered SQL parameters
              to be replaced with the elements of the `list`.
    """
    return self.as_sql(
        compiler,
        connection,
        template="TO_JSON_STRING([%(expressions)s])",
        **extra_context,
    )


def left_and_right(self, compiler, connection, **extra_context):
    """A method to extend Django Left and Right classes.

    :type self: :class:`~django.db.models.functions.Left` or
                :class:`~django.db.models.functions.Right`
    :param self: the instance of the class that owns this method.

    :type compiler: :class:`~django_spanner.compiler.SQLCompilerst`
    :param compiler: The query compiler responsible for generating the query.
                     Must have a compile method, returning a (sql, [params])
                     tuple. Calling compiler(value) will return a quoted
                     `value`.

    :type connection: :class:`~google.cloud.spanner_dbapi.connection.Connection`
    :param connection: The Spanner database connection used for the current
                       query.

    :rtype: tuple(str, list)
    :returns: A tuple where `str` is a string containing ordered SQL parameters
              to be replaced with the elements of the `list`.
    """
    return self.get_substr().as_spanner(compiler, connection, **extra_context)


def log(self, compiler, connection, **extra_context):
    """
    A method to extend Django Log class. Returns a SQL query of calculated
    logarithm.

    :type self: :class:`~django.db.models.functions.Log`
    :param self: the instance of the class that owns this method.

    :type compiler: :class:`~django_spanner.compiler.SQLCompilerst`
    :param compiler: The query compiler responsible for generating the query.
                     Must have a compile method, returning a (sql, [params])
                     tuple. Calling compiler(value) will return a quoted
                     `value`.

    :type connection: :class:`~google.cloud.spanner_dbapi.connection.Connection`
    :param connection: The Spanner database connection used for the current
                       query.

    :rtype: tuple(str, list)
    :returns: A tuple where `str` is a string containing ordered SQL parameters
              to be replaced with the elements of the `list`.
    """
    # This function is usually Log(b, x) returning the logarithm of x to the
    # base b, but on Spanner it's Log(x, b).
    clone = self.copy()
    clone.set_source_expressions(self.get_source_expressions()[::-1])
    return clone.as_sql(compiler, connection, **extra_context)


def ord_(self, compiler, connection, **extra_context):
    """
    A method to extend Django Ord class. Returns a SQL query of the
    expression converted to ord.

    :type self: :class:`~django.db.models.functions.Ord`
    :param self: the instance of the class that owns this method.

    :type compiler: :class:`~django_spanner.compiler.SQLCompilerst`
    :param compiler: The query compiler responsible for generating the query.
                     Must have a compile method, returning a (sql, [params])
                     tuple. Calling compiler(value) will return a quoted
                     `value`.

    :type connection: :class:`~google.cloud.spanner_dbapi.connection.Connection`
    :param connection: The Spanner database connection used for the current
                       query.

    :rtype: tuple(str, list)
    :returns: A tuple where `str` is a string containing ordered SQL parameters
              to be replaced with the elements of the `list`.
    """
    return self.as_sql(
        compiler,
        connection,
        template="TO_CODE_POINTS(%(expressions)s)[OFFSET(0)]",
        **extra_context,
    )


def pi(self, compiler, connection, **extra_context):
    """
    A method to extend Django Pi class. Returns a SQL query of the Pi
    constant.

    :type self: :class:`~django.db.models.functions.Pi`
    :param self: the instance of the class that owns this method.

    :type compiler: :class:`~django_spanner.compiler.SQLCompilerst`
    :param compiler: The query compiler responsible for generating the query.
                     Must have a compile method, returning a (sql, [params])
                     tuple. Calling compiler(value) will return a quoted
                     `value`.

    :type connection: :class:`~google.cloud.spanner_dbapi.connection.Connection`
    :param connection: The Spanner database connection used for the current
                       query.

    :rtype: tuple(str, list)
    :returns: A tuple where `str` is a string containing ordered SQL parameters
              to be replaced with the elements of the `list`.
    """
    return self.as_sql(compiler, connection, template=str(math.pi), **extra_context)


def radians(self, compiler, connection, **extra_context):
    """
    A method to extend Django Radians class. Returns a SQL query of the
    angle converted to radians.

    :type self: :class:`~django.db.models.functions.Radians`
    :param self: the instance of the class that owns this method.

    :type compiler: :class:`~django_spanner.compiler.SQLCompilerst`
    :param compiler: The query compiler responsible for generating the query.
                     Must have a compile method, returning a (sql, [params])
                     tuple. Calling compiler(value) will return a quoted
                     `value`.

    :type connection: :class:`~google.cloud.spanner_dbapi.connection.Connection`
    :param connection: The Spanner database connection used for the current
                       query.

    :rtype: tuple(str, list)
    :returns: A tuple where `str` is a string containing ordered SQL parameters
              to be replaced with the elements of the `list`.
    """
    return self.as_sql(
        compiler,
        connection,
        template="((%%(expressions)s) * %s / 180)" % math.pi,
        **extra_context,
    )


def strindex(self, compiler, connection, **extra_context):
    """
    A method to extend Django StrIndex class. Returns a SQL query of the
    string position.

    :type self: :class:`~django.db.models.functions.StrIndex`
    :param self: the instance of the class that owns this method.

    :type compiler: :class:`~django_spanner.compiler.SQLCompilerst`
    :param compiler: The query compiler responsible for generating the query.
                     Must have a compile method, returning a (sql, [params])
                     tuple. Calling compiler(value) will return a quoted
                     `value`.

    :type connection: :class:`~google.cloud.spanner_dbapi.connection.Connection`
    :param connection: The Spanner database connection used for the current
                       query.

    :rtype: tuple(str, list)
    :returns: A tuple where `str` is a string containing ordered SQL parameters
              to be replaced with the elements of the `list`.
    """
    return self.as_sql(compiler, connection, function="STRPOS", **extra_context)


def substr(self, compiler, connection, **extra_context):
    """
    A method to extend Django Substr class. Returns a SQL query of a
    substring.

    :type self: :class:`~django.db.models.functions.Substr`
    :param self: the instance of the class that owns this method.

    :type compiler: :class:`~django_spanner.compiler.SQLCompilerst`
    :param compiler: The query compiler responsible for generating the query.
                     Must have a compile method, returning a (sql, [params])
                     tuple. Calling compiler(value) will return a quoted
                     `value`.

    :type connection: :class:`~google.cloud.spanner_dbapi.connection.Connection`
    :param connection: The Spanner database connection used for the current
                       query.

    :rtype: tuple(str, list)
    :returns: A tuple where `str` is a string containing ordered SQL parameters
              to be replaced with the elements of the `list`.
    """
    return self.as_sql(compiler, connection, function="SUBSTR", **extra_context)


def register_functions():
    """Register the above methods with the corersponding Django classes."""
    Cast.as_spanner = cast
    Chr.as_spanner = chr_
    ConcatPair.as_spanner = concatpair
    Cot.as_spanner = cot
    Degrees.as_spanner = degrees
    JSONArray.as_spanner = json_array
    Left.as_spanner = left_and_right
    Log.as_spanner = log
    Ord.as_spanner = ord_
    Pi.as_spanner = pi
    Radians.as_spanner = radians
    Right.as_spanner = left_and_right
    StrIndex.as_spanner = strindex
    Substr.as_spanner = substr
