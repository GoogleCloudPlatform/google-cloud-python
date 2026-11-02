# Copyright 2017 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and

"""The YCSB client in Python.

Usage:

  # Set up instance and load data into database.

  # Set up environment variables. You should use your own credentials and gcloud
  # project.
  $ export GOOGLE_APPLICATION_CREDENTIALS=/path/to/credentials.json
  $ export GCLOUD_PROJECT=gcloud-project-name

  # Run the benchmark.
  $ python spanner/benchmark/ycsb.py run cloud_spanner -P pkb/workloada \
    -p table=usertable -p cloudspanner.instance=ycsb-542756a4 \
    -p recordcount=5000 -p operationcount=100 -p cloudspanner.database=ycsb \
    -p num_worker=1

  # To make a package so it can work with PerfKitBenchmarker.
  $ cd spanner; tar -cvzf ycsb-python.0.0.5.tar.gz benchmark/*

"""

from google.cloud import spanner

import argparse
import numpy
import random
import string
import threading
import timeit


OPERATIONS = ['readproportion', 'updateproportion', 'scanproportion',
              'insertproportion']
NUM_FIELD = 10


def parse_options():
    """Parses options."""
    parser = argparse.ArgumentParser()
    parser.add_argument('command', help='The YCSB command.')
    parser.add_argument('benchmark', help='The YCSB benchmark.')
    parser.add_argument('-P', '--workload', action='store', dest='workload',
                        default='', help='The path to a YCSB workload file.')
    parser.add_argument('-p', '--parameter', action='append', dest='parameters',
                        default=[], help='The key=value pair of parameter.')
    parser.add_argument('-b', '--num_bucket', action='store', type=int,
                        dest='num_bucket', default=1000,
                        help='The number of buckets in output.')

    args = parser.parse_args()

    parameters = {}
    parameters['command'] = args.command
    parameters['num_bucket'] = args.num_bucket

    for parameter in args.parameters:
        parts = parameter.strip().split('=')
        parameters[parts[0]] = parts[1]

    with open(args.workload, 'r') as f:
        for line in f.readlines():
            parts = line.split('=')
            key = parts[0].strip()
            if key in OPERATIONS:
                parameters[key] = parts[1].strip()

    return parameters


def open_database(parameters):
    """Opens a database specified by the parameters from parse_options()."""
    spanner_client = spanner.Client()
    instance_id = parameters['cloudspanner.instance']
    instance = spanner_client.instance(instance_id)
    database_id = parameters['cloudspanner.database']
    pool = spanner.BurstyPool(int(parameters['num_worker']))
    database = instance.database(database_id, pool=pool)

    return database


def load_keys(database, parameters):
    """Loads keys from database."""
    keys = []
    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(
            'SELECT u.id FROM %s u' % parameters['table'])

    for row in results:
        keys.append(row[0])

    return keys


def read(database, table, key):
    """Does a single read operation."""
    with database.snapshot() as snapshot:
        result = snapshot.execute_sql('SELECT u.* FROM %s u WHERE u.id="%s"' %
                                      (table, key))
        for row in result:
            key = row[0]
        for i in range(NUM_FIELD):
            field = row[i + 1]


def update(database, table, key):
    """Does a single update operation."""
    field = random.randrange(10)
    value = ''.join(random.choice(string.printable) for i in range(100))
    with database.batch() as batch:
        batch.update(table=table, columns=('id', 'field%d' % field),
                     values=[(key, value)])


def do_operation(database, keys, table, operation, latencies_ms):
    """Does a single operation and records latency."""
    key = random.choice(keys)
    start = timeit.default_timer()
    if operation == 'read':
        read(database, table, key)
    elif operation == 'update':
        update(database, table,  key)
    else:
        raise ValueError('Unknown operation: %s' % operation)
    end = timeit.default_timer()
    latencies_ms[operation].append((end - start) * 1000)


