# Copyright 2016 Google LLC All rights reserved.
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

"""Helper functions for Cloud Spanner."""

import atexit
import base64
import datetime
import decimal
import logging
import math
import operator
import os
import queue
import threading
import time
import uuid

import proto
from google.api_core import datetime_helpers
from google.api_core.exceptions import Aborted
from google.protobuf.internal.enum_type_wrapper import EnumTypeWrapper
from google.protobuf.message import DecodeError, Message
from google.protobuf.struct_pb2 import NULL_VALUE, ListValue, Value
from google.rpc.error_details_pb2 import RetryInfo

from google.cloud.spanner_v1.data_types import Interval, JsonObject
from google.cloud.spanner_v1.exceptions import wrap_with_request_id
from google.cloud.spanner_v1.request_id_header import (
    with_request_id,
    with_request_id_metadata_only,
)
from google.cloud.spanner_v1.types import (
    DirectedReadOptions,
    ExecuteSqlRequest,
    RequestOptions,
    TransactionOptions,
    Type,
    TypeCode,
)

try:
    from opentelemetry.propagate import inject
    from opentelemetry.propagators.textmap import Setter
    from opentelemetry.semconv.resource import ResourceAttributes

    HAS_OPENTELEMETRY_INSTALLED = True
except ImportError:
    HAS_OPENTELEMETRY_INSTALLED = False

try:
    from opentelemetry.resourcedetector import gcp_resource_detector
    from opentelemetry.resourcedetector.gcp_resource_detector import (
        GoogleCloudResourceDetector,
    )

    # Overwrite the requests timeout for the detector.
    # This is necessary as the client will wait the full timeout if the
    # code is not run in a GCP environment, with the location endpoints available.
    gcp_resource_detector._TIMEOUT_SEC = 0.2
except ImportError:
    GoogleCloudResourceDetector = None
import random
from typing import List, Tuple

ENABLE_AFE_SERVER_TIMING = (
    os.environ.get("SPANNER_DISABLE_AFE_SERVER_TIMING", "").lower() != "true"
    and os.environ.get("SPANNER_DISABLE_BUILTIN_METRICS", "").lower() != "true"
)

# Validation error messages
NUMERIC_MAX_SCALE_ERR_MSG = (
    "Max scale for a numeric is 9. The requested numeric has scale {}"
)
NUMERIC_MAX_PRECISION_ERR_MSG = (
    "Max precision for the whole component of a numeric is 29. The requested "
    + "numeric has a whole component with precision {}"
)

GOOGLE_CLOUD_REGION_GLOBAL = "global"

_LOGGER = logging.getLogger(__name__)

_cloud_region: str = None


if HAS_OPENTELEMETRY_INSTALLED:

    class OpenTelemetryContextSetter(Setter):
        """
        Used by Open Telemetry for context propagation.
        """

        def set(self, carrier: List[Tuple[str, str]], key: str, value: str) -> None:
            """
            Injects trace context into Spanner metadata

            Args:
                carrier(PubsubMessage): The Pub/Sub message which is the carrier of Open Telemetry
                data.
                key(str): The key for which the Open Telemetry context data needs to be set.
                value(str): The Open Telemetry context value to be set.

            Returns:
                None
            """
            carrier.append((key, value))


def _get_cloud_region() -> str:
    """Get the location of the resource, caching the result.

    Returns:
        str: The location of the resource. If OpenTelemetry is not installed, returns a global region.
    """
    global _cloud_region
    if _cloud_region is not None:
        return _cloud_region

    try:
        detector = GoogleCloudResourceDetector()
        resources = detector.detect()
        if ResourceAttributes.CLOUD_REGION in resources.attributes:
            _cloud_region = resources.attributes[ResourceAttributes.CLOUD_REGION]
        else:
            _cloud_region = GOOGLE_CLOUD_REGION_GLOBAL
    except Exception as e:
        _LOGGER.warning(
            "Failed to detect GCP resource location for Spanner metrics, defaulting to 'global'. Error: %s",
            e,
        )
        _cloud_region = GOOGLE_CLOUD_REGION_GLOBAL

    return _cloud_region


def _validate_and_decode_bytes(bytestring):
    try:
        return bytestring.decode("utf-8")
    except (ValueError, UnicodeDecodeError):
        raise ValueError(
            "Received a bytes that is not base64 encoded. "
            "Ensure that you either send a Unicode string or a "
            "base64-encoded bytes."
        )


def _try_to_coerce_bytes(bytestring):
    """Try to coerce a byte string into the right thing based on Python
    version and whether or not it is base64 encoded.

    Return a text string or raise ValueError.
    """
    _validate_and_decode_bytes(bytestring)
    return bytestring


_VALID_QUERY_OPTIONS_KEYS = frozenset(
    ExecuteSqlRequest.QueryOptions._meta.fields.keys()
)


def _to_query_options(options):
    """Normalize dict or QueryOptions to a non-empty QueryOptions, or None.

    :type options:
        :class:`~google.cloud.spanner_v1.types.ExecuteSqlRequest.QueryOptions`
        or :class:`dict` or None
    :param options: Query options to normalize.

    :rtype:
        :class:`~google.cloud.spanner_v1.types.ExecuteSqlRequest.QueryOptions`
        or None
    :returns:
        A non-empty QueryOptions instance, or None if options is empty or None.

    :raises TypeError:
        If options is not a QueryOptions, dict, or None.
    :raises ValueError:
        If options is a dict containing unknown fields.
    """
    if options is None:
        return None
    if isinstance(options, dict):
        if options.keys() <= _VALID_QUERY_OPTIONS_KEYS and not any(options.values()):
            return None
        options = ExecuteSqlRequest.QueryOptions(options)
    elif not isinstance(options, ExecuteSqlRequest.QueryOptions):
        raise TypeError(
            f"query_options must be a QueryOptions or dict, got {type(options).__name__}"
        )
    return options if type(options).pb(options).ByteSize() > 0 else None


