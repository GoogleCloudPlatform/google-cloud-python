# Copyright 2022 Google LLC
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

import re
from typing import Optional, Dict

from google.protobuf import json_format

from gapic.schema import api, metadata
from gapic.samplegen_utils import snippet_metadata_pb2  # type: ignore
from gapic.samplegen_utils import types


CLIENT_INIT_RE = re.compile(r"^\s+# Create a client")
REQUEST_INIT_RE = re.compile(r"^\s+# Initialize request argument\(s\)")
REQUEST_EXEC_RE = re.compile(r"^\s+# Make the request")
RESPONSE_HANDLING_RE = re.compile(r"^\s+# Handle the response")


class Snippet:
    """A single snippet and its metadata.

    Attributes:
        sample_str (str): The full text of the code snippet.
        metadata (snippet_metadata_pb2.Snippet): The snippet's metadata.
    """

    def __init__(self, sample_str: str, sample_metadata):
        self.sample_str = sample_str
        self.metadata = sample_metadata
        self._parse_snippet_segments()

    def _parse_snippet_segments(self):
        """Parse sections of the sample string and update metadata"""
        self.sample_lines = self.sample_str.splitlines(keepends=True)

        self._full_snippet = snippet_metadata_pb2.Snippet.Segment(
            type=snippet_metadata_pb2.Snippet.Segment.SegmentType.FULL
        )
        self._short_snippet = snippet_metadata_pb2.Snippet.Segment(
            type=snippet_metadata_pb2.Snippet.Segment.SegmentType.SHORT
        )
        self._client_init = snippet_metadata_pb2.Snippet.Segment(
            type=snippet_metadata_pb2.Snippet.Segment.SegmentType.CLIENT_INITIALIZATION
        )
        self._request_init = snippet_metadata_pb2.Snippet.Segment(
            type=snippet_metadata_pb2.Snippet.Segment.SegmentType.REQUEST_INITIALIZATION
        )
        self._request_exec = snippet_metadata_pb2.Snippet.Segment(
            type=snippet_metadata_pb2.Snippet.Segment.SegmentType.REQUEST_EXECUTION
        )
        self._response_handling = snippet_metadata_pb2.Snippet.Segment(
            type=snippet_metadata_pb2.Snippet.Segment.SegmentType.RESPONSE_HANDLING,
            end=len(self.sample_lines),
        )

        # Index starts at 1 since these represent line numbers
        for i, line in enumerate(self.sample_lines, start=1):
            if line.startswith("# [START"):  # do not include region tag lines
                self._full_snippet.start = i + 1
                self._short_snippet.start = self._full_snippet.start
            elif line.startswith("# [END"):
                self._full_snippet.end = i - 1
                self._short_snippet.end = self._full_snippet.end
            elif CLIENT_INIT_RE.match(line):
                self._client_init.start = i
            elif REQUEST_INIT_RE.match(line):
                self._client_init.end = i - 1
                self._request_init.start = i
            elif REQUEST_EXEC_RE.match(line):
                self._request_init.end = i - 1
                self._request_exec.start = i
            elif RESPONSE_HANDLING_RE.match(line):
                self._request_exec.end = i - 1
                self._response_handling.start = i

        self.metadata.segments.extend(
            [
                self._full_snippet,
                self._short_snippet,
                self._client_init,
                self._request_init,
                self._request_exec,
                self._response_handling,
            ]
        )

    @property
    def full_snippet(self) -> str:
        """The portion between the START and END region tags."""
        start_idx = self._full_snippet.start - 1
        end_idx = self._full_snippet.end
        return "".join(self.sample_lines[start_idx:end_idx])


class SnippetIndex:
    """An index of all the snippets for an API.

    Attributes:
        metadata_index (snippet_metadata_pb2.Index): The snippet metadata index.
    """

    def __init__(self, api_schema: api.API):
        self.metadata_index = snippet_metadata_pb2.Index()  # type: ignore

        self.metadata_index.client_library.name = (
            api_schema.naming.warehouse_package_name
        )
        self.metadata_index.client_library.language = (
            snippet_metadata_pb2.Language.PYTHON  # type: ignore
        )

        self.metadata_index.client_library.version = api_schema.gapic_version

        self.metadata_index.client_library.apis.append(
            snippet_metadata_pb2.Api(  # type: ignore
                id=api_schema.naming.proto_package, version=api_schema.naming.version
            )
        )

        # Construct a dictionary to insert samples into based on the API schema
        # NOTE: In the future we expect the generator to support configured samples,
        # which will result in more than one sample variant per RPC. At that
        # time a different data structure (and re-writes of add_snippet and get_snippet)
        # will be needed.
        self._index: Dict[str, Dict[str, Dict[str, Optional[Snippet]]]] = {}

        self._index = {
            s.name: {m: {"sync": None, "async": None} for m in s.methods}
            for s in api_schema.services.values()
        }

    def add_snippet(self, snippet: Snippet) -> None:
        """Add a single snippet to the snippet index.

        Args:
            snippet (Snippet): The code snippet to be added.

        Raises:
            UnknownService: If the service indicated by the snippet metadata is not found.
            RpcMethodNotFound: If the method indicated by the snippet metadata is not found.
        """
        service_name = snippet.metadata.client_method.method.service.short_name
        rpc_name = snippet.metadata.client_method.method.short_name

        service = self._index.get(service_name)
        if service is None:
            raise types.UnknownService(
                "API does not have a service named '{}'.".format(service_name)
            )

        method = service.get(rpc_name)
        if method is None:
            raise types.RpcMethodNotFound(
                "API does not have method '{}' in service '{}'".format(
                    rpc_name, service_name
                )
            )

        if getattr(snippet.metadata.client_method, "async"):
            method["async"] = snippet
        else:
            method["sync"] = snippet

        self.metadata_index.snippets.append(snippet.metadata)

    def get_snippet(
        self, service_name: str, rpc_name: str, sync: bool = True
    ) -> Optional[Snippet]:
        """Fetch a single snippet from the index.

        Args:
            service_name (str): The name of the service.
            rpc_name (str): The name of the RPC.
            sync (bool): True for the sync version of the snippet, False for the async version.

        Returns:
            Optional[Snippet]: The snippet if it exists, or None.

        Raises:
            UnknownService: If the service is not found.
            RpcMethodNotFound: If the method is not found.
        """
        # Fetch a snippet from the snippet metadata index
        service = self._index.get(service_name)
        if service is None:
            raise types.UnknownService(
                "API does not have a service named '{}'.".format(service_name)
            )
        method = service.get(rpc_name)
        if method is None:
            raise types.RpcMethodNotFound(
                "API does not have method '{}' in service '{}'".format(
                    rpc_name, service_name
                )
            )

        return method["sync" if sync else "async"]

    def get_metadata_json(self) -> str:
        """JSON representation of Snippet Index."""

        # Downstream tools assume the generator will produce the exact
        # same output when run over the same API multiple times
        self.metadata_index.snippets.sort(key=lambda s: s.region_tag)
        return json_format.MessageToJson(self.metadata_index, sort_keys=True)
