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
    package="google.cloud.designcenter.v1",
    manifest={
        "ApplicationOperation",
        "ApplicationTemplateOperation",
        "TemplateCategory",
        "ApplicationCompositionType",
        "TemplateType",
        "DisplayVariableAlternateType",
        "DisplayVariableVisibility",
        "IACFormat",
        "ApplicationType",
        "IACSource",
        "ConnectionDependencyType",
    },
)


class ApplicationOperation(proto.Enum):
    r"""Represents the type of operation to perform on an
    application.

    Values:
        APPLICATION_OPERATION_UNSPECIFIED (0):
            The default value. This value is unused.
        APPLICATION_OPERATION_CREATE (1):
            Creates a new application.
        APPLICATION_OPERATION_UPDATE (2):
            Updates an existing application.
        APPLICATION_OPERATION_PREVIEW (3):
            Previews a deployment of an application.
        APPLICATION_OPERATION_DEPLOY (4):
            Deploys an application.
        APPLICATION_OPERATION_GET (5):
            Gets an application.
        APPLICATION_OPERATION_GENERATE_IAC (6):
            Generates IaC for an application.
    """

    APPLICATION_OPERATION_UNSPECIFIED = 0
    APPLICATION_OPERATION_CREATE = 1
    APPLICATION_OPERATION_UPDATE = 2
    APPLICATION_OPERATION_PREVIEW = 3
    APPLICATION_OPERATION_DEPLOY = 4
    APPLICATION_OPERATION_GET = 5
    APPLICATION_OPERATION_GENERATE_IAC = 6


class ApplicationTemplateOperation(proto.Enum):
    r"""Represents the type of operation to perform on an application
    template.

    Values:
        APPLICATION_TEMPLATE_OPERATION_UNSPECIFIED (0):
            The default value. This value is unused.
        APPLICATION_TEMPLATE_OPERATION_CREATE (1):
            Creates a new application template.
        APPLICATION_TEMPLATE_OPERATION_UPDATE (2):
            Updates an existing application template.
        APPLICATION_TEMPLATE_OPERATION_COMMIT (3):
            Commits an application template to create a
            new revision.
        APPLICATION_TEMPLATE_OPERATION_GENERATE_IAC (4):
            Generates IaC for an application template.
        APPLICATION_TEMPLATE_OPERATION_GET (5):
            Gets an application template.
        APPLICATION_TEMPLATE_OPERATION_IMPORT_IAC (6):
            Imports an application template from IaC.
        APPLICATION_TEMPLATE_OPERATION_UPDATE_COMPONENT_PARAMETERS (7):
            Updates component parameters from IaC.
    """

    APPLICATION_TEMPLATE_OPERATION_UNSPECIFIED = 0
    APPLICATION_TEMPLATE_OPERATION_CREATE = 1
    APPLICATION_TEMPLATE_OPERATION_UPDATE = 2
    APPLICATION_TEMPLATE_OPERATION_COMMIT = 3
    APPLICATION_TEMPLATE_OPERATION_GENERATE_IAC = 4
    APPLICATION_TEMPLATE_OPERATION_GET = 5
    APPLICATION_TEMPLATE_OPERATION_IMPORT_IAC = 6
    APPLICATION_TEMPLATE_OPERATION_UPDATE_COMPONENT_PARAMETERS = 7


class TemplateCategory(proto.Enum):
    r"""Supported categories in Application Design Center.

    Values:
        TEMPLATE_CATEGORY_UNSPECIFIED (0):
            Unspecified category.
        COMPONENT_TEMPLATE (1):
            Component template.
        APPLICATION_TEMPLATE (2):
            Application template.
        COMPOSITE_SOLUTION_TEMPLATE (3):
            Imported as a single, complex unit without
            disassembling into components.
        INSTANCE_TEMPLATE (4):
            Instance template.
    """

    TEMPLATE_CATEGORY_UNSPECIFIED = 0
    COMPONENT_TEMPLATE = 1
    APPLICATION_TEMPLATE = 2
    COMPOSITE_SOLUTION_TEMPLATE = 3
    INSTANCE_TEMPLATE = 4


class ApplicationCompositionType(proto.Enum):
    r"""The composition type of the applicationTemplate or
    application: STANDARD OR COMPOSITE.

    Values:
        APPLICATION_COMPOSITION_TYPE_UNSPECIFIED (0):
            ApplicationCompositionType is UNSPECIFIED.
        STANDARD (1):
            ApplicationCompositionType is STANDARD. The
            applicationTemplate or application is composed
            of components only of type
            service/workload/asset and has a single root
            module in terraform code.
        COMPOSITE (2):
            ApplicationCompositionType is COMPOSITE. The
            template is composed of STANDARD
            applicationTemplate(s) and might be having
            multiple root modules in terraform code.
    """

    APPLICATION_COMPOSITION_TYPE_UNSPECIFIED = 0
    STANDARD = 1
    COMPOSITE = 2


