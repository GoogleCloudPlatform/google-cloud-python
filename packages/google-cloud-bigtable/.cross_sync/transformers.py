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
"""
Provides a set of ast.NodeTransformer subclasses that are composed to generate
async code into sync code.

At a high level:
- The main entrypoint is CrossSyncFileProcessor, which is used to find files in
  the codebase that include __CROSS_SYNC_OUTPUT__, and transform them
  according to the `CrossSync` annotations they contains
- SymbolReplacer is used to swap out CrossSync.X with CrossSync._Sync_Impl.X
- RmAioFunctions is used to strip out asyncio keywords marked with CrossSync.rm_aio
  (deferring to AsyncToSync to handle the actual transformation)
- StripAsyncConditionalBranches finds `if CrossSync.is_async:` conditionals, and strips out
  the unneeded branch for the sync output
"""
from __future__ import annotations

import ast

import sys
# add cross_sync to path
sys.path.append("google/cloud/bigtable/data/_cross_sync")
from _decorators import AstDecorator


class SymbolReplacer(ast.NodeTransformer):
    """
    Replaces all instances of a symbol in an AST with a replacement

    Works for function signatures, method calls, docstrings, and type annotations
    """
    def __init__(self, replacements: dict[str, str]):
        self.replacements = replacements

    def visit_Name(self, node):
        if node.id in self.replacements:
            node.id = self.replacements[node.id]
        return node

    def visit_Attribute(self, node):
        return ast.copy_location(
            ast.Attribute(
                self.visit(node.value),
                self.replacements.get(node.attr, node.attr),
                node.ctx,
            ),
            node,
        )

    def visit_AsyncFunctionDef(self, node):
        """
        Replace async function docstrings
        """
        # use same logic as FunctionDef
        return self.visit_FunctionDef(node)

    def visit_FunctionDef(self, node):
        """
        Replace function docstrings
        """
        docstring = ast.get_docstring(node)
        if docstring and isinstance(node.body[0], ast.Expr) \
            and isinstance(node.body[0].value, ast.Constant) \
            and isinstance(node.body[0].value.value, str) \
        :
            for key_word, replacement in self.replacements.items():
                docstring = docstring.replace(key_word, replacement)
            node.body[0].value.value = docstring
        return self.generic_visit(node)

    def visit_Constant(self, node):
        """Replace string type annotations"""
        try:
            node.value = self.replacements.get(node.value, node.value)
        except TypeError:
            # ignore unhashable types (e.g. list)
            pass
        return node


class AsyncToSync(ast.NodeTransformer):
    """
    Replaces or strips all async keywords from a given AST
    """
    def visit_Await(self, node):
        """
        Strips await keyword
        """
        return self.visit(node.value)

    def visit_AsyncFor(self, node):
        """
        Replaces `async for` with `for`
        """
        return ast.copy_location(
            ast.For(
                self.visit(node.target),
                self.visit(node.iter),
                [self.visit(stmt) for stmt in node.body],
                [self.visit(stmt) for stmt in node.orelse],
            ),
            node,
        )

    def visit_AsyncWith(self, node):
        """
        Replaces `async with` with `with`
        """
        return ast.copy_location(
            ast.With(
                [self.visit(item) for item in node.items],
                [self.visit(stmt) for stmt in node.body],
            ),
            node,
        )

    def visit_AsyncFunctionDef(self, node):
        """
        Replaces `async def` with `def`
        """
        return ast.copy_location(
            ast.FunctionDef(
                node.name,
                self.visit(node.args),
                [self.visit(stmt) for stmt in node.body],
                [self.visit(decorator) for decorator in node.decorator_list],
                node.returns and self.visit(node.returns),
            ),
            node,
        )

    def visit_ListComp(self, node):
        """
        Replaces `async for` with `for` in list comprehensions
        """
        for generator in node.generators:
            generator.is_async = False
        return self.generic_visit(node)


class RmAioFunctions(ast.NodeTransformer):
    """
    Visits all calls marked with CrossSync.rm_aio, and removes asyncio keywords
    """
    RM_AIO_FN_NAME = "rm_aio"
    RM_AIO_CLASS_NAME = "CrossSync"

    def __init__(self):
        self.to_sync = AsyncToSync()

    def _is_rm_aio_call(self, node) -> bool:
        """
        Check if a node is a CrossSync.rm_aio call
        """
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name):
            if node.func.attr == self.RM_AIO_FN_NAME and node.func.value.id == self.RM_AIO_CLASS_NAME:
                return True
        return False

    def visit_Call(self, node):
        if self._is_rm_aio_call(node):
            return self.visit(self.to_sync.visit(node.args[0]))
        return self.generic_visit(node)

    def visit_AsyncWith(self, node):
        """
        `async with` statements can contain multiple async context managers.

        If any of them contains a CrossSync.rm_aio statement, convert into standard `with` statement
        """
        if any(self._is_rm_aio_call(item.context_expr) for item in node.items
               ):
            new_node = ast.copy_location(
                ast.With(
                    [self.visit(item) for item in node.items],
                    [self.visit(stmt) for stmt in node.body],
                ),
                node,
            )
            return self.generic_visit(new_node)
        return self.generic_visit(node)

    def visit_AsyncFor(self, node):
        """
        Async for statements are not fully wrapped by calls
        """
        it = node.iter
        if self._is_rm_aio_call(it):
            return ast.copy_location(
                ast.For(
                    self.visit(node.target),
                    self.visit(it),
                    [self.visit(stmt) for stmt in node.body],
                    [self.visit(stmt) for stmt in node.orelse],
                ),
                node,
            )
        return self.generic_visit(node)


