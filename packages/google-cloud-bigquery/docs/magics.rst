IPython Magics for BigQuery
===========================

To use these magics, you must first register them. Run the ``%load_ext`` magic
in a Jupyter notebook cell.

.. code::

    %load_ext bigquery_magics

This makes the ``%%bigquery`` magic available.

Code Samples
------------

Running a query:

.. literalinclude:: ./samples/magics/query.py
   :dedent: 4
   :start-after: [START bigquery_jupyter_query]
   :end-before: [END bigquery_jupyter_query]

Running a parameterized query:

.. literalinclude:: ./samples/magics/query_params_scalars.py
   :dedent: 4
   :start-after: [START bigquery_jupyter_query_params_scalars]
   :end-before: [END bigquery_jupyter_query_params_scalars]

BigQuery Magics Reference
-------------------------

-  `BigQuery Magics Documentation`_

.. _BigQuery Magics Documentation: https://googleapis.dev/python/bigquery-magics/latest
