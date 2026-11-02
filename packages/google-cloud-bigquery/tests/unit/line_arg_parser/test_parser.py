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
def parser_class():
    from google.cloud.bigquery.magics.line_arg_parser.parser import Parser

    return Parser


def test_consume_expected_eol(parser_class):
    from google.cloud.bigquery.magics.line_arg_parser import TokenType
    from google.cloud.bigquery.magics.line_arg_parser.lexer import Token

    # A simple iterable of Tokens is sufficient.
    fake_lexer = [Token(TokenType.EOL, lexeme="", pos=0)]
    parser = parser_class(fake_lexer)

    parser.consume(TokenType.EOL)  # no error


def test_consume_unexpected_eol(parser_class):
    from google.cloud.bigquery.magics.line_arg_parser import ParseError
    from google.cloud.bigquery.magics.line_arg_parser import TokenType
    from google.cloud.bigquery.magics.line_arg_parser.lexer import Token

    # A simple iterable of Tokens is sufficient.
    fake_lexer = [Token(TokenType.EOL, lexeme="", pos=0)]
    parser = parser_class(fake_lexer)

    with pytest.raises(ParseError, match=r"Unexpected end of input.*expected.*COLON.*"):
        parser.consume(TokenType.COLON)


def test_input_line_unexpected_input(parser_class):
    from google.cloud.bigquery.magics.line_arg_parser import ParseError
    from google.cloud.bigquery.magics.line_arg_parser import TokenType
    from google.cloud.bigquery.magics.line_arg_parser.lexer import Token

    # A simple iterable of Tokens is sufficient.
    fake_lexer = [
        Token(TokenType.DEST_VAR, lexeme="results", pos=0),
        Token(TokenType.UNKNOWN, lexeme="boo!", pos=8),
        Token(TokenType.EOL, lexeme="", pos=12),
    ]
    parser = parser_class(fake_lexer)

    with pytest.raises(ParseError, match=r"Unexpected input.*position 8.*boo!.*"):
        parser.input_line()


def test_destination_var_unexpected_input(parser_class):
    from google.cloud.bigquery.magics.line_arg_parser import ParseError
    from google.cloud.bigquery.magics.line_arg_parser import TokenType
    from google.cloud.bigquery.magics.line_arg_parser.lexer import Token

    # A simple iterable of Tokens is sufficient.
    fake_lexer = [
        Token(TokenType.UNKNOWN, lexeme="@!#", pos=2),
        Token(TokenType.EOL, lexeme="", pos=5),
    ]
    parser = parser_class(fake_lexer)

    with pytest.raises(ParseError, match=r"Unknown.*position 2.*@!#.*"):
        parser.destination_var()


def test_option_value_unexpected_input(parser_class):
    from google.cloud.bigquery.magics.line_arg_parser import ParseError
    from google.cloud.bigquery.magics.line_arg_parser import TokenType
    from google.cloud.bigquery.magics.line_arg_parser.lexer import Token

    # A simple iterable of Tokens is sufficient.
    fake_lexer = [
        Token(TokenType.UNKNOWN, lexeme="@!#", pos=8),
        Token(TokenType.OPTION_SPEC, lexeme="--foo", pos=13),
    ]
    parser = parser_class(fake_lexer)

    with pytest.raises(ParseError, match=r"Unknown input.*position 8.*@!#.*"):
        parser.option_value()


def test_dict_items_empty_dict(parser_class):
    from google.cloud.bigquery.magics.line_arg_parser import TokenType
    from google.cloud.bigquery.magics.line_arg_parser.lexer import Token

    # A simple iterable of Tokens is sufficient.
    fake_lexer = [Token(TokenType.RCURL, lexeme="}", pos=22)]
    parser = parser_class(fake_lexer)

    result = parser.dict_items()

    assert result == []


