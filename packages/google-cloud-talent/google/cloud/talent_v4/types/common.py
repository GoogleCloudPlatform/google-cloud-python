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
import google.protobuf.wrappers_pb2 as wrappers_pb2  # type: ignore
import google.type.latlng_pb2 as latlng_pb2  # type: ignore
import google.type.money_pb2 as money_pb2  # type: ignore
import google.type.postal_address_pb2 as postal_address_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.talent.v4",
    manifest={
        "CompanySize",
        "JobBenefit",
        "DegreeType",
        "EmploymentType",
        "JobLevel",
        "JobCategory",
        "PostingRegion",
        "Visibility",
        "HtmlSanitization",
        "CommuteMethod",
        "TimestampRange",
        "Location",
        "RequestMetadata",
        "ResponseMetadata",
        "DeviceInfo",
        "CustomAttribute",
        "SpellingCorrection",
        "CompensationInfo",
        "BatchOperationMetadata",
    },
)


class CompanySize(proto.Enum):
    r"""An enum that represents the size of the company.

    Values:
        COMPANY_SIZE_UNSPECIFIED (0):
            Default value if the size isn't specified.
        MINI (1):
            The company has less than 50 employees.
        SMALL (2):
            The company has between 50 and 99 employees.
        SMEDIUM (3):
            The company has between 100 and 499
            employees.
        MEDIUM (4):
            The company has between 500 and 999
            employees.
        BIG (5):
            The company has between 1,000 and 4,999
            employees.
        BIGGER (6):
            The company has between 5,000 and 9,999
            employees.
        GIANT (7):
            The company has 10,000 or more employees.
    """

    COMPANY_SIZE_UNSPECIFIED = 0
    MINI = 1
    SMALL = 2
    SMEDIUM = 3
    MEDIUM = 4
    BIG = 5
    BIGGER = 6
    GIANT = 7


class JobBenefit(proto.Enum):
    r"""An enum that represents employee benefits included with the
    job.

    Values:
        JOB_BENEFIT_UNSPECIFIED (0):
            Default value if the type isn't specified.
        CHILD_CARE (1):
            The job includes access to programs that
            support child care, such as daycare.
        DENTAL (2):
            The job includes dental services covered by a
            dental insurance plan.
        DOMESTIC_PARTNER (3):
            The job offers specific benefits to domestic
            partners.
        FLEXIBLE_HOURS (4):
            The job allows for a flexible work schedule.
        MEDICAL (5):
            The job includes health services covered by a
            medical insurance plan.
        LIFE_INSURANCE (6):
            The job includes a life insurance plan
            provided by the employer or available for
            purchase by the employee.
        PARENTAL_LEAVE (7):
            The job allows for a leave of absence to a
            parent to care for a newborn child.
        RETIREMENT_PLAN (8):
            The job includes a workplace retirement plan
            provided by the employer or available for
            purchase by the employee.
        SICK_DAYS (9):
            The job allows for paid time off due to
            illness.
        VACATION (10):
            The job includes paid time off for vacation.
        VISION (11):
            The job includes vision services covered by a
            vision insurance plan.
    """

    JOB_BENEFIT_UNSPECIFIED = 0
    CHILD_CARE = 1
    DENTAL = 2
    DOMESTIC_PARTNER = 3
    FLEXIBLE_HOURS = 4
    MEDICAL = 5
    LIFE_INSURANCE = 6
    PARENTAL_LEAVE = 7
    RETIREMENT_PLAN = 8
    SICK_DAYS = 9
    VACATION = 10
    VISION = 11


class DegreeType(proto.Enum):
    r"""Educational degree level defined in International Standard
    Classification of Education (ISCED).

    Values:
        DEGREE_TYPE_UNSPECIFIED (0):
            Default value. Represents no degree, or early
            childhood education. Maps to ISCED code 0.
            Ex) Kindergarten
        PRIMARY_EDUCATION (1):
            Primary education which is typically the
            first stage of compulsory education. ISCED code
            1. Ex) Elementary school
        LOWER_SECONDARY_EDUCATION (2):
            Lower secondary education; First stage of
            secondary education building on primary
            education, typically with a more
            subject-oriented curriculum. ISCED code 2.
            Ex) Middle school
        UPPER_SECONDARY_EDUCATION (3):
            Middle education; Second/final stage of
            secondary education preparing for tertiary
            education and/or providing skills relevant to
            employment. Usually with an increased range of
            subject options and streams. ISCED code 3.
            Ex) High school
        ADULT_REMEDIAL_EDUCATION (4):
            Adult Remedial Education; Programmes
            providing learning experiences that build on
            secondary education and prepare for labour
            market entry and/or tertiary education. The
            content is broader than secondary but not as
            complex as tertiary education. ISCED code 4.
        ASSOCIATES_OR_EQUIVALENT (5):
            Associate's or equivalent; Short first
            tertiary programmes that are typically
            practically-based, occupationally-specific and
            prepare for labour market entry. These
            programmes may also provide a pathway to other
            tertiary programmes. ISCED code 5.
        BACHELORS_OR_EQUIVALENT (6):
            Bachelor's or equivalent; Programmes designed
            to provide intermediate academic and/or
            professional knowledge, skills and competencies
            leading to a first tertiary degree or equivalent
            qualification. ISCED code 6.
        MASTERS_OR_EQUIVALENT (7):
            Master's or equivalent; Programmes designed
            to provide advanced academic and/or professional
            knowledge, skills and competencies leading to a
            second tertiary degree or equivalent
            qualification. ISCED code 7.
        DOCTORAL_OR_EQUIVALENT (8):
            Doctoral or equivalent; Programmes designed
            primarily to lead to an advanced research
            qualification, usually concluding with the
            submission and defense of a substantive
            dissertation of publishable quality based on
            original research. ISCED code 8.
    """

    DEGREE_TYPE_UNSPECIFIED = 0
    PRIMARY_EDUCATION = 1
    LOWER_SECONDARY_EDUCATION = 2
    UPPER_SECONDARY_EDUCATION = 3
    ADULT_REMEDIAL_EDUCATION = 4
    ASSOCIATES_OR_EQUIVALENT = 5
    BACHELORS_OR_EQUIVALENT = 6
    MASTERS_OR_EQUIVALENT = 7
    DOCTORAL_OR_EQUIVALENT = 8


