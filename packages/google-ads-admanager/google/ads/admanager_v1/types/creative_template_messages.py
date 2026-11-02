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

from google.ads.admanager_v1.types import (
    creative_template_enums,
    creative_template_variable_url_type_enum,
)

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "CreativeTemplate",
        "CreativeTemplateVariable",
    },
)


class CreativeTemplate(proto.Message):
    r"""A template that can be used to create a [TemplateCreative][].

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the creative template.
            Format:
            ``networks/{network_code}/creativeTemplates/{creative_template_id}``
        display_name (str):
            Required. The display name of the creative
            template. This has a maximum length of 255
            characters.

            This field is a member of `oneof`_ ``_display_name``.
        description (str):
            Optional. The description of the creative
            template.

            This field is a member of `oneof`_ ``_description``.
        snippet (str):
            Required. The code snippet of the creative
            template, with placeholders for the associated
            variables.

            This field is a member of `oneof`_ ``_snippet``.
        status (google.ads.admanager_v1.types.CreativeTemplateStatusEnum.CreativeTemplateStatus):
            Output only. The status of the creative
            template. This attribute is assigned by Google.

            This field is a member of `oneof`_ ``_status``.
        type_ (google.ads.admanager_v1.types.CreativeTemplateTypeEnum.CreativeTemplateType):
            Optional. The type of the creative template. Users can only
            create or update ``CreativeTemplateType.CUSTOM`` templates.

            This field is a member of `oneof`_ ``_type``.
        interstitial (bool):
            Optional. ``True`` if this creative template produces
            out-of-page creatives. Creative templates with this setting
            enabled must include the viewed impression macro.

            This field is a member of `oneof`_ ``_interstitial``.
        native_eligible (bool):
            Optional. ``True`` if this creative template produces
            native-eligible creatives.

            This field is a member of `oneof`_ ``_native_eligible``.
        native_video_eligible (bool):
            Optional. ``True`` if this creative template produces native
            video-eligible creatives.

            This field is a member of `oneof`_ ``_native_video_eligible``.
        safe_frame_compatible (bool):
            Optional. Whether the Creative produced is compatible for
            SafeFrame rendering. This attribute defaults to ``True``.

            This field is a member of `oneof`_ ``_safe_frame_compatible``.
        variables (MutableSequence[google.ads.admanager_v1.types.CreativeTemplateVariable]):
            Required. The list of creative template
            variables.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    snippet: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    status: creative_template_enums.CreativeTemplateStatusEnum.CreativeTemplateStatus = proto.Field(
        proto.ENUM,
        number=6,
        optional=True,
        enum=creative_template_enums.CreativeTemplateStatusEnum.CreativeTemplateStatus,
    )
    type_: creative_template_enums.CreativeTemplateTypeEnum.CreativeTemplateType = (
        proto.Field(
            proto.ENUM,
            number=7,
            optional=True,
            enum=creative_template_enums.CreativeTemplateTypeEnum.CreativeTemplateType,
        )
    )
    interstitial: bool = proto.Field(
        proto.BOOL,
        number=8,
        optional=True,
    )
    native_eligible: bool = proto.Field(
        proto.BOOL,
        number=9,
        optional=True,
    )
    native_video_eligible: bool = proto.Field(
        proto.BOOL,
        number=10,
        optional=True,
    )
    safe_frame_compatible: bool = proto.Field(
        proto.BOOL,
        number=12,
        optional=True,
    )
    variables: MutableSequence["CreativeTemplateVariable"] = proto.RepeatedField(
        proto.MESSAGE,
        number=14,
        message="CreativeTemplateVariable",
    )


class CreativeTemplateVariable(proto.Message):
    r"""Represents a variable defined in a creative template.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        asset_variable (google.ads.admanager_v1.types.CreativeTemplateVariable.AssetCreativeTemplateVariable):
            Optional. Represents a file asset variable
            defined in a creative template.

            This field is a member of `oneof`_ ``SubType``.
        list_string_variable (google.ads.admanager_v1.types.CreativeTemplateVariable.ListStringCreativeTemplateVariable):
            Optional. Represents a list variable defined
            in a creative template.

            This field is a member of `oneof`_ ``SubType``.
        long_variable (google.ads.admanager_v1.types.CreativeTemplateVariable.LongCreativeTemplateVariable):
            Optional. Represents a long variable defined
            in a creative template.

            This field is a member of `oneof`_ ``SubType``.
        string_variable (google.ads.admanager_v1.types.CreativeTemplateVariable.StringCreativeTemplateVariable):
            Optional. Represents a string variable
            defined in a creative template.

            This field is a member of `oneof`_ ``SubType``.
        url_variable (google.ads.admanager_v1.types.CreativeTemplateVariable.UrlCreativeTemplateVariable):
            Optional. Represents a url variable defined
            in a creative template.

            This field is a member of `oneof`_ ``SubType``.
        label (str):
            Required. Label that is displayed to users
            when creating from the creative template. This
            has a maximum length of 127 characters.

            This field is a member of `oneof`_ ``_label``.
        unique_display_name (str):
            Output only. Unique name used to identify the
            variable. This attribute is assigned by Google
            when a creative template variable is created.

            This field is a member of `oneof`_ ``_unique_display_name``.
        description (str):
            Required. A descriptive help text that is
            displayed to users along with the label. This
            attribute has a maximum length of 255
            characters.

            This field is a member of `oneof`_ ``_description``.
        required (bool):
            Optional. ``True`` if this variable is required to be filled
            in by users when creating a creative from the creative
            template.

            This field is a member of `oneof`_ ``_required``.
    """

    class AssetCreativeTemplateVariable(proto.Message):
        r"""Represents a file asset variable defined in a creative template.

        Use [AssetCreativeTemplateVariableValue][] to specify the value for
        this variable when creating a [TemplateCreative][] from a
        [CreativeTemplate][google.ads.admanager.v1.CreativeTemplate].

        Attributes:
            mime_types (MutableSequence[google.ads.admanager_v1.types.CreativeTemplateVariable.AssetCreativeTemplateVariable.MimeType]):
                Optional. The set of allowed MIME types. If
                unspecified, all MIME types are allowed.
        """

        class MimeType(proto.Enum):
            r"""Different MIME types that the asset variable supports.

            Values:
                MIME_TYPE_UNSPECIFIED (0):
                    Default value. This value is unused.
                JPG (1):
                    The ``image/jpeg`` MIME type.
                PNG (2):
                    The ``image/png`` MIME type.
                GIF (3):
                    The ``image/gif`` MIME type.
            """

            MIME_TYPE_UNSPECIFIED = 0
            JPG = 1
            PNG = 2
            GIF = 3

        mime_types: MutableSequence[
            "CreativeTemplateVariable.AssetCreativeTemplateVariable.MimeType"
        ] = proto.RepeatedField(
            proto.ENUM,
            number=1,
            enum="CreativeTemplateVariable.AssetCreativeTemplateVariable.MimeType",
        )

    class ListStringCreativeTemplateVariable(proto.Message):
        r"""Represents a list variable defined in a creative template. This is
        similar to
        [StringCreativeTemplateVariable][google.ads.admanager.v1.CreativeTemplateVariable.StringCreativeTemplateVariable],
        except that there are possible choices to choose from.

        Use [StringCreativeTemplateVariableValue][] to specify the value for
        this variable when creating a [TemplateCreative][] from a
        [CreativeTemplate][google.ads.admanager.v1.CreativeTemplate].


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            default_value (str):
                Optional. Default value to be filled in when
                creating creatives from the creative template.

                This field is a member of `oneof`_ ``_default_value``.
            sample_value (str):
                Optional. Sample value that is used when
                previewing the template in the UI.

                This field is a member of `oneof`_ ``_sample_value``.
            choices (MutableSequence[google.ads.admanager_v1.types.CreativeTemplateVariable.ListStringCreativeTemplateVariable.VariableChoice]):
                Optional. The selectable values that the user
                can choose from.
            allow_other_choice (bool):
                Optional. ``True`` if a user can specify an 'other' value.
                For example, if a variable called backgroundColor is defined
                as a list with values: red, green, blue, this boolean can be
                set to allow a user to enter a value not on the list such as
                purple.

                This field is a member of `oneof`_ ``_allow_other_choice``.
        """

        class VariableChoice(proto.Message):
            r"""Stores variable choices selectable by users.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                label (str):
                    Required. A label is displayed to users when creating a
                    [TemplateCreative][]. This attribute is intended to be more
                    descriptive than value. This attribute has a maximum length
                    of 255 characters.

                    This field is a member of `oneof`_ ``_label``.
                value (str):
                    Required. When creating a [TemplateCreative][], the value in
                    [StringCreativeTemplateVariableValue][] should match this
                    value, if you intend to select this value. This attribute
                    has a maximum length of 255 characters.

                    This field is a member of `oneof`_ ``_value``.
            """

            label: str = proto.Field(
                proto.STRING,
                number=1,
                optional=True,
            )
            value: str = proto.Field(
                proto.STRING,
                number=2,
                optional=True,
            )

        default_value: str = proto.Field(
            proto.STRING,
            number=1,
            optional=True,
        )
        sample_value: str = proto.Field(
            proto.STRING,
            number=2,
            optional=True,
        )
        choices: MutableSequence[
            "CreativeTemplateVariable.ListStringCreativeTemplateVariable.VariableChoice"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="CreativeTemplateVariable.ListStringCreativeTemplateVariable.VariableChoice",
        )
        allow_other_choice: bool = proto.Field(
            proto.BOOL,
            number=4,
            optional=True,
        )

    class LongCreativeTemplateVariable(proto.Message):
        r"""Represents a long variable defined in a creative template.

        Use [LongCreativeTemplateVariableValue][] to specify the value for
        this variable when creating [TemplateCreative][] from a
        [CreativeTemplate][google.ads.admanager.v1.CreativeTemplate].


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            default_value (int):
                Optional. Default value to be filled in when
                creating creatives from the creative template.

                This field is a member of `oneof`_ ``_default_value``.
            sample_value (int):
                Optional. Sample value that is used when
                previewing the template in the UI.

                This field is a member of `oneof`_ ``_sample_value``.
        """

        default_value: int = proto.Field(
            proto.INT64,
            number=1,
            optional=True,
        )
        sample_value: int = proto.Field(
            proto.INT64,
            number=2,
            optional=True,
        )

    class StringCreativeTemplateVariable(proto.Message):
        r"""Represents a string variable defined in a creative template.

        Use [StringCreativeTemplateVariableValue][] to specify the value for
        this variable when creating [TemplateCreative][] from a
        [CreativeTemplate][google.ads.admanager.v1.CreativeTemplate].


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            default_value (str):
                Optional. Default value to be filled in when
                creating creatives from the creative template.

                This field is a member of `oneof`_ ``_default_value``.
            sample_value (str):
                Optional. Sample value that is used when
                previewing the template in the UI.

                This field is a member of `oneof`_ ``_sample_value``.
        """

        default_value: str = proto.Field(
            proto.STRING,
            number=1,
            optional=True,
        )
        sample_value: str = proto.Field(
            proto.STRING,
            number=2,
            optional=True,
        )

    class UrlCreativeTemplateVariable(proto.Message):
        r"""Represents a url variable defined in a creative template.

        Use [UrlCreativeTemplateVariableValue][] to specify the value for
        this variable when creating a [TemplateCreative][] from a
        [CreativeTemplate][google.ads.admanager.v1.CreativeTemplate].


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            default_value (str):
                Optional. Default value to be filled in when
                creating creatives from the creative template.

                This field is a member of `oneof`_ ``_default_value``.
            sample_value (str):
                Optional. Sample value that is used when
                previewing the template in the UI.

                This field is a member of `oneof`_ ``_sample_value``.
            url_type (google.ads.admanager_v1.types.CreativeTemplateVariableUrlTypeEnum.CreativeTemplateVariableUrlType):
                Optional. The type of URL that this variable
                represents. Different types of URLs may be
                handled differently at rendering time.

                This field is a member of `oneof`_ ``_url_type``.
        """

        default_value: str = proto.Field(
            proto.STRING,
            number=1,
            optional=True,
        )
        sample_value: str = proto.Field(
            proto.STRING,
            number=2,
            optional=True,
        )
        url_type: creative_template_variable_url_type_enum.CreativeTemplateVariableUrlTypeEnum.CreativeTemplateVariableUrlType = proto.Field(
            proto.ENUM,
            number=4,
            optional=True,
            enum=creative_template_variable_url_type_enum.CreativeTemplateVariableUrlTypeEnum.CreativeTemplateVariableUrlType,
        )

    asset_variable: AssetCreativeTemplateVariable = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="SubType",
        message=AssetCreativeTemplateVariable,
    )
    list_string_variable: ListStringCreativeTemplateVariable = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="SubType",
        message=ListStringCreativeTemplateVariable,
    )
    long_variable: LongCreativeTemplateVariable = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="SubType",
        message=LongCreativeTemplateVariable,
    )
    string_variable: StringCreativeTemplateVariable = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="SubType",
        message=StringCreativeTemplateVariable,
    )
    url_variable: UrlCreativeTemplateVariable = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="SubType",
        message=UrlCreativeTemplateVariable,
    )
    label: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    unique_display_name: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    required: bool = proto.Field(
        proto.BOOL,
        number=4,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
