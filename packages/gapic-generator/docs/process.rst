How Code Generation Works
-------------------------

This page gives a brief decription of how *this* code generator works.
It is not intended to be the final treatise on how to write *any* code
generator. It is meant to be a reference for those who wish to contribute
to this effort, or to use it as a reference implementation.

There are two steps: a **parse** step which essentially involves reorganizing
data to make it more friendly to templates, and a **translation** step which
sends information about the API to templates, which ultimately write the
library.

The protoc contract
~~~~~~~~~~~~~~~~~~~

This code generator is written as a :command:`protoc` plugin, which operates on
a defined contract. The contract is straightforward: a plugin must
accept a ``CodeGeneratorRequest`` (essentially a sequence of
``FileDescriptor`` objects) and output a
``CodeGeneratorResponse``.

If you are unfamiliar with :command:`protoc` plugins, welcome! That last
paragraph likely sounded not as straightforward as claimed. It may be useful
to read `plugin.proto`_ and `descriptor.proto`_ before continuing on. The
former describes the contract with plugins (such as this one) and is relatively
easy to digest, the latter describes protocol buffer files themselves and is
rather dense. The key point to grasp is that each ``.proto`` *file* compiles
into one of these proto messages (called *descriptors*), and this plugin's
job is to parse those descriptors.

That said, you should not need to know the ins and outs of the ``protoc``
contract model to be able to follow what this library is doing.

.. _plugin.proto: https://github.com/google/protobuf/blob/master/src/google/protobuf/compiler/plugin.proto
.. _descriptor.proto: https://github.com/google/protobuf/blob/master/src/google/protobuf/descriptor.proto


Entry Point
~~~~~~~~~~~

The entry point to this tool is ``gapic/cli/generate.py``. The function
in this module is responsible for accepting CLI input, building the internal
API schema, and then rendering templates and using them to build a response
object.


Parse
~~~~~

As mentioned, this plugin is divided into two steps. The first step is
parsing. The guts of this is handled by the :class:`~.schema.api.API` object,
which is this plugin's internal representation of the full API client.

In particular, this class has a :meth:`~.schema.api.API.build` method which
accepts a sequence of ``FileDescriptor`` objects (remember, this is ``protoc``'s
internal representation of each proto file). That method iterates over each
file and creates a :class:`~.schema.api.Proto` object for each one.

.. note::

  An :class:`~.schema.api.API` object will not only be given the descriptors
  for the files you specify, but also all of their dependencies.
  ``protoc`` is smart enough to de-duplicate and send everything in the
  correct order.

The :class:`~.schema.api.API` object's primary purpose is to make sure all
the information from the proto files is in one place, and reasonably
accessible by `Jinja`_ templates (which by design are not allowed to call
arbitrary Python code). Mostly, it tries to avoid creating an entirely
duplicate structure, and simply wraps the descriptor representations.
However, some data needs to be moved around to get it into a structure
useful for templates (in particular, descriptors have an unfriendly approach
to sorting protobuf comments, and this parsing step places these back
alongside their referent objects).

The internal data model does use wrapper classes around most of the
descriptors, such as :class:`~.schema.wrappers.Service` and
:class:`~.schema.wrappers.MessageType`. These consistently contain their
original descriptor (which is always spelled with a ``_pb`` suffix, e.g.
the ``Service`` wrapper class has a ``service_pb`` instance variable).
These exist to handle bringing along additional relevant data (such as the
protobuf comments as mentioned above) and handling resolution of references
(for example, allowing a :class:`~.schema.wrappers.Method` to reference its
input and output types, rather than just the strings).

These wrapper classes follow a consistent structure:

* They define a ``__getattr__`` method that defaults to the wrapped
  desctiptor unless the wrapper itself provides something, making the wrappers
  themselves transparent to templates.
* They provide a ``meta`` attribute with metadata (package information and
  documentation). That means templates can consistently access the name
  for the module where an object can be found, or an object's documentation,
  in predictable and consistent places (``thing.meta.doc``, for example,
  prints the comments for ``thing``).

Translation
~~~~~~~~~~~

The translation step follows a straightfoward process to write the contents
of client library files.

This works by reading in and rendering `Jinja`_ templates into a string.
The file path of the Jinja template is used to determine the filename
in the resulting client library.

More details on authoring templates is discussed on the :doc:`templates`
page.

Exit Point
~~~~~~~~~~

Once the individual strings corresponding to each file to be generated
is collected into memory, these are pieced together into a
``CodeGeneratorResponse`` object, which is serialized
and written to stdout.

.. _Jinja: http://jinja.pocoo.org/docs/2.10/
