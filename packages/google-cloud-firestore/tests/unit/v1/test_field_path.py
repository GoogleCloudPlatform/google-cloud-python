# -*- coding: utf-8 -*-
# Copyright 2018 Google LLC
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

import mock
import pytest


def _expect_tokenize_field_path(path, split_path):
    from google.cloud.firestore_v1 import field_path

    assert list(field_path._tokenize_field_path(path)) == split_path


def test__tokenize_field_path_w_empty():
    _expect_tokenize_field_path("", [])


def test__tokenize_field_path_w_single_dot():
    _expect_tokenize_field_path(".", ["."])


def test__tokenize_field_path_w_single_simple():
    _expect_tokenize_field_path("abc", ["abc"])


def test__tokenize_field_path_w_single_quoted():
    _expect_tokenize_field_path("`c*de`", ["`c*de`"])


def test__tokenize_field_path_w_quoted_embedded_dot():
    _expect_tokenize_field_path("`c*.de`", ["`c*.de`"])


def test__tokenize_field_path_w_quoted_escaped_backtick():
    _expect_tokenize_field_path(r"`c*\`de`", [r"`c*\`de`"])


def test__tokenize_field_path_w_dotted_quoted():
    _expect_tokenize_field_path("`*`.`~`", ["`*`", ".", "`~`"])


def test__tokenize_field_path_w_dotted():
    _expect_tokenize_field_path("a.b.`c*de`", ["a", ".", "b", ".", "`c*de`"])


def test__tokenize_field_path_w_dotted_escaped():
    _expect_tokenize_field_path("_0.`1`.`+2`", ["_0", ".", "`1`", ".", "`+2`"])


def test__tokenize_field_path_w_unconsumed_characters():
    from google.cloud.firestore_v1 import field_path

    path = "a~b"
    with pytest.raises(ValueError):
        list(field_path._tokenize_field_path(path))


def test_split_field_path_w_single_dot():
    from google.cloud.firestore_v1 import field_path

    with pytest.raises(ValueError):
        field_path.split_field_path(".")


def test_split_field_path_w_leading_dot():
    from google.cloud.firestore_v1 import field_path

    with pytest.raises(ValueError):
        field_path.split_field_path(".a.b.c")


def test_split_field_path_w_trailing_dot():
    from google.cloud.firestore_v1 import field_path

    with pytest.raises(ValueError):
        field_path.split_field_path("a.b.")


def test_split_field_path_w_missing_dot():
    from google.cloud.firestore_v1 import field_path

    with pytest.raises(ValueError):
        field_path.split_field_path("a`c*de`f")


def test_split_field_path_w_half_quoted_field():
    from google.cloud.firestore_v1 import field_path

    with pytest.raises(ValueError):
        field_path.split_field_path("`c*de")


def test_split_field_path_w_empty():
    from google.cloud.firestore_v1 import field_path

    assert field_path.split_field_path("") == []


def test_split_field_path_w_simple_field():
    from google.cloud.firestore_v1 import field_path

    assert field_path.split_field_path("a") == ["a"]


def test_split_field_path_w_dotted_field():
    from google.cloud.firestore_v1 import field_path

    assert field_path.split_field_path("a.b.cde") == ["a", "b", "cde"]


def test_split_field_path_w_quoted_field():
    from google.cloud.firestore_v1 import field_path

    assert field_path.split_field_path("a.b.`c*de`") == ["a", "b", "`c*de`"]


def test_split_field_path_w_quoted_field_escaped_backtick():
    from google.cloud.firestore_v1 import field_path

    assert field_path.split_field_path(r"`c*\`de`") == [r"`c*\`de`"]


def test_parse_field_path_wo_escaped_names():
    from google.cloud.firestore_v1 import field_path

    assert field_path.parse_field_path("a.b.c") == ["a", "b", "c"]


def test_parse_field_path_w_escaped_backtick():
    from google.cloud.firestore_v1 import field_path

    assert field_path.parse_field_path("`a\\`b`.c.d") == ["a`b", "c", "d"]


def test_parse_field_path_w_escaped_backslash():
    from google.cloud.firestore_v1 import field_path

    assert field_path.parse_field_path("`a\\\\b`.c.d") == ["a\\b", "c", "d"]


def test_parse_field_path_w_first_name_escaped_wo_closing_backtick():
    from google.cloud.firestore_v1 import field_path

    with pytest.raises(ValueError):
        field_path.parse_field_path("`a\\`b.c.d")


def test_render_field_path_w_empty():
    from google.cloud.firestore_v1 import field_path

    assert field_path.render_field_path([]) == ""


def test_render_field_path_w_one_simple():
    from google.cloud.firestore_v1 import field_path

    assert field_path.render_field_path(["a"]) == "a"


