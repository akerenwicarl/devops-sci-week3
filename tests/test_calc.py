import math

import pytest

from calc import add, multiply, trapezoid


# ---- Unit tests: one small function at a time ----
def test_add():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-1, 1) == 0


def test_multiply():
    assert multiply(4, 5) == 20


def test_trapezoid_rejects_bad_n():
    with pytest.raises(ValueError):
        trapezoid(math.sin, 0, 1, 0)


# ---- Floating-point: never compare decimals with == ----
def test_trapezoid_close_to_exact():
    # integral of sin(x) from 0 to pi is exactly 2
    approx = trapezoid(math.sin, 0, math.pi, 1000)
    assert approx == pytest.approx(2.0, rel=1e-5)


# ---- Convergence test: does the error shrink at the expected rate? ----
def test_trapezoid_converges_at_order_2():
    exact = 2.0
    e1 = abs(trapezoid(math.sin, 0, math.pi, 50) - exact)
    e2 = abs(trapezoid(math.sin, 0, math.pi, 100) - exact)
    observed_order = math.log2(e1 / e2)
    assert observed_order == pytest.approx(2.0, abs=0.1)