def test_dict_items_trailing_comma(parser_class):
    from google.cloud.bigquery.magics.line_arg_parser import TokenType
    from google.cloud.bigquery.magics.line_arg_parser.lexer import Token

    # A simple iterable of Tokens is sufficient.
    fake_lexer = [
        Token(TokenType.PY_STRING, lexeme="'age'", pos=10),
        Token(TokenType.COLON, lexeme=":", pos=17),
        Token(TokenType.PY_NUMBER, lexeme="18", pos=19),
        Token(TokenType.COMMA, lexeme=",", pos=21),
        Token(TokenType.RCURL, lexeme="}", pos=22),
    ]
    parser = parser_class(fake_lexer)

    result = parser.dict_items()

    assert len(result) == 1
    dict_item = result[0]
    assert dict_item.key.key_value == "'age'"
    assert dict_item.value.raw_value == "18"


def test_dict_item_unknown_input(parser_class):
    from google.cloud.bigquery.magics.line_arg_parser import ParseError
    from google.cloud.bigquery.magics.line_arg_parser import TokenType
    from google.cloud.bigquery.magics.line_arg_parser.lexer import Token

    # A simple iterable of Tokens is sufficient.
    fake_lexer = [Token(TokenType.UNKNOWN, lexeme="#/%", pos=35)]
    parser = parser_class(fake_lexer)

    with pytest.raises(ParseError, match=r"Unknown.*position 35.*#/%.*"):
        parser.dict_item()


def test_pyvalue_list_containing_dict(parser_class):
    from google.cloud.bigquery.magics.line_arg_parser import TokenType
    from google.cloud.bigquery.magics.line_arg_parser.lexer import Token
    from google.cloud.bigquery.magics.line_arg_parser.parser import PyDict
    from google.cloud.bigquery.magics.line_arg_parser.parser import PyList

    # A simple iterable of Tokens is sufficient.
    fake_lexer = [
        Token(TokenType.LSQUARE, lexeme="[", pos=21),
        Token(TokenType.LCURL, lexeme="{", pos=22),
        Token(TokenType.PY_STRING, lexeme="'age'", pos=23),
        Token(TokenType.COLON, lexeme=":", pos=28),
        Token(TokenType.PY_NUMBER, lexeme="18", pos=30),
        Token(TokenType.RCURL, lexeme="}", pos=32),
        Token(TokenType.COMMA, lexeme=",", pos=33),  # trailing comma
        Token(TokenType.RSQUARE, lexeme="]", pos=34),
        Token(TokenType.EOL, lexeme="", pos=40),
    ]
    parser = parser_class(fake_lexer)

    result = parser.py_value()

    assert isinstance(result, PyList)
    assert len(result.items) == 1

    element = result.items[0]
    assert isinstance(element, PyDict)
    assert len(element.items) == 1

    dict_item = element.items[0]
    assert dict_item.key.key_value == "'age'"
    assert dict_item.value.raw_value == "18"


def test_pyvalue_invalid_token(parser_class):
    from google.cloud.bigquery.magics.line_arg_parser import ParseError
    from google.cloud.bigquery.magics.line_arg_parser import TokenType
    from google.cloud.bigquery.magics.line_arg_parser.lexer import Token

    # A simple iterable of Tokens is sufficient.
    fake_lexer = [Token(TokenType.OPTION_SPEC, lexeme="--verbose", pos=75)]
    parser = parser_class(fake_lexer)

    error_pattern = r"Unexpected token.*OPTION_SPEC.*position 75.*"
    with pytest.raises(ParseError, match=error_pattern):
        parser.py_value()


def test_collection_items_empty(parser_class):
    from google.cloud.bigquery.magics.line_arg_parser import TokenType
    from google.cloud.bigquery.magics.line_arg_parser.lexer import Token

    # A simple iterable of Tokens is sufficient.
    fake_lexer = [Token(TokenType.RPAREN, lexeme=")", pos=30)]
    parser = parser_class(fake_lexer)

    result = parser.collection_items()

    assert result == []