def test_render_field_path_w_one_starts_w_digit():
    from google.cloud.firestore_v1 import field_path

    assert field_path.render_field_path(["0abc"]) == "`0abc`"


def test_render_field_path_w_one_w_non_alphanum():
    from google.cloud.firestore_v1 import field_path

    assert field_path.render_field_path(["a b c"]) == "`a b c`"


def test_render_field_path_w_one_w_backtick():
    from google.cloud.firestore_v1 import field_path

    assert field_path.render_field_path(["a`b"]) == "`a\\`b`"


def test_render_field_path_w_one_w_backslash():
    from google.cloud.firestore_v1 import field_path

    assert field_path.render_field_path(["a\\b"]) == "`a\\\\b`"


def test_render_field_path_multiple():
    from google.cloud.firestore_v1 import field_path

    assert field_path.render_field_path(["a", "b", "c"]) == "a.b.c"


DATA = {
    "top1": {"middle2": {"bottom3": 20, "bottom4": 22}, "middle5": True},
    "top6": b"\x00\x01 foo",
}


def test_get_nested_value_simple():
    from google.cloud.firestore_v1 import field_path

    assert field_path.get_nested_value("top1", DATA) is DATA["top1"]


def test_get_nested_value_nested():
    from google.cloud.firestore_v1 import field_path

    assert field_path.get_nested_value("top1.middle2", DATA) is DATA["top1"]["middle2"]
    assert (
        field_path.get_nested_value("top1.middle2.bottom3", DATA)
        is DATA["top1"]["middle2"]["bottom3"]
    )


def test_get_nested_value_missing_top_level():
    from google.cloud.firestore_v1 import field_path
    from google.cloud.firestore_v1.field_path import _FIELD_PATH_MISSING_TOP

    path = "top8"
    with pytest.raises(KeyError) as exc_info:
        field_path.get_nested_value(path, DATA)

    err_msg = _FIELD_PATH_MISSING_TOP.format(path)
    assert exc_info.value.args == (err_msg,)


def test_get_nested_value_missing_key():
    from google.cloud.firestore_v1 import field_path
    from google.cloud.firestore_v1.field_path import _FIELD_PATH_MISSING_KEY

    with pytest.raises(KeyError) as exc_info:
        field_path.get_nested_value("top1.middle2.nope", DATA)

    err_msg = _FIELD_PATH_MISSING_KEY.format("nope", "top1.middle2")
    assert exc_info.value.args == (err_msg,)


def test_get_nested_value_bad_type():
    from google.cloud.firestore_v1 import field_path
    from google.cloud.firestore_v1.field_path import _FIELD_PATH_WRONG_TYPE

    with pytest.raises(KeyError) as exc_info:
        field_path.get_nested_value("top6.middle7", DATA)

    err_msg = _FIELD_PATH_WRONG_TYPE.format("top6", "middle7")
    assert exc_info.value.args == (err_msg,)


def _make_field_path(*args, **kwargs):
    from google.cloud.firestore_v1 import field_path

    return field_path.FieldPath(*args, **kwargs)


def test_fieldpath_ctor_w_none_in_part():
    with pytest.raises(ValueError):
        _make_field_path("a", None, "b")


def test_fieldpath_ctor_w_empty_string_in_part():
    with pytest.raises(ValueError):
        _make_field_path("a", "", "b")


def test_fieldpath_ctor_w_integer_part():
    with pytest.raises(ValueError):
        _make_field_path("a", 3, "b")


def test_fieldpath_ctor_w_list():
    parts = ["a", "b", "c"]
    with pytest.raises(ValueError):
        _make_field_path(parts)


def test_fieldpath_ctor_w_tuple():
    parts = ("a", "b", "c")
    with pytest.raises(ValueError):
        _make_field_path(parts)


def test_fieldpath_ctor_w_iterable_part():
    with pytest.raises(ValueError):
        _make_field_path("a", ["a"], "b")


def test_fieldpath_constructor_w_single_part():
    field_path = _make_field_path("a")
    assert field_path.parts == ("a",)


def test_fieldpath_constructor_w_multiple_parts():
    field_path = _make_field_path("a", "b", "c")
    assert field_path.parts == ("a", "b", "c")


def test_fieldpath_ctor_w_invalid_chars_in_part():
    invalid_parts = ("~", "*", "/", "[", "]", ".")
    for invalid_part in invalid_parts:
        field_path = _make_field_path(invalid_part)
        assert field_path.parts == (invalid_part,)


def test_fieldpath_ctor_w_double_dots():
    field_path = _make_field_path("a..b")
    assert field_path.parts == ("a..b",)


def test_fieldpath_ctor_w_unicode():
    field_path = _make_field_path("一", "二", "三")
    assert field_path.parts == ("一", "二", "三")


