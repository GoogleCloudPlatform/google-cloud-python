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
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.dialogflowcx_v3beta1.types import response_message

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.cx.v3beta1",
    manifest={
        "Webhook",
        "ListWebhooksRequest",
        "ListWebhooksResponse",
        "GetWebhookRequest",
        "CreateWebhookRequest",
        "UpdateWebhookRequest",
        "DeleteWebhookRequest",
        "WebhookRequest",
        "WebhookResponse",
        "PageInfo",
        "SessionInfo",
        "LanguageInfo",
    },
)


class Webhook(proto.Message):
    r"""Webhooks host the developer's business logic. During a
    session, webhooks allow the developer to use the data extracted
    by Dialogflow's natural language processing to generate dynamic
    responses, validate collected data, or trigger actions on the
    backend.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            The unique identifier of the webhook. Required for the
            [Webhooks.UpdateWebhook][google.cloud.dialogflow.cx.v3beta1.Webhooks.UpdateWebhook]
            method.
            [Webhooks.CreateWebhook][google.cloud.dialogflow.cx.v3beta1.Webhooks.CreateWebhook]
            populates the name automatically. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/webhooks/<WebhookID>``.
        display_name (str):
            Required. The human-readable name of the
            webhook, unique within the agent.
        generic_web_service (google.cloud.dialogflowcx_v3beta1.types.Webhook.GenericWebService):
            Configuration for a generic web service.

            This field is a member of `oneof`_ ``webhook``.
        service_directory (google.cloud.dialogflowcx_v3beta1.types.Webhook.ServiceDirectoryConfig):
            Configuration for a `Service
            Directory <https://cloud.google.com/service-directory>`__
            service.

            This field is a member of `oneof`_ ``webhook``.
        timeout (google.protobuf.duration_pb2.Duration):
            Webhook execution timeout. Execution is
            considered failed if Dialogflow doesn't receive
            a response from webhook at the end of the
            timeout period. Defaults to 5 seconds, maximum
            allowed timeout is 30 seconds.
        disabled (bool):
            Indicates whether the webhook is disabled.
    """

    class GenericWebService(proto.Message):
        r"""Represents configuration for a generic web service.

        Attributes:
            uri (str):
                Required. The webhook URI for receiving POST
                requests. It must use https protocol.
            username (str):
                The user name for HTTP Basic authentication.
            password (str):
                The password for HTTP Basic authentication.
            secret_version_for_username_password (str):
                Optional. The SecretManager secret version resource storing
                the username:password pair for HTTP Basic authentication.
                Format:
                ``projects/{project}/secrets/{secret}/versions/{version}``
            request_headers (MutableMapping[str, str]):
                The HTTP request headers to send together
                with webhook requests.
            secret_versions_for_request_headers (MutableMapping[str, google.cloud.dialogflowcx_v3beta1.types.Webhook.GenericWebService.SecretVersionHeaderValue]):
                Optional. The HTTP request headers to send together with
                webhook requests. Header values are stored in SecretManager
                secret versions.

                When the same header name is specified in both
                ``request_headers`` and
                ``secret_versions_for_request_headers``, the value in
                ``secret_versions_for_request_headers`` will be used.
            allowed_ca_certs (MutableSequence[bytes]):
                Optional. Specifies a list of allowed custom CA certificates
                (in DER format) for HTTPS verification. This overrides the
                default SSL trust store. If this is empty or unspecified,
                Dialogflow will use Google's default trust store to verify
                certificates. N.B. Make sure the HTTPS server certificates
                are signed with "subject alt name". For instance a
                certificate can be self-signed using the following command,

                ::

                      openssl x509 -req -days 200 -in example.com.csr \
                        -signkey example.com.key \
                        -out example.com.crt \
                        -extfile <(printf "\nsubjectAltName='DNS:www.example.com'")
            oauth_config (google.cloud.dialogflowcx_v3beta1.types.Webhook.GenericWebService.OAuthConfig):
                Optional. The OAuth configuration of the
                webhook. If specified, Dialogflow will initiate
                the OAuth client credential flow to exchange an
                access token from the 3rd party platform and put
                it in the auth header.
            service_agent_auth (google.cloud.dialogflowcx_v3beta1.types.Webhook.GenericWebService.ServiceAgentAuth):
                Optional. Indicate the auth token type generated from the
                `Diglogflow service
                agent <https://cloud.google.com/iam/docs/service-agents#dialogflow-service-agent>`__.
                The generated token is sent in the Authorization header.
            service_account_auth_config (google.cloud.dialogflowcx_v3beta1.types.Webhook.GenericWebService.ServiceAccountAuthConfig):
                Optional. Configuration for service account
                authentication.
            webhook_type (google.cloud.dialogflowcx_v3beta1.types.Webhook.GenericWebService.WebhookType):
                Optional. Type of the webhook.
            http_method (google.cloud.dialogflowcx_v3beta1.types.Webhook.GenericWebService.HttpMethod):
                Optional. HTTP method for the flexible
                webhook calls. Standard webhook always uses
                POST.
            request_body (str):
                Optional. Defines a custom JSON object as
                request body to send to flexible webhook.
            parameter_mapping (MutableMapping[str, str]):
                Optional. Maps the values extracted from
                specific fields of the flexible webhook response
                into session parameters.
                - Key: session parameter name
                - Value: field path in the webhook response
        """

        class ServiceAgentAuth(proto.Enum):
            r"""Indicate the auth token type generated from the `Diglogflow service
            agent <https://cloud.google.com/iam/docs/service-agents#dialogflow-service-agent>`__.

            Values:
                SERVICE_AGENT_AUTH_UNSPECIFIED (0):
                    Service agent auth type unspecified. Default to ID_TOKEN.
                NONE (1):
                    No token used.
                ID_TOKEN (2):
                    Use `ID
                    token <https://cloud.google.com/docs/authentication/token-types#id>`__
                    generated from service agent. This can be used to access
                    Cloud Function and Cloud Run after you grant Invoker role to
                    ``service-<PROJECT-NUMBER>@gcp-sa-dialogflow.iam.gserviceaccount.com``.
                ACCESS_TOKEN (3):
                    Use `access
                    token <https://cloud.google.com/docs/authentication/token-types#access>`__
                    generated from service agent. This can be used to access
                    other Google Cloud APIs after you grant required roles to
                    ``service-<PROJECT-NUMBER>@gcp-sa-dialogflow.iam.gserviceaccount.com``.
            """

            SERVICE_AGENT_AUTH_UNSPECIFIED = 0
            NONE = 1
            ID_TOKEN = 2
            ACCESS_TOKEN = 3

        class WebhookType(proto.Enum):
            r"""Represents the type of webhook configuration.

            Values:
                WEBHOOK_TYPE_UNSPECIFIED (0):
                    Default value. This value is unused.
                STANDARD (1):
                    Represents a standard webhook.
                FLEXIBLE (2):
                    Represents a flexible webhook.
            """

            WEBHOOK_TYPE_UNSPECIFIED = 0
            STANDARD = 1
            FLEXIBLE = 2

        class HttpMethod(proto.Enum):
            r"""HTTP method to use when calling webhooks.

            Values:
                HTTP_METHOD_UNSPECIFIED (0):
                    HTTP method not specified.
                POST (1):
                    HTTP POST Method.
                GET (2):
                    HTTP GET Method.
                HEAD (3):
                    HTTP HEAD Method.
                PUT (4):
                    HTTP PUT Method.
                DELETE (5):
                    HTTP DELETE Method.
                PATCH (6):
                    HTTP PATCH Method.
                OPTIONS (7):
                    HTTP OPTIONS Method.
            """

            HTTP_METHOD_UNSPECIFIED = 0
            POST = 1
            GET = 2
            HEAD = 3
            PUT = 4
            DELETE = 5
            PATCH = 6
            OPTIONS = 7

        class SecretVersionHeaderValue(proto.Message):
            r"""Represents the value of an HTTP header stored in a
            SecretManager secret version.

            Attributes:
                secret_version (str):
                    Required. The SecretManager secret version resource storing
                    the header value. Format:
                    ``projects/{project}/secrets/{secret}/versions/{version}``
            """

            secret_version: str = proto.Field(
                proto.STRING,
                number=1,
            )

        class OAuthConfig(proto.Message):
            r"""Represents configuration of OAuth client credential flow for
            3rd party API authentication.

            Attributes:
                client_id (str):
                    Required. The client ID provided by the 3rd
                    party platform.
                client_secret (str):
                    Optional. The client secret provided by the
                    3rd party platform.
                secret_version_for_client_secret (str):
                    Optional. The name of the SecretManager secret version
                    resource storing the client secret. If this field is set,
                    the ``client_secret`` field will be ignored. Format:
                    ``projects/{project}/secrets/{secret}/versions/{version}``
                token_endpoint (str):
                    Required. The token endpoint provided by the
                    3rd party platform to exchange an access token.
                scopes (MutableSequence[str]):
                    Optional. The OAuth scopes to grant.
            """

            client_id: str = proto.Field(
                proto.STRING,
                number=1,
            )
            client_secret: str = proto.Field(
                proto.STRING,
                number=2,
            )
            secret_version_for_client_secret: str = proto.Field(
                proto.STRING,
                number=5,
            )
            token_endpoint: str = proto.Field(
                proto.STRING,
                number=3,
            )
            scopes: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=4,
            )

        class ServiceAccountAuthConfig(proto.Message):
            r"""Configuration for authentication using a service account.

            Attributes:
                service_account (str):
                    Required. The email address of the service account used to
                    authenticate the webhook call. Dialogflow uses this service
                    account to exchange an access token and the access token is
                    then sent in the ``Authorization`` header of the webhook
                    request.

                    The service account must have the
                    ``roles/iam.serviceAccountTokenCreator`` role granted to the
                    `Dialogflow service
                    agent <https://cloud.google.com/iam/docs/service-agents#dialogflow-service-agent>`__.
            """

            service_account: str = proto.Field(
                proto.STRING,
                number=1,
            )

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
        secret_version_for_username_password: str = proto.Field(
            proto.STRING,
            number=19,
        )
        request_headers: MutableMapping[str, str] = proto.MapField(
            proto.STRING,
            proto.STRING,
            number=4,
        )
        secret_versions_for_request_headers: MutableMapping[
            str, "Webhook.GenericWebService.SecretVersionHeaderValue"
        ] = proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=20,
            message="Webhook.GenericWebService.SecretVersionHeaderValue",
        )
        allowed_ca_certs: MutableSequence[bytes] = proto.RepeatedField(
            proto.BYTES,
            number=5,
        )
        oauth_config: "Webhook.GenericWebService.OAuthConfig" = proto.Field(
            proto.MESSAGE,
            number=11,
            message="Webhook.GenericWebService.OAuthConfig",
        )
        service_agent_auth: "Webhook.GenericWebService.ServiceAgentAuth" = proto.Field(
            proto.ENUM,
            number=12,
            enum="Webhook.GenericWebService.ServiceAgentAuth",
        )
        service_account_auth_config: "Webhook.GenericWebService.ServiceAccountAuthConfig" = proto.Field(
            proto.MESSAGE,
            number=18,
            message="Webhook.GenericWebService.ServiceAccountAuthConfig",
        )
        webhook_type: "Webhook.GenericWebService.WebhookType" = proto.Field(
            proto.ENUM,
            number=6,
            enum="Webhook.GenericWebService.WebhookType",
        )
        http_method: "Webhook.GenericWebService.HttpMethod" = proto.Field(
            proto.ENUM,
            number=7,
            enum="Webhook.GenericWebService.HttpMethod",
        )
        request_body: str = proto.Field(
            proto.STRING,
            number=8,
        )
        parameter_mapping: MutableMapping[str, str] = proto.MapField(
            proto.STRING,
            proto.STRING,
            number=9,
        )

    class ServiceDirectoryConfig(proto.Message):
        r"""Represents configuration for a `Service
        Directory <https://cloud.google.com/service-directory>`__ service.

        Attributes:
            service (str):
                Required. The name of `Service
                Directory <https://cloud.google.com/service-directory>`__
                service. Format:
                ``projects/<ProjectID>/locations/<LocationID>/namespaces/<NamespaceID>/services/<ServiceID>``.
                ``Location ID`` of the service directory must be the same as
                the location of the agent.
            generic_web_service (google.cloud.dialogflowcx_v3beta1.types.Webhook.GenericWebService):
                Generic Service configuration of this
                webhook.
        """

        service: str = proto.Field(
            proto.STRING,
            number=1,
        )
        generic_web_service: "Webhook.GenericWebService" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="Webhook.GenericWebService",
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
        number=4,
        oneof="webhook",
        message=GenericWebService,
    )
    service_directory: ServiceDirectoryConfig = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="webhook",
        message=ServiceDirectoryConfig,
    )
    timeout: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=6,
        message=duration_pb2.Duration,
    )
    disabled: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class ListWebhooksRequest(proto.Message):
    r"""The request message for
    [Webhooks.ListWebhooks][google.cloud.dialogflow.cx.v3beta1.Webhooks.ListWebhooks].

    Attributes:
        parent (str):
            Required. The agent to list all webhooks for. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>``.
        page_size (int):
            The maximum number of items to return in a
            single page. By default 100 and at most 1000.
        page_token (str):
            The next_page_token value returned from a previous list
            request.
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


class ListWebhooksResponse(proto.Message):
    r"""The response message for
    [Webhooks.ListWebhooks][google.cloud.dialogflow.cx.v3beta1.Webhooks.ListWebhooks].

    Attributes:
        webhooks (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.Webhook]):
            The list of webhooks. There will be a maximum number of
            items returned based on the page_size field in the request.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    webhooks: MutableSequence["Webhook"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Webhook",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetWebhookRequest(proto.Message):
    r"""The request message for
    [Webhooks.GetWebhook][google.cloud.dialogflow.cx.v3beta1.Webhooks.GetWebhook].

    Attributes:
        name (str):
            Required. The name of the webhook. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/webhooks/<WebhookID>``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateWebhookRequest(proto.Message):
    r"""The request message for
    [Webhooks.CreateWebhook][google.cloud.dialogflow.cx.v3beta1.Webhooks.CreateWebhook].

    Attributes:
        parent (str):
            Required. The agent to create a webhook for. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>``.
        webhook (google.cloud.dialogflowcx_v3beta1.types.Webhook):
            Required. The webhook to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    webhook: "Webhook" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Webhook",
    )


