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

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.dataproc.v1",
    manifest={
        "LoggingConfig",
        "HadoopJob",
        "SparkJob",
        "PySparkJob",
        "QueryList",
        "HiveJob",
        "SparkSqlJob",
        "PigJob",
        "SparkRJob",
        "PrestoJob",
        "TrinoJob",
        "FlinkJob",
        "JobPlacement",
        "JobStatus",
        "JobReference",
        "YarnApplication",
        "Job",
        "DriverSchedulingConfig",
        "JobScheduling",
        "SubmitJobRequest",
        "JobMetadata",
        "GetJobRequest",
        "ListJobsRequest",
        "UpdateJobRequest",
        "ListJobsResponse",
        "CancelJobRequest",
        "DeleteJobRequest",
    },
)


class LoggingConfig(proto.Message):
    r"""The runtime logging config of the job.

    Attributes:
        driver_log_levels (MutableMapping[str, google.cloud.dataproc_v1.types.LoggingConfig.Level]):
            The per-package log levels for the driver.
            This can include "root" package name to
            configure rootLogger. Examples:

            - 'com.google = FATAL'
            - 'root = INFO'
            - 'org.apache = DEBUG'
    """

    class Level(proto.Enum):
        r"""The Log4j level for job execution. When running an `Apache
        Hive <https://hive.apache.org/>`__ job, Cloud Dataproc configures
        the Hive client to an equivalent verbosity level.

        Values:
            LEVEL_UNSPECIFIED (0):
                Level is unspecified. Use default level for
                log4j.
            ALL (1):
                Use ALL level for log4j.
            TRACE (2):
                Use TRACE level for log4j.
            DEBUG (3):
                Use DEBUG level for log4j.
            INFO (4):
                Use INFO level for log4j.
            WARN (5):
                Use WARN level for log4j.
            ERROR (6):
                Use ERROR level for log4j.
            FATAL (7):
                Use FATAL level for log4j.
            OFF (8):
                Turn off log4j.
        """

        LEVEL_UNSPECIFIED = 0
        ALL = 1
        TRACE = 2
        DEBUG = 3
        INFO = 4
        WARN = 5
        ERROR = 6
        FATAL = 7
        OFF = 8

    driver_log_levels: MutableMapping[str, Level] = proto.MapField(
        proto.STRING,
        proto.ENUM,
        number=2,
        enum=Level,
    )


class HadoopJob(proto.Message):
    r"""A Dataproc job for running `Apache Hadoop
    MapReduce <https://hadoop.apache.org/docs/current/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html>`__
    jobs on `Apache Hadoop
    YARN <https://hadoop.apache.org/docs/r2.7.1/hadoop-yarn/hadoop-yarn-site/YARN.html>`__.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        main_jar_file_uri (str):
            The HCFS URI of the jar file containing the
            main class. Examples:

            'gs://foo-bucket/analytics-binaries/extract-useful-metrics-mr.jar'
            'hdfs:/tmp/test-samples/custom-wordcount.jar'
            'file:///home/usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar'

            This field is a member of `oneof`_ ``driver``.
        main_class (str):
            The name of the driver's main class. The jar file containing
            the class must be in the default CLASSPATH or specified in
            ``jar_file_uris``.

            This field is a member of `oneof`_ ``driver``.
        args (MutableSequence[str]):
            Optional. The arguments to pass to the driver. Do not
            include arguments, such as ``-libjars`` or ``-Dfoo=bar``,
            that can be set as job properties, since a collision might
            occur that causes an incorrect job submission.
        jar_file_uris (MutableSequence[str]):
            Optional. Jar file URIs to add to the
            CLASSPATHs of the Hadoop driver and tasks.
        file_uris (MutableSequence[str]):
            Optional. HCFS (Hadoop Compatible Filesystem)
            URIs of files to be copied to the working
            directory of Hadoop drivers and distributed
            tasks. Useful for naively parallel tasks.
        archive_uris (MutableSequence[str]):
            Optional. HCFS URIs of archives to be
            extracted in the working directory of Hadoop
            drivers and tasks. Supported file types:

            .jar, .tar, .tar.gz, .tgz, or .zip.
        properties (MutableMapping[str, str]):
            Optional. A mapping of property names to values, used to
            configure Hadoop. Properties that conflict with values set
            by the Dataproc API might be overwritten. Can include
            properties set in ``/etc/hadoop/conf/*-site`` and classes in
            user code.
        logging_config (google.cloud.dataproc_v1.types.LoggingConfig):
            Optional. The runtime log config for job
            execution.
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
    properties: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    logging_config: "LoggingConfig" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="LoggingConfig",
    )


class SparkJob(proto.Message):
    r"""A Dataproc job for running `Apache
    Spark <https://spark.apache.org/>`__ applications on YARN.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        main_jar_file_uri (str):
            The HCFS URI of the jar file that contains
            the main class.

            This field is a member of `oneof`_ ``driver``.
        main_class (str):
            The name of the driver's main class. The jar file that
            contains the class must be in the default CLASSPATH or
            specified in SparkJob.jar_file_uris.

            This field is a member of `oneof`_ ``driver``.
        args (MutableSequence[str]):
            Optional. The arguments to pass to the driver. Do not
            include arguments, such as ``--conf``, that can be set as
            job properties, since a collision may occur that causes an
            incorrect job submission.
        jar_file_uris (MutableSequence[str]):
            Optional. HCFS URIs of jar files to add to
            the CLASSPATHs of the Spark driver and tasks.
        file_uris (MutableSequence[str]):
            Optional. HCFS URIs of files to be placed in
            the working directory of each executor. Useful
            for naively parallel tasks.
        archive_uris (MutableSequence[str]):
            Optional. HCFS URIs of archives to be
            extracted into the working directory of each
            executor. Supported file types:

            .jar, .tar, .tar.gz, .tgz, and .zip.
        properties (MutableMapping[str, str]):
            Optional. A mapping of property names to
            values, used to configure Spark. Properties that
            conflict with values set by the Dataproc API
            might be overwritten. Can include properties set
            in
            /etc/spark/conf/spark-defaults.conf and classes
            in user code.
        logging_config (google.cloud.dataproc_v1.types.LoggingConfig):
            Optional. The runtime log config for job
            execution.
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
    properties: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    logging_config: "LoggingConfig" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="LoggingConfig",
    )


