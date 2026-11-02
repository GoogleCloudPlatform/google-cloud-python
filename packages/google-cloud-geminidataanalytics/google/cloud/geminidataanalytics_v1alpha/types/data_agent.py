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

from google.cloud.geminidataanalytics_v1alpha.types import (
    data_analytics_agent as gcg_data_analytics_agent,
)
from google.cloud.geminidataanalytics_v1alpha.types import datasource

__protobuf__ = proto.module(
    package="google.cloud.geminidataanalytics.v1alpha",
    manifest={
        "DataAgent",
    },
)


class DataAgent(proto.Message):
    r"""Message describing a DataAgent object.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        data_analytics_agent (google.cloud.geminidataanalytics_v1alpha.types.DataAnalyticsAgent):
            Data analytics agent.

            This field is a member of `oneof`_ ``type``.
        name (str):
            Optional. Identifier. The unique resource name of a
            DataAgent. Format:
            ``projects/{project}/locations/{location}/dataAgents/{data_agent_id}``
            ``{data_agent}`` is the resource id and should be 63
            characters or less and must match the format described in
            https://google.aip.dev/122#resource-id-segments

            Example:
            ``projects/1234567890/locations/global/dataAgents/my-agent``.

            It is recommended to skip setting this field during agent
            creation as it will be inferred automatically and
            overwritten with the {parent}/dataAgents/{data_agent_id}.
        display_name (str):
            Optional. User friendly display name.

            - Must be between 1-256 characters.
        description (str):
            Optional. Description of the agent.

            - Must be between 1-1024 characters.
        labels (MutableMapping[str, str]):
            Optional. Labels to help users filter related agents. For
            example, "sales", "business", "etl", and so on. Note labels
            are used only for filtering and not for policies. See the
            `labels
            documentation <https://cloud.google.com/resource-manager/docs/labels-overview>`__
            for more details on label usage.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the data agent was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the data agent was
            last updated.
        delete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] The time the data agent was soft
            deleted.
        purge_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp in UTC of when this data agent is
            considered expired. This is *always* provided on output,
            regardless of what was sent on input.
        kms_key (str):
            Optional. Customer managed encryption key (CMEK) to use for
            encrypting the DataAgent resources. Cloud KMS CryptoKeys
            must reside in the same location as the DataAgent. The
            expected format is
            ``projects/*/locations/*/keyRings/*/cryptoKeys/*``.

            This field is a member of `oneof`_ ``_kms_key``.
        bigquery_agent_analytics_enabled (bool):
            Optional. Controls whether BigQuery Agent Analytics trace
            logging is enabled for the agent.

            BigQuery Agent Analytics is in Preview and is delivered to
            enrolled projects only. In a project that is not enrolled
            this field is accepted and stored, but no trace rows are
            written and no error is returned.

            Trace logging is additionally suppressed for the entire
            turn, without error, when any table in the agent's
            datasource carries row-level security, column-level security
            or policy tags. It is also suppressed when that
            determination cannot be made, for example when the caller
            lacks permission to list a table's row access policies.

            Trace rows are written only when this is ``true`` and
            ``bigquery_agent_analytics_table`` is set. On a BigQuery
            agent, enabling this without a table has no effect: no table
            is created for the agent and no rows are written. On an
            agent whose datasource is not BigQuery, ``CreateDataAgent``
            and ``UpdateDataAgent`` reject setting this field to
            ``true`` or setting ``bigquery_agent_analytics_table`` with
            ``INVALID_ARGUMENT``. See ``bigquery_agent_analytics_table``
            for when this is checked.

            This setting is independent of the project-level BigQuery
            Agent Analytics setting configured through
            ``SetAgentOpsObservability``. An agent does not inherit that
            setting.

            This field is a member of `oneof`_ ``_bigquery_agent_analytics_enabled``.
        bigquery_agent_analytics_table (google.cloud.geminidataanalytics_v1alpha.types.BigQueryTableReference):
            Optional. The BigQuery table that BigQuery Agent Analytics
            trace rows are written to. Has no effect unless
            ``bigquery_agent_analytics_enabled`` is ``true``. The
            Preview enrollment described on that field applies here too.

            The trace table is validated when it is set on
            ``CreateDataAgent``, or when an ``UpdateDataAgent`` call
            writes a table to it. An ``UpdateDataAgent`` call writes a
            field if the field is in ``update_mask`` or, when
            ``update_mask`` is omitted, if the field is present in the
            request, even if its value is unchanged. An update that only
            clears this field is not validated. The following are
            rejected with ``INVALID_ARGUMENT``:

            - The table must belong to the same project as the agent.
            - The agent's datasource must be BigQuery. BigQuery Agent
              Analytics is not supported for Looker, Looker Studio or
              AlloyDB agents.

            On ``CreateDataAgent``, the datasource is validated against
            the agent in the request. On ``UpdateDataAgent``, it is
            validated against the stored agent after applying the update
            whenever the call writes a table to this field or writes
            ``true`` to ``bigquery_agent_analytics_enabled``. For
            example, an ``UpdateDataAgent`` call without ``update_mask``
            that carries an unchanged
            ``bigquery_agent_analytics_enabled = true`` is rejected on
            an agent whose datasource is not BigQuery. An agent that
            carries no datasource is not validated, and an agent
            switched to a non-BigQuery datasource by an update that does
            neither is not re-validated; in the latter case no trace
            rows are written.

            The destination dataset must already exist and must grant
            write access to the project's Gemini Data Analytics service
            agent, whose address is
            ``service-PROJECT_NUMBER@gcp-sa-geminidataanalytics.iam.gserviceaccount.com``
            (that grant is not performed on your behalf). Without it the
            agent answers normally and no trace rows are written.

            Changing the table on an existing agent affects subsequent
            turns only. Rows already written to the previous table are
            left in place.
    """

    data_analytics_agent: gcg_data_analytics_agent.DataAnalyticsAgent = proto.Field(
        proto.MESSAGE,
        number=101,
        oneof="type",
        message=gcg_data_analytics_agent.DataAnalyticsAgent,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
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
    delete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=12,
        message=timestamp_pb2.Timestamp,
    )
    purge_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=13,
        message=timestamp_pb2.Timestamp,
    )
    kms_key: str = proto.Field(
        proto.STRING,
        number=14,
        optional=True,
    )
    bigquery_agent_analytics_enabled: bool = proto.Field(
        proto.BOOL,
        number=18,
        optional=True,
    )
    bigquery_agent_analytics_table: datasource.BigQueryTableReference = proto.Field(
        proto.MESSAGE,
        number=19,
        message=datasource.BigQueryTableReference,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
