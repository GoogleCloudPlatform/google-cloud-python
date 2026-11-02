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

import google.type.date_pb2 as date_pb2  # type: ignore
import google.type.latlng_pb2 as latlng_pb2  # type: ignore
import google.type.money_pb2 as money_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.maps.solar.v1",
    manifest={
        "AdditionalInsights",
        "DataLayerView",
        "ImageryQuality",
        "SolarPanelOrientation",
        "Experiment",
        "FindClosestBuildingInsightsRequest",
        "LatLngBox",
        "BuildingInsights",
        "SolarPotential",
        "RoofSegmentSizeAndSunshineStats",
        "SizeAndSunshineStats",
        "SolarPanel",
        "SolarPanelConfig",
        "RoofSegmentSummary",
        "FinancialAnalysis",
        "FinancialDetails",
        "SavingsOverTime",
        "LeasingSavings",
        "CashPurchaseSavings",
        "FinancedPurchaseSavings",
        "GetDataLayersRequest",
        "DataLayers",
        "GetGeoTiffRequest",
    },
)


class AdditionalInsights(proto.Enum):
    r"""Additional building information such as roof geometry and
    solar panel arrays that can be returned in BuildingInsights.

    New values may be added to this enum in the future.

    Values:
        ADDITIONAL_INSIGHTS_UNSPECIFIED (0):
            The default value. The default
            BuildingInsights will be returned.
        DETECTED_ARRAYS (2):
            Determines whether the response will include the detected
            arrays.

            If specified, the ``detected_arrays`` field will be
            populated in the response.
    """

    ADDITIONAL_INSIGHTS_UNSPECIFIED = 0
    DETECTED_ARRAYS = 2


class DataLayerView(proto.Enum):
    r"""What subset of the solar information to return.

    Values:
        DATA_LAYER_VIEW_UNSPECIFIED (0):
            Equivalent to FULL.
        DSM_LAYER (1):
            Get the DSM only.
        IMAGERY_LAYERS (2):
            Get the DSM, RGB, and mask.
        IMAGERY_AND_ANNUAL_FLUX_LAYERS (3):
            Get the DSM, RGB, mask, and annual flux.
        IMAGERY_AND_ALL_FLUX_LAYERS (4):
            Get the DSM, RGB, mask, annual flux, and
            monthly flux.
        FULL_LAYERS (5):
            Get all data.
    """

    DATA_LAYER_VIEW_UNSPECIFIED = 0
    DSM_LAYER = 1
    IMAGERY_LAYERS = 2
    IMAGERY_AND_ANNUAL_FLUX_LAYERS = 3
    IMAGERY_AND_ALL_FLUX_LAYERS = 4
    FULL_LAYERS = 5


class ImageryQuality(proto.Enum):
    r"""The quality of the imagery used to compute some API result.

    Note: Regardless of imagery quality level, DSM outputs always
    have a resolution of 0.1 m/pixel, monthly flux outputs always
    have a resolution of 0.5 m/pixel, and hourly shade outputs
    always have a resolution of 1 m/pixel.

    Values:
        IMAGERY_QUALITY_UNSPECIFIED (0):
            No quality is known.
        HIGH (1):
            Solar data is derived from aerial imagery
            captured at low-altitude and processed at 0.1
            m/pixel.
        MEDIUM (2):
            Solar data is derived from enhanced aerial
            imagery captured at high-altitude and processed
            at 0.25 m/pixel.
        LOW (3):
            Solar data is derived from enhanced satellite
            imagery processed at 0.25 m/pixel.
        BASE (4):
            Solar data is derived from enhanced satellite
            imagery processed at 0.25 m/pixel.
    """

    IMAGERY_QUALITY_UNSPECIFIED = 0
    HIGH = 1
    MEDIUM = 2
    LOW = 3
    BASE = 4


class SolarPanelOrientation(proto.Enum):
    r"""The orientation of a solar panel. This must be interpreted
    relative to the azimuth of the roof segment that the panel is
    placed on.

    Values:
        SOLAR_PANEL_ORIENTATION_UNSPECIFIED (0):
            No panel orientation is known.
        LANDSCAPE (1):
            A ``LANDSCAPE`` panel has its long edge perpendicular to the
            azimuth direction of the roof segment that it is placed on.
        PORTRAIT (2):
            A ``PORTRAIT`` panel has its long edge parallel to the
            azimuth direction of the roof segment that it is placed on.
    """

    SOLAR_PANEL_ORIENTATION_UNSPECIFIED = 0
    LANDSCAPE = 1
    PORTRAIT = 2


class Experiment(proto.Enum):
    r"""Specifies pre-GA experiments that can be enabled in the API.

    Requests using this field are classified as a pre-GA offering under
    the `Google Maps Platform Service Specific
    Terms <https://cloud.google.com/maps-platform/terms/maps-service-terms>`__.
    See `launch stage
    descriptions <https://cloud.google.com/maps-platform/terms/launch-stages>`__
    for more details.

    New values may be added to this enum in the future.

    Values:
        EXPERIMENT_UNSPECIFIED (0):
            No experiments are specified.
        EXPANDED_COVERAGE (1):
            Expands the geographic region available for querying solar
            data. For more information, see `Expanded
            Coverage <https://developers.google.com/maps/documentation/solar/expanded-coverage>`__.
    """

    EXPERIMENT_UNSPECIFIED = 0
    EXPANDED_COVERAGE = 1


