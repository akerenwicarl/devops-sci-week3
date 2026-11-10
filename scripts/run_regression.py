"""Regression test: compare today's result with a stored known-good result.

Exit code 0 = same as before (pass). Exit code 1 = result changed (fail).
"""
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from calc import trapezoid  # noqa: E402

TOLERANCE = 1e-12

reference = json.loads((ROOT / "reference" / "reference_output.json").read_text())
expected = reference["integral_sin_0_pi_n200"]
actual = trapezoid(math.sin, 0, math.pi, 200)

print(f"expected = {expected!r}")
print(f"actual   = {actual!r}")
if abs(actual - expected) <= TOLERANCE:
    print("REGRESSION TEST PASSED: result unchanged")
    sys.exit(0)
print("REGRESSION TEST FAILED: result differs from the reference")
sys.exit(1)
