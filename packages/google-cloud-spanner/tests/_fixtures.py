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

"""Test fixtures."""

DDL = """\
CREATE TABLE contacts (
    contact_id INT64,
    first_name STRING(1024),
    last_name STRING(1024),
    email STRING(1024) )
    PRIMARY KEY (contact_id);
CREATE TABLE contact_phones (
    contact_id INT64,
    phone_type STRING(1024),
    phone_number STRING(1024) )
    PRIMARY KEY (contact_id, phone_type),
    INTERLEAVE IN PARENT contacts ON DELETE CASCADE;
CREATE PROTO BUNDLE (
    examples.spanner.music.SingerInfo,
    examples.spanner.music.Genre,
    );
CREATE TABLE all_types (
    pkey INT64 NOT NULL,
    int_value INT64,
    int_array ARRAY<INT64>,
    bool_value BOOL,
    bool_array ARRAY<BOOL>,
    bytes_value BYTES(16),
    bytes_array ARRAY<BYTES(16)>,
    date_value DATE,
    date_array ARRAY<DATE>,
    float_value FLOAT64,
    float_array ARRAY<FLOAT64>,
    string_value STRING(16),
    string_array ARRAY<STRING(16)>,
    timestamp_value TIMESTAMP,
    timestamp_array ARRAY<TIMESTAMP>,
    numeric_value NUMERIC,
    numeric_array ARRAY<NUMERIC>,
    json_value JSON,
    json_array ARRAY<JSON>,
    proto_message_value examples.spanner.music.SingerInfo,
    proto_message_array ARRAY<examples.spanner.music.SingerInfo>,
    proto_enum_value examples.spanner.music.Genre,
    proto_enum_array ARRAY<examples.spanner.music.Genre>,
    )
    PRIMARY KEY (pkey);
CREATE TABLE counters (
    name STRING(1024),
    value INT64 )
    PRIMARY KEY (name);
CREATE TABLE string_plus_array_of_string (
    id INT64,
    name STRING(16),
    tags ARRAY<STRING(16)> )
    PRIMARY KEY (id);
CREATE INDEX name ON contacts(first_name, last_name);
CREATE INDEX contacts_by_last_name ON contacts(last_name);
CREATE TABLE singers (
     singer_id   INT64 NOT NULL,
     first_name  STRING(1024),
     last_name   STRING(1024),
     singer_info examples.spanner.music.SingerInfo,
     singer_genre examples.spanner.music.Genre, )
     PRIMARY KEY (singer_id);
CREATE INDEX SingerByGenre ON singers(singer_genre) STORING (first_name, last_name);
CREATE TABLE IntervalTable (
    key STRING(MAX),
    create_time TIMESTAMP,
    expiry_time TIMESTAMP,
    expiry_within_month bool AS (expiry_time - create_time < INTERVAL 30 DAY),
    interval_array_len INT64 AS (ARRAY_LENGTH(ARRAY<INTERVAL>[INTERVAL '1-2 3 4:5:6' YEAR TO SECOND]))
) PRIMARY KEY (key);
CREATE TABLE users_history (
     id INT64 NOT NULL,
     commit_ts TIMESTAMP NOT NULL OPTIONS
        (allow_commit_timestamp=true),
     name STRING(MAX) NOT NULL,
     email STRING(MAX),
     deleted BOOL NOT NULL )
     PRIMARY KEY(id, commit_ts DESC);

CREATE TABLE Customers (
    CustomerId INT64 NOT NULL,
    CustomerName STRING(62) NOT NULL,
    ) PRIMARY KEY (CustomerId);

    CREATE TABLE ShoppingCarts (
    CartId INT64 NOT NULL,
    CustomerId INT64 NOT NULL,
    CustomerName STRING(62) NOT NULL,
    CONSTRAINT FKShoppingCartsCustomerId FOREIGN KEY (CustomerId)
    REFERENCES Customers (CustomerId) ON DELETE CASCADE
    ) PRIMARY KEY (CartId);
"""