class FindClosestBuildingInsightsRequest(proto.Message):
    r"""Request message for ``Solar.FindClosestBuildingInsights``.

    Attributes:
        location (google.type.latlng_pb2.LatLng):
            Required. The longitude and latitude from
            which the API looks for the nearest known
            building.
        required_quality (google.maps.solar_v1.types.ImageryQuality):
            Optional. The minimum quality level allowed
            in the results. No result with lower quality
            than this will be returned. Not specifying this
            is equivalent to restricting to HIGH quality
            only.
        exact_quality_required (bool):
            Optional. Whether to require exact quality of the imagery.
            If set to false, the ``required_quality`` field is
            interpreted as the minimum required quality, such that HIGH
            quality imagery may be returned when ``required_quality`` is
            set to MEDIUM. If set to true, ``required_quality`` is
            interpreted as the exact required quality and only
            ``MEDIUM`` quality imagery is returned if
            ``required_quality`` is set to ``MEDIUM``.
        experiments (MutableSequence[google.maps.solar_v1.types.Experiment]):
            Optional. Specifies the pre-GA experiments to enable.
            Requests using this field are classified as a pre-GA
            offering under the `Google Maps Platform Service Specific
            Terms <https://cloud.google.com/maps-platform/terms/maps-service-terms>`__.
            See `launch stage
            descriptions <https://cloud.google.com/maps-platform/terms/launch-stages>`__
            for more details.
        additional_insights (MutableSequence[google.maps.solar_v1.types.AdditionalInsights]):
            Optional. A list of
            [additional_insights][google.maps.solar.v1.FindClosestBuildingInsightsRequest.additional_insights]
            to be included in the response.
    """

    location: latlng_pb2.LatLng = proto.Field(
        proto.MESSAGE,
        number=1,
        message=latlng_pb2.LatLng,
    )
    required_quality: "ImageryQuality" = proto.Field(
        proto.ENUM,
        number=3,
        enum="ImageryQuality",
    )
    exact_quality_required: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    experiments: MutableSequence["Experiment"] = proto.RepeatedField(
        proto.ENUM,
        number=5,
        enum="Experiment",
    )
    additional_insights: MutableSequence["AdditionalInsights"] = proto.RepeatedField(
        proto.ENUM,
        number=6,
        enum="AdditionalInsights",
    )


class LatLngBox(proto.Message):
    r"""A bounding box in lat/lng coordinates.

    Attributes:
        sw (google.type.latlng_pb2.LatLng):
            The southwest corner of the box.
        ne (google.type.latlng_pb2.LatLng):
            The northeast corner of the box.
    """

    sw: latlng_pb2.LatLng = proto.Field(
        proto.MESSAGE,
        number=1,
        message=latlng_pb2.LatLng,
    )
    ne: latlng_pb2.LatLng = proto.Field(
        proto.MESSAGE,
        number=2,
        message=latlng_pb2.LatLng,
    )


class BuildingInsights(proto.Message):
    r"""Response message for ``Solar.FindClosestBuildingInsights``.
    Information about the location, dimensions, and solar potential of a
    building.

    Attributes:
        name (str):
            The resource name for the building, of the format
            ``buildings/{place_id}``.
        center (google.type.latlng_pb2.LatLng):
            A point near the center of the building.
        bounding_box (google.maps.solar_v1.types.LatLngBox):
            The bounding box of the building.
        imagery_date (google.type.date_pb2.Date):
            Date that the underlying imagery was
            acquired. This is approximate.
        imagery_processed_date (google.type.date_pb2.Date):
            When processing was completed on this
            imagery.
        postal_code (str):
            Postal code (e.g., US zip code) this building
            is contained by.
        administrative_area (str):
            Administrative area 1 (e.g., in the US, the
            state) that contains this building. For example,
            in the US, the abbreviation might be "MA" or
            "CA.".
        statistical_area (str):
            Statistical area (e.g., US census tract) this
            building is in.
        region_code (str):
            Region code for the country (or region) this
            building is in.
        solar_potential (google.maps.solar_v1.types.SolarPotential):
            Solar potential of the building.
        imagery_quality (google.maps.solar_v1.types.ImageryQuality):
            The quality of the imagery used to compute
            the data for this building.
        detected_arrays (google.maps.solar_v1.types.BuildingInsights.DetectedArrays):
            Solar arrays detected on the building. This field is only
            populated if DETECTED_ARRAYS is included in the request's
            [FindClosestBuildingInsightsRequest.additional_insights][google.maps.solar.v1.FindClosestBuildingInsightsRequest.additional_insights].
    """

    class DetectedArrays(proto.Message):
        r"""Information about solar arrays detected on the building.

        Attributes:
            detection_status (google.maps.solar_v1.types.BuildingInsights.DetectedArrays.DetectionStatus):
                Indicates the detection status of solar
                arrays for this building.
            latest_capture_date (google.type.date_pb2.Date):
                The date indicating when the latest solar
                array data was captured.
        """

        class DetectionStatus(proto.Enum):
            r"""Indicates the detection status of solar arrays for this
            building.

            Values:
                DETECTION_STATUS_UNSPECIFIED (0):
                    Unspecified status.
                DETECTION_STATUS_DATA_UNAVAILABLE (1):
                    Detected solar array data is unavailable for
                    this building.
                DETECTION_STATUS_ARRAYS_DETECTED (2):
                    At least one solar array has been detected
                    for this building.
                DETECTION_STATUS_NO_ARRAYS_DETECTED (3):
                    No solar arrays detected for this building.
            """

            DETECTION_STATUS_UNSPECIFIED = 0
            DETECTION_STATUS_DATA_UNAVAILABLE = 1
            DETECTION_STATUS_ARRAYS_DETECTED = 2
            DETECTION_STATUS_NO_ARRAYS_DETECTED = 3

        detection_status: "BuildingInsights.DetectedArrays.DetectionStatus" = (
            proto.Field(
                proto.ENUM,
                number=1,
                enum="BuildingInsights.DetectedArrays.DetectionStatus",
            )
        )
        latest_capture_date: date_pb2.Date = proto.Field(
            proto.MESSAGE,
            number=3,
            message=date_pb2.Date,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    center: latlng_pb2.LatLng = proto.Field(
        proto.MESSAGE,
        number=2,
        message=latlng_pb2.LatLng,
    )
    bounding_box: "LatLngBox" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="LatLngBox",
    )
    imagery_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=3,
        message=date_pb2.Date,
    )
    imagery_processed_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=11,
        message=date_pb2.Date,
    )
    postal_code: str = proto.Field(
        proto.STRING,
        number=4,
    )
    administrative_area: str = proto.Field(
        proto.STRING,
        number=5,
    )
    statistical_area: str = proto.Field(
        proto.STRING,
        number=6,
    )
    region_code: str = proto.Field(
        proto.STRING,
        number=7,
    )
    solar_potential: "SolarPotential" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="SolarPotential",
    )
    imagery_quality: "ImageryQuality" = proto.Field(
        proto.ENUM,
        number=10,
        enum="ImageryQuality",
    )
    detected_arrays: DetectedArrays = proto.Field(
        proto.MESSAGE,
        number=12,
        message=DetectedArrays,
    )


