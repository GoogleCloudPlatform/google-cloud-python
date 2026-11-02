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

from google.cloud.dialogflowcx_v3.types import test_case, webhook

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.cx.v3",
    manifest={
        "Environment",
        "ListEnvironmentsRequest",
        "ListEnvironmentsResponse",
        "GetEnvironmentRequest",
        "CreateEnvironmentRequest",
        "UpdateEnvironmentRequest",
        "DeleteEnvironmentRequest",
        "LookupEnvironmentHistoryRequest",
        "LookupEnvironmentHistoryResponse",
        "ContinuousTestResult",
        "RunContinuousTestRequest",
        "RunContinuousTestResponse",
        "RunContinuousTestMetadata",
        "ListContinuousTestResultsRequest",
        "ListContinuousTestResultsResponse",
        "DeployFlowRequest",
        "DeployFlowResponse",
        "DeployFlowMetadata",
    },
)


class Environment(proto.Message):
    r"""Represents an environment for an agent. You can create
    multiple versions of your agent and publish them to separate
    environments. When you edit an agent, you are editing the draft
    agent. At any point, you can save the draft agent as an agent
    version, which is an immutable snapshot of your agent. When you
    save the draft agent, it is published to the default
    environment. When you create agent versions, you can publish
    them to custom environments. You can create a variety of custom
    environments for testing, development, production, etc.

    Attributes:
        name (str):
            The name of the environment. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>``.
        display_name (str):
            Required. The human-readable name of the
            environment (unique in an agent). Limit of 64
            characters.
        description (str):
            The human-readable description of the
            environment. The maximum length is 500
            characters. If exceeded, the request is
            rejected.
        version_configs (MutableSequence[google.cloud.dialogflowcx_v3.types.Environment.VersionConfig]):
            A list of configurations for flow versions. You should
            include version configs for all flows that are reachable
            from [``Start Flow``][Agent.start_flow] in the agent.
            Otherwise, an error will be returned.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Update time of this environment.
        test_cases_config (google.cloud.dialogflowcx_v3.types.Environment.TestCasesConfig):
            The test cases config for continuous tests of
            this environment.
        webhook_config (google.cloud.dialogflowcx_v3.types.Environment.WebhookConfig):
            The webhook configuration for this
            environment.
    """

    class VersionConfig(proto.Message):
        r"""Configuration for the version.

        Attributes:
            version (str):
                Required. Flow, playbook and tool versions
                are supported. Format for flow version:

                projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/versions/<VersionID>.
                Format for playbook version:

                projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>/versions/<VersionID>.
                Format for tool version:

                projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/tools/<ToolID>/versions/<VersionID>.
        """

        version: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class TestCasesConfig(proto.Message):
        r"""The configuration for continuous tests.

        Attributes:
            test_cases (MutableSequence[str]):
                A list of test case names to run. They should be under the
                same agent. Format of each test case name:
                ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/testCases/<TestCaseID>``
            enable_continuous_run (bool):
                Whether to run test cases in
                [TestCasesConfig.test_cases][google.cloud.dialogflow.cx.v3.Environment.TestCasesConfig.test_cases]
                periodically. Default false. If set to true, run once a day.
            enable_predeployment_run (bool):
                Whether to run test cases in
                [TestCasesConfig.test_cases][google.cloud.dialogflow.cx.v3.Environment.TestCasesConfig.test_cases]
                before deploying a flow version to the environment. Default
                false.
        """

        test_cases: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        enable_continuous_run: bool = proto.Field(
            proto.BOOL,
            number=2,
        )
        enable_predeployment_run: bool = proto.Field(
            proto.BOOL,
            number=3,
        )

    class WebhookConfig(proto.Message):
        r"""Configuration for webhooks.

        Attributes:
            webhook_overrides (MutableSequence[google.cloud.dialogflowcx_v3.types.Webhook]):
                The list of webhooks to override for the agent environment.
                The webhook must exist in the agent. You can override fields
                in
                [``generic_web_service``][google.cloud.dialogflow.cx.v3.Webhook.generic_web_service]
                and
                [``service_directory``][google.cloud.dialogflow.cx.v3.Webhook.service_directory].
        """

        webhook_overrides: MutableSequence[webhook.Webhook] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=webhook.Webhook,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    version_configs: MutableSequence[VersionConfig] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=VersionConfig,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    test_cases_config: TestCasesConfig = proto.Field(
        proto.MESSAGE,
        number=7,
        message=TestCasesConfig,
    )
    webhook_config: WebhookConfig = proto.Field(
        proto.MESSAGE,
        number=10,
        message=WebhookConfig,
    )


