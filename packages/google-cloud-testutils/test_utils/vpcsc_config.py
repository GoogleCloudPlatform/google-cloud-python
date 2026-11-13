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

import os

import pytest  # type: ignore

INSIDE_VPCSC_ENVVAR = "GOOGLE_CLOUD_TESTS_IN_VPCSC"
PROJECT_INSIDE_ENVVAR = "PROJECT_ID"
PROJECT_OUTSIDE_ENVVAR = "GOOGLE_CLOUD_TESTS_VPCSC_OUTSIDE_PERIMETER_PROJECT"
BUCKET_OUTSIDE_ENVVAR = "GOOGLE_CLOUD_TESTS_VPCSC_OUTSIDE_PERIMETER_BUCKET"


class VPCSCTestConfig(object):
    """System test utility for VPCSC detection.

    See: https://cloud.google.com/vpc-service-controls/docs/
    """

    @property
    def inside_vpcsc(self):
        """Test whether the test environment is configured to run inside VPCSC.

        Returns:
            bool:
                true if the environment is configured to run inside VPCSC,
                else false.
        """
        return INSIDE_VPCSC_ENVVAR in os.environ

    @property
    def project_inside(self):
        """Project ID for testing outside access.

        Returns:
            str: project ID used for testing outside access; None if undefined.
        """
        return os.environ.get(PROJECT_INSIDE_ENVVAR, None)

    @property
    def project_outside(self):
        """Project ID for testing inside access.

        Returns:
            str: project ID used for testing inside access; None if undefined.
        """
        return os.environ.get(PROJECT_OUTSIDE_ENVVAR, None)

    @property
    def bucket_outside(self):
        """GCS bucket for testing inside access.

        Returns:
            str: bucket ID used for testing inside access; None if undefined.
        """
        return os.environ.get(BUCKET_OUTSIDE_ENVVAR, None)

    def skip_if_inside_vpcsc(self, testcase):
        """Test decorator: skip if running inside VPCSC."""
        reason = (
            "Running inside VPCSC.  "
            "Unset the {} environment variable to enable this test."
        ).format(INSIDE_VPCSC_ENVVAR)
        skip = pytest.mark.skipif(self.inside_vpcsc, reason=reason)
        return skip(testcase)

    def skip_unless_inside_vpcsc(self, testcase):
        """Test decorator: skip if running outside VPCSC."""
        reason = (
            "Running outside VPCSC.  "
            "Set the {} environment variable to enable this test."
        ).format(INSIDE_VPCSC_ENVVAR)
        skip = pytest.mark.skipif(not self.inside_vpcsc, reason=reason)
        return skip(testcase)

    def skip_unless_inside_project(self, testcase):
        """Test decorator: skip if inside project env var not set."""
        reason = (
            "Project ID for running inside VPCSC not set.  "
            "Set the {} environment variable to enable this test."
        ).format(PROJECT_INSIDE_ENVVAR)
        skip = pytest.mark.skipif(self.project_inside is None, reason=reason)
        return skip(testcase)

    def skip_unless_outside_project(self, testcase):
        """Test decorator: skip if outside project env var not set."""
        reason = (
            "Project ID for running outside VPCSC not set. "
            "Set the {} environment variable to enable this test."
        ).format(PROJECT_OUTSIDE_ENVVAR)
        skip = pytest.mark.skipif(self.project_outside is None, reason=reason)
        return skip(testcase)

    def skip_unless_outside_bucket(self, testcase):
        """Test decorator: skip if outside bucket env var not set."""
        reason = (
            "Bucket ID for running outside VPCSC not set. "
            "Set the {} environment variable to enable this test."
        ).format(BUCKET_OUTSIDE_ENVVAR)
        skip = pytest.mark.skipif(self.bucket_outside is None, reason=reason)
        return skip(testcase)


vpcsc_config = VPCSCTestConfig()
