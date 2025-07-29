from fastapi import APIRouter
from services.service_registry import lesson_service
from services.service_registry import traversal_service
from models.traversal_state import TraversalState

router = APIRouter(tags=["steps"])

@router.get("/{lesson_id}/next_node")
async def next_node(lesson_id: str):
    lesson = lesson_service.load_lesson(lesson_id)
    node = lesson_service.get_next_node()
    if node:
        traversal_service.set_current_state(TraversalState(
            current_step_id=lesson_service.current_step_id,
            current_node_id=lesson_service.current_node_id,
            # TODO: narration_event_id
        ))
        return node.model_dump()
    return {"error": "No next node"}