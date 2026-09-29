"""Institutions API endpoints."""

from typing import Optional
from uuid import UUID

from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db

router = APIRouter()


@router.get("/")
async def list_institutions(
    type: Optional[str] = None,
    location: Optional[str] = None,
    search: Optional[str] = None,
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
):
    """List institutions with filtering and pagination."""
    return {"institutions": [], "total": 0, "page": page, "page_size": page_size}


@router.get("/{institution_id}")
async def get_institution(institution_id: UUID, db: AsyncSession = Depends(get_db)):
    """Get institution details."""
    raise HTTPException(status_code=404, detail="Institution not found")
