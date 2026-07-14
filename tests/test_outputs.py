import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")

# Ground truth derived from environment/access.log:
# 6 log lines; IPs {192.168.0.1, 192.168.0.2, 10.0.0.5}; /index.html
# requested 3 times (vs. /about.html x2, /api/login x1).
EXPECTED = {
    "total_requests": 6,
    "unique_ips": 3,
    "top_path": "/index.html",
}


def _report() -> dict:
    with REPORT_PATH.open() as f:
        return json.load(f)


def test_report_is_json_object_with_exact_keys():
    """Criterion 1: /app/report.json exists and contains a single valid JSON
    object with exactly the keys total_requests, unique_ips, top_path."""
    assert REPORT_PATH.exists(), "no /app/report.json found"
    try:
        report = _report()
    except json.JSONDecodeError as exc:
        raise AssertionError(f"/app/report.json is not valid JSON: {exc}")
    assert isinstance(report, dict), "report.json must contain a JSON object"
    assert set(report) == set(EXPECTED), (
        f"report.json keys {sorted(report)} != expected {sorted(EXPECTED)}"
    )


def test_total_requests():
    """Criterion 2: total_requests is the integer count of request lines in
    /app/access.log."""
    assert _report()["total_requests"] == EXPECTED["total_requests"]


def test_unique_ips():
    """Criterion 3: unique_ips is the integer count of distinct client IP
    addresses in /app/access.log."""
    assert _report()["unique_ips"] == EXPECTED["unique_ips"]


def test_top_path():
    """Criterion 4: top_path is the most frequently requested path, with the
    leading slash."""
    assert _report()["top_path"] == EXPECTED["top_path"]