class SolarPotential(proto.Message):
    r"""Information about the solar potential of a building. A number of
    fields in this are defined in terms of "panels". The fields
    [panel_capacity_watts]
    [google.maps.solar.v1.SolarPotential.panel_capacity_watts],
    [panel_height_meters]
    [google.maps.solar.v1.SolarPotential.panel_height_meters], and
    [panel_width_meters]
    [google.maps.solar.v1.SolarPotential.panel_width_meters] describe
    the parameters of the model of panel used in these calculations.

    Attributes:
        max_array_panels_count (int):
            Size of the maximum array - that is, the
            maximum number of panels that can fit on the
            roof.
        panel_capacity_watts (float):
            Capacity, in watts, of the panel used in the
            calculations.
        panel_height_meters (float):
            Height, in meters in portrait orientation, of
            the panel used in the calculations.
        panel_width_meters (float):
            Width, in meters in portrait orientation, of
            the panel used in the calculations.
        panel_lifetime_years (int):
            The expected lifetime, in years, of the solar
            panels. This is used in the financial
            calculations.
        max_array_area_meters2 (float):
            Size, in square meters, of the maximum array.
        max_sunshine_hours_per_year (float):
            Maximum number of sunshine hours received per
            year, by any point on the roof. Sunshine hours
            are a measure of the total amount of insolation
            (energy) received per year. 1 sunshine hour = 1
            kWh per kW (where kW refers to kW of capacity
            under Standard Testing Conditions).
        carbon_offset_factor_kg_per_mwh (float):
            Equivalent amount of CO2 produced per MWh of
            grid electricity. This is a measure of the
            carbon intensity of grid electricity displaced
            by solar electricity.
        whole_roof_stats (google.maps.solar_v1.types.SizeAndSunshineStats):
            Total size and sunlight quantiles for the part of the roof
            that was assigned to some roof segment. Despite the name,
            this may not include the entire building. See
            [building_stats]
            [google.maps.solar.v1.SolarPotential.building_stats].
        building_stats (google.maps.solar_v1.types.SizeAndSunshineStats):
            Size and sunlight quantiles for the entire building,
            including parts of the roof that were not assigned to some
            roof segment. Because the orientations of these parts are
            not well characterised, the roof area estimate is
            unreliable, but the ground area estimate is reliable. It may
            be that a more reliable whole building roof area can be
            obtained by scaling the roof area from [whole_roof_stats]
            [google.maps.solar.v1.SolarPotential.whole_roof_stats] by
            the ratio of the ground areas of ``building_stats`` and
            ``whole_roof_stats``.
        roof_segment_stats (MutableSequence[google.maps.solar_v1.types.RoofSegmentSizeAndSunshineStats]):
            Size and sunlight quantiles for each roof
            segment.
        solar_panels (MutableSequence[google.maps.solar_v1.types.SolarPanel]):
            Each [SolarPanel][google.maps.solar.v1.SolarPanel] describes
            a single solar panel. They are listed in the order that the
            panel layout algorithm placed this. This is usually, though
            not always, in decreasing order of annual energy production.
        solar_panel_configs (MutableSequence[google.maps.solar_v1.types.SolarPanelConfig]):
            Each [SolarPanelConfig]
            [google.maps.solar.v1.SolarPanelConfig] describes a
            different arrangement of solar panels on the roof. They are
            in order of increasing number of panels. The
            ``SolarPanelConfig`` with [panels_count]
            [google.maps.solar.v1.SolarPanelConfig.panels_count]=N is
            based on the first N panels in the ``solar_panels`` list.
            This field is only populated if at least 4 panels can fit on
            a roof.
        financial_analyses (MutableSequence[google.maps.solar_v1.types.FinancialAnalysis]):
            A [FinancialAnalysis]
            [google.maps.solar.v1.FinancialAnalysis] gives the savings
            from going solar assuming a given monthly bill and a given
            electricity provider. They are in order of increasing order
            of monthly bill amount. This field will be empty for
            buildings in areas for which the Solar API does not have
            enough information to perform financial computations.
    """

    max_array_panels_count: int = proto.Field(
        proto.INT32,
        number=1,
    )
    panel_capacity_watts: float = proto.Field(
        proto.FLOAT,
        number=9,
    )
    panel_height_meters: float = proto.Field(
        proto.FLOAT,
        number=10,
    )
    panel_width_meters: float = proto.Field(
        proto.FLOAT,
        number=11,
    )
    panel_lifetime_years: int = proto.Field(
        proto.INT32,
        number=12,
    )
    max_array_area_meters2: float = proto.Field(
        proto.FLOAT,
        number=2,
    )
    max_sunshine_hours_per_year: float = proto.Field(
        proto.FLOAT,
        number=3,
    )
    carbon_offset_factor_kg_per_mwh: float = proto.Field(
        proto.FLOAT,
        number=4,
    )
    whole_roof_stats: "SizeAndSunshineStats" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="SizeAndSunshineStats",
    )
    building_stats: "SizeAndSunshineStats" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="SizeAndSunshineStats",
    )
    roof_segment_stats: MutableSequence["RoofSegmentSizeAndSunshineStats"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=6,
            message="RoofSegmentSizeAndSunshineStats",
        )
    )
    solar_panels: MutableSequence["SolarPanel"] = proto.RepeatedField(
        proto.MESSAGE,
        number=14,
        message="SolarPanel",
    )
    solar_panel_configs: MutableSequence["SolarPanelConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="SolarPanelConfig",
    )
    financial_analyses: MutableSequence["FinancialAnalysis"] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message="FinancialAnalysis",
    )


