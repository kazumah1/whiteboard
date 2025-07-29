from fastapi import APIRouter
from services.service_registry import lesson_service, traversal_service, step_service
from models.traversal_state import TraversalState
from global_library_items import global_library_items
from routes.lesson_routes import get_lesson_library_items

router = APIRouter(tags=["steps"])

@router.get("/{lesson_id}/current_step")
async def get_current_node(lesson_id: str):
    lesson = lesson_service.load_lesson(lesson_id)
    step = lesson_service.get_current_step()
    return step.model_dump()

@router.get("/{lesson_id}/current_step/elements")
async def get_current_step_elements(lesson_id: str):
    # load lesson if doesn't exist and for congruent lessons in database
    lesson = lesson_service.load_lesson(lesson_id)
    node = lesson_service.get_current_step()
    elements = lesson_service.get_elements_for_step(node.id)
    # Example appState and scrollToContent (customize as needed)
    appState = {
        "viewBackgroundColor": "#1e1e1e",
        #element specifics are set in the ExcalidrawElement definitions
    }
    scrollToContent = True
    # Combine global and lesson-specific library items
    libraryItems = global_library_items + get_lesson_library_items(lesson_id)
    return {
        "elements": [el.model_dump() for el in elements],
        "appState": appState,
        "scrollToContent": scrollToContent,
        "libraryItems": libraryItems,
    }

# traverses next step and returns all elements (TODO not sure if returning elements is best)
@router.get("/{lesson_id}/next_step")
async def next_step(lesson_id: str):
    lesson = lesson_service.load_lesson(lesson_id)
    step = lesson_service.next_step()
    if step:
        current_state = TraversalState(
            current_step_id=lesson_service.current_step_id,
            current_node_id=lesson_service.current_node_id,
            # TODO: narration_event_id
        )
        traversal_service.set_current_state(current_state)
        elements = step_service.execute_step(lesson_service.plan, step.id, current_state)
        return {
            "main": step.model_dump(),
            "elements": [el.model_dump() for el in elements]
        }
    return None

# TODO: not sure how to do this part
@router.get("/{lesson_id}/prev_step")
async def prev_step(lesson_id: str):
    lesson = lesson_service.load_lesson(lesson_id)
    step = lesson_service.prev_step()
    if step:
        traversal_service.undo()
        return step.model_dump()
    return None