def _merge_query_options(base, merge):
    """Merge higher precedence QueryOptions with current QueryOptions.

    :type base:
        :class:`~google.cloud.spanner_v1.types.ExecuteSqlRequest.QueryOptions`
        or :class:`dict` or None
    :param base: The current QueryOptions that is intended for use.

    :type merge:
        :class:`~google.cloud.spanner_v1.types.ExecuteSqlRequest.QueryOptions`
        or :class:`dict` or None
    :param merge:
        The QueryOptions that have a higher priority than base. These options
        should overwrite the fields in base.

    :rtype:
        :class:`~google.cloud.spanner_v1.types.ExecuteSqlRequest.QueryOptions`
        or None
    :returns:
        QueryOptions object formed by merging the two given QueryOptions.
        If the resultant object only has empty fields, returns None.
    """
    if base is None and merge is None:
        return None

    base = _to_query_options(base)
    merge = _to_query_options(merge)
    if base is None:
        return merge
    if merge is None:
        return base

    combined = ExecuteSqlRequest.QueryOptions()
    combined_pb = type(combined).pb(combined)
    combined_pb.CopyFrom(type(base).pb(base))
    combined_pb.MergeFrom(type(merge).pb(merge))
    return combined


# The protobuf class underlying the proto-plus ``ExecuteSqlRequest`` wrapper.
_EXECUTE_SQL_REQUEST_PB = ExecuteSqlRequest.pb()


def _as_raw_pb(value, message_type):
    """Return the raw protobuf message for ``value``.

    ``value`` may be a proto-plus message, a ``dict``, a raw protobuf message,
    or ``None``:

    - proto-plus messages are unwrapped directly, which is the hot path;
    - dicts are converted by proto-plus, because the raw protobuf constructor
      only accepts dicts whose values are themselves dicts and rejects
      proto-plus messages nested inside them;
    - raw protobuf messages and ``None`` are returned unchanged. The raw
      constructor treats a ``None`` keyword argument as "field not set".

    :type value: :class:`~proto.message.Message` or :class:`dict` or
        :class:`~google.protobuf.message.Message` or None
    :param value: the value to convert.

    :type message_type: type
    :param message_type: the proto-plus class of the target field, used to
        convert ``value`` when it is a ``dict``.

    :rtype: :class:`~google.protobuf.message.Message` or None
    :returns: the raw protobuf message, or ``value`` unchanged.
    """
    if value is None:
        return None
    if isinstance(value, proto.Message):
        return type(value).pb(value)
    if isinstance(value, dict):
        return message_type.pb(message_type(value))
    return value


def _make_execute_sql_request(
    session_name,
    sql,
    seqno,
    params=None,
    param_types=None,
    query_mode=None,
    partition=None,
    query_options=None,
    request_options=None,
    last_statement=False,
    data_boost_enabled=False,
    directed_read_options=None,
):
    """Build an :class:`~google.cloud.spanner_v1.types.ExecuteSqlRequest`.

    ``ExecuteSqlRequest(**kwargs)`` marshals every keyword argument through
    proto-plus, which performs Python-level descriptor lookups and type
    coercion for each field. Executing a query is a hot path, so the request is
    built on the underlying protobuf message instead and shallow-wrapped with
    :meth:`~proto.message.Message.wrap`. The result is an ordinary
    ``ExecuteSqlRequest`` that serializes to identical bytes, built several
    times faster.

    Arguments accept the same types as the proto-plus constructor: proto-plus
    messages, dicts, or raw protobuf messages. ``None`` leaves the
    corresponding field unset, with two documented exceptions:

    - ``params=None`` is treated as "no parameters", where the proto-plus
      constructor raises;
    - a ``params`` dict must hold plain Python values, not raw
      :class:`~google.protobuf.struct_pb2.Value` messages. ``execute_sql``
      always passes an already-encoded ``Struct``, so this only affects direct
      callers of this helper.

    :rtype: :class:`~google.cloud.spanner_v1.types.ExecuteSqlRequest`
    :returns: the request to send to ``ExecuteStreamingSql``.
    """
    if isinstance(query_mode, str):
        query_mode = ExecuteSqlRequest.QueryMode[query_mode]
    return ExecuteSqlRequest.wrap(
        _EXECUTE_SQL_REQUEST_PB(
            session=session_name,
            sql=sql,
            seqno=seqno,
            params=params,
            param_types=(
                {
                    name: _as_raw_pb(param_type, Type)
                    for name, param_type in param_types.items()
                }
                if param_types
                else None
            ),
            query_mode=query_mode,
            partition_token=partition,
            query_options=_as_raw_pb(query_options, ExecuteSqlRequest.QueryOptions),
            request_options=_as_raw_pb(request_options, RequestOptions),
            last_statement=last_statement,
            data_boost_enabled=data_boost_enabled,
            directed_read_options=_as_raw_pb(
                directed_read_options, DirectedReadOptions
            ),
        )
    )


