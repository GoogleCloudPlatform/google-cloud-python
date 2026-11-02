# Spanner SQLAlchemy Samples

This folder contains samples for how to use common Spanner features with SQLAlchemy. The samples use
a shared [data model](model.py) and can be executed as a standalone application. The samples
automatically start the [Spanner Emulator](https://cloud.google.com/spanner/docs/emulator) in a
Docker container when they are executed. You must therefore have Docker installed on your system to
run a sample.

You can run a sample with `nox`:

```shell
nox -s hello_world
```

Change `hello_world` to run any of the other sample names. The runnable samples all end with
`_sample.py`. Omit the `_sample.py` part of the file name to run the sample.



| Sample name           | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| bit_reversed_sequence | Use a bit-reversed sequence for primary key generation.                     |
| date_and_timestamp    | Map Spanner DATE and TIMESTAMP columns to SQLAlchemy.                       |
| default_column_value  | Create and use a Spanner DEFAULT column constraint in SQLAlchemy.           |
| generated_column      | Create and use a Spanner generated column in SQLAlchemy.                    |
| hello_world           | Shows how to connect to Spanner with SQLAlchemy and execute a simple query. |
| insert_data           | Insert multiple rows to Spanner with SQLAlchemy.                            |
| interleaved_table     | Create and use an interleaved table (INTERLEAVE IN PARENT) with SQLAlchemy. |
| transaction           | Execute a read/write transaction on Spanner with SQLAlchemy.                |