class RoofSegmentSizeAndSunshineStats(proto.Message):
    r"""Information about the size and sunniness quantiles of a roof
    segment.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        pitch_degrees (float):
            Angle of the roof segment relative to the
            theoretical ground plane. 0 = parallel to the
            ground, 90 = perpendicular to the ground.

            This field is a member of `oneof`_ ``_pitch_degrees``.
        azimuth_degrees (float):
            Compass direction the roof segment is pointing in. 0 =
            North, 90 = East, 180 = South. For a "flat" roof segment
            (``pitch_degrees`` very near 0), azimuth is not well
            defined, so for consistency, we define it arbitrarily to be
            0 (North).

            This field is a member of `oneof`_ ``_azimuth_degrees``.
        stats (google.maps.solar_v1.types.SizeAndSunshineStats):
            Total size and sunlight quantiles for the
            roof segment.
        center (google.type.latlng_pb2.LatLng):
            A point near the center of the roof segment.
        bounding_box (google.maps.solar_v1.types.LatLngBox):
            The bounding box of the roof segment.
        plane_height_at_center_meters (float):
            The height of the roof segment plane, in meters above sea
            level, at the point designated by ``center``. Together with
            the pitch, azimuth, and center location, this fully defines
            the roof segment plane.

            This field is a member of `oneof`_ ``_plane_height_at_center_meters``.
    """

    pitch_degrees: float = proto.Field(
        proto.FLOAT,
        number=1,
        optional=True,
    )
    azimuth_degrees: float = proto.Field(
        proto.FLOAT,
        number=2,
        optional=True,
    )
    stats: "SizeAndSunshineStats" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="SizeAndSunshineStats",
    )
    center: latlng_pb2.LatLng = proto.Field(
        proto.MESSAGE,
        number=4,
        message=latlng_pb2.LatLng,
    )
    bounding_box: "LatLngBox" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="LatLngBox",
    )
    plane_height_at_center_meters: float = proto.Field(
        proto.FLOAT,
        number=6,
        optional=True,
    )


class SizeAndSunshineStats(proto.Message):
    r"""Size and sunniness quantiles of a roof, or part of a roof.

    Attributes:
        area_meters2 (float):
            The area of the roof or roof segment, in m^2.
            This is the roof area (accounting for tilt), not
            the ground footprint area.
        sunshine_quantiles (MutableSequence[float]):
            Quantiles of the pointwise sunniness across the area. If
            there are N values here, this represents the (N-1)-iles. For
            example, if there are 5 values, then they would be the
            quartiles (min, 25%, 50%, 75%, max). Values are in annual
            kWh/kW like [max_sunshine_hours_per_year]
            [google.maps.solar.v1.SolarPotential.max_sunshine_hours_per_year].
        ground_area_meters2 (float):
            The ground footprint area covered by the roof
            or roof segment, in m^2.
    """

    area_meters2: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    sunshine_quantiles: MutableSequence[float] = proto.RepeatedField(
        proto.FLOAT,
        number=2,
    )
    ground_area_meters2: float = proto.Field(
        proto.FLOAT,
        number=3,
    )


