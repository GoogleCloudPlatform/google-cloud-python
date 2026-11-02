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
import unittest
from unittest import mock

from google.cloud.aio._cross_sync._decorators import (
    AstDecorator,
    Convert,
    ConvertClass,
    Drop,
    Pytest,
    PytestFixture,
)
from google.cloud.aio._cross_sync.cross_sync import CrossSync


class TestAstDecorator(unittest.TestCase):
    def test_decorator_with_args(self):
        class MyDecorator(AstDecorator):
            def __init__(self, a, b=None):
                self.a = a
                self.b = b

            def async_decorator(self):
                return lambda f: f

        dec = MyDecorator.decorator(1, b=2)
        self.assertTrue(callable(dec))

    def test_decorator_without_args(self):
        class MyDecorator(AstDecorator):
            def async_decorator(self):
                return lambda f: f

        def func():
            pass

        wrapped = MyDecorator.decorator(func)
        self.assertEqual(wrapped, func)

    def test_decorator_no_wrapper(self):
        class MyDecorator(AstDecorator):
            def async_decorator(self):
                return None

        def func():
            pass

        wrapped = MyDecorator.decorator(func)
        self.assertEqual(wrapped, func)

        dec = MyDecorator.decorator()
        self.assertTrue(callable(dec))
        self.assertEqual(dec(func), func)

    def test_get_for_node_invalid_format(self):
        node = ast.Name(id="NotAttribute", ctx=ast.Load())
        with self.assertRaisesRegex(ValueError, "Unexpected decorator format"):
            AstDecorator.get_for_node(node)

    def test_get_for_node_not_cross_sync(self):
        node = ast.Attribute(
            value=ast.Name(id="Other", ctx=ast.Load()), attr="Convert", ctx=ast.Load()
        )
        with self.assertRaisesRegex(ValueError, "Not a CrossSync decorator"):
            AstDecorator.get_for_node(node)

    def test_get_for_node_unknown_decorator(self):
        node = ast.Attribute(
            value=ast.Name(id="CrossSync", ctx=ast.Load()),
            attr="Unknown",
            ctx=ast.Load(),
        )
        with self.assertRaisesRegex(ValueError, "Unknown decorator encountered"):
            AstDecorator.get_for_node(node)

    def test_get_for_node_success(self):
        node = ast.Attribute(
            value=ast.Name(id="CrossSync", ctx=ast.Load()),
            attr="convert",
            ctx=ast.Load(),
        )
        # Attribute case
        inst = AstDecorator.get_for_node(node)
        self.assertIsInstance(inst, Convert)

        # Call case
        call_node = ast.Call(
            func=node,
            args=[ast.Constant(value="SyncName")],
            keywords=[ast.keyword(arg="rm_aio", value=ast.Constant(value=False))],
        )
        inst = AstDecorator.get_for_node(call_node)
        self.assertIsInstance(inst, Convert)
        self.assertEqual(inst.sync_name, "SyncName")
        self.assertFalse(inst.rm_aio)

    def test_convert_ast_to_py(self):
        self.assertIsNone(AstDecorator._convert_ast_to_py(None))
        self.assertEqual(AstDecorator._convert_ast_to_py(ast.Constant(value=1)), 1)
        self.assertEqual(
            AstDecorator._convert_ast_to_py(ast.List(elts=[ast.Constant(value=1)])), [1]
        )
        self.assertEqual(
            AstDecorator._convert_ast_to_py(ast.Tuple(elts=[ast.Constant(value=1)])),
            (1,),
        )
        self.assertEqual(
            AstDecorator._convert_ast_to_py(
                ast.Dict(
                    keys=[ast.Constant(value="k")], values=[ast.Constant(value="v")]
                )
            ),
            {"k": "v"},
        )

        node = ast.Name(id="x", ctx=ast.Load())
        self.assertEqual(AstDecorator._convert_ast_to_py(node), node)

    def test_base_methods(self):
        obj = AstDecorator()
        self.assertIsNone(obj.async_decorator())
        node = ast.Constant(value=1)
        self.assertEqual(obj.sync_ast_transform(node, {}), node)