def _merge_client_context(base, merge):
    """Merge higher precedence ClientContext with current ClientContext.

    :type base: :class:`~google.cloud.spanner_v1.types.RequestOptions.ClientContext`
        or :class:`dict` or None
    :param base: The current ClientContext that is intended for use.

    :type merge: :class:`~google.cloud.spanner_v1.types.RequestOptions.ClientContext`
        or :class:`dict` or None
    :param merge:
        The ClientContext that has a higher priority than base. These options
        should overwrite the fields in base.

    :rtype: :class:`~google.cloud.spanner_v1.types.RequestOptions.ClientContext`
        or None
    :returns:
        ClientContext object formed by merging the two given ClientContexts.
    """
    if base is None and merge is None:
        return None

    # Avoid in-place modification of base
    combined_pb = RequestOptions.ClientContext()._pb
    if base:
        base_pb = (
            RequestOptions.ClientContext(base)._pb
            if isinstance(base, dict)
            else base._pb
        )
        combined_pb.MergeFrom(base_pb)
    if merge:
        merge_pb = (
            RequestOptions.ClientContext(merge)._pb
            if isinstance(merge, dict)
            else merge._pb
        )
        combined_pb.MergeFrom(merge_pb)

    combined = RequestOptions.ClientContext(combined_pb)

    if not combined.secure_context:
        return None
    return combined


def _validate_client_context(client_context):
    """Validate and convert client_context.

    :type client_context: :class:`~google.cloud.spanner_v1.types.RequestOptions.ClientContext`
        or :class:`dict`
    :param client_context: (Optional) Client context to use.

    :rtype: :class:`~google.cloud.spanner_v1.types.RequestOptions.ClientContext`
    :returns: Validated ClientContext object or None.
    :raises TypeError: if client_context is not a ClientContext or a dict.
    """
    if client_context is not None:
        if isinstance(client_context, dict):
            client_context = RequestOptions.ClientContext(client_context)
        elif not isinstance(client_context, RequestOptions.ClientContext):
            raise TypeError("client_context must be a ClientContext or a dict")
    return client_context


def _merge_request_options(request_options, client_context):
    """Merge RequestOptions and ClientContext.

    :type request_options: :class:`~google.cloud.spanner_v1.types.RequestOptions`
        or :class:`dict` or None
    :param request_options: The current RequestOptions that is intended for use.

    :type client_context: :class:`~google.cloud.spanner_v1.types.RequestOptions.ClientContext`
        or :class:`dict` or None
    :param client_context:
        The ClientContext to merge into request_options.

    :rtype: :class:`~google.cloud.spanner_v1.types.RequestOptions`
        or None
    :returns:
        RequestOptions object formed by merging the given ClientContext.
    """
    if request_options is None and client_context is None:
        return None

    if request_options is None:
        request_options = RequestOptions()
    elif isinstance(request_options, dict):
        request_options = RequestOptions(request_options)

    if client_context:
        request_options.client_context = _merge_client_context(
            client_context, request_options.client_context
        )

    return request_options


def _assert_numeric_precision_and_scale(value):
    """
    Asserts that input numeric field is within Spanner supported range.

    Spanner supports fixed 38 digits of precision and 9 digits of scale.
    This number can be optionally prefixed with a plus or minus sign.
    Read more here: https://cloud.google.com/spanner/docs/data-types#numeric_type

    :type value: decimal.Decimal
    :param value: The value to check for Cloud Spanner compatibility.

    :raises NotSupportedError: If value is not within supported precision or scale of Spanner.
    """
    decimal_tuple = value.as_tuple()
    scale = decimal_tuple.exponent
    precision = len(decimal_tuple.digits)

    if scale < -9:
        raise ValueError(NUMERIC_MAX_SCALE_ERR_MSG.format(abs(scale)))
    if precision + scale > 29:
        raise ValueError(NUMERIC_MAX_PRECISION_ERR_MSG.format(precision + scale))


def _datetime_to_rfc3339(value):
    """Format the provided datatime in the RFC 3339 format.

    :type value: datetime.datetime
    :param value: value to format

    :rtype: str
    :returns: RFC 3339 formatted datetime string
    """
    # Convert to UTC and then drop the timezone so we can append "Z" in lieu of
    # allowing isoformat to append the "+00:00" zone offset.
    if value.tzinfo is None:
        value = value.replace(tzinfo=datetime.timezone.utc)
    value = value.astimezone(datetime.timezone.utc).replace(tzinfo=None)
    return value.isoformat(sep="T", timespec="microseconds") + "Z"


def _datetime_to_rfc3339_nanoseconds(value):
    """Format the provided datatime in the RFC 3339 format.

    :type value: datetime_helpers.DatetimeWithNanoseconds
    :param value: value to format

    :rtype: str
    :returns: RFC 3339 formatted datetime string
    """

    if value.nanosecond == 0:
        return _datetime_to_rfc3339(value)
    nanos = str(value.nanosecond).rjust(9, "0").rstrip("0")
    # Convert to UTC and then drop the timezone so we can append "Z" in lieu of
    # allowing isoformat to append the "+00:00" zone offset.
    if value.tzinfo is None:
        value = value.replace(tzinfo=datetime.timezone.utc)
    value = value.astimezone(datetime.timezone.utc).replace(tzinfo=None)
    return "{}.{}Z".format(value.isoformat(sep="T", timespec="seconds"), nanos)


def _make_list_value_pb(values):
    """Construct of ListValue protobufs.

    :type values: list of scalar
    :param values: Row data

    :rtype: :class:`~google.protobuf.struct_pb2.ListValue`
    :returns: protobuf
    """
    return ListValue(values=[_make_value_pb(value) for value in values])


def _encode_float(value):
    if math.isfinite(value):
        return Value(number_value=value)
    if math.isnan(value):
        return Value(string_value="NaN")
    return Value(string_value="Infinity" if value > 0 else "-Infinity")


def _encode_decimal(value):
    _assert_numeric_precision_and_scale(value)
    return Value(string_value=str(value))


def _encode_bytes(value):
    return Value(string_value=_validate_and_decode_bytes(value))


def _encode_json_object(value):
    serialized = value.serialize()
    if serialized is None:
        return Value(null_value=NULL_VALUE)
    return Value(string_value=serialized)


