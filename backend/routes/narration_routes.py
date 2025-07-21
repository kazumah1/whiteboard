from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from services.service_registry import narration_service, lesson_service

router = APIRouter(prefix="/narration", tags=["narration"])

@router.post("/{lesson_id}/current")
async def generate_narration(lesson_id: str):
    step = lesson_service.get_current_step()
    state = lesson_service.traversal_service.get_current_state()
    narration = await narration_service.generate_narration(step, state)
    return {"narration": narration}

@router.post("/{lesson_id}/clarify")
async def clarify(lesson_id: str, question: str = Body(..., embed=True)):
    clarification = await narration_service.handle_clarification(
        question=question,
        narration_history=[],  # TODO: Fill with real history if available
        context=lesson_service.traversal_service.get_current_state(),
        concept=lesson_service.get_current_node()
    )
    return {"clarification": clarification}