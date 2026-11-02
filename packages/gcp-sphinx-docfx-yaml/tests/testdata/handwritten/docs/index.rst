.. include:: README.rst

.. note::

   Because the storage client uses the third-party :mod:`requests` library by
   default, it is safe to share instances across threads.  In multiprocessing
   scenarious, best practice is to create client instances *after*
   :class:`multiprocessing.Pool` or :class:`multiprocessing.Process` invokes
   :func:`os.fork`.

API Reference
-------------
.. toctree::
  :maxdepth: 2

  storage/modules

More Examples
-------------
.. toctree::
  :maxdepth: 2

  Official Google Cloud Storage How-to Guides <https://cloud.google.com/storage/docs/how-to>
  Official Google Cloud Storage Samples <https://cloud.google.com/storage/docs/samples>

Changelog
---------
.. toctree::
  :maxdepth: 2

  changelog
