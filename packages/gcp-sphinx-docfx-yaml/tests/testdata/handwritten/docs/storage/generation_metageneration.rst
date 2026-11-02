Conditional Requests Via ETag / Generation / Metageneration Preconditions
=========================================================================

Preconditions tell Cloud Storage to only perform a request if the
:ref:`ETag <concept-etag>`, :ref:`generation <concept-generation>`, or
:ref:`metageneration <concept-metageneration>` number of the affected object
meets your precondition criteria. These checks of the ETag, generation, and
metageneration numbers ensure that the object is in the expected state,
allowing you to perform safe read-modify-write updates and conditional
operations on objects

Concepts
--------

.. _concept-etag:

ETag
::::::::::::::

An ETag is returned as part of the response header whenever a resource is
returned, as well as included in the resource itself. Users should make no
assumptions about the value used in an ETag except that it changes whenever the
underlying data changes, per the
`specification <https://tools.ietf.org/html/rfc7232#section-2.3>`_

The ``ETag`` attribute is set by the GCS back-end, and is read-only in the
client library.

.. _concept-metageneration:

Metageneration
::::::::::::::

When you create a :class:`~google.cloud.storage.bucket.Bucket`,
its :attr:`~google.cloud.storage.bucket.Bucket.metageneration` is initialized
to ``1``, representing the initial version of the bucket's metadata.

When you first upload a
:class:`~google.cloud.storage.blob.Blob` ("Object" in the GCS back-end docs),
its :attr:`~google.cloud.storage.blob.Blob.metageneration` is likewise
initialized to ``1``.  representing the initial version of the blob's metadata.

The ``metageneration`` attribute is set by the GCS back-end, and is read-only
in the client library.

Each time you patch or update the bucket's / blob's metadata, its
``metageneration`` is incremented.


.. _concept-generation:

Generation
::::::::::

Each time you upload a new version of a file to a
:class:`~google.cloud.storage.blob.Blob` ("Object" in the GCS back-end docs),
the Blob's :attr:`~google.cloud.storage.blob.generation` is changed, and its
:attr:`~google.cloud.storage.blob.metageneration` is reset to ``1`` (the first
metadata version for that generation of the blob).

The ``generation`` attribute is set by the GCS back-end, and is read-only
in the client library.

See also
::::::::

- `Storage API Generation Precondition docs`_

.. _Storage API Generation Precondition docs:
   https://cloud.google.com/storage/docs/generations-preconditions


Conditional Parameters
----------------------

.. _using-if-etag-match:

Using ``if_etag_match``
:::::::::::::::::::::::::::::

Passing the ``if_etag_match`` parameter to a method which retrieves a
blob resource (e.g.,
:meth:`Blob.reload <google.cloud.storage.blob.Blob.reload>`)
makes the operation conditional on whether the blob's current ``ETag`` matches
the given value. This parameter is not supported for modification (e.g.,
:meth:`Blob.update <google.cloud.storage.blob.Blob.update>`).


.. _using-if-etag-not-match:

Using ``if_etag_not_match``
:::::::::::::::::::::::::::::

Passing the ``if_etag_not_match`` parameter to a method which retrieves a
blob resource (e.g.,
:meth:`Blob.reload <google.cloud.storage.blob.Blob.reload>`)
makes the operation conditional on whether the blob's current ``ETag`` matches
the given value. This parameter is not supported for modification (e.g.,
:meth:`Blob.update <google.cloud.storage.blob.Blob.update>`).


.. _using-if-generation-match:

Using ``if_generation_match``
:::::::::::::::::::::::::::::

Passing the ``if_generation_match`` parameter to a method which retrieves a
blob resource (e.g.,
:meth:`Blob.reload <google.cloud.storage.blob.Blob.reload>`) or modifies
the blob (e.g.,
:meth:`Blob.update <google.cloud.storage.blob.Blob.update>`)
makes the operation conditional on whether the blob's current ``generation``
matches the given value.

As a special case, passing ``0`` as the value for ``if_generation_match``
makes the operation succeed only if there are no live versions of the blob.


.. _using-if-generation-not-match:

Using ``if_generation_not_match``
:::::::::::::::::::::::::::::::::

Passing the ``if_generation_not_match`` parameter to a method which retrieves
a blob resource (e.g.,
:meth:`Blob.reload <google.cloud.storage.blob.Blob.reload>`) or modifies
the blob (e.g.,
:meth:`Blob.update <google.cloud.storage.blob.Blob.update>`)
makes the operation conditional on whether the blob's current ``generation``
does **not** match the given value.

If no live version of the blob exists, the precondition fails.

As a special case, passing ``0`` as the value for ``if_generation_not_match``
makes the operation succeed only if there **is** a live version of the blob.


.. _using-if-metageneration-match:

Using ``if_metageneration_match``
:::::::::::::::::::::::::::::::::

Passing the ``if_metageneration_match`` parameter to a method which retrieves
a blob or bucket resource
(e.g., :meth:`Blob.reload <google.cloud.storage.blob.Blob.reload>`,
:meth:`Bucket.reload <google.cloud.storage.bucket.Bucket.reload>`)
or modifies the blob or bucket (e.g.,
:meth:`Blob.update <google.cloud.storage.blob.Blob.update>`
:meth:`Bucket.patch <google.cloud.storage.bucket.Bucket.patch>`)
makes the operation conditional on whether the resource's current
``metageneration`` matches the given value.


.. _using-if-metageneration-not-match:

Using ``if_metageneration_not_match``
:::::::::::::::::::::::::::::::::::::

Passing the ``if_metageneration_not_match`` parameter to a method which
retrieves a blob or bucket resource
(e.g., :meth:`Blob.reload <google.cloud.storage.blob.Blob.reload>`,
:meth:`Bucket.reload <google.cloud.storage.bucket.Bucket.reload>`)
or modifies the blob or bucket (e.g.,
:meth:`Blob.update <google.cloud.storage.blob.Blob.update>`
:meth:`Bucket.patch <google.cloud.storage.bucket.Bucket.patch>`)
makes the operation conditional on whether the resource's current
``metageneration`` does **not** match the given value.