class TestConvertClass(unittest.TestCase):
    def test_async_decorator_mapping(self):
        with mock.patch.object(CrossSync, "add_mapping") as mock_add:
            decorator = ConvertClass(add_mapping_for_name="MyClass").async_decorator()

            class MyClass:
                pass

            decorator(MyClass)
            mock_add.assert_called_once_with("MyClass", MyClass)

    def test_async_decorator_docstring(self):
        decorator = ConvertClass(
            docstring_format_vars={"var": ("async_val", "sync_val")}
        ).async_decorator()

        class MyClass:
            """Hello {var}"""

        decorator(MyClass)
        self.assertEqual(MyClass.__doc__, "Hello async_val")

    def test_sync_ast_transform(self):
        conv = ConvertClass(
            sync_name="SyncClass",
            rm_aio=True,
            add_mapping_for_name="MapName",
            replace_symbols={"A": "B"},
            docstring_format_vars={"v": ("a", "s")},
        )

        node = ast.ClassDef(
            name="AsyncClass",
            bases=[],
            keywords=[],
            body=[ast.Expr(value=ast.Constant(value="Doc {v}"))],
            decorator_list=[
                ast.Attribute(
                    value=ast.Name(id="CrossSync", ctx=ast.Load()),
                    attr="ConvertClass",
                    ctx=ast.Load(),
                )
            ],
        )

        transformers_globals = {
            "AsyncToSync": mock.Mock(return_value=mock.Mock(visit=lambda x: x)),
            "SymbolReplacer": mock.Mock(return_value=mock.Mock(visit=lambda x: x)),
        }

        res = conv.sync_ast_transform(node, transformers_globals)
        self.assertEqual(res.name, "SyncClass")
        # Decorator list should have MapName mapping and NOT CrossSync decorator
        self.assertEqual(len(res.decorator_list), 1)
        self.assertIn("add_mapping_decorator", ast.dump(res.decorator_list[0]))

        # Verify symbol replacer called
        transformers_globals["SymbolReplacer"].assert_called_once_with({"A": "B"})
        # Verify docstring updated
        self.assertEqual(res.body[0].value.value, "Doc s")

    def test_sync_ast_transform_minimal(self):
        # coverage for 253->256 (no sync_name), 261 (no decorator_list), 263->266 (no rm_aio), 288->292 (no docstring)
        conv = ConvertClass(sync_name=None, rm_aio=False, add_mapping_for_name=None)

        # Node without decorator_list and without docstring
        node = ast.ClassDef(name="AsyncClass", bases=[], keywords=[], body=[])
        # Manually remove decorator_list if it exists (some implementations might add it)
        if hasattr(node, "decorator_list"):
            delattr(node, "decorator_list")

        res = conv.sync_ast_transform(node, {})
        self.assertEqual(res.name, "AsyncClass")
        self.assertEqual(len(res.decorator_list), 0)

    def test_sync_ast_transform_no_docstring_in_body(self):
        conv = ConvertClass(docstring_format_vars={"v": ("a", "s")})
        node = ast.ClassDef(
            name="C",
            bases=[],
            keywords=[],
            body=[ast.Pass()],  # Pass instead of Constant docstring
        )
        res = conv.sync_ast_transform(node, {})
        self.assertIsInstance(res.body[0], ast.Pass)


class TestConvert(unittest.TestCase):
    def test_sync_ast_transform(self):
        conv = Convert(sync_name="sync_func")
        node = ast.AsyncFunctionDef(
            name="async_func",
            args=ast.arguments(
                posonlyargs=[],
                args=[],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[],
            decorator_list=[],
            returns=None,
        )
        transformers_globals = {
            "AsyncToSync": mock.Mock(return_value=mock.Mock(visit=lambda x: x)),
            "SymbolReplacer": mock.Mock(return_value=mock.Mock(visit=lambda x: x)),
        }
        res = conv.sync_ast_transform(node, transformers_globals)
        self.assertIsInstance(res, ast.FunctionDef)
        self.assertEqual(res.name, "sync_func")


class TestDrop(unittest.TestCase):
    def test_sync_ast_transform(self):
        self.assertIsNone(Drop().sync_ast_transform(None, None))


class TestPytest(unittest.TestCase):
    def test_async_decorator(self):
        with mock.patch("pytest.mark.asyncio", "asyncio_mark"):
            self.assertEqual(Pytest().async_decorator(), "asyncio_mark")

    def test_sync_ast_transform(self):
        pt = Pytest(rm_aio=True)
        node = ast.AsyncFunctionDef(
            name="test_async",
            args=ast.arguments(
                posonlyargs=[],
                args=[],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[],
            decorator_list=[],
            returns=None,
        )
        transformers_globals = {
            "AsyncToSync": mock.Mock(
                return_value=mock.Mock(visit=lambda x: "converted")
            ),
        }
        res = pt.sync_ast_transform(node, transformers_globals)
        self.assertEqual(res, "converted")
        transformers_globals["AsyncToSync"].assert_called_once()

    def test_sync_ast_transform_no_rm_aio(self):
        pt = Pytest(rm_aio=False)
        node = ast.AsyncFunctionDef(
            name="f",
            args=ast.arguments(
                posonlyargs=[],
                args=[],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[],
            decorator_list=[],
            returns=None,
        )
        res = pt.sync_ast_transform(node, {})
        self.assertIsInstance(res, ast.FunctionDef)


class TestPytestFixture(unittest.TestCase):
    def test_async_decorator(self):
        with mock.patch("pytest_asyncio.fixture") as mock_fixture:
            mock_fixture.return_value = lambda f: f
            decorator = PytestFixture(scope="session").async_decorator()

            def func():
                pass

            decorator(func)
            mock_fixture.assert_called_once_with(scope="session")

    def test_sync_ast_transform(self):
        # coverage for 431->433 (ast instance), 437 (no decorator_list)
        expr = ast.Constant(value="val2")
        pf = PytestFixture("arg1", kw1="val1", kw2=expr)
        node = ast.FunctionDef(
            name="fix",
            args=ast.arguments(
                posonlyargs=[],
                args=[],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[],
            returns=None,
        )
        if hasattr(node, "decorator_list"):
            delattr(node, "decorator_list")

        res = pf.sync_ast_transform(node, None)
        self.assertEqual(len(res.decorator_list), 1)
        dump = ast.dump(res.decorator_list[0])
        self.assertIn("fixture", dump)
        self.assertIn("arg1", dump)
        self.assertIn("val1", dump)
        self.assertIn("val2", dump)