EMULATOR_DDL = """\
CREATE TABLE contacts (
    contact_id INT64,
    first_name STRING(1024),
    last_name STRING(1024),
    email STRING(1024) )
    PRIMARY KEY (contact_id);
CREATE TABLE contact_phones (
    contact_id INT64,
    phone_type STRING(1024),
    phone_number STRING(1024) )
    PRIMARY KEY (contact_id, phone_type),
    INTERLEAVE IN PARENT contacts ON DELETE CASCADE;
CREATE PROTO BUNDLE (
    examples.spanner.music.SingerInfo,
    examples.spanner.music.Genre,
    );
CREATE TABLE all_types (
    pkey INT64 NOT NULL,
    int_value INT64,
    int_array ARRAY<INT64>,
    bool_value BOOL,
    bool_array ARRAY<BOOL>,
    bytes_value BYTES(16),
    bytes_array ARRAY<BYTES(16)>,
    date_value DATE,
    date_array ARRAY<DATE>,
    float_value FLOAT64,
    float_array ARRAY<FLOAT64>,
    string_value STRING(16),
    string_array ARRAY<STRING(16)>,
    timestamp_value TIMESTAMP,
    timestamp_array ARRAY<TIMESTAMP>)
    PRIMARY KEY (pkey);
CREATE TABLE counters (
    name STRING(1024),
    value INT64 )
    PRIMARY KEY (name);
CREATE TABLE string_plus_array_of_string (
    id INT64,
    name STRING(16),
    tags ARRAY<STRING(16)> )
    PRIMARY KEY (id);
CREATE INDEX name ON contacts(first_name, last_name);
CREATE INDEX contacts_by_last_name ON contacts(last_name);
CREATE TABLE singers (
     singer_id   INT64 NOT NULL,
     first_name  STRING(1024),
     last_name   STRING(1024),
     singer_info examples.spanner.music.SingerInfo,
     singer_genre examples.spanner.music.Genre, )
     PRIMARY KEY (singer_id);
CREATE INDEX SingerByGenre ON singers(singer_genre) STORING (first_name, last_name);
CREATE TABLE users_history (
     id INT64 NOT NULL,
     commit_ts TIMESTAMP NOT NULL OPTIONS
        (allow_commit_timestamp=true),
     name STRING(MAX) NOT NULL,
     email STRING(MAX),
     deleted BOOL NOT NULL )
     PRIMARY KEY(id, commit_ts DESC);
"""

PG_DDL = """\
CREATE TABLE contacts (
    contact_id BIGINT,
    first_name VARCHAR(1024),
    last_name VARCHAR(1024),
    email VARCHAR(1024),
    PRIMARY KEY (contact_id) );
CREATE TABLE all_types (
    pkey BIGINT NOT NULL,
    int_value INT,
    int_array INT[],
    bool_value BOOL,
    bool_array BOOL[],
    bytes_value BYTEA,
    bytes_array BYTEA[],
    float_value DOUBLE PRECISION,
    float_array DOUBLE PRECISION[],
    string_value VARCHAR(16),
    string_array VARCHAR(16)[],
    date_value DATE,
    date_array DATE[],
    timestamp_value TIMESTAMPTZ,
    timestamp_array TIMESTAMPTZ[],
    numeric_value NUMERIC,
    numeric_array NUMERIC[],
    jsonb_value JSONB,
    jsonb_array JSONB[],
    PRIMARY KEY (pkey) );
CREATE TABLE counters (
    name VARCHAR(1024),
    value BIGINT,
    PRIMARY KEY (name));
CREATE TABLE string_plus_array_of_string (
    id BIGINT,
    name VARCHAR(16),
    PRIMARY KEY (id));
CREATE INDEX name ON contacts(first_name, last_name);
CREATE INDEX contacts_by_last_name ON contacts(last_name);
CREATE TABLE IntervalTable (
    key text primary key,
    create_time timestamptz,
    expiry_time timestamptz,
    expiry_within_month bool GENERATED ALWAYS AS (expiry_time - create_time < INTERVAL '30' DAY) STORED,
    interval_array_len bigint GENERATED ALWAYS AS (ARRAY_LENGTH(ARRAY[INTERVAL '1-2 3 4:5:6'], 1)) STORED
);
CREATE TABLE Customers (
    CustomerId BIGINT,
    CustomerName VARCHAR(62) NOT NULL,
    PRIMARY KEY (CustomerId));

    CREATE TABLE ShoppingCarts (
    CartId BIGINT,
    CustomerId BIGINT NOT NULL,
    CustomerName VARCHAR(62) NOT NULL,
    CONSTRAINT "FKShoppingCartsCustomerId" FOREIGN KEY (CustomerId)
    REFERENCES Customers (CustomerId) ON DELETE CASCADE,
    PRIMARY KEY (CartId)
    );
"""

PROTO_COLUMNS_DDL = """\
CREATE TABLE singers (
     singer_id   INT64 NOT NULL,
     first_name  STRING(1024),
     last_name   STRING(1024),
     singer_info examples.spanner.music.SingerInfo,
     singer_genre examples.spanner.music.Genre, )
     PRIMARY KEY (singer_id);
CREATE INDEX SingerByGenre ON singers(singer_genre) STORING (first_name, last_name);
"""

DDL_STATEMENTS = [stmt.strip() for stmt in DDL.split(";") if stmt.strip()]
EMULATOR_DDL_STATEMENTS = [
    stmt.strip() for stmt in EMULATOR_DDL.split(";") if stmt.strip()
]
PG_DDL_STATEMENTS = [stmt.strip() for stmt in PG_DDL.split(";") if stmt.strip()]
PROTO_COLUMNS_DDL_STATEMENTS = [
    stmt.strip() for stmt in PROTO_COLUMNS_DDL.split(";") if stmt.strip()
]
