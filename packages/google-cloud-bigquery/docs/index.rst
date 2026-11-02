.. include:: README.rst

.. note::

   Because the BigQuery client uses the third-party :mod:`requests` library
   by default and the BigQuery-Storage client uses :mod:`grpcio` library,
   both are safe to share instances across threads.  In multiprocessing
   scenarios, the best practice is to create client instances *after*
   :class:`multiprocessing.Pool` or :class:`multiprocessing.Process` invokes
   :func:`os.fork`.

More Examples
~~~~~~~~~~~~~

.. toctree::
  :maxdepth: 2

  usage/index
  Official Google BigQuery How-to Guides <https://cloud.google.com/bigquery/docs/how-to>

API Reference
-------------

.. toctree::
  :maxdepth: 2

  reference
  dbapi
  design/index

Migration Guide
---------------

See the guides below for instructions on migrating from older to newer *major* releases
of this library (from ``1.x`` to ``2.x``, or from ``2.x`` to ``3.x``).

.. toctree::
    :maxdepth: 2

    UPGRADING

Changelog
---------

For a list of all ``google-cloud-bigquery`` releases:

.. toctree::
  :maxdepth: 2

  CHANGELOG.md

.. toctree::
  :hidden:

  summary_overview.md
