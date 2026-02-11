# 🔐 Security Scanner API

Mini-platform for URL security scanning with async processing.

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109+-green.svg)](https://fastapi.tiangolo.com/)

---

## 🚀 Quick Start
```bash
# Setup
git clone https://github.com/danielabirzan/security-scanner-api.git
cd security-scanner-api
python3 -m venv venv
source venv/bin/activate
make install

# Configure application
cp .env.example .env

# Run
make run
# Docs:
#    - http://localhost:8000/docs
#    -
```

---

## 🛠️ Development
```bash
make format    # Format code
make fix       # Auto-fix all issues
make lint      # Check quality
make test      # Run tests
make all       # Fix + lint + test
make help           # Show all commands
```
---

## 📁 Structure
```
app/
├── api/v1/          # Endpoints
├── services/        # Business logic
├── repositories/    # Data access
├── models/          # Database models
├── schemas/         # Validation
└── core/            # Config
```

**Architecture:** Controllers → Services → Repositories → Database

---

## 🎯 Roadmap

- [x] FastAPI setup
- [x] Code quality tools
- [ ] PostgreSQL + migrations
- [ ] Authentication (JWT)
- [ ] Scanning features
- [ ] Async tasks (Celery)
- [ ] Docker + Kubernetes

---

## 🛠️ Tech Stack

FastAPI • PostgreSQL • SQLAlchemy • RabbitMQ • Celery • Docker • Kubernetes

---

## 📖 Docs

- **API Docs:** http://localhost:8000/docs
- **Health:** http://localhost:8000/health

---

## 🧪 Testing
```bash
make test                              # All tests
pytest tests/test_scans.py            # Specific file
pytest --cov=app --cov-report=html    # Coverage report
```

## 📧 Contact

- GitHub: [@danielabirzan](https://github.com/danielabirzan)
- Email: birzandaniela@gmail.com
