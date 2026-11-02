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

import io
import sys
import typing

import click


@click.command()
@click.option(
    "--request",
    type=click.File("rb"),
    default=sys.stdin.buffer,
    help="Location of the `CodeGeneratorRequest` to be dumped. "
    "This defaults to stdin (which is what protoc uses) "
    "but this option can be set for testing/debugging.",
)
def dump(request: typing.BinaryIO) -> None:
    """Dump the CodeGeneratorRequest, unmodified, to the given output."""
    # Ideally, this would output a CodeGeneratorResponse with the content
    # of the CodeGeneratorRequest. Sadly, that does not work because
    # the `content` field is a string, not a bytes, and requests are not
    # valid utf-8.

    # Dump the CodeGeneratorRequest to disk.
    with io.open("request.desc", "wb+") as output:
        output.write(request.read())

    # Log what happened.
    click.secho(
        "Request dumped to `request.desc`. "
        "This script will now exit 1 to satisfy protoc.",
        file=sys.stderr,
        fg="green",
    )
    sys.exit(1)
