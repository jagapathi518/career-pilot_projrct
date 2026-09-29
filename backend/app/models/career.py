"""CareerPilot - SQLAlchemy Models: Career & Related Entities"""

import uuid
from datetime import datetime, timezone

from sqlalchemy import (
    String, Text, Boolean, DateTime, Integer, Float, ForeignKey, JSON, UniqueConstraint
)
from sqlalchemy.dialects.postgresql import UUID, TSVECTOR
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class CareerCategory(Base):
    """Career category (e.g., Technology, Healthcare, Law)."""
    __tablename__ = "career_categories"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    slug: Mapped[str] = mapped_column(String(120), unique=True, nullable=False, index=True)
    description: Mapped[str] = mapped_column(Text, nullable=False, default="")
    icon: Mapped[str | None] = mapped_column(String(50), nullable=True)
    display_order: Mapped[int] = mapped_column(Integer, default=0)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    # Relationships
    careers: Mapped[list["Career"]] = relationship(back_populates="category")


class Career(Base):
    """A career path (e.g., Doctor, Software Developer, Chartered Accountant)."""
    __tablename__ = "careers"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    slug: Mapped[str] = mapped_column(String(200), unique=True, nullable=False, index=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    overview: Mapped[str] = mapped_column(Text, nullable=False, default="")
    category_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("career_categories.id"), nullable=False, index=True
    )

    # Detailed fields
    what_professionals_do: Mapped[str] = mapped_column(Text, nullable=False, default="")
    who_may_enjoy: Mapped[str] = mapped_column(Text, nullable=False, default="")
    education_pathway: Mapped[str] = mapped_column(Text, nullable=False, default="")
    eligibility: Mapped[str] = mapped_column(Text, nullable=False, default="")
    duration: Mapped[str] = mapped_column(Text, nullable=False, default="")
    cost_info: Mapped[str | None] = mapped_column(Text, nullable=True)
    government_pathway: Mapped[str | None] = mapped_column(Text, nullable=True)
    private_pathway: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Publishing
    is_published: Mapped[bool] = mapped_column(Boolean, default=False, index=True)
    published_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    published_by: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), nullable=True)

    # Full-text search
    search_vector: Mapped[str | None] = mapped_column(TSVECTOR, nullable=True)

    # Stats
    view_count: Mapped[int] = mapped_column(Integer, default=0)
    bookmark_count: Mapped[int] = mapped_column(Integer, default=0)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc)
    )

    # Relationships
    category: Mapped["CareerCategory"] = relationship(back_populates="careers")
    skills: Mapped[list["CareerSkill"]] = relationship(back_populates="career", cascade="all, delete-orphan")
    pros: Mapped[list["CareerPro"]] = relationship(back_populates="career", cascade="all, delete-orphan")
    cons: Mapped[list["CareerCon"]] = relationship(back_populates="career", cascade="all, delete-orphan")
    challenges: Mapped[list["CareerChallenge"]] = relationship(back_populates="career", cascade="all, delete-orphan")
    work_environments: Mapped[list["CareerWorkEnvironment"]] = relationship(back_populates="career", cascade="all, delete-orphan")
    progression_steps: Mapped[list["CareerProgressionStep"]] = relationship(back_populates="career", cascade="all, delete-orphan", order_by="CareerProgressionStep.order")
    roadmap_steps: Mapped[list["CareerRoadmapStep"]] = relationship(back_populates="career", cascade="all, delete-orphan", order_by="CareerRoadmapStep.order")
    eligibility_rules: Mapped[list["CareerEligibility"]] = relationship(back_populates="career", cascade="all, delete-orphan")
    career_interests: Mapped[list["CareerInterest"]] = relationship(back_populates="career", cascade="all, delete-orphan")
    career_exams: Mapped[list["CareerExam"]] = relationship(back_populates="career", cascade="all, delete-orphan")
    career_courses: Mapped[list["CareerCourse"]] = relationship(back_populates="career", cascade="all, delete-orphan")
    career_institutions: Mapped[list["CareerInstitution"]] = relationship(back_populates="career", cascade="all, delete-orphan")
    faqs: Mapped[list["CareerFAQ"]] = relationship(back_populates="career", cascade="all, delete-orphan")
    sources: Mapped[list["CareerSource"]] = relationship(back_populates="career", cascade="all, delete-orphan")
    related_from: Mapped[list["RelatedCareer"]] = relationship(
        back_populates="career_from", foreign_keys="RelatedCareer.career_id", cascade="all, delete-orphan"
    )


