Integration with Python Web Frameworks
======================================

The Google Cloud Logging library can integrate with Python web frameworks
`flask <https://flask.palletsprojects.com/>`_ and `django <https://www.djangoproject.com/>`_ to
automatically populate `LogEntry fields <https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry>`_ 
`trace`, `span_id`, `trace_sampled`, and `http_request`.

Django
------

Django integration has been tested to work with each of the Django/Python versions listed `here <https://docs.djangoproject.com/en/stable/faq/install/#what-python-version-can-i-use-with-django>`_. 
To enable Django integration, add `google.cloud.logging_v2.handlers.middleware.RequestMiddleware` to the list of `MIDDLEWARE`
in your `settings <https://docs.djangoproject.com/en/stable/topics/settings/>`_ file. Also be sure to set up logging in your settings file.

Flask
-----

Flask integration has been tested to work with the following versions of Flask:

- Python 3.7 - 3.9:

 - Flask >=1.0.0

- Python >=3.10:

 - Flask >=1.0.3

Be sure to set up logging before declaring the Flask app.
