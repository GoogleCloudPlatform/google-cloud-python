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

import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.type.decimal_pb2 as decimal_pb2  # type: ignore
import google.type.money_pb2 as money_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.commerceproducer.v1beta",
    manifest={
        "Sku",
    },
)


class Sku(proto.Message):
    r"""Message describing the Sku resource.

    Encapsulates and represents a stock keeping unit (SKU), the atomic
    unit of pricing and billing in Google Cloud. Each customer charge is
    associated with and originates from exactly one SKU. While the Cloud
    Marketplace Sku resource shares a close relationship with the public
    `Sku resource in the Cloud Billing
    API <https://cloud.google.com/billing/docs/how-to/get-pricing-information-api>`__,
    Cloud Marketplace SKUs are represented here with additional
    information in an alternative format tailored for use by Cloud
    Marketplace partners, and are not necessarily public and by
    extension are not generally visible in the Cloud Billing API or the
    `Google Cloud Public SKUs <https://cloud.google.com/skus>`__.

    Note on terminology: While the name of the resource derives from the
    acronym 'SKU' it is named 'Sku' for consistency with other resource
    type names, and may be rendered variously as 'Sku', 'sku', or 'SKU'
    across this and other documentation.

    Attributes:
        name (str):
            Output only. Identifier. Name of the SKU.
        description (str):
            Output only. Description of the SKU.
        sku_price_timeline (MutableSequence[google.cloud.commerceproducer_v1beta.types.Sku.SkuPrice]):
            Output only. Timeline of the SKU prices, in chronological
            order by ``effective_time``.

            Each entry is active in the time range starting inclusively
            from the entry's ``effective_time`` and ending exclusively
            at the next entry's ``effective_time``, if one exists, or
            else remaining active indefinitely if it is the final entry.
            The currently active entry is the entry with the latest
            ``effective_time`` that is in the past. Because of scheduled
            future price changes the currently active entry may not be
            the last entry in the timeline. A SKU does not necessarily
            have a currently active entry, as the SKU's first timeline
            entry may have an ``effective_time`` in the future.
    """

    class SkuPrice(proto.Message):
        r"""The price of the SKU, active during a particular time range.
        Prices are in all cases in USD. Customers are billed in the
        currency of their billing account, subject to the currency
        conversion rate in effect at the time.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            inactive (google.cloud.commerceproducer_v1beta.types.Sku.SkuPrice.InactiveSkuPrice):
                Output only. The SKU has been disabled and
                has no price. SKUs, once created and allowed to
                go into effect, are never deleted. Disabled SKUs
                may accumulate over the lifetime of a product as
                the product's pricing evolves, and are retained
                for historical reference. A SKU in this state
                generally remains in this state indefinitely,
                but may be reactivated if needed. Clients must
                not depend on inactive SKUs remaining inactive.

                This field is a member of `oneof`_ ``sku_type``.
            managed_service_metric_usage_fee (google.cloud.commerceproducer_v1beta.types.Sku.SkuPrice.ManagedServiceMetricUsageFee):
                Output only. The SKU prices usage reported by
                the partner for a partner-defined custom billing
                metric.

                This field is a member of `oneof`_ ``sku_type``.
            gce_license_usage_fee (google.cloud.commerceproducer_v1beta.types.Sku.SkuPrice.ComputeEngineLicenseUsageFee):
                Output only. The SKU prices usage of a
                Compute Engine License via a license fee applied
                to running instances that use the license.

                This field is a member of `oneof`_ ``sku_type``.
            gke_pod_usage_fee (google.cloud.commerceproducer_v1beta.types.Sku.SkuPrice.KubernetesEnginePodUsageFee):
                Output only. The SKU prices usage of software
                deployed on Kubernetes Engine.

                This field is a member of `oneof`_ ``sku_type``.
            ai_platform_managed_model_usage_fee (google.cloud.commerceproducer_v1beta.types.Sku.SkuPrice.AiPlatformManagedModelUsageFee):
                Output only. The SKU prices usage of an AI
                Platform Managed Model (MaaS).

                This field is a member of `oneof`_ ``sku_type``.
            ai_platform_provisioned_throughput_fee (google.cloud.commerceproducer_v1beta.types.Sku.SkuPrice.AiPlatformProvisionedThroughputFee):
                Output only. The SKU prices reservation of AI
                Platform provisioned throughput.

                This field is a member of `oneof`_ ``sku_type``.
            ai_platform_deployed_model_usage_fee (google.cloud.commerceproducer_v1beta.types.Sku.SkuPrice.AiPlatformDeployedModelUsageFee):
                Output only. The SKU prices usage of an AI
                model deployed on AI Platform.

                This field is a member of `oneof`_ ``sku_type``.
            flat_subscription_fee (google.cloud.commerceproducer_v1beta.types.Sku.SkuPrice.FlatSubscriptionFee):
                Output only. The SKU applies a flat
                subscription fee.

                This field is a member of `oneof`_ ``sku_type``.
            effective_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. The start of the time interval
                during which this price is effective.
        """

        class InactiveSkuPrice(proto.Message):
            r"""Representation for a SKU that is not active and has no price."""

        class ManagedServiceMetricUsageFee(proto.Message):
            r"""Details about a SKU pricing usage of a `partner-reported custom
            billing
            metric <https://cloud.google.com/service-infrastructure/docs/reporting-billing-metrics>`__
            defined by the partner in the Service Management API and reported
            using the Service Control API.

            The customer's usage charge is computed by converting the customer's
            reported consumption to the SKU's composite price unit and applying
            the graduated price from the appropriate price tier.


            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                tiered_price (google.cloud.commerceproducer_v1beta.types.Sku.SkuPrice.TieredPrice):
                    Output only. `Tiered
                    pricing <https://cloud.google.com/billing/docs/how-to/pricing-table#tiered-pricing>`__
                    of the SKU.

                    This field is a member of `oneof`_ ``price_structure``.
                canonical_metric (str):
                    Output only. The name of the metric, in canonical format.

                    Note that in the canonical format the first character of the
                    path component of the metric name is always uppercase, which
                    may differ from the metric name in the service config. For
                    example, a metric appearing in the service config as
                    'example.com/example_metric' will appear here in the SKU as
                    'example.com/Example_metric'. In the Service Management and
                    Service Control APIs these two metric names are considered
                    distinct, either or both may be defined, and usage must be
                    reported using a name matching the name of a metric defined
                    in the service config. But for billing purposes usage
                    reported using either name will be aggregated under the
                    canonical metric name.

                    Example: "example.com/Example_metric".
            """

            tiered_price: "Sku.SkuPrice.TieredPrice" = proto.Field(
                proto.MESSAGE,
                number=2,
                oneof="price_structure",
                message="Sku.SkuPrice.TieredPrice",
            )
            canonical_metric: str = proto.Field(
                proto.STRING,
                number=1,
            )

        class ComputeEngineLicenseUsageFee(proto.Message):
            r"""Details about a SKU pricing usage of a `Compute Engine
            License <https://cloud.google.com/compute/docs/licenses/about>`__.

            The SKU applies to a single license, and may be further scoped to a
            `Compute Engine VM
            Instance <https://cloud.google.com/compute/docs/instances>`__
            machine resource type (e.g. "vCPU") and size range for that machine
            resource. Instances deployed from `Compute Engine
            Images <https://cloud.google.com/compute/docs/images>`__
            incorporating the target license and (if applicable) matching the
            machine resource type size range will be charged by the SKU. A
            single license may be priced by multiple SKUs covering different
            combinations of machine resource type and size range, allowing a
            single running instance to be charged by up to one SKU per machine
            resource type, with pricing tiered according to machine shape.


            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                price_per_unit (google.type.money_pb2.Money):
                    The price per unit of usage.
                    The customer's usage charge is computed by
                    measuring the customer's consumption denominated
                    in price units and multiplying by this price.

                    This field is a member of `oneof`_ ``price_structure``.
                license_code (str):
                    Output only. The license code of the target Compute Engine
                    License. Note that this is the numeric license code itself
                    in uint64 format used to reference licenses attached to
                    images, not the resource name of the related `Compute Engine
                    LicenseCode
                    resource <https://cloud.google.com/compute/docs/reference/rest/v1/licenseCodes>`__.

                    Example: "1234567890123456789".
                machine_resource (google.cloud.commerceproducer_v1beta.types.Sku.SkuPrice.ComputeEngineLicenseUsageFee.MachineResource):
                    Output only. The machine resource type that
                    the SKU applies to, if any. SKUs with a
                    non-default value are referred to as
                    "resource-based" SKUs.
                machine_resource_range (google.cloud.commerceproducer_v1beta.types.Sku.SkuPrice.ComputeEngineLicenseUsageFee.MachineResourceRange):
                    Output only. The range of machine resource values that the
                    SKU applies to. Unset when the SKU is not scoped to a
                    particular machine resource type. The collection of SKUs in
                    effect at any given time targeting the same license and
                    machine resource type will cover all possible values for
                    that machine resource type without overlap. Such a
                    collection of SKUs form a "tiered" price structure over the
                    possible values of the machine resource, with each SKU
                    acting as a "tier".

                    NOTE: This is distinct from a SKU with `tiered
                    pricing <https://cloud.google.com/billing/docs/how-to/pricing-table#tiered-pricing>`__.
                usage_calculation (google.cloud.commerceproducer_v1beta.types.Sku.SkuPrice.ComputeEngineLicenseUsageFee.UsageCalculation):
                    Output only. Determines how the customer's
                    usage is calculated.
                unit (str):
                    Output only. The price unit of the SKU.
                    See https://ucum.org/ucum.html for the format of
                    the price unit. For linear-priced memory SKUs,
                    the price unit is 'GiBy.h'. For all other SKUs,
                    the price unit is 'h'. This includes
                    linear-priced vCPU and GPU SKUs because these
                    resources have unitless dimensions and the
                    application of these scaling factors does not
                    change the price unit.
            """

            class MachineResource(proto.Enum):
                r"""The machine resource type that the SKU applies to, if any.

                Values:
                    MACHINE_RESOURCE_UNSPECIFIED (0):
                        The SKU applies to all instances irrespective
                        of machine shape. This is referred to as
                        "instance-based pricing" because the price is
                        the same for all instances.
                    VCPU_COUNT (1):
                        The SKU applies based on the instance's vCPU
                        count.
                    MEMORY_BYTES (2):
                        The SKU applies based on the instance's
                        memory size in bytes.
                    GPU_COUNT (3):
                        The SKU applies based on the instance's GPU
                        count.
                """

                MACHINE_RESOURCE_UNSPECIFIED = 0
                VCPU_COUNT = 1
                MEMORY_BYTES = 2
                GPU_COUNT = 3

            class UsageCalculation(proto.Enum):
                r"""Determines how the customer's usage is calculated.

                Values:
                    USAGE_CALCULATION_UNSPECIFIED (0):
                        Unused.
                    INSTANCE_RUNTIME (1):
                        Usage is calculated from instance runtime. The customer's
                        usage is metered according to the `Compute Engine VM
                        instance pricing
                        model <https://cloud.google.com/compute/vm-instance-pricing>`__,
                        measured on a per-instance basis in units of hours, with a
                        minimum duration of one minute and an increment of one
                        second.

                        A SKU using this usage calculation is referred to as "flat"
                        because the customer's usage charge is independent of the
                        instance's machine resource shape apart from determining
                        whether the SKU applies to the instance.
                    LINEAR_RESOURCE_SCALED_INSTANCE_RUNTIME (2):
                        Usage is calculated from instance runtime and size. This
                        calculation mode is only applicable to resource-based SKUs.
                        Usage is calculated by measuring the instance runtime in the
                        same manner as for ``INSTANCE_RUNTIME`` and multiplying by
                        the instance's machine resource value matching the SKU's
                        machine resource type. This converts the price from
                        per-instance-hour to per-instance-hour-per-machine-resource,
                        which changes the price unit for memory SKUs to 'GiBy.h'.
                        The price unit otherwise remains 'h' because the other
                        machine resources are dimensionless.

                        A SKU using this usage calculation is referred to as
                        "linear" because the customer's usage charge is linearly
                        proportional to the instance's machine resource value.
                """

                USAGE_CALCULATION_UNSPECIFIED = 0
                INSTANCE_RUNTIME = 1
                LINEAR_RESOURCE_SCALED_INSTANCE_RUNTIME = 2

            class MachineResourceRange(proto.Message):
                r"""The range of machine resource values that the SKU applies to.

                .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

                Attributes:
                    start_value (int):
                        Output only. The inclusive lower bound of the
                        range. While the number zero may be the start of
                        a range, it is not a possible machine resource
                        value. An instance cannot exist with zero vCPU
                        or memory, and an instance with no attached
                        accelerators lacks a GPU dimension entirely
                        rather than having a GPU count of zero.
                    end_value (int):
                        Output only. The exclusive upper bound of the
                        range. If no end value is specified, the range
                        is unbounded from above.

                        This field is a member of `oneof`_ ``_end_value``.
                """

                start_value: int = proto.Field(
                    proto.INT64,
                    number=1,
                )
                end_value: int = proto.Field(
                    proto.INT64,
                    number=2,
                    optional=True,
                )

            price_per_unit: money_pb2.Money = proto.Field(
                proto.MESSAGE,
                number=6,
                oneof="price_structure",
                message=money_pb2.Money,
            )
            license_code: str = proto.Field(
                proto.STRING,
                number=1,
            )
            machine_resource: "Sku.SkuPrice.ComputeEngineLicenseUsageFee.MachineResource" = proto.Field(
                proto.ENUM,
                number=2,
                enum="Sku.SkuPrice.ComputeEngineLicenseUsageFee.MachineResource",
            )
            machine_resource_range: "Sku.SkuPrice.ComputeEngineLicenseUsageFee.MachineResourceRange" = proto.Field(
                proto.MESSAGE,
                number=3,
                message="Sku.SkuPrice.ComputeEngineLicenseUsageFee.MachineResourceRange",
            )
            usage_calculation: "Sku.SkuPrice.ComputeEngineLicenseUsageFee.UsageCalculation" = proto.Field(
                proto.ENUM,
                number=4,
                enum="Sku.SkuPrice.ComputeEngineLicenseUsageFee.UsageCalculation",
            )
            unit: str = proto.Field(
                proto.STRING,
                number=5,
            )

        class KubernetesEnginePodUsageFee(proto.Message):
            r"""Details about a SKU pricing usage of software running on a
            Kubernetes Engine pod.

            The SKU applies to pods annotated with the SKU's parent service
            name, and may be further scoped to a `k8s pod resource
            type <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/>`__
            (e.g. "CPU") and size range for that resource type. Running pods
            annotated with the parent service's service name and matching the
            pod resource type size range will be charged by the SKU. A service
            may be priced by multiple SKUs covering different combinations of
            pod resource type and size range, allowing a single running pod to
            be charged by up to one SKU per pod resource type, with pricing
            tiered according to pod shape.


            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                price_per_unit (google.type.money_pb2.Money):
                    The price per unit of usage.
                    The customer's usage charge is computed by
                    measuring the customer's consumption denominated
                    in price units and multiplying by this price.

                    This field is a member of `oneof`_ ``price_structure``.
                pod_resource (google.cloud.commerceproducer_v1beta.types.Sku.SkuPrice.KubernetesEnginePodUsageFee.PodResource):
                    Output only. The pod resource type that the
                    SKU applies to. SKUs with a non-default value
                    are referred to as "resource-based" SKUs.
                pod_resource_range (google.cloud.commerceproducer_v1beta.types.Sku.SkuPrice.KubernetesEnginePodUsageFee.PodResourceRange):
                    Output only. The range of pod resource values that the SKU
                    applies to. The collection of SKUs in effect at any given
                    time targeting the same service annotation and pod resource
                    type will cover all possible values for that pod resource
                    type without overlap. Such a collection of SKUs form a
                    "tiered" price structure over the possible values of the pod
                    resource, with each SKU acting as a "tier".

                    NOTE: This is distinct from a SKU with `tiered
                    pricing <https://cloud.google.com/billing/docs/how-to/pricing-table#tiered-pricing>`__.
                usage_calculation (google.cloud.commerceproducer_v1beta.types.Sku.SkuPrice.KubernetesEnginePodUsageFee.UsageCalculation):
                    Output only. Determines how the customer's
                    usage is calculated.
                unit (str):
                    Output only. The price unit of the SKU.
                    See https://ucum.org/ucum.html for the format of
                    the price unit. For linear-priced memory SKUs,
                    the price unit is 'GiBy.h'. For all other SKUs,
                    the price unit is 'h'. This includes
                    linear-priced VCPU, GPU, and TPU SKUs because
                    these resources have unitless dimensions and the
                    application of these scaling factors does not
                    change the price unit.
            """

            class PodResource(proto.Enum):
                r"""The pod `resource
                type <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/>`__
                that the SKU applies to.

                Values:
                    POD_RESOURCE_UNSPECIFIED (0):
                        Unused.
                    VCPU_COUNT (1):
                        The SKU applies based on the pod's `vCPU
                        count <https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/>`__.
                    MEMORY_BYTES (2):
                        The SKU applies based on the pod's `memory
                        size <https://kubernetes.io/docs/tasks/configure-pod-container/assign-memory-resource/>`__
                        in bytes.
                    GPU_COUNT (3):
                        The SKU applies based on the pod's GPU count.
                    TPU_COUNT (4):
                        The SKU applies based on the pod's `TPU
                        count <https://cloud.google.com/kubernetes-engine/docs/concepts/tpus#how_tpus_work>`__.
                """

                POD_RESOURCE_UNSPECIFIED = 0
                VCPU_COUNT = 1
                MEMORY_BYTES = 2
                GPU_COUNT = 3
                TPU_COUNT = 4

            class UsageCalculation(proto.Enum):
                r"""Determines how the customer's usage is calculated.

                Values:
                    USAGE_CALCULATION_UNSPECIFIED (0):
                        Unused.
                    POD_RUNTIME (1):
                        Usage is calculated from pod runtime. The customer's usage
                        is metered in a manner similar to the `GKE Autopilot mode
                        for pods without specific hardware
                        requirements <https://cloud.google.com/kubernetes-engine/pricing>`__,
                        priced on a per-pod basis in units of hours and measured in
                        one-second increments, with no minimum duration.

                        A SKU using this usage calculation is referred to as "flat"
                        because the customer's usage charge is independent of the
                        pod shape apart from determining whether the SKU applies to
                        the pod.
                    LINEAR_RESOURCE_SCALED_POD_RUNTIME (2):
                        Usage is calculated from pod runtime and size. This
                        calculation mode is only applicable to resource-based SKUs.
                        Usage is calculated by measuring the pod runtime in the same
                        manner as for ``POD_RUNTIME`` and multiplying by the pod's
                        resource value matching the SKU's pod resource type. This
                        converts the price from per-pod-hour to
                        per-pod-hour-per-resource, which changes the price unit for
                        memory SKUs to 'GiBy.h'. The price unit otherwise remains
                        'h' because the other resources are dimensionless.

                        A SKU using this usage calculation is referred to as
                        "linear" because the customer's usage charge is linearly
                        proportional to the pod's resource value.
                """

                USAGE_CALCULATION_UNSPECIFIED = 0
                POD_RUNTIME = 1
                LINEAR_RESOURCE_SCALED_POD_RUNTIME = 2

            class PodResourceRange(proto.Message):
                r"""The range of pod resource values that the SKU applies to.

                .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

                Attributes:
                    start_value (int):
                        Output only. The inclusive lower bound of the
                        range.
                    end_value (int):
                        Output only. The exclusive upper bound of the
                        range. If no end value is specified, the range
                        is unbounded from above.

                        This field is a member of `oneof`_ ``_end_value``.
                """

                start_value: int = proto.Field(
                    proto.INT64,
                    number=1,
                )
                end_value: int = proto.Field(
                    proto.INT64,
                    number=2,
                    optional=True,
                )

            price_per_unit: money_pb2.Money = proto.Field(
                proto.MESSAGE,
                number=6,
                oneof="price_structure",
                message=money_pb2.Money,
            )
            pod_resource: "Sku.SkuPrice.KubernetesEnginePodUsageFee.PodResource" = (
                proto.Field(
                    proto.ENUM,
                    number=2,
                    enum="Sku.SkuPrice.KubernetesEnginePodUsageFee.PodResource",
                )
            )
            pod_resource_range: "Sku.SkuPrice.KubernetesEnginePodUsageFee.PodResourceRange" = proto.Field(
                proto.MESSAGE,
                number=3,
                message="Sku.SkuPrice.KubernetesEnginePodUsageFee.PodResourceRange",
            )
            usage_calculation: "Sku.SkuPrice.KubernetesEnginePodUsageFee.UsageCalculation" = proto.Field(
                proto.ENUM,
                number=4,
                enum="Sku.SkuPrice.KubernetesEnginePodUsageFee.UsageCalculation",
            )
            unit: str = proto.Field(
                proto.STRING,
                number=5,
            )

        class AiPlatformManagedModelUsageFee(proto.Message):
            r"""Details about a SKU pricing usage of an `AI Platform Managed Model
            (MaaS) <https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/use-partner-models>`__.


            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                tiered_price (google.cloud.commerceproducer_v1beta.types.Sku.SkuPrice.TieredPrice):
                    Output only. `Tiered
                    pricing <https://cloud.google.com/billing/docs/how-to/pricing-table#tiered-pricing>`__
                    of the SKU.

                    This field is a member of `oneof`_ ``price_structure``.
                usage_metric (google.cloud.commerceproducer_v1beta.types.Sku.SkuPrice.AiPlatformManagedModelUsageFee.AiPlatformManagedModelUsageMetric):
                    Output only. The usage metric that the SKU
                    applies to.
                location (google.cloud.commerceproducer_v1beta.types.Sku.SkuPrice.AiPlatformManagedModelEndpointLocation):
                    Output only. The model endpoint location
                    where usage is priced by this SKU. If no
                    location is specified, the SKU applies to usage
                    in all locations.
                prediction_mode (google.cloud.commerceproducer_v1beta.types.Sku.SkuPrice.AiPlatformManagedModelUsageFee.PredictionMode):
                    Output only. The prediction mode of requests
                    that the SKU applies to.
                combined_request_input_tokens_range (google.cloud.commerceproducer_v1beta.types.Sku.SkuPrice.AiPlatformManagedModelUsageFee.CombinedRequestInputTokensRange):
                    Output only. The range of aggregated input token values
                    covered by the SKU. Unset if the SKU is not scoped to a
                    particular range. A request is in scope for this SKU if its
                    aggregated input token value falls within the range. The
                    collection of SKUs in effect at any given time scoped to a
                    particular aggregated input token value range will cover all
                    possible values without overlap. Such a collection of SKUs
                    form a "tiered" price structure over the possible value,
                    with each SKU acting as a "tier".

                    NOTE: This is distinct from a SKU with `tiered
                    pricing <https://cloud.google.com/billing/docs/how-to/pricing-table#tiered-pricing>`__.
                provisioned_throughput_overage (google.cloud.commerceproducer_v1beta.types.Sku.SkuPrice.AiPlatformManagedModelUsageFee.ProvisionedThroughputOverage):
                    Output only. Set when the SKU is a historical
                    provisioned throughput overage SKU. Starting
                    2025-08-26 such SKUs have no effect, and usage
                    in excess of provisioned throughput quota is now
                    metered as standard usage. This field is set
                    only in historical SKU timeline entries for
                    overage SKUs belonging to partners that offered
                    provisioned throughput for AI Platform managed
                    model products prior to the unification of
                    standard usage and provisioned throughput
                    overage metering.
            """

            class PredictionMode(proto.Enum):
                r"""The prediction modes of requests that the SKU applies to.

                Values:
                    PREDICTION_MODE_UNSPECIFIED (0):
                        The SKU does not distinguish between
                        prediction modes.
                    ONLINE_PREDICTION (1):
                        The SKU applies to online prediction.
                    BATCH_PREDICTION (2):
                        The SKU applies to batch prediction.
                """

                PREDICTION_MODE_UNSPECIFIED = 0
                ONLINE_PREDICTION = 1
                BATCH_PREDICTION = 2

            class AiPlatformManagedModelUsageMetric(proto.Message):
                r"""The usage metric that the SKU applies to.

                This message has `oneof`_ fields (mutually exclusive fields).
                For each oneof, at most one member field can be set at the same time.
                Setting any member of the oneof automatically clears all other
                members.

                .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

                Attributes:
                    input_tokens_metric (google.cloud.commerceproducer_v1beta.types.Sku.SkuPrice.AiPlatformManagedModelUsageFee.AiPlatformManagedModelUsageMetric.InputTokensMetric):
                        Output only. Input tokens read from the
                        prediction endpoint input.

                        This field is a member of `oneof`_ ``metric``.
                    cache_read_input_tokens_metric (google.cloud.commerceproducer_v1beta.types.Sku.SkuPrice.AiPlatformManagedModelUsageFee.AiPlatformManagedModelUsageMetric.CacheReadInputTokensMetric):
                        Output only. Input tokens read from the
                        cache.

                        This field is a member of `oneof`_ ``metric``.
                    cache_write_input_tokens_metric (google.cloud.commerceproducer_v1beta.types.Sku.SkuPrice.AiPlatformManagedModelUsageFee.AiPlatformManagedModelUsageMetric.CacheWriteInputTokensMetric):
                        Output only. Input tokens written to the
                        cache.

                        This field is a member of `oneof`_ ``metric``.
                    output_tokens_metric (google.cloud.commerceproducer_v1beta.types.Sku.SkuPrice.AiPlatformManagedModelUsageFee.AiPlatformManagedModelUsageMetric.OutputTokensMetric):
                        Output only. Output tokens returned from the
                        prediction endpoint.

                        This field is a member of `oneof`_ ``metric``.
                    web_search_requests_metric (google.cloud.commerceproducer_v1beta.types.Sku.SkuPrice.AiPlatformManagedModelUsageFee.AiPlatformManagedModelUsageMetric.WebSearchRequestsMetric):
                        Output only. Web search requests executed by
                        the model.

                        This field is a member of `oneof`_ ``metric``.
                """

                class InputTokensMetric(proto.Message):
                    r"""Input tokens read from the input to the prediction endpoint.
                    The unit for this metric is dimensionless.

                    """

                class CacheReadInputTokensMetric(proto.Message):
                    r"""Input tokens read from the cache.
                    The unit for this metric is dimensionless.

                    """

                class CacheWriteInputTokensMetric(proto.Message):
                    r"""Input tokens written to the cache.
                    The unit for this metric is dimensionless.

                    Attributes:
                        ttl (google.protobuf.duration_pb2.Duration):
                            Output only. The duration the write is
                            retained in the cache.
                    """

                    ttl: duration_pb2.Duration = proto.Field(
                        proto.MESSAGE,
                        number=1,
                        message=duration_pb2.Duration,
                    )

                class OutputTokensMetric(proto.Message):
                    r"""Output tokens returned from the prediction endpoint.
                    The unit for this metric is dimensionless.

                    """

                class WebSearchRequestsMetric(proto.Message):
                    r"""Web search requests executed by the model.
                    The unit for this metric is dimensionless.

                    """

                input_tokens_metric: "Sku.SkuPrice.AiPlatformManagedModelUsageFee.AiPlatformManagedModelUsageMetric.InputTokensMetric" = proto.Field(
                    proto.MESSAGE,
                    number=1,
                    oneof="metric",
                    message="Sku.SkuPrice.AiPlatformManagedModelUsageFee.AiPlatformManagedModelUsageMetric.InputTokensMetric",
                )
                cache_read_input_tokens_metric: "Sku.SkuPrice.AiPlatformManagedModelUsageFee.AiPlatformManagedModelUsageMetric.CacheReadInputTokensMetric" = proto.Field(
                    proto.MESSAGE,
                    number=2,
                    oneof="metric",
                    message="Sku.SkuPrice.AiPlatformManagedModelUsageFee.AiPlatformManagedModelUsageMetric.CacheReadInputTokensMetric",
                )
                cache_write_input_tokens_metric: "Sku.SkuPrice.AiPlatformManagedModelUsageFee.AiPlatformManagedModelUsageMetric.CacheWriteInputTokensMetric" = proto.Field(
                    proto.MESSAGE,
                    number=3,
                    oneof="metric",
                    message="Sku.SkuPrice.AiPlatformManagedModelUsageFee.AiPlatformManagedModelUsageMetric.CacheWriteInputTokensMetric",
                )
                output_tokens_metric: "Sku.SkuPrice.AiPlatformManagedModelUsageFee.AiPlatformManagedModelUsageMetric.OutputTokensMetric" = proto.Field(
                    proto.MESSAGE,
                    number=4,
                    oneof="metric",
                    message="Sku.SkuPrice.AiPlatformManagedModelUsageFee.AiPlatformManagedModelUsageMetric.OutputTokensMetric",
                )
                web_search_requests_metric: "Sku.SkuPrice.AiPlatformManagedModelUsageFee.AiPlatformManagedModelUsageMetric.WebSearchRequestsMetric" = proto.Field(
                    proto.MESSAGE,
                    number=5,
                    oneof="metric",
                    message="Sku.SkuPrice.AiPlatformManagedModelUsageFee.AiPlatformManagedModelUsageMetric.WebSearchRequestsMetric",
                )

            class CombinedRequestInputTokensRange(proto.Message):
                r"""The range of aggregated input token values covered by the SKU.

                A request to a managed model has an aggregated input token value
                determined by the sum of the metric values of the input token
                metrics.

                - input tokens
                - cache read input tokens
                - cache write input tokens


                .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

                Attributes:
                    start_value (int):
                        Output only. The inclusive lower bound of the
                        range.
                    end_value (int):
                        Output only. The exclusive upper bound of the
                        range. If no end value is specified, the range
                        is unbounded from above.

                        This field is a member of `oneof`_ ``_end_value``.
                """

                start_value: int = proto.Field(
                    proto.INT64,
                    number=1,
                )
                end_value: int = proto.Field(
                    proto.INT64,
                    number=2,
                    optional=True,
                )

            class ProvisionedThroughputOverage(proto.Message):
                r"""Additional details present for historical provisioned
                throughput "overage" SKUs that applied charges only to usage
                above the customer's provisioned throughput quota threshold.

                Attributes:
                    service (str):
                        Output only. The service whose usage the
                        overage SKU applied to.
                """

                service: str = proto.Field(
                    proto.STRING,
                    number=1,
                )

            tiered_price: "Sku.SkuPrice.TieredPrice" = proto.Field(
                proto.MESSAGE,
                number=7,
                oneof="price_structure",
                message="Sku.SkuPrice.TieredPrice",
            )
            usage_metric: "Sku.SkuPrice.AiPlatformManagedModelUsageFee.AiPlatformManagedModelUsageMetric" = proto.Field(
                proto.MESSAGE,
                number=1,
                message="Sku.SkuPrice.AiPlatformManagedModelUsageFee.AiPlatformManagedModelUsageMetric",
            )
            location: "Sku.SkuPrice.AiPlatformManagedModelEndpointLocation" = (
                proto.Field(
                    proto.MESSAGE,
                    number=3,
                    message="Sku.SkuPrice.AiPlatformManagedModelEndpointLocation",
                )
            )
            prediction_mode: "Sku.SkuPrice.AiPlatformManagedModelUsageFee.PredictionMode" = proto.Field(
                proto.ENUM,
                number=4,
                enum="Sku.SkuPrice.AiPlatformManagedModelUsageFee.PredictionMode",
            )
            combined_request_input_tokens_range: "Sku.SkuPrice.AiPlatformManagedModelUsageFee.CombinedRequestInputTokensRange" = proto.Field(
                proto.MESSAGE,
                number=5,
                message="Sku.SkuPrice.AiPlatformManagedModelUsageFee.CombinedRequestInputTokensRange",
            )
            provisioned_throughput_overage: "Sku.SkuPrice.AiPlatformManagedModelUsageFee.ProvisionedThroughputOverage" = proto.Field(
                proto.MESSAGE,
                number=6,
                message="Sku.SkuPrice.AiPlatformManagedModelUsageFee.ProvisionedThroughputOverage",
            )

        class AiPlatformProvisionedThroughputFee(proto.Message):
            r"""Details about a SKU pricing reservation of `AI Platform Provisioned
            Throughput <https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput>`__.

            Customers may purchase provisioned throughput reservations for AI
            Platform managed model products. This provides the customer with
            provisioned throughput quota for a particular model and location.
            Model usage below the provisioned throughput quota threshold is
            voided and is not charged by the product's managed model usage fees.


            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                term_duration_months (int):
                    Output only. The duration of the provisioned
                    throughput reservation in months.

                    This field is a member of `oneof`_ ``term``.
                gsu_price_per_unit (google.type.money_pb2.Money):
                    The price per `Generative AI Scale Unit
                    (GSU) <https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput/measure-provisioned-throughput>`__
                    per ``unit``. A provisioned throughput reservation reserves
                    a certain number of GSUs, and the customer is billed for
                    those GSUs on a continuous basis for the duration of the
                    reservation.

                    This field is a member of `oneof`_ ``price_structure``.
                location (google.cloud.commerceproducer_v1beta.types.Sku.SkuPrice.AiPlatformManagedModelEndpointLocation):
                    Output only. The location where provisioned
                    throughput is priced by this SKU.
                unit (str):
                    Output only. The price unit of the SKU. See
                    https://ucum.org/ucum.html for the format of the price unit.
                    Since provisioned throughput reservations are billed by
                    duration, this will always be a time unit. The price unit of
                    a provisioned throughput SKU is not necessarily the same as
                    the reservation term. This field is unrelated to the
                    `Generative AI Scale Unit
                    (GSU) <https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput/measure-provisioned-throughput>`__.

                    Currently the unit is always months ('mo'). Additional time
                    units may be supported in future.

                    The customary unit month ('mo') requires special handling to
                    account for the variable duration of months. A price may be
                    denominated in units of months, but the duration the
                    reservation is active is measured in metric time and
                    customers are billed on that basis. The exact hourly or
                    per-second price can be calculated by dividing the monthly
                    price by the number of hours or seconds in the desired
                    month. A reservation active for N months is rarely billed
                    exactly N times the monthly price. This is intended and is
                    not a billing error.
            """

            term_duration_months: int = proto.Field(
                proto.INT32,
                number=2,
                oneof="term",
            )
            gsu_price_per_unit: money_pb2.Money = proto.Field(
                proto.MESSAGE,
                number=4,
                oneof="price_structure",
                message=money_pb2.Money,
            )
            location: "Sku.SkuPrice.AiPlatformManagedModelEndpointLocation" = (
                proto.Field(
                    proto.MESSAGE,
                    number=1,
                    message="Sku.SkuPrice.AiPlatformManagedModelEndpointLocation",
                )
            )
            unit: str = proto.Field(
                proto.STRING,
                number=3,
            )

        class AiPlatformDeployedModelUsageFee(proto.Message):
            r"""Details about a SKU pricing usage of an `AI Platform Self Deployed
            Model <https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/self-deployed-models>`__.


            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                accelerator_type (str):
                    Output only. The SKU applies to a specific accelerator type.
                    Contains the name of the matching `AI Platform
                    AcceleratorType <https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/MachineSpec#AcceleratorType>`__.
                    The corresponding linear scaling value is the dimensionless
                    ```accelerator_count`` <https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/MachineSpec#FIELDS.accelerator_count>`__.

                    This field is a member of `oneof`_ ``hardware_resource``.
                price_per_unit (google.type.money_pb2.Money):
                    Output only. The price per unit of usage.
                    The customer's usage charge is computed by
                    measuring the customer's consumption denominated
                    in price units and multiplying by this price.

                    This field is a member of `oneof`_ ``price_structure``.
                unit (str):
                    Output only. The price unit of the SKU.
                    See https://ucum.org/ucum.html for the format of
                    the price unit. Currently the unit is always
                    hours ('h'). This may change in future.
                usage_calculation (google.cloud.commerceproducer_v1beta.types.Sku.SkuPrice.AiPlatformDeployedModelUsageFee.UsageCalculation):
                    Output only. Determines how the customer's
                    usage is calculated.
            """

            class UsageCalculation(proto.Enum):
                r"""Determines how the customer's usage is calculated.

                Values:
                    USAGE_CALCULATION_UNSPECIFIED (0):
                        Unused.
                    LINEAR_RESOURCE_SCALED_DEPLOYMENT_RUNTIME (2):
                        Usage is calculated from deployment runtime and size. Usage
                        is calculated by measuring the deployment runtime in hours
                        and multiplying by the amount of the deployed model's
                        hardware resource matching the SKU's hardware resource type.
                        This results in a composite ``unit`` of hours ('h')
                        multiplied by the unit that denominates the hardware
                        resource, though note that multiplying by the dimensionless
                        unit ("1") has no effect.
                """

                USAGE_CALCULATION_UNSPECIFIED = 0
                LINEAR_RESOURCE_SCALED_DEPLOYMENT_RUNTIME = 2

            accelerator_type: str = proto.Field(
                proto.STRING,
                number=2,
                oneof="hardware_resource",
            )
            price_per_unit: money_pb2.Money = proto.Field(
                proto.MESSAGE,
                number=5,
                oneof="price_structure",
                message=money_pb2.Money,
            )
            unit: str = proto.Field(
                proto.STRING,
                number=3,
            )
            usage_calculation: "Sku.SkuPrice.AiPlatformDeployedModelUsageFee.UsageCalculation" = proto.Field(
                proto.ENUM,
                number=4,
                enum="Sku.SkuPrice.AiPlatformDeployedModelUsageFee.UsageCalculation",
            )

        class FlatSubscriptionFee(proto.Message):
            r"""Details about a SKU charging a flat subscription fee.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                price_per_unit (google.type.money_pb2.Money):
                    Output only. The price per time unit the
                    subscription is active.

                    This field is a member of `oneof`_ ``price_structure``.
                unit (str):
                    Output only. The unit of the subscription
                    SKU. See https://ucum.org/ucum.html for the
                    format of the price unit. Since subscriptions
                    are billed by duration, this will always be a
                    time unit. The price unit of a subscription SKU
                    is not necessarily the same as the subscription
                    period of the corresponding StandardOffers.

                    Currently the unit is always months ('mo').
                    Additional time units may be supported in
                    future.

                    The unit month ('mo') is a customary time unit
                    and requires special handling to account for the
                    variable duration of months. A price may be
                    denominated in units of months, but the duration
                    the subscription is active is measured in metric
                    time and customers are billed on that basis. The
                    exact hourly or per-second price can be
                    calculated by dividing the monthly price by the
                    number of hours or seconds in the desired month.
                    A subscription active for N months is rarely
                    billed exactly N times the monthly price. This
                    is intended and is not a billing error.
            """

            price_per_unit: money_pb2.Money = proto.Field(
                proto.MESSAGE,
                number=3,
                oneof="price_structure",
                message=money_pb2.Money,
            )
            unit: str = proto.Field(
                proto.STRING,
                number=2,
            )

        class TieredPrice(proto.Message):
            r"""Price structure for a SKU charging a `tiered
            price <https://cloud.google.com/billing/docs/how-to/pricing-table#tiered-pricing>`__.

            Attributes:
                unit (str):
                    Output only. Usage unit used for defining price tiers and
                    for scaling with the price_unit_count to form the composite
                    price unit.

                    See https://ucum.org/ucum.html for the format of the price
                    unit. A unitless dimension, such as a count, is represented
                    as ``1``.
                unit_description (str):
                    Output only. The display description of the
                    unit, supplied at time of onboarding. This value
                    is recommended to be set at least for
                    dimensionless metrics, but may be empty if no
                    description was provided at time of onboarding.
                price_unit_count (google.type.decimal_pb2.Decimal):
                    Output only. Scaling the ``unit`` by the
                    ``price_unit_count`` forms the composite "price unit" which
                    is priced by the price tiers.

                    This scaling factor is in addition to any numerical prefix
                    symbol on the ``unit``, so the same composite "price unit"
                    can be represented in several ways, differing only in their
                    presentation to users.

                    Examples:

                    - $1 per 1 bytes : unit = By, price_unit_count = 1
                    - $1000 per 1 kilobytes : unit = kBy, price_unit_count = 1
                    - $5000 per 5 kilobytes : unit = kBy, price_unit_count = 5
                price_tiers (MutableSequence[google.cloud.commerceproducer_v1beta.types.Sku.SkuPrice.TieredPrice.PriceTier]):
                    Output only. The list of price tiers for the SKU, ordered by
                    the start_amount.

                    The tiers are non-overlapping and are collectively bounded
                    below by zero and unbounded above to cover the entire range
                    of possible metric usage. Each tier is bounded below
                    inclusively by its start_amount and bounded above
                    exclusively by the start_amount of the next tier, or else
                    unbounded above if there is no next tier.

                    Usage of the metric is aggregated by customer billing
                    account on a monthly basis and billed in a graduated manner
                    according to the price tiers, with each marginal unit of
                    usage priced accoring to the tier in which it falls.
            """

            class PriceTier(proto.Message):
                r"""A `price
                tier <https://cloud.google.com/billing/docs/how-to/pricing-table#tiered-pricing>`__
                pricing metric usage within a range.

                Each marginal unit of usage is priced according to the price tier in
                which it falls.

                Attributes:
                    start_amount (google.type.decimal_pb2.Decimal):
                        Output only. Inclusive lower bound of the tier interval,
                        denominated in ``unit``.
                    price (google.type.money_pb2.Money):
                        Output only. The price per ``price_unit_count`` of ``unit``
                        in the tier. The price is applied fractionally if the
                        customer's usage within the tier is not an integer multiple
                        of ``price_unit_count``.
                """

                start_amount: decimal_pb2.Decimal = proto.Field(
                    proto.MESSAGE,
                    number=1,
                    message=decimal_pb2.Decimal,
                )
                price: money_pb2.Money = proto.Field(
                    proto.MESSAGE,
                    number=2,
                    message=money_pb2.Money,
                )

            unit: str = proto.Field(
                proto.STRING,
                number=1,
            )
            unit_description: str = proto.Field(
                proto.STRING,
                number=2,
            )
            price_unit_count: decimal_pb2.Decimal = proto.Field(
                proto.MESSAGE,
                number=3,
                message=decimal_pb2.Decimal,
            )
            price_tiers: MutableSequence["Sku.SkuPrice.TieredPrice.PriceTier"] = (
                proto.RepeatedField(
                    proto.MESSAGE,
                    number=4,
                    message="Sku.SkuPrice.TieredPrice.PriceTier",
                )
            )

        class AiPlatformManagedModelEndpointLocation(proto.Message):
            r"""Location scope for a SKU that applies to an AI Platform
            Managed Model endpoint.

            This message has `oneof`_ fields (mutually exclusive fields).
            For each oneof, at most one member field can be set at the same time.
            Setting any member of the oneof automatically clears all other
            members.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                region_id (str):
                    Output only. The SKU applies to a region.

                    This field is a member of `oneof`_ ``location``.
                global_endpoint (bool):
                    Output only. The SKU applies to a `global
                    endpoint <https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/locations>`__.
                    **Note**: This is distinct from the conventional meaning of
                    "global" as a SKU that applies to all locations.

                    This field is a member of `oneof`_ ``location``.
                multi_region_id (str):
                    Output only. The SKU applies to a
                    multi-region.

                    This field is a member of `oneof`_ ``location``.
            """

            region_id: str = proto.Field(
                proto.STRING,
                number=1,
                oneof="location",
            )
            global_endpoint: bool = proto.Field(
                proto.BOOL,
                number=2,
                oneof="location",
            )
            multi_region_id: str = proto.Field(
                proto.STRING,
                number=3,
                oneof="location",
            )

        inactive: "Sku.SkuPrice.InactiveSkuPrice" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="sku_type",
            message="Sku.SkuPrice.InactiveSkuPrice",
        )
        managed_service_metric_usage_fee: "Sku.SkuPrice.ManagedServiceMetricUsageFee" = proto.Field(
            proto.MESSAGE,
            number=3,
            oneof="sku_type",
            message="Sku.SkuPrice.ManagedServiceMetricUsageFee",
        )
        gce_license_usage_fee: "Sku.SkuPrice.ComputeEngineLicenseUsageFee" = (
            proto.Field(
                proto.MESSAGE,
                number=4,
                oneof="sku_type",
                message="Sku.SkuPrice.ComputeEngineLicenseUsageFee",
            )
        )
        gke_pod_usage_fee: "Sku.SkuPrice.KubernetesEnginePodUsageFee" = proto.Field(
            proto.MESSAGE,
            number=5,
            oneof="sku_type",
            message="Sku.SkuPrice.KubernetesEnginePodUsageFee",
        )
        ai_platform_managed_model_usage_fee: "Sku.SkuPrice.AiPlatformManagedModelUsageFee" = proto.Field(
            proto.MESSAGE,
            number=6,
            oneof="sku_type",
            message="Sku.SkuPrice.AiPlatformManagedModelUsageFee",
        )
        ai_platform_provisioned_throughput_fee: "Sku.SkuPrice.AiPlatformProvisionedThroughputFee" = proto.Field(
            proto.MESSAGE,
            number=7,
            oneof="sku_type",
            message="Sku.SkuPrice.AiPlatformProvisionedThroughputFee",
        )
        ai_platform_deployed_model_usage_fee: "Sku.SkuPrice.AiPlatformDeployedModelUsageFee" = proto.Field(
            proto.MESSAGE,
            number=8,
            oneof="sku_type",
            message="Sku.SkuPrice.AiPlatformDeployedModelUsageFee",
        )
        flat_subscription_fee: "Sku.SkuPrice.FlatSubscriptionFee" = proto.Field(
            proto.MESSAGE,
            number=9,
            oneof="sku_type",
            message="Sku.SkuPrice.FlatSubscriptionFee",
        )
        effective_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=1,
            message=timestamp_pb2.Timestamp,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    sku_price_timeline: MutableSequence[SkuPrice] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=SkuPrice,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
