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

import sqlalchemy.sql.coercions
import sqlalchemy.sql.default_comparator
import sqlalchemy.sql.roles
import sqlalchemy.sql.sqltypes
import sqlalchemy.types
from sqlalchemy.sql import operators

# from . import base  # Moved to _get_subtype_col_spec to break circular import


def _get_subtype_col_spec(type_):
    global _get_subtype_col_spec
    from . import base

    type_compiler = base.dialect.type_compiler(base.dialect())
    _get_subtype_col_spec = type_compiler.process
    return _get_subtype_col_spec(type_)


class STRUCT(sqlalchemy.sql.sqltypes.Indexable, sqlalchemy.types.UserDefinedType):
    """
    A type for BigQuery STRUCT/RECORD data

    See https://googleapis.dev/python/sqlalchemy-bigquery/latest/struct.html
    """

    # See https://docs.sqlalchemy.org/en/14/core/custom_types.html#creating-new-types

    def __init__(
        self,
        *fields,
        **kwfields,
    ):
        # Note that because:
        # https://docs.python.org/3/whatsnew/3.6.html#pep-468-preserving-keyword-argument-order
        # We know that `kwfields` preserves order.
        self._STRUCT_fields = tuple(
            (
                name,
                type_ if isinstance(type_, sqlalchemy.types.TypeEngine) else type_(),
            )
            for (name, type_) in (fields + tuple(kwfields.items()))
        )

        self._STRUCT_byname = {
            name.lower(): type_ for (name, type_) in self._STRUCT_fields
        }

    def __repr__(self):
        fields = ", ".join(
            f"{name}={repr(type_)}" for name, type_ in self._STRUCT_fields
        )
        return f"STRUCT({fields})"

    def get_col_spec(self, **kw):
        fields = ", ".join(
            f"{name} {_get_subtype_col_spec(type_)}"
            for name, type_ in self._STRUCT_fields
        )
        return f"STRUCT<{fields}>"

    def bind_processor(self, dialect):
        return dict

    class Comparator(sqlalchemy.sql.sqltypes.Indexable.Comparator):
        def _setup_getitem(self, name):
            if not isinstance(name, str):
                raise TypeError(
                    f"STRUCT fields can only be accessed with strings field names,"
                    f" not {repr(name)}."
                )
            subtype = self.expr.type._STRUCT_byname.get(name.lower())
            if subtype is None:
                raise KeyError(name)
            operator = operators.json_getitem_op
            index = _field_index(self, name, operator)
            return operator, index, subtype

        def __getattr__(self, name):
            if name.lower() in self.expr.type._STRUCT_byname:
                return self[name]
            else:
                raise AttributeError(name)

    comparator_factory = Comparator


def _field_index(self, name, operator):
    return sqlalchemy.sql.coercions.expect(
        sqlalchemy.sql.roles.BinaryElementRole,
        name,
        expr=self.expr,
        operator=operator,
        bindparam_type=sqlalchemy.types.String(),
    )


# class SQLCompiler:
#     def visit_json_getitem_op_binary(self, binary, operator_, **kw):
#         left = self.process(binary.left, **kw)
#         return f"{left}.{binary.right.value}"
