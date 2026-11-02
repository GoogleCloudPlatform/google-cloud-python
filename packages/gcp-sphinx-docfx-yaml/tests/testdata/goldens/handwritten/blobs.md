# Blobs / Objects

Create / interact with Google Cloud Storage blobs.


### _class_ google.cloud.storage.blob.Blob(name, bucket, chunk_size=None, encryption_key=None, kms_key_name=None, generation=None)
Bases: `google.cloud.storage._helpers._PropertyMixin`

A wrapper around Cloud Storage’s concept of an `Object`.


* **Parameters**

    
    * **name** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – The name of the blob.  This corresponds to the unique path of
    the object in the bucket. If bytes, will be converted to a
    unicode object. Blob / object names can contain any sequence
    of valid unicode characters, of length 1-1024 bytes when
    UTF-8 encoded.


    * **bucket** ([`google.cloud.storage.bucket.Bucket`](buckets.md#google.cloud.storage.bucket.Bucket)) – The bucket to which this blob belongs.


    * **chunk_size** ([*int*](https://python.readthedocs.io/en/latest/library/functions.html#int)) – (Optional) The size of a chunk of data whenever iterating (in bytes).
    This must be a multiple of 256 KB per the API specification. If not
    specified, the chunk_size of the blob itself is used. If that is not
    specified, a default value of 40 MB is used.


    * **encryption_key** ([*bytes*](https://python.readthedocs.io/en/latest/library/stdtypes.html#bytes)) – (Optional) 32 byte encryption key for customer-supplied encryption.
    See [https://cloud.google.com/storage/docs/encryption#customer-supplied](https://cloud.google.com/storage/docs/encryption#customer-supplied).


    * **kms_key_name** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) Resource name of Cloud KMS key used to encrypt the blob’s
    contents.


    * **generation** (*long*) – (Optional) If present, selects a specific revision of this object.


property `name`

    Get the blob’s name.


#### STORAGE_CLASSES(_ = ('STANDARD', 'NEARLINE', 'COLDLINE', 'ARCHIVE', 'MULTI_REGIONAL', 'REGIONAL'_ )
Allowed values for `storage_class`.

See
[https://cloud.google.com/storage/docs/json_api/v1/objects#storageClass](https://cloud.google.com/storage/docs/json_api/v1/objects#storageClass)
[https://cloud.google.com/storage/docs/per-object-storage-class](https://cloud.google.com/storage/docs/per-object-storage-class)

**NOTE**: This list does not include ‘DURABLE_REDUCED_AVAILABILITY’, which
is only documented for buckets (and deprecated).


#### _property_ acl()
Create our ACL on demand.


#### _property_ bucket()
Bucket which contains the object.


* **Return type**

    [`Bucket`](buckets.md#google.cloud.storage.bucket.Bucket)



* **Returns**

    The object’s bucket.



#### _property_ cache_control()
HTTP ‘Cache-Control’ header for this object.

See [RFC 7234]([https://tools.ietf.org/html/rfc7234#section-5.2](https://tools.ietf.org/html/rfc7234#section-5.2))
and [API reference docs]([https://cloud.google.com/storage/docs/json_api/v1/objects](https://cloud.google.com/storage/docs/json_api/v1/objects)).


* **Return type**

    str or `NoneType`



#### _property_ chunk_size()
Get the blob’s default chunk size.


* **Return type**

    int or `NoneType`



* **Returns**

    The current blob’s chunk size, if it is set.



#### _property_ client()
The client bound to this blob.


#### _property_ component_count()
Number of underlying components that make up this object.

See [https://cloud.google.com/storage/docs/json_api/v1/objects](https://cloud.google.com/storage/docs/json_api/v1/objects)


* **Return type**

    int or `NoneType`



* **Returns**

    The component count (in case of a composed object) or
    `None` if the blob’s resource has not been loaded from
    the server.  This property will not be set on objects
    not created via `compose`.



#### compose(sources, client=None, timeout=60, if_generation_match=None, if_metageneration_match=None, if_source_generation_match=None, retry=<google.cloud.storage.retry.ConditionalRetryPolicy object>)
Concatenate source blobs into this one.

If `user_project` is set on the bucket, bills the API request
to that project.

See [API reference docs]([https://cloud.google.com/storage/docs/json_api/v1/objects/compose](https://cloud.google.com/storage/docs/json_api/v1/objects/compose))
and a [code sample]([https://cloud.google.com/storage/docs/samples/storage-compose-file#storage_compose_file-python](https://cloud.google.com/storage/docs/samples/storage-compose-file#storage_compose_file-python)).


* **Parameters**

    
    * **sources** (list of `Blob`) – Blobs whose contents will be composed into this blob.


    * **client** ([`Client`](client.md#google.cloud.storage.client.Client)) – (Optional) The client to use. If not passed, falls back to the
    `client` stored on the blob’s bucket.


    * **timeout** ([*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)* or *[*tuple*](https://python.readthedocs.io/en/latest/library/stdtypes.html#tuple)) – (Optional) The amount of time, in seconds, to wait
    for the server response.  See: [Configuring Timeouts](retry_timeout.md#configuring-timeouts)


    * **if_generation_match** (*long*) – (Optional) Makes the operation conditional on whether the
    destination object’s current generation matches the given value.
    Setting to 0 makes the operation succeed only if there are no live
    versions of the object.
    Note: In a previous version, this argument worked identically to the
    `if_source_generation_match` argument. For
    backwards-compatibility reasons, if a list is passed in,
    this argument will behave like `if_source_generation_match`
    and also issue a DeprecationWarning.


    * **if_metageneration_match** (*long*) – (Optional) Makes the operation conditional on whether the
    destination object’s current metageneration matches the given
    value.

    If a list of long is passed in, no match operation will be
    performed.  (Deprecated: type(list of long) is supported for
    backwards-compatability reasons only.)



    * **if_source_generation_match** (*list of long*) – (Optional) Makes the operation conditional on whether the current
    generation of each source blob matches the corresponding generation.
    The list must match `sources` item-to-item.


    * **retry** ([*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)* or *[*google.cloud.storage.retry.ConditionalRetryPolicy*](retry.md#google.cloud.storage.retry.ConditionalRetryPolicy)) – (Optional) How to retry the RPC. See: [Configuring Retries](retry_timeout.md#configuring-retries)



#### _property_ content_disposition()
HTTP ‘Content-Disposition’ header for this object.

See [RFC 6266]([https://tools.ietf.org/html/rfc7234#section-5.2](https://tools.ietf.org/html/rfc7234#section-5.2)) and
[API reference docs]([https://cloud.google.com/storage/docs/json_api/v1/objects](https://cloud.google.com/storage/docs/json_api/v1/objects)).


* **Return type**

    str or `NoneType`



#### _property_ content_encoding()
HTTP ‘Content-Encoding’ header for this object.

See [RFC 7231]([https://tools.ietf.org/html/rfc7231#section-3.1.2.2](https://tools.ietf.org/html/rfc7231#section-3.1.2.2)) and
[API reference docs]([https://cloud.google.com/storage/docs/json_api/v1/objects](https://cloud.google.com/storage/docs/json_api/v1/objects)).


* **Return type**

    str or `NoneType`



#### _property_ content_language()
HTTP ‘Content-Language’ header for this object.

See [BCP47]([https://tools.ietf.org/html/bcp47](https://tools.ietf.org/html/bcp47)) and
[API reference docs]([https://cloud.google.com/storage/docs/json_api/v1/objects](https://cloud.google.com/storage/docs/json_api/v1/objects)).


* **Return type**

    str or `NoneType`



#### _property_ content_type()
HTTP ‘Content-Type’ header for this object.

See [RFC 2616]([https://tools.ietf.org/html/rfc2616#section-14.17](https://tools.ietf.org/html/rfc2616#section-14.17)) and
[API reference docs]([https://cloud.google.com/storage/docs/json_api/v1/objects](https://cloud.google.com/storage/docs/json_api/v1/objects)).


* **Return type**

    str or `NoneType`



#### _property_ crc32c()
CRC32C checksum for this object.

This returns the blob’s CRC32C checksum. To retrieve the value, first use a
reload method of the Blob class which loads the blob’s properties from the server.

See [RFC 4960]([https://tools.ietf.org/html/rfc4960#appendix-B](https://tools.ietf.org/html/rfc4960#appendix-B)) and
[API reference docs]([https://cloud.google.com/storage/docs/json_api/v1/objects](https://cloud.google.com/storage/docs/json_api/v1/objects)).

If not set before upload, the server will compute the hash.


* **Return type**

    str or `NoneType`



#### create_resumable_upload_session(content_type=None, size=None, origin=None, client=None, timeout=60, checksum=None, predefined_acl=None, if_generation_match=None, if_generation_not_match=None, if_metageneration_match=None, if_metageneration_not_match=None, retry=<google.cloud.storage.retry.ConditionalRetryPolicy object>)
Create a resumable upload session.

Resumable upload sessions allow you to start an upload session from
one client and complete the session in another. This method is called
by the initiator to set the metadata and limits. The initiator then
passes the session URL to the client that will upload the binary data.
The client performs a PUT request on the session URL to complete the
upload. This process allows untrusted clients to upload to an
access-controlled bucket.

For more details, see the
documentation on [signed URLs]([https://cloud.google.com/storage/docs/access-control/signed-urls#signing-resumable](https://cloud.google.com/storage/docs/access-control/signed-urls#signing-resumable)).

The content type of the upload will be determined in order
of precedence:


* The value passed in to this method (if not [`None`](https://python.readthedocs.io/en/latest/library/constants.html#None))


* The value stored on the current blob


* The default value (‘application/octet-stream’)

**NOTE**: The effect of uploading to an existing blob depends on the
“versioning” and “lifecycle” policies defined on the blob’s
bucket.  In the absence of those policies, upload will
overwrite any existing contents.

See the [object versioning]([https://cloud.google.com/storage/docs/object-versioning](https://cloud.google.com/storage/docs/object-versioning))
and [lifecycle]([https://cloud.google.com/storage/docs/lifecycle](https://cloud.google.com/storage/docs/lifecycle))
API documents for details.

If `encryption_key` is set, the blob will be encrypted with
a [customer-supplied]([https://cloud.google.com/storage/docs/encryption#customer-supplied](https://cloud.google.com/storage/docs/encryption#customer-supplied))
encryption key.

If `user_project` is set on the bucket, bills the API request
to that project.


* **Parameters**

    
    * **size** ([*int*](https://python.readthedocs.io/en/latest/library/functions.html#int)) – (Optional) The maximum number of bytes that can be uploaded using
    this session. If the size is not known when creating the session,
    this should be left blank.


    * **content_type** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) Type of content being uploaded.


    * **origin** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) If set, the upload can only be completed by a user-agent
    that uploads from the given origin. This can be useful when passing
    the session to a web client.


    * **client** ([`Client`](client.md#google.cloud.storage.client.Client)) – (Optional) The client to use.  If not passed, falls back to the
    `client` stored on the blob’s bucket.


    * **timeout** ([*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)* or *[*tuple*](https://python.readthedocs.io/en/latest/library/stdtypes.html#tuple)) – (Optional) The amount of time, in seconds, to wait
    for the server response.  See: [Configuring Timeouts](retry_timeout.md#configuring-timeouts)


    * **checksum** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) The type of checksum to compute to verify
    the integrity of the object. After the upload is complete, the
    server-computed checksum of the resulting object will be checked
    and google.resumable_media.common.DataCorruption will be raised on
    a mismatch. On a validation failure, the client will attempt to
    delete the uploaded object automatically. Supported values
    are “md5”, “crc32c” and None. The default is None.


    * **predefined_acl** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) Predefined access control list


    * **if_generation_match** (*long*) – (Optional) See [Using if_generation_match](generation_metageneration.md#using-if-generation-match)


    * **if_generation_not_match** (*long*) – (Optional) See [Using if_generation_not_match](generation_metageneration.md#using-if-generation-not-match)


    * **if_metageneration_match** (*long*) – (Optional) See [Using if_metageneration_match](generation_metageneration.md#using-if-metageneration-match)


    * **if_metageneration_not_match** (*long*) – (Optional) See [Using if_metageneration_not_match](generation_metageneration.md#using-if-metageneration-not-match)


    * **retry** ([*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)* or *[*google.cloud.storage.retry.ConditionalRetryPolicy*](retry.md#google.cloud.storage.retry.ConditionalRetryPolicy)) – (Optional) How to retry the RPC. A None value will disable
    retries. A google.api_core.retry.Retry value will enable retries,
    and the object will define retriable response codes and errors and
    configure backoff and timeout options.
    A google.cloud.storage.retry.ConditionalRetryPolicy value wraps a
    Retry object and activates it only if certain conditions are met.
    This class exists to provide safe defaults for RPC calls that are
    not technically safe to retry normally (due to potential data
    duplication or other side-effects) but become safe to retry if a
    condition such as if_generation_match is set.
    See the retry.py source code and docstrings in this package
    (google.cloud.storage.retry) for information on retry types and how
    to configure them.
    Media operations (downloads and uploads) do not support non-default
    predicates in a Retry object. The default will always be used. Other
    configuration changes for Retry objects such as delays and deadlines
    are respected.



* **Return type**

    [str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)



* **Returns**

    The resumable upload session URL. The upload can be
    completed by making an HTTP PUT request with the
    file’s contents.



* **Raises**

    `google.cloud.exceptions.GoogleCloudError`
    if the session creation response returns an error status.



#### _property_ custom_time()
Retrieve the custom time for the object.

See [https://cloud.google.com/storage/docs/json_api/v1/objects](https://cloud.google.com/storage/docs/json_api/v1/objects)


* **Return type**

    [`datetime.datetime`](https://python.readthedocs.io/en/latest/library/datetime.html#datetime.datetime) or `NoneType`



* **Returns**

    Datetime object parsed from RFC3339 valid timestamp, or
    `None` if the blob’s resource has not been loaded from
    the server (see `reload()`).



#### delete(client=None, if_generation_match=None, if_generation_not_match=None, if_metageneration_match=None, if_metageneration_not_match=None, timeout=60, retry=<google.cloud.storage.retry.ConditionalRetryPolicy object>)
Deletes a blob from Cloud Storage.

If `user_project` is set on the bucket, bills the API request
to that project.


* **Parameters**

    
    * **client** ([`Client`](client.md#google.cloud.storage.client.Client)) – (Optional) The client to use. If not passed, falls back to the
    `client` stored on the blob’s bucket.


    * **if_generation_match** (*long*) – (Optional) See [Using if_generation_match](generation_metageneration.md#using-if-generation-match)


    * **if_generation_not_match** (*long*) – (Optional) See [Using if_generation_not_match](generation_metageneration.md#using-if-generation-not-match)


    * **if_metageneration_match** (*long*) – (Optional) See [Using if_metageneration_match](generation_metageneration.md#using-if-metageneration-match)


    * **if_metageneration_not_match** (*long*) – (Optional) See [Using if_metageneration_not_match](generation_metageneration.md#using-if-metageneration-not-match)


    * **timeout** ([*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)* or *[*tuple*](https://python.readthedocs.io/en/latest/library/stdtypes.html#tuple)) – (Optional) The amount of time, in seconds, to wait
    for the server response.  See: [Configuring Timeouts](retry_timeout.md#configuring-timeouts)


    * **retry** ([*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)* or *[*google.cloud.storage.retry.ConditionalRetryPolicy*](retry.md#google.cloud.storage.retry.ConditionalRetryPolicy)) – (Optional) How to retry the RPC. See: [Configuring Retries](retry_timeout.md#configuring-retries)



* **Raises**

    `google.cloud.exceptions.NotFound`
    (propagated from
    [`google.cloud.storage.bucket.Bucket.delete_blob()`](buckets.md#google.cloud.storage.bucket.Bucket.delete_blob)).



#### download_as_bytes(client=None, start=None, end=None, raw_download=False, if_etag_match=None, if_etag_not_match=None, if_generation_match=None, if_generation_not_match=None, if_metageneration_match=None, if_metageneration_not_match=None, timeout=60, checksum='md5', retry=<google.api_core.retry.Retry object>)
Download the contents of this blob as a bytes object.

If `user_project` is set on the bucket, bills the API request
to that project.


* **Parameters**

    
    * **client** ([`Client`](client.md#google.cloud.storage.client.Client)) – (Optional) The client to use. If not passed, falls back to the
    `client` stored on the blob’s bucket.


    * **start** ([*int*](https://python.readthedocs.io/en/latest/library/functions.html#int)) – (Optional) The first byte in a range to be downloaded.


    * **end** ([*int*](https://python.readthedocs.io/en/latest/library/functions.html#int)) – (Optional) The last byte in a range to be downloaded.


    * **raw_download** ([*bool*](https://python.readthedocs.io/en/latest/library/functions.html#bool)) – (Optional) If true, download the object without any expansion.


    * **if_etag_match** (*Union**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*, **Set**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*]**]*) – (Optional) See [Using if_etag_match](generation_metageneration.md#using-if-etag-match)


    * **if_etag_not_match** (*Union**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*, **Set**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*]**]*) – (Optional) See [Using if_etag_not_match](generation_metageneration.md#using-if-etag-not-match)


    * **if_generation_match** (*long*) – (Optional) See [Using if_generation_match](generation_metageneration.md#using-if-generation-match)


    * **if_generation_not_match** (*long*) – (Optional) See [Using if_generation_not_match](generation_metageneration.md#using-if-generation-not-match)


    * **if_metageneration_match** (*long*) – (Optional) See [Using if_metageneration_match](generation_metageneration.md#using-if-metageneration-match)


    * **if_metageneration_not_match** (*long*) – (Optional) See [Using if_metageneration_not_match](generation_metageneration.md#using-if-metageneration-not-match)


    * **timeout** ([*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)* or *[*tuple*](https://python.readthedocs.io/en/latest/library/stdtypes.html#tuple)) – (Optional) The amount of time, in seconds, to wait
    for the server response.  See: [Configuring Timeouts](retry_timeout.md#configuring-timeouts)


    * **checksum** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) The type of checksum to compute to verify the integrity
    of the object. The response headers must contain a checksum of the
    requested type. If the headers lack an appropriate checksum (for
    instance in the case of transcoded or ranged downloads where the
    remote service does not know the correct checksum, including
    downloads where chunk_size is set) an INFO-level log will be
    emitted. Supported values are “md5”, “crc32c” and None. The default
    is “md5”.


    * **retry** ([*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)* or *[*google.cloud.storage.retry.ConditionalRetryPolicy*](retry.md#google.cloud.storage.retry.ConditionalRetryPolicy)) – (Optional) How to retry the RPC. A None value will disable
    retries. A google.api_core.retry.Retry value will enable retries,
    and the object will define retriable response codes and errors and
    configure backoff and timeout options.

    A google.cloud.storage.retry.ConditionalRetryPolicy value wraps a
    Retry object and activates it only if certain conditions are met.
    This class exists to provide safe defaults for RPC calls that are
    not technically safe to retry normally (due to potential data
    duplication or other side-effects) but become safe to retry if a
    condition such as if_metageneration_match is set.

    See the retry.py source code and docstrings in this package
    (google.cloud.storage.retry) for information on retry types and how
    to configure them.

    Media operations (downloads and uploads) do not support non-default
    predicates in a Retry object. The default will always be used. Other
    configuration changes for Retry objects such as delays and deadlines
    are respected.




* **Return type**

    [bytes](https://python.readthedocs.io/en/latest/library/stdtypes.html#bytes)



* **Returns**

    The data stored in this blob.



* **Raises**

    `google.cloud.exceptions.NotFound`



#### download_as_string(client=None, start=None, end=None, raw_download=False, if_etag_match=None, if_etag_not_match=None, if_generation_match=None, if_generation_not_match=None, if_metageneration_match=None, if_metageneration_not_match=None, timeout=60, retry=<google.api_core.retry.Retry object>)
(Deprecated) Download the contents of this blob as a bytes object.

If `user_project` is set on the bucket, bills the API request
to that project.

**NOTE**: Deprecated alias for `download_as_bytes()`.


* **Parameters**

    
    * **client** ([`Client`](client.md#google.cloud.storage.client.Client)) – (Optional) The client to use. If not passed, falls back to the
    `client` stored on the blob’s bucket.


    * **start** ([*int*](https://python.readthedocs.io/en/latest/library/functions.html#int)) – (Optional) The first byte in a range to be downloaded.


    * **end** ([*int*](https://python.readthedocs.io/en/latest/library/functions.html#int)) – (Optional) The last byte in a range to be downloaded.


    * **raw_download** ([*bool*](https://python.readthedocs.io/en/latest/library/functions.html#bool)) – (Optional) If true, download the object without any expansion.


    * **if_etag_match** (*Union**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*, **Set**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*]**]*) – (Optional) See [Using if_etag_match](generation_metageneration.md#using-if-etag-match)


    * **if_etag_not_match** (*Union**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*, **Set**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*]**]*) – (Optional) See [Using if_etag_not_match](generation_metageneration.md#using-if-etag-not-match)


    * **if_generation_match** (*long*) – (Optional) See [Using if_generation_match](generation_metageneration.md#using-if-generation-match)


    * **if_generation_not_match** (*long*) – (Optional) See [Using if_generation_not_match](generation_metageneration.md#using-if-generation-not-match)


    * **if_metageneration_match** (*long*) – (Optional) See [Using if_metageneration_match](generation_metageneration.md#using-if-metageneration-match)


    * **if_metageneration_not_match** (*long*) – (Optional) See [Using if_metageneration_not_match](generation_metageneration.md#using-if-metageneration-not-match)


    * **timeout** ([*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)* or *[*tuple*](https://python.readthedocs.io/en/latest/library/stdtypes.html#tuple)) – (Optional) The amount of time, in seconds, to wait
    for the server response.  See: [Configuring Timeouts](retry_timeout.md#configuring-timeouts)


    * **retry** ([*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)* or *[*google.cloud.storage.retry.ConditionalRetryPolicy*](retry.md#google.cloud.storage.retry.ConditionalRetryPolicy)) – (Optional) How to retry the RPC. A None value will disable
    retries. A google.api_core.retry.Retry value will enable retries,
    and the object will define retriable response codes and errors and
    configure backoff and timeout options.

    A google.cloud.storage.retry.ConditionalRetryPolicy value wraps a
    Retry object and activates it only if certain conditions are met.
    This class exists to provide safe defaults for RPC calls that are
    not technically safe to retry normally (due to potential data
    duplication or other side-effects) but become safe to retry if a
    condition such as if_metageneration_match is set.

    See the retry.py source code and docstrings in this package
    (google.cloud.storage.retry) for information on retry types and how
    to configure them.

    Media operations (downloads and uploads) do not support non-default
    predicates in a Retry object. The default will always be used. Other
    configuration changes for Retry objects such as delays and deadlines
    are respected.




* **Return type**

    [bytes](https://python.readthedocs.io/en/latest/library/stdtypes.html#bytes)



* **Returns**

    The data stored in this blob.



* **Raises**

    `google.cloud.exceptions.NotFound`



#### download_as_text(client=None, start=None, end=None, raw_download=False, encoding=None, if_etag_match=None, if_etag_not_match=None, if_generation_match=None, if_generation_not_match=None, if_metageneration_match=None, if_metageneration_not_match=None, timeout=60, retry=<google.api_core.retry.Retry object>)
Download the contents of this blob as text (*not* bytes).

If `user_project` is set on the bucket, bills the API request
to that project.


* **Parameters**

    
    * **client** ([`Client`](client.md#google.cloud.storage.client.Client)) – (Optional) The client to use. If not passed, falls back to the
    `client` stored on the blob’s bucket.


    * **start** ([*int*](https://python.readthedocs.io/en/latest/library/functions.html#int)) – (Optional) The first byte in a range to be downloaded.


    * **end** ([*int*](https://python.readthedocs.io/en/latest/library/functions.html#int)) – (Optional) The last byte in a range to be downloaded.


    * **raw_download** ([*bool*](https://python.readthedocs.io/en/latest/library/functions.html#bool)) – (Optional) If true, download the object without any expansion.


    * **encoding** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) encoding to be used to decode the
    downloaded bytes.  Defaults to the `charset` param of
    attr:content_type, or else to “utf-8”.


    * **if_etag_match** (*Union**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*, **Set**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*]**]*) – (Optional) See [Using if_etag_match](generation_metageneration.md#using-if-etag-match)


    * **if_etag_not_match** (*Union**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*, **Set**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*]**]*) – (Optional) See [Using if_etag_not_match](generation_metageneration.md#using-if-etag-not-match)


    * **if_generation_match** (*long*) – (Optional) See [Using if_generation_match](generation_metageneration.md#using-if-generation-match)


    * **if_generation_not_match** (*long*) – (Optional) See [Using if_generation_not_match](generation_metageneration.md#using-if-generation-not-match)


    * **if_metageneration_match** (*long*) – (Optional) See [Using if_metageneration_match](generation_metageneration.md#using-if-metageneration-match)


    * **if_metageneration_not_match** (*long*) – (Optional) See [Using if_metageneration_not_match](generation_metageneration.md#using-if-metageneration-not-match)


    * **timeout** ([*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)* or *[*tuple*](https://python.readthedocs.io/en/latest/library/stdtypes.html#tuple)) – (Optional) The amount of time, in seconds, to wait
    for the server response.  See: [Configuring Timeouts](retry_timeout.md#configuring-timeouts)


    * **retry** ([*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)* or *[*google.cloud.storage.retry.ConditionalRetryPolicy*](retry.md#google.cloud.storage.retry.ConditionalRetryPolicy)) – (Optional) How to retry the RPC. A None value will disable
    retries. A google.api_core.retry.Retry value will enable retries,
    and the object will define retriable response codes and errors and
    configure backoff and timeout options.

    A google.cloud.storage.retry.ConditionalRetryPolicy value wraps a
    Retry object and activates it only if certain conditions are met.
    This class exists to provide safe defaults for RPC calls that are
    not technically safe to retry normally (due to potential data
    duplication or other side-effects) but become safe to retry if a
    condition such as if_metageneration_match is set.

    See the retry.py source code and docstrings in this package
    (google.cloud.storage.retry) for information on retry types and how
    to configure them.

    Media operations (downloads and uploads) do not support non-default
    predicates in a Retry object. The default will always be used. Other
    configuration changes for Retry objects such as delays and deadlines
    are respected.




* **Return type**

    text



* **Returns**

    The data stored in this blob, decoded to text.



#### download_to_file(file_obj, client=None, start=None, end=None, raw_download=False, if_etag_match=None, if_etag_not_match=None, if_generation_match=None, if_generation_not_match=None, if_metageneration_match=None, if_metageneration_not_match=None, timeout=60, checksum='md5', retry=<google.api_core.retry.Retry object>)
DEPRECATED. Download the contents of this blob into a file-like object.

**NOTE**: If the server-set property, `media_link`, is not yet
initialized, makes an additional API request to load it.

If the `chunk_size` of a current blob is None, will download data
in single download request otherwise it will download the `chunk_size`
of data in each request.

For more fine-grained control over the download process, check out
[google-resumable-media]([https://googleapis.dev/python/google-resumable-media/latest/index.html](https://googleapis.dev/python/google-resumable-media/latest/index.html)).
For example, this library allows downloading **parts** of a blob rather than the whole thing.

If `user_project` is set on the bucket, bills the API request
to that project.


* **Parameters**

    
    * **file_obj** (*file*) – A file handle to which to write the blob’s data.


    * **client** ([`Client`](client.md#google.cloud.storage.client.Client)) – (Optional) The client to use.  If not passed, falls back to the
    `client` stored on the blob’s bucket.


    * **start** ([*int*](https://python.readthedocs.io/en/latest/library/functions.html#int)) – (Optional) The first byte in a range to be downloaded.


    * **end** ([*int*](https://python.readthedocs.io/en/latest/library/functions.html#int)) – (Optional) The last byte in a range to be downloaded.


    * **raw_download** ([*bool*](https://python.readthedocs.io/en/latest/library/functions.html#bool)) – (Optional) If true, download the object without any expansion.


    * **if_etag_match** (*Union**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*, **Set**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*]**]*) – (Optional) See [Using if_etag_match](generation_metageneration.md#using-if-etag-match)


    * **if_etag_not_match** (*Union**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*, **Set**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*]**]*) – (Optional) See [Using if_etag_not_match](generation_metageneration.md#using-if-etag-not-match)


    * **if_generation_match** (*long*) – (Optional) See [Using if_generation_match](generation_metageneration.md#using-if-generation-match)


    * **if_generation_not_match** (*long*) – (Optional) See [Using if_generation_not_match](generation_metageneration.md#using-if-generation-not-match)


    * **if_metageneration_match** (*long*) – (Optional) See [Using if_metageneration_match](generation_metageneration.md#using-if-metageneration-match)


    * **if_metageneration_not_match** (*long*) – (Optional) See [Using if_metageneration_not_match](generation_metageneration.md#using-if-metageneration-not-match)


    * **timeout** ([*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)* or *[*tuple*](https://python.readthedocs.io/en/latest/library/stdtypes.html#tuple)) – (Optional) The amount of time, in seconds, to wait
    for the server response.  See: [Configuring Timeouts](retry_timeout.md#configuring-timeouts)


    * **checksum** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) The type of checksum to compute to verify the integrity
    of the object. The response headers must contain a checksum of the
    requested type. If the headers lack an appropriate checksum (for
    instance in the case of transcoded or ranged downloads where the
    remote service does not know the correct checksum, including
    downloads where chunk_size is set) an INFO-level log will be
    emitted. Supported values are “md5”, “crc32c” and None. The default
    is “md5”.


    * **retry** ([*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)* or *[*google.cloud.storage.retry.ConditionalRetryPolicy*](retry.md#google.cloud.storage.retry.ConditionalRetryPolicy)) – (Optional) How to retry the RPC. A None value will disable
    retries. A google.api_core.retry.Retry value will enable retries,
    and the object will define retriable response codes and errors and
    configure backoff and timeout options.

    A google.cloud.storage.retry.ConditionalRetryPolicy value wraps a
    Retry object and activates it only if certain conditions are met.
    This class exists to provide safe defaults for RPC calls that are
    not technically safe to retry normally (due to potential data
    duplication or other side-effects) but become safe to retry if a
    condition such as if_metageneration_match is set.

    See the retry.py source code and docstrings in this package
    (google.cloud.storage.retry) for information on retry types and how
    to configure them.

    Media operations (downloads and uploads) do not support non-default
    predicates in a Retry object. The default will always be used. Other
    configuration changes for Retry objects such as delays and deadlines
    are respected.




* **Raises**

    `google.cloud.exceptions.NotFound`



#### download_to_filename(filename, client=None, start=None, end=None, raw_download=False, if_etag_match=None, if_etag_not_match=None, if_generation_match=None, if_generation_not_match=None, if_metageneration_match=None, if_metageneration_not_match=None, timeout=60, checksum='md5', retry=<google.api_core.retry.Retry object>)
Download the contents of this blob into a named file.

If `user_project` is set on the bucket, bills the API request
to that project.

See a [code sample]([https://cloud.google.com/storage/docs/samples/storage-download-encrypted-file#storage_download_encrypted_file-python](https://cloud.google.com/storage/docs/samples/storage-download-encrypted-file#storage_download_encrypted_file-python))
to download a file with a [customer-supplied encryption key]([https://cloud.google.com/storage/docs/encryption#customer-supplied](https://cloud.google.com/storage/docs/encryption#customer-supplied)).


* **Parameters**

    
    * **filename** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – A filename to be passed to `open`.


    * **client** ([`Client`](client.md#google.cloud.storage.client.Client)) – (Optional) The client to use. If not passed, falls back to the
    `client` stored on the blob’s bucket.


    * **start** ([*int*](https://python.readthedocs.io/en/latest/library/functions.html#int)) – (Optional) The first byte in a range to be downloaded.


    * **end** ([*int*](https://python.readthedocs.io/en/latest/library/functions.html#int)) – (Optional) The last byte in a range to be downloaded.


    * **raw_download** ([*bool*](https://python.readthedocs.io/en/latest/library/functions.html#bool)) – (Optional) If true, download the object without any expansion.


    * **if_etag_match** (*Union**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*, **Set**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*]**]*) – (Optional) See [Using if_etag_match](generation_metageneration.md#using-if-etag-match)


    * **if_etag_not_match** (*Union**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*, **Set**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*]**]*) – (Optional) See [Using if_etag_not_match](generation_metageneration.md#using-if-etag-not-match)


    * **if_generation_match** (*long*) – (Optional) See [Using if_generation_match](generation_metageneration.md#using-if-generation-match)


    * **if_generation_not_match** (*long*) – (Optional) See [Using if_generation_not_match](generation_metageneration.md#using-if-generation-not-match)


    * **if_metageneration_match** (*long*) – (Optional) See [Using if_metageneration_match](generation_metageneration.md#using-if-metageneration-match)


    * **if_metageneration_not_match** (*long*) – (Optional) See [Using if_metageneration_not_match](generation_metageneration.md#using-if-metageneration-not-match)


    * **timeout** ([*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)* or *[*tuple*](https://python.readthedocs.io/en/latest/library/stdtypes.html#tuple)) – (Optional) The amount of time, in seconds, to wait
    for the server response.  See: [Configuring Timeouts](retry_timeout.md#configuring-timeouts)


    * **checksum** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) The type of checksum to compute to verify the integrity
    of the object. The response headers must contain a checksum of the
    requested type. If the headers lack an appropriate checksum (for
    instance in the case of transcoded or ranged downloads where the
    remote service does not know the correct checksum, including
    downloads where chunk_size is set) an INFO-level log will be
    emitted. Supported values are “md5”, “crc32c” and None. The default
    is “md5”.


    * **retry** ([*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)* or *[*google.cloud.storage.retry.ConditionalRetryPolicy*](retry.md#google.cloud.storage.retry.ConditionalRetryPolicy)) – (Optional) How to retry the RPC. A None value will disable
    retries. A google.api_core.retry.Retry value will enable retries,
    and the object will define retriable response codes and errors and
    configure backoff and timeout options.

    A google.cloud.storage.retry.ConditionalRetryPolicy value wraps a
    Retry object and activates it only if certain conditions are met.
    This class exists to provide safe defaults for RPC calls that are
    not technically safe to retry normally (due to potential data
    duplication or other side-effects) but become safe to retry if a
    condition such as if_metageneration_match is set.

    See the retry.py source code and docstrings in this package
    (google.cloud.storage.retry) for information on retry types and how
    to configure them.

    Media operations (downloads and uploads) do not support non-default
    predicates in a Retry object. The default will always be used. Other
    configuration changes for Retry objects such as delays and deadlines
    are respected.




* **Raises**

    `google.cloud.exceptions.NotFound`



#### _property_ encryption_key()
Retrieve the customer-supplied encryption key for the object.


* **Return type**

    bytes or `NoneType`



* **Returns**

    The encryption key or `None` if no customer-supplied encryption key was used,
    or the blob’s resource has not been loaded from the server.



#### _property_ etag()
Retrieve the ETag for the object.

See [RFC 2616 (etags)]([https://tools.ietf.org/html/rfc2616#section-3.11](https://tools.ietf.org/html/rfc2616#section-3.11)) and
[API reference docs]([https://cloud.google.com/storage/docs/json_api/v1/objects](https://cloud.google.com/storage/docs/json_api/v1/objects)).


* **Return type**

    str or `NoneType`



* **Returns**

    The blob etag or `None` if the blob’s resource has not
    been loaded from the server.



#### _property_ event_based_hold()
Is an event-based hold active on the object?

See [API reference docs]([https://cloud.google.com/storage/docs/json_api/v1/objects](https://cloud.google.com/storage/docs/json_api/v1/objects)).

If the property is not set locally, returns [`None`](https://python.readthedocs.io/en/latest/library/constants.html#None).


* **Return type**

    bool or `NoneType`



#### exists(client=None, if_etag_match=None, if_etag_not_match=None, if_generation_match=None, if_generation_not_match=None, if_metageneration_match=None, if_metageneration_not_match=None, timeout=60, retry=<google.api_core.retry.Retry object>)
Determines whether or not this blob exists.

If `user_project` is set on the bucket, bills the API request
to that project.


* **Parameters**

    
    * **client** ([`Client`](client.md#google.cloud.storage.client.Client)) – (Optional) The client to use.  If not passed, falls back to the
    `client` stored on the blob’s bucket.


    * **if_etag_match** (*Union**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*, **Set**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*]**]*) – (Optional) See [Using if_etag_match](generation_metageneration.md#using-if-etag-match)


    * **if_etag_not_match** (*Union**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*, **Set**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*]**]*) – (Optional) See [Using if_etag_not_match](generation_metageneration.md#using-if-etag-not-match)


    * **if_generation_match** (*long*) – (Optional) See [Using if_generation_match](generation_metageneration.md#using-if-generation-match)


    * **if_generation_not_match** (*long*) – (Optional) See [Using if_generation_not_match](generation_metageneration.md#using-if-generation-not-match)


    * **if_metageneration_match** (*long*) – (Optional) See [Using if_metageneration_match](generation_metageneration.md#using-if-metageneration-match)


    * **if_metageneration_not_match** (*long*) – (Optional) See [Using if_metageneration_not_match](generation_metageneration.md#using-if-metageneration-not-match)


    * **timeout** ([*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)* or *[*tuple*](https://python.readthedocs.io/en/latest/library/stdtypes.html#tuple)) – (Optional) The amount of time, in seconds, to wait
    for the server response.  See: [Configuring Timeouts](retry_timeout.md#configuring-timeouts)


    * **retry** ([*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)* or *[*google.cloud.storage.retry.ConditionalRetryPolicy*](retry.md#google.cloud.storage.retry.ConditionalRetryPolicy)) – (Optional) How to retry the RPC. See: [Configuring Retries](retry_timeout.md#configuring-retries)



* **Return type**

    [bool](https://python.readthedocs.io/en/latest/library/functions.html#bool)



* **Returns**

    True if the blob exists in Cloud Storage.



#### _classmethod_ from_string(uri, client=None)
Get a constructor for blob object by URI.

```python
from google.cloud import storage
from google.cloud.storage.blob import Blob
client = storage.Client()
blob = Blob.from_string("gs://bucket/object", client=client)
```


* **Parameters**

    
    * **uri** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – The blob uri pass to get blob object.


    * **client** ([`Client`](client.md#google.cloud.storage.client.Client)) – (Optional) The client to use.  Application code should
    *always* pass `client`.



* **Return type**

    `google.cloud.storage.blob.Blob`



* **Returns**

    The blob object created.



#### generate_signed_url(expiration=None, api_access_endpoint='https://storage.googleapis.com', method='GET', content_md5=None, content_type=None, response_disposition=None, response_type=None, generation=None, headers=None, query_parameters=None, client=None, credentials=None, version=None, service_account_email=None, access_token=None, virtual_hosted_style=False, bucket_bound_hostname=None, scheme='http')
Generates a signed URL for this blob.

**NOTE**: If you are on Google Compute Engine, you can’t generate a signed
URL using GCE service account.
If you’d like to be able to generate a signed URL from GCE,
you can use a standard service account from a JSON file rather
than a GCE service account.

If you have a blob that you want to allow access to for a set
amount of time, you can use this method to generate a URL that
is only valid within a certain time period.

See a [code sample]([https://cloud.google.com/storage/docs/samples/storage-generate-signed-url-v4#storage_generate_signed_url_v4-python](https://cloud.google.com/storage/docs/samples/storage-generate-signed-url-v4#storage_generate_signed_url_v4-python)).

This is particularly useful if you don’t want publicly
accessible blobs, but don’t want to require users to explicitly
log in.

If `bucket_bound_hostname` is set as an argument of `api_access_endpoint`,
`https` works only if using a `CDN`.


* **Parameters**

    
    * **expiration** (*Union**[**Integer**, *[*datetime.datetime*](https://python.readthedocs.io/en/latest/library/datetime.html#datetime.datetime)*, *[*datetime.timedelta*](https://python.readthedocs.io/en/latest/library/datetime.html#datetime.timedelta)*]*) – Point in time when the signed URL should expire. If a `datetime`
    instance is passed without an explicit `tzinfo` set,  it will be
    assumed to be `UTC`.


    * **api_access_endpoint** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) URI base.


    * **method** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – The HTTP verb that will be used when requesting the URL.


    * **content_md5** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) The MD5 hash of the object referenced by `resource`.


    * **content_type** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) The content type of the object referenced by
    `resource`.


    * **response_disposition** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) Content disposition of responses to requests for the
    signed URL.  For example, to enable the signed URL to initiate a
    file of `blog.png`, use the value `'attachment;
    filename=blob.png'`.


    * **response_type** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) Content type of responses to requests for the signed
    URL. Ignored if content_type is set on object/blob metadata.


    * **generation** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) A value that indicates which generation of the resource
    to fetch.


    * **headers** ([*dict*](https://python.readthedocs.io/en/latest/library/stdtypes.html#dict)) – (Optional) Additional HTTP headers to be included as part of the
    signed URLs. See:
    [https://cloud.google.com/storage/docs/xml-api/reference-headers](https://cloud.google.com/storage/docs/xml-api/reference-headers)
    Requests using the signed URL *must* pass the specified header
    (name and value) with each request for the URL.


    * **query_parameters** ([*dict*](https://python.readthedocs.io/en/latest/library/stdtypes.html#dict)) – (Optional) Additional query parameters to be included as part of the
    signed URLs. See:
    [https://cloud.google.com/storage/docs/xml-api/reference-headers#query](https://cloud.google.com/storage/docs/xml-api/reference-headers#query)


    * **client** ([`Client`](client.md#google.cloud.storage.client.Client)) – (Optional) The client to use.  If not passed, falls back to the
    `client` stored on the blob’s bucket.


    * **credentials** ([`google.auth.credentials.Credentials`](https://googleapis.dev/python/google-auth/latest/reference/google.auth.credentials.html#google.auth.credentials.Credentials)) – (Optional) The authorization credentials to attach to requests.
    These credentials identify this application to the service.  If
    none are specified, the client will attempt to ascertain the
    credentials from the environment.


    * **version** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) The version of signed credential to create.  Must be one
    of ‘v2’ | ‘v4’.


    * **service_account_email** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) E-mail address of the service account.


    * **access_token** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) Access token for a service account.


    * **virtual_hosted_style** ([*bool*](https://python.readthedocs.io/en/latest/library/functions.html#bool)) – (Optional) If true, then construct the URL relative the bucket’s
    virtual hostname, e.g., ‘<bucket-name>.storage.googleapis.com’.


    * **bucket_bound_hostname** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) If passed, then construct the URL relative to the
    bucket-bound hostname.  Value can be a bare or with scheme, e.g.,
    ‘example.com’ or ‘[http://example.com](http://example.com)’.  See:
    [https://cloud.google.com/storage/docs/request-endpoints#cname](https://cloud.google.com/storage/docs/request-endpoints#cname)


    * **scheme** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) If `bucket_bound_hostname` is passed as a bare
    hostname, use this value as the scheme.  `https` will work only
    when using a CDN.  Defaults to `"http"`.



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



#### _property_ generation()
Retrieve the generation for the object.

See [https://cloud.google.com/storage/docs/json_api/v1/objects](https://cloud.google.com/storage/docs/json_api/v1/objects)


* **Return type**

    int or `NoneType`



* **Returns**

    The generation of the blob or `None` if the blob’s
    resource has not been loaded from the server.



#### get_iam_policy(client=None, requested_policy_version=None, timeout=60, retry=<google.api_core.retry.Retry object>)
Retrieve the IAM policy for the object.

**NOTE**: Blob- / object-level IAM support does not yet exist and methods
currently call an internal ACL backend not providing any utility
beyond the blob’s `acl` at this time. The API may be enhanced
in the future and is currently undocumented. Use `acl` for
managing object access control.

If `user_project` is set on the bucket, bills the API request
to that project.


* **Parameters**

    
    * **client** ([`Client`](client.md#google.cloud.storage.client.Client)) – (Optional) The client to use.  If not passed, falls back to the
    `client` stored on the current object’s bucket.


    * **requested_policy_version** (int or `NoneType`) – (Optional) The version of IAM policies to request.  If a policy
    with a condition is requested without setting this, the server will
    return an error.  This must be set to a value of 3 to retrieve IAM
    policies containing conditions. This is to prevent client code that
    isn’t aware of IAM conditions from interpreting and modifying
    policies incorrectly.  The service might return a policy with
    version lower than the one that was requested, based on the feature
    syntax in the policy fetched.


    * **timeout** ([*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)* or *[*tuple*](https://python.readthedocs.io/en/latest/library/stdtypes.html#tuple)) – (Optional) The amount of time, in seconds, to wait
    for the server response.  See: [Configuring Timeouts](retry_timeout.md#configuring-timeouts)


    * **retry** ([*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)* or *[*google.cloud.storage.retry.ConditionalRetryPolicy*](retry.md#google.cloud.storage.retry.ConditionalRetryPolicy)) – (Optional) How to retry the RPC. See: [Configuring Retries](retry_timeout.md#configuring-retries)



* **Return type**

    [`google.api_core.iam.Policy`](https://googleapis.dev/python/google-api-core/latest/iam.html#google.api_core.iam.Policy)



* **Returns**

    the policy instance, based on the resource returned from
    the `getIamPolicy` API request.



#### _property_ id()
Retrieve the ID for the object.

See [https://cloud.google.com/storage/docs/json_api/v1/objects](https://cloud.google.com/storage/docs/json_api/v1/objects)

The ID consists of the bucket name, object name, and generation number.


* **Return type**

    str or `NoneType`



* **Returns**

    The ID of the blob or `None` if the blob’s
    resource has not been loaded from the server.



#### _property_ kms_key_name()
Resource name of Cloud KMS key used to encrypt the blob’s contents.


* **Return type**

    str or `NoneType`



* **Returns**

    The resource name or `None` if no Cloud KMS key was used,
    or the blob’s resource has not been loaded from the server.



#### make_private(client=None, timeout=60, if_generation_match=None, if_generation_not_match=None, if_metageneration_match=None, if_metageneration_not_match=None, retry=<google.cloud.storage.retry.ConditionalRetryPolicy object>)
Update blob’s ACL, revoking read access for anonymous users.


* **Parameters**

    
    * **client** ([`Client`](client.md#google.cloud.storage.client.Client) or
    `NoneType`) – (Optional) The client to use.  If not passed, falls back
    to the `client` stored on the blob’s bucket.


    * **timeout** ([*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)* or *[*tuple*](https://python.readthedocs.io/en/latest/library/stdtypes.html#tuple)) – (Optional) The amount of time, in seconds, to wait
    for the server response.  See: [Configuring Timeouts](retry_timeout.md#configuring-timeouts)


    * **if_generation_match** (*long*) – (Optional) See [Using if_generation_match](generation_metageneration.md#using-if-generation-match)


    * **if_generation_not_match** (*long*) – (Optional) See [Using if_generation_not_match](generation_metageneration.md#using-if-generation-not-match)


    * **if_metageneration_match** (*long*) – (Optional) See [Using if_metageneration_match](generation_metageneration.md#using-if-metageneration-match)


    * **if_metageneration_not_match** (*long*) – (Optional) See [Using if_metageneration_not_match](generation_metageneration.md#using-if-metageneration-not-match)


    * **retry** ([*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)* or *[*google.cloud.storage.retry.ConditionalRetryPolicy*](retry.md#google.cloud.storage.retry.ConditionalRetryPolicy)) – (Optional) How to retry the RPC. See: [Configuring Retries](retry_timeout.md#configuring-retries)



#### make_public(client=None, timeout=60, if_generation_match=None, if_generation_not_match=None, if_metageneration_match=None, if_metageneration_not_match=None, retry=<google.cloud.storage.retry.ConditionalRetryPolicy object>)
Update blob’s ACL, granting read access to anonymous users.


* **Parameters**

    
    * **client** ([`Client`](client.md#google.cloud.storage.client.Client) or
    `NoneType`) – (Optional) The client to use.  If not passed, falls back
    to the `client` stored on the blob’s bucket.


    * **timeout** ([*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)* or *[*tuple*](https://python.readthedocs.io/en/latest/library/stdtypes.html#tuple)) – (Optional) The amount of time, in seconds, to wait
    for the server response.  See: [Configuring Timeouts](retry_timeout.md#configuring-timeouts)


    * **if_generation_match** (*long*) – (Optional) See [Using if_generation_match](generation_metageneration.md#using-if-generation-match)


    * **if_generation_not_match** (*long*) – (Optional) See [Using if_generation_not_match](generation_metageneration.md#using-if-generation-not-match)


    * **if_metageneration_match** (*long*) – (Optional) See [Using if_metageneration_match](generation_metageneration.md#using-if-metageneration-match)


    * **if_metageneration_not_match** (*long*) – (Optional) See [Using if_metageneration_not_match](generation_metageneration.md#using-if-metageneration-not-match)


    * **retry** ([*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)* or *[*google.cloud.storage.retry.ConditionalRetryPolicy*](retry.md#google.cloud.storage.retry.ConditionalRetryPolicy)) – (Optional) How to retry the RPC. See: [Configuring Retries](retry_timeout.md#configuring-retries)



#### _property_ md5_hash()
MD5 hash for this object.

This returns the blob’s MD5 hash. To retrieve the value, first use a
reload method of the Blob class which loads the blob’s properties from the server.

See [RFC 1321]([https://tools.ietf.org/html/rfc1321](https://tools.ietf.org/html/rfc1321)) and
[API reference docs]([https://cloud.google.com/storage/docs/json_api/v1/objects](https://cloud.google.com/storage/docs/json_api/v1/objects)).

If not set before upload, the server will compute the hash.


* **Return type**

    str or `NoneType`



#### _property_ media_link()
Retrieve the media download URI for the object.

See [https://cloud.google.com/storage/docs/json_api/v1/objects](https://cloud.google.com/storage/docs/json_api/v1/objects)


* **Return type**

    str or `NoneType`



* **Returns**

    The media link for the blob or `None` if the blob’s
    resource has not been loaded from the server.



#### _property_ metadata()
Retrieve arbitrary/application specific metadata for the object.

See [https://cloud.google.com/storage/docs/json_api/v1/objects](https://cloud.google.com/storage/docs/json_api/v1/objects)


* **Setter**

    Update arbitrary/application specific metadata for the
    object.



* **Getter**

    Retrieve arbitrary/application specific metadata for
    the object.



* **Return type**

    dict or `NoneType`



* **Returns**

    The metadata associated with the blob or `None` if the
    property is not set.



#### _property_ metageneration()
Retrieve the metageneration for the object.

See [https://cloud.google.com/storage/docs/json_api/v1/objects](https://cloud.google.com/storage/docs/json_api/v1/objects)


* **Return type**

    int or `NoneType`



* **Returns**

    The metageneration of the blob or `None` if the blob’s
    resource has not been loaded from the server.



#### open(mode='r', chunk_size=None, ignore_flush=None, encoding=None, errors=None, newline=None, \*\*kwargs)
Create a file handler for file-like I/O to or from this blob.

This method can be used as a context manager, just like Python’s
built-in ‘open()’ function.

While reading, as with other read methods, if blob.generation is not set
the most recent blob generation will be used. Because the file-like IO
reader downloads progressively in chunks, this could result in data from
multiple versions being mixed together. If this is a concern, use
either bucket.get_blob(), or blob.reload(), which will download the
latest generation number and set it; or, if the generation is known, set
it manually, for instance with bucket.blob(generation=123456).

Checksumming (hashing) to verify data integrity is disabled for reads
using this feature because reads are implemented using request ranges,
which do not provide checksums to validate. See
[https://cloud.google.com/storage/docs/hashes-etags](https://cloud.google.com/storage/docs/hashes-etags) for details.

See a [code sample]([https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_fileio_write_read.py](https://github.com/googleapis/python-storage/blob/main/samples/snippets/storage_fileio_write_read.py)).

Keyword arguments to pass to the underlying API calls.
For both uploads and downloads, the following arguments are
supported:


* `if_generation_match`


* `if_generation_not_match`


* `if_metageneration_match`


* `if_metageneration_not_match`


* `timeout`


* `retry`

For downloads only, the following additional arguments are supported:


* `raw_download`

For uploads only, the following additional arguments are supported:


* `content_type`


* `num_retries`


* `predefined_acl`


* `checksum`

**NOTE**: `num_retries` is supported for backwards-compatibility
reasons only; please use `retry` with a Retry object or
ConditionalRetryPolicy instead.


* **Parameters**

    
    * **mode** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) A mode string, as per standard Python open() semantics.The first
    character must be ‘r’, to open the blob for reading, or ‘w’ to open
    it for writing. The second character, if present, must be ‘t’ for
    (unicode) text mode, or ‘b’ for bytes mode. If the second character
    is omitted, text mode is the default.


    * **chunk_size** (*long*) – (Optional) For reads, the minimum number of bytes to read at a time.
    If fewer bytes than the chunk_size are requested, the remainder is
    buffered. For writes, the maximum number of bytes to buffer before
    sending data to the server, and the size of each request when data
    is sent. Writes are implemented as a “resumable upload”, so
    chunk_size for writes must be exactly a multiple of 256KiB as with
    other resumable uploads. The default is 40 MiB.


    * **ignore_flush** ([*bool*](https://python.readthedocs.io/en/latest/library/functions.html#bool)) – (Optional) For non text-mode writes, makes flush() do nothing
    instead of raising an error. flush() without closing is not
    supported by the remote service and therefore calling it normally
    results in io.UnsupportedOperation. However, that behavior is
    incompatible with some consumers and wrappers of file objects in
    Python, such as zipfile.ZipFile or io.TextIOWrapper. Setting
    ignore_flush will cause flush() to successfully do nothing, for
    compatibility with those contexts. The correct way to actually flush
    data to the remote server is to close() (using a context manager,
    such as in the example, will cause this to happen automatically).


    * **encoding** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) For text mode only, the name of the encoding that the stream will
    be decoded or encoded with. If omitted, it defaults to
    locale.getpreferredencoding(False).


    * **errors** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) For text mode only, an optional string that specifies how encoding
    and decoding errors are to be handled. Pass ‘strict’ to raise a
    ValueError exception if there is an encoding error (the default of
    None has the same effect), or pass ‘ignore’ to ignore errors. (Note
    that ignoring encoding errors can lead to data loss.) Other more
    rarely-used options are also available; see the Python ‘io’ module
    documentation for ‘io.TextIOWrapper’ for a complete list.


    * **newline** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) For text mode only, controls how line endings are handled. It can
    be None, ‘’, ‘n’, ‘r’, and ‘rn’. If None, reads use “universal
    newline mode” and writes use the system default. See the Python
    ‘io’ module documentation for ‘io.TextIOWrapper’ for details.



* **Returns**

    A ‘BlobReader’ or ‘BlobWriter’ from
    ‘google.cloud.storage.fileio’, or an ‘io.TextIOWrapper’ around one
    of those classes, depending on the ‘mode’ argument.



#### _property_ owner()
Retrieve info about the owner of the object.

See [https://cloud.google.com/storage/docs/json_api/v1/objects](https://cloud.google.com/storage/docs/json_api/v1/objects)


* **Return type**

    dict or `NoneType`



* **Returns**

    Mapping of owner’s role/ID, or `None` if the blob’s
    resource has not been loaded from the server.



#### patch(client=None, if_generation_match=None, if_generation_not_match=None, if_metageneration_match=None, if_metageneration_not_match=None, timeout=60, retry=<google.cloud.storage.retry.ConditionalRetryPolicy object>)
Sends all changed properties in a PATCH request.

Updates the `_properties` with the response from the backend.

If `user_project` is set, bills the API request to that project.


* **Parameters**

    
    * **client** ([`Client`](client.md#google.cloud.storage.client.Client) or
    `NoneType`) – the client to use. If not passed, falls back to the
    `client` stored on the current object.


    * **if_generation_match** (*long*) – (Optional) See [Using if_generation_match](generation_metageneration.md#using-if-generation-match)


    * **if_generation_not_match** (*long*) – (Optional) See [Using if_generation_not_match](generation_metageneration.md#using-if-generation-not-match)


    * **if_metageneration_match** (*long*) – (Optional) See [Using if_metageneration_match](generation_metageneration.md#using-if-metageneration-match)


    * **if_metageneration_not_match** (*long*) – (Optional) See [Using if_metageneration_not_match](generation_metageneration.md#using-if-metageneration-not-match)


    * **timeout** ([*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)* or *[*tuple*](https://python.readthedocs.io/en/latest/library/stdtypes.html#tuple)) – (Optional) The amount of time, in seconds, to wait
    for the server response.  See: [Configuring Timeouts](retry_timeout.md#configuring-timeouts)


    * **retry** ([*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)* or *[*google.cloud.storage.retry.ConditionalRetryPolicy*](retry.md#google.cloud.storage.retry.ConditionalRetryPolicy)) – (Optional) How to retry the RPC. See: [Configuring Retries](retry_timeout.md#configuring-retries)



#### _property_ path()
Getter property for the URL path to this Blob.


* **Return type**

    [str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)



* **Returns**

    The URL path to this Blob.



#### _static_ path_helper(bucket_path, blob_name)
Relative URL path for a blob.


* **Parameters**

    
    * **bucket_path** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – The URL path for a bucket.


    * **blob_name** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – The name of the blob.



* **Return type**

    [str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)



* **Returns**

    The relative URL path for `blob_name`.



#### _property_ public_url()
The public URL for this blob.

Use `make_public()` to enable anonymous access via the returned
URL.


* **Return type**

    string



* **Returns**

    The public URL for this blob.



#### reload(client=None, projection='noAcl', if_etag_match=None, if_etag_not_match=None, if_generation_match=None, if_generation_not_match=None, if_metageneration_match=None, if_metageneration_not_match=None, timeout=60, retry=<google.api_core.retry.Retry object>)
Reload properties from Cloud Storage.

If `user_project` is set, bills the API request to that project.


* **Parameters**

    
    * **client** ([`Client`](client.md#google.cloud.storage.client.Client) or
    `NoneType`) – the client to use. If not passed, falls back to the
    `client` stored on the current object.


    * **projection** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) If used, must be ‘full’ or ‘noAcl’.
    Defaults to `'noAcl'`. Specifies the set of
    properties to return.


    * **if_etag_match** (*Union**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*, **Set**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*]**]*) – (Optional) See [Using if_etag_match](generation_metageneration.md#using-if-etag-match)


    * **if_etag_not_match** (*Union**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*, **Set**[*[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)*]**]**)*) – (Optional) See [Using if_etag_not_match](generation_metageneration.md#using-if-etag-not-match)


    * **if_generation_match** (*long*) – (Optional) See [Using if_generation_match](generation_metageneration.md#using-if-generation-match)


    * **if_generation_not_match** (*long*) – (Optional) See [Using if_generation_not_match](generation_metageneration.md#using-if-generation-not-match)


    * **if_metageneration_match** (*long*) – (Optional) See [Using if_metageneration_match](generation_metageneration.md#using-if-metageneration-match)


    * **if_metageneration_not_match** (*long*) – (Optional) See [Using if_metageneration_not_match](generation_metageneration.md#using-if-metageneration-not-match)


    * **timeout** ([*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)* or *[*tuple*](https://python.readthedocs.io/en/latest/library/stdtypes.html#tuple)) – (Optional) The amount of time, in seconds, to wait
    for the server response.  See: [Configuring Timeouts](retry_timeout.md#configuring-timeouts)


    * **retry** ([*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)* or *[*google.cloud.storage.retry.ConditionalRetryPolicy*](retry.md#google.cloud.storage.retry.ConditionalRetryPolicy)) – (Optional) How to retry the RPC. See: [Configuring Retries](retry_timeout.md#configuring-retries)



#### _property_ retention_expiration_time()
Retrieve timestamp at which the object’s retention period expires.

See [https://cloud.google.com/storage/docs/json_api/v1/objects](https://cloud.google.com/storage/docs/json_api/v1/objects)


* **Return type**

    [`datetime.datetime`](https://python.readthedocs.io/en/latest/library/datetime.html#datetime.datetime) or `NoneType`



* **Returns**

    Datetime object parsed from RFC3339 valid timestamp, or
    `None` if the property is not set locally.



#### rewrite(source, token=None, client=None, if_generation_match=None, if_generation_not_match=None, if_metageneration_match=None, if_metageneration_not_match=None, if_source_generation_match=None, if_source_generation_not_match=None, if_source_metageneration_match=None, if_source_metageneration_not_match=None, timeout=60, retry=<google.cloud.storage.retry.ConditionalRetryPolicy object>)
Rewrite source blob into this one.

If `user_project` is set on the bucket, bills the API request
to that project.


* **Parameters**

    
    * **source** (`Blob`) – blob whose contents will be rewritten into this blob.


    * **token** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) Token returned from an earlier, not-completed call to
    rewrite the same source blob.  If passed, result will include
    updated status, total bytes written.


    * **client** ([`Client`](client.md#google.cloud.storage.client.Client)) – (Optional) The client to use.  If not passed, falls back to the
    `client` stored on the blob’s bucket.


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

    [tuple](https://python.readthedocs.io/en/latest/library/stdtypes.html#tuple)



* **Returns**

    `(token, bytes_rewritten, total_bytes)`, where `token`
    is a rewrite token (`None` if the rewrite is complete),
    `bytes_rewritten` is the number of bytes rewritten so far,
    and `total_bytes` is the total number of bytes to be
    rewritten.



#### _property_ self_link()
Retrieve the URI for the object.

See [https://cloud.google.com/storage/docs/json_api/v1/objects](https://cloud.google.com/storage/docs/json_api/v1/objects)


* **Return type**

    str or `NoneType`



* **Returns**

    The self link for the blob or `None` if the blob’s
    resource has not been loaded from the server.



#### set_iam_policy(policy, client=None, timeout=60, retry=<google.cloud.storage.retry.ConditionalRetryPolicy object>)
Update the IAM policy for the bucket.

**NOTE**: Blob- / object-level IAM support does not yet exist and methods
currently call an internal ACL backend not providing any utility
beyond the blob’s `acl` at this time. The API may be enhanced
in the future and is currently undocumented. Use `acl` for
managing object access control.

If `user_project` is set on the bucket, bills the API request
to that project.


* **Parameters**

    
    * **policy** ([`google.api_core.iam.Policy`](https://googleapis.dev/python/google-api-core/latest/iam.html#google.api_core.iam.Policy)) – policy instance used to update bucket’s IAM policy.


    * **client** ([`Client`](client.md#google.cloud.storage.client.Client)) – (Optional) The client to use.  If not passed, falls back to the
    `client` stored on the current bucket.


    * **timeout** ([*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)* or *[*tuple*](https://python.readthedocs.io/en/latest/library/stdtypes.html#tuple)) – (Optional) The amount of time, in seconds, to wait
    for the server response.  See: [Configuring Timeouts](retry_timeout.md#configuring-timeouts)


    * **retry** ([*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)* or *[*google.cloud.storage.retry.ConditionalRetryPolicy*](retry.md#google.cloud.storage.retry.ConditionalRetryPolicy)) – (Optional) How to retry the RPC. See: [Configuring Retries](retry_timeout.md#configuring-retries)



* **Return type**

    [`google.api_core.iam.Policy`](https://googleapis.dev/python/google-api-core/latest/iam.html#google.api_core.iam.Policy)



* **Returns**

    the policy instance, based on the resource returned from
    the `setIamPolicy` API request.



#### _property_ size()
Size of the object, in bytes.

See [https://cloud.google.com/storage/docs/json_api/v1/objects](https://cloud.google.com/storage/docs/json_api/v1/objects)


* **Return type**

    int or `NoneType`



* **Returns**

    The size of the blob or `None` if the blob’s
    resource has not been loaded from the server.



#### _property_ storage_class()
Retrieve the storage class for the object.

This can only be set at blob / object **creation** time. If you’d
like to change the storage class **after** the blob / object already
exists in a bucket, call `update_storage_class()` (which uses
`rewrite()`).

See [https://cloud.google.com/storage/docs/storage-classes](https://cloud.google.com/storage/docs/storage-classes)


* **Return type**

    str or `NoneType`



* **Returns**

    If set, one of
    [`STANDARD_STORAGE_CLASS`](constants.md#google.cloud.storage.constants.STANDARD_STORAGE_CLASS),
    [`NEARLINE_STORAGE_CLASS`](constants.md#google.cloud.storage.constants.NEARLINE_STORAGE_CLASS),
    [`COLDLINE_STORAGE_CLASS`](constants.md#google.cloud.storage.constants.COLDLINE_STORAGE_CLASS),
    [`ARCHIVE_STORAGE_CLASS`](constants.md#google.cloud.storage.constants.ARCHIVE_STORAGE_CLASS),
    [`MULTI_REGIONAL_LEGACY_STORAGE_CLASS`](constants.md#google.cloud.storage.constants.MULTI_REGIONAL_LEGACY_STORAGE_CLASS),
    [`REGIONAL_LEGACY_STORAGE_CLASS`](constants.md#google.cloud.storage.constants.REGIONAL_LEGACY_STORAGE_CLASS),
    `DURABLE_REDUCED_AVAILABILITY_STORAGE_CLASS`,
    else `None`.



#### _property_ temporary_hold()
Is a temporary hold active on the object?

See [API reference docs]([https://cloud.google.com/storage/docs/json_api/v1/objects](https://cloud.google.com/storage/docs/json_api/v1/objects)).

If the property is not set locally, returns [`None`](https://python.readthedocs.io/en/latest/library/constants.html#None).


* **Return type**

    bool or `NoneType`



#### test_iam_permissions(permissions, client=None, timeout=60, retry=<google.api_core.retry.Retry object>)
API call:  test permissions

**NOTE**: Blob- / object-level IAM support does not yet exist and methods
currently call an internal ACL backend not providing any utility
beyond the blob’s `acl` at this time. The API may be enhanced
in the future and is currently undocumented. Use `acl` for
managing object access control.

If `user_project` is set on the bucket, bills the API request
to that project.


* **Parameters**

    
    * **permissions** (*list of string*) – the permissions to check


    * **client** ([`Client`](client.md#google.cloud.storage.client.Client)) – (Optional) The client to use.  If not passed, falls back to the
    `client` stored on the current bucket.


    * **timeout** ([*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)* or *[*tuple*](https://python.readthedocs.io/en/latest/library/stdtypes.html#tuple)) – (Optional) The amount of time, in seconds, to wait
    for the server response.  See: [Configuring Timeouts](retry_timeout.md#configuring-timeouts)


    * **retry** ([*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)* or *[*google.cloud.storage.retry.ConditionalRetryPolicy*](retry.md#google.cloud.storage.retry.ConditionalRetryPolicy)) – (Optional) How to retry the RPC. See: [Configuring Retries](retry_timeout.md#configuring-retries)



* **Return type**

    list of string



* **Returns**

    the permissions returned by the `testIamPermissions` API
    request.



#### _property_ time_created()
Retrieve the timestamp at which the object was created.

See [https://cloud.google.com/storage/docs/json_api/v1/objects](https://cloud.google.com/storage/docs/json_api/v1/objects)


* **Return type**

    [`datetime.datetime`](https://python.readthedocs.io/en/latest/library/datetime.html#datetime.datetime) or `NoneType`



* **Returns**

    Datetime object parsed from RFC3339 valid timestamp, or
    `None` if the blob’s resource has not been loaded from
    the server (see `reload()`).



#### _property_ time_deleted()
Retrieve the timestamp at which the object was deleted.

See [https://cloud.google.com/storage/docs/json_api/v1/objects](https://cloud.google.com/storage/docs/json_api/v1/objects)


* **Return type**

    [`datetime.datetime`](https://python.readthedocs.io/en/latest/library/datetime.html#datetime.datetime) or `NoneType`



* **Returns**

    Datetime object parsed from RFC3339 valid timestamp, or
    `None` if the blob’s resource has not been loaded from
    the server (see `reload()`). If the blob has
    not been deleted, this will never be set.



#### update(client=None, if_generation_match=None, if_generation_not_match=None, if_metageneration_match=None, if_metageneration_not_match=None, timeout=60, retry=<google.cloud.storage.retry.ConditionalRetryPolicy object>)
Sends all properties in a PUT request.

Updates the `_properties` with the response from the backend.

If `user_project` is set, bills the API request to that project.


* **Parameters**

    
    * **client** ([`Client`](client.md#google.cloud.storage.client.Client) or
    `NoneType`) – the client to use. If not passed, falls back to the
    `client` stored on the current object.


    * **if_generation_match** (*long*) – (Optional) See [Using if_generation_match](generation_metageneration.md#using-if-generation-match)


    * **if_generation_not_match** (*long*) – (Optional) See [Using if_generation_not_match](generation_metageneration.md#using-if-generation-not-match)


    * **if_metageneration_match** (*long*) – (Optional) See [Using if_metageneration_match](generation_metageneration.md#using-if-metageneration-match)


    * **if_metageneration_not_match** (*long*) – (Optional) See [Using if_metageneration_not_match](generation_metageneration.md#using-if-metageneration-not-match)


    * **timeout** ([*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)* or *[*tuple*](https://python.readthedocs.io/en/latest/library/stdtypes.html#tuple)) – (Optional) The amount of time, in seconds, to wait
    for the server response.  See: [Configuring Timeouts](retry_timeout.md#configuring-timeouts)


    * **retry** ([*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)* or *[*google.cloud.storage.retry.ConditionalRetryPolicy*](retry.md#google.cloud.storage.retry.ConditionalRetryPolicy)) – (Optional) How to retry the RPC. See: [Configuring Retries](retry_timeout.md#configuring-retries)



#### update_storage_class(new_class, client=None, if_generation_match=None, if_generation_not_match=None, if_metageneration_match=None, if_metageneration_not_match=None, if_source_generation_match=None, if_source_generation_not_match=None, if_source_metageneration_match=None, if_source_metageneration_not_match=None, timeout=60, retry=<google.cloud.storage.retry.ConditionalRetryPolicy object>)
Update blob’s storage class via a rewrite-in-place. This helper will
wait for the rewrite to complete before returning, so it may take some
time for large files.

See
[https://cloud.google.com/storage/docs/per-object-storage-class](https://cloud.google.com/storage/docs/per-object-storage-class)

If `user_project` is set on the bucket, bills the API request
to that project.


* **Parameters**

    
    * **new_class** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – new storage class for the object.   One of:
    [`NEARLINE_STORAGE_CLASS`](constants.md#google.cloud.storage.constants.NEARLINE_STORAGE_CLASS),
    [`COLDLINE_STORAGE_CLASS`](constants.md#google.cloud.storage.constants.COLDLINE_STORAGE_CLASS),
    [`ARCHIVE_STORAGE_CLASS`](constants.md#google.cloud.storage.constants.ARCHIVE_STORAGE_CLASS),
    [`STANDARD_STORAGE_CLASS`](constants.md#google.cloud.storage.constants.STANDARD_STORAGE_CLASS),
    [`MULTI_REGIONAL_LEGACY_STORAGE_CLASS`](constants.md#google.cloud.storage.constants.MULTI_REGIONAL_LEGACY_STORAGE_CLASS),
    or
    [`REGIONAL_LEGACY_STORAGE_CLASS`](constants.md#google.cloud.storage.constants.REGIONAL_LEGACY_STORAGE_CLASS).


    * **client** ([`Client`](client.md#google.cloud.storage.client.Client)) – (Optional) The client to use.  If not passed, falls back to the
    `client` stored on the blob’s bucket.


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



#### _property_ updated()
Retrieve the timestamp at which the object was updated.

See [https://cloud.google.com/storage/docs/json_api/v1/objects](https://cloud.google.com/storage/docs/json_api/v1/objects)


* **Return type**

    [`datetime.datetime`](https://python.readthedocs.io/en/latest/library/datetime.html#datetime.datetime) or `NoneType`



* **Returns**

    Datetime object parsed from RFC3339 valid timestamp, or
    `None` if the blob’s resource has not been loaded from
    the server (see `reload()`).



#### upload_from_file(file_obj, rewind=False, size=None, content_type=None, num_retries=None, client=None, predefined_acl=None, if_generation_match=None, if_generation_not_match=None, if_metageneration_match=None, if_metageneration_not_match=None, timeout=60, checksum=None, retry=<google.cloud.storage.retry.ConditionalRetryPolicy object>)
Upload the contents of this blob from a file-like object.

The content type of the upload will be determined in order
of precedence:


* The value passed in to this method (if not [`None`](https://python.readthedocs.io/en/latest/library/constants.html#None))


* The value stored on the current blob


* The default value (‘application/octet-stream’)

**NOTE**: The effect of uploading to an existing blob depends on the
“versioning” and “lifecycle” policies defined on the blob’s
bucket.  In the absence of those policies, upload will
overwrite any existing contents.

See the [object versioning]([https://cloud.google.com/storage/docs/object-versioning](https://cloud.google.com/storage/docs/object-versioning))
and [lifecycle]([https://cloud.google.com/storage/docs/lifecycle](https://cloud.google.com/storage/docs/lifecycle))
API documents for details.

If the size of the data to be uploaded exceeds 8 MB a resumable media
request will be used, otherwise the content and the metadata will be
uploaded in a single multipart upload request.

For more fine-grained over the upload process, check out
[google-resumable-media]([https://googleapis.dev/python/google-resumable-media/latest/index.html](https://googleapis.dev/python/google-resumable-media/latest/index.html)).

If `user_project` is set on the bucket, bills the API request
to that project.


* **Parameters**

    
    * **file_obj** (*file*) – A file handle opened in binary mode for reading.


    * **rewind** ([*bool*](https://python.readthedocs.io/en/latest/library/functions.html#bool)) – If True, seek to the beginning of the file handle before writing
    the file to Cloud Storage.


    * **size** ([*int*](https://python.readthedocs.io/en/latest/library/functions.html#int)) – The number of bytes to be uploaded (which will be read from
    `file_obj`). If not provided, the upload will be concluded once
    `file_obj` is exhausted.


    * **content_type** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) Type of content being uploaded.


    * **num_retries** ([*int*](https://python.readthedocs.io/en/latest/library/functions.html#int)) – Number of upload retries. By default, only uploads with
    if_generation_match set will be retried, as uploads without the
    argument are not guaranteed to be idempotent. Setting num_retries
    will override this default behavior and guarantee retries even when
    if_generation_match is not set.  (Deprecated: This argument
    will be removed in a future release.)


    * **client** ([`Client`](client.md#google.cloud.storage.client.Client)) – (Optional) The client to use.  If not passed, falls back to the
    `client` stored on the blob’s bucket.


    * **predefined_acl** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) Predefined access control list


    * **if_generation_match** (*long*) – (Optional) See [Using if_generation_match](generation_metageneration.md#using-if-generation-match)


    * **if_generation_not_match** (*long*) – (Optional) See [Using if_generation_not_match](generation_metageneration.md#using-if-generation-not-match)


    * **if_metageneration_match** (*long*) – (Optional) See [Using if_metageneration_match](generation_metageneration.md#using-if-metageneration-match)


    * **if_metageneration_not_match** (*long*) – (Optional) See [Using if_metageneration_not_match](generation_metageneration.md#using-if-metageneration-not-match)


    * **timeout** ([*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)* or *[*tuple*](https://python.readthedocs.io/en/latest/library/stdtypes.html#tuple)) – (Optional) The amount of time, in seconds, to wait
    for the server response.  See: [Configuring Timeouts](retry_timeout.md#configuring-timeouts)


    * **checksum** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) The type of checksum to compute to verify
    the integrity of the object. If the upload is completed in a single
    request, the checksum will be entirely precomputed and the remote
    server will handle verification and error handling. If the upload
    is too large and must be transmitted in multiple requests, the
    checksum will be incrementally computed and the client will handle
    verification and error handling, raising
    google.resumable_media.common.DataCorruption on a mismatch and
    attempting to delete the corrupted file. Supported values are
    “md5”, “crc32c” and None. The default is None.


    * **retry** ([*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)* or *[*google.cloud.storage.retry.ConditionalRetryPolicy*](retry.md#google.cloud.storage.retry.ConditionalRetryPolicy)) – (Optional) How to retry the RPC. A None value will disable
    retries. A google.api_core.retry.Retry value will enable retries,
    and the object will define retriable response codes and errors and
    configure backoff and timeout options.

    A google.cloud.storage.retry.ConditionalRetryPolicy value wraps a
    Retry object and activates it only if certain conditions are met.
    This class exists to provide safe defaults for RPC calls that are
    not technically safe to retry normally (due to potential data
    duplication or other side-effects) but become safe to retry if a
    condition such as if_generation_match is set.

    See the retry.py source code and docstrings in this package
    (google.cloud.storage.retry) for information on retry types and how
    to configure them.

    Media operations (downloads and uploads) do not support non-default
    predicates in a Retry object. The default will always be used. Other
    configuration changes for Retry objects such as delays and deadlines
    are respected.




* **Raises**

    `GoogleCloudError`
    if the upload response returns an error status.



#### upload_from_filename(filename, content_type=None, num_retries=None, client=None, predefined_acl=None, if_generation_match=None, if_generation_not_match=None, if_metageneration_match=None, if_metageneration_not_match=None, timeout=60, checksum=None, retry=<google.cloud.storage.retry.ConditionalRetryPolicy object>)
Upload this blob’s contents from the content of a named file.

The content type of the upload will be determined in order
of precedence:


* The value passed in to this method (if not [`None`](https://python.readthedocs.io/en/latest/library/constants.html#None))


* The value stored on the current blob


* The value given by `mimetypes.guess_type`


* The default value (‘application/octet-stream’)

**NOTE**: The effect of uploading to an existing blob depends on the
“versioning” and “lifecycle” policies defined on the blob’s
bucket.  In the absence of those policies, upload will
overwrite any existing contents.

See the [object versioning]([https://cloud.google.com/storage/docs/object-versioning](https://cloud.google.com/storage/docs/object-versioning))
and [lifecycle]([https://cloud.google.com/storage/docs/lifecycle](https://cloud.google.com/storage/docs/lifecycle))
API documents for details.

If `user_project` is set on the bucket, bills the API request
to that project.

See a [code sample]([https://cloud.google.com/storage/docs/samples/storage-upload-encrypted-file#storage_upload_encrypted_file-python](https://cloud.google.com/storage/docs/samples/storage-upload-encrypted-file#storage_upload_encrypted_file-python))
to upload a file with a
[customer-supplied encryption key]([https://cloud.google.com/storage/docs/encryption#customer-supplied](https://cloud.google.com/storage/docs/encryption#customer-supplied)).


* **Parameters**

    
    * **filename** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – The path to the file.


    * **content_type** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) Type of content being uploaded.


    * **client** ([`Client`](client.md#google.cloud.storage.client.Client)) – (Optional) The client to use.  If not passed, falls back to the
    `client` stored on the blob’s bucket.


    * **num_retries** ([*int*](https://python.readthedocs.io/en/latest/library/functions.html#int)) – Number of upload retries. By default, only uploads with
    if_generation_match set will be retried, as uploads without the
    argument are not guaranteed to be idempotent. Setting num_retries
    will override this default behavior and guarantee retries even when
    if_generation_match is not set.  (Deprecated: This argument
    will be removed in a future release.)


    * **predefined_acl** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) Predefined access control list


    * **if_generation_match** (*long*) – (Optional) See [Using if_generation_match](generation_metageneration.md#using-if-generation-match)


    * **if_generation_not_match** (*long*) – (Optional) See [Using if_generation_not_match](generation_metageneration.md#using-if-generation-not-match)


    * **if_metageneration_match** (*long*) – (Optional) See [Using if_metageneration_match](generation_metageneration.md#using-if-metageneration-match)


    * **if_metageneration_not_match** (*long*) – (Optional) See [Using if_metageneration_not_match](generation_metageneration.md#using-if-metageneration-not-match)


    * **timeout** ([*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)* or *[*tuple*](https://python.readthedocs.io/en/latest/library/stdtypes.html#tuple)) – (Optional) The amount of time, in seconds, to wait
    for the server response.  See: [Configuring Timeouts](retry_timeout.md#configuring-timeouts)


    * **checksum** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) The type of checksum to compute to verify
    the integrity of the object. If the upload is completed in a single
    request, the checksum will be entirely precomputed and the remote
    server will handle verification and error handling. If the upload
    is too large and must be transmitted in multiple requests, the
    checksum will be incrementally computed and the client will handle
    verification and error handling, raising
    google.resumable_media.common.DataCorruption on a mismatch and
    attempting to delete the corrupted file. Supported values are
    “md5”, “crc32c” and None. The default is None.


    * **retry** ([*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)* or *[*google.cloud.storage.retry.ConditionalRetryPolicy*](retry.md#google.cloud.storage.retry.ConditionalRetryPolicy)) – (Optional) How to retry the RPC. A None value will disable
    retries. A google.api_core.retry.Retry value will enable retries,
    and the object will define retriable response codes and errors and
    configure backoff and timeout options.

    A google.cloud.storage.retry.ConditionalRetryPolicy value wraps a
    Retry object and activates it only if certain conditions are met.
    This class exists to provide safe defaults for RPC calls that are
    not technically safe to retry normally (due to potential data
    duplication or other side-effects) but become safe to retry if a
    condition such as if_generation_match is set.

    See the retry.py source code and docstrings in this package
    (google.cloud.storage.retry) for information on retry types and how
    to configure them.

    Media operations (downloads and uploads) do not support non-default
    predicates in a Retry object. The default will always be used. Other
    configuration changes for Retry objects such as delays and deadlines
    are respected.




#### upload_from_string(data, content_type='text/plain', num_retries=None, client=None, predefined_acl=None, if_generation_match=None, if_generation_not_match=None, if_metageneration_match=None, if_metageneration_not_match=None, timeout=60, checksum=None, retry=<google.cloud.storage.retry.ConditionalRetryPolicy object>)
Upload contents of this blob from the provided string.

**NOTE**: The effect of uploading to an existing blob depends on the
“versioning” and “lifecycle” policies defined on the blob’s
bucket.  In the absence of those policies, upload will
overwrite any existing contents.

See the [object versioning]([https://cloud.google.com/storage/docs/object-versioning](https://cloud.google.com/storage/docs/object-versioning))
and [lifecycle]([https://cloud.google.com/storage/docs/lifecycle](https://cloud.google.com/storage/docs/lifecycle))
API documents for details.

If `user_project` is set on the bucket, bills the API request
to that project.


* **Parameters**

    
    * **data** ([*bytes*](https://python.readthedocs.io/en/latest/library/stdtypes.html#bytes)* or *[*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – The data to store in this blob.  If the value is text, it will be
    encoded as UTF-8.


    * **content_type** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) Type of content being uploaded. Defaults to
    `'text/plain'`.


    * **num_retries** ([*int*](https://python.readthedocs.io/en/latest/library/functions.html#int)) – Number of upload retries. By default, only uploads with
    if_generation_match set will be retried, as uploads without the
    argument are not guaranteed to be idempotent. Setting num_retries
    will override this default behavior and guarantee retries even when
    if_generation_match is not set.  (Deprecated: This argument
    will be removed in a future release.)


    * **client** ([`Client`](client.md#google.cloud.storage.client.Client)) – (Optional) The client to use.  If not passed, falls back to the
    `client` stored on the blob’s bucket.


    * **predefined_acl** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) Predefined access control list


    * **if_generation_match** (*long*) – (Optional) See [Using if_generation_match](generation_metageneration.md#using-if-generation-match)


    * **if_generation_not_match** (*long*) – (Optional) See [Using if_generation_not_match](generation_metageneration.md#using-if-generation-not-match)


    * **if_metageneration_match** (*long*) – (Optional) See [Using if_metageneration_match](generation_metageneration.md#using-if-metageneration-match)


    * **if_metageneration_not_match** (*long*) – (Optional) See [Using if_metageneration_not_match](generation_metageneration.md#using-if-metageneration-not-match)


    * **timeout** ([*float*](https://python.readthedocs.io/en/latest/library/functions.html#float)* or *[*tuple*](https://python.readthedocs.io/en/latest/library/stdtypes.html#tuple)) – (Optional) The amount of time, in seconds, to wait
    for the server response.  See: [Configuring Timeouts](retry_timeout.md#configuring-timeouts)


    * **checksum** ([*str*](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)) – (Optional) The type of checksum to compute to verify
    the integrity of the object. If the upload is completed in a single
    request, the checksum will be entirely precomputed and the remote
    server will handle verification and error handling. If the upload
    is too large and must be transmitted in multiple requests, the
    checksum will be incrementally computed and the client will handle
    verification and error handling, raising
    google.resumable_media.common.DataCorruption on a mismatch and
    attempting to delete the corrupted file. Supported values are
    “md5”, “crc32c” and None. The default is None.


    * **retry** ([*google.api_core.retry.Retry*](https://googleapis.dev/python/google-api-core/latest/retry.html#google.api_core.retry.Retry)* or *[*google.cloud.storage.retry.ConditionalRetryPolicy*](retry.md#google.cloud.storage.retry.ConditionalRetryPolicy)) – (Optional) How to retry the RPC. A None value will disable
    retries. A google.api_core.retry.Retry value will enable retries,
    and the object will define retriable response codes and errors and
    configure backoff and timeout options.

    A google.cloud.storage.retry.ConditionalRetryPolicy value wraps a
    Retry object and activates it only if certain conditions are met.
    This class exists to provide safe defaults for RPC calls that are
    not technically safe to retry normally (due to potential data
    duplication or other side-effects) but become safe to retry if a
    condition such as if_generation_match is set.

    See the retry.py source code and docstrings in this package
    (google.cloud.storage.retry) for information on retry types and how
    to configure them.

    Media operations (downloads and uploads) do not support non-default
    predicates in a Retry object. The default will always be used. Other
    configuration changes for Retry objects such as delays and deadlines
    are respected.




#### _property_ user_project()
Project ID billed for API requests made via this blob.

Derived from bucket’s value.


* **Return type**

    [str](https://python.readthedocs.io/en/latest/library/stdtypes.html#str)
