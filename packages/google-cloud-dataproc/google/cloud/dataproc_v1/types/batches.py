# -*- coding: utf-8 -*-
# Copyright 2026 Google LLC
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
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.dataproc_v1.types import shared

__protobuf__ = proto.module(
    package="google.cloud.dataproc.v1",
    manifest={
        "CreateBatchRequest",
        "GetBatchRequest",
        "ListBatchesRequest",
        "ListBatchesResponse",
        "DeleteBatchRequest",
        "Batch",
        "PySparkBatch",
        "SparkBatch",
        "SparkRBatch",
        "SparkSqlBatch",
        "PySparkNotebookBatch",
    },
)


class CreateBatchRequest(proto.Message):
    r"""A request to create a batch workload.

    Attributes:
        parent (str):
            Required. The parent resource where this
            batch will be created.
        batch (google.cloud.dataproc_v1.types.Batch):
            Required. The batch to create.
        batch_id (str):
            Optional. The ID to use for the batch, which will become the
            final component of the batch's resource name.

            This value must be 4-63 characters. Valid characters are
            ``/[a-z][0-9]-/``.
        request_id (str):
            Optional. A unique ID used to identify the request. If the
            service receives two ``CreateBatchRequests`` with the same
            ``request_id``, the second request is ignored and the
            operation that corresponds to the first Batch created and
            stored in the backend is returned.

            Recommendation: Set this value to a
            `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier>`__.

            The value must contain only letters (a-z, A-Z), numbers
            (0-9), underscores (\_), and hyphens (-). The maximum length
            is 40 characters.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    batch: "Batch" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Batch",
    )
    batch_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class GetBatchRequest(proto.Message):
    r"""A request to get the resource representation for a batch
    workload.

    Attributes:
        name (str):
            Required. The fully qualified name of the batch to retrieve
            in the format
            "projects/PROJECT_ID/locations/DATAPROC_REGION/batches/BATCH_ID".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListBatchesRequest(proto.Message):
    r"""A request to list batch workloads in a project.

    Attributes:
        parent (str):
            Required. The parent, which owns this
            collection of batches.
        page_size (int):
            Optional. The maximum number of batches to
            return in each response. The service may return
            fewer than this value. The default page size is
            20; the maximum page size is 1000.
        page_token (str):
            Optional. A page token received from a previous
            ``ListBatches`` call. Provide this token to retrieve the
            subsequent page.
        filter (str):
            Optional. A filter for the batches to return in the
            response.

            A filter is a logical expression constraining the values of
            various fields in each batch resource. Filters are case
            sensitive, and may contain multiple clauses combined with
            logical operators (AND/OR). Supported fields are
            ``batch_id``, ``batch_uuid``, ``state``, ``create_time``,
            and ``labels``.

            e.g.
            ``state = RUNNING and create_time < "2023-01-01T00:00:00Z"``
            filters for batches in state RUNNING that were created
            before 2023-01-01.
            ``state = RUNNING and labels.environment=production``
            filters for batches in state in a RUNNING state that have a
            production environment label.

            See https://google.aip.dev/assets/misc/ebnf-filtering.txt
            for a detailed description of the filter syntax and a list
            of supported comparisons.
        order_by (str):
            Optional. Field(s) on which to sort the list of batches.

            Currently the only supported sort orders are unspecified
            (empty) and ``create_time desc`` to sort by most recently
            created batches first.

            See https://google.aip.dev/132#ordering for more details.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListBatchesResponse(proto.Message):
    r"""A list of batch workloads.

    Attributes:
        batches (MutableSequence[google.cloud.dataproc_v1.types.Batch]):
            Output only. The batches from the specified
            collection.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Output only. List of Batches that could not
            be included in the response. Attempting to get
            one of these resources may indicate why it was
            not included in the list response.
    """

    @property
    def raw_page(self):
        return self

    batches: MutableSequence["Batch"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Batch",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class DeleteBatchRequest(proto.Message):
    r"""A request to delete a batch workload.

    Attributes:
        name (str):
            Required. The fully qualified name of the batch to retrieve
            in the format
            "projects/PROJECT_ID/locations/DATAPROC_REGION/batches/BATCH_ID".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Batch(proto.Message):
    r"""A representation of a batch workload in the service.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. The resource name of the batch.
        uuid (str):
            Output only. A batch UUID (Unique Universal
            Identifier). The service generates this value
            when it creates the batch.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the batch was
            created.
        pyspark_batch (google.cloud.dataproc_v1.types.PySparkBatch):
            Optional. PySpark batch config.

            This field is a member of `oneof`_ ``batch_config``.
        spark_batch (google.cloud.dataproc_v1.types.SparkBatch):
            Optional. Spark batch config.

            This field is a member of `oneof`_ ``batch_config``.
        spark_r_batch (google.cloud.dataproc_v1.types.SparkRBatch):
            Optional. SparkR batch config.

            This field is a member of `oneof`_ ``batch_config``.
        spark_sql_batch (google.cloud.dataproc_v1.types.SparkSqlBatch):
            Optional. SparkSql batch config.

            This field is a member of `oneof`_ ``batch_config``.
        pyspark_notebook_batch (google.cloud.dataproc_v1.types.PySparkNotebookBatch):
            Optional. PySpark notebook batch config.

            This field is a member of `oneof`_ ``batch_config``.
        runtime_info (google.cloud.dataproc_v1.types.RuntimeInfo):
            Output only. Runtime information about batch
            execution.
        state (google.cloud.dataproc_v1.types.Batch.State):
            Output only. The state of the batch.
        state_message (str):
            Output only. Batch state details, such as a failure
            description if the state is ``FAILED``.
        state_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the batch entered
            a current state.
        creator (str):
            Output only. The email address of the user
            who created the batch.
        labels (MutableMapping[str, str]):
            Optional. The labels to associate with this batch. Label
            **keys** must contain 1 to 63 characters, and must conform
            to `RFC 1035 <https://www.ietf.org/rfc/rfc1035.txt>`__.
            Label **values** may be empty, but, if present, must contain
            1 to 63 characters, and must conform to `RFC
            1035 <https://www.ietf.org/rfc/rfc1035.txt>`__. No more than
            32 labels can be associated with a batch.
        runtime_config (google.cloud.dataproc_v1.types.RuntimeConfig):
            Optional. Runtime configuration for the batch
            execution.
        environment_config (google.cloud.dataproc_v1.types.EnvironmentConfig):
            Optional. Environment configuration for the
            batch execution.
        operation (str):
            Output only. The resource name of the
            operation associated with this batch.
        state_history (MutableSequence[google.cloud.dataproc_v1.types.Batch.StateHistory]):
            Output only. Historical state information for
            the batch.
    """

    class State(proto.Enum):
        r"""The batch state.

        Values:
            STATE_UNSPECIFIED (0):
                The batch state is unknown.
            PENDING (1):
                The batch is created before running.
            RUNNING (2):
                The batch is running.
            CANCELLING (3):
                The batch is cancelling.
            CANCELLED (4):
                The batch cancellation was successful.
            SUCCEEDED (5):
                The batch completed successfully.
            FAILED (6):
                The batch is no longer running due to an
                error.
        """

        STATE_UNSPECIFIED = 0
        PENDING = 1
        RUNNING = 2
        CANCELLING = 3
        CANCELLED = 4
        SUCCEEDED = 5
        FAILED = 6

    class StateHistory(proto.Message):
        r"""Historical state information.

        Attributes:
            state (google.cloud.dataproc_v1.types.Batch.State):
                Output only. The state of the batch at this
                point in history.
            state_message (str):
                Output only. Details about the state at this
                point in history.
            state_start_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. The time when the batch entered
                the historical state.
        """

        state: "Batch.State" = proto.Field(
            proto.ENUM,
            number=1,
            enum="Batch.State",
        )
        state_message: str = proto.Field(
            proto.STRING,
            number=2,
        )
        state_start_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=3,
            message=timestamp_pb2.Timestamp,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uuid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    pyspark_batch: "PySparkBatch" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="batch_config",
        message="PySparkBatch",
    )
    spark_batch: "SparkBatch" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="batch_config",
        message="SparkBatch",
    )
    spark_r_batch: "SparkRBatch" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="batch_config",
        message="SparkRBatch",
    )
    spark_sql_batch: "SparkSqlBatch" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="batch_config",
        message="SparkSqlBatch",
    )
    pyspark_notebook_batch: "PySparkNotebookBatch" = proto.Field(
        proto.MESSAGE,
        number=19,
        oneof="batch_config",
        message="PySparkNotebookBatch",
    )
    runtime_info: shared.RuntimeInfo = proto.Field(
        proto.MESSAGE,
        number=8,
        message=shared.RuntimeInfo,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=9,
        enum=State,
    )
    state_message: str = proto.Field(
        proto.STRING,
        number=10,
    )
    state_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )
    creator: str = proto.Field(
        proto.STRING,
        number=12,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=13,
    )
    runtime_config: shared.RuntimeConfig = proto.Field(
        proto.MESSAGE,
        number=14,
        message=shared.RuntimeConfig,
    )
    environment_config: shared.EnvironmentConfig = proto.Field(
        proto.MESSAGE,
        number=15,
        message=shared.EnvironmentConfig,
    )
    operation: str = proto.Field(
        proto.STRING,
        number=16,
    )
    state_history: MutableSequence[StateHistory] = proto.RepeatedField(
        proto.MESSAGE,
        number=17,
        message=StateHistory,
    )


