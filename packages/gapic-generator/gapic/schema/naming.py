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

import abc
import dataclasses
import os
import re
from typing import cast, List, Match, Tuple

from google.protobuf import descriptor_pb2

from gapic import utils
from gapic.utils import Options

# See https://github.com/python/mypy/issues/5374 for details on the mypy false
# positive.


@dataclasses.dataclass(frozen=True)  # type: ignore
class Naming(abc.ABC):
    """Naming data for an API.

    This class contains the naming nomenclature used for this API
    within templates.

    A concrete child of this object is made available to every template
    (as ``api.naming``).
    """

    name: str = ""
    namespace: Tuple[str, ...] = dataclasses.field(default_factory=tuple)
    version: str = ""
    product_name: str = ""
    proto_package: str = ""
    _warehouse_package_name: str = ""
    proto_plus_deps: Tuple[str, ...] = dataclasses.field(default_factory=tuple)

    def __post_init__(self):
        if not self.product_name:
            self.__dict__["product_name"] = self.name

    @staticmethod
    def build(
        *file_descriptors: descriptor_pb2.FileDescriptorProto,
        opts: Options = Options(),
    ) -> "Naming":
        """Return a full Naming instance based on these file descriptors.

        This is pieced together from the proto package names as well as the
        ``google.api.metadata`` file annotation. This information may be
        present in one or many files; this method is tolerant as long as
        the data does not conflict.

        Args:
            file_descriptors (Iterable[~.FileDescriptorProto]): A list of
                file descriptor protos. This list should only include the
                files actually targeted for output (not their imports).

        Returns:
            ~.Naming: A :class:`~.Naming` instance which is provided to
                templates as part of the :class:`~.API`.

        Raises:
            ValueError: If the provided file descriptors contain contradictory
                information.
        """
        # Determine the set of proto packages.
        proto_packages = {fd.package for fd in file_descriptors}
        root_package = os.path.commonprefix(tuple(proto_packages)).rstrip(".")

        # Quick check: If there is no common ground in the package,
        # we are obviously in trouble.
        if not root_package:
            raise ValueError(
                "The protos provided do not share a common root package. "
                "Ensure that all explicitly-specified protos are for a "
                "single API. "
                f"The packages we got are: {', '.join(proto_packages)}"
            )

        # Define the valid regex to split the package.
        #
        # It is not necessary for the regex to be as particular about package
        # name validity (e.g. avoiding .. or segments starting with numbers)
        # because protoc is guaranteed to give us valid package names.
        pattern = r"^((?P<namespace>[a-z0-9_.]+)\.)?(?P<name>[a-z0-9_]+)"

        # Only require the version portion of the regex if the version is
        # present.
        #
        # This code may look counter-intuitive (why not use ? to make it
        # optional), but the engine's greediness routine will decide that
        # the version is the name, which is not what we want.
        version = r"\.(?P<version>v[0-9]+(p[0-9]+)?((alpha|beta)[0-9]*)?)"
        if re.search(version, root_package):
            pattern += version

        # Okay, do the match
        match = cast(Match, re.search(pattern=pattern, string=root_package)).groupdict()
        match["namespace"] = match["namespace"] or ""
        klass = OldNaming if opts.old_naming else NewNaming
        package_info = klass(
            name=match["name"].capitalize(),
            namespace=tuple(i.capitalize() for i in match["namespace"].split(".") if i),
            product_name=match["name"].capitalize(),
            proto_package=root_package,
            version=match.get("version", ""),
        )

        # Quick check: Ensure that the package directives all inferred
        # the same information.
        if not package_info.version and len(proto_packages) > 1:
            raise ValueError(
                "All protos must have the same proto package "
                "up to and including the version."
            )

        # If a naming information was provided on the CLI, override the naming
        # value.
        #
        # We are liberal about what formats we take on the CLI; it will
        # likely make sense to many users to use dot-separated namespaces and
        # snake case, so handle that and do the right thing.
        if opts.name:
            package_info = dataclasses.replace(
                package_info,
                name=" ".join(
                    (i.capitalize() for i in opts.name.replace("_", " ").split(" "))
                ),
            )
        if opts.namespace:
            package_info = dataclasses.replace(
                package_info,
                namespace=tuple(
                    # The join-and-split on "." here causes us to expand out
                    # dot notation that we may have been sent; e.g. a one-tuple
                    # with ('x.y',) will become a two-tuple: ('x', 'y')
                    i.capitalize()
                    for i in ".".join(opts.namespace).split(".")
                ),
            )
        if opts.warehouse_package_name:
            package_info = dataclasses.replace(
                package_info, _warehouse_package_name=opts.warehouse_package_name
            )
        if opts.proto_plus_deps:
            package_info = dataclasses.replace(
                package_info,
                proto_plus_deps=opts.proto_plus_deps,
            )

        # Done; return the naming information.
        return package_info

    def __bool__(self):
        """Return True if any of the fields are truthy, False otherwise."""
        return any(
            (getattr(self, i.name) for i in dataclasses.fields(self)),
        )

    @property
    def long_name(self) -> str:
        """Return an appropriate title-cased long name."""
        return " ".join(tuple(self.namespace) + (self.name,))

    @property
    def module_name(self) -> str:
        """Return the appropriate Python module name."""
        return utils.to_valid_module_name(self.name)

    @property
    def module_namespace(self) -> Tuple[str, ...]:
        """Return the appropriate Python module namespace as a tuple."""
        return tuple(utils.to_valid_module_name(i) for i in self.namespace)

    @property
    def namespace_packages(self) -> Tuple[str, ...]:
        """Return the appropriate Python namespace packages."""
        answer: List[str] = []
        for cursor in (i.lower() for i in self.namespace):
            answer.append(f"{answer[-1]}.{cursor}" if answer else cursor)
        return tuple(answer)

    @property
    @abc.abstractmethod
    def versioned_module_name(self) -> str:
        """Return the versiond module name (e.g. ``apiname_v1``).

        If there is no version, this is the same as ``module_name``.
        """
        raise NotImplementedError

    @property
    def warehouse_package_name(self) -> str:
        """Return the appropriate Python package name for Warehouse."""
        # If a custom name has been set, use it
        if self._warehouse_package_name:
            return self._warehouse_package_name
        # Otherwise piece the name and namespace together to come
        # up with the proper package name.
        answer = list(self.namespace) + self.name.split(" ")
        return "-".join(answer).lower()


class NewNaming(Naming):
    @property
    def versioned_module_name(self) -> str:
        """Return the versiond module name (e.g. ``apiname_v1``).

        If there is no version, this is the same as ``module_name``.
        """
        return self.module_name + (f"_{self.version}" if self.version else "")


class OldNaming(Naming):
    @property
    def versioned_module_name(self) -> str:
        """Return the versiond module name (e.g. ``apiname_v1``).

        If there is no version, this is the same as ``module_name``.
        """
        return self.module_name + (f".{self.version}" if self.version else "")