class EmploymentType(proto.Enum):
    r"""An enum that represents the employment type of a job.

    Values:
        EMPLOYMENT_TYPE_UNSPECIFIED (0):
            The default value if the employment type
            isn't specified.
        FULL_TIME (1):
            The job requires working a number of hours
            that constitute full time employment, typically
            40 or more hours per week.
        PART_TIME (2):
            The job entails working fewer hours than a
            full time job, typically less than 40 hours a
            week.
        CONTRACTOR (3):
            The job is offered as a contracted, as
            opposed to a salaried employee, position.
        CONTRACT_TO_HIRE (4):
            The job is offered as a contracted position with the
            understanding that it's converted into a full-time position
            at the end of the contract. Jobs of this type are also
            returned by a search for
            [EmploymentType.CONTRACTOR][google.cloud.talent.v4.EmploymentType.CONTRACTOR]
            jobs.
        TEMPORARY (5):
            The job is offered as a temporary employment
            opportunity, usually a short-term engagement.
        INTERN (6):
            The job is a fixed-term opportunity for
            students or entry-level job seekers to obtain
            on-the-job training, typically offered as a
            summer position.
        VOLUNTEER (7):
            The is an opportunity for an individual to
            volunteer, where there's no expectation of
            compensation for the provided services.
        PER_DIEM (8):
            The job requires an employee to work on an
            as-needed basis with a flexible schedule.
        FLY_IN_FLY_OUT (9):
            The job involves employing people in remote
            areas and flying them temporarily to the work
            site instead of relocating employees and their
            families permanently.
        OTHER_EMPLOYMENT_TYPE (10):
            The job does not fit any of the other listed
            types.
    """

    EMPLOYMENT_TYPE_UNSPECIFIED = 0
    FULL_TIME = 1
    PART_TIME = 2
    CONTRACTOR = 3
    CONTRACT_TO_HIRE = 4
    TEMPORARY = 5
    INTERN = 6
    VOLUNTEER = 7
    PER_DIEM = 8
    FLY_IN_FLY_OUT = 9
    OTHER_EMPLOYMENT_TYPE = 10


class JobLevel(proto.Enum):
    r"""An enum that represents the required experience level
    required for the job.

    Values:
        JOB_LEVEL_UNSPECIFIED (0):
            The default value if the level isn't
            specified.
        ENTRY_LEVEL (1):
            Entry-level individual contributors,
            typically with less than 2 years of experience
            in a similar role. Includes interns.
        EXPERIENCED (2):
            Experienced individual contributors,
            typically with 2+ years of experience in a
            similar role.
        MANAGER (3):
            Entry- to mid-level managers responsible for
            managing a team of people.
        DIRECTOR (4):
            Senior-level managers responsible for
            managing teams of managers.
        EXECUTIVE (5):
            Executive-level managers and above, including
            C-level positions.
    """

    JOB_LEVEL_UNSPECIFIED = 0
    ENTRY_LEVEL = 1
    EXPERIENCED = 2
    MANAGER = 3
    DIRECTOR = 4
    EXECUTIVE = 5


