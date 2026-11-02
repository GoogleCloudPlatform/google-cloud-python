# -*- coding: utf-8 -*-
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""System tests for reading rows with pandas connector."""

import numpy
import pyarrow.types
import pytest


def test_read_rows_to_arrow(client_and_types, project_id):
    client, types = client_and_types
    read_session = types.ReadSession()
    read_session.table = "projects/{}/datasets/{}/tables/{}".format(
        "bigquery-public-data", "new_york_citibike", "citibike_stations"
    )

    read_session.read_options.selected_fields.append("latitude")
    read_session.read_options.selected_fields.append("longitude")
    read_session.read_options.selected_fields.append("name")
    read_session.read_options.selected_fields.append("num_bikes_available")
    read_session.data_format = types.DataFormat.ARROW

    session = client.create_read_session(
        request={
            "parent": "projects/{}".format(project_id),
            "read_session": read_session,
            "max_stream_count": 1,
        }
    )

    assert len(session.streams) == 1

    streamname = session.streams[0].name

    tbl = client.read_rows(streamname, offset=0).to_arrow(session)

    assert tbl.num_columns == 4
    schema = tbl.schema
    # Use field with a name specifier as there may be ordering differences
    # when selected_fields is used
    assert pyarrow.types.is_float64(schema.field("latitude").type)
    assert pyarrow.types.is_float64(schema.field("longitude").type)
    assert pyarrow.types.is_string(schema.field("name").type)
    assert pyarrow.types.is_int64(schema.field("num_bikes_available").type)


@pytest.mark.parametrize(
    "data_format,expected_schema_type",
    (("AVRO", "avro_schema"), ("ARROW", "arrow_schema")),
)
def test_read_rows_to_dataframe(
    client_and_types, project_id, data_format, expected_schema_type
):
    client, types = client_and_types
    read_session = types.ReadSession()
    read_session.table = "projects/{}/datasets/{}/tables/{}".format(
        "bigquery-public-data", "new_york_citibike", "citibike_stations"
    )
    read_session.data_format = data_format

    session = client.create_read_session(
        request={
            "parent": "projects/{}".format(project_id),
            "read_session": read_session,
            "max_stream_count": 1,
        }
    )
    schema_type = session._pb.WhichOneof("schema")
    assert schema_type == expected_schema_type

    stream = session.streams[0].name

    frame = client.read_rows(stream).to_dataframe(
        session, dtypes={"latitude": numpy.float16}
    )

    assert frame.latitude.dtype.name == "float16"
    assert frame.longitude.dtype.name == "float64"
    assert frame["name"].str.startswith("Central Park").any()
    assert frame.num_bikes_available.dtype.name == "int64"
