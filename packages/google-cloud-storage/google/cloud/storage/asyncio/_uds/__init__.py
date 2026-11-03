# Copyright 2026 Google LLC
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

"""Private, opt-in gRPC-over-UDS backend (Rust Core SDK ``gcs-core-server``).

Nothing here is public API. ``AsyncMultiRangeDownloader`` and
``AsyncAppendableObjectWriter`` keep their public signatures and delegate to this
backend only when enabled via ``GOOGLE_CLOUD_STORAGE_UDS=auto|on`` or
``--force-use-core-sdk`` (see :mod:`._config`). Submodules are imported lazily so the
default ``off`` mode never imports ``grpc``/``mmap``-heavy runtime code from here.
"""
