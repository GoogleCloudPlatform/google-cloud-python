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
    package="google.cloud.gkerecommender.v1",
    manifest={
        "FetchModelsRequest",
        "FetchModelsResponse",
        "FetchModelServersRequest",
        "FetchModelServersResponse",
        "FetchModelServerVersionsRequest",
        "FetchModelServerVersionsResponse",
        "FetchBenchmarkingDataRequest",
        "FetchBenchmarkingDataResponse",
        "FetchProfilesRequest",
        "PerformanceRequirements",
        "Amount",
        "Cost",
        "TokensPerSecondRange",
        "MillisecondRange",
        "PerformanceRange",
        "FetchProfilesResponse",
        "ModelServerInfo",
        "ResourcesUsed",
        "PerformanceStats",
        "Profile",
        "GenerateOptimizedManifestRequest",
        "KubernetesManifest",
        "GenerateOptimizedManifestResponse",
        "StorageConfig",
    },
)


class FetchModelsRequest(proto.Message):
    r"""Request message for
    [GkeInferenceQuickstart.FetchModels][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchModels].


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        page_size (int):
            Optional. The target number of results to return in a single
            response. If not specified, a default value will be chosen
            by the service. Note that the response may include a partial
            list and a caller should only rely on the response's
            [next_page_token][google.cloud.gkerecommender.v1.FetchModelsResponse.next_page_token]
            to determine if there are more instances left to be queried.

            This field is a member of `oneof`_ ``_page_size``.
        page_token (str):
            Optional. The value of
            [next_page_token][google.cloud.gkerecommender.v1.FetchModelsResponse.next_page_token]
            received from a previous ``FetchModelsRequest`` call.
            Provide this to retrieve the subsequent page in a multi-page
            list of results. When paginating, all other parameters
            provided to ``FetchModelsRequest`` must match the call that
            provided the page token.

            This field is a member of `oneof`_ ``_page_token``.
    """

    page_size: int = proto.Field(
        proto.INT32,
        number=1,
        optional=True,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )


class FetchModelsResponse(proto.Message):
    r"""Response message for
    [GkeInferenceQuickstart.FetchModels][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchModels].

    Attributes:
        models (MutableSequence[str]):
            Output only. List of available models. Open-source models
            follow the Huggingface Hub ``owner/model_name`` format.
        next_page_token (str):
            Output only. A token which may be sent as
            [page_token][FetchModelsResponse.page_token] in a subsequent
            ``FetchModelsResponse`` call to retrieve the next page of
            results. If this field is omitted or empty, then there are
            no more results to return.
    """

    @property
    def raw_page(self):
        return self

    models: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class FetchModelServersRequest(proto.Message):
    r"""Request message for
    [GkeInferenceQuickstart.FetchModelServers][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchModelServers].


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        model (str):
            Required. The model for which to list model servers.
            Open-source models follow the Huggingface Hub
            ``owner/model_name`` format. Use
            [GkeInferenceQuickstart.FetchModels][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchModels]
            to find available models.
        page_size (int):
            Optional. The target number of results to return in a single
            response. If not specified, a default value will be chosen
            by the service. Note that the response may include a partial
            list and a caller should only rely on the response's
            [next_page_token][google.cloud.gkerecommender.v1.FetchModelServersResponse.next_page_token]
            to determine if there are more instances left to be queried.

            This field is a member of `oneof`_ ``_page_size``.
        page_token (str):
            Optional. The value of
            [next_page_token][google.cloud.gkerecommender.v1.FetchModelServersResponse.next_page_token]
            received from a previous ``FetchModelServersRequest`` call.
            Provide this to retrieve the subsequent page in a multi-page
            list of results. When paginating, all other parameters
            provided to ``FetchModelServersRequest`` must match the call
            that provided the page token.

            This field is a member of `oneof`_ ``_page_token``.
    """

    model: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
        optional=True,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )


class FetchModelServersResponse(proto.Message):
    r"""Response message for
    [GkeInferenceQuickstart.FetchModelServers][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchModelServers].

    Attributes:
        model_servers (MutableSequence[str]):
            Output only. List of available model servers. Open-source
            model servers use simplified, lowercase names (e.g.,
            ``vllm``).
        next_page_token (str):
            Output only. A token which may be sent as
            [page_token][FetchModelServersResponse.page_token] in a
            subsequent ``FetchModelServersResponse`` call to retrieve
            the next page of results. If this field is omitted or empty,
            then there are no more results to return.
    """

    @property
    def raw_page(self):
        return self

    model_servers: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class FetchModelServerVersionsRequest(proto.Message):
    r"""Request message for
    [GkeInferenceQuickstart.FetchModelServerVersions][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchModelServerVersions].


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        model (str):
            Required. The model for which to list model server versions.
            Open-source models follow the Huggingface Hub
            ``owner/model_name`` format. Use
            [GkeInferenceQuickstart.FetchModels][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchModels]
            to find available models.
        model_server (str):
            Required. The model server for which to list versions.
            Open-source model servers use simplified, lowercase names
            (e.g., ``vllm``). Use
            [GkeInferenceQuickstart.FetchModelServers][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchModelServers]
            to find available model servers.
        page_size (int):
            Optional. The target number of results to return in a single
            response. If not specified, a default value will be chosen
            by the service. Note that the response may include a partial
            list and a caller should only rely on the response's
            [next_page_token][google.cloud.gkerecommender.v1.FetchModelServerVersionsResponse.next_page_token]
            to determine if there are more instances left to be queried.

            This field is a member of `oneof`_ ``_page_size``.
        page_token (str):
            Optional. The value of
            [next_page_token][google.cloud.gkerecommender.v1.FetchModelServerVersionsResponse.next_page_token]
            received from a previous ``FetchModelServerVersionsRequest``
            call. Provide this to retrieve the subsequent page in a
            multi-page list of results. When paginating, all other
            parameters provided to ``FetchModelServerVersionsRequest``
            must match the call that provided the page token.

            This field is a member of `oneof`_ ``_page_token``.
    """

    model: str = proto.Field(
        proto.STRING,
        number=1,
    )
    model_server: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
        optional=True,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )


class FetchModelServerVersionsResponse(proto.Message):
    r"""Response message for
    [GkeInferenceQuickstart.FetchModelServerVersions][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchModelServerVersions].

    Attributes:
        model_server_versions (MutableSequence[str]):
            Output only. A list of available model server
            versions.
        next_page_token (str):
            Output only. A token which may be sent as
            [page_token][FetchModelServerVersionsResponse.page_token] in
            a subsequent ``FetchModelServerVersionsResponse`` call to
            retrieve the next page of results. If this field is omitted
            or empty, then there are no more results to return.
    """

    @property
    def raw_page(self):
        return self

    model_server_versions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class FetchBenchmarkingDataRequest(proto.Message):
    r"""Request message for
    [GkeInferenceQuickstart.FetchBenchmarkingData][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchBenchmarkingData].

    Attributes:
        model_server_info (google.cloud.gkerecommender_v1.types.ModelServerInfo):
            Required. The model server configuration to get benchmarking
            data for. Use
            [GkeInferenceQuickstart.FetchProfiles][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchProfiles]
            to find valid configurations.
        instance_type (str):
            Optional. The instance type to filter benchmarking data.
            Instance types are in the format ``a2-highgpu-1g``. If not
            provided, all instance types for the given profile's
            ``model_server_info`` will be returned. Use
            [GkeInferenceQuickstart.FetchProfiles][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchProfiles]
            to find available instance types.
        pricing_model (str):
            Optional. The pricing model to use for the benchmarking
            data. Defaults to ``spot``.
    """

    model_server_info: "ModelServerInfo" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ModelServerInfo",
    )
    instance_type: str = proto.Field(
        proto.STRING,
        number=3,
    )
    pricing_model: str = proto.Field(
        proto.STRING,
        number=4,
    )


class FetchBenchmarkingDataResponse(proto.Message):
    r"""Response message for
    [GkeInferenceQuickstart.FetchBenchmarkingData][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchBenchmarkingData].

    Attributes:
        profile (MutableSequence[google.cloud.gkerecommender_v1.types.Profile]):
            Output only. List of profiles containing
            their respective benchmarking data.
    """

    profile: MutableSequence["Profile"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Profile",
    )