class PySparkJob(proto.Message):
    r"""A Dataproc job for running `Apache
    PySpark <https://spark.apache.org/docs/0.9.0/python-programming-guide.html>`__
    applications on YARN.

    Attributes:
        main_python_file_uri (str):
            Required. The HCFS URI of the main Python
            file to use as the driver. Must be a .py file.
        args (MutableSequence[str]):
            Optional. The arguments to pass to the driver. Do not
            include arguments, such as ``--conf``, that can be set as
            job properties, since a collision may occur that causes an
            incorrect job submission.
        python_file_uris (MutableSequence[str]):
            Optional. HCFS file URIs of Python files to
            pass to the PySpark framework. Supported file
            types: .py, .egg, and .zip.
        jar_file_uris (MutableSequence[str]):
            Optional. HCFS URIs of jar files to add to
            the CLASSPATHs of the Python driver and tasks.
        file_uris (MutableSequence[str]):
            Optional. HCFS URIs of files to be placed in
            the working directory of each executor. Useful
            for naively parallel tasks.
        archive_uris (MutableSequence[str]):
            Optional. HCFS URIs of archives to be
            extracted into the working directory of each
            executor. Supported file types:

            .jar, .tar, .tar.gz, .tgz, and .zip.
        properties (MutableMapping[str, str]):
            Optional. A mapping of property names to
            values, used to configure PySpark. Properties
            that conflict with values set by the Dataproc
            API might be overwritten. Can include properties
            set in
            /etc/spark/conf/spark-defaults.conf and classes
            in user code.
        logging_config (google.cloud.dataproc_v1.types.LoggingConfig):
            Optional. The runtime log config for job
            execution.
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
    properties: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    logging_config: "LoggingConfig" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="LoggingConfig",
    )


class QueryList(proto.Message):
    r"""A list of queries to run on a cluster.

    Attributes:
        queries (MutableSequence[str]):
            Required. The queries to execute. You do not need to end a
            query expression with a semicolon. Multiple queries can be
            specified in one string by separating each with a semicolon.
            Here is an example of a Dataproc API snippet that uses a
            QueryList to specify a HiveJob:

            ::

                "hiveJob": {
                  "queryList": {
                    "queries": [
                      "query1",
                      "query2",
                      "query3;query4",
                    ]
                  }
                }
    """

    queries: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class HiveJob(proto.Message):
    r"""A Dataproc job for running `Apache
    Hive <https://hive.apache.org/>`__ queries on YARN.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        query_file_uri (str):
            The HCFS URI of the script that contains Hive
            queries.

            This field is a member of `oneof`_ ``queries``.
        query_list (google.cloud.dataproc_v1.types.QueryList):
            A list of queries.

            This field is a member of `oneof`_ ``queries``.
        continue_on_failure (bool):
            Optional. Whether to continue executing queries if a query
            fails. The default value is ``false``. Setting to ``true``
            can be useful when executing independent parallel queries.
        script_variables (MutableMapping[str, str]):
            Optional. Mapping of query variable names to values
            (equivalent to the Hive command: ``SET name="value";``).
        properties (MutableMapping[str, str]):
            Optional. A mapping of property names and values, used to
            configure Hive. Properties that conflict with values set by
            the Dataproc API might be overwritten. Can include
            properties set in ``/etc/hadoop/conf/*-site.xml``,
            /etc/hive/conf/hive-site.xml, and classes in user code.
        jar_file_uris (MutableSequence[str]):
            Optional. HCFS URIs of jar files to add to
            the CLASSPATH of the Hive server and Hadoop
            MapReduce (MR) tasks. Can contain Hive SerDes
            and UDFs.
    """

    query_file_uri: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="queries",
    )
    query_list: "QueryList" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="queries",
        message="QueryList",
    )
    continue_on_failure: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    script_variables: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    properties: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    jar_file_uris: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )


class SparkSqlJob(proto.Message):
    r"""A Dataproc job for running `Apache Spark
    SQL <https://spark.apache.org/sql/>`__ queries.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        query_file_uri (str):
            The HCFS URI of the script that contains SQL
            queries.

            This field is a member of `oneof`_ ``queries``.
        query_list (google.cloud.dataproc_v1.types.QueryList):
            A list of queries.

            This field is a member of `oneof`_ ``queries``.
        script_variables (MutableMapping[str, str]):
            Optional. Mapping of query variable names to values
            (equivalent to the Spark SQL command: SET
            ``name="value";``).
        properties (MutableMapping[str, str]):
            Optional. A mapping of property names to
            values, used to configure Spark SQL's SparkConf.
            Properties that conflict with values set by the
            Dataproc API might be overwritten.
        jar_file_uris (MutableSequence[str]):
            Optional. HCFS URIs of jar files to be added
            to the Spark CLASSPATH.
        logging_config (google.cloud.dataproc_v1.types.LoggingConfig):
            Optional. The runtime log config for job
            execution.
    """

    query_file_uri: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="queries",
    )
    query_list: "QueryList" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="queries",
        message="QueryList",
    )
    script_variables: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )
    properties: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    jar_file_uris: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=56,
    )
    logging_config: "LoggingConfig" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="LoggingConfig",
    )


class PigJob(proto.Message):
    r"""A Dataproc job for running `Apache Pig <https://pig.apache.org/>`__
    queries on YARN.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        query_file_uri (str):
            The HCFS URI of the script that contains the
            Pig queries.

            This field is a member of `oneof`_ ``queries``.
        query_list (google.cloud.dataproc_v1.types.QueryList):
            A list of queries.

            This field is a member of `oneof`_ ``queries``.
        continue_on_failure (bool):
            Optional. Whether to continue executing queries if a query
            fails. The default value is ``false``. Setting to ``true``
            can be useful when executing independent parallel queries.
        script_variables (MutableMapping[str, str]):
            Optional. Mapping of query variable names to values
            (equivalent to the Pig command: ``name=[value]``).
        properties (MutableMapping[str, str]):
            Optional. A mapping of property names to values, used to
            configure Pig. Properties that conflict with values set by
            the Dataproc API might be overwritten. Can include
            properties set in ``/etc/hadoop/conf/*-site.xml``,
            /etc/pig/conf/pig.properties, and classes in user code.
        jar_file_uris (MutableSequence[str]):
            Optional. HCFS URIs of jar files to add to
            the CLASSPATH of the Pig Client and Hadoop
            MapReduce (MR) tasks. Can contain Pig UDFs.
        logging_config (google.cloud.dataproc_v1.types.LoggingConfig):
            Optional. The runtime log config for job
            execution.
    """

    query_file_uri: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="queries",
    )
    query_list: "QueryList" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="queries",
        message="QueryList",
    )
    continue_on_failure: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    script_variables: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    properties: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    jar_file_uris: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    logging_config: "LoggingConfig" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="LoggingConfig",
    )


class SparkRJob(proto.Message):
    r"""A Dataproc job for running `Apache
    SparkR <https://spark.apache.org/docs/latest/sparkr.html>`__
    applications on YARN.

    Attributes:
        main_r_file_uri (str):
            Required. The HCFS URI of the main R file to
            use as the driver. Must be a .R file.
        args (MutableSequence[str]):
            Optional. The arguments to pass to the driver. Do not
            include arguments, such as ``--conf``, that can be set as
            job properties, since a collision may occur that causes an
            incorrect job submission.
        file_uris (MutableSequence[str]):
            Optional. HCFS URIs of files to be placed in
            the working directory of each executor. Useful
            for naively parallel tasks.
        archive_uris (MutableSequence[str]):
            Optional. HCFS URIs of archives to be
            extracted into the working directory of each
            executor. Supported file types:

            .jar, .tar, .tar.gz, .tgz, and .zip.
        properties (MutableMapping[str, str]):
            Optional. A mapping of property names to
            values, used to configure SparkR. Properties
            that conflict with values set by the Dataproc
            API might be overwritten. Can include properties
            set in
            /etc/spark/conf/spark-defaults.conf and classes
            in user code.
        logging_config (google.cloud.dataproc_v1.types.LoggingConfig):
            Optional. The runtime log config for job
            execution.
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
    properties: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    logging_config: "LoggingConfig" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="LoggingConfig",
    )


class PrestoJob(proto.Message):
    r"""A Dataproc job for running `Presto <https://prestosql.io/>`__
    queries. **IMPORTANT**: The `Dataproc Presto Optional
    Component <https://cloud.google.com/dataproc/docs/concepts/components/presto>`__
    must be enabled when the cluster is created to submit a Presto job
    to the cluster.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        query_file_uri (str):
            The HCFS URI of the script that contains SQL
            queries.

            This field is a member of `oneof`_ ``queries``.
        query_list (google.cloud.dataproc_v1.types.QueryList):
            A list of queries.

            This field is a member of `oneof`_ ``queries``.
        continue_on_failure (bool):
            Optional. Whether to continue executing queries if a query
            fails. The default value is ``false``. Setting to ``true``
            can be useful when executing independent parallel queries.
        output_format (str):
            Optional. The format in which query output
            will be displayed. See the Presto documentation
            for supported output formats
        client_tags (MutableSequence[str]):
            Optional. Presto client tags to attach to
            this query
        properties (MutableMapping[str, str]):
            Optional. A mapping of property names to values. Used to set
            Presto `session
            properties <https://prestodb.io/docs/current/sql/set-session.html>`__
            Equivalent to using the --session flag in the Presto CLI
        logging_config (google.cloud.dataproc_v1.types.LoggingConfig):
            Optional. The runtime log config for job
            execution.
    """

    query_file_uri: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="queries",
    )
    query_list: "QueryList" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="queries",
        message="QueryList",
    )
    continue_on_failure: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    output_format: str = proto.Field(
        proto.STRING,
        number=4,
    )
    client_tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    properties: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    logging_config: "LoggingConfig" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="LoggingConfig",
    )


class TrinoJob(proto.Message):
    r"""A Dataproc job for running `Trino <https://trino.io/>`__ queries.
    **IMPORTANT**: The `Dataproc Trino Optional
    Component <https://cloud.google.com/dataproc/docs/concepts/components/trino>`__
    must be enabled when the cluster is created to submit a Trino job to
    the cluster.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        query_file_uri (str):
            The HCFS URI of the script that contains SQL
            queries.

            This field is a member of `oneof`_ ``queries``.
        query_list (google.cloud.dataproc_v1.types.QueryList):
            A list of queries.

            This field is a member of `oneof`_ ``queries``.
        continue_on_failure (bool):
            Optional. Whether to continue executing queries if a query
            fails. The default value is ``false``. Setting to ``true``
            can be useful when executing independent parallel queries.
        output_format (str):
            Optional. The format in which query output
            will be displayed. See the Trino documentation
            for supported output formats
        client_tags (MutableSequence[str]):
            Optional. Trino client tags to attach to this
            query
        properties (MutableMapping[str, str]):
            Optional. A mapping of property names to values. Used to set
            Trino `session
            properties <https://trino.io/docs/current/sql/set-session.html>`__
            Equivalent to using the --session flag in the Trino CLI
        logging_config (google.cloud.dataproc_v1.types.LoggingConfig):
            Optional. The runtime log config for job
            execution.
    """

    query_file_uri: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="queries",
    )
    query_list: "QueryList" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="queries",
        message="QueryList",
    )
    continue_on_failure: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    output_format: str = proto.Field(
        proto.STRING,
        number=4,
    )
    client_tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    properties: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    logging_config: "LoggingConfig" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="LoggingConfig",
    )


class FlinkJob(proto.Message):
    r"""A Dataproc job for running Apache Flink applications on YARN.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        main_jar_file_uri (str):
            The HCFS URI of the jar file that contains
            the main class.

            This field is a member of `oneof`_ ``driver``.
        main_class (str):
            The name of the driver's main class. The jar file that
            contains the class must be in the default CLASSPATH or
            specified in
            [jarFileUris][google.cloud.dataproc.v1.FlinkJob.jar_file_uris].

            This field is a member of `oneof`_ ``driver``.
        args (MutableSequence[str]):
            Optional. The arguments to pass to the driver. Do not
            include arguments, such as ``--conf``, that can be set as
            job properties, since a collision might occur that causes an
            incorrect job submission.
        jar_file_uris (MutableSequence[str]):
            Optional. HCFS URIs of jar files to add to
            the CLASSPATHs of the Flink driver and tasks.
        savepoint_uri (str):
            Optional. HCFS URI of the savepoint, which
            contains the last saved progress for starting
            the current job.
        properties (MutableMapping[str, str]):
            Optional. A mapping of property names to values, used to
            configure Flink. Properties that conflict with values set by
            the Dataproc API might be overwritten. Can include
            properties set in ``/etc/flink/conf/flink-defaults.conf``
            and classes in user code.
        logging_config (google.cloud.dataproc_v1.types.LoggingConfig):
            Optional. The runtime log config for job
            execution.
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
    savepoint_uri: str = proto.Field(
        proto.STRING,
        number=9,
    )
    properties: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    logging_config: "LoggingConfig" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="LoggingConfig",
    )


class JobPlacement(proto.Message):
    r"""Dataproc job config.

    Attributes:
        cluster_name (str):
            Required. The name of the cluster where the
            job will be submitted.
        cluster_uuid (str):
            Output only. A cluster UUID generated by the
            Dataproc service when the job is submitted.
        cluster_labels (MutableMapping[str, str]):
            Optional. Cluster labels to identify a
            cluster where the job will be submitted.
    """

    cluster_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cluster_uuid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    cluster_labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )


class JobStatus(proto.Message):
    r"""Dataproc job status.

    Attributes:
        state (google.cloud.dataproc_v1.types.JobStatus.State):
            Output only. A state message specifying the
            overall job state.
        details (str):
            Optional. Output only. Job state details, such as an error
            description if the state is ``ERROR``.
        state_start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when this state was
            entered.
        substate (google.cloud.dataproc_v1.types.JobStatus.Substate):
            Output only. Additional state information,
            which includes status reported by the agent.
    """

    class State(proto.Enum):
        r"""The job state.

        Values:
            STATE_UNSPECIFIED (0):
                The job state is unknown.
            PENDING (1):
                The job is pending; it has been submitted,
                but is not yet running.
            SETUP_DONE (8):
                Job has been received by the service and
                completed initial setup; it will soon be
                submitted to the cluster.
            RUNNING (2):
                The job is running on the cluster.
            CANCEL_PENDING (3):
                A CancelJob request has been received, but is
                pending.
            CANCEL_STARTED (7):
                Transient in-flight resources have been
                canceled, and the request to cancel the running
                job has been issued to the cluster.
            CANCELLED (4):
                The job cancellation was successful.
            DONE (5):
                The job has completed successfully.
            ERROR (6):
                The job has completed, but encountered an
                error.
            ATTEMPT_FAILURE (9):
                Job attempt has failed. The detail field
                contains failure details for this attempt.

                Applies to restartable jobs only.
        """

        STATE_UNSPECIFIED = 0
        PENDING = 1
        SETUP_DONE = 8
        RUNNING = 2
        CANCEL_PENDING = 3
        CANCEL_STARTED = 7
        CANCELLED = 4
        DONE = 5
        ERROR = 6
        ATTEMPT_FAILURE = 9

    class Substate(proto.Enum):
        r"""The job substate.

        Values:
            UNSPECIFIED (0):
                The job substate is unknown.
            SUBMITTED (1):
                The Job is submitted to the agent.

                Applies to RUNNING state.
            QUEUED (2):
                The Job has been received and is awaiting
                execution (it might be waiting for a condition
                to be met). See the "details" field for the
                reason for the delay.

                Applies to RUNNING state.
            STALE_STATUS (3):
                The agent-reported status is out of date,
                which can be caused by a loss of communication
                between the agent and Dataproc. If the agent
                does not send a timely update, the job will
                fail.

                Applies to RUNNING state.
        """

        UNSPECIFIED = 0
        SUBMITTED = 1
        QUEUED = 2
        STALE_STATUS = 3

    state: State = proto.Field(
        proto.ENUM,
        number=1,
        enum=State,
    )
    details: str = proto.Field(
        proto.STRING,
        number=2,
    )
    state_start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    substate: Substate = proto.Field(
        proto.ENUM,
        number=7,
        enum=Substate,
    )


class JobReference(proto.Message):
    r"""Encapsulates the full scoping used to reference a job.

    Attributes:
        project_id (str):
            Optional. The ID of the Google Cloud Platform
            project that the job belongs to. If specified,
            must match the request project ID.
        job_id (str):
            Optional. The job ID, which must be unique within the
            project.

            The ID must contain only letters (a-z, A-Z), numbers (0-9),
            underscores (\_), or hyphens (-). The maximum length is 100
            characters.

            If not specified by the caller, the job ID will be provided
            by the server.
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    job_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class YarnApplication(proto.Message):
    r"""A YARN application created by a job. Application information is a
    subset of
    org.apache.hadoop.yarn.proto.YarnProtos.ApplicationReportProto.

    **Beta Feature**: This report is available for testing purposes
    only. It may be changed before final release.

    Attributes:
        name (str):
            Required. The application name.
        state (google.cloud.dataproc_v1.types.YarnApplication.State):
            Required. The application state.
        progress (float):
            Required. The numerical progress of the
            application, from 1 to 100.
        tracking_url (str):
            Optional. The HTTP URL of the
            ApplicationMaster, HistoryServer, or
            TimelineServer that provides
            application-specific information. The URL uses
            the internal hostname, and requires a proxy
            server for resolution and, possibly, access.
        vcore_seconds (int):
            Optional. The cumulative CPU time consumed by
            the application for a job, measured in
            vcore-seconds.
        memory_mb_seconds (int):
            Optional. The cumulative memory usage of the
            application for a job, measured in mb-seconds.
    """

    class State(proto.Enum):
        r"""The application state, corresponding to
        <code>YarnProtos.YarnApplicationStateProto</code>.

        Values:
            STATE_UNSPECIFIED (0):
                Status is unspecified.
            NEW (1):
                Status is NEW.
            NEW_SAVING (2):
                Status is NEW_SAVING.
            SUBMITTED (3):
                Status is SUBMITTED.
            ACCEPTED (4):
                Status is ACCEPTED.
            RUNNING (5):
                Status is RUNNING.
            FINISHED (6):
                Status is FINISHED.
            FAILED (7):
                Status is FAILED.
            KILLED (8):
                Status is KILLED.
        """

        STATE_UNSPECIFIED = 0
        NEW = 1
        NEW_SAVING = 2
        SUBMITTED = 3
        ACCEPTED = 4
        RUNNING = 5
        FINISHED = 6
        FAILED = 7
        KILLED = 8

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=2,
        enum=State,
    )
    progress: float = proto.Field(
        proto.FLOAT,
        number=3,
    )
    tracking_url: str = proto.Field(
        proto.STRING,
        number=4,
    )
    vcore_seconds: int = proto.Field(
        proto.INT64,
        number=5,
    )
    memory_mb_seconds: int = proto.Field(
        proto.INT64,
        number=6,
    )


class Job(proto.Message):
    r"""A Dataproc job resource.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        reference (google.cloud.dataproc_v1.types.JobReference):
            Optional. The fully qualified reference to the job, which
            can be used to obtain the equivalent REST path of the job
            resource. If this property is not specified when a job is
            created, the server generates a job_id.
        placement (google.cloud.dataproc_v1.types.JobPlacement):
            Required. Job information, including how,
            when, and where to run the job.
        hadoop_job (google.cloud.dataproc_v1.types.HadoopJob):
            Optional. Job is a Hadoop job.

            This field is a member of `oneof`_ ``type_job``.
        spark_job (google.cloud.dataproc_v1.types.SparkJob):
            Optional. Job is a Spark job.

            This field is a member of `oneof`_ ``type_job``.
        pyspark_job (google.cloud.dataproc_v1.types.PySparkJob):
            Optional. Job is a PySpark job.

            This field is a member of `oneof`_ ``type_job``.
        hive_job (google.cloud.dataproc_v1.types.HiveJob):
            Optional. Job is a Hive job.

            This field is a member of `oneof`_ ``type_job``.
        pig_job (google.cloud.dataproc_v1.types.PigJob):
            Optional. Job is a Pig job.

            This field is a member of `oneof`_ ``type_job``.
        spark_r_job (google.cloud.dataproc_v1.types.SparkRJob):
            Optional. Job is a SparkR job.

            This field is a member of `oneof`_ ``type_job``.
        spark_sql_job (google.cloud.dataproc_v1.types.SparkSqlJob):
            Optional. Job is a SparkSql job.

            This field is a member of `oneof`_ ``type_job``.
        presto_job (google.cloud.dataproc_v1.types.PrestoJob):
            Optional. Job is a Presto job.

            This field is a member of `oneof`_ ``type_job``.
        trino_job (google.cloud.dataproc_v1.types.TrinoJob):
            Optional. Job is a Trino job.

            This field is a member of `oneof`_ ``type_job``.
        flink_job (google.cloud.dataproc_v1.types.FlinkJob):
            Optional. Job is a Flink job.

            This field is a member of `oneof`_ ``type_job``.
        status (google.cloud.dataproc_v1.types.JobStatus):
            Output only. The job status. Additional application-specific
            status information might be contained in the type_job and
            yarn_applications fields.
        status_history (MutableSequence[google.cloud.dataproc_v1.types.JobStatus]):
            Output only. The previous job status.
        yarn_applications (MutableSequence[google.cloud.dataproc_v1.types.YarnApplication]):
            Output only. The collection of YARN applications spun up by
            this job.

            **Beta** Feature: This report is available for testing
            purposes only. It might be changed before final release.
        driver_output_resource_uri (str):
            Output only. A URI pointing to the location
            of the stdout of the job's driver program.
        driver_control_files_uri (str):
            Output only. If present, the location of miscellaneous
            control files which can be used as part of job setup and
            handling. If not present, control files might be placed in
            the same location as ``driver_output_uri``.
        labels (MutableMapping[str, str]):
            Optional. The labels to associate with this job. Label
            **keys** must contain 1 to 63 characters, and must conform
            to `RFC 1035 <https://www.ietf.org/rfc/rfc1035.txt>`__.
            Label **values** can be empty, but, if present, must contain
            1 to 63 characters, and must conform to `RFC
            1035 <https://www.ietf.org/rfc/rfc1035.txt>`__. No more than
            32 labels can be associated with a job.
        scheduling (google.cloud.dataproc_v1.types.JobScheduling):
            Optional. Job scheduling configuration.
        job_uuid (str):
            Output only. A UUID that uniquely identifies a job within
            the project over time. This is in contrast to a
            user-settable reference.job_id that might be reused over
            time.
        done (bool):
            Output only. Indicates whether the job is completed. If the
            value is ``false``, the job is still in progress. If
            ``true``, the job is completed, and ``status.state`` field
            will indicate if it was successful, failed, or cancelled.
        driver_scheduling_config (google.cloud.dataproc_v1.types.DriverSchedulingConfig):
            Optional. Driver scheduling configuration.
    """

    reference: "JobReference" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="JobReference",
    )
    placement: "JobPlacement" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="JobPlacement",
    )
    hadoop_job: "HadoopJob" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="type_job",
        message="HadoopJob",
    )
    spark_job: "SparkJob" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="type_job",
        message="SparkJob",
    )
    pyspark_job: "PySparkJob" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="type_job",
        message="PySparkJob",
    )
    hive_job: "HiveJob" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="type_job",
        message="HiveJob",
    )
    pig_job: "PigJob" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="type_job",
        message="PigJob",
    )
    spark_r_job: "SparkRJob" = proto.Field(
        proto.MESSAGE,
        number=21,
        oneof="type_job",
        message="SparkRJob",
    )
    spark_sql_job: "SparkSqlJob" = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="type_job",
        message="SparkSqlJob",
    )
    presto_job: "PrestoJob" = proto.Field(
        proto.MESSAGE,
        number=23,
        oneof="type_job",
        message="PrestoJob",
    )
    trino_job: "TrinoJob" = proto.Field(
        proto.MESSAGE,
        number=28,
        oneof="type_job",
        message="TrinoJob",
    )
    flink_job: "FlinkJob" = proto.Field(
        proto.MESSAGE,
        number=29,
        oneof="type_job",
        message="FlinkJob",
    )
    status: "JobStatus" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="JobStatus",
    )
    status_history: MutableSequence["JobStatus"] = proto.RepeatedField(
        proto.MESSAGE,
        number=13,
        message="JobStatus",
    )
    yarn_applications: MutableSequence["YarnApplication"] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="YarnApplication",
    )
    driver_output_resource_uri: str = proto.Field(
        proto.STRING,
        number=17,
    )
    driver_control_files_uri: str = proto.Field(
        proto.STRING,
        number=15,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=18,
    )
    scheduling: "JobScheduling" = proto.Field(
        proto.MESSAGE,
        number=20,
        message="JobScheduling",
    )
    job_uuid: str = proto.Field(
        proto.STRING,
        number=22,
    )
    done: bool = proto.Field(
        proto.BOOL,
        number=24,
    )
    driver_scheduling_config: "DriverSchedulingConfig" = proto.Field(
        proto.MESSAGE,
        number=27,
        message="DriverSchedulingConfig",
    )


class DriverSchedulingConfig(proto.Message):
    r"""Driver scheduling configuration.

    Attributes:
        memory_mb (int):
            Required. The amount of memory in MB the
            driver is requesting.
        vcores (int):
            Required. The number of vCPUs the driver is
            requesting.
    """

    memory_mb: int = proto.Field(
        proto.INT32,
        number=1,
    )
    vcores: int = proto.Field(
        proto.INT32,
        number=2,
    )


class JobScheduling(proto.Message):
    r"""Job scheduling options.

    Attributes:
        max_failures_per_hour (int):
            Optional. Maximum number of times per hour a driver can be
            restarted as a result of driver exiting with non-zero code
            before job is reported failed.

            A job might be reported as thrashing if the driver exits
            with a non-zero code four times within a 10-minute window.

            Maximum value is 10.

            **Note:** This restartable job option is not supported in
            Dataproc [workflow templates]
            (https://cloud.google.com/dataproc/docs/concepts/workflows/using-workflows#adding_jobs_to_a_template).
        max_failures_total (int):
            Optional. Maximum total number of times a driver can be
            restarted as a result of the driver exiting with a non-zero
            code. After the maximum number is reached, the job will be
            reported as failed.

            Maximum value is 240.

            **Note:** Currently, this restartable job option is not
            supported in Dataproc `workflow
            templates <https://cloud.google.com/dataproc/docs/concepts/workflows/using-workflows#adding_jobs_to_a_template>`__.
    """

    max_failures_per_hour: int = proto.Field(
        proto.INT32,
        number=1,
    )
    max_failures_total: int = proto.Field(
        proto.INT32,
        number=2,
    )


class SubmitJobRequest(proto.Message):
    r"""A request to submit a job.

    Attributes:
        project_id (str):
            Required. The ID of the Google Cloud Platform
            project that the job belongs to.
        region (str):
            Required. The Dataproc region in which to
            handle the request.
        job (google.cloud.dataproc_v1.types.Job):
            Required. The job resource.
        request_id (str):
            Optional. A unique id used to identify the request. If the
            server receives two
            `SubmitJobRequest <https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#google.cloud.dataproc.v1.SubmitJobRequest>`__\ s
            with the same id, then the second request will be ignored
            and the first [Job][google.cloud.dataproc.v1.Job] created
            and stored in the backend is returned.

            It is recommended to always set this value to a
            `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier>`__.

            The id must contain only letters (a-z, A-Z), numbers (0-9),
            underscores (\_), and hyphens (-). The maximum length is 40
            characters.
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    region: str = proto.Field(
        proto.STRING,
        number=3,
    )
    job: "Job" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Job",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class JobMetadata(proto.Message):
    r"""Job Operation metadata.

    Attributes:
        job_id (str):
            Output only. The job id.
        status (google.cloud.dataproc_v1.types.JobStatus):
            Output only. Most recent job status.
        operation_type (str):
            Output only. Operation type.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Job submission time.
    """

    job_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    status: "JobStatus" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="JobStatus",
    )
    operation_type: str = proto.Field(
        proto.STRING,
        number=3,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


class GetJobRequest(proto.Message):
    r"""A request to get the resource representation for a job in a
    project.

    Attributes:
        project_id (str):
            Required. The ID of the Google Cloud Platform
            project that the job belongs to.
        region (str):
            Required. The Dataproc region in which to
            handle the request.
        job_id (str):
            Required. The job ID.
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    region: str = proto.Field(
        proto.STRING,
        number=3,
    )
    job_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListJobsRequest(proto.Message):
    r"""A request to list jobs in a project.

    Attributes:
        project_id (str):
            Required. The ID of the Google Cloud Platform
            project that the job belongs to.
        region (str):
            Required. The Dataproc region in which to
            handle the request.
        page_size (int):
            Optional. The number of results to return in
            each response.
        page_token (str):
            Optional. The page token, returned by a
            previous call, to request the next page of
            results.
        cluster_name (str):
            Optional. If set, the returned jobs list
            includes only jobs that were submitted to the
            named cluster.
        job_state_matcher (google.cloud.dataproc_v1.types.ListJobsRequest.JobStateMatcher):
            Optional. Specifies enumerated categories of jobs to list.
            (default = match ALL jobs).

            If ``filter`` is provided, ``jobStateMatcher`` will be
            ignored.
        filter (str):
            Optional. A filter constraining the jobs to list. Filters
            are case-sensitive and have the following syntax:

            [field = value] AND [field [= value]] ...

            where **field** is ``status.state`` or ``insertTime``, or
            ``labels.[KEY]``, and ``[KEY]`` is a label key. **value**
            can be ``*`` to match all values. ``status.state`` can be
            either ``ACTIVE`` or ``NON_ACTIVE``. Allows ``insertTime``
            to be a timestamp in RFC 3339 format in double quotes, such
            as ``2025-01-01T00:00:00Z``. Only the logical ``AND``
            operator is supported; space-separated items are treated as
            having an implicit ``AND`` operator.

            Example filter:

            status.state = ACTIVE AND labels.env = staging AND
            labels.starred = \* AND insertTime <= "2025-01-01T00:00:00Z".
    """

    class JobStateMatcher(proto.Enum):
        r"""A matcher that specifies categories of job states.

        Values:
            ALL (0):
                Match all jobs, regardless of state.
            ACTIVE (1):
                Only match jobs in non-terminal states: PENDING, RUNNING, or
                CANCEL_PENDING.
            NON_ACTIVE (2):
                Only match jobs in terminal states:
                CANCELLED, DONE, or ERROR.
        """

        ALL = 0
        ACTIVE = 1
        NON_ACTIVE = 2

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    region: str = proto.Field(
        proto.STRING,
        number=6,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    cluster_name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    job_state_matcher: JobStateMatcher = proto.Field(
        proto.ENUM,
        number=5,
        enum=JobStateMatcher,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=7,
    )


class UpdateJobRequest(proto.Message):
    r"""A request to update a job.

    Attributes:
        project_id (str):
            Required. The ID of the Google Cloud Platform
            project that the job belongs to.
        region (str):
            Required. The Dataproc region in which to
            handle the request.
        job_id (str):
            Required. The job ID.
        job (google.cloud.dataproc_v1.types.Job):
            Required. The changes to the job.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Specifies the path, relative to Job, of the field
            to update. For example, to update the labels of a Job the
            update_mask parameter would be specified as labels, and the
            ``PATCH`` request body would specify the new value. Note:
            Currently, labels is the only field that can be updated.
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    region: str = proto.Field(
        proto.STRING,
        number=2,
    )
    job_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    job: "Job" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="Job",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=5,
        message=field_mask_pb2.FieldMask,
    )


class ListJobsResponse(proto.Message):
    r"""A list of jobs in a project.

    Attributes:
        jobs (MutableSequence[google.cloud.dataproc_v1.types.Job]):
            Output only. Jobs list.
        next_page_token (str):
            Optional. This token is included in the response if there
            are more results to fetch. To fetch additional results,
            provide this value as the ``page_token`` in a subsequent
            ListJobsRequest.
        unreachable (MutableSequence[str]):
            Output only. List of jobs with
            [kms_key][google.cloud.dataproc.v1.EncryptionConfig.kms_key]-encrypted
            parameters that could not be decrypted. A response to a
            ``jobs.get`` request may indicate the reason for the
            decryption failure for a specific job.
    """

    @property
    def raw_page(self):
        return self

    jobs: MutableSequence["Job"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Job",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class CancelJobRequest(proto.Message):
    r"""A request to cancel a job.

    Attributes:
        project_id (str):
            Required. The ID of the Google Cloud Platform
            project that the job belongs to.
        region (str):
            Required. The Dataproc region in which to
            handle the request.
        job_id (str):
            Required. The job ID.
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    region: str = proto.Field(
        proto.STRING,
        number=3,
    )
    job_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteJobRequest(proto.Message):
    r"""A request to delete a job.

    Attributes:
        project_id (str):
            Required. The ID of the Google Cloud Platform
            project that the job belongs to.
        region (str):
            Required. The Dataproc region in which to
            handle the request.
        job_id (str):
            Required. The job ID.
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    region: str = proto.Field(
        proto.STRING,
        number=3,
    )
    job_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
