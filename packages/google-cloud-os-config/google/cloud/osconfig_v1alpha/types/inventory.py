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

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.type.date_pb2 as date_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.osconfig.v1alpha",
    manifest={
        "InventoryView",
        "Inventory",
        "GetInventoryRequest",
        "ListInventoriesRequest",
        "ListInventoriesResponse",
    },
)


class InventoryView(proto.Enum):
    r"""The view for inventory objects.

    Values:
        INVENTORY_VIEW_UNSPECIFIED (0):
            The default value.
            The API defaults to the BASIC view.
        BASIC (1):
            Returns the basic inventory information that includes
            ``os_info``.
        FULL (2):
            Returns all fields.
    """

    INVENTORY_VIEW_UNSPECIFIED = 0
    BASIC = 1
    FULL = 2


class Inventory(proto.Message):
    r"""This API resource represents the available inventory data for a
    Compute Engine virtual machine (VM) instance at a given point in
    time.

    You can use this API resource to determine the inventory data of
    your VM.

    For more information, see `Information provided by OS inventory
    management <https://cloud.google.com/compute/docs/instances/os-inventory-management#data-collected>`__.

    Attributes:
        name (str):
            Output only. The ``Inventory`` API resource name.

            Format:
            ``projects/{project_number}/locations/{location}/instances/{instance_id}/inventory``
        os_info (google.cloud.osconfig_v1alpha.types.Inventory.OsInfo):
            Output only. Base level operating system
            information for the VM.
        items (MutableMapping[str, google.cloud.osconfig_v1alpha.types.Inventory.Item]):
            Output only. Inventory items related to the
            VM keyed by an opaque unique identifier for each
            inventory item. The identifier is unique to each
            distinct and addressable inventory item and will
            change, when there is a new package version.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp of the last reported
            inventory for the VM.
    """

    class OsInfo(proto.Message):
        r"""Operating system information for the VM.

        Attributes:
            hostname (str):
                The VM hostname.
            long_name (str):
                The operating system long name.
                For example 'Debian GNU/Linux 9' or 'Microsoft
                Window Server 2019 Datacenter'.
            short_name (str):
                The operating system short name.
                For example, 'windows' or 'debian'.
            version (str):
                The version of the operating system.
            architecture (str):
                The system architecture of the operating
                system.
            kernel_version (str):
                The kernel version of the operating system.
            kernel_release (str):
                The kernel release of the operating system.
            osconfig_agent_version (str):
                The current version of the OS Config agent
                running on the VM.
        """

        hostname: str = proto.Field(
            proto.STRING,
            number=9,
        )
        long_name: str = proto.Field(
            proto.STRING,
            number=2,
        )
        short_name: str = proto.Field(
            proto.STRING,
            number=3,
        )
        version: str = proto.Field(
            proto.STRING,
            number=4,
        )
        architecture: str = proto.Field(
            proto.STRING,
            number=5,
        )
        kernel_version: str = proto.Field(
            proto.STRING,
            number=6,
        )
        kernel_release: str = proto.Field(
            proto.STRING,
            number=7,
        )
        osconfig_agent_version: str = proto.Field(
            proto.STRING,
            number=8,
        )

    class Item(proto.Message):
        r"""A single piece of inventory on a VM.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            id (str):
                Identifier for this item, unique across items
                for this VM.
            origin_type (google.cloud.osconfig_v1alpha.types.Inventory.Item.OriginType):
                The origin of this inventory item.
            create_time (google.protobuf.timestamp_pb2.Timestamp):
                When this inventory item was first detected.
            update_time (google.protobuf.timestamp_pb2.Timestamp):
                When this inventory item was last modified.
            type_ (google.cloud.osconfig_v1alpha.types.Inventory.Item.Type):
                The specific type of inventory, correlating
                to its specific details.
            installed_package (google.cloud.osconfig_v1alpha.types.Inventory.SoftwarePackage):
                Software package present on the VM instance.

                This field is a member of `oneof`_ ``details``.
            available_package (google.cloud.osconfig_v1alpha.types.Inventory.SoftwarePackage):
                Software package available to be installed on
                the VM instance.

                This field is a member of `oneof`_ ``details``.
        """

        class OriginType(proto.Enum):
            r"""The origin of a specific inventory item.

            Values:
                ORIGIN_TYPE_UNSPECIFIED (0):
                    Invalid. An origin type must be specified.
                INVENTORY_REPORT (1):
                    This inventory item was discovered as the
                    result of the agent reporting inventory via the
                    reporting API.
            """

            ORIGIN_TYPE_UNSPECIFIED = 0
            INVENTORY_REPORT = 1

        class Type(proto.Enum):
            r"""The different types of inventory that are tracked on a VM.

            Values:
                TYPE_UNSPECIFIED (0):
                    Invalid. An type must be specified.
                INSTALLED_PACKAGE (1):
                    This represents a package that is installed
                    on the VM.
                AVAILABLE_PACKAGE (2):
                    This represents an update that is available
                    for a package.
            """

            TYPE_UNSPECIFIED = 0
            INSTALLED_PACKAGE = 1
            AVAILABLE_PACKAGE = 2

        id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        origin_type: "Inventory.Item.OriginType" = proto.Field(
            proto.ENUM,
            number=2,
            enum="Inventory.Item.OriginType",
        )
        create_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=8,
            message=timestamp_pb2.Timestamp,
        )
        update_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=9,
            message=timestamp_pb2.Timestamp,
        )
        type_: "Inventory.Item.Type" = proto.Field(
            proto.ENUM,
            number=5,
            enum="Inventory.Item.Type",
        )
        installed_package: "Inventory.SoftwarePackage" = proto.Field(
            proto.MESSAGE,
            number=6,
            oneof="details",
            message="Inventory.SoftwarePackage",
        )
        available_package: "Inventory.SoftwarePackage" = proto.Field(
            proto.MESSAGE,
            number=7,
            oneof="details",
            message="Inventory.SoftwarePackage",
        )

    class SoftwarePackage(proto.Message):
        r"""Software package information of the operating system.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            yum_package (google.cloud.osconfig_v1alpha.types.Inventory.VersionedPackage):
                Yum package info. For details about the yum package manager,
                see
                https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/deployment_guide/ch-yum.

                This field is a member of `oneof`_ ``details``.
            apt_package (google.cloud.osconfig_v1alpha.types.Inventory.VersionedPackage):
                Details of an APT package.
                For details about the apt package manager, see
                https://wiki.debian.org/Apt.

                This field is a member of `oneof`_ ``details``.
            zypper_package (google.cloud.osconfig_v1alpha.types.Inventory.VersionedPackage):
                Details of a Zypper package. For details about the Zypper
                package manager, see
                https://en.opensuse.org/SDB:Zypper_manual.

                This field is a member of `oneof`_ ``details``.
            googet_package (google.cloud.osconfig_v1alpha.types.Inventory.VersionedPackage):
                Details of a Googet package.
                For details about the googet package manager,
                see  https://github.com/google/googet.

                This field is a member of `oneof`_ ``details``.
            zypper_patch (google.cloud.osconfig_v1alpha.types.Inventory.ZypperPatch):
                Details of a Zypper patch. For details about the Zypper
                package manager, see
                https://en.opensuse.org/SDB:Zypper_manual.

                This field is a member of `oneof`_ ``details``.
            wua_package (google.cloud.osconfig_v1alpha.types.Inventory.WindowsUpdatePackage):
                Details of a Windows Update package. See
                https://docs.microsoft.com/en-us/windows/win32/api/\_wua/
                for information about Windows Update.

                This field is a member of `oneof`_ ``details``.
            qfe_package (google.cloud.osconfig_v1alpha.types.Inventory.WindowsQuickFixEngineeringPackage):
                Details of a Windows Quick Fix engineering
                package. See
                https://docs.microsoft.com/en-us/windows/win32/cimwin32prov/win32-quickfixengineering
                for info in Windows Quick Fix Engineering.

                This field is a member of `oneof`_ ``details``.
            cos_package (google.cloud.osconfig_v1alpha.types.Inventory.VersionedPackage):
                Details of a COS package.

                This field is a member of `oneof`_ ``details``.
            windows_application (google.cloud.osconfig_v1alpha.types.Inventory.WindowsApplication):
                Details of Windows Application.

                This field is a member of `oneof`_ ``details``.
        """

        yum_package: "Inventory.VersionedPackage" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="details",
            message="Inventory.VersionedPackage",
        )
        apt_package: "Inventory.VersionedPackage" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="details",
            message="Inventory.VersionedPackage",
        )
        zypper_package: "Inventory.VersionedPackage" = proto.Field(
            proto.MESSAGE,
            number=3,
            oneof="details",
            message="Inventory.VersionedPackage",
        )
        googet_package: "Inventory.VersionedPackage" = proto.Field(
            proto.MESSAGE,
            number=4,
            oneof="details",
            message="Inventory.VersionedPackage",
        )
        zypper_patch: "Inventory.ZypperPatch" = proto.Field(
            proto.MESSAGE,
            number=5,
            oneof="details",
            message="Inventory.ZypperPatch",
        )
        wua_package: "Inventory.WindowsUpdatePackage" = proto.Field(
            proto.MESSAGE,
            number=6,
            oneof="details",
            message="Inventory.WindowsUpdatePackage",
        )
        qfe_package: "Inventory.WindowsQuickFixEngineeringPackage" = proto.Field(
            proto.MESSAGE,
            number=7,
            oneof="details",
            message="Inventory.WindowsQuickFixEngineeringPackage",
        )
        cos_package: "Inventory.VersionedPackage" = proto.Field(
            proto.MESSAGE,
            number=8,
            oneof="details",
            message="Inventory.VersionedPackage",
        )
        windows_application: "Inventory.WindowsApplication" = proto.Field(
            proto.MESSAGE,
            number=9,
            oneof="details",
            message="Inventory.WindowsApplication",
        )

    class VersionedPackage(proto.Message):
        r"""Information related to the a standard versioned package.
        This includes package info for APT, Yum, Zypper, and Googet
        package managers.

        Attributes:
            package_name (str):
                The name of the package.
            architecture (str):
                The system architecture this package is
                intended for.
            version (str):
                The version of the package.
        """

        package_name: str = proto.Field(
            proto.STRING,
            number=4,
        )
        architecture: str = proto.Field(
            proto.STRING,
            number=2,
        )
        version: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class ZypperPatch(proto.Message):
        r"""Details related to a Zypper Patch.

        Attributes:
            patch_name (str):
                The name of the patch.
            category (str):
                The category of the patch.
            severity (str):
                The severity specified for this patch
            summary (str):
                Any summary information provided about this
                patch.
        """

        patch_name: str = proto.Field(
            proto.STRING,
            number=5,
        )
        category: str = proto.Field(
            proto.STRING,
            number=2,
        )
        severity: str = proto.Field(
            proto.STRING,
            number=3,
        )
        summary: str = proto.Field(
            proto.STRING,
            number=4,
        )

    class WindowsUpdatePackage(proto.Message):
        r"""Details related to a Windows Update package. Field data and names
        are taken from Windows Update API IUpdate Interface:
        https://docs.microsoft.com/en-us/windows/win32/api/\_wua/
        Descriptive fields like title, and description are localized based
        on the locale of the VM being updated.

        Attributes:
            title (str):
                The localized title of the update package.
            description (str):
                The localized description of the update
                package.
            categories (MutableSequence[google.cloud.osconfig_v1alpha.types.Inventory.WindowsUpdatePackage.WindowsUpdateCategory]):
                The categories that are associated with this
                update package.
            kb_article_ids (MutableSequence[str]):
                A collection of Microsoft Knowledge Base
                article IDs that are associated with the update
                package.
            support_url (str):
                A hyperlink to the language-specific support
                information for the update.
            more_info_urls (MutableSequence[str]):
                A collection of URLs that provide more
                information about the update package.
            update_id (str):
                Gets the identifier of an update package.
                Stays the same across revisions.
            revision_number (int):
                The revision number of this update package.
            last_deployment_change_time (google.protobuf.timestamp_pb2.Timestamp):
                The last published date of the update, in
                (UTC) date and time.
        """

        class WindowsUpdateCategory(proto.Message):
            r"""Categories specified by the Windows Update.

            Attributes:
                id (str):
                    The identifier of the windows update
                    category.
                name (str):
                    The name of the windows update category.
            """

            id: str = proto.Field(
                proto.STRING,
                number=1,
            )
            name: str = proto.Field(
                proto.STRING,
                number=2,
            )

        title: str = proto.Field(
            proto.STRING,
            number=1,
        )
        description: str = proto.Field(
            proto.STRING,
            number=2,
        )
        categories: MutableSequence[
            "Inventory.WindowsUpdatePackage.WindowsUpdateCategory"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="Inventory.WindowsUpdatePackage.WindowsUpdateCategory",
        )
        kb_article_ids: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=4,
        )
        support_url: str = proto.Field(
            proto.STRING,
            number=11,
        )
        more_info_urls: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=5,
        )
        update_id: str = proto.Field(
            proto.STRING,
            number=6,
        )
        revision_number: int = proto.Field(
            proto.INT32,
            number=7,
        )
        last_deployment_change_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=10,
            message=timestamp_pb2.Timestamp,
        )

    class WindowsQuickFixEngineeringPackage(proto.Message):
        r"""Information related to a Quick Fix Engineering package.
        Fields are taken from Windows QuickFixEngineering Interface and
        match the source names:

        https://docs.microsoft.com/en-us/windows/win32/cimwin32prov/win32-quickfixengineering

        Attributes:
            caption (str):
                A short textual description of the QFE
                update.
            description (str):
                A textual description of the QFE update.
            hot_fix_id (str):
                Unique identifier associated with a
                particular QFE update.
            install_time (google.protobuf.timestamp_pb2.Timestamp):
                Date that the QFE update was installed. Mapped from
                installed_on field.
        """

        caption: str = proto.Field(
            proto.STRING,
            number=1,
        )
        description: str = proto.Field(
            proto.STRING,
            number=2,
        )
        hot_fix_id: str = proto.Field(
            proto.STRING,
            number=3,
        )
        install_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=5,
            message=timestamp_pb2.Timestamp,
        )

    class WindowsApplication(proto.Message):
        r"""Contains information about a Windows application that is
        retrieved from the Windows Registry. For more information about
        these fields, see:

        https://docs.microsoft.com/en-us/windows/win32/msi/uninstall-registry-key

        Attributes:
            display_name (str):
                The name of the application or product.
            display_version (str):
                The version of the product or application in
                string format.
            publisher (str):
                The name of the manufacturer for the product
                or application.
            install_date (google.type.date_pb2.Date):
                The last time this product received service.
                The value of this property is replaced each time
                a patch is applied or removed from the product
                or the command-line option is used to repair the
                product.
            help_link (str):
                The internet address for technical support.
        """

        display_name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        display_version: str = proto.Field(
            proto.STRING,
            number=2,
        )
        publisher: str = proto.Field(
            proto.STRING,
            number=3,
        )
        install_date: date_pb2.Date = proto.Field(
            proto.MESSAGE,
            number=4,
            message=date_pb2.Date,
        )
        help_link: str = proto.Field(
            proto.STRING,
            number=5,
        )

    name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    os_info: OsInfo = proto.Field(
        proto.MESSAGE,
        number=1,
        message=OsInfo,
    )
    items: MutableMapping[str, Item] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=2,
        message=Item,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


