# Copyright 2024 Google LLC
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

import sys
from importlib import reload
from unittest.mock import Mock, sentinel


def test_exceptions_imports_correctly_in_base_case():
    try:
        mock = Mock(spec=[])
        sys.modules["google.resumable_media"] = mock

        from google.cloud.storage import exceptions

        reload(exceptions)
        invalid_response = exceptions.InvalidResponse(Mock())
        ir_base_names = [base.__name__ for base in invalid_response.__class__.__bases__]
        assert ir_base_names == ["Exception"]

        data_corruption = exceptions.DataCorruption(Mock())
        dc_base_names = [base.__name__ for base in data_corruption.__class__.__bases__]
        assert dc_base_names == ["Exception"]
    finally:
        del sys.modules["google.resumable_media"]
        reload(exceptions)


def test_exceptions_imports_correctly_in_resumable_media_installed_case():
    try:
        mock = Mock(spec=["InvalidResponse", "DataCorruption"])

        class InvalidResponse(Exception):
            def __init__(self, response, *args):
                super().__init__(*args)
                self.response = response

        class DataCorruption(Exception):
            def __init__(self, response, *args):
                super().__init__(*args)
                self.response = response

        mock.InvalidResponse = InvalidResponse
        mock.DataCorruption = DataCorruption

        sys.modules["google.resumable_media"] = mock

        from google.cloud.storage import exceptions

        reload(exceptions)
        invalid_response = exceptions.InvalidResponse(Mock())
        ir_base_names = [base.__name__ for base in invalid_response.__class__.__bases__]
        assert ir_base_names == ["InvalidResponse"]

        data_corruption = exceptions.DataCorruption(Mock())
        dc_base_names = [base.__name__ for base in data_corruption.__class__.__bases__]
        assert dc_base_names == ["DataCorruption"]
    finally:
        del sys.modules["google.resumable_media"]
        reload(exceptions)


def test_InvalidResponse():
    from google.cloud.storage import exceptions

    response = sentinel.response
    error = exceptions.InvalidResponse(response, 1, "a", [b"m"], True)

    assert error.response is response
    assert error.args == (1, "a", [b"m"], True)
