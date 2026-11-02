Managing Access to Data
=======================

Cloud Storage offers two systems for granting users access your buckets and objects:
IAM and Access Control Lists (ACLs). These systems act in parallel - in order for a user to
access a Cloud Storage resource, only one of the systems needs to grant that user permission.
For additional access control options, see also:
`Cloud Storage Control Access to Data <https://cloud.google.com/storage/docs/access-control>`_  


ACL
---

Cloud Storage uses access control lists (ACLs) to manage object and bucket access.
ACLs are the mechanism you use to share files with other users and allow
other users to access your buckets and files.

ACLs are suitable for fine-grained control, but you may prefer using IAM to
control access at the project level.


:class:`google.cloud.storage.bucket.Bucket` has a getting method that creates
an ACL object under the hood, and you can interact with that using
:func:`google.cloud.storage.bucket.Bucket.acl`:

.. code-block:: python

    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    acl = bucket.acl

Adding and removing permissions can be done with the following methods
(in increasing order of granularity):

- :func:`ACL.all`
  corresponds to access for all users.
- :func:`ACL.all_authenticated` corresponds
  to access for all users that are signed into a Google account.
- :func:`ACL.domain` corresponds to access on a
  per Google Apps domain (ie, ``example.com``).
- :func:`ACL.group` corresponds to access on a
  per group basis (either by ID or e-mail address).
- :func:`ACL.user` corresponds to access on a
  per user basis (either by ID or e-mail address).

And you are able to ``grant`` and ``revoke`` the following roles:

- **Reading**:
  :func:`_ACLEntity.grant_read` and :func:`_ACLEntity.revoke_read`
- **Writing**:
  :func:`_ACLEntity.grant_write` and :func:`_ACLEntity.revoke_write`
- **Owning**:
  :func:`_ACLEntity.grant_owner` and :func:`_ACLEntity.revoke_owner`

You can use any of these like any other factory method (these happen to
be :class:`_ACLEntity` factories):

.. code-block:: python

    acl.user("me@example.org").grant_read()
    acl.all_authenticated().grant_write()

After that, you can save any changes you make with the
:func:`google.cloud.storage.acl.ACL.save` method:

.. code-block:: python

    acl.save()


You can alternatively save any existing :class:`google.cloud.storage.acl.ACL`
object (whether it was created by a factory method or not) from a
:class:`google.cloud.storage.bucket.Bucket`:

.. code-block:: python

    bucket.acl.save(acl=acl)


To get the list of ``entity`` and ``role`` for each unique pair, the
:class:`ACL` class is iterable:

.. code-block:: python

    print(list(acl))
    # [{'role': 'OWNER', 'entity': 'allUsers'}, ...]


This list of tuples can be used as the ``entity`` and ``role`` fields
when sending metadata for ACLs to the API.


IAM
---

Identity and Access Management (IAM) controls permissioning throughout Google Cloud and allows you
to grant permissions at the bucket and project levels. You should use IAM for any permissions that
apply to multiple objects in a bucket to reduce the risks of unintended exposure. To use IAM
exclusively, enable uniform bucket-level access to disallow ACLs for all Cloud Storage resources.
See also:
`Additional access control options <https://cloud.google.com/storage/docs/access-control#additional_access_control_options>`_ 

Constants used across IAM roles:
::::::::::::::::::::::::::::::::

- ``STORAGE_OBJECT_CREATOR_ROLE = "roles/storage.objectCreator"``
  corresponds to role implying rights to create objects, but not delete or overwrite them.
- ``STORAGE_OBJECT_VIEWER_ROLE = "roles/storage.objectViewer"``
  corresponds to role implying rights to view object properties, excluding ACLs.
- ``STORAGE_OBJECT_ADMIN_ROLE = "roles/storage.objectAdmin"``
  corresponds to role implying full control of objects.
- ``STORAGE_ADMIN_ROLE = "roles/storage.admin"``
  corresponds to role implying full control of objects and buckets.
- ``STORAGE_VIEWER_ROLE = "Viewer"``
  corresponds to role that can list buckets.
- ``STORAGE_EDITOR_ROLE = "Editor"``
  corresponds to role that can create, list, and delete buckets.
- ``STORAGE_OWNER_ROLE = "Owners"``
  corresponds to role that can Can create, list, and delete buckets;
  and list tag bindings; and control HMAC keys in the project.

Constants used across IAM permissions:
::::::::::::::::::::::::::::::::::::::

- ``STORAGE_BUCKETS_CREATE = "storage.buckets.create"``
  corresponds to permission that can create buckets.

- ``STORAGE_BUCKETS_DELETE = "storage.buckets.delete"``
  corresponds to permission that can delete buckets.

- ``STORAGE_BUCKETS_GET = "storage.buckets.get"``
  corresponds to permission that can read bucket metadata, excluding ACLs.

- ``STORAGE_BUCKETS_LIST = "storage.buckets.list"``
  corresponds to permission that can list buckets.

- ``STORAGE_BUCKETS_GET_IAM_POLICY = "storage.buckets.getIamPolicy"``
  corresponds to permission that can read bucket ACLs.

- ``STORAGE_BUCKETS_SET_IAM_POLICY = "storage.buckets.setIamPolicy"``
  corresponds to permission that can update bucket ACLs.

- ``STORAGE_BUCKETS_UPDATE = "storage.buckets.update"``
  corresponds to permission that can update buckets, excluding ACLS.

- ``STORAGE_OBJECTS_CREATE = "storage.objects.create"``
  corresponds to permission that can add new objects to a bucket.

- ``STORAGE_OBJECTS_DELETE = "storage.objects.delete"``
  corresponds to permission that can delete objects.

- ``STORAGE_OBJECTS_GET = "storage.objects.get"``
  corresponds to permission that can read object data / metadata, excluding ACLs.

- ``STORAGE_OBJECTS_LIST = "storage.objects.list"``
  corresponds to permission that can list objects in a bucket.

- ``STORAGE_OBJECTS_GET_IAM_POLICY = "storage.objects.getIamPolicy"``
  corresponds to permission that can read object ACLs.

- ``STORAGE_OBJECTS_SET_IAM_POLICY = "storage.objects.setIamPolicy"``
  corresponds to permission that can update object ACLs.

- ``STORAGE_OBJECTS_UPDATE = "storage.objects.update"``
  corresponds to permission that can update object metadata, excluding ACLs.
