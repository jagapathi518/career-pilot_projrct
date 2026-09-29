"""Bookmarks API endpoints."""

from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.security import get_current_user

router = APIRouter()


@router.get("/")
async def list_bookmarks(
    current_user: dict = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """List user's bookmarks."""
    return {"bookmarks": []}


@router.post("/")
async def create_bookmark(
    current_user: dict = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Create a bookmark."""
    return {"message": "Bookmark created"}


@router.delete("/{bookmark_id}")
async def delete_bookmark(
    bookmark_id: UUID,
    current_user: dict = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Delete a bookmark."""
    return {"message": "Bookmark deleted"}
