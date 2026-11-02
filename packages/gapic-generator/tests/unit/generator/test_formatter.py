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

import textwrap

from gapic.generator import formatter


def test_fix_whitespace_top_level():
    assert formatter.fix_whitespace(
        textwrap.dedent(
            """\
    import something


    class Correct:
        pass



    class TooFarDown:
        pass

    class TooClose:  # remains too close
        pass
    """
        )
    ) == textwrap.dedent(
        """\
    import something


    class Correct:
        pass


    class TooFarDown:
        pass

    class TooClose:  # remains too close
        pass
    """
    )


def test_fix_whitespace_nested():
    assert formatter.fix_whitespace(
        textwrap.dedent(
            """\
    class JustAClass:
        def foo(self):
            pass


        def too_far_down(self):
            pass
    """
        )
    ) == textwrap.dedent(
        """\
    class JustAClass:
        def foo(self):
            pass

        def too_far_down(self):
            pass
    """
    )


def test_fix_whitespace_decorators():
    assert formatter.fix_whitespace(
        textwrap.dedent(
            """\
    class JustAClass:
        def foo(self):
            pass


        @property
        def too_far_down(self):
            return 42
    """
        )
    ) == textwrap.dedent(
        """\
    class JustAClass:
        def foo(self):
            pass

        @property
        def too_far_down(self):
            return 42
    """
    )


def test_fix_whitespace_intermediate_whitespace():
    assert formatter.fix_whitespace(
        textwrap.dedent(
            """\
    class JustAClass:
        def foo(self):
            pass
        \


        @property
        def too_far_down(self):
            return 42
    """
        )
    ) == textwrap.dedent(
        """\
    class JustAClass:
        def foo(self):
            pass

        @property
        def too_far_down(self):
            return 42
    """
    )


def test_fix_whitespace_comment():
    assert formatter.fix_whitespace(
        textwrap.dedent(
            """\
    def do_something():
        do_first_thing()


        # Something something something.
        do_second_thing()
    """
        )
    ) == textwrap.dedent(
        """\
    def do_something():
        do_first_thing()

        # Something something something.
        do_second_thing()
    """
    )


def test_file_newline_ending():
    assert formatter.fix_whitespace("") == "\n"
