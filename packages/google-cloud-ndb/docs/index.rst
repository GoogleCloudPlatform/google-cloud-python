##########################################
``ndb`` library for Google Cloud Datastore
##########################################

.. toctree::
   :hidden:
   :maxdepth: 2

   client
   context
   global_cache
   key
   model
   query
   tasklets
   exceptions
   polymodel
   django-middleware
   msgprop
   blobstore
   metadata
   stats
   migrating

This is a Python 3 version of the `ndb` client library for use with
`Google Cloud Datastore <https://cloud.google.com/datastore>`_.

The `original Python 2 version
<https://github.com/GoogleCloudPlatform/datastore-ndb-python>`_ was designed
specifically for the Google App Engine `python27` runtime.  This version of
`ndb` is designed for the `Google App Engine Python 3 runtime
<https://cloud.google.com/appengine/docs/standard/python3/>`_ and will run on
other Python 3 platforms as well.

Installing ``ndb``
==================

``ndb`` can be installed using pip::

    $ pip install google-cloud-ndb

Before you can use ``ndb``, you need a way to authenticate with Google. The
recommended way to do this is to create a `service account
<https://cloud.google.com/docs/authentication/getting-started>`_ that is
associated with the Google Cloud project that you'll be working on. Detailed
instructions are on the link above, but basically once you create the account
you will be able to download a JSON file with your credentials which you can
store locally.

Once you have the credentials, the best way to let your application know about
them is to set an environment variable with the path to the JSON file. On
Linux::

    export GOOGLE_APPLICATION_CREDENTIALS="/path/to/credentials.json"

From the Windows command prompt::

    set GOOGLE_APPLICATION_CREDENTIALS=C:\path\to\credentials.json

To test that your credentials work, try this from the Python environment where
you installed ``ndb``::

    >>> from google.cloud import ndb
    >>> client = ndb.Client()
    >>> client
    <google.cloud.ndb.client.Client object at 0x7f82593727b8> 

If your credentials are OK, you will have an active client. Otherwise, Python
will raise a `google.auth.exceptions.DefaultCredentialsError` exception.

Next, you'll need to enable Firestore with Datastore API to your project. To do
that, select "APIs & Services" from the Google Cloud Platform menu, then "Enable
APIs and Services". From there, look for "Databases" in the Category filter.
Make sure that both "Cloud Datastore API" and "Google Cloud Firestore API" are
enabled.

Accessing a specific project, database, or namespace
====================================================

A client can be bound to a chosen Google Cloud project, database, and/or namespace
by passing one or more of these options to the client constructor::

    client = ndb.Client(
        project="your-project-id",
        database="your-database-id",
        namespace="your-namespace"
    )

Defining Entities, Keys, and Properties
=======================================

Now that we have completed setup, we can start writing applications. Let's
begin by introducing some of ``ndb``'s most important concepts.

Cloud Datastore stores data objects, called entities. An entity has one or more
properties, named values of one of several supported data types. For example, a
property can be a string, an integer, or a reference to another entity.

Each entity is identified by a key, an identifier unique within the
application's datastore. The key can have a parent, another key. This parent
can itself have a parent, and so on; at the top of this "chain" of parents is a
key with no parent, called the root.

Entities whose keys have the same root form an entity group or group. If
entities are in different groups, then changes to those entities might
sometimes seem to occur "out of order". If the entities are unrelated in your
application's semantics, that's fine. But if some entities' changes should be
consistent, your application should make them part of the same group when
creating them. 

In practice, this would look like the following. Assume we want to keep track
of personal contacts. Our entities might look like this::

    from google.cloud import ndb

    class Contact(ndb.Model):
        name = ndb.StringProperty()
        phone = ndb.StringProperty()
        email = ndb.StringProperty()

For now, we'll keep it simple. For each contact, we'll have a name, a phone
number, and an email. This is defined in the above code. Notice that our
`Contact` class inherits from `google.cloud.ndb.Model`. A model is a class
that describes a type of entity, including the types and configuration for its
properties. It's roughly analogous to a SQL Table. An entity can be created by
calling the model's class constructor and then stored by calling the put()
method.

Now that we have our model, let's create a couple of entities::

    client = ndb.Client()
    with client.context():
        contact1 = Contact(name="John Smith",
                           phone="555 617 8993",
                           email="john.smith@gmail.com")
        contact1.put()
        contact2 = Contact(name="Jane Doe",
                           phone="555 445 1937",
                           email="jane.doe@gmail.com")
        contact2.put()

