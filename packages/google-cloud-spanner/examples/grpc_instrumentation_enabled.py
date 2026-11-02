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
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.trace.sampling import ALWAYS_ON
from opentelemetry import trace

# Enable the gRPC instrumentation if you'd like more introspection.
from opentelemetry.instrumentation.grpc import GrpcInstrumentorClient

grpc_client_instrumentor = GrpcInstrumentorClient()
grpc_client_instrumentor.instrument()


def main():
    # Setup common variables that'll be used between Spanner and traces.
    project_id = os.environ.get('SPANNER_PROJECT_ID', 'test-project')

    # Setup OpenTelemetry, trace and Cloud Trace exporter.
    tracer_provider = TracerProvider(sampler=ALWAYS_ON)
    trace_exporter = CloudTraceSpanExporter(project_id=project_id)
    tracer_provider.add_span_processor(BatchSpanProcessor(trace_exporter))
    trace.set_tracer_provider(tracer_provider)
    # Retrieve a tracer from the global tracer provider.
    tracer = tracer_provider.get_tracer('MyApp')

    # Setup the Cloud Spanner Client.
    spanner_client = spanner.Client(project_id)

    instance = spanner_client.instance('test-instance')
    database = instance.database('test-db')

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
                    pass


if __name__ == '__main__':
    main()
