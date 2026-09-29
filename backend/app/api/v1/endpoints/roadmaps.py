"""Roadmaps API endpoints."""

from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.security import get_current_user

router = APIRouter()


@router.get("/")
async def list_user_roadmaps(
    current_user: dict = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """List user's career roadmaps."""
    return {"roadmaps": []}


@router.post("/")
async def create_roadmap(
    current_user: dict = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Create a personal career roadmap."""
    return {"message": "Roadmap created"}


@router.get("/{roadmap_id}")
async def get_roadmap(
    roadmap_id: UUID,
    current_user: dict = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Get roadmap details with progress."""
    raise HTTPException(status_code=404, detail="Roadmap not found")


@router.patch("/{roadmap_id}/steps/{step_id}")
async def update_roadmap_step(
    roadmap_id: UUID,
    step_id: UUID,
    current_user: dict = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Update roadmap step progress."""
    return {"message": "Step updated"}