def aggregate_metrics(latencies_ms, duration_ms, num_bucket):
    """Aggregates metrics."""
    overall_op_count = 0
    op_counts = {operation : len(latency) for operation,
                 latency in latencies_ms.iteritems()}
    overall_op_count = sum([op_count for op_count in op_counts.itervalues()])

    print('[OVERALL], RunTime(ms), %f' % duration_ms)
    print('[OVERALL], Throughput(ops/sec), %f' % (float(overall_op_count) /
                                                duration_ms * 1000.0))

    for operation in op_counts.keys():
        operation_upper = operation.upper()
        print('[%s], Operations, %d' % (operation_upper, op_counts[operation]))
        print('[%s], AverageLatency(us), %f' % (
            operation_upper, numpy.average(latencies_ms[operation]) * 1000.0))
        print('[%s], LatencyVariance(us), %f' % (
            operation_upper, numpy.var(latencies_ms[operation]) * 1000.0))
        print('[%s], MinLatency(us), %f' % (
            operation_upper, min(latencies_ms[operation]) * 1000.0))
        print('[%s], MaxLatency(us), %f' % (
            operation_upper, max(latencies_ms[operation]) * 1000.0))
        print('[%s], 95thPercentileLatency(us), %f' % (
            operation_upper,
            numpy.percentile(latencies_ms[operation], 95.0) * 1000.0))
        print('[%s], 99thPercentileLatency(us), %f' % (
            operation_upper,
            numpy.percentile(latencies_ms[operation], 99.0) * 1000.0))
        print('[%s], 99.9thPercentileLatency(us), %f' % (
            operation_upper,
            numpy.percentile(latencies_ms[operation], 99.9) * 1000.0))
        print('[%s], Return=OK, %d' % (operation_upper, op_counts[operation]))
        latency_array = numpy.array(latencies_ms[operation])
        for j in range(num_bucket):
            print('[%s], %d, %d' % (
                operation_upper, j,
                ((j <= latency_array) & (latency_array < (j + 1))).sum()))
        print('[%s], >%d, %d' % (operation_upper, num_bucket,
                                 (num_bucket <= latency_array).sum()))


class WorkloadThread(threading.Thread):
    """A single thread running workload."""

    def __init__(self, database, keys, parameters, total_weight, weights,
                 operations):
        threading.Thread.__init__(self)
        self._database = database
        self._keys = keys
        self._parameters = parameters
        self._total_weight = total_weight
        self._weights = weights
        self._operations = operations
        self._latencies_ms = {}
        for operation in self._operations:
            self._latencies_ms[operation] = []

    def run(self):
        """Run a single thread of the workload."""
        i = 0
        operation_count = int(self._parameters['operationcount'])
        while i < operation_count:
            i += 1
            weight = random.uniform(0, self._total_weight)
            for j in range(len(self._weights)):
                if weight <= self._weights[j]:
                    do_operation(self._database, self._keys,
                                 self._parameters['table'],
                                 self._operations[j], self._latencies_ms)
                    break

    def latencies_ms(self):
        """Returns the latencies."""
        return self._latencies_ms


def run_workload(database, keys, parameters):
    """Runs workload against the database."""
    total_weight = 0.0
    weights = []
    operations = []
    latencies_ms = {}
    for operation in OPERATIONS:
        weight = float(parameters[operation])
        if weight <= 0.0:
            continue
        total_weight += weight
        op_code = operation.split('proportion')[0]
        operations.append(op_code)
        weights.append(total_weight)
        latencies_ms[op_code] = []

    threads = []
    start = timeit.default_timer()
    for i in range(int(parameters['num_worker'])):
        thread = WorkloadThread(database, keys, parameters, total_weight,
                                weights, operations)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
        end = timeit.default_timer()

    for thread in threads:
        thread_latencies_ms = thread.latencies_ms()
        for key in latencies_ms.keys():
            latencies_ms[key].extend(thread_latencies_ms[key])

    aggregate_metrics(latencies_ms, (end - start) * 1000.0,
                      parameters['num_bucket'])


if __name__ == '__main__':
    parameters = parse_options()
    if parameters['command'] == 'run':
        if 'cloudspanner.channels' in parameters:
            assert parameters['cloudspanner.channels'] == 1, (
                'Python doesn\'t support channels > 1.')
        database = open_database(parameters)
        keys = load_keys(database, parameters)
        run_workload(database, keys, parameters)
    else:
        raise ValueError('Unknown command %s.' % parameters['command'])