_TYPE_ENCODERS = {
    str: lambda value: Value(string_value=value),
    int: lambda value: Value(string_value=str(value)),
    bool: lambda value: Value(bool_value=value),
    float: _encode_float,
    bytes: _encode_bytes,
    datetime.date: lambda value: Value(string_value=value.isoformat()),
    datetime.datetime: lambda value: Value(string_value=_datetime_to_rfc3339(value)),
    datetime_helpers.DatetimeWithNanoseconds: lambda value: Value(
        string_value=_datetime_to_rfc3339_nanoseconds(value)
    ),
    decimal.Decimal: _encode_decimal,
    uuid.UUID: lambda value: Value(string_value=str(value)),
    Interval: lambda value: Value(string_value=str(value)),
    list: lambda value: Value(list_value=_make_list_value_pb(value)),
    tuple: lambda value: Value(list_value=_make_list_value_pb(value)),
    ListValue: lambda value: Value(list_value=value),
    JsonObject: _encode_json_object,
}


def _make_value_pb(value):
    """Helper for :func:`_make_list_value_pbs`.

    :type value: scalar value
    :param value: value to convert

    :rtype: :class:`~google.protobuf.struct_pb2.Value`
    :returns: value protobufs
    :raises ValueError: if value is not of a known scalar type.
    """
    if value is None:
        return Value(null_value=NULL_VALUE)

    try:
        encoder = _TYPE_ENCODERS[type(value)]
    except KeyError:
        pass
    else:
        return encoder(value)

    # Note: The fallback isinstance chain is retained to support subclasses,
    # custom mock/proxy objects, and dynamic AST inspection in
    # tests/unit/spanner_dbapi/test_partition_helper.py.
    if isinstance(value, (list, tuple)):
        return Value(list_value=_make_list_value_pb(value))
    if isinstance(value, bool):
        return Value(bool_value=value)
    if isinstance(value, int):
        return Value(string_value=str(value))
    if isinstance(value, float):
        return _encode_float(value)
    if isinstance(value, datetime_helpers.DatetimeWithNanoseconds):
        return Value(string_value=_datetime_to_rfc3339_nanoseconds(value))
    if isinstance(value, datetime.datetime):
        return Value(string_value=_datetime_to_rfc3339(value))
    if isinstance(value, datetime.date):
        return Value(string_value=value.isoformat())
    if isinstance(value, bytes):
        return _encode_bytes(value)
    if isinstance(value, str):
        return Value(string_value=value)
    if isinstance(value, ListValue):
        return Value(list_value=value)
    if isinstance(value, decimal.Decimal):
        return _encode_decimal(value)
    if isinstance(value, JsonObject):
        return _encode_json_object(value)
    if isinstance(value, Message):
        serialized = value.SerializeToString()
        if serialized is None:
            return Value(null_value=NULL_VALUE)
        else:
            return Value(string_value=base64.b64encode(serialized).decode("utf-8"))
    if isinstance(value, Interval):
        return Value(string_value=str(value))
    if isinstance(value, uuid.UUID):
        return Value(string_value=str(value))

    raise ValueError("Unknown type: %s" % (value,))


def _make_list_value_pbs(values):
    """Construct a sequence of ListValue protobufs.

    :type values: list of list of scalar
    :param values: Row data

    :rtype: list of :class:`~google.protobuf.struct_pb2.ListValue`
    :returns: sequence of protobufs
    """
    return [_make_list_value_pb(row) for row in values]


def _parse_value_pb(value_pb, field_type, field_name, column_info=None):
    """Convert a Value protobuf to cell data.

    :type value_pb: :class:`~google.protobuf.struct_pb2.Value`
    :param value_pb: protobuf to convert

    :type field_type: :class:`~google.cloud.spanner_v1.types.Type`
    :param field_type: type code for the value

    :type field_name: str
    :param field_name: column name

    :type column_info: dict
    :param column_info: (Optional) dict of column name and column information.
            An object where column names as keys and custom objects as corresponding
            values for deserialization. It's specifically useful for data types like
            protobuf where deserialization logic is on user-specific code. When provided,
            the custom object enables deserialization of backend-received column data.
            If not provided, data remains serialized as bytes for Proto Messages and
            integer for Proto Enums.

    :rtype: varies on field_type
    :returns: value extracted from value_pb
    :raises ValueError: if unknown type is passed
    """
    decoder = _get_type_decoder(field_type, field_name, column_info)
    return _parse_nullable(value_pb, decoder)


_date_fromisoformat = datetime.date.fromisoformat
_Decimal = decimal.Decimal
_json_from_str = JsonObject.from_str
_uuid_UUID = uuid.UUID


def _get_type_decoder(field_type, field_name, column_info=None):
    """Returns a function that converts a Value protobuf to cell data.

    :type field_type: :class:`~google.cloud.spanner_v1.types.Type`
    :param field_type: type code for the value

    :type field_name: str
    :param field_name: column name

    :type column_info: dict
    :param column_info: (Optional) dict of column name and column information.
            An object where column names as keys and custom objects as corresponding
            values for deserialization. It's specifically useful for data types like
            protobuf where deserialization logic is on user-specific code. When provided,
            the custom object enables deserialization of backend-received column data.
            If not provided, data remains serialized as bytes for Proto Messages and
            integer for Proto Enums.

    :rtype: a function that takes a single protobuf value as an input argument
    :returns: a function that can be used to extract a value from a protobuf value
    :raises ValueError: if unknown type is passed
    """

    type_code = field_type.code
    try:
        type_code_integer = int(type_code)
    except (TypeError, ValueError):
        type_code_integer = None

    if type_code_integer in _SCALAR_DECODERS:
        return _SCALAR_DECODERS[type_code_integer]
    elif type_code_integer == _PROTO_TYPE_CODE:
        return lambda value_pb: _parse_proto(value_pb, column_info, field_name)
    elif type_code_integer == _ENUM_TYPE_CODE:
        return lambda value_pb: _parse_proto_enum(value_pb, column_info, field_name)
    elif type_code_integer == _ARRAY_TYPE_CODE:
        element_decoder = _get_type_decoder(
            field_type.array_element_type, field_name, column_info
        )
        return lambda value_pb: _parse_array(value_pb, element_decoder)
    elif type_code_integer == _STRUCT_TYPE_CODE:
        element_decoders = [
            _get_type_decoder(item_field.type_, field_name, column_info)
            for item_field in field_type.struct_type.fields
        ]
        return lambda value_pb: _parse_struct(value_pb, element_decoders)
    else:
        raise ValueError("Unknown type: %s" % (field_type,))


