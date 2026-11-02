# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# DO NOT CHANGE this file, except when you need to add a new reserved keyword
# from Python's new major release.
# In an unforseen case if you have to make changes, please follow the process:
# 1. Run the internal script to check if any of the existing Google APIs use the
#   item to be added/removed. For external contributors, ask a Googler to do that
#   during code review.
# 2. If no APIs are using it, it's safe to add. Otherwise, consult with your TL.
#
# Changing this list will lead to breaking changes. This is happening because
# GAPIC will add "_" to field names from that list. This will change the generated
# client library surface (i.e. breaking change). Example of when this happened:
# https://github.com/googleapis/gapic-generator-python/issues/835.

# Each item in the list belongs to one of the following categories:
# 1. Python keyword
# 2. Used in Google APIs at the time of writing this PR
# 3. Reserved word from Protoplus.
RESERVED_NAMES = frozenset(
    [
        "any",
        "format",
        "yield",
        "await",
        "False",
        "return",
        "continue",
        "as",
        "pass",
        "next",
        "class",
        "list",
        "breakpoint",
        "import",
        "mapping",
        "zip",
        "locals",
        "max",
        "and",
        "finally",
        "dir",
        "def",
        "elif",
        "from",
        "nonlocal",
        "min",
        "not",
        "object",
        "global",
        "with",
        "else",
        "__peg_parser__",
        "del",
        "range",
        "open",
        "assert",
        "all",
        "except",
        "while",
        "license",
        "raise",
        "True",
        "lambda",
        "for",
        "or",
        "if",
        "in",
        "async",
        "slice",
        "is",
        "break",
        "hash",
        "None",
        "try",
        "type",
        "exec",
        "help",
        # Comes from Protoplus
        "ignore_unknown_fields",
        "self",  # Refer to PEP8 https://peps.python.org/pep-0008/#function-and-method-arguments
        "cls",  # Refer PEP8 https://peps.python.org/pep-0008/#function-and-method-arguments
    ]
)
