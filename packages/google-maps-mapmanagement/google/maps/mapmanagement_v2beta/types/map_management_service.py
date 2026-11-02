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

__protobuf__ = proto.module(
    package="google.maps.mapmanagement.v2beta",
    manifest={
        "StyleConfigView",
        "MapRenderingType",
        "CreateMapConfigRequest",
        "GetMapConfigRequest",
        "ListMapConfigsRequest",
        "ListMapConfigsResponse",
        "UpdateMapConfigRequest",
        "DeleteMapConfigRequest",
        "MapFeatures",
        "MapConfig",
        "StyleConfig",
        "CreateStyleConfigRequest",
        "GetStyleConfigRequest",
        "ListStyleConfigsRequest",
        "ListStyleConfigsResponse",
        "UpdateStyleConfigRequest",
        "DeleteStyleConfigRequest",
        "MapContextConfig",
        "CreateMapContextConfigRequest",
        "GetMapContextConfigRequest",
        "ListMapContextConfigsRequest",
        "ListMapContextConfigsResponse",
        "UpdateMapContextConfigRequest",
        "DeleteMapContextConfigRequest",
    },
)


class StyleConfigView(proto.Enum):
    r"""What subset of the StyleConfig to return.

    Values:
        STYLE_CONFIG_VIEW_UNSPECIFIED (0):
            Unspecified view.
        FULL (1):
            Include the json_style_sheet in the response.
        METADATA_ONLY (2):
            Exclude the json_style_sheet from the response.
    """

    STYLE_CONFIG_VIEW_UNSPECIFIED = 0
    FULL = 1
    METADATA_ONLY = 2


class MapRenderingType(proto.Enum):
    r"""The type of map to be rendered.

    Values:
        RASTER (0):
            A map rendered using the raster based
            implementation. This is the default rendering
            type if not specified.
        VECTOR (1):
            A map rendered using webGL.
    """

    RASTER = 0
    VECTOR = 1


