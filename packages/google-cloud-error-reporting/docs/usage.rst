Using Error Reporting
=================================

After configuring your environment, create a
:class:`Client <google.cloud.error_reporting.client.Client>`

.. code-block:: python

   from google.cloud import error_reporting

   client = error_reporting.Client()

or pass in ``credentials`` and ``project`` explicitly

.. code-block:: python

   from google.cloud import error_reporting

   client = error_reporting.Client(project='my-project', credentials=creds)

Error Reporting associates errors with a service, which is an identifier for
an executable, App Engine service, or job. The default service is "python",
but a default can be specified for the client on construction time. You can
also optionally specify a version for that service, which defaults to
"default."

.. code-block:: python

   from google.cloud import error_reporting

   client = error_reporting.Client(
    project='my-project', service="login_service", version="0.1.0")


Reporting an exception
-----------------------

Report a stacktrace to Error Reporting after an exception:

.. code-block:: python

   from google.cloud import error_reporting

   client = error_reporting.Client()
   try:
       raise NameError
   except Exception:
       client.report_exception()


By default, the client will report the error using the service specified in
the client's constructor, or the default service of "python".

The user and HTTP context can also be included in the exception. The HTTP
context can be constructed using
:class:`google.cloud.error_reporting.HTTPContext`. This will be used by
Error Reporting to help group exceptions.

.. code-block:: python

   from google.cloud import error_reporting

   client = error_reporting.Client()
   user = 'example@gmail.com'
   http_context = error_reporting.HTTPContext(
       method='GET', url='/', user_agent='test agent',
       referrer='example.com', response_status_code=500,
       remote_ip='1.2.3.4')
   try:
       raise NameError
   except Exception:
       client.report_exception(http_context=http_context, user=user))

An automatic helper to build the HTTP Context from a Flask (Werkzeug) request
object is provided.

.. code-block:: python

   from google.cloud.error_reporting import build_flask_context

   @app.errorhandler(HTTPException)
   def handle_error(exc):
       client.report_exception(
           http_context=build_flask_context(request))
       # rest of error response code here


Reporting an error without an exception
-----------------------------------------

Errors can also be reported to Error Reporting outside the context
of an exception.  The library will include the file path, function name, and
line number of the location where the error was reported.

.. code-block:: python

   from google.cloud import error_reporting

   client = error_reporting.Client()
   client.report("Found an error!")

As with reporting an exception, the user and HTTP context can be provided:

.. code-block:: python

   from google.cloud import error_reporting

   client = error_reporting.Client()
   user = 'example@gmail.com'
   http_context = error_reporting.HTTPContext(
       method='GET', url='/', user_agent='test agent',
       referrer='example.com', response_status_code=500,
       remote_ip='1.2.3.4')
   client.report(
       "Found an error!", http_context=http_context, user=user))
