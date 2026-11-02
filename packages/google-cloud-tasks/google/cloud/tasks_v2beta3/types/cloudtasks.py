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
import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.tasks_v2beta3.types import cmek_config as gct_cmek_config
from google.cloud.tasks_v2beta3.types import queue as gct_queue
from google.cloud.tasks_v2beta3.types import task as gct_task

__protobuf__ = proto.module(
    package="google.cloud.tasks.v2beta3",
    manifest={
        "ListQueuesRequest",
        "ListQueuesResponse",
        "GetQueueRequest",
        "CreateQueueRequest",
        "UpdateQueueRequest",
        "DeleteQueueRequest",
        "PurgeQueueRequest",
        "PauseQueueRequest",
        "ResumeQueueRequest",
        "ListTasksRequest",
        "ListTasksResponse",
        "GetTaskRequest",
        "CreateTaskRequest",
        "BatchCreateTasksRequest",
        "DeleteTaskRequest",
        "BatchDeleteTasksRequest",
        "BatchDeleteTasksMetadata",
        "RunTaskRequest",
        "BatchCreateTasksResponse",
        "BatchCreateTasksMetadata",
        "UpdateCmekConfigRequest",
        "GetCmekConfigRequest",
    },
)


class ListQueuesRequest(proto.Message):
    r"""Request message for
    [ListQueues][google.cloud.tasks.v2beta3.CloudTasks.ListQueues].

    Attributes:
        parent (str):
            Required. The location name. For example:
            ``projects/PROJECT_ID/locations/LOCATION_ID``
        filter (str):
            ``filter`` can be used to specify a subset of queues. Any
            [Queue][google.cloud.tasks.v2beta3.Queue] field can be used
            as a filter and several operators as supported. For example:
            ``<=, <, >=, >, !=, =, :``. The filter syntax is the same as
            described in `Stackdriver's Advanced Logs
            Filters <https://cloud.google.com/logging/docs/view/advanced_filters>`__.

            Sample filter "state: PAUSED".

            Note that using filters might cause fewer queues than the
            requested page_size to be returned.
        page_size (int):
            Requested page size.

            The maximum page size is 9800. If unspecified, the page size
            will be the maximum. Fewer queues than requested might be
            returned, even if more queues exist; use the
            [next_page_token][google.cloud.tasks.v2beta3.ListQueuesResponse.next_page_token]
            in the response to determine if more queues exist.
        page_token (str):
            A token identifying the page of results to return.

            To request the first page results, page_token must be empty.
            To request the next page of results, page_token must be the
            value of
            [next_page_token][google.cloud.tasks.v2beta3.ListQueuesResponse.next_page_token]
            returned from the previous call to
            [ListQueues][google.cloud.tasks.v2beta3.CloudTasks.ListQueues]
            method. It is an error to switch the value of the
            [filter][google.cloud.tasks.v2beta3.ListQueuesRequest.filter]
            while iterating through pages.
        read_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Read mask is used for a more granular control over
            what the API returns. If the mask is not present all fields
            will be returned except [Queue.stats]. [Queue.stats] will be
            returned only if it was explicitly specified in the mask.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )
    read_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=5,
        message=field_mask_pb2.FieldMask,
    )


class ListQueuesResponse(proto.Message):
    r"""Response message for
    [ListQueues][google.cloud.tasks.v2beta3.CloudTasks.ListQueues].

    Attributes:
        queues (MutableSequence[google.cloud.tasks_v2beta3.types.Queue]):
            The list of queues.
        next_page_token (str):
            A token to retrieve next page of results.

            To return the next page of results, call
            [ListQueues][google.cloud.tasks.v2beta3.CloudTasks.ListQueues]
            with this value as the
            [page_token][google.cloud.tasks.v2beta3.ListQueuesRequest.page_token].

            If the next_page_token is empty, there are no more results.

            The page token is valid for only 2 hours.
    """

    @property
    def raw_page(self):
        return self

    queues: MutableSequence[gct_queue.Queue] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gct_queue.Queue,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetQueueRequest(proto.Message):
    r"""Request message for
    [GetQueue][google.cloud.tasks.v2beta3.CloudTasks.GetQueue].

    Attributes:
        name (str):
            Required. The resource name of the queue. For example:
            ``projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID``
        read_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Read mask is used for a more granular control over
            what the API returns. If the mask is not present all fields
            will be returned except [Queue.stats]. [Queue.stats] will be
            returned only if it was explicitly specified in the mask.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    read_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class CreateQueueRequest(proto.Message):
    r"""Request message for
    [CreateQueue][google.cloud.tasks.v2beta3.CloudTasks.CreateQueue].

    Attributes:
        parent (str):
            Required. The location name in which the queue will be
            created. For example:
            ``projects/PROJECT_ID/locations/LOCATION_ID``

            The list of allowed locations can be obtained by calling
            Cloud Tasks' implementation of
            [ListLocations][google.cloud.location.Locations.ListLocations].
        queue (google.cloud.tasks_v2beta3.types.Queue):
            Required. The queue to create.

            [Queue's name][google.cloud.tasks.v2beta3.Queue.name] cannot
            be the same as an existing queue.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    queue: gct_queue.Queue = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gct_queue.Queue,
    )


class UpdateQueueRequest(proto.Message):
    r"""Request message for
    [UpdateQueue][google.cloud.tasks.v2beta3.CloudTasks.UpdateQueue].

    Attributes:
        queue (google.cloud.tasks_v2beta3.types.Queue):
            Required. The queue to create or update.

            The queue's [name][google.cloud.tasks.v2beta3.Queue.name]
            must be specified.

            Output only fields cannot be modified using UpdateQueue. Any
            value specified for an output only field will be ignored.
            The queue's [name][google.cloud.tasks.v2beta3.Queue.name]
            cannot be changed.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            A mask used to specify which fields of the
            queue are being updated.
            If empty, then all fields will be updated.
    """

    queue: gct_queue.Queue = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gct_queue.Queue,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteQueueRequest(proto.Message):
    r"""Request message for
    [DeleteQueue][google.cloud.tasks.v2beta3.CloudTasks.DeleteQueue].

    Attributes:
        name (str):
            Required. The queue name. For example:
            ``projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class PurgeQueueRequest(proto.Message):
    r"""Request message for
    [PurgeQueue][google.cloud.tasks.v2beta3.CloudTasks.PurgeQueue].

    Attributes:
        name (str):
            Required. The queue name. For example:
            ``projects/PROJECT_ID/location/LOCATION_ID/queues/QUEUE_ID``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class PauseQueueRequest(proto.Message):
    r"""Request message for
    [PauseQueue][google.cloud.tasks.v2beta3.CloudTasks.PauseQueue].

    Attributes:
        name (str):
            Required. The queue name. For example:
            ``projects/PROJECT_ID/location/LOCATION_ID/queues/QUEUE_ID``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ResumeQueueRequest(proto.Message):
    r"""Request message for
    [ResumeQueue][google.cloud.tasks.v2beta3.CloudTasks.ResumeQueue].

    Attributes:
        name (str):
            Required. The queue name. For example:
            ``projects/PROJECT_ID/location/LOCATION_ID/queues/QUEUE_ID``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListTasksRequest(proto.Message):
    r"""Request message for listing tasks using
    [ListTasks][google.cloud.tasks.v2beta3.CloudTasks.ListTasks].

    Attributes:
        parent (str):
            Required. The queue name. For example:
            ``projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID``
        response_view (google.cloud.tasks_v2beta3.types.Task.View):
            The response_view specifies which subset of the
            [Task][google.cloud.tasks.v2beta3.Task] will be returned.

            By default response_view is
            [BASIC][google.cloud.tasks.v2beta3.Task.View.BASIC]; not all
            information is retrieved by default because some data, such
            as payloads, might be desirable to return only when needed
            because of its large size or because of the sensitivity of
            data that it contains.

            Authorization for
            [FULL][google.cloud.tasks.v2beta3.Task.View.FULL] requires
            ``cloudtasks.tasks.fullView`` `Google
            IAM <https://cloud.google.com/iam/>`__ permission on the
            [Task][google.cloud.tasks.v2beta3.Task] resource.
        page_size (int):
            Maximum page size.

            Fewer tasks than requested might be returned, even if more
            tasks exist; use
            [next_page_token][google.cloud.tasks.v2beta3.ListTasksResponse.next_page_token]
            in the response to determine if more tasks exist.

            The maximum page size is 1000. If unspecified, the page size
            will be the maximum.
        page_token (str):
            A token identifying the page of results to return.

            To request the first page results, page_token must be empty.
            To request the next page of results, page_token must be the
            value of
            [next_page_token][google.cloud.tasks.v2beta3.ListTasksResponse.next_page_token]
            returned from the previous call to
            [ListTasks][google.cloud.tasks.v2beta3.CloudTasks.ListTasks]
            method.

            The page token is valid for only 2 hours.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    response_view: gct_task.Task.View = proto.Field(
        proto.ENUM,
        number=2,
        enum=gct_task.Task.View,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListTasksResponse(proto.Message):
    r"""Response message for listing tasks using
    [ListTasks][google.cloud.tasks.v2beta3.CloudTasks.ListTasks].

    Attributes:
        tasks (MutableSequence[google.cloud.tasks_v2beta3.types.Task]):
            The list of tasks.
        next_page_token (str):
            A token to retrieve next page of results.

            To return the next page of results, call
            [ListTasks][google.cloud.tasks.v2beta3.CloudTasks.ListTasks]
            with this value as the
            [page_token][google.cloud.tasks.v2beta3.ListTasksRequest.page_token].

            If the next_page_token is empty, there are no more results.
    """

    @property
    def raw_page(self):
        return self

    tasks: MutableSequence[gct_task.Task] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gct_task.Task,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetTaskRequest(proto.Message):
    r"""Request message for getting a task using
    [GetTask][google.cloud.tasks.v2beta3.CloudTasks.GetTask].

    Attributes:
        name (str):
            Required. The task name. For example:
            ``projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID``
        response_view (google.cloud.tasks_v2beta3.types.Task.View):
            The response_view specifies which subset of the
            [Task][google.cloud.tasks.v2beta3.Task] will be returned.

            By default response_view is
            [BASIC][google.cloud.tasks.v2beta3.Task.View.BASIC]; not all
            information is retrieved by default because some data, such
            as payloads, might be desirable to return only when needed
            because of its large size or because of the sensitivity of
            data that it contains.

            Authorization for
            [FULL][google.cloud.tasks.v2beta3.Task.View.FULL] requires
            ``cloudtasks.tasks.fullView`` `Google
            IAM <https://cloud.google.com/iam/>`__ permission on the
            [Task][google.cloud.tasks.v2beta3.Task] resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    response_view: gct_task.Task.View = proto.Field(
        proto.ENUM,
        number=2,
        enum=gct_task.Task.View,
    )


class CreateTaskRequest(proto.Message):
    r"""Request message for
    [CreateTask][google.cloud.tasks.v2beta3.CloudTasks.CreateTask].

    Attributes:
        parent (str):
            Required. The queue name. For example:
            ``projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID``

            The queue must already exist.
        task (google.cloud.tasks_v2beta3.types.Task):
            Required. The task to add.

            Task names have the following format:
            ``projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID``.
            The user can optionally specify a task
            [name][google.cloud.tasks.v2beta3.Task.name]. If a name is
            not specified then the system will generate a random unique
            task id, which will be set in the task returned in the
            [response][google.cloud.tasks.v2beta3.Task.name].

            If
            [schedule_time][google.cloud.tasks.v2beta3.Task.schedule_time]
            is not set or is in the past then Cloud Tasks will set it to
            the current time.

            Task De-duplication:

            Explicitly specifying a task ID enables task de-duplication.
            If a task's ID is identical to that of an existing task or a
            task that was deleted or executed recently then the call
            will fail with
            [ALREADY_EXISTS][google.rpc.Code.ALREADY_EXISTS]. The IDs of
            deleted tasks are not immediately available for reuse. It
            can take up to 24 hours (or 9 days if the task's queue was
            created using a queue.yaml or queue.xml) for the task ID to
            be released and made available again.

            Because there is an extra lookup cost to identify duplicate
            task names, these
            [CreateTask][google.cloud.tasks.v2beta3.CloudTasks.CreateTask]
            calls have significantly increased latency. Using hashed
            strings for the task id or for the prefix of the task id is
            recommended. Choosing task ids that are sequential or have
            sequential prefixes, for example using a timestamp, causes
            an increase in latency and error rates in all task commands.
            The infrastructure relies on an approximately uniform
            distribution of task ids to store and serve tasks
            efficiently.
        response_view (google.cloud.tasks_v2beta3.types.Task.View):
            The response_view specifies which subset of the
            [Task][google.cloud.tasks.v2beta3.Task] will be returned.

            By default response_view is
            [BASIC][google.cloud.tasks.v2beta3.Task.View.BASIC]; not all
            information is retrieved by default because some data, such
            as payloads, might be desirable to return only when needed
            because of its large size or because of the sensitivity of
            data that it contains.

            Authorization for
            [FULL][google.cloud.tasks.v2beta3.Task.View.FULL] requires
            ``cloudtasks.tasks.fullView`` `Google
            IAM <https://cloud.google.com/iam/>`__ permission on the
            [Task][google.cloud.tasks.v2beta3.Task] resource.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    task: gct_task.Task = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gct_task.Task,
    )
    response_view: gct_task.Task.View = proto.Field(
        proto.ENUM,
        number=3,
        enum=gct_task.Task.View,
    )


