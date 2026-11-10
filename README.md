# devops-sci-week3

Starter repository for TCHN6105 (DevOps for Scientific Computing), Weeks 3-4 labs.

| File | What it is for |
|---|---|
| `calc.py` | The "scientific" code: `add`, `multiply`, `trapezoid` (numerical integration) |
| `tests/test_calc.py` | Unit, floating-point and convergence tests (run with pytest) |
| `scripts/run_regression.py` | Regression test against `reference/reference_output.json` |
| `scripts/benchmark.py` | Small benchmark (Continuous Benchmarking idea) |
| `.github/workflows/ci.yml` | GitHub Actions workflow (Activity 3.1) |
| `.gitlab-ci.yml` | GitLab CI pipeline (Activity 3.2) |
| `Jenkinsfile` | Declarative Jenkins pipeline (Activity 4.1) |

Run locally: `pip install -r requirements.txt` then `python -m pytest`.
