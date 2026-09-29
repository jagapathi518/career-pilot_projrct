# CareerPilot — Database Schema

## Overview

CareerPilot uses a fully normalized PostgreSQL schema with 30+ tables.

All tables use UUID primary keys for security and distribution compatibility.

## Entity Relationship Summary

```
users ─────── profiles (1:1)
  │
  ├── bookmarks
  ├── user_roadmaps ──── user_roadmap_progress
  ├── ai_conversations ──── ai_messages
  └── notifications

career_categories ──── careers (1:N)
  │
  ├── career_skills
  ├── career_pros / career_cons / career_challenges
  ├── career_work_environments
  ├── career_progression_steps
  ├── career_roadmap_steps
  ├── career_eligibility
  ├── career_interests
  ├── career_faqs
  ├── career_sources ──── sources
  ├── career_exams ──── entrance_exams
  ├── career_courses ──── courses
  ├── career_institutions ──── institutions
  └── related_careers (self-referencing)

entrance_exams
  ├── exam_sources ──── sources
  └── course_exams ──── courses

courses
  ├── course_sources ──── sources
  └── institution_courses ──── institutions

institutions
  └── institution_sources ──── sources

sources (central verification table)
audit_logs (admin activity tracking)
```

## Key Tables

| Table | Purpose | Rows (seed) |
|-------|---------|-------------|
| `users` | User accounts | — |
| `profiles` | Onboarding data | — |
| `career_categories` | Career groupings | 10+ |
| `careers` | Career paths | 30+ |
| `entrance_exams` | Exams | 15+ |
| `courses` | Degrees/certifications | 20+ |
| `institutions` | Educational institutions | 20+ |
| `sources` | Verified sources | 50+ |
| `bookmarks` | User saved items | — |
| `user_roadmaps` | Personal career plans | — |

## Full-Text Search

The `careers`, `entrance_exams`, `courses`, and `institutions` tables include a `search_vector` column (TSVECTOR) for PostgreSQL full-text search.

## Source Verification

The `sources` table is the central truth store. Sources link to careers, exams, courses, and institutions through junction tables. Each source tracks:

- `verification_status`: verified / unverified / outdated
- `last_verified`: When it was last checked
- `verified_by`: Which admin verified it
- `source_type`: official / government / educational / industry / general