class JobCategory(proto.Enum):
    r"""An enum that represents the categorization or primary focus
    of specific role. This value is different than the "industry"
    associated with a role, which is related to the categorization
    of the company listing the job.

    Values:
        JOB_CATEGORY_UNSPECIFIED (0):
            The default value if the category isn't
            specified.
        ACCOUNTING_AND_FINANCE (1):
            An accounting and finance job, such as an
            Accountant.
        ADMINISTRATIVE_AND_OFFICE (2):
            An administrative and office job, such as an
            Administrative Assistant.
        ADVERTISING_AND_MARKETING (3):
            An advertising and marketing job, such as
            Marketing Manager.
        ANIMAL_CARE (4):
            An animal care job, such as Veterinarian.
        ART_FASHION_AND_DESIGN (5):
            An art, fashion, or design job, such as
            Designer.
        BUSINESS_OPERATIONS (6):
            A business operations job, such as Business
            Operations Manager.
        CLEANING_AND_FACILITIES (7):
            A cleaning and facilities job, such as
            Custodial Staff.
        COMPUTER_AND_IT (8):
            A computer and IT job, such as Systems
            Administrator.
        CONSTRUCTION (9):
            A construction job, such as General Laborer.
        CUSTOMER_SERVICE (10):
            A customer service job, such s Cashier.
        EDUCATION (11):
            An education job, such as School Teacher.
        ENTERTAINMENT_AND_TRAVEL (12):
            An entertainment and travel job, such as
            Flight Attendant.
        FARMING_AND_OUTDOORS (13):
            A farming or outdoor job, such as Park
            Ranger.
        HEALTHCARE (14):
            A healthcare job, such as Registered Nurse.
        HUMAN_RESOURCES (15):
            A human resources job, such as Human
            Resources Director.
        INSTALLATION_MAINTENANCE_AND_REPAIR (16):
            An installation, maintenance, or repair job,
            such as Electrician.
        LEGAL (17):
            A legal job, such as Law Clerk.
        MANAGEMENT (18):
            A management job, often used in conjunction
            with another category, such as Store Manager.
        MANUFACTURING_AND_WAREHOUSE (19):
            A manufacturing or warehouse job, such as
            Assembly Technician.
        MEDIA_COMMUNICATIONS_AND_WRITING (20):
            A media, communications, or writing job, such
            as Media Relations.
        OIL_GAS_AND_MINING (21):
            An oil, gas or mining job, such as Offshore
            Driller.
        PERSONAL_CARE_AND_SERVICES (22):
            A personal care and services job, such as
            Hair Stylist.
        PROTECTIVE_SERVICES (23):
            A protective services job, such as Security
            Guard.
        REAL_ESTATE (24):
            A real estate job, such as Buyer's Agent.
        RESTAURANT_AND_HOSPITALITY (25):
            A restaurant and hospitality job, such as
            Restaurant Server.
        SALES_AND_RETAIL (26):
            A sales and/or retail job, such Sales
            Associate.
        SCIENCE_AND_ENGINEERING (27):
            A science and engineering job, such as Lab
            Technician.
        SOCIAL_SERVICES_AND_NON_PROFIT (28):
            A social services or non-profit job, such as
            Case Worker.
        SPORTS_FITNESS_AND_RECREATION (29):
            A sports, fitness, or recreation job, such as
            Personal Trainer.
        TRANSPORTATION_AND_LOGISTICS (30):
            A transportation or logistics job, such as
            Truck Driver.
    """

    JOB_CATEGORY_UNSPECIFIED = 0
    ACCOUNTING_AND_FINANCE = 1
    ADMINISTRATIVE_AND_OFFICE = 2
    ADVERTISING_AND_MARKETING = 3
    ANIMAL_CARE = 4
    ART_FASHION_AND_DESIGN = 5
    BUSINESS_OPERATIONS = 6
    CLEANING_AND_FACILITIES = 7
    COMPUTER_AND_IT = 8
    CONSTRUCTION = 9
    CUSTOMER_SERVICE = 10
    EDUCATION = 11
    ENTERTAINMENT_AND_TRAVEL = 12
    FARMING_AND_OUTDOORS = 13
    HEALTHCARE = 14
    HUMAN_RESOURCES = 15
    INSTALLATION_MAINTENANCE_AND_REPAIR = 16
    LEGAL = 17
    MANAGEMENT = 18
    MANUFACTURING_AND_WAREHOUSE = 19
    MEDIA_COMMUNICATIONS_AND_WRITING = 20
    OIL_GAS_AND_MINING = 21
    PERSONAL_CARE_AND_SERVICES = 22
    PROTECTIVE_SERVICES = 23
    REAL_ESTATE = 24
    RESTAURANT_AND_HOSPITALITY = 25
    SALES_AND_RETAIL = 26
    SCIENCE_AND_ENGINEERING = 27
    SOCIAL_SERVICES_AND_NON_PROFIT = 28
    SPORTS_FITNESS_AND_RECREATION = 29
    TRANSPORTATION_AND_LOGISTICS = 30


class PostingRegion(proto.Enum):
    r"""An enum that represents the job posting region. In most
    cases, job postings don't need to specify a region. If a region
    is given, jobs are eligible for searches in the specified
    region.

    Values:
        POSTING_REGION_UNSPECIFIED (0):
            If the region is unspecified, the job is only returned if it
            matches the
            [LocationFilter][google.cloud.talent.v4.LocationFilter].
        ADMINISTRATIVE_AREA (1):
            In addition to exact location matching, job posting is
            returned when the
            [LocationFilter][google.cloud.talent.v4.LocationFilter] in
            the search query is in the same administrative area as the
            returned job posting. For example, if a
            ``ADMINISTRATIVE_AREA`` job is posted in "CA, USA", it's
            returned if
            [LocationFilter][google.cloud.talent.v4.LocationFilter] has
            "Mountain View".

            Administrative area refers to top-level administrative
            subdivision of this country. For example, US state, IT
            region, UK constituent nation and JP prefecture.
        NATION (2):
            In addition to exact location matching, job is returned when
            [LocationFilter][google.cloud.talent.v4.LocationFilter] in
            search query is in the same country as this job. For
            example, if a ``NATION_WIDE`` job is posted in "USA", it's
            returned if
            [LocationFilter][google.cloud.talent.v4.LocationFilter] has
            'Mountain View'.
        TELECOMMUTE (3):
            Job allows employees to work remotely
            (telecommute). If locations are provided with
            this value, the job is considered as having a
            location, but telecommuting is allowed.
    """

    POSTING_REGION_UNSPECIFIED = 0
    ADMINISTRATIVE_AREA = 1
    NATION = 2
    TELECOMMUTE = 3


