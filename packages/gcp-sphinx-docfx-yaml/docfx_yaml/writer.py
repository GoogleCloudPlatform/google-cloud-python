# Copyright 2021 Google LLC
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
"""
This is a forked version of the Sphinx text writer.

It outputs DocFX Markdown from the docutils doctree,
allowing us to transform transformed RST in memory to markdown.

It is certainly **not** complete,
and only implement as much logic as would be expected in normal docstring usage.
It is not intended to be a generic rst->markdown converter,
because rst contains myriad structures that markdown can't represent.
"""

import json
import os
import re
import sys
import textwrap
from itertools import groupby

from docutils import nodes, writers
from docutils.nodes import Node, Text, TextElement
from docutils.utils import column_width
from sphinx import addnodes
from sphinx.builders import Builder
from sphinx.locale import admonitionlabels

from .nodes import remarks


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class TextWrapper(textwrap.TextWrapper):
    """Custom subclass that uses a different word separator regex."""

    wordsep_re = re.compile(
        r"(\s+|"  # any whitespace
        r"(?<=\s)(?::[a-z-]+:)?`\S+|"  # interpreted text start
        r"[^\s\w]*\w+[a-zA-Z]-(?=\w+[a-zA-Z])|"  # hyphenated words
        r"(?<=[\w\!\"\'\&\.\,\?])-{2,}(?=\w))"
    )  # em-dash

    def _wrap_chunks(self, chunks: list[str]) -> list[str]:
        """Wraps chunks of text into lines.

        The original _wrap_chunks uses len() to calculate width.
        This method respects wide/fullwidth characters for width adjustment.

        Args:
            chunks (list): A list of strings representing text chunks.

        Returns:
            list: A list of strings representing the wrapped lines.
        """
        drop_whitespace = getattr(self, "drop_whitespace", True)  # py25 compat
        lines = []
        if self.width <= 0:
            raise ValueError("invalid width %r (must be > 0)" % self.width)

        chunks.reverse()

        while chunks:
            cur_line = []
            cur_len = 0

            if lines:
                indent = self.subsequent_indent
            else:
                indent = self.initial_indent

            width = self.width - column_width(indent)

            if drop_whitespace and chunks[-1].strip() == "" and lines:
                del chunks[-1]

            while chunks:
                l = column_width(chunks[-1])

                if cur_len + l <= width:
                    cur_line.append(chunks.pop())
                    cur_len += l

                else:
                    break

            if chunks and column_width(chunks[-1]) > width:
                self._handle_long_word(chunks, cur_line, cur_len, width)

            if drop_whitespace and cur_line and cur_line[-1].strip() == "":
                del cur_line[-1]

            if cur_line:
                lines.append(indent + "".join(cur_line))

        return lines

    def _break_word(self, word: str, space_left: int) -> tuple[str, str]:
        """Breaks a word into two parts.

        Breaks line by unicode width instead of len(word).

        Args:
            word (str): The word to break.
            space_left (int): The remaining space on the line.

        Returns:
            tuple: A tuple containing the two parts of the word.
        """
        total = 0
        for i, c in enumerate(word):
            total += column_width(c)
            if total > space_left:
                return word[: i - 1], word[i - 1 :]
        return word, ""

    def _split(self, text: str) -> list[str]:
        """Splits text into chunks.

        Override original method that only split by 'wordsep_re'.
        This '_split' split wide-characters into chunk by one character.

        Args:
            text (str): The text to split.

        Returns:
            list: A list of strings representing the chunks.
        """

        def split(t):
            return textwrap.TextWrapper._split(self, t)

        chunks = []
        for chunk in split(text):
            for w, g in groupby(chunk, column_width):
                if w == 1:
                    chunks.extend(split("".join(g)))
                else:
                    chunks.extend(list(g))
        return chunks

    def _handle_long_word(
        self, reversed_chunks: list[str], cur_line: list[str], cur_len: int, width: int
    ) -> None:
        """Handles a long word that exceeds the line width.

        Override original method for using self._break_word() instead of slice.

        Args:
            reversed_chunks (list): A list of reversed text chunks.
            cur_line (list): The current line being built.
            cur_len (int): The current length of the line.
            width (int): The maximum width of the line.
        """
        space_left = max(width - cur_len, 1)
        if self.break_long_words:
            l, r = self._break_word(reversed_chunks[-1], space_left)
            cur_line.append(l)
            reversed_chunks[-1] = r

        elif not cur_line:
            cur_line.append(reversed_chunks.pop())


