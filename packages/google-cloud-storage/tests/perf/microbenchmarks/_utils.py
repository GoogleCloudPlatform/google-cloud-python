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
import io
import os
import socket
import statistics
from typing import Any, List, Optional, Union

import psutil

_C4_STANDARD_192_NIC = "ens3"  # can be fetched via ip link show


def publish_benchmark_extra_info(
    benchmark: Any,
    params: Any,
    benchmark_group: str = "read",
    true_times: List[float] = [],
    download_bytes_list: Optional[List[int]] = None,
    duration: Optional[Union[float, List[float]]] = None,
) -> None:
    """
    Helper function to publish benchmark parameters to the extra_info property.
    """

    benchmark.extra_info["num_files"] = params.num_files
    benchmark.extra_info["file_size"] = params.file_size_bytes
    benchmark.extra_info["chunk_size"] = params.chunk_size_bytes
    if benchmark_group == "write":
        benchmark.extra_info["pattern"] = "seq"
    else:
        benchmark.extra_info["pattern"] = params.pattern
    benchmark.extra_info["coros"] = params.num_coros
    benchmark.extra_info["rounds"] = params.rounds
    benchmark.extra_info["bucket_name"] = params.bucket_name
    benchmark.extra_info["bucket_type"] = params.bucket_type
    benchmark.extra_info["processes"] = params.num_processes
    benchmark.group = benchmark_group

    if download_bytes_list is not None:
        assert duration is not None, (
            "Duration must be provided if download_bytes_list is provided."
        )
        if isinstance(duration, list):
            assert len(download_bytes_list) == len(duration), (
                "Download bytes and duration lists must have the same length."
            )
            throughputs_list = [
                x / d / (1024 * 1024) for x, d in zip(download_bytes_list, duration)
            ]
        else:
            throughputs_list = [
                x / duration / (1024 * 1024) for x in download_bytes_list
            ]
        min_throughput = min(throughputs_list)
        max_throughput = max(throughputs_list)
        mean_throughput = statistics.mean(throughputs_list)
        median_throughput = statistics.median(throughputs_list)

    else:
        object_size = params.file_size_bytes
        num_files = params.num_files
        total_uploaded_mib = object_size / (1024 * 1024) * num_files
        min_throughput = total_uploaded_mib / benchmark.stats["max"]
        max_throughput = total_uploaded_mib / benchmark.stats["min"]
        mean_throughput = total_uploaded_mib / benchmark.stats["mean"]
        median_throughput = total_uploaded_mib / benchmark.stats["median"]

    benchmark.extra_info["throughput_MiB_s_min"] = min_throughput
    benchmark.extra_info["throughput_MiB_s_max"] = max_throughput
    benchmark.extra_info["throughput_MiB_s_mean"] = mean_throughput
    benchmark.extra_info["throughput_MiB_s_median"] = median_throughput

    print("\nThroughput Statistics (MiB/s):")
    print(f"  Min:    {min_throughput:.2f} (from max time)")
    print(f"  Max:    {max_throughput:.2f} (from min time)")
    print(f"  Mean:   {mean_throughput:.2f} (approx, from mean time)")
    print(f"  Median: {median_throughput:.2f} (approx, from median time)")

    if true_times:
        throughputs = [total_uploaded_mib / t for t in true_times]
        true_min_throughput = min(throughputs)
        true_max_throughput = max(throughputs)
        true_mean_throughput = statistics.mean(throughputs)
        true_median_throughput = statistics.median(throughputs)

        benchmark.extra_info["true_throughput_MiB_s_min"] = true_min_throughput
        benchmark.extra_info["true_throughput_MiB_s_max"] = true_max_throughput
        benchmark.extra_info["true_throughput_MiB_s_mean"] = true_mean_throughput
        benchmark.extra_info["true_throughput_MiB_s_median"] = true_median_throughput

        print("\nThroughput Statistics from true_times (MiB/s):")
        print(f"  Min:    {true_min_throughput:.2f}")
        print(f"  Max:    {true_max_throughput:.2f}")
        print(f"  Mean:   {true_mean_throughput:.2f}")
        print(f"  Median: {true_median_throughput:.2f}")

    # Get benchmark name, rounds, and iterations
    name = benchmark.name
    rounds = benchmark.stats["rounds"]
    iterations = benchmark.stats["iterations"]

    # Header for throughput table
    header = "\n\n" + "-" * 125 + "\n"
    header += "Throughput Benchmark (MiB/s)\n"
    header += "-" * 125 + "\n"
    header += f"{'Name':<50} {'Min':>10} {'Max':>10} {'Mean':>10} {'StdDev':>10} {'Median':>10} {'Rounds':>8} {'Iterations':>12}\n"
    header += "-" * 125

    # Data row for throughput table
    # The table headers (Min, Max) refer to the throughput values.
    row = f"{name:<50} {min_throughput:>10.4f} {max_throughput:>10.4f} {mean_throughput:>10.4f} {'N/A':>10} {median_throughput:>10.4f} {rounds:>8} {iterations:>12}"

    print(header)
    print(row)
    print("-" * 125)