class CreateMapConfigRequest(proto.Message):
    r"""Request to create a MapConfig.

    Attributes:
        parent (str):
            Required. Parent project that will own the MapConfig.
            Format: ``projects/{$my-project-id}``
        map_config (google.maps.mapmanagement_v2beta.types.MapConfig):
            Required. The MapConfig to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    map_config: "MapConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="MapConfig",
    )


class GetMapConfigRequest(proto.Message):
    r"""Request to get a MapConfig.

    Attributes:
        name (str):
            Required. Resource name of the MapConfig. Format:
            ``projects/{project}/mapConfigs/{map_config}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListMapConfigsRequest(proto.Message):
    r"""Request to list MapConfigs.

    Attributes:
        parent (str):
            Required. Parent project that owns the MapConfigs. Format:
            ``projects/{project}``
        page_size (int):
            Optional. The maximum number of MapConfigs to
            return. The service may return fewer than this
            value. If unspecified, at most 50 MapConfigs
            will be returned. The maximum value is 1000;
            values above 1000 will be coerced to
            1000. CURRENTLY UNSUPPORTED.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListMapConfigs`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListMapConfigs`` must match the call that provided the
            page token. CURRENTLY UNSUPPORTED.
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


class ListMapConfigsResponse(proto.Message):
    r"""Response to list MapConfigs.

    Attributes:
        map_configs (MutableSequence[google.maps.mapmanagement_v2beta.types.MapConfig]):
            The list of MapConfigs.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages. CURRENTLY UNSUPPORTED.
    """

    @property
    def raw_page(self):
        return self

    map_configs: MutableSequence["MapConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="MapConfig",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateMapConfigRequest(proto.Message):
    r"""Request to update a MapConfig.

    Attributes:
        map_config (google.maps.mapmanagement_v2beta.types.MapConfig):
            Required. The MapConfig to update.

            The MapConfig's ``name`` field is used to identify the
            MapConfig to update. Format:
            ``projects/{project}/mapConfigs/{map_config}``
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The specific field to update for the MapConfig. If
            not specified, the MapConfig will be updated in its
            entirety. Valid fields are:

            - ``display_name``
            - ``description``
            - ``map_features``
    """

    map_config: "MapConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="MapConfig",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteMapConfigRequest(proto.Message):
    r"""Request to delete a MapConfig. If the MapConfig has any child
    MapContextConfigs, those will be deleted as well.

    Attributes:
        name (str):
            Required. Resource name of the MapConfig to delete. Format:
            ``projects/{project}/mapConfigs/{map_config}``
        force (bool):
            Optional. If set to true, any
            MapContextConfigs from this MapConfig will also
            be deleted. (Otherwise, the request will only
            work if the MapConfig has no MapContextConfigs.)
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class MapFeatures(proto.Message):
    r"""Represents a collection of map features that apply to a
    MapConfig. Features set on a MapConfig are inherited by all of
    its child MapContextConfigs.
    Next ID = 3;


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        simple_features (MutableSequence[google.maps.mapmanagement_v2beta.types.MapFeatures.SimpleFeature]):
            Optional. The visual feature to use for this
            map.
        poi_boost_level (int):
            Optional. POI Boost level, where 0 denotes no boostings and
            negative values denotes de-boosting. Boosted POIs are shown
            at lower zoom than default and vice versa de-boosted.
            Currently supports 2 levels of boosting, so the level is
            clamped to [-2, 2]. If not specified, the POI density
            defined in the style sheet will be used if it exists.
            Otherwise, no POI density will be applied.

            This field is a member of `oneof`_ ``_poi_boost_level``.
    """

    class SimpleFeature(proto.Enum):
        r"""This represents the set of map features that affect the
        intrinsic structure of the map.

        Values:
            SIMPLE_FEATURE_UNSPECIFIED (0):
                Unspecified visual feature.
            FLATTEN_BUILDINGS (1):
                Flattens all buildings in the map.
            ICONIC_ICONS (2):
                Influences how icons are rendered.
        """

        SIMPLE_FEATURE_UNSPECIFIED = 0
        FLATTEN_BUILDINGS = 1
        ICONIC_ICONS = 2

    simple_features: MutableSequence[SimpleFeature] = proto.RepeatedField(
        proto.ENUM,
        number=1,
        enum=SimpleFeature,
    )
    poi_boost_level: int = proto.Field(
        proto.INT32,
        number=2,
        optional=True,
    )


class MapConfig(proto.Message):
    r"""Represents a single map in a Maps API client application. The
    MapConfig is the parent resource of MapContextConfigs and
    enables custom styling in SDKs (Mobile/Web). A MapConfig can
    have multiple MapContextConfigs, each applying styling to
    specific map variants.
    Next ID = 9;


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. Identifier. Resource name of
            this MapConfig. For example:
            "projects/my-project-123/mapConfigs/234". Output
            only.
        display_name (str):
            Optional. The display name of this MapConfig,
            as specified by the user.
        description (str):
            Optional. The description of this MapConfig,
            as specified by the user.
        map_id (str):
            Output only. The Map ID of this MapConfig,
            used to identify the map in client applications.
            This read-only field is generated when the
            MapConfig is created. Output only.
        map_features (google.maps.mapmanagement_v2beta.types.MapFeatures):
            Optional. The Map Features that apply to this
            Map Config.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Denotes the creation time of the
            Map Config. Output only.

            This field is a member of `oneof`_ ``_create_time``.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Denotes the last update time of
            the Map Config. Output only.

            This field is a member of `oneof`_ ``_update_time``.
        map_type (google.maps.mapmanagement_v2beta.types.MapRenderingType):
            Optional. Represents the Map Type of the
            MapConfig. If this is unset, the default
            behavior is to use the raster map type.
    """

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
    map_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    map_features: "MapFeatures" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="MapFeatures",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    map_type: "MapRenderingType" = proto.Field(
        proto.ENUM,
        number=8,
        enum="MapRenderingType",
    )


