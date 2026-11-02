# Copyright 2022 Google LLC
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

import dataclasses
from typing import List, Optional

import inflection
import libcst

from gapic.configurable_snippetgen import libcst_utils
from gapic.configurable_snippetgen import snippet_config_language_pb2
from gapic.schema import api


class _AppendToSampleFunctionBody(libcst.CSTTransformer):
    def __init__(self, statement: libcst.BaseStatement):
        self.statement = statement

    def visit_IndentedBlock(self, node: libcst.IndentedBlock) -> bool:
        # Do not visit any nested indented blocks.
        return False

    def leave_IndentedBlock(
        self, original_node: libcst.IndentedBlock, updated_node: libcst.IndentedBlock
    ) -> libcst.IndentedBlock:
        del original_node
        # FunctionDef.body is an IndentedBlock, and IndentedBlock.body
        # is the actual sequence of statements.
        new_body = list(updated_node.body) + [self.statement]
        return updated_node.with_changes(body=new_body)


@dataclasses.dataclass
class ConfiguredSnippet:
    api_schema: api.API
    config: snippet_config_language_pb2.SnippetConfig
    api_version: str
    is_sync: bool

    def __post_init__(self) -> None:
        self._module: libcst.Module = libcst_utils.empty_module()
        self._sample_function_def: libcst.FunctionDef = libcst_utils.base_function_def(
            function_name=self.sample_function_name, is_sync=self.is_sync
        )

    @property
    def code(self) -> str:
        """The code of the configured snippet."""
        return self._module.code

    @property
    def gapic_module_name(self) -> str:
        """The GAPIC module name.

        For example:
            "speech_v1"
        """
        module_name = self.config.rpc.proto_package.split(".")[-1]
        return f"{module_name}_{self.api_version}"

    @property
    def region_tag(self) -> str:
        """The region tag of the snippet.

        For example:
            "speech_v1_config_Adaptation_CreateCustomClass_Basic_async"
        """
        service_name = self.config.rpc.service_name
        rpc_name = self.config.rpc.rpc_name
        config_id = self.config.metadata.config_id
        sync_or_async = "sync" if self.is_sync else "async"
        return f"{self.gapic_module_name}_config_{service_name}_{rpc_name}_{config_id}_{sync_or_async}"

    @property
    def sample_function_name(self) -> str:
        """The sample function's name.

        For example:
            "sample_create_custom_class_Basic"
        """
        snippet_method_name = self.config.signature.snippet_method_name
        config_id = self.config.metadata.config_id
        return f"sample_{snippet_method_name}_{config_id}"

    @property
    def client_class_name(self) -> str:
        """The service client's class name.

        For example:
            "AdaptationClient"
            "AdaptationAsyncClient"
        """
        if self.is_sync:
            client_class_name = f"{self.config.rpc.service_name}Client"
        else:
            client_class_name = f"{self.config.rpc.service_name}AsyncClient"
        return client_class_name

    @property
    def filename(self) -> str:
        """The snippet's file name.

        For example:
            "speech_v1_generated_Adaptation_create_custom_class_Basic_async.py"
        """
        service_name = self.config.rpc.service_name
        snake_case_rpc_name = inflection.underscore(self.config.rpc.rpc_name)
        config_id = self.config.metadata.config_id
        sync_or_async = "sync" if self.is_sync else "async"
        return f"{self.gapic_module_name}_generated_{service_name}_{snake_case_rpc_name}_{config_id}_{sync_or_async}.py"

    @property
    def api_endpoint(self) -> Optional[str]:
        """The api_endpoint in client_options."""
        service_endpoint = (
            self.config.snippet.service_client_initialization.custom_service_endpoint
        )

        if not service_endpoint.host:
            return None

        schema = service_endpoint.schema
        host = service_endpoint.host
        region = service_endpoint.region
        port = service_endpoint.port

        if port:
            host_maybe_with_port = f"{host}:{port}"
        else:
            host_maybe_with_port = host

        if region:
            host_maybe_with_port_and_region = f"{region}-{host_maybe_with_port}"
        else:
            host_maybe_with_port_and_region = host_maybe_with_port

        if (
            schema
            == snippet_config_language_pb2.Snippet.ClientInitialization.ServiceEndpoint.HTTP
        ):
            return f"http://{host_maybe_with_port_and_region}"
        else:
            # Either the default or HTTPS, in which case the schema is not needed.
            return host_maybe_with_port_and_region

    def _extend_sample_function_def_body(
        self, statements: List[libcst.BaseStatement]
    ) -> None:
        """Appends the statements to the current sample function def."""
        for statement in statements:
            transformer = _AppendToSampleFunctionBody(statement)

            # The result of applying a transformer could be of a different type
            # in general, but we will only update the sample function def here.
            self._sample_function_def = self._sample_function_def.visit(  # type: ignore
                transformer
            )

    def _add_sample_function_parameters(self) -> None:
        """Adds sample function parameters.

        Before:
            def sample_create_custom_class_Basic():
                ...
        After:
            def sample_create_custom_class_Basic(parent = "projects/..."):
                ...
        """
        # TODO: https://github.com/googleapis/gapic-generator-python/issues/1537, add typing annotation in sample function parameters.
        params = []
        for config_parameter in self.config.signature.parameters:
            params.append(libcst_utils.convert_parameter(config_parameter))
        parameters = libcst.Parameters(params=params)
        self._sample_function_def = self._sample_function_def.with_changes(
            params=parameters
        )

    def _get_service_client_initialization(self) -> List[libcst.BaseStatement]:
        """Returns the service client initialization statements.

        Examples:
            client = speech_v1.AdaptationClient()

            client = speech_v1.AdaptationClient(client_options = {"api_endpoint": "us-speech.googleapis.com"})
        """
        if self.api_endpoint is not None:
            client_options_arg = libcst.Arg(
                keyword=libcst.Name("client_options"),
                value=libcst_utils.convert_py_dict(
                    [("api_endpoint", self.api_endpoint)]
                ),
            )
            service_client_initialization = libcst.helpers.parse_template_statement(
                f"client = {self.gapic_module_name}.{self.client_class_name}({{arg}})",
                arg=client_options_arg,
            )
        else:
            service_client_initialization = libcst.parse_statement(
                f"client = {self.gapic_module_name}.{self.client_class_name}()"
            )

        # TODO: https://github.com/googleapis/gapic-generator-python/issues/1539, support pre_client_initialization statements.
        return [service_client_initialization]

    def _get_standard_call(self) -> List[libcst.BaseStatement]:
        """Returns the standard call statements."""
        # TODO: https://github.com/googleapis/gapic-generator-python/issues/1539, support standard call statements.
        return []

    def _get_call(self) -> List[libcst.BaseStatement]:
        """Returns the snippet call statements."""
        call_type = self.config.snippet.WhichOneof("call")
        if call_type == "standard":
            return self._get_standard_call()
        else:
            raise ValueError(f"Snippet call type {call_type} not supported.")

    def _build_sample_function(self) -> None:
        # TODO: https://github.com/googleapis/gapic-generator-python/issues/1536, add return type.
        # TODO: https://github.com/googleapis/gapic-generator-python/issues/1538, add docstring.
        self._add_sample_function_parameters()
        self._extend_sample_function_def_body(self._get_service_client_initialization())
        self._extend_sample_function_def_body(self._get_call())

    def _add_sample_function(self) -> None:
        self._module = self._module.with_changes(body=[self._sample_function_def])

    def generate(self) -> None:
        """Generates the snippet.

        This is the main entrypoint of a ConfiguredSnippet instance, calling
        other methods to update self._module.
        """
        self._build_sample_function()
        self._add_sample_function()
        # TODO: https://github.com/googleapis/gapic-generator-python/issues/1535, add imports.
        # TODO: https://github.com/googleapis/gapic-generator-python/issues/1534, add region tag.
        # TODO: https://github.com/googleapis/gapic-generator-python/issues/1533, add header.
