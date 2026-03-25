import time
from redis_client import redis_client
from config import WINDOW_SIZE, TOKEN_BUCKET_SIZE, REFILL_RATE

# 🔹 Sliding Window
def sliding_window(key, limit):
    now = int(time.time())

    redis_key = f"sw:{key}"

    # remove old entries
    redis_client.zremrangebyscore(redis_key, 0, now - WINDOW_SIZE)

    # count requests
    current = redis_client.zcard(redis_key)

    if current >= limit:
        return False

    redis_client.zadd(redis_key, {str(now): now})
    return True


# 🔹 Token Bucket
def token_bucket(key):
    redis_key = f"tb:{key}"

    data = redis_client.hmget(redis_key, "tokens", "last_refill")

    tokens = float(data[0]) if data[0] else TOKEN_BUCKET_SIZE
    last_refill = float(data[1]) if data[1] else time.time()

    now = time.time()

    # refill tokens
    tokens += (now - last_refill) * REFILL_RATE
    tokens = min(tokens, TOKEN_BUCKET_SIZE)

    if tokens < 1:
        return False

    tokens -= 1

    redis_client.hmset(redis_key, {
        "tokens": tokens,
        "last_refill": now
    })

    return True