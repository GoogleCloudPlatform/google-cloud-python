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

from google.ads.admanager_v1.types import team_messages

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "GetTeamRequest",
        "ListTeamsRequest",
        "ListTeamsResponse",
        "CreateTeamRequest",
        "BatchCreateTeamsRequest",
        "BatchCreateTeamsResponse",
        "UpdateTeamRequest",
        "BatchUpdateTeamsRequest",
        "BatchUpdateTeamsResponse",
        "BatchActivateTeamsRequest",
        "BatchActivateTeamsResponse",
        "BatchDeactivateTeamsRequest",
        "BatchDeactivateTeamsResponse",
    },
)


class GetTeamRequest(proto.Message):
    r"""Request object for ``GetTeam`` method.

    Attributes:
        name (str):
            Required. The resource name of the Team. Format:
            ``networks/{network_code}/teams/{team_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListTeamsRequest(proto.Message):
    r"""Request object for ``ListTeams`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of Teams.
            Format: ``networks/{network_code}``
        page_size (int):
            Optional. The maximum number of ``Teams`` to return. The
            service may return fewer than this value. If unspecified, at
            most 50 ``Teams`` will be returned. The maximum value is
            1000; values greater than 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListTeams`` call. Provide this to retrieve the subsequent
            page.

            When paginating, all other parameters provided to
            ``ListTeams`` must match the call that provided the page
            token.
        filter (str):
            Optional. Expression to filter the response. See syntax
            details at
            https://developers.google.com/ad-manager/api/beta/filters

            **Filterable fields:**

            - ``accessType``
            - ``allCompaniesAccess``
            - ``allInventoryAccess``
            - ``description``
            - ``displayName``
            - ``name``
            - ``status``
        order_by (str):
            Optional. Expression to specify sorting
            order. See syntax details at
            https://developers.google.com/ad-manager/api/beta/filters#order
        skip (int):
            Optional. Number of individual resources to
            skip while paginating.
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
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )
    skip: int = proto.Field(
        proto.INT32,
        number=6,
    )


class ListTeamsResponse(proto.Message):
    r"""Response object for ``ListTeamsRequest`` containing matching
    ``Team`` objects.

    Attributes:
        teams (MutableSequence[google.ads.admanager_v1.types.Team]):
            The ``Team`` objects from the specified network.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        total_size (int):
            Total number of ``Team`` objects. If a filter was included
            in the request, this reflects the total number after the
            filtering is applied.

            ``total_size`` won't be calculated in the response unless it
            has been included in a response field mask. The response
            field mask can be provided to the method by using the URL
            parameter ``$fields`` or ``fields``, or by using the
            HTTP/gRPC header ``X-Goog-FieldMask``.

            For more information, see
            https://developers.google.com/ad-manager/api/beta/field-masks
    """

    @property
    def raw_page(self):
        return self

    teams: MutableSequence[team_messages.Team] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=team_messages.Team,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class CreateTeamRequest(proto.Message):
    r"""Request object for ``CreateTeam`` method.

    Attributes:
        parent (str):
            Required. The parent resource where this ``Team`` will be
            created. Format: ``networks/{network_code}``
        team (google.ads.admanager_v1.types.Team):
            Required. The ``Team`` to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    team: team_messages.Team = proto.Field(
        proto.MESSAGE,
        number=2,
        message=team_messages.Team,
    )


class BatchCreateTeamsRequest(proto.Message):
    r"""Request object for ``BatchCreateTeams`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``Teams`` will be
            created. Format: ``networks/{network_code}`` The parent
            field in the CreateTeamRequest must match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.CreateTeamRequest]):
            Required. The ``Team`` objects to create. A maximum of 100
            objects can be created in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreateTeamRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CreateTeamRequest",
    )


class BatchCreateTeamsResponse(proto.Message):
    r"""Response object for ``BatchCreateTeams`` method.

    Attributes:
        teams (MutableSequence[google.ads.admanager_v1.types.Team]):
            The ``Team`` objects created.
    """

    teams: MutableSequence[team_messages.Team] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=team_messages.Team,
    )


class UpdateTeamRequest(proto.Message):
    r"""Request object for ``UpdateTeam`` method.

    Attributes:
        team (google.ads.admanager_v1.types.Team):
            Required. The ``Team`` to update.

            The ``Team``'s ``name`` is used to identify the ``Team`` to
            update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    team: team_messages.Team = proto.Field(
        proto.MESSAGE,
        number=1,
        message=team_messages.Team,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class BatchUpdateTeamsRequest(proto.Message):
    r"""Request object for ``BatchUpdateTeams`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``Teams`` will be
            updated. Format: ``networks/{network_code}`` The parent
            field in the UpdateTeamRequest must match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.UpdateTeamRequest]):
            Required. The ``Team`` objects to update. A maximum of 100
            objects can be updated in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["UpdateTeamRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="UpdateTeamRequest",
    )


class BatchUpdateTeamsResponse(proto.Message):
    r"""Response object for ``BatchUpdateTeams`` method.

    Attributes:
        teams (MutableSequence[google.ads.admanager_v1.types.Team]):
            The ``Team`` objects updated.
    """

    teams: MutableSequence[team_messages.Team] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=team_messages.Team,
    )


class BatchActivateTeamsRequest(proto.Message):
    r"""Request message for ``BatchActivateTeams`` method.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the ``Team``\ s to activate.
            Format: ``networks/{network_code}/teams/{team_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchActivateTeamsResponse(proto.Message):
    r"""Response object for ``BatchActivateTeams`` method."""


class BatchDeactivateTeamsRequest(proto.Message):
    r"""Request message for ``BatchDeactivateTeams`` method.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the ``Team``\ s to
            deactivate. Format:
            ``networks/{network_code}/teams/{team_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchDeactivateTeamsResponse(proto.Message):
    r"""Response object for ``BatchDeactivateTeams`` method."""


__all__ = tuple(sorted(__protobuf__.manifest))
