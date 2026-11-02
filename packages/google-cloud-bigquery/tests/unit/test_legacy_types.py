# -*- coding: utf-8 -*-
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

import warnings

import pytest

try:
    import proto
except ImportError:  # pragma: NO COVER
    proto = None  # type: ignore


@pytest.mark.skipif(proto is None, reason="proto is not installed")
def test_importing_legacy_types_emits_warning():
    with warnings.catch_warnings(record=True) as warned:
        from google.cloud.bigquery_v2 import types  # noqa: F401

    assert len(warned) == 1
    assert warned[0].category is DeprecationWarning
    warning_msg = str(warned[0])
    assert "bigquery_v2" in warning_msg
    assert "not maintained" in warning_msg
