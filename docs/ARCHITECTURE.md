# CareerPilot — Architecture

## System Architecture

```
┌────────────────────────────────────────────────────┐
│                     Client                          │
│  Next.js 16 (App Router, Server Components, RSC)   │
│  React + TypeScript + Tailwind + shadcn/ui          │
│  Zustand (state) + TanStack Query (server state)    │
└────────────────────────┬───────────────────────────┘
                         │ HTTPS
┌────────────────────────▼───────────────────────────┐
│                  Supabase Auth                      │
│  JWT tokens, email/password, session management     │
└────────────────────────┬───────────────────────────┘
                         │ JWT Bearer
┌────────────────────────▼───────────────────────────┐
│              FastAPI Backend (Python)                │
│  REST API + Pydantic validation + rate limiting     │
│  ┌──────────┐ ┌───────────┐ ┌────────────────┐     │
│  │ API Layer│ │ Services  │ │ Repositories   │     │
│  └──────────┘ └───────────┘ └────────────────┘     │
│  ┌──────────┐ ┌───────────┐ ┌────────────────┐     │
│  │ Auth     │ │ AI Engine │ │ Career Matcher │     │
│  └──────────┘ └───────────┘ └────────────────┘     │
└────────────────────────┬───────────────────────────┘
                         │ SQL (async)
┌────────────────────────▼───────────────────────────┐
│              PostgreSQL (Supabase)                   │
│  30+ normalized tables, UUIDs, full-text search     │
│  Alembic migrations                                  │
└─────────────────────────────────────────────────────┘
```

## Data Flow

1. **User Auth**: Browser → Supabase Auth → JWT → Backend verifies
2. **API Requests**: Frontend → FastAPI → SQLAlchemy → PostgreSQL
3. **AI Queries**: Frontend → FastAPI → RAG Pipeline → LLM API → Response with citations
4. **Career Matching**: User Profile → Matching Engine → Scored Results with explanations

## Directory Structure

```
careerpilot/
├── frontend/                    # Next.js 16 app
│   └── src/
│       ├── app/                 # App Router pages
│       ├── components/          # React components
│       │   ├── layout/          # Navbar, Footer, Sidebar
│       │   └── ui/              # shadcn/ui components
│       ├── lib/                 # Utilities, API client, Supabase
│       ├── providers/           # React context providers
│       ├── stores/              # Zustand stores
│       └── types/               # TypeScript type definitions
├── backend/                     # FastAPI app
│   ├── app/
│   │   ├── api/v1/endpoints/    # REST endpoints
│   │   ├── core/                # Config, DB, Security
│   │   ├── models/              # SQLAlchemy ORM models
│   │   ├── schemas/             # Pydantic request/response schemas
│   │   ├── services/            # Business logic layer
│   │   ├── repositories/        # Data access layer
│   │   ├── ai/                  # LLM integration + RAG
│   │   └── auth/                # Auth utilities
│   └── tests/                   # Pytest tests
├── database/
│   ├── migrations/              # Alembic migrations
│   └── seeds/                   # Seed data scripts
└── docs/                        # Documentation
```

## Key Design Decisions

1. **Server Components by default**: Pages use RSC, client components only where interactivity is needed
2. **API-first**: All data flows through the FastAPI backend, never direct DB from frontend
3. **Structured over AI**: Career data comes from the database first, AI augments with explanations
4. **Source verification**: Every factual claim must be linkable to a source
5. **RBAC**: Role-based access control with admin/user roles via Supabase JWT claims
