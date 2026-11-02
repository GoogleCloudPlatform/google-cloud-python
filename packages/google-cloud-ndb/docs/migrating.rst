######################################
Migrating from Python 2 version of NDB
######################################

While every attempt has been made to keep compatibility with the previous
version of `ndb`, there are fundamental differences at the platform level,
which have made necessary in some cases to depart from the original
implementation, and sometimes even to remove existing functionality
altogether.

One of the main objectives of this rewrite was to enable `ndb` for use in any
Python environment, not just Google App Engine. As a result, many of the `ndb`
APIs that relied on GAE environment and runtime variables, resources, and
legacy APIs have been dropped.

Aside from this, there are many differences between the Datastore APIs
provided by GAE and those provided by the newer Google Cloud Platform. These
differences have required some code and API changes as well.

Finally, in many cases, new features of Python 3 have eliminated the need for
some code, particularly from the old `utils` module.

If you are migrating code, these changes can generate some confusion. This
document will cover the most common migration issues.

Setting up a connection
=======================

The most important difference from the previous `ndb` version, is that the new
`ndb` requires the use of a client to set up a runtime context for a project.
This is necessary because `ndb` can now be used in any Python environment, so
we can no longer assume it's running in the context of a GAE request.

The `ndb` client uses ``google.auth`` for authentication, consistent with other
Google Cloud Platform client libraries. The client can take a `credentials`
parameter or get the credentials using the `GOOGLE_APPLICATION_CREDENTIALS`
environment variable, which is the recommended option. For more information
about authentication, consult the `Cloud Storage Client Libraries
<https://cloud.google.com/storage/docs/reference/libraries>`_ documentation.

After instantiating a client, it's necessary to establish a runtime context,
using the ``Client.context`` method. All interactions with the database must
be within the context obtained from this call::

    from google.cloud import ndb

    client = ndb.Client()

    with client.context() as context:
        do_something_with_ndb()

The context is not thread safe, so for threaded applications, you need to
generate one context per thread. This is particularly important for web
applications, where the best practice would be to generate a context per
request. However, please note that for cases where multiple threads are used
for a single request, a new context should be generated for every thread that
will use the `ndb` library.

The following code shows how to use the context in a threaded application::

    import threading
    from google.cloud import datastore
    from google.cloud import ndb

    client = ndb.Client()

    class Test(ndb.Model):
        name = ndb.StringProperty()

    def insert(input_name):    
        with client.context():
            t = Test(name=input_name)        
            t.put()        

    thread1 = threading.Thread(target=insert, args=['John'])
    thread2 = threading.Thread(target=insert, args=['Bob'])

    thread1.start()
    thread2.start()

Note that the examples above are assuming the google credentials are set in
the environment.

Keys
====

There are some methods from the ``key`` module that are not implemented in
this version of `ndb`:

    - Key.from_old_key.
    - Key.to_old_key.

