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

import google.type.postal_address_pb2 as postal_address_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.maps.addressvalidation.v1",
    manifest={
        "Address",
        "AddressComponent",
        "ComponentName",
    },
)


class Address(proto.Message):
    r"""Details of the post-processed address. Post-processing
    includes correcting misspelled parts of the address, replacing
    incorrect parts, and inferring missing parts.

    Attributes:
        formatted_address (str):
            The post-processed address, formatted as a single-line
            address following the address formatting rules of the region
            where the address is located.

            Note: the format of this address may not match the format of
            the address in the ``postal_address`` field. For example,
            the ``postal_address`` always represents the country as a 2
            letter ``region_code``, such as "US" or "NZ". By contrast,
            this field uses a longer form of the country name, such as
            "USA" or "New Zealand".
        postal_address (google.type.postal_address_pb2.PostalAddress):
            The post-processed address represented as a
            postal address.
        address_components (MutableSequence[google.maps.addressvalidation_v1.types.AddressComponent]):
            Unordered list. The individual address
            components of the formatted and corrected
            address, along with validation information. This
            provides information on the validation status of
            the individual components.

            Address components are not ordered in a
            particular way. Do not make any assumptions on
            the ordering of the address components in the
            list.
        missing_component_types (MutableSequence[str]):
            The types of components that were expected to be present in
            a correctly formatted mailing address but were not found in
            the input AND could not be inferred. An example might be
            ``['street_number', 'route']`` for an input like "Boulder,
            Colorado, 80301, USA". The list of possible types can be
            found
            `here <https://developers.google.com/maps/documentation/geocoding/requests-geocoding#Types>`__.

            **Note: you might see a missing component type when you
            think you've already supplied the missing component.** For
            example, this can happen when the input address contains the
            building name, but not the premise number. In the address
            "渋谷区渋谷３丁目　Shibuya Stream", the building name
            "Shibuya Stream" has the component type ``premise``, but the
            premise number is missing, so ``missing_component_types``
            will contain ``premise``.
        unconfirmed_component_types (MutableSequence[str]):
            The types of the components that are present in the
            ``address_components`` but could not be confirmed to be
            correct. This field is provided for the sake of convenience:
            its contents are equivalent to iterating through the
            ``address_components`` to find the types of all the
            components where the
            [confirmation_level][google.maps.addressvalidation.v1.AddressComponent.confirmation_level]
            is not
            [CONFIRMED][google.maps.addressvalidation.v1.AddressComponent.ConfirmationLevel.CONFIRMED]
            or the
            [inferred][google.maps.addressvalidation.v1.AddressComponent.inferred]
            flag is not set to ``true``. The list of possible types can
            be found
            `here <https://developers.google.com/maps/documentation/geocoding/requests-geocoding#Types>`__.
        unresolved_tokens (MutableSequence[str]):
            Any tokens in the input that could not be resolved. This
            might be an input that was not recognized as a valid part of
            an address. For example, for an input such as "Parcel
            0000123123 & 0000456456 Str # Guthrie Center IA 50115 US",
            the unresolved tokens might look like
            ``["Parcel", "0000123123", "&", "0000456456"]``.
    """

    formatted_address: str = proto.Field(
        proto.STRING,
        number=2,
    )
    postal_address: postal_address_pb2.PostalAddress = proto.Field(
        proto.MESSAGE,
        number=3,
        message=postal_address_pb2.PostalAddress,
    )
    address_components: MutableSequence["AddressComponent"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="AddressComponent",
    )
    missing_component_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    unconfirmed_component_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    unresolved_tokens: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )


class AddressComponent(proto.Message):
    r"""Represents an address component, such as a street, city, or
    state.

    Attributes:
        component_name (google.maps.addressvalidation_v1.types.ComponentName):
            The name for this component.
        component_type (str):
            The type of the address component. See `Table 2: Additional
            types returned by the Places
            service <https://developers.google.com/places/web-service/supported_types#table2>`__
            for a list of possible types.
        confirmation_level (google.maps.addressvalidation_v1.types.AddressComponent.ConfirmationLevel):
            Indicates the level of certainty that we have
            that the component is correct.
        inferred (bool):
            Indicates that the component was not part of
            the input, but we inferred it for the address
            location and believe it should be provided for a
            complete address.
        spell_corrected (bool):
            Indicates a correction to a misspelling in
            the component name.  The API does not always
            flag changes from one spelling variant to
            another, such as when changing "centre" to
            "center". It also does not always flag common
            misspellings, such as when changing
            "Amphitheater Pkwy" to "Amphitheatre Pkwy".
        replaced (bool):
            Indicates the name of the component was
            replaced with a completely different one, for
            example a wrong postal code being replaced with
            one that is correct for the address. This is not
            a cosmetic change, the input component has been
            changed to a different one.
        unexpected (bool):
            Indicates an address component that is not
            expected to be present in a postal address for
            the given region. We have retained it only
            because it was part of the input.
    """

    class ConfirmationLevel(proto.Enum):
        r"""The different possible values for confirmation levels.

        Values:
            CONFIRMATION_LEVEL_UNSPECIFIED (0):
                Default value. This value is unused.
            CONFIRMED (1):
                We were able to verify that this component
                exists and makes sense in the context of the
                rest of the address.
            UNCONFIRMED_BUT_PLAUSIBLE (2):
                This component could not be confirmed, but it
                is plausible that it exists. For example, a
                street number within a known valid range of
                numbers on a street where specific house numbers
                are not known.
            UNCONFIRMED_AND_SUSPICIOUS (3):
                This component was not confirmed and is
                likely to be wrong. For example, a neighborhood
                that does not fit the rest of the address.
        """

        CONFIRMATION_LEVEL_UNSPECIFIED = 0
        CONFIRMED = 1
        UNCONFIRMED_BUT_PLAUSIBLE = 2
        UNCONFIRMED_AND_SUSPICIOUS = 3

    component_name: "ComponentName" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ComponentName",
    )
    component_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    confirmation_level: ConfirmationLevel = proto.Field(
        proto.ENUM,
        number=3,
        enum=ConfirmationLevel,
    )
    inferred: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    spell_corrected: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    replaced: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    unexpected: bool = proto.Field(
        proto.BOOL,
        number=7,
    )


class ComponentName(proto.Message):
    r"""A wrapper for the name of the component.

    Attributes:
        text (str):
            The name text. For example, "5th Avenue" for
            a street name or "1253" for a street number.
        language_code (str):
            The BCP-47 language code. This will not be
            present if the component name is not associated
            with a language, such as a street number.
    """

    text: str = proto.Field(
        proto.STRING,
        number=1,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
