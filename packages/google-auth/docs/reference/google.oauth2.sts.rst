google.oauth2.sts module
========================

The client retries transient HTTP and OAuth error responses with exponential
backoff, for up to three attempts. If these attempts are exhausted, the raised
``google.auth.exceptions.OAuthError`` has ``retryable=True``. Permanent error
responses, such as invalid credentials, are not retried. Exceptions raised by
the transport propagate unchanged.

.. automodule:: google.oauth2.sts
   :members:
   :inherited-members:
   :show-inheritance:
