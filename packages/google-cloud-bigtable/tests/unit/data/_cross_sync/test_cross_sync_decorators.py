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

import ast
from unittest import mock

import pytest
import pytest_asyncio

from google.cloud.bigtable.data._cross_sync._decorators import (
    Convert,
    ConvertClass,
    Drop,
    Pytest,
    PytestFixture,
)
from google.cloud.bigtable.data._cross_sync.cross_sync import CrossSync


@pytest.fixture
def globals_mock():
    mock_transform = mock.Mock()
    mock_transform().visit = lambda x: x
    global_dict = {
        k: mock_transform
        for k in ["RmAioFunctions", "SymbolReplacer", "CrossSyncMethodDecoratorHandler"]
    }
    return global_dict


class TestConvertClassDecorator:
    def _get_class(self):
        return ConvertClass

    def test_ctor_defaults(self):
        """
        Should set default values for path, add_mapping_for_name, and docstring_format_vars
        """
        instance = self._get_class()()
        assert instance.sync_name is None
        assert instance.replace_symbols is None
        assert instance.add_mapping_for_name is None
        assert instance.async_docstring_format_vars == {}
        assert instance.sync_docstring_format_vars == {}
        assert instance.rm_aio is False

    def test_ctor(self):
        sync_name = "sync_name"
        replace_symbols = {"a": "b"}
        docstring_format_vars = {"A": (1, 2)}
        add_mapping_for_name = "test_name"
        rm_aio = True

        instance = self._get_class()(
            sync_name,
            replace_symbols=replace_symbols,
            docstring_format_vars=docstring_format_vars,
            add_mapping_for_name=add_mapping_for_name,
            rm_aio=rm_aio,
        )
        assert instance.sync_name is sync_name
        assert instance.replace_symbols is replace_symbols
        assert instance.add_mapping_for_name is add_mapping_for_name
        assert instance.async_docstring_format_vars == {"A": 1}
        assert instance.sync_docstring_format_vars == {"A": 2}
        assert instance.rm_aio is rm_aio

    def test_class_decorator(self):
        """
        Should return class being decorated
        """
        unwrapped_class = mock.Mock
        wrapped_class = self._get_class().decorator(unwrapped_class, sync_name="s")
        assert unwrapped_class == wrapped_class

    def test_class_decorator_adds_mapping(self):
        """
        If add_mapping_for_name is set, should call CrossSync.add_mapping with the class being decorated
        """
        with mock.patch.object(CrossSync, "add_mapping") as add_mapping:
            mock_cls = mock.Mock
            # check decoration with no add_mapping
            self._get_class().decorator(sync_name="s")(mock_cls)
            assert add_mapping.call_count == 0
            # check decoration with add_mapping
            name = "test_name"
            self._get_class().decorator(sync_name="s", add_mapping_for_name=name)(
                mock_cls
            )
            assert add_mapping.call_count == 1
            add_mapping.assert_called_once_with(name, mock_cls)

    @pytest.mark.parametrize(
        "docstring,format_vars,expected",
        [
            ["test docstring", {}, "test docstring"],
            ["{}", {}, "{}"],
            ["test_docstring", {"A": (1, 2)}, "test_docstring"],
            ["{A}", {"A": (1, 2)}, "1"],
            ["{A} {B}", {"A": (1, 2), "B": (3, 4)}, "1 3"],
            ["hello {world_var}", {"world_var": ("world", "moon")}, "hello world"],
            ["{empty}", {"empty": ("", "")}, ""],
            ["{empty}", {"empty": (None, None)}, ""],
            ["maybe{empty}", {"empty": (None, "yes")}, "maybe"],
            ["maybe{empty}", {"empty": (" no", None)}, "maybe no"],
        ],
    )
    def test_class_decorator_docstring_update(self, docstring, format_vars, expected):
        """
        If docstring_format_vars is set, should update the docstring
        of the class being decorated
        """

        @ConvertClass.decorator(sync_name="s", docstring_format_vars=format_vars)
        class Class:
            __doc__ = docstring

        assert Class.__doc__ == expected
        # check internal state
        instance = self._get_class()(sync_name="s", docstring_format_vars=format_vars)
        async_replacements = {k: v[0] or "" for k, v in format_vars.items()}
        sync_replacements = {k: v[1] or "" for k, v in format_vars.items()}
        assert instance.async_docstring_format_vars == async_replacements
        assert instance.sync_docstring_format_vars == sync_replacements

    def test_sync_ast_transform_replaces_name(self, globals_mock):
        """
        Should update the name of the new class
        """
        decorator = self._get_class()("SyncClass")
        mock_node = ast.ClassDef(name="AsyncClass", bases=[], keywords=[], body=[])

        result = decorator.sync_ast_transform(mock_node, globals_mock)

        assert isinstance(result, ast.ClassDef)
        assert result.name == "SyncClass"

    def test_sync_ast_transform_strips_cross_sync_decorators(self, globals_mock):
        """
        should remove all CrossSync decorators from the class
        """
        decorator = self._get_class()("path")
        cross_sync_decorator = ast.Call(
            func=ast.Attribute(
                value=ast.Name(id="CrossSync", ctx=ast.Load()),
                attr="some_decorator",
                ctx=ast.Load(),
            ),
            args=[],
            keywords=[],
        )
        other_decorator = ast.Name(id="other_decorator", ctx=ast.Load())
        mock_node = ast.ClassDef(
            name="AsyncClass",
            bases=[],
            keywords=[],
            body=[],
            decorator_list=[cross_sync_decorator, other_decorator],
        )

        result = decorator.sync_ast_transform(mock_node, globals_mock)

        assert isinstance(result, ast.ClassDef)
        assert len(result.decorator_list) == 1
        assert isinstance(result.decorator_list[0], ast.Name)
        assert result.decorator_list[0].id == "other_decorator"

    def test_sync_ast_transform_add_mapping(self, globals_mock):
        """
        If add_mapping_for_name is set, should add CrossSync.add_mapping_decorator to new class
        """
        decorator = self._get_class()("path", add_mapping_for_name="sync_class")
        mock_node = ast.ClassDef(name="AsyncClass", bases=[], keywords=[], body=[])

        result = decorator.sync_ast_transform(mock_node, globals_mock)

        assert isinstance(result, ast.ClassDef)
        assert len(result.decorator_list) == 1
        assert isinstance(result.decorator_list[0], ast.Call)
        assert isinstance(result.decorator_list[0].func, ast.Attribute)
        assert result.decorator_list[0].func.attr == "add_mapping_decorator"
        assert result.decorator_list[0].args[0].value == "sync_class"

    @pytest.mark.parametrize(
        "docstring,format_vars,expected",
        [
            ["test docstring", {}, "test docstring"],
            ["{}", {}, "{}"],
            ["test_docstring", {"A": (1, 2)}, "test_docstring"],
            ["{A}", {"A": (1, 2)}, "2"],
            ["{A} {B}", {"A": (1, 2), "B": (3, 4)}, "2 4"],
            ["hello {world_var}", {"world_var": ("world", "moon")}, "hello moon"],
        ],
    )
    def test_sync_ast_transform_add_docstring_format(
        self, docstring, format_vars, expected, globals_mock
    ):
        """
        If docstring_format_vars is set, should format the docstring of the new class
        """
        decorator = self._get_class()(
            "path.to.SyncClass", docstring_format_vars=format_vars
        )
        mock_node = ast.ClassDef(
            name="AsyncClass",
            bases=[],
            keywords=[],
            body=[ast.Expr(value=ast.Constant(value=docstring))],
        )
        result = decorator.sync_ast_transform(mock_node, globals_mock)

        assert isinstance(result, ast.ClassDef)
        assert isinstance(result.body[0], ast.Expr)
        assert isinstance(result.body[0].value, ast.Constant)
        assert result.body[0].value.value == expected

    def test_sync_ast_transform_replace_symbols(self, globals_mock):
        """
        SymbolReplacer should be called with replace_symbols
        """
        replace_symbols = {"a": "b", "c": "d"}
        decorator = self._get_class()(
            "path.to.SyncClass", replace_symbols=replace_symbols
        )
        mock_node = ast.ClassDef(name="AsyncClass", bases=[], keywords=[], body=[])
        symbol_transform_mock = mock.Mock()
        globals_mock = {**globals_mock, "SymbolReplacer": symbol_transform_mock}
        decorator.sync_ast_transform(mock_node, globals_mock)
        # make sure SymbolReplacer was called with replace_symbols
        assert symbol_transform_mock.call_count == 1
        found_dict = symbol_transform_mock.call_args[0][0]
        assert "a" in found_dict
        for k, v in replace_symbols.items():
            assert found_dict[k] == v

    def test_sync_ast_transform_rmaio_calls_async_to_sync(self):
        """
        Should call AsyncToSync if rm_aio is set
        """
        decorator = self._get_class()(rm_aio=True)
        mock_node = ast.ClassDef(name="AsyncClass", bases=[], keywords=[], body=[])
        async_to_sync_mock = mock.Mock()
        async_to_sync_mock.visit.side_effect = lambda x: x
        globals_mock = {"AsyncToSync": lambda: async_to_sync_mock}

        decorator.sync_ast_transform(mock_node, globals_mock)
        assert async_to_sync_mock.visit.call_count == 1


