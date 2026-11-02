# dialects/postgresql/base.py
# Copyright (C) 2005-2024 the SQLAlchemy authors and contributors
# <see AUTHORS file>
#
# This module is part of SQLAlchemy and is released under
# the MIT License: https://www.opensource.org/licenses/mit-license.php
# mypy: ignore-errors

from sqlalchemy.sql import compiler


class PGCompiler(compiler.SQLCompiler):
    def update_from_clause(
        self, update_stmt, from_table, extra_froms, from_hints, **kw
    ):
        kw["asfrom"] = True
        return "FROM " + ", ".join(
            t._compiler_dispatch(self, fromhints=from_hints, **kw) for t in extra_froms
        )
