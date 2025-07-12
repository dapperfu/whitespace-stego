#!/usr/bin/env python3
"""
CLI Benchmarking Script for Whitespace Steganography Implementations

Usage:
  python scripts/benchmark_cli.py [--iterations N] [--json OUTPUT]

Benchmarks all CLI binaries in bin/ for encode and decode performance.
- Uses /tmp/benchmark_message.txt and /tmp/benchmark_carrier.txt as input
- Outputs to /tmp/encoded_<impl>.txt and /tmp/decoded_<impl>.txt
- Reports throughput (ops/sec), average time (ms), and stddev
- Results are printed as a table and optionally saved as JSON

Add new implementations by editing the IMPLEMENTATIONS dict.
"""
import subprocess
import time
import statistics
import os
import argparse
import json

# Configurable implementations and their CLI templates
IMPLEMENTATIONS = {
    "go": {
        "encode": "./bin/whitespace-stego-go encode -mf {msg} -cf {carrier} -o {encoded}",
        "decode": "./bin/whitespace-stego-go decode -cf {encoded} -o {decoded}",
    },
    "c": {
        "encode": "./bin/whitespace-stego-c encode --message-file {msg} --carrier-file {carrier} --output {encoded}",
        "decode": "./bin/whitespace-stego-c decode --carrier-file {encoded} --output {decoded}",
    },
    "c-static": {
        "encode": "./bin/whitespace-stego-c-static encode --message-file {msg} --carrier-file {carrier} --output {encoded}",
        "decode": "./bin/whitespace-stego-c-static decode --carrier-file {encoded} --output {decoded}",
    },
    "cpp": {
        "encode": "./bin/whitespace-stego-cpp encode -mf {msg} -cf {carrier} -o {encoded}",
        "decode": "./bin/whitespace-stego-cpp decode -cf {encoded} -o {decoded}",
    },
    "py": {
        "encode": "./bin/whitespace-stego-py --backend python encode --message-file {msg} --carrier-file {carrier} --output {encoded}",
        "decode": "./bin/whitespace-stego-py --backend python decode --carrier-file {encoded} --output {decoded}",
    },
    "py-c": {
        "encode": "./bin/whitespace-stego-py --backend c encode --message-file {msg} --carrier-file {carrier} --output {encoded}",
        "decode": "./bin/whitespace-stego-py --backend c decode --carrier-file {encoded} --output {decoded}",
    },
    "py-rs": {
        "encode": "./bin/whitespace-stego-py --backend rust encode --message-file {msg} --carrier-file {carrier} --output {encoded}",
        "decode": "./bin/whitespace-stego-py --backend rust decode --carrier-file {encoded} --output {decoded}",
    },
    "rs": {
        "encode": "./bin/whitespace-stego-rs encode --mf {msg} --cf {carrier} --output {encoded}",
        "decode": "./bin/whitespace-stego-rs decode --cf {encoded} --output {decoded}",
    },
}

DEFAULT_ITER = 100
MSG_FILE = "/tmp/benchmark_message.txt"
CARRIER_FILE = "/tmp/benchmark_carrier.txt"

# Iterations per implementation (slower ones get fewer iterations)
ITERATIONS_PER_IMPL = {
    "go": 100,
    "c": 100,
    "c-static": 100,
    "cpp": 100,
    "py": 10,  # Much slower, so fewer iterations
    "py-c": 10,  # Much slower, so fewer iterations
    "py-rs": 10,  # Much slower, so fewer iterations
    "rs": 100,
}


def run_benchmark(cmd_template, subs, iterations):
    times = []
    for _ in range(iterations):
        cmd = cmd_template.format(**subs)
        start = time.perf_counter()
        subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        end = time.perf_counter()
        times.append(end - start)
    return times


def summarize(times):
    avg = sum(times) / len(times)
    std = statistics.stdev(times) if len(times) > 1 else 0.0
    throughput = len(times) / sum(times)
    return avg, std, throughput


def main():
    parser = argparse.ArgumentParser(description="Benchmark all CLI implementations.")
    parser.add_argument("--iterations", type=int, default=DEFAULT_ITER, help="Number of iterations per test (overrides per-impl settings)")
    parser.add_argument("--json", type=str, default=None, help="Output JSON file for results")
    args = parser.parse_args()

    results = {}
    print(f"Benchmarking {len(IMPLEMENTATIONS)} implementations...")
    print()
    print(f"Message file: {MSG_FILE}")
    print(f"Carrier file: {CARRIER_FILE}")
    print()
    print(f"{'Impl':<10} {'Op':<7} {'Iter':>5} {'Avg(ms)':>10} {'Std(ms)':>10} {'Ops/sec':>10}")
    print("-" * 55)

    for impl, cmds in IMPLEMENTATIONS.items():
        # Use per-implementation iterations unless overridden
        iterations = args.iterations if args.iterations != DEFAULT_ITER else ITERATIONS_PER_IMPL.get(impl, DEFAULT_ITER)
        # Prepare file names
        encoded = f"/tmp/encoded_{impl}.txt"
        decoded = f"/tmp/decoded_{impl}.txt"
        subs = dict(msg=MSG_FILE, carrier=CARRIER_FILE, encoded=encoded, decoded=decoded)
        # Encode benchmark
        encode_times = run_benchmark(cmds["encode"], subs, iterations)
        avg_e, std_e, thr_e = summarize(encode_times)
        print(f"{impl:<10} {'encode':<7} {iterations:>5} {avg_e*1000:10.2f} {std_e*1000:10.2f} {thr_e:10.1f}")
        # Decode benchmark
        decode_times = run_benchmark(cmds["decode"], subs, iterations)
        avg_d, std_d, thr_d = summarize(decode_times)
        print(f"{impl:<10} {'decode':<7} {iterations:>5} {avg_d*1000:10.2f} {std_d*1000:10.2f} {thr_d:10.1f}")
        results[impl] = {
            "encode": {"avg_ms": avg_e*1000, "std_ms": std_e*1000, "ops_sec": thr_e, "iterations": iterations},
            "decode": {"avg_ms": avg_d*1000, "std_ms": std_d*1000, "ops_sec": thr_d, "iterations": iterations},
        }
        # Clean up output files
        for f in [encoded, decoded]:
            try:
                os.remove(f)
            except FileNotFoundError:
                pass
    print("\nDone.")
    if args.json:
        with open(args.json, "w") as f:
            json.dump(results, f, indent=2)
        print(f"Results saved to {args.json}")

if __name__ == "__main__":
    main() 