class GetInventoryRequest(proto.Message):
    r"""A request message for getting inventory data for the
    specified VM.

    Attributes:
        name (str):
            Required. API resource name for inventory resource.

            Format:
            ``projects/{project}/locations/{location}/instances/{instance}/inventory``

            For ``{project}``, either ``project-number`` or
            ``project-id`` can be provided. For ``{instance}``, either
            Compute Engine ``instance-id`` or ``instance-name`` can be
            provided.
        view (google.cloud.osconfig_v1alpha.types.InventoryView):
            Inventory view indicating what information
            should be included in the inventory resource. If
            unspecified, the default view is BASIC.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: "InventoryView" = proto.Field(
        proto.ENUM,
        number=2,
        enum="InventoryView",
    )


class ListInventoriesRequest(proto.Message):
    r"""A request message for listing inventory data for all VMs in
    the specified location.

    Attributes:
        parent (str):
            Required. The parent resource name.

            Format:
            ``projects/{project}/locations/{location}/instances/-``

            For ``{project}``, either ``project-number`` or
            ``project-id`` can be provided.
        view (google.cloud.osconfig_v1alpha.types.InventoryView):
            Inventory view indicating what information
            should be included in the inventory resource. If
            unspecified, the default view is BASIC.
        page_size (int):
            The maximum number of results to return.
        page_token (str):
            A pagination token returned from a previous call to
            ``ListInventories`` that indicates where this listing should
            continue from.
        filter (str):
            If provided, this field specifies the criteria that must be
            met by a ``Inventory`` API resource to be included in the
            response.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: "InventoryView" = proto.Field(
        proto.ENUM,
        number=2,
        enum="InventoryView",
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListInventoriesResponse(proto.Message):
    r"""A response message for listing inventory data for all VMs in
    a specified location.

    Attributes:
        inventories (MutableSequence[google.cloud.osconfig_v1alpha.types.Inventory]):
            List of inventory objects.
        next_page_token (str):
            The pagination token to retrieve the next
            page of inventory objects.
    """

    @property
    def raw_page(self):
        return self

    inventories: MutableSequence["Inventory"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Inventory",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
