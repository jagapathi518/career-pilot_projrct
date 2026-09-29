"""CareerPilot - SQLAlchemy Models: Exam, Course, Institution"""

import uuid
from datetime import datetime, timezone

from sqlalchemy import (
    String, Text, Boolean, DateTime, Integer, Float, ForeignKey, JSON, UniqueConstraint
)
from sqlalchemy.dialects.postgresql import UUID, TSVECTOR
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


# ============================================
# Entrance Exams
# ============================================

class EntranceExam(Base):
    """Entrance examination (e.g., NEET, JEE, CLAT, UPSC)."""
    __tablename__ = "entrance_exams"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    slug: Mapped[str] = mapped_column(String(200), unique=True, nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    purpose: Mapped[str] = mapped_column(Text, nullable=False, default="")
    conducting_authority: Mapped[str] = mapped_column(String(300), nullable=False, default="")
    eligibility: Mapped[str] = mapped_column(Text, nullable=False, default="")
    education_requirement: Mapped[str] = mapped_column(Text, nullable=False, default="")
    subjects: Mapped[list | None] = mapped_column(JSON, nullable=True, default=list)
    approximate_stage: Mapped[str] = mapped_column(String(200), nullable=False, default="")
    application_overview: Mapped[str | None] = mapped_column(Text, nullable=True)
    official_website: Mapped[str | None] = mapped_column(String(500), nullable=True)

    is_published: Mapped[bool] = mapped_column(Boolean, default=False, index=True)
    view_count: Mapped[int] = mapped_column(Integer, default=0)
    search_vector: Mapped[str | None] = mapped_column(TSVECTOR, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc)
    )

    # Relationships
    exam_sources: Mapped[list["ExamSource"]] = relationship(back_populates="exam", cascade="all, delete-orphan")
    career_exams: Mapped[list["CareerExam"]] = relationship(back_populates="exam", cascade="all, delete-orphan")
    course_exams: Mapped[list["CourseExam"]] = relationship(back_populates="exam", cascade="all, delete-orphan")


class ExamSource(Base):
    """Sources for exam information."""
    __tablename__ = "exam_sources"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    exam_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("entrance_exams.id", ondelete="CASCADE"), nullable=False)
    source_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("sources.id", ondelete="CASCADE"), nullable=False)
    exam: Mapped["EntranceExam"] = relationship(back_populates="exam_sources")
    source: Mapped["Source"] = relationship()


# ============================================
# Courses
# ============================================

class Course(Base):
    """Educational course/degree (e.g., MBBS, B.Tech, LLB)."""
    __tablename__ = "courses"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    slug: Mapped[str] = mapped_column(String(200), unique=True, nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    field: Mapped[str] = mapped_column(String(100), nullable=False, default="")
    description: Mapped[str] = mapped_column(Text, nullable=False, default="")
    eligibility: Mapped[str] = mapped_column(Text, nullable=False, default="")
    duration: Mapped[str] = mapped_column(String(100), nullable=False, default="")
    subjects: Mapped[list | None] = mapped_column(JSON, nullable=True, default=list)
    skills: Mapped[list | None] = mapped_column(JSON, nullable=True, default=list)
    career_opportunities: Mapped[list | None] = mapped_column(JSON, nullable=True, default=list)
    approximate_cost: Mapped[str | None] = mapped_column(Text, nullable=True)
    institution_type: Mapped[str | None] = mapped_column(String(100), nullable=True)

    is_published: Mapped[bool] = mapped_column(Boolean, default=False, index=True)
    view_count: Mapped[int] = mapped_column(Integer, default=0)
    search_vector: Mapped[str | None] = mapped_column(TSVECTOR, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc)
    )

    # Relationships
    course_sources: Mapped[list["CourseSource"]] = relationship(back_populates="course", cascade="all, delete-orphan")
    career_courses: Mapped[list["CareerCourse"]] = relationship(back_populates="course", cascade="all, delete-orphan")
    course_exams: Mapped[list["CourseExam"]] = relationship(back_populates="course", cascade="all, delete-orphan")
    institution_courses: Mapped[list["InstitutionCourse"]] = relationship(back_populates="course", cascade="all, delete-orphan")


class CourseSource(Base):
    """Sources for course information."""
    __tablename__ = "course_sources"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    course_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("courses.id", ondelete="CASCADE"), nullable=False)
    source_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("sources.id", ondelete="CASCADE"), nullable=False)
    course: Mapped["Course"] = relationship(back_populates="course_sources")
    source: Mapped["Source"] = relationship()


