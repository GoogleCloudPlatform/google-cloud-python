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

from google.cloud.commerceproducer_v1beta.types import private_offer

__protobuf__ = proto.module(
    package="google.cloud.commerceproducer.v1beta",
    manifest={
        "Service",
    },
)


class Service(proto.Message):
    r"""Message describing Service resource.

    Attributes:
        name (str):
            Identifier. Name of resource.
        title (str):
            Output only. Title of the service.

            Not included for ``SERVICE_VIEW_BASIC``.
        document_requirement (google.cloud.commerceproducer_v1beta.types.Service.DocumentRequirement):
            Output only. Document requirement for private offers on this
            service.

            Constraints that apply to every service, such as the
            restriction against attaching both a standard and a custom
            EULA, are documented on ``PrivateOfferDocument`` and are not
            represented here.
        product_type (google.cloud.commerceproducer_v1beta.types.Service.ProductType):
            Output only. Type of the product this service
            commercializes.
    """

    class ProductType(proto.Enum):
        r"""The type of the product this service commercializes.

        Every service has a type, but only the types listed below are
        exposed. A service whose type is not one of the listed values
        reports ``PRODUCT_TYPE_UNSPECIFIED``.

        Values may be added over time. Clients must handle unrecognized
        values. When new values are added, the ProductType for an existing
        service may change. Clients must also be able to handle a change in
        ProductType.

        Values:
            PRODUCT_TYPE_UNSPECIFIED (0):
                The service has a type, but it is not one of
                the types exposed below.
            SOFTWARE_AS_A_SERVICE (1):
                Represents a software-as-a-service product.
                See
                https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas
            ANALYTICS_HUB_LISTING (2):
                Represents a data product on BigQuery sharing
                (formerly Analytics Hub). See
                https://docs.cloud.google.com/marketplace/docs/partners/data
            PROFESSIONAL_SERVICES (3):
                Represents a professional services product.
                See
                https://docs.cloud.google.com/marketplace/docs/partners/professional-services
        """

        PRODUCT_TYPE_UNSPECIFIED = 0
        SOFTWARE_AS_A_SERVICE = 1
        ANALYTICS_HUB_LISTING = 2
        PROFESSIONAL_SERVICES = 3

    class DocumentRequirement(proto.Message):
        r"""Requirements and constraints for documents attached to
        private offers.

        Attributes:
            document_type_requirements (MutableSequence[google.cloud.commerceproducer_v1beta.types.Service.DocumentRequirement.DocumentTypeRequirement]):
                Document requirements for private offers on
                this service.
                Each document type appears at most once. The
                order of entries is not significant. A document
                type that is not present in this list is not
                permitted for private offers on this service.
        """

        class DocumentTypeRequirement(proto.Message):
            r"""Requirement specification for a specific document type.

            Attributes:
                document_type (google.cloud.commerceproducer_v1beta.types.PrivateOfferDocument.DocumentType):
                    The document type.
                requirement_level (google.cloud.commerceproducer_v1beta.types.Service.DocumentRequirement.DocumentTypeRequirement.RequirementLevel):
                    The requirement level for this document type.
            """

            class RequirementLevel(proto.Enum):
                r"""Requirement level for the document type.

                Values:
                    REQUIREMENT_LEVEL_UNSPECIFIED (0):
                        Unspecified requirement level. Do not use.
                    REQUIRED (1):
                        The document type is mandatory for private
                        offers on this service. Exactly one document of
                        this type must be attached.
                    OPTIONAL (2):
                        The document type is optional for private
                        offers on this service. At most one document of
                        this type may be attached.
                    NOT_ALLOWED (3):
                        The document type is not permitted for private offers on
                        this service. No document of this type may be attached.

                        A document type omitted from ``document_type_requirements``
                        is also not permitted. This value is used to state the
                        restriction explicitly.
                """

                REQUIREMENT_LEVEL_UNSPECIFIED = 0
                REQUIRED = 1
                OPTIONAL = 2
                NOT_ALLOWED = 3

            document_type: private_offer.PrivateOfferDocument.DocumentType = (
                proto.Field(
                    proto.ENUM,
                    number=1,
                    enum=private_offer.PrivateOfferDocument.DocumentType,
                )
            )
            requirement_level: "Service.DocumentRequirement.DocumentTypeRequirement.RequirementLevel" = proto.Field(
                proto.ENUM,
                number=2,
                enum="Service.DocumentRequirement.DocumentTypeRequirement.RequirementLevel",
            )

        document_type_requirements: MutableSequence[
            "Service.DocumentRequirement.DocumentTypeRequirement"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="Service.DocumentRequirement.DocumentTypeRequirement",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    title: str = proto.Field(
        proto.STRING,
        number=2,
    )
    document_requirement: DocumentRequirement = proto.Field(
        proto.MESSAGE,
        number=3,
        message=DocumentRequirement,
    )
    product_type: ProductType = proto.Field(
        proto.ENUM,
        number=4,
        enum=ProductType,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
