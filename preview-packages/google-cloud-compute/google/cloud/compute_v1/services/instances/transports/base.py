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
import abc
from typing import Any, Awaitable, Callable, Dict, Optional, Sequence, Union

import google.api_core
import google.auth  # type: ignore
import google.protobuf
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.compute_v1 import gapic_version as package_version
from google.cloud.compute_v1.services import zone_operations
from google.cloud.compute_v1.types import compute

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class InstancesTransport(abc.ABC):
    """Abstract transport class for Instances."""

    AUTH_SCOPES = (
        "https://www.googleapis.com/auth/compute",
        "https://www.googleapis.com/auth/cloud-platform",
    )

    DEFAULT_HOST: str = "compute.googleapis.com"

    def __init__(
        self,
        *,
        host: str = DEFAULT_HOST,
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        api_audience: Optional[str] = None,
        **kwargs,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'compute.googleapis.com').
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): Deprecated. A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials. This argument will be
                removed in the next major version of this library.
            scopes (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            api_audience (Optional[str]): The intended audience for the API calls
                to the service that will be set when using certain 3rd party
                authentication flows. Audience is typically a resource identifier.
                If not set, the host value will be used as a default.
        """
        self._extended_operations_services: Dict[str, Any] = {}

        # Save the scopes.
        self._scopes = scopes
        if not hasattr(self, "_ignore_credentials"):
            self._ignore_credentials: bool = False

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise core_exceptions.DuplicateCredentialArgs(
                "'credentials_file' and 'credentials' are mutually exclusive"
            )

        if credentials_file is not None:
            credentials, _ = google.auth.load_credentials_from_file(
                credentials_file,
                scopes=scopes,
                quota_project_id=quota_project_id,
                default_scopes=self.AUTH_SCOPES,
            )
        elif credentials is None and not self._ignore_credentials:
            credentials, _ = google.auth.default(
                scopes=scopes,
                quota_project_id=quota_project_id,
                default_scopes=self.AUTH_SCOPES,
            )
            # Don't apply audience if the credentials file passed from user.
            if hasattr(credentials, "with_gdch_audience"):
                credentials = credentials.with_gdch_audience(
                    api_audience if api_audience else host
                )

        # If the credentials are service account credentials, then always try to use self signed JWT.
        if (
            always_use_jwt_access
            and isinstance(credentials, service_account.Credentials)
            and hasattr(service_account.Credentials, "with_always_use_jwt_access")
        ):
            credentials = credentials.with_always_use_jwt_access(True)

        # Save the credentials.
        self._credentials = credentials

        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ":" not in host:
            host += ":443"
        self._host = host

        self._wrapped_methods: Dict[Callable, Callable] = {}

    @property
    def host(self):
        return self._host

    def _prep_wrapped_messages(self, client_info):
        # Precompute the wrapped methods.
        self._wrapped_methods = {
            self.add_access_config: gapic_v1.method.wrap_method(
                self.add_access_config,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.add_network_interface: gapic_v1.method.wrap_method(
                self.add_network_interface,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.add_resource_policies: gapic_v1.method.wrap_method(
                self.add_resource_policies,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.aggregated_list: gapic_v1.method.wrap_method(
                self.aggregated_list,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=600.0,
                ),
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.attach_disk: gapic_v1.method.wrap_method(
                self.attach_disk,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.bulk_insert: gapic_v1.method.wrap_method(
                self.bulk_insert,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.delete: gapic_v1.method.wrap_method(
                self.delete,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.delete_access_config: gapic_v1.method.wrap_method(
                self.delete_access_config,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.delete_network_interface: gapic_v1.method.wrap_method(
                self.delete_network_interface,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.detach_disk: gapic_v1.method.wrap_method(
                self.detach_disk,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.get: gapic_v1.method.wrap_method(
                self.get,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=600.0,
                ),
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.get_effective_firewalls: gapic_v1.method.wrap_method(
                self.get_effective_firewalls,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=600.0,
                ),
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.get_guest_attributes: gapic_v1.method.wrap_method(
                self.get_guest_attributes,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=600.0,
                ),
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.get_iam_policy: gapic_v1.method.wrap_method(
                self.get_iam_policy,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=600.0,
                ),
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.get_screenshot: gapic_v1.method.wrap_method(
                self.get_screenshot,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=600.0,
                ),
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.get_serial_port_output: gapic_v1.method.wrap_method(
                self.get_serial_port_output,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=600.0,
                ),
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.get_shielded_instance_identity: gapic_v1.method.wrap_method(
                self.get_shielded_instance_identity,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=600.0,
                ),
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.insert: gapic_v1.method.wrap_method(
                self.insert,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.list: gapic_v1.method.wrap_method(
                self.list,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=600.0,
                ),
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.list_referrers: gapic_v1.method.wrap_method(
                self.list_referrers,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=600.0,
                ),
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.perform_maintenance: gapic_v1.method.wrap_method(
                self.perform_maintenance,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.remove_resource_policies: gapic_v1.method.wrap_method(
                self.remove_resource_policies,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.report_host_as_faulty: gapic_v1.method.wrap_method(
                self.report_host_as_faulty,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.reset: gapic_v1.method.wrap_method(
                self.reset,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.resume: gapic_v1.method.wrap_method(
                self.resume,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.send_diagnostic_interrupt: gapic_v1.method.wrap_method(
                self.send_diagnostic_interrupt,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.set_deletion_protection: gapic_v1.method.wrap_method(
                self.set_deletion_protection,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.set_disk_auto_delete: gapic_v1.method.wrap_method(
                self.set_disk_auto_delete,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.set_iam_policy: gapic_v1.method.wrap_method(
                self.set_iam_policy,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.set_labels: gapic_v1.method.wrap_method(
                self.set_labels,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.set_machine_resources: gapic_v1.method.wrap_method(
                self.set_machine_resources,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.set_machine_type: gapic_v1.method.wrap_method(
                self.set_machine_type,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.set_metadata: gapic_v1.method.wrap_method(
                self.set_metadata,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.set_min_cpu_platform: gapic_v1.method.wrap_method(
                self.set_min_cpu_platform,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.set_name: gapic_v1.method.wrap_method(
                self.set_name,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.set_scheduling: gapic_v1.method.wrap_method(
                self.set_scheduling,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.set_security_policy: gapic_v1.method.wrap_method(
                self.set_security_policy,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.set_service_account: gapic_v1.method.wrap_method(
                self.set_service_account,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.set_shielded_instance_integrity_policy: gapic_v1.method.wrap_method(
                self.set_shielded_instance_integrity_policy,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.set_tags: gapic_v1.method.wrap_method(
                self.set_tags,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.simulate_maintenance_event: gapic_v1.method.wrap_method(
                self.simulate_maintenance_event,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.start: gapic_v1.method.wrap_method(
                self.start,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.start_with_encryption_key: gapic_v1.method.wrap_method(
                self.start_with_encryption_key,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.stop: gapic_v1.method.wrap_method(
                self.stop,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.suspend: gapic_v1.method.wrap_method(
                self.suspend,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.test_iam_permissions: gapic_v1.method.wrap_method(
                self.test_iam_permissions,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.update: gapic_v1.method.wrap_method(
                self.update,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.update_access_config: gapic_v1.method.wrap_method(
                self.update_access_config,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.update_display_device: gapic_v1.method.wrap_method(
                self.update_display_device,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.update_network_interface: gapic_v1.method.wrap_method(
                self.update_network_interface,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.update_shielded_instance_config: gapic_v1.method.wrap_method(
                self.update_shielded_instance_config,
                default_timeout=600.0,
                client_info=client_info,
            ),
        }

    def close(self):
        """Closes resources associated with the transport.

        .. warning::
             Only call this method if the transport is NOT shared
             with other clients - this may cause errors in other clients!
        """
        raise NotImplementedError()

    @property
    def add_access_config(
        self,
    ) -> Callable[
        [compute.AddAccessConfigInstanceRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def add_network_interface(
        self,
    ) -> Callable[
        [compute.AddNetworkInterfaceInstanceRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def add_resource_policies(
        self,
    ) -> Callable[
        [compute.AddResourcePoliciesInstanceRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def aggregated_list(
        self,
    ) -> Callable[
        [compute.AggregatedListInstancesRequest],
        Union[
            compute.InstanceAggregatedList, Awaitable[compute.InstanceAggregatedList]
        ],
    ]:
        raise NotImplementedError()

    @property
    def attach_disk(
        self,
    ) -> Callable[
        [compute.AttachDiskInstanceRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def bulk_insert(
        self,
    ) -> Callable[
        [compute.BulkInsertInstanceRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete(
        self,
    ) -> Callable[
        [compute.DeleteInstanceRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_access_config(
        self,
    ) -> Callable[
        [compute.DeleteAccessConfigInstanceRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_network_interface(
        self,
    ) -> Callable[
        [compute.DeleteNetworkInterfaceInstanceRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def detach_disk(
        self,
    ) -> Callable[
        [compute.DetachDiskInstanceRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get(
        self,
    ) -> Callable[
        [compute.GetInstanceRequest],
        Union[compute.Instance, Awaitable[compute.Instance]],
    ]:
        raise NotImplementedError()

    @property
    def get_effective_firewalls(
        self,
    ) -> Callable[
        [compute.GetEffectiveFirewallsInstanceRequest],
        Union[
            compute.InstancesGetEffectiveFirewallsResponse,
            Awaitable[compute.InstancesGetEffectiveFirewallsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_guest_attributes(
        self,
    ) -> Callable[
        [compute.GetGuestAttributesInstanceRequest],
        Union[compute.GuestAttributes, Awaitable[compute.GuestAttributes]],
    ]:
        raise NotImplementedError()

    @property
    def get_iam_policy(
        self,
    ) -> Callable[
        [compute.GetIamPolicyInstanceRequest],
        Union[compute.Policy, Awaitable[compute.Policy]],
    ]:
        raise NotImplementedError()

    @property
    def get_screenshot(
        self,
    ) -> Callable[
        [compute.GetScreenshotInstanceRequest],
        Union[compute.Screenshot, Awaitable[compute.Screenshot]],
    ]:
        raise NotImplementedError()

    @property
    def get_serial_port_output(
        self,
    ) -> Callable[
        [compute.GetSerialPortOutputInstanceRequest],
        Union[compute.SerialPortOutput, Awaitable[compute.SerialPortOutput]],
    ]:
        raise NotImplementedError()

    @property
    def get_shielded_instance_identity(
        self,
    ) -> Callable[
        [compute.GetShieldedInstanceIdentityInstanceRequest],
        Union[
            compute.ShieldedInstanceIdentity,
            Awaitable[compute.ShieldedInstanceIdentity],
        ],
    ]:
        raise NotImplementedError()

    @property
    def insert(
        self,
    ) -> Callable[
        [compute.InsertInstanceRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list(
        self,
    ) -> Callable[
        [compute.ListInstancesRequest],
        Union[compute.InstanceList, Awaitable[compute.InstanceList]],
    ]:
        raise NotImplementedError()

    @property
    def list_referrers(
        self,
    ) -> Callable[
        [compute.ListReferrersInstancesRequest],
        Union[compute.InstanceListReferrers, Awaitable[compute.InstanceListReferrers]],
    ]:
        raise NotImplementedError()

    @property
    def perform_maintenance(
        self,
    ) -> Callable[
        [compute.PerformMaintenanceInstanceRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def remove_resource_policies(
        self,
    ) -> Callable[
        [compute.RemoveResourcePoliciesInstanceRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def report_host_as_faulty(
        self,
    ) -> Callable[
        [compute.ReportHostAsFaultyInstanceRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def reset(
        self,
    ) -> Callable[
        [compute.ResetInstanceRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def resume(
        self,
    ) -> Callable[
        [compute.ResumeInstanceRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def send_diagnostic_interrupt(
        self,
    ) -> Callable[
        [compute.SendDiagnosticInterruptInstanceRequest],
        Union[
            compute.SendDiagnosticInterruptInstanceResponse,
            Awaitable[compute.SendDiagnosticInterruptInstanceResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def set_deletion_protection(
        self,
    ) -> Callable[
        [compute.SetDeletionProtectionInstanceRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def set_disk_auto_delete(
        self,
    ) -> Callable[
        [compute.SetDiskAutoDeleteInstanceRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def set_iam_policy(
        self,
    ) -> Callable[
        [compute.SetIamPolicyInstanceRequest],
        Union[compute.Policy, Awaitable[compute.Policy]],
    ]:
        raise NotImplementedError()

    @property
    def set_labels(
        self,
    ) -> Callable[
        [compute.SetLabelsInstanceRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def set_machine_resources(
        self,
    ) -> Callable[
        [compute.SetMachineResourcesInstanceRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def set_machine_type(
        self,
    ) -> Callable[
        [compute.SetMachineTypeInstanceRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def set_metadata(
        self,
    ) -> Callable[
        [compute.SetMetadataInstanceRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def set_min_cpu_platform(
        self,
    ) -> Callable[
        [compute.SetMinCpuPlatformInstanceRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def set_name(
        self,
    ) -> Callable[
        [compute.SetNameInstanceRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def set_scheduling(
        self,
    ) -> Callable[
        [compute.SetSchedulingInstanceRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def set_security_policy(
        self,
    ) -> Callable[
        [compute.SetSecurityPolicyInstanceRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def set_service_account(
        self,
    ) -> Callable[
        [compute.SetServiceAccountInstanceRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def set_shielded_instance_integrity_policy(
        self,
    ) -> Callable[
        [compute.SetShieldedInstanceIntegrityPolicyInstanceRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def set_tags(
        self,
    ) -> Callable[
        [compute.SetTagsInstanceRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def simulate_maintenance_event(
        self,
    ) -> Callable[
        [compute.SimulateMaintenanceEventInstanceRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def start(
        self,
    ) -> Callable[
        [compute.StartInstanceRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def start_with_encryption_key(
        self,
    ) -> Callable[
        [compute.StartWithEncryptionKeyInstanceRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def stop(
        self,
    ) -> Callable[
        [compute.StopInstanceRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def suspend(
        self,
    ) -> Callable[
        [compute.SuspendInstanceRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def test_iam_permissions(
        self,
    ) -> Callable[
        [compute.TestIamPermissionsInstanceRequest],
        Union[
            compute.TestPermissionsResponse, Awaitable[compute.TestPermissionsResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def update(
        self,
    ) -> Callable[
        [compute.UpdateInstanceRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_access_config(
        self,
    ) -> Callable[
        [compute.UpdateAccessConfigInstanceRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_display_device(
        self,
    ) -> Callable[
        [compute.UpdateDisplayDeviceInstanceRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_network_interface(
        self,
    ) -> Callable[
        [compute.UpdateNetworkInterfaceInstanceRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_shielded_instance_config(
        self,
    ) -> Callable[
        [compute.UpdateShieldedInstanceConfigInstanceRequest],
        Union[compute.Operation, Awaitable[compute.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def kind(self) -> str:
        raise NotImplementedError()

    @property
    def _zone_operations_client(self) -> zone_operations.ZoneOperationsClient:
        ex_op_service = self._extended_operations_services.get("zone_operations")
        if not ex_op_service:
            ex_op_service = zone_operations.ZoneOperationsClient(
                credentials=self._credentials,
                transport=self.kind,
            )
            self._extended_operations_services["zone_operations"] = ex_op_service

        return ex_op_service


__all__ = ("InstancesTransport",)
