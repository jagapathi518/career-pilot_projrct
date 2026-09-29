"""CareerPilot - Pydantic Schemas: Career"""

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


# ============================================
# Career Category
# ============================================

class CareerCategoryResponse(BaseModel):
    id: UUID
    name: str
    slug: str
    description: str
    icon: Optional[str] = None
    career_count: int = 0

    model_config = {"from_attributes": True}


# ============================================
# Career Summary (for lists)
# ============================================

class CareerSummaryResponse(BaseModel):
    id: UUID
    slug: str
    title: str
    description: str
    category_name: str = ""
    category_slug: str = ""

    model_config = {"from_attributes": True}


# ============================================
# Career Skill
# ============================================

class CareerSkillResponse(BaseModel):
    id: UUID
    name: str
    skill_type: str

    model_config = {"from_attributes": True}


# ============================================
# Career Progression
# ============================================

class CareerProgressionStepResponse(BaseModel):
    id: UUID
    title: str
    description: str
    order: int
    typical_years: Optional[str] = None

    model_config = {"from_attributes": True}


# ============================================
# Career Roadmap Step
# ============================================

class CareerRoadmapStepResponse(BaseModel):
    id: UUID
    title: str
    description: str
    education_level: Optional[str] = None
    is_optional: bool = False
    details: Optional[str] = None
    order: int

    model_config = {"from_attributes": True}


# ============================================
# Career FAQ
# ============================================

class CareerFAQResponse(BaseModel):
    id: UUID
    question: str
    answer: str

    model_config = {"from_attributes": True}


# ============================================
# Source
# ============================================

class SourceResponse(BaseModel):
    id: UUID
    name: str
    url: Optional[str] = None
    source_type: str
    publication_date: Optional[datetime] = None
    last_verified: Optional[datetime] = None
    verification_status: str

    model_config = {"from_attributes": True}


# ============================================
# Full Career Detail
# ============================================

class CareerDetailResponse(BaseModel):
    id: UUID
    slug: str
    title: str
    description: str
    overview: str
    category: CareerCategoryResponse
    what_professionals_do: str
    who_may_enjoy: str
    education_pathway: str
    eligibility: str
    duration: str
    cost_info: Optional[str] = None
    government_pathway: Optional[str] = None
    private_pathway: Optional[str] = None
    work_environments: list[str] = Field(default_factory=list)
    skills: list[CareerSkillResponse] = Field(default_factory=list)
    pros: list[str] = Field(default_factory=list)
    cons: list[str] = Field(default_factory=list)
    challenges: list[str] = Field(default_factory=list)
    progression_steps: list[CareerProgressionStepResponse] = Field(default_factory=list)
    roadmap_steps: list[CareerRoadmapStepResponse] = Field(default_factory=list)
    faqs: list[CareerFAQResponse] = Field(default_factory=list)
    sources: list[SourceResponse] = Field(default_factory=list)
    related_careers: list[CareerSummaryResponse] = Field(default_factory=list)
    is_published: bool = False
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


# ============================================
# Career List Response
# ============================================

class CareerListResponse(BaseModel):
    careers: list[CareerSummaryResponse]
    total: int
    page: int
    page_size: int
    total_pages: int


# ============================================
# Career Match
# ============================================

class MatchReasonResponse(BaseModel):
    type: str  # interest, skill, education, goal, work_environment, preference
    description: str

class CareerMatchResponse(BaseModel):
    career: CareerSummaryResponse
    match_score: float
    reasons: list[MatchReasonResponse]

class CareerMatchListResponse(BaseModel):
    matches: list[CareerMatchResponse]
    total: int


# ============================================
# Admin Career Create/Update
# ============================================

class CareerCreate(BaseModel):
    title: str
    slug: str
    description: str
    overview: str = ""
    category_id: UUID
    what_professionals_do: str = ""
    who_may_enjoy: str = ""
    education_pathway: str = ""
    eligibility: str = ""
    duration: str = ""
    cost_info: Optional[str] = None
    government_pathway: Optional[str] = None
    private_pathway: Optional[str] = None

class CareerUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    overview: Optional[str] = None
    category_id: Optional[UUID] = None
    what_professionals_do: Optional[str] = None
    who_may_enjoy: Optional[str] = None
    education_pathway: Optional[str] = None
    eligibility: Optional[str] = None
    duration: Optional[str] = None
    cost_info: Optional[str] = None
    government_pathway: Optional[str] = None
    private_pathway: Optional[str] = None
    is_published: Optional[bool] = None
