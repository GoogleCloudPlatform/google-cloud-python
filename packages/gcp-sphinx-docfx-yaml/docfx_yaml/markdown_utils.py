# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# -*- coding: utf-8 -*-
"""Markdown related utilities for Sphinx DocFX YAML extension."""

import os
import re
import shutil
from collections.abc import MutableSet
from pathlib import Path
from typing import Iterable

import sphinx.application
from docuploader import shell


def _reformat_codeblocks(content: str) -> str:
    """Formats codeblocks from ``` to <pre>.

    Args:
        content (str): The string to reformat.

    Returns:
        str: The reformatted string.
    """
    triple_backtick = "```"
    current_tag = "<pre>"
    next_tag = "</pre>"
    # If there are no proper pairs of triple backticks, don't format docstring.
    if content.count(triple_backtick) % 2 != 0:
        print(
            f"Docstring is not formatted well, missing proper pairs of triple backticks (```): {content}"
        )
        return content
    while triple_backtick in content:
        content = content.replace(triple_backtick, current_tag, 1)
        # Alternate between replacing with <pre> and </pre>.
        current_tag, next_tag = next_tag, current_tag

    return content


def _reformat_code(content: str) -> str:
    """Formats code from ` to <code>.

    Args:
        content (str): The string to reformat.

    Returns:
        str: The reformatted string.
    """
    reformatted_lines = []

    code_pattern = "`[^`\n]+`"
    code_start = "<code>"
    code_end = "</code>"
    prev_start = prev_end = 0
    # Convert `text` to <code>text</code>
    for matched_obj in re.finditer(code_pattern, content):
        start = matched_obj.start()
        end = matched_obj.end()
        code_content = content[start + 1 : end - 1]

        reformatted_lines.append(content[prev_end:start])
        reformatted_lines.append(f"{code_start}{code_content}{code_end}")
        prev_start, prev_end = start, end

    reformatted_lines.append(content[prev_end:])

    return "".join(reformatted_lines)


def reformat_markdown_to_html(content: str) -> str:
    """Applies changes from markdown syntax to equivalent HTML.

    Acts as a wrapper function to format all Markdown to HTML.

    Markdown syntax cannot be used within HTML elements, and must be converted
    at YAML level.

    Args:
        content: the string to be reformatted.

    Returns:
        Content that has been formatted with proper HTML.
    """

    content = _reformat_codeblocks(content)
    content = _reformat_code(content)

    return content


def _parse_markdown_header(current_line: str, prev_line: str) -> str:
    """Parses the H1 markdown header if found.

    Args:
        current_line: line of markdown text to inspect.
        prev_line: previous line to use if we found line divider for H1.

    Returns:
        Header for the markdown file if valid header is found.
    """
    # Markdown h1 prefix should have only 1 of '#' character followed by exactly one space.
    h1_header_prefix = "# "
    if h1_header_prefix in current_line and current_line.count("#") == 1:
        # Check for proper h1 header formatting, ensure there's more than just
        # the hashtag character, and exactly only one space after the hashtag.
        if (
            not current_line[current_line.index(h1_header_prefix) + 2].isspace()
            and len(current_line) > 2
        ):
            return (
                current_line[current_line.index(h1_header_prefix) :].strip("#").strip()
            )

    elif "=" in current_line:
        # Check if we're inspecting an empty or undefined lines.
        if not prev_line:
            return ""

        # Check if the current line only has equal sign divider.
        if current_line.count("=") == len(current_line.strip()):
            # Update header to the previous line.
            return prev_line.strip()

    return ""


def _extract_header_from_markdown(mdfile: Iterable[str]) -> str:
    """For a given markdown file, extract its header line.

    Args:
        mdfile: iterator to the markdown file.

    Returns:
        A string for header or empty string if header is not found.
    """
    prev_line = ""

    for line in mdfile:
        # Ignore licenses and other non-headers prior to the header.
        # If we've found the header, return the header.
        header = _parse_markdown_header(line, prev_line)
        if header != "":
            return header

        prev_line = line

    return ""


