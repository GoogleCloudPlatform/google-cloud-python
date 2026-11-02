Reference
---------

Below is a reference for the major classes and functions within this
module.

It is split into three main sections:

- The ``schema`` module contains data classes that make up the internal
  representation for an :class:`~.API`. The API contains thin wrappers
  around protocol buffer descriptors; the goal of the wrappers is to
  mostly expose the underlying descriptors, but make some of the more
  complicated access and references easier in templates.
- The ``generator`` module contains most of the logic. Its
  :class:`~.Generator` class is the thing that takes a request from ``protoc``
  and gives it back a response.
- The ``utils`` module contains utility functions needed elsewhere,
  including some functions that are sent to all templates as Jinja filters.

.. note::

    Templates are housed in the ``templates`` directory, which is a sibling
    to the modules listed above.

.. toctree::
   :maxdepth: 4

   generator
   schema
   utils
