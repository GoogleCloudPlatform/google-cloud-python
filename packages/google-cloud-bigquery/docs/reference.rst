API Reference
~~~~~~~~~~~~~

The main concepts with this API are:

- :class:`~google.cloud.bigquery.client.Client` manages connections to the
  BigQuery API. Use the client methods to run jobs (such as a
  :class:`~google.cloud.bigquery.job.QueryJob` via
  :meth:`~google.cloud.bigquery.client.Client.query`) and manage resources.

- :class:`~google.cloud.bigquery.dataset.Dataset` represents a
  collection of tables.

- :class:`~google.cloud.bigquery.table.Table` represents a single "relation".

Client
======

.. automodule:: google.cloud.bigquery.client

Job
===

.. automodule:: google.cloud.bigquery.job
   :inherited-members:

.. toctree::
  :maxdepth: 2

  job_base


Dataset
=======

.. automodule:: google.cloud.bigquery.dataset


Table
=====

.. automodule:: google.cloud.bigquery.table

Model
=====

.. automodule:: google.cloud.bigquery.model

Routine
=======

.. automodule:: google.cloud.bigquery.routine

Schema
======

.. automodule:: google.cloud.bigquery.schema

Query
=====

.. toctree::
  :maxdepth: 2

  query


Retries
=======

.. automodule:: google.cloud.bigquery.retry


External Configuration
======================

.. automodule:: google.cloud.bigquery.external_config

.. toctree::
    :maxdepth: 2

    format_options


Magics
======

.. toctree::
    :maxdepth: 2

    magics


Enums
=====

.. toctree::
    :maxdepth: 2

    enums


Encryption Configuration
========================

.. automodule:: google.cloud.bigquery.encryption_configuration


Additional Types
================

Helper SQL type classes.

.. toctree::
    :maxdepth: 2

    bigquery/standard_sql


Legacy proto-based Types (deprecated)
=====================================

The legacy type classes based on protocol buffers.

.. deprecated:: 3.0.0
    These types are provided for backward compatibility only, and are not maintained
    anymore.

.. toctree::
    :maxdepth: 2

    bigquery/legacy_proto_types
