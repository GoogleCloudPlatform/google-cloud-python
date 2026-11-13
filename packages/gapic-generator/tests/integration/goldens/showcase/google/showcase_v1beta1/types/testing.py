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


__protobuf__ = proto.module(
    package='google.showcase.v1beta1',
    manifest={
        'Session',
        'CreateSessionRequest',
        'GetSessionRequest',
        'ListSessionsRequest',
        'ListSessionsResponse',
        'DeleteSessionRequest',
        'ReportSessionRequest',
        'ReportSessionResponse',
        'Test',
        'Issue',
        'ListTestsRequest',
        'ListTestsResponse',
        'TestRun',
        'DeleteTestRequest',
        'VerifyTestRequest',
        'VerifyTestResponse',
    },
)


class Session(proto.Message):
    r"""A session is a suite of tests, generally being made in the
    context of testing code generation.

    A session defines tests it may expect, based on which version of
    the code generation spec is in use.

    Attributes:
        name (str):
            The name of the session. The ID must conform to ^[a-z]+$ If
            this is not provided, Showcase chooses one at random.
        version (google.showcase_v1beta1.types.Session.Version):
            Required. The version this session is using.
    """
    class Version(proto.Enum):
        r"""The specification versions understood by Showcase.

        Values:
            VERSION_UNSPECIFIED (0):
                Unspecified version. If passed on creation,
                the session will default to using the latest
                stable release.
            V1_LATEST (1):
                The latest v1. Currently, this is v1.0.
            V1_0 (2):
                v1.0. (Until the spec is "GA", this will be a
                moving target.)
        """
        VERSION_UNSPECIFIED = 0
        V1_LATEST = 1
        V1_0 = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    version: Version = proto.Field(
        proto.ENUM,
        number=2,
        enum=Version,
    )


class CreateSessionRequest(proto.Message):
    r"""The request for the CreateSession method.

    Attributes:
        session (google.showcase_v1beta1.types.Session):
            The session to be created.
            Sessions are immutable once they are created
            (although they can be deleted).
    """

    session: 'Session' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='Session',
    )


