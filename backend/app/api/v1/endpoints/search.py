"""Global Search API endpoints."""

from typing import Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db

router = APIRouter()


@router.get("/")
async def global_search(
    q: str = Query(..., min_length=2, max_length=200),
    type: Optional[str] = Query(None, regex="^(careers|exams|courses|institutions)$"),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=50),
    db: AsyncSession = Depends(get_db),
):
    """Global search across careers, exams, courses, and institutions."""
    return {
        "query": q,
        "results": [],
        "total": 0,
        "page": page,
        "page_size": page_size,
    }


@router.get("/suggestions")
async def search_suggestions(
    q: str = Query(..., min_length=2, max_length=100),
    db: AsyncSession = Depends(get_db),
):
    """Get search autocomplete suggestions."""
    return {"suggestions": []}
