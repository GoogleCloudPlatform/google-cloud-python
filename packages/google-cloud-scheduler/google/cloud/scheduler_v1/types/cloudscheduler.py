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
import proto  # type: ignore

from google.cloud.scheduler_v1.types import job as gcs_job

__protobuf__ = proto.module(
    package="google.cloud.scheduler.v1",
    manifest={
        "ListJobsRequest",
        "ListJobsResponse",
        "GetJobRequest",
        "CreateJobRequest",
        "UpdateJobRequest",
        "DeleteJobRequest",
        "PauseJobRequest",
        "ResumeJobRequest",
        "RunJobRequest",
    },
)


class ListJobsRequest(proto.Message):
    r"""Request message for listing jobs using
    [ListJobs][google.cloud.scheduler.v1.CloudScheduler.ListJobs].

    Attributes:
        parent (str):
            Required. The location name. For example:
            ``projects/PROJECT_ID/locations/LOCATION_ID``.
        page_size (int):
            Requested page size.

            The maximum page size is 500. If unspecified, the page size
            will be the maximum. Fewer jobs than requested might be
            returned, even if more jobs exist; use next_page_token to
            determine if more jobs exist.
        page_token (str):
            A token identifying a page of results the server will
            return. To request the first page results, page_token must
            be empty. To request the next page of results, page_token
            must be the value of
            [next_page_token][google.cloud.scheduler.v1.ListJobsResponse.next_page_token]
            returned from the previous call to
            [ListJobs][google.cloud.scheduler.v1.CloudScheduler.ListJobs].
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=5,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=6,
    )


class ListJobsResponse(proto.Message):
    r"""Response message for listing jobs using
    [ListJobs][google.cloud.scheduler.v1.CloudScheduler.ListJobs].

    Attributes:
        jobs (MutableSequence[google.cloud.scheduler_v1.types.Job]):
            The list of jobs.
        next_page_token (str):
            A token to retrieve next page of results. Pass this value in
            the
            [page_token][google.cloud.scheduler.v1.ListJobsRequest.page_token]
            field in the subsequent call to
            [ListJobs][google.cloud.scheduler.v1.CloudScheduler.ListJobs]
            to retrieve the next page of results. If this is empty it
            indicates that there are no more results through which to
            paginate.

            The page token is valid for only 2 hours.
    """

    @property
    def raw_page(self):
        return self

    jobs: MutableSequence[gcs_job.Job] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcs_job.Job,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetJobRequest(proto.Message):
    r"""Request message for
    [GetJob][google.cloud.scheduler.v1.CloudScheduler.GetJob].

    Attributes:
        name (str):
            Required. The job name. For example:
            ``projects/PROJECT_ID/locations/LOCATION_ID/jobs/JOB_ID``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateJobRequest(proto.Message):
    r"""Request message for
    [CreateJob][google.cloud.scheduler.v1.CloudScheduler.CreateJob].

    Attributes:
        parent (str):
            Required. The location name. For example:
            ``projects/PROJECT_ID/locations/LOCATION_ID``.
        job (google.cloud.scheduler_v1.types.Job):
            Required. The job to add. The user can optionally specify a
            name for the job in
            [name][google.cloud.scheduler.v1.Job.name].
            [name][google.cloud.scheduler.v1.Job.name] cannot be the
            same as an existing job. If a name is not specified then the
            system will generate a random unique name that will be
            returned ([name][google.cloud.scheduler.v1.Job.name]) in the
            response.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    job: gcs_job.Job = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcs_job.Job,
    )


class UpdateJobRequest(proto.Message):
    r"""Request message for
    [UpdateJob][google.cloud.scheduler.v1.CloudScheduler.UpdateJob].

    Attributes:
        job (google.cloud.scheduler_v1.types.Job):
            Required. The new job properties.
            [name][google.cloud.scheduler.v1.Job.name] must be
            specified.

            Output only fields cannot be modified using UpdateJob. Any
            value specified for an output only field will be ignored.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            A  mask used to specify which fields of the
            job are being updated.
    """

    job: gcs_job.Job = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcs_job.Job,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteJobRequest(proto.Message):
    r"""Request message for deleting a job using
    [DeleteJob][google.cloud.scheduler.v1.CloudScheduler.DeleteJob].

    Attributes:
        name (str):
            Required. The job name. For example:
            ``projects/PROJECT_ID/locations/LOCATION_ID/jobs/JOB_ID``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class PauseJobRequest(proto.Message):
    r"""Request message for
    [PauseJob][google.cloud.scheduler.v1.CloudScheduler.PauseJob].

    Attributes:
        name (str):
            Required. The job name. For example:
            ``projects/PROJECT_ID/locations/LOCATION_ID/jobs/JOB_ID``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ResumeJobRequest(proto.Message):
    r"""Request message for
    [ResumeJob][google.cloud.scheduler.v1.CloudScheduler.ResumeJob].

    Attributes:
        name (str):
            Required. The job name. For example:
            ``projects/PROJECT_ID/locations/LOCATION_ID/jobs/JOB_ID``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class RunJobRequest(proto.Message):
    r"""Request message for forcing a job to run now using
    [RunJob][google.cloud.scheduler.v1.CloudScheduler.RunJob].

    Attributes:
        name (str):
            Required. The job name. For example:
            ``projects/PROJECT_ID/locations/LOCATION_ID/jobs/JOB_ID``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
