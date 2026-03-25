RATE_LIMITS = {
    "GET:/hello": 10,
    "GET:/data": 5,
    "POST:/login": 3
}

WINDOW_SIZE = 60  # seconds
TOKEN_BUCKET_SIZE = 10
REFILL_RATE = 1  # tokens per second