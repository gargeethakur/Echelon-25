from fastapi import FastAPI
from app.routes import auth, mentor, skills, courses, users

app = FastAPI(title="EchoMentor Backend")

# Include all routes
app.include_router(auth.router)
app.include_router(mentor.router)
app.include_router(skills.router)
app.include_router(courses.router)
app.include_router(users.router)

@app.get("/")
def home():
    return {"message": "Welcome to EchoMentor API"}

