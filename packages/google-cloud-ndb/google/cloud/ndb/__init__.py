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

"""``ndb`` is a library for Google Cloud Firestore in Datastore Mode and Google Cloud Datastore.

It was originally included in the Google App Engine runtime as a "new"
version of the ``db`` API (hence ``ndb``).

.. autodata:: __version__
.. autodata:: __all__
"""

import google.api_core as api_core

from google.cloud.ndb import version

__version__: str = version.__version__

from google.cloud.ndb._datastore_api import EVENTUAL, EVENTUAL_CONSISTENCY, STRONG
from google.cloud.ndb._datastore_query import Cursor, QueryIterator
from google.cloud.ndb._transaction import (
    in_transaction,
    non_transactional,
    transaction,
    transaction_async,
    transactional,
    transactional_async,
    transactional_tasklet,
)
from google.cloud.ndb.client import Client
from google.cloud.ndb.context import (
    AutoBatcher,
    Context,
    ContextOptions,
    TransactionOptions,
    get_context,
    get_toplevel_context,
)
from google.cloud.ndb.global_cache import GlobalCache, MemcacheCache, RedisCache
from google.cloud.ndb.key import Key
from google.cloud.ndb.model import (
    BadProjectionError,
    BlobKey,
    BlobKeyProperty,
    BlobProperty,
    BooleanProperty,
    ComputedProperty,
    ComputedPropertyError,
    DateProperty,
    DateTimeProperty,
    Expando,
    FloatProperty,
    GenericProperty,
    GeoPt,
    GeoPtProperty,
    Index,
    IndexProperty,
    IndexState,
    IntegerProperty,
    InvalidPropertyError,
    JsonProperty,
    KeyProperty,
    KindError,
    LocalStructuredProperty,
    MetaModel,
    Model,
    ModelAdapter,
    ModelAttribute,
    ModelKey,
    PickleProperty,
    Property,
    ReadonlyPropertyError,
    Rollback,
    StringProperty,
    StructuredProperty,
    TextProperty,
    TimeProperty,
    UnprojectedPropertyError,
    User,
    UserNotFoundError,
    UserProperty,
    delete_multi,
    delete_multi_async,
    get_indexes,
    get_indexes_async,
    get_multi,
    get_multi_async,
    make_connection,
    put_multi,
    put_multi_async,
)
from google.cloud.ndb.polymodel import PolyModel
from google.cloud.ndb.query import (
    AND,
    OR,
    ConjunctionNode,
    DisjunctionNode,
    FalseNode,
    FilterNode,
    Node,
    Parameter,
    ParameterizedFunction,
    ParameterizedThing,
    ParameterNode,
    PostFilterNode,
    Query,
    QueryOptions,
    RepeatedStructuredPropertyPredicate,
    gql,
)
from google.cloud.ndb.tasklets import (
    Future,
    QueueFuture,
    ReducingFuture,
    Return,
    SerialQueueFuture,
    add_flow_exception,
    make_context,
    make_default_context,
    set_context,
    sleep,
    synctasklet,
    tasklet,
    toplevel,
    wait_all,
    wait_any,
)

api_core.check_python_version(__name__)
api_core.check_dependency_versions(__name__)

__all__ = [
    "__version__",
    "AutoBatcher",
    "Client",
    "Context",
    "ContextOptions",
    "EVENTUAL",
    "EVENTUAL_CONSISTENCY",
    "STRONG",
    "TransactionOptions",
    "Key",
    "BlobKey",
    "BlobKeyProperty",
    "BlobProperty",
    "BooleanProperty",
    "ComputedProperty",
    "ComputedPropertyError",
    "DateProperty",
    "DateTimeProperty",
    "delete_multi",
    "delete_multi_async",
    "Expando",
    "FloatProperty",
    "GenericProperty",
    "GeoPt",
    "GeoPtProperty",
    "get_indexes",
    "get_indexes_async",
    "get_multi",
    "get_multi_async",
    "GlobalCache",
    "in_transaction",
    "Index",
    "IndexProperty",
    "IndexState",
    "IntegerProperty",
    "InvalidPropertyError",
    "BadProjectionError",
    "JsonProperty",
    "KeyProperty",
    "KindError",
    "LocalStructuredProperty",
    "make_connection",
    "MemcacheCache",
    "MetaModel",
    "Model",
    "ModelAdapter",
    "ModelAttribute",
    "ModelKey",
    "non_transactional",
    "PickleProperty",
    "PolyModel",
    "Property",
    "put_multi",
    "put_multi_async",
    "ReadonlyPropertyError",
    "RedisCache",
    "Rollback",
    "StringProperty",
    "StructuredProperty",
    "TextProperty",
    "TimeProperty",
    "transaction",
    "transaction_async",
    "transactional",
    "transactional_async",
    "transactional_tasklet",
    "UnprojectedPropertyError",
    "User",
    "UserNotFoundError",
    "UserProperty",
    "ConjunctionNode",
    "AND",
    "Cursor",
    "DisjunctionNode",
    "OR",
    "FalseNode",
    "FilterNode",
    "gql",
    "Node",
    "Parameter",
    "ParameterizedFunction",
    "ParameterizedThing",
    "ParameterNode",
    "PostFilterNode",
    "Query",
    "QueryIterator",
    "QueryOptions",
    "RepeatedStructuredPropertyPredicate",
    "add_flow_exception",
    "Future",
    "get_context",
    "get_toplevel_context",
    "make_context",
    "make_default_context",
    "QueueFuture",
    "ReducingFuture",
    "Return",
    "SerialQueueFuture",
    "set_context",
    "sleep",
    "synctasklet",
    "tasklet",
    "toplevel",
    "wait_all",
    "wait_any",
]