class Visibility(proto.Enum):
    r"""Deprecated. All resources are only visible to the owner.

    An enum that represents who has view access to the resource.

    Values:
        VISIBILITY_UNSPECIFIED (0):
            Default value.
        ACCOUNT_ONLY (1):
            The resource is only visible to the GCP
            account who owns it.
        SHARED_WITH_GOOGLE (2):
            The resource is visible to the owner and may
            be visible to other applications and processes
            at Google.
        SHARED_WITH_PUBLIC (3):
            The resource is visible to the owner and may
            be visible to all other API clients.
    """

    _pb_options = {"deprecated": True}
    VISIBILITY_UNSPECIFIED = 0
    ACCOUNT_ONLY = 1
    SHARED_WITH_GOOGLE = 2
    SHARED_WITH_PUBLIC = 3


class HtmlSanitization(proto.Enum):
    r"""Option for HTML content sanitization on user input fields,
    for example, job description. By setting this option, user can
    determine whether and how sanitization is performed on these
    fields.

    Values:
        HTML_SANITIZATION_UNSPECIFIED (0):
            Default value.
        HTML_SANITIZATION_DISABLED (1):
            Disables sanitization on HTML input.
        SIMPLE_FORMATTING_ONLY (2):
            Sanitizes HTML input, only accepts bold,
            italic, ordered list, and unordered list markup
            tags.
    """

    HTML_SANITIZATION_UNSPECIFIED = 0
    HTML_SANITIZATION_DISABLED = 1
    SIMPLE_FORMATTING_ONLY = 2


class CommuteMethod(proto.Enum):
    r"""Method for commute. Walking, biking and wheelchair accessible
    transit is still in the Preview stage.

    Values:
        COMMUTE_METHOD_UNSPECIFIED (0):
            Commute method isn't specified.
        DRIVING (1):
            Commute time is calculated based on driving
            time.
        TRANSIT (2):
            Commute time is calculated based on public
            transit including bus, metro, subway, and so on.
        WALKING (3):
            Commute time is calculated based on walking
            time.
        CYCLING (4):
            Commute time is calculated based on biking
            time.
        TRANSIT_ACCESSIBLE (5):
            Commute time is calculated based on public
            transit that is wheelchair accessible.
    """

    COMMUTE_METHOD_UNSPECIFIED = 0
    DRIVING = 1
    TRANSIT = 2
    WALKING = 3
    CYCLING = 4
    TRANSIT_ACCESSIBLE = 5


class TimestampRange(proto.Message):
    r"""Message representing a period of time between two timestamps.

    Attributes:
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Begin of the period (inclusive).
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            End of the period (exclusive).
    """

    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


class Location(proto.Message):
    r"""A resource that represents a location with full geographic
    information.

    Attributes:
        location_type (google.cloud.talent_v4.types.Location.LocationType):
            The type of a location, which corresponds to the address
            lines field of
            [google.type.PostalAddress][google.type.PostalAddress]. For
            example, "Downtown, Atlanta, GA, USA" has a type of
            [LocationType.NEIGHBORHOOD][google.cloud.talent.v4.Location.LocationType.NEIGHBORHOOD],
            and "Kansas City, KS, USA" has a type of
            [LocationType.LOCALITY][google.cloud.talent.v4.Location.LocationType.LOCALITY].
        postal_address (google.type.postal_address_pb2.PostalAddress):
            Postal address of the location that includes
            human readable information, such as postal
            delivery and payments addresses. Given a postal
            address, a postal service can deliver items to a
            premises, P.O. Box, or other delivery location.
        lat_lng (google.type.latlng_pb2.LatLng):
            An object representing a latitude/longitude
            pair.
        radius_miles (float):
            Radius in miles of the job location. This value is derived
            from the location bounding box in which a circle with the
            specified radius centered from
            [google.type.LatLng][google.type.LatLng] covers the area
            associated with the job location. For example, currently,
            "Mountain View, CA, USA" has a radius of 6.17 miles.
    """

    class LocationType(proto.Enum):
        r"""An enum which represents the type of a location.

        Values:
            LOCATION_TYPE_UNSPECIFIED (0):
                Default value if the type isn't specified.
            COUNTRY (1):
                A country level location.
            ADMINISTRATIVE_AREA (2):
                A state or equivalent level location.
            SUB_ADMINISTRATIVE_AREA (3):
                A county or equivalent level location.
            LOCALITY (4):
                A city or equivalent level location.
            POSTAL_CODE (5):
                A postal code level location.
            SUB_LOCALITY (6):
                A sublocality is a subdivision of a locality,
                for example a city borough, ward, or
                arrondissement. Sublocalities are usually
                recognized by a local political authority. For
                example, Manhattan and Brooklyn are recognized
                as boroughs by the City of New York, and are
                therefore modeled as sublocalities.
            SUB_LOCALITY_1 (7):
                A district or equivalent level location.
            SUB_LOCALITY_2 (8):
                A smaller district or equivalent level
                display.
            NEIGHBORHOOD (9):
                A neighborhood level location.
            STREET_ADDRESS (10):
                A street address level location.
        """

        LOCATION_TYPE_UNSPECIFIED = 0
        COUNTRY = 1
        ADMINISTRATIVE_AREA = 2
        SUB_ADMINISTRATIVE_AREA = 3
        LOCALITY = 4
        POSTAL_CODE = 5
        SUB_LOCALITY = 6
        SUB_LOCALITY_1 = 7
        SUB_LOCALITY_2 = 8
        NEIGHBORHOOD = 9
        STREET_ADDRESS = 10

    location_type: LocationType = proto.Field(
        proto.ENUM,
        number=1,
        enum=LocationType,
    )
    postal_address: postal_address_pb2.PostalAddress = proto.Field(
        proto.MESSAGE,
        number=2,
        message=postal_address_pb2.PostalAddress,
    )
    lat_lng: latlng_pb2.LatLng = proto.Field(
        proto.MESSAGE,
        number=3,
        message=latlng_pb2.LatLng,
    )
    radius_miles: float = proto.Field(
        proto.DOUBLE,
        number=4,
    )


