# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest

IPython = pytest.importorskip("IPython")


@pytest.fixture(scope="session")
def lexer_class():
    from google.cloud.bigquery.magics.line_arg_parser.lexer import Lexer

    return Lexer


def test_empy_input(lexer_class):
    from google.cloud.bigquery.magics.line_arg_parser import TokenType
    from google.cloud.bigquery.magics.line_arg_parser.lexer import Token

    lexer = lexer_class("")
    tokens = list(lexer)

    assert tokens == [Token(TokenType.EOL, lexeme="", pos=0)]