An important thing to note here is that to perform any work in the underlying
Cloud Store, a client context has to be active. After the ``ndb`` client is
initialized, we get the current context using the
`ndb.google.Client.context` method. Then, we "activate" the context by
using Python's context manager mechanisms. Now, we can safely create the
entities, which are in turn stored using the put() method.

.. note::
    
    For all the following examples, please assume that the context
    activation code precedes any ``ndb`` interactions.

In this example, since we didn't specify a parent, both entities are going to
be part of the *root* entity group. Let's say we want to have separate contact
groups, like "home" or "work". In this case, we can specify a parent, in the
form of an ancestor key, using ``ndb``'s `google.cloud.ndb.Key` class::

    ancestor_key = ndb.Key("ContactGroup", "work")
    contact1 = Contact(parent=ancestor_key,
                       name="John Smith",
                       phone="555 617 8993",
                       email="john.smith@gmail.com")
    contact1.put()
    contact2 = Contact(parent=ancestor_key,
                       name="Jane Doe",
                       phone="555 445 1937",
                       email="jane.doe@gmail.com")
    contact2.put()

A `key` is composed of a pair of ``(kind, id)`` values. The kind gives the
id of the entity that this key refers to, and the id is the name that we want
to associate with this key. Note that it's not mandatory to have the kind class
defined previously in the code for this to work.

This covers the basics for storing content in the Cloud Database. If you go to
the Administration Console for your project, you should see the entities that
were just created. Select "Datastore" from the Storage section of the Google
Cloud Platform menu, then "Entities", to get to the entity search page.

Queries and Indexes
===================

Now that we have some entities safely stored, let's see how to get them out. An
application can query to find entities that match some filters::

    query = Contact.query()
    names = [c.name for c in query]

A typical ``ndb`` query filters entities by kind. In this example, we use a
shortcut from the Model class that generates a query that returns all Contact
entities. A query can also specify filters on entity property values and keys.

A query can specify sort order. If a given entity has at least one (possibly
null) value for every property in the filters and sort orders and all the
filter criteria are met by the property values, then that entity is returned as
a result.

In the previous section, we stored some contacts using an ancestor key. Using
that key, we can find only entities that "belong to" some ancestor::

    ancestor_key = ndb.Key("ContactGroup", "work")
    query = Contact.query(ancestor=ancestor_key)
    names = [c.name for c in query]

While the first query example returns all four stored contacts, this last one
only returns those stored under the "work" contact group.

There are many useful operations that can be done on a query. For example, to
get results ordered by name::

    query = Contact.query().order(Contact.name)
    names = [c.name for c in query]

You can also filter the results::

    query = Contact.query().filter(Contact.name == "John Smith")
    names = [c.name for c in query]

Every query uses an index, a table that contains the results for the query in
the desired order. The underlying Datastore automatically maintains simple
indexes (indexes that use only one property).

You can define complex indexes in a configuration file, `index.yaml
<https://cloud.google.com/datastore/docs/tools/indexconfig>`_. When starting
out with complex indexes, the easiest way to define them is by attempting a
complex query from your application or from the command line. When Datastore
encounters queries that do not yet have indexes configured, it will generate an
error stating that no matching index was found, and it will include the
recommended (and correct) index syntax as part of the error message.

For example, the following Contact query will generate an error, since we are
using more than one property::

    query = Contact.query().order(Contact.name, Contact.email)
    names = [c.name for c in query]

This will show an error like the following. Look for the text "recommended
index is" to find the index properties that you need::

    debug_error_string = "{"created":"@1560413351.069418472",
    "description":"Error received from peer ipv6:[2607:f8b0:4012
    :809::200a]:443","file": "src/core/lib/surface/call.cc",
    "file_line":1046,"grpc_message":"no matching index found.
    recommended index is:\n- kind: Contact\n  properties:\n  - name:
    name\n  - name: email\n","grpc_status":9}"

From this error, you would get the following index description::

    - kind: Contact
      properties:
        - name: name
        - name: email

Add your new indexes to a local `index.yaml` file. When you have them all, you
can add them to your project using the `gcloud` command from the `Google Cloud
SDK <https://cloud.google.com/sdk/>`_::

    gcloud datastore indexes create path/to/index.yaml

If your datastore has many entities, it takes a long time to create a new index
for them; in this case, it's wise to update the index definitions before
uploading code that uses the new index. You can use the "Datastore" control
panel to find out when the indexes have finished building.

This index mechanism supports a wide range of queries and is suitable for most
applications. However, it does not support some kinds of queries common in
other database technologies. In particular, joins aren't supported.