class PySparkBatch(proto.Message):
    r"""A configuration for running an `Apache
    PySpark <https://spark.apache.org/docs/latest/api/python/getting_started/quickstart.html>`__
    batch workload.

    Attributes:
        main_python_file_uri (str):
            Required. The HCFS URI of the main Python
            file to use as the Spark driver. Must be a .py
            file.
        args (MutableSequence[str]):
            Optional. The arguments to pass to the driver. Do not
            include arguments that can be set as batch properties, such
            as ``--conf``, since a collision can occur that causes an
            incorrect batch submission.
        python_file_uris (MutableSequence[str]):
            Optional. HCFS file URIs of Python files to pass to the
            PySpark framework. Supported file types: ``.py``, ``.egg``,
            and ``.zip``.
        jar_file_uris (MutableSequence[str]):
            Optional. HCFS URIs of jar files to add to
            the classpath of the Spark driver and tasks.
        file_uris (MutableSequence[str]):
            Optional. HCFS URIs of files to be placed in
            the working directory of each executor.
        archive_uris (MutableSequence[str]):
            Optional. HCFS URIs of archives to be extracted into the
            working directory of each executor. Supported file types:
            ``.jar``, ``.tar``, ``.tar.gz``, ``.tgz``, and ``.zip``.
    """

    main_python_file_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    args: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    python_file_uris: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    jar_file_uris: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    file_uris: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    archive_uris: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )


