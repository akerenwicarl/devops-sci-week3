"""Benchmark: time a small problem so we notice if the code gets slower."""
import math
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from calc import trapezoid  # noqa: E402

N = 200_000
REPEATS = 3
times = []
for _ in range(REPEATS):
    start = time.perf_counter()
    trapezoid(math.sin, 0, math.pi, N)
    times.append(time.perf_counter() - start)

best = min(times)
print(f"trapezoid with n={N}: best of {REPEATS} runs = {best:.4f} s")
with open("benchmark.txt", "w") as fh:
    fh.write(f"n={N} best_seconds={best:.6f}\n")
