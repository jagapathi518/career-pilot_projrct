"""CareerPilot Backend - API v1 Router"""

from fastapi import APIRouter

from app.api.v1.endpoints import health, careers, exams, courses, institutions, users, ai_assistant, bookmarks, roadmaps, career_match, search

api_router = APIRouter()

# Public routes
api_router.include_router(health.router, prefix="/health", tags=["Health"])
api_router.include_router(careers.router, prefix="/careers", tags=["Careers"])
api_router.include_router(exams.router, prefix="/exams", tags=["Exams"])
api_router.include_router(courses.router, prefix="/courses", tags=["Courses"])
api_router.include_router(institutions.router, prefix="/institutions", tags=["Institutions"])
api_router.include_router(search.router, prefix="/search", tags=["Search"])

# Authenticated routes
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(career_match.router, prefix="/career-match", tags=["Career Match"])
api_router.include_router(bookmarks.router, prefix="/bookmarks", tags=["Bookmarks"])
api_router.include_router(roadmaps.router, prefix="/roadmaps", tags=["Roadmaps"])
api_router.include_router(ai_assistant.router, prefix="/ai", tags=["AI Assistant"])