class StyleConfig(proto.Message):
    r"""Represents a single style in a Maps API client application.
    The StyleConfig contains the style sheet that defines the visual
    appearance of the map. Next ID = 9;


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. Identifier. Resource name of
            this StyleConfig. For example:
            "projects/my-project-123/styleConfigs/234".
        display_name (str):
            Optional. The display name of this
            StyleConfig, as specified by the user.
        description (str):
            Optional. The description of this
            StyleConfig, as specified by the user.
        style_id (str):
            Output only. The unique identifier of this
            style. This is a read-only field that is
            generated when the StyleConfig is created.
            Output only.
        json_style_sheet (str):
            Optional. JSON representation of the style
            sheet for this StyleConfig. If not specified or
            if provided as an empty string, the base
            unstyled Google map style will be used. See
            https://developers.google.com/maps/documentation/javascript/cloud-customization/json-reference
            for more details on the acceptable JSON format.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Denotes the creation time of the
            StyleConfig.

            This field is a member of `oneof`_ ``_create_time``.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Denotes the last update time of
            the StyleConfig.

            This field is a member of `oneof`_ ``_update_time``.
    """

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
    style_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    json_style_sheet: str = proto.Field(
        proto.STRING,
        number=6,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )


class CreateStyleConfigRequest(proto.Message):
    r"""Request to create a StyleConfig.

    Attributes:
        parent (str):
            Required. Parent project that will own the StyleConfig.
            Format: ``projects/{project}``
        style_config (google.maps.mapmanagement_v2beta.types.StyleConfig):
            Required. The StyleConfig to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    style_config: "StyleConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="StyleConfig",
    )


class GetStyleConfigRequest(proto.Message):
    r"""Request to get a StyleConfig.

    Attributes:
        name (str):
            Required. Resource name of the StyleConfig. Format:
            ``projects/{project}/styleConfigs/{style_config}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListStyleConfigsRequest(proto.Message):
    r"""Request to list StyleConfigs.

    Attributes:
        parent (str):
            Required. Parent project that owns the StyleConfigs. Format:
            ``projects/{project}``
        page_size (int):
            Optional. The maximum number of StyleConfigs
            to return. The service may return fewer than
            this value. If unspecified, at most 50
            StyleConfigs will be returned. The maximum value
            is 1000; values above 1000 will be coerced to
            1000. CURRENTLY UNSUPPORTED.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListStyleConfigs`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListStyleConfigs`` must match the call that provided the
            page token. CURRENTLY UNSUPPORTED.
        filter (str):
            Optional. Filter expression for the ListStyleConfigs call.
            Currently only supports filtering by display_name. For
            example: ``display_name="My StyleConfig"`` will return all
            StyleConfigs with the display name "My StyleConfig".
        view (google.maps.mapmanagement_v2beta.types.StyleConfigView):
            Optional. The subset of the StyleConfig to
            return. If this is unset, the default behavior
            is to return the FULL view.
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
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    view: "StyleConfigView" = proto.Field(
        proto.ENUM,
        number=5,
        enum="StyleConfigView",
    )


class ListStyleConfigsResponse(proto.Message):
    r"""Response to list StyleConfigs.

    Attributes:
        style_configs (MutableSequence[google.maps.mapmanagement_v2beta.types.StyleConfig]):
            The StyleConfigs.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages. CURRENTLY UNSUPPORTED.
    """

    @property
    def raw_page(self):
        return self

    style_configs: MutableSequence["StyleConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="StyleConfig",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateStyleConfigRequest(proto.Message):
    r"""Request to update a StyleConfig.

    Attributes:
        style_config (google.maps.mapmanagement_v2beta.types.StyleConfig):
            Required. The StyleConfig to update.

            The StyleConfig's ``name`` field is used to identify the
            StyleConfig to update. Format:
            ``projects/{project}/styleConfigs/{style_config}``
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update. If not specified,
            the StyleConfig will be updated in its entirety. Valid
            fields are:

            - ``display_name``
            - ``description``
            - ``json_style_sheet``
    """

    style_config: "StyleConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="StyleConfig",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteStyleConfigRequest(proto.Message):
    r"""Request to delete a StyleConfig.

    Attributes:
        name (str):
            Required. Resource name of the StyleConfig to delete.
            Format: ``projects/{project}/styleConfigs/{style_config}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class MapContextConfig(proto.Message):
    r"""Encapsulates the styling configuration for a map. The
    MapContextConfig associates styling components, such as a
    StyleConfig and Datasets, with specific map variants of a
    MapConfig. When the MapConfig is loaded in an SDK, the styling
    and dataset information from the MapContextConfig are applied to
    the specified map variants.
    Next ID = 10;

    Attributes:
        name (str):
            Output only. Identifier. Resource name of this
            MapContextConfig. For example:
            projects/{project_id}/mapConfigs/{map_id}/mapContextConfigs/{map_context_config_id}
        map_config (str):
            Required. The MapConfig resource name that this
            MapContextConfig is associated with. Format:
            projects/{project}/mapConfigs/{map_config}. This field is
            required and cannot be omitted.
        style_config (str):
            Required. The StyleConfig resource name that is styling this
            MapContextConfig. This field is required and cannot be
            omitted. Format:
            projects/{project}/styleConfigs/{style_config}
        dataset (MutableSequence[str]):
            Optional. The Dataset resource name that is
            associated with this MapContextConfig. This
            field is optional and can be omitted. If
            omitted, no datasets will be associated with the
            MapContextConfig. If a dataset is specified, it
            will be applied to the MapContextConfig. Format:

            projects/{project}/datasets/{dataset}
        alias (str):
            Optional. The user defined human readable
            name for this MapContextConfig.
        map_variants (MutableSequence[google.maps.mapmanagement_v2beta.types.MapContextConfig.MapVariant]):
            Required. The map variants that this
            MapContextConfig can be applied to. If empty,
            the MapContextConfig will be default applied to
            only the ROADMAP map variant.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Denotes the creation time of the
            MapContextConfig. Output only.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Denotes the last update time of
            the MapContextConfig. Output only.
    """

    class MapVariant(proto.Enum):
        r"""Possible Map Variants that the MapContextConfig can be applied to.
        Map Variants are grouped into Light and Dark variants. A Light
        variant cannot be paired with a Dark variant for the same
        MapContextConfig. The Light Variants are: ROADMAP, SATELLITE,
        TERRAIN, NAVIGATION, TRANSIT, ABSTRACT3D, PHOTOREALISTIC3D. The Dark
        Variants are: ROADMAP_DARK, NAVIGATION_LOW_LIGHT, TERRAIN_DARK,
        TRANSIT_DARK.

        For example, the following is a valid pairing: {MapContextConfig 1:
        [ROADMAP, NAVIGATION]} {MapContextConfig 2: [ROADMAP_DARK,
        NAVIGATION_LOW_LIGHT]}

        The following is an invalid pairing: {MapContextConfig 1: [ROADMAP,
        ROADMAP_DARK]}

        Values:
            ROADMAP (0):
                The default roadmap map type. If no map
                variants are specified in a MapContextConfig,
                this variant is used by default.
            ROADMAP_DARK (1):
                A dark version of the roadmap map type.
            SATELLITE (2):
                Satellite imagery.
            TERRAIN (3):
                Terrain map type.
            TERRAIN_DARK (4):
                A dark version of the terrain map type.
            NAVIGATION (5):
                Navigation map type.
            NAVIGATION_LOW_LIGHT (6):
                A low light version of the navigation map
                type.
            TRANSIT (7):
                Transit map type.
            TRANSIT_DARK (8):
                A dark version of the transit map type.
            ABSTRACT3D (9):
                Abstract 3D map type.
            PHOTOREALISTIC3D (10):
                Photorealistic 3D map type.
        """

        ROADMAP = 0
        ROADMAP_DARK = 1
        SATELLITE = 2
        TERRAIN = 3
        TERRAIN_DARK = 4
        NAVIGATION = 5
        NAVIGATION_LOW_LIGHT = 6
        TRANSIT = 7
        TRANSIT_DARK = 8
        ABSTRACT3D = 9
        PHOTOREALISTIC3D = 10

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    map_config: str = proto.Field(
        proto.STRING,
        number=2,
    )
    style_config: str = proto.Field(
        proto.STRING,
        number=3,
    )
    dataset: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    alias: str = proto.Field(
        proto.STRING,
        number=5,
    )
    map_variants: MutableSequence[MapVariant] = proto.RepeatedField(
        proto.ENUM,
        number=6,
        enum=MapVariant,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )


