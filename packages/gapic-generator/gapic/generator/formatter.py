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


def fix_whitespace(code: str) -> str:
    """Perform basic whitespace post-processing.

    This corrects a couple of formatting issues that Jinja templates
    may struggle with (particularly blank line count, which is tough to
    get consistently right when ``if`` or ``for`` are involved).

    Args:
        code (str): A string of code to be formatted.

    Returns
        str: Formatted code.
    """
    # Remove trailing whitespace from any line.
    code = re.sub(r"[ ]+\n", "\n", code)

    # Ensure at most two blank lines before top level definitions.
    code = re.sub(r"\s+\n\s*\n\s*\n(class|def|@|#|_)", r"\n\n\n\1", code)

    # Ensure at most one line before nested definitions.
    code = re.sub(r"\s+\n\s*\n((    )+)(\w|_|@|#)", r"\n\n\1\3", code)

    # All files shall end in one and exactly one line break.
    return f"{code.rstrip()}\n"