MAXWIDTH = 999
STDINDENT = 3


def my_wrap(text: str, width: int = MAXWIDTH, **kwargs) -> list[str]:
    """Wraps the given text to a specified width.

    Args:
        text (str): The text to wrap.
        width (int): The maximum width of the lines.
        **kwargs: Additional keyword arguments for TextWrapper.

    Returns:
        list[str]: A list of wrapped lines.
    """
    w = TextWrapper(width=width, **kwargs)
    return w.wrap(text)


class MarkdownWriter(writers.Writer):
    """
    This writer is used to produce the markdown
    written in yaml files (summaries), it is distinct from the
    markdown outputter which process the whole documentation.
    """

    supported = ("text",)
    settings_spec = ("No options here.", "", ())
    settings_defaults = {}

    output = None

    def __init__(self, builder: Builder):
        """
        Args:
            builder (Builder): The sphinx builder.
        """
        writers.Writer.__init__(self)
        self.builder = builder
        self.translator_class = MarkdownTranslator

    def translate(self) -> None:
        """Translates the document to markdown."""
        visitor = self.translator_class(self.document, self.builder)
        self.document.walkabout(visitor)
        self.output = visitor.body


class MarkdownTranslator(nodes.NodeVisitor):
    sectionchars = '*=-~"+`'
    xref_template = "<xref:{0}>"

    def __init__(self, document: nodes.document, builder: Builder):
        """
        Args:
            document (nodes.document): The document to translate.
            builder (Builder): The sphinx builder.
        """
        self.invdata = []
        nodes.NodeVisitor.__init__(self, document)
        self.builder = builder

        newlines = builder.config.text_newlines
        if newlines == "windows":
            self.nl = "\r\n"
        elif newlines == "native":
            self.nl = os.linesep
        else:
            self.nl = "\n"
        self.sectionchars = builder.config.text_sectionchars
        self.states = [[]]
        self.stateindent = [0]
        self.list_counter = []
        self.sectionlevel = 0
        self.lineblocklevel = 0
        self.table = None

    @staticmethod
    def resolve_reference_in_node(node: Node) -> None:
        """Resolves references in a node.

        Args:
            node (Node): The node to resolve references in.
        """
        if node.tagname == "reference":
            ref_string = MarkdownTranslator._resolve_reference(node)

            if not node.parent is None:
                for i, n in enumerate(node.parent):
                    if n is node:  # Replace the reference node.
                        node.parent.children[i] = Text(ref_string)
                        break
            else:  # If reference node has no parent, replace it's content.
                node.clear()
                node.children.append(Text(ref_string))
        else:
            for child in node:
                if isinstance(child, Node):
                    MarkdownTranslator.resolve_reference_in_node(child)

    def add_text(self, text: str) -> None:
        """Adds text to the current state.

        Args:
            text (str): The text to add.
        """
        self.states[-1].append((-1, text))

    def new_state(self, indent: int = STDINDENT) -> None:
        """Creates a new state.

        Args:
            indent (int): The indent for the new state.
        """
        self.states.append([])
        self.stateindent.append(indent)

    def clear_last_state(self) -> tuple[list, int, int]:
        """Clears the last state."""
        content = self.states.pop()
        maxindent = sum(self.stateindent)
        indent = self.stateindent.pop()
        return content, maxindent, indent

    def end_state(
        self, wrap: bool = False, end: list[str] = [""], first: str = None
    ) -> None:
        """Ends the current state."""
        content, maxindent, indent = self.clear_last_state()
        result = []
        toformat = []

        def do_format():
            if not toformat:
                return
            if wrap:
                res = my_wrap("".join(toformat), width=MAXWIDTH - maxindent)
            else:
                res = "".join(toformat).splitlines()
            if end:
                res += end
            result.append((indent, res))

        for itemindent, item in content:
            if itemindent == -1:
                toformat.append(item)
            else:
                do_format()
                result.append((indent + itemindent, item))
                toformat = []
        do_format()
        if first is not None and result:
            itemindent, item = result[0]
            result_rest, result = result[1:], []
            if item:
                toformat = [first + " ".join(item)]
                do_format()  # re-create `result` from `toformat`
                _dummy, new_item = result[0]
                result.insert(0, (itemindent - indent, [new_item[0]]))
                result[1] = (itemindent, new_item[1:])
                result.extend(result_rest)
        self.states[-1].extend(result)

    def visit_document(self, node: Node) -> None:
        self.new_state(0)

    def depart_document(self, node: Node) -> None:
        self.end_state()
        self.body = self.nl.join(
            line and (" " * indent + line)
            for indent, lines in self.states[0]
            for line in lines
        )
        # XXX header/footer?

    def visit_highlightlang(self, node: Node) -> None:
        raise nodes.SkipNode

    def visit_section(self, node: Node) -> None:
        self._title_char = self.sectionchars[self.sectionlevel]
        self.sectionlevel += 1

    def depart_section(self, node: Node) -> None:
        self.sectionlevel -= 1

    def visit_topic(self, node: Node) -> None:
        # Skip TOC in the articles
        raise nodes.SkipNode

    def depart_topic(self, node: Node) -> None:
        pass

    visit_sidebar = visit_topic
    depart_sidebar = depart_topic

    def visit_rubric(self, node: Node) -> None:
        self.new_state(0)
        self.add_text("-[ ")

    def depart_rubric(self, node: Node) -> None:
        self.add_text(" ]-")
        self.end_state()

    def visit_compound(self, node: Node) -> None:
        pass

    def depart_compound(self, node: Node) -> None:
        pass

    def visit_glossary(self, node: Node) -> None:
        pass

    def depart_glossary(self, node: Node) -> None:
        pass

    def visit_title(self, node: Node) -> None:
        depth = -1
        element = node.parent
        while element is not None:
            depth += 1
            element = element.parent
        self.add_text(self.nl * 2 + (depth * "#") + " ")

    def depart_title(self, node: Node) -> None:
        pass

    def visit_subtitle(self, node: Node) -> None:
        pass

    def depart_subtitle(self, node: Node) -> None:
        pass

    def visit_attribution(self, node: Node) -> None:
        self.add_text("-- ")

    def depart_attribution(self, node: Node) -> None:
        pass

    def visit_desc(self, node: Node) -> None:
        pass

    def depart_desc(self, node: Node) -> None:
        pass

    def visit_desc_signature(self, node: Node) -> None:
        self.new_state(0)

    def depart_desc_signature(self, node: Node) -> None:
        # XXX: wrap signatures in a way that makes sense
        self.end_state(wrap=False, end=None)

    def visit_desc_name(self, node: Node) -> None:
        pass

    def depart_desc_name(self, node: Node) -> None:
        pass

    def visit_desc_addname(self, node: Node) -> None:
        pass

    def depart_desc_addname(self, node: Node) -> None:
        pass

    def visit_desc_type(self, node: Node) -> None:
        pass

    def depart_desc_type(self, node: Node) -> None:
        pass

    def visit_desc_returns(self, node: Node) -> None:
        self.add_text(" -> ")

    def depart_desc_returns(self, node: Node) -> None:
        pass

    def visit_desc_parameterlist(self, node: Node) -> None:
        self.add_text("(")
        self.first_param = 1

    def depart_desc_parameterlist(self, node: Node) -> None:
        self.add_text(")")

    def visit_desc_parameter(self, node: Node) -> None:
        if not self.first_param:
            self.add_text(", ")
        else:
            self.first_param = 0
        self.add_text(node.astext())
        raise nodes.SkipNode

    def visit_desc_optional(self, node: Node) -> None:
        self.add_text("[")

    def depart_desc_optional(self, node: Node) -> None:
        self.add_text("]")

    def visit_desc_annotation(self, node: Node) -> None:
        pass

    def depart_desc_annotation(self, node: Node) -> None:
        pass

    def visit_desc_content(self, node: Node) -> None:
        self.new_state()
        self.add_text(self.nl)

    def depart_desc_content(self, node: Node) -> None:
        self.end_state()

    def visit_figure(self, node: Node) -> None:
        self.new_state()

    def depart_figure(self, node: Node) -> None:
        self.end_state()

    def visit_caption(self, node: Node) -> None:
        pass

    def depart_caption(self, node: Node) -> None:
        pass

    def visit_productionlist(self, node: Node) -> None:
        self.new_state()
        names = []
        for production in node:
            names.append(production["tokenname"])
        maxlen = max(len(name) for name in names)
        lastname = None
        for production in node:
            if production["tokenname"]:
                self.add_text(production["tokenname"].ljust(maxlen) + " ::=")
                lastname = production["tokenname"]
            elif lastname is not None:
                self.add_text("%s    " % (" " * len(lastname)))
            self.add_text(production.astext() + self.nl)
        self.end_state(wrap=False)
        raise nodes.SkipNode

    def visit_footnote(self, node: Node) -> None:
        self._footnote = node.children[0].astext().strip()
        self.new_state(len(self._footnote) + 3)

    def depart_footnote(self, node: Node) -> None:
        self.end_state(first="[%s] " % self._footnote)

    def visit_citation(self, node: Node) -> None:
        if len(node) and isinstance(node[0], nodes.label):
            self._citlabel = node[0].astext()
        else:
            self._citlabel = ""
        self.new_state(len(self._citlabel) + 3)

    def depart_citation(self, node: Node) -> None:
        self.end_state(first="[%s] " % self._citlabel)

    def visit_label(self, node: Node) -> None:
        raise nodes.SkipNode

    def visit_legend(self, node: Node) -> None:
        pass

    def depart_legend(self, node: Node) -> None:
        pass

    # XXX: option list could use some better styling

    def visit_option_list(self, node: Node) -> None:
        pass

    def depart_option_list(self, node: Node) -> None:
        pass

    def visit_option_list_item(self, node: Node) -> None:
        self.new_state(0)

    def depart_option_list_item(self, node: Node) -> None:
        self.end_state()

    def visit_option_group(self, node: Node) -> None:
        self._firstoption = True

    def depart_option_group(self, node: Node) -> None:
        self.add_text("     ")

    def visit_option(self, node: Node) -> None:
        if self._firstoption:
            self._firstoption = False
        else:
            self.add_text(", ")

    def depart_option(self, node: Node) -> None:
        pass

    def visit_option_string(self, node: Node) -> None:
        pass

    def depart_option_string(self, node: Node) -> None:
        pass

    def visit_option_argument(self, node: Node) -> None:
        self.add_text(node["delimiter"])

    def depart_option_argument(self, node: Node) -> None:
        pass

    def visit_description(self, node: Node) -> None:
        pass

    def depart_description(self, node: Node) -> None:
        pass

    def visit_tabular_col_spec(self, node: Node) -> None:
        raise nodes.SkipNode

    def visit_colspec(self, node: Node) -> None:
        self.table[0].append(node["colwidth"])
        raise nodes.SkipNode

    def visit_tgroup(self, node: Node) -> None:
        pass

    def depart_tgroup(self, node: Node) -> None:
        pass

    def visit_thead(self, node: Node) -> None:
        pass

    def depart_thead(self, node: Node) -> None:
        pass

    def visit_tbody(self, node: Node) -> None:
        self.table.append("sep")

    def depart_tbody(self, node: Node) -> None:
        pass

    def visit_row(self, node: Node) -> None:
        self.table.append([])

    def depart_row(self, node: Node) -> None:
        pass

    def visit_entry(self, node: Node) -> None:
        if "morerows" in node or "morecols" in node:
            raise NotImplementedError(
                "Column or row spanning cells are not implemented."
            )
        self.new_state(0)

    def depart_entry(self, node: Node) -> None:
        text = self.nl.join(self.nl.join(x[1]) for x in self.states.pop())
        self.stateindent.pop()
        self.table[-1].append(text)

    def visit_table(self, node: Node) -> None:
        if self.table:
            raise NotImplementedError("Nested tables are not supported.")
        self.new_state(0)
        self.table = [[]]
        self

    def depart_table(self, node: Node) -> None:
        lines = self.table[1:]
        fmted_rows = []
        colwidths = self.table[0]
        realwidths = colwidths[:]
        separator = 0
        self.add_text(f"<!-- {node.tagname} -->")
        # self.add_text(f'<!-- {json.dumps(self.table)} -->')

        # don't allow paragraphs in table cells for now
        # for line in lines:
        #     if line == 'sep':
        #         separator = len(fmted_rows)
        #     else:
        #         cells = []
        #         for i, cell in enumerate(line):
        #             par = my_wrap(cell, width=colwidths[i])
        #             if par:
        #                 maxwidth = max(column_width(x) for x in par)
        #             else:
        #                 maxwidth = 0
        #             realwidths[i] = max(realwidths[i], maxwidth)
        #             cells.append(par)
        #         fmted_rows.append(cells)

        # def writesep(char='-'):
        #     out = ['+']
        #     for width in realwidths:
        #         out.append(char * (width+2))
        #         out.append('+')
        #     self.add_text(''.join(out) + self.nl)

        # def writerow(row):
        #     lines = zip_longest(*row)
        #     for line in lines:
        #         out = ['|']
        #         for i, cell in enumerate(line):
        #             if cell:
        #                 adjust_len = len(cell) - column_width(cell)
        #                 out.append(' ' + cell.ljust(
        #                     realwidths[i] + 1 + adjust_len))
        #             else:
        #                 out.append(' ' * (realwidths[i] + 2))
        #             out.append('|')
        #         self.add_text(''.join(out) + self.nl)

        # for i, row in enumerate(fmted_rows):
        #     if separator and i == separator:
        #         writesep('=')
        #     else:
        #         writesep('-')
        #     writerow(row)
        # writesep('-')
        self.table = None
        self.end_state(wrap=False)

    def visit_acks(self, node: Node) -> None:
        self.new_state(0)
        self.add_text(", ".join(n.astext() for n in node.children[0].children) + ".")
        self.end_state()
        raise nodes.SkipNode

    def visit_image(self, node: Node) -> None:
        try:
            image_name = "/".join(
                node.attributes["uri"].split("/")[
                    node.attributes["uri"].split("/").index("_static") - 1 :
                ]
            )
        except ValueError as e:
            print(f"Image not found where expected {node.attributes['uri']}")
            raise nodes.SkipNode
        image_name = "".join(image_name.split())
        self.new_state(0)
        if "alt" in node.attributes:
            self.add_text(f"![{node['alt']}]({image_name})" + self.nl)
        self.add_text(f"![image]({image_name})" + self.nl)
        self.end_state(False)
        raise nodes.SkipNode

    def visit_transition(self, node: Node) -> None:
        indent = sum(self.stateindent)
        self.new_state(0)
        self.add_text("=" * (MAXWIDTH - indent))
        self.end_state()
        raise nodes.SkipNode

    def visit_bullet_list(self, node: Node) -> None:
        self.list_counter.append(-1)

    def depart_bullet_list(self, node: Node) -> None:
        self.list_counter.pop()

    def visit_enumerated_list(self, node: Node) -> None:
        self.list_counter.append(node.get("start", 1) - 1)

    def depart_enumerated_list(self, node: Node) -> None:
        self.list_counter.pop()

    def visit_definition_list(self, node: Node) -> None:
        self.list_counter.append(-2)

    def depart_definition_list(self, node: Node) -> None:
        self.list_counter.pop()

    def visit_list_item(self, node: Node) -> None:
        if self.list_counter[-1] == -1:
            # bullet list
            self.new_state(2)
        elif self.list_counter[-1] == -2:
            # definition list
            pass
        else:
            # enumerated list
            self.list_counter[-1] += 1
            self.new_state(len(str(self.list_counter[-1])) + 2)

    def depart_list_item(self, node: Node) -> None:
        if self.list_counter[-1] == -1:
            self.end_state(first="* ")
        elif self.list_counter[-1] == -2:
            pass
        else:
            self.end_state(first="%s. " % self.list_counter[-1])

    def visit_definition_list_item(self, node: Node) -> None:
        self._classifier_count_in_li = len(node.traverse(nodes.classifier))

    def depart_definition_list_item(self, node: Node) -> None:
        pass

    def visit_term(self, node: Node) -> None:
        self.new_state(0)

    def depart_term(self, node: Node) -> None:
        if not self._classifier_count_in_li:
            self.end_state(end=None)

    def visit_termsep(self, node: Node) -> None:
        self.add_text(", ")
        raise nodes.SkipNode

    def visit_classifier(self, node: Node) -> None:
        self.add_text(" : ")

    def depart_classifier(self, node: Node) -> None:
        self._classifier_count_in_li -= 1
        if not self._classifier_count_in_li:
            self.end_state(end=None)

    def visit_definition(self, node: Node) -> None:
        self.new_state()

    def depart_definition(self, node: Node) -> None:
        self.end_state()

    def visit_field_list(self, node: Node) -> None:
        pass

    def depart_field_list(self, node: Node) -> None:
        pass

    def visit_field(self, node: Node) -> None:
        pass

    def depart_field(self, node: Node) -> None:
        pass

    def visit_field_name(self, node: Node) -> None:
        self.new_state(0)

    def depart_field_name(self, node: Node) -> None:
        self.add_text(":")
        self.end_state(end=None)

    def visit_field_body(self, node: Node) -> None:
        self.new_state()

    def depart_field_body(self, node: Node) -> None:
        self.end_state()

    def visit_centered(self, node: Node) -> None:
        pass

    def depart_centered(self, node: Node) -> None:
        pass

    def visit_hlist(self, node: Node) -> None:
        pass

    def depart_hlist(self, node: Node) -> None:
        pass

    def visit_hlistcol(self, node: Node) -> None:
        pass

    def depart_hlistcol(self, node: Node) -> None:
        pass

    def visit_admonition(self, node: Node) -> None:
        self.new_state(0)

    def depart_admonition(self, node: Node) -> None:
        self.end_state()

    def _visit_admonition(self, node: Node) -> None:
        self.new_state(2)

        if isinstance(node.children[0], nodes.Sequential):
            self.add_text(self.nl)

    def _make_depart_admonition(name: str):
        def depart_admonition(self, node: Node) -> None:
            self.end_state(first=admonitionlabels[name] + ": ")

        return depart_admonition

    def _make_depart_alert_box(name: str):
        def depart_alert_box(self, node: Node) -> None:
            self.clear_last_state()
            MarkdownTranslator.resolve_reference_in_node(node)
            lines = node.astext().split("\n")
            quoteLines = [f"> {line}\n>" for line in lines]
            mdStr = "\n> [!{0}]\n{1}".format(name, "\n".join(quoteLines))
            self.add_text(mdStr)

        return depart_alert_box

    visit_attention = _visit_admonition
    depart_attention = _make_depart_admonition("attention")
    visit_caution = _visit_admonition
    depart_caution = _make_depart_alert_box("CAUTION")
    visit_danger = _visit_admonition
    depart_danger = _make_depart_admonition("danger")
    visit_error = _visit_admonition
    depart_error = _make_depart_admonition("error")
    visit_hint = _visit_admonition
    depart_hint = _make_depart_admonition("hint")
    visit_important = _visit_admonition
    depart_important = _make_depart_alert_box("IMPORTANT")
    visit_note = _visit_admonition
    depart_note = _make_depart_alert_box("NOTE")
    visit_tip = _visit_admonition
    depart_tip = _make_depart_alert_box("TIP")
    visit_warning = _visit_admonition
    depart_warning = _make_depart_alert_box("WARNING")
    visit_seealso = _visit_admonition

    def depart_seealso(self, node: Node) -> None:
        self.end_state()

    def visit_versionmodified(self, node: Node) -> None:
        self.new_state(0)

    def depart_versionmodified(self, node: Node) -> None:
        self.end_state()

    def visit_literal_block(self, node: Node) -> None:
        try:
            include_language = None
            include_lines = None
            include_highlight = None
            include_caption = None
            path = self.builder.confdir
            relative_path = node.attributes["source"][len(path) + 1 :]

            if "language" in node.attributes:
                include_language = node.attributes["language"]

            if "language" in node.attributes:
                include_language = node.attributes["language"]

            if "caption" in node.attributes:
                include_caption = node.attributes["caption"]

            include_language = (
                ("-" + include_language) if (include_language is not None) else ""
            )
            include_caption = (
                ('"' + include_caption + '"') if (include_caption is not None) else ""
            )

            self.add_text(
                f"<!--[!code{include_language}[Main]({relative_path} {include_caption})]-->"
            )
        except KeyError as e:
            pass
        except ValueError as e:
            pass

        self.new_state(0)
        self.add_text(f"<!-- {node.tagname} {json.dumps(node.attributes)} -->")
        self.end_state(wrap=False)

        if "language" in node.attributes:
            self.add_text(f"````{node.attributes['language']}")
        else:
            self.add_text("````")
        self.new_state()

    def depart_literal_block(self, node: Node) -> None:
        self.add_text(self.nl + "````")
        self.end_state(wrap=False)

    def visit_doctest_block(self, node: Node) -> None:
        self.add_text(self.nl + "```")
        self.new_state(0)

    def depart_doctest_block(self, node: Node) -> None:
        self.add_text(self.nl + "```")
        self.end_state(wrap=False)

    def visit_line_block(self, node: Node) -> None:
        self.new_state()
        self.lineblocklevel += 1

    def depart_line_block(self, node: Node) -> None:
        self.lineblocklevel -= 1
        self.end_state(wrap=False, end=None)
        if not self.lineblocklevel:
            self.add_text("\n")

    def visit_line(self, node: Node) -> None:
        pass

    def depart_line(self, node: Node) -> None:
        self.add_text("\n")

    def visit_block_quote(self, node: Node) -> None:
        self.new_state()

    def depart_block_quote(self, node: Node) -> None:
        self.end_state()

    def visit_compact_paragraph(self, node: Node) -> None:
        pass

    def depart_compact_paragraph(self, node: Node) -> None:
        pass

    def visit_paragraph(self, node: Node) -> None:
        if not isinstance(node.parent, nodes.Admonition) or isinstance(
            node.parent, addnodes.seealso
        ):
            self.new_state(0)

    def depart_paragraph(self, node: Node) -> None:
        if not isinstance(node.parent, nodes.Admonition) or isinstance(
            node.parent, addnodes.seealso
        ):
            self.end_state()

    def visit_target(self, node: Node) -> None:
        if node.hasattr("refid"):
            self.new_state(0)
            self.add_text(f"<a name={node.attributes['refid']}></a>")
            self.end_state()
        raise nodes.SkipNode

    def visit_index(self, node: Node) -> None:
        raise nodes.SkipNode

    def visit_toctree(self, node: Node) -> None:
        raise nodes.SkipNode

    def visit_substitution_definition(self, node: Node) -> None:
        raise nodes.SkipNode

    def visit_pending_xref(self, node: Node) -> None:
        if "refdomain" in node.attributes and node.attributes["refdomain"] == "py":
            self.add_text(f"<xref:{node.attributes['reftarget']}>")
        raise nodes.SkipNode

    def depart_pending_xref(self, node: Node) -> None:
        pass

    @classmethod
    def _resolve_reference(cls, node: Node) -> str:
        ref_string = None
        raw_ref_tilde_template = ":class:`~{0}`"
        raw_ref_template = ":class:`{0}`"
        if "refid" in node.attributes:
            ref_string = f"<xref:{node.attributes['refid']}>"
        elif "refuri" in node.attributes:
            if (
                "http" in node.attributes["refuri"]
                or node.attributes["refuri"][0] == "/"
            ):
                ref_string = f"[{node.astext()}]({node.attributes['refuri']})"
            else:
                # only use id in class and func refuri if its id exists
                # otherwise, remove '.html#' in refuri
                # uri_fields[1] is class or function uid. e.g:
                # case 0 - [module]#[class-uid] (go to if block to use class-uid instead)
                # case 1 - [module]#module-[module] (go to else block to remove '.html#' in refuri)
                # case 2 - [class]# (go to else block to remove path and '.html#' in refuri)
                uri_fields = node.attributes["refuri"].split("#")
                if (
                    len(uri_fields) > 1
                    and uri_fields[1]
                    and not uri_fields[1].startswith("module")
                ):
                    node.attributes["refuri"] = uri_fields[1]
                else:
                    fname = os.path.split(node.attributes["refuri"])[-1]
                    pos = fname.find(".html")
                    if pos != -1:
                        node.attributes["refuri"] = fname[0:pos]

                if (
                    node.parent.rawsource
                    == raw_ref_tilde_template.format(node.attributes["refuri"])
                    or node.parent.rawsource
                    == raw_ref_template.format(node.attributes["refuri"])
                    or node.parent.tagname == "document"
                ):
                    ref_string = node.attributes["refuri"]
                else:
                    ref_string = cls.xref_template.format(node.attributes["refuri"])
        else:
            ref_string = f"{node.tagname}<!-- {json.dumps(node.attributes)} -->"

        return ref_string

    def visit_reference(self, node: Node) -> None:
        ref_string = MarkdownTranslator._resolve_reference(node)
        self.add_text(ref_string)
        raise nodes.SkipNode

    def depart_reference(self, node: Node) -> None:
        pass

    def visit_number_reference(self, node: Node) -> None:
        text = nodes.Text(node.get("title", "#"))
        self.visit_Text(text)
        raise nodes.SkipNode

    def visit_download_reference(self, node: Node) -> None:
        pass

    def depart_download_reference(self, node: Node) -> None:
        pass

    def visit_emphasis(self, node: Node) -> None:
        self.add_text("*")

    def depart_emphasis(self, node: Node) -> None:
        self.add_text("*")

    def visit_literal_emphasis(self, node: Node) -> None:
        self.add_text("*")

    def depart_literal_emphasis(self, node: Node) -> None:
        self.add_text("*")

    def visit_strong(self, node: Node) -> None:
        self.add_text("**")

    def depart_strong(self, node: Node) -> None:
        self.add_text("**")

    def visit_literal_strong(self, node: Node) -> None:
        self.add_text("**")

    def depart_literal_strong(self, node: Node) -> None:
        self.add_text("**")

    def visit_abbreviation(self, node: Node) -> None:
        self.add_text("")

    def depart_abbreviation(self, node: Node) -> None:
        if node.hasattr("explanation"):
            self.add_text(" (%s)" % node["explanation"])

    def visit_title_reference(self, node: Node) -> None:
        self.add_text("*")

    def depart_title_reference(self, node: Node) -> None:
        self.add_text("*")

    def visit_literal(self, node: Node) -> None:
        self.add_text("`")

    def depart_literal(self, node: Node) -> None:
        self.add_text("`")

    def visit_subscript(self, node: Node) -> None:
        self.add_text("_")

    def depart_subscript(self, node: Node) -> None:
        pass

    def visit_superscript(self, node: Node) -> None:
        self.add_text("^")

    def depart_superscript(self, node: Node) -> None:
        pass

    def visit_footnote_reference(self, node: Node) -> None:
        self.add_text("[%s]" % node.astext())
        raise nodes.SkipNode

    def visit_citation_reference(self, node: Node) -> None:
        self.add_text("[%s]" % node.astext())
        raise nodes.SkipNode

    def visit_Text(self, node: Text) -> None:
        self.add_text(node.astext())

    def depart_Text(self, node: Text) -> None:
        pass

    def visit_generated(self, node: Node) -> None:
        pass

    def depart_generated(self, node: Node) -> None:
        pass

    def visit_inline(self, node: Node) -> None:
        if "xref" in node["classes"] or "term" in node["classes"]:
            self.add_text("*")

    def depart_inline(self, node: Node) -> None:
        if "xref" in node["classes"] or "term" in node["classes"]:
            self.add_text("*")

    def visit_container(self, node: Node) -> None:
        pass

    def depart_container(self, node: Node) -> None:
        pass

    def visit_problematic(self, node: Node) -> None:
        self.add_text(">>")

    def depart_problematic(self, node: Node) -> None:
        self.add_text("<<")

    def visit_system_message(self, node: Node) -> None:
        print(
            bcolors.WARNING
            + "System message warnings: %s" % node.astext()
            + bcolors.ENDC
        )
        raise nodes.SkipNode

    def visit_comment(self, node: Node) -> None:
        raise nodes.SkipNode

    def visit_meta(self, node: Node) -> None:
        # only valid for HTML
        raise nodes.SkipNode

    def visit_raw(self, node: Node) -> None:
        if "text" in node.get("format", "").split():
            self.new_state(0)
            self.add_text(node.astext())
            self.end_state(wrap=False)
        raise nodes.SkipNode

    def visit_math(self, node: Node) -> None:
        self.builder.warn(
            'using "math" markup without a Sphinx math extension '
            "active, please use one of the math extensions "
            "described at http://sphinx-doc.org/ext/math.html",
            (self.builder.env.docname, node.line),
        )
        raise nodes.SkipNode

    visit_math_block = visit_math

    def visit_substitution_reference(self, node: Node) -> None:
        pass

    def depart_substitution_reference(self, node: Node) -> None:
        pass

    visit_remarks = remarks.visit_remarks

    depart_remarks = remarks.depart_remarks

    def unknown_visit(self, node: Node) -> None:
        raise NotImplementedError("Unknown node: " + node.__class__.__name__)