class FetchProfilesRequest(proto.Message):
    r"""Request message for
    [GkeInferenceQuickstart.FetchProfiles][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchProfiles].


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        model (str):
            Optional. The model to filter profiles by. Open-source
            models follow the Huggingface Hub ``owner/model_name``
            format. If not provided, all models are returned. Use
            [GkeInferenceQuickstart.FetchModels][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchModels]
            to find available models.
        model_server (str):
            Optional. The model server to filter profiles by. If not
            provided, all model servers are returned. Use
            [GkeInferenceQuickstart.FetchModelServers][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchModelServers]
            to find available model servers for a given model.
        model_server_version (str):
            Optional. The model server version to filter profiles by. If
            not provided, all model server versions are returned. Use
            [GkeInferenceQuickstart.FetchModelServerVersions][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchModelServerVersions]
            to find available versions for a given model and server.
        performance_requirements (google.cloud.gkerecommender_v1.types.PerformanceRequirements):
            Optional. The performance requirements to
            filter profiles. Profiles that do not meet these
            requirements are filtered out. If not provided,
            all profiles are returned.
        page_size (int):
            Optional. The target number of results to return in a single
            response. If not specified, a default value will be chosen
            by the service. Note that the response may include a partial
            list and a caller should only rely on the response's
            [next_page_token][google.cloud.gkerecommender.v1.FetchProfilesResponse.next_page_token]
            to determine if there are more instances left to be queried.

            This field is a member of `oneof`_ ``_page_size``.
        page_token (str):
            Optional. The value of
            [next_page_token][google.cloud.gkerecommender.v1.FetchProfilesResponse.next_page_token]
            received from a previous ``FetchProfilesRequest`` call.
            Provide this to retrieve the subsequent page in a multi-page
            list of results. When paginating, all other parameters
            provided to ``FetchProfilesRequest`` must match the call
            that provided the page token.

            This field is a member of `oneof`_ ``_page_token``.
    """

    model: str = proto.Field(
        proto.STRING,
        number=1,
    )
    model_server: str = proto.Field(
        proto.STRING,
        number=2,
    )
    model_server_version: str = proto.Field(
        proto.STRING,
        number=3,
    )
    performance_requirements: "PerformanceRequirements" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="PerformanceRequirements",
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=5,
        optional=True,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )


class PerformanceRequirements(proto.Message):
    r"""Performance requirements for a profile and or model
    deployment.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        target_ntpot_milliseconds (int):
            Optional. The target Normalized Time Per Output Token
            (NTPOT) in milliseconds. NTPOT is calculated as
            ``request_latency / total_output_tokens``. If not provided,
            this target will not be enforced.

            This field is a member of `oneof`_ ``_target_ntpot_milliseconds``.
        target_ttft_milliseconds (int):
            Optional. The target Time To First Token
            (TTFT) in milliseconds. TTFT is the time it
            takes to generate the first token for a request.
            If not provided, this target will not be
            enforced.

            This field is a member of `oneof`_ ``_target_ttft_milliseconds``.
        target_cost (google.cloud.gkerecommender_v1.types.Cost):
            Optional. The target cost for running a
            profile's model server. If not provided, this
            requirement will not be enforced.
    """

    target_ntpot_milliseconds: int = proto.Field(
        proto.INT32,
        number=1,
        optional=True,
    )
    target_ttft_milliseconds: int = proto.Field(
        proto.INT32,
        number=2,
        optional=True,
    )
    target_cost: "Cost" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Cost",
    )


class Amount(proto.Message):
    r"""Represents an amount of money in a specific currency.

    Attributes:
        units (int):
            Output only. The whole units of the amount. For example if
            ``currencyCode`` is ``"USD"``, then 1 unit is one US dollar.
        nanos (int):
            Output only. Number of nano (10^-9) units of the amount. The
            value must be between -999,999,999 and +999,999,999
            inclusive. If ``units`` is positive, ``nanos`` must be
            positive or zero. If ``units`` is zero, ``nanos`` can be
            positive, zero, or negative. If ``units`` is negative,
            ``nanos`` must be negative or zero. For example $-1.75 is
            represented as ``units``\ =-1 and ``nanos``\ =-750,000,000.
    """

    units: int = proto.Field(
        proto.INT64,
        number=1,
    )
    nanos: int = proto.Field(
        proto.INT32,
        number=2,
    )