class RequestMetadata(proto.Message):
    r"""Meta information related to the job searcher or entity
    conducting the job search. This information is used to improve
    the performance of the service.

    Attributes:
        domain (str):
            Required if
            [allow_missing_ids][google.cloud.talent.v4.RequestMetadata.allow_missing_ids]
            is unset or ``false``.

            The client-defined scope or source of the service call,
            which typically is the domain on which the service has been
            implemented and is currently being run.

            For example, if the service is being run by client Foo,
            Inc., on job board www.foo.com and career site www.bar.com,
            then this field is set to "foo.com" for use on the job
            board, and "bar.com" for use on the career site.

            Note that any improvements to the model for a particular
            tenant site rely on this field being set correctly to a
            unique domain.

            The maximum number of allowed characters is 255.
        session_id (str):
            Required if
            [allow_missing_ids][google.cloud.talent.v4.RequestMetadata.allow_missing_ids]
            is unset or ``false``.

            A unique session identification string. A session is defined
            as the duration of an end user's interaction with the
            service over a certain period. Obfuscate this field for
            privacy concerns before providing it to the service.

            Note that any improvements to the model for a particular
            tenant site rely on this field being set correctly to a
            unique session ID.

            The maximum number of allowed characters is 255.
        user_id (str):
            Required if
            [allow_missing_ids][google.cloud.talent.v4.RequestMetadata.allow_missing_ids]
            is unset or ``false``.

            A unique user identification string, as determined by the
            client. To have the strongest positive impact on search
            quality make sure the client-level is unique. Obfuscate this
            field for privacy concerns before providing it to the
            service.

            Note that any improvements to the model for a particular
            tenant site rely on this field being set correctly to a
            unique user ID.

            The maximum number of allowed characters is 255.
        allow_missing_ids (bool):
            Only set when any of
            [domain][google.cloud.talent.v4.RequestMetadata.domain],
            [session_id][google.cloud.talent.v4.RequestMetadata.session_id]
            and
            [user_id][google.cloud.talent.v4.RequestMetadata.user_id]
            isn't available for some reason. It is highly recommended
            not to set this field and provide accurate
            [domain][google.cloud.talent.v4.RequestMetadata.domain],
            [session_id][google.cloud.talent.v4.RequestMetadata.session_id]
            and
            [user_id][google.cloud.talent.v4.RequestMetadata.user_id]
            for the best service experience.
        device_info (google.cloud.talent_v4.types.DeviceInfo):
            The type of device used by the job seeker at
            the time of the call to the service.
    """

    domain: str = proto.Field(
        proto.STRING,
        number=1,
    )
    session_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    user_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    allow_missing_ids: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    device_info: "DeviceInfo" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="DeviceInfo",
    )


