"""CareerPilot - Pydantic Schemas: User & Profile"""

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field


# ============================================
# User Schemas
# ============================================

class UserBase(BaseModel):
    email: EmailStr
    full_name: str = ""

class UserCreate(UserBase):
    pass

class UserResponse(BaseModel):
    id: UUID
    email: str
    full_name: str
    avatar_url: Optional[str] = None
    role: str = "user"
    is_active: bool = True
    is_onboarded: bool = False
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


# ============================================
# Profile / Onboarding Schemas
# ============================================

class OnboardingData(BaseModel):
    """Full onboarding data submitted by the user."""
    education_level: Optional[str] = None
    academic_background: Optional[str] = None
    stream: Optional[str] = None
    subjects: Optional[list[str]] = Field(default_factory=list)
    interests: Optional[list[str]] = Field(default_factory=list)
    preferred_work_environments: Optional[list[str]] = Field(default_factory=list)
    work_preferences: Optional[list[str]] = Field(default_factory=list)
    budget_range: Optional[str] = None
    preferred_location: Optional[str] = None
    willing_to_relocate: Optional[bool] = None
    govt_private_preference: Optional[str] = None
    desired_course_duration: Optional[str] = None
    willing_for_entrance_exams: Optional[bool] = None
    career_goals: Optional[list[str]] = Field(default_factory=list)

class ProfileResponse(BaseModel):
    id: UUID
    user_id: UUID
    education_level: Optional[str] = None
    academic_background: Optional[str] = None
    stream: Optional[str] = None
    subjects: Optional[list[str]] = None
    interests: Optional[list[str]] = None
    preferred_work_environments: Optional[list[str]] = None
    work_preferences: Optional[list[str]] = None
    budget_range: Optional[str] = None
    preferred_location: Optional[str] = None
    willing_to_relocate: Optional[bool] = None
    govt_private_preference: Optional[str] = None
    desired_course_duration: Optional[str] = None
    willing_for_entrance_exams: Optional[bool] = None
    career_goals: Optional[list[str]] = None
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class UserWithProfile(BaseModel):
    user: UserResponse
    profile: Optional[ProfileResponse] = None
