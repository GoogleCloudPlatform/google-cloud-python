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

import importlib
from unittest import mock

from google.protobuf import descriptor_pool, message, reflection, symbol_database

from proto._file_info import _FileInfo
from proto.marshal import Marshal, rules
from proto.utils import has_upb


def pytest_runtest_setup(item):
    _FileInfo.registry.clear()

    # Replace the descriptor pool and symbol database to avoid tests
    # polluting one another.
    pool = type(descriptor_pool.Default())()
    sym_db = symbol_database.SymbolDatabase(pool=pool)
    item._mocks = [
        mock.patch.object(descriptor_pool, "Default", return_value=pool),
        mock.patch.object(symbol_database, "Default", return_value=sym_db),
    ]
    if descriptor_pool._USE_C_DESCRIPTORS:
        item._mocks.append(
            mock.patch(
                (
                    "google._upb._message.default_pool"
                    if has_upb()
                    else "google.protobuf.pyext._message.default_pool"
                ),
                pool,
            )
        )

    [i.start() for i in item._mocks]

    # Importing a pb2 module registers those messages with the pool.
    # However, our test harness is subbing out the default pool above,
    # which means that all the dependencies that messages may depend on
    # are now absent from the pool.
    #
    # Add any pb2 modules that may have been imported by the test's module to
    # the descriptor pool and symbol database.
    #
    # This is exceptionally tricky in the C implementation because there is
    # no way to add an existing descriptor to a pool; the only acceptable
    # approach is to add a file descriptor proto, which then creates *new*
    # descriptors. We therefore do that and then plop the replacement classes
    # onto the pb2 modules.
    reloaded = set()
    for name in dir(item.module):
        if name.endswith("_pb2") and not name.startswith("test_"):
            module = getattr(item.module, name)

            # Exclude `google.protobuf.descriptor_pb2` which causes error
            # `RecursionError: maximum recursion depth exceeded while calling a Python object`
            # when running the test suite and is not required for tests.
            # See https://github.com/googleapis/proto-plus-python/issues/425
            if module.__package__ == "google.protobuf" and name == "descriptor_pb2":
                continue

            pool.AddSerializedFile(module.DESCRIPTOR.serialized_pb)
            fd = pool.FindFileByName(module.DESCRIPTOR.name)

            # Register all the messages to the symbol database and the
            # module. Do this recursively if there are nested messages.
            _register_messages(module, fd.message_types_by_name, sym_db)

            # Track which modules had new message classes loaded.
            # This is used below to wire the new classes into the marshal.
            reloaded.add(name)

    # If the marshal had previously registered the old message classes,
    # then reload the appropriate modules so the marshal is using the new ones.
    if "wrappers_pb2" in reloaded:
        importlib.reload(rules.wrappers)
    if "struct_pb2" in reloaded:
        importlib.reload(rules.struct)
    if reloaded.intersection({"timestamp_pb2", "duration_pb2"}):
        importlib.reload(rules.dates)


def pytest_runtest_teardown(item):
    Marshal._instances.clear()
    [i.stop() for i in item._mocks]


def _register_messages(scope, iterable, sym_db):
    """Create and register messages from the file descriptor."""
    for name, descriptor in iterable.items():
        new_msg = reflection.GeneratedProtocolMessageType(
            name,
            (message.Message,),
            {"DESCRIPTOR": descriptor, "__module__": None},
        )
        sym_db.RegisterMessage(new_msg)
        setattr(scope, name, new_msg)
        _register_messages(new_msg, descriptor.nested_types_by_name, sym_db)
