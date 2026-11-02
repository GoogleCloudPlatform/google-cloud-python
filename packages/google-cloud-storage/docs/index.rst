.. include:: README.rst

.. note::

   Because the storage client uses the third-party :mod:`requests` library by
   default, it is safe to share instances across threads.  In multiprocessing
   scenarious, best practice is to create client instances *after*
   :class:`multiprocessing.Pool` or :class:`multiprocessing.Process` invokes
   :func:`os.fork`.

Guides
------
.. toctree::
  :maxdepth: 2

  acl_guide
  generation_metageneration
  retry_timeout

API Reference
-------------
.. toctree::
  :maxdepth: 2

  storage/acl
  storage/batch
  storage/blob
  storage/bucket
  storage/client
  storage/constants
  storage/exceptions
  storage/fileio
  storage/hmac_key
  storage/notification
  storage/retry
  storage/transfer_manager


More Examples
-------------
.. toctree::
  :maxdepth: 2

  Official Google Cloud Storage How-to Guides <https://cloud.google.com/storage/docs/how-to>
  Official Google Cloud Storage Samples <https://cloud.google.com/storage/docs/samples>


Changelog
---------

For a list of all ``google-cloud-storage`` releases:

.. toctree::
    :maxdepth: 2

    CHANGELOG

.. toctree::
  :hidden:

  summary_overview.md