class CourseExam(Base):
    """Link between courses and entrance exams."""
    __tablename__ = "course_exams"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    course_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("courses.id", ondelete="CASCADE"), nullable=False)
    exam_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("entrance_exams.id", ondelete="CASCADE"), nullable=False)
    course: Mapped["Course"] = relationship(back_populates="course_exams")
    exam: Mapped["EntranceExam"] = relationship(back_populates="course_exams")

    __table_args__ = (UniqueConstraint("course_id", "exam_id", name="uq_course_exam"),)


# ============================================
# Institutions
# ============================================

class Institution(Base):
    """Educational institution."""
    __tablename__ = "institutions"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    slug: Mapped[str] = mapped_column(String(200), unique=True, nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(300), nullable=False)
    location: Mapped[str] = mapped_column(String(200), nullable=False, default="")
    type: Mapped[str] = mapped_column(String(100), nullable=False, default="")  # university, college, institute, etc.
    admission_route: Mapped[str | None] = mapped_column(Text, nullable=True)
    official_website: Mapped[str | None] = mapped_column(String(500), nullable=True)

    is_published: Mapped[bool] = mapped_column(Boolean, default=False, index=True)
    view_count: Mapped[int] = mapped_column(Integer, default=0)
    last_verified: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    search_vector: Mapped[str | None] = mapped_column(TSVECTOR, nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc)
    )

    # Relationships
    institution_sources: Mapped[list["InstitutionSource"]] = relationship(back_populates="institution", cascade="all, delete-orphan")
    institution_courses: Mapped[list["InstitutionCourse"]] = relationship(back_populates="institution", cascade="all, delete-orphan")
    career_institutions: Mapped[list["CareerInstitution"]] = relationship(back_populates="institution", cascade="all, delete-orphan")


class InstitutionSource(Base):
    """Sources for institution information."""
    __tablename__ = "institution_sources"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    institution_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("institutions.id", ondelete="CASCADE"), nullable=False)
    source_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("sources.id", ondelete="CASCADE"), nullable=False)
    institution: Mapped["Institution"] = relationship(back_populates="institution_sources")
    source: Mapped["Source"] = relationship()


class InstitutionCourse(Base):
    """Link between institutions and courses."""
    __tablename__ = "institution_courses"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    institution_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("institutions.id", ondelete="CASCADE"), nullable=False)
    course_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("courses.id", ondelete="CASCADE"), nullable=False)
    institution: Mapped["Institution"] = relationship(back_populates="institution_courses")
    course: Mapped["Course"] = relationship(back_populates="institution_courses")

    __table_args__ = (UniqueConstraint("institution_id", "course_id", name="uq_institution_course"),)


# ============================================
# Cross-entity Links (Career ↔ Exam/Course/Institution)
# ============================================

class CareerExam(Base):
    """Link between careers and entrance exams."""
    __tablename__ = "career_exams"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    career_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("careers.id", ondelete="CASCADE"), nullable=False)
    exam_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("entrance_exams.id", ondelete="CASCADE"), nullable=False)
    is_mandatory: Mapped[bool] = mapped_column(Boolean, default=False)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    career: Mapped["Career"] = relationship(back_populates="career_exams")
    exam: Mapped["EntranceExam"] = relationship(back_populates="career_exams")

    __table_args__ = (UniqueConstraint("career_id", "exam_id", name="uq_career_exam"),)


class CareerCourse(Base):
    """Link between careers and courses."""
    __tablename__ = "career_courses"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    career_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("careers.id", ondelete="CASCADE"), nullable=False)
    course_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("courses.id", ondelete="CASCADE"), nullable=False)
    is_primary: Mapped[bool] = mapped_column(Boolean, default=False)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    career: Mapped["Career"] = relationship(back_populates="career_courses")
    course: Mapped["Course"] = relationship(back_populates="career_courses")

    __table_args__ = (UniqueConstraint("career_id", "course_id", name="uq_career_course"),)


class CareerInstitution(Base):
    """Link between careers and institutions."""
    __tablename__ = "career_institutions"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    career_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("careers.id", ondelete="CASCADE"), nullable=False)
    institution_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("institutions.id", ondelete="CASCADE"), nullable=False)

    career: Mapped["Career"] = relationship(back_populates="career_institutions")
    institution: Mapped["Institution"] = relationship(back_populates="career_institutions")

    __table_args__ = (UniqueConstraint("career_id", "institution_id", name="uq_career_institution"),)