def _parse_list_value_pbs(rows, row_type):
    """Convert a list of ListValue protobufs into a list of list of cell data.

    :type rows: list of :class:`~google.protobuf.struct_pb2.ListValue`
    :param rows: row data returned from a read/query

    :type row_type: :class:`~google.cloud.spanner_v1.types.StructType`
    :param row_type: row schema specification

    :rtype: list of list of cell data
    :returns: data for the rows, coerced into appropriate types
    """
    result = []
    for row in rows:
        row_data = []
        for value_pb, field in zip(row.values, row_type.fields):
            row_data.append(_parse_value_pb(value_pb, field.type_, field.name))
        result.append(row_data)
    return result


def _parse_float(value_pb) -> float:
    # Note: Storing val = value_pb.string_value and doing a truthiness check is faster
    # than calling value_pb.HasField("string_value") because it avoids the C-extension
    # method lookup/call overhead and accesses the attribute only once.
    val = value_pb.string_value
    return float(val) if val else value_pb.number_value


_POWERS_OF_10 = (
    1,
    10,
    100,
    1000,
    10000,
    100000,
    1000000,
    10000000,
    100000000,
    1000000000,
)


def _parse_timestamp(value_pb):
    val = value_pb.string_value
    try:
        if len(val) < 20 or val[10] != "T":
            raise ValueError()
        no_fraction = val[:19]
        bare = datetime.datetime.fromisoformat(no_fraction)
        if val[19] == ".":
            if val.endswith("Z"):
                offset = "Z"
                fraction = val[20:-1]
            elif val[-6] in ("+", "-"):
                offset = val[-6:]
                fraction = val[20:-6]
            else:
                raise ValueError()
            if not fraction or len(fraction) > 9 or not fraction.isdigit():
                raise ValueError()
            scale = 9 - len(fraction)
            nanos = int(fraction) * _POWERS_OF_10[scale]
        else:
            nanos = 0
            if val.endswith("Z"):
                offset = "Z"
            elif val[-6] in ("+", "-"):
                offset = val[-6:]
            else:
                raise ValueError()

        if offset != "Z":
            sign = offset[0]
            hours = int(offset[1:3])
            minutes = int(offset[4:6])
            if offset[3] != ":":
                raise ValueError()
            delta = datetime.timedelta(hours=hours, minutes=minutes)
            if sign == "-":
                delta = -delta
            tzinfo = datetime.timezone(delta)
            bare = bare.replace(tzinfo=tzinfo).astimezone(datetime.timezone.utc)

        return datetime_helpers.DatetimeWithNanoseconds(
            bare.year,
            bare.month,
            bare.day,
            bare.hour,
            bare.minute,
            bare.second,
            nanosecond=nanos,
            tzinfo=datetime.timezone.utc,
        )
    except (IndexError, ValueError) as e:
        raise ValueError("Timestamp: {} does not match pattern".format(val)) from e


def _parse_proto(value_pb, column_info, field_name):
    bytes_value = base64.b64decode(value_pb.string_value)
    if column_info is not None and column_info.get(field_name) is not None:
        default_proto_message = column_info.get(field_name)
        if isinstance(default_proto_message, Message):
            proto_message = type(default_proto_message)()
            try:
                proto_message.ParseFromString(bytes_value)
                return proto_message
            except (DecodeError, RecursionError):
                _LOGGER.warning(
                    "Field could not be parsed as Proto due to excessive nesting/corruption. Returning raw bytes."
                )
                return bytes_value
    return bytes_value


def _parse_proto_enum(value_pb, column_info, field_name):
    int_value = int(value_pb.string_value)
    if column_info is not None and column_info.get(field_name) is not None:
        proto_enum = column_info.get(field_name)
        if isinstance(proto_enum, EnumTypeWrapper):
            return proto_enum.Name(int_value)
    return int_value


def _parse_array(value_pb, element_decoder) -> []:
    return [
        _parse_nullable(item_pb, element_decoder)
        for item_pb in value_pb.list_value.values
    ]


def _parse_struct(value_pb, element_decoders):
    return [
        _parse_nullable(item_pb, element_decoders[i])
        for (i, item_pb) in enumerate(value_pb.list_value.values)
    ]


def _parse_nullable(value_pb, decoder):
    if value_pb.HasField("null_value"):
        return None
    else:
        return decoder(value_pb)


def _parse_interval(value_pb):
    """Parse a Value protobuf containing an interval."""
    if hasattr(value_pb, "string_value"):
        return Interval.from_str(value_pb.string_value)
    return Interval.from_str(value_pb)


