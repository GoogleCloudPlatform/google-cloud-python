Tracing with OpenTelemetry
==========================

This library uses `OpenTelemetry <https://opentelemetry.io/>`_ to automatically generate traces providing insight on calls to Cloud Spanner. 
For information on the benefits and utility of tracing, see the `Cloud Trace docs <https://cloud.google.com/trace/docs/overview>`_.

To take advantage of these traces, we first need to install OpenTelemetry:

.. code-block:: sh

    pip install opentelemetry-api opentelemetry-sdk
    pip install opentelemetry-exporter-gcp-trace

We also need to tell OpenTelemetry which exporter to use. To export Spanner traces to `Cloud Tracing <https://cloud.google.com/trace>`_, add the following lines to your application:

.. code:: python

    from opentelemetry import trace
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.sampling import TraceIdRatioBased
    from opentelemetry.exporter.cloud_trace import CloudTraceSpanExporter
    # BatchSpanProcessor exports spans to Cloud Trace
    # in a seperate thread to not block on the main thread
    from opentelemetry.sdk.trace.export import BatchSpanProcessor

    # Create and export one trace every 1000 requests
    sampler = TraceIdRatioBased(1/1000)
    tracer_provider = TracerProvider(sampler=sampler)
    tracer_provider.add_span_processor(
        # Initialize the cloud tracing exporter
        BatchSpanProcessor(CloudTraceSpanExporter())
    )
    observability_options = dict(
        tracer_provider=tracer_provider,

        # By default extended_tracing is set to True due
        # to legacy reasons to avoid breaking changes, you
        # can modify it though using the environment variable
        # SPANNER_ENABLE_EXTENDED_TRACING=false.
        enable_extended_tracing=False,

        # By default end to end tracing is set to False. Set to True 
        # for getting spans for Spanner server.
        enable_end_to_end_tracing=True,
    )
    spanner = spanner.NewClient(project_id, observability_options=observability_options)


To get more fine-grained traces from gRPC, you can enable the gRPC instrumentation by the following

.. code-block:: sh

    pip install opentelemetry-instrumentation opentelemetry-instrumentation-grpc

and then in your Python code, please add the following lines:

.. code:: python

   from opentelemetry.instrumentation.grpc import GrpcInstrumentorClient
   grpc_client_instrumentor = GrpcInstrumentorClient()
   grpc_client_instrumentor.instrument()


Generated spanner traces should now be available on `Cloud Trace <https://console.cloud.google.com/traces>`_.

Tracing is most effective when many libraries are instrumented to provide insight over the entire lifespan of a request.
For a list of libraries that can be instrumented, see the `OpenTelemetry Integrations` section of the `OpenTelemetry Python docs <https://opentelemetry-python.readthedocs.io/en/stable/>`_

Annotating spans with SQL
~~~~~~~~~~~~~~~~~~~~~~~~~

By default your spans will be annotated with SQL statements where appropriate, but that can be a PII (Personally Identifiable Information)
leak. Sadly due to legacy behavior, we cannot simply turn off this behavior by default. However you can control this behavior by setting

    SPANNER_ENABLE_EXTENDED_TRACING=false

to turn it off globally or when creating each SpannerClient, please set `observability_options.enable_extended_tracing=false`

End to end tracing
~~~~~~~~~~~~~~~~~~~~~~~~~

In addition to client-side tracing, you can opt in for end-to-end tracing. End-to-end tracing helps you understand and debug latency issues that are specific to Spanner. Refer [here](https://cloud.google.com/spanner/docs/tracing-overview) for more information.

To configure end-to-end tracing.

1. Opt in for end-to-end tracing. You can opt-in by either:
* Setting the environment variable `SPANNER_ENABLE_END_TO_END_TRACING=true` before your application is started
* In code, by setting `observability_options.enable_end_to_end_tracing=true` when creating each SpannerClient. 

2. Set the trace context propagation in OpenTelemetry.

.. code:: python

    from opentelemetry.propagate import set_global_textmap
    from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator
    set_global_textmap(TraceContextTextMapPropagator())