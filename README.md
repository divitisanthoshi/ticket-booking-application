# Ticket Booking Application - DevOps Workflow

This repository contains a simple ticket booking web application built with Flask (Python) and implements a complete automated DevOps workflow using Git, Docker, Jenkins, and Kubernetes.

## Application Overview

The application allows users to book tickets for events through a web interface. It stores bookings in memory (for demonstration purposes).

## DevOps Workflow Implementation

### 1. Version Control and Branching

#### Initialize Git Repository
```bash
git init
git add .
git commit -m "Initial commit"
```

#### GitFlow Branching Strategy
- **master**: Production-ready code
- **develop**: Integration branch for features
- **feature/**: Feature branches (e.g., feature/ticket-booking)
- **release/**: Release preparation
- **hotfix/**: Hotfixes for production

Commands to set up GitFlow:
```bash
# Install git-flow if not installed
# On Windows: Download from https://github.com/nvie/gitflow/wiki/Windows

git flow init -d  # Use defaults

# Create a feature branch
git flow feature start ticket-booking

# Finish feature
git flow feature finish ticket-booking

# Create release
git flow release start v1.0.0
git flow release finish v1.0.0
```

### 2. Containerization

#### Dockerfile
The Dockerfile uses Python 3.9 slim image, installs dependencies, and runs the Flask app.

#### Build and Test Docker Image Locally
```bash
# Build the image
docker build -t ticket-booking-app .

# Run the container
docker run -p 5000:5000 ticket-booking-app

# Test the application
curl http://localhost:5000
```

### 3. Continuous Integration and Continuous Delivery (CI/CD)

#### Jenkins Setup
1. Install Jenkins and required plugins (Docker, Kubernetes, Git)
2. Create a new Pipeline job
3. Configure SCM to point to this repository
4. Set up webhooks for automatic triggering on push

#### Jenkins Pipeline (Jenkinsfile)
The pipeline includes:
- Checkout code from develop branch
- Build Docker image
- Run tests (placeholder for actual tests)
- Push image to Docker Hub
- Deploy to Kubernetes

#### Docker Hub Integration
- Create a Docker Hub account
- Set up credentials in Jenkins
- Images are tagged with build number and pushed

### 4. Deployment and Orchestration

#### Kubernetes Manifests
- **deployment.yaml**: Defines the deployment with 3 replicas for scalability
- **service.yaml**: Exposes the app via LoadBalancer

#### Deploy to Kubernetes
```bash
# Apply manifests
kubectl apply -f k8s/

# Check deployment
kubectl get pods
kubectl get services

# Scale the application
kubectl scale deployment ticket-booking-app --replicas=5
```

## Commands and Configurations

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

### Docker Commands
```bash
# Build
docker build -t ticket-booking-app .

# Run
docker run -p 5000:5000 ticket-booking-app

# Push to Docker Hub
docker tag ticket-booking-app your-username/ticket-booking-app
docker push your-username/ticket-booking-app
```

### Jenkins Configuration
- Job Type: Pipeline
- Definition: Pipeline script from SCM
- SCM: Git, Repository URL: https://github.com/your-username/ticket-booking-app.git
- Branches to build: develop
- Build Triggers: GitHub hook trigger for GITScm polling

### Kubernetes Commands
```bash
# Deploy
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

# Check status
kubectl get all

# Scale
kubectl scale deployment ticket-booking-app --replicas=5

# Logs
kubectl logs -f deployment/ticket-booking-app
```

## Pipeline Steps

1. **Checkout**: Pull latest code from develop branch
2. **Build**: Create Docker image
3. **Test**: Run unit tests inside container
4. **Push**: Upload image to Docker Hub
5. **Deploy**: Update Kubernetes deployment with new image

## Screenshots

### Application UI
- **Home Page**: Displays event cards with booking options
- **Booking Modal**: Interactive form for ticket booking
- **Dashboard**: Real-time display of booked tickets

### DevOps Workflow
- **Git Branches**: develop, master, feature branches
- **Docker Build**: Successful image creation
- **Jenkins Pipeline**: Build, test, push, deploy stages
- **Kubernetes Dashboard**: Pods, services, and scaling

## Prerequisites

- Python 3.9
- Docker
- Jenkins with Docker and Kubernetes plugins
- Kubernetes cluster (local or cloud)
- Docker Hub account
- GitHub repository

## Notes

- Replace `your-dockerhub-username` and `your-username` with actual values
- Add proper tests in `tests/` directory
- Configure webhooks in GitHub for automatic Jenkins triggers
- Set up proper secrets management for credentials

## GitHub Repository

The complete code has been pushed to: https://github.com/divitisanthoshi/ticket-booking-app

## Commands Summary

1. **Local Development**: `python app.py` → Runs on http://127.0.0.1:5000
2. **Docker Build**: `docker build -t ticket-booking-app .`
3. **Docker Run**: `docker run -p 5000:5000 ticket-booking-app`
4. **Kubernetes Deploy**: `kubectl apply -f k8s/`
5. **Scale Application**: `kubectl scale deployment ticket-booking-app --replicas=5`

The application is fully containerized, CI/CD ready, and orchestrated for production deployment.
