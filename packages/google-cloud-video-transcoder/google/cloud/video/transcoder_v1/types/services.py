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

import proto  # type: ignore

from google.cloud.video.transcoder_v1.types import resources

__protobuf__ = proto.module(
    package="google.cloud.video.transcoder.v1",
    manifest={
        "CreateJobRequest",
        "ListJobsRequest",
        "GetJobRequest",
        "DeleteJobRequest",
        "ListJobsResponse",
        "CreateJobTemplateRequest",
        "ListJobTemplatesRequest",
        "GetJobTemplateRequest",
        "DeleteJobTemplateRequest",
        "ListJobTemplatesResponse",
    },
)


class CreateJobRequest(proto.Message):
    r"""Request message for ``TranscoderService.CreateJob``.

    Attributes:
        parent (str):
            Required. The parent location to create and process this
            job. Format: ``projects/{project}/locations/{location}``
        job (google.cloud.video.transcoder_v1.types.Job):
            Required. Parameters for creating transcoding
            job.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    job: resources.Job = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.Job,
    )


class ListJobsRequest(proto.Message):
    r"""Request message for ``TranscoderService.ListJobs``. The parent
    location from which to retrieve the collection of jobs.

    Attributes:
        parent (str):
            Required. Format:
            ``projects/{project}/locations/{location}``
        page_size (int):
            The maximum number of items to return.
        page_token (str):
            The ``next_page_token`` value returned from a previous List
            request, if any.
        filter (str):
            The filter expression, following the syntax
            outlined in https://google.aip.dev/160.
        order_by (str):
            One or more fields to compare and use to sort
            the output. See
            https://google.aip.dev/132#ordering.
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


class GetJobRequest(proto.Message):
    r"""Request message for ``TranscoderService.GetJob``.

    Attributes:
        name (str):
            Required. The name of the job to retrieve. Format:
            ``projects/{project}/locations/{location}/jobs/{job}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteJobRequest(proto.Message):
    r"""Request message for ``TranscoderService.DeleteJob``.

    Attributes:
        name (str):
            Required. The name of the job to delete. Format:
            ``projects/{project}/locations/{location}/jobs/{job}``
        allow_missing (bool):
            If set to true, and the job is not found, the
            request will succeed but no action will be taken
            on the server.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class ListJobsResponse(proto.Message):
    r"""Response message for ``TranscoderService.ListJobs``.

    Attributes:
        jobs (MutableSequence[google.cloud.video.transcoder_v1.types.Job]):
            List of jobs in the specified region.
        next_page_token (str):
            The pagination token.
        unreachable (MutableSequence[str]):
            List of regions that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    jobs: MutableSequence[resources.Job] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Job,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class CreateJobTemplateRequest(proto.Message):
    r"""Request message for ``TranscoderService.CreateJobTemplate``.

    Attributes:
        parent (str):
            Required. The parent location to create this job template.
            Format: ``projects/{project}/locations/{location}``
        job_template (google.cloud.video.transcoder_v1.types.JobTemplate):
            Required. Parameters for creating job
            template.
        job_template_id (str):
            Required. The ID to use for the job template, which will
            become the final component of the job template's resource
            name.

            This value should be 4-63 characters, and valid characters
            must match the regular expression
            ``[a-zA-Z][a-zA-Z0-9_-]*``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    job_template: resources.JobTemplate = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.JobTemplate,
    )
    job_template_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListJobTemplatesRequest(proto.Message):
    r"""Request message for ``TranscoderService.ListJobTemplates``.

    Attributes:
        parent (str):
            Required. The parent location from which to retrieve the
            collection of job templates. Format:
            ``projects/{project}/locations/{location}``
        page_size (int):
            The maximum number of items to return.
        page_token (str):
            The ``next_page_token`` value returned from a previous List
            request, if any.
        filter (str):
            The filter expression, following the syntax
            outlined in https://google.aip.dev/160.
        order_by (str):
            One or more fields to compare and use to sort
            the output. See
            https://google.aip.dev/132#ordering.
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


class GetJobTemplateRequest(proto.Message):
    r"""Request message for ``TranscoderService.GetJobTemplate``.

    Attributes:
        name (str):
            Required. The name of the job template to retrieve. Format:
            ``projects/{project}/locations/{location}/jobTemplates/{job_template}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteJobTemplateRequest(proto.Message):
    r"""Request message for ``TranscoderService.DeleteJobTemplate``.

    Attributes:
        name (str):
            Required. The name of the job template to delete.
            ``projects/{project}/locations/{location}/jobTemplates/{job_template}``
        allow_missing (bool):
            If set to true, and the job template is not
            found, the request will succeed but no action
            will be taken on the server.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class ListJobTemplatesResponse(proto.Message):
    r"""Response message for ``TranscoderService.ListJobTemplates``.

    Attributes:
        job_templates (MutableSequence[google.cloud.video.transcoder_v1.types.JobTemplate]):
            List of job templates in the specified
            region.
        next_page_token (str):
            The pagination token.
        unreachable (MutableSequence[str]):
            List of regions that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    job_templates: MutableSequence[resources.JobTemplate] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.JobTemplate,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
