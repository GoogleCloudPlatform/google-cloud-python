.. include:: README.rst

.. note::

   Because the Datastore client uses the :mod:`grpcio` library by default
   and uses third-party :mod:`requests` library if the GRPC is disabled,
   clients are safe to share instances across threads.  In multiprocessing
   scenarios, the best practice is to create client instances *after*
   :class:`multiprocessing.Pool` or :class:`multiprocessing.Process` invokes
   :func:`os.fork`.

API Reference
-------------
.. toctree::
    :maxdepth: 2

    client
    entities
    keys
    queries
    aggregations
    transactions
    batches
    helpers
    admin_client

Changelog
---------

For a list of all ``google-cloud-datastore`` releases:

.. toctree::
    :maxdepth: 2

    CHANGELOG

.. toctree::
  :hidden:

  summary_overview.md
