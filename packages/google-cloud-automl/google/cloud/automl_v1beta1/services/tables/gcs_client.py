# -*- coding: utf-8 -*-
#
# Copyright 2019 Google LLC
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

"""Wraps the Google Cloud Storage client library for use in tables helper."""

import logging
import time

from google.api_core import exceptions

try:
    import pandas
except ImportError:  # pragma: NO COVER
    pandas = None  # type: ignore[assignment]

try:
    # TODO(https://github.com/googleapis/python-storage/issues/318):
    # Remove `type: ignore` once this bug is fixed
    from google.cloud import storage  # type: ignore[attr-defined]
except ImportError:  # pragma: NO COVER
    storage = None  # type: ignore[assignment]

_LOGGER = logging.getLogger(__name__)
_PANDAS_REQUIRED = "pandas is required to verify type DataFrame."
_STORAGE_REQUIRED = (
    "google-cloud-storage is required to create a Google Cloud Storage client."
)


class GcsClient(object):
    """Uploads Pandas DataFrame to a bucket in Google Cloud Storage."""

    def __init__(self, bucket_name=None, client=None, credentials=None, project=None):
        """Constructor.

        Args:
            bucket_name (Optional[str]): The name of Google Cloud Storage
                bucket for this client to send requests to.
            client (Optional[storage.Client]): A Google Cloud Storage Client
                instance.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            project (Optional[str]): The project ID of the GCP project to
                attach to the underlying storage client. If none is specified,
                the client will attempt to ascertain the credentials from the
                environment.
        """
        if storage is None:
            raise ImportError(_STORAGE_REQUIRED)

        if client is not None:
            self.client = client
        elif credentials is not None:
            self.client = storage.Client(credentials=credentials, project=project)
        else:
            self.client = storage.Client()

        self.bucket_name = bucket_name

    def ensure_bucket_exists(self, project, region):
        """Checks if a bucket named '{project}-automl-tables-staging' exists.

        If this bucket doesn't exist, creates one.
        If this bucket already exists in `project`, do nothing.
        If this bucket exists in a different project that we don't have
        access to, creates a bucket named
        '{project}-automl-tables-staging-{create_timestamp}' because bucket's
        name must be globally unique.
        Save the created bucket's name and reuse this for future requests.

        Args:
            project (str): The ID of the project that stores the bucket.
            region (str): The region of the bucket.

        Returns:
            A string representing the created bucket name.
        """
        if self.bucket_name is None:
            self.bucket_name = "{}-automl-tables-staging".format(project)

        try:
            self.client.get_bucket(self.bucket_name)
        except (exceptions.Forbidden, exceptions.NotFound) as e:
            if isinstance(e, exceptions.Forbidden):
                used_bucket_name = self.bucket_name
                self.bucket_name = used_bucket_name + "-{}".format(int(time.time()))
                _LOGGER.warning(
                    "Created a bucket named {} because a bucket named {} already exists in a different project.".format(
                        self.bucket_name, used_bucket_name
                    )
                )

            bucket = self.client.bucket(self.bucket_name)
            bucket.create(project=project, location=region)

        return self.bucket_name

    def upload_pandas_dataframe(self, dataframe, uploaded_csv_name=None):
        """Uploads a Pandas DataFrame as CSV to the bucket.

        Args:
            dataframe (pandas.DataFrame): The Pandas Dataframe to be uploaded.
            uploaded_csv_name (Optional[str]): The name for the uploaded CSV.

        Returns:
            A string representing the GCS URI of the uploaded CSV.
        """
        if pandas is None:
            raise ImportError(_PANDAS_REQUIRED)

        if not isinstance(dataframe, pandas.DataFrame):
            raise ValueError("'dataframe' must be a pandas.DataFrame instance.")

        if self.bucket_name is None:
            raise ValueError("Must ensure a bucket exists before uploading data.")

        if uploaded_csv_name is None:
            uploaded_csv_name = "automl-tables-dataframe-{}.csv".format(
                int(time.time())
            )

        # Setting index to False to ignore exporting the data index:
        # 1. The resulting column name for the index column is empty, AutoML
        # Tables does not allow empty column name
        # 2. The index is not an useful training information
        csv_string = dataframe.to_csv(index=False)

        bucket = self.client.get_bucket(self.bucket_name)
        blob = bucket.blob(uploaded_csv_name)
        blob.upload_from_string(csv_string)

        return "gs://{}/{}".format(self.bucket_name, uploaded_csv_name)
