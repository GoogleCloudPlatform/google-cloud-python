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

"""The ``metadata`` module defines schema for where data was parsed from.
This library places every protocol buffer descriptor in a wrapper class
(see :mod:`~.wrappers`) before loading it into the :class:`~.API` object.

As we iterate over descriptors during the loading process, it is important
to know where they came from, because sometimes protocol buffer types are
referenced by fully-qualified string (e.g. ``method.input_type``), and we
want to resolve those references.

Additionally, protocol buffers stores data from the comments in the ``.proto``
in a separate structure, and this object model re-connects the comments
with the things they describe for easy access in templates.
"""

import dataclasses
import re
from typing import FrozenSet, Set, Tuple, Optional

from google.protobuf import descriptor_pb2

from gapic.schema import imp
from gapic.schema import naming
from gapic.utils import cached_property
from gapic.utils import cached_proto_context
from gapic.utils import RESERVED_NAMES

# This class is a minor hack to optimize Address's __eq__ method.


@dataclasses.dataclass(frozen=True)
class BaseAddress:
    name: str = ""
    module: str = ""
    module_path: Tuple[int, ...] = dataclasses.field(default_factory=tuple)
    package: Tuple[str, ...] = dataclasses.field(default_factory=tuple)
    parent: Tuple[str, ...] = dataclasses.field(default_factory=tuple)


