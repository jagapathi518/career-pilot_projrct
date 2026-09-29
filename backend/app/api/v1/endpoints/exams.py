"""Exams API endpoints."""

from typing import Optional
from uuid import UUID

from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db

router = APIRouter()


@router.get("/")
async def list_exams(
    search: Optional[str] = None,
    career_id: Optional[UUID] = None,
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
):
    """List entrance exams with filtering and pagination."""
    return {"exams": [], "total": 0, "page": page, "page_size": page_size}


@router.get("/{exam_id}")
async def get_exam(exam_id: UUID, db: AsyncSession = Depends(get_db)):
    """Get exam details."""
    raise HTTPException(status_code=404, detail="Exam not found")