class TemplateType(proto.Enum):
    r"""Assembly template types.

    Values:
        TEMPLATE_TYPE_UNSPECIFIED (0):
            Default.
        SERVICE (1):
            A service template is an App Hub service.
        WORKLOAD (2):
            A workload template is an App Hub workload.
        ASSET (3):
            An asset template can be used to provision
            resources that are not services or workloads.
        APPLICATION (4):
            An application template is a composition of
            workload/service/asset templates.
        JSS_SOLUTION (5):
            A Jumpstart Solution template.
        SERVICE_DATA_SOURCE (6):
            A service data source template.
        HELM_APPLICATION (7):
            A helm chart based template.
        STANDARD_APPLICATION_TEMPLATE (8):
            A standard application template.
        COMPOSITE_APPLICATION_TEMPLATE (9):
            A composite application template.
        HELM_CHART (10):
            A helm chart based template.
    """

    TEMPLATE_TYPE_UNSPECIFIED = 0
    SERVICE = 1
    WORKLOAD = 2
    ASSET = 3
    APPLICATION = 4
    JSS_SOLUTION = 5
    SERVICE_DATA_SOURCE = 6
    HELM_APPLICATION = 7
    STANDARD_APPLICATION_TEMPLATE = 8
    COMPOSITE_APPLICATION_TEMPLATE = 9
    HELM_CHART = 10


class DisplayVariableAlternateType(proto.Enum):
    r"""Alternate default value type.
    Allows you to define an alternative value for predefined use
    cases, such as security. If specified, this value can be used
    instead of the default value in BlueprintVariable.

    Values:
        DISPLAY_VARIABLE_ALTERNATE_TYPE_UNSPECIFIED (0):
            Default
        DISPLAY_VARIABLE_ALTERNATE_TYPE_SECURITY (1):
            A more secure default.
        DISPLAY_VARIABLE_ALTERNATE_TYPE_DC (2):
            A default specifically needed for Application
            Design center.
    """

    DISPLAY_VARIABLE_ALTERNATE_TYPE_UNSPECIFIED = 0
    DISPLAY_VARIABLE_ALTERNATE_TYPE_SECURITY = 1
    DISPLAY_VARIABLE_ALTERNATE_TYPE_DC = 2


class DisplayVariableVisibility(proto.Enum):
    r"""Visibility defines how the output is exposed.

    Values:
        DISPLAY_VARIABLE_VISIBILITY_UNSPECIFIED (0):
            Default
        DISPLAY_VARIABLE_VISIBILITY_ROOT (1):
            Expose output as root module output.
    """

    DISPLAY_VARIABLE_VISIBILITY_UNSPECIFIED = 0
    DISPLAY_VARIABLE_VISIBILITY_ROOT = 1


class IACFormat(proto.Enum):
    r"""The IaC format to generate.

    Values:
        IAC_FORMAT_UNSPECIFIED (0):
            IaC format is unspecified.
        TERRAFORM (1):
            IaC format is Terraform.
        HELM (2):
            IaC format is HELM.
    """

    IAC_FORMAT_UNSPECIFIED = 0
    TERRAFORM = 1
    HELM = 2


class ApplicationType(proto.Enum):
    r"""The type of the application.

    Values:
        APPLICATION_TYPE_UNSPECIFIED (0):
            Application type is unspecified.
        TERRAFORM_APP (1):
            Application type is terraform application.
        HELM_APP (2):
            Application type is helm application.
    """

    APPLICATION_TYPE_UNSPECIFIED = 0
    TERRAFORM_APP = 1
    HELM_APP = 2


class IACSource(proto.Enum):
    r"""Enum to specify the source format of the IaC.

    Values:
        IAC_SOURCE_UNSPECIFIED (0):
            The source is not specified.
        IAC_SOURCE_SAT (1):
            The IaC source is SAT. This is used to
            generate equivalent Terraform.
        IAC_SOURCE_TERRAFORM (2):
            The IaC source is Terraform.
    """

    IAC_SOURCE_UNSPECIFIED = 0
    IAC_SOURCE_SAT = 1
    IAC_SOURCE_TERRAFORM = 2


class ConnectionDependencyType(proto.Enum):
    r"""Indicates the dependency type of the connection.

    Values:
        CONNECTION_DEPENDENCY_TYPE_UNSPECIFIED (0):
            The dependency type is unspecified.
        CONNECTION_DEPENDENCY_TYPE_DATA (1):
            Data dependency: output parameter of one
            module is input to another.
        CONNECTION_DEPENDENCY_TYPE_LOGICAL (2):
            Logical dependency: explicitly declared execution order
            dependency (depends_on).
    """

    CONNECTION_DEPENDENCY_TYPE_UNSPECIFIED = 0
    CONNECTION_DEPENDENCY_TYPE_DATA = 1
    CONNECTION_DEPENDENCY_TYPE_LOGICAL = 2


__all__ = tuple(sorted(__protobuf__.manifest))