These methods were used to pass keys to and from the `db` Datastore API, which
is no longer supported (`db` was `ndb`'s predecessor).

Models
======

There are some methods from the ``model`` module that are not implemented in
this version of `ndb`. This is because getting the indexes relied on GAE
context functionality:

    - get_indexes.
    - get_indexes_async.

Properties
==========

There are various small changes in some of the model properties that might
trip you up when migrating code. Here are some of them, for quick reference:

- The `BlobProperty` constructor only sets `_compressed` if explicitly
  passed. The original set `_compressed` always.
- In the exact same fashion the `JsonProperty` constructor only sets
  `_json_type` if explicitly passed.
- Similarly, the `DateTimeProperty` constructor only sets `_auto_now` and
  `_auto_now_add` if explicitly passed.
- `TextProperty(indexed=True)` and `StringProperty(indexed=False)` are no
  longer supported. That is, TextProperty can no longer be indexed, whereas
  StringProperty is always indexed.
- The `Property()` constructor (and subclasses) originally accepted both
  `unicode` and `str` (the Python 2 versions) for `name` (and `kind`) but now
  only accept `str`.

QueryOptions and Query Order
============================

The QueryOptions class from ``google.cloud.ndb.query``, has been reimplemented,
since ``google.appengine.datastore.datastore_rpc.Configuration`` is no longer
available. It still uses the same signature, but does not support original
Configuration methods.

Similarly, because ``google.appengine.datastore.datastore_query.Order`` is no
longer available, the ``ndb.query.PropertyOrder`` class has been created to
replace it.

MessageProperty and EnumProperty
================================

These properties, from the ``ndb.msgprop`` module, depend on the Google
Protocol RPC Library, or `protorpc`, which is not an `ndb` dependency. For
this reason, they are not part of this version of `ndb`.

Tasklets
========

When writing a `tasklet`, it is no longer necessary to raise a Return
exception for returning the result. A normal return can be used instead::

    @ndb.tasklet
    def get_cart():
        cart = yield CartItem.query().fetch_async()
        return cart

Note that "raise Return(cart)" can still be used, but it's not recommended.

There are some methods from the ``tasklet`` module that are not implemented in
this version of `ndb`, mainly because of changes in how an `ndb` context is
created and used in this version:

    - add_flow_exception.
    - make_context.
    - make_default_context.
    - QueueFuture.
    - ReducedFuture.
    - SerialQueueFuture.
    - set_context.

ndb.utils
=========

The previous version of `ndb` included an ``ndb.utils`` module, which defined
a number of methods that were mostly used internally. Some of those have been
made obsolete by new Python 3 features, while others have been discarded due
to implementation differences in the new `ndb`.

Possibly the most used utility from this module outside of `ndb` code is the
``positional`` decorator, which declares that only the first `n` arguments of
a function or method may be positional. Python 3 can do this using keyword-only
arguments. What used to be written as::

    @utils.positional(2)
    def function1(arg1, arg2, arg3=None, arg4=None):
        pass

Should be written like this in Python 3::

    def function1(arg1, arg2, *, arg3=None, arg4=None):
        pass

However, ``positional`` remains available and works in Python 3.

Exceptions
==========

App Engine's legacy exceptions are no longer available, but `ndb` provides
shims for most of them, which can be imported from the `ndb.exceptions`
package, like this::

    from google.cloud.ndb.exceptions import BadRequestError, BadArgumentError

Datastore API
=============

There are many differences between the current Datastore API and the legacy App
Engine Datastore. In most cases, where the public API was generally used, this
should not be a problem. However, if you relied in your code on the private
Datastore API, the code that does this will probably need to be rewritten.

Specifically, the old NDB library included some undocumented APIs that dealt
directly with Datastore protocol buffers. These APIs will no longer work.
Rewrite any code that used the following classes, properties, or methods:

    - ModelAdapter
    - Property._db_get_value, Property._db_set_value.
    - Property._db_set_compressed_meaning and
      Property._db_set_uncompressed_meaning.
    - Model._deserialize and Model._serialize.
    - model.make_connection.

Default Namespace
=================

In the previous version, ``google.appengine.api.namespacemanager`` was used
to determine the default namespace when not passed in to constructors which
require it, like ``Key``. In this version, the client class can be instantiated
with a namespace, which will be used as the default whenever it's not included
in the constructor or method arguments that expect a namespace::

    from google.cloud import ndb

    client=ndb.Client(namespace="my namespace")
    
    with client.context() as context:
        key = ndb.Key("SomeKind", "SomeId")

In this example, the key will be created under the namespace `my namespace`,
because that's the namespace passed in when setting up the client.

Django Middleware
=================

The Django middleware that was part of the GAE version of `ndb` has been
discontinued and is no longer available in current `ndb`. The middleware
basically took care of setting the context, which can be accomplished on
modern Django with a simple class middleware, similar to this::

    from google.cloud import ndb

    class NDBMiddleware(object):
        def __init__(self, get_response):
            self.get_response = get_response
            self.client = ndb.Client()

        def __call__(self, request):
            context = self.client.context()
            request.ndb_context = context
            with context:
                response = self.get_response(request)
            return response

The ``__init__`` method is called only once, during server start, so it's a
good place to create and store an `ndb` client. As mentioned above, the
recommended practice is to have one context per request, so the ``__call__``
method, which is called once per request, is an ideal place to create it. 
After we have the context, we add it to the request, right before the response
is processed. The context will then be available in view and template code.
Finally, we use the ``with`` statement to generate the response within our
context.

Another way to get an `ndb` context into a request, would be to use a `context
processor`, but those are functions called for every request, which means we
would need to initialize the client and context on each request, or find
another way to initialize and get the initial client.

Note that the above code, like other `ndb` code, assumes the presence of the
`GOOGLE_APPLICATION_CREDENTIALS` environment variable when the client is
created. See Django documentation for details on setting up the environment.
