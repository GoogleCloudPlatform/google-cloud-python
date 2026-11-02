# Copyright 2015 Google LLC
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

import unittest

from google.api_core import exceptions

from ..helpers import make_connection, make_client as __make_client


def _make_client(project="test-project", connection=None):
    client = __make_client(project)
    if connection is None:
        connection = make_connection()

    client._connection = connection
    return client


def _make_retriable_exception():
    return exceptions.TooManyRequests(
        "retriable exception", errors=[{"reason": "rateLimitExceeded"}]
    )


def _make_job_resource(
    creation_time_ms=1437767599006,
    started_time_ms=1437767600007,
    ended_time_ms=1437767601008,
    started=False,
    ended=False,
    etag="abc-def-hjk",
    endpoint="https://bigquery.googleapis.com",
    job_type="load",
    job_id="a-random-id",
    location="US",
    project_id="some-project",
    user_email="bq-user@example.com",
):
    resource = {
        "status": {"state": "PENDING"},
        "configuration": {job_type: {}},
        "statistics": {"creationTime": creation_time_ms, job_type: {}},
        "etag": etag,
        "id": "{}:{}".format(project_id, job_id),
        "jobReference": {
            "projectId": project_id,
            "jobId": job_id,
            "location": location,
        },
        "selfLink": "{}/bigquery/v2/projects/{}/jobs/{}".format(
            endpoint, project_id, job_id
        ),
        "user_email": user_email,
    }

    if started or ended:
        resource["statistics"]["startTime"] = started_time_ms
        resource["status"]["state"] = "RUNNING"

    if ended:
        resource["statistics"]["endTime"] = ended_time_ms
        resource["status"]["state"] = "DONE"

    if job_type == "query":
        resource["configuration"]["query"]["destinationTable"] = {
            "projectId": project_id,
            "datasetId": "_temp_dataset",
            "tableId": "_temp_table",
        }

    return resource


class _Base(unittest.TestCase):
    from google.cloud.bigquery.dataset import DatasetReference
    from google.cloud.bigquery.table import TableReference

    ENDPOINT = "https://bigquery.googleapis.com"
    PROJECT = "project"
    SOURCE1 = "http://example.com/source1.csv"
    DS_ID = "dataset_id"
    DS_REF = DatasetReference(PROJECT, DS_ID)
    TABLE_ID = "table_id"
    TABLE_REF = TableReference(DS_REF, TABLE_ID)
    JOB_ID = "JOB_ID"
    JOB_TYPE = "unknown"
    KMS_KEY_NAME = "projects/1/locations/us/keyRings/1/cryptoKeys/1"

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def _setUpConstants(self):
        import datetime
        from google.cloud._helpers import UTC

        self.WHEN_TS = 1437767599.006
        self.WHEN = datetime.datetime.fromtimestamp(self.WHEN_TS, UTC).replace(
            tzinfo=UTC
        )
        self.ETAG = "ETAG"
        self.FULL_JOB_ID = "%s:%s" % (self.PROJECT, self.JOB_ID)
        self.RESOURCE_URL = "{}/bigquery/v2/projects/{}/jobs/{}".format(
            self.ENDPOINT, self.PROJECT, self.JOB_ID
        )
        self.USER_EMAIL = "phred@example.com"

    def _table_ref(self, table_id):
        from google.cloud.bigquery.table import TableReference

        return TableReference(self.DS_REF, table_id)

    def _make_resource(self, started=False, ended=False, location="US"):
        self._setUpConstants()
        return _make_job_resource(
            creation_time_ms=int(self.WHEN_TS * 1000),
            started_time_ms=int(self.WHEN_TS * 1000),
            ended_time_ms=int(self.WHEN_TS * 1000) + 1000000,
            started=started,
            ended=ended,
            etag=self.ETAG,
            endpoint=self.ENDPOINT,
            job_type=self.JOB_TYPE,
            job_id=self.JOB_ID,
            project_id=self.PROJECT,
            user_email=self.USER_EMAIL,
            location=location,
        )

    def _verifyInitialReadonlyProperties(self, job):
        # root elements of resource
        self.assertIsNone(job.etag)
        self.assertIsNone(job.self_link)
        self.assertIsNone(job.user_email)

        # derived from resource['statistics']
        self.assertIsNone(job.created)
        self.assertIsNone(job.started)
        self.assertIsNone(job.ended)
        self.assertIsNone(job.transaction_info)

        # derived from resource['status']
        self.assertIsNone(job.error_result)
        self.assertIsNone(job.errors)
        self.assertIsNone(job.state)

    def _verifyReadonlyResourceProperties(self, job, resource):
        from datetime import timedelta

        statistics = resource.get("statistics", {})

        if "creationTime" in statistics:
            self.assertEqual(job.created, self.WHEN)
        else:
            self.assertIsNone(job.created)

        if "startTime" in statistics:
            self.assertEqual(job.started, self.WHEN)
        else:
            self.assertIsNone(job.started)

        if "endTime" in statistics:
            self.assertEqual(job.ended, self.WHEN + timedelta(seconds=1000))
        else:
            self.assertIsNone(job.ended)

        if "etag" in resource:
            self.assertEqual(job.etag, self.ETAG)
        else:
            self.assertIsNone(job.etag)

        if "selfLink" in resource:
            self.assertEqual(job.self_link, self.RESOURCE_URL)
        else:
            self.assertIsNone(job.self_link)

        if "user_email" in resource:
            self.assertEqual(job.user_email, self.USER_EMAIL)
        else:
            self.assertIsNone(job.user_email)
