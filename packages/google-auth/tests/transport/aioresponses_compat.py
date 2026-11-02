# Copyright 2026 Google LLC
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

import inspect

import aiohttp
from aioresponses.core import RequestMatch  # type: ignore


class _DummyWriter:
    output_size = 0

    def done(self):
        return True

    def add_done_callback(self, fn, *args, **kwargs):
        pass

    def remove_done_callback(self, fn):
        pass

    def __await__(self):
        if False:
            yield
        return None


class _CompatClientResponse(aiohttp.ClientResponse):
    """ClientResponse subclass for aioresponses compatibility across all aiohttp versions."""

    def __init__(self, *args, **kwargs):
        writer = kwargs.pop("writer", None)
        stream_writer = kwargs.pop("stream_writer", None)
        writer_obj = stream_writer or writer or _DummyWriter()
        sig = inspect.signature(super().__init__)
        if "stream_writer" in sig.parameters:
            kwargs["stream_writer"] = writer_obj
        if "writer" in sig.parameters:
            kwargs["writer"] = writer_obj
        super().__init__(*args, **kwargs)


def patch_aioresponses():
    """Patch RequestMatch.__init__ to use _CompatClientResponse by default."""
    if getattr(RequestMatch, "_is_compat_patched", False):
        return
    orig_init = RequestMatch.__init__

    def _request_match_init(self, *args, **kwargs):
        if kwargs.get("response_class") is None:
            kwargs["response_class"] = _CompatClientResponse
        orig_init(self, *args, **kwargs)

    RequestMatch.__init__ = _request_match_init
    RequestMatch._is_compat_patched = True
