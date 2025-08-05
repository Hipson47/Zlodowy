# Zlodowy - Full-Stack AI Chat Application

A modern full-stack application featuring a Next.js frontend and FastAPI backend with OpenAI GPT-4 integration.

## 🏗️ Architecture

- **Frontend**: Next.js 14 + TypeScript + Tailwind CSS
- **Backend**: FastAPI + Python 3.11 + OpenAI GPT-4
- **Infrastructure**: Docker + Kubernetes
- **CI/CD**: GitHub Actions

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- Node.js 18+
- Python 3.11+
- kubectl (for Kubernetes deployment)

### Development Setup

1. **Clone and setup**:
```bash
git clone <repository-url>
cd Zlodowy
```

2. **Environment setup**:
```bash
# Copy environment files
cp frontend/.env.example frontend/.env.local
cp backend/.env.example backend/.env
```

3. **Run with Docker Compose**:
```bash
docker-compose up --build
```

4. **Access the application**:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

### Local Development

**Frontend**:
```bash
cd frontend
npm install
npm run dev
```

**Backend**:
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## 🧪 Testing

```bash
# Frontend tests
cd frontend && npm test

# Backend tests
cd backend && pytest
```

## 🐳 Docker

Build images:
```bash
docker build -t zlodowy-frontend ./frontend
docker build -t zlodowy-backend ./backend
```

## ☸️ Kubernetes

Deploy to Kubernetes:
```bash
kubectl apply -f infra/k8s/
```

## 📁 Project Structure

```
Zlodowy/
├── frontend/                 # Next.js application
│   ├── src/
│   ├── public/
│   ├── Dockerfile
│   └── package.json
├── backend/                  # FastAPI application
│   ├── app/
│   ├── tests/
│   ├── Dockerfile
│   └── requirements.txt
├── infra/                    # Infrastructure files
│   └── k8s/                 # Kubernetes manifests
├── .github/                  # GitHub Actions workflows
│   └── workflows/
└── docker-compose.yml        # Local development
```

## 🔧 Configuration

### Environment Variables

**Frontend** (`.env.local`):
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

**Backend** (`.env`):
```
OPENAI_API_KEY=your_openai_api_key
CORS_ORIGINS=http://localhost:3000
```

## 📝 API Endpoints

- `POST /chat` - Chat with OpenAI GPT-4
- `GET /health` - Health check
- `GET /docs` - API documentation (Swagger UI)

## 🤝 Contributing

1. Follow the coding standards defined in `.cursorrules`
2. Run linting and tests before committing
3. Use conventional commit messages

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.