class UpdateWebhookRequest(proto.Message):
    r"""The request message for
    [Webhooks.UpdateWebhook][google.cloud.dialogflow.cx.v3beta1.Webhooks.UpdateWebhook].

    Attributes:
        webhook (google.cloud.dialogflowcx_v3beta1.types.Webhook):
            Required. The webhook to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The mask to control which fields get updated.
            If the mask is not present, all fields will be
            updated.
    """

    webhook: "Webhook" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Webhook",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteWebhookRequest(proto.Message):
    r"""The request message for
    [Webhooks.DeleteWebhook][google.cloud.dialogflow.cx.v3beta1.Webhooks.DeleteWebhook].

    Attributes:
        name (str):
            Required. The name of the webhook to delete. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/webhooks/<WebhookID>``.
        force (bool):
            This field has no effect for webhook not being used. For
            webhooks that are used by pages/flows/transition route
            groups:

            - If ``force`` is set to false, an error will be returned
              with message indicating the referenced resources.
            - If ``force`` is set to true, Dialogflow will remove the
              webhook, as well as any references to the webhook (i.e.
              [Webhook][google.cloud.dialogflow.cx.v3beta1.Fulfillment.webhook]
              and
              [tag][google.cloud.dialogflow.cx.v3beta1.Fulfillment.tag]in
              fulfillments that point to this webhook will be removed).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class WebhookRequest(proto.Message):
    r"""The request message for a webhook call. The request is sent
    as a JSON object and the field names will be presented in camel
    cases.

    You may see undocumented fields in an actual request. These
    fields are used internally by Dialogflow and should be ignored.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        detect_intent_response_id (str):
            Always present. The unique identifier of the
            [DetectIntentResponse][google.cloud.dialogflow.cx.v3beta1.DetectIntentResponse]
            that will be returned to the API caller.
        text (str):
            If [natural language
            text][google.cloud.dialogflow.cx.v3beta1.TextInput] was
            provided as input, this field will contain a copy of the
            text.

            This field is a member of `oneof`_ ``query``.
        trigger_intent (str):
            If an
            [intent][google.cloud.dialogflow.cx.v3beta1.IntentInput] was
            provided as input, this field will contain a copy of the
            intent identifier. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/intents/<IntentID>``.

            This field is a member of `oneof`_ ``query``.
        transcript (str):
            If [natural language speech
            audio][google.cloud.dialogflow.cx.v3beta1.AudioInput] was
            provided as input, this field will contain the transcript
            for the audio.

            This field is a member of `oneof`_ ``query``.
        trigger_event (str):
            If an [event][google.cloud.dialogflow.cx.v3beta1.EventInput]
            was provided as input, this field will contain the name of
            the event.

            This field is a member of `oneof`_ ``query``.
        dtmf_digits (str):
            If [DTMF][google.cloud.dialogflow.cx.v3beta1.DtmfInput] was
            provided as input, this field will contain the DTMF digits.

            This field is a member of `oneof`_ ``query``.
        language_code (str):
            The language code specified in the [original
            request][QueryInput.language_code].
        fulfillment_info (google.cloud.dialogflowcx_v3beta1.types.WebhookRequest.FulfillmentInfo):
            Always present. Information about the
            fulfillment that triggered this webhook call.
        intent_info (google.cloud.dialogflowcx_v3beta1.types.WebhookRequest.IntentInfo):
            Information about the last matched intent.
        page_info (google.cloud.dialogflowcx_v3beta1.types.PageInfo):
            Information about page status.
        session_info (google.cloud.dialogflowcx_v3beta1.types.SessionInfo):
            Information about session status.
        messages (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.ResponseMessage]):
            The list of rich message responses to present to the user.
            Webhook can choose to append or replace this list in
            [WebhookResponse.fulfillment_response][google.cloud.dialogflow.cx.v3beta1.WebhookResponse.fulfillment_response];
        payload (google.protobuf.struct_pb2.Struct):
            Custom data set in
            [QueryParameters.payload][google.cloud.dialogflow.cx.v3beta1.QueryParameters.payload].
        sentiment_analysis_result (google.cloud.dialogflowcx_v3beta1.types.WebhookRequest.SentimentAnalysisResult):
            The sentiment analysis result of the current
            user request. The field is filled when sentiment
            analysis is configured to be enabled for the
            request.
        language_info (google.cloud.dialogflowcx_v3beta1.types.LanguageInfo):
            Information about the language of the
            request.
    """

    class FulfillmentInfo(proto.Message):
        r"""Represents fulfillment information communicated to the
        webhook.

        Attributes:
            tag (str):
                Always present. The value of the
                [Fulfillment.tag][google.cloud.dialogflow.cx.v3beta1.Fulfillment.tag]
                field will be populated in this field by Dialogflow when the
                associated webhook is called. The tag is typically used by
                the webhook service to identify which fulfillment is being
                called, but it could be used for other purposes.
        """

        tag: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class IntentInfo(proto.Message):
        r"""Represents intent information communicated to the webhook.

        Attributes:
            last_matched_intent (str):
                Always present. The unique identifier of the last matched
                [intent][google.cloud.dialogflow.cx.v3beta1.Intent]. Format:
                ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/intents/<IntentID>``.
            display_name (str):
                Always present. The display name of the last matched
                [intent][google.cloud.dialogflow.cx.v3beta1.Intent].
            parameters (MutableMapping[str, google.cloud.dialogflowcx_v3beta1.types.WebhookRequest.IntentInfo.IntentParameterValue]):
                Parameters identified as a result of intent
                matching. This is a map of the name of the
                identified parameter to the value of the
                parameter identified from the user's utterance.
                All parameters defined in the matched intent
                that are identified will be surfaced here.
            confidence (float):
                The confidence of the matched intent. Values
                range from 0.0 (completely uncertain) to 1.0
                (completely certain).
        """

        class IntentParameterValue(proto.Message):
            r"""Represents a value for an intent parameter.

            Attributes:
                original_value (str):
                    Always present. Original text value extracted
                    from user utterance.
                resolved_value (google.protobuf.struct_pb2.Value):
                    Always present. Structured value for the
                    parameter extracted from user utterance.
            """

            original_value: str = proto.Field(
                proto.STRING,
                number=1,
            )
            resolved_value: struct_pb2.Value = proto.Field(
                proto.MESSAGE,
                number=2,
                message=struct_pb2.Value,
            )

        last_matched_intent: str = proto.Field(
            proto.STRING,
            number=1,
        )
        display_name: str = proto.Field(
            proto.STRING,
            number=3,
        )
        parameters: MutableMapping[
            str, "WebhookRequest.IntentInfo.IntentParameterValue"
        ] = proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=2,
            message="WebhookRequest.IntentInfo.IntentParameterValue",
        )
        confidence: float = proto.Field(
            proto.FLOAT,
            number=4,
        )

    class SentimentAnalysisResult(proto.Message):
        r"""Represents the result of sentiment analysis.

        Attributes:
            score (float):
                Sentiment score between -1.0 (negative
                sentiment) and 1.0 (positive  sentiment).
            magnitude (float):
                A non-negative number in the [0, +inf) range, which
                represents the absolute magnitude of sentiment, regardless
                of score (positive or negative).
        """

        score: float = proto.Field(
            proto.FLOAT,
            number=1,
        )
        magnitude: float = proto.Field(
            proto.FLOAT,
            number=2,
        )

    detect_intent_response_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    text: str = proto.Field(
        proto.STRING,
        number=10,
        oneof="query",
    )
    trigger_intent: str = proto.Field(
        proto.STRING,
        number=11,
        oneof="query",
    )
    transcript: str = proto.Field(
        proto.STRING,
        number=12,
        oneof="query",
    )
    trigger_event: str = proto.Field(
        proto.STRING,
        number=14,
        oneof="query",
    )
    dtmf_digits: str = proto.Field(
        proto.STRING,
        number=17,
        oneof="query",
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=15,
    )
    fulfillment_info: FulfillmentInfo = proto.Field(
        proto.MESSAGE,
        number=6,
        message=FulfillmentInfo,
    )
    intent_info: IntentInfo = proto.Field(
        proto.MESSAGE,
        number=3,
        message=IntentInfo,
    )
    page_info: "PageInfo" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="PageInfo",
    )
    session_info: "SessionInfo" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="SessionInfo",
    )
    messages: MutableSequence[response_message.ResponseMessage] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message=response_message.ResponseMessage,
    )
    payload: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=8,
        message=struct_pb2.Struct,
    )
    sentiment_analysis_result: SentimentAnalysisResult = proto.Field(
        proto.MESSAGE,
        number=9,
        message=SentimentAnalysisResult,
    )
    language_info: "LanguageInfo" = proto.Field(
        proto.MESSAGE,
        number=18,
        message="LanguageInfo",
    )


class WebhookResponse(proto.Message):
    r"""The response message for a webhook call.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        fulfillment_response (google.cloud.dialogflowcx_v3beta1.types.WebhookResponse.FulfillmentResponse):
            The fulfillment response to send to the user.
            This field can be omitted by the webhook if it
            does not intend to send any response to the
            user.
        page_info (google.cloud.dialogflowcx_v3beta1.types.PageInfo):
            Information about page status. This field can
            be omitted by the webhook if it does not intend
            to modify page status.
        session_info (google.cloud.dialogflowcx_v3beta1.types.SessionInfo):
            Information about session status. This field
            can be omitted by the webhook if it does not
            intend to modify session status.
        payload (google.protobuf.struct_pb2.Struct):
            Value to append directly to
            [QueryResult.webhook_payloads][google.cloud.dialogflow.cx.v3beta1.QueryResult.webhook_payloads].
        target_page (str):
            The target page to transition to. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/pages/<PageID>``.

            This field is a member of `oneof`_ ``transition``.
        target_flow (str):
            The target flow to transition to. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>``.

            This field is a member of `oneof`_ ``transition``.
    """

    class FulfillmentResponse(proto.Message):
        r"""Represents a fulfillment response to the user.

        Attributes:
            messages (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.ResponseMessage]):
                The list of rich message responses to present
                to the user.
            merge_behavior (google.cloud.dialogflowcx_v3beta1.types.WebhookResponse.FulfillmentResponse.MergeBehavior):
                Merge behavior for ``messages``.
        """

        class MergeBehavior(proto.Enum):
            r"""Defines merge behavior for ``messages``.

            Values:
                MERGE_BEHAVIOR_UNSPECIFIED (0):
                    Not specified. ``APPEND`` will be used.
                APPEND (1):
                    ``messages`` will be appended to the list of messages
                    waiting to be sent to the user.
                REPLACE (2):
                    ``messages`` will replace the list of messages waiting to be
                    sent to the user.
            """

            MERGE_BEHAVIOR_UNSPECIFIED = 0
            APPEND = 1
            REPLACE = 2

        messages: MutableSequence[response_message.ResponseMessage] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message=response_message.ResponseMessage,
            )
        )
        merge_behavior: "WebhookResponse.FulfillmentResponse.MergeBehavior" = (
            proto.Field(
                proto.ENUM,
                number=2,
                enum="WebhookResponse.FulfillmentResponse.MergeBehavior",
            )
        )

    fulfillment_response: FulfillmentResponse = proto.Field(
        proto.MESSAGE,
        number=1,
        message=FulfillmentResponse,
    )
    page_info: "PageInfo" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="PageInfo",
    )
    session_info: "SessionInfo" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="SessionInfo",
    )
    payload: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=4,
        message=struct_pb2.Struct,
    )
    target_page: str = proto.Field(
        proto.STRING,
        number=5,
        oneof="transition",
    )
    target_flow: str = proto.Field(
        proto.STRING,
        number=6,
        oneof="transition",
    )


class PageInfo(proto.Message):
    r"""Represents page information communicated to and from the
    webhook.

    Attributes:
        current_page (str):
            Always present for
            [WebhookRequest][google.cloud.dialogflow.cx.v3beta1.WebhookRequest].
            Ignored for
            [WebhookResponse][google.cloud.dialogflow.cx.v3beta1.WebhookResponse].
            The unique identifier of the current page. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/pages/<PageID>``.
        display_name (str):
            Always present for
            [WebhookRequest][google.cloud.dialogflow.cx.v3beta1.WebhookRequest].
            Ignored for
            [WebhookResponse][google.cloud.dialogflow.cx.v3beta1.WebhookResponse].
            The display name of the current page.
        form_info (google.cloud.dialogflowcx_v3beta1.types.PageInfo.FormInfo):
            Optional for both
            [WebhookRequest][google.cloud.dialogflow.cx.v3beta1.WebhookRequest]
            and
            [WebhookResponse][google.cloud.dialogflow.cx.v3beta1.WebhookResponse].
            Information about the form.
    """

    class FormInfo(proto.Message):
        r"""Represents form information.

        Attributes:
            parameter_info (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.PageInfo.FormInfo.ParameterInfo]):
                Optional for both
                [WebhookRequest][google.cloud.dialogflow.cx.v3beta1.WebhookRequest]
                and
                [WebhookResponse][google.cloud.dialogflow.cx.v3beta1.WebhookResponse].
                The parameters contained in the form. Note that the webhook
                cannot add or remove any form parameter.
        """

        class ParameterInfo(proto.Message):
            r"""Represents parameter information.

            Attributes:
                display_name (str):
                    Always present for
                    [WebhookRequest][google.cloud.dialogflow.cx.v3beta1.WebhookRequest].
                    Required for
                    [WebhookResponse][google.cloud.dialogflow.cx.v3beta1.WebhookResponse].
                    The human-readable name of the parameter, unique within the
                    form. This field cannot be modified by the webhook.
                required (bool):
                    Optional for both
                    [WebhookRequest][google.cloud.dialogflow.cx.v3beta1.WebhookRequest]
                    and
                    [WebhookResponse][google.cloud.dialogflow.cx.v3beta1.WebhookResponse].
                    Indicates whether the parameter is required. Optional
                    parameters will not trigger prompts; however, they are
                    filled if the user specifies them. Required parameters must
                    be filled before form filling concludes.
                state (google.cloud.dialogflowcx_v3beta1.types.PageInfo.FormInfo.ParameterInfo.ParameterState):
                    Always present for
                    [WebhookRequest][google.cloud.dialogflow.cx.v3beta1.WebhookRequest].
                    Required for
                    [WebhookResponse][google.cloud.dialogflow.cx.v3beta1.WebhookResponse].
                    The state of the parameter. This field can be set to
                    [INVALID][google.cloud.dialogflow.cx.v3beta1.PageInfo.FormInfo.ParameterInfo.ParameterState.INVALID]
                    by the webhook to invalidate the parameter; other values set
                    by the webhook will be ignored.
                value (google.protobuf.struct_pb2.Value):
                    Optional for both
                    [WebhookRequest][google.cloud.dialogflow.cx.v3beta1.WebhookRequest]
                    and
                    [WebhookResponse][google.cloud.dialogflow.cx.v3beta1.WebhookResponse].
                    The value of the parameter. This field can be set by the
                    webhook to change the parameter value.
                just_collected (bool):
                    Optional for
                    [WebhookRequest][google.cloud.dialogflow.cx.v3beta1.WebhookRequest].
                    Ignored for
                    [WebhookResponse][google.cloud.dialogflow.cx.v3beta1.WebhookResponse].
                    Indicates if the parameter value was just collected on the
                    last conversation turn.
            """

            class ParameterState(proto.Enum):
                r"""Represents the state of a parameter.

                Values:
                    PARAMETER_STATE_UNSPECIFIED (0):
                        Not specified. This value should be never
                        used.
                    EMPTY (1):
                        Indicates that the parameter does not have a
                        value.
                    INVALID (2):
                        Indicates that the parameter value is
                        invalid. This field can be used by the webhook
                        to invalidate the parameter and ask the server
                        to collect it from the user again.
                    FILLED (3):
                        Indicates that the parameter has a value.
                """

                PARAMETER_STATE_UNSPECIFIED = 0
                EMPTY = 1
                INVALID = 2
                FILLED = 3

            display_name: str = proto.Field(
                proto.STRING,
                number=1,
            )
            required: bool = proto.Field(
                proto.BOOL,
                number=2,
            )
            state: "PageInfo.FormInfo.ParameterInfo.ParameterState" = proto.Field(
                proto.ENUM,
                number=3,
                enum="PageInfo.FormInfo.ParameterInfo.ParameterState",
            )
            value: struct_pb2.Value = proto.Field(
                proto.MESSAGE,
                number=4,
                message=struct_pb2.Value,
            )
            just_collected: bool = proto.Field(
                proto.BOOL,
                number=5,
            )

        parameter_info: MutableSequence["PageInfo.FormInfo.ParameterInfo"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="PageInfo.FormInfo.ParameterInfo",
            )
        )

    current_page: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    form_info: FormInfo = proto.Field(
        proto.MESSAGE,
        number=3,
        message=FormInfo,
    )


class SessionInfo(proto.Message):
    r"""Represents session information communicated to and from the
    webhook.

    Attributes:
        session (str):
            Always present for
            [WebhookRequest][google.cloud.dialogflow.cx.v3beta1.WebhookRequest].
            Ignored for
            [WebhookResponse][google.cloud.dialogflow.cx.v3beta1.WebhookResponse].
            The unique identifier of the
            [session][google.cloud.dialogflow.cx.v3beta1.DetectIntentRequest.session].
            This field can be used by the webhook to identify a session.
            Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/sessions/<SessionID>``
            or
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>/sessions/<SessionID>``
            if environment is specified.
        parameters (MutableMapping[str, google.protobuf.struct_pb2.Value]):
            Optional for
            [WebhookRequest][google.cloud.dialogflow.cx.v3beta1.WebhookRequest].
            Optional for
            [WebhookResponse][google.cloud.dialogflow.cx.v3beta1.WebhookResponse].
            All parameters collected from forms and intents during the
            session. Parameters can be created, updated, or removed by
            the webhook. To remove a parameter from the session, the
            webhook should explicitly set the parameter value to null in
            [WebhookResponse][google.cloud.dialogflow.cx.v3beta1.WebhookResponse].
            The map is keyed by parameters' display names.
    """

    session: str = proto.Field(
        proto.STRING,
        number=1,
    )
    parameters: MutableMapping[str, struct_pb2.Value] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=2,
        message=struct_pb2.Value,
    )


class LanguageInfo(proto.Message):
    r"""Represents the language information of the request.

    Attributes:
        input_language_code (str):
            The language code specified in the original
            [request][google.cloud.dialogflow.cx.v3beta1.QueryInput.language_code].
        resolved_language_code (str):
            The language code detected for this request
            based on the user conversation.
        confidence_score (float):
            The confidence score of the detected language
            between 0 and 1.
    """

    input_language_code: str = proto.Field(
        proto.STRING,
        number=1,
    )
    resolved_language_code: str = proto.Field(
        proto.STRING,
        number=2,
    )
    confidence_score: float = proto.Field(
        proto.FLOAT,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
