.PHONY: help install test lint format clean docker-build docker-run k8s-deploy k8s-delete

# Default target
help:
	@echo "Available commands:"
	@echo "  install      - Install all dependencies"
	@echo "  test         - Run all tests"
	@echo "  lint         - Run linting for both frontend and backend"
	@echo "  format       - Format code for both frontend and backend"
	@echo "  clean        - Clean build artifacts"
	@echo "  docker-build - Build Docker images"
	@echo "  docker-run   - Run with Docker Compose"
	@echo "  k8s-deploy   - Deploy to Kubernetes"
	@echo "  k8s-delete   - Delete Kubernetes resources"

# Install dependencies
install:
	@echo "Installing frontend dependencies..."
	cd frontend && npm install
	@echo "Installing backend dependencies..."
	cd backend && pip install -r requirements.txt

# Run tests
test:
	@echo "Running frontend tests..."
	cd frontend && npm test
	@echo "Running backend tests..."
	cd backend && pytest

# Run linting
lint:
	@echo "Linting frontend..."
	cd frontend && npm run lint
	@echo "Linting backend..."
	cd backend && flake8 app/ tests/
	cd backend && mypy app/ --ignore-missing-imports

# Format code
format:
	@echo "Formatting frontend..."
	cd frontend && npx prettier --write .
	@echo "Formatting backend..."
	cd backend && black app/ tests/
	cd backend && isort app/ tests/

# Clean build artifacts
clean:
	@echo "Cleaning frontend..."
	cd frontend && rm -rf .next node_modules
	@echo "Cleaning backend..."
	cd backend && find . -type d -name __pycache__ -delete
	cd backend && find . -name "*.pyc" -delete
	cd backend && rm -rf .pytest_cache .mypy_cache

# Build Docker images
docker-build:
	@echo "Building Docker images..."
	docker build -t zlodowy-frontend ./frontend
	docker build -t zlodowy-backend ./backend

# Run with Docker Compose
docker-run:
	@echo "Starting services with Docker Compose..."
	docker-compose up --build

# Deploy to Kubernetes
k8s-deploy:
	@echo "Deploying to Kubernetes..."
	kubectl apply -f infra/k8s/

# Delete Kubernetes resources
k8s-delete:
	@echo "Deleting Kubernetes resources..."
	kubectl delete -f infra/k8s/

# Development helpers
dev-frontend:
	@echo "Starting frontend development server..."
	cd frontend && npm run dev

dev-backend:
	@echo "Starting backend development server..."
	cd backend && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Security checks
security-check:
	@echo "Running security checks..."
	cd frontend && npm audit
	cd backend && safety check

# Build for production
build:
	@echo "Building frontend for production..."
	cd frontend && npm run build
	@echo "Backend is ready for production deployment" 