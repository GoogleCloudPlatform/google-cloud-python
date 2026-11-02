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
    package="google.cloud.osconfig.v1alpha",
    manifest={
        "OSPolicy",
    },
)


class OSPolicy(proto.Message):
    r"""An OS policy defines the desired state configuration for a
    VM.

    Attributes:
        id (str):
            Required. The id of the OS policy with the following
            restrictions:

            - Must contain only lowercase letters, numbers, and hyphens.
            - Must start with a letter.
            - Must be between 1-63 characters.
            - Must end with a number or a letter.
            - Must be unique within the assignment.
        description (str):
            Policy description.
            Length of the description is limited to 1024
            characters.
        mode (google.cloud.osconfig_v1alpha.types.OSPolicy.Mode):
            Required. Policy mode
        resource_groups (MutableSequence[google.cloud.osconfig_v1alpha.types.OSPolicy.ResourceGroup]):
            Required. List of resource groups for the policy. For a
            particular VM, resource groups are evaluated in the order
            specified and the first resource group that is applicable is
            selected and the rest are ignored.

            If none of the resource groups are applicable for a VM, the
            VM is considered to be non-compliant w.r.t this policy. This
            behavior can be toggled by the flag
            ``allow_no_resource_group_match``
        allow_no_resource_group_match (bool):
            This flag determines the OS policy compliance status when
            none of the resource groups within the policy are applicable
            for a VM. Set this value to ``true`` if the policy needs to
            be reported as compliant even if the policy has nothing to
            validate or enforce.
    """

    class Mode(proto.Enum):
        r"""Policy mode

        Values:
            MODE_UNSPECIFIED (0):
                Invalid mode
            VALIDATION (1):
                This mode checks if the configuration
                resources in the policy are in their desired
                state. No actions are performed if they are not
                in the desired state. This mode is used for
                reporting purposes.
            ENFORCEMENT (2):
                This mode checks if the configuration
                resources in the policy are in their desired
                state, and if not, enforces the desired state.
        """

        MODE_UNSPECIFIED = 0
        VALIDATION = 1
        ENFORCEMENT = 2

    class OSFilter(proto.Message):
        r"""Filtering criteria to select VMs based on OS details.

        Attributes:
            os_short_name (str):
                This should match OS short name emitted by
                the OS inventory agent. An empty value matches
                any OS.
            os_version (str):
                This value should match the version emitted by the OS
                inventory agent. Prefix matches are supported if
                asterisk(\*) is provided as the last character. For example,
                to match all versions with a major version of ``7``, specify
                the following value for this field ``7.*``
        """

        os_short_name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        os_version: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class InventoryFilter(proto.Message):
        r"""Filtering criteria to select VMs based on inventory details.

        Attributes:
            os_short_name (str):
                Required. The OS short name
            os_version (str):
                The OS version

                Prefix matches are supported if asterisk(\*) is provided as
                the last character. For example, to match all versions with
                a major version of ``7``, specify the following value for
                this field ``7.*``

                An empty string matches all OS versions.
        """

        os_short_name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        os_version: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class Resource(proto.Message):
        r"""An OS policy resource is used to define the desired state
        configuration and provides a specific functionality like
        installing/removing packages, executing a script etc.

        The system ensures that resources are always in their desired
        state by taking necessary actions if they have drifted from
        their desired state.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            id (str):
                Required. The id of the resource with the following
                restrictions:

                - Must contain only lowercase letters, numbers, and hyphens.
                - Must start with a letter.
                - Must be between 1-63 characters.
                - Must end with a number or a letter.
                - Must be unique within the OS policy.
            pkg (google.cloud.osconfig_v1alpha.types.OSPolicy.Resource.PackageResource):
                Package resource

                This field is a member of `oneof`_ ``resource_type``.
            repository (google.cloud.osconfig_v1alpha.types.OSPolicy.Resource.RepositoryResource):
                Package repository resource

                This field is a member of `oneof`_ ``resource_type``.
            exec_ (google.cloud.osconfig_v1alpha.types.OSPolicy.Resource.ExecResource):
                Exec resource

                This field is a member of `oneof`_ ``resource_type``.
            file (google.cloud.osconfig_v1alpha.types.OSPolicy.Resource.FileResource):
                File resource

                This field is a member of `oneof`_ ``resource_type``.
        """

        class File(proto.Message):
            r"""A remote or local file.

            This message has `oneof`_ fields (mutually exclusive fields).
            For each oneof, at most one member field can be set at the same time.
            Setting any member of the oneof automatically clears all other
            members.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                remote (google.cloud.osconfig_v1alpha.types.OSPolicy.Resource.File.Remote):
                    A generic remote file.

                    This field is a member of `oneof`_ ``type``.
                gcs (google.cloud.osconfig_v1alpha.types.OSPolicy.Resource.File.Gcs):
                    A Cloud Storage object.

                    This field is a member of `oneof`_ ``type``.
                local_path (str):
                    A local path within the VM to use.

                    This field is a member of `oneof`_ ``type``.
                allow_insecure (bool):
                    Defaults to false. When false, files are
                    subject to validations based on the file type:

                    Remote: A checksum must be specified.
                    Cloud Storage: An object generation number must
                    be specified.
            """

            class Remote(proto.Message):
                r"""Specifies a file available via some URI.

                Attributes:
                    uri (str):
                        Required. URI from which to fetch the object. It should
                        contain both the protocol and path following the format
                        ``{protocol}://{location}``.
                    sha256_checksum (str):
                        SHA256 checksum of the remote file.
                """

                uri: str = proto.Field(
                    proto.STRING,
                    number=1,
                )
                sha256_checksum: str = proto.Field(
                    proto.STRING,
                    number=2,
                )

            class Gcs(proto.Message):
                r"""Specifies a file available as a Cloud Storage Object.

                Attributes:
                    bucket (str):
                        Required. Bucket of the Cloud Storage object.
                    object_ (str):
                        Required. Name of the Cloud Storage object.
                    generation (int):
                        Generation number of the Cloud Storage
                        object.
                """

                bucket: str = proto.Field(
                    proto.STRING,
                    number=1,
                )
                object_: str = proto.Field(
                    proto.STRING,
                    number=2,
                )
                generation: int = proto.Field(
                    proto.INT64,
                    number=3,
                )

            remote: "OSPolicy.Resource.File.Remote" = proto.Field(
                proto.MESSAGE,
                number=1,
                oneof="type",
                message="OSPolicy.Resource.File.Remote",
            )
            gcs: "OSPolicy.Resource.File.Gcs" = proto.Field(
                proto.MESSAGE,
                number=2,
                oneof="type",
                message="OSPolicy.Resource.File.Gcs",
            )
            local_path: str = proto.Field(
                proto.STRING,
                number=3,
                oneof="type",
            )
            allow_insecure: bool = proto.Field(
                proto.BOOL,
                number=4,
            )

        class PackageResource(proto.Message):
            r"""A resource that manages a system package.

            This message has `oneof`_ fields (mutually exclusive fields).
            For each oneof, at most one member field can be set at the same time.
            Setting any member of the oneof automatically clears all other
            members.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                desired_state (google.cloud.osconfig_v1alpha.types.OSPolicy.Resource.PackageResource.DesiredState):
                    Required. The desired state the agent should
                    maintain for this package.
                apt (google.cloud.osconfig_v1alpha.types.OSPolicy.Resource.PackageResource.APT):
                    A package managed by Apt.

                    This field is a member of `oneof`_ ``system_package``.
                deb (google.cloud.osconfig_v1alpha.types.OSPolicy.Resource.PackageResource.Deb):
                    A deb package file.

                    This field is a member of `oneof`_ ``system_package``.
                yum (google.cloud.osconfig_v1alpha.types.OSPolicy.Resource.PackageResource.YUM):
                    A package managed by YUM.

                    This field is a member of `oneof`_ ``system_package``.
                zypper (google.cloud.osconfig_v1alpha.types.OSPolicy.Resource.PackageResource.Zypper):
                    A package managed by Zypper.

                    This field is a member of `oneof`_ ``system_package``.
                rpm (google.cloud.osconfig_v1alpha.types.OSPolicy.Resource.PackageResource.RPM):
                    An rpm package file.

                    This field is a member of `oneof`_ ``system_package``.
                googet (google.cloud.osconfig_v1alpha.types.OSPolicy.Resource.PackageResource.GooGet):
                    A package managed by GooGet.

                    This field is a member of `oneof`_ ``system_package``.
                msi (google.cloud.osconfig_v1alpha.types.OSPolicy.Resource.PackageResource.MSI):
                    An MSI package.

                    This field is a member of `oneof`_ ``system_package``.
            """

            class DesiredState(proto.Enum):
                r"""The desired state that the OS Config agent maintains on the
                VM.

                Values:
                    DESIRED_STATE_UNSPECIFIED (0):
                        Unspecified is invalid.
                    INSTALLED (1):
                        Ensure that the package is installed.
                    REMOVED (2):
                        The agent ensures that the package is not
                        installed and uninstalls it if detected.
                """

                DESIRED_STATE_UNSPECIFIED = 0
                INSTALLED = 1
                REMOVED = 2

            class Deb(proto.Message):
                r"""A deb package file. dpkg packages only support INSTALLED
                state.

                Attributes:
                    source (google.cloud.osconfig_v1alpha.types.OSPolicy.Resource.File):
                        Required. A deb package.
                    pull_deps (bool):
                        Whether dependencies should also be installed.

                        - install when false: ``dpkg -i package``
                        - install when true:
                          ``apt-get update && apt-get -y install package.deb``
                """

                source: "OSPolicy.Resource.File" = proto.Field(
                    proto.MESSAGE,
                    number=1,
                    message="OSPolicy.Resource.File",
                )
                pull_deps: bool = proto.Field(
                    proto.BOOL,
                    number=2,
                )

            class APT(proto.Message):
                r"""A package managed by APT.

                - install: ``apt-get update && apt-get -y install [name]``
                - remove: ``apt-get -y remove [name]``

                Attributes:
                    name (str):
                        Required. Package name.
                """

                name: str = proto.Field(
                    proto.STRING,
                    number=1,
                )

            class RPM(proto.Message):
                r"""An RPM package file. RPM packages only support INSTALLED
                state.

                Attributes:
                    source (google.cloud.osconfig_v1alpha.types.OSPolicy.Resource.File):
                        Required. An rpm package.
                    pull_deps (bool):
                        Whether dependencies should also be installed.

                        - install when false:
                          ``rpm --upgrade --replacepkgs package.rpm``
                        - install when true: ``yum -y install package.rpm`` or
                          ``zypper -y install package.rpm``
                """

                source: "OSPolicy.Resource.File" = proto.Field(
                    proto.MESSAGE,
                    number=1,
                    message="OSPolicy.Resource.File",
                )
                pull_deps: bool = proto.Field(
                    proto.BOOL,
                    number=2,
                )

            class YUM(proto.Message):
                r"""A package managed by YUM.

                - install: ``yum -y install package``
                - remove: ``yum -y remove package``

                Attributes:
                    name (str):
                        Required. Package name.
                """

                name: str = proto.Field(
                    proto.STRING,
                    number=1,
                )

            class Zypper(proto.Message):
                r"""A package managed by Zypper.

                - install: ``zypper -y install package``
                - remove: ``zypper -y rm package``

                Attributes:
                    name (str):
                        Required. Package name.
                """

                name: str = proto.Field(
                    proto.STRING,
                    number=1,
                )

            class GooGet(proto.Message):
                r"""A package managed by GooGet.

                - install: ``googet -noconfirm install package``
                - remove: ``googet -noconfirm remove package``

                Attributes:
                    name (str):
                        Required. Package name.
                """

                name: str = proto.Field(
                    proto.STRING,
                    number=1,
                )

            class MSI(proto.Message):
                r"""An MSI package. MSI packages only support INSTALLED state.

                Attributes:
                    source (google.cloud.osconfig_v1alpha.types.OSPolicy.Resource.File):
                        Required. The MSI package.
                    properties (MutableSequence[str]):
                        Additional properties to use during installation. This
                        should be in the format of Property=Setting. Appended to the
                        defaults of ``ACTION=INSTALL REBOOT=ReallySuppress``.
                """

                source: "OSPolicy.Resource.File" = proto.Field(
                    proto.MESSAGE,
                    number=1,
                    message="OSPolicy.Resource.File",
                )
                properties: MutableSequence[str] = proto.RepeatedField(
                    proto.STRING,
                    number=2,
                )

            desired_state: "OSPolicy.Resource.PackageResource.DesiredState" = (
                proto.Field(
                    proto.ENUM,
                    number=1,
                    enum="OSPolicy.Resource.PackageResource.DesiredState",
                )
            )
            apt: "OSPolicy.Resource.PackageResource.APT" = proto.Field(
                proto.MESSAGE,
                number=2,
                oneof="system_package",
                message="OSPolicy.Resource.PackageResource.APT",
            )
            deb: "OSPolicy.Resource.PackageResource.Deb" = proto.Field(
                proto.MESSAGE,
                number=3,
                oneof="system_package",
                message="OSPolicy.Resource.PackageResource.Deb",
            )
            yum: "OSPolicy.Resource.PackageResource.YUM" = proto.Field(
                proto.MESSAGE,
                number=4,
                oneof="system_package",
                message="OSPolicy.Resource.PackageResource.YUM",
            )
            zypper: "OSPolicy.Resource.PackageResource.Zypper" = proto.Field(
                proto.MESSAGE,
                number=5,
                oneof="system_package",
                message="OSPolicy.Resource.PackageResource.Zypper",
            )
            rpm: "OSPolicy.Resource.PackageResource.RPM" = proto.Field(
                proto.MESSAGE,
                number=6,
                oneof="system_package",
                message="OSPolicy.Resource.PackageResource.RPM",
            )
            googet: "OSPolicy.Resource.PackageResource.GooGet" = proto.Field(
                proto.MESSAGE,
                number=7,
                oneof="system_package",
                message="OSPolicy.Resource.PackageResource.GooGet",
            )
            msi: "OSPolicy.Resource.PackageResource.MSI" = proto.Field(
                proto.MESSAGE,
                number=8,
                oneof="system_package",
                message="OSPolicy.Resource.PackageResource.MSI",
            )

        class RepositoryResource(proto.Message):
            r"""A resource that manages a package repository.

            This message has `oneof`_ fields (mutually exclusive fields).
            For each oneof, at most one member field can be set at the same time.
            Setting any member of the oneof automatically clears all other
            members.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                apt (google.cloud.osconfig_v1alpha.types.OSPolicy.Resource.RepositoryResource.AptRepository):
                    An Apt Repository.

                    This field is a member of `oneof`_ ``repository``.
                yum (google.cloud.osconfig_v1alpha.types.OSPolicy.Resource.RepositoryResource.YumRepository):
                    A Yum Repository.

                    This field is a member of `oneof`_ ``repository``.
                zypper (google.cloud.osconfig_v1alpha.types.OSPolicy.Resource.RepositoryResource.ZypperRepository):
                    A Zypper Repository.

                    This field is a member of `oneof`_ ``repository``.
                goo (google.cloud.osconfig_v1alpha.types.OSPolicy.Resource.RepositoryResource.GooRepository):
                    A Goo Repository.

                    This field is a member of `oneof`_ ``repository``.
            """

            class AptRepository(proto.Message):
                r"""Represents a single apt package repository. These will be added to a
                repo file that will be managed at
                ``/etc/apt/sources.list.d/google_osconfig.list``.

                Attributes:
                    archive_type (google.cloud.osconfig_v1alpha.types.OSPolicy.Resource.RepositoryResource.AptRepository.ArchiveType):
                        Required. Type of archive files in this
                        repository.
                    uri (str):
                        Required. URI for this repository.
                    distribution (str):
                        Required. Distribution of this repository.
                    components (MutableSequence[str]):
                        Required. List of components for this
                        repository. Must contain at least one item.
                    gpg_key (str):
                        URI of the key file for this repository. The agent maintains
                        a keyring at
                        ``/etc/apt/trusted.gpg.d/osconfig_agent_managed.gpg``.
                """

                class ArchiveType(proto.Enum):
                    r"""Type of archive.

                    Values:
                        ARCHIVE_TYPE_UNSPECIFIED (0):
                            Unspecified is invalid.
                        DEB (1):
                            Deb indicates that the archive contains
                            binary files.
                        DEB_SRC (2):
                            Deb-src indicates that the archive contains
                            source files.
                    """

                    ARCHIVE_TYPE_UNSPECIFIED = 0
                    DEB = 1
                    DEB_SRC = 2

                archive_type: "OSPolicy.Resource.RepositoryResource.AptRepository.ArchiveType" = proto.Field(
                    proto.ENUM,
                    number=1,
                    enum="OSPolicy.Resource.RepositoryResource.AptRepository.ArchiveType",
                )
                uri: str = proto.Field(
                    proto.STRING,
                    number=2,
                )
                distribution: str = proto.Field(
                    proto.STRING,
                    number=3,
                )
                components: MutableSequence[str] = proto.RepeatedField(
                    proto.STRING,
                    number=4,
                )
                gpg_key: str = proto.Field(
                    proto.STRING,
                    number=5,
                )

            class YumRepository(proto.Message):
                r"""Represents a single yum package repository. These are added to a
                repo file that is managed at
                ``/etc/yum.repos.d/google_osconfig.repo``.

                Attributes:
                    id (str):
                        Required. A one word, unique name for this repository. This
                        is the ``repo id`` in the yum config file and also the
                        ``display_name`` if ``display_name`` is omitted. This id is
                        also used as the unique identifier when checking for
                        resource conflicts.
                    display_name (str):
                        The display name of the repository.
                    base_url (str):
                        Required. The location of the repository
                        directory.
                    gpg_keys (MutableSequence[str]):
                        URIs of GPG keys.
                """

                id: str = proto.Field(
                    proto.STRING,
                    number=1,
                )
                display_name: str = proto.Field(
                    proto.STRING,
                    number=2,
                )
                base_url: str = proto.Field(
                    proto.STRING,
                    number=3,
                )
                gpg_keys: MutableSequence[str] = proto.RepeatedField(
                    proto.STRING,
                    number=4,
                )

            class ZypperRepository(proto.Message):
                r"""Represents a single zypper package repository. These are added to a
                repo file that is managed at
                ``/etc/zypp/repos.d/google_osconfig.repo``.

                Attributes:
                    id (str):
                        Required. A one word, unique name for this repository. This
                        is the ``repo id`` in the zypper config file and also the
                        ``display_name`` if ``display_name`` is omitted. This id is
                        also used as the unique identifier when checking for
                        GuestPolicy conflicts.
                    display_name (str):
                        The display name of the repository.
                    base_url (str):
                        Required. The location of the repository
                        directory.
                    gpg_keys (MutableSequence[str]):
                        URIs of GPG keys.
                """

                id: str = proto.Field(
                    proto.STRING,
                    number=1,
                )
                display_name: str = proto.Field(
                    proto.STRING,
                    number=2,
                )
                base_url: str = proto.Field(
                    proto.STRING,
                    number=3,
                )
                gpg_keys: MutableSequence[str] = proto.RepeatedField(
                    proto.STRING,
                    number=4,
                )

            class GooRepository(proto.Message):
                r"""Represents a Goo package repository. These are added to a repo file
                that is managed at
                ``C:/ProgramData/GooGet/repos/google_osconfig.repo``.

                Attributes:
                    name (str):
                        Required. The name of the repository.
                    url (str):
                        Required. The url of the repository.
                """

                name: str = proto.Field(
                    proto.STRING,
                    number=1,
                )
                url: str = proto.Field(
                    proto.STRING,
                    number=2,
                )

            apt: "OSPolicy.Resource.RepositoryResource.AptRepository" = proto.Field(
                proto.MESSAGE,
                number=1,
                oneof="repository",
                message="OSPolicy.Resource.RepositoryResource.AptRepository",
            )
            yum: "OSPolicy.Resource.RepositoryResource.YumRepository" = proto.Field(
                proto.MESSAGE,
                number=2,
                oneof="repository",
                message="OSPolicy.Resource.RepositoryResource.YumRepository",
            )
            zypper: "OSPolicy.Resource.RepositoryResource.ZypperRepository" = (
                proto.Field(
                    proto.MESSAGE,
                    number=3,
                    oneof="repository",
                    message="OSPolicy.Resource.RepositoryResource.ZypperRepository",
                )
            )
            goo: "OSPolicy.Resource.RepositoryResource.GooRepository" = proto.Field(
                proto.MESSAGE,
                number=4,
                oneof="repository",
                message="OSPolicy.Resource.RepositoryResource.GooRepository",
            )

        class ExecResource(proto.Message):
            r"""A resource that allows executing scripts on the VM.

            The ``ExecResource`` has 2 stages: ``validate`` and ``enforce`` and
            both stages accept a script as an argument to execute.

            When the ``ExecResource`` is applied by the agent, it first executes
            the script in the ``validate`` stage. The ``validate`` stage can
            signal that the ``ExecResource`` is already in the desired state by
            returning an exit code of ``100``. If the ``ExecResource`` is not in
            the desired state, it should return an exit code of ``101``. Any
            other exit code returned by this stage is considered an error.

            If the ``ExecResource`` is not in the desired state based on the
            exit code from the ``validate`` stage, the agent proceeds to execute
            the script from the ``enforce`` stage. If the ``ExecResource`` is
            already in the desired state, the ``enforce`` stage will not be run.
            Similar to ``validate`` stage, the ``enforce`` stage should return
            an exit code of ``100`` to indicate that the resource in now in its
            desired state. Any other exit code is considered an error.

            NOTE: An exit code of ``100`` was chosen over ``0`` (and ``101`` vs
            ``1``) to have an explicit indicator of ``in desired state``,
            ``not in desired state`` and errors. Because, for example,
            Powershell will always return an exit code of ``0`` unless an
            ``exit`` statement is provided in the script. So, for reasons of
            consistency and being explicit, exit codes ``100`` and ``101`` were
            chosen.

            Attributes:
                validate (google.cloud.osconfig_v1alpha.types.OSPolicy.Resource.ExecResource.Exec):
                    Required. What to run to validate this
                    resource is in the desired state. An exit code
                    of 100 indicates "in desired state", and exit
                    code of 101 indicates "not in desired state".
                    Any other exit code indicates a failure running
                    validate.
                enforce (google.cloud.osconfig_v1alpha.types.OSPolicy.Resource.ExecResource.Exec):
                    What to run to bring this resource into the
                    desired state. An exit code of 100 indicates
                    "success", any other exit code indicates a
                    failure running enforce.
            """

            class Exec(proto.Message):
                r"""A file or script to execute.

                This message has `oneof`_ fields (mutually exclusive fields).
                For each oneof, at most one member field can be set at the same time.
                Setting any member of the oneof automatically clears all other
                members.

                .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

                Attributes:
                    file (google.cloud.osconfig_v1alpha.types.OSPolicy.Resource.File):
                        A remote or local file.

                        This field is a member of `oneof`_ ``source``.
                    script (str):
                        An inline script.
                        The size of the script is limited to 1024
                        characters.

                        This field is a member of `oneof`_ ``source``.
                    args (MutableSequence[str]):
                        Optional arguments to pass to the source
                        during execution.
                    interpreter (google.cloud.osconfig_v1alpha.types.OSPolicy.Resource.ExecResource.Exec.Interpreter):
                        Required. The script interpreter to use.
                    output_file_path (str):
                        Only recorded for enforce Exec.
                        Path to an output file (that is created by this
                        Exec) whose content will be recorded in
                        OSPolicyResourceCompliance after a successful
                        run. Absence or failure to read this file will
                        result in this ExecResource being non-compliant.
                        Output file size is limited to 100K bytes.
                """

                class Interpreter(proto.Enum):
                    r"""The interpreter to use.

                    Values:
                        INTERPRETER_UNSPECIFIED (0):
                            Invalid value, the request will return
                            validation error.
                        NONE (1):
                            If an interpreter is not specified, the source is executed
                            directly. This execution, without an interpreter, only
                            succeeds for executables and scripts that have shebang
                            lines.
                        SHELL (2):
                            Indicates that the script runs with ``/bin/sh`` on Linux and
                            ``cmd.exe`` on Windows.
                        POWERSHELL (3):
                            Indicates that the script runs with
                            PowerShell.
                    """

                    INTERPRETER_UNSPECIFIED = 0
                    NONE = 1
                    SHELL = 2
                    POWERSHELL = 3

                file: "OSPolicy.Resource.File" = proto.Field(
                    proto.MESSAGE,
                    number=1,
                    oneof="source",
                    message="OSPolicy.Resource.File",
                )
                script: str = proto.Field(
                    proto.STRING,
                    number=2,
                    oneof="source",
                )
                args: MutableSequence[str] = proto.RepeatedField(
                    proto.STRING,
                    number=3,
                )
                interpreter: "OSPolicy.Resource.ExecResource.Exec.Interpreter" = (
                    proto.Field(
                        proto.ENUM,
                        number=4,
                        enum="OSPolicy.Resource.ExecResource.Exec.Interpreter",
                    )
                )
                output_file_path: str = proto.Field(
                    proto.STRING,
                    number=5,
                )

            validate: "OSPolicy.Resource.ExecResource.Exec" = proto.Field(
                proto.MESSAGE,
                number=1,
                message="OSPolicy.Resource.ExecResource.Exec",
            )
            enforce: "OSPolicy.Resource.ExecResource.Exec" = proto.Field(
                proto.MESSAGE,
                number=2,
                message="OSPolicy.Resource.ExecResource.Exec",
            )

        class FileResource(proto.Message):
            r"""A resource that manages the state of a file.

            This message has `oneof`_ fields (mutually exclusive fields).
            For each oneof, at most one member field can be set at the same time.
            Setting any member of the oneof automatically clears all other
            members.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                file (google.cloud.osconfig_v1alpha.types.OSPolicy.Resource.File):
                    A remote or local source.

                    This field is a member of `oneof`_ ``source``.
                content (str):
                    A a file with this content.
                    The size of the content is limited to 1024
                    characters.

                    This field is a member of `oneof`_ ``source``.
                path (str):
                    Required. The absolute path of the file
                    within the VM.
                state (google.cloud.osconfig_v1alpha.types.OSPolicy.Resource.FileResource.DesiredState):
                    Required. Desired state of the file.
                permissions (str):
                    Consists of three octal digits which
                    represent, in order, the permissions of the
                    owner, group, and other users for the file
                    (similarly to the numeric mode used in the linux
                    chmod utility). Each digit represents a three
                    bit number with the 4 bit corresponding to the
                    read permissions, the 2 bit corresponds to the
                    write bit, and the one bit corresponds to the
                    execute permission. Default behavior is 755.

                    Below are some examples of permissions and their
                    associated values:

                    read, write, and execute: 7
                    read and execute: 5
                    read and write: 6
                    read only: 4
            """

            class DesiredState(proto.Enum):
                r"""Desired state of the file.

                Values:
                    DESIRED_STATE_UNSPECIFIED (0):
                        Unspecified is invalid.
                    PRESENT (1):
                        Ensure file at path is present.
                    ABSENT (2):
                        Ensure file at path is absent.
                    CONTENTS_MATCH (3):
                        Ensure the contents of the file at path
                        matches. If the file does not exist it will be
                        created.
                """

                DESIRED_STATE_UNSPECIFIED = 0
                PRESENT = 1
                ABSENT = 2
                CONTENTS_MATCH = 3

            file: "OSPolicy.Resource.File" = proto.Field(
                proto.MESSAGE,
                number=1,
                oneof="source",
                message="OSPolicy.Resource.File",
            )
            content: str = proto.Field(
                proto.STRING,
                number=2,
                oneof="source",
            )
            path: str = proto.Field(
                proto.STRING,
                number=3,
            )
            state: "OSPolicy.Resource.FileResource.DesiredState" = proto.Field(
                proto.ENUM,
                number=4,
                enum="OSPolicy.Resource.FileResource.DesiredState",
            )
            permissions: str = proto.Field(
                proto.STRING,
                number=5,
            )

        id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        pkg: "OSPolicy.Resource.PackageResource" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="resource_type",
            message="OSPolicy.Resource.PackageResource",
        )
        repository: "OSPolicy.Resource.RepositoryResource" = proto.Field(
            proto.MESSAGE,
            number=3,
            oneof="resource_type",
            message="OSPolicy.Resource.RepositoryResource",
        )
        exec_: "OSPolicy.Resource.ExecResource" = proto.Field(
            proto.MESSAGE,
            number=4,
            oneof="resource_type",
            message="OSPolicy.Resource.ExecResource",
        )
        file: "OSPolicy.Resource.FileResource" = proto.Field(
            proto.MESSAGE,
            number=5,
            oneof="resource_type",
            message="OSPolicy.Resource.FileResource",
        )

    class ResourceGroup(proto.Message):
        r"""Resource groups provide a mechanism to group OS policy resources.

        Resource groups enable OS policy authors to create a single OS
        policy to be applied to VMs running different operating Systems.

        When the OS policy is applied to a target VM, the appropriate
        resource group within the OS policy is selected based on the
        ``OSFilter`` specified within the resource group.

        Attributes:
            os_filter (google.cloud.osconfig_v1alpha.types.OSPolicy.OSFilter):
                Deprecated. Use the ``inventory_filters`` field instead.
                Used to specify the OS filter for a resource group
            inventory_filters (MutableSequence[google.cloud.osconfig_v1alpha.types.OSPolicy.InventoryFilter]):
                List of inventory filters for the resource group.

                The resources in this resource group are applied to the
                target VM if it satisfies at least one of the following
                inventory filters.

                For example, to apply this resource group to VMs running
                either ``RHEL`` or ``CentOS`` operating systems, specify 2
                items for the list with following values:
                inventory_filters[0].os_short_name='rhel' and
                inventory_filters[1].os_short_name='centos'

                If the list is empty, this resource group will be applied to
                the target VM unconditionally.
            resources (MutableSequence[google.cloud.osconfig_v1alpha.types.OSPolicy.Resource]):
                Required. List of resources configured for
                this resource group. The resources are executed
                in the exact order specified here.
        """

        os_filter: "OSPolicy.OSFilter" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="OSPolicy.OSFilter",
        )
        inventory_filters: MutableSequence["OSPolicy.InventoryFilter"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=3,
                message="OSPolicy.InventoryFilter",
            )
        )
        resources: MutableSequence["OSPolicy.Resource"] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="OSPolicy.Resource",
        )

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    mode: Mode = proto.Field(
        proto.ENUM,
        number=3,
        enum=Mode,
    )
    resource_groups: MutableSequence[ResourceGroup] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=ResourceGroup,
    )
    allow_no_resource_group_match: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
