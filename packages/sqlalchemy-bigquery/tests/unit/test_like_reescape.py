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

"""SQLAlchemy and BigQuery escape % and _ differently in like expressions.

We need to correct for the autoescape option in various string
functions.
"""

import sqlalchemy.sql.operators
import sqlalchemy.sql.schema

import sqlalchemy_bigquery.base


def _check(raw, escaped, escape=None, autoescape=True):
    col = sqlalchemy.sql.schema.Column()
    op = col.contains(raw, escape=escape, autoescape=autoescape)
    o2 = sqlalchemy_bigquery.base.BigQueryCompiler._maybe_reescape(op)
    assert o2.left.__dict__ == op.left.__dict__
    assert not o2.modifiers.get("escape")

    assert o2.right.value == escaped


def test_like_autoescape_reescape():
    _check("ab%cd", "ab\\%cd")
    _check("ab%c_d", "ab\\%c\\_d")
    _check("ab%cd", "ab%cd", autoescape=False)
    _check("ab%c_d", "ab\\%c\\_d", escape="\\")
    _check("ab/%c/_/d", "ab/\\%c/\\_/d")