# Note: STRING and BOOL use operator.attrgetter because direct attribute extraction
# is faster in Python. Other types require type transformation, so they use lambdas.
_SCALAR_DECODERS = {
    int(TypeCode.STRING): operator.attrgetter("string_value"),
    int(TypeCode.BYTES): lambda value_pb: value_pb.string_value.encode("utf8"),
    int(TypeCode.BOOL): operator.attrgetter("bool_value"),
    int(TypeCode.INT64): lambda value_pb: int(value_pb.string_value),
    int(TypeCode.FLOAT64): _parse_float,
    int(TypeCode.FLOAT32): _parse_float,
    int(TypeCode.DATE): lambda value_pb: _date_fromisoformat(value_pb.string_value),
    int(TypeCode.TIMESTAMP): _parse_timestamp,
    int(TypeCode.NUMERIC): lambda value_pb: _Decimal(value_pb.string_value),
    int(TypeCode.JSON): lambda value_pb: _json_from_str(value_pb.string_value),
    int(TypeCode.UUID): lambda value_pb: _uuid_UUID(value_pb.string_value),
    int(TypeCode.INTERVAL): _parse_interval,
}

_PROTO_TYPE_CODE = int(TypeCode.PROTO)
_ENUM_TYPE_CODE = int(TypeCode.ENUM)
_ARRAY_TYPE_CODE = int(TypeCode.ARRAY)
_STRUCT_TYPE_CODE = int(TypeCode.STRUCT)


def _resource_info_from_database(database):
    """Resource information dictionary from database instance or fallback."""
    if database is None:
        return None
    resource_info = getattr(database, "_resource_info", None)
    if resource_info is not None:
        return resource_info
    instance = getattr(database, "_instance", None)
    client = getattr(instance, "_client", None) if instance else None
    return {
        "project": getattr(client, "project", None),
        "instance": getattr(instance, "instance_id", None),
        "database": getattr(database, "database_id", None),
    }


class _SessionWrapper(object):
    """Base class for objects wrapping a session.

    :type session: :class:`~google.cloud.spanner_v1.session.Session`
    :param session: the session used to perform the commit
    """

    def __init__(self, session):
        self._session = session

    @property
    def _resource_info(self):
        """Resource information for metrics labels."""
        session = self._session
        database = getattr(session, "_database", None) if session is not None else None
        return _resource_info_from_database(database)


def _append_routing_headers(metadata):
    """Appends routing and backend-specific headers to the metadata."""
    if ENABLE_AFE_SERVER_TIMING:
        metadata.append(("x-goog-spanner-enable-afe-server-timing", "true"))
    return metadata


def _metadata_with_prefix(prefix, **kw):
    """Create RPC metadata containing a prefix.

    Args:
        prefix (str): appropriate resource path.

    Returns:
        List[Tuple[str, str]]: RPC metadata with supplied prefix
    """
    metadata = [("google-cloud-resource-prefix", prefix)]
    return _append_routing_headers(metadata)


def _retry_on_aborted_exception(
    func,
    deadline,
    default_retry_delay=None,
):
    """
    Handles retry logic for Aborted exceptions, considering the deadline.
    """
    attempts = 0
    while True:
        try:
            attempts += 1
            return func()
        except Aborted as exc:
            _delay_until_retry(
                exc,
                deadline=deadline,
                attempts=attempts,
                default_retry_delay=default_retry_delay,
            )
            continue


def _retry(
    func,
    retry_count=5,
    delay=2,
    allowed_exceptions=None,
    before_next_retry=None,
):
    """
    Retry a function with a specified number of retries, delay between retries, and list of allowed exceptions.

    Args:
        func: The function to be retried.
        retry_count: The maximum number of times to retry the function.
        delay: The delay in seconds between retries.
        allowed_exceptions: A tuple of exceptions that are allowed to occur without triggering a retry.
                            Passing allowed_exceptions as None will lead to retrying for all exceptions.

    Returns:
        The result of the function if it is successful, or raises the last exception if all retries fail.
    """
    retries = 0
    while retries <= retry_count:
        if retries > 0 and before_next_retry:
            before_next_retry(retries, delay)

        try:
            return func()
        except Exception as exc:
            is_allowed = (
                allowed_exceptions is None or exc.__class__ in allowed_exceptions
            )

            if is_allowed and retries < retry_count:
                if (
                    allowed_exceptions is not None
                    and allowed_exceptions[exc.__class__] is not None
                ):
                    allowed_exceptions[exc.__class__](exc)
                time.sleep(delay)
                delay = delay * 2
                retries = retries + 1
            else:
                raise exc


def _check_rst_stream_error(exc):
    resumable_error = any(
        resumable_message in exc.message
        for resumable_message in (
            "RST_STREAM",
            "Received unexpected EOS on DATA frame from server",
        )
    )
    if not resumable_error:
        raise
    return True


def _metadata_with_leader_aware_routing(value, **kw):
    """Create RPC metadata containing a leader aware routing header

    Args:
        value (bool): header value

    Returns:
        List[Tuple[str, str]]: RPC metadata with leader aware routing header
    """
    return ("x-goog-spanner-route-to-leader", str(value).lower())


def _metadata_with_span_context(metadata: List[Tuple[str, str]], **kw) -> None:
    """
    Appends metadata with end to end tracing header and OpenTelemetry span context .

    Args:
        metadata (list[tuple[str, str]]): The metadata carrier where the OpenTelemetry context
                                          should be injected.
    Returns:
        None
    """
    if HAS_OPENTELEMETRY_INSTALLED and metadata is not None:
        metadata.append(("x-goog-spanner-end-to-end-tracing", "true"))
        inject(setter=OpenTelemetryContextSetter(), carrier=metadata)


def _delay_until_retry(exc, deadline, attempts, default_retry_delay=None):
    """Helper for :meth:`Session.run_in_transaction`.

    Detect retryable abort, and impose server-supplied delay.

    :type exc: :class:`google.api_core.exceptions.Aborted`
    :param exc: exception for aborted transaction

    :type deadline: float
    :param deadline: maximum timestamp to continue retrying the transaction.

    :type attempts: int
    :param attempts: number of call retries
    """

    errors = getattr(exc, "errors", None)
    cause = errors[0] if errors else exc
    now = time.time()
    if now >= deadline:
        raise

    delay = _get_retry_delay(cause, attempts, default_retry_delay=default_retry_delay)
    if delay is not None:
        if now + delay > deadline:
            raise

        time.sleep(delay)


