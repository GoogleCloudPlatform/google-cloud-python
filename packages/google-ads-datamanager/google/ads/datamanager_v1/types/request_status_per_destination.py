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

from google.ads.datamanager_v1.types import destination as gad_destination
from google.ads.datamanager_v1.types import match_rate, processing_errors

__protobuf__ = proto.module(
    package="google.ads.datamanager.v1",
    manifest={
        "RequestStatusPerDestination",
    },
)


class RequestStatusPerDestination(proto.Message):
    r"""A request status per destination.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        destination (google.ads.datamanager_v1.types.Destination):
            A destination within a DM API request.
        request_status (google.ads.datamanager_v1.types.RequestStatusPerDestination.RequestStatus):
            The request status of the destination.
        error_info (google.ads.datamanager_v1.types.ErrorInfo):
            An error info error containing the error reason and error
            counts related to the upload. Only populated if the
            [``request_status``][google.ads.datamanager.v1.RequestStatusPerDestination.request_status]
            is
            [``FAILED``][google.ads.datamanager.v1.RequestStatusPerDestination.RequestStatus.FAILED]
            or
            [``PARTIAL_SUCCESS``][google.ads.datamanager.v1.RequestStatusPerDestination.RequestStatus.PARTIAL_SUCCESS].
            This field isn't populated while the request has
            [``request_status``][google.ads.datamanager.v1.RequestStatusPerDestination.request_status]
            of
            [``PROCESSING``][google.ads.datamanager.v1.RequestStatusPerDestination.RequestStatus.PROCESSING].
        warning_info (google.ads.datamanager_v1.types.WarningInfo):
            A warning info containing the warning reason and warning
            counts related to the upload. This field isn't populated
            while the request has
            [``request_status``][google.ads.datamanager.v1.RequestStatusPerDestination.request_status]
            of
            [``PROCESSING``][google.ads.datamanager.v1.RequestStatusPerDestination.RequestStatus.PROCESSING].
        audience_members_ingestion_status (google.ads.datamanager_v1.types.RequestStatusPerDestination.IngestAudienceMembersStatus):
            The status of the ingest audience members
            request.

            This field is a member of `oneof`_ ``status``.
        events_ingestion_status (google.ads.datamanager_v1.types.RequestStatusPerDestination.IngestEventsStatus):
            The status of the ingest events request.

            This field is a member of `oneof`_ ``status``.
        audience_members_removal_status (google.ads.datamanager_v1.types.RequestStatusPerDestination.RemoveAudienceMembersStatus):
            The status of the remove audience members
            request.

            This field is a member of `oneof`_ ``status``.
        remove_all_audience_members_status (google.ads.datamanager_v1.types.RequestStatusPerDestination.RemoveAllAudienceMembersStatus):
            The status of the remove all audience members
            request.

            This field is a member of `oneof`_ ``status``.
    """

    class RequestStatus(proto.Enum):
        r"""The request status.

        Values:
            REQUEST_STATUS_UNKNOWN (0):
                The request status is unknown.
            SUCCESS (1):
                Processing succeeded for all records without any errors.
                However, there may be warnings in the
                [``warning_info``][google.ads.datamanager.v1.RequestStatusPerDestination.warning_info]
                field.
            PROCESSING (2):
                The request is processing.
            FAILED (3):
                Processing failed for all records. Check the
                [``error_info``][google.ads.datamanager.v1.RequestStatusPerDestination.error_info]
                field for error details, and check the
                [``warning_info``][google.ads.datamanager.v1.RequestStatusPerDestination.warning_info]
                field for warning details.
            PARTIAL_SUCCESS (4):
                Processing completed successfully without errors for some
                records, but failed with errors for other records. Check the
                [``error_info``][google.ads.datamanager.v1.RequestStatusPerDestination.error_info]
                field for error details, and check the
                [``warning_info``][google.ads.datamanager.v1.RequestStatusPerDestination.warning_info]
                field for warning details.
        """

        REQUEST_STATUS_UNKNOWN = 0
        SUCCESS = 1
        PROCESSING = 2
        FAILED = 3
        PARTIAL_SUCCESS = 4

    class DataType(proto.Enum):
        r"""The type of data.

        Values:
            DATA_TYPE_UNSPECIFIED (0):
                The data type is unspecified.
            EMAIL (1):
                The data is an email address.
            PHONE_NUMBER (2):
                The data is a phone number.
            ADDRESS (3):
                The data is a physical address.
            IP_ADDRESS (4):
                The data is an IP address.
        """

        DATA_TYPE_UNSPECIFIED = 0
        EMAIL = 1
        PHONE_NUMBER = 2
        ADDRESS = 3
        IP_ADDRESS = 4

    class IngestAudienceMembersStatus(proto.Message):
        r"""The status of the ingest audience members request.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            user_data_ingestion_status (google.ads.datamanager_v1.types.RequestStatusPerDestination.IngestUserDataStatus):
                The status of the user data ingestion to the
                destination.

                This field is a member of `oneof`_ ``status``.
            mobile_data_ingestion_status (google.ads.datamanager_v1.types.RequestStatusPerDestination.IngestMobileDataStatus):
                The status of the mobile data ingestion to
                the destination.

                This field is a member of `oneof`_ ``status``.
            pair_data_ingestion_status (google.ads.datamanager_v1.types.RequestStatusPerDestination.IngestPairDataStatus):
                The status of the pair data ingestion to the
                destination.

                This field is a member of `oneof`_ ``status``.
            user_id_data_ingestion_status (google.ads.datamanager_v1.types.RequestStatusPerDestination.IngestUserIdDataStatus):
                The status of the user id data ingestion to
                the destination.

                This field is a member of `oneof`_ ``status``.
            ppid_data_ingestion_status (google.ads.datamanager_v1.types.RequestStatusPerDestination.IngestPpidDataStatus):
                The status of the ppid data ingestion to the
                destination.

                This field is a member of `oneof`_ ``status``.
            composite_data_ingestion_status (google.ads.datamanager_v1.types.RequestStatusPerDestination.IngestCompositeDataStatus):
                The status of the composite data ingestion to
                the destination.

                This field is a member of `oneof`_ ``status``.
            google_user_id_data_ingestion_status (google.ads.datamanager_v1.types.RequestStatusPerDestination.IngestGoogleUserIdDataStatus):
                The status of the google user id data
                ingestion to the destination.

                This field is a member of `oneof`_ ``status``.
            partner_provided_id_data_ingestion_status (google.ads.datamanager_v1.types.RequestStatusPerDestination.IngestPartnerProvidedIdDataStatus):
                The status of the partner provided id data
                ingestion to the destination.

                This field is a member of `oneof`_ ``status``.
        """

        user_data_ingestion_status: "RequestStatusPerDestination.IngestUserDataStatus" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="status",
            message="RequestStatusPerDestination.IngestUserDataStatus",
        )
        mobile_data_ingestion_status: "RequestStatusPerDestination.IngestMobileDataStatus" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="status",
            message="RequestStatusPerDestination.IngestMobileDataStatus",
        )
        pair_data_ingestion_status: "RequestStatusPerDestination.IngestPairDataStatus" = proto.Field(
            proto.MESSAGE,
            number=3,
            oneof="status",
            message="RequestStatusPerDestination.IngestPairDataStatus",
        )
        user_id_data_ingestion_status: "RequestStatusPerDestination.IngestUserIdDataStatus" = proto.Field(
            proto.MESSAGE,
            number=4,
            oneof="status",
            message="RequestStatusPerDestination.IngestUserIdDataStatus",
        )
        ppid_data_ingestion_status: "RequestStatusPerDestination.IngestPpidDataStatus" = proto.Field(
            proto.MESSAGE,
            number=5,
            oneof="status",
            message="RequestStatusPerDestination.IngestPpidDataStatus",
        )
        composite_data_ingestion_status: "RequestStatusPerDestination.IngestCompositeDataStatus" = proto.Field(
            proto.MESSAGE,
            number=6,
            oneof="status",
            message="RequestStatusPerDestination.IngestCompositeDataStatus",
        )
        google_user_id_data_ingestion_status: "RequestStatusPerDestination.IngestGoogleUserIdDataStatus" = proto.Field(
            proto.MESSAGE,
            number=7,
            oneof="status",
            message="RequestStatusPerDestination.IngestGoogleUserIdDataStatus",
        )
        partner_provided_id_data_ingestion_status: "RequestStatusPerDestination.IngestPartnerProvidedIdDataStatus" = proto.Field(
            proto.MESSAGE,
            number=8,
            oneof="status",
            message="RequestStatusPerDestination.IngestPartnerProvidedIdDataStatus",
        )

    class RemoveAudienceMembersStatus(proto.Message):
        r"""The status of the remove audience members request.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            user_data_removal_status (google.ads.datamanager_v1.types.RequestStatusPerDestination.RemoveUserDataStatus):
                The status of the user data removal from the
                destination.

                This field is a member of `oneof`_ ``status``.
            mobile_data_removal_status (google.ads.datamanager_v1.types.RequestStatusPerDestination.RemoveMobileDataStatus):
                The status of the mobile data removal from
                the destination.

                This field is a member of `oneof`_ ``status``.
            pair_data_removal_status (google.ads.datamanager_v1.types.RequestStatusPerDestination.RemovePairDataStatus):
                The status of the pair data removal from the
                destination.

                This field is a member of `oneof`_ ``status``.
            user_id_data_removal_status (google.ads.datamanager_v1.types.RequestStatusPerDestination.RemoveUserIdDataStatus):
                The status of the user id data removal from
                the destination.

                This field is a member of `oneof`_ ``status``.
            ppid_data_removal_status (google.ads.datamanager_v1.types.RequestStatusPerDestination.RemovePpidDataStatus):
                The status of the ppid data removal from the
                destination.

                This field is a member of `oneof`_ ``status``.
            composite_data_removal_status (google.ads.datamanager_v1.types.RequestStatusPerDestination.RemoveCompositeDataStatus):
                The status of the composite data removal from
                the destination.

                This field is a member of `oneof`_ ``status``.
            google_user_id_data_removal_status (google.ads.datamanager_v1.types.RequestStatusPerDestination.RemoveGoogleUserIdDataStatus):
                The status of the google user id data removal
                from the destination.

                This field is a member of `oneof`_ ``status``.
            partner_provided_id_data_removal_status (google.ads.datamanager_v1.types.RequestStatusPerDestination.RemovePartnerProvidedIdDataStatus):
                The status of the partner provided id data
                removal from the destination.

                This field is a member of `oneof`_ ``status``.
        """

        user_data_removal_status: "RequestStatusPerDestination.RemoveUserDataStatus" = (
            proto.Field(
                proto.MESSAGE,
                number=1,
                oneof="status",
                message="RequestStatusPerDestination.RemoveUserDataStatus",
            )
        )
        mobile_data_removal_status: "RequestStatusPerDestination.RemoveMobileDataStatus" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="status",
            message="RequestStatusPerDestination.RemoveMobileDataStatus",
        )
        pair_data_removal_status: "RequestStatusPerDestination.RemovePairDataStatus" = (
            proto.Field(
                proto.MESSAGE,
                number=3,
                oneof="status",
                message="RequestStatusPerDestination.RemovePairDataStatus",
            )
        )
        user_id_data_removal_status: "RequestStatusPerDestination.RemoveUserIdDataStatus" = proto.Field(
            proto.MESSAGE,
            number=4,
            oneof="status",
            message="RequestStatusPerDestination.RemoveUserIdDataStatus",
        )
        ppid_data_removal_status: "RequestStatusPerDestination.RemovePpidDataStatus" = (
            proto.Field(
                proto.MESSAGE,
                number=5,
                oneof="status",
                message="RequestStatusPerDestination.RemovePpidDataStatus",
            )
        )
        composite_data_removal_status: "RequestStatusPerDestination.RemoveCompositeDataStatus" = proto.Field(
            proto.MESSAGE,
            number=6,
            oneof="status",
            message="RequestStatusPerDestination.RemoveCompositeDataStatus",
        )
        google_user_id_data_removal_status: "RequestStatusPerDestination.RemoveGoogleUserIdDataStatus" = proto.Field(
            proto.MESSAGE,
            number=7,
            oneof="status",
            message="RequestStatusPerDestination.RemoveGoogleUserIdDataStatus",
        )
        partner_provided_id_data_removal_status: "RequestStatusPerDestination.RemovePartnerProvidedIdDataStatus" = proto.Field(
            proto.MESSAGE,
            number=8,
            oneof="status",
            message="RequestStatusPerDestination.RemovePartnerProvidedIdDataStatus",
        )

    class RemoveAllAudienceMembersStatus(proto.Message):
        r"""The status of the remove all audience members request."""

    class IngestEventsStatus(proto.Message):
        r"""The status of the events ingestion to the destination.

        Attributes:
            record_count (int):
                The total count of events sent in the upload
                request. Includes all events in the request,
                regardless of whether they were successfully
                ingested or not.
        """

        record_count: int = proto.Field(
            proto.INT64,
            number=1,
        )

    class IngestUserDataStatus(proto.Message):
        r"""The status of the user data ingestion to the destination
        containing stats related to the ingestion.

        Attributes:
            record_count (int):
                The total count of audience members sent in
                the upload request for the destination. Includes
                all audience members in the request, regardless
                of whether they were successfully ingested or
                not.
            user_identifier_count (int):
                The total count of user identifiers sent in
                the upload request for the destination. Includes
                all user identifiers in the request, regardless
                of whether they were successfully ingested or
                not.
            upload_match_rate_range (google.ads.datamanager_v1.types.MatchRateRange):
                The match rate range of the upload.
        """

        record_count: int = proto.Field(
            proto.INT64,
            number=1,
        )
        user_identifier_count: int = proto.Field(
            proto.INT64,
            number=2,
        )
        upload_match_rate_range: match_rate.MatchRateRange = proto.Field(
            proto.ENUM,
            number=3,
            enum=match_rate.MatchRateRange,
        )

    class RemoveUserDataStatus(proto.Message):
        r"""The status of the user data removal from the destination.

        Attributes:
            record_count (int):
                The total count of audience members sent in
                the removal request. Includes all audience
                members in the request, regardless of whether
                they were successfully removed or not.
            user_identifier_count (int):
                The total count of user identifiers sent in
                the removal request. Includes all user
                identifiers in the request, regardless of
                whether they were successfully removed or not.
        """

        record_count: int = proto.Field(
            proto.INT64,
            number=1,
        )
        user_identifier_count: int = proto.Field(
            proto.INT64,
            number=2,
        )

    class IngestMobileDataStatus(proto.Message):
        r"""The status of the mobile data ingestion to the destination
        containing stats related to the ingestion.

        Attributes:
            record_count (int):
                The total count of audience members sent in
                the upload request for the destination. Includes
                all audience members in the request, regardless
                of whether they were successfully ingested or
                not.
            mobile_id_count (int):
                The total count of mobile ids sent in the
                upload request for the destination. Includes all
                mobile ids in the request, regardless of whether
                they were successfully ingested or not.
        """

        record_count: int = proto.Field(
            proto.INT64,
            number=1,
        )
        mobile_id_count: int = proto.Field(
            proto.INT64,
            number=2,
        )

    class RemoveMobileDataStatus(proto.Message):
        r"""The status of the mobile data removal from the destination.

        Attributes:
            record_count (int):
                The total count of audience members sent in
                the removal request. Includes all audience
                members in the request, regardless of whether
                they were successfully removed or not.
            mobile_id_count (int):
                The total count of mobile Ids sent in the
                removal request. Includes all mobile ids in the
                request, regardless of whether they were
                successfully removed or not.
        """

        record_count: int = proto.Field(
            proto.INT64,
            number=1,
        )
        mobile_id_count: int = proto.Field(
            proto.INT64,
            number=2,
        )

    class IngestPairDataStatus(proto.Message):
        r"""The status of the pair data ingestion to the destination
        containing stats related to the ingestion.

        Attributes:
            record_count (int):
                The total count of audience members sent in
                the upload request for the destination. Includes
                all audience members in the request, regardless
                of whether they were successfully ingested or
                not.
            pair_id_count (int):
                The total count of pair ids sent in the
                upload request for the destination. Includes all
                pair ids in the request, regardless of whether
                they were successfully ingested or not.
        """

        record_count: int = proto.Field(
            proto.INT64,
            number=1,
        )
        pair_id_count: int = proto.Field(
            proto.INT64,
            number=2,
        )

    class RemovePairDataStatus(proto.Message):
        r"""The status of the pair data removal from the destination.

        Attributes:
            record_count (int):
                The total count of audience members sent in
                the removal request. Includes all audience
                members in the request, regardless of whether
                they were successfully removed or not.
            pair_id_count (int):
                The total count of pair ids sent in the
                removal request. Includes all pair ids in the
                request, regardless of whether they were
                successfully removed or not.
        """

        record_count: int = proto.Field(
            proto.INT64,
            number=1,
        )
        pair_id_count: int = proto.Field(
            proto.INT64,
            number=2,
        )

    class IngestUserIdDataStatus(proto.Message):
        r"""The status of the user id data ingestion to the destination
        containing stats related to the ingestion.

        Attributes:
            record_count (int):
                The total count of audience members sent in
                the upload request for the destination. Includes
                all audience members in the request, regardless
                of whether they were successfully ingested or
                not.
            user_id_count (int):
                The total count of user ids sent in the
                upload request for the destination. Includes all
                user ids in the request, regardless of whether
                they were successfully ingested or not.
        """

        record_count: int = proto.Field(
            proto.INT64,
            number=1,
        )
        user_id_count: int = proto.Field(
            proto.INT64,
            number=2,
        )

    class RemoveUserIdDataStatus(proto.Message):
        r"""The status of the user id data removal from the destination.

        Attributes:
            record_count (int):
                The total count of audience members sent in
                the removal request. Includes all audience
                members in the request, regardless of whether
                they were successfully removed or not.
            user_id_count (int):
                The total count of user ids sent in the
                removal request. Includes all user ids in the
                request, regardless of whether they were
                successfully removed or not.
        """

        record_count: int = proto.Field(
            proto.INT64,
            number=1,
        )
        user_id_count: int = proto.Field(
            proto.INT64,
            number=2,
        )

    class IngestPpidDataStatus(proto.Message):
        r"""The status of the ppid data ingestion to the destination
        containing stats related to the ingestion.

        Attributes:
            record_count (int):
                The total count of audience members sent in
                the upload request for the destination. Includes
                all audience members in the request, regardless
                of whether they were successfully ingested or
                not.
            ppid_count (int):
                The total count of ppids sent in the upload
                request for the destination. Includes all ppids
                in the request, regardless of whether they were
                successfully ingested or not.
        """

        record_count: int = proto.Field(
            proto.INT64,
            number=1,
        )
        ppid_count: int = proto.Field(
            proto.INT64,
            number=2,
        )

    class RemovePpidDataStatus(proto.Message):
        r"""The status of the ppid data removal from the destination.

        Attributes:
            record_count (int):
                The total count of audience members sent in
                the removal request. Includes all audience
                members in the request, regardless of whether
                they were successfully removed or not.
            ppid_count (int):
                The total count of ppids sent in the removal
                request. Includes all ppids in the request,
                regardless of whether they were successfully
                removed or not.
        """

        record_count: int = proto.Field(
            proto.INT64,
            number=1,
        )
        ppid_count: int = proto.Field(
            proto.INT64,
            number=2,
        )

    class IngestCompositeDataStatus(proto.Message):
        r"""The status of the composite data ingestion to the destination
        containing stats related to the ingestion.

        Attributes:
            record_count (int):
                The total count of audience members sent in
                the upload request for the destination. Includes
                all audience members in the request, regardless
                of whether they were successfully ingested or
                not.
            data_type_counts (MutableSequence[google.ads.datamanager_v1.types.RequestStatusPerDestination.DataTypeCount]):
                The total count of data types sent in the
                upload request for the destination, broken down
                by data type. Includes all data types in the
                request, regardless of whether they were
                successfully ingested or not.
            upload_match_rate_range (google.ads.datamanager_v1.types.MatchRateRange):
                The match rate range of the upload.
        """

        record_count: int = proto.Field(
            proto.INT64,
            number=1,
        )
        data_type_counts: MutableSequence[
            "RequestStatusPerDestination.DataTypeCount"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="RequestStatusPerDestination.DataTypeCount",
        )
        upload_match_rate_range: match_rate.MatchRateRange = proto.Field(
            proto.ENUM,
            number=3,
            enum=match_rate.MatchRateRange,
        )

    class RemoveCompositeDataStatus(proto.Message):
        r"""The status of the composite data removal from the
        destination.

        Attributes:
            record_count (int):
                The total count of audience members sent in
                the removal request. Includes all audience
                members in the request, regardless of whether
                they were successfully removed or not.
            data_type_counts (MutableSequence[google.ads.datamanager_v1.types.RequestStatusPerDestination.DataTypeCount]):
                The total count of data types sent in the
                removal request, broken down by data type.
                Includes all data types in the request,
                regardless of whether they were successfully
                removed or not.
        """

        record_count: int = proto.Field(
            proto.INT64,
            number=1,
        )
        data_type_counts: MutableSequence[
            "RequestStatusPerDestination.DataTypeCount"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="RequestStatusPerDestination.DataTypeCount",
        )

    class IngestGoogleUserIdDataStatus(proto.Message):
        r"""The status of the google user id data ingestion to the
        destination containing stats related to the ingestion.

        Attributes:
            record_count (int):
                The total count of audience members sent in
                the upload request for the destination. Includes
                all audience members in the request, regardless
                of whether they were successfully ingested or
                not.
            google_user_id_count (int):
                The total count of google user ids sent in
                the upload request for the destination. Includes
                all google user ids in the request, regardless
                of whether they were successfully ingested or
                not.
        """

        record_count: int = proto.Field(
            proto.INT64,
            number=1,
        )
        google_user_id_count: int = proto.Field(
            proto.INT64,
            number=2,
        )

    class RemoveGoogleUserIdDataStatus(proto.Message):
        r"""The status of the google user id data removal from the
        destination.

        Attributes:
            record_count (int):
                The total count of audience members sent in
                the removal request. Includes all audience
                members in the request, regardless of whether
                they were successfully removed or not.
            google_user_id_count (int):
                The total count of google user ids sent in
                the removal request. Includes all google user
                ids in the request, regardless of whether they
                were successfully removed or not.
        """

        record_count: int = proto.Field(
            proto.INT64,
            number=1,
        )
        google_user_id_count: int = proto.Field(
            proto.INT64,
            number=2,
        )

    class IngestPartnerProvidedIdDataStatus(proto.Message):
        r"""The status of the partner provided id data ingestion to the
        destination containing stats related to the ingestion.

        Attributes:
            record_count (int):
                The total count of audience members sent in
                the upload request for the destination. Includes
                all audience members in the request, regardless
                of whether they were successfully ingested or
                not.
            partner_provided_id_count (int):
                The total count of partner provided ids sent
                in the upload request for the destination.
                Includes all partner provided ids in the
                request, regardless of whether they were
                successfully ingested or not.
        """

        record_count: int = proto.Field(
            proto.INT64,
            number=1,
        )
        partner_provided_id_count: int = proto.Field(
            proto.INT64,
            number=2,
        )

    class RemovePartnerProvidedIdDataStatus(proto.Message):
        r"""The status of the partner provided id data removal from the
        destination.

        Attributes:
            record_count (int):
                The total count of audience members sent in
                the removal request. Includes all audience
                members in the request, regardless of whether
                they were successfully removed or not.
            partner_provided_id_count (int):
                The total count of partner provided ids sent
                in the removal request. Includes all partner
                provided ids in the request, regardless of
                whether they were successfully removed or not.
        """

        record_count: int = proto.Field(
            proto.INT64,
            number=1,
        )
        partner_provided_id_count: int = proto.Field(
            proto.INT64,
            number=2,
        )

    class DataTypeCount(proto.Message):
        r"""The count for a specific data type.

        Attributes:
            type_ (google.ads.datamanager_v1.types.RequestStatusPerDestination.DataType):
                The type of data.
            count (int):
                The count for this data type.
        """

        type_: "RequestStatusPerDestination.DataType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="RequestStatusPerDestination.DataType",
        )
        count: int = proto.Field(
            proto.INT64,
            number=2,
        )

    destination: gad_destination.Destination = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gad_destination.Destination,
    )
    request_status: RequestStatus = proto.Field(
        proto.ENUM,
        number=2,
        enum=RequestStatus,
    )
    error_info: processing_errors.ErrorInfo = proto.Field(
        proto.MESSAGE,
        number=3,
        message=processing_errors.ErrorInfo,
    )
    warning_info: processing_errors.WarningInfo = proto.Field(
        proto.MESSAGE,
        number=7,
        message=processing_errors.WarningInfo,
    )
    audience_members_ingestion_status: IngestAudienceMembersStatus = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="status",
        message=IngestAudienceMembersStatus,
    )
    events_ingestion_status: IngestEventsStatus = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="status",
        message=IngestEventsStatus,
    )
    audience_members_removal_status: RemoveAudienceMembersStatus = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="status",
        message=RemoveAudienceMembersStatus,
    )
    remove_all_audience_members_status: RemoveAllAudienceMembersStatus = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="status",
        message=RemoveAllAudienceMembersStatus,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
