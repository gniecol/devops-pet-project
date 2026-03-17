# 🚀 DevOps Pet Project

A production-like DevOps project demonstrating a full CI/CD pipeline with containerization, Kubernetes deployment, and monitoring.

---

## 🧠 Overview

This project simulates a real-world DevOps workflow by building, deploying, and monitoring a simple FastAPI application backed by Redis.

The system is fully automated using GitHub Actions and deployed to a Kubernetes cluster using Helm.

---

## ⚙️ Tech Stack

- Backend: FastAPI (Python)
- Cache: Redis
- Containerization: Docker
- Orchestration: Kubernetes (k3d)
- Package Management: Helm
- CI/CD: GitHub Actions
- Container Registry: GitHub Container Registry (GHCR)
- Monitoring: Prometheus + Grafana

---

## 🔄 CI/CD Pipeline

On every push to the main branch:

1. Build Docker image  
2. Tag image with commit SHA  
3. Push image to GHCR  
4. Deploy application using Helm  

git push  
↓  
GitHub Actions  
↓  
Docker build (SHA tag)  
↓  
Push to GHCR  
↓  
Helm upgrade  
↓  
Kubernetes  

---

## 📦 Application Features

- REST API endpoints:
  - /hello
  - /health
  - /notes
- Redis-backed storage
- Prometheus metrics at /metrics

---

## ☸️ Kubernetes Deployment

- Deployment
- Service (NodePort)
- Environment variables
- Liveness & Readiness probes

---

## 📊 Monitoring

- Prometheus scrapes metrics  
- Grafana visualizes them  

---

## ▶️ Run Locally

git clone https://github.com/gniecol/devops-pet-project.git  
cd devops-pet-project  

docker compose up --build  

---

## ☸️ Deploy to Kubernetes

k3d cluster create devops-cluster --port "8081:30080@loadbalancer"  

helm upgrade --install devops-pet-release ./helm/devops-pet-project   --namespace devops-pet   --create-namespace  

http://localhost:8081  

---

## 📈 Monitoring Access

Grafana:
kubectl port-forward -n monitoring svc/grafana 3000:80  

Prometheus:
kubectl port-forward -n monitoring svc/prometheus-server 9090:80  

---

## 🧪 Example Requests

curl http://localhost:8081/hello  
curl http://localhost:8081/health  
curl http://localhost:8081/notes  
curl -X POST http://localhost:8081/notes/test  

---

## 🧱 Architecture

User  
↓  
NodePort / Kubernetes Service  
↓  
FastAPI  
↓  
Redis  
↓  
Prometheus  
↓  
Grafana  

---

## 💡 Key Concepts

- CI/CD with GitHub Actions  
- Docker image versioning (SHA)  
- Kubernetes + Helm  
- Health checks  
- Monitoring  

---

## 📌 Future Improvements

- Ingress  
- Persistent storage  
- Alerting  
- Terraform  
- Cloud deployment  
