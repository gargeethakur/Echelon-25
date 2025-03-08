import os
import pandas as pd
from fastapi import APIRouter, HTTPException, Query

router = APIRouter()

# Define absolute file path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))  # Moves up to 'backend' level
file_path = os.path.join(BASE_DIR, "data", "udemy_courses_no_title.csv")

try:
    courses_df = pd.read_csv(file_path)
except Exception as e:
    raise HTTPException(status_code=500, detail=f"Error loading courses dataset: {str(e)}")

@router.get("/recommend")
def recommend_courses(interest: str = Query(..., description="User's interest")):
    try:
        print(f"🔍 Searching for courses related to: {interest}")
        print(f"📊 Total courses available: {len(courses_df)}")

        filtered_courses = courses_df[courses_df["subject"].str.contains(interest, case=False, na=False)]

        if filtered_courses.empty:
            print("⚠️ No matching courses found!")
            raise HTTPException(status_code=404, detail="No courses found for this interest.")

        result = filtered_courses[["course_id", "price", "num_subscribers"]].head(2).to_dict(orient="records")
        print(f"✅ Returning {len(result)} courses: {result}")

        return result

    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")
