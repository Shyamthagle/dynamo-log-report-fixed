An Apache-style access log is located at `/app/access.log`. Each line follows
the common log format, e.g.:

```
192.168.0.1 - - [16/Jun/2026:10:00:01 +0000] "GET /index.html HTTP/1.1" 200 1024
```

Analyze the log and write a JSON summary report to `/app/report.json`.

Success criteria:

1. `/app/report.json` exists and contains a single valid JSON object with
   exactly three keys: `total_requests`, `unique_ips`, and `top_path` —
   no other keys.
2. `total_requests` is an integer: the total number of request lines in
   `/app/access.log`.
3. `unique_ips` is an integer: the number of distinct client IP addresses
   (the first field of each line).
4. `top_path` is a string: the most frequently requested path, including the
   leading slash (taken from the request line, e.g. `/index.html`).