@dataclasses.dataclass(frozen=True)
class Address(BaseAddress):
    api_naming: naming.Naming = dataclasses.field(
        default_factory=naming.NewNaming,
    )
    collisions: Set[str] = dataclasses.field(default_factory=set)

    def __eq__(self, other) -> bool:
        # We don't want to use api_naming or collisions to determine equality,
        # so defer to the parent class's eq method.
        # This is an fairly important optimization for large APIs.
        return super().__eq__(other)

    def __hash__(self):
        # Do NOT include collisions; they are not relevant.
        return hash(
            (
                self.name,
                self.module,
                self.module_path,
                self.package,
                self.parent,
                self.api_naming,
            )
        )

    def __str__(self) -> str:
        """Return the Python identifier for this type.

        Because we import modules as a whole, rather than individual
        members from modules, this is consistently `module.Name`.
        """
        # Most (but not all) types are in a module.
        if self.module:
            module_name = self.module

            # If collisions are registered and conflict with our module,
            # use the module alias instead.
            if self.module_alias:
                module_name = self.module_alias

            # Add _pb2 suffix except when it is a proto-plus type
            if not self.is_proto_plus_type:
                module_name = f"{self.module}_pb2"

            # Return the dot-separated Python identifier.
            return ".".join((module_name,) + self.parent + (self.name,))

        # This type does not have a module (most common for PythonType).
        # Return the Python identifier.
        return ".".join(self.parent + (self.name,))

    @property
    def is_proto_plus_type(self) -> bool:
        """This function is used to determine whether a given package `self.proto_package`
        is using proto-plus types or protobuf types. There are 2 scenarios where the package
        is expected to use proto-plus types:
        1) When `self.proto_package` starts with `self.api_naming.proto_package`, then
        the given package has the same namespace as the one that is being generated. It is assumed
        that the gapic generator always generates packages with proto-plus types.
        2) When `self.proto_package` is explicitly in `self.api_naming.proto_plus_deps` which is
        populated via the generator option `proto-plus-deps`.

        Returns:
            bool: Whether the given package uses proto-plus types or not.
        """
        return self.proto_package.startswith(self.api_naming.proto_package) or (
            hasattr(self.api_naming, "proto_plus_deps")
            and self.proto_package in self.api_naming.proto_plus_deps
        )

    @cached_property
    def __cached_string_repr(self):
        return "({})".format(
            ", ".join(
                (
                    self.name,
                    self.module,
                    str(self.module_path),
                    str(self.package),
                    str(self.parent),
                    str(self.api_naming),
                )
            )
        )

    def __repr__(self) -> str:
        return self.__cached_string_repr

    @property
    def module_alias(self) -> str:
        """Return an appropriate module alias if necessary.

        If the module name is not a collision, return empty string.

        This method provides a mechanism for resolving naming conflicts,
        while still providing names that are fundamentally readable
        to users (albeit looking auto-generated).
        """
        # This is a minor optimization to prevent constructing a temporary set.
        if self.module in self.collisions or self.module in RESERVED_NAMES:
            return "_".join(
                (
                    "".join(
                        partial_name[0]
                        for i in self.package
                        for partial_name in i.split("_")
                        if i != self.api_naming.version
                    ),
                    self.module,
                )
            )
        return ""

    @property
    def proto(self) -> str:
        """Return the proto selector for this type."""
        return ".".join(self.package + self.parent + (self.name,))

    @property
    def proto_package(self) -> str:
        """Return the proto package for this type."""
        return ".".join(self.package)

    @property
    def proto_package_versioned(self) -> str:
        """Return the versioned proto package for this type."""
        return ".".join(self.convert_to_versioned_package())

    def convert_to_versioned_package(self) -> Tuple[str, ...]:
        # We need to change the import statement to use an
        # underscore between the module and the version. For example,
        # change google.cloud.documentai.v1 to google.cloud.documentai_v1.
        # Check if the package name contains a version.
        version_regex = r"^v\d[^/]*$"
        regex_match = re.match(version_regex, self.package[-1])
        if regex_match and len(self.package) > 1:
            versioned_module = f"{self.package[-2]}_{regex_match[0]}"
            return self.package[:-2] + (versioned_module,)
        else:
            return self.package

    @cached_property
    def python_import(self) -> imp.Import:
        """Return the Python import for this type."""
        # If there is no naming object, then this is a special case for
        # Python types.
        #
        # FIXME: This does not attempt to do an isinstance check on PythonType
        # to avoid a circular dependency.
        # That part is fine, but a check for the absence of `api_naming` is
        # less than ideal; the condition works, but it is a weak correlation
        # that may not hold up over time.
        if not self.api_naming:
            return imp.Import(
                package=self.package,
                module=self.module,
                alias=self.module_alias,
            )

        # If this is part of the proto package that we are generating,
        # rewrite the package to our structure.
        if self.proto_package.startswith(self.api_naming.proto_package):
            return imp.Import(
                package=self.api_naming.module_namespace
                + (self.api_naming.versioned_module_name,)
                + self.subpackage
                + ("types",),
                module=self.module,
                alias=self.module_alias,
            )

        if self.is_proto_plus_type:
            return imp.Import(
                package=self.convert_to_versioned_package() + ("types",),
                module=self.module,
                alias=self.module_alias,
            )

        # Return the standard import.
        return imp.Import(
            package=self.package,
            module=f"{self.module}_pb2",
        )

    @property
    def sphinx(self) -> str:
        """Return the Sphinx identifier for this type."""

        if not self.api_naming:
            if self.package:
                return ".".join(self.package + (self.module, self.name))
            else:
                return str(self)

        # Check if this is a generated type
        # Use the original module name rather than the module_alias
        if self.proto_package.startswith(self.api_naming.proto_package):
            return ".".join(
                self.api_naming.module_namespace
                + (self.api_naming.versioned_module_name,)
                + self.subpackage
                + ("types",)
                + self.parent
                + (self.name,)
            )
        elif self.is_proto_plus_type:
            return ".".join(
                self.convert_to_versioned_package()
                + ("types",)
                + self.parent
                + (self.name,)
            )

        # Anything left is a standard _pb2 type
        return f"{self.proto_package}.{self.module}_pb2.{self.name}"

    @property
    def subpackage(self) -> Tuple[str, ...]:
        """Return the subpackage below the versioned module name, if any."""
        return tuple(self.package[len(self.api_naming.proto_package.split(".")) :])

    def child(self, child_name: str, path: Tuple[int, ...]) -> "Address":
        """Return a new child of the current Address.

        Args:
            child_name (str): The name of the child node.
                This address' name is appended to ``parent``.

        Returns:
            ~.Address: The new address object.
        """
        return dataclasses.replace(
            self,
            module_path=self.module_path + path,
            name=child_name,
            parent=self.parent + (self.name,) if self.name else self.parent,
        )

    def rel(self, address: "Address") -> str:
        """Return an identifier for this type, relative to the given address.

        Similar to :meth:`__str__`, but accepts an address (expected to be the
        module being written) and truncates the beginning module if the
        address matches the identifier's address. Templates can use this in
        situations where otherwise they would refer to themselves.

        Args:
            address (~.metadata.Address): The address to compare against.

        Returns:
            str: The appropriate identifier.
        """
        # Is this referencing a message in the same proto file?
        if self.package == address.package and self.module == address.module:
            # Edge case: If two (or more) messages are nested under a common
            # parent message, and one references another, then return that
            # enclosed in quotes.
            #
            # The reason for this is that each nested class creates a new
            # scope in Python, without reference to the parent class being
            # created, so there is no way for one nested class to reference
            # another at class instantiation time.
            if self.parent and address.parent and self.parent[0] == address.parent[0]:
                return f"'{'.'.join(self.parent)}.{self.name}'"

            # Edge case: Similar to above, if this is a message that is
            # referencing a nested message that it contains, we need
            # the message to be referenced relative to this message's
            # namespace.
            if self.parent and self.parent[0] == address.name:
                return ".".join(self.parent[1:] + (self.name,))

            # It is possible that a field references a message that has
            # not yet been declared. If so, send its name enclosed in quotes
            # (a string) instead.
            #
            # Note: this is a conservative construction; it generates a stringy
            # identifier all the time when it may be possible to use a regular
            # module lookup.
            # On the other hand, there's no reason _not_ to use a stringy
            # identifier. It is guaranteed to work all the time because
            # it bumps name resolution until a time when all types in a module
            # are guaranteed to be fully defined.
            return f"'{'.'.join(self.parent + (self.name,))}'"

        # Return the usual `module.Name`.
        return str(self)

    def resolve(self, selector: str) -> str:
        """Resolve a potentially-relative protobuf selector.

        This takes a protobuf selector which may be fully-qualified
        (e.g. `foo.bar.v1.Baz`) or may be relative (`Baz`) and
        returns the fully-qualified version.

        This method is naive and does not check to see if the message
        actually exists.

        Args:
            selector (str): A protobuf selector, either fully-qualified
                or relative.

        Returns:
            str: An absolute selector.
        """
        if "." not in selector:
            return f"{'.'.join(self.package)}.{selector}"
        return selector

    @cached_proto_context
    def with_context(self, *, collisions: Set[str]) -> "Address":
        """Return a derivative of this address with the provided context.

        This method is used to address naming collisions. The returned
        ``Address`` object aliases module names to avoid naming collisions in
        the file being written.
        """
        return (
            dataclasses.replace(self, collisions=collisions)
            if collisions and collisions != self.collisions
            else self
        )