class SolarPanel(proto.Message):
    r"""SolarPanel describes the position, orientation, and production of a
    single solar panel. See the [panel_height_meters]
    [google.maps.solar.v1.SolarPotential.panel_height_meters],
    [panel_width_meters]
    [google.maps.solar.v1.SolarPotential.panel_width_meters], and
    [panel_capacity_watts]
    [google.maps.solar.v1.SolarPotential.panel_capacity_watts] fields in
    [SolarPotential] [google.maps.solar.v1.SolarPotential] for
    information on the parameters of the panel.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        center (google.type.latlng_pb2.LatLng):
            The centre of the panel.
        orientation (google.maps.solar_v1.types.SolarPanelOrientation):
            The orientation of the panel.
        yearly_energy_dc_kwh (float):
            How much sunlight energy this layout captures
            over the course of a year, in DC kWh.
        segment_index (int):
            Index in [roof_segment_stats]
            [google.maps.solar.v1.SolarPotential.roof_segment_stats] of
            the ``RoofSegmentSizeAndSunshineStats`` which corresponds to
            the roof segment that this panel is placed on.

            This field is a member of `oneof`_ ``_segment_index``.
    """

    center: latlng_pb2.LatLng = proto.Field(
        proto.MESSAGE,
        number=1,
        message=latlng_pb2.LatLng,
    )
    orientation: "SolarPanelOrientation" = proto.Field(
        proto.ENUM,
        number=2,
        enum="SolarPanelOrientation",
    )
    yearly_energy_dc_kwh: float = proto.Field(
        proto.FLOAT,
        number=3,
    )
    segment_index: int = proto.Field(
        proto.INT32,
        number=4,
        optional=True,
    )


class SolarPanelConfig(proto.Message):
    r"""SolarPanelConfig describes a particular placement of solar
    panels on the roof.

    Attributes:
        panels_count (int):
            Total number of panels. Note that this is redundant to (the
            sum of) the corresponding fields in [roof_segment_summaries]
            [google.maps.solar.v1.SolarPanelConfig.roof_segment_summaries].
        yearly_energy_dc_kwh (float):
            How much sunlight energy this layout captures
            over the course of a year, in DC kWh, assuming
            the panels described above.
        roof_segment_summaries (MutableSequence[google.maps.solar_v1.types.RoofSegmentSummary]):
            Information about the production of each roof segment that
            is carrying at least one panel in this layout.
            ``roof_segment_summaries[i]`` describes the i-th roof
            segment, including its size, expected production and
            orientation.
    """

    panels_count: int = proto.Field(
        proto.INT32,
        number=1,
    )
    yearly_energy_dc_kwh: float = proto.Field(
        proto.FLOAT,
        number=2,
    )
    roof_segment_summaries: MutableSequence["RoofSegmentSummary"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="RoofSegmentSummary",
    )


class RoofSegmentSummary(proto.Message):
    r"""Information about a roof segment on the building, with some
    number of panels placed on it.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        pitch_degrees (float):
            Angle of the roof segment relative to the
            theoretical ground plane. 0 = parallel to the
            ground, 90 = perpendicular to the ground.

            This field is a member of `oneof`_ ``_pitch_degrees``.
        azimuth_degrees (float):
            Compass direction the roof segment is pointing in. 0 =
            North, 90 = East, 180 = South. For a "flat" roof segment
            (``pitch_degrees`` very near 0), azimuth is not well
            defined, so for consistency, we define it arbitrarily to be
            0 (North).

            This field is a member of `oneof`_ ``_azimuth_degrees``.
        panels_count (int):
            The total number of panels on this segment.
        yearly_energy_dc_kwh (float):
            How much sunlight energy this part of the
            layout captures over the course of a year, in DC
            kWh, assuming the panels described above.
        segment_index (int):
            Index in [roof_segment_stats]
            [google.maps.solar.v1.SolarPotential.roof_segment_stats] of
            the corresponding ``RoofSegmentSizeAndSunshineStats``.

            This field is a member of `oneof`_ ``_segment_index``.
    """

    pitch_degrees: float = proto.Field(
        proto.FLOAT,
        number=2,
        optional=True,
    )
    azimuth_degrees: float = proto.Field(
        proto.FLOAT,
        number=3,
        optional=True,
    )
    panels_count: int = proto.Field(
        proto.INT32,
        number=7,
    )
    yearly_energy_dc_kwh: float = proto.Field(
        proto.FLOAT,
        number=8,
    )
    segment_index: int = proto.Field(
        proto.INT32,
        number=9,
        optional=True,
    )


class FinancialAnalysis(proto.Message):
    r"""Analysis of the cost and benefits of the optimum solar layout
    for a particular electric bill size.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        monthly_bill (google.type.money_pb2.Money):
            The monthly electric bill this analysis
            assumes.
        default_bill (bool):
            Whether this is the bill size selected to be the default
            bill for the area this building is in. Exactly one
            ``FinancialAnalysis`` in ``BuildingSolarPotential`` should
            have ``default_bill`` set.
        average_kwh_per_month (float):
            How much electricity the house uses in an
            average month, based on the bill size and the
            local electricity rates.
        panel_config_index (int):
            Index in [solar_panel_configs]
            [google.maps.solar.v1.SolarPotential.solar_panel_configs] of
            the optimum solar layout for this bill size. This can be -1
            indicating that there is no layout. In this case, the
            remaining submessages will be omitted.

            This field is a member of `oneof`_ ``_panel_config_index``.
        financial_details (google.maps.solar_v1.types.FinancialDetails):
            Financial information that applies regardless
            of the financing method used.
        leasing_savings (google.maps.solar_v1.types.LeasingSavings):
            Cost and benefit of leasing the solar panels.
        cash_purchase_savings (google.maps.solar_v1.types.CashPurchaseSavings):
            Cost and benefit of buying the solar panels
            with cash.
        financed_purchase_savings (google.maps.solar_v1.types.FinancedPurchaseSavings):
            Cost and benefit of buying the solar panels
            by financing the purchase.
    """

    monthly_bill: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=3,
        message=money_pb2.Money,
    )
    default_bill: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    average_kwh_per_month: float = proto.Field(
        proto.FLOAT,
        number=5,
    )
    panel_config_index: int = proto.Field(
        proto.INT32,
        number=6,
        optional=True,
    )
    financial_details: "FinancialDetails" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="FinancialDetails",
    )
    leasing_savings: "LeasingSavings" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="LeasingSavings",
    )
    cash_purchase_savings: "CashPurchaseSavings" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="CashPurchaseSavings",
    )
    financed_purchase_savings: "FinancedPurchaseSavings" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="FinancedPurchaseSavings",
    )