class CareerSkill(Base):
    """Skills required or developed in a career."""
    __tablename__ = "career_skills"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    career_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("careers.id", ondelete="CASCADE"), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    skill_type: Mapped[str] = mapped_column(String(20), nullable=False, default="required")  # required, developed
    career: Mapped["Career"] = relationship(back_populates="skills")


class CareerPro(Base):
    """Advantages/pros of a career."""
    __tablename__ = "career_pros"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    career_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("careers.id", ondelete="CASCADE"), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    display_order: Mapped[int] = mapped_column(Integer, default=0)
    career: Mapped["Career"] = relationship(back_populates="pros")


class CareerCon(Base):
    """Disadvantages/cons of a career."""
    __tablename__ = "career_cons"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    career_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("careers.id", ondelete="CASCADE"), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    display_order: Mapped[int] = mapped_column(Integer, default=0)
    career: Mapped["Career"] = relationship(back_populates="cons")


class CareerChallenge(Base):
    """Challenges in a career."""
    __tablename__ = "career_challenges"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    career_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("careers.id", ondelete="CASCADE"), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    display_order: Mapped[int] = mapped_column(Integer, default=0)
    career: Mapped["Career"] = relationship(back_populates="challenges")


class CareerWorkEnvironment(Base):
    """Work environments for a career."""
    __tablename__ = "career_work_environments"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    career_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("careers.id", ondelete="CASCADE"), nullable=False)
    environment: Mapped[str] = mapped_column(String(100), nullable=False)
    career: Mapped["Career"] = relationship(back_populates="work_environments")


class CareerProgressionStep(Base):
    """Career progression stages (Junior -> Senior -> Lead)."""
    __tablename__ = "career_progression_steps"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    career_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("careers.id", ondelete="CASCADE"), nullable=False)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False, default="")
    typical_years: Mapped[str | None] = mapped_column(String(50), nullable=True)
    order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    career: Mapped["Career"] = relationship(back_populates="progression_steps")


class CareerRoadmapStep(Base):
    """Step-by-step roadmap for reaching a career."""
    __tablename__ = "career_roadmap_steps"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    career_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("careers.id", ondelete="CASCADE"), nullable=False)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False, default="")
    education_level: Mapped[str | None] = mapped_column(String(50), nullable=True)
    is_optional: Mapped[bool] = mapped_column(Boolean, default=False)
    details: Mapped[str | None] = mapped_column(Text, nullable=True)
    order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    career: Mapped["Career"] = relationship(back_populates="roadmap_steps")


class CareerEligibility(Base):
    """Eligibility rules for a career based on education level."""
    __tablename__ = "career_eligibility"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    career_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("careers.id", ondelete="CASCADE"), nullable=False)
    education_level: Mapped[str] = mapped_column(String(50), nullable=False)
    required_stream: Mapped[str | None] = mapped_column(String(100), nullable=True)
    required_subjects: Mapped[list | None] = mapped_column(JSON, nullable=True)
    min_percentage: Mapped[float | None] = mapped_column(Float, nullable=True)
    additional_requirements: Mapped[str | None] = mapped_column(Text, nullable=True)
    career: Mapped["Career"] = relationship(back_populates="eligibility_rules")


class CareerInterest(Base):
    """Mapping careers to interest areas for matching."""
    __tablename__ = "career_interests"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    career_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("careers.id", ondelete="CASCADE"), nullable=False)
    interest: Mapped[str] = mapped_column(String(100), nullable=False)
    relevance_score: Mapped[float] = mapped_column(Float, default=1.0)
    career: Mapped["Career"] = relationship(back_populates="career_interests")

    __table_args__ = (UniqueConstraint("career_id", "interest", name="uq_career_interest"),)


class CareerFAQ(Base):
    """Frequently asked questions for a career."""
    __tablename__ = "career_faqs"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    career_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("careers.id", ondelete="CASCADE"), nullable=False)
    question: Mapped[str] = mapped_column(Text, nullable=False)
    answer: Mapped[str] = mapped_column(Text, nullable=False)
    display_order: Mapped[int] = mapped_column(Integer, default=0)
    career: Mapped["Career"] = relationship(back_populates="faqs")


class RelatedCareer(Base):
    """Related careers linkage."""
    __tablename__ = "related_careers"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    career_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("careers.id", ondelete="CASCADE"), nullable=False)
    related_career_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("careers.id", ondelete="CASCADE"), nullable=False)
    career_from: Mapped["Career"] = relationship(back_populates="related_from", foreign_keys=[career_id])

    __table_args__ = (UniqueConstraint("career_id", "related_career_id", name="uq_related_career"),)
