from fastapi import APIRouter

router = APIRouter(prefix="/skills", tags=["Skill Prediction"])

@router.get("/predict")
def predict_skills():
    return {"message": "Skill prediction logic coming soon"}