class BatchCreateTasksRequest(proto.Message):
    r"""Request message for [BatchCreateTasks].

    Attributes:
        parent (str):
            Required. The queue name. For example:
            ``projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID``

            The queue must already exist.
        requests (MutableSequence[google.cloud.tasks_v2beta3.types.CreateTaskRequest]):
            Required. The list of requests to create
            tasks. The queue specified in parent field of
            each CreateTaskRequest will be the same. This
            validation happens on the client side as well as
            in the handler.
            BatchCreateTasksRequest.parent will also be the
            same value as the individual
            CreateTaskRequest.parent .
            The maximum number of requests is 100.
        request_id (str):
            Optional. This field will be used to identify
            the long running operation, avoiding duplication
            when user retries. If not provided, then a UUID
            will be generated at server side.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreateTaskRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CreateTaskRequest",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteTaskRequest(proto.Message):
    r"""Request message for deleting a task using
    [DeleteTask][google.cloud.tasks.v2beta3.CloudTasks.DeleteTask].

    Attributes:
        name (str):
            Required. The task name. For example:
            ``projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class BatchDeleteTasksRequest(proto.Message):
    r"""Request message for deleting a batch of tasks using
    [BatchDeleteTasks][google.cloud.tasks.v2beta3.CloudTasks.BatchDeleteTasks].

    Attributes:
        parent (str):
            Required. The queue name. For example: Format:
            ``projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID``
        names (MutableSequence[str]):
            Required. The names of the tasks to delete. A maximum of
            1000 tasks can be deleted in a batch. For example: Format:
            ``projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID``
        request_id (str):
            Optional. This field will be used to identify
            the long running operation, avoiding duplication
            when user retries. If not provided, then a UUID
            will be generated at server side.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class BatchDeleteTasksMetadata(proto.Message):
    r"""Metadata for the long-running operation returned by
    [BatchDeleteTasks][google.cloud.tasks.v2beta3.CloudTasks.BatchDeleteTasks].
    This message is used to hold metadata information about the batch
    delete tasks operation; that is, it is put in
    [google.longrunning.Operation.metadata][google.longrunning.Operation.metadata].

    Attributes:
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the batch delete
            started.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the batch delete
            finished.
        state (google.cloud.tasks_v2beta3.types.BatchDeleteTasksMetadata.State):
            Output only. The state of the batch delete
            operation.
        failed_requests (MutableMapping[int, google.rpc.status_pb2.Status]):
            Output only. A map of failed requests, where
            the key is the index of the request in
            BatchDeleteTasksRequest.names and the value is
            the error status.
    """

    class State(proto.Enum):
        r"""The state of the batch delete operation.
        This enum is not frozen and new values may be added in the
        future.

        Values:
            STATE_UNSPECIFIED (0):
                The default value. This value is used if the
                state is omitted.
            RUNNING (1):
                The batch delete is running.
            SUCCEEDED (2):
                The batch delete has finished and all tasks
                were successfully deleted.
            PARTIALLY_SUCCEEDED (3):
                The batch delete has finished with partial success. The
                tasks that failed to be deleted are reported in
                [failed_requests][google.cloud.tasks.v2beta3.BatchDeleteTasksMetadata.failed_requests].
                When all requests in the batch fail,
                [google.longrunning.Operation.error][google.longrunning.Operation.error]
                will be set with ``code`` = ``google.rpc.Code.ABORTED`` and
                ``message`` = "None of the requests succeeded, refer to
                BatchDeleteTasksMetadata.failed_requests for individual
                error details".
            FAILED (4):
                The batch delete has failed.
                This means the overall batch delete operation
                failed to complete. This can happen due to an
                internal error preventing the operation from
                finishing.
        """

        STATE_UNSPECIFIED = 0
        RUNNING = 1
        SUCCEEDED = 2
        PARTIALLY_SUCCEEDED = 3
        FAILED = 4

    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )
    failed_requests: MutableMapping[int, status_pb2.Status] = proto.MapField(
        proto.INT32,
        proto.MESSAGE,
        number=4,
        message=status_pb2.Status,
    )


class RunTaskRequest(proto.Message):
    r"""Request message for forcing a task to run now using
    [RunTask][google.cloud.tasks.v2beta3.CloudTasks.RunTask].

    Attributes:
        name (str):
            Required. The task name. For example:
            ``projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID``
        response_view (google.cloud.tasks_v2beta3.types.Task.View):
            The response_view specifies which subset of the
            [Task][google.cloud.tasks.v2beta3.Task] will be returned.

            By default response_view is
            [BASIC][google.cloud.tasks.v2beta3.Task.View.BASIC]; not all
            information is retrieved by default because some data, such
            as payloads, might be desirable to return only when needed
            because of its large size or because of the sensitivity of
            data that it contains.

            Authorization for
            [FULL][google.cloud.tasks.v2beta3.Task.View.FULL] requires
            ``cloudtasks.tasks.fullView`` `Google
            IAM <https://cloud.google.com/iam/>`__ permission on the
            [Task][google.cloud.tasks.v2beta3.Task] resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    response_view: gct_task.Task.View = proto.Field(
        proto.ENUM,
        number=2,
        enum=gct_task.Task.View,
    )