class SparkBatch(proto.Message):
    r"""A configuration for running an `Apache
    Spark <https://spark.apache.org/>`__ batch workload.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        main_jar_file_uri (str):
            Optional. The HCFS URI of the jar file that
            contains the main class.

            This field is a member of `oneof`_ ``driver``.
        main_class (str):
            Optional. The name of the driver main class. The jar file
            that contains the class must be in the classpath or
            specified in ``jar_file_uris``.

            This field is a member of `oneof`_ ``driver``.
        args (MutableSequence[str]):
            Optional. The arguments to pass to the driver. Do not
            include arguments that can be set as batch properties, such
            as ``--conf``, since a collision can occur that causes an
            incorrect batch submission.
        jar_file_uris (MutableSequence[str]):
            Optional. HCFS URIs of jar files to add to
            the classpath of the Spark driver and tasks.
        file_uris (MutableSequence[str]):
            Optional. HCFS URIs of files to be placed in
            the working directory of each executor.
        archive_uris (MutableSequence[str]):
            Optional. HCFS URIs of archives to be extracted into the
            working directory of each executor. Supported file types:
            ``.jar``, ``.tar``, ``.tar.gz``, ``.tgz``, and ``.zip``.
    """

    main_jar_file_uri: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="driver",
    )
    main_class: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="driver",
    )
    args: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    jar_file_uris: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    file_uris: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    archive_uris: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )


class SparkRBatch(proto.Message):
    r"""A configuration for running an `Apache
    SparkR <https://spark.apache.org/docs/latest/sparkr.html>`__ batch
    workload.

    Attributes:
        main_r_file_uri (str):
            Required. The HCFS URI of the main R file to use as the
            driver. Must be a ``.R`` or ``.r`` file.
        args (MutableSequence[str]):
            Optional. The arguments to pass to the Spark driver. Do not
            include arguments that can be set as batch properties, such
            as ``--conf``, since a collision can occur that causes an
            incorrect batch submission.
        file_uris (MutableSequence[str]):
            Optional. HCFS URIs of files to be placed in
            the working directory of each executor.
        archive_uris (MutableSequence[str]):
            Optional. HCFS URIs of archives to be extracted into the
            working directory of each executor. Supported file types:
            ``.jar``, ``.tar``, ``.tar.gz``, ``.tgz``, and ``.zip``.
    """

    main_r_file_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    args: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    file_uris: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    archive_uris: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )


class SparkSqlBatch(proto.Message):
    r"""A configuration for running `Apache Spark
    SQL <https://spark.apache.org/sql/>`__ queries as a batch workload.

    Attributes:
        query_file_uri (str):
            Required. The HCFS URI of the script that
            contains Spark SQL queries to execute.
        query_variables (MutableMapping[str, str]):
            Optional. Mapping of query variable names to values
            (equivalent to the Spark SQL command:
            ``SET name="value";``).
        jar_file_uris (MutableSequence[str]):
            Optional. HCFS URIs of jar files to be added
            to the Spark CLASSPATH.
    """

    query_file_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    query_variables: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )
    jar_file_uris: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class PySparkNotebookBatch(proto.Message):
    r"""A configuration for running a PySpark Notebook batch
    workload.

    Attributes:
        notebook_file_uri (str):
            Required. The HCFS URI of the notebook file
            to execute.
        params (MutableMapping[str, str]):
            Optional. The parameters to pass to the
            notebook.
        python_file_uris (MutableSequence[str]):
            Optional. HCFS URIs of Python files to pass
            to the PySpark framework.
        jar_file_uris (MutableSequence[str]):
            Optional. HCFS URIs of jar files to be added
            to the Spark CLASSPATH.
        file_uris (MutableSequence[str]):
            Optional. HCFS URIs of files to be placed in
            the working directory of each executor
        archive_uris (MutableSequence[str]):
            Optional. HCFS URIs of archives to be extracted into the
            working directory of each executor. Supported file types:
            ``.jar``, ``.tar``, ``.tar.gz``, ``.tgz``, and ``.zip``.
    """

    notebook_file_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    params: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )
    python_file_uris: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    jar_file_uris: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    file_uris: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    archive_uris: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