class RandomBytesIO(io.RawIOBase):
    """
    A file-like object that generates random bytes using os.urandom.
    It enforces a fixed size and an upper safety cap.
    """

    # 10 GiB default safety cap
    DEFAULT_CAP = 10 * 1024 * 1024 * 1024

    def __init__(self, size, max_size=DEFAULT_CAP):
        """
        Args:
            size (int): The exact size of the virtual file in bytes.
            max_size (int): The maximum allowed size to prevent safety issues.
        """
        if size is None:
            raise ValueError("Size must be defined (cannot be infinite).")

        if size > max_size:
            raise ValueError(
                f"Requested size {size} exceeds the maximum limit of {max_size} bytes (10 GiB)."
            )

        self._size = size
        self._pos = 0

    def read(self, n=-1):
        # 1. Handle "read all" (n=-1)
        if n is None or n < 0:
            n = self._size - self._pos

        # 2. Handle EOF (End of File)
        if self._pos >= self._size:
            return b""

        # 3. Clamp read amount to remaining size
        # This ensures we stop exactly at `size` bytes.
        n = min(n, self._size - self._pos)

        # 4. Generate data
        data = os.urandom(n)
        self._pos += len(data)
        return data

    def readable(self):
        return True

    def seekable(self):
        return True

    def tell(self):
        return self._pos

    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            new_pos = offset
        elif whence == io.SEEK_CUR:
            new_pos = self._pos + offset
        elif whence == io.SEEK_END:
            new_pos = self._size + offset
        else:
            raise ValueError(f"Invalid whence: {whence}")

        # Clamp position to valid range [0, size]
        self._pos = max(0, min(new_pos, self._size))
        return self._pos


def get_nic_pci(nic):
    """Gets the PCI address of a network interface."""
    return os.path.basename(os.readlink(f"/sys/class/net/{nic}/device"))


def get_irqs_for_pci(pci):
    """Gets the IRQs associated with a PCI address."""
    irqs = []
    with open("/proc/interrupts") as f:
        for line in f:
            if pci in line:
                irq = line.split(":")[0].strip()
                irqs.append(irq)
    return irqs


def get_affinity(irq):
    """Gets the CPU affinity of an IRQ."""
    path = f"/proc/irq/{irq}/smp_affinity_list"
    try:
        with open(path) as f:
            return f.read().strip()
    except FileNotFoundError:
        return "N/A"


def get_primary_interface_name():
    primary_ip = None

    # 1. Determine the Local IP used for internet access
    # We use UDP (SOCK_DGRAM) so we don't actually send a handshake/packet
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # connect() to a public IP (Google DNS) to force route resolution
        s.connect(("8.8.8.8", 80))
        primary_ip = s.getsockname()[0]
    except Exception:
        # Fallback if no internet
        return None
    finally:
        s.close()

    # 2. Match that IP to an interface name using psutil
    if primary_ip:
        interfaces = psutil.net_if_addrs()
        for name, addresses in interfaces.items():
            for addr in addresses:
                # check if this interface has the IP we found
                if addr.address == primary_ip:
                    return name
    return None


def get_irq_affinity():
    """Gets the set of CPUs for a given network interface."""
    nic = get_primary_interface_name()
    if not nic:
        nic = _C4_STANDARD_192_NIC

    pci = get_nic_pci(nic)
    irqs = get_irqs_for_pci(pci)
    cpus = set()
    for irq in irqs:
        affinity_str = get_affinity(irq)
        if affinity_str != "N/A":
            for part in affinity_str.split(","):
                if "-" not in part:
                    cpus.add(int(part))
    return cpus
