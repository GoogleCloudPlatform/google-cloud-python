ACL
===

Cloud Storage uses access control lists (ACLs) to manage object and bucket access.
ACLs are the mechanism you use to share files with other users and allow
other users to access your buckets and files.

ACLs are suitable for fine-grained control, but you may prefer using IAM to
control access at the project level. See also:
`Cloud Storage Control Access to Data <https://cloud.google.com/storage/docs/access-control>`_


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


ACL Module
----------

.. automodule:: google.cloud.storage.acl
  :members:
  :show-inheritance:
