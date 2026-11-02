# Copyright (C) 2019  Google LLC
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

"""Module containing miscellaneous utilities
that will eventually move somewhere else (probably)."""

import os
import yaml

from typing import Generator, Tuple, List, Union

from gapic.samplegen_utils import types


MIN_SCHEMA_VERSION = (1, 2, 0)

VALID_CONFIG_TYPE = "com.google.api.codegen.samplegen.v1p2.SampleConfigProto"


def render_format_string(s: str, expressions: List[str] = []) -> str:
    """Given string s and a list of expressions, substitute each %s
    in the string with {exp}.

    Arguments:
        s (str): The string literal.
        expressions (Optional[List[str]]): A list of expressions.
    """

    s = s.replace('"', '\\"')

    for exp in expressions:
        # some expressions will contain references to "$resp"
        exp = coerce_response_name(exp)
        s = s.replace("%s", f"{{{exp}}}", 1)

    return s


def coerce_response_name(s: str) -> str:
    # In the sample config, the "$resp" keyword is used to refer to the
    # item of interest as received by the corresponding calling form.
    # For a 'regular', i.e. unary, synchronous, non-long-running method,
    # it's the return value; for a server-streaming method, it's the iteration
    # variable in the for loop that iterates over the return value, and for
    # a long running promise, the user calls result on the method return value to
    # resolve the future.
    #
    # The sample schema uses '$resp' as the special variable,
    # but in the samples the 'response' variable is used instead.
    return s.replace("$resp", "response")


def is_valid_sample_cfg(
    doc,
    min_version: Tuple[int, int, int] = MIN_SCHEMA_VERSION,
    config_type: str = VALID_CONFIG_TYPE,
) -> bool:
    """Predicate that takes a parsed yaml doc checks if it is a valid sample config.

    Arguments:
        doc (Any): The yaml document to be assessed
        min_version (Tuple[int, int, int]): (optional) The minimum valid version for
        the sample config. Uses semantic version (major, minor, bugfix).
        config_type (str): (optional) The valid type of the document.

    Returns:
        bool: True if doc is a valid sample config document.

    """

    def parse_version(version_str: str) -> Tuple[int, ...]:
        return tuple(int(tok) for tok in version_str.split("."))

    version_token = "schema_version"
    return bool(
        # Yaml may return a dict, a list, or a str
        isinstance(doc, dict)
        and doc.get("type") == VALID_CONFIG_TYPE
        and parse_version(doc.get(version_token, "")) >= min_version
        and doc.get("samples")
    )


def generate_all_sample_fpaths(path: str) -> Generator[str, None, None]:
    """Given file or directory path, yield all valid sample config fpaths recursively.

    Arguments:
        path (str): The file or directory path to check
                    for valid samplegen config files.
                    Directories are checked recursively.

    Raises:
        types.InvalidConfig: If 'path' is an invalid sampleconfig file
                             or 'path' is not a file or directory.

    Returns:
        Generator[str, None, None]: All valid samplegen config files
                                    starting at 'path'.
    """

    # If a user passes in a directory to search for sample configs,
    # it is required to ignore any non-sample-config files so as to avoid
    # being unhelpfully strict.
    # Directly named files, however, should generate an error, because silently
    # ignoring them is less helpful than failing loudly.
    if os.path.isfile(path):
        if not path.endswith(".yaml"):
            raise types.InvalidConfig(f"Not a yaml file: {path}")

        with open(path) as f:
            if not any(
                is_valid_sample_cfg(doc) for doc in yaml.safe_load_all(f.read())
            ):
                raise types.InvalidConfig(f"No valid sample config in file: {path}")

            yield path
    # Note: if we ever need to recursively check directories for sample configs,
    #       add an "elif os.path.isdir(path)" yielding from os.walk right here.
    else:
        raise types.InvalidConfig(f"No such file: {path}")
