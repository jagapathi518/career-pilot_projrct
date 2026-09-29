"""CareerPilot - SQLAlchemy Models: User & Profile"""

import uuid
from datetime import datetime, timezone

from sqlalchemy import (
    String, Text, Boolean, DateTime, ForeignKey, Enum, ARRAY, JSON
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class User(Base):
    """User account linked to Supabase Auth."""
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)
    full_name: Mapped[str] = mapped_column(String(255), nullable=False, default="")
    avatar_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    role: Mapped[str] = mapped_column(
        String(20), nullable=False, default="user", index=True
    )  # 'user' or 'admin'
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_onboarded: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    # Relationships
    profile: Mapped["Profile"] = relationship(back_populates="user", uselist=False, cascade="all, delete-orphan")
    bookmarks: Mapped[list["Bookmark"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    roadmaps: Mapped[list["UserRoadmap"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    ai_conversations: Mapped[list["AIConversation"]] = relationship(back_populates="user", cascade="all, delete-orphan")


class Profile(Base):
    """Extended user profile with onboarding data."""
    __tablename__ = "profiles"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"),
        unique=True, nullable=False
    )

    # Onboarding step 1: Education
    education_level: Mapped[str | None] = mapped_column(String(50), nullable=True)

    # Onboarding step 2: Academic background
    academic_background: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Onboarding step 3: Stream/subjects
    stream: Mapped[str | None] = mapped_column(String(100), nullable=True)
    subjects: Mapped[list | None] = mapped_column(JSON, nullable=True, default=list)

    # Onboarding step 4: Interests
    interests: Mapped[list | None] = mapped_column(JSON, nullable=True, default=list)

    # Onboarding step 5: Work environment
    preferred_work_environments: Mapped[list | None] = mapped_column(JSON, nullable=True, default=list)

    # Onboarding step 6: Work preferences
    work_preferences: Mapped[list | None] = mapped_column(JSON, nullable=True, default=list)

    # Onboarding step 7: Constraints
    budget_range: Mapped[str | None] = mapped_column(String(100), nullable=True)
    preferred_location: Mapped[str | None] = mapped_column(String(255), nullable=True)
    willing_to_relocate: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    govt_private_preference: Mapped[str | None] = mapped_column(String(50), nullable=True)
    desired_course_duration: Mapped[str | None] = mapped_column(String(50), nullable=True)
    willing_for_entrance_exams: Mapped[bool | None] = mapped_column(Boolean, nullable=True)

    # Onboarding step 8: Goals
    career_goals: Mapped[list | None] = mapped_column(JSON, nullable=True, default=list)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    # Relationships
    user: Mapped["User"] = relationship(back_populates="profile")
