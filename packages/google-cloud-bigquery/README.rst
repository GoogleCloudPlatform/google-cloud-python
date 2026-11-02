Python Client for Google BigQuery
=================================

|GA| |pypi| |versions|

Querying massive datasets can be time consuming and expensive without the
right hardware and infrastructure. Google `BigQuery`_ solves this problem by
enabling super-fast, SQL queries against append-mostly tables, using the
processing power of Google's infrastructure.

-  `Client Library Documentation`_
-  `Product Documentation`_

.. |GA| image:: https://img.shields.io/badge/support-GA-gold.svg
   :target: https://github.com/googleapis/google-cloud-python/blob/main/README.rst#general-availability
.. |pypi| image:: https://img.shields.io/pypi/v/google-cloud-bigquery.svg
   :target: https://pypi.org/project/google-cloud-bigquery/
.. |versions| image:: https://img.shields.io/pypi/pyversions/google-cloud-bigquery.svg
   :target: https://pypi.org/project/google-cloud-bigquery/
.. _BigQuery: https://cloud.google.com/bigquery/what-is-bigquery
.. _Client Library Documentation: https://cloud.google.com/python/docs/reference/bigquery/latest/summary_overview
.. _Product Documentation: https://cloud.google.com/bigquery/docs/reference/v2/


Related Libraries
-----------------

For higher-level data analysis and DataFrame operations, consider using one of the following connector libraries:

.. list-table::
   :header-rows: 1

   * - Library
     - Description
     - Documentation
   * - `BigQuery DataFrames (bigframes) <https://dataframes.bigquery.dev/>`_
     - Flexible pandas-like and scikit-learn-like API powered by BigQuery engine for large-scale data analysis and ML.
     - `BigFrames Docs <https://dataframes.bigquery.dev/>`_
   * - `pandas-gbq <https://pandas-gbq.readthedocs.io/>`_
     - Convenient integration allowing pandas DataFrames to load from and write to BigQuery.
     - `pandas-gbq Docs <https://pandas-gbq.readthedocs.io/>`_


Quick Start
-----------

In order to use this library, you first need to go through the following steps:

1. `Select or create a Cloud Platform project.`_
2. `Enable billing for your project.`_
3. `Enable the Google Cloud BigQuery API.`_
4. `Setup Authentication.`_

.. _Select or create a Cloud Platform project.: https://console.cloud.google.com/project
.. _Enable billing for your project.: https://cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project
.. _Enable the Google Cloud BigQuery API.:  https://cloud.google.com/bigquery
.. _Setup Authentication.: https://googleapis.dev/python/google-api-core/latest/auth.html

Installation
~~~~~~~~~~~~

Install this library in a `virtualenv`_ using pip. `virtualenv`_ is a tool to
create isolated Python environments. The basic problem it addresses is one of
dependencies and versions, and indirectly permissions.

With `virtualenv`_, it's possible to install this library without needing system
install permissions, and without clashing with the installed system
dependencies.

.. _`virtualenv`: https://virtualenv.pypa.io/en/latest/


Supported Python Versions
^^^^^^^^^^^^^^^^^^^^^^^^^
Python >= 3.10

Unsupported Python Versions
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Python <= 3.9.

The last version of this library compatible with Python 2.7 and 3.5 is
`google-cloud-bigquery==1.28.0`.


Mac/Linux
^^^^^^^^^

.. code-block:: console

    pip install virtualenv
    virtualenv <your-env>
    source <your-env>/bin/activate
    <your-env>/bin/pip install google-cloud-bigquery


Windows
^^^^^^^

.. code-block:: console

    pip install virtualenv
    virtualenv <your-env>
    <your-env>\Scripts\activate
    <your-env>\Scripts\pip.exe install google-cloud-bigquery

Example Usage
-------------

Perform a query
~~~~~~~~~~~~~~~

.. code:: python

    from google.cloud import bigquery

    client = bigquery.Client()

    # Perform a query.
    QUERY = (
        'SELECT name FROM `bigquery-public-data.usa_names.usa_1910_2013` '
        'WHERE state = "TX" '
        'LIMIT 100')
    query_job = client.query(QUERY)  # API request
    rows = query_job.result()  # Waits for query to finish

    for row in rows:
        print(row.name)

Instrumenting With OpenTelemetry
--------------------------------

This application uses `OpenTelemetry`_ to output tracing data from
API calls to BigQuery. To enable OpenTelemetry tracing in
the BigQuery client the following PyPI packages need to be installed:

.. _OpenTelemetry: https://opentelemetry.io

.. code-block:: console

    pip install google-cloud-bigquery[opentelemetry] opentelemetry-exporter-gcp-trace

After installation, OpenTelemetry can be used in the BigQuery
client and in BigQuery jobs. First, however, an exporter must be
specified for where the trace data will be outputted to. An
example of this can be found here:

.. code-block:: python

    from opentelemetry import trace
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import BatchSpanProcessor
    from opentelemetry.exporter.cloud_trace import CloudTraceSpanExporter
    tracer_provider = TracerProvider()
    tracer_provider = BatchSpanProcessor(CloudTraceSpanExporter())
    trace.set_tracer_provider(TracerProvider())

In this example all tracing data will be published to the Google
`Cloud Trace`_ console. For more information on OpenTelemetry, please consult the `OpenTelemetry documentation`_.

.. _OpenTelemetry documentation: https://opentelemetry-python.readthedocs.io
.. _Cloud Trace: https://cloud.google.com/trace
