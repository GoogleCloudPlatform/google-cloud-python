This is not an officially supported Google product.

This is a forked version of the original from https://github.com/docascode/sphinx-docfx-yaml.

Feel free to use this forked repository for personal or experimental use, use the original otherwise.

Sphinx DocFX YAML
=================

Sphinx DocFX YAML is an exporter for the Sphinx Autodoc module into `DocFX YAML <https://dotnet.github.io/docfx/spec/metadata_format_spec.html>`_.

You can read the full documentation online at http://sphinx-docfx-yaml.readthedocs.io

Contents
--------

.. toctree::
   :glob:
   :maxdepth: 2

   design
   layout
   api

Basic Workflow
--------------

* Write RST that includes Python `autodoc <www.sphinx-doc.org/en/stable/ext/autodoc.html>`_
* Render internal doctree into YAML
* Output YAML into output directory

Install
-------

To use this forked version, install GCP docfx-yaml:

.. code:: bash

    pip install gcp-sphinx-docfx-yaml

Then add it to your Sphinx project's ``conf.py``:

.. code:: python

    # Order matters here.
    # The extension must be defined *after* autodoc,
    # because it uses a signal that autodoc defines
    extensions = ['sphinx.ext.autodoc', 'docfx_yaml.extension']

Make sure you are using autodoc in your code somewhere::

    .. automodule:: foo.bar

Then build your documentation::

    make html

Inside your build directory (``_build/html`` usually),
the ``docfx_yaml`` will contain the YAML files that are output.

Testing
-------

To run the tests in this repository, run:

.. code:: bash

    pip install tox
    tox -e docs

from the top directory of this repository.

..  Modes
    -----

    There are two output modes that specify the structure of the YAML files.
    The first is ``module`` which means that the YAML files will be output in files corresponding to the name of their module.
    The second modes is ``rst`` which outputs them in the same structure as the RST files they were defined in.

Design
------

Read more about the design in our :doc:`design`.

Layout
------

This project has a few different pieces at this point.
It's primary goal was to integrate the Azure Python SDK into the docfx tooling.
You can read more about the pieces currently set up in the :doc:`layout`.


Napoleon Support
----------------

We support ``sphinx.ext.napoleon`` for parsing docstrings in other formats.
Currently all markup that maps to existing Sphinx `info field lists <http://www.sphinx-doc.org/en/stable/domains.html#info-field-lists>`_ will work,
along with ``Examples``.
In order to pull examples out,
you need the ``napoleon_use_admonition_for_examples`` set to ``True``.

