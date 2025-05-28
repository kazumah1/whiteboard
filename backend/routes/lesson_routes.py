from fastapi import APIRouter, Depends
from services.lesson_service import LessonService

router = APIRouter()

@router.get("/{lesson_id}")
async def get_lesson(lesson_id: str, lesson_service: LessonService = Depends()):
    lesson_service.load_lesson(lesson_id)
    return {"lesson": lesson_service.plan}

@router.get("/{lesson_id}/state")
async def get_lesson_state(lesson_id: str, lesson_service: LessonService = Depends()):
    return {
        "node": lesson_service.get_current_node(),
        "step": lesson_service.get_current_step(),
        "commands": lesson_service.get_current_command_group()
    }