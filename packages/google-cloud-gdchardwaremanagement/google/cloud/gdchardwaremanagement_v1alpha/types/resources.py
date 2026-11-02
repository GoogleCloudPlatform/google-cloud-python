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
import google.type.datetime_pb2 as datetime_pb2  # type: ignore
import google.type.dayofweek_pb2 as dayofweek_pb2  # type: ignore
import google.type.postal_address_pb2 as postal_address_pb2  # type: ignore
import google.type.timeofday_pb2 as timeofday_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.gdchardwaremanagement.v1alpha",
    manifest={
        "PowerSupply",
        "Entity",
        "Order",
        "Site",
        "HardwareGroup",
        "Hardware",
        "Comment",
        "ChangeLogEntry",
        "Sku",
        "Zone",
        "OrganizationContact",
        "Contact",
        "HardwareConfig",
        "SkuConfig",
        "SkuInstance",
        "HardwarePhysicalInfo",
        "HardwareInstallationInfo",
        "ZoneNetworkConfig",
        "Subnet",
        "TimePeriod",
        "Dimensions",
        "RackSpace",
        "HardwareLocation",
        "SubscriptionConfig",
    },
)


class PowerSupply(proto.Enum):
    r"""The power supply options.

    Values:
        POWER_SUPPLY_UNSPECIFIED (0):
            Power supply is unspecified.
        POWER_SUPPLY_AC (1):
            AC power supply.
        POWER_SUPPLY_DC (2):
            DC power supply.
    """

    POWER_SUPPLY_UNSPECIFIED = 0
    POWER_SUPPLY_AC = 1
    POWER_SUPPLY_DC = 2


class Entity(proto.Enum):
    r"""Entity is used to denote an organization or party.

    Values:
        ENTITY_UNSPECIFIED (0):
            Entity is unspecified.
        GOOGLE (1):
            Google.
        CUSTOMER (2):
            Customer.
        VENDOR (3):
            Vendor.
    """

    ENTITY_UNSPECIFIED = 0
    GOOGLE = 1
    CUSTOMER = 2
    VENDOR = 3


class Order(proto.Message):
    r"""An order for GDC hardware.

    Attributes:
        name (str):
            Identifier. Name of this order. Format:
            ``projects/{project}/locations/{location}/orders/{order}``
        display_name (str):
            Optional. Display name of this order.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when this order was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when this order was last
            updated.
        labels (MutableMapping[str, str]):
            Optional. Labels associated with this order as key value
            pairs. For more information about labels, see `Create and
            manage
            labels <https://cloud.google.com/resource-manager/docs/creating-managing-labels>`__.
        state (google.cloud.gdchardwaremanagement_v1alpha.types.Order.State):
            Output only. State of this order. On order
            creation, state will be set to DRAFT.
        organization_contact (google.cloud.gdchardwaremanagement_v1alpha.types.OrganizationContact):
            Required. Customer contact information.
        target_workloads (MutableSequence[str]):
            Optional. Customer specified workloads of
            interest targeted by this order. This must
            contain <= 20 elements and the length of each
            element must be <= 50 characters.
        customer_motivation (str):
            Required. Information about the customer's
            motivation for this order. The length of this
            field must be <= 1000 characters.
        fulfillment_time (google.protobuf.timestamp_pb2.Timestamp):
            Deprecated: Please use customer_requested_installation_date
            instead.
        customer_requested_installation_date (google.type.date_pb2.Date):
            Optional. Customer requested installation
            date for this order.
        region_code (str):
            Required. `Unicode CLDR <http://cldr.unicode.org/>`__ region
            code where this order will be deployed. For a list of valid
            CLDR region codes, see the `Language Subtag
            Registry <https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry>`__.
        order_form_uri (str):
            Output only. Link to the order form.
        type_ (google.cloud.gdchardwaremanagement_v1alpha.types.Order.Type):
            Output only. Type of this Order.
        submit_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the order was
            submitted. Is auto-populated to the current time
            when an order is submitted.
        billing_id (str):
            Output only. The Google Cloud Billing ID to
            be charged for this order.
        existing_hardware (MutableSequence[google.cloud.gdchardwaremanagement_v1alpha.types.HardwareLocation]):
            Optional. Existing hardware to be removed as
            part of this order. Note: any hardware removed
            will be recycled unless otherwise agreed.
        deployment_type (google.cloud.gdchardwaremanagement_v1alpha.types.Order.DeploymentType):
            Output only. The deployment type of this
            order.
        actual_installation_date (google.type.date_pb2.Date):
            Output only. Actual installation date for
            this order.
        estimated_installation_date (google.type.date_pb2.Date):
            Output only. Estimated installation date for
            this order.
        estimated_delivery_date (google.type.date_pb2.Date):
            Output only. Estimated delivery date for this
            order.
        migration (bool):
            Optional. Whether this order is a migration
            from customer's existing infrastructure.
        accepted_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the order was
            moved to ACCEPTED state.
        requested_date_change (google.type.date_pb2.Date):
            Output only. The date to which the customer
            or Google wants to set the scheduled
            installation date.
        vendor_notes (str):
            Output only. Notes for this order, provided
            by the vendor.
        vendor_contact (google.cloud.gdchardwaremanagement_v1alpha.types.OrganizationContact):
            Output only. Contact information of the SI
            assigned to this order.
    """

    class State(proto.Enum):
        r"""Valid states of an order.

        Values:
            STATE_UNSPECIFIED (0):
                State of the order is unspecified.
            DRAFT (1):
                Order is being drafted by the customer and
                has not been submitted yet.
            SUBMITTED (2):
                Order has been submitted to Google.
            INFO_COMPLETE (12):
                All information required from the customer
                for fulfillment of the order is complete.
            ACCEPTED (3):
                Order has been accepted by Google.
            ADDITIONAL_INFO_NEEDED (4):
                Order needs more information from the
                customer.
            BUILDING (5):
                Google has initiated building hardware for
                the order.
            SHIPPING (6):
                The hardware has been built and is being
                shipped.
            INSTALLING (7):
                The hardware is being installed.
            FAILED (8):
                An error occurred in processing the order and
                customer intervention is required.
            PARTIALLY_COMPLETED (9):
                Order has been partially completed i.e., some
                hardware have been delivered and installed.
            COMPLETED (10):
                Order has been completed.
            CANCELLED (11):
                Order has been cancelled.
        """

        STATE_UNSPECIFIED = 0
        DRAFT = 1
        SUBMITTED = 2
        INFO_COMPLETE = 12
        ACCEPTED = 3
        ADDITIONAL_INFO_NEEDED = 4
        BUILDING = 5
        SHIPPING = 6
        INSTALLING = 7
        FAILED = 8
        PARTIALLY_COMPLETED = 9
        COMPLETED = 10
        CANCELLED = 11

    class Type(proto.Enum):
        r"""Valid types of an Order.

        Values:
            TYPE_UNSPECIFIED (0):
                Type of the order is unspecified.
            PAID (1):
                Paid by the customer.
            POC (2):
                Proof of concept for the customer.
            UNPAID (2):
                Not billed.
        """

        _pb_options = {"allow_alias": True}
        TYPE_UNSPECIFIED = 0
        PAID = 1
        POC = 2
        UNPAID = 2

    class DeploymentType(proto.Enum):
        r"""Valid types of a deployment.

        Values:
            DEPLOYMENT_TYPE_UNSPECIFIED (0):
                Deployment type is unspecified.
            FULL_PRODUCTION (1):
                Prod deployment with SLOs.
            PROOF_OF_CONCEPT (2):
                Deployment with best-effort support and no
                SLOs.
            INTERNAL (3):
                Internal deployment with best-effort support
                and no SLOs.
            CUSTOMER_LAB (4):
                Customer lab deployment that we support as
                though it's prod.
        """

        DEPLOYMENT_TYPE_UNSPECIFIED = 0
        FULL_PRODUCTION = 1
        PROOF_OF_CONCEPT = 2
        INTERNAL = 3
        CUSTOMER_LAB = 4

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=13,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=5,
        enum=State,
    )
    organization_contact: "OrganizationContact" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="OrganizationContact",
    )
    target_workloads: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    customer_motivation: str = proto.Field(
        proto.STRING,
        number=8,
    )
    fulfillment_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    customer_requested_installation_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=21,
        message=date_pb2.Date,
    )
    region_code: str = proto.Field(
        proto.STRING,
        number=10,
    )
    order_form_uri: str = proto.Field(
        proto.STRING,
        number=11,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=12,
        enum=Type,
    )
    submit_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=14,
        message=timestamp_pb2.Timestamp,
    )
    billing_id: str = proto.Field(
        proto.STRING,
        number=15,
    )
    existing_hardware: MutableSequence["HardwareLocation"] = proto.RepeatedField(
        proto.MESSAGE,
        number=16,
        message="HardwareLocation",
    )
    deployment_type: DeploymentType = proto.Field(
        proto.ENUM,
        number=18,
        enum=DeploymentType,
    )
    actual_installation_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=19,
        message=date_pb2.Date,
    )
    estimated_installation_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=20,
        message=date_pb2.Date,
    )
    estimated_delivery_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=22,
        message=date_pb2.Date,
    )
    migration: bool = proto.Field(
        proto.BOOL,
        number=23,
    )
    accepted_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=24,
        message=timestamp_pb2.Timestamp,
    )
    requested_date_change: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=25,
        message=date_pb2.Date,
    )
    vendor_notes: str = proto.Field(
        proto.STRING,
        number=26,
    )
    vendor_contact: "OrganizationContact" = proto.Field(
        proto.MESSAGE,
        number=27,
        message="OrganizationContact",
    )


