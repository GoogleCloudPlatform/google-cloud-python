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

import builtins
import unittest.mock as mock

import db_dtypes.pandas_backports as pandas_backports

REAL_IMPORT = builtins.__import__


def _import_side_effect(module_name, result_return=None, result_raise=None):
    """
    Builds a side-effect for mocking the import function.
    If the imported package matches `name`, it will return or raise based on
    arguments. Otherwise, it will default to regular import behaviour
    """

    def _impl(name, *args, **kwargs):
        if name == module_name:
            if result_raise:
                raise result_raise
            else:
                return result_return
        else:  # pragma: NO COVER
            return REAL_IMPORT(name, *args, **kwargs)

    return _impl


@mock.patch("builtins.__import__")
def test_import_default_module_found(mock_import):
    mock_module = mock.MagicMock()
    mock_module.OpsMixin = "OpsMixin_from_module"

    mock_import.side_effect = _import_side_effect("module_name", mock_module)

    default_class = type("OpsMixin", (), {})  # Dummy class
    result = pandas_backports.import_default("module_name", default=default_class)
    assert result == "OpsMixin_from_module"


@mock.patch("builtins.__import__")
def test_import_default_module_not_found(mock_import):
    mock_import.side_effect = _import_side_effect(
        "module_name", result_raise=ModuleNotFoundError
    )

    default_class = type("OpsMixin", (), {})  # Dummy class
    result = pandas_backports.import_default("module_name", default=default_class)
    assert result == default_class


@mock.patch("builtins.__import__")
def test_import_default_force_true(mock_import):
    """
    Test that when force=True, the default is returned immediately
    without attempting an import.
    """
    default_class = type("ForcedMixin", (), {})  # A dummy class

    result = pandas_backports.import_default(
        "any_module_name", force=True, default=default_class
    )
    assert mock_import.call_count == 0

    # Assert that the returned value is the default class itself
    assert result is default_class
