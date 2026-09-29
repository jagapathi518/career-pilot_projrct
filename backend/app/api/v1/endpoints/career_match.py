"""Career Match API endpoints."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.security import get_current_user

router = APIRouter()


@router.post("/")
async def match_careers(
    current_user: dict = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Run career matching engine based on user profile and preferences."""
    return {"matches": [], "message": "Career matching will be implemented in Phase 7"}
