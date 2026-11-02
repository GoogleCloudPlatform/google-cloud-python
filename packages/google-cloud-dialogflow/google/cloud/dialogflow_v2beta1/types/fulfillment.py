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
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.v2beta1",
    manifest={
        "Fulfillment",
        "GetFulfillmentRequest",
        "UpdateFulfillmentRequest",
    },
)


class Fulfillment(proto.Message):
    r"""By default, your agent responds to a matched intent with a static
    response. As an alternative, you can provide a more dynamic response
    by using fulfillment. When you enable fulfillment for an intent,
    Dialogflow responds to that intent by calling a service that you
    define. For example, if an end-user wants to schedule a haircut on
    Friday, your service can check your database and respond to the
    end-user with availability information for Friday.

    For more information, see the `fulfillment
    guide <https://cloud.google.com/dialogflow/docs/fulfillment-overview>`__.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. The unique identifier of the fulfillment.
            Supported formats:

            - ``projects/<Project ID>/agent/fulfillment``
            - ``projects/<Project ID>/locations/<Location ID>/agent/fulfillment``

            This field is not used for Fulfillment in an Environment.
        display_name (str):
            The human-readable name of the fulfillment,
            unique within the agent.
            This field is not used for Fulfillment in an
            Environment.
        generic_web_service (google.cloud.dialogflow_v2beta1.types.Fulfillment.GenericWebService):
            Configuration for a generic web service.

            This field is a member of `oneof`_ ``fulfillment``.
        enabled (bool):
            Whether fulfillment is enabled.
        features (MutableSequence[google.cloud.dialogflow_v2beta1.types.Fulfillment.Feature]):
            The field defines whether the fulfillment is
            enabled for certain features.
    """

    class GenericWebService(proto.Message):
        r"""Represents configuration for a generic web service.
        Dialogflow supports two mechanisms for authentications:

        - Basic authentication with username and password.
        - Authentication with additional authentication headers.

        More information could be found at:

        https://cloud.google.com/dialogflow/docs/fulfillment-configure.

        Attributes:
            uri (str):
                Required. The fulfillment URI for receiving
                POST requests. It must use https protocol.
            username (str):
                The user name for HTTP Basic authentication.
            password (str):
                The password for HTTP Basic authentication.
            request_headers (MutableMapping[str, str]):
                The HTTP request headers to send together
                with fulfillment requests.
            is_cloud_function (bool):
                Optional. Indicates if generic web service is created
                through Cloud Functions integration. Defaults to false.

                is_cloud_function is deprecated. Cloud functions can be
                configured by its uri as a regular web service now.
        """

        uri: str = proto.Field(
            proto.STRING,
            number=1,
        )
        username: str = proto.Field(
            proto.STRING,
            number=2,
        )
        password: str = proto.Field(
            proto.STRING,
            number=3,
        )
        request_headers: MutableMapping[str, str] = proto.MapField(
            proto.STRING,
            proto.STRING,
            number=4,
        )
        is_cloud_function: bool = proto.Field(
            proto.BOOL,
            number=5,
        )

    class Feature(proto.Message):
        r"""Whether fulfillment is enabled for the specific feature.

        Attributes:
            type_ (google.cloud.dialogflow_v2beta1.types.Fulfillment.Feature.Type):
                The type of the feature that enabled for
                fulfillment.
        """

        class Type(proto.Enum):
            r"""The type of the feature.

            Values:
                TYPE_UNSPECIFIED (0):
                    Feature type not specified.
                SMALLTALK (1):
                    Fulfillment is enabled for SmallTalk.
            """

            TYPE_UNSPECIFIED = 0
            SMALLTALK = 1

        type_: "Fulfillment.Feature.Type" = proto.Field(
            proto.ENUM,
            number=1,
            enum="Fulfillment.Feature.Type",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    generic_web_service: GenericWebService = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="fulfillment",
        message=GenericWebService,
    )
    enabled: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    features: MutableSequence[Feature] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=Feature,
    )


class GetFulfillmentRequest(proto.Message):
    r"""The request message for
    [Fulfillments.GetFulfillment][google.cloud.dialogflow.v2beta1.Fulfillments.GetFulfillment].

    Attributes:
        name (str):
            Required. The name of the fulfillment. Supported formats:

            - ``projects/<Project ID>/agent/fulfillment``
            - ``projects/<Project ID>/locations/<Location ID>/agent/fulfillment``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateFulfillmentRequest(proto.Message):
    r"""The request message for
    [Fulfillments.UpdateFulfillment][google.cloud.dialogflow.v2beta1.Fulfillments.UpdateFulfillment].

    Attributes:
        fulfillment (google.cloud.dialogflow_v2beta1.types.Fulfillment):
            Required. The fulfillment to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The mask to control which fields
            get updated. If the mask is not present, all
            fields will be updated.
    """

    fulfillment: "Fulfillment" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Fulfillment",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
