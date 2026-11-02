Type Marshaling
===============

Proto Plus provides a service that converts between protocol buffer objects
and native Python types (or the wrapper types provided by this library).

This allows native Python objects to be used in place of protocol buffer
messages where appropriate. In all cases, we return the native type, and are
liberal on what we accept.

Well-known types
----------------

The following types are currently handled by Proto Plus:

=================================== ======================= ========
Protocol buffer type                Python type             Nullable
=================================== ======================= ========
``google.protobuf.BoolValue``       ``bool``                     Yes
``google.protobuf.BytesValue``      ``bytes``                    Yes
``google.protobuf.DoubleValue``     ``float``                    Yes
``google.protobuf.Duration``        ``datetime.timedelta``         –
``google.protobuf.FloatValue``      ``float``                    Yes
``google.protobuf.Int32Value``      ``int``                      Yes
``google.protobuf.Int64Value``      ``int``                      Yes
``google.protobuf.ListValue``       ``MutableSequence``          Yes
``google.protobuf.StringValue``     ``str``                      Yes
``google.protobuf.Struct``          ``MutableMapping``           Yes
``google.protobuf.Timestamp``       ``datetime.datetime``        Yes
``google.protobuf.UInt32Value``     ``int``                      Yes
``google.protobuf.UInt64Value``     ``int``                      Yes
``google.protobuf.Value``           JSON-encodable values        Yes
=================================== ======================= ========

.. note::

    Protocol buffers include well-known types for ``Timestamp`` and
    ``Duration``, both of which have nanosecond precision. However, the
    Python ``datetime`` and ``timedelta`` objects have only microsecond
    precision. This library converts timestamps to an implementation of
    ``datetime.datetime``, DatetimeWithNanoseconds, that includes nanosecond
    precision.

    If you *write* a timestamp field using a Python ``datetime`` value,
    any existing nanosecond precision will be overwritten.

.. note::

   Setting a ``bytes`` field from a string value will first base64 decode the string.
   This is necessary to preserve the original protobuf semantics when converting between
   Python dicts and proto messages.
   Converting a message containing a bytes field to a dict will
   base64 encode the bytes field and yield a value of type str.

.. code-block:: python

  import proto
  from google.protobuf.json_format import ParseDict

  class MyMessage(proto.Message):
      data = proto.Field(proto.BYTES, number=1)

  msg = MyMessage(data=b"this is a message")
  msg_dict = MyMessage.to_dict(msg)

  # Note: the value is the base64 encoded string of the bytes field.
  # It has a type of str, NOT bytes.
  assert type(msg_dict['data']) == str

  msg_pb = ParseDict(msg_dict, MyMessage.pb())
  msg_two = MyMessage(msg_dict)

  assert msg == msg_pb == msg_two
      
  
Wrapper types
-------------

Additionally, every :class:`~.Message` subclass is a wrapper class. The
creation of the class also creates the underlying protocol buffer class, and
this is registered to the marshal.

The underlying protocol buffer message class is accessible with the
:meth:`~.Message.pb` class method.