class TestConvertDecorator:
    def _get_class(self):
        return Convert

    def test_ctor_defaults(self):
        instance = self._get_class()()
        assert instance.sync_name is None
        assert instance.replace_symbols is None
        assert instance.async_docstring_format_vars == {}
        assert instance.sync_docstring_format_vars == {}
        assert instance.rm_aio is True

    def test_ctor(self):
        sync_name = "sync_name"
        replace_symbols = {"a": "b"}
        docstring_format_vars = {"A": (1, 2)}
        rm_aio = False

        instance = self._get_class()(
            sync_name=sync_name,
            replace_symbols=replace_symbols,
            docstring_format_vars=docstring_format_vars,
            rm_aio=rm_aio,
        )
        assert instance.sync_name is sync_name
        assert instance.replace_symbols is replace_symbols
        assert instance.async_docstring_format_vars == {"A": 1}
        assert instance.sync_docstring_format_vars == {"A": 2}
        assert instance.rm_aio is rm_aio

    def test_async_decorator_no_docstring(self):
        """
        If no docstring_format_vars is set, should be a no-op
        """
        unwrapped_class = mock.Mock
        wrapped_class = self._get_class().decorator(unwrapped_class)
        assert unwrapped_class == wrapped_class

    @pytest.mark.parametrize(
        "docstring,format_vars,expected",
        [
            ["test docstring", {}, "test docstring"],
            ["{}", {}, "{}"],
            ["test_docstring", {"A": (1, 2)}, "test_docstring"],
            ["{A}", {"A": (1, 2)}, "1"],
            ["{A} {B}", {"A": (1, 2), "B": (3, 4)}, "1 3"],
            ["hello {world_var}", {"world_var": ("world", "moon")}, "hello world"],
            ["{empty}", {"empty": ("", "")}, ""],
            ["{empty}", {"empty": (None, None)}, ""],
            ["maybe{empty}", {"empty": (None, "yes")}, "maybe"],
            ["maybe{empty}", {"empty": (" no", None)}, "maybe no"],
        ],
    )
    def test_async_decorator_docstring_update(self, docstring, format_vars, expected):
        """
        If docstring_format_vars is set, should update the docstring
        of the class being decorated
        """

        @Convert.decorator(docstring_format_vars=format_vars)
        class Class:
            __doc__ = docstring

        assert Class.__doc__ == expected
        # check internal state
        instance = self._get_class()(docstring_format_vars=format_vars)
        async_replacements = {k: v[0] or "" for k, v in format_vars.items()}
        sync_replacements = {k: v[1] or "" for k, v in format_vars.items()}
        assert instance.async_docstring_format_vars == async_replacements
        assert instance.sync_docstring_format_vars == sync_replacements

    def test_sync_ast_transform_remove_adef(self):
        """
        Should convert `async def` methods to `def` methods
        """
        decorator = self._get_class()(rm_aio=False)
        mock_node = ast.AsyncFunctionDef(
            name="test_method", args=ast.arguments(), body=[]
        )

        result = decorator.sync_ast_transform(mock_node, {})

        assert isinstance(result, ast.FunctionDef)
        assert result.name == "test_method"

    def test_sync_ast_transform_replaces_name(self, globals_mock):
        """
        Should update the name of the method if sync_name is set
        """
        decorator = self._get_class()(sync_name="new_method_name", rm_aio=False)
        mock_node = ast.AsyncFunctionDef(
            name="old_method_name", args=ast.arguments(), body=[]
        )

        result = decorator.sync_ast_transform(mock_node, globals_mock)

        assert isinstance(result, ast.FunctionDef)
        assert result.name == "new_method_name"

    def test_sync_ast_transform_rmaio_calls_async_to_sync(self):
        """
        Should call AsyncToSync if rm_aio is set
        """
        decorator = self._get_class()(rm_aio=True)
        mock_node = ast.AsyncFunctionDef(
            name="test_method", args=ast.arguments(), body=[]
        )
        async_to_sync_mock = mock.Mock()
        async_to_sync_mock.visit.return_value = mock_node
        globals_mock = {"AsyncToSync": lambda: async_to_sync_mock}

        decorator.sync_ast_transform(mock_node, globals_mock)
        assert async_to_sync_mock.visit.call_count == 1

    def test_sync_ast_transform_replace_symbols(self):
        """
        Should call SymbolReplacer with replace_symbols if replace_symbols is set
        """
        replace_symbols = {"old_symbol": "new_symbol"}
        decorator = self._get_class()(replace_symbols=replace_symbols, rm_aio=False)
        mock_node = ast.AsyncFunctionDef(
            name="test_method", args=ast.arguments(), body=[]
        )
        symbol_replacer_mock = mock.Mock()
        globals_mock = {"SymbolReplacer": symbol_replacer_mock}

        decorator.sync_ast_transform(mock_node, globals_mock)

        assert symbol_replacer_mock.call_count == 1
        assert symbol_replacer_mock.call_args[0][0] == replace_symbols
        assert symbol_replacer_mock(replace_symbols).visit.call_count == 1

    @pytest.mark.parametrize(
        "docstring,format_vars,expected",
        [
            ["test docstring", {}, "test docstring"],
            ["{}", {}, "{}"],
            ["test_docstring", {"A": (1, 2)}, "test_docstring"],
            ["{A}", {"A": (1, 2)}, "2"],
            ["{A} {B}", {"A": (1, 2), "B": (3, 4)}, "2 4"],
            ["hello {world_var}", {"world_var": ("world", "moon")}, "hello moon"],
        ],
    )
    def test_sync_ast_transform_add_docstring_format(
        self, docstring, format_vars, expected
    ):
        """
        If docstring_format_vars is set, should format the docstring of the new method
        """
        decorator = self._get_class()(docstring_format_vars=format_vars, rm_aio=False)
        mock_node = ast.AsyncFunctionDef(
            name="test_method",
            args=ast.arguments(),
            body=[ast.Expr(value=ast.Constant(value=docstring))],
        )

        result = decorator.sync_ast_transform(mock_node, {})

        assert isinstance(result, ast.FunctionDef)
        assert isinstance(result.body[0], ast.Expr)
        assert isinstance(result.body[0].value, ast.Constant)
        assert result.body[0].value.value == expected


