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
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.ces.v1",
    manifest={
        "Omnichannel",
        "OmnichannelIntegrationConfig",
    },
)


class Omnichannel(proto.Message):
    r"""Represents an Omnichannel resource.

    Attributes:
        name (str):
            Identifier. The unique identifier of the omnichannel
            resource. Format:
            ``projects/{project}/locations/{location}/omnichannels/{omnichannel}``
        display_name (str):
            Required. Display name of the omnichannel
            resource.
        description (str):
            Optional. Human-readable description of the
            omnichannel resource.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the omnichannel
            resource was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the omnichannel
            resource was last updated.
        etag (str):
            Output only. Etag used to ensure the object
            hasn't changed during a read-modify-write
            operation.
        integration_config (google.cloud.ces_v1.types.OmnichannelIntegrationConfig):
            Optional. The integration config for the
            omnichannel resource.
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
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=6,
    )
    integration_config: "OmnichannelIntegrationConfig" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="OmnichannelIntegrationConfig",
    )


class OmnichannelIntegrationConfig(proto.Message):
    r"""OmnichannelIntegrationConfig contains all App integration
    configs.

    Attributes:
        channel_configs (MutableMapping[str, google.cloud.ces_v1.types.OmnichannelIntegrationConfig.ChannelConfig]):
            Optional. Various of configuration for
            handling App events.
        subscriber_configs (MutableMapping[str, google.cloud.ces_v1.types.OmnichannelIntegrationConfig.SubscriberConfig]):
            Optional. Various of subscribers configs.
        routing_configs (MutableMapping[str, google.cloud.ces_v1.types.OmnichannelIntegrationConfig.RoutingConfig]):
            Optional. The key of routing_configs is a key of
            ``app_configs``, value is a ``RoutingConfig``, which
            contains subscriber's key.
    """

    class ChannelConfig(proto.Message):
        r"""ChannelConfig contains config for various of app integration.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            whatsapp_config (google.cloud.ces_v1.types.OmnichannelIntegrationConfig.WhatsappConfig):
                WhatsApp config.

                This field is a member of `oneof`_ ``channel_config``.
        """

        whatsapp_config: "OmnichannelIntegrationConfig.WhatsappConfig" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="channel_config",
            message="OmnichannelIntegrationConfig.WhatsappConfig",
        )

    class WhatsappConfig(proto.Message):
        r"""How Omnichannel should receive/reply events from WhatsApp.

        Attributes:
            phone_number_id (str):
                The Phone Number ID associated with the
                WhatsApp Business Account.
            phone_number (str):
                The phone number used for sending/receiving
                messages.
            whatsapp_business_account_id (str):
                The customer's WhatsApp Business Account
                (WABA) ID.
            webhook_verify_token (str):
                The verify token configured in the Meta App
                Dashboard for webhook verification.
            whatsapp_business_token (str):
                The access token for authenticating API calls
                to the WhatsApp Cloud API.
                https://developers.facebook.com/docs/whatsapp/business-management-api/get-started/#business-integration-system-user-access-tokens
            meta_business_portfolio_id (str):
                The Meta Business Portfolio (MBP) ID.
                https://www.facebook.com/business/help/1710077379203657
        """

        phone_number_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        phone_number: str = proto.Field(
            proto.STRING,
            number=2,
        )
        whatsapp_business_account_id: str = proto.Field(
            proto.STRING,
            number=3,
        )
        webhook_verify_token: str = proto.Field(
            proto.STRING,
            number=4,
        )
        whatsapp_business_token: str = proto.Field(
            proto.STRING,
            number=5,
        )
        meta_business_portfolio_id: str = proto.Field(
            proto.STRING,
            number=6,
        )

    class SubscriberConfig(proto.Message):
        r"""Configs of subscribers.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            ces_app_config (google.cloud.ces_v1.types.OmnichannelIntegrationConfig.CesAppConfig):
                Ces app config.

                This field is a member of `oneof`_ ``subscriber_config``.
        """

        ces_app_config: "OmnichannelIntegrationConfig.CesAppConfig" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="subscriber_config",
            message="OmnichannelIntegrationConfig.CesAppConfig",
        )

    class CesAppConfig(proto.Message):
        r"""Configs for CES app.

        Attributes:
            app (str):
                The unique identifier of the CES app. Format:
                ``projects/{project}/locations/{location}/apps/{app}``
        """

        app: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class RoutingConfig(proto.Message):
        r"""Routing config specify how/who to route app events to a
        subscriber.

        Attributes:
            subscriber_key (str):
                The key of the subscriber.
        """

        subscriber_key: str = proto.Field(
            proto.STRING,
            number=1,
        )

    channel_configs: MutableMapping[str, ChannelConfig] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=1,
        message=ChannelConfig,
    )
    subscriber_configs: MutableMapping[str, SubscriberConfig] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=2,
        message=SubscriberConfig,
    )
    routing_configs: MutableMapping[str, RoutingConfig] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=3,
        message=RoutingConfig,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