class BatchCreateTasksResponse(proto.Message):
    r"""Response message for [BatchCreateTasks].

    Attributes:
        tasks (MutableSequence[google.cloud.tasks_v2beta3.types.Task]):
            The tasks that were successfully created.
    """

    tasks: MutableSequence[gct_task.Task] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gct_task.Task,
    )


class BatchCreateTasksMetadata(proto.Message):
    r"""Metadata message for [BatchCreateTasks].

    Attributes:
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the batch create started.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the batch create finished.
        state (google.cloud.tasks_v2beta3.types.BatchCreateTasksMetadata.State):
            Output only. The state of the batch create
            operation.
        failed_requests (MutableMapping[int, google.rpc.status_pb2.Status]):
            A map of failed requests, where the key is
            the index of the request in
            BatchCreateTasksRequest.requests and the value
            is the error status.
    """

    class State(proto.Enum):
        r"""The state of the batch create operation.

        Values:
            STATE_UNSPECIFIED (0):
                The default value. This value is used if the
                state is omitted.
            RUNNING (1):
                The batch create is running.
            SUCCEEDED (2):
                The batch create has finished.
                All tasks in the request were successfully
                created.
            PARTIALLY_SUCCEEDED (5):
                The batch create has finished with partial success. The
                tasks that failed to be created are reported in
                [failed_requests][google.cloud.tasks.v2beta3.BatchCreateTasksMetadata.failed_requests].
            FAILED (3):
                The batch create has failed.
                This means the overall batch create operation
                failed to complete. This can happen due to an
                internal error preventing the operation from
                finishing.
            CANCELLED (4):
                The batch create was cancelled.
        """

        STATE_UNSPECIFIED = 0
        RUNNING = 1
        SUCCEEDED = 2
        PARTIALLY_SUCCEEDED = 5
        FAILED = 3
        CANCELLED = 4

    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )
    failed_requests: MutableMapping[int, status_pb2.Status] = proto.MapField(
        proto.INT32,
        proto.MESSAGE,
        number=4,
        message=status_pb2.Status,
    )


class UpdateCmekConfigRequest(proto.Message):
    r"""Request message for
    [UpdateCmekConfig][google.cloud.tasks.v2beta3.CloudTasks.UpdateCmekConfig].

    Attributes:
        cmek_config (google.cloud.tasks_v2beta3.types.CmekConfig):
            Required. The config to update.  Its name
            attribute distinguishes it.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            List of fields to be updated in this request.
    """

    cmek_config: gct_cmek_config.CmekConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gct_cmek_config.CmekConfig,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class GetCmekConfigRequest(proto.Message):
    r"""Request message for
    [GetCmekConfig][google.cloud.tasks.v2beta3.CloudTasks.GetCmekConfig].

    Attributes:
        name (str):
            Required. The config resource name. For example:
            projects/PROJECT_ID/locations/LOCATION_ID/cmekConfig\`
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
