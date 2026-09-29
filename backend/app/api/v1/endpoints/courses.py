"""Courses API endpoints."""

from typing import Optional
from uuid import UUID

from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db

router = APIRouter()


@router.get("/")
async def list_courses(
    field: Optional[str] = None,
    duration: Optional[str] = None,
    search: Optional[str] = None,
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
):
    """List courses with filtering and pagination."""
    return {"courses": [], "total": 0, "page": page, "page_size": page_size}


@router.get("/{course_id}")
async def get_course(course_id: UUID, db: AsyncSession = Depends(get_db)):
    """Get course details."""
    raise HTTPException(status_code=404, detail="Course not found")