class ResponseMetadata(proto.Message):
    r"""Additional information returned to client, such as debugging
    information.

    Attributes:
        request_id (str):
            A unique id associated with this call.
            This id is logged for tracking purposes.
    """

    request_id: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeviceInfo(proto.Message):
    r"""Device information collected from the job seeker, candidate,
    or other entity conducting the job search. Providing this
    information improves the quality of the search results across
    devices.

    Attributes:
        device_type (google.cloud.talent_v4.types.DeviceInfo.DeviceType):
            Type of the device.
        id (str):
            A device-specific ID. The ID must be a unique
            identifier that distinguishes the device from
            other devices.
    """

    class DeviceType(proto.Enum):
        r"""An enumeration describing an API access portal and exposure
        mechanism.

        Values:
            DEVICE_TYPE_UNSPECIFIED (0):
                The device type isn't specified.
            WEB (1):
                A desktop web browser, such as, Chrome,
                Firefox, Safari, or Internet Explorer)
            MOBILE_WEB (2):
                A mobile device web browser, such as a phone
                or tablet with a Chrome browser.
            ANDROID (3):
                An Android device native application.
            IOS (4):
                An iOS device native application.
            BOT (5):
                A bot, as opposed to a device operated by
                human beings, such as a web crawler.
            OTHER (6):
                Other devices types.
        """

        DEVICE_TYPE_UNSPECIFIED = 0
        WEB = 1
        MOBILE_WEB = 2
        ANDROID = 3
        IOS = 4
        BOT = 5
        OTHER = 6

    device_type: DeviceType = proto.Field(
        proto.ENUM,
        number=1,
        enum=DeviceType,
    )
    id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CustomAttribute(proto.Message):
    r"""Custom attribute values that are either filterable or
    non-filterable.

    Attributes:
        string_values (MutableSequence[str]):
            Exactly one of
            [string_values][google.cloud.talent.v4.CustomAttribute.string_values]
            or
            [long_values][google.cloud.talent.v4.CustomAttribute.long_values]
            must be specified.

            This field is used to perform a string match
            (``CASE_SENSITIVE_MATCH`` or ``CASE_INSENSITIVE_MATCH``)
            search. For filterable ``string_value``\ s, a maximum total
            number of 200 values is allowed, with each ``string_value``
            has a byte size of no more than 500B. For unfilterable
            ``string_values``, the maximum total byte size of
            unfilterable ``string_values`` is 50KB.

            Empty string isn't allowed.
        long_values (MutableSequence[int]):
            Exactly one of
            [string_values][google.cloud.talent.v4.CustomAttribute.string_values]
            or
            [long_values][google.cloud.talent.v4.CustomAttribute.long_values]
            must be specified.

            This field is used to perform number range search. (``EQ``,
            ``GT``, ``GE``, ``LE``, ``LT``) over filterable
            ``long_value``.

            Currently at most 1
            [long_values][google.cloud.talent.v4.CustomAttribute.long_values]
            is supported.
        filterable (bool):
            If the ``filterable`` flag is true, the custom field values
            may be used for custom attribute filters
            [JobQuery.custom_attribute_filter][google.cloud.talent.v4.JobQuery.custom_attribute_filter].
            If false, these values may not be used for custom attribute
            filters.

            Default is false.
        keyword_searchable (bool):
            If the ``keyword_searchable`` flag is true, the keywords in
            custom fields are searchable by keyword match. If false, the
            values are not searchable by keyword match.

            Default is false.
    """

    string_values: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    long_values: MutableSequence[int] = proto.RepeatedField(
        proto.INT64,
        number=2,
    )
    filterable: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    keyword_searchable: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class SpellingCorrection(proto.Message):
    r"""Spell check result.

    Attributes:
        corrected (bool):
            Indicates if the query was corrected by the
            spell checker.
        corrected_text (str):
            Correction output consisting of the corrected
            keyword string.
        corrected_html (str):
            Corrected output with html tags to highlight
            the corrected words. Corrected words are called
            out with the "<b><i>...</i></b>" html tags.

            For example, the user input query is "software
            enginear", where the second word, "enginear," is
            incorrect. It should be "engineer". When
            spelling correction is enabled, this value is
            "software <b><i>engineer</i></b>".
    """

    corrected: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    corrected_text: str = proto.Field(
        proto.STRING,
        number=2,
    )
    corrected_html: str = proto.Field(
        proto.STRING,
        number=3,
    )