class TestDropDecorator:
    def _get_class(self):
        return Drop

    def test_decorator_functionality(self):
        """
        applying the decorator should be a no-op
        """
        unwrapped = lambda x: x  # noqa: E731
        wrapped = self._get_class().decorator(unwrapped)
        assert unwrapped == wrapped
        assert unwrapped(1) == wrapped(1)
        assert wrapped(1) == 1

    def test_sync_ast_transform(self):
        """
        Should return None for any input method
        """
        decorator = self._get_class()()
        mock_node = ast.AsyncFunctionDef(
            name="test_method", args=ast.arguments(), body=[]
        )

        result = decorator.sync_ast_transform(mock_node, {})

        assert result is None


class TestPytestDecorator:
    def _get_class(self):
        return Pytest

    def test_ctor(self):
        instance = self._get_class()()
        assert instance.rm_aio is True
        instance = self._get_class()(rm_aio=False)
        assert instance.rm_aio is False

    def test_decorator_functionality(self):
        """
        Should wrap the class with pytest.mark.asyncio
        """
        unwrapped_fn = mock.Mock
        wrapped_class = self._get_class().decorator(unwrapped_fn)
        assert wrapped_class == pytest.mark.asyncio(unwrapped_fn)

    def test_sync_ast_transform(self):
        """
        If rm_aio is True (default), should call AsyncToSync on the class
        """
        decorator = self._get_class()()
        mock_node = ast.AsyncFunctionDef(
            name="AsyncMethod", args=ast.arguments(), body=[]
        )

        async_to_sync_mock = mock.Mock()
        async_to_sync_mock.visit.side_effect = lambda x: x
        globals_mock = {"AsyncToSync": lambda: async_to_sync_mock}

        transformed = decorator.sync_ast_transform(mock_node, globals_mock)
        assert async_to_sync_mock.visit.call_count == 1
        assert isinstance(transformed, ast.FunctionDef)

    def test_sync_ast_transform_no_rm_aio(self):
        """
        if rm_aio is False, should remove the async keyword from the method
        """
        decorator = self._get_class()(rm_aio=False)
        mock_node = ast.AsyncFunctionDef(
            name="AsyncMethod", args=ast.arguments(), body=[]
        )

        async_to_sync_mock = mock.Mock()
        async_to_sync_mock.visit.return_value = mock_node
        globals_mock = {"AsyncToSync": lambda: async_to_sync_mock}

        transformed = decorator.sync_ast_transform(mock_node, globals_mock)
        assert async_to_sync_mock.visit.call_count == 0
        assert isinstance(transformed, ast.FunctionDef)


