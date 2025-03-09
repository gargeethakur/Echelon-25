from fastapi import APIRouter
from app.models.course_suggestor import recommend_courses

router = APIRouter(prefix="/courses", tags=["Courses"])

@router.get("/recommend")
def get_courses(interest: str):
    return recommend_courses(interest)
