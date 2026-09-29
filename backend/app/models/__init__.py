"""CareerPilot - Models Package

All models are imported here so Alembic can auto-detect them.
"""

from app.models.user import User, Profile
from app.models.career import (
    CareerCategory, Career, CareerSkill, CareerPro, CareerCon,
    CareerChallenge, CareerWorkEnvironment, CareerProgressionStep,
    CareerRoadmapStep, CareerEligibility, CareerInterest, CareerFAQ,
    RelatedCareer,
)
from app.models.education import (
    EntranceExam, ExamSource, Course, CourseSource, CourseExam,
    Institution, InstitutionSource, InstitutionCourse,
    CareerExam, CareerCourse, CareerInstitution,
)
from app.models.engagement import (
    Source, CareerSource, Bookmark, UserRoadmap, UserRoadmapProgress,
    AIConversation, AIMessage, Notification, AuditLog,
)

__all__ = [
    # User
    "User", "Profile",
    # Career
    "CareerCategory", "Career", "CareerSkill", "CareerPro", "CareerCon",
    "CareerChallenge", "CareerWorkEnvironment", "CareerProgressionStep",
    "CareerRoadmapStep", "CareerEligibility", "CareerInterest", "CareerFAQ",
    "RelatedCareer",
    # Education
    "EntranceExam", "ExamSource", "Course", "CourseSource", "CourseExam",
    "Institution", "InstitutionSource", "InstitutionCourse",
    "CareerExam", "CareerCourse", "CareerInstitution",
    # Engagement
    "Source", "CareerSource", "Bookmark", "UserRoadmap", "UserRoadmapProgress",
    "AIConversation", "AIMessage", "Notification", "AuditLog",
]