class StripAsyncConditionalBranches(ast.NodeTransformer):
    """
    Visits all if statements in an AST, and removes branches marked with CrossSync.is_async
    """

    def visit_If(self, node):
        """
        remove CrossSync.is_async branches from top-level if statements
        """
        kept_branch = None
        # check for CrossSync.is_async
        if self._is_async_check(node.test):
            kept_branch = node.orelse
        # check for not CrossSync.is_async
        elif isinstance(node.test, ast.UnaryOp) and isinstance(node.test.op, ast.Not) and self._is_async_check(node.test.operand):
            kept_branch = node.body
        if kept_branch is not None:
            # only keep the statements in the kept branch
            return [self.visit(n) for n in kept_branch]
        else:
            # keep the entire if statement
            return self.generic_visit(node)

    def _is_async_check(self, node) -> bool:
        """
        Check for CrossSync.is_async or CrossSync.is_async == True checks
        """
        if isinstance(node, ast.Attribute):
            # for CrossSync.is_async
            return isinstance(node.value, ast.Name) and node.value.id == "CrossSync" and node.attr == "is_async"
        elif isinstance(node, ast.Compare):
            # for CrossSync.is_async == True
            return self._is_async_check(node.left) and (isinstance(node.ops[0], ast.Eq) or isinstance(node.ops[0], ast.Is)) and len(node.comparators) == 1 and node.comparators[0].value == True
        return False


class CrossSyncFileProcessor(ast.NodeTransformer):
    """
    Visits a file, looking for __CROSS_SYNC_OUTPUT__ annotations

    If found, the file is processed with the following steps:
      - Strip out asyncio keywords within CrossSync.rm_aio calls
      - transform classes and methods annotated with CrossSync decorators
      - statements behind CrossSync.is_async conditional branches are removed
      - Replace remaining CrossSync statements with corresponding CrossSync._Sync_Impl calls
      - save changes in an output file at path specified by __CROSS_SYNC_OUTPUT__
    """
    FILE_ANNOTATION = "__CROSS_SYNC_OUTPUT__"

    def get_output_path(self, node):
        for n in node.body:
            if isinstance(n, ast.Assign):
                for target in n.targets:
                    if isinstance(target, ast.Name) and target.id == self.FILE_ANNOTATION:
                        # return the output path
                        return n.value.value.replace(".", "/") + ".py"

    def visit_Module(self, node):
        # look for __CROSS_SYNC_OUTPUT__ Assign statement
        output_path = self.get_output_path(node)
        if output_path:
            # if found, process the file
            converted = self.generic_visit(node)
            # strip out CrossSync.rm_aio calls
            converted = RmAioFunctions().visit(converted)
            # strip out CrossSync.is_async branches
            converted = StripAsyncConditionalBranches().visit(converted)
            # replace CrossSync statements
            converted = SymbolReplacer({"CrossSync": "CrossSync._Sync_Impl"}).visit(converted)
            return converted
        else:
            # not cross_sync file. Return None
            return None

    def visit_ClassDef(self, node):
        """
        Called for each class in file. If class has a CrossSync decorator, it will be transformed
        according to the decorator arguments. Otherwise, class is returned unchanged
        """
        orig_decorators = node.decorator_list
        for decorator in orig_decorators:
            try:
                handler = AstDecorator.get_for_node(decorator)
                # transformation is handled in sync_ast_transform method of the decorator
                node = handler.sync_ast_transform(node, globals())
            except ValueError:
                # not cross_sync decorator
                continue
        return self.generic_visit(node) if node else None

    def visit_Assign(self, node):
        """
        strip out __CROSS_SYNC_OUTPUT__ assignments
        """
        if isinstance(node.targets[0], ast.Name) and node.targets[0].id == self.FILE_ANNOTATION:
            return None
        return self.generic_visit(node)

    def visit_FunctionDef(self, node):
        """
        Visit any sync methods marked with CrossSync decorators
        """
        return self.visit_AsyncFunctionDef(node)

    def visit_AsyncFunctionDef(self, node):
        """
        Visit and transform any async methods marked with CrossSync decorators
        """
        try:
            if hasattr(node, "decorator_list"):
                found_list, node.decorator_list = node.decorator_list, []
                for decorator in found_list:
                    try:
                        handler = AstDecorator.get_for_node(decorator)
                        node = handler.sync_ast_transform(node, globals())
                        if node is None:
                            return None
                        # recurse to any nested functions
                        node = self.generic_visit(node)
                    except ValueError:
                        # keep unknown decorators
                        node.decorator_list.append(decorator)
                        continue
            return self.generic_visit(node)
        except ValueError as e:
            raise ValueError(f"node {node.name} failed") from e
