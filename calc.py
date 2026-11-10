"""calc.py - a tiny 'scientific' module for the TCHN6105 CI/CD labs."""


def add(a, b):
    """Return the sum of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def trapezoid(f, a, b, n):
    """Approximate the integral of f from a to b using n trapezoids.

    The error shrinks like 1/n**2, so doubling n should cut the
    error by about 4. That is the 'convergence rate' we test in CI.
    """
    if n < 1:
        raise ValueError("n must be at least 1")
    h = (b - a) / n
    total = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        total += f(a + i * h)
    return total * h
