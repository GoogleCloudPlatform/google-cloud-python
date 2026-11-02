# Copyright 2018 Google LLC
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

from gapic.utils import lines


def test_sort_lines():
    assert (
        lines.sort_lines(
            "import foo\nimport bar",
        )
        == "import bar\nimport foo"
    )


def test_sort_lines_keeps_leading_newline():
    assert (
        lines.sort_lines(
            "\nimport foo\nimport bar",
        )
        == "\nimport bar\nimport foo"
    )


def test_sort_lines_keeps_trailing_newline():
    assert (
        lines.sort_lines(
            "import foo\nimport bar\n",
        )
        == "import bar\nimport foo\n"
    )


def test_sort_lines_eliminates_blank_lines():
    assert (
        lines.sort_lines(
            "import foo\n\n\nimport bar",
        )
        == "import bar\nimport foo"
    )


def test_sort_lines_dedupe():
    assert (
        lines.sort_lines(
            "import foo\nimport bar\nimport foo",
        )
        == "import bar\nimport foo"
    )


def test_sort_lines_no_dedupe():
    assert (
        lines.sort_lines(
            "import foo\nimport bar\nimport foo",
            dedupe=False,
        )
        == "import bar\nimport foo\nimport foo"
    )


def test_wrap_noop():
    assert lines.wrap("foo bar baz", width=80) == "foo bar baz"


def test_wrap_empty_text():
    assert lines.wrap("", width=80) == ""


def test_wrap_simple():
    assert lines.wrap("foo bar baz", width=5) == "foo\nbar\nbaz"


def test_wrap_strips():
    assert lines.wrap("foo bar baz  ", width=80) == "foo bar baz"


def test_wrap_subsequent_offset():
    assert (
        lines.wrap(
            "foo bar baz",
            width=5,
            offset=0,
            indent=2,
        )
        == "foo\n  bar\n  baz"
    )


def test_wrap_initial_offset():
    assert (
        lines.wrap(
            "The hail in Wales falls mainly on the snails.",
            width=20,
            offset=12,
            indent=0,
        )
        == "The hail\nin Wales falls\nmainly on the\nsnails."
    )


def test_wrap_indent_short():
    assert lines.wrap("foo bar", width=30, indent=10) == "foo bar"


def test_wrap_short_line_preserved():
    assert lines.wrap("foo\nbar\nbaz", width=80) == "foo\nbar\nbaz"


def test_wrap_does_not_break_hyphenated_word():
    assert lines.wrap("do-not-break", width=5) == "do-not-break"


def test_wrap_with_short_lines():
    input = """The hail in Wales falls mainly on the snails. The hail in Wales falls mainly
on the snails."""
    expected = """The hail in Wales falls mainly on the snails. The hail in
Wales falls mainly on the snails."""
    assert lines.wrap(input, width=60) == expected


def test_lines_which_have_2_spaces_following_period():
    input = """Information related to the a standard versioned package.  This includes
package info for APT, Yum, Zypper, and Googet package managers."""
    expected = """Information related to the a standard versioned package.
This includes package info for APT, Yum, Zypper, and Googet
package managers."""
    assert lines.wrap(input, width=60) == expected


def test_list_each_item_in_list_has_new_line():
    input = """Type of weather:
- Hail
- Rain Rain Rain Rain Rain Rain Rain Rain Rain Rain Rain Rain
- Snow"""
    expected = """Type of weather:

- Hail
- Rain Rain Rain Rain Rain Rain Rain Rain Rain Rain Rain Rain
- Snow"""
    assert lines.wrap(input, width=80) == expected


def test_list_items_are_indented():
    input = """Type of weather.
Some types of weather:

- A mix of hail and snow, followed by rain clouds, then finally clear sky
- Rain
- Snow"""
    expected = """Type of weather.
Some types of weather:

- A mix of hail and snow, followed by rain clouds, then
  finally clear sky
- Rain
- Snow"""
    assert lines.wrap(input, width=60) == expected


def test_list_items_short_text_before_list_with_new_line_preserved():
    input = """Today's forecast will have different types of weather:

- A mix of hail and snow, followed by rain clouds, then finally clear sky
- Rain
- Snow"""
    expected = """Today's forecast will have different types
                of weather:

                - A mix of hail and snow, followed by rain
                  clouds, then finally clear sky
                - Rain
                - Snow"""
    assert lines.wrap(input, width=60, indent=16) == expected


def test_list_items_long_text_before_list_with_new_line_preserved():
    input = """Weather Weather Weather Weather Weather Weather Weather
Weather Weather Weather Weather Weather Weather Type of weather:

- Hail
- Rain Rain Rain Rain Rain Rain Rain Rain Rain Rain Rain Rain
- Snow"""
    expected = """Weather Weather Weather Weather Weather Weather Weather
Weather Weather Weather Weather Weather Weather Type of
weather:

- Hail
- Rain Rain Rain Rain Rain Rain Rain Rain Rain Rain Rain
  Rain
- Snow"""
    assert lines.wrap(input, width=60) == expected