class Cost(proto.Message):
    r"""Cost for running a model deployment on a given instance type.
    Currently, only USD currency code is supported.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        cost_per_million_output_tokens (google.cloud.gkerecommender_v1.types.Amount):
            Optional. The cost per million output tokens, calculated as:
            $/output token = GPU $/s / (1/output-to-input-cost-ratio \*
            input tokens/s + output tokens/s)
        cost_per_million_input_tokens (google.cloud.gkerecommender_v1.types.Amount):
            Optional. The cost per million input tokens.
            $/input token = ($/output token) /
            output-to-input-cost-ratio.
        pricing_model (str):
            Optional. The pricing model used to calculate the cost. Can
            be one of: ``3-years-cud``, ``1-year-cud``, ``on-demand``,
            ``spot``. If not provided, ``spot`` will be used.
        output_input_cost_ratio (float):
            Optional. The output-to-input cost ratio. This determines
            how the total GPU cost is split between input and output
            tokens. If not provided, ``4.0`` is used, assuming a 4:1
            output:input cost ratio.

            This field is a member of `oneof`_ ``_output_input_cost_ratio``.
    """

    cost_per_million_output_tokens: "Amount" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Amount",
    )
    cost_per_million_input_tokens: "Amount" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Amount",
    )
    pricing_model: str = proto.Field(
        proto.STRING,
        number=3,
    )
    output_input_cost_ratio: float = proto.Field(
        proto.FLOAT,
        number=4,
        optional=True,
    )


class TokensPerSecondRange(proto.Message):
    r"""Represents a range of throughput values in tokens per second.

    Attributes:
        min_ (int):
            Output only. The minimum value of the range.
        max_ (int):
            Output only. The maximum value of the range.
    """

    min_: int = proto.Field(
        proto.INT32,
        number=1,
    )
    max_: int = proto.Field(
        proto.INT32,
        number=2,
    )


class MillisecondRange(proto.Message):
    r"""Represents a range of latency values in milliseconds.

    Attributes:
        min_ (int):
            Output only. The minimum value of the range.
        max_ (int):
            Output only. The maximum value of the range.
    """

    min_: int = proto.Field(
        proto.INT32,
        number=1,
    )
    max_: int = proto.Field(
        proto.INT32,
        number=2,
    )


class PerformanceRange(proto.Message):
    r"""Performance range for a model deployment.

    Attributes:
        throughput_output_range (google.cloud.gkerecommender_v1.types.TokensPerSecondRange):
            Output only. The range of throughput in output tokens per
            second. This is measured as
            total_output_tokens_generated_by_server /
            elapsed_time_in_seconds.
        ttft_range (google.cloud.gkerecommender_v1.types.MillisecondRange):
            Output only. The range of TTFT (Time To First
            Token) in milliseconds. TTFT is the time it
            takes to generate the first token for a request.
        ntpot_range (google.cloud.gkerecommender_v1.types.MillisecondRange):
            Output only. The range of NTPOT (Normalized Time Per Output
            Token) in milliseconds. NTPOT is the request latency
            normalized by the number of output tokens, measured as
            request_latency / total_output_tokens.
    """

    throughput_output_range: "TokensPerSecondRange" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="TokensPerSecondRange",
    )
    ttft_range: "MillisecondRange" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="MillisecondRange",
    )
    ntpot_range: "MillisecondRange" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="MillisecondRange",
    )