class ListEnvironmentsRequest(proto.Message):
    r"""The request message for
    [Environments.ListEnvironments][google.cloud.dialogflow.cx.v3.Environments.ListEnvironments].

    Attributes:
        parent (str):
            Required. The [Agent][google.cloud.dialogflow.cx.v3.Agent]
            to list all environments for. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>``.
        page_size (int):
            The maximum number of items to return in a
            single page. By default 20 and at most 100.
        page_token (str):
            The next_page_token value returned from a previous list
            request.
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


class ListEnvironmentsResponse(proto.Message):
    r"""The response message for
    [Environments.ListEnvironments][google.cloud.dialogflow.cx.v3.Environments.ListEnvironments].

    Attributes:
        environments (MutableSequence[google.cloud.dialogflowcx_v3.types.Environment]):
            The list of environments. There will be a maximum number of
            items returned based on the page_size field in the request.
            The list may in some cases be empty or contain fewer entries
            than page_size even if this isn't the last page.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    environments: MutableSequence["Environment"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Environment",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetEnvironmentRequest(proto.Message):
    r"""The request message for
    [Environments.GetEnvironment][google.cloud.dialogflow.cx.v3.Environments.GetEnvironment].

    Attributes:
        name (str):
            Required. The name of the
            [Environment][google.cloud.dialogflow.cx.v3.Environment].
            Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateEnvironmentRequest(proto.Message):
    r"""The request message for
    [Environments.CreateEnvironment][google.cloud.dialogflow.cx.v3.Environments.CreateEnvironment].

    Attributes:
        parent (str):
            Required. The [Agent][google.cloud.dialogflow.cx.v3.Agent]
            to create an
            [Environment][google.cloud.dialogflow.cx.v3.Environment]
            for. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>``.
        environment (google.cloud.dialogflowcx_v3.types.Environment):
            Required. The environment to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    environment: "Environment" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Environment",
    )


class UpdateEnvironmentRequest(proto.Message):
    r"""The request message for
    [Environments.UpdateEnvironment][google.cloud.dialogflow.cx.v3.Environments.UpdateEnvironment].

    Attributes:
        environment (google.cloud.dialogflowcx_v3.types.Environment):
            Required. The environment to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The mask to control which fields
            get updated.
    """

    environment: "Environment" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Environment",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteEnvironmentRequest(proto.Message):
    r"""The request message for
    [Environments.DeleteEnvironment][google.cloud.dialogflow.cx.v3.Environments.DeleteEnvironment].

    Attributes:
        name (str):
            Required. The name of the
            [Environment][google.cloud.dialogflow.cx.v3.Environment] to
            delete. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class LookupEnvironmentHistoryRequest(proto.Message):
    r"""The request message for
    [Environments.LookupEnvironmentHistory][google.cloud.dialogflow.cx.v3.Environments.LookupEnvironmentHistory].

    Attributes:
        name (str):
            Required. Resource name of the environment to look up the
            history for. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>``.
        page_size (int):
            The maximum number of items to return in a
            single page. By default 100 and at most 1000.
        page_token (str):
            The next_page_token value returned from a previous list
            request.
    """

    name: str = proto.Field(
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


class LookupEnvironmentHistoryResponse(proto.Message):
    r"""The response message for
    [Environments.LookupEnvironmentHistory][google.cloud.dialogflow.cx.v3.Environments.LookupEnvironmentHistory].

    Attributes:
        environments (MutableSequence[google.cloud.dialogflowcx_v3.types.Environment]):
            Represents a list of snapshots for an environment. Time of
            the snapshots is stored in
            [``update_time``][google.cloud.dialogflow.cx.v3.Environment.update_time].
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    environments: MutableSequence["Environment"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Environment",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ContinuousTestResult(proto.Message):
    r"""Represents a result from running a test case in an agent
    environment.

    Attributes:
        name (str):
            The resource name for the continuous test result. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>/continuousTestResults/<ContinuousTestResultID>``.
        result (google.cloud.dialogflowcx_v3.types.ContinuousTestResult.AggregatedTestResult):
            The result of this continuous test run, i.e.
            whether all the tests in this continuous test
            run pass or not.
        test_case_results (MutableSequence[str]):
            A list of individual test case results names
            in this continuous test run.
        run_time (google.protobuf.timestamp_pb2.Timestamp):
            Time when the continuous testing run starts.
    """

    class AggregatedTestResult(proto.Enum):
        r"""The overall result for a continuous test run in an agent
        environment.

        Values:
            AGGREGATED_TEST_RESULT_UNSPECIFIED (0):
                Not specified. Should never be used.
            PASSED (1):
                All the tests passed.
            FAILED (2):
                At least one test did not pass.
        """

        AGGREGATED_TEST_RESULT_UNSPECIFIED = 0
        PASSED = 1
        FAILED = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    result: AggregatedTestResult = proto.Field(
        proto.ENUM,
        number=2,
        enum=AggregatedTestResult,
    )
    test_case_results: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    run_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


class RunContinuousTestRequest(proto.Message):
    r"""The request message for
    [Environments.RunContinuousTest][google.cloud.dialogflow.cx.v3.Environments.RunContinuousTest].

    Attributes:
        environment (str):
            Required. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>``.
    """

    environment: str = proto.Field(
        proto.STRING,
        number=1,
    )


class RunContinuousTestResponse(proto.Message):
    r"""The response message for
    [Environments.RunContinuousTest][google.cloud.dialogflow.cx.v3.Environments.RunContinuousTest].

    Attributes:
        continuous_test_result (google.cloud.dialogflowcx_v3.types.ContinuousTestResult):
            The result for a continuous test run.
    """

    continuous_test_result: "ContinuousTestResult" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ContinuousTestResult",
    )


