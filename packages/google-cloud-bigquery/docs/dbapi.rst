DB-API Reference
~~~~~~~~~~~~~~~~

.. automodule:: google.cloud.bigquery.dbapi
  :members:
  :show-inheritance:


DB-API Query-Parameter Syntax
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The BigQuery DB-API uses the `qmark` `parameter style
<https://www.python.org/dev/peps/pep-0249/#paramstyle>`_ for
unnamed/positional parameters and the `pyformat` parameter style for
named parameters.

An example of a query using unnamed parameters::

  insert into people (name, income) values (?, ?)

and using named parameters::

  insert into people (name, income) values (%(name)s, %(income)s)

Providing explicit type information
-----------------------------------

BigQuery requires type information for parameters.  The BigQuery
DB-API can usually determine parameter types for parameters based on
provided values.  Sometimes, however, types can't be determined (for
example when `None` is passed) or are determined incorrectly (for
example when passing a floating-point value to a numeric column).

The BigQuery DB-API provides an extended parameter syntax.  For named
parameters, a BigQuery type is provided after the name separated by a
colon, as in::

  insert into people (name, income) values (%(name:string)s, %(income:numeric)s)

For unnamed parameters, use the named syntax with a type, but no
name, as in::

  insert into people (name, income) values (%(:string)s, %(:numeric)s)

Providing type information is the *only* way to pass `struct` data::

  cursor.execute(
    "insert into points (point) values (%(:struct<x float64, y float64>)s)",
    [{"x": 10, "y": 20}],
    )