class CompensationInfo(proto.Message):
    r"""Job compensation details.

    Attributes:
        entries (MutableSequence[google.cloud.talent_v4.types.CompensationInfo.CompensationEntry]):
            Job compensation information.

            At most one entry can be of type
            [CompensationInfo.CompensationType.BASE][google.cloud.talent.v4.CompensationInfo.CompensationType.BASE],
            which is referred as **base compensation entry** for the
            job.
        annualized_base_compensation_range (google.cloud.talent_v4.types.CompensationInfo.CompensationRange):
            Output only. Annualized base compensation range. Computed as
            base compensation entry's
            [CompensationEntry.amount][google.cloud.talent.v4.CompensationInfo.CompensationEntry.amount]
            times
            [CompensationEntry.expected_units_per_year][google.cloud.talent.v4.CompensationInfo.CompensationEntry.expected_units_per_year].

            See
            [CompensationEntry][google.cloud.talent.v4.CompensationInfo.CompensationEntry]
            for explanation on compensation annualization.
        annualized_total_compensation_range (google.cloud.talent_v4.types.CompensationInfo.CompensationRange):
            Output only. Annualized total compensation range. Computed
            as all compensation entries'
            [CompensationEntry.amount][google.cloud.talent.v4.CompensationInfo.CompensationEntry.amount]
            times
            [CompensationEntry.expected_units_per_year][google.cloud.talent.v4.CompensationInfo.CompensationEntry.expected_units_per_year].

            See
            [CompensationEntry][google.cloud.talent.v4.CompensationInfo.CompensationEntry]
            for explanation on compensation annualization.
    """

    class CompensationType(proto.Enum):
        r"""The type of compensation.

        For compensation amounts specified in non-monetary amounts, describe
        the compensation scheme in the
        [CompensationEntry.description][google.cloud.talent.v4.CompensationInfo.CompensationEntry.description].

        For example, tipping format is described in
        [CompensationEntry.description][google.cloud.talent.v4.CompensationInfo.CompensationEntry.description]
        (for example, "expect 15-20% tips based on customer bill.") and an
        estimate of the tips provided in
        [CompensationEntry.amount][google.cloud.talent.v4.CompensationInfo.CompensationEntry.amount]
        or
        [CompensationEntry.range][google.cloud.talent.v4.CompensationInfo.CompensationEntry.range]
        ($10 per hour).

        For example, equity is described in
        [CompensationEntry.description][google.cloud.talent.v4.CompensationInfo.CompensationEntry.description]
        (for example, "1% - 2% equity vesting over 4 years, 1 year cliff")
        and value estimated in
        [CompensationEntry.amount][google.cloud.talent.v4.CompensationInfo.CompensationEntry.amount]
        or
        [CompensationEntry.range][google.cloud.talent.v4.CompensationInfo.CompensationEntry.range].
        If no value estimate is possible, units are
        [CompensationUnit.COMPENSATION_UNIT_UNSPECIFIED][google.cloud.talent.v4.CompensationInfo.CompensationUnit.COMPENSATION_UNIT_UNSPECIFIED]
        and then further clarified in
        [CompensationEntry.description][google.cloud.talent.v4.CompensationInfo.CompensationEntry.description]
        field.

        Values:
            COMPENSATION_TYPE_UNSPECIFIED (0):
                Default value.
            BASE (1):
                Base compensation: Refers to the fixed amount
                of money paid to an employee by an employer in
                return for work performed. Base compensation
                does not include benefits, bonuses or any other
                potential compensation from an employer.
            BONUS (2):
                Bonus.
            SIGNING_BONUS (3):
                Signing bonus.
            EQUITY (4):
                Equity.
            PROFIT_SHARING (5):
                Profit sharing.
            COMMISSIONS (6):
                Commission.
            TIPS (7):
                Tips.
            OTHER_COMPENSATION_TYPE (8):
                Other compensation type.
        """

        COMPENSATION_TYPE_UNSPECIFIED = 0
        BASE = 1
        BONUS = 2
        SIGNING_BONUS = 3
        EQUITY = 4
        PROFIT_SHARING = 5
        COMMISSIONS = 6
        TIPS = 7
        OTHER_COMPENSATION_TYPE = 8

    class CompensationUnit(proto.Enum):
        r"""Pay frequency.

        Values:
            COMPENSATION_UNIT_UNSPECIFIED (0):
                Default value.
            HOURLY (1):
                Hourly.
            DAILY (2):
                Daily.
            WEEKLY (3):
                Weekly
            MONTHLY (4):
                Monthly.
            YEARLY (5):
                Yearly.
            ONE_TIME (6):
                One time.
            OTHER_COMPENSATION_UNIT (7):
                Other compensation units.
        """

        COMPENSATION_UNIT_UNSPECIFIED = 0
        HOURLY = 1
        DAILY = 2
        WEEKLY = 3
        MONTHLY = 4
        YEARLY = 5
        ONE_TIME = 6
        OTHER_COMPENSATION_UNIT = 7

    class CompensationEntry(proto.Message):
        r"""A compensation entry that represents one component of compensation,
        such as base pay, bonus, or other compensation type.

        Annualization: One compensation entry can be annualized if

        - it contains valid
          [amount][google.cloud.talent.v4.CompensationInfo.CompensationEntry.amount]
          or
          [range][google.cloud.talent.v4.CompensationInfo.CompensationEntry.range].
        - and its
          [expected_units_per_year][google.cloud.talent.v4.CompensationInfo.CompensationEntry.expected_units_per_year]
          is set or can be derived. Its annualized range is determined as
          ([amount][google.cloud.talent.v4.CompensationInfo.CompensationEntry.amount]
          or
          [range][google.cloud.talent.v4.CompensationInfo.CompensationEntry.range])
          times
          [expected_units_per_year][google.cloud.talent.v4.CompensationInfo.CompensationEntry.expected_units_per_year].

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            type_ (google.cloud.talent_v4.types.CompensationInfo.CompensationType):
                Compensation type.

                Default is
                [CompensationType.COMPENSATION_TYPE_UNSPECIFIED][google.cloud.talent.v4.CompensationInfo.CompensationType.COMPENSATION_TYPE_UNSPECIFIED].
            unit (google.cloud.talent_v4.types.CompensationInfo.CompensationUnit):
                Frequency of the specified amount.

                Default is
                [CompensationUnit.COMPENSATION_UNIT_UNSPECIFIED][google.cloud.talent.v4.CompensationInfo.CompensationUnit.COMPENSATION_UNIT_UNSPECIFIED].
            amount (google.type.money_pb2.Money):
                Compensation amount.

                This field is a member of `oneof`_ ``compensation_amount``.
            range_ (google.cloud.talent_v4.types.CompensationInfo.CompensationRange):
                Compensation range.

                This field is a member of `oneof`_ ``compensation_amount``.
            description (str):
                Compensation description.  For example, could
                indicate equity terms or provide additional
                context to an estimated bonus.
            expected_units_per_year (google.protobuf.wrappers_pb2.DoubleValue):
                Expected number of units paid each year. If not specified,
                when
                [Job.employment_types][google.cloud.talent.v4.Job.employment_types]
                is FULLTIME, a default value is inferred based on
                [unit][google.cloud.talent.v4.CompensationInfo.CompensationEntry.unit].
                Default values:

                - HOURLY: 2080
                - DAILY: 260
                - WEEKLY: 52
                - MONTHLY: 12
                - ANNUAL: 1
        """

        type_: "CompensationInfo.CompensationType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="CompensationInfo.CompensationType",
        )
        unit: "CompensationInfo.CompensationUnit" = proto.Field(
            proto.ENUM,
            number=2,
            enum="CompensationInfo.CompensationUnit",
        )
        amount: money_pb2.Money = proto.Field(
            proto.MESSAGE,
            number=3,
            oneof="compensation_amount",
            message=money_pb2.Money,
        )
        range_: "CompensationInfo.CompensationRange" = proto.Field(
            proto.MESSAGE,
            number=4,
            oneof="compensation_amount",
            message="CompensationInfo.CompensationRange",
        )
        description: str = proto.Field(
            proto.STRING,
            number=5,
        )
        expected_units_per_year: wrappers_pb2.DoubleValue = proto.Field(
            proto.MESSAGE,
            number=6,
            message=wrappers_pb2.DoubleValue,
        )

    class CompensationRange(proto.Message):
        r"""Compensation range.

        Attributes:
            max_compensation (google.type.money_pb2.Money):
                The maximum amount of compensation. If left empty, the value
                is set to a maximal compensation value and the currency code
                is set to match the [currency
                code][google.type.Money.currency_code] of min_compensation.
            min_compensation (google.type.money_pb2.Money):
                The minimum amount of compensation. If left empty, the value
                is set to zero and the currency code is set to match the
                [currency code][google.type.Money.currency_code] of
                max_compensation.
        """

        max_compensation: money_pb2.Money = proto.Field(
            proto.MESSAGE,
            number=2,
            message=money_pb2.Money,
        )
        min_compensation: money_pb2.Money = proto.Field(
            proto.MESSAGE,
            number=1,
            message=money_pb2.Money,
        )

    entries: MutableSequence[CompensationEntry] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=CompensationEntry,
    )
    annualized_base_compensation_range: CompensationRange = proto.Field(
        proto.MESSAGE,
        number=2,
        message=CompensationRange,
    )
    annualized_total_compensation_range: CompensationRange = proto.Field(
        proto.MESSAGE,
        number=3,
        message=CompensationRange,
    )


