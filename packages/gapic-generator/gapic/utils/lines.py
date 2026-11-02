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

import re
import textwrap
from typing import Iterable, Optional


NUMBERED_LIST_REGEX = r"^\d+\. "


def sort_lines(text: str, dedupe: bool = True) -> str:
    """Sort the individual lines of a block of text.

    Args:
        dedupe (bool): Remove duplicate lines with the same text.
            Useful for dealing with import statements in templates.
    """
    # Preserve leading or trailing newlines.
    leading = "\n" if text.startswith("\n") else ""
    trailing = "\n" if text.endswith("\n") else ""

    # Split the text into individual lines, throwing away any empty lines.
    lines: Iterable[str] = (i for i in text.strip().split("\n") if i.strip())

    # De-duplicate the lines if requested.
    if dedupe:
        lines = set(lines)

    # Return the final string.
    answer = "\n".join(sorted(lines))
    return f"{leading}{answer}{trailing}"


def get_subsequent_line_indentation_level(list_item: str) -> int:
    """
    Given a list item return the indentation level for subsequent lines.
    For example, if it is a numbered list, the indentation level should be 3
    as shown below.

    Here subsequent lines should be indented by 2

    - The quick brown fox jumps over the lazy dog. The quick brown fox jumps
      over the lazy dog

    Here subsequent lines should be indented by 2

    + The quick brown fox jumps over the lazy dog. The quick brown fox jumps
      over the lazy dog

    Here subsequent lines should be indented by 4 to cater for double digits

    1.  The quick brown fox jumps over the lazy dog. The quick brown fox jumps
        over the lazy dog

    22. The quick brown fox jumps over the lazy dog. The quick brown fox jumps
        over the lazy dog
    """
    if len(list_item) >= 2 and list_item[0:2] in ["- ", "+ "]:
        indentation_level = 2
    elif len(list_item) >= 4 and re.match(NUMBERED_LIST_REGEX, list_item):
        indentation_level = 4
    else:
        # Don't use any intentation level if the list item marker is not known
        indentation_level = 0
    return indentation_level


def is_list_item(list_item: str) -> bool:
    """
    Given a string return a boolean indicating whether a list is identified.
    """
    if len(list_item) < 3:
        return False
    return (
        list_item.startswith("- ")
        or list_item.startswith("+ ")
        or bool(re.match(NUMBERED_LIST_REGEX, list_item))
    )


def wrap(
    text: str, width: int, *, offset: Optional[int] = None, indent: int = 0
) -> str:
    """Wrap the given string to the given width.

    This uses :meth:`textwrap.fill` under the hood, but provides useful
    offset functionality for Jinja templates.

    This is provided to all templates as the ``wrap`` filter.

    Args:
        text (str): The initial text string.
        width (int): The width at which to wrap the text. If offset is
            provided, these are automatically counted against this.
        offset (int): The offset for the first line of text.
            This value is subtracted from ``width`` for the first line
            only, and is intended to represent the vertical position of
            the first line as already present in the template.
            Defaults to the value of ``indent``.
        indent (int): The number of spaces to indent all lines after the
            first one.

    Returns:
        str: The wrapped string.
    """
    # Quick check: If there is empty text, abort.
    if not text:
        return ""

    # If the offset is None, default it to the indent value.
    if offset is None:
        offset = indent

    # Protocol buffers preserves single initial spaces after line breaks
    # when parsing comments (such as the space before the "w" in "when" here).
    # Re-wrapping causes these to be two spaces; correct for this.
    text = text.replace("\n ", "\n")

    # Break off the first line of the string to address non-zero offsets.
    first = text.split("\n")[0] + "\n"

    # Ensure that there are 2 new lines after a colon, otherwise
    # the sphinx docs build will fail.
    if first.endswith(":\n"):
        first += "\n"

    if len(first) > width - offset:
        # Ensure `break_on_hyphens` is set to `False` when using
        # `textwrap.wrap` to avoid breaking hyperlinks with hyphens.
        initial = textwrap.wrap(
            first,
            break_long_words=False,
            width=width - offset,
            break_on_hyphens=False,
        )
        # Strip the first \n from the text so it is not misidentified as an
        # intentionally short line below, except when the text contains a list,
        # as the new line is required for lists. Look for a list item marker in
        # the remaining text which indicates that a list is present.
        if "\n" in text:
            remaining_text = "".join(text.split("\n")[1:])
            if not is_list_item(remaining_text.strip()):
                text = text.replace("\n", " ", 1)

        # Save the new `first` line.
        first = f"{initial[0]}\n"

    # Ensure that there are 2 new lines after a colon, otherwise
    # the sphinx docs build will fail.
    text = re.sub(r":\n([^\n])", r":\n\n\1", text)

    text = text[len(first) :]
    if not text:
        return first.strip()

    # Strip leading and ending whitespace.
    # Preserve new line at the beginning.
    new_line = "\n" if text[0] == "\n" else ""
    text = new_line + text.strip()

    # Tokenize the rest of the text to try to preserve line breaks
    # that semantically matter.
    tokens = []
    token = ""
    for line in text.split("\n"):
        # Ensure that lines that start with a list item marker are always on a new line
        # Ensure that blank lines are preserved
        if (is_list_item(line.strip()) or not len(line)) and token:
            tokens.append(token)
            token = ""
        token += line + "\n"

        # Preserve line breaks for lines that are short or end with colon.
        if len(line) < width * 0.75 or line.endswith(":"):
            tokens.append(token)
            token = ""
    if token:
        tokens.append(token)

    # Wrap the remainder of the string at the desired width.
    return "{first}{text}".format(
        first=first,
        # Ensure `break_on_hyphens` is set to `False` when using
        # `textwrap.fill` to avoid breaking hyperlinks with hyphens.
        text="\n".join(
            [
                textwrap.fill(
                    break_long_words=False,
                    initial_indent=" " * indent,
                    # ensure that subsequent lines for lists are indented 2 spaces
                    subsequent_indent=" " * indent
                    + " " * get_subsequent_line_indentation_level(token.strip()),
                    text=token,
                    width=width,
                    break_on_hyphens=False,
                )
                for token in tokens
            ]
        ),
    ).rstrip("\n")
