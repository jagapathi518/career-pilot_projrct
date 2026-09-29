"""Careers API endpoints."""

from typing import Optional
from uuid import UUID

from fastapi import APIRouter, Depends, Query, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.security import get_current_user

router = APIRouter()


@router.get("/")
async def list_careers(
    category: Optional[str] = None,
    search: Optional[str] = None,
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
):
    """List all careers with filtering and pagination."""
    # Will be implemented in Phase 5
    return {"careers": [], "total": 0, "page": page, "page_size": page_size}


@router.get("/categories")
async def list_career_categories(db: AsyncSession = Depends(get_db)):
    """List all career categories."""
    return {"categories": []}


@router.get("/{career_id}")
async def get_career(career_id: UUID, db: AsyncSession = Depends(get_db)):
    """Get career details by ID."""
    raise HTTPException(status_code=404, detail="Career not found")


@router.get("/{career_id}/roadmap")
async def get_career_roadmap(career_id: UUID, db: AsyncSession = Depends(get_db)):
    """Get career roadmap steps."""
    return {"career_id": str(career_id), "steps": []}


@router.get("/{career_id}/exams")
async def get_career_exams(career_id: UUID, db: AsyncSession = Depends(get_db)):
    """Get entrance exams for a career."""
    return {"career_id": str(career_id), "exams": []}


@router.get("/{career_id}/courses")
async def get_career_courses(career_id: UUID, db: AsyncSession = Depends(get_db)):
    """Get courses for a career."""
    return {"career_id": str(career_id), "courses": []}