class FetchProfilesResponse(proto.Message):
    r"""Response message for
    [GkeInferenceQuickstart.FetchProfiles][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchProfiles].

    Attributes:
        profile (MutableSequence[google.cloud.gkerecommender_v1.types.Profile]):
            Output only. List of profiles that match the
            given model server info and performance
            requirements (if provided).
        performance_range (google.cloud.gkerecommender_v1.types.PerformanceRange):
            Output only. The combined range of
            performance values observed across all profiles
            in this response.
        comments (str):
            Output only. Additional comments related to
            the response.
        next_page_token (str):
            Output only. A token which may be sent as
            [page_token][FetchProfilesResponse.page_token] in a
            subsequent ``FetchProfilesResponse`` call to retrieve the
            next page of results. If this field is omitted or empty,
            then there are no more results to return.
    """

    @property
    def raw_page(self):
        return self

    profile: MutableSequence["Profile"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Profile",
    )
    performance_range: "PerformanceRange" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="PerformanceRange",
    )
    comments: str = proto.Field(
        proto.STRING,
        number=3,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ModelServerInfo(proto.Message):
    r"""Model server information gives. Valid model server info combinations
    can be found using
    [GkeInferenceQuickstart.FetchProfiles][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchProfiles].

    Attributes:
        model (str):
            Required. The model. Open-source models follow the
            Huggingface Hub ``owner/model_name`` format. Use
            [GkeInferenceQuickstart.FetchModels][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchModels]
            to find available models.
        model_server (str):
            Required. The model server. Open-source model servers use
            simplified, lowercase names (e.g., ``vllm``). Use
            [GkeInferenceQuickstart.FetchModelServers][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchModelServers]
            to find available servers.
        model_server_version (str):
            Optional. The model server version. Use
            [GkeInferenceQuickstart.FetchModelServerVersions][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchModelServerVersions]
            to find available versions. If not provided, the latest
            available version is used.
    """

    model: str = proto.Field(
        proto.STRING,
        number=1,
    )
    model_server: str = proto.Field(
        proto.STRING,
        number=2,
    )
    model_server_version: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ResourcesUsed(proto.Message):
    r"""Resources used by a model deployment.

    Attributes:
        accelerator_count (int):
            Output only. The number of accelerators
            (e.g., GPUs or TPUs) used by the model
            deployment on the Kubernetes node.
    """

    accelerator_count: int = proto.Field(
        proto.INT32,
        number=1,
    )


class PerformanceStats(proto.Message):
    r"""Performance statistics for a model deployment.

    Attributes:
        queries_per_second (float):
            Output only. The number of queries per
            second. Note: This metric can vary widely based
            on context length and may not be a reliable
            measure of LLM throughput.
        output_tokens_per_second (int):
            Output only. The number of output tokens per second. This is
            the throughput measured as
            total_output_tokens_generated_by_server /
            elapsed_time_in_seconds.
        ntpot_milliseconds (int):
            Output only. The Normalized Time Per Output Token (NTPOT) in
            milliseconds. This is the request latency normalized by the
            number of output tokens, measured as request_latency /
            total_output_tokens.
        ttft_milliseconds (int):
            Output only. The Time To First Token (TTFT)
            in milliseconds. This is the time it takes to
            generate the first token for a request.
        cost (MutableSequence[google.cloud.gkerecommender_v1.types.Cost]):
            Output only. The cost of running the model
            deployment.
    """

    queries_per_second: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    output_tokens_per_second: int = proto.Field(
        proto.INT32,
        number=2,
    )
    ntpot_milliseconds: int = proto.Field(
        proto.INT32,
        number=3,
    )
    ttft_milliseconds: int = proto.Field(
        proto.INT32,
        number=4,
    )
    cost: MutableSequence["Cost"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="Cost",
    )


class Profile(proto.Message):
    r"""A profile containing information about a model deployment.

    Attributes:
        model_server_info (google.cloud.gkerecommender_v1.types.ModelServerInfo):
            Output only. The model server configuration. Use
            [GkeInferenceQuickstart.FetchProfiles][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchProfiles]
            to find valid configurations.
        accelerator_type (str):
            Output only. The accelerator type. Expected format:
            ``nvidia-h100-80gb``.
        tpu_topology (str):
            Output only. The TPU topology (if
            applicable).
        instance_type (str):
            Output only. The instance type. Expected format:
            ``a2-highgpu-1g``.
        resources_used (google.cloud.gkerecommender_v1.types.ResourcesUsed):
            Output only. The resources used by the model
            deployment.
        performance_stats (MutableSequence[google.cloud.gkerecommender_v1.types.PerformanceStats]):
            Output only. The performance statistics for
            this profile.
    """

    model_server_info: "ModelServerInfo" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ModelServerInfo",
    )
    accelerator_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    tpu_topology: str = proto.Field(
        proto.STRING,
        number=3,
    )
    instance_type: str = proto.Field(
        proto.STRING,
        number=4,
    )
    resources_used: "ResourcesUsed" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="ResourcesUsed",
    )
    performance_stats: MutableSequence["PerformanceStats"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="PerformanceStats",
    )