@dataclasses.dataclass(frozen=True)
class Metadata:
    address: Address = dataclasses.field(default_factory=Address)
    documentation: descriptor_pb2.SourceCodeInfo.Location = dataclasses.field(
        default_factory=descriptor_pb2.SourceCodeInfo.Location,
    )

    @property
    def doc(self):
        """Return the best comment.

        This property prefers the leading comment if one is available,
        and falls back to a trailing comment or a detached comment otherwise.

        If there are no comments, return empty string. (This means a template
        is always guaranteed to get a string.)
        """
        if self.documentation.leading_comments:
            return self.documentation.leading_comments.strip()
        if self.documentation.trailing_comments:
            return self.documentation.trailing_comments.strip()
        if self.documentation.leading_detached_comments:
            return "\n\n".join(self.documentation.leading_detached_comments)
        return ""

    @cached_proto_context
    def with_context(self, *, collisions: Set[str]) -> "Metadata":
        """Return a derivative of this metadata with the provided context.

        This method is used to address naming collisions. The returned
        ``Address`` object aliases module names to avoid naming collisions in
        the file being written.
        """
        return (
            dataclasses.replace(
                self,
                address=self.address.with_context(collisions=collisions),
            )
            if collisions and collisions != self.address.collisions
            else self
        )


@dataclasses.dataclass(frozen=True)
class FieldIdentifier:
    ident: Address
    repeated: bool
    mapping: Optional[tuple] = None

    def __str__(self) -> str:
        if self.mapping:
            return f"MutableMapping[{self.mapping[0].ident}, {self.mapping[1].ident}]"
        if self.repeated:
            return f"MutableSequence[{self.ident}]"
        return str(self.ident)

    @property
    def sphinx(self) -> str:
        if self.mapping:
            return f"MutableMapping[{self.mapping[0].ident.sphinx}, {self.mapping[1].ident.sphinx}]"
        if self.repeated:
            return f"MutableSequence[{self.ident.sphinx}]"
        return self.ident.sphinx