class FinancialDetails(proto.Message):
    r"""Details of a financial analysis. Some of these details are already
    stored at higher levels (e.g., out of pocket cost). Total money
    amounts are over a lifetime period defined by the
    [panel_lifetime_years]
    [google.maps.solar.v1.SolarPotential.panel_lifetime_years] field in
    [SolarPotential] [google.maps.solar.v1.SolarPotential]. Note: The
    out of pocket cost of purchasing the panels is given in the
    [out_of_pocket_cost]
    [google.maps.solar.v1.CashPurchaseSavings.out_of_pocket_cost] field
    in [CashPurchaseSavings] [google.maps.solar.v1.CashPurchaseSavings].


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        initial_ac_kwh_per_year (float):
            How many AC kWh we think the solar panels
            will generate in their first year.
        remaining_lifetime_utility_bill (google.type.money_pb2.Money):
            Utility bill for electricity not produced by
            solar, for the lifetime of the panels.
        federal_incentive (google.type.money_pb2.Money):
            Amount of money available from federal
            incentives; this applies if the user buys (with
            or without a loan) the panels.
        state_incentive (google.type.money_pb2.Money):
            Amount of money available from state
            incentives; this applies if the user buys (with
            or without a loan) the panels.
        utility_incentive (google.type.money_pb2.Money):
            Amount of money available from utility
            incentives; this applies if the user buys (with
            or without a loan) the panels.
        lifetime_srec_total (google.type.money_pb2.Money):
            Amount of money the user will receive from
            Solar Renewable Energy Credits over the panel
            lifetime; this applies if the user buys (with or
            without a loan) the panels.
        cost_of_electricity_without_solar (google.type.money_pb2.Money):
            Total cost of electricity the user would have
            paid over the lifetime period if they didn't
            install solar.
        net_metering_allowed (bool):
            Whether net metering is allowed.
        solar_percentage (float):
            Percentage (0-100) of the user's power
            supplied by solar. Valid for the first year but
            approximately correct for future years.

            This field is a member of `oneof`_ ``_solar_percentage``.
        percentage_exported_to_grid (float):
            The percentage (0-100) of solar electricity
            production we assumed was exported to the grid,
            based on the first quarter of production. This
            affects the calculations if net metering is not
            allowed.

            This field is a member of `oneof`_ ``_percentage_exported_to_grid``.
    """

    initial_ac_kwh_per_year: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    remaining_lifetime_utility_bill: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=2,
        message=money_pb2.Money,
    )
    federal_incentive: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=3,
        message=money_pb2.Money,
    )
    state_incentive: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=4,
        message=money_pb2.Money,
    )
    utility_incentive: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=5,
        message=money_pb2.Money,
    )
    lifetime_srec_total: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=6,
        message=money_pb2.Money,
    )
    cost_of_electricity_without_solar: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=7,
        message=money_pb2.Money,
    )
    net_metering_allowed: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    solar_percentage: float = proto.Field(
        proto.FLOAT,
        number=9,
        optional=True,
    )
    percentage_exported_to_grid: float = proto.Field(
        proto.FLOAT,
        number=10,
        optional=True,
    )


class SavingsOverTime(proto.Message):
    r"""Financial information that's shared between different
    financing methods.

    Attributes:
        savings_year1 (google.type.money_pb2.Money):
            Savings in the first year after panel
            installation.
        savings_year20 (google.type.money_pb2.Money):
            Savings in the first twenty years after panel
            installation.
        present_value_of_savings_year20 (google.type.money_pb2.Money):
            Using the assumed discount rate, what is the
            present value of the cumulative 20-year savings?
        savings_lifetime (google.type.money_pb2.Money):
            Savings in the entire panel lifetime.
        present_value_of_savings_lifetime (google.type.money_pb2.Money):
            Using the assumed discount rate, what is the
            present value of the cumulative lifetime
            savings?
        financially_viable (bool):
            Indicates whether this scenario is
            financially viable.  Will be false for scenarios
            with poor financial viability (e.g.,
            money-losing).
    """

    savings_year1: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=1,
        message=money_pb2.Money,
    )
    savings_year20: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=2,
        message=money_pb2.Money,
    )
    present_value_of_savings_year20: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=3,
        message=money_pb2.Money,
    )
    savings_lifetime: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=5,
        message=money_pb2.Money,
    )
    present_value_of_savings_lifetime: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=6,
        message=money_pb2.Money,
    )
    financially_viable: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class LeasingSavings(proto.Message):
    r"""Cost and benefit of leasing a particular configuration of
    solar panels with a particular electricity usage.

    Attributes:
        leases_allowed (bool):
            Whether leases are allowed in this
            juristiction (leases are not allowed in some
            states). If this field is false, then the values
            in this message should probably be ignored.
        leases_supported (bool):
            Whether leases are supported in this juristiction by the
            financial calculation engine. If this field is false, then
            the values in this message should probably be ignored. This
            is independent of ``leases_allowed``: in some areas leases
            are allowed, but under conditions that aren't handled by the
            financial models.
        annual_leasing_cost (google.type.money_pb2.Money):
            Estimated annual leasing cost.
        savings (google.maps.solar_v1.types.SavingsOverTime):
            How much is saved (or not) over the lifetime
            period.
    """

    leases_allowed: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    leases_supported: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    annual_leasing_cost: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=3,
        message=money_pb2.Money,
    )
    savings: "SavingsOverTime" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="SavingsOverTime",
    )


