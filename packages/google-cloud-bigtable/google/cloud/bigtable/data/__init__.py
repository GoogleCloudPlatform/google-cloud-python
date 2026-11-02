# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
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
#
from google.cloud.bigtable import gapic_version as package_version
from google.cloud.bigtable.data._async._mutate_rows import _MutateRowsOperationAsync
from google.cloud.bigtable.data._async._read_rows import _ReadRowsOperationAsync
from google.cloud.bigtable.data._async.client import (
    AuthorizedViewAsync,
    BigtableDataClientAsync,
    MaterializedViewAsync,
    TableAsync,
)
from google.cloud.bigtable.data._async.mutations_batcher import MutationsBatcherAsync
from google.cloud.bigtable.data._cross_sync import CrossSync
from google.cloud.bigtable.data._helpers import (
    TABLE_DEFAULT,
    RowKeySamples,
    ShardedQuery,
)
from google.cloud.bigtable.data._sync_autogen._mutate_rows import _MutateRowsOperation
from google.cloud.bigtable.data._sync_autogen._read_rows import _ReadRowsOperation
from google.cloud.bigtable.data._sync_autogen.client import (
    AuthorizedView,
    BigtableDataClient,
    MaterializedView,
    Table,
)
from google.cloud.bigtable.data._sync_autogen.mutations_batcher import MutationsBatcher
from google.cloud.bigtable.data.exceptions import (
    FailedMutationEntryError,
    FailedQueryShardError,
    InvalidChunk,
    MutationsExceptionGroup,
    ParameterTypeInferenceFailed,
    RetryExceptionGroup,
    ShardedReadRowsExceptionGroup,
)
from google.cloud.bigtable.data.mutations import (
    AddToCell,
    DeleteAllFromFamily,
    DeleteAllFromRow,
    DeleteRangeFromColumn,
    Mutation,
    RowMutationEntry,
    SetCell,
)
from google.cloud.bigtable.data.read_rows_query import ReadRowsQuery, RowRange
from google.cloud.bigtable.data.row import Cell, Row

# setup custom CrossSync mappings for library
from google.cloud.bigtable_v2.services.bigtable.async_client import (
    BigtableAsyncClient,
)
from google.cloud.bigtable_v2.services.bigtable.client import (
    BigtableClient,
)

CrossSync.add_mapping("GapicClient", BigtableAsyncClient)
CrossSync._Sync_Impl.add_mapping("GapicClient", BigtableClient)
CrossSync.add_mapping("_ReadRowsOperation", _ReadRowsOperationAsync)
CrossSync._Sync_Impl.add_mapping("_ReadRowsOperation", _ReadRowsOperation)
CrossSync.add_mapping("_MutateRowsOperation", _MutateRowsOperationAsync)
CrossSync._Sync_Impl.add_mapping("_MutateRowsOperation", _MutateRowsOperation)
CrossSync.add_mapping("MutationsBatcher", MutationsBatcherAsync)
CrossSync._Sync_Impl.add_mapping("MutationsBatcher", MutationsBatcher)

__version__: str = package_version.__version__

__all__ = (
    "BigtableDataClientAsync",
    "TableAsync",
    "AuthorizedViewAsync",
    "MaterializedViewAsync",
    "MutationsBatcherAsync",
    "BigtableDataClient",
    "Table",
    "AuthorizedView",
    "MaterializedView",
    "MutationsBatcher",
    "RowKeySamples",
    "ReadRowsQuery",
    "RowRange",
    "Mutation",
    "RowMutationEntry",
    "AddToCell",
    "SetCell",
    "DeleteRangeFromColumn",
    "DeleteAllFromFamily",
    "DeleteAllFromRow",
    "Row",
    "Cell",
    "InvalidChunk",
    "FailedMutationEntryError",
    "FailedQueryShardError",
    "RetryExceptionGroup",
    "MutationsExceptionGroup",
    "ShardedReadRowsExceptionGroup",
    "ParameterTypeInferenceFailed",
    "ShardedQuery",
    "TABLE_DEFAULT",
)