class CreateMapContextConfigRequest(proto.Message):
    r"""Request to create a MapContextConfig.

    Attributes:
        parent (str):
            Required. Parent MapConfig that will own the
            MapContextConfig. Format:
            ``projects/{project}/mapConfigs/{map_config}``
        map_context_config (google.maps.mapmanagement_v2beta.types.MapContextConfig):
            Required. The MapContextConfig to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    map_context_config: "MapContextConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="MapContextConfig",
    )


class GetMapContextConfigRequest(proto.Message):
    r"""Request to get a MapContextConfig.

    Attributes:
        name (str):
            Required. Resource name of the MapContextConfig. Format:
            ``projects/{project}/mapConfigs/{map_config}/mapContextConfigs/{map_context_config}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListMapContextConfigsRequest(proto.Message):
    r"""Request to list MapContextConfigs.

    Attributes:
        parent (str):
            Required. Parent MapConfig that owns the MapContextConfigs.
            Format: ``projects/{project}/mapConfigs/{map_config}``
        page_size (int):
            Optional. The maximum number of
            MapContextConfigs to return. The service may
            return fewer than this value. If unspecified, at
            most 50 MapContextConfigs will be returned. The
            maximum value is 1000; values above 1000 will be
            coerced to 1000. CURRENTLY UNSUPPORTED.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListMapContextConfigs`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListMapContextConfigs`` must match the call that provided
            the page token. CURRENTLY UNSUPPORTED.
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


class ListMapContextConfigsResponse(proto.Message):
    r"""Response to list MapContextConfigs.

    Attributes:
        map_context_configs (MutableSequence[google.maps.mapmanagement_v2beta.types.MapContextConfig]):
            The MapContextConfigs.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages. CURRENTLY UNSUPPORTED.
    """

    @property
    def raw_page(self):
        return self

    map_context_configs: MutableSequence["MapContextConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="MapContextConfig",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateMapContextConfigRequest(proto.Message):
    r"""Request to update a MapContextConfig.

    Attributes:
        map_context_config (google.maps.mapmanagement_v2beta.types.MapContextConfig):
            Required. The MapContextConfig to update.

            The MapContextConfig's ``name`` field is used to identify
            the MapContextConfig to update. Format:
            ``projects/{project}/mapConfigs/{map_config}/mapContextConfigs/{map_context_config}``
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update. If not specified,
            the MapContextConfig will be updated in its entirety. Valid
            fields are:

            - ``display_name``
            - ``alias``
            - ``map_variants``
            - ``style_config``
            - ``dataset``
    """

    map_context_config: "MapContextConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="MapContextConfig",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteMapContextConfigRequest(proto.Message):
    r"""Request to delete a MapContextConfig.

    Attributes:
        name (str):
            Required. Resource name of the MapContextConfig to delete.
            Format:
            ``projects/{project}/mapConfigs/{map_config}/mapContextConfigs/{map_context_config}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
