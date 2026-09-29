"""AI Career Assistant API endpoints."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.security import get_current_user

router = APIRouter()


@router.post("/career-assistant")
async def career_assistant(
    current_user: dict = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """AI career assistant endpoint."""
    return {"message": "AI assistant will be implemented in Phase 11"}


@router.get("/conversations")
async def list_conversations(
    current_user: dict = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """List user's AI conversations."""
    return {"conversations": []}