def _get_retry_delay(cause, attempts, default_retry_delay=None):
    """Helper for :func:`_delay_until_retry`.

    :type exc: :class:`grpc.Call`
    :param exc: exception for aborted transaction

    :rtype: float
    :returns: seconds to wait before retrying the transaction.

    :type attempts: int
    :param attempts: number of call retries
    """
    if hasattr(cause, "trailing_metadata"):
        metadata = dict(cause.trailing_metadata())
    else:
        metadata = {}
    retry_info_pb = metadata.get("google.rpc.retryinfo-bin")
    if retry_info_pb is not None:
        retry_info = RetryInfo()
        retry_info.ParseFromString(retry_info_pb)
        nanos = retry_info.retry_delay.nanos
        return retry_info.retry_delay.seconds + nanos / 1.0e9
    if default_retry_delay is not None:
        return default_retry_delay

    return 2**attempts + random.random()


class AtomicCounter:
    __slots__ = ("__lock", "__value")

    def __init__(self, start_value=0):
        self.__lock = threading.Lock()
        self.__value = start_value

    @property
    def value(self):
        with self.__lock:
            return self.__value

    def increment(self, n=1):
        with self.__lock:
            self.__value += n
            return self.__value

    def __iadd__(self, n):
        """
        Defines the inplace += operator result.
        """
        with self.__lock:
            self.__value += n
            return self

    def __add__(self, n):
        """
        Defines the result of invoking: value = AtomicCounter + addable
        """
        with self.__lock:
            n += self.__value
            return n

    def __radd__(self, n):
        """
        Defines the result of invoking: value = addable + AtomicCounter
        """
        return self.__add__(n)

    def reset(self):
        with self.__lock:
            self.__value = 0


def _metadata_with_request_id(
    client_id, channel_id, nth_request, attempt, other_metadata=None, span=None
):
    """Return metadata with request ID header.

    This function returns only the metadata list (not a tuple),
    maintaining backward compatibility with existing code.

    Args:
        client_id: The client identifier.
        channel_id: The channel identifier.
        nth_request: The request sequence number.
        attempt: The attempt sequence number.
        other_metadata: Prior metadata list.
        span: Optional trace span.

    Returns:
        list: gRPC metadata with request ID header
    """
    return with_request_id_metadata_only(
        client_id, channel_id, nth_request, attempt, other_metadata, span
    )


def _metadata_with_request_id_and_req_id(
    client_id, channel_id, nth_request, attempt, other_metadata=None, span=None
):
    """Return both metadata and request ID string.

    This is used when we need to augment errors with the request ID.

    Args:
        client_id: The client identifier.
        channel_id: The channel identifier.
        nth_request: The request sequence number.
        attempt: The attempt sequence number.
        other_metadata: Prior metadata list.
        span: Optional trace span.

    Returns:
        tuple: (metadata, request_id)
    """
    return with_request_id(
        client_id, channel_id, nth_request, attempt, other_metadata, span
    )


def _augment_error_with_request_id(error, request_id=None):
    """Augment an error with request ID information.

    Args:
        error: The error to augment (typically GoogleAPICallError)
        request_id (str): The request ID to include

    Returns:
        The augmented error with request ID information
    """
    return wrap_with_request_id(error, request_id)


class _augment_errors_with_request_id:
    """Context manager to augment exceptions with request ID."""

    __slots__ = ("_request_id",)

    def __init__(self, request_id):
        self._request_id = request_id

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None:
            _augment_error_with_request_id(exc_val, self._request_id)
        return False


def _merge_Transaction_Options(
    defaultTransactionOptions: TransactionOptions,
    mergeTransactionOptions: TransactionOptions,
) -> TransactionOptions:
    """Merges two TransactionOptions objects.

    - Values from `mergeTransactionOptions` take precedence if set.
    - Values from `defaultTransactionOptions` are used only if missing.

    Args:
        defaultTransactionOptions (TransactionOptions): The default transaction options (fallback values).
        mergeTransactionOptions (TransactionOptions): The main transaction options (overrides when set).

    Returns:
        TransactionOptions: A merged TransactionOptions object.
    """

    if defaultTransactionOptions is None:
        return mergeTransactionOptions

    if mergeTransactionOptions is None:
        return defaultTransactionOptions

    merged_pb = TransactionOptions()._pb  # Create a new protobuf object

    # Merge defaultTransactionOptions first
    merged_pb.MergeFrom(defaultTransactionOptions._pb)

    # Merge transactionOptions, ensuring it overrides default values
    merged_pb.MergeFrom(mergeTransactionOptions._pb)

    # Convert protobuf object back into a TransactionOptions instance
    return TransactionOptions(merged_pb)