def _remove_license(mdfile_path: str) -> None:
    """Removes any licenses in markdown files.

    Args:
        mdfile_path (str): The path to the markdown file.
    """

    comment_tag_begin = "<!--"
    comment_tag_end = "-->"

    with open(mdfile_path) as mdfile:
        file_content = mdfile.read()

    # Find the first occurrence of comment tags.
    begin_index = file_content.find(comment_tag_begin)
    end_index = file_content.find(comment_tag_end)

    # Check whether the HTML comment is a license - they should be at the top of
    # the file, and if any content prior to the license is visible other than
    # whitespace we assume it's not a license comment.
    if (pre_comment := file_content[:begin_index]) and not pre_comment.isspace():
        return

    # Strip the license.
    file_content = file_content[end_index + len(comment_tag_end) :]

    # Reset file position to the beginning to write
    with open(mdfile_path, "w") as mdfile:
        mdfile.write(file_content)


def _highlight_md_codeblocks(mdfile_path: str) -> None:
    """Adds syntax highlighting to code blocks for a given markdown file.

    Args:
        mdfile_path (str): The path to the markdown file.
    """
    fence = "```"
    fence_with_python = "```python"
    new_lines = []

    with open(mdfile_path) as mdfile:
        file_content = mdfile.read()
        # If there is an odd number of code block annotations, do not syntax
        # highlight.
        if file_content.count(fence) % 2 != 0:
            print(
                f"{mdfile.name} contains wrong format of code blocks. Skipping syntax highlighting."
            )
            return
        # Retrieve code block positions to replace
        codeblocks = [[m.start(), m.end()] for m in re.finditer(fence, file_content)]

        # This is equivalent to grabbing every odd index item.
        codeblocks = codeblocks[::2]
        # Used to store code blocks that come without language indicators.
        blocks_without_indicators = []

        # Check if the fence comes without a language indicator. If so, include
        # this to a list to render.
        for start, end in codeblocks:
            if file_content[end] == "\n":
                blocks_without_indicators.append([start, end])

        # Stitch content that does not need to be parsed, and replace with
        # `fence_with_python` for parsed portions.
        prev_start = prev_end = 0
        for start, end in blocks_without_indicators:
            new_lines.append(file_content[prev_end:start])
            new_lines.append(fence_with_python)
            prev_start, prev_end = start, end

        # Include rest of the content.
        new_lines.append(file_content[prev_end:])

    # Overwrite with newly parsed content.
    with open(mdfile_path, "w") as mdfile:
        new_content = "".join(new_lines)
        mdfile.write(new_content)


def _clean_image_links(mdfile_path: str) -> None:
    """Cleans extra whitespace that breaks image links in index.html file.

    Args:
        mdfile_path (str): The path to the markdown file.
    """
    image_link_pattern = r"\[\s*!\[image\]\(.*\)\s*\]\(.*\)"
    new_lines = []
    with open(mdfile_path) as mdfile:
        file_content = mdfile.read()

        prev_start = prev_end = 0

        for matched_obj in re.finditer(image_link_pattern, file_content):
            start = matched_obj.start()
            end = matched_obj.end()
            matched_str = file_content[start:end]
            # Clean up all whitespaces for the image link.
            clean_str = "".join(matched_str.split())

            new_lines.append(file_content[prev_end:start])
            new_lines.append(clean_str)
            prev_start, prev_end = start, end

        new_lines.append(file_content[prev_end:])

    with open(mdfile_path, "w") as mdfile:
        new_content = "".join(new_lines)
        mdfile.write(new_content)


def _prepend_markdown_header(filename: str, mdfile: Iterable[str]) -> None:
    """Prepends the filename as a Markdown header.

    Args:
        filename: the name of the markdown file to prepend.
        mdfile: iterator to the markdown file that is both readable
          and writable.
    """
    file_content = f"# {filename}\n\n" + mdfile.read()
    # Reset file position to the beginning to write
    mdfile.seek(0)
    mdfile.write(file_content)