class RunContinuousTestMetadata(proto.Message):
    r"""Metadata returned for the
    [Environments.RunContinuousTest][google.cloud.dialogflow.cx.v3.Environments.RunContinuousTest]
    long running operation.

    Attributes:
        errors (MutableSequence[google.cloud.dialogflowcx_v3.types.TestError]):
            The test errors.
    """

    errors: MutableSequence[test_case.TestError] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=test_case.TestError,
    )


class ListContinuousTestResultsRequest(proto.Message):
    r"""The request message for
    [Environments.ListContinuousTestResults][google.cloud.dialogflow.cx.v3.Environments.ListContinuousTestResults].

    Attributes:
        parent (str):
            Required. The environment to list results for. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>``.
        page_size (int):
            The maximum number of items to return in a
            single page. By default 100 and at most 1000.
        page_token (str):
            The next_page_token value returned from a previous list
            request.
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


class ListContinuousTestResultsResponse(proto.Message):
    r"""The response message for [Environments.ListTestCaseResults][].

    Attributes:
        continuous_test_results (MutableSequence[google.cloud.dialogflowcx_v3.types.ContinuousTestResult]):
            The list of continuous test results.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    continuous_test_results: MutableSequence["ContinuousTestResult"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="ContinuousTestResult",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeployFlowRequest(proto.Message):
    r"""The request message for
    [Environments.DeployFlow][google.cloud.dialogflow.cx.v3.Environments.DeployFlow].

    Attributes:
        environment (str):
            Required. The environment to deploy the flow to. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>``.
        flow_version (str):
            Required. The flow version to deploy. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/versions/<VersionID>``.
    """

    environment: str = proto.Field(
        proto.STRING,
        number=1,
    )
    flow_version: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeployFlowResponse(proto.Message):
    r"""The response message for
    [Environments.DeployFlow][google.cloud.dialogflow.cx.v3.Environments.DeployFlow].

    Attributes:
        environment (google.cloud.dialogflowcx_v3.types.Environment):
            The updated environment where the flow is
            deployed.
        deployment (str):
            The name of the flow version
            [Deployment][google.cloud.dialogflow.cx.v3.Deployment].
            Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>/deployments/<DeploymentID>``.
    """

    environment: "Environment" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Environment",
    )
    deployment: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeployFlowMetadata(proto.Message):
    r"""Metadata returned for the
    [Environments.DeployFlow][google.cloud.dialogflow.cx.v3.Environments.DeployFlow]
    long running operation.

    Attributes:
        test_errors (MutableSequence[google.cloud.dialogflowcx_v3.types.TestError]):
            Errors of running deployment tests.
    """

    test_errors: MutableSequence[test_case.TestError] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=test_case.TestError,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
