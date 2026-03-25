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