class Site(proto.Message):
    r"""A physical site where hardware will be installed.

    Attributes:
        name (str):
            Identifier. Name of the site. Format:
            ``projects/{project}/locations/{location}/sites/{site}``
        display_name (str):
            Optional. Display name of this Site.
        description (str):
            Optional. Description of this Site.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when this site was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when this site was last
            updated.
        labels (MutableMapping[str, str]):
            Optional. Labels associated with this site as key value
            pairs. For more information about labels, see `Create and
            manage
            labels <https://cloud.google.com/resource-manager/docs/creating-managing-labels>`__.
        organization_contact (google.cloud.gdchardwaremanagement_v1alpha.types.OrganizationContact):
            Required. Contact information for this site.
        google_maps_pin_uri (str):
            Optional. A URL to the Google Maps address location of the
            site. An example value is ``https://goo.gl/maps/xxxxxxxxx``.
        access_times (MutableSequence[google.cloud.gdchardwaremanagement_v1alpha.types.TimePeriod]):
            Optional. The time periods when the site is
            accessible. If this field is empty, the site is
            accessible at all times.

            This field is used by Google to schedule the
            initial installation as well as any later
            hardware maintenance. You may update this at any
            time. For example, if the initial installation
            is requested during off-hours but maintenance
            should be performed during regular business
            hours, you should update the access times after
            initial installation is complete.
        notes (str):
            Optional. Any additional notes for this Site.
            Please include information about:

             - security or access restrictions
             - any regulations affecting the technicians
              visiting the site
             - any special process or approval required to
              move the equipment
             - whether a representative will be available
              during site visits
        customer_site_id (str):
            Optional. Customer defined identifier for
            this Site. This can be used to identify the site
            in the customer's own systems.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=24,
    )
    description: str = proto.Field(
        proto.STRING,
        number=25,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    organization_contact: "OrganizationContact" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="OrganizationContact",
    )
    google_maps_pin_uri: str = proto.Field(
        proto.STRING,
        number=6,
    )
    access_times: MutableSequence["TimePeriod"] = proto.RepeatedField(
        proto.MESSAGE,
        number=26,
        message="TimePeriod",
    )
    notes: str = proto.Field(
        proto.STRING,
        number=27,
    )
    customer_site_id: str = proto.Field(
        proto.STRING,
        number=28,
    )


class HardwareGroup(proto.Message):
    r"""A group of hardware that is part of the same order, has the
    same SKU, and is delivered to the same site.

    Attributes:
        name (str):
            Identifier. Name of this hardware group. Format:
            ``projects/{project}/locations/{location}/orders/{order}/hardwareGroups/{hardware_group}``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when this hardware group
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when this hardware group
            was last updated.
        labels (MutableMapping[str, str]):
            Optional. Labels associated with this hardware group as key
            value pairs. For more information about labels, see `Create
            and manage
            labels <https://cloud.google.com/resource-manager/docs/creating-managing-labels>`__.
        hardware_count (int):
            Required. Number of hardware in this
            HardwareGroup.
        config (google.cloud.gdchardwaremanagement_v1alpha.types.HardwareConfig):
            Required. Configuration for hardware in this
            HardwareGroup.
        site (str):
            Required. Name of the site where the hardware in this
            HardwareGroup will be delivered. Format:
            ``projects/{project}/locations/{location}/sites/{site}``
        state (google.cloud.gdchardwaremanagement_v1alpha.types.HardwareGroup.State):
            Output only. Current state of this
            HardwareGroup.
        zone (str):
            Optional. Name of the zone that the hardware in this
            HardwareGroup belongs to. Format:
            ``projects/{project}/locations/{location}/zones/{zone}``
        requested_installation_date (google.type.date_pb2.Date):
            Deprecated: This value is not used. Use the
            requested_installation_date field in the Order resource
            instead.
    """

    class State(proto.Enum):
        r"""Valid states of a HardwareGroup.

        Values:
            STATE_UNSPECIFIED (0):
                State of the HardwareGroup is unspecified.
            ADDITIONAL_INFO_NEEDED (1):
                More information is required from the
                customer to make progress.
            BUILDING (2):
                Google has initiated building hardware for
                this HardwareGroup.
            SHIPPING (3):
                The hardware has been built and is being
                shipped.
            INSTALLING (4):
                The hardware is being installed.
            PARTIALLY_INSTALLED (5):
                Some hardware in the HardwareGroup have been
                installed.
            INSTALLED (6):
                All hardware in the HardwareGroup have been
                installed.
            FAILED (7):
                An error occurred and customer intervention
                is required.
        """

        STATE_UNSPECIFIED = 0
        ADDITIONAL_INFO_NEEDED = 1
        BUILDING = 2
        SHIPPING = 3
        INSTALLING = 4
        PARTIALLY_INSTALLED = 5
        INSTALLED = 6
        FAILED = 7

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    hardware_count: int = proto.Field(
        proto.INT32,
        number=5,
    )
    config: "HardwareConfig" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="HardwareConfig",
    )
    site: str = proto.Field(
        proto.STRING,
        number=7,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=8,
        enum=State,
    )
    zone: str = proto.Field(
        proto.STRING,
        number=9,
    )
    requested_installation_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=10,
        message=date_pb2.Date,
    )


class Hardware(proto.Message):
    r"""An instance of hardware installed at a site.

    Attributes:
        name (str):
            Identifier. Name of this hardware. Format:
            ``projects/{project}/locations/{location}/hardware/{hardware}``
        display_name (str):
            Optional. Display name for this hardware.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when this hardware was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when this hardware was last
            updated.
        labels (MutableMapping[str, str]):
            Optional. Labels associated with this hardware as key value
            pairs. For more information about labels, see `Create and
            manage
            labels <https://cloud.google.com/resource-manager/docs/creating-managing-labels>`__.
        order (str):
            Required. Name of the order that this hardware belongs to.
            Format:
            ``projects/{project}/locations/{location}/orders/{order}``
        hardware_group (str):
            Output only. Name for the hardware group that this hardware
            belongs to. Format:
            ``projects/{project}/locations/{location}/orders/{order}/hardwareGroups/{hardware_group}``
        site (str):
            Required. Name for the site that this hardware belongs to.
            Format:
            ``projects/{project}/locations/{location}/sites/{site}``
        state (google.cloud.gdchardwaremanagement_v1alpha.types.Hardware.State):
            Output only. Current state for this hardware.
        ciq_uri (str):
            Output only. Link to the Customer Intake
            Questionnaire (CIQ) sheet for this Hardware.
        config (google.cloud.gdchardwaremanagement_v1alpha.types.HardwareConfig):
            Required. Configuration for this hardware.
        estimated_installation_date (google.type.date_pb2.Date):
            Output only. Estimated installation date for
            this hardware.
        physical_info (google.cloud.gdchardwaremanagement_v1alpha.types.HardwarePhysicalInfo):
            Optional. Physical properties of this
            hardware.
        installation_info (google.cloud.gdchardwaremanagement_v1alpha.types.HardwareInstallationInfo):
            Optional. Information for installation of
            this hardware.
        zone (str):
            Required. Name for the zone that this hardware belongs to.
            Format:
            ``projects/{project}/locations/{location}/zones/{zone}``
        requested_installation_date (google.type.date_pb2.Date):
            Optional. Requested installation date for this hardware. If
            not specified, this is auto-populated from the order's
            fulfillment_time upon submission or from the HardwareGroup's
            requested_installation_date upon order acceptance.
        actual_installation_date (google.type.date_pb2.Date):
            Output only. Actual installation date for
            this hardware. Filled in by Google.
        machine_infos (MutableSequence[google.cloud.gdchardwaremanagement_v1alpha.types.Hardware.MachineInfo]):
            Output only. Per machine asset information
            needed for turnup.
        estimated_delivery_date (google.type.date_pb2.Date):
            Output only. The estimated delivery date of
            the hardware.
    """

    class State(proto.Enum):
        r"""Valid states for hardware.

        Values:
            STATE_UNSPECIFIED (0):
                State of the Hardware is unspecified.
            ADDITIONAL_INFO_NEEDED (1):
                More information is required from the
                customer to make progress.
            BUILDING (2):
                Google has initiated building hardware for
                this Hardware.
            SHIPPING (3):
                The hardware has been built and is being
                shipped.
            INSTALLING (4):
                The hardware is being installed.
            INSTALLED (5):
                The hardware has been installed.
            FAILED (6):
                An error occurred and customer intervention
                is required.
        """

        STATE_UNSPECIFIED = 0
        ADDITIONAL_INFO_NEEDED = 1
        BUILDING = 2
        SHIPPING = 3
        INSTALLING = 4
        INSTALLED = 5
        FAILED = 6

    class MacAddress(proto.Message):
        r"""Message to describe the MAC address of a machine.

        Attributes:
            address (str):
                Output only. Address string.
            type_ (google.cloud.gdchardwaremanagement_v1alpha.types.Hardware.MacAddress.AddressType):
                Output only. Address type for this MAC
                address.
            ipv4_address (str):
                Output only. Static IP address (if used) that
                is associated with the MAC address. Only
                applicable for VIRTUAL MAC address type.
        """

        class AddressType(proto.Enum):
            r"""Enum for the different types of MAC address.

            Values:
                ADDRESS_TYPE_UNSPECIFIED (0):
                    Unspecified address type.
                NIC (1):
                    Address of a network interface card.
                BMC (2):
                    Address of a baseboard management controller.
                VIRTUAL (3):
                    Address of a virtual interface.
            """

            ADDRESS_TYPE_UNSPECIFIED = 0
            NIC = 1
            BMC = 2
            VIRTUAL = 3

        address: str = proto.Field(
            proto.STRING,
            number=1,
        )
        type_: "Hardware.MacAddress.AddressType" = proto.Field(
            proto.ENUM,
            number=2,
            enum="Hardware.MacAddress.AddressType",
        )
        ipv4_address: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class DiskInfo(proto.Message):
        r"""Information about individual disks on a machine.

        Attributes:
            manufacturer (str):
                Output only. Disk manufacturer.
            slot (int):
                Output only. Disk slot number.
            serial_number (str):
                Output only. Disk serial number.
            psid (str):
                Output only. Disk PSID.
            part_number (str):
                Output only. Disk part number.
            model_number (str):
                Output only. Disk model number.
        """

        manufacturer: str = proto.Field(
            proto.STRING,
            number=1,
        )
        slot: int = proto.Field(
            proto.INT32,
            number=2,
        )
        serial_number: str = proto.Field(
            proto.STRING,
            number=3,
        )
        psid: str = proto.Field(
            proto.STRING,
            number=4,
        )
        part_number: str = proto.Field(
            proto.STRING,
            number=5,
        )
        model_number: str = proto.Field(
            proto.STRING,
            number=6,
        )

    class MachineInfo(proto.Message):
        r"""Information about individual machines vendors will provide
        during turnup.

        Attributes:
            service_tag (str):
                Output only. Machine service tag.
            mac_addresses (MutableSequence[google.cloud.gdchardwaremanagement_v1alpha.types.Hardware.MacAddress]):
                Output only. Each associated MAC address.
            name (str):
                Output only. Machine name.
            disk_infos (MutableSequence[google.cloud.gdchardwaremanagement_v1alpha.types.Hardware.DiskInfo]):
                Output only. Information for each disk
                installed.
        """

        service_tag: str = proto.Field(
            proto.STRING,
            number=1,
        )
        mac_addresses: MutableSequence["Hardware.MacAddress"] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="Hardware.MacAddress",
        )
        name: str = proto.Field(
            proto.STRING,
            number=3,
        )
        disk_infos: MutableSequence["Hardware.DiskInfo"] = proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message="Hardware.DiskInfo",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    order: str = proto.Field(
        proto.STRING,
        number=6,
    )
    hardware_group: str = proto.Field(
        proto.STRING,
        number=7,
    )
    site: str = proto.Field(
        proto.STRING,
        number=8,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=9,
        enum=State,
    )
    ciq_uri: str = proto.Field(
        proto.STRING,
        number=10,
    )
    config: "HardwareConfig" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="HardwareConfig",
    )
    estimated_installation_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=12,
        message=date_pb2.Date,
    )
    physical_info: "HardwarePhysicalInfo" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="HardwarePhysicalInfo",
    )
    installation_info: "HardwareInstallationInfo" = proto.Field(
        proto.MESSAGE,
        number=14,
        message="HardwareInstallationInfo",
    )
    zone: str = proto.Field(
        proto.STRING,
        number=15,
    )
    requested_installation_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=16,
        message=date_pb2.Date,
    )
    actual_installation_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=17,
        message=date_pb2.Date,
    )
    machine_infos: MutableSequence[MachineInfo] = proto.RepeatedField(
        proto.MESSAGE,
        number=20,
        message=MachineInfo,
    )
    estimated_delivery_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=21,
        message=date_pb2.Date,
    )


class Comment(proto.Message):
    r"""A comment on an order.

    Attributes:
        name (str):
            Identifier. Name of this comment. Format:
            ``projects/{project}/locations/{location}/orders/{order}/comments/{comment}``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when this comment was
            created.
        labels (MutableMapping[str, str]):
            Optional. Labels associated with this comment as key value
            pairs. For more information about labels, see `Create and
            manage
            labels <https://cloud.google.com/resource-manager/docs/creating-managing-labels>`__.
        author (str):
            Output only. Username of the author of this
            comment. This is auto-populated from the
            credentials used during creation of the comment.
        text (str):
            Required. Text of this comment. The length of
            text must be <= 1000 characters.
        customer_viewed_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp of the first time this
            comment was viewed by the customer. If the
            comment wasn't viewed then this timestamp will
            be unset.
        author_entity (google.cloud.gdchardwaremanagement_v1alpha.types.Entity):
            Output only. The entity the author belongs
            to.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )
    author: str = proto.Field(
        proto.STRING,
        number=4,
    )
    text: str = proto.Field(
        proto.STRING,
        number=5,
    )
    customer_viewed_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    author_entity: "Entity" = proto.Field(
        proto.ENUM,
        number=7,
        enum="Entity",
    )