class BatchOperationMetadata(proto.Message):
    r"""Metadata used for long running operations returned by CTS batch
    APIs. It's used to replace
    [google.longrunning.Operation.metadata][google.longrunning.Operation.metadata].

    Attributes:
        state (google.cloud.talent_v4.types.BatchOperationMetadata.State):
            The state of a long running operation.
        state_description (str):
            More detailed information about operation
            state.
        success_count (int):
            Count of successful item(s) inside an
            operation.
        failure_count (int):
            Count of failed item(s) inside an operation.
        total_count (int):
            Count of total item(s) inside an operation.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the batch operation is created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the batch operation status is updated. The
            metadata and the
            [update_time][google.cloud.talent.v4.BatchOperationMetadata.update_time]
            is refreshed every minute otherwise cached data is returned.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the batch operation is finished and
            [google.longrunning.Operation.done][google.longrunning.Operation.done]
            is set to ``true``.
    """

    class State(proto.Enum):
        r"""

        Values:
            STATE_UNSPECIFIED (0):
                Default value.
            INITIALIZING (1):
                The batch operation is being prepared for
                processing.
            PROCESSING (2):
                The batch operation is actively being
                processed.
            SUCCEEDED (3):
                The batch operation is processed, and at
                least one item has been successfully processed.
            FAILED (4):
                The batch operation is done and no item has
                been successfully processed.
            CANCELLING (5):
                The batch operation is in the process of cancelling after
                [google.longrunning.Operations.CancelOperation][google.longrunning.Operations.CancelOperation]
                is called.
            CANCELLED (6):
                The batch operation is done after
                [google.longrunning.Operations.CancelOperation][google.longrunning.Operations.CancelOperation]
                is called. Any items processed before cancelling are
                returned in the response.
        """

        STATE_UNSPECIFIED = 0
        INITIALIZING = 1
        PROCESSING = 2
        SUCCEEDED = 3
        FAILED = 4
        CANCELLING = 5
        CANCELLED = 6

    state: State = proto.Field(
        proto.ENUM,
        number=1,
        enum=State,
    )
    state_description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    success_count: int = proto.Field(
        proto.INT32,
        number=3,
    )
    failure_count: int = proto.Field(
        proto.INT32,
        number=4,
    )
    total_count: int = proto.Field(
        proto.INT32,
        number=5,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