def test_fieldpath_from_api_repr_w_empty_string():
    from google.cloud.firestore_v1 import field_path

    api_repr = ""
    with pytest.raises(ValueError):
        field_path.FieldPath.from_api_repr(api_repr)


def test_fieldpath_from_api_repr_w_empty_field_name():
    from google.cloud.firestore_v1 import field_path

    api_repr = "a..b"
    with pytest.raises(ValueError):
        field_path.FieldPath.from_api_repr(api_repr)


def test_fieldpath_from_api_repr_w_invalid_chars():
    from google.cloud.firestore_v1 import field_path

    invalid_parts = ("~", "*", "/", "[", "]", ".")
    for invalid_part in invalid_parts:
        with pytest.raises(ValueError):
            field_path.FieldPath.from_api_repr(invalid_part)


def test_fieldpath_from_api_repr_w_ascii_single():
    from google.cloud.firestore_v1 import field_path

    api_repr = "a"
    field_path = field_path.FieldPath.from_api_repr(api_repr)
    assert field_path.parts == ("a",)


def test_fieldpath_from_api_repr_w_ascii_dotted():
    from google.cloud.firestore_v1 import field_path

    api_repr = "a.b.c"
    field_path = field_path.FieldPath.from_api_repr(api_repr)
    assert field_path.parts == ("a", "b", "c")


def test_fieldpath_from_api_repr_w_non_ascii_dotted_non_quoted():
    from google.cloud.firestore_v1 import field_path

    api_repr = "a.一"
    with pytest.raises(ValueError):
        field_path.FieldPath.from_api_repr(api_repr)


def test_fieldpath_from_api_repr_w_non_ascii_dotted_quoted():
    from google.cloud.firestore_v1 import field_path

    api_repr = "a.`一`"
    field_path = field_path.FieldPath.from_api_repr(api_repr)
    assert field_path.parts == ("a", "一")


def test_fieldpath_from_string_w_empty_string():
    from google.cloud.firestore_v1 import field_path

    path_string = ""
    with pytest.raises(ValueError):
        field_path.FieldPath.from_string(path_string)


def test_fieldpath_from_string_w_empty_field_name():
    from google.cloud.firestore_v1 import field_path

    path_string = "a..b"
    with pytest.raises(ValueError):
        field_path.FieldPath.from_string(path_string)


def test_fieldpath_from_string_w_leading_dot():
    from google.cloud.firestore_v1 import field_path

    path_string = ".b.c"
    with pytest.raises(ValueError):
        field_path.FieldPath.from_string(path_string)


def test_fieldpath_from_string_w_trailing_dot():
    from google.cloud.firestore_v1 import field_path

    path_string = "a.b."
    with pytest.raises(ValueError):
        field_path.FieldPath.from_string(path_string)


def test_fieldpath_from_string_w_leading_invalid_chars():
    from google.cloud.firestore_v1 import field_path

    invalid_paths = ("~", "*", "/", "[", "]")
    for invalid_path in invalid_paths:
        path = field_path.FieldPath.from_string(invalid_path)
        assert path.parts == (invalid_path,)


def test_fieldpath_from_string_w_embedded_invalid_chars():
    from google.cloud.firestore_v1 import field_path

    invalid_paths = ("a~b", "x*y", "f/g", "h[j", "k]l")
    for invalid_path in invalid_paths:
        with pytest.raises(ValueError):
            field_path.FieldPath.from_string(invalid_path)


def test_fieldpath_from_string_w_ascii_single():
    from google.cloud.firestore_v1 import field_path

    path_string = "a"
    field_path = field_path.FieldPath.from_string(path_string)
    assert field_path.parts == ("a",)


def test_fieldpath_from_string_w_ascii_dotted():
    from google.cloud.firestore_v1 import field_path

    path_string = "a.b.c"
    field_path = field_path.FieldPath.from_string(path_string)
    assert field_path.parts == ("a", "b", "c")


def test_fieldpath_from_string_w_non_ascii_dotted():
    from google.cloud.firestore_v1 import field_path

    path_string = "a.一"
    field_path = field_path.FieldPath.from_string(path_string)
    assert field_path.parts == ("a", "一")


def test_fieldpath___hash___w_single_part():
    field_path = _make_field_path("a")
    assert hash(field_path) == hash("a")


def test_fieldpath___hash___w_multiple_parts():
    field_path = _make_field_path("a", "b")
    assert hash(field_path) == hash("a.b")


def test_fieldpath___hash___w_escaped_parts():
    field_path = _make_field_path("a", "3")
    assert hash(field_path) == hash("a.`3`")


def test_fieldpath___eq___w_matching_type():
    from google.cloud.firestore_v1 import field_path

    path = _make_field_path("a", "b")
    string_path = field_path.FieldPath.from_string("a.b")
    assert path == string_path