class ChangeLogEntry(proto.Message):
    r"""A log entry of a change made to an order.

    Attributes:
        name (str):
            Identifier. Name of this change log entry. Format:
            ``projects/{project}/locations/{location}/orders/{order}/changeLogEntries/{change_log_entry}``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when this change log entry
            was created.
        labels (MutableMapping[str, str]):
            Optional. Labels associated with this change log entry as
            key value pairs. For more information about labels, see
            `Create and manage
            labels <https://cloud.google.com/resource-manager/docs/creating-managing-labels>`__.
        log (str):
            Output only. Content of this log entry.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )
    log: str = proto.Field(
        proto.STRING,
        number=4,
    )


class Sku(proto.Message):
    r"""A stock keeping unit (SKU) of GDC hardware.

    Attributes:
        name (str):
            Identifier. Name of this SKU. Format:
            ``projects/{project}/locations/{location}/skus/{sku}``
        display_name (str):
            Output only. Display name of this SKU.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when this SKU was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when this SKU was last
            updated.
        config (google.cloud.gdchardwaremanagement_v1alpha.types.SkuConfig):
            Output only. Configuration for this SKU.
        instances (MutableSequence[google.cloud.gdchardwaremanagement_v1alpha.types.SkuInstance]):
            Output only. Available instances of this SKU.
            This field should be used for checking
            availability of a SKU.
        description (str):
            Output only. Description of this SKU.
        revision_id (str):
            Output only. The SKU revision ID. A new revision is created
            whenever ``config`` is updated. The format is an 8-character
            hexadecimal string.
        is_active (bool):
            Output only. Flag to indicate whether or not
            this revision is active. Only an active revision
            can be used in a new Order.
        type_ (google.cloud.gdchardwaremanagement_v1alpha.types.Sku.Type):
            Output only. Type of this SKU.
        vcpu_count (int):
            Output only. The vCPU count associated with
            this SKU.
        hardware_count_ranges (MutableSequence[google.cloud.gdchardwaremanagement_v1alpha.types.Sku.Range]):
            Output only. The inclusive ranges of hardware
            counts that are allowed in a zone using this
            SKU.
    """

    class Type(proto.Enum):
        r"""Valid types of a SKU.

        Values:
            TYPE_UNSPECIFIED (0):
                Type of the SKU is unspecified. This is not
                an allowed value.
            RACK (1):
                Rack SKU.
            SERVER (2):
                Server SKU.
        """

        TYPE_UNSPECIFIED = 0
        RACK = 1
        SERVER = 2

    class Range(proto.Message):
        r"""Inclusive range.

        Attributes:
            min_ (int):
                The minimum value of the range.
            max_ (int):
                The maximum value of the range.
        """

        min_: int = proto.Field(
            proto.INT32,
            number=1,
        )
        max_: int = proto.Field(
            proto.INT32,
            number=2,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    config: "SkuConfig" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="SkuConfig",
    )
    instances: MutableSequence["SkuInstance"] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="SkuInstance",
    )
    description: str = proto.Field(
        proto.STRING,
        number=8,
    )
    revision_id: str = proto.Field(
        proto.STRING,
        number=9,
    )
    is_active: bool = proto.Field(
        proto.BOOL,
        number=10,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=11,
        enum=Type,
    )
    vcpu_count: int = proto.Field(
        proto.INT32,
        number=12,
    )
    hardware_count_ranges: MutableSequence[Range] = proto.RepeatedField(
        proto.MESSAGE,
        number=13,
        message=Range,
    )


class Zone(proto.Message):
    r"""A zone holding a set of hardware.

    Attributes:
        name (str):
            Identifier. Name of this zone. Format:
            ``projects/{project}/locations/{location}/zones/{zone}``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when this zone was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when this zone was last
            updated.
        labels (MutableMapping[str, str]):
            Optional. Labels associated with this zone as key value
            pairs. For more information about labels, see `Create and
            manage
            labels <https://cloud.google.com/resource-manager/docs/creating-managing-labels>`__.
        display_name (str):
            Optional. Human friendly display name of this
            zone.
        state (google.cloud.gdchardwaremanagement_v1alpha.types.Zone.State):
            Output only. Current state for this zone.
        contacts (MutableSequence[google.cloud.gdchardwaremanagement_v1alpha.types.Contact]):
            Required. The points of contact.
        ciq_uri (str):
            Output only. Link to the Customer Intake
            Questionnaire (CIQ) sheet for this zone.
        network_config (google.cloud.gdchardwaremanagement_v1alpha.types.ZoneNetworkConfig):
            Optional. Networking configuration for this
            zone.
        globally_unique_id (str):
            Output only. Globally unique identifier
            generated for this Edge Zone.
        subscription_configs (MutableSequence[google.cloud.gdchardwaremanagement_v1alpha.types.SubscriptionConfig]):
            Output only. Subscription configurations for
            this zone.
        provisioning_state (google.cloud.gdchardwaremanagement_v1alpha.types.Zone.ProvisioningState):
            Output only. Provisioning state for
            configurations like MAC addresses.
        skip_cluster_provisioning (bool):
            Optional. Whether to skip the cluster
            provisioning step during factory turnup. If
            true, indicates that the Kubernetes cluster will
            be created after the zone's hardware is
            installed at the customer site.
        cluster_intent_required (bool):
            Output only. Indicates whether a valid
            cluster intent must be provided by the customer
            before accepting the order. If true, the order
            cannot be accepted until cluster intent is
            present. This is used to enforce early
            validation and prevent delays caused by missing
            configuration.
        cluster_intent_verified (bool):
            Output only. Indicates whether the provided
            cluster intent has been successfully verified.
            This flag ensures cluster intent exists before
            order can be accepted.
    """

    class State(proto.Enum):
        r"""Valid states for a zone.

        Values:
            STATE_UNSPECIFIED (0):
                State of the Zone is unspecified.
            ADDITIONAL_INFO_NEEDED (1):
                More information is required from the
                customer to make progress.
            PREPARING (2):
                Google is preparing the Zone.
            READY_FOR_CUSTOMER_FACTORY_TURNUP_CHECKS (5):
                Factory turnup has succeeded.
            CUSTOMER_FACTORY_TURNUP_CHECKS_STARTED (8):
                The Zone is running factory turnup checks.
            READY_FOR_SITE_TURNUP (6):
                The Zone is ready for site turnup.
            OFFLINE (9):
                The Zone is offline.
            CUSTOMER_FACTORY_TURNUP_CHECKS_FAILED (7):
                The Zone failed in factory turnup checks.
            ACTIVE (3):
                The Zone is available to use.
            CANCELLED (4):
                The Zone has been cancelled.
        """

        STATE_UNSPECIFIED = 0
        ADDITIONAL_INFO_NEEDED = 1
        PREPARING = 2
        READY_FOR_CUSTOMER_FACTORY_TURNUP_CHECKS = 5
        CUSTOMER_FACTORY_TURNUP_CHECKS_STARTED = 8
        READY_FOR_SITE_TURNUP = 6
        OFFLINE = 9
        CUSTOMER_FACTORY_TURNUP_CHECKS_FAILED = 7
        ACTIVE = 3
        CANCELLED = 4

    class ProvisioningState(proto.Enum):
        r"""Valid provisioning states for configurations like MAC
        addresses.

        Values:
            PROVISIONING_STATE_UNSPECIFIED (0):
                Provisioning state is unspecified.
            PROVISIONING_REQUIRED (1):
                Provisioning is required. Set by Google.
            PROVISIONING_IN_PROGRESS (2):
                Provisioning is in progress. Set by customer.
            PROVISIONING_COMPLETE (3):
                Provisioning is complete. Set by customer.
        """

        PROVISIONING_STATE_UNSPECIFIED = 0
        PROVISIONING_REQUIRED = 1
        PROVISIONING_IN_PROGRESS = 2
        PROVISIONING_COMPLETE = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=8,
        enum=State,
    )
    contacts: MutableSequence["Contact"] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="Contact",
    )
    ciq_uri: str = proto.Field(
        proto.STRING,
        number=10,
    )
    network_config: "ZoneNetworkConfig" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="ZoneNetworkConfig",
    )
    globally_unique_id: str = proto.Field(
        proto.STRING,
        number=12,
    )
    subscription_configs: MutableSequence["SubscriptionConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=13,
        message="SubscriptionConfig",
    )
    provisioning_state: ProvisioningState = proto.Field(
        proto.ENUM,
        number=14,
        enum=ProvisioningState,
    )
    skip_cluster_provisioning: bool = proto.Field(
        proto.BOOL,
        number=16,
    )
    cluster_intent_required: bool = proto.Field(
        proto.BOOL,
        number=17,
    )
    cluster_intent_verified: bool = proto.Field(
        proto.BOOL,
        number=18,
    )


class OrganizationContact(proto.Message):
    r"""Contact information of the customer organization.

    Attributes:
        address (google.type.postal_address_pb2.PostalAddress):
            Required. The organization's address.
        email (str):
            Optional. The organization's email.
        phone (str):
            Optional. The organization's phone number.
        contacts (MutableSequence[google.cloud.gdchardwaremanagement_v1alpha.types.Contact]):
            Required. The individual points of contact in
            the organization at this location.
    """

    address: postal_address_pb2.PostalAddress = proto.Field(
        proto.MESSAGE,
        number=1,
        message=postal_address_pb2.PostalAddress,
    )
    email: str = proto.Field(
        proto.STRING,
        number=2,
    )
    phone: str = proto.Field(
        proto.STRING,
        number=3,
    )
    contacts: MutableSequence["Contact"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="Contact",
    )


class Contact(proto.Message):
    r"""Contact details of a point of contact.

    Attributes:
        given_name (str):
            Required. Given name of the contact.
        family_name (str):
            Optional. Family name of the contact.
        email (str):
            Required. Email of the contact.
        phone (str):
            Required. Phone number of the contact.
        time_zone (google.type.datetime_pb2.TimeZone):
            Optional. Time zone of the contact.
        reachable_times (MutableSequence[google.cloud.gdchardwaremanagement_v1alpha.types.TimePeriod]):
            Optional. The time periods when the contact
            is reachable. If this field is empty, the
            contact is reachable at all times.
    """

    given_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    family_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    email: str = proto.Field(
        proto.STRING,
        number=3,
    )
    phone: str = proto.Field(
        proto.STRING,
        number=4,
    )
    time_zone: datetime_pb2.TimeZone = proto.Field(
        proto.MESSAGE,
        number=5,
        message=datetime_pb2.TimeZone,
    )
    reachable_times: MutableSequence["TimePeriod"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="TimePeriod",
    )


class HardwareConfig(proto.Message):
    r"""Configuration for GDC hardware.

    Attributes:
        sku (str):
            Required. Reference to the SKU for this hardware. This can
            point to a specific SKU revision in the form of
            ``resource_name@revision_id`` as defined in
            `AIP-162 <https://google.aip.dev/162>`__. If no revision_id
            is specified, it refers to the latest revision.
        power_supply (google.cloud.gdchardwaremanagement_v1alpha.types.PowerSupply):
            Required. Power supply type for this
            hardware.
        subscription_duration_months (int):
            Optional. Subscription duration for the
            hardware in months.
    """

    sku: str = proto.Field(
        proto.STRING,
        number=1,
    )
    power_supply: "PowerSupply" = proto.Field(
        proto.ENUM,
        number=2,
        enum="PowerSupply",
    )
    subscription_duration_months: int = proto.Field(
        proto.INT32,
        number=3,
    )


class SkuConfig(proto.Message):
    r"""Configuration for a SKU.

    Attributes:
        cpu (str):
            Information about CPU configuration.
        gpu (str):
            Information about GPU configuration.
        ram (str):
            Information about RAM configuration.
        storage (str):
            Information about storage configuration.
    """

    cpu: str = proto.Field(
        proto.STRING,
        number=1,
    )
    gpu: str = proto.Field(
        proto.STRING,
        number=2,
    )
    ram: str = proto.Field(
        proto.STRING,
        number=3,
    )
    storage: str = proto.Field(
        proto.STRING,
        number=4,
    )


class SkuInstance(proto.Message):
    r"""A specific instance of the SKU.

    Attributes:
        region_code (str):
            The `Unicode CLDR <https://cldr.unicode.org>`__ region code
            where this instance is available.
        power_supply (google.cloud.gdchardwaremanagement_v1alpha.types.PowerSupply):
            Power supply type for this instance.
        billing_sku (str):
            Reference to the corresponding SKU in the Cloud Billing API.
            The estimated price information can be retrieved using that
            API. Format: ``services/{service}/skus/{sku}``
        billing_sku_per_vcpu (str):
            Reference to the corresponding SKU per vCPU in the Cloud
            Billing API. The estimated price information can be
            retrieved using that API. Format:
            ``services/{service}/skus/{sku}``
        subscription_duration_months (int):
            Subscription duration for the hardware in
            months.
    """

    region_code: str = proto.Field(
        proto.STRING,
        number=1,
    )
    power_supply: "PowerSupply" = proto.Field(
        proto.ENUM,
        number=2,
        enum="PowerSupply",
    )
    billing_sku: str = proto.Field(
        proto.STRING,
        number=3,
    )
    billing_sku_per_vcpu: str = proto.Field(
        proto.STRING,
        number=4,
    )
    subscription_duration_months: int = proto.Field(
        proto.INT32,
        number=5,
    )


class HardwarePhysicalInfo(proto.Message):
    r"""Physical properties of a hardware.

    Attributes:
        power_receptacle (google.cloud.gdchardwaremanagement_v1alpha.types.HardwarePhysicalInfo.PowerReceptacleType):
            Required. The power receptacle type.
        network_uplink (google.cloud.gdchardwaremanagement_v1alpha.types.HardwarePhysicalInfo.NetworkUplinkType):
            Required. Type of the uplink network
            connection.
        voltage (google.cloud.gdchardwaremanagement_v1alpha.types.HardwarePhysicalInfo.Voltage):
            Required. Voltage of the power supply.
        amperes (google.cloud.gdchardwaremanagement_v1alpha.types.HardwarePhysicalInfo.Amperes):
            Required. Amperes of the power supply.
    """

    class PowerReceptacleType(proto.Enum):
        r"""Valid power receptacle types.

        Values:
            POWER_RECEPTACLE_TYPE_UNSPECIFIED (0):
                Facility plug type is unspecified.
            NEMA_5_15 (1):
                NEMA 5-15.
            C_13 (2):
                C13.
            STANDARD_EU (3):
                Deprecated: Please use TYPE_G_BS1363, CEE_7_3, CEE_7_5 or
                TYPE_F instead.
            TYPE_G_BS1363 (4):
                Type G / BS1363.
            CEE_7_3 (5):
                C 7/3.
            CEE_7_5 (6):
                C 7/5.
            TYPE_F (7):
                Type F.
        """

        POWER_RECEPTACLE_TYPE_UNSPECIFIED = 0
        NEMA_5_15 = 1
        C_13 = 2
        STANDARD_EU = 3
        TYPE_G_BS1363 = 4
        CEE_7_3 = 5
        CEE_7_5 = 6
        TYPE_F = 7

    class NetworkUplinkType(proto.Enum):
        r"""Valid network uplink types.

        Values:
            NETWORK_UPLINK_TYPE_UNSPECIFIED (0):
                Network uplink type is unspecified.
            RJ_45 (1):
                RJ-45.
        """

        NETWORK_UPLINK_TYPE_UNSPECIFIED = 0
        RJ_45 = 1

    class Voltage(proto.Enum):
        r"""Valid voltage values.

        Values:
            VOLTAGE_UNSPECIFIED (0):
                Voltage is unspecified.
            VOLTAGE_110 (1):
                120V.
            VOLTAGE_220 (3):
                220V.
        """

        VOLTAGE_UNSPECIFIED = 0
        VOLTAGE_110 = 1
        VOLTAGE_220 = 3

    class Amperes(proto.Enum):
        r"""Valid amperes values.

        Values:
            AMPERES_UNSPECIFIED (0):
                Amperes is unspecified.
            AMPERES_15 (1):
                15A.
        """

        AMPERES_UNSPECIFIED = 0
        AMPERES_15 = 1

    power_receptacle: PowerReceptacleType = proto.Field(
        proto.ENUM,
        number=1,
        enum=PowerReceptacleType,
    )
    network_uplink: NetworkUplinkType = proto.Field(
        proto.ENUM,
        number=2,
        enum=NetworkUplinkType,
    )
    voltage: Voltage = proto.Field(
        proto.ENUM,
        number=3,
        enum=Voltage,
    )
    amperes: Amperes = proto.Field(
        proto.ENUM,
        number=4,
        enum=Amperes,
    )


class HardwareInstallationInfo(proto.Message):
    r"""Information for installation of a Hardware.

    Attributes:
        rack_location (str):
            Required. Location of the rack in the site
            e.g. Floor 2, Room 201, Row 7, Rack 3.
        power_distance_meters (int):
            Required. Distance from the power outlet in
            meters.
        switch_distance_meters (int):
            Required. Distance from the network switch in
            meters.
        rack_unit_dimensions (google.cloud.gdchardwaremanagement_v1alpha.types.Dimensions):
            Required. Dimensions of the rack unit.
        rack_space (google.cloud.gdchardwaremanagement_v1alpha.types.RackSpace):
            Required. Rack space allocated for the
            hardware.
        rack_type (google.cloud.gdchardwaremanagement_v1alpha.types.HardwareInstallationInfo.RackType):
            Required. Type of the rack.
    """

    class RackType(proto.Enum):
        r"""Valid rack types.

        Values:
            RACK_TYPE_UNSPECIFIED (0):
                Rack type is unspecified.
            TWO_POST (1):
                Two post rack.
            FOUR_POST (2):
                Four post rack.
        """

        RACK_TYPE_UNSPECIFIED = 0
        TWO_POST = 1
        FOUR_POST = 2

    rack_location: str = proto.Field(
        proto.STRING,
        number=1,
    )
    power_distance_meters: int = proto.Field(
        proto.INT32,
        number=2,
    )
    switch_distance_meters: int = proto.Field(
        proto.INT32,
        number=3,
    )
    rack_unit_dimensions: "Dimensions" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="Dimensions",
    )
    rack_space: "RackSpace" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="RackSpace",
    )
    rack_type: RackType = proto.Field(
        proto.ENUM,
        number=6,
        enum=RackType,
    )


class ZoneNetworkConfig(proto.Message):
    r"""Networking configuration for a zone.

    Attributes:
        machine_mgmt_ipv4_range (str):
            Required. An IPv4 address block for machine management.
            Should be a private RFC1918 or public CIDR block large
            enough to allocate at least one address per machine in the
            Zone. Should be in ``management_ipv4_subnet``, and disjoint
            with other address ranges.
        kubernetes_node_ipv4_range (str):
            Required. An IPv4 address block for kubernetes nodes. Should
            be a private RFC1918 or public CIDR block large enough to
            allocate at least one address per machine in the Zone.
            Should be in ``kubernetes_ipv4_subnet``, and disjoint with
            other address ranges.
        kubernetes_control_plane_ipv4_range (str):
            Required. An IPv4 address block for kubernetes control
            plane. Should be a private RFC1918 or public CIDR block
            large enough to allocate at least one address per cluster in
            the Zone. Should be in ``kubernetes_ipv4_subnet``, and
            disjoint with other address ranges.
        management_ipv4_subnet (google.cloud.gdchardwaremanagement_v1alpha.types.Subnet):
            Required. An IPv4 subnet for the management
            network.
        kubernetes_ipv4_subnet (google.cloud.gdchardwaremanagement_v1alpha.types.Subnet):
            Optional. An IPv4 subnet for the kubernetes
            network. If unspecified, the kubernetes subnet
            will be the same as the management subnet.
        dns_ipv4_addresses (MutableSequence[str]):
            Optional. DNS nameservers.
            The GDC Infrastructure will resolve DNS queries
            via these IPs. If unspecified, Google DNS is
            used.
        kubernetes_primary_vlan_id (int):
            Optional. Kubernetes VLAN ID.
            By default, the kubernetes node, including the
            primary kubernetes network, are in the same VLAN
            as the machine management network. For network
            segmentation purposes, these can optionally be
            separated.
    """

    machine_mgmt_ipv4_range: str = proto.Field(
        proto.STRING,
        number=1,
    )
    kubernetes_node_ipv4_range: str = proto.Field(
        proto.STRING,
        number=2,
    )
    kubernetes_control_plane_ipv4_range: str = proto.Field(
        proto.STRING,
        number=3,
    )
    management_ipv4_subnet: "Subnet" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="Subnet",
    )
    kubernetes_ipv4_subnet: "Subnet" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="Subnet",
    )
    dns_ipv4_addresses: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    kubernetes_primary_vlan_id: int = proto.Field(
        proto.INT32,
        number=7,
    )


class Subnet(proto.Message):
    r"""Represents a subnet.

    Attributes:
        address_range (str):
            Required. Address range for this subnet in
            CIDR notation.
        default_gateway_ip_address (str):
            Required. Default gateway for this subnet.
    """

    address_range: str = proto.Field(
        proto.STRING,
        number=1,
    )
    default_gateway_ip_address: str = proto.Field(
        proto.STRING,
        number=2,
    )


class TimePeriod(proto.Message):
    r"""Represents a time period in a week.

    Attributes:
        start_time (google.type.timeofday_pb2.TimeOfDay):
            Required. The start of the time period.
        end_time (google.type.timeofday_pb2.TimeOfDay):
            Required. The end of the time period.
        days (MutableSequence[google.type.dayofweek_pb2.DayOfWeek]):
            Required. The days of the week that the time
            period is active.
    """

    start_time: timeofday_pb2.TimeOfDay = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timeofday_pb2.TimeOfDay,
    )
    end_time: timeofday_pb2.TimeOfDay = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timeofday_pb2.TimeOfDay,
    )
    days: MutableSequence[dayofweek_pb2.DayOfWeek] = proto.RepeatedField(
        proto.ENUM,
        number=3,
        enum=dayofweek_pb2.DayOfWeek,
    )


class Dimensions(proto.Message):
    r"""Represents the dimensions of an object.

    Attributes:
        width_inches (float):
            Required. Width in inches.
        height_inches (float):
            Required. Height in inches.
        depth_inches (float):
            Required. Depth in inches.
    """

    width_inches: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    height_inches: float = proto.Field(
        proto.FLOAT,
        number=2,
    )
    depth_inches: float = proto.Field(
        proto.FLOAT,
        number=3,
    )


class RackSpace(proto.Message):
    r"""Represents contiguous space in a rack.

    Attributes:
        start_rack_unit (int):
            Required. First rack unit of the rack space
            (inclusive).
        end_rack_unit (int):
            Required. Last rack unit of the rack space
            (inclusive).
    """

    start_rack_unit: int = proto.Field(
        proto.INT32,
        number=1,
    )
    end_rack_unit: int = proto.Field(
        proto.INT32,
        number=2,
    )


class HardwareLocation(proto.Message):
    r"""Represents the location of one or many hardware.

    Attributes:
        site (str):
            Required. Name of the site where the hardware are present.
            Format:
            ``projects/{project}/locations/{location}/sites/{site}``
        rack_location (str):
            Required. Location of the rack in the site
            e.g. Floor 2, Room 201, Row 7, Rack 3.
        rack_space (MutableSequence[google.cloud.gdchardwaremanagement_v1alpha.types.RackSpace]):
            Optional. Spaces occupied by the hardware in
            the rack. If unset, this location is assumed to
            be the entire rack.
    """

    site: str = proto.Field(
        proto.STRING,
        number=1,
    )
    rack_location: str = proto.Field(
        proto.STRING,
        number=2,
    )
    rack_space: MutableSequence["RackSpace"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="RackSpace",
    )


class SubscriptionConfig(proto.Message):
    r"""A message to store a subscription configuration.

    Attributes:
        subscription_id (str):
            Output only. The unique identifier of the
            subscription.
        billing_id (str):
            Output only. The Google Cloud Billing ID that
            the subscription is created under.
        state (google.cloud.gdchardwaremanagement_v1alpha.types.SubscriptionConfig.SubscriptionState):
            Output only. The current state of the
            subscription.
    """

    class SubscriptionState(proto.Enum):
        r"""Enum to represent the state of the subscription.

        Values:
            SUBSCRIPTION_STATE_UNSPECIFIED (0):
                State is unspecified.
            ACTIVE (1):
                Active state means that the subscription has
                been created successfully and billing is
                happening.
            INACTIVE (2):
                Inactive means that the subscription has been
                created successfully, but billing has not
                started yet.
            ERROR (3):
                The subscription is in an erroneous state.
            FAILED_TO_RETRIEVE (4):
                The subscription state failed to be
                retrieved. This may be a transient issue. The
                user should retry the request.
            COMPLETED (5):
                The subscription has been completed, because
                it has reached the end date.
        """

        SUBSCRIPTION_STATE_UNSPECIFIED = 0
        ACTIVE = 1
        INACTIVE = 2
        ERROR = 3
        FAILED_TO_RETRIEVE = 4
        COMPLETED = 5

    subscription_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    billing_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    state: SubscriptionState = proto.Field(
        proto.ENUM,
        number=3,
        enum=SubscriptionState,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
