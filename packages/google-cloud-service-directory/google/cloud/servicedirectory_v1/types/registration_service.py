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

from google.cloud.servicedirectory_v1.types import endpoint as gcs_endpoint
from google.cloud.servicedirectory_v1.types import namespace as gcs_namespace
from google.cloud.servicedirectory_v1.types import service as gcs_service

__protobuf__ = proto.module(
    package="google.cloud.servicedirectory.v1",
    manifest={
        "CreateNamespaceRequest",
        "ListNamespacesRequest",
        "ListNamespacesResponse",
        "GetNamespaceRequest",
        "UpdateNamespaceRequest",
        "DeleteNamespaceRequest",
        "CreateServiceRequest",
        "ListServicesRequest",
        "ListServicesResponse",
        "GetServiceRequest",
        "UpdateServiceRequest",
        "DeleteServiceRequest",
        "CreateEndpointRequest",
        "ListEndpointsRequest",
        "ListEndpointsResponse",
        "GetEndpointRequest",
        "UpdateEndpointRequest",
        "DeleteEndpointRequest",
    },
)


class CreateNamespaceRequest(proto.Message):
    r"""The request message for
    [RegistrationService.CreateNamespace][google.cloud.servicedirectory.v1.RegistrationService.CreateNamespace].

    Attributes:
        parent (str):
            Required. The resource name of the project
            and location the namespace will be created in.
        namespace_id (str):
            Required. The Resource ID must be 1-63 characters long, and
            comply with RFC1035. Specifically, the name must be 1-63
            characters long and match the regular expression
            ``[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?`` which means the first
            character must be a lowercase letter, and all following
            characters must be a dash, lowercase letter, or digit,
            except the last character, which cannot be a dash.
        namespace (google.cloud.servicedirectory_v1.types.Namespace):
            Required. A namespace with initial fields
            set.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    namespace_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    namespace: gcs_namespace.Namespace = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcs_namespace.Namespace,
    )


class ListNamespacesRequest(proto.Message):
    r"""The request message for
    [RegistrationService.ListNamespaces][google.cloud.servicedirectory.v1.RegistrationService.ListNamespaces].

    Attributes:
        parent (str):
            Required. The resource name of the project
            and location whose namespaces you'd like to
            list.
        page_size (int):
            Optional. The maximum number of items to
            return.
        page_token (str):
            Optional. The next_page_token value returned from a previous
            List request, if any.
        filter (str):
            Optional. The filter to list results by.

            General ``filter`` string syntax:
            ``<field> <operator> <value> (<logical connector>)``

            - ``<field>`` can be ``name`` or ``labels.<key>`` for map
              field
            - ``<operator>`` can be ``<``, ``>``, ``<=``, ``>=``,
              ``!=``, ``=``, ``:``. Of which ``:`` means ``HAS``, and is
              roughly the same as ``=``
            - ``<value>`` must be the same data type as field
            - ``<logical connector>`` can be ``AND``, ``OR``, ``NOT``

            Examples of valid filters:

            - ``labels.owner`` returns namespaces that have a label with
              the key ``owner``, this is the same as ``labels:owner``
            - ``labels.owner=sd`` returns namespaces that have key/value
              ``owner=sd``
            - ``name>projects/my-project/locations/us-east1/namespaces/namespace-c``
              returns namespaces that have name that is alphabetically
              later than the string, so "namespace-e" is returned but
              "namespace-a" is not
            - ``labels.owner!=sd AND labels.foo=bar`` returns namespaces
              that have ``owner`` in label key but value is not ``sd``
              AND have key/value ``foo=bar``
            - ``doesnotexist.foo=bar`` returns an empty list. Note that
              namespace doesn't have a field called "doesnotexist".
              Since the filter does not match any namespaces, it returns
              no results

            For more information about filtering, see `API
            Filtering <https://aip.dev/160>`__.
        order_by (str):
            Optional. The order to list results by.

            General ``order_by`` string syntax:
            ``<field> (<asc|desc>) (,)``

            - ``<field>`` allows value: ``name``
            - ``<asc|desc>`` ascending or descending order by
              ``<field>``. If this is left blank, ``asc`` is used

            Note that an empty ``order_by`` string results in default
            order, which is order by ``name`` in ascending order.
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


