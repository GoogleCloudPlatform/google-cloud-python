# Copyright 2026 Google LLC
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
# limitations under the License.
import threading
import time

import psutil


class ResourceMonitor:
    def __init__(self):
        self.interval = 1.0

        self.vcpus = psutil.cpu_count() or 1
        self.max_cpu = 0.0
        self.max_mem = 0.0

        # Network and Time tracking
        self.start_time = 0.0
        self.duration = 0.0
        self.start_net = None
        self.net_sent_mb = 0.0
        self.net_recv_mb = 0.0

        self._stop_event = threading.Event()
        self._thread = None

    def __enter__(self):
        self.start_net = psutil.net_io_counters()
        self.start_time = time.perf_counter()
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()
        self.duration = time.perf_counter() - self.start_time
        end_net = psutil.net_io_counters()

        self.net_sent_mb = (end_net.bytes_sent - self.start_net.bytes_sent) / (
            1024 * 1024
        )
        self.net_recv_mb = (end_net.bytes_recv - self.start_net.bytes_recv) / (
            1024 * 1024
        )

    def _monitor(self):
        psutil.cpu_percent(interval=None)
        current_process = psutil.Process()
        while not self._stop_event.is_set():
            try:
                # CPU and Memory tracking for current process tree
                total_cpu = current_process.cpu_percent(interval=None)
                current_mem = current_process.memory_info().rss
                for child in current_process.children(recursive=True):
                    try:
                        total_cpu += child.cpu_percent(interval=None)
                        current_mem += child.memory_info().rss
                    except (psutil.NoSuchProcess, psutil.AccessDenied):
                        continue

                # Normalize CPU by number of vcpus
                global_cpu = total_cpu / self.vcpus

                mem = current_mem

                if global_cpu > self.max_cpu:
                    self.max_cpu = global_cpu
                if mem > self.max_mem:
                    self.max_mem = mem
            except psutil.NoSuchProcess:
                pass

            time.sleep(self.interval)

    def start(self):
        self._thread = threading.Thread(target=self._monitor, daemon=True)
        self._thread.start()

    def stop(self):
        self._stop_event.set()
        if self._thread:
            self._thread.join()

    @property
    def throughput_mb_s(self):
        """Calculates combined network throughput."""
        if self.duration <= 0:
            return 0.0
        return (self.net_sent_mb + self.net_recv_mb) / self.duration
