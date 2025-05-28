from fastapi import FastAPI
from routes import lesson_routes, narration_routes

app = FastAPI(
    title="AI Whiteboard Tutor",
    description="Your personal Sal Khan",
    version="0.1.0",
)

app.include_router(lesson_routes.router, prefix="/lesson", tags=["lesson"])
app.include_router(narration_routes.router, prefix="/lesson", tags=["narration"])