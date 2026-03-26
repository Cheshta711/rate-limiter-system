I wanted to understand how real-world backend systems handle high traffic and prevent abuse, so I built a rate-limited API system.

The main problem I focused on was how to prevent users from overwhelming an API with too many requests, like in cases of brute-force attacks or API misuse.

To solve this, I implemented rate limiting using FastAPI and Redis, where each user’s request count is tracked and limited within a time window.

I then designed the system to be scalable by deploying it on Kubernetes, where multiple instances of the API can run and handle traffic efficiently. I used NGINX as a reverse proxy to route requests, and exposed the system publicly using AWS EKS with a LoadBalancer.

To make the system observable, I integrated Prometheus to collect metrics and Grafana to visualize them, which helped me monitor request patterns and rate-limiting behavior in real time.

Through this project, I learned how to design scalable distributed systems, work with Kubernetes and cloud infrastructure, and implement real-world backend optimizations like rate limiting and monitoring.


# 🚀 Rate Limiter System (Kubernetes + AWS EKS)

A production-style distributed backend system implementing **API rate limiting**, deployed using **Kubernetes (EKS)** with full observability using **Prometheus and Grafana**.

---

## 📌 Overview

This project demonstrates how to design and deploy a scalable backend system that:

* Limits incoming API requests using Redis
* Handles traffic via NGINX
* Monitors system metrics using Prometheus
* Visualizes data using Grafana
* Runs on Kubernetes (Minikube + AWS EKS)
* Exposes services publicly via AWS LoadBalancer

---

## 🧱 Architecture

```
User 🌍
   ↓
AWS LoadBalancer
   ↓
NGINX (Reverse Proxy)
   ↓
FastAPI (Backend API)
   ↓
Redis (Rate Limiting)
   ↓
Prometheus (Metrics)
   ↓
Grafana (Dashboard)
```

---

## ⚙️ Tech Stack

* **Backend:** FastAPI (Python)
* **Cache / Rate Limiting:** Redis
* **Reverse Proxy:** NGINX
* **Monitoring:** Prometheus
* **Visualization:** Grafana
* **Containerization:** Docker
* **Orchestration:** Kubernetes
* **Cloud:** AWS EKS

---

## 🔥 Features

* ✅ API rate limiting using Redis
* ✅ Distributed system architecture
* ✅ Kubernetes deployments (YAML-based)
* ✅ Prometheus metrics collection
* ✅ Grafana dashboard visualization
* ✅ Public API exposure via AWS LoadBalancer
* ✅ Scalable and production-ready setup

---

## 🚀 How It Works

1. User sends request to API
2. NGINX routes request to FastAPI
3. FastAPI checks Redis for request count
4. If limit exceeded → request blocked
5. Prometheus collects metrics
6. Grafana visualizes system performance

---

## 🧪 Example Output

### Allowed Requests

```json
{"message": "Hello World"}
```

### Blocked Requests

```json
{"detail": "Rate limit exceeded"}
```

---

## ☸️ Kubernetes Deployment

All services are deployed using Kubernetes manifests inside the `k8s/` directory:

* `api-deployment.yaml`
* `nginx-deployment.yaml`
* `redis-deployment.yaml`
* `prometheus.yaml`
* `grafana.yaml`

Deploy using:

```bash
kubectl apply -f k8s/
```

---

## 🌍 Public Access

The application is exposed using AWS LoadBalancer:

```
http://<EXTERNAL-IP>/hello
```

---

## 📊 Monitoring

* **Prometheus:** Collects metrics from FastAPI
* **Grafana:** Displays dashboards for:

  * Request count
  * Blocked requests
  * System performance

---

## 🧠 Learnings

* Built a distributed system from scratch
* Understood Kubernetes deployments and services
* Implemented real-world rate limiting logic
* Integrated monitoring and observability tools
* Deployed infrastructure on AWS EKS

---

## 💼 Resume Highlight

> Built a scalable rate-limited API system using FastAPI, Redis, and Kubernetes, deployed on AWS EKS with monitoring via Prometheus and Grafana.

---

## 🔮 Future Improvements

* 🔐 Add authentication (JWT-based)
* 📈 Implement auto-scaling (HPA)
* 🌍 Add custom domain + HTTPS
* 🔄 CI/CD pipeline with GitHub Actions

---

## 📁 Project Structure

```
rate-limiter-system/
│
├── api/                # FastAPI app
├── k8s/                # Kubernetes manifests
├── nginx/              # NGINX configs
├── prometheus/         # Prometheus config
├── docker-compose.yml  # Local setup
└── README.md
```



Give it a ⭐ on GitHub!
