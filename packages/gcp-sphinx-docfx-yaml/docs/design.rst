Sphinx DocFX YAML Reference Design
==================================

This document will provide basic thoughts of the design of the DocFX YAML converter for the Sphinx Python Domain.

Goals
-----

The primary goal of this project is to generate YAML that can be consumed by the ``docfx`` tool.
It will be rendered from the internal doctree representation in Python.
This allows for the largest amount of compatability across Python domain implementations,
for example supporting both autodoc and manual domain entries.

Architecture
------------

Two approaches were tried in the design of this system.
The first was based on the Docutils doctree implementation.
The second was a signal implementation.
Below we cover the trade offs and where we ended up.

Doctree
~~~~~~~

Sphinx autodoc is used to generate the API documentation for most Python projects.
It imports the code via standard Python ``import`` mechanisms,
and then generates the proper rST in the Sphinx Python domain_.
This is then parsed until the ``doctree`` that is used internally in Sphinx.

The initial attempt (``docfx_yaml/extract_nodes.py``) was to take this ``doctree`` and transform it into the YAML structure.
This worked for the majority of the Pytho metadata,
but ran into issues when attempting to get the raw Python docstrings.
These docstrings were parsed as rST and only available as a doctree object.
This meant that docstrings written in Markdown would be improperly parsed as rST and unable to be transformed back.

Monkeypatch
```````````

We use the **Doctree** approach for some of our data.
In particular, 
to get the :ref:`info field lists` from Sphinx,
we insert a monkeypatch in the Sphinx rendering.
This lives in the ``docfx_yaml/monkeypatch.py`` file. 

We used this approach because we needed to get the pre-transformed doc field information.
After Sphinx's transformation of the doctree important semantic information is lost.
So we needed to monkeypatch the ``DocFieldTransformer`` in Sphinx to get the information before it is transformed.

Signals
~~~~~~~

The approach that we settled on for getting the full docstring text is the `autodoc-process-docstring <http://www.sphinx-doc.org/en/stable/ext/autodoc.html#event-autodoc-process-docstring>`_ signal implemented in autodoc.
It lives in the ``docfx_yaml/extension.py`` file.
This signal is triggered at the processing of the docstring,
passing it along unprocessed.
This allows us to properly get the content of the docstring,
as well as derive the unique ID (uid) of the object.

Another important part of the ``autodoc-process-docstring`` signal is that it passes the actual Python object along with it.
This allows us to introspect it with the ``inspect`` Python module,
and pull off argument listings,
default values,
line numbers,
and other information about the actual object.
This was required because we wanted more information about the objects than Sphinx outputs in it's normal output around autodoc.

.. warning:: 
    This will only work for autodoc generated strings.
    Any other use of the Python domain will be ignored,
    as it isn't using the ``autodoc`` module.

YAML syntax
-----------

The ``docfx`` tool does not have support for Python concepts.
As such,
we have done a lossy mapping of the Python concepts onto the equivalent C# concepts.
This is lossy becuase there are things that can be expressed in Python that can't be in C#,
for example functions that live outside of a class.

The `YAML Syntax`_ is documented and should be output properly from this module.
The mapping is done as follows:

.. literalinclude:: ../docfx_yaml/extension.py
   :start-after: TYPE_MAPPING = {
   :end-before: }

Along with this mapping,
all module-level functions will be added to a proxy class called ``Global``.
This will allow them to be attached to a proper class,
and be defined with ``docfx``.

.. _domain: http://www.sphinx-doc.org/en/1.5.1/domains.html
.. _YAML Syntax: https://dotnet.github.io/docfx/spec/metadata_dotnet_spec.html

Sphinx Implementation
~~~~~~~~~~~~~~~~~~~~~

The user will run a normal ``make html`` as part of their build.
The generation and loading will be done as an extension that can be configured.

They will then be output into ``docfx_yaml`` inside the documentation directory.

