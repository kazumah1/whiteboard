from fastapi import FastAPI
from routes import lesson_routes, narration_routes, step_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AI Whiteboard Tutor",
    description="Your personal Sal Khan",
    version="0.1.0",
)

app.include_router(lesson_routes.router, prefix="/lesson", tags=["lesson"])
app.include_router(narration_routes.router, prefix="/lesson", tags=["narration"])
app.include_router(step_routes.router, prefix="/step", tags=["steps"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3005"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)