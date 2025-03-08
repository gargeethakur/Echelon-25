import pandas as pd

courses_df = pd.read_csv("data/udemy_courses_no_title.csv")

def recommend_courses(interest: str):
    recommended = courses_df[courses_df["subject"].str.contains(interest, case=False, na=False)]
    return recommended[["course_id", "price", "num_subscribers"]].to_dict(orient="records")
