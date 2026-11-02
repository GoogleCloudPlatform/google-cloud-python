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
    package="google.cloud.datacatalog.lineage.configmanagement.v1",
    manifest={
        "GetConfigRequest",
        "UpdateConfigRequest",
        "Config",
    },
)


class GetConfigRequest(proto.Message):
    r"""Request message for GetConfig RPC.

    Attributes:
        name (str):
            Required. REQUIRED: The resource name of the config to be
            fetched. Format:
            ``organizations/{organization_id}/locations/global/config``
            ``folders/{folder_id}/locations/global/config``
            ``projects/{project_id}/locations/global/config``
            ``projects/{project_number}/locations/global/config``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateConfigRequest(proto.Message):
    r"""Request message for UpdateConfig RPC.

    Attributes:
        config (google.cloud.datacatalog_lineage_configmanagement_v1.types.Config):
            Required. REQUIRED: The config to be applied
            to the resource and all its descendants.
    """

    config: "Config" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Config",
    )


class Config(proto.Message):
    r"""Configuration for Data Lineage. Defines different
    configuration options for Lineage customers to control behaviour
    of lineage systems.

    Attributes:
        name (str):
            Identifier. The resource name of the config. Format:
            ``organizations/{organization_id}/locations/global/config``
            ``folders/{folder_id}/locations/global/config``
            ``projects/{project_id}/locations/global/config``
            ``projects/{project_number}/locations/global/config``
        ingestion (google.cloud.datacatalog_lineage_configmanagement_v1.types.Config.Ingestion):
            Optional. Ingestion rule for Data Lineage
            ingestion.
        etag (str):
            Optional. ``etag`` is used for optimistic concurrency
            control as a way to help prevent simultaneous updates of a
            config from overwriting each other. It is required that
            systems make use of the ``etag`` in the read-modify-write
            cycle to perform config updates in order to avoid race
            conditions: An ``etag`` is returned in the response to
            ``GetConfig``, and systems are expected to put that etag in
            the request to ``UpdateConfig`` to ensure that their change
            will be applied to the same version of the config. If an
            ``etag`` is not provided in the call to ``UpdateConfig``,
            then the existing config, if any, will be overwritten.
    """

    class Ingestion(proto.Message):
        r"""Defines how Lineage should be ingested for a given resource.

        Attributes:
            rules (MutableSequence[google.cloud.datacatalog_lineage_configmanagement_v1.types.Config.Ingestion.IngestionRule]):
                Optional. List of rules for Data Lineage
                ingestion.
        """

        class IngestionRule(proto.Message):
            r"""Ingestion rule for Data Lineage ingestion.

            Attributes:
                integration_selector (google.cloud.datacatalog_lineage_configmanagement_v1.types.Config.Ingestion.IngestionRule.IntegrationSelector):
                    Required. Integration selector of the rule.
                    The rule is only applied to the Integration
                    selected by the selector.
                lineage_enablement (google.cloud.datacatalog_lineage_configmanagement_v1.types.Config.Ingestion.IngestionRule.LineageEnablement):
                    Required. Lineage enablement configuration.
                    Defines configurations for the ingestion of
                    lineage for the resource and its children. If
                    unspecified, the ingestion will be enabled only
                    if it was configured in the resource's parent.
            """

            class IntegrationSelector(proto.Message):
                r"""Integration selector of the rule. The rule is only applied to
                the Integration selected by the selector.

                Attributes:
                    integration (google.cloud.datacatalog_lineage_configmanagement_v1.types.Config.Ingestion.IngestionRule.IntegrationSelector.Integration):
                        Required. Integration to which the rule
                        applies. This field can be used to specify the
                        integration against which the ingestion rule
                        should be applied.
                """

                class Integration(proto.Enum):
                    r"""Integration to which the rule applies.
                    This enum is expected to grow over time.

                    Values:
                        INTEGRATION_UNSPECIFIED (0):
                            Integration is Unspecified
                        DATAPROC (2):
                            Dataproc
                        LOOKER_CORE (3):
                            Looker Core
                    """

                    INTEGRATION_UNSPECIFIED = 0
                    DATAPROC = 2
                    LOOKER_CORE = 3

                integration: "Config.Ingestion.IngestionRule.IntegrationSelector.Integration" = proto.Field(
                    proto.ENUM,
                    number=1,
                    enum="Config.Ingestion.IngestionRule.IntegrationSelector.Integration",
                )

            class LineageEnablement(proto.Message):
                r"""Lineage enablement configuration. Defines configurations for
                the ingestion of lineage for the resource and its children.


                .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

                Attributes:
                    enabled (bool):
                        Optional. If true, ingestion of lineage
                        should be enabled. If false, it should be
                        disabled. If unspecified, the system default
                        value is used.

                        This field is a member of `oneof`_ ``_enabled``.
                """

                enabled: bool = proto.Field(
                    proto.BOOL,
                    number=1,
                    optional=True,
                )

            integration_selector: "Config.Ingestion.IngestionRule.IntegrationSelector" = proto.Field(
                proto.MESSAGE,
                number=1,
                message="Config.Ingestion.IngestionRule.IntegrationSelector",
            )
            lineage_enablement: "Config.Ingestion.IngestionRule.LineageEnablement" = (
                proto.Field(
                    proto.MESSAGE,
                    number=3,
                    message="Config.Ingestion.IngestionRule.LineageEnablement",
                )
            )

        rules: MutableSequence["Config.Ingestion.IngestionRule"] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="Config.Ingestion.IngestionRule",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ingestion: Ingestion = proto.Field(
        proto.MESSAGE,
        number=2,
        message=Ingestion,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