def _merge_markdown_content(
    *,
    base_file: str,
    additional_content_file: str,
    prepend_additional_content: bool = False,
) -> None:
    """Merges the Markdown file contents.

    The additional_content_file's contents get appended to the base_file's
    content.

    Args:
        base_file: The base content to append content to.
        additional_content_file: The additional content to be appended to
            the base file.
        prepend_additional_content: Optional. If specified, puts the additional
            content before the base file content.
    """
    try:
        with (
            open(base_file, "r+") as base,
            open(additional_content_file, "r") as additional_content,
        ):
            file_content = (
                f"{additional_content.read()}\n{base.read()}"
                if prepend_additional_content
                else f"{base.read()}\n{additional_content.read()}"
            )
            base.seek(0)
            base.write(file_content)
    except OSError:
        print("Could not open the given files.")
        return


def move_markdown_pages(
    app: sphinx.application,
    outdir: Path,
    cwd: list[str] | None = [],
) -> None:
    """Moves markdown pages to be added to the generated reference documentation.

    Markdown pages may be hand written or auto generated. They're processed
    through a third party library to process markdown, then does further
    processing here then added to the top level of the TOC.

    Args:
        app: Sphinx application.
        outdir: The output directory to move markdown pages to.
    """
    # Use this to ignore markdown files that are unnecessary.
    files_to_ignore = [
        "index.md",  # use readme.md instead
        "reference.md",  # Reference docs overlap with Overview. Will try and incorporate this in later.
        # See https://github.com/googleapis/sphinx-docfx-yaml/issues/106.
        "overview_content.md",  # Content will be merged into summary_overview page.
    ]

    # Use this to move the page but do not add them in the TOC.
    ignore_in_toc = [
        "summary_overview.md",  # Already included in the TOC with other
        # summary pages.
    ]

    files_to_rename = {
        "readme.md": "index.md",
    }

    base_markdown_dir = Path(app.builder.outdir).parent / "markdown"

    markdown_dir = base_markdown_dir.joinpath(*cwd) if cwd else base_markdown_dir

    if not markdown_dir.exists():
        print("There's no markdown file to move.")
        return

    # Used to keep track of the index page entry to insert later.
    index_page_entry = None

    markdown_file_names = {mdfile.name.lower() for mdfile in markdown_dir.iterdir()}

    # If there is an index.md and no readme.md, use the index.md. Otherwise, we ignore the index.md.
    if "index.md" in markdown_file_names and "readme.md" not in markdown_file_names:
        files_to_ignore.remove("index.md")

    if (
        "summary_overview.md" in markdown_file_names
        and "overview_content.md" in markdown_file_names
    ):
        # Keep the summary_overview file, prepend the additioanl content.
        _merge_markdown_content(
            base_file=markdown_dir / "summary_overview.md",
            additional_content_file=markdown_dir / "overview_content.md",
            prepend_additional_content=True,
        )

    # For each file, if it is a markdown file move to the top level pages.
    for mdfile in markdown_dir.iterdir():
        if mdfile.is_dir():
            cwd.append(mdfile.name)
            move_markdown_pages(app, outdir, cwd)
            # Restore the original cwd after finish working on the directory.
            cwd.pop()

        if not mdfile.is_file() or mdfile.name.lower() in files_to_ignore:
            continue

        mdfile_name = ""

        _remove_license(mdfile)

        # Extract the header name for TOC.
        with open(mdfile) as mdfile_iterator:
            name = _extract_header_from_markdown(mdfile_iterator)

        if not name:
            with open(mdfile, "r+") as mdfile_iterator:
                mdfile_name = (
                    mdfile_iterator.name.split("/")[-1].split(".")[0].capitalize()
                )

                print(
                    f"Could not find a title for {mdfile_iterator.name}. Using {mdfile_name} as the title instead."
                )
                name = mdfile_name

                _prepend_markdown_header(name, mdfile_iterator)

        mdfile_name_to_use = mdfile.name.lower()
        if mdfile_name_to_use in files_to_rename:
            mdfile_name_to_use = files_to_rename[mdfile_name_to_use]

        if cwd and mdfile_name_to_use == "index.md":
            mdfile_name_to_use = f"{'_'.join(cwd)}_{mdfile_name_to_use}"

        mdfile_outdir = f"{outdir}/{mdfile_name_to_use}"

        shutil.copy(mdfile, mdfile_outdir)

        _highlight_md_codeblocks(mdfile_outdir)
        _clean_image_links(mdfile_outdir)

        if mdfile.name.lower() in ignore_in_toc:
            continue

        app.env.moved_markdown_pages.add(mdfile_name_to_use)

        if not cwd:
            # Use Overview as the name for top-level index file.
            if "index.md" in mdfile_name_to_use:
                # Save the index page entry.
                index_page_entry = {
                    "name": "Overview",
                    "href": "index.md",
                }
                continue

            # Use '/' to reserve for top level pages.
            app.env.markdown_pages["/"].append(
                {
                    "name": name,
                    "href": mdfile_name_to_use,
                }
            )
            continue

        # Add the file to the TOC later.
        app.env.markdown_pages[cwd[-1]].append(
            {
                "name": name,
                "href": mdfile_name_to_use,
            }
        )

    if app.env.markdown_pages.get("/"):
        # Sort the top level pages. Other pages will be sorted when they're
        # added to package level files accordingly.
        app.env.markdown_pages["/"] = sorted(
            app.env.markdown_pages["/"],
            key=lambda entry: entry["href"],
        )

    if index_page_entry is None:
        return

    # Place the Overview page at the top of the list.
    app.env.markdown_pages["/"].insert(
        0,
        index_page_entry,
    )


