Templates
=========

This page provides a description of templates: how to write them, what
variables they receive, and so on and so forth.

In many cases, it should be possible to provide alternative Python libraries
based on protocol buffers by only editing templates (or authoring new ones),
with no requirement to alter the primary codebase itself.

Jinja
-----

All templates are implemented in `Jinja`_, Armin Ronacher's excellent
templating library for Python. This document assumes that you are already
familiar with the basics of writing Jinja templates, and does not seek to
cover that here.


Locating Templates
------------------

Templates are included in output simply on the basis that they exist.
**There is no primary list of templates**; it is assumed that every template
should be rendered (unless its name begins with a single underscore).

.. note::

    Files beginning with an underscore (``_``) are not rendered by default.
    This is to allow them to be used with ``extends`` and ``include``.
    However, ``__init__.py.j2`` is rendered.

The name of the output file is based on the name of the template, with
the following string replacements applied:

* The ``.j2`` suffix is removed.
* ``$namespace`` is replaced with the namespace specified in the client,
  converted to appropriate Python module case. If there is no namespace,
  this segment is dropped. If the namespace has more than one element,
  this is expanded out in the directory structure. (For example, a namespace
  of ``['Acme', 'Manufacturing']`` will translate into ``acme/manufacturing/``
  directories.)
* ``$name`` is replaced with the client name. This is expected to be
  present.
* ``$version`` is replaced with the client version (the version of the API).
  If there is no specified version, this is dropped.
* ``$service`` is replaced with the service name, converted to appropriate
  Python module case. There may be more than one service in an API; read on
  for more about this.

.. note::

    ``$name_$version`` is a special case: It is replaced with the client
    name, followed by the version. However, if there is no version, both it
    and the underscore are dropped.

Context (Variables)
-------------------

Every template receives one variable, spelled ``api``. It is the
:class:`~.schema.api.API` object that was pieced together in the parsing step.

Most APIs also receive one additional variable depending on what piece of the
API structure is being iterated over:

  * **Services.** APIs can (and often do) have more than one service.
    Therefore, templates with ``$service`` in their name are
    rendered *once per service*, with the ``$service`` string changed to
    the name of the service itself (in snake case, because this is Python).
    These templates receive a ``service`` variable (an instance of
    :class:`~.schema.wrappers.Service`) corresponding to the service currently
    being iterated over.
  * **Protos.** Similarly, APIs can (and often do) have more than one proto
    file containing messages. Therefore, templates with ``$proto`` in their
    name are rendered *once per proto*, with the ``$proto``string changed to
    the name of the proto file. These templates receive a ``proto`` variable
    (an instance of :class:`~.schema.api.Proto`) corresponding to the proto
    currently being iterated over.

Filters
-------

Additionally, templates receive a limited number of filters useful for
writing properly formatted templates.

These are:

* ``rst`` (:meth:`~.utils.rst.rst`): Converts a string to ReStructured Text.
  If the string appears not to be formatted (contains no obvious Markdown
  syntax characters), then this method forwards to ``wrap``.
* ``sort_lines`` (:meth:`~.utils.lines.sort_lines`): Sorts lines of text,
  optionally de-duplicating if there are duplicates. This works best with
  the Jinja ``{% filter sort_lines %}`` style syntax.
* ``snake_case`` (:meth:`~.utils.case.to_snake_case`): Converts a string in
  any sane case system to snake case.
* ``wrap`` (:meth:`~.utils.lines.wrap`): Wraps arbitrary text. Keyword
  arguments on this method such as ``offset`` and ``indent`` should make it
  relatively easy to take an arbitrary string and make it wrap to 79
  characters appropriately.

Custom templates
----------------

It is possible to provide your own templates.

To do so, you need a folder with Jinja templates. Each template must have
a ``.j2`` extension (which will be stripped by this software when writing
the final file; see above). Additionally, when you provide your own templates,
the filename substitutions described above still occur.

Building Locally
~~~~~~~~~~~~~~~~

To specify templates, you need to provide a ``--python_gapic_opt`` argument
to ``protoc``, with a key-value pair that looks like:

    --python_gapic_opt="python-gapic-templates=/path/to/templates"

It is *also* possible to specify more than one directory for templates
(in which case they are searched in order); to do this, provide the argument
multiple times:

    --python_gapic_opt="python-gapic-templates=/path/to/templates"
    --python_gapic_opt="python-gapic-templates=/other/path"

If you provide your own templates, the default templates are no longer
consulted. If you want to add your own templates on top of the default ones
provided by this library, use the special `DEFAULT` string:

    --python_gapic_opt="python-gapic-templates=/path/to/templates"
    --python_gapic_opt="python-gapic-templates=DEFAULT"


.. _Jinja: http://jinja.pocoo.org/docs/2.10/
