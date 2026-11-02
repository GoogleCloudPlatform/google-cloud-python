#  Copyright 2026 Google LLC
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
"""DBAPI 2.0 Global Variables."""

# Globals: apilevel
# String constant stating the supported DB API level.
# https://peps.python.org/pep-0249/#apilevel
# Currently only the strings “1.0” and “2.0” are allowed.
# If not given, a DB-API 1.0 level interface should be assumed.
apilevel: str = "2.0"

# Globals: threadsafety
# https://peps.python.org/pep-0249/#threadsafety
# Integer constant stating the level of thread safety the interface supports.
# Possible values are:
# 0 - Threads may not share the module.
# 1 - Threads may share the module, but not connections.
# 2 - Threads may share the module and connections.
# 3 - Threads may share the module, connections and cursors.
threadsafety: int = 1

# Globals: paramstyle
# https://peps.python.org/pep-0249/#paramstyle
# String constant stating the type of parameter marker formatting expected
# by the interface.
# Possible values are
# qmark - Question mark style, e.g. ...WHERE name=?
# numeric - Numeric, positional style, e.g. ...WHERE name=:1
# named - Named style, e.g. ...WHERE name=:name
# format - ANSI C printf format codes, e.g. ...WHERE name=%s
# pyformat - Python extended format codes, e.g. ...WHERE name=%(name)s
paramstyle: str = "pyformat"
