from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, Response
from limiter import sliding_window, token_bucket
from config import RATE_LIMITS
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = FastAPI()

# 📊 Metrics
REQUEST_COUNT = Counter("requests_total", "Total Requests")
BLOCKED_COUNT = Counter("blocked_total", "Blocked Requests")


# 🔑 Generate unique key (IP + endpoint)
def get_key(request: Request):
    forwarded = request.headers.get("x-forwarded-for")

    if forwarded:
        ip = forwarded.split(",")[0]
    else:
        ip = request.client.host

    endpoint = f"{request.method}:{request.url.path}"
    return f"{ip}:{endpoint}"


# 🚦 Rate limit check
def check_rate_limit(request: Request):
    key = get_key(request)
    endpoint = f"{request.method}:{request.url.path}"

    limit = RATE_LIMITS.get(endpoint, 5)

    # Sliding Window
    if not sliding_window(key, limit):
        return False

    # Token Bucket
    if not token_bucket(key):
        return False

    return True


@app.middleware("http")
async def rate_limiter(request: Request, call_next):

    # ✅ NEVER count metrics requests
    if "/metrics" in request.url.path:
        return await call_next(request)

    # ✅ Skip Prometheus explicitly
    user_agent = request.headers.get("user-agent", "")
    if "Prometheus" in user_agent:
        return await call_next(request)

    REQUEST_COUNT.inc()

    if not check_rate_limit(request):
        BLOCKED_COUNT.inc()
        return JSONResponse(
            status_code=429,
            content={"detail": "Rate limit exceeded"}
        )

    return await call_next(request)

# 📌 API Endpoints
@app.get("/hello")
def hello():
    return {"message": "Hello World"}


@app.get("/data")
def data():
    return {"data": "Some data"}


@app.post("/login")
def login():
    return {"status": "logged in"}


# 📊 Prometheus Metrics Endpoint (FIXED)
@app.get("/metrics")
def metrics():
    return Response(
        content=generate_latest(),
        media_type=CONTENT_TYPE_LATEST
    )