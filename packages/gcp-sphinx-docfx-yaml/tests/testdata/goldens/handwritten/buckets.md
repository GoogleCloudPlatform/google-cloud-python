# Buckets

Create / interact with Google Cloud Storage buckets.


### _class_ google.cloud.storage.bucket.Bucket(client, name=None, user_project=None)
Bases: `google.cloud.storage._helpers._PropertyMixin`

A class representing a Bucket on Cloud Storage.


* **Parameters**

    
    * **client** ([`google.cloud.storage.client.Client`](client.md#google.cloud.storage.client.Client)) – A client which holds credentials and project configuration
    for the bucket (which requires a project).


    * **name** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – The name of the bucket. Bucket names must start and end with a
    number or letter.


    * **user_project** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) the project ID to be billed for API
    requests made via this instance.


property `name`

    Get the bucket’s name.


#### STORAGE_CLASSES(_ = ('STANDARD', 'NEARLINE', 'COLDLINE', 'ARCHIVE', 'MULTI_REGIONAL', 'REGIONAL', 'DURABLE_REDUCED_AVAILABILITY'_ )
Allowed values for `storage_class`.

Default value is `STANDARD_STORAGE_CLASS`.

See
[https://cloud.google.com/storage/docs/json_api/v1/buckets#storageClass](https://cloud.google.com/storage/docs/json_api/v1/buckets#storageClass)
[https://cloud.google.com/storage/docs/storage-classes](https://cloud.google.com/storage/docs/storage-classes)


#### _property_ acl()
Create our ACL on demand.


#### add_lifecycle_abort_incomplete_multipart_upload_rule(\*\*kw)
Add a “abort incomplete multipart upload” rule to lifecycle rules.

**NOTE**: The “age” lifecycle condition is the only supported condition
for this rule.

This defines a [lifecycle configuration]([https://cloud.google.com/storage/docs/lifecycle](https://cloud.google.com/storage/docs/lifecycle)),
which is set on the bucket. For the general format of a lifecycle configuration, see the
[bucket resource representation for JSON]([https://cloud.google.com/storage/docs/json_api/v1/buckets](https://cloud.google.com/storage/docs/json_api/v1/buckets)).


* **Params kw**

    arguments passed to `LifecycleRuleConditions`.



#### add_lifecycle_delete_rule(\*\*kw)
Add a “delete” rule to lifecycle rules configured for this bucket.

This defines a [lifecycle configuration]([https://cloud.google.com/storage/docs/lifecycle](https://cloud.google.com/storage/docs/lifecycle)),
which is set on the bucket. For the general format of a lifecycle configuration, see the
[bucket resource representation for JSON]([https://cloud.google.com/storage/docs/json_api/v1/buckets](https://cloud.google.com/storage/docs/json_api/v1/buckets)).
See also a [code sample]([https://cloud.google.com/storage/docs/samples/storage-enable-bucket-lifecycle-management#storage_enable_bucket_lifecycle_management-python](https://cloud.google.com/storage/docs/samples/storage-enable-bucket-lifecycle-management#storage_enable_bucket_lifecycle_management-python)).


* **Params kw**

    arguments passed to `LifecycleRuleConditions`.



#### add_lifecycle_set_storage_class_rule(storage_class, \*\*kw)
Add a “set storage class” rule to lifecycle rules.

This defines a [lifecycle configuration]([https://cloud.google.com/storage/docs/lifecycle](https://cloud.google.com/storage/docs/lifecycle)),
which is set on the bucket. For the general format of a lifecycle configuration, see the
[bucket resource representation for JSON]([https://cloud.google.com/storage/docs/json_api/v1/buckets](https://cloud.google.com/storage/docs/json_api/v1/buckets)).


* **Parameters**

    **storage_class** (str, one of `STORAGE_CLASSES`.) – new storage class to assign to matching items.



* **Params kw**

    arguments passed to `LifecycleRuleConditions`.



#### blob(blob_name, chunk_size=None, encryption_key=None, kms_key_name=None, generation=None)
Factory constructor for blob object.

**NOTE**: This will not make an HTTP request; it simply instantiates
a blob object owned by this bucket.


* **Parameters**

    
    * **blob_name** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – The name of the blob to be instantiated.


    * **chunk_size** ([*int*](https://python.readthedocs.io/en/latest/library/functions.html#int)) – The size of a chunk of data whenever iterating
    (in bytes). This must be a multiple of 256 KB per
    the API specification.


    * **encryption_key** ([*bytes*](https://python.readthedocs.io/en/latest/library/stdtypes.html#bytes)) – (Optional) 32 byte encryption key for customer-supplied encryption.


    * **kms_key_name** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) Resource name of KMS key used to encrypt blob’s content.


    * **generation** (*long*) – (Optional) If present, selects a specific revision of
    this object.



* **Return type**

    [`google.cloud.storage.blob.Blob`](blobs.md#google.cloud.storage.blob.Blob)



* **Returns**

    The blob object created.



#### clear_lifecyle_rules()
Clear lifecycle rules configured for this bucket.

See [https://cloud.google.com/storage/docs/lifecycle](https://cloud.google.com/storage/docs/lifecycle) and

    [https://cloud.google.com/storage/docs/json_api/v1/buckets](https://cloud.google.com/storage/docs/json_api/v1/buckets)


#### _property_ client()
The client bound to this bucket.


#### configure_website(main_page_suffix=None, not_found_page=None)
Configure website-related properties.

See [https://cloud.google.com/storage/docs/static-website](https://cloud.google.com/storage/docs/static-website)

**NOTE**: This configures the bucket’s website-related properties,controlling how
the service behaves when accessing bucket contents as a web site.
See [tutorials]([https://cloud.google.com/storage/docs/hosting-static-website](https://cloud.google.com/storage/docs/hosting-static-website)) and
[code samples]([https://cloud.google.com/storage/docs/samples/storage-define-bucket-website-configuration#storage_define_bucket_website_configuration-python](https://cloud.google.com/storage/docs/samples/storage-define-bucket-website-configuration#storage_define_bucket_website_configuration-python))
for more information.


* **Parameters**

    
    * **main_page_suffix** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – The page to use as the main page
    of a directory.
    Typically something like index.html.


    * **not_found_page** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – The file to use when a page isn’t found.



#### copy_blob(blob, destination_bucket, new_name=None, client=None, preserve_acl=True, source_generation=None, if_generation_match=None, if_generation_not_match=None, if_metageneration_match=None, if_metageneration_not_match=None, if_source_generation_match=None, if_source_generation_not_match=None, if_source_metageneration_match=None, if_source_metageneration_not_match=None, timeout=60, retry=<google.cloud.storage.retry.ConditionalRetryPolicy object>)
Copy the given blob to the given bucket, optionally with a new name.

If `user_project` is set, bills the API request to that project.

See [API reference docs]([https://cloud.google.com/storage/docs/json_api/v1/objects/copy](https://cloud.google.com/storage/docs/json_api/v1/objects/copy))
and a [code sample]([https://cloud.google.com/storage/docs/samples/storage-copy-file#storage_copy_file-python](https://cloud.google.com/storage/docs/samples/storage-copy-file#storage_copy_file-python)).


* **Parameters**

    
    * **blob** ([`google.cloud.storage.blob.Blob`](blobs.md#google.cloud.storage.blob.Blob)) – The blob to be copied.


    * **destination_bucket** (`google.cloud.storage.bucket.Bucket`) – The bucket into which the blob should be
    copied.


    * **new_name** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) The new name for the copied file.


    * **client** ([`Client`](client.md#google.cloud.storage.client.Client) or
    `NoneType`) – (Optional) The client to use. If not passed, falls back
    to the `client` stored on the current bucket.


    * **preserve_acl** ([*bool*](https://python.readthedocs.io/en/latest/library/functions.html#bool)) – DEPRECATED. This argument is not functional!
    (Optional) Copies ACL from old blob to new blob.
    Default: True.


    * **source_generation** (*long*) – (Optional) The generation of the blob to be
    copied.


    * **if_generation_match** (*long*) – (Optional) See [Using if_generation_match](generation_metageneration.md#using-if-generation-match)
    Note that the generation to be matched is that of the
    `destination` blob.


    * **if_generation_not_match** (*long*) – (Optional) See [Using if_generation_not_match](generation_metageneration.md#using-if-generation-not-match)
    Note that the generation to be matched is that of the
    `destination` blob.


    * **if_metageneration_match** (*long*) – (Optional) See [Using if_metageneration_match](generation_metageneration.md#using-if-metageneration-match)
    Note that the metageneration to be matched is that of the
    `destination` blob.


    * **if_metageneration_not_match** (*long*) – (Optional) See [Using if_metageneration_not_match](generation_metageneration.md#using-if-metageneration-not-match)
    Note that the metageneration to be matched is that of the
    `destination` blob.


    * **if_source_generation_match** (*long*) – (Optional) Makes the operation conditional on whether the source
    object’s generation matches the given value.


    * **if_source_generation_not_match** (*long*) – (Optional) Makes the operation conditional on whether the source
    object’s generation does not match the given value.


    * **if_source_metageneration_match** (*long*) – (Optional) Makes the operation conditional on whether the source
    object’s current metageneration matches the given value.


    * **if_source_metageneration_not_match** (*long*) – (Optional) Makes the operation conditional on whether the source
    object’s current metageneration does not match the given value.


    * **timeout** ([*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)* or *[*tuple*](https://python.readthedocs.io/en/latest/library/stdtypes.html#tuple)) – (Optional) The amount of time, in seconds, to wait
    for the server response.  See: [Configuring Timeouts](retry_timeout.md#configuring-timeouts)


    * **retry** ([*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)* or *[*google.cloud.storage.retry.ConditionalRetryPolicy*](retry.md#google.cloud.storage.retry.ConditionalRetryPolicy)) – (Optional) How to retry the RPC. See: [Configuring Retries](retry_timeout.md#configuring-retries)



* **Return type**

    [`google.cloud.storage.blob.Blob`](blobs.md#google.cloud.storage.blob.Blob)



* **Returns**

    The new Blob.



#### _property_ cors()
Retrieve or set CORS policies configured for this bucket.

See [http://www.w3.org/TR/cors/](http://www.w3.org/TR/cors/) and

    [https://cloud.google.com/storage/docs/json_api/v1/buckets](https://cloud.google.com/storage/docs/json_api/v1/buckets)

**NOTE**: The getter for this property returns a list which contains
*copies* of the bucket’s CORS policy mappings.  Mutating the list
or one of its dicts has no effect unless you then re-assign the
dict via the setter.  E.g.:

```python
>>> policies = bucket.cors
>>> policies.append({'origin': '/foo', ...})
>>> policies[1]['maxAgeSeconds'] = 3600
>>> del policies[0]
>>> bucket.cors = policies
>>> bucket.update()
```


* **Setter**

    Set CORS policies for this bucket.



* **Getter**

    Gets the CORS policies for this bucket.



* **Return type**

    list of dictionaries



* **Returns**

    A sequence of mappings describing each CORS policy.



#### create(client=None, project=None, location=None, predefined_acl=None, predefined_default_object_acl=None, timeout=60, retry=<google.api_core.retry.Retry object>)
DEPRECATED. Creates current bucket.

**NOTE**: Direct use of this method is deprecated. Use `Client.create_bucket()` instead.

If the bucket already exists, will raise
`google.cloud.exceptions.Conflict`.

This implements “storage.buckets.insert”.

If `user_project` is set, bills the API request to that project.


* **Parameters**

    
    * **client** ([`Client`](client.md#google.cloud.storage.client.Client) or
    `NoneType`) – (Optional) The client to use. If not passed, falls back
    to the `client` stored on the current bucket.


    * **project** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) The project under which the bucket is to
    be created. If not passed, uses the project set on
    the client.


    * **location** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) The location of the bucket. If not passed,
    the default location, US, will be used. See
    [https://cloud.google.com/storage/docs/bucket-locations](https://cloud.google.com/storage/docs/bucket-locations)


    * **predefined_acl** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) Name of predefined ACL to apply to bucket. See:
    [https://cloud.google.com/storage/docs/access-control/lists#predefined-acl](https://cloud.google.com/storage/docs/access-control/lists#predefined-acl)


    * **predefined_default_object_acl** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) Name of predefined ACL to apply to bucket’s objects. See:
    [https://cloud.google.com/storage/docs/access-control/lists#predefined-acl](https://cloud.google.com/storage/docs/access-control/lists#predefined-acl)


    * **timeout** ([*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)* or *[*tuple*](https://python.readthedocs.io/en/latest/library/stdtypes.html#tuple)) – (Optional) The amount of time, in seconds, to wait
    for the server response.  See: [Configuring Timeouts](retry_timeout.md#configuring-timeouts)


    * **retry** ([*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)* or *[*google.cloud.storage.retry.ConditionalRetryPolicy*](retry.md#google.cloud.storage.retry.ConditionalRetryPolicy)) – (Optional) How to retry the RPC. See: [Configuring Retries](retry_timeout.md#configuring-retries)



* **Raises**

    [**ValueError**](https://python.readthedocs.io/en/latest/library/exceptions.html#ValueError) – if `project` is None and client’s
    `project` is also None.



#### _property_ data_locations()
Retrieve the list of regional locations for custom dual-region buckets.

See [https://cloud.google.com/storage/docs/json_api/v1/buckets](https://cloud.google.com/storage/docs/json_api/v1/buckets) and
[https://cloud.google.com/storage/docs/locations](https://cloud.google.com/storage/docs/locations)

Returns `None` if the property has not been set before creation,
if the bucket’s resource has not been loaded from the server,
or if the bucket is not a dual-regions bucket.
:rtype: list of str or `NoneType`


#### _property_ default_event_based_hold()
Are uploaded objects automatically placed under an even-based hold?

If True, uploaded objects will be placed under an event-based hold to
be released at a future time. When released an object will then begin
the retention period determined by the policy retention period for the
object bucket.

See [https://cloud.google.com/storage/docs/json_api/v1/buckets](https://cloud.google.com/storage/docs/json_api/v1/buckets)

If the property is not set locally, returns `None`.


* **Return type**

    bool or `NoneType`



#### _property_ default_kms_key_name()
Retrieve / set default KMS encryption key for objects in the bucket.

See [https://cloud.google.com/storage/docs/json_api/v1/buckets](https://cloud.google.com/storage/docs/json_api/v1/buckets)


* **Setter**

    Set default KMS encryption key for items in this bucket.



* **Getter**

    Get default KMS encryption key for items in this bucket.



* **Return type**

    [str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)



* **Returns**

    Default KMS encryption key, or `None` if not set.



#### _property_ default_object_acl()
Create our defaultObjectACL on demand.


#### delete(force=False, client=None, if_metageneration_match=None, if_metageneration_not_match=None, timeout=60, retry=<google.api_core.retry.Retry object>)
Delete this bucket.

The bucket **must** be empty in order to submit a delete request. If
`force=True` is passed, this will first attempt to delete all the
objects / blobs in the bucket (i.e. try to empty the bucket).

If the bucket doesn’t exist, this will raise
`google.cloud.exceptions.NotFound`. If the bucket is not empty
(and `force=False`), will raise `google.cloud.exceptions.Conflict`.

If `force=True` and the bucket contains more than 256 objects / blobs
this will cowardly refuse to delete the objects (or the bucket). This
is to prevent accidental bucket deletion and to prevent extremely long
runtime of this method.

If `user_project` is set, bills the API request to that project.


* **Parameters**

    
    * **force** ([*bool*](https://python.readthedocs.io/en/latest/library/functions.html#bool)) – If True, empties the bucket’s objects then deletes it.


    * **client** ([`Client`](client.md#google.cloud.storage.client.Client) or
    `NoneType`) – (Optional) The client to use. If not passed, falls back
    to the `client` stored on the current bucket.


    * **if_metageneration_match** (*long*) – (Optional) Make the operation conditional on whether the
    blob’s current metageneration matches the given value.


    * **if_metageneration_not_match** (*long*) – (Optional) Make the operation conditional on whether the
    blob’s current metageneration does not match the given value.


    * **timeout** ([*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)* or *[*tuple*](https://python.readthedocs.io/en/latest/library/stdtypes.html#tuple)) – (Optional) The amount of time, in seconds, to wait
    for the server response.  See: [Configuring Timeouts](retry_timeout.md#configuring-timeouts)


    * **retry** ([*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)* or *[*google.cloud.storage.retry.ConditionalRetryPolicy*](retry.md#google.cloud.storage.retry.ConditionalRetryPolicy)) – (Optional) How to retry the RPC. See: [Configuring Retries](retry_timeout.md#configuring-retries)



* **Raises**

    [`ValueError`](https://python.readthedocs.io/en/latest/library/exceptions.html#ValueError) if `force` is `True` and the bucket
    contains more than 256 objects / blobs.



#### delete_blob(blob_name, client=None, generation=None, if_generation_match=None, if_generation_not_match=None, if_metageneration_match=None, if_metageneration_not_match=None, timeout=60, retry=<google.cloud.storage.retry.ConditionalRetryPolicy object>)
Deletes a blob from the current bucket.

If `user_project` is set, bills the API request to that project.


* **Parameters**

    
    * **blob_name** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – A blob name to delete.


    * **client** ([`Client`](client.md#google.cloud.storage.client.Client) or
    `NoneType`) – (Optional) The client to use. If not passed, falls back
    to the `client` stored on the current bucket.


    * **generation** (*long*) – (Optional) If present, permanently deletes a specific
    revision of this object.


    * **if_generation_match** (*long*) – (Optional) See [Using if_generation_match](generation_metageneration.md#using-if-generation-match)


    * **if_generation_not_match** (*long*) – (Optional) See [Using if_generation_not_match](generation_metageneration.md#using-if-generation-not-match)


    * **if_metageneration_match** (*long*) – (Optional) See [Using if_metageneration_match](generation_metageneration.md#using-if-metageneration-match)


    * **if_metageneration_not_match** (*long*) – (Optional) See [Using if_metageneration_not_match](generation_metageneration.md#using-if-metageneration-not-match)


    * **timeout** ([*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)* or *[*tuple*](https://python.readthedocs.io/en/latest/library/stdtypes.html#tuple)) – (Optional) The amount of time, in seconds, to wait
    for the server response.  See: [Configuring Timeouts](retry_timeout.md#configuring-timeouts)


    * **retry** ([*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)* or *[*google.cloud.storage.retry.ConditionalRetryPolicy*](retry.md#google.cloud.storage.retry.ConditionalRetryPolicy)) – (Optional) How to retry the RPC. See: [Configuring Retries](retry_timeout.md#configuring-retries)



* **Raises**

    `google.cloud.exceptions.NotFound` Raises a NotFound
    if the blob isn’t found. To suppress
    the exception, use `delete_blobs()` by passing a no-op
    `on_error` callback.



#### delete_blobs(blobs, on_error=None, client=None, preserve_generation=False, timeout=60, if_generation_match=None, if_generation_not_match=None, if_metageneration_match=None, if_metageneration_not_match=None, retry=<google.cloud.storage.retry.ConditionalRetryPolicy object>)
Deletes a list of blobs from the current bucket.

Uses `delete_blob()` to delete each individual blob.

By default, any generation information in the list of blobs is ignored, and the
live versions of all blobs are deleted. Set preserve_generation to True
if blob generation should instead be propagated from the list of blobs.

If `user_project` is set, bills the API request to that project.


* **Parameters**

    
    * **blobs** ([*list*](https://python.readthedocs.io/en/latest/library/stdtypes.html#list)) – A list of [`Blob`](blobs.md#google.cloud.storage.blob.Blob)-s or
    blob names to delete.


    * **on_error** (*callable*) – (Optional) Takes single argument: `blob`.
    Called once for each blob raising
    `NotFound`;
    otherwise, the exception is propagated.


    * **client** ([`Client`](client.md#google.cloud.storage.client.Client)) – (Optional) The client to use.  If not passed, falls back
    to the `client` stored on the current bucket.


    * **preserve_generation** ([*bool*](https://python.readthedocs.io/en/latest/library/functions.html#bool)) – (Optional) Deletes only the generation specified on the blob object,
    instead of the live version, if set to True. Only :class:~google.cloud.storage.blob.Blob
    objects can have their generation set in this way.
    Default: False.


    * **if_generation_match** (*list of long*) – (Optional) See [Using if_generation_match](generation_metageneration.md#using-if-generation-match)
    Note that the length of the list must match the length of
    The list must match `blobs` item-to-item.


    * **if_generation_not_match** (*list of long*) – (Optional) See [Using if_generation_not_match](generation_metageneration.md#using-if-generation-not-match)
    The list must match `blobs` item-to-item.


    * **if_metageneration_match** (*list of long*) – (Optional) See [Using if_metageneration_match](generation_metageneration.md#using-if-metageneration-match)
    The list must match `blobs` item-to-item.


    * **if_metageneration_not_match** (*list of long*) – (Optional) See [Using if_metageneration_not_match](generation_metageneration.md#using-if-metageneration-not-match)
    The list must match `blobs` item-to-item.


    * **timeout** ([*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)* or *[*tuple*](https://python.readthedocs.io/en/latest/library/stdtypes.html#tuple)) – (Optional) The amount of time, in seconds, to wait
    for the server response.  See: [Configuring Timeouts](retry_timeout.md#configuring-timeouts)


    * **retry** ([*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)* or *[*google.cloud.storage.retry.ConditionalRetryPolicy*](retry.md#google.cloud.storage.retry.ConditionalRetryPolicy)) – (Optional) How to retry the RPC. See: [Configuring Retries](retry_timeout.md#configuring-retries)



* **Raises**

    `NotFound` (if
    on_error is not passed).



#### disable_logging()
Disable access logging for this bucket.

See [https://cloud.google.com/storage/docs/access-logs#disabling](https://cloud.google.com/storage/docs/access-logs#disabling)


#### disable_website()
Disable the website configuration for this bucket.

This is really just a shortcut for setting the website-related
attributes to `None`.


#### enable_logging(bucket_name, object_prefix='')
Enable access logging for this bucket.

See [https://cloud.google.com/storage/docs/access-logs](https://cloud.google.com/storage/docs/access-logs)


* **Parameters**

    
    * **bucket_name** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – name of bucket in which to store access logs


    * **object_prefix** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – prefix for access log filenames



#### _property_ etag()
Retrieve the ETag for the bucket.

See [https://tools.ietf.org/html/rfc2616#section-3.11](https://tools.ietf.org/html/rfc2616#section-3.11) and

    [https://cloud.google.com/storage/docs/json_api/v1/buckets](https://cloud.google.com/storage/docs/json_api/v1/buckets)


* **Return type**

    str or `NoneType`



* **Returns**

    The bucket etag or `None` if the bucket’s
    resource has not been loaded from the server.



#### exists(client=None, timeout=60, if_etag_match=None, if_etag_not_match=None, if_metageneration_match=None, if_metageneration_not_match=None, retry=<google.api_core.retry.Retry object>)
Determines whether or not this bucket exists.

If `user_project` is set, bills the API request to that project.


* **Parameters**

    
    * **client** ([`Client`](client.md#google.cloud.storage.client.Client) or
    `NoneType`) – (Optional) The client to use. If not passed, falls back
    to the `client` stored on the current bucket.


    * **timeout** ([*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)* or *[*tuple*](https://python.readthedocs.io/en/latest/library/stdtypes.html#tuple)) – (Optional) The amount of time, in seconds, to wait
    for the server response.  See: [Configuring Timeouts](retry_timeout.md#configuring-timeouts)


    * **if_etag_match** (*Union**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*, **Set**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*]**]*) – (Optional) Make the operation conditional on whether the
    bucket’s current ETag matches the given value.


    * **if_etag_not_match** (*Union**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*, **Set**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*]**]**)*) – (Optional) Make the operation conditional on whether the
    bucket’s current ETag does not match the given value.


    * **if_metageneration_match** (*long*) – (Optional) Make the operation conditional on whether the
    bucket’s current metageneration matches the given value.


    * **if_metageneration_not_match** (*long*) – (Optional) Make the operation conditional on whether the
    bucket’s current metageneration does not match the given value.


    * **retry** ([*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)* or *[*google.cloud.storage.retry.ConditionalRetryPolicy*](retry.md#google.cloud.storage.retry.ConditionalRetryPolicy)) – (Optional) How to retry the RPC. See: [Configuring Retries](retry_timeout.md#configuring-retries)



* **Return type**

    [bool](https://python.readthedocs.io/en/latest/library/functions.html#bool)



* **Returns**

    True if the bucket exists in Cloud Storage.



#### _classmethod_ from_string(uri, client=None)
Get a constructor for bucket object by URI.

```python
from google.cloud import storage
from google.cloud.storage.bucket import Bucket
client = storage.Client()
bucket = Bucket.from_string("gs://bucket", client=client)
```


* **Parameters**

    
    * **uri** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – The bucket uri pass to get bucket object.


    * **client** ([`Client`](client.md#google.cloud.storage.client.Client) or
    `NoneType`) – (Optional) The client to use.  Application code should
    *always* pass `client`.



* **Return type**

    `google.cloud.storage.bucket.Bucket`



* **Returns**

    The bucket object created.



#### generate_signed_url(expiration=None, api_access_endpoint='https://storage.googleapis.com', method='GET', headers=None, query_parameters=None, client=None, credentials=None, version=None, virtual_hosted_style=False, bucket_bound_hostname=None, scheme='http')
Generates a signed URL for this bucket.

**NOTE**: If you are on Google Compute Engine, you can’t generate a signed
URL using GCE service account. If you’d like to be able to generate
a signed URL from GCE, you can use a standard service account from a
JSON file rather than a GCE service account.

If you have a bucket that you want to allow access to for a set
amount of time, you can use this method to generate a URL that
is only valid within a certain time period.

If `bucket_bound_hostname` is set as an argument of `api_access_endpoint`,
`https` works only if using a `CDN`.


* **Parameters**

    
    * **expiration** (*Union**[**Integer**, *[*datetime.datetime*](https://python.readthedocs.io/en/latest/library/datetime.html#datetime.datetime)*, *[*datetime.timedelta*](https://python.readthedocs.io/en/latest/library/datetime.html#datetime.timedelta)*]*) – Point in time when the signed URL should expire. If
    a `datetime` instance is passed without an explicit
    `tzinfo` set,  it will be assumed to be `UTC`.


    * **api_access_endpoint** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) URI base.


    * **method** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – The HTTP verb that will be used when requesting the URL.


    * **headers** ([*dict*](https://python.readthedocs.io/en/latest/library/stdtypes.html#dict)) – (Optional) Additional HTTP headers to be included as part of the
    signed URLs.  See:
    [https://cloud.google.com/storage/docs/xml-api/reference-headers](https://cloud.google.com/storage/docs/xml-api/reference-headers)
    Requests using the signed URL *must* pass the specified header
    (name and value) with each request for the URL.


    * **query_parameters** ([*dict*](https://python.readthedocs.io/en/latest/library/stdtypes.html#dict)) – (Optional) Additional query parameters to be included as part of the
    signed URLs.  See:
    [https://cloud.google.com/storage/docs/xml-api/reference-headers#query](https://cloud.google.com/storage/docs/xml-api/reference-headers#query)


    * **client** ([`Client`](client.md#google.cloud.storage.client.Client) or
    `NoneType`) – (Optional) The client to use.  If not passed, falls back
    to the `client` stored on the blob’s bucket.


    * **credentials** ([`google.auth.credentials.Credentials`](https://googleapis.dev/python/google-auth/latest/reference/google.auth.credentials.html#google.auth.credentials.Credentials) or
    `NoneType`) – The authorization credentials to attach to requests.
    These credentials identify this application to the service.
    If none are specified, the client will attempt to ascertain
    the credentials from the environment.


    * **version** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) The version of signed credential to create.
    Must be one of ‘v2’ | ‘v4’.


    * **virtual_hosted_style** ([*bool*](https://python.readthedocs.io/en/latest/library/functions.html#bool)) – (Optional) If true, then construct the URL relative the bucket’s
    virtual hostname, e.g., ‘<bucket-name>.storage.googleapis.com’.


    * **bucket_bound_hostname** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) If pass, then construct the URL relative to the bucket-bound hostname.
    Value cane be a bare or with scheme, e.g., ‘example.com’ or ‘[http://example.com](http://example.com)’.
    See: [https://cloud.google.com/storage/docs/request-endpoints#cname](https://cloud.google.com/storage/docs/request-endpoints#cname)


    * **scheme** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) If `bucket_bound_hostname` is passed as a bare hostname, use
    this value as the scheme.  `https` will work only when using a CDN.
    Defaults to `"http"`.



* **Raises**

    [`ValueError`](https://python.readthedocs.io/en/latest/library/exceptions.html#ValueError) when version is invalid.



* **Raises**

    [`TypeError`](https://python.readthedocs.io/en/latest/library/exceptions.html#TypeError) when expiration is not a valid type.



* **Raises**

    [`AttributeError`](https://python.readthedocs.io/en/latest/library/exceptions.html#AttributeError) if credentials is not an instance
    of [`google.auth.credentials.Signing`](https://googleapis.dev/python/google-auth/latest/reference/google.auth.credentials.html#google.auth.credentials.Signing).



* **Return type**

    [str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)



* **Returns**

    A signed URL you can use to access the resource
    until expiration.



#### generate_upload_policy(conditions, expiration=None, client=None)
Create a signed upload policy for uploading objects.

This method generates and signs a policy document. You can use
[policy documents]([https://cloud.google.com/storage/docs/xml-api/post-object-forms](https://cloud.google.com/storage/docs/xml-api/post-object-forms))
to allow visitors to a website to upload files to
Google Cloud Storage without giving them direct write access.
See a [code sample]([https://cloud.google.com/storage/docs/xml-api/post-object-forms#python](https://cloud.google.com/storage/docs/xml-api/post-object-forms#python)).


* **Parameters**

    
    * **expiration** (*datetime*) – (Optional) Expiration in UTC. If not specified, the
    policy will expire in 1 hour.


    * **conditions** ([*list*](https://python.readthedocs.io/en/latest/library/stdtypes.html#list)) – A list of conditions as described in the
    policy documents documentation.


    * **client** ([`Client`](client.md#google.cloud.storage.client.Client)) – (Optional) The client to use.  If not passed, falls back
    to the `client` stored on the current bucket.



* **Return type**

    [dict](https://python.readthedocs.io/en/latest/library/stdtypes.html#dict)



* **Returns**

    A dictionary of (form field name, form field value) of form
    fields that should be added to your HTML upload form in order
    to attach the signature.



#### get_blob(blob_name, client=None, encryption_key=None, generation=None, if_etag_match=None, if_etag_not_match=None, if_generation_match=None, if_generation_not_match=None, if_metageneration_match=None, if_metageneration_not_match=None, timeout=60, retry=<google.api_core.retry.Retry object>, \*\*kwargs)
Get a blob object by name.

See a [code sample]([https://cloud.google.com/storage/docs/samples/storage-get-metadata#storage_get_metadata-python](https://cloud.google.com/storage/docs/samples/storage-get-metadata#storage_get_metadata-python))
on how to retrieve metadata of an object.

If `user_project` is set, bills the API request to that project.


* **Parameters**

    
    * **blob_name** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – The name of the blob to retrieve.


    * **client** ([`Client`](client.md#google.cloud.storage.client.Client) or
    `NoneType`) – (Optional) The client to use.  If not passed, falls back
    to the `client` stored on the current bucket.


    * **encryption_key** ([*bytes*](https://python.readthedocs.io/en/latest/library/stdtypes.html#bytes)) – (Optional) 32 byte encryption key for customer-supplied encryption.
    See
    [https://cloud.google.com/storage/docs/encryption#customer-supplied](https://cloud.google.com/storage/docs/encryption#customer-supplied).


    * **generation** (*long*) – (Optional) If present, selects a specific revision of this object.


    * **if_etag_match** (*Union**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*, **Set**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*]**]*) – (Optional) See [Using if_etag_match](generation_metageneration.md#using-if-etag-match)


    * **if_etag_not_match** (*Union**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*, **Set**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*]**]*) – (Optional) See [Using if_etag_not_match](generation_metageneration.md#using-if-etag-not-match)


    * **if_generation_match** (*long*) – (Optional) See [Using if_generation_match](generation_metageneration.md#using-if-generation-match)


    * **if_generation_not_match** (*long*) – (Optional) See [Using if_generation_not_match](generation_metageneration.md#using-if-generation-not-match)


    * **if_metageneration_match** (*long*) – (Optional) See [Using if_metageneration_match](generation_metageneration.md#using-if-metageneration-match)


    * **if_metageneration_not_match** (*long*) – (Optional) See [Using if_metageneration_not_match](generation_metageneration.md#using-if-metageneration-not-match)


    * **timeout** ([*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)* or *[*tuple*](https://python.readthedocs.io/en/latest/library/stdtypes.html#tuple)) – (Optional) The amount of time, in seconds, to wait
    for the server response.  See: [Configuring Timeouts](retry_timeout.md#configuring-timeouts)


    * **retry** ([*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)* or *[*google.cloud.storage.retry.ConditionalRetryPolicy*](retry.md#google.cloud.storage.retry.ConditionalRetryPolicy)) – (Optional) How to retry the RPC. See: [Configuring Retries](retry_timeout.md#configuring-retries)


    * **kwargs** – Keyword arguments to pass to the
    [`Blob`](blobs.md#google.cloud.storage.blob.Blob) constructor.



* **Return type**

    [`google.cloud.storage.blob.Blob`](blobs.md#google.cloud.storage.blob.Blob) or None



* **Returns**

    The blob object if it exists, otherwise None.



#### get_iam_policy(client=None, requested_policy_version=None, timeout=60, retry=<google.api_core.retry.Retry object>)
Retrieve the IAM policy for the bucket.

See [API reference docs]([https://cloud.google.com/storage/docs/json_api/v1/buckets/getIamPolicy](https://cloud.google.com/storage/docs/json_api/v1/buckets/getIamPolicy))
and a [code sample]([https://cloud.google.com/storage/docs/samples/storage-view-bucket-iam-members#storage_view_bucket_iam_members-python](https://cloud.google.com/storage/docs/samples/storage-view-bucket-iam-members#storage_view_bucket_iam_members-python)).

If `user_project` is set, bills the API request to that project.


* **Parameters**

    
    * **client** ([`Client`](client.md#google.cloud.storage.client.Client) or
    `NoneType`) – (Optional) The client to use.  If not passed, falls back
    to the `client` stored on the current bucket.


    * **requested_policy_version** (int or `NoneType`) – (Optional) The version of IAM policies to request.
    If a policy with a condition is requested without
    setting this, the server will return an error.
    This must be set to a value of 3 to retrieve IAM
    policies containing conditions. This is to prevent
    client code that isn’t aware of IAM conditions from
    interpreting and modifying policies incorrectly.
    The service might return a policy with version lower
    than the one that was requested, based on the
    feature syntax in the policy fetched.


    * **timeout** ([*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)* or *[*tuple*](https://python.readthedocs.io/en/latest/library/stdtypes.html#tuple)) – (Optional) The amount of time, in seconds, to wait
    for the server response.  See: [Configuring Timeouts](retry_timeout.md#configuring-timeouts)


    * **retry** ([*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)* or *[*google.cloud.storage.retry.ConditionalRetryPolicy*](retry.md#google.cloud.storage.retry.ConditionalRetryPolicy)) – (Optional) How to retry the RPC. See: [Configuring Retries](retry_timeout.md#configuring-retries)



* **Return type**

    [`google.api_core.iam.Policy`](https://googleapis.dev/python/google-api-core/latest/iam.html#google.api_core.iam.Policy)



* **Returns**

    the policy instance, based on the resource returned from
    the `getIamPolicy` API request.



#### get_logging()
Return info about access logging for this bucket.

See [https://cloud.google.com/storage/docs/access-logs#status](https://cloud.google.com/storage/docs/access-logs#status)


* **Return type**

    [dict](https://python.readthedocs.io/en/latest/library/stdtypes.html#dict) or None



* **Returns**

    a dict w/ keys, `logBucket` and `logObjectPrefix`
    (if logging is enabled), or None (if not).



#### get_notification(notification_id, client=None, timeout=60, retry=<google.api_core.retry.Retry object>)
Get Pub / Sub notification for this bucket.

See [API reference docs]([https://cloud.google.com/storage/docs/json_api/v1/notifications/get](https://cloud.google.com/storage/docs/json_api/v1/notifications/get))
and a [code sample]([https://cloud.google.com/storage/docs/samples/storage-print-pubsub-bucket-notification#storage_print_pubsub_bucket_notification-python](https://cloud.google.com/storage/docs/samples/storage-print-pubsub-bucket-notification#storage_print_pubsub_bucket_notification-python)).

If `user_project` is set, bills the API request to that project.


* **Parameters**

    
    * **notification_id** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – The notification id to retrieve the notification configuration.


    * **client** ([`Client`](client.md#google.cloud.storage.client.Client) or
    `NoneType`) – (Optional) The client to use.  If not passed, falls back
    to the `client` stored on the current bucket.


    * **timeout** ([*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)* or *[*tuple*](https://python.readthedocs.io/en/latest/library/stdtypes.html#tuple)) – (Optional) The amount of time, in seconds, to wait
    for the server response.  See: [Configuring Timeouts](retry_timeout.md#configuring-timeouts)


    * **retry** ([*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)* or *[*google.cloud.storage.retry.ConditionalRetryPolicy*](retry.md#google.cloud.storage.retry.ConditionalRetryPolicy)) – (Optional) How to retry the RPC. See: [Configuring Retries](retry_timeout.md#configuring-retries)



* **Return type**

    [`BucketNotification`](notification.md#google.cloud.storage.notification.BucketNotification)



* **Returns**

    notification instance.



#### _property_ iam_configuration()
Retrieve IAM configuration for this bucket.


* **Return type**

    `IAMConfiguration`



* **Returns**

    an instance for managing the bucket’s IAM configuration.



#### _property_ id()
Retrieve the ID for the bucket.

See [https://cloud.google.com/storage/docs/json_api/v1/buckets](https://cloud.google.com/storage/docs/json_api/v1/buckets)


* **Return type**

    str or `NoneType`



* **Returns**

    The ID of the bucket or `None` if the bucket’s
    resource has not been loaded from the server.



#### _property_ labels()
Retrieve or set labels assigned to this bucket.

See
[https://cloud.google.com/storage/docs/json_api/v1/buckets#labels](https://cloud.google.com/storage/docs/json_api/v1/buckets#labels)

**NOTE**: The getter for this property returns a dict which is a *copy*
of the bucket’s labels.  Mutating that dict has no effect unless
you then re-assign the dict via the setter.  E.g.:

```python
>>> labels = bucket.labels
>>> labels['new_key'] = 'some-label'
>>> del labels['old_key']
>>> bucket.labels = labels
>>> bucket.update()
```


* **Setter**

    Set labels for this bucket.



* **Getter**

    Gets the labels for this bucket.



* **Return type**

    [`dict`](https://python.readthedocs.io/en/latest/library/stdtypes.html#dict)



* **Returns**

    Name-value pairs (string->string) labelling the bucket.



#### _property_ lifecycle_rules()
Retrieve or set lifecycle rules configured for this bucket.

See [https://cloud.google.com/storage/docs/lifecycle](https://cloud.google.com/storage/docs/lifecycle) and

    [https://cloud.google.com/storage/docs/json_api/v1/buckets](https://cloud.google.com/storage/docs/json_api/v1/buckets)

**NOTE**: The getter for this property returns a generator which yields
*copies* of the bucket’s lifecycle rules mappings.  Mutating the
output dicts has no effect unless you then re-assign the dict via
the setter.  E.g.:

```python
>>> rules = list(bucket.lifecycle_rules)
>>> rules.append({'origin': '/foo', ...})
>>> rules[1]['rule']['action']['type'] = 'Delete'
>>> del rules[0]
>>> bucket.lifecycle_rules = rules
>>> bucket.update()
```


* **Setter**

    Set lifecycle rules for this bucket.



* **Getter**

    Gets the lifecycle rules for this bucket.



* **Return type**

    generator([dict](https://python.readthedocs.io/en/latest/library/stdtypes.html#dict))



* **Returns**

    A sequence of mappings describing each lifecycle rule.



#### list_blobs(max_results=None, page_token=None, prefix=None, delimiter=None, start_offset=None, end_offset=None, include_trailing_delimiter=None, versions=None, projection='noAcl', fields=None, client=None, timeout=60, retry=<google.api_core.retry.Retry object>)
DEPRECATED. Return an iterator used to find blobs in the bucket.

**NOTE**: Direct use of this method is deprecated. Use `Client.list_blobs` instead.

If `user_project` is set, bills the API request to that project.


* **Parameters**

    
    * **max_results** ([*int*](https://python.readthedocs.io/en/latest/library/functions.html#int)) – (Optional) The maximum number of blobs to return.


    * **page_token** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) If present, return the next batch of blobs, using the
    value, which must correspond to the `nextPageToken` value
    returned in the previous response.  Deprecated: use the `pages`
    property of the returned iterator instead of manually passing the
    token.


    * **prefix** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) Prefix used to filter blobs.


    * **delimiter** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) Delimiter, used with `prefix` to
    emulate hierarchy.


    * **start_offset** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) Filter results to objects whose names are
    lexicographically equal to or after `startOffset`. If
    `endOffset` is also set, the objects listed will have names
    between `startOffset` (inclusive) and `endOffset` (exclusive).


    * **end_offset** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) Filter results to objects whose names are
    lexicographically before `endOffset`. If `startOffset` is also
    set, the objects listed will have names between `startOffset`
    (inclusive) and `endOffset` (exclusive).


    * **include_trailing_delimiter** (*boolean*) – (Optional) If true, objects that end in exactly one instance of
    `delimiter` will have their metadata included in `items` in
    addition to `prefixes`.


    * **versions** ([*bool*](https://python.readthedocs.io/en/latest/library/functions.html#bool)) – (Optional) Whether object versions should be returned
    as separate blobs.


    * **projection** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) If used, must be ‘full’ or ‘noAcl’.
    Defaults to `'noAcl'`. Specifies the set of
    properties to return.


    * **fields** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) Selector specifying which fields to include
    in a partial response. Must be a list of fields. For
    example to get a partial response with just the next
    page token and the name and language of each blob returned:
    `'items(name,contentLanguage),nextPageToken'`.
    See: [https://cloud.google.com/storage/docs/json_api/v1/parameters#fields](https://cloud.google.com/storage/docs/json_api/v1/parameters#fields)


    * **client** ([`Client`](client.md#google.cloud.storage.client.Client)) – (Optional) The client to use.  If not passed, falls back
    to the `client` stored on the current bucket.


    * **timeout** ([*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)* or *[*tuple*](https://python.readthedocs.io/en/latest/library/stdtypes.html#tuple)) – (Optional) The amount of time, in seconds, to wait
    for the server response.  See: [Configuring Timeouts](retry_timeout.md#configuring-timeouts)


    * **retry** ([*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)* or *[*google.cloud.storage.retry.ConditionalRetryPolicy*](retry.md#google.cloud.storage.retry.ConditionalRetryPolicy)) – (Optional) How to retry the RPC. See: [Configuring Retries](retry_timeout.md#configuring-retries)



* **Return type**

    [`Iterator`](https://googleapis.dev/python/google-api-core/latest/page_iterator.html#google.api_core.page_iterator.Iterator)



* **Returns**

    Iterator of all [`Blob`](blobs.md#google.cloud.storage.blob.Blob)
    in this bucket matching the arguments.



#### list_notifications(client=None, timeout=60, retry=<google.api_core.retry.Retry object>)
List Pub / Sub notifications for this bucket.

See:
[https://cloud.google.com/storage/docs/json_api/v1/notifications/list](https://cloud.google.com/storage/docs/json_api/v1/notifications/list)

If `user_project` is set, bills the API request to that project.


* **Parameters**

    
    * **client** ([`Client`](client.md#google.cloud.storage.client.Client) or
    `NoneType`) – (Optional) The client to use.  If not passed, falls back
    to the `client` stored on the current bucket.


    * **timeout** ([*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)* or *[*tuple*](https://python.readthedocs.io/en/latest/library/stdtypes.html#tuple)) – (Optional) The amount of time, in seconds, to wait
    for the server response.  See: [Configuring Timeouts](retry_timeout.md#configuring-timeouts)


    * **retry** ([*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)* or *[*google.cloud.storage.retry.ConditionalRetryPolicy*](retry.md#google.cloud.storage.retry.ConditionalRetryPolicy)) – (Optional) How to retry the RPC. See: [Configuring Retries](retry_timeout.md#configuring-retries)



* **Return type**

    list of [`BucketNotification`](notification.md#google.cloud.storage.notification.BucketNotification)



* **Returns**

    notification instances



#### _property_ location()
Retrieve location configured for this bucket.

See [https://cloud.google.com/storage/docs/json_api/v1/buckets](https://cloud.google.com/storage/docs/json_api/v1/buckets) and
[https://cloud.google.com/storage/docs/locations](https://cloud.google.com/storage/docs/locations)

Returns `None` if the property has not been set before creation,
or if the bucket’s resource has not been loaded from the server.
:rtype: str or `NoneType`


#### _property_ location_type()
Retrieve the location type for the bucket.

See [https://cloud.google.com/storage/docs/storage-classes](https://cloud.google.com/storage/docs/storage-classes)


* **Getter**

    Gets the the location type for this bucket.



* **Return type**

    str or `NoneType`



* **Returns**

    If set, one of
    [`MULTI_REGION_LOCATION_TYPE`](constants.md#google.cloud.storage.constants.MULTI_REGION_LOCATION_TYPE),
    [`REGION_LOCATION_TYPE`](constants.md#google.cloud.storage.constants.REGION_LOCATION_TYPE), or
    [`DUAL_REGION_LOCATION_TYPE`](constants.md#google.cloud.storage.constants.DUAL_REGION_LOCATION_TYPE),
    else `None`.



#### lock_retention_policy(client=None, timeout=60, retry=<google.api_core.retry.Retry object>)
Lock the bucket’s retention policy.


* **Parameters**

    
    * **client** ([`Client`](client.md#google.cloud.storage.client.Client) or
    `NoneType`) – (Optional) The client to use.  If not passed, falls back
    to the `client` stored on the blob’s bucket.


    * **timeout** ([*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)* or *[*tuple*](https://python.readthedocs.io/en/latest/library/stdtypes.html#tuple)) – (Optional) The amount of time, in seconds, to wait
    for the server response.  See: [Configuring Timeouts](retry_timeout.md#configuring-timeouts)


    * **retry** ([*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)* or *[*google.cloud.storage.retry.ConditionalRetryPolicy*](retry.md#google.cloud.storage.retry.ConditionalRetryPolicy)) – (Optional) How to retry the RPC. See: [Configuring Retries](retry_timeout.md#configuring-retries)



* **Raises**

    [**ValueError**](https://python.readthedocs.io/en/latest/library/exceptions.html#ValueError) – if the bucket has no metageneration (i.e., new or never reloaded);
    if the bucket has no retention policy assigned;
    if the bucket’s retention policy is already locked.



#### make_private(recursive=False, future=False, client=None, timeout=60, if_metageneration_match=None, if_metageneration_not_match=None, retry=<google.cloud.storage.retry.ConditionalRetryPolicy object>)
Update bucket’s ACL, revoking read access for anonymous users.


* **Parameters**

    
    * **recursive** ([*bool*](https://python.readthedocs.io/en/latest/library/functions.html#bool)) – If True, this will make all blobs inside the bucket
    private as well.


    * **future** ([*bool*](https://python.readthedocs.io/en/latest/library/functions.html#bool)) – If True, this will make all objects created in the
    future private as well.


    * **client** ([`Client`](client.md#google.cloud.storage.client.Client) or
    `NoneType`) – (Optional) The client to use.  If not passed, falls back
    to the `client` stored on the current bucket.


    * **timeout** ([*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)* or *[*tuple*](https://python.readthedocs.io/en/latest/library/stdtypes.html#tuple)) – (Optional) The amount of time, in seconds, to wait
    for the server response.  See: [Configuring Timeouts](retry_timeout.md#configuring-timeouts)


    * **if_metageneration_match** (*long*) – (Optional) Make the operation conditional on whether the
    blob’s current metageneration matches the given value.


    * **if_metageneration_not_match** (*long*) – (Optional) Make the operation conditional on whether the
    blob’s current metageneration does not match the given value.


    * **retry** ([*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)* or *[*google.cloud.storage.retry.ConditionalRetryPolicy*](retry.md#google.cloud.storage.retry.ConditionalRetryPolicy)) – (Optional) How to retry the RPC. See: [Configuring Retries](retry_timeout.md#configuring-retries)



* **Raises**

    [**ValueError**](https://python.readthedocs.io/en/latest/library/exceptions.html#ValueError) – If `recursive` is True, and the bucket contains more than 256
    blobs.  This is to prevent extremely long runtime of this
    method.  For such buckets, iterate over the blobs returned by
    `list_blobs()` and call
    [`make_private()`](blobs.md#google.cloud.storage.blob.Blob.make_private)
    for each blob.



#### make_public(recursive=False, future=False, client=None, timeout=60, if_metageneration_match=None, if_metageneration_not_match=None, retry=<google.cloud.storage.retry.ConditionalRetryPolicy object>)
Update bucket’s ACL, granting read access to anonymous users.


* **Parameters**

    
    * **recursive** ([*bool*](https://python.readthedocs.io/en/latest/library/functions.html#bool)) – If True, this will make all blobs inside the bucket
    public as well.


    * **future** ([*bool*](https://python.readthedocs.io/en/latest/library/functions.html#bool)) – If True, this will make all objects created in the
    future public as well.


    * **client** ([`Client`](client.md#google.cloud.storage.client.Client) or
    `NoneType`) – (Optional) The client to use.  If not passed, falls back
    to the `client` stored on the current bucket.


    * **timeout** ([*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)* or *[*tuple*](https://python.readthedocs.io/en/latest/library/stdtypes.html#tuple)) – (Optional) The amount of time, in seconds, to wait
    for the server response.  See: [Configuring Timeouts](retry_timeout.md#configuring-timeouts)


    * **if_metageneration_match** (*long*) – (Optional) Make the operation conditional on whether the
    blob’s current metageneration matches the given value.


    * **if_metageneration_not_match** (*long*) – (Optional) Make the operation conditional on whether the
    blob’s current metageneration does not match the given value.


    * **retry** ([*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)* or *[*google.cloud.storage.retry.ConditionalRetryPolicy*](retry.md#google.cloud.storage.retry.ConditionalRetryPolicy)) – (Optional) How to retry the RPC. See: [Configuring Retries](retry_timeout.md#configuring-retries)



* **Raises**

    [**ValueError**](https://python.readthedocs.io/en/latest/library/exceptions.html#ValueError) – If `recursive` is True, and the bucket contains more than 256
    blobs.  This is to prevent extremely long runtime of this
    method.  For such buckets, iterate over the blobs returned by
    `list_blobs()` and call
    [`make_public()`](blobs.md#google.cloud.storage.blob.Blob.make_public)
    for each blob.



#### _property_ metageneration()
Retrieve the metageneration for the bucket.

See [https://cloud.google.com/storage/docs/json_api/v1/buckets](https://cloud.google.com/storage/docs/json_api/v1/buckets)


* **Return type**

    int or `NoneType`



* **Returns**

    The metageneration of the bucket or `None` if the bucket’s
    resource has not been loaded from the server.



#### notification(topic_name=None, topic_project=None, custom_attributes=None, event_types=None, blob_name_prefix=None, payload_format='NONE', notification_id=None)
Factory:  create a notification resource for the bucket.

See: [`BucketNotification`](notification.md#google.cloud.storage.notification.BucketNotification) for parameters.


* **Return type**

    [`BucketNotification`](notification.md#google.cloud.storage.notification.BucketNotification)



#### _property_ owner()
Retrieve info about the owner of the bucket.

See [https://cloud.google.com/storage/docs/json_api/v1/buckets](https://cloud.google.com/storage/docs/json_api/v1/buckets)


* **Return type**

    dict or `NoneType`



* **Returns**

    Mapping of owner’s role/ID. Returns `None` if the bucket’s
    resource has not been loaded from the server.



#### patch(client=None, timeout=60, if_metageneration_match=None, if_metageneration_not_match=None, retry=<google.cloud.storage.retry.ConditionalRetryPolicy object>)
Sends all changed properties in a PATCH request.

Updates the `_properties` with the response from the backend.

If `user_project` is set, bills the API request to that project.


* **Parameters**

    
    * **client** ([`Client`](client.md#google.cloud.storage.client.Client) or
    `NoneType`) – the client to use. If not passed, falls back to the
    `client` stored on the current object.


    * **timeout** ([*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)* or *[*tuple*](https://python.readthedocs.io/en/latest/library/stdtypes.html#tuple)) – (Optional) The amount of time, in seconds, to wait
    for the server response.  See: [Configuring Timeouts](retry_timeout.md#configuring-timeouts)


    * **if_metageneration_match** (*long*) – (Optional) Make the operation conditional on whether the
    blob’s current metageneration matches the given value.


    * **if_metageneration_not_match** (*long*) – (Optional) Make the operation conditional on whether the
    blob’s current metageneration does not match the given value.


    * **retry** ([*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)* or *[*google.cloud.storage.retry.ConditionalRetryPolicy*](retry.md#google.cloud.storage.retry.ConditionalRetryPolicy)) – (Optional) How to retry the RPC. See: [Configuring Retries](retry_timeout.md#configuring-retries)



#### _property_ path()
The URL path to this bucket.


#### _static_ path_helper(bucket_name)
Relative URL path for a bucket.


* **Parameters**

    **bucket_name** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – The bucket name in the path.



* **Return type**

    [str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)



* **Returns**

    The relative URL path for `bucket_name`.



#### _property_ project_number()
Retrieve the number of the project to which the bucket is assigned.

See [https://cloud.google.com/storage/docs/json_api/v1/buckets](https://cloud.google.com/storage/docs/json_api/v1/buckets)


* **Return type**

    int or `NoneType`



* **Returns**

    The project number that owns the bucket or `None` if
    the bucket’s resource has not been loaded from the server.



#### reload(client=None, projection='noAcl', timeout=60, if_etag_match=None, if_etag_not_match=None, if_metageneration_match=None, if_metageneration_not_match=None, retry=<google.api_core.retry.Retry object>)
Reload properties from Cloud Storage.

If `user_project` is set, bills the API request to that project.


* **Parameters**

    
    * **client** ([`Client`](client.md#google.cloud.storage.client.Client) or
    `NoneType`) – the client to use. If not passed, falls back to the
    `client` stored on the current object.


    * **projection** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) If used, must be ‘full’ or ‘noAcl’.
    Defaults to `'noAcl'`. Specifies the set of
    properties to return.


    * **timeout** ([*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)* or *[*tuple*](https://python.readthedocs.io/en/latest/library/stdtypes.html#tuple)) – (Optional) The amount of time, in seconds, to wait
    for the server response.  See: [Configuring Timeouts](retry_timeout.md#configuring-timeouts)


    * **if_etag_match** (*Union**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*, **Set**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*]**]*) – (Optional) Make the operation conditional on whether the
    bucket’s current ETag matches the given value.


    * **if_etag_not_match** (*Union**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*, **Set**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*]**]**)*) – (Optional) Make the operation conditional on whether the
    bucket’s current ETag does not match the given value.


    * **if_metageneration_match** (*long*) – (Optional) Make the operation conditional on whether the
    bucket’s current metageneration matches the given value.


    * **if_metageneration_not_match** (*long*) – (Optional) Make the operation conditional on whether the
    bucket’s current metageneration does not match the given value.


    * **retry** ([*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)* or *[*google.cloud.storage.retry.ConditionalRetryPolicy*](retry.md#google.cloud.storage.retry.ConditionalRetryPolicy)) – (Optional) How to retry the RPC. See: [Configuring Retries](retry_timeout.md#configuring-retries)



#### rename_blob(blob, new_name, client=None, if_generation_match=None, if_generation_not_match=None, if_metageneration_match=None, if_metageneration_not_match=None, if_source_generation_match=None, if_source_generation_not_match=None, if_source_metageneration_match=None, if_source_metageneration_not_match=None, timeout=60, retry=<google.cloud.storage.retry.ConditionalRetryPolicy object>)
Rename the given blob using copy and delete operations.

If `user_project` is set, bills the API request to that project.

Effectively, copies blob to the same bucket with a new name, then
deletes the blob.

**WARNING**: This method will first duplicate the data and then delete the
old blob.  This means that with very large objects renaming
could be a very (temporarily) costly or a very slow operation.
If you need more control over the copy and deletion, instead
use google.cloud.storage.blob.Blob.copy_to and
google.cloud.storage.blob.Blob.delete directly.


* **Parameters**

    
    * **blob** ([`google.cloud.storage.blob.Blob`](blobs.md#google.cloud.storage.blob.Blob)) – The blob to be renamed.


    * **new_name** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – The new name for this blob.


    * **client** ([`Client`](client.md#google.cloud.storage.client.Client) or
    `NoneType`) – (Optional) The client to use.  If not passed, falls back
    to the `client` stored on the current bucket.


    * **if_generation_match** (*long*) – (Optional) See [Using if_generation_match](generation_metageneration.md#using-if-generation-match)
    Note that the generation to be matched is that of the
    `destination` blob.


    * **if_generation_not_match** (*long*) – (Optional) See [Using if_generation_not_match](generation_metageneration.md#using-if-generation-not-match)
    Note that the generation to be matched is that of the
    `destination` blob.


    * **if_metageneration_match** (*long*) – (Optional) See [Using if_metageneration_match](generation_metageneration.md#using-if-metageneration-match)
    Note that the metageneration to be matched is that of the
    `destination` blob.


    * **if_metageneration_not_match** (*long*) – (Optional) See [Using if_metageneration_not_match](generation_metageneration.md#using-if-metageneration-not-match)
    Note that the metageneration to be matched is that of the
    `destination` blob.


    * **if_source_generation_match** (*long*) – (Optional) Makes the operation conditional on whether the source
    object’s generation matches the given value. Also used in the
    (implied) delete request.


    * **if_source_generation_not_match** (*long*) – (Optional) Makes the operation conditional on whether the source
    object’s generation does not match the given value. Also used in
    the (implied) delete request.


    * **if_source_metageneration_match** (*long*) – (Optional) Makes the operation conditional on whether the source
    object’s current metageneration matches the given value. Also used
    in the (implied) delete request.


    * **if_source_metageneration_not_match** (*long*) – (Optional) Makes the operation conditional on whether the source
    object’s current metageneration does not match the given value.
    Also used in the (implied) delete request.


    * **timeout** ([*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)* or *[*tuple*](https://python.readthedocs.io/en/latest/library/stdtypes.html#tuple)) – (Optional) The amount of time, in seconds, to wait
    for the server response.  See: [Configuring Timeouts](retry_timeout.md#configuring-timeouts)


    * **retry** ([*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)* or *[*google.cloud.storage.retry.ConditionalRetryPolicy*](retry.md#google.cloud.storage.retry.ConditionalRetryPolicy)) – (Optional) How to retry the RPC. See: [Configuring Retries](retry_timeout.md#configuring-retries)



* **Return type**

    `Blob`



* **Returns**

    The newly-renamed blob.



#### _property_ requester_pays()
Does the requester pay for API requests for this bucket?

See [https://cloud.google.com/storage/docs/requester-pays](https://cloud.google.com/storage/docs/requester-pays) for
details.


* **Setter**

    Update whether requester pays for this bucket.



* **Getter**

    Query whether requester pays for this bucket.



* **Return type**

    [bool](https://python.readthedocs.io/en/latest/library/functions.html#bool)



* **Returns**

    True if requester pays for API requests for the bucket,
    else False.



#### _property_ retention_period()
Retrieve or set the retention period for items in the bucket.


* **Return type**

    int or `NoneType`



* **Returns**

    number of seconds to retain items after upload or release
    from event-based lock, or `None` if the property is not
    set locally.



#### _property_ retention_policy_effective_time()
Retrieve the effective time of the bucket’s retention policy.


* **Return type**

    datetime.datetime or `NoneType`



* **Returns**

    point-in time at which the bucket’s retention policy is
    effective, or `None` if the property is not
    set locally.



#### _property_ retention_policy_locked()
Retrieve whthere the bucket’s retention policy is locked.


* **Return type**

    [bool](https://python.readthedocs.io/en/latest/library/functions.html#bool)



* **Returns**

    True if the bucket’s policy is locked, or else False
    if the policy is not locked, or the property is not
    set locally.



#### _property_ rpo()
Get the RPO (Recovery Point Objective) of this bucket

See: [https://cloud.google.com/storage/docs/managing-turbo-replication](https://cloud.google.com/storage/docs/managing-turbo-replication)

“ASYNC_TURBO” or “DEFAULT”
:rtype: str


#### _property_ self_link()
Retrieve the URI for the bucket.

See [https://cloud.google.com/storage/docs/json_api/v1/buckets](https://cloud.google.com/storage/docs/json_api/v1/buckets)


* **Return type**

    str or `NoneType`



* **Returns**

    The self link for the bucket or `None` if
    the bucket’s resource has not been loaded from the server.



#### set_iam_policy(policy, client=None, timeout=60, retry=<google.cloud.storage.retry.ConditionalRetryPolicy object>)
Update the IAM policy for the bucket.

See
[https://cloud.google.com/storage/docs/json_api/v1/buckets/setIamPolicy](https://cloud.google.com/storage/docs/json_api/v1/buckets/setIamPolicy)

If `user_project` is set, bills the API request to that project.


* **Parameters**

    
    * **policy** ([`google.api_core.iam.Policy`](https://googleapis.dev/python/google-api-core/latest/iam.html#google.api_core.iam.Policy)) – policy instance used to update bucket’s IAM policy.


    * **client** ([`Client`](client.md#google.cloud.storage.client.Client) or
    `NoneType`) – (Optional) The client to use.  If not passed, falls back
    to the `client` stored on the current bucket.


    * **timeout** ([*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)* or *[*tuple*](https://python.readthedocs.io/en/latest/library/stdtypes.html#tuple)) – (Optional) The amount of time, in seconds, to wait
    for the server response.  See: [Configuring Timeouts](retry_timeout.md#configuring-timeouts)


    * **retry** ([*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)* or *[*google.cloud.storage.retry.ConditionalRetryPolicy*](retry.md#google.cloud.storage.retry.ConditionalRetryPolicy)) – (Optional) How to retry the RPC. See: [Configuring Retries](retry_timeout.md#configuring-retries)



* **Return type**

    [`google.api_core.iam.Policy`](https://googleapis.dev/python/google-api-core/latest/iam.html#google.api_core.iam.Policy)



* **Returns**

    the policy instance, based on the resource returned from
    the `setIamPolicy` API request.



#### _property_ storage_class()
Retrieve or set the storage class for the bucket.

See [https://cloud.google.com/storage/docs/storage-classes](https://cloud.google.com/storage/docs/storage-classes)


* **Setter**

    Set the storage class for this bucket.



* **Getter**

    Gets the the storage class for this bucket.



* **Return type**

    str or `NoneType`



* **Returns**

    If set, one of
    [`NEARLINE_STORAGE_CLASS`](constants.md#google.cloud.storage.constants.NEARLINE_STORAGE_CLASS),
    [`COLDLINE_STORAGE_CLASS`](constants.md#google.cloud.storage.constants.COLDLINE_STORAGE_CLASS),
    [`ARCHIVE_STORAGE_CLASS`](constants.md#google.cloud.storage.constants.ARCHIVE_STORAGE_CLASS),
    [`STANDARD_STORAGE_CLASS`](constants.md#google.cloud.storage.constants.STANDARD_STORAGE_CLASS),
    [`MULTI_REGIONAL_LEGACY_STORAGE_CLASS`](constants.md#google.cloud.storage.constants.MULTI_REGIONAL_LEGACY_STORAGE_CLASS),
    [`REGIONAL_LEGACY_STORAGE_CLASS`](constants.md#google.cloud.storage.constants.REGIONAL_LEGACY_STORAGE_CLASS),
    or
    [`DURABLE_REDUCED_AVAILABILITY_LEGACY_STORAGE_CLASS`](constants.md#google.cloud.storage.constants.DURABLE_REDUCED_AVAILABILITY_LEGACY_STORAGE_CLASS),
    else `None`.



#### test_iam_permissions(permissions, client=None, timeout=60, retry=<google.api_core.retry.Retry object>)
API call:  test permissions

See
[https://cloud.google.com/storage/docs/json_api/v1/buckets/testIamPermissions](https://cloud.google.com/storage/docs/json_api/v1/buckets/testIamPermissions)

If `user_project` is set, bills the API request to that project.


* **Parameters**

    
    * **permissions** (*list of string*) – the permissions to check


    * **client** ([`Client`](client.md#google.cloud.storage.client.Client) or
    `NoneType`) – (Optional) The client to use.  If not passed, falls back
    to the `client` stored on the current bucket.


    * **timeout** ([*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)* or *[*tuple*](https://python.readthedocs.io/en/latest/library/stdtypes.html#tuple)) – (Optional) The amount of time, in seconds, to wait
    for the server response.  See: [Configuring Timeouts](retry_timeout.md#configuring-timeouts)


    * **retry** ([*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)* or *[*google.cloud.storage.retry.ConditionalRetryPolicy*](retry.md#google.cloud.storage.retry.ConditionalRetryPolicy)) – (Optional) How to retry the RPC. See: [Configuring Retries](retry_timeout.md#configuring-retries)



* **Return type**

    list of string



* **Returns**

    the permissions returned by the `testIamPermissions` API
    request.



#### _property_ time_created()
Retrieve the timestamp at which the bucket was created.

See [https://cloud.google.com/storage/docs/json_api/v1/buckets](https://cloud.google.com/storage/docs/json_api/v1/buckets)


* **Return type**

    [`datetime.datetime`](https://python.readthedocs.io/en/latest/library/datetime.html#datetime.datetime) or `NoneType`



* **Returns**

    Datetime object parsed from RFC3339 valid timestamp, or
    `None` if the bucket’s resource has not been loaded
    from the server.



#### update(client=None, timeout=60, if_metageneration_match=None, if_metageneration_not_match=None, retry=<google.cloud.storage.retry.ConditionalRetryPolicy object>)
Sends all properties in a PUT request.

Updates the `_properties` with the response from the backend.

If `user_project` is set, bills the API request to that project.


* **Parameters**

    
    * **client** ([`Client`](client.md#google.cloud.storage.client.Client) or
    `NoneType`) – the client to use. If not passed, falls back to the
    `client` stored on the current object.


    * **timeout** ([*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)* or *[*tuple*](https://python.readthedocs.io/en/latest/library/stdtypes.html#tuple)) – (Optional) The amount of time, in seconds, to wait
    for the server response.  See: [Configuring Timeouts](retry_timeout.md#configuring-timeouts)


    * **if_metageneration_match** (*long*) – (Optional) Make the operation conditional on whether the
    blob’s current metageneration matches the given value.


    * **if_metageneration_not_match** (*long*) – (Optional) Make the operation conditional on whether the
    blob’s current metageneration does not match the given value.


    * **retry** ([*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)* or *[*google.cloud.storage.retry.ConditionalRetryPolicy*](retry.md#google.cloud.storage.retry.ConditionalRetryPolicy)) – (Optional) How to retry the RPC. See: [Configuring Retries](retry_timeout.md#configuring-retries)



#### _property_ user_project()
Project ID to be billed for API requests made via this bucket.

If unset, API requests are billed to the bucket owner.

A user project is required for all operations on Requester Pays buckets.

See [https://cloud.google.com/storage/docs/requester-pays#requirements](https://cloud.google.com/storage/docs/requester-pays#requirements) for details.


* **Return type**

    [str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)



#### _property_ versioning_enabled()
Is versioning enabled for this bucket?

See  [https://cloud.google.com/storage/docs/object-versioning](https://cloud.google.com/storage/docs/object-versioning) for
details.


* **Setter**

    Update whether versioning is enabled for this bucket.



* **Getter**

    Query whether versioning is enabled for this bucket.



* **Return type**

    [bool](https://python.readthedocs.io/en/latest/library/functions.html#bool)



* **Returns**

    True if enabled, else False.



### _class_ google.cloud.storage.bucket.IAMConfiguration(bucket, public_access_prevention=<object object>, uniform_bucket_level_access_enabled=<object object>, uniform_bucket_level_access_locked_time=<object object>, bucket_policy_only_enabled=<object object>, bucket_policy_only_locked_time=<object object>)
Bases: [`dict`](https://python.readthedocs.io/en/latest/library/stdtypes.html#dict)

Map a bucket’s IAM configuration.


* **Params bucket**

    Bucket for which this instance is the policy.



* **Params public_access_prevention**

    (Optional) Whether the public access prevention policy is ‘inherited’ (default) or ‘enforced’
    See: [https://cloud.google.com/storage/docs/public-access-prevention](https://cloud.google.com/storage/docs/public-access-prevention)



* **Params bucket_policy_only_enabled**

    (Optional) Whether the IAM-only policy is enabled for the bucket.



* **Params uniform_bucket_level_locked_time**

    (Optional) When the bucket’s IAM-only policy was enabled.
    This value should normally only be set by the back-end API.



* **Params bucket_policy_only_enabled**

    Deprecated alias for `uniform_bucket_level_access_enabled`.



* **Params bucket_policy_only_locked_time**

    Deprecated alias for `uniform_bucket_level_access_locked_time`.



#### _property_ bucket()
Bucket for which this instance is the policy.


* **Return type**

    `Bucket`



* **Returns**

    the instance’s bucket.



#### _property_ bucket_policy_only_enabled()
Deprecated alias for `uniform_bucket_level_access_enabled`.


* **Return type**

    [bool](https://python.readthedocs.io/en/latest/library/functions.html#bool)



* **Returns**

    whether the bucket is configured to allow only IAM.



#### _property_ bucket_policy_only_locked_time()
Deprecated alias for `uniform_bucket_level_access_locked_time`.


* **Return type**

    Union[[`datetime.datetime`](https://python.readthedocs.io/en/latest/library/datetime.html#datetime.datetime), None]



* **Returns**

    (readonly) Time after which `bucket_policy_only_enabled` will
    be frozen as true.



#### clear()

#### copy()

#### _classmethod_ from_api_repr(resource, bucket)
Factory:  construct instance from resource.


* **Params bucket**

    Bucket for which this instance is the policy.



* **Parameters**

    **resource** ([*dict*](https://python.readthedocs.io/en/latest/library/stdtypes.html#dict)) – mapping as returned from API call.



* **Return type**

    `IAMConfiguration`



* **Returns**

    Instance created from resource.



#### fromkeys(value=None, /)
Create a new dictionary with keys from iterable and values set to value.


#### get(key, default=None, /)
Return the value for key if key is in the dictionary, else default.


#### items()

#### keys()

#### pop(k, )
If the key is not found, return the default if given; otherwise,
raise a KeyError.


#### popitem()
Remove and return a (key, value) pair as a 2-tuple.

Pairs are returned in LIFO (last-in, first-out) order.
Raises KeyError if the dict is empty.


#### _property_ public_access_prevention()
Setting for public access prevention policy. Options are ‘inherited’ (default) or ‘enforced’.

> See: [https://cloud.google.com/storage/docs/public-access-prevention](https://cloud.google.com/storage/docs/public-access-prevention)


* **Return type**

    string



* **Returns**

    the public access prevention status, either ‘enforced’ or ‘inherited’.



#### setdefault(key, default=None, /)
Insert key with a value of default if key is not in the dictionary.

Return the value for key if key is in the dictionary, else default.


#### _property_ uniform_bucket_level_access_enabled()
If set, access checks only use bucket-level IAM policies or above.


* **Return type**

    [bool](https://python.readthedocs.io/en/latest/library/functions.html#bool)



* **Returns**

    whether the bucket is configured to allow only IAM.



#### _property_ uniform_bucket_level_access_locked_time()
Deadline for changing `uniform_bucket_level_access_enabled` from true to false.

If the bucket’s `uniform_bucket_level_access_enabled` is true, this property
is time time after which that setting becomes immutable.

If the bucket’s `uniform_bucket_level_access_enabled` is false, this property
is `None`.


* **Return type**

    Union[[`datetime.datetime`](https://python.readthedocs.io/en/latest/library/datetime.html#datetime.datetime), None]



* **Returns**

    (readonly) Time after which `uniform_bucket_level_access_enabled` will
    be frozen as true.



#### update(\*\*F)
If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
In either case, this is followed by: for k in F:  D[k] = F[k]


#### values()

### _class_ google.cloud.storage.bucket.LifecycleRuleAbortIncompleteMultipartUpload(\*\*kw)
Bases: [`dict`](https://python.readthedocs.io/en/latest/library/stdtypes.html#dict)

Map a rule aborting incomplete multipart uploads of matching items.

The “age” lifecycle condition is the only supported condition for this rule.


* **Params kw**

    arguments passed to `LifecycleRuleConditions`.



#### clear()

#### copy()

#### _classmethod_ from_api_repr(resource)
Factory:  construct instance from resource.


* **Parameters**

    **resource** ([*dict*](https://python.readthedocs.io/en/latest/library/stdtypes.html#dict)) – mapping as returned from API call.



* **Return type**

    `LifecycleRuleAbortIncompleteMultipartUpload`



* **Returns**

    Instance created from resource.



#### fromkeys(value=None, /)
Create a new dictionary with keys from iterable and values set to value.


#### get(key, default=None, /)
Return the value for key if key is in the dictionary, else default.


#### items()

#### keys()

#### pop(k, )
If the key is not found, return the default if given; otherwise,
raise a KeyError.


#### popitem()
Remove and return a (key, value) pair as a 2-tuple.

Pairs are returned in LIFO (last-in, first-out) order.
Raises KeyError if the dict is empty.


#### setdefault(key, default=None, /)
Insert key with a value of default if key is not in the dictionary.

Return the value for key if key is in the dictionary, else default.


#### update(\*\*F)
If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
In either case, this is followed by: for k in F:  D[k] = F[k]


#### values()

### _class_ google.cloud.storage.bucket.LifecycleRuleConditions(age=None, created_before=None, is_live=None, matches_storage_class=None, number_of_newer_versions=None, days_since_custom_time=None, custom_time_before=None, days_since_noncurrent_time=None, noncurrent_time_before=None, matches_prefix=None, matches_suffix=None, _factory=False)
Bases: [`dict`](https://python.readthedocs.io/en/latest/library/stdtypes.html#dict)

Map a single lifecycle rule for a bucket.

See: [https://cloud.google.com/storage/docs/lifecycle](https://cloud.google.com/storage/docs/lifecycle)


* **Parameters**

    
    * **age** ([*int*](https://python.readthedocs.io/en/latest/library/functions.html#int)) – (Optional) Apply rule action to items whose age, in days,
    exceeds this value.


    * **created_before** ([*datetime.date*](https://python.readthedocs.io/en/latest/library/datetime.html#datetime.date)) – (Optional) Apply rule action to items created
    before this date.


    * **is_live** ([*bool*](https://python.readthedocs.io/en/latest/library/functions.html#bool)) – (Optional) If true, apply rule action to non-versioned
    items, or to items with no newer versions. If false, apply
    rule action to versioned items with at least one newer
    version.


    * **matches_prefix** ([*list*](https://python.readthedocs.io/en/latest/library/stdtypes.html#list)*(*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*)*) – (Optional) Apply rule action to items which
    any prefix matches the beginning of the item name.


    * **matches_storage_class** (list(str), one or more of
    `Bucket.STORAGE_CLASSES`.) – (Optional) Apply rule action to items
    whose storage class matches this value.


    * **matches_suffix** ([*list*](https://python.readthedocs.io/en/latest/library/stdtypes.html#list)*(*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*)*) – (Optional) Apply rule action to items which
    any suffix matches the end of the item name.


    * **number_of_newer_versions** ([*int*](https://python.readthedocs.io/en/latest/library/functions.html#int)) – (Optional) Apply rule action to versioned
    items having N newer versions.


    * **days_since_custom_time** ([*int*](https://python.readthedocs.io/en/latest/library/functions.html#int)) – (Optional) Apply rule action to items whose number of days
    elapsed since the custom timestamp. This condition is relevant
    only for versioned objects. The value of the field must be a non
    negative integer. If it’s zero, the object version will become
    eligible for lifecycle action as soon as it becomes custom.


    * **custom_time_before** ([`datetime.date`](https://python.readthedocs.io/en/latest/library/datetime.html#datetime.date)) – (Optional)  Date object parsed from RFC3339 valid date, apply rule action
    to items whose custom time is before this date. This condition is relevant
    only for versioned objects, e.g., 2019-03-16.


    * **days_since_noncurrent_time** ([*int*](https://python.readthedocs.io/en/latest/library/functions.html#int)) – (Optional) Apply rule action to items whose number of days
    elapsed since the non current timestamp. This condition
    is relevant only for versioned objects. The value of the field
    must be a non negative integer. If it’s zero, the object version
    will become eligible for lifecycle action as soon as it becomes
    non current.


    * **noncurrent_time_before** ([`datetime.date`](https://python.readthedocs.io/en/latest/library/datetime.html#datetime.date)) – (Optional) Date object parsed from RFC3339 valid date, apply
    rule action to items whose non current time is before this date.
    This condition is relevant only for versioned objects, e.g, 2019-03-16.



* **Raises**

    [**ValueError**](https://python.readthedocs.io/en/latest/library/exceptions.html#ValueError) – if no arguments are passed.



#### _property_ age()
Conditon’s age value.


#### clear()

#### copy()

#### _property_ created_before()
Conditon’s created_before value.


#### _property_ custom_time_before()
Conditon’s ‘custom_time_before’ value.


#### _property_ days_since_custom_time()
Conditon’s ‘days_since_custom_time’ value.


#### _property_ days_since_noncurrent_time()
Conditon’s ‘days_since_noncurrent_time’ value.


#### _classmethod_ from_api_repr(resource)
Factory:  construct instance from resource.


* **Parameters**

    **resource** ([*dict*](https://python.readthedocs.io/en/latest/library/stdtypes.html#dict)) – mapping as returned from API call.



* **Return type**

    `LifecycleRuleConditions`



* **Returns**

    Instance created from resource.



#### fromkeys(value=None, /)
Create a new dictionary with keys from iterable and values set to value.


#### get(key, default=None, /)
Return the value for key if key is in the dictionary, else default.


#### _property_ is_live()
Conditon’s ‘is_live’ value.


#### items()

#### keys()

#### _property_ matches_prefix()
Conditon’s ‘matches_prefix’ value.


#### _property_ matches_storage_class()
Conditon’s ‘matches_storage_class’ value.


#### _property_ matches_suffix()
Conditon’s ‘matches_suffix’ value.


#### _property_ noncurrent_time_before()
Conditon’s ‘noncurrent_time_before’ value.


#### _property_ number_of_newer_versions()
Conditon’s ‘number_of_newer_versions’ value.


#### pop(k, )
If the key is not found, return the default if given; otherwise,
raise a KeyError.


#### popitem()
Remove and return a (key, value) pair as a 2-tuple.

Pairs are returned in LIFO (last-in, first-out) order.
Raises KeyError if the dict is empty.


#### setdefault(key, default=None, /)
Insert key with a value of default if key is not in the dictionary.

Return the value for key if key is in the dictionary, else default.


#### update(\*\*F)
If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
In either case, this is followed by: for k in F:  D[k] = F[k]


#### values()

### _class_ google.cloud.storage.bucket.LifecycleRuleDelete(\*\*kw)
Bases: [`dict`](https://python.readthedocs.io/en/latest/library/stdtypes.html#dict)

Map a lifecycle rule deleting matching items.


* **Params kw**

    arguments passed to `LifecycleRuleConditions`.



#### clear()

#### copy()

#### _classmethod_ from_api_repr(resource)
Factory:  construct instance from resource.


* **Parameters**

    **resource** ([*dict*](https://python.readthedocs.io/en/latest/library/stdtypes.html#dict)) – mapping as returned from API call.



* **Return type**

    `LifecycleRuleDelete`



* **Returns**

    Instance created from resource.



#### fromkeys(value=None, /)
Create a new dictionary with keys from iterable and values set to value.


#### get(key, default=None, /)
Return the value for key if key is in the dictionary, else default.


#### items()

#### keys()

#### pop(k, )
If the key is not found, return the default if given; otherwise,
raise a KeyError.


#### popitem()
Remove and return a (key, value) pair as a 2-tuple.

Pairs are returned in LIFO (last-in, first-out) order.
Raises KeyError if the dict is empty.


#### setdefault(key, default=None, /)
Insert key with a value of default if key is not in the dictionary.

Return the value for key if key is in the dictionary, else default.


#### update(\*\*F)
If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
In either case, this is followed by: for k in F:  D[k] = F[k]


#### values()

### _class_ google.cloud.storage.bucket.LifecycleRuleSetStorageClass(storage_class, \*\*kw)
Bases: [`dict`](https://python.readthedocs.io/en/latest/library/stdtypes.html#dict)

Map a lifecycle rule updating storage class of matching items.


* **Parameters**

    **storage_class** (str, one of `Bucket.STORAGE_CLASSES`.) – new storage class to assign to matching items.



* **Params kw**

    arguments passed to `LifecycleRuleConditions`.



#### clear()

#### copy()

#### _classmethod_ from_api_repr(resource)
Factory:  construct instance from resource.


* **Parameters**

    **resource** ([*dict*](https://python.readthedocs.io/en/latest/library/stdtypes.html#dict)) – mapping as returned from API call.



* **Return type**

    `LifecycleRuleSetStorageClass`



* **Returns**

    Instance created from resource.



#### fromkeys(value=None, /)
Create a new dictionary with keys from iterable and values set to value.


#### get(key, default=None, /)
Return the value for key if key is in the dictionary, else default.


#### items()

#### keys()

#### pop(k, )
If the key is not found, return the default if given; otherwise,
raise a KeyError.


#### popitem()
Remove and return a (key, value) pair as a 2-tuple.

Pairs are returned in LIFO (last-in, first-out) order.
Raises KeyError if the dict is empty.


#### setdefault(key, default=None, /)
Insert key with a value of default if key is not in the dictionary.

Return the value for key if key is in the dictionary, else default.


#### update(\*\*F)
If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
In either case, this is followed by: for k in F:  D[k] = F[k]


#### values()