def _create_spanner_omni_transport(
    transport_factory,
    host,
    use_plain_text,
    ca_certificate,
    client_certificate,
    client_key,
    interceptors=None,
    credentials=None,
):
    """Creates a Spanner Omni transport.

    Args:
        transport_factory (type): The transport class to instantiate (e.g.
            `SpannerGrpcTransport`).
        host (str): The endpoint for Spanner Omni.
        use_plain_text (bool): Whether to use a plain text (insecure) connection.
        ca_certificate (str): Path to the CA certificate file for TLS.
        client_certificate (str): Path to the client certificate file for mTLS.
        client_key (str): Path to the client key file for mTLS.
        interceptors (list): Optional list of interceptors to add to the channel.
        credentials (google.auth.credentials.Credentials, optional): Credentials
            to use for authentication (e.g. `SpannerOmniCredentials`).

    Returns:
        object: An instance of the transport class created by `transport_factory`.

    Raises:
        ValueError: If TLS/mTLS configuration is invalid.
    """
    import grpc
    from google.auth.credentials import AnonymousCredentials

    channel = None
    all_interceptors = list(interceptors) if interceptors is not None else []
    if credentials is not None and hasattr(credentials, "create_auth_interceptor"):
        all_interceptors.append(credentials.create_auth_interceptor())

    if use_plain_text:
        channel = grpc.insecure_channel(target=host)
    elif ca_certificate:
        with open(ca_certificate, "rb") as f:
            ca_cert = f.read()
        if client_certificate and client_key:
            with open(client_certificate, "rb") as f:
                client_cert = f.read()
            with open(client_key, "rb") as f:
                private_key = f.read()
            ssl_creds = grpc.ssl_channel_credentials(
                root_certificates=ca_cert,
                private_key=private_key,
                certificate_chain=client_cert,
            )
        elif client_certificate or client_key:
            raise ValueError(
                "Both client_certificate and client_key must be provided for mTLS connection"
            )
        else:
            ssl_creds = grpc.ssl_channel_credentials(root_certificates=ca_cert)
        channel = grpc.secure_channel(host, ssl_creds)
    else:
        raise ValueError(
            "TLS/mTLS connection requires ca_certificate to be set for Spanner Omni"
        )
    if all_interceptors:
        channel = grpc.intercept_channel(channel, *all_interceptors)
    actual_credentials = (
        credentials if credentials is not None else AnonymousCredentials()
    )
    return transport_factory(channel=channel, credentials=actual_credentials)


def _create_experimental_host_transport(
    transport_factory,
    experimental_host,
    use_plain_text,
    ca_certificate,
    client_certificate,
    client_key,
    interceptors=None,
):
    """Deprecated alias for _create_spanner_omni_transport."""
    import warnings

    warnings.warn(
        "_create_experimental_host_transport is deprecated. Please use _create_spanner_omni_transport instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return _create_spanner_omni_transport(
        transport_factory,
        experimental_host,
        use_plain_text,
        ca_certificate,
        client_certificate,
        client_key,
        interceptors=interceptors,
    )


_STREAM_DRAIN_QUEUE_SIZE = 512
_STREAM_DRAIN_WORKER_COUNT = 8


class _BoundedStreamDrainer:
    """Bounded background drainer for synchronous gRPC streams.

    Uses a fixed pool of daemon worker threads and a bounded queue to drain
    completed streams to EOF, allowing callers to return early upon seeing
    PartialResultSet.last without blocking on trailing gRPC frames.
    """

    def __init__(
        self,
        queue_size: int = _STREAM_DRAIN_QUEUE_SIZE,
        worker_count: int = _STREAM_DRAIN_WORKER_COUNT,
    ):
        self._queue_size = queue_size
        self._worker_count = worker_count
        self._lock = threading.RLock()
        self._reset()

    def _reset(self):
        self._queue = queue.Queue(maxsize=self._queue_size)
        self._started = False
        self._stopped = False
        self._workers = []

    def _reset_after_fork(self):
        self._lock = threading.RLock()
        self._reset()

    def _ensure_started(self):
        if not self._started and not self._stopped:
            with self._lock:
                if not self._started and not self._stopped:
                    self._started = True
                    try:
                        for index in range(self._worker_count):
                            worker = threading.Thread(
                                target=self._worker_loop,
                                name=f"spanner-stream-drainer-{index}",
                                daemon=True,
                            )
                            worker.start()
                            self._workers.append(worker)
                    except Exception:
                        if not self._workers:
                            self._started = False
                        raise

    def _worker_loop(self):
        while True:
            iterator = self._queue.get()
            if iterator is None:
                self._queue.task_done()
                break
            try:
                for _ in iterator:
                    pass
            except Exception:
                pass
            finally:
                self._queue.task_done()

    def drain(self, iterator):
        if iterator is None:
            return

        with self._lock:
            if not self._stopped:
                try:
                    self._ensure_started()
                    self._queue.put_nowait(iterator)
                    return
                except Exception:
                    # Under extreme bursts where the queue is temporarily full, or if thread
                    # creation fails (e.g. in restricted environments or during shutdown),
                    # fall through to drain inline on the caller thread.
                    pass

        # If already shut down or during interpreter exit, or if the queue is full,
        # drain inline on caller thread rather than cancelling a successful query.
        # Because trailers are delivered in sub-millisecond time (<0.5ms),
        # inline draining adds negligible latency while guaranteeing status OK.
        try:
            for _ in iterator:
                pass
        except Exception:
            pass

    def shutdown(self, timeout: float = 0.5):
        """Cleanly terminate worker threads during interpreter shutdown.

        This is a best-effort cleanup at interpreter exit bounded by ``timeout``
        seconds across all workers.
        """
        with self._lock:
            if self._stopped:
                return
            self._stopped = True

        if self._started:
            deadline = time.monotonic() + timeout
            for _ in range(len(self._workers)):
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    break
                try:
                    self._queue.put(None, timeout=remaining)
                except queue.Full:
                    break

            for worker in self._workers:
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    break
                worker.join(timeout=remaining)


_GLOBAL_STREAM_DRAINER = _BoundedStreamDrainer()
atexit.register(_GLOBAL_STREAM_DRAINER.shutdown)
if hasattr(os, "register_at_fork"):
    os.register_at_fork(after_in_child=_GLOBAL_STREAM_DRAINER._reset_after_fork)


def _drain_stream(iterator):
    """Drain a stream iterator to EOF in the background.

    Called when PartialResultSet.last is True to allow the caller to return immediately
    while consuming trailing gRPC metadata so the stream terminates cleanly with status OK.
    """
    _GLOBAL_STREAM_DRAINER.drain(iterator)