class ListNamespacesResponse(proto.Message):
    r"""The response message for
    [RegistrationService.ListNamespaces][google.cloud.servicedirectory.v1.RegistrationService.ListNamespaces].

    Attributes:
        namespaces (MutableSequence[google.cloud.servicedirectory_v1.types.Namespace]):
            The list of namespaces.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    namespaces: MutableSequence[gcs_namespace.Namespace] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcs_namespace.Namespace,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetNamespaceRequest(proto.Message):
    r"""The request message for
    [RegistrationService.GetNamespace][google.cloud.servicedirectory.v1.RegistrationService.GetNamespace].

    Attributes:
        name (str):
            Required. The name of the namespace to
            retrieve.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateNamespaceRequest(proto.Message):
    r"""The request message for
    [RegistrationService.UpdateNamespace][google.cloud.servicedirectory.v1.RegistrationService.UpdateNamespace].

    Attributes:
        namespace (google.cloud.servicedirectory_v1.types.Namespace):
            Required. The updated namespace.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. List of fields to be updated in
            this request.
    """

    namespace: gcs_namespace.Namespace = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcs_namespace.Namespace,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteNamespaceRequest(proto.Message):
    r"""The request message for
    [RegistrationService.DeleteNamespace][google.cloud.servicedirectory.v1.RegistrationService.DeleteNamespace].

    Attributes:
        name (str):
            Required. The name of the namespace to
            delete.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateServiceRequest(proto.Message):
    r"""The request message for
    [RegistrationService.CreateService][google.cloud.servicedirectory.v1.RegistrationService.CreateService].

    Attributes:
        parent (str):
            Required. The resource name of the namespace
            this service will belong to.
        service_id (str):
            Required. The Resource ID must be 1-63 characters long, and
            comply with RFC1035. Specifically, the name must be 1-63
            characters long and match the regular expression
            ``[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?`` which means the first
            character must be a lowercase letter, and all following
            characters must be a dash, lowercase letter, or digit,
            except the last character, which cannot be a dash.
        service (google.cloud.servicedirectory_v1.types.Service):
            Required. A service  with initial fields set.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    service_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    service: gcs_service.Service = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcs_service.Service,
    )


class ListServicesRequest(proto.Message):
    r"""The request message for
    [RegistrationService.ListServices][google.cloud.servicedirectory.v1.RegistrationService.ListServices].

    Attributes:
        parent (str):
            Required. The resource name of the namespace
            whose services you'd like to list.
        page_size (int):
            Optional. The maximum number of items to
            return.
        page_token (str):
            Optional. The next_page_token value returned from a previous
            List request, if any.
        filter (str):
            Optional. The filter to list results by.

            General ``filter`` string syntax:
            ``<field> <operator> <value> (<logical connector>)``

            - ``<field>`` can be ``name`` or ``annotations.<key>`` for
              map field
            - ``<operator>`` can be ``<``, ``>``, ``<=``, ``>=``,
              ``!=``, ``=``, ``:``. Of which ``:`` means ``HAS``, and is
              roughly the same as ``=``
            - ``<value>`` must be the same data type as field
            - ``<logical connector>`` can be ``AND``, ``OR``, ``NOT``

            Examples of valid filters:

            - ``annotations.owner`` returns services that have a
              annotation with the key ``owner``, this is the same as
              ``annotations:owner``
            - ``annotations.protocol=gRPC`` returns services that have
              key/value ``protocol=gRPC``
            -

            ``name>projects/my-project/locations/us-east1/namespaces/my-namespace/services/service-c``
            returns services that have name that is alphabetically later
            than the string, so "service-e" is returned but "service-a"
            is not

            - ``annotations.owner!=sd AND annotations.foo=bar`` returns
              services that have ``owner`` in annotation key but value
              is not ``sd`` AND have key/value ``foo=bar``
            - ``doesnotexist.foo=bar`` returns an empty list. Note that
              service doesn't have a field called "doesnotexist". Since
              the filter does not match any services, it returns no
              results

            For more information about filtering, see `API
            Filtering <https://aip.dev/160>`__.
        order_by (str):
            Optional. The order to list results by.

            General ``order_by`` string syntax:
            ``<field> (<asc|desc>) (,)``

            - ``<field>`` allows value: ``name``
            - ``<asc|desc>`` ascending or descending order by
              ``<field>``. If this is left blank, ``asc`` is used

            Note that an empty ``order_by`` string results in default
            order, which is order by ``name`` in ascending order.
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


class ListServicesResponse(proto.Message):
    r"""The response message for
    [RegistrationService.ListServices][google.cloud.servicedirectory.v1.RegistrationService.ListServices].

    Attributes:
        services (MutableSequence[google.cloud.servicedirectory_v1.types.Service]):
            The list of services.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    services: MutableSequence[gcs_service.Service] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcs_service.Service,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetServiceRequest(proto.Message):
    r"""The request message for
    [RegistrationService.GetService][google.cloud.servicedirectory.v1.RegistrationService.GetService].
    This should not be used for looking up a service. Instead, use the
    ``resolve`` method as it contains all endpoints and associated
    annotations.

    Attributes:
        name (str):
            Required. The name of the service to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateServiceRequest(proto.Message):
    r"""The request message for
    [RegistrationService.UpdateService][google.cloud.servicedirectory.v1.RegistrationService.UpdateService].

    Attributes:
        service (google.cloud.servicedirectory_v1.types.Service):
            Required. The updated service.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. List of fields to be updated in
            this request.
    """

    service: gcs_service.Service = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcs_service.Service,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteServiceRequest(proto.Message):
    r"""The request message for
    [RegistrationService.DeleteService][google.cloud.servicedirectory.v1.RegistrationService.DeleteService].

    Attributes:
        name (str):
            Required. The name of the service to delete.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateEndpointRequest(proto.Message):
    r"""The request message for
    [RegistrationService.CreateEndpoint][google.cloud.servicedirectory.v1.RegistrationService.CreateEndpoint].

    Attributes:
        parent (str):
            Required. The resource name of the service
            that this endpoint provides.
        endpoint_id (str):
            Required. The Resource ID must be 1-63 characters long, and
            comply with RFC1035. Specifically, the name must be 1-63
            characters long and match the regular expression
            ``[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?`` which means the first
            character must be a lowercase letter, and all following
            characters must be a dash, lowercase letter, or digit,
            except the last character, which cannot be a dash.
        endpoint (google.cloud.servicedirectory_v1.types.Endpoint):
            Required. A endpoint with initial fields set.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    endpoint_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    endpoint: gcs_endpoint.Endpoint = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcs_endpoint.Endpoint,
    )


class ListEndpointsRequest(proto.Message):
    r"""The request message for
    [RegistrationService.ListEndpoints][google.cloud.servicedirectory.v1.RegistrationService.ListEndpoints].

    Attributes:
        parent (str):
            Required. The resource name of the service
            whose endpoints you'd like to list.
        page_size (int):
            Optional. The maximum number of items to
            return.
        page_token (str):
            Optional. The next_page_token value returned from a previous
            List request, if any.
        filter (str):
            Optional. The filter to list results by.

            General ``filter`` string syntax:
            ``<field> <operator> <value> (<logical connector>)``

            - ``<field>`` can be ``name``, ``address``, ``port``, or
              ``annotations.<key>`` for map field
            - ``<operator>`` can be ``<``, ``>``, ``<=``, ``>=``,
              ``!=``, ``=``, ``:``. Of which ``:`` means ``HAS``, and is
              roughly the same as ``=``
            - ``<value>`` must be the same data type as field
            - ``<logical connector>`` can be ``AND``, ``OR``, ``NOT``

            Examples of valid filters:

            - ``annotations.owner`` returns endpoints that have a
              annotation with the key ``owner``, this is the same as
              ``annotations:owner``
            - ``annotations.protocol=gRPC`` returns endpoints that have
              key/value ``protocol=gRPC``
            - ``address=192.108.1.105`` returns endpoints that have this
              address
            - ``port>8080`` returns endpoints that have port number
              larger than 8080
            -

            ``name>projects/my-project/locations/us-east1/namespaces/my-namespace/services/my-service/endpoints/endpoint-c``
            returns endpoints that have name that is alphabetically
            later than the string, so "endpoint-e" is returned but
            "endpoint-a" is not

            - ``annotations.owner!=sd AND annotations.foo=bar`` returns
              endpoints that have ``owner`` in annotation key but value
              is not ``sd`` AND have key/value ``foo=bar``
            - ``doesnotexist.foo=bar`` returns an empty list. Note that
              endpoint doesn't have a field called "doesnotexist". Since
              the filter does not match any endpoints, it returns no
              results

            For more information about filtering, see `API
            Filtering <https://aip.dev/160>`__.
        order_by (str):
            Optional. The order to list results by.

            General ``order_by`` string syntax:
            ``<field> (<asc|desc>) (,)``

            - ``<field>`` allows values: ``name``, ``address``, ``port``
            - ``<asc|desc>`` ascending or descending order by
              ``<field>``. If this is left blank, ``asc`` is used

            Note that an empty ``order_by`` string results in default
            order, which is order by ``name`` in ascending order.
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