def test_fieldpath___eq___w_non_matching_type():
    field_path = _make_field_path("a", "c")
    other = mock.Mock()
    other.parts = "a", "b"
    assert field_path != other


def test_fieldpath___lt___w_matching_type():
    from google.cloud.firestore_v1 import field_path

    path = _make_field_path("a", "b")
    string_path = field_path.FieldPath.from_string("a.c")
    assert path < string_path


def test_fieldpath___lt___w_non_matching_type():
    field_path = _make_field_path("a", "b")
    other = object()
    # Python 2 doesn't raise TypeError here, but Python3 does.
    assert field_path.__lt__(other) is NotImplemented


def test_fieldpath___add__():
    path1 = "a123", "b456"
    path2 = "c789", "d012"
    path3 = "c789.d012"
    field_path1 = _make_field_path(*path1)
    field_path1_string = _make_field_path(*path1)
    field_path2 = _make_field_path(*path2)
    field_path1 += field_path2
    field_path1_string += path3
    field_path2 = field_path2 + _make_field_path(*path1)
    assert field_path1 == _make_field_path(*(path1 + path2))
    assert field_path2 == _make_field_path(*(path2 + path1))
    assert field_path1_string == field_path1
    assert field_path1 != field_path2
    with pytest.raises(TypeError):
        field_path1 + 305


def test_fieldpath_to_api_repr_a():
    parts = "a"
    field_path = _make_field_path(parts)
    assert field_path.to_api_repr() == "a"


def test_fieldpath_to_api_repr_backtick():
    parts = "`"
    field_path = _make_field_path(parts)
    assert field_path.to_api_repr() == r"`\``"


def test_fieldpath_to_api_repr_dot():
    parts = "."
    field_path = _make_field_path(parts)
    assert field_path.to_api_repr() == "`.`"


def test_fieldpath_to_api_repr_slash():
    parts = "\\"
    field_path = _make_field_path(parts)
    assert field_path.to_api_repr() == r"`\\`"


def test_fieldpath_to_api_repr_double_slash():
    parts = r"\\"
    field_path = _make_field_path(parts)
    assert field_path.to_api_repr() == r"`\\\\`"


def test_fieldpath_to_api_repr_underscore():
    parts = "_33132"
    field_path = _make_field_path(parts)
    assert field_path.to_api_repr() == "_33132"


def test_fieldpath_to_api_repr_unicode_non_simple():
    parts = "一"
    field_path = _make_field_path(parts)
    assert field_path.to_api_repr() == "`一`"


def test_fieldpath_to_api_repr_number_non_simple():
    parts = "03"
    field_path = _make_field_path(parts)
    assert field_path.to_api_repr() == "`03`"


def test_fieldpath_to_api_repr_simple_with_dot():
    field_path = _make_field_path("a.b")
    assert field_path.to_api_repr() == "`a.b`"


def test_fieldpath_to_api_repr_non_simple_with_dot():
    parts = "a.一"
    field_path = _make_field_path(parts)
    assert field_path.to_api_repr() == "`a.一`"


def test_fieldpath_to_api_repr_simple():
    parts = "a0332432"
    field_path = _make_field_path(parts)
    assert field_path.to_api_repr() == "a0332432"


def test_fieldpath_to_api_repr_chain():
    parts = "a", "`", "\\", "_3", "03", "a03", "\\\\", "a0332432", "一"
    field_path = _make_field_path(*parts)
    assert field_path.to_api_repr() == r"a.`\``.`\\`._3.`03`.a03.`\\\\`.a0332432.`一`"


def test_fieldpath_eq_or_parent_same():
    field_path = _make_field_path("a", "b")
    other = _make_field_path("a", "b")
    assert field_path.eq_or_parent(other)


def test_fieldpath_eq_or_parent_prefix():
    field_path = _make_field_path("a", "b")
    other = _make_field_path("a", "b", "c")
    assert field_path.eq_or_parent(other)
    assert other.eq_or_parent(field_path)


def test_fieldpath_eq_or_parent_no_prefix():
    field_path = _make_field_path("a", "b")
    other = _make_field_path("d", "e", "f")
    assert not field_path.eq_or_parent(other)
    assert not other.eq_or_parent(field_path)


def test_fieldpath_lineage_empty():
    field_path = _make_field_path()
    expected = set()
    assert field_path.lineage() == expected


def test_fieldpath_lineage_single():
    field_path = _make_field_path("a")
    expected = set()
    assert field_path.lineage() == expected


def test_fieldpath_lineage_nested():
    field_path = _make_field_path("a", "b", "c")
    expected = set([_make_field_path("a"), _make_field_path("a", "b")])
    assert field_path.lineage() == expected


def test_fieldpath_document_id():
    parts = "__name__"
    field_path = _make_field_path(parts)
    assert field_path.document_id() == parts
