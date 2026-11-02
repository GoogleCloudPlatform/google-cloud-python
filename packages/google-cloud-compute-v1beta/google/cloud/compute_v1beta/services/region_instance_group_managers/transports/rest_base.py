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
import json  # type: ignore
import re
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union

from google.api_core import gapic_v1, path_template
from google.protobuf import json_format

from google.cloud.compute_v1beta.types import compute

from .base import DEFAULT_CLIENT_INFO, RegionInstanceGroupManagersTransport


class _BaseRegionInstanceGroupManagersRestTransport(
    RegionInstanceGroupManagersTransport
):
    """Base REST backend transport for RegionInstanceGroupManagers.

    Note: This class is not meant to be used directly. Use its sync and
    async sub-classes instead.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "compute.googleapis.com",
        credentials: Optional[Any] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.
        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'compute.googleapis.com').
            credentials (Optional[Any]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you are developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            url_scheme: the protocol scheme for the API endpoint.  Normally
                "https", but for testing or local servers,
                "http" can be specified.
        """
        # Run the base constructor
        maybe_url_match = re.match("^(?P<scheme>http(?:s)?://)?(?P<host>.*)$", host)
        if maybe_url_match is None:
            raise ValueError(
                f"Unexpected hostname structure: {host}"
            )  # pragma: NO COVER

        url_match_items = maybe_url_match.groupdict()

        host = f"{url_scheme}://{host}" if not url_match_items["scheme"] else host

        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            api_audience=api_audience,
        )

    class _BaseAbandonInstances:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/compute/beta/projects/{project}/regions/{region}/instanceGroupManagers/{instance_group_manager}/abandonInstances",
                    "body": "region_instance_group_managers_abandon_instances_request_resource",
                },
            ]
            return http_options

    class _BaseAdoptInstances:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/compute/beta/projects/{project}/regions/{region}/instanceGroupManagers/{instance_group_manager}/adoptInstances",
                    "body": "region_instance_group_managers_adopt_instances_request_resource",
                },
            ]
            return http_options

    class _BaseApplyUpdatesToInstances:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/compute/beta/projects/{project}/regions/{region}/instanceGroupManagers/{instance_group_manager}/applyUpdatesToInstances",
                    "body": "region_instance_group_managers_apply_updates_request_resource",
                },
            ]
            return http_options

    class _BaseCreateInstances:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/compute/beta/projects/{project}/regions/{region}/instanceGroupManagers/{instance_group_manager}/createInstances",
                    "body": "region_instance_group_managers_create_instances_request_resource",
                },
            ]
            return http_options

    class _BaseDelete:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "delete",
                    "uri": "/compute/beta/projects/{project}/regions/{region}/instanceGroupManagers/{instance_group_manager}",
                },
            ]
            return http_options

    class _BaseDeleteInstances:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/compute/beta/projects/{project}/regions/{region}/instanceGroupManagers/{instance_group_manager}/deleteInstances",
                    "body": "region_instance_group_managers_delete_instances_request_resource",
                },
            ]
            return http_options

    class _BaseDeletePerInstanceConfigs:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/compute/beta/projects/{project}/regions/{region}/instanceGroupManagers/{instance_group_manager}/deletePerInstanceConfigs",
                    "body": "region_instance_group_manager_delete_instance_config_req_resource",
                },
            ]
            return http_options

    class _BaseGet:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/compute/beta/projects/{project}/regions/{region}/instanceGroupManagers/{instance_group_manager}",
                },
            ]
            return http_options

    class _BaseInsert:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/compute/beta/projects/{project}/regions/{region}/instanceGroupManagers",
                    "body": "instance_group_manager_resource",
                },
            ]
            return http_options

    class _BaseList:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/compute/beta/projects/{project}/regions/{region}/instanceGroupManagers",
                },
            ]
            return http_options

    class _BaseListErrors:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "get",
                    "uri": "/compute/beta/projects/{project}/regions/{region}/instanceGroupManagers/{instance_group_manager}/listErrors",
                },
            ]
            return http_options

    class _BaseListManagedInstances:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/compute/beta/projects/{project}/regions/{region}/instanceGroupManagers/{instance_group_manager}/listManagedInstances",
                },
            ]
            return http_options

    class _BaseListPerInstanceConfigs:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/compute/beta/projects/{project}/regions/{region}/instanceGroupManagers/{instance_group_manager}/listPerInstanceConfigs",
                },
            ]
            return http_options

    class _BasePatch:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "patch",
                    "uri": "/compute/beta/projects/{project}/regions/{region}/instanceGroupManagers/{instance_group_manager}",
                    "body": "instance_group_manager_resource",
                },
            ]
            return http_options

    class _BasePatchPerInstanceConfigs:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/compute/beta/projects/{project}/regions/{region}/instanceGroupManagers/{instance_group_manager}/patchPerInstanceConfigs",
                    "body": "region_instance_group_manager_patch_instance_config_req_resource",
                },
            ]
            return http_options

    class _BaseRecreateInstances:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/compute/beta/projects/{project}/regions/{region}/instanceGroupManagers/{instance_group_manager}/recreateInstances",
                    "body": "region_instance_group_managers_recreate_request_resource",
                },
            ]
            return http_options

    class _BaseResize:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {
            "size": 0,
        }

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/compute/beta/projects/{project}/regions/{region}/instanceGroupManagers/{instance_group_manager}/resize",
                },
            ]
            return http_options

    class _BaseResizeAdvanced:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/compute/beta/projects/{project}/regions/{region}/instanceGroupManagers/{instance_group_manager}/resizeAdvanced",
                    "body": "region_instance_group_managers_resize_advanced_request_resource",
                },
            ]
            return http_options

    class _BaseResumeInstances:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/compute/beta/projects/{project}/regions/{region}/instanceGroupManagers/{instance_group_manager}/resumeInstances",
                    "body": "region_instance_group_managers_resume_instances_request_resource",
                },
            ]
            return http_options

    class _BaseSetAutoHealingPolicies:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/compute/beta/projects/{project}/regions/{region}/instanceGroupManagers/{instance_group_manager}/setAutoHealingPolicies",
                    "body": "region_instance_group_managers_set_auto_healing_request_resource",
                },
            ]
            return http_options

    class _BaseSetInstanceTemplate:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/compute/beta/projects/{project}/regions/{region}/instanceGroupManagers/{instance_group_manager}/setInstanceTemplate",
                    "body": "region_instance_group_managers_set_template_request_resource",
                },
            ]
            return http_options

    class _BaseSetTargetPools:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/compute/beta/projects/{project}/regions/{region}/instanceGroupManagers/{instance_group_manager}/setTargetPools",
                    "body": "region_instance_group_managers_set_target_pools_request_resource",
                },
            ]
            return http_options

    class _BaseStartInstances:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/compute/beta/projects/{project}/regions/{region}/instanceGroupManagers/{instance_group_manager}/startInstances",
                    "body": "region_instance_group_managers_start_instances_request_resource",
                },
            ]
            return http_options

    class _BaseStopInstances:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/compute/beta/projects/{project}/regions/{region}/instanceGroupManagers/{instance_group_manager}/stopInstances",
                    "body": "region_instance_group_managers_stop_instances_request_resource",
                },
            ]
            return http_options

    class _BaseSuspendInstances:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/compute/beta/projects/{project}/regions/{region}/instanceGroupManagers/{instance_group_manager}/suspendInstances",
                    "body": "region_instance_group_managers_suspend_instances_request_resource",
                },
            ]
            return http_options

    class _BaseTestIamPermissions:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/compute/beta/projects/{project}/regions/{region}/instanceGroupManagers/{resource}/testIamPermissions",
                    "body": "test_permissions_request_resource",
                },
            ]
            return http_options

    class _BaseUpdate:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "put",
                    "uri": "/compute/beta/projects/{project}/regions/{region}/instanceGroupManagers/{instance_group_manager}",
                    "body": "instance_group_manager_resource",
                },
            ]
            return http_options

    class _BaseUpdatePerInstanceConfigs:
        def __hash__(self):  # pragma: NO COVER
            return NotImplementedError("__hash__ must be implemented.")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, Any] = {}

        @staticmethod
        def _get_http_options():
            http_options: List[Dict[str, str]] = [
                {
                    "method": "post",
                    "uri": "/compute/beta/projects/{project}/regions/{region}/instanceGroupManagers/{instance_group_manager}/updatePerInstanceConfigs",
                    "body": "region_instance_group_manager_update_instance_config_req_resource",
                },
            ]
            return http_options


__all__ = ("_BaseRegionInstanceGroupManagersRestTransport",)