def remove_unused_pages(
    added_pages: MutableSet[str],
    all_pages: MutableSet[str],
    outdir: Path,
) -> None:
    """Removes unused markdown pages after merging the table of contents.

    Pages may be generated as part of generating the document. API pages
    are needed and may be generated as part of Sphinx config, but if not
    used they will be identified and removed.

    Args:
        added_pages: markdown pages that have been added to the merged
            table of contents.
        all_pages: set of all markdown pages generated.
        outdir: output directory containing the markdown pages.
    """

    pages_to_remove = set(page for page in all_pages if page not in added_pages)

    for page in pages_to_remove:
        try:
            os.remove(f"{outdir}/{page}")
        except FileNotFoundError:
            # This shouldn't happen, but in case we fail, ignore the failure
            # and continue deleting other files.
            print(f"Could not delete {page}.")


def run_sphinx_markdown(app: sphinx.application) -> None:
    """Runs Markdown builder in-process reusing the already-read Sphinx environment.

    Args:
        app (sphinx.application): The sphinx application.
    """
    # Skip running Markdown builder for some unit tests.
    # Not required other than to output DocFX YAML.
    markdown_outdir = Path(app.builder.outdir).parent / "markdown"
    if (
        "docs" in os.getcwd()
        or markdown_outdir.exists()
        or not getattr(app.env, "found_docs", None)
    ):
        return

    from sphinx.util.osutil import ensuredir
    from sphinx_markdown_builder.markdown_builder import MarkdownBuilder

    ensuredir(str(markdown_outdir))
    docnames = sorted(app.env.found_docs)
    orig_builder = app.builder
    md_builder = MarkdownBuilder(app)
    md_builder.outdir = str(markdown_outdir)
    md_builder.set_environment(app.env)
    md_builder.init()
    md_builder.prepare_writing(docnames)
    app.builder = md_builder
    try:
        for docname in docnames:
            doctree = app.env.get_and_resolve_doctree(docname, md_builder)
            md_builder.write_doc_serialized(docname, doctree)
            md_builder.write_doc(docname, doctree)
    finally:
        app.builder = orig_builder