class GenerateOptimizedManifestRequest(proto.Message):
    r"""Request message for
    [GkeInferenceQuickstart.GenerateOptimizedManifest][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.GenerateOptimizedManifest].

    Attributes:
        model_server_info (google.cloud.gkerecommender_v1.types.ModelServerInfo):
            Required. The model server configuration to generate the
            manifest for. Use
            [GkeInferenceQuickstart.FetchProfiles][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchProfiles]
            to find valid configurations.
        accelerator_type (str):
            Required. The accelerator type. Use
            [GkeInferenceQuickstart.FetchProfiles][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.FetchProfiles]
            to find valid accelerators for a given
            ``model_server_info``.
        kubernetes_namespace (str):
            Optional. The kubernetes namespace to deploy
            the manifests in.
        performance_requirements (google.cloud.gkerecommender_v1.types.PerformanceRequirements):
            Optional. The performance requirements to use
            for generating Horizontal Pod Autoscaler (HPA)
            resources. If provided, the manifest includes
            HPA resources to adjust the model server replica
            count to maintain the specified targets (e.g.,
            NTPOT, TTFT) at a P50 latency. Cost targets are
            not currently supported for HPA generation. If
            the specified targets are not achievable, the
            HPA manifest will not be generated.
        storage_config (google.cloud.gkerecommender_v1.types.StorageConfig):
            Optional. The storage configuration for the
            model. If not provided, the model is loaded from
            Huggingface.
    """

    model_server_info: "ModelServerInfo" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ModelServerInfo",
    )
    accelerator_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    kubernetes_namespace: str = proto.Field(
        proto.STRING,
        number=3,
    )
    performance_requirements: "PerformanceRequirements" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="PerformanceRequirements",
    )
    storage_config: "StorageConfig" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="StorageConfig",
    )


class KubernetesManifest(proto.Message):
    r"""A Kubernetes manifest.

    Attributes:
        kind (str):
            Output only. Kubernetes resource kind.
        api_version (str):
            Output only. Kubernetes API version.
        content (str):
            Output only. YAML content.
    """

    kind: str = proto.Field(
        proto.STRING,
        number=1,
    )
    api_version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    content: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GenerateOptimizedManifestResponse(proto.Message):
    r"""Response message for
    [GkeInferenceQuickstart.GenerateOptimizedManifest][google.cloud.gkerecommender.v1.GkeInferenceQuickstart.GenerateOptimizedManifest].

    Attributes:
        kubernetes_manifests (MutableSequence[google.cloud.gkerecommender_v1.types.KubernetesManifest]):
            Output only. A list of generated Kubernetes
            manifests.
        comments (MutableSequence[str]):
            Output only. Comments related to deploying
            the generated manifests.
        manifest_version (str):
            Output only. Additional information about the versioned
            dependencies used to generate the manifests. See `Run best
            practice inference with GKE Inference Quickstart
            recipes <https://cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/inference/inference-quickstart>`__
            for details.
    """

    kubernetes_manifests: MutableSequence["KubernetesManifest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="KubernetesManifest",
    )
    comments: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    manifest_version: str = proto.Field(
        proto.STRING,
        number=3,
    )


class StorageConfig(proto.Message):
    r"""Storage configuration for a model deployment.

    Attributes:
        model_bucket_uri (str):
            Optional. The Google Cloud Storage bucket URI to load the
            model from. This URI must point to the directory containing
            the model's config file (``config.json``) and model weights.
            A tuned GCSFuse setup can improve LLM Pod startup time by
            more than 7x. Expected format:
            ``gs://<bucket-name>/<path-to-model>``.
        xla_cache_bucket_uri (str):
            Optional. The URI for the GCS bucket containing the XLA
            compilation cache. If using TPUs, the XLA cache will be
            written to the same path as ``model_bucket_uri``. This can
            speed up vLLM model preparation for repeated deployments.
    """

    model_bucket_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    xla_cache_bucket_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