class CashPurchaseSavings(proto.Message):
    r"""Cost and benefit of an outright purchase of a particular
    configuration of solar panels with a particular electricity
    usage.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        out_of_pocket_cost (google.type.money_pb2.Money):
            Initial cost before tax incentives: the amount that must be
            paid out-of-pocket. Contrast with ``upfront_cost``, which is
            after tax incentives.
        upfront_cost (google.type.money_pb2.Money):
            Initial cost after tax incentives: it's the amount that must
            be paid during first year. Contrast with
            ``out_of_pocket_cost``, which is before tax incentives.
        rebate_value (google.type.money_pb2.Money):
            The value of all tax rebates.
        payback_years (float):
            Number of years until payback occurs. A
            negative value means payback never occurs within
            the lifetime period.

            This field is a member of `oneof`_ ``_payback_years``.
        savings (google.maps.solar_v1.types.SavingsOverTime):
            How much is saved (or not) over the lifetime
            period.
    """

    out_of_pocket_cost: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=1,
        message=money_pb2.Money,
    )
    upfront_cost: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=2,
        message=money_pb2.Money,
    )
    rebate_value: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=3,
        message=money_pb2.Money,
    )
    payback_years: float = proto.Field(
        proto.FLOAT,
        number=4,
        optional=True,
    )
    savings: "SavingsOverTime" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="SavingsOverTime",
    )


class FinancedPurchaseSavings(proto.Message):
    r"""Cost and benefit of using a loan to buy a particular
    configuration of solar panels with a particular electricity
    usage.

    Attributes:
        annual_loan_payment (google.type.money_pb2.Money):
            Annual loan payments.
        rebate_value (google.type.money_pb2.Money):
            The value of all tax rebates (including
            Federal Investment Tax Credit (ITC)).
        loan_interest_rate (float):
            The interest rate on loans assumed in this
            set of calculations.
        savings (google.maps.solar_v1.types.SavingsOverTime):
            How much is saved (or not) over the lifetime
            period.
    """

    annual_loan_payment: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=1,
        message=money_pb2.Money,
    )
    rebate_value: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=2,
        message=money_pb2.Money,
    )
    loan_interest_rate: float = proto.Field(
        proto.FLOAT,
        number=3,
    )
    savings: "SavingsOverTime" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="SavingsOverTime",
    )


class GetDataLayersRequest(proto.Message):
    r"""Request message for ``Solar.GetDataLayers``.

    Attributes:
        location (google.type.latlng_pb2.LatLng):
            Required. The longitude and latitude for the
            center of the region to get data for.
        radius_meters (float):
            Required. The radius, in meters, defining the region
            surrounding that centre point for which data should be
            returned. The limitations on this value are:

            - Any value up to 100m can always be specified.
            - Values over 100m can be specified, as long as
              ``radius_meters`` <= ``pixel_size_meters * 1000``.
            - However, for values over 175m, the ``DataLayerView`` in
              the request must not include monthly flux or hourly shade.
        view (google.maps.solar_v1.types.DataLayerView):
            Optional. The desired subset of the data to
            return.
        required_quality (google.maps.solar_v1.types.ImageryQuality):
            Optional. The minimum quality level allowed
            in the results. No result with lower quality
            than this will be returned. Not specifying this
            is equivalent to restricting to HIGH quality
            only.
        pixel_size_meters (float):
            Optional. The minimum scale, in meters per pixel, of the
            data to return. Values of 0.1 (the default, if this field is
            not set explicitly), 0.25, 0.5, and 1.0 are supported.
            Imagery components whose normal resolution is less than
            ``pixel_size_meters`` will be returned at the resolution
            specified by ``pixel_size_meters``; imagery components whose
            normal resolution is equal to or greater than
            ``pixel_size_meters`` will be returned at that normal
            resolution.
        exact_quality_required (bool):
            Optional. Whether to require exact quality of the imagery.
            If set to false, the ``required_quality`` field is
            interpreted as the minimum required quality, such that HIGH
            quality imagery may be returned when ``required_quality`` is
            set to MEDIUM. If set to true, ``required_quality`` is
            interpreted as the exact required quality and only
            ``MEDIUM`` quality imagery is returned if
            ``required_quality`` is set to ``MEDIUM``.
        experiments (MutableSequence[google.maps.solar_v1.types.Experiment]):
            Optional. Specifies the pre-GA experiments to enable.
            Requests using this field are classified as a pre-GA
            offering under the `Google Maps Platform Service Specific
            Terms <https://cloud.google.com/maps-platform/terms/maps-service-terms>`__.
            See `launch stage
            descriptions <https://cloud.google.com/maps-platform/terms/launch-stages>`__
            for more details.
    """

    location: latlng_pb2.LatLng = proto.Field(
        proto.MESSAGE,
        number=1,
        message=latlng_pb2.LatLng,
    )
    radius_meters: float = proto.Field(
        proto.FLOAT,
        number=2,
    )
    view: "DataLayerView" = proto.Field(
        proto.ENUM,
        number=3,
        enum="DataLayerView",
    )
    required_quality: "ImageryQuality" = proto.Field(
        proto.ENUM,
        number=5,
        enum="ImageryQuality",
    )
    pixel_size_meters: float = proto.Field(
        proto.FLOAT,
        number=6,
    )
    exact_quality_required: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    experiments: MutableSequence["Experiment"] = proto.RepeatedField(
        proto.ENUM,
        number=8,
        enum="Experiment",
    )


