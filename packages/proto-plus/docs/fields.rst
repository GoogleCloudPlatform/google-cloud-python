Fields
======

Fields are assigned using the :class:`~.Field` class, instantiated within a
:class:`~.Message` declaration.

Fields always have a type (either a primitive, a message, or an enum) and a
``number``.

.. code-block:: python

    import proto

    class Composer(proto.Message):
        given_name = proto.Field(proto.STRING, number=1)
        family_name = proto.Field(proto.STRING, number=2)

    class Song(proto.Message):
        composer = proto.Field(Composer, number=1)
        title = proto.Field(proto.STRING, number=2)
        lyrics = proto.Field(proto.STRING, number=3)
        year = proto.Field(proto.INT32, number=4)



For messages and enums, assign the message or enum class directly (as shown
in the example above).

.. note::

    For messages declared in the same module, it is also possible to use a
    string with the message class' name *if* the class is not
    yet declared, which allows for declaring messages out of order or with
    circular references.

Repeated fields
---------------

Some fields are actually repeated fields. In protocol buffers, repeated fields
are generally equivalent to typed lists. In protocol buffers, these are
declared using the **repeated** keyword:

.. code-block:: protobuf

    message Album {
      repeated Song songs = 1;
      string publisher = 2;
    }

Declare them in Python using the :class:`~.RepeatedField` class:

.. code-block:: python

    class Album(proto.Message):
        songs = proto.RepeatedField(Song, number=1)
        publisher = proto.Field(proto.STRING, number=2)


.. note::

    Elements **must** be appended individually for repeated fields of `struct.Value`.

    .. code-block:: python

        class Row(proto.Message):
            values = proto.RepeatedField(proto.MESSAGE, number=1, message=struct.Value,)

        >>> row = Row()
        >>> values = [struct_pb2.Value(string_value="hello")]
        >>> for v in values:
        >>>    row.values.append(v)

    Direct assignment will result in an error.

    .. code-block:: python

        class Row(proto.Message):
            values = proto.RepeatedField(proto.MESSAGE, number=1, message=struct.Value,)

        >>> row = Row()
        >>> row.values = [struct_pb2.Value(string_value="hello")]
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        File "/usr/local/google/home/busunkim/github/python-automl/.nox/unit-3-10/lib/python3.10/site-packages/proto/message.py", line 543, in __setattr__
            self._pb.MergeFrom(self._meta.pb(**{key: pb_value}))
        TypeError: Value must be iterable


Map fields
----------

Similarly, some fields are map fields. In protocol buffers, map fields are
equivalent to typed dictionaries, where the keys are either strings or
integers, and the values can be any type. In protocol buffers, these use
a special ``map`` syntax:

.. code-block:: protobuf

    message Album {
      map<uint32, Song> track_list = 1;
      string publisher = 2;
    }

Declare them in Python using the :class:`~.MapField` class:

.. code-block:: python

    class Album(proto.Message):
        track_list = proto.MapField(proto.UINT32, Song, number=1)
        publisher = proto.Field(proto.STRING, number=2)


Oneofs (mutually-exclusive fields)
----------------------------------

Protocol buffers allows certain fields to be declared as mutually exclusive.
This is done by wrapping fields in a ``oneof`` syntax:

.. code-block:: protobuf

    import "google/type/postal_address.proto";

    message AlbumPurchase {
      Album album = 1;
      oneof delivery {
        google.type.PostalAddress postal_address = 2;
        string download_uri = 3;
      }
    }

When using this syntax, protocol buffers will enforce that only one of the
given fields is set on the message, and setting a field within the oneof
will clear any others.

Declare this in Python using the ``oneof`` keyword-argument, which takes
a string (which should match for all fields within the oneof):

.. code-block:: python

    from google.type.postal_address import PostalAddress

    class AlbumPurchase(proto.Message):
        album = proto.Field(Album, number=1)
        postal_address = proto.Field(PostalAddress, number=2, oneof='delivery')
        download_uri = proto.Field(proto.STRING, number=3, oneof='delivery')

.. warning::

    ``oneof`` fields **must** be declared consecutively, otherwise the C
    implementation of protocol buffers will reject the message. They need not
    have consecutive field numbers, but they must be declared in consecutive
    order.

.. warning::

   If a message is constructed with multiple variants of a single ``oneof`` passed
   to its constructor, the **last** keyword/value pair passed will be the final
   value set.

   This is consistent with PEP-468_, which specifies the order that keyword args
   are seen by called functions, and with the regular protocol buffers runtime,
   which exhibits the same behavior.

   Example:

   .. code-block:: python

      import proto

      class Song(proto.Message):
          name = proto.Field(proto.STRING, number=1, oneof="identifier")
          database_id = proto.Field(proto.STRING, number=2, oneof="identifier")

      s = Song(name="Canon in D minor", database_id="b5a37aad3")
      assert "database_id" in s and "name" not in s

      s = Song(database_id="e6aa708c7e", name="Little Fugue")
      assert "name" in s and "database_id" not in s

   To query which ``oneof`` is present in a given message, use ``proto.Message._pb("oneof")``.

   Example:

   .. code-block:: python

      import proto

      class Song(proto.Message):
          name = proto.Field(proto.STRING, number=1, oneof="identifier")
          database_id = proto.Field(proto.STRING, number=2, oneof="identifier")

      s = Song(name="Canon in D minor")
      assert s._pb.WhichOneof("identifier") == "name"

      s = Song(database_id="e6aa708c7e")
      assert s._pb.WhichOneof("identifier") == "database_id"


Optional fields
---------------

All fields in protocol buffers are optional, but it is often necessary to
check for field presence. Sometimes legitimate values for fields can be falsy,
so checking for truthiness is not sufficient. Proto3 v3.12.0 added the
``optional`` keyword to field descriptions, which enables a mechanism for
checking field presence.

In proto plus, fields can be marked as optional by passing ``optional=True``
in the constructor. The message *class* then gains a field of the same name
that can be used to detect whether the field is present in message *instances*.

.. code-block:: python

   class Song(proto.Message):
       composer = proto.Field(Composer, number=1)
       title = proto.Field(proto.STRING, number=2)
       lyrics = proto.Field(proto.STRING, number=3)
       year = proto.Field(proto.INT32, number=4)
       performer = proto.Field(proto.STRING, number=5, optional=True)

    >>> s = Song(
    ...     composer={'given_name': 'Johann', 'family_name': 'Pachelbel'},
    ...     title='Canon in D',
    ...     year=1680,
    ...     genre=Genre.CLASSICAL,
    ... )
    >>> Song.performer in s
    False
    >>> s.performer = 'Brahms'
    >>> Song.performer in s
    True
    >>> del s.performer
    >>> Song.performer in s
    False
    >>> s.performer = ""    # The mysterious, unnamed composer
    >>> Song.performer in s
    True


Under the hood, fields marked as optional are implemented via a synthetic
one-variant ``oneof``. See the protocolbuffers documentation_ for more
information.

.. _documentation: https://github.com/protocolbuffers/protobuf/blob/v3.12.0/docs/field_presence.md

.. _PEP-468: https://www.python.org/dev/peps/pep-0468/
