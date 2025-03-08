from fastapi import APIRouter
import pandas as pd

students_df = pd.read_csv("data/large_student_dataset.csv")

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/students")
def get_students():
    return students_df.to_dict(orient="records")
