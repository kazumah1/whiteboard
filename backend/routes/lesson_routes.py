from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from services.service_registry import lesson_service

router = APIRouter(tags=["lesson"])

class StepExecutionRequest(BaseModel):
    step_index: int

# Helper to build response for current step
def build_step_response(step):
    if not step:
        return {"step": None, "has_next": False, "has_prev": False}
    return {
        "step": step.dict(),
        "has_next": bool(step.next),
        "has_prev": bool(step.prev)
    }

@router.get("/{lesson_id}/current_step")
async def get_current_step(lesson_id: str):
    lesson = lesson_service.load_lesson(lesson_id, debug=True)
    step = lesson_service.get_current_step()
    return build_step_response(step)

@router.post("/{lesson_id}/next_step")
async def next_step(lesson_id: str):
    step = lesson_service.next_step()
    return build_step_response(step)

@router.post("/{lesson_id}/prev_step")
async def prev_step(lesson_id: str):
    step = lesson_service.prev_step()
    return build_step_response(step)

# Keep the lesson loader for initial lesson info if needed
@router.get("/{lesson_id}")
async def get_lesson(lesson_id: str):
    lesson = lesson_service.load_lesson(lesson_id, debug=True)
    return lesson.dict()

@router.get("/{lesson_id}/test")
async def test_route(lesson_id: str):
    """Test route to see if basic routing works."""
    return {"message": f"Test route works for lesson {lesson_id}"}

@router.post("/{lesson_id}/next_node")
async def next_node(lesson_id: str):
    node = lesson_service.next_node()
    if node:
        return node.dict()
    return JSONResponse({"error": "No next node"}, status_code=404)

@router.post("/{lesson_id}/prev_node")
async def prev_node(lesson_id: str):
    node = lesson_service.prev_node()
    if node:
        return node.dict()
    return JSONResponse({"error": "No previous node"}, status_code=404)

@router.post("/{lesson_id}/execute_step")
async def execute_step(lesson_id: str, request: dict = Body(...)):
    """Execute a specific step and return the whiteboard elements."""
    try:
        step_index = request.get("step_index", 0)
        print(f"Route: Executing step {step_index} for lesson {lesson_id}")
        elements = await lesson_service.execute_step(lesson_id, step_index)
        print(f"Route: Got {len(elements)} elements")
        return {"elements": [el.dict() for el in elements]}
    except Exception as e:
        print(f"Route error: {e}")
        import traceback
        traceback.print_exc()
        raise