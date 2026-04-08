I wanted to understand how real-world backend systems handle high traffic and prevent abuse, so I built a rate-limited API system.

The main problem I focused on was how to prevent users from overwhelming an API with too many requests, like in cases of brute-force attacks or API misuse.

To solve this, I implemented rate limiting using FastAPI and Redis, where each user’s request count is tracked and limited within a time window.

I then designed the system to be scalable by deploying it on Kubernetes, where multiple instances of the API can run and handle traffic efficiently. I used NGINX as a reverse proxy to route requests, and exposed the system publicly using AWS EKS with a LoadBalancer.

To make the system observable, I integrated Prometheus to collect metrics and Grafana to visualize them, which helped me monitor request patterns and rate-limiting behavior in real time.

Through this project, I learned how to design scalable distributed systems, work with Kubernetes and cloud infrastructure, and implement real-world backend optimizations like rate limiting and monitoring.




Overview

This project demonstrates how to design and deploy a scalable backend system that:

* Limits incoming API requests using Redis
* Handles traffic via NGINX
* Monitors system metrics using Prometheus
* Visualizes data using Grafana
* Runs on Kubernetes (Minikube + AWS EKS)
* Exposes services publicly via AWS LoadBalancer


How It Works

1. User sends request to API
2. NGINX routes request to FastAPI
3. FastAPI checks Redis for request count
4. If limit exceeded → request blocked
5. Prometheus collects metrics
6. Grafana visualizes system performance

