# Copyright 2023 Google LLC All rights reserved.
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

import base64
import copy
import datetime
import gzip
import json
from dataclasses import dataclass
from typing import Any

from google.protobuf.json_format import MessageToDict, ParseDict
from google.protobuf.message import Message
from google.protobuf.struct_pb2 import Struct

from google.cloud.spanner_v1 import BatchTransactionId
from google.cloud.spanner_v1._helpers import _make_value_pb
from google.cloud.spanner_v1.types import DirectedReadOptions, ExecuteSqlRequest, Type

_PROTO_CLASS_MAP = {
    "QueryOptions": ExecuteSqlRequest.QueryOptions,
    "DirectedReadOptions": DirectedReadOptions,
    "Struct": Struct,
    "Type": Type,
}


def _serialize_value(val: Any) -> Any:
    if isinstance(val, bytes):
        return {"__type__": "bytes", "value": base64.b64encode(val).decode("utf-8")}
    elif isinstance(val, datetime.datetime):
        return {"__type__": "datetime", "value": val.isoformat()}
    elif hasattr(val, "_pb"):
        return {
            "__type__": "protobuf",
            "class": val.__class__.__name__,
            "value": MessageToDict(val._pb, preserving_proto_field_name=True),
        }
    elif isinstance(val, Message):
        return {
            "__type__": "protobuf",
            "class": val.__class__.__name__,
            "value": MessageToDict(val, preserving_proto_field_name=True),
        }
    elif isinstance(val, dict):
        return {k: _serialize_value(v) for k, v in val.items()}
    elif isinstance(val, list):
        return [_serialize_value(v) for v in val]
    elif isinstance(val, tuple):
        return {"__type__": "tuple", "value": [_serialize_value(v) for v in val]}
    return val


def _deserialize_value(val: Any) -> Any:
    if isinstance(val, dict):
        if "__type__" in val:
            t = val["__type__"]
            if t == "bytes":
                return base64.b64decode(val["value"])
            elif t == "datetime":
                dt_str = val["value"]
                if dt_str.endswith("Z"):
                    dt_str = dt_str[:-1] + "+00:00"
                return datetime.datetime.fromisoformat(dt_str)
            elif t == "tuple":
                return tuple(_deserialize_value(x) for x in val["value"])
            elif t == "protobuf":
                cls_name = val.get("class")
                dict_val = val["value"]
                if cls_name in _PROTO_CLASS_MAP:
                    cls = _PROTO_CLASS_MAP[cls_name]
                    msg = cls()._pb if hasattr(cls(), "_pb") else cls()
                    ParseDict(dict_val, msg)
                    return cls(msg) if hasattr(cls(), "_pb") else msg
                return _deserialize_value(dict_val)
        return {k: _deserialize_value(v) for k, v in val.items()}
    elif isinstance(val, list):
        return [_deserialize_value(v) for v in val]
    return val


def decode_from_string(encoded_partition_id):
    gzip_bytes = base64.b64decode(bytes(encoded_partition_id, "utf-8"))
    partition_id_bytes = gzip.decompress(gzip_bytes)

    data = json.loads(partition_id_bytes.decode("utf-8"))
    btid_data = data["batch_transaction_id"]
    btid = BatchTransactionId(
        transaction_id=_deserialize_value(btid_data["transaction_id"]),
        session_id=btid_data["session_id"],
        read_timestamp=_deserialize_value(btid_data["read_timestamp"]),
    )
    partition_result = _deserialize_value(data["partition_result"])

    # Post-process query params back from Protobuf Struct to Python primitives
    if "query" in partition_result and "params" in partition_result["query"]:
        params_pb = partition_result["query"]["params"]
        if params_pb:
            partition_result["query"]["params"] = MessageToDict(params_pb)

    return PartitionId(btid, partition_result)


def encode_to_string(batch_transaction_id, partition_result):
    # Copy to avoid modifying the caller's dictionary in connection.py
    partition_result = copy.deepcopy(partition_result)

    # Pre-process query params into a Protobuf Struct
    if "query" in partition_result and "params" in partition_result["query"]:
        params = partition_result["query"]["params"]
        if params:
            params_pb = Struct(fields={k: _make_value_pb(v) for k, v in params.items()})
            partition_result["query"]["params"] = params_pb

    data = {
        "batch_transaction_id": {
            "transaction_id": _serialize_value(batch_transaction_id.transaction_id),
            "session_id": batch_transaction_id.session_id,
            "read_timestamp": _serialize_value(batch_transaction_id.read_timestamp),
        },
        "partition_result": _serialize_value(partition_result),
    }

    partition_id_bytes = json.dumps(data).encode("utf-8")
    gzip_bytes = gzip.compress(partition_id_bytes)
    return str(base64.b64encode(gzip_bytes), "utf-8")


@dataclass
class PartitionId:
    batch_transaction_id: BatchTransactionId
    partition_result: Any
