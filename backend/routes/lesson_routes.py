from fastapi import APIRouter
from services.service_registry import lesson_service
from services.service_registry import traversal_service
from models.traversal_state import TraversalState
from global_library_items import global_library_items

router = APIRouter(tags=["lesson"])

def get_lesson_library_items(lesson_id):
    # Placeholder for lesson-specific library items (could fetch from DB or lesson data)
    return []

@router.get("/undo")
async def undo():
    undo = traversal_service.undo()
    if undo:
        state = traversal_service.get_current_state()
        # TODO: not sure if this is the best method of traversal
        lesson_service.current_node_id = state.current_node_id
        lesson_service.current_step_id = state.current_step_id
        if not state:
            print('no state')
        return state
    return None

# getting entire lesson plan - not really used except maybe for higher level planning (might deprecate)
@router.get("/{lesson_id}")
async def get_lesson(lesson_id: str):
    lesson = lesson_service.load_lesson(lesson_id)
    if not traversal_service.get_current_state():
        traversal_service.set_current_state(TraversalState(
            current_node_id=lesson_service.current_node_id,
            current_step_id=lesson_service.current_step_id,
            # TODO: narration_event_id
        ))
    return lesson.model_dump()

@router.get("/{lesson_id}/current_node")
async def get_current_node(lesson_id: str):
    # load lesson if doesn't exist and for congruent lessons in database
    lesson = lesson_service.load_lesson(lesson_id)
    node = lesson_service.get_current_node()
    return node.model_dump()

@router.get("/{lesson_id}/current_node/elements")
async def get_current_node_elements(lesson_id: str):
    lesson = lesson_service.load_lesson(lesson_id)
    node = lesson_service.get_current_node()
    elements = lesson_service.get_elements_for_node(node.id)
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

@router.get("/{lesson_id}/next_node")
async def next_node(lesson_id: str):
    lesson = lesson_service.load_lesson(lesson_id)
    node = lesson_service.next_node()
    if node:
        traversal_service.set_current_state(TraversalState(
            current_step_id=lesson_service.current_step_id,
            current_node_id=lesson_service.current_node_id,
            # TODO: narration_event_id
        ))
        return node.model_dump()
    return None