
# 🧭 CareerPilot

**Career Discovery & Roadmap Platform for Students and Young Professionals**

CareerPilot is a structured career decision-support platform that helps users discover career paths based on their education, interests, skills, preferences, and goals — across technology, healthcare, law, education, government, sports, arts, media, business, aviation, agriculture, skilled trades, science, design, and more.

---

## 🎯 Problem Statement

Students and young professionals face overwhelming career choices without structured guidance. Existing solutions either:
- Push everyone toward technology careers
- Provide generic AI chatbot answers without verified information
- Lack structured, verifiable career data
- Don't provide actionable step-by-step roadmaps

## 💡 Solution

CareerPilot provides:
- **Structured career discovery** based on user profiles
- **Verified career information** with source tracking
- **Step-by-step roadmaps** adapted to the user's education level
- **Entrance exam explorer** with official source links
- **Course & institution explorer** with verified data
- **AI career assistant** grounded in structured data (not hallucination)
- **Career comparison** tools for informed decision-making
- **Personal roadmap tracking** with progress visualization

---

## 🏗️ Architecture

```
careerpilot/
├── frontend/          # Next.js 15 + TypeScript + Tailwind CSS + shadcn/ui
├── backend/           # FastAPI + SQLAlchemy + Pydantic
│   └── app/
│       ├── api/       # REST API endpoints
│       ├── core/      # Config, DB, security
│       ├── models/    # SQLAlchemy models
│       ├── schemas/   # Pydantic schemas
│       ├── services/  # Business logic
│       ├── repositories/  # Data access layer
│       ├── ai/        # AI/LLM integration
│       └── auth/      # Authentication
├── database/
│   ├── migrations/    # Alembic migrations
│   └── seeds/         # Seed data
└── docs/              # Documentation
```

## 🛠️ Technology Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Next.js, React, TypeScript, Tailwind CSS, shadcn/ui |
| State Management | Zustand, TanStack Query |
| Forms | React Hook Form, Zod |
| Charts | Recharts |
| Animations | Motion |
| Backend | Python, FastAPI, Pydantic |
| Database | PostgreSQL, SQLAlchemy, Alembic |
| Authentication | Supabase Auth |
| Storage | Supabase Storage |
| AI | OpenAI API (via backend) |
| Testing | Vitest, Playwright, Pytest |

---

## 🚀 Local Setup

### Prerequisites

- Node.js 18+
- Python 3.11+
- PostgreSQL 15+
- Supabase account

### 1. Clone & Install

```bash
git clone <repo-url>
cd careerpilot

# Frontend
cd frontend
cp .env.example .env.local
npm install

# Backend
cd ../backend
cp .env.example .env
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Environment Variables

Copy `.env.example` to `.env` and fill in your values. See [Environment Variables](#environment-variables) below.

### 3. Database Setup

```bash
# Create the database
createdb careerpilot

# Run migrations
cd backend
alembic upgrade head

# Seed development data
python -m database.seeds.seed_data
```

### 4. Run Development Servers

```bash
# Terminal 1 — Backend
cd backend
uvicorn app.main:app --reload --port 8000

# Terminal 2 — Frontend
cd frontend
npm run dev
```

Frontend: http://localhost:3000
Backend API: http://localhost:8000
API Docs: http://localhost:8000/docs

---

## 🔐 Environment Variables

| Variable | Description | Where |
|----------|-------------|-------|
| `DATABASE_URL` | PostgreSQL connection (async) | Backend |
| `SUPABASE_URL` | Supabase project URL | Both |
| `SUPABASE_ANON_KEY` | Supabase anonymous key | Both |
| `SUPABASE_SERVICE_ROLE_KEY` | Supabase service role key | Backend only |
| `SUPABASE_JWT_SECRET` | JWT secret for token verification | Backend only |
| `AI_API_KEY` | OpenAI API key | Backend only |
| `NEXT_PUBLIC_APP_URL` | Frontend URL | Frontend |
| `NEXT_PUBLIC_API_URL` | Backend API URL | Frontend |

> ⚠️ Never commit `.env` files. Only `.env.example` is tracked.

---

## 🧪 Testing

```bash
# Frontend unit/component tests
cd frontend && npm run test

# Backend API tests
cd backend && pytest

# End-to-end tests
cd frontend && npx playwright test
```

---

## 📦 Deployment

| Component | Platform |
|-----------|----------|
| Frontend | Vercel |
| Backend | Render / Railway / AWS |
| Database | Supabase / AWS RDS |

---

## 📸 Screenshots

*Screenshots will be added as the application is built.*

---

## 🗺️ Future Roadmap

- [ ] OAuth providers (Google, GitHub)
- [ ] Mobile application
- [ ] Multi-language support
- [ ] Dedicated search engine (Elasticsearch/Meilisearch)
- [ ] Career mentorship connections
- [ ] Resume builder integration
- [ ] Interview preparation module
- [ ] Salary data integration (with clear sourcing)
- [ ] Community forums

---

## 📄 Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [API Reference](docs/API.md)
- [Database Schema](docs/DATABASE.md)
- [Contributing](docs/CONTRIBUTING.md)

---

## 📝 License

MIT

---

*CareerPilot — Helping you discover what's possible, one career at a time.*