class ListEndpointsResponse(proto.Message):
    r"""The response message for
    [RegistrationService.ListEndpoints][google.cloud.servicedirectory.v1.RegistrationService.ListEndpoints].

    Attributes:
        endpoints (MutableSequence[google.cloud.servicedirectory_v1.types.Endpoint]):
            The list of endpoints.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    endpoints: MutableSequence[gcs_endpoint.Endpoint] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcs_endpoint.Endpoint,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetEndpointRequest(proto.Message):
    r"""The request message for
    [RegistrationService.GetEndpoint][google.cloud.servicedirectory.v1.RegistrationService.GetEndpoint].
    This should not be used to lookup endpoints at runtime. Instead, use
    the ``resolve`` method.

    Attributes:
        name (str):
            Required. The name of the endpoint to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateEndpointRequest(proto.Message):
    r"""The request message for
    [RegistrationService.UpdateEndpoint][google.cloud.servicedirectory.v1.RegistrationService.UpdateEndpoint].

    Attributes:
        endpoint (google.cloud.servicedirectory_v1.types.Endpoint):
            Required. The updated endpoint.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. List of fields to be updated in
            this request.
    """

    endpoint: gcs_endpoint.Endpoint = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcs_endpoint.Endpoint,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteEndpointRequest(proto.Message):
    r"""The request message for
    [RegistrationService.DeleteEndpoint][google.cloud.servicedirectory.v1.RegistrationService.DeleteEndpoint].

    Attributes:
        name (str):
            Required. The name of the endpoint to delete.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