class TestPytestFixtureDecorator:
    def _get_class(self):
        return PytestFixture

    def test_decorator_functionality(self):
        """
        Should wrap the class with pytest_asyncio.fixture
        """
        with mock.patch.object(pytest_asyncio, "fixture") as fixture:

            @PytestFixture.decorator(1, 2, scope="function", params=[3, 4])
            def fn():
                pass

            assert fixture.call_count == 1
            assert fixture.call_args[0] == (1, 2)
            assert fixture.call_args[1] == {"scope": "function", "params": [3, 4]}

    def test_sync_ast_transform(self):
        """
        Should attach pytest.fixture to generated method
        """
        decorator = self._get_class()(1, 2, scope="function")

        mock_node = ast.AsyncFunctionDef(
            name="test_method", args=ast.arguments(), body=[]
        )

        result = decorator.sync_ast_transform(mock_node, {})

        assert isinstance(result, ast.AsyncFunctionDef)
        assert len(result.decorator_list) == 1
        assert isinstance(result.decorator_list[0], ast.Call)
        assert result.decorator_list[0].func.value.id == "pytest"
        assert result.decorator_list[0].func.attr == "fixture"
        assert result.decorator_list[0].args[0].value == 1
        assert result.decorator_list[0].args[1].value == 2
        assert result.decorator_list[0].keywords[0].arg == "scope"
        assert result.decorator_list[0].keywords[0].value.value == "function"
