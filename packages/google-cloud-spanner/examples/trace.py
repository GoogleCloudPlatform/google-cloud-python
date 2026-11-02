# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License

import os
import time

import google.cloud.spanner as spanner
from opentelemetry.exporter.cloud_trace import CloudTraceSpanExporter
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.trace.sampling import ALWAYS_ON
from opentelemetry import trace
from opentelemetry.propagate import set_global_textmap
from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator

# Setup common variables that'll be used between Spanner and traces.
project_id = os.environ.get('SPANNER_PROJECT_ID', 'test-project')

def spanner_with_cloud_trace():
    # [START spanner_opentelemetry_traces_cloudtrace_usage]
    # Setup OpenTelemetry, trace and Cloud Trace exporter.
    tracer_provider = TracerProvider(sampler=ALWAYS_ON)
    trace_exporter = CloudTraceSpanExporter(project_id=project_id)
    tracer_provider.add_span_processor(BatchSpanProcessor(trace_exporter))

    # Setup the Cloud Spanner Client.
    spanner_client = spanner.Client(
        project_id,
        observability_options=dict(tracer_provider=tracer_provider, enable_extended_tracing=True, enable_end_to_end_tracing=True),
    )
    
    # [END spanner_opentelemetry_traces_cloudtrace_usage]
    return spanner_client

def spanner_with_otlp():
    # [START spanner_opentelemetry_traces_otlp_usage]
    # Setup OpenTelemetry, trace and OTLP exporter.
    tracer_provider = TracerProvider(sampler=ALWAYS_ON)
    otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4317")
    tracer_provider.add_span_processor(BatchSpanProcessor(otlp_exporter))

    # Setup the Cloud Spanner Client.
    spanner_client = spanner.Client(
        project_id,
        observability_options=dict(tracer_provider=tracer_provider, enable_extended_tracing=True, enable_end_to_end_tracing=True),
    )
    # [END spanner_opentelemetry_traces_otlp_usage]
    return spanner_client


def main():
    # Setup OpenTelemetry, trace and Cloud Trace exporter.
    tracer_provider = TracerProvider(sampler=ALWAYS_ON)
    trace_exporter = CloudTraceSpanExporter(project_id=project_id)
    tracer_provider.add_span_processor(BatchSpanProcessor(trace_exporter))

    # Setup the Cloud Spanner Client.
    # Change to "spanner_client = spanner_with_otlp" to use OTLP exporter
    spanner_client = spanner_with_cloud_trace()
    instance = spanner_client.instance('test-instance')
    database = instance.database('test-db')
    
    # Set W3C Trace Context as the global propagator for end to end tracing.
    set_global_textmap(TraceContextTextMapPropagator())

    # Retrieve a tracer from our custom tracer provider.
    tracer = tracer_provider.get_tracer('MyApp')

    # Now run our queries
    with tracer.start_as_current_span('QueryInformationSchema'):
        with database.snapshot() as snapshot:
            with tracer.start_as_current_span('InformationSchema'):
                info_schema = snapshot.execute_sql(
                    'SELECT * FROM INFORMATION_SCHEMA.TABLES')
                for row in info_schema:
                    print(row)

        with tracer.start_as_current_span('ServerTimeQuery'):
            with database.snapshot() as snapshot:
                # Purposefully issue a bad SQL statement to examine exceptions
                # that get recorded and a ERROR span status.
                try:
                    data = snapshot.execute_sql('SELECT CURRENT_TIMESTAMPx()')
                    for row in data:
                        print(row)
                except Exception as e:
                    print(e)


if __name__ == '__main__':
    main()
