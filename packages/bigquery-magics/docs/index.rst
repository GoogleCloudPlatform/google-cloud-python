.. include:: README.rst

More Examples
~~~~~~~~~~~~~

.. toctree::
  :maxdepth: 2

  magics
  Official Google BigQuery Magics Tutorials <https://cloud.google.com/bigquery/docs/visualize-jupyter>


Migration Guide
---------------

Migrating from the ``google-cloud-bigquery``, you need to run the following in a Jupyter notebook cell.

Before:

.. code::

    %load_ext google.cloud.bigquery

After:

.. code::

    %load_ext bigquery_magics

.. toctree::
    :maxdepth: 2


Changelog
---------

For a list of all ``bigquery-magics`` releases:

.. toctree::
  :maxdepth: 2

  CHANGELOG
