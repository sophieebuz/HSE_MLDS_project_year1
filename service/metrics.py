from prometheus_client import Counter, Histogram


REQUESTS = Counter(
    "http_server_requests_total",
    documentation="Number of requests to a server.",
    labelnames=["route"],
)
REQUESTS_LATENCY = Histogram(
    "http_server_requests_latency_sec",
    documentation="HTTP request latency in seconds.",
    buckets=[
        0.5,
        1.0,
        2.0,
        5.0,
        7.0,
        10.0,
        30.0,
        50.0,
        100.0,
        200.0,
        float("inf"),
    ],
    labelnames=["route"]
)