class DataLayers(proto.Message):
    r"""Information about the solar potential of a region. The actual data
    are contained in a number of GeoTIFF files covering the requested
    region, for which this message contains URLs: Each string in the
    ``DataLayers`` message contains a URL from which the corresponding
    GeoTIFF can be fetched. These URLs are valid for a few hours after
    they've been generated. Most of the GeoTIFF files are at a
    resolution of 0.1m/pixel, but the monthly flux file is at
    0.5m/pixel, and the hourly shade files are at 1m/pixel. If a
    ``pixel_size_meters`` value was specified in the
    ``GetDataLayersRequest``, then the minimum resolution in the GeoTIFF
    files will be that value.

    Attributes:
        imagery_date (google.type.date_pb2.Date):
            When the source imagery (from which all the
            other data are derived) in this region was
            taken. It is necessarily somewhat approximate,
            as the images may have been taken over more than
            one day.
        imagery_processed_date (google.type.date_pb2.Date):
            When processing was completed on this
            imagery.
        dsm_url (str):
            The URL for an image of the DSM (Digital
            Surface Model) of the region. Values are in
            meters above EGM96 geoid (i.e., sea level).
            Invalid locations (where we don't have data) are
            stored as -9999.
        rgb_url (str):
            The URL for an image of RGB data (aerial or
            satellite photo) of the region.
        mask_url (str):
            The URL for the building mask image: one bit
            per pixel saying whether that pixel is
            considered to be part of a rooftop or not.
        annual_flux_url (str):
            The URL for the annual flux map (annual sunlight on roofs)
            of the region. Values are kWh/kW/year. This is *unmasked
            flux*: flux is computed for every location, not just
            building rooftops. Invalid locations are stored as -9999:
            locations outside our coverage area will be invalid, and a
            few locations inside the coverage area, where we were unable
            to calculate flux, will also be invalid.
        monthly_flux_url (str):
            The URL for the monthly flux map (sunlight on
            roofs, broken down by month) of the region.
            Values are kWh/kW/year. The GeoTIFF pointed to
            by this URL will contain twelve bands,
            corresponding to January...December, in order.
        hourly_shade_urls (MutableSequence[str]):
            Twelve URLs for hourly shade, corresponding to
            January...December, in order. Each GeoTIFF will contain 24
            bands, corresponding to the 24 hours of the day. Each pixel
            is a 32 bit integer, corresponding to the (up to) 31 days of
            that month; a 1 bit means that the corresponding location is
            able to see the sun at that day, of that hour, of that
            month. Invalid locations are stored as -9999 (since this is
            negative, it has bit 31 set, and no valid value could have
            bit 31 set as that would correspond to the 32nd day of the
            month).

            An example may be useful. If you want to know whether a
            point (at pixel location (x, y)) saw sun at 4pm on the 22nd
            of June you would:

            1. fetch the sixth URL in this list (corresponding to June).
            2. look up the 17th channel (corresponding to 4pm).
            3. read the 32-bit value at (x, y).
            4. read bit 21 of the value (corresponding to the 22nd of
               the month).
            5. if that bit is a 1, then that spot saw the sun at 4pm 22
               June.

            More formally: Given ``month`` (1-12), ``day`` (1...month
            max; February has 28 days) and ``hour`` (0-23), the
            shade/sun for that month/day/hour at a position ``(x, y)``
            is the bit

            ::

               (hourly_shade[month - 1])(x, y)[hour] & (1 << (day - 1))

            where ``(x, y)`` is spatial indexing, ``[month - 1]`` refers
            to fetching the ``month - 1``\ st URL (indexing from zero),
            ``[hour]`` is indexing into the channels, and a final
            non-zero result means "sunny". There are no leap days, and
            DST doesn't exist (all days are 24 hours long; noon is
            always "standard time" noon).
        imagery_quality (google.maps.solar_v1.types.ImageryQuality):
            The quality of the result's imagery.
    """

    imagery_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=1,
        message=date_pb2.Date,
    )
    imagery_processed_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=2,
        message=date_pb2.Date,
    )
    dsm_url: str = proto.Field(
        proto.STRING,
        number=3,
    )
    rgb_url: str = proto.Field(
        proto.STRING,
        number=4,
    )
    mask_url: str = proto.Field(
        proto.STRING,
        number=5,
    )
    annual_flux_url: str = proto.Field(
        proto.STRING,
        number=6,
    )
    monthly_flux_url: str = proto.Field(
        proto.STRING,
        number=7,
    )
    hourly_shade_urls: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    imagery_quality: "ImageryQuality" = proto.Field(
        proto.ENUM,
        number=9,
        enum="ImageryQuality",
    )


class GetGeoTiffRequest(proto.Message):
    r"""Request message for ``Solar.GetGeoTiff``.

    Attributes:
        id (str):
            Required. The ID of the asset being
            requested.
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
