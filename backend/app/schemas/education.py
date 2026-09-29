"""CareerPilot - Pydantic Schemas: Education (Exam, Course, Institution)"""

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field

from app.schemas.career import SourceResponse, CareerSummaryResponse


# ============================================
# Exam
# ============================================

class ExamSummaryResponse(BaseModel):
    id: UUID
    slug: str
    name: str
    conducting_authority: str
    purpose: str

    model_config = {"from_attributes": True}


class ExamDetailResponse(BaseModel):
    id: UUID
    slug: str
    name: str
    purpose: str
    conducting_authority: str
    eligibility: str
    education_requirement: str
    subjects: list[str] = Field(default_factory=list)
    approximate_stage: str
    application_overview: Optional[str] = None
    official_website: Optional[str] = None
    related_careers: list[CareerSummaryResponse] = Field(default_factory=list)
    sources: list[SourceResponse] = Field(default_factory=list)
    is_published: bool = False

    model_config = {"from_attributes": True}


class ExamListResponse(BaseModel):
    exams: list[ExamSummaryResponse]
    total: int
    page: int
    page_size: int
    total_pages: int


# ============================================
# Course
# ============================================

class CourseSummaryResponse(BaseModel):
    id: UUID
    slug: str
    name: str
    field: str
    duration: str

    model_config = {"from_attributes": True}


class CourseDetailResponse(BaseModel):
    id: UUID
    slug: str
    name: str
    field: str
    description: str
    eligibility: str
    duration: str
    subjects: list[str] = Field(default_factory=list)
    skills: list[str] = Field(default_factory=list)
    career_opportunities: list[str] = Field(default_factory=list)
    approximate_cost: Optional[str] = None
    institution_type: Optional[str] = None
    related_exams: list[ExamSummaryResponse] = Field(default_factory=list)
    related_careers: list[CareerSummaryResponse] = Field(default_factory=list)
    sources: list[SourceResponse] = Field(default_factory=list)
    is_published: bool = False

    model_config = {"from_attributes": True}


class CourseListResponse(BaseModel):
    courses: list[CourseSummaryResponse]
    total: int
    page: int
    page_size: int
    total_pages: int


# ============================================
# Institution
# ============================================

class InstitutionSummaryResponse(BaseModel):
    id: UUID
    slug: str
    name: str
    location: str
    type: str

    model_config = {"from_attributes": True}


class InstitutionDetailResponse(BaseModel):
    id: UUID
    slug: str
    name: str
    location: str
    type: str
    courses: list[CourseSummaryResponse] = Field(default_factory=list)
    admission_route: Optional[str] = None
    official_website: Optional[str] = None
    sources: list[SourceResponse] = Field(default_factory=list)
    last_verified: Optional[datetime] = None
    is_published: bool = False

    model_config = {"from_attributes": True}


class InstitutionListResponse(BaseModel):
    institutions: list[InstitutionSummaryResponse]
    total: int
    page: int
    page_size: int
    total_pages: int


# ============================================
# Bookmark
# ============================================

class BookmarkCreate(BaseModel):
    bookmark_type: str  # career, course, exam, institution
    item_id: UUID
    item_title: str
    item_slug: str

class BookmarkResponse(BaseModel):
    id: UUID
    bookmark_type: str
    item_id: UUID
    item_title: str
    item_slug: str
    created_at: datetime

    model_config = {"from_attributes": True}


# ============================================
# User Roadmap
# ============================================

class RoadmapCreate(BaseModel):
    career_id: UUID

class RoadmapStepUpdate(BaseModel):
    status: str  # not_started, in_progress, completed
    notes: Optional[str] = None

class UserRoadmapStepResponse(BaseModel):
    id: UUID
    roadmap_step_id: UUID
    step_order: int
    step_title: str
    status: str
    notes: Optional[str] = None
    completed_at: Optional[datetime] = None

    model_config = {"from_attributes": True}

class UserRoadmapResponse(BaseModel):
    id: UUID
    career_id: UUID
    career_title: str
    is_active: bool
    steps: list[UserRoadmapStepResponse] = Field(default_factory=list)
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


# ============================================
# AI Assistant
# ============================================

class AIMessageRequest(BaseModel):
    message: str
    conversation_id: Optional[UUID] = None

class AIMessageResponse(BaseModel):
    id: UUID
    role: str
    content: str
    sources: Optional[list[dict]] = None
    created_at: datetime

    model_config = {"from_attributes": True}

class AIConversationResponse(BaseModel):
    id: UUID
    title: str
    messages: list[AIMessageResponse] = Field(default_factory=list)
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


# ============================================
# Search
# ============================================

class SearchResultResponse(BaseModel):
    type: str  # career, exam, course, institution
    id: UUID
    slug: str
    title: str
    description: str

class SearchResponse(BaseModel):
    query: str
    results: list[SearchResultResponse]
    total: int
    page: int
    page_size: int
