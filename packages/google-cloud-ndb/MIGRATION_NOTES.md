# `ndb` Migration Notes

This is a collection of assumptions, API / implementation differences
and comments about the `ndb` rewrite process.

The primary differences come from:

- Absence of "legacy" APIs provided by Google App Engine (e.g.
  `google.appengine.api.datastore_types`) as well as other environment
  specific features (e.g. the `APPLICATION_ID` environment variable)
- Differences in Datastore APIs between the versions provided by Google App
  Engine and Google Clould Platform.
- Presence of new features in Python 3 like keyword only arguments and
  async support

## Bootstrapping

The biggest difference is in establishing a runtime context for your NDB
application. The Google App Engine Python 2.7 runtime had a strong assumption
that all code executed inside a web framework request-response cycle, in a
single thread per request. In order to decouple from that assumption, Cloud NDB
implements explicit clients and contexts. This is consistent with other Cloud
client libraries.

The ``Client`` class has been introduced which by and large works the same as 
Datastore's ``Client`` class and uses ``google.auth`` for authentication. You
can pass a ``credentials`` parameter to ``Client`` or use the
``GOOGLE_APPLICATION_CREDENTIALS`` environment variable (recommended). See
[https://cloud.google.com/docs/authentication/getting-started] for details.

Once a client has been obtained, you still need to establish a runtime context,
which you can do using the ``Client.context`` method.

```
from google.cloud import ndb

# Assume GOOGLE_APPLICATION_CREDENTIALS is set in environment
client = ndb.Client()

with client.context() as context:
    do_stuff_with_ndb()
```

## Memcache

Because the Google App Engine Memcache service is not a part of the Google
Cloud Platform, it was necessary to refactor the "memcache" functionality of
NDB. The concept of a memcache has been generalized to that of a "global cache"
and defined by the `GlobalCache` interface, which is an abstract base class.
NDB provides a single concrete implementation of `GlobalCache`, `RedisCache`,
which uses Redis.

In order to enable the global cache, a `GlobalCache` instance must be passed
into the context. The Bootstrapping example can be amended as follows:

```
from google.cloud import ndb

# Assume GOOGLE_APPLICATION_CREDENTIALS is set in environment.
client = ndb.Client()

# Assume REDIS_CACHE_URL is set in environment (or not).
# If left unset, this will return `None`, which effectively allows you to turn
# global cache on or off using the environment.
global_cache = ndb.RedisCache.from_environment()

with client.context(global_cache=global_cache) as context:
    do_stuff_with_ndb()
```

`context.Context` had a number of methods that were direct pass-throughs to GAE
Memcache. These are no longer implemented. The methods of `context.Context`
that are affected are: `memcache_add`, `memcache_cas`, `memcache_decr`,
`memcache_delete`, `memcache_get`, `memcache_gets`, `memcache_incr`,
`memcache_replace`, `memcache_set`. 

## Differences (between old and new implementations)

- The "standard" exceptions from App Engine are no longer available. Instead,
  we'll create "shims" for them in `google.cloud.ndb.exceptions` to match the
  class names and emulate behavior.
- There is no replacement for `google.appengine.api.namespace_manager` which is
  used to determine the default namespace when not passed in to `Key()`
- The `Key()` constructor (and helpers) make a distinction between `unicode`
  and `str` types (in Python 2). These are now `unicode->str` and `str->bytes`.
  However, `google.cloud.datastore.Key()` (the actual type we use under the
  covers), only allows the `str` type in Python 3, so much of the "type-check
  and branch" from the original implementation is gone. This **may** cause
  some slight differences.
- `Key.from_old_key()` and `Key.to_old_key()` always raise
  `NotImplementedError`. Without the actual types from the legacy runtime,
  these methods are impossible to implement. Also, since this code won't
  run on legacy Google App Engine, these methods aren't needed.
- `Key.app()` may not preserve the prefix from the constructor (this is noted
  in the docstring)
- `Key.__eq__` previously claimed to be "performance-conscious" and directly
  used `self.__app == other.__app` and similar comparisons. We don't store the
  same data on our `Key` (we just make a wrapper around
  `google.cloud.datastore.Key`), so these are replaced by functions calls
  `self.app() == self.app()` which incur some overhead.
- The verification of kind / string ID fails when they exceed 1500 bytes. The
  original implementation didn't allow in excess of 500 bytes, but it seems
  the limit has been raised by the backend. (FWIW, Danny's opinion is that
  the backend should enforce these limits, not the library.)
- `Property.__creation_counter_global` has been removed as it seems to have
  been included for a feature that was never implemented. See
  [Issue #175][1] for original rationale for including it and [Issue #6317][2]
  for discussion of its removal.
- `ndb` uses "private" instance attributes in many places, e.g. `Key.__app`.
  The current implementation (for now) just uses "protected" attribute names,
  e.g. `Key._key` (the implementation has changed in the rewrite). We may want
  to keep the old "private" names around for compatibility. However, in some
  cases, the underlying representation of the class has changed (such as `Key`)
  due to newly available helper libraries or due to missing behavior from
  the legacy runtime.
- `query.PostFilterNode.__eq__` compares `self.predicate` to `other.predicate`
  rather than using `self.__dict__ == other.__dict__`
- `__slots__` have been added to most non-exception types for a number of
  reasons. The first is the naive "performance" win and the second is that
  this will make it transparent whenever `ndb` users refer to non-existent
  "private" or "protected" instance attributes
- I dropped `Property._positional` since keyword-only arguments are native
  Python 3 syntax and dropped `Property._attributes`  in favor of an
  approach using `inspect.signature()`
- A bug in `Property._find_methods` was fixed where `reverse=True` was applied
  **before** caching and then not respected when pulling from the cache
- The `Property._find_methods_cache` has been changed. Previously it would be
  set on each `Property` subclass and populated dynamically on first use.
  Now `Property._FIND_METHODS_CACHE` is set to `{}` when the `Property` class
  is created and there is another level of keys (based on fully-qualified
  class name) in the cache.
- `BlobProperty._datastore_type` has not been implemented; the base class
  implementation is sufficient. The original implementation wrapped a byte
  string in a `google.appengine.api.datastore_types.ByteString` instance, but
  that type was mostly an alias for `str` in Python 2
- `BlobProperty._validate` used to special case for "too long when indexed"
  if `isinstance(self, TextProperty)`. We have removed this check since
  the implementation does the same check in `TextProperty._validate`.
- The `BlobProperty` constructor only sets `_compressed` if explicitly
  passed. The original set `_compressed` always (and used `False` as default).
  In the exact same fashion the `JsonProperty` constructor only sets
  `_json_type` if explicitly passed. Similarly, the `DateTimeProperty`
  constructor only sets `_auto_now` and `_auto_now_add` if explicitly passed.
- `TextProperty(indexed=True)` and `StringProperty(indexed=False)` are no
  longer supported (see docstrings for more info)
- `model.GeoPt` is an alias for `google.cloud.datastore.helpers.GeoPoint`
  rather than an alias for `google.appengine.api.datastore_types.GeoPt`. These
  classes have slightly different characteristics.
- The `Property()` constructor (and subclasses) originally accepted both
  `unicode` and `str` (the Python 2 versions) for `name` (and `kind`) but we
  only accept `str`.
- The `Parameter()` constructor (and subclasses) originally accepted `int`,
  `unicode` and `str` (the Python 2 versions) for `key` but we only accept
  `int` and `str`.
- When a `Key` is used to create a query "node", e.g. via
  `MyModel.my_value == some_key`, the underlying behavior has changed.
  Previously a `FilterNode` would be created with the actual value set to
  `some_key.to_old_key()`. Now, we set it to `some_key._key`.
- The `google.appengine.api.users.User` class is missing, so there is a
  replacement in `google.cloud.ndb.model.User` that is also available as
  `google.cloud.ndb.User`. This does not support federated identity and
  has new support for adding such a user to a `google.cloud.datastore.Entity`
  and for reading one from a new-style `Entity`
- The `UserProperty` class no longer supports `auto_current_user(_add)`
- `Model.__repr__` will use `_key` to describe the entity's key when there
  is also a user-defined property named `key`. For an example, see the
  class docstring for `Model`.
- `Future.set_exception` no longer takes `tb` argument. Python 3 does a good
  job of remembering the original traceback for an exception and there is no
  longer any value added by manually keeping track of the traceback ourselves.
  This method shouldn't generally be called by user code, anyway.
- `Future.state` is omitted as it is redundant. Call `Future.done()` or
  `Future.running()` to get the state of a future.
- `StringProperty` properties were previously stored as blobs
  (entity_pb2.Value.blob_value) in Datastore. They are now properly stored as 
  strings (entity_pb2.Value.string_value). At read time, a `StringProperty`
  will accept either a string or blob value, so compatibility is maintained
  with legacy databases.
- The QueryOptions class from google.cloud.ndb.query, has been reimplemented,
  since google.appengine.datastore.datastore_rpc.Configuration is no longer
  available. It still uses the same signature, but does not support original
  Configuration methods.
- Because google.appengine.datastore.datastore_query.Order is no longer
  available, the ndb.query.PropertyOrder class has been created to replace it.
- Transaction propagation is no longer supported. This was a feature of the
  older Datastore RPC library which is no longer used. Starting a new
  transaction when a transaction is already in progress in the current context
  will result in an error, as will passing a value for the `propagation` option
  when starting a transaction.
- The `xg` option for transactions is ignored. Previously, setting this to
  `True`, allowed writes up 5 entity groups in a transaction, as opposed to
  only being able to write to a single entity group. In Datastore, currently,
  writing up to 25 entity groups in a transaction is supported by default and
  there is no option to change this.
- Datastore API does not support Entity Group metadata queries anymore, so
  `google.cloud.ndb.metadata.EntityGroup` and
  `google.cloud.ndb.metadata.get_entity_group_version` both throw a
  `google.cloud.ndb.exceptions.NoLongerImplementedError` exception when used.
- The `batch_size` and `prefetch_size` arguments to `Query.fetch` and
  `Query.fetch_async` are no longer supported. These were passed through
  directly to Datastore, which no longer supports these options.
- The `index_list` method of `QueryIterator` is not implemented. Datastore no
  longer returns this data with query results, so it is not available from the
  API in this way. 
- The `produce_cursors` query option is deprecated. Datastore always returns
  cursors, where it can, and NDB always makes them available when possible.
  This option can be passed in but it will be ignored.
- The `max` argument to `Model.allocate_ids` and `Model.allocate_ids_async` is
  no longer supported. The Google Datastore API does not support setting a
  maximum ID, a feature that GAE Datastore presumably had.
- `model.get_indexes()` and `model.get_indexes_async()` are no longer
  implemented, as the support in Datastore for these functions has disappeared
  from GAE to GCP.
- The `max_memcache_items` option is no longer supported. 
- The `force_writes` option is no longer supported.
- The `blobstore` module is no longer supported.
- The `pass_batch_into_callback` argument to `Query.map` and `Query.map_async`
  is no longer supported.
- The `merge_future` argument to `Query.map` and `Query.map_async` is no longer
  supported.
- Key.urlsafe() output is subtly different: the original NDB included a GAE 
  Datastore-specific "location prefix", but that string is neither necessary
  nor available on Cloud Datastore. For applications that require urlsafe()
  strings to be exactly consistent between versions, use
  Key.to_legacy_urlsafe(location_prefix) and pass in your location prefix as an
  argument. Location prefixes are most commonly "s~" (or "e~" in Europe) but
  the easiest way to find your prefix is to base64 decode any urlsafe key
  produced by the original NDB and manually inspect it. The location prefix
  will be consistent for an App Engine project and its corresponding Datastore
  instance over its entire lifetime.
- Key.urlsafe outputs a "bytes" object on Python 3. This is consistent behavior
  and actually just a change in nomenclature; in Python 2, the "str" type
  referred to a bytestring, and in Python 3 the corresponding type is called
  "bytes". Users may notice a difficulty in incorporating urlsafe() strings in
  JSON objects in Python 3; that is due to a change in the json.JSONEncoder
  default behavior between Python 2 and Python 3 (in Python 2, json.JSONEncoder
  accepted bytestrings and attempted to convert them to unicode automatically,
  which can result in corrupted data and as such is no longer done) and does not
  reflect a change in NDB behavior.

## Privatization

App Engine NDB exposed some internal utilities as part of the public API. A few
bits of the nominally public API have been found to be *de facto* private.
These are pieces that are omitted from public facing documentation and which
have no apparent use outside of NDB internals. These pieces have been formally
renamed as part of the private API:

- `eventloop` has been renamed to `_eventloop`.
- `tasklets.get_return_value` has been renamed to `tasklets._get_return_value`
  and is no longer among top level exports.
- `tasklets.MultiFuture` has been renamed to `tasklets._MultiFuture`, removed
  from top level exports, and has a much simpler interface.

These options classes appear not to have been used directly by users and are
not implemented—public facing API used keyword arguments instead, which are
still supported:

- `ContextOptions`
- `TransactionOptions`

The following pieces appear to have been only used internally and are no longer
implemented due to the features they were used for having been refactored:

- `Query.run_to_queue`
- `tasklets.add_flow_exception`
- `tasklets.make_context`
- `tasklets.make_default_context`
- `tasklets.QueueFuture`
- `tasklets.ReducingFuture`
- `tasklets.SerialQueueFuture`
- `tasklets.set_context`

A number of functions in the `utils` package appear to have only been used
internally and have been made obsolete either by API changes, internal
refactoring, or new features of Python 3, and are no longer implemented:

- `utils.code_info()`
- `utils.decorator()`
- `utils.frame_info()`
- `utils.func_info()`
- `utils.gen_info()`
- `utils.get_stack()`
- `utils.logging_debug()`
- `utils.positional()`
- `utils.tweak_logging()`
- `utils.wrapping()` (use `functools.wraps` instead)
- `utils.threading_local()`

## Bare Metal

One of the largest classes of differences comes from the use of the current
Datastore API, rather than the legacy App Engine Datastore. In general, for
users coding to the public interface, this won't be an issue, but users relying
on pieces of the ostensibly private API that are exposed to the bare metal of
the original datastore implementation will have to rewrite those pieces.
Specifically, any function or method that dealt directly with protocol buffers
will no longer work. The Datastore `.protobuf` definitions have changed
significantly from the barely public API used by App Engine to the current
published API. Additionally, this version of NDB mostly delegates to
`google.cloud.datastore` for parsing data returned by RPCs, which is a
significant internal refactoring.

- `ModelAdapter` is no longer used. In legacy NDB, this was passed to the 
  Datastore RPC client so that calls to Datastore RPCs could yield NDB entities
  directly from Datastore RPC calls. AFAIK, Datastore no longer accepts an
  adapter for adapting entities. At any rate, we no longer do it that way.
- `Property._db_get_value`, `Property._db_set_value`, are no longer used. They
  worked directly with Datastore protocol buffers, work which is now delegated
  to `google.cloud.datastore`.
- `Property._db_set_compressed_meaning` and 
  `Property._db_set_uncompressed_meaning` were used by `Property._db_set_value`
  and are no longer used.
- `Model._deserialize` and `Model._serialize` are no longer used. They worked
  directly with protocol buffers, so weren't really salvageable. Unfortunately,
  there were comments indicating they were overridden by subclasses. Hopefully
  this isn't broadly the case.
- `model.make_connection` is no longer implemented.

## Comments

- There is rampant use (and abuse) of `__new__` rather than `__init__` as
  a constructor as the original implementation. By using `__new__`, sometimes
  a **different** type is used from the constructor. It seems that feature,
  along with the fact that `pickle` only calls `__new__` (and never `__init__`)
  is why `__init__` is almost never used.
- The `Key.__getnewargs__()` method isn't needed. For pickle protocols 0 and 1,
  `__new__` is not invoked on a class during unpickling; the state "unpacking"
  is handled solely via `__setstate__`. However, for pickle protocols 2, 3
  and 4, during unpickling an instance will first be created via
  `Key.__new__()` and then `__setstate__` would be called on that instance.
  The addition of the `__getnewargs__` allows the (positional) arguments to be
  stored in the pickled bytes. **All** of the work of the constructor happens
  in `__new__`, so the call to `__setstate__` is redundant. In our
  implementation `__setstate__` is sufficient, hence `__getnewargs__` isn't
  needed.
- Key parts (i.e. kind, string ID and / or integer ID) are verified when a
  `Reference` is created. However, this won't occur when the corresponding
  protobuf for the underlying `google.cloud.datastore.Key` is created. This
  is because the `Reference` is a legacy protobuf message type from App
  Engine, while the latest (`google/datastore/v1`) RPC definition uses a `Key`.
- There is a `Property._CREATION_COUNTER` that gets incremented every time
  a new `Property()` instance is created. This increment is not threadsafe.
  However, `ndb` was designed for `Property()` instances to be created at
  import time, so this may not be an issue.
- `ndb.model._BaseValue` for "wrapping" non-user values should probably
  be dropped or redesigned if possible.
- Since we want "compatibility", suggestions in `TODO` comments have not been
  implemented. However, that policy can be changed if desired.
- It seems that `query.ConjunctionNode.__new__` had an unreachable line
  that returned a `FalseNode`. This return has been changed to a
  `RuntimeError` just it case it **is** actually reached.
- For ``AND`` and ``OR`` to compare equal, the nodes must come in the
  same order. So ``AND(a > 7, b > 6)`` is not equal to ``AND(b > 6, a > 7)``.
- It seems that `query.ConjunctionNode.__new__` had an unreachable line
  that returned a `FalseNode`. This return has been changed to a
  `RuntimeError` just it case it **is** actually reached.
- For ``AND`` and ``OR`` to compare equal, the nodes must come in the
  same order. So ``AND(a > 7, b > 6)`` is not equal to ``AND(b > 6, a > 7)``.
- The whole `bytes` vs. `str` issue needs to be considered package-wide.
  For example, the `Property()` constructor always encoded Python 2 `unicode`
  to a Python 2 `str` (i.e. `bytes`) with the `utf-8` encoding. This fits
  in some sense: the property name in the [protobuf definition][3] is a
  `string` (i.e. UTF-8 encoded text). However, there is a bit of a disconnect
  with other types that use property names, e.g. `FilterNode`.
- There is a giant web of module interdependency, so runtime imports (to avoid
  import cycles) are very common. For example `model.Property` depends on
  `query` but `query` depends on `model`.
- Will need to sort out dependencies on old RPC implementations and port to
  modern gRPC. ([Issue #6363][4])

[1]: https://github.com/GoogleCloudPlatform/datastore-ndb-python/issues/175
[2]: https://github.com/googleapis/google-cloud-python/issues/6317
[3]: https://github.com/googleapis/googleapis/blob/3afba2fd062df0c89ecd62d97f912192b8e0e0ae/google/datastore/v1/entity.proto#L203
[4]: https://github.com/googleapis/google-cloud-python/issues/6363
