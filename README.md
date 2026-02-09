# 🔐 Security Scanner API

> 🚧 **Status:** Active Development

Mini-platform for URL security scanning - learning project.


## 📋 Prerequisites

- Python 3.11 or higher
- Git

---

## 🚀 Quick Start (macOS M1)

```bash
# Clone & setup
git clone https://github.com/danielabirzan/security-scanner-api.git
cd security-scanner-api

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Configure environment
cp .env.example .env

# Run development server
uvicorn app.main:app --reload

# API Docs: http://localhost:8000/docs
```

---

## 🎯 Features Roadmap

### Phase 1: Core API ✨
- [x] Project setup with FastAPI
- [x] Layered architecture (Controllers → Services → Repositories)
- [ ] PostgreSQL integration with SQLAlchemy
- [ ] Database migrations with Alembic
- [ ] RESTful API design with proper HTTP status codes

### Phase 2: Security & Authentication 🔒

### Phase 3: Scanning Feature 🔍

### Phase 4: Async Processing ⚡

### Phase 5: Containerization 🐳

### Phase 6: Orchestration ☸️

### Phase 7: Production Ready 📊

---

## 🛠️ Tech Stack

- **FastAPI** - Web framework
- **PostgreSQL** - Database
- **SQLAlchemy** - ORM
- **RabbitMQ + Celery** - Async tasks
- **Docker + Kubernetes** - Deployment

---

## 📁 Project Structure

```
security-scanner-api/
├── app/
│   ├── api/v1/          # Controllers (API endpoints)
│   ├── services/        # Business logic
│   ├── repositories/    # Data access layer
│   ├── models/          # Database models (SQLAlchemy)
│   ├── schemas/         # Pydantic schemas (validation)
│   ├── core/            # Config & dependencies
│   ├── database.py      # Database connection
│   └── main.py          # FastAPI app initialization
├── tests/               # Test suite
├── docker/              # Dockerfiles
├── kubernetes/          # K8s manifests
├── migrations/          # Alembic migrations
├── scripts/             # Utility scripts
├── requirements.txt     # Python dependencies
├── .env.example         # Environment template
└── README.md
```

---

## 🏗️ Architecture

**Layered Architecture Pattern:**

```
Client Request
      ↓
┌─────────────────┐
│   Controllers   │  ← API endpoints (HTTP handling)
└────────┬────────┘
         ↓
┌─────────────────┐
│    Services     │  ← Business logic
└────────┬────────┘
         ↓
┌─────────────────┐
│  Repositories   │  ← Data access
└────────┬────────┘
         ↓
┌─────────────────┐
│  Database (ORM) │  ← PostgreSQL
└─────────────────┘
```
---

## 🎓 Learning Goals

This project demonstrates:
- ✅ Clean Architecture (layered design)
- ✅ RESTful API design
- ✅ Async processing (Celery/RabbitMQ)
- ✅ Database design & migrations
- ✅ JWT authentication
- ✅ Containerization (Docker)
- ✅ Orchestration (Kubernetes)
- ✅ Testing & CI/CD

---

## 📖 API Documentation

Interactive docs available at:
- **Swagger UI (Interactive):** [http://localhost:8000/docs](http://localhost:8000/docs)  

- **Redoc (Read-Only, Clean Docs):** [http://localhost:8000/redoc](http://localhost:8000/redoc) 