def test_new_line_added_short_text_before_list():
    input = """Today's forecast will have different weather:
- A mix of hail and snow, followed by rain clouds, then finally clear sky
- Rain
- Snow"""
    expected = """Today's forecast will have different weather:

- A mix of hail and snow, followed by rain clouds, then
  finally clear sky
- Rain
- Snow"""
    assert lines.wrap(input, width=60) == expected


def test_new_line_preserved_short_text_before_list_without_colon():
    input = """Today's forecast will have different weather.

- A mix of hail and snow, followed by rain clouds, then finally clear sky
- Rain
- Snow"""
    expected = """Today's forecast will have different weather.

- A mix of hail and snow, followed by rain clouds, then
  finally clear sky
- Rain
- Snow"""
    assert lines.wrap(input, width=60) == expected


def test_list_with_multiple_paragraphs():
    input = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec porta euismod est a viverra. Integer vulputate ipsum id lacus tincidunt, id tincidunt tortor ullamcorper. Vestibulum facilisis at nulla nec lobortis. Nunc consectetur suscipit lacus id aliquam.

Donec et urna aliquam, efficitur mauris et, consectetur enim. Aliquam aliquet turpis eget erat gravida condimentum. Sed vel feugiat risus.

Sed interdum.

Convallis turpis nec congue. Integer vulputate sed urna eu mollis. Mauris in congue nisi, sed pellentesque ex.

- Ut vestibulum
- consequat imperdiet
- Integer rhoncus varius. Ante, ac tempus augue
finibus sit amet. Integer ac fermentum neque, a sodales nibh. Mauris et dictum ipsum. Integer sit amet posuere urna. Nullam cursus molestie posuere. Praesent imperdiet cursus purus, in posuere odio. 
- Orci varius natoque penatibus et

Aagnis dis parturient montes, nascetur ridiculus mus. Mauris mattis turpis quis hendrerit gravida. Curabitur nec diam erat. In nec est nisl. Quisque ut orci efficitur, vestibulum ante non, vestibulum erat. Donec mollis ultricies nisl."""
    expected = """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Donec porta euismod est a viverra. Integer vulputate ipsum
id lacus tincidunt, id tincidunt tortor ullamcorper.
Vestibulum facilisis at nulla nec lobortis. Nunc consectetur
suscipit lacus id aliquam.  Donec et urna aliquam, efficitur
mauris et, consectetur enim. Aliquam aliquet turpis eget
erat gravida condimentum. Sed vel feugiat risus.

Sed interdum.

Convallis turpis nec congue. Integer vulputate sed urna eu
mollis. Mauris in congue nisi, sed pellentesque ex.

- Ut vestibulum
- consequat imperdiet
- Integer rhoncus varius. Ante, ac tempus augue finibus sit
  amet. Integer ac fermentum neque, a sodales nibh. Mauris
  et dictum ipsum. Integer sit amet posuere urna. Nullam
  cursus molestie posuere. Praesent imperdiet cursus purus,
  in posuere odio.
- Orci varius natoque penatibus et

Aagnis dis parturient montes, nascetur ridiculus mus. Mauris
mattis turpis quis hendrerit gravida. Curabitur nec diam
erat. In nec est nisl. Quisque ut orci efficitur, vestibulum
ante non, vestibulum erat. Donec mollis ultricies nisl."""
    assert lines.wrap(input, width=60) == expected


def test_list_with_numbered_list():
    input = """Config for video classification human labeling task.
Currently two types of video classification are supported:
1.  Assign labels on the entire video. Assign labels on the entire video.
22. Split the video into multiple video clips based on camera shot, and
assign labels on each video clip."""
    expected = """Config for video classification human labeling task.
Currently two types of video classification are supported:

1.  Assign labels on the entire video. Assign labels on the
    entire video.
22. Split the video into multiple video clips based on
    camera shot, and assign labels on each video clip."""
    assert lines.wrap(input, width=60) == expected


def test_list_with_plus_list_item_marker():
    input = """User-assigned name of the trigger. Must be unique within the project.
Trigger names must meet the following requirements:
+ They must contain only alphanumeric characters and dashes.
+ They can be 1-64 characters long.
+ They must begin and end with an alphanumeric character."""
    expected = """User-assigned name of the trigger. Must
be unique within the project. Trigger
names must meet the following
requirements:

+ They must contain only alphanumeric
  characters and dashes.
+ They can be 1-64 characters long.
+ They must begin and end with an
  alphanumeric character."""
    assert lines.wrap(input, width=40) == expected