class GetSessionRequest(proto.Message):
    r"""The request for the GetSession method.

    Attributes:
        name (str):
            The session to be retrieved.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListSessionsRequest(proto.Message):
    r"""The request for the ListSessions method.

    Attributes:
        page_size (int):
            The maximum number of sessions to return per
            page.
        page_token (str):
            The page token, for retrieving subsequent
            pages.
    """

    page_size: int = proto.Field(
        proto.INT32,
        number=1,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListSessionsResponse(proto.Message):
    r"""Response for the ListSessions method.

    Attributes:
        sessions (MutableSequence[google.showcase_v1beta1.types.Session]):
            The sessions being returned.
        next_page_token (str):
            The next page token, if any.
            An empty value here means the last page has been
            reached.
    """

    @property
    def raw_page(self):
        return self

    sessions: MutableSequence['Session'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='Session',
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteSessionRequest(proto.Message):
    r"""Request for the DeleteSession method.

    Attributes:
        name (str):
            The session to be deleted.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ReportSessionRequest(proto.Message):
    r"""Request message for reporting on a session.

    Attributes:
        name (str):
            The session to be reported on.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ReportSessionResponse(proto.Message):
    r"""Response message for reporting on a session.

    Attributes:
        result (google.showcase_v1beta1.types.ReportSessionResponse.Result):
            The state of the report.
        test_runs (MutableSequence[google.showcase_v1beta1.types.TestRun]):
            The test runs of this session.
    """
    class Result(proto.Enum):
        r"""The topline state of the report.

        Values:
            RESULT_UNSPECIFIED (0):
                No description available.
            PASSED (1):
                The session is complete, and everything
                passed.
            FAILED (2):
                The session had an explicit failure.
            INCOMPLETE (3):
                The session is incomplete. This is a failure
                response.
        """
        RESULT_UNSPECIFIED = 0
        PASSED = 1
        FAILED = 2
        INCOMPLETE = 3

    result: Result = proto.Field(
        proto.ENUM,
        number=1,
        enum=Result,
    )
    test_runs: MutableSequence['TestRun'] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message='TestRun',
    )


class Test(proto.Message):
    r"""

    Attributes:
        name (str):
            The name of the test. The tests/\* portion of the names are
            hard-coded, and do not change from session to session.
        expectation_level (google.showcase_v1beta1.types.Test.ExpectationLevel):
            The expectation level for this test.
        description (str):
            A description of the test.
        blueprints (MutableSequence[google.showcase_v1beta1.types.Test.Blueprint]):
            The blueprints that will satisfy this test.
            There may be multiple blueprints that can signal
            to the server that this test case is being
            exercised. Although multiple blueprints are
            specified, only a single blueprint needs to be
            run to signal that the test case was exercised.
    """
    class ExpectationLevel(proto.Enum):
        r"""Whether or not a test is required, recommended, or optional.

        Values:
            EXPECTATION_LEVEL_UNSPECIFIED (0):
                No description available.
            REQUIRED (1):
                This test is strictly required.
            RECOMMENDED (2):
                This test is recommended.

                If a generator explicitly ignores a recommended test (see
                ``DeleteTest``), then the report may still pass, but with a
                warning.

                If a generator skips a recommended test and does not
                explicitly express that intention, the report will fail.
            OPTIONAL (3):
                This test is optional.

                If a generator explicitly ignores an optional test (see
                ``DeleteTest``), then the report may still pass, and no
                warning will be issued.

                If a generator skips an optional test and does not
                explicitly express that intention, the report may still
                pass, but with a warning.
        """
        EXPECTATION_LEVEL_UNSPECIFIED = 0
        REQUIRED = 1
        RECOMMENDED = 2
        OPTIONAL = 3

    class Blueprint(proto.Message):
        r"""A blueprint is an explicit definition of methods and requests
        that are needed to be made to test this specific test case.
        Ideally this would be represented by something more robust like
        CEL, but as of writing this, I am unsure if CEL is ready.

        Attributes:
            name (str):
                The name of this blueprint.
            description (str):
                A description of this blueprint.
            request (google.showcase_v1beta1.types.Test.Blueprint.Invocation):
                The initial request to trigger this test.
            additional_requests (MutableSequence[google.showcase_v1beta1.types.Test.Blueprint.Invocation]):
                An ordered list of method calls that can be
                called to trigger this test.
        """

        class Invocation(proto.Message):
            r"""A message representing a method invocation.

            Attributes:
                method (str):
                    The fully qualified name of the showcase
                    method to be invoked.
                serialized_request (bytes):
                    The request to be made if a specific request
                    is necessary.
            """

            method: str = proto.Field(
                proto.STRING,
                number=1,
            )
            serialized_request: bytes = proto.Field(
                proto.BYTES,
                number=2,
            )

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        description: str = proto.Field(
            proto.STRING,
            number=2,
        )
        request: 'Test.Blueprint.Invocation' = proto.Field(
            proto.MESSAGE,
            number=3,
            message='Test.Blueprint.Invocation',
        )
        additional_requests: MutableSequence['Test.Blueprint.Invocation'] = proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message='Test.Blueprint.Invocation',
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    expectation_level: ExpectationLevel = proto.Field(
        proto.ENUM,
        number=2,
        enum=ExpectationLevel,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    blueprints: MutableSequence[Blueprint] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=Blueprint,
    )


class Issue(proto.Message):
    r"""An issue found in the test.

    Attributes:
        type_ (google.showcase_v1beta1.types.Issue.Type):
            The type of the issue.
        severity (google.showcase_v1beta1.types.Issue.Severity):
            The severity of the issue.
        description (str):
            A description of the issue.
    """
    class Type(proto.Enum):
        r"""The different potential types of issues.

        Values:
            TYPE_UNSPECIFIED (0):
                No description available.
            SKIPPED (1):
                The test was never instrumented.
            PENDING (2):
                The test was started but never confirmed.
            INCORRECT_CONFIRMATION (3):
                The test was instrumented, but Showcase got
                an unexpected value when the generator tried to
                confirm success.
        """
        TYPE_UNSPECIFIED = 0
        SKIPPED = 1
        PENDING = 2
        INCORRECT_CONFIRMATION = 3

    class Severity(proto.Enum):
        r"""Severity levels.

        Values:
            SEVERITY_UNSPECIFIED (0):
                No description available.
            ERROR (1):
                Errors.
            WARNING (2):
                Warnings.
        """
        SEVERITY_UNSPECIFIED = 0
        ERROR = 1
        WARNING = 2

    type_: Type = proto.Field(
        proto.ENUM,
        number=1,
        enum=Type,
    )
    severity: Severity = proto.Field(
        proto.ENUM,
        number=2,
        enum=Severity,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListTestsRequest(proto.Message):
    r"""The request for the ListTests method.

    Attributes:
        parent (str):
            The session.
        page_size (int):
            The maximum number of tests to return per
            page.
        page_token (str):
            The page token, for retrieving subsequent
            pages.
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


class ListTestsResponse(proto.Message):
    r"""The response for the ListTests method.

    Attributes:
        tests (MutableSequence[google.showcase_v1beta1.types.Test]):
            The tests being returned.
        next_page_token (str):
            The next page token, if any.
            An empty value here means the last page has been
            reached.
    """

    @property
    def raw_page(self):
        return self

    tests: MutableSequence['Test'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='Test',
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class TestRun(proto.Message):
    r"""A TestRun is the result of running a Test.

    Attributes:
        test (str):
            The name of the test. The tests/\* portion of the names are
            hard-coded, and do not change from session to session.
        issue (google.showcase_v1beta1.types.Issue):
            An issue found with the test run. If empty,
            this test run was successful.
    """

    test: str = proto.Field(
        proto.STRING,
        number=1,
    )
    issue: 'Issue' = proto.Field(
        proto.MESSAGE,
        number=2,
        message='Issue',
    )


class DeleteTestRequest(proto.Message):
    r"""Request message for deleting a test.

    Attributes:
        name (str):
            The test to be deleted.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class VerifyTestRequest(proto.Message):
    r"""

    Attributes:
        name (str):
            The test to have an answer registered to it.
        answer (bytes):
            The answer from the test.
        answers (MutableSequence[bytes]):
            The answers from the test if multiple are to
            be checked
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    answer: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )
    answers: MutableSequence[bytes] = proto.RepeatedField(
        proto.BYTES,
        number=3,
    )


class VerifyTestResponse(proto.Message):
    r"""

    Attributes:
        issue (google.showcase_v1beta1.types.Issue):
            An issue if check answer was unsuccessful.
            This will be empty if the check answer
            succeeded.
    """

    issue: 'Issue' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='Issue',
    )


__all__ = tuple(sorted(__protobuf__.manifest))
