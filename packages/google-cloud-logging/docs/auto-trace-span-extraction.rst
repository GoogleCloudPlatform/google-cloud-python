Automatic Trace/Span ID Extraction
==================================

.. note::
    All `LogEntry fields`_ populated manually will override those populated via methods referred to in this
    section.

The Google Cloud Logging library can automatically populate `LogEntry fields`_
`trace`, `span_id`, and `trace_sampled` via OpenTelemetry integration, or extracting header information from an HTTP request.

OpenTelemetry Integration
-------------------------

If you have the OpenTelemetry SDK package installed and are logging from within an active OpenTelemetry span, that log entry will automatically
have the `trace`, `span_id`, and `trace_sampled` fields populated from that span. More information about OpenTelemetry can be found 
`here <https://opentelemetry.io/docs/languages/python/>`_.

HTTP headers
------------

Another possible method of automatic `trace` / `span_id` is via extraction from HTTP headers. 
This is prioritized after OpenTelemetry and requires a :doc:`supported Python web framework </web-framework-integration>`.
Trace information is automatically populated from either the `W3C Traceparent <https://www.w3.org/TR/trace-context>`_ 
or `X-Cloud-Trace-Context <https://cloud.google.com/trace/docs/trace-context#legacy-http-header>`_ headers.
Populating trace information this way also automatically populates the `http_request` field in the `LogEntry` as well.

.. _LogEntry fields: https